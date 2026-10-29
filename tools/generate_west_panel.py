#!/usr/bin/env python3
"""Generate Rhomania's West situation panel, its per-prefecture actions and their loc.

The West has four fixed prefectures (italy, africa, spania, gaul). Everything the emperor does
to ONE province has to name it, and a panel button cannot pass a country to an action: a
situation action driven from a button gets the actor and the situation and nothing else (see
the gotchas on GUI-invoked actions). So each per-prefecture action exists once per prefecture
as a thin wrapper around one scripted effect, and each prefecture has its own card reading its
own published variables. Edit the tables and templates here, never the output.

Writes:
  submods/rhomania/in_game/gui/panels/situation/cc_byz_the_west.gui
  submods/rhomania/in_game/common/generic_actions/cc_byz_west_prefecture_actions.txt
  submods/rhomania/main_menu/localization/english/cc_byz_west_pf_l_english.yml

The logic lives in scripted_effects/cc_byz_west_prefecture_effects.txt and the gates in
scripted_triggers/cc_byz_west_prefecture_triggers.txt. Card bodies reuse the existing panel
strings in cc_byz_west_panel_l_english.yml.

    python tools/generate_west_panel.py
    python tools/generate_west_panel.py --check   # exit 1 if any output is stale
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SUB = REPO / 'submods' / 'rhomania'
GUI_OUT = SUB / 'in_game' / 'gui' / 'panels' / 'situation' / 'cc_byz_the_west.gui'
ACTIONS_OUT = SUB / 'in_game' / 'common' / 'generic_actions' / 'cc_byz_west_prefecture_actions.txt'
LOC_OUT = SUB / 'main_menu' / 'localization' / 'english' / 'cc_byz_west_pf_l_english.yml'

GENERATED = '# GENERATED FILE. Do not edit by hand: python tools/generate_west_panel.py\n'
BOM = '﻿'

# key, card title, short name for action labels, opening requirement
PREFECTURES = [
    ('italy', 'Exarchate of Ravenna', 'Ravenna', '8 locations in Italy and 75% of one Italian area'),
    ('africa', 'Exarchate of Carthage', 'Carthage', '6 locations in the Maghreb and 75% of one area there'),
    ('spania', 'Province of Spania', 'Spania', '4 locations in Iberia and 75% of one Iberian area'),
    ('gaul', 'Prefecture of the Gauls', 'the Gauls', '10 locations in France and 75% of one French area'),
]

# Per-prefecture actions.
# key: (button label, action name, description, price, allow lines, cooldown years, ai weight,
#       prefectures it exists for or None for all, extra potential)
ACTIONS = {
    'donative': dict(
        button='Pay', name='Pay the Garrisons of {short}',
        desc='Pay this province\'s garrisons their arrears. A third of the full donative\'s cost, for one province.\n\nThe exarch gains #G 2#! loyalty and imperial grip rises by #G 1#!.',
        price=None, allow=['scope:actor = { gold >= 75 }'], cd=5, ai=12, only=None, potential=None,
    ),
    'honours': dict(
        button='Honour', name='Confer a Court Title on the Exarch of {short}',
        desc='Make the exarch a patrikios, or a magistros if he is one already. It costs the emperor prestige and gives the west no more say.\n\nThe exarch gains #G 2#! loyalty and loses #G 1#! appetite.',
        price=None, allow=['scope:actor = { prestige >= 25 }'], cd=10, ai=10, only=None, potential=None,
    ),
    'confirm_son': dict(
        button='Confirm son', name='Confirm the Son of the Exarch of {short}',
        desc='Confirm the exarch\'s son as his successor. The office becomes his family\'s.\n\nThe exarch gains #G 3#! loyalty. Western autonomy rises by #R 8#!, and the empire leans toward the Dynatoi. The first confirmation is a precedent every other exarch will cite.',
        price='cc_byz_west_minor_price',
        allow=[
            'custom_tooltip = {',
            '\ttext = cc_byz_west_pf_needs_loyal_tt',
            '\tscope:actor = {',
            '\t\tany_subject = {',
            '\t\t\tcc_byz_exarch_in_{pf}_trigger = yes',
            '\t\t\tcc_byz_exarch_loyalty_at_least_trigger = {{ VALUE = 1 }}',
            '\t\t}',
            '\t}',
            '}',
        ],
        cd=None, ai=4, only=None,
        potential='scope:actor = { any_subject = { cc_byz_exarch_in_{pf}_trigger = yes  NOT = { has_variable = cc_byz_exarch_hereditary } } }',
    ),
    'strategos': dict(
        button='Strategos', name='Send a Strategos to {short}',
        desc='Send a general and his men to this province. The exarch gains army tradition and manpower.\n\nWestern autonomy rises by #R 5#!: a general in the west has troops who know him.',
        price='cc_byz_west_minor_price', allow=['scope:actor = { army_tradition >= 30 }'], cd=20, ai=6, only=None, potential=None,
    ),
    'recall': dict(
        button='Recall', name='Summon the Exarch of {short}',
        desc='Order this exarch to the capital. Whether he comes depends on his loyalty, and on whether his office has become his family\'s.',
        price=None, allow=['scope:actor = { stability >= 0 }'], cd=15, ai=4, only=None, potential=None,
    ),
    'charter': dict(
        button='Charter', name='Charter a Commune in {short}',
        desc='Grant a city its charter. Trade and the burghers gain, and the exarch gains #G 1#! loyalty.\n\nWestern autonomy rises by #R 6#!. The first charter is the precedent every other commune cites.',
        price='cc_byz_west_minor_price', allow=[], cd=20, ai=6, only=('italy', 'gaul'), potential=None,
    ),
}
ORDER = ['donative', 'honours', 'confirm_son', 'strategos', 'recall', 'charter']

# Empire-wide actions on the Governing card: action key, button label, cooldown modifier.
EMPIRE_ACTIONS = [
    ('cc_byz_west_order_census', 'Order a census', 'cc_byz_west_census_taken'),
    ('cc_byz_west_donative', 'Pay the donative', 'cc_byz_west_donative_paid'),
    ('cc_byz_west_demand_tribute', 'Demand tribute', 'cc_byz_west_tribute_taken'),
]
CONSISTORY_ACTIONS = [
    ('cc_byz_io_convene_consistory', 'Convene'),
    ('cc_byz_io_elevate_senior_exarch', 'Elevate a senior exarch'),
    ('cc_byz_io_dissolve_prefecture', 'Dissolve a prefecture'),
]

SIT = "SituationView.GetActiveSituation.GetSituation.MakeScope"
GRIP = f"{SIT}.GetVariable('cc_byz_imperial_grip').GetValue"
AUT = f"{SIT}.GetVariable('cc_byz_western_autonomy').GetValue"


def act_key(a: str, pf: str) -> str:
    return f'cc_byz_west_pf_{a}_{pf}'


def actions_for(pf: str) -> list[str]:
    return [a for a in ORDER if ACTIONS[a]['only'] is None or pf in ACTIONS[a]['only']]


def ind(lines: list[str], n: int) -> list[str]:
    return [('\t' * n + l) if l else l for l in lines]


###############################################################################
# ACTIONS
###############################################################################

def emit_actions() -> str:
    out = [BOM + GENERATED.rstrip('\n'),
           '#',
           '# Per-prefecture West actions. One copy per prefecture because a panel button cannot pass',
           '# a country: each wraps cc_byz_west_pf_save_effect plus one shared body in',
           '# scripted_effects/cc_byz_west_prefecture_effects.txt. type = situation with the usual',
           '# situation select_trigger, which is what binds scope:recipient to the parameter the panel',
           '# button passes. Cooldowns are timed variables on the empire, checked in allow so the',
           '# button tooltip says why it is disabled.',
           '']
    for pf, _title, _short, _req in PREFECTURES:
        for a in actions_for(pf):
            d = ACTIONS[a]
            freq = 12 if d['cd'] is None else max(12, min(60, d['cd'] * 6))
            b = [f'{act_key(a, pf)} = {{',
                 '\ttype = situation',
                 '\tai_tick = monthly',
                 f'\tai_tick_frequency = {freq}',
                 '\tautomation_tick = monthly',
                 f'\tautomation_tick_frequency = {freq}']
            if d['price']:
                b.append(f"\tprice = price:{d['price']}")
            b += ['',
                  '\tselect_trigger = {',
                  '\t\tlooking_for_a = situation',
                  '\t\ttarget_flag = recipient',
                  '\t\tname = "choose_situation"',
                  '\t\tcolumn = { data = name }',
                  '\t\tvisible = {',
                  '\t\t\tsituation:cc_byz_the_west = this',
                  '\t\t\tsituation_is_active = yes',
                  '\t\t}',
                  '\t}',
                  '',
                  '\tpotential = {',
                  f'\t\tcc_byz_west_pf_action_potential_trigger = {{ PF = {pf} }}']
            if d['potential']:
                b.append('\t\t' + d['potential'].replace('{pf}', pf))
            b += ['\t}', '', '\tallow = {']
            if d['cd']:
                b += ['\t\tcustom_tooltip = {',
                      '\t\t\ttext = cc_byz_west_pf_cooldown_tt',
                      f'\t\t\tscope:actor = {{ NOT = {{ has_variable = cc_byz_west_{a}_cd_{pf} }} }}',
                      '\t\t}']
            for l in d['allow']:
                b.append('\t\t' + l.replace('{pf}', pf).replace('{{', '{').replace('}}', '}'))
            if not d['cd'] and not d['allow']:
                b.append('\t\talways = yes')
            b += ['\t}', '', '\teffect = {', '\t\tscope:actor = {']
            if d['cd']:
                b.append(f"\t\t\tset_variable = {{ name = cc_byz_west_{a}_cd_{pf}  value = yes  years = {d['cd']} }}")
            b += [f'\t\t\tcc_byz_west_pf_save_effect = {{ PF = {pf} }}',
                  f'\t\t\tcc_byz_west_pf_{a}_effect = yes',
                  '\t\t\thidden_effect = { cc_byz_west_publish_effect = yes }',
                  '\t\t}',
                  '\t}',
                  '',
                  f"\tai_will_do = {{ add = {d['ai']} }}",
                  '}',
                  '']
            out += b
    return '\n'.join(out)


###############################################################################
# LOC
###############################################################################

def esc(s: str) -> str:
    # Loc values are single lines: a real newline ends the value and the reader rejects the
    # rest ("Missing colon separator"). Write the two-character escape instead.
    return s.replace('"', '\\"').replace(chr(10), '\\n')


def emit_loc() -> str:
    L = [BOM + 'l_english:', ' ' + GENERATED.strip().replace('# ', '# '), '']
    L.append(' # ---- Per-prefecture actions ----')
    for pf, title, short, _req in PREFECTURES:
        for a in actions_for(pf):
            d = ACTIONS[a]
            L.append(f' {act_key(a, pf)}: "{esc(d["name"].format(short=short))}"')
            L.append(f' {act_key(a, pf)}_desc: "{esc(d["desc"])}"')
    L += ['',
          ' cc_byz_west_pf_cooldown_tt: "This province was dealt with this way recently"',
          ' cc_byz_west_pf_needs_loyal_tt: "The exarch\'s loyalty is at least 1"',
          ' cc_byz_west_succ_resist_tt: "The province may prefer the son. If it does, the new exarch loses #R 2#! loyalty and western autonomy rises by #R 5#!. Starting at 30%, this is #G less likely#! with an able candidate (160+ ability points, more so at 200+) or imperial grip of 60+, or if the dead exarch was loyal (2+). It is #R more likely#! with a weak candidate (below 120), western autonomy of 60+, a hereditary office, or a disloyal exarch (-2 or lower). A candidate of 180+ who is accepted starts with #G 1#! loyalty."',
          ' cc_byz_west_succ_consistory_tt: "The consistory picks either a man the capital can live with (#G +1#! loyalty, autonomy #R +2#!) or one of the west\'s own (#R -1#! loyalty, autonomy #R +5#!). Even odds, tilted toward the capital\'s man by imperial grip of 60+ or a loyal predecessor (2+), and toward the west\'s by western autonomy of 60+."',
          '',
          ' # ---- Panel ----',
          ' CC_BYZ_WEST_PANEL_HEADER: "The Prefectures of the West"',
          ' CC_BYZ_WEST_PANEL_HEADER_TT: "Grip and autonomy are two separate counters. Each prefecture card shows its exarch and the actions that act on that province alone. The empire-wide actions are on the Governing card, and the consistory has its own tab."',
          ' CC_BYZ_WEST_THIS_YEAR: "this year"',
          ' CC_BYZ_WEST_ENDINGS: "Where this ends"',
          ' CC_BYZ_WEST_ENDINGS_TT: "No corner counts until the West has run fifty years with at least two prefectures seated. After that, holding a corner for five years settles the West there, with a warning when the count starts and a final choice when it ends. If nothing is settled by the Age of Revolutions, the nearest corner is taken. The highlighted cell is the half each counter is in now."',
          ' CC_BYZ_WEST_GATE: "Endings locked: [FixedPointToInt(SituationView.GetActiveSituation.GetSituation.MakeScope.GetVariable(\'cc_byz_west_years\').GetValue)] of 50 years, and two prefectures needed"',
          ' CC_BYZ_WEST_SETTLING_1: "Settling toward reabsorption: year [FixedPointToInt(SituationView.GetActiveSituation.GetSituation.MakeScope.GetVariable(\'cc_byz_west_corner_years\').GetValue)] of 5"',
          ' CC_BYZ_WEST_SETTLING_2: "Settling toward the diarchy: year [FixedPointToInt(SituationView.GetActiveSituation.GetSituation.MakeScope.GetVariable(\'cc_byz_west_corner_years\').GetValue)] of 5"',
          ' CC_BYZ_WEST_SETTLING_3: "Settling toward the acclamation: year [FixedPointToInt(SituationView.GetActiveSituation.GetSituation.MakeScope.GetVariable(\'cc_byz_west_corner_years\').GetValue)] of 5"',
          ' CC_BYZ_WEST_SETTLING_4: "Settling toward neglect: year [FixedPointToInt(SituationView.GetActiveSituation.GetSituation.MakeScope.GetVariable(\'cc_byz_west_corner_years\').GetValue)] of 5"',
          ' CC_BYZ_WEST_END_REABSORB: "Reabsorbed"',
          ' CC_BYZ_WEST_END_REABSORB_REQ: "Grip 65+, autonomy below 35"',
          ' CC_BYZ_WEST_END_DIARCHY: "The diarchy"',
          ' CC_BYZ_WEST_END_DIARCHY_REQ: "Grip 60+, autonomy 60+"',
          ' CC_BYZ_WEST_END_NEGLECT: "Neglected"',
          ' CC_BYZ_WEST_END_NEGLECT_REQ: "Grip below 25, autonomy below 30"',
          ' CC_BYZ_WEST_END_ACCLAIM: "The acclamation"',
          ' CC_BYZ_WEST_END_ACCLAIM_REQ: "Autonomy 80+, grip below 40"',
          ' CC_BYZ_WEST_AXIS_AUT: "Autonomy low / high"',
          ' CC_BYZ_WEST_DEADLINE: "Settled by the Age of Revolutions at the latest"',
          ' CC_BYZ_WEST_SEC_PREFECTURES: "Prefectures"',
          ' CC_BYZ_WEST_SEC_GOVERNING: "Governing the West"',
          ' CC_BYZ_WEST_GOVERNING_DESC: "These act on every prefecture at once."',
          ' CC_BYZ_WEST_ON_COOLDOWN: "recently done"',
          ' CC_BYZ_WEST_PF_EMPTY: "No exarch seated"',
          ' CC_BYZ_WEST_PF_OPEN: "An exarch can be appointed now"',
          ' CC_BYZ_WEST_KIND_1: "Caretaker exarch"',
          ' CC_BYZ_WEST_KIND_2: "Effective exarch"',
          ' CC_BYZ_WEST_KIND_3: "Strategos exarch"',
          ' CC_BYZ_WEST_TAG_HEREDITARY: "Hereditary"',
          ' CC_BYZ_WEST_TAG_HEREDITARY_TT: "His son\'s succession was confirmed. The office passes in this family."',
          ' CC_BYZ_WEST_TAG_DISAFFECTED: "Disaffected"',
          ' CC_BYZ_WEST_TAG_DISAFFECTED_TT: "He is raising men, and not for the capital\'s use."',
          ' CC_BYZ_WEST_TAG_CONTENTED: "Contented"',
          ' CC_BYZ_WEST_TAG_CONTENTED_TT: "Paid, confirmed, and doing well out of the arrangement."',
          ' CC_BYZ_WEST_TAG_SENIOR: "Senior Exarch"',
          ' CC_BYZ_WEST_COL_APPETITE: "Appetite"',
          ' CC_BYZ_WEST_COL_APPETITE_TT: "How much more of his province he thinks should be his, 0 to 5. Rises when his requests are refused and when the cession review is withheld; falls when they are granted or he is honoured."',
          ' CC_BYZ_WEST_REVIEW_DONE: "Cession review: held in the last five years"',
          ' CC_BYZ_WEST_REVIEW_DUE: "Cession review: due if we hold ground in his region"',
          ' CC_BYZ_WEST_TAB_CONSISTORY: "Consistory"',
          ' CC_BYZ_WEST_CONS_DORMANT: "Dormant: the prefects govern, but do not meet"',
          ' CC_BYZ_WEST_CONS_SITTING: "In session"',
          ' CC_BYZ_WEST_VOTES_EMPEROR: "The emperor: 3 votes"',
          ' CC_BYZ_WEST_VOTES_WEST: "The prefects together"',
          ' CC_BYZ_WEST_VOTES_SAFE: "The emperor cannot be outvoted"',
          ' CC_BYZ_WEST_VOTES_TIE: "A tie: motions against the emperor fail, and so do his"',
          ' CC_BYZ_WEST_VOTES_LOST: "The prefects can outvote the emperor"',
          ' CC_BYZ_WEST_CONS_QUESTIONS: "The consistory votes on four questions: who the western armies obey, where the western revenue goes, which rite the western churches use, and how a dead prefect is replaced."',
          ' CC_BYZ_WEST_COL_VOTES: "Votes"',
          '']
    for pf, title, short, req in PREFECTURES:
        L.append(f' CC_BYZ_WEST_PF_{pf.upper()}: "{esc(title)}"')
        L.append(f' CC_BYZ_WEST_PF_{pf.upper()}_REQ: "Needs {esc(req)}"')
    for a in ORDER:
        L.append(f' CC_BYZ_WEST_BTN_{a.upper()}: "{esc(ACTIONS[a]["button"])}"')
    for key, label, _m in EMPIRE_ACTIONS:
        L.append(f' CC_BYZ_WEST_BTN_{key.upper()}: "{esc(label)}"')
    for key, label in CONSISTORY_ACTIONS:
        L.append(f' CC_BYZ_WEST_BTN_{key.upper()}: "{esc(label)}"')
    return '\n'.join(L) + '\n'


###############################################################################
# GUI
###############################################################################

def ge(var: str, n: int) -> str:
    """var >= n"""
    return f"Not(GreaterThan_CFixedPoint('(CFixedPoint){n}', {var}))"


def lt(var: str, n: int) -> str:
    return f"GreaterThan_CFixedPoint('(CFixedPoint){n}', {var})"


def card_title(key: str, info: str | None = None) -> list[str]:
    l = ['hbox = {',
         '\tlayoutpolicy_horizontal = expanding',
         '\tspacing = 6',
         f'\ttext_single = {{ fontsize = 14  align = left|nobaseline  text = "{key}" }}',
         '\texpand = {}']
    if info:
        l += ['\ticon = {',
              '\t\tsize = { 20 20 }',
              '\t\ttexture = "gfx/interface/icons/flat_icons/tabicons/info_flat_icon.dds"',
              '\t\ttexture_density = 2',
              '\t\ttooltipwidget = {',
              '\t\t\tContextualTooltipType = {',
              f'\t\t\t\tblockoverride "title_text" {{ text = "{key}" }}',
              '\t\t\t\tblockoverride "tooltip_content" {',
              f'\t\t\t\t\ttext_multi = {{ autoresize = yes  multiline = yes  max_width = 340  text = "{info}" }}',
              '\t\t\t\t}',
              '\t\t\t}',
              '\t\t}',
              '\t}']
    l += ['}', 'widget = { size = { 32 2 }  background = { using = color_white_texture  alpha = 0.35 } }']
    return l


def button(action: str, label: str, width: int, actor: str = '[SituationView.GetPlayer]') -> list[str]:
    return ['card_header_button_01 = {',
            f'\tsize = {{ {width} 22 }}',
            '\tscripted_action_tooltip = {',
            '\t\tclick_type = left',
            '\t\tclick_mode = single',
            f'\t\taction_name = "{action}"',
            f'\t\tactor = "{actor}"',
            '\t\tparameter = {',
            '\t\t\tparameter_name = "recipient"',
            '\t\t\tparameter_value = "[SituationView.GetActiveSituation.GetSituation]"',
            '\t\t}',
            '\t}',
            '\tenabled = "[PdxGuiWidget.IsUberButtonEnabled]"',
            '\ttooltipwidget = { using = action_tooltip_pop_out }',
            f'\ttext_single = {{ parentanchor = center  align = center  fontsize = 10  text = "{label}" }}',
            '}']


def bar(label: str, value: str, lo: int, hi: int, tex: str, tooltip: str | None = None, width: int = -1) -> list[str]:
    l = ['progressbar = {',
         '\tlayoutpolicy_horizontal = expanding' if width < 0 else f'\tsize = {{ {width} 10 }}']
    if width < 0:
        l.append('\tsize = { -1 10 }')
    l += ['\tnoprogresstexture = "gfx/interface/progressbars/progress_bar_grey_alt.dds"',
          f'\tprogresstexture = "gfx/interface/progressbars/{tex}"',
          '\ttexture_density = 2',
          '\tspriteType = Corneredstretched',
          '\tspriteborder = { 12 0 }',
          f'\tmin = {lo}',
          f'\tmax = {hi}',
          f'\tvalue = "[FixedPointToFloat({value})]"']
    if tooltip:
        l.append(f'\ttooltip = "{tooltip}"')
    l.append('}')
    return l


def signed(value: str, fontsize: int = 13) -> list[str]:
    """Three mutually exclusive widgets: there is no conditional-colour form."""
    return [
        f'text_single = {{ fontsize = {fontsize}  default_format = "#color_green"  visible = "[GreaterThan_CFixedPoint({value}, \'(CFixedPoint)0\')]"  raw_text = "+[FixedPointToInt({value})]" }}',
        f'text_single = {{ fontsize = {fontsize}  default_format = "#color_red"  visible = "[GreaterThan_CFixedPoint(\'(CFixedPoint)0\', {value})]"  raw_text = "[FixedPointToInt({value})]" }}',
        f'text_single = {{ fontsize = {fontsize}  default_format = "#weak"  visible = "[EqualTo_CFixedPoint({value}, \'(CFixedPoint)0\')]"  raw_text = "0" }}',
    ]


def counter_block(label: str, var: str, drift: str, tex: str, tooltip: str) -> list[str]:
    v = f"{SIT}.GetVariable('{var}').GetValue"
    d = f"{SIT}.GetVariable('{drift}').GetValue"
    l = ['vbox = {',
         '\tlayoutpolicy_horizontal = expanding',
         '\tspacing = 2',
         '\thbox = {',
         '\t\tlayoutpolicy_horizontal = expanding',
         '\t\tspacing = 4',
         f'\t\ttext_single = {{ fontsize = 13  align = left|nobaseline  text = "{label}" }}',
         '\t\texpand = {}',
         '\t\thbox = {',
         f"\t\t\tvisible = \"[{SIT}.GetVariable('{drift}').IsSet]\"",
         '\t\t\tspacing = 3']
    l += ind(signed(d, 11), 3)
    l += ['\t\t\ttext_single = { fontsize = 10  default_format = "#weak"  text = "CC_BYZ_WEST_THIS_YEAR" }',
          '\t\t}',
          f'\t\ttext_single = {{ fontsize = 14  raw_text = "[FixedPointToInt({v})]/100" }}',
          '\t}']
    l += ind(bar(label, v, 0, 100, tex, tooltip), 1)
    l.append('}')
    return l


def ending_cell(name: str, req: str, cond: str) -> list[str]:
    return ['widget = {',
            '\tsize = { 236 38 }',
            '\tbackground = { using = color_whiteish_texture  alpha = 0.06 }',
            '\twidget = {',
            '\t\tsize = { 236 38 }',
            f'\t\tvisible = "[{cond}]"',
            '\t\tbackground = { using = color_white_texture  alpha = 0.16 }',
            '\t}',
            '\tvbox = {',
            '\t\tparentanchor = center',
            f'\t\ttext_single = {{ fontsize = 12  align = center|nobaseline  text = "{name}" }}',
            f'\t\ttext_single = {{ fontsize = 10  default_format = "#weak"  align = center|nobaseline  text = "{req}" }}',
            '\t}',
            '}']


def balance_card() -> list[str]:
    g_hi, g_lo = ge(GRIP, 50), lt(GRIP, 50)
    a_hi, a_lo = ge(AUT, 50), lt(AUT, 50)
    l = ['vbox = {',
         '\tlayoutpolicy_horizontal = expanding',
         '\tbackground = { using = color_whiteish_texture  alpha = 0.10 }',
         '\tmargin = { 10 8 }',
         '\tspacing = 6']
    l += ind(card_title('CC_BYZ_WEST_CARD_BALANCE', 'CC_BYZ_WEST_CARD_BALANCE_INFO'), 1)
    l += ['\ttext_multi = { layoutpolicy_horizontal = expanding  autoresize = yes  multiline = yes  max_width = 480  fontsize = 11  default_format = "#weak"  text = "CC_BYZ_WEST_CARD_BALANCE_DESC" }']
    l += ind(counter_block('CC_BYZ_WEST_BAR_GRIP', 'cc_byz_imperial_grip', 'cc_byz_west_grip_drift', 'progress_bar_yellow.dds', 'CC_BYZ_WEST_BAR_GRIP_TT'), 1)
    l += ind(counter_block('CC_BYZ_WEST_BAR_AUTONOMY', 'cc_byz_western_autonomy', 'cc_byz_west_autonomy_drift', 'progress_bar_orange.dds', 'CC_BYZ_WEST_BAR_AUTONOMY_TT'), 1)
    # tension lines, as before
    l += [f'\ttext_single = {{ fontsize = 12  default_format = "#color_red"  text = "CC_BYZ_WEST_TENSION_BOTH_HIGH"  tooltip = "CC_BYZ_WEST_TENSION_BOTH_HIGH_TT"  visible = "[And(GreaterThan_CFixedPoint({GRIP}, \'(CFixedPoint)59\'), GreaterThan_CFixedPoint({AUT}, \'(CFixedPoint)59\'))]" }}',
          f'\ttext_single = {{ fontsize = 12  default_format = "#weak"  text = "CC_BYZ_WEST_TENSION_DRIFTING"  tooltip = "CC_BYZ_WEST_TENSION_DRIFTING_TT"  visible = "[And(GreaterThan_CFixedPoint(\'(CFixedPoint)30\', {GRIP}), GreaterThan_CFixedPoint({AUT}, \'(CFixedPoint)59\'))]" }}']
    # endings map
    l += ['\thbox = {',
          '\t\tlayoutpolicy_horizontal = expanding',
          '\t\tmargin_top = 4',
          '\t\ttext_single = { fontsize = 12  default_format = "#weak"  text = "CC_BYZ_WEST_ENDINGS"  tooltip = "CC_BYZ_WEST_ENDINGS_TT" }',
          '\t\texpand = {}',
          '\t\ttext_single = { fontsize = 10  default_format = "#weak"  text = "CC_BYZ_WEST_AXIS_AUT" }',
          '\t}',
          '\thbox = {',
          '\t\tspacing = 4']
    l += ind(ending_cell('CC_BYZ_WEST_END_REABSORB', 'CC_BYZ_WEST_END_REABSORB_REQ', f'And({g_hi}, {a_lo})'), 2)
    l += ind(ending_cell('CC_BYZ_WEST_END_DIARCHY', 'CC_BYZ_WEST_END_DIARCHY_REQ', f'And({g_hi}, {a_hi})'), 2)
    l += ['\t}', '\thbox = {', '\t\tspacing = 4']
    l += ind(ending_cell('CC_BYZ_WEST_END_NEGLECT', 'CC_BYZ_WEST_END_NEGLECT_REQ', f'And({g_lo}, {a_lo})'), 2)
    l += ind(ending_cell('CC_BYZ_WEST_END_ACCLAIM', 'CC_BYZ_WEST_END_ACCLAIM_REQ', f'And({g_lo}, {a_hi})'), 2)
    l += ['\t}',
          '\ttext_single = { fontsize = 10  default_format = "#weak"  text = "CC_BYZ_WEST_DEADLINE"  tooltip = "CC_BYZ_WEST_ENDINGS_TT" }',
          # The gate, then the countdown once a corner is being held.
          f"\ttext_single = {{ fontsize = 11  default_format = \"#weak\"  text = \"CC_BYZ_WEST_GATE\"  tooltip = \"CC_BYZ_WEST_ENDINGS_TT\"  visible = \"[Not({SIT}.GetVariable('cc_byz_west_gate_open').IsSet)]\" }}",
          ] + [
          f"\ttext_single = {{ fontsize = 12  default_format = \"#color_yellow\"  text = \"CC_BYZ_WEST_SETTLING_{n}\"  tooltip = \"CC_BYZ_WEST_ENDINGS_TT\"  visible = \"[EqualTo_CFixedPoint({SIT}.GetVariable('cc_byz_west_corner').GetValue, '(CFixedPoint){n}')]\" }}"
          for n in (1, 2, 3, 4)] + [
          '}']
    return l


def tag(key: str, tt: str, visible: str, fmt: str) -> str:
    return f'text_single = {{ fontsize = 10  default_format = "{fmt}"  text = "{key}"  tooltip = "{tt}"  visible = "[{visible}]" }}'


def pf_card(pf: str) -> list[str]:
    pv = f"Player.MakeScope.GetVariable('cc_byz_west_pf_{pf}')"
    loy = "Country.MakeScope.GetVariable('cc_byz_exarch_loyalty').GetValue"
    app = "Country.MakeScope.GetVariable('cc_byz_exarch_appetite').GetValue"
    kind = "Country.MakeScope.GetVariable('cc_byz_exarch_kind').GetValue"
    up = pf.upper()
    l = [f'# ---- {pf} ----',
         '# Seated.',
         'widget = {',
         '\tsize = { 246 270 }',
         f'\tvisible = "[{pv}.IsSet]"',
         f'\tdatacontext = "[{pv}.GetCountry]"',
         '\tbackground = { using = color_whiteish_texture  alpha = 0.10 }',
         '\tvbox = {',
         '\t\tlayoutpolicy_horizontal = expanding',
         '\t\tlayoutpolicy_vertical = expanding',
         '\t\tmargin = { 8 6 }',
         '\t\tspacing = 3',
         f'\t\ttext_single = {{ layoutpolicy_horizontal = expanding  fontsize = 10  default_format = "#weak"  align = left|nobaseline  text = "CC_BYZ_WEST_PF_{up}" }}',
         '\t\twidget = { size = { 32 2 }  background = { using = color_white_texture  alpha = 0.35 } }',
         '\t\thbox = {',
         '\t\t\tlayoutpolicy_horizontal = expanding',
         '\t\t\tspacing = 6',
         '\t\t\tcountry_flag_small = {}',
         '\t\t\ttext_single = { fontsize = 14  align = left|nobaseline  max_width = 190  elide = right  text = "[Country.GetName]" }',
         '\t\t\texpand = {}',
         '\t\t}',
         '\t\thbox = {',
         '\t\t\tlayoutpolicy_horizontal = expanding',
         '\t\t\tspacing = 6',
         '\t\t\twidget = {',
         '\t\t\t\tsize = { 38 44 }',
         '\t\t\t\tdatacontext = "[Country.GetGovernment.GetRuler]"',
         '\t\t\t\tportrait_standard_head_framed_button = {',
         '\t\t\t\t\tsize = { 38 44 }',
         '\t\t\t\t\tonclick = "[ShowCharacter(Character.Self)]"',
         '\t\t\t\t}',
         '\t\t\t}',
         '\t\t\tvbox = {',
         '\t\t\t\tlayoutpolicy_horizontal = expanding',
         '\t\t\t\ttext_single = { layoutpolicy_horizontal = expanding  fontsize = 12  align = left|nobaseline  text = "[Country.GetGovernment.GetRuler.GetShortNameWithNoTooltip]" }']
    for k in (1, 2, 3):
        l.append(f"\t\t\t\ttext_single = {{ layoutpolicy_horizontal = expanding  fontsize = 10  default_format = \"#weak\"  align = left|nobaseline  text = \"CC_BYZ_WEST_KIND_{k}\"  visible = \"[EqualTo_CFixedPoint({kind}, '(CFixedPoint){k}')]\" }}")
    l += ['\t\t\t\thbox = {',
          '\t\t\t\t\tspacing = 6',
          '\t\t\t\t\t' + tag('CC_BYZ_WEST_TAG_HEREDITARY', 'CC_BYZ_WEST_TAG_HEREDITARY_TT', "Country.MakeScope.GetVariable('cc_byz_exarch_hereditary').IsSet", '#color_yellow'),
          '\t\t\t\t\t' + tag('CC_BYZ_WEST_TAG_SENIOR', 'CC_BYZ_WEST_TAG_SENIOR', "Country.MakeScope.GetVariable('cc_byz_exarch_senior').IsSet", '#color_yellow'),
          '\t\t\t\t\t' + tag('CC_BYZ_WEST_TAG_DISAFFECTED', 'CC_BYZ_WEST_TAG_DISAFFECTED_TT', "Country.HasModifier('cc_byz_exarch_disaffected')", '#color_red'),
          '\t\t\t\t\t' + tag('CC_BYZ_WEST_TAG_CONTENTED', 'CC_BYZ_WEST_TAG_CONTENTED_TT', "Country.HasModifier('cc_byz_exarch_contented')", '#color_green'),
          '\t\t\t\t}',
          '\t\t\t}',
          '\t\t}',
          # loyalty
          '\t\thbox = {',
          '\t\t\tlayoutpolicy_horizontal = expanding',
          '\t\t\tspacing = 4',
          '\t\t\ttext_single = { fontsize = 11  default_format = "#weak"  text = "CC_BYZ_WEST_COL_LOYALTY"  tooltip = "CC_BYZ_WEST_CARD_PREFECTURES_INFO" }',
          '\t\t\texpand = {}']
    l += ind(signed(loy, 12), 3)
    l += ['\t\t}']
    l += ind(bar('', loy, -5, 5, 'progress_bar_green_alt.dds', 'CC_BYZ_WEST_CARD_PREFECTURES_INFO'), 2)
    # appetite
    l += ['\t\thbox = {',
          '\t\t\tlayoutpolicy_horizontal = expanding',
          '\t\t\tspacing = 4',
          '\t\t\ttext_single = { fontsize = 11  default_format = "#weak"  text = "CC_BYZ_WEST_COL_APPETITE"  tooltip = "CC_BYZ_WEST_COL_APPETITE_TT" }',
          '\t\t\texpand = {}',
          f'\t\t\ttext_single = {{ fontsize = 12  raw_text = "[FixedPointToInt({app})]/5" }}',
          '\t\t}']
    l += ind(bar('', app, 0, 5, 'progress_bar_red_alt.dds', 'CC_BYZ_WEST_COL_APPETITE_TT'), 2)
    l += [f"\t\ttext_single = {{ layoutpolicy_horizontal = expanding  fontsize = 10  default_format = \"#weak\"  align = left|nobaseline  text = \"CC_BYZ_WEST_REVIEW_DONE\"  visible = \"[Country.MakeScope.GetVariable('cc_byz_exarch_cession_cd').IsSet]\" }}",
          f"\t\ttext_single = {{ layoutpolicy_horizontal = expanding  fontsize = 10  default_format = \"#weak\"  align = left|nobaseline  text = \"CC_BYZ_WEST_REVIEW_DUE\"  visible = \"[Not(Country.MakeScope.GetVariable('cc_byz_exarch_cession_cd').IsSet)]\" }}",
          '\t\texpand = {}']
    # buttons, three per row
    acts = actions_for(pf)
    rows = [acts[i:i + 3] for i in range(0, len(acts), 3)]
    for row in rows:
        l += ['\t\thbox = {', '\t\t\tspacing = 4']
        for a in row:
            l += ind(button(act_key(a, pf), f'CC_BYZ_WEST_BTN_{a.upper()}', 74), 3)
        l += ['\t\t}']
    l += ['\t}', '}']
    # empty
    l += ['# Empty.',
          'widget = {',
          '\tsize = { 246 270 }',
          f'\tvisible = "[Not({pv}.IsSet)]"',
          '\tbackground = { using = color_black_texture  alpha = 0.18 }',
          '\tvbox = {',
          '\t\tlayoutpolicy_horizontal = expanding',
          '\t\tmargin = { 8 6 }',
          '\t\tspacing = 3',
          f'\t\ttext_single = {{ layoutpolicy_horizontal = expanding  fontsize = 10  default_format = "#weak"  align = left|nobaseline  text = "CC_BYZ_WEST_PF_{up}" }}',
          '\t\twidget = { size = { 32 2 }  background = { using = color_white_texture  alpha = 0.35 } }',
          '\t\ttext_single = { layoutpolicy_horizontal = expanding  fontsize = 13  default_format = "#weak"  align = left|nobaseline  text = "CC_BYZ_WEST_PF_EMPTY" }',
          f"\t\ttext_single = {{ layoutpolicy_horizontal = expanding  fontsize = 11  default_format = \"#color_green\"  align = left|nobaseline  text = \"CC_BYZ_WEST_PF_OPEN\"  visible = \"[Player.MakeScope.GetVariable('cc_byz_west_pf_{pf}_open').IsSet]\" }}",
          f"\t\ttext_multi = {{ layoutpolicy_horizontal = expanding  autoresize = yes  multiline = yes  max_width = 228  fontsize = 10  default_format = \"#weak\"  text = \"CC_BYZ_WEST_PF_{up}_REQ\"  visible = \"[Not(Player.MakeScope.GetVariable('cc_byz_west_pf_{pf}_open').IsSet)]\" }}",
          '\t\texpand = {}',
          '\t}',
          '}']
    return l


def governing_card() -> list[str]:
    l = ['vbox = {',
         '\tlayoutpolicy_horizontal = expanding',
         '\tbackground = { using = color_whiteish_texture  alpha = 0.10 }',
         '\tmargin = { 10 8 }',
         '\tspacing = 4']
    l += ind(card_title('CC_BYZ_WEST_SEC_GOVERNING'), 1)
    l += ['\ttext_single = { layoutpolicy_horizontal = expanding  fontsize = 11  default_format = "#weak"  align = left|nobaseline  text = "CC_BYZ_WEST_GOVERNING_DESC" }',
          '\thbox = {',
          '\t\tspacing = 6']
    for key, _label, mod in EMPIRE_ACTIONS:
        l += ['\t\tvbox = {', '\t\t\tspacing = 1']
        l += ind(button(key, f'CC_BYZ_WEST_BTN_{key.upper()}', 156), 3)
        l += [f"\t\t\ttext_single = {{ fontsize = 10  default_format = \"#weak\"  align = center|nobaseline  text = \"CC_BYZ_WEST_ON_COOLDOWN\"  visible = \"[Player.HasModifier('{mod}')]\" }}",
              '\t\t}']
    l += ['\t}', '}']
    return l


def consistory_tab() -> list[str]:
    votes = "Player.MakeScope.GetVariable('cc_byz_west_votes_west').GetValue"
    l = ['scrollarea = {',
         "\tvisible = \"[SituationView.Vars.HasValue( 'situation_tab', 'cc_byz_west_consistory' )]\"",
         '\tusing = layoutpolicy_expanding',
         '\tscrollbarpolicy_horizontal = always_off',
         '\tautoresizeviewport = yes',
         '\tviewportwidget = { widget = { scissor = yes } }',
         '\tscrollbar_vertical = { using = Scrollbar_Vertical }',
         '\tscrollwidget = {',
         '\t\tvbox = {',
         '\t\t\tlayoutpolicy_horizontal = expanding',
         '\t\t\tusing = bg_secondary_inner_alt',
         '\t\t\tmargin = { 10 8 }',
         '\t\t\tspacing = 6',
         '\t\t\tvbox = {',
         '\t\t\t\tlayoutpolicy_horizontal = expanding',
         '\t\t\t\tbackground = { using = color_whiteish_texture  alpha = 0.10 }',
         '\t\t\t\tmargin = { 10 8 }',
         '\t\t\t\tspacing = 5']
    l += ind(card_title('CC_BYZ_WEST_CARD_CONSISTORY', 'CC_BYZ_WEST_CARD_CONSISTORY_INFO'), 4)
    l += ['\t\t\t\ttext_multi = { layoutpolicy_horizontal = expanding  autoresize = yes  multiline = yes  max_width = 480  fontsize = 11  default_format = "#weak"  text = "CC_BYZ_WEST_CARD_CONSISTORY_DESC" }',
          "\t\t\t\ttext_single = { fontsize = 13  default_format = \"#color_green\"  text = \"CC_BYZ_WEST_CONS_SITTING\"  visible = \"[Player.MakeScope.GetVariable('cc_byz_west_convened').IsSet]\" }",
          "\t\t\t\ttext_single = { fontsize = 13  default_format = \"#weak\"  text = \"CC_BYZ_WEST_CONS_DORMANT\"  visible = \"[Not(Player.MakeScope.GetVariable('cc_byz_west_convened').IsSet)]\" }",
          '\t\t\t\thbox = {',
          '\t\t\t\t\tlayoutpolicy_horizontal = expanding',
          '\t\t\t\t\ttext_single = { fontsize = 13  text = "CC_BYZ_WEST_VOTES_EMPEROR" }',
          '\t\t\t\t\texpand = {}',
          '\t\t\t\t\ttext_single = { fontsize = 13  text = "CC_BYZ_WEST_VOTES_WEST" }',
          f'\t\t\t\t\ttext_single = {{ fontsize = 15  default_format = "#color_yellow"  raw_text = " [FixedPointToInt({votes})]" }}',
          '\t\t\t\t}',
          f"\t\t\t\ttext_single = {{ fontsize = 12  default_format = \"#color_green\"  text = \"CC_BYZ_WEST_VOTES_SAFE\"  visible = \"[GreaterThan_CFixedPoint('(CFixedPoint)3', {votes})]\" }}",
          f"\t\t\t\ttext_single = {{ fontsize = 12  default_format = \"#color_yellow\"  text = \"CC_BYZ_WEST_VOTES_TIE\"  visible = \"[EqualTo_CFixedPoint({votes}, '(CFixedPoint)3')]\" }}",
          f"\t\t\t\ttext_single = {{ fontsize = 12  default_format = \"#color_red\"  text = \"CC_BYZ_WEST_VOTES_LOST\"  visible = \"[GreaterThan_CFixedPoint({votes}, '(CFixedPoint)3')]\" }}",
          # member roster
          '\t\t\t\tvbox = {',
          '\t\t\t\t\tlayoutpolicy_horizontal = expanding',
          '\t\t\t\t\tspacing = 2',
          '\t\t\t\t\tdatamodel = "[Player.GetDiplomacy.GetSubjects]"',
          '\t\t\t\t\tignoreinvisible = yes',
          '\t\t\t\t\titem = {',
          '\t\t\t\t\t\thbox = {',
          '\t\t\t\t\t\t\tlayoutpolicy_horizontal = expanding',
          '\t\t\t\t\t\t\tminimumsize = { -1 26 }',
          '\t\t\t\t\t\t\tspacing = 6',
          "\t\t\t\t\t\t\tvisible = \"[Country.MakeScope.GetVariable('cc_byz_is_exarchate').IsSet]\"",
          '\t\t\t\t\t\t\tcountry_flag_small = {}',
          '\t\t\t\t\t\t\ttext_single = { fontsize = 13  max_width = 220  elide = right  text = "[Country.GetName]" }',
          "\t\t\t\t\t\t\ttext_single = { fontsize = 10  default_format = \"#color_yellow\"  text = \"CC_BYZ_WEST_TAG_SENIOR\"  visible = \"[Country.MakeScope.GetVariable('cc_byz_exarch_senior').IsSet]\" }",
          '\t\t\t\t\t\t\texpand = {}',
          '\t\t\t\t\t\t\ttext_single = { fontsize = 11  default_format = "#weak"  text = "CC_BYZ_WEST_COL_VOTES" }',
          "\t\t\t\t\t\t\ttext_single = { fontsize = 13  raw_text = \"2\"  visible = \"[Country.MakeScope.GetVariable('cc_byz_exarch_senior').IsSet]\" }",
          "\t\t\t\t\t\t\ttext_single = { fontsize = 13  raw_text = \"1\"  visible = \"[Not(Country.MakeScope.GetVariable('cc_byz_exarch_senior').IsSet)]\" }",
          '\t\t\t\t\t\t}',
          '\t\t\t\t\t}',
          '\t\t\t\t}',
          '\t\t\t\ttext_multi = { layoutpolicy_horizontal = expanding  autoresize = yes  multiline = yes  max_width = 480  fontsize = 11  default_format = "#weak"  text = "CC_BYZ_WEST_CONS_QUESTIONS" }',
          '\t\t\t\thbox = {',
          '\t\t\t\t\tspacing = 6']
    for key, _label in CONSISTORY_ACTIONS:
        l += ind(button(key, f'CC_BYZ_WEST_BTN_{key.upper()}', 156), 5)
    l += ['\t\t\t\t}',
          '\t\t\t}',
          '\t\t}',
          '\t}',
          '}']
    return l


def emit_gui() -> str:
    head = [BOM + '######################################################################',
            '# The West: situation panel',
            '#',
            GENERATED.rstrip('\n'),
            '#',
            '# Breakdown tab (the default): header, the balance (two counters, the year\'s drift and the',
            '# map of endings), one card per prefecture with its exarch and its own actions, and the',
            '# empire-wide actions. Consistory tab: the vote arithmetic, the roster and the IO actions.',
            '#',
            '# Reads, all republished by script because the GUI cannot run triggers or script values:',
            '#   situation  cc_byz_imperial_grip, cc_byz_western_autonomy, cc_byz_west_*_drift',
            '#   empire     cc_byz_west_pf_<key> (the exarchate), cc_byz_west_pf_<key>_open,',
            '#              cc_byz_west_convened, cc_byz_west_votes_west',
            '#   exarchate  cc_byz_exarch_loyalty, _appetite, _kind, _hereditary, _senior, _cession_cd',
            '# See scripted_effects/cc_byz_west_prefecture_effects.txt.',
            '#',
            '# The vanilla actions card is emptied: every action is a button on its card. The',
            '# illustration block is NOT overridden (see the Court Ledger for why).',
            '######################################################################',
            '',
            'situation_panel = {',
            '']
    body = []
    # top subheader: the two numbers and the restive signal, as before
    body += ['blockoverride "situation_top_subheader_content" {',
             '\thbox = {',
             '\t\tlayoutpolicy_horizontal = expanding',
             '\t\tmargin = { 8 0 }',
             '\t\tspacing = 10',
             '\t\thbox = {',
             '\t\t\tsize = { 170 28 }',
             '\t\t\tspacing = 5',
             '\t\t\ttext_single = { fontsize = 13  default_format = "#weak"  text = "CC_BYZ_WEST_HDR_GRIP" }',
             f'\t\t\ttext_single = {{ fontsize = 15  default_format = "#color_yellow"  raw_text = "[FixedPointToInt({GRIP})]" }}',
             '\t\t}',
             '\t\texpand = {}',
             '\t\ttext_single = { fontsize = 14  default_format = "#color_red"  text = "CC_BYZ_WEST_HDR_RESTIVE"  visible = "[Player.HasModifier(\'cc_byz_west_restive\')]"  tooltip = "CC_BYZ_WEST_HDR_RESTIVE_TT" }',
             '\t\texpand = {}',
             '\t\thbox = {',
             '\t\t\tsize = { 170 28 }',
             '\t\t\tspacing = 5',
             f'\t\t\ttext_single = {{ fontsize = 15  default_format = "#color_red"  raw_text = "[FixedPointToInt({AUT})]" }}',
             '\t\t\ttext_single = { fontsize = 13  default_format = "#weak"  text = "CC_BYZ_WEST_HDR_AUTONOMY" }',
             '\t\t}',
             '\t}',
             '}',
             '',
             'blockoverride "situation_subheader_content" {}',
             'blockoverride "situation_panel_main_content_top" {}',
             'blockoverride "situation_panel_main_actions" {}',
             '',
             'blockoverride "situation_panel_main_content" {',
             '\t# Header card',
             '\tvbox = {',
             '\t\tlayoutpolicy_horizontal = expanding',
             '\t\tsize = { 510 40 }',
             '\t\tusing = bg_card_header_01_government',
             '\t\thbox = {',
             '\t\t\tlayoutpolicy_horizontal = expanding',
             '\t\t\tspacing = 6',
             '\t\t\tmargin = { 10 0 }',
             '\t\t\ticon = { size = { 24 24 }  texture = "gfx/interface/icons/situations/cc_byz_the_west.dds"  texture_density = 2 }',
             '\t\t\ttext_single = { fontsize = 16  text = "CC_BYZ_WEST_PANEL_HEADER" }',
             '\t\t\texpand = {}',
             '\t\t\ticon = {',
             '\t\t\t\tsize = { 20 20 }',
             '\t\t\t\ttexture = "gfx/interface/icons/flat_icons/tabicons/info_flat_icon.dds"',
             '\t\t\t\ttexture_density = 2',
             '\t\t\t\ttooltipwidget = {',
             '\t\t\t\t\tContextualTooltipType = {',
             '\t\t\t\t\t\tblockoverride "title_text" { text = "CC_BYZ_WEST_PANEL_HEADER" }',
             '\t\t\t\t\t\tblockoverride "tooltip_content" {',
             '\t\t\t\t\t\t\ttext_multi = { autoresize = yes  multiline = yes  max_width = 330  text = "CC_BYZ_WEST_PANEL_HEADER_TT" }',
             '\t\t\t\t\t\t}',
             '\t\t\t\t\t}',
             '\t\t\t\t}',
             '\t\t\t}',
             '\t\t}',
             '\t}',
             '']
    body += ind(balance_card(), 1)
    body += ['',
             '\ttext_single = { layoutpolicy_horizontal = expanding  fontsize = 12  default_format = "#weak"  margin_top = 4  text = "CC_BYZ_WEST_SEC_PREFECTURES"  tooltip = "CC_BYZ_WEST_CARD_PREFECTURES_DESC" }',
             '\tflowcontainer = {',
             '\t\tdirection = horizontal',
             '\t\twrap_count = 2',
             '\t\tignoreinvisible = yes',
             '\t\tspacing = 6']
    for pf, *_ in PREFECTURES:
        body += ind(pf_card(pf), 2)
    body += ['\t}', '']
    body += ind(governing_card(), 1)
    body += ['}',
             '',
             'blockoverride "situation_extra_tabs_content" {',
             '\tbutton_secondary_tab_alt = {',
             '\t\tusing = layoutpolicy_expanding',
             '\t\tblockoverride "tab_text" { text = "CC_BYZ_WEST_TAB_CONSISTORY" }',
             '\t\taction_tooltip = {',
             '\t\t\ttitle = "OPEN_TAB"',
             "\t\t\ton_action = \"[SituationView.Vars.Set( 'situation_tab', 'cc_byz_west_consistory' )]\"",
             '\t\t}',
             "\t\tdown = \"[SituationView.Vars.HasValue( 'situation_tab', 'cc_byz_west_consistory' )]\"",
             '\t}',
             '}',
             '',
             'blockoverride "situation_extra_tab_panels" {']
    body += ind(consistory_tab(), 1)
    body += ['}']
    return '\n'.join(head + ind(body, 1) + ['}', ''])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true', help='report stale outputs and exit 1 instead of writing')
    args = ap.parse_args()

    outputs = {GUI_OUT: emit_gui(), ACTIONS_OUT: emit_actions(), LOC_OUT: emit_loc()}
    stale = []
    for path, text in outputs.items():
        current = path.read_text(encoding='utf-8') if path.exists() else None
        if current != text:
            stale.append(path)
            if not args.check:
                path.write_text(text, encoding='utf-8')
    for path in stale:
        print(('stale: ' if args.check else 'wrote: ') + str(path.relative_to(REPO)))
    if not stale:
        print('up to date')
    return 1 if (args.check and stale) else 0


if __name__ == '__main__':
    sys.exit(main())
