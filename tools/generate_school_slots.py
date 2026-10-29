#!/usr/bin/env python3
"""Generate the per-school actions, their loc and the school cards for the court panel.

A realm has at most three schools, held in numbered country variables (cc_xp_school_N_*).
Everything a player does to ONE school has to name the slot, and a panel button cannot pass a
slot number to an action: a generic_action driven from a button gets an actor and nothing
else (see the gotchas on GUI-invoked actions). So each action exists once per slot as a thin
wrapper around one scripted effect that takes N, and each slot has its own card template
and tooltip strings that read its own variables. That is three copies of the same thing,
which is what this script is for: edit the tables and templates here, never the output.

Writes:
  in_game/common/generic_actions/cc_xp_school_actions.txt
  in_game/gui/panels/situation/cc_xp_school_cards.gui
  in_game/localization/english/cc_xp_school_actions_l_english.yml

The logic lives in scripted_effects/cc_xp_school_effects.txt and the gates in
scripted_triggers/cc_xp_triggers.txt; the shared strings in
localization/english/cc_xp_school_l_english.yml. The generated loc only aliases them or
fills in the slot's variables.

    python tools/generate_school_slots.py
    python tools/generate_school_slots.py --check   # exit 1 if any output is stale
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SLOTS = (1, 2, 3)

ACTIONS_OUT = REPO / 'in_game' / 'common' / 'generic_actions' / 'cc_xp_school_actions.txt'
GUI_OUT = REPO / 'in_game' / 'gui' / 'panels' / 'situation' / 'cc_xp_school_cards.gui'
LOC_OUT = REPO / 'in_game' / 'localization' / 'english' / 'cc_xp_school_actions_l_english.yml'

# key, price (or None), allow trigger, effect, button loc key
ACTIONS = [
    ('endow', 'cc_xp_school_endow', 'cc_xp_school_can_act', 'cc_xp_school_do_endow', 'CC_XP_SCHOOL_BTN_ENDOW'),
    ('chairs', 'cc_xp_school_chairs', 'cc_xp_school_can_act', 'cc_xp_school_do_chairs', 'CC_XP_SCHOOL_BTN_CHAIRS'),
    ('scholars', 'cc_xp_school_scholars', 'cc_xp_school_can_act', 'cc_xp_school_do_scholars', 'CC_XP_SCHOOL_BTN_SCHOLARS'),
    ('disputation', None, 'cc_xp_school_can_act', 'cc_xp_school_do_disputation', 'CC_XP_SCHOOL_BTN_DISPUTATION'),
    ('curriculum', None, 'cc_xp_school_can_change_curriculum', 'cc_xp_school_do_curriculum', 'CC_XP_SCHOOL_BTN_CURRICULUM'),
    # One per Admission level, drawn as a radio group so any level can be picked directly.
    ('admission_1', None, 'cc_xp_school_can_admission_1', 'cc_xp_school_do_admission_1', 'CC_XP_SCHOOL_ADMISSION_1'),
    ('admission_2', None, 'cc_xp_school_can_admission_2', 'cc_xp_school_do_admission_2', 'CC_XP_SCHOOL_ADMISSION_2'),
    ('admission_3', None, 'cc_xp_school_can_admission_3', 'cc_xp_school_do_admission_3', 'CC_XP_SCHOOL_ADMISSION_3'),
]
# Actions whose button sits in a row of the card rather than the action bar at its foot.
ROW_ACTIONS = {'admission_1', 'admission_2', 'admission_3'}
ADMISSIONS = 3     # CC_XP_SCHOOL_ADMISSION_1..3 (Low, Medium, High)
# Royal Chairs also needs someone to teach.
EXTRA_ALLOW = {'chairs': 'cc_xp_school_has_members'}

KINDS = 8          # CC_XP_SCHOOL_KIND_1..8
CURRICULA = 15     # CC_XP_CURRICULUM_1..15 (five per discipline)
TRACKS = {1: 'CC_XP_COL_ADM', 2: 'CC_XP_COL_DIP', 3: 'CC_XP_COL_MIL'}
# Tier names for renown and quality: (lower bound, loc key suffix), 0-100 in quarters.
TIERS = [(0, 1), (25, 2), (50, 3), (75, 4)]

GENERATED = '# GENERATED FILE. Do not edit by hand: python tools/generate_school_slots.py\n'
T = '\t'


def emit_actions() -> str:
    out = [
        '﻿' + '#' * 79,
        GENERATED.rstrip(),
        '#',
        '# One generic action per school action per slot. Each is a thin wrapper: the gates are',
        '# scripted triggers and the work is a scripted effect, both taking N. type = owncountry',
        '# with no select_trigger, because the court panel drives these from a button that',
        '# supplies an actor and nothing else (see cc_xp_court_actions.txt for why).',
        '#' * 79,
        '',
    ]
    for n in SLOTS:
        out.append(f'\n########## School {n} ##########\n')
        for key, price, gate, effect, _ in ACTIONS:
            allow = [f'\t\t\t{gate} = {{ N = {n} }}']
            if key in EXTRA_ALLOW:
                allow.append(f'\t\t\t{EXTRA_ALLOW[key]} = {{ N = {n} }}')
            out.append(f'cc_xp_school_{n}_{key} = {{')
            out.append('\ttype = owncountry')
            if price:
                out.append(f'\tprice = price:{price}')
            out.append('\tai_tick = never')
            out.append('')
            out.append('\tpotential = {')
            out.append('\t\tscope:actor = {')
            out.append('\t\t\tcc_xp_enabled = yes')
            out.append(f'\t\t\thas_variable = cc_xp_school_{n}_founder')
            out.append('\t\t}')
            out.append('\t}')
            out.append('')
            out.append('\tallow = {')
            out.append('\t\tscope:actor = {')
            out.extend(allow)
            out.append('\t\t}')
            out.append('\t}')
            out.append('')
            out.append('\teffect = {')
            out.append(f'\t\tscope:actor = {{ {effect} = {{ N = {n} }} }}')
            out.append('\t}')
            out.append('')
            out.append('\tai_will_do = {')
            out.append('\t\tadd = { value = 0 }')
            out.append('\t}')
            out.append('}')
            out.append('')
    return '\n'.join(out) + '\n'


def lv(n: int, name: str, fmt: str = '0') -> str:
    """A slot variable as a loc command."""
    return f"[Player.MakeScope.GetVariable('cc_xp_school_{n}_{name}').GetValue|{fmt}]"


def emit_loc() -> str:
    nl = '\\n'
    out = ['﻿l_english:', ' ' + GENERATED.strip()]
    for n in SLOTS:
        for key, *_ in ACTIONS:
            out.append(f' cc_xp_school_{n}_{key}: "$cc_xp_school_{key}$"')
            out.append(f' cc_xp_school_{n}_{key}_desc: "$cc_xp_school_{key}_desc$"')
    # Card strings that read the slot's own variables, so one per slot.
    for n in SLOTS:
        out.append(
            f' CC_XP_SCHOOL_{n}_RENOWN_TT: "$CC_XP_SCHOOL_RENOWN_TT_HEAD${nl}{nl}'
            f'$CC_XP_SCHOOL_TT_MATURITY$ #Y {lv(n, "maturity")}%#!{nl}'
            f'$CC_XP_SCHOOL_TT_RANK$ #Y {lv(n, "r_rank", "1")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_PRESTIGE$ #Y {lv(n, "r_prestige", "1")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_WEALTH$ #Y {lv(n, "r_wealth", "1")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_LEARNING$ #Y {lv(n, "r_learning", "1")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_TEACHING$ #Y {lv(n, "r_quality", "1")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_TARGET$ #Y {lv(n, "renown_target")}#!{nl}{nl}'
            f'$CC_XP_SCHOOL_RENOWN_TT_FOOT$"')
        out.append(
            f' CC_XP_SCHOOL_{n}_QUALITY_TT: "$CC_XP_SCHOOL_QUALITY_TT_HEAD${nl}{nl}'
            f'$CC_XP_SCHOOL_TT_FUNDING$ #Y {lv(n, "q_funding")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_RECTOR$ #Y {lv(n, "q_rector")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_STABLE$ #Y {lv(n, "q_stable")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_MEMBERS_APT$ #Y {lv(n, "q_members", "1")}#! ($CC_XP_SCHOOL_TT_APT_AVG$ {lv(n, "apt_avg")}){nl}'
            f'$CC_XP_SCHOOL_TT_TARGET$ #Y {lv(n, "quality_target")}#!{nl}{nl}'
            f'$CC_XP_SCHOOL_QUALITY_TT_FOOT$ #Y {lv(n, "qscale", "2")}#!"')
        out.append(f' CC_XP_SCHOOL_{n}_STANDING: "$CC_XP_SCHOOL_STANDING_PREFIX$ {lv(n, "standing")}"')
        out.append(f' CC_XP_SCHOOL_{n}_COST: "{lv(n, "cost", "1")} @gold!$CC_XP_SCHOOL_PER_MONTH$"')
        out.append(f' CC_XP_SCHOOL_{n}_FOUNDED: "$CC_XP_SCHOOL_FOUNDED_PREFIX$ {lv(n, "founded")}"')
        out.append(f' CC_XP_SCHOOL_{n}_MEMBERS: "{lv(n, "members")} / {lv(n, "capacity")}"')
        out.append(
            f' CC_XP_SCHOOL_{n}_MEMBERS_TT: "$CC_XP_SCHOOL_MEMBERS_TT${nl}{nl}'
            f'$CC_XP_SCHOOL_TT_CAPACITY$ #Y {lv(n, "capacity")}#!{nl}'
            f'$CC_XP_SCHOOL_TT_ENROL_CHANCE$ #Y {lv(n, "enrol_chance")}%#!{nl}'
            f'$CC_XP_SCHOOL_TT_APT_AVG$ #Y {lv(n, "apt_avg")}#!"')
    return '\n'.join(out) + '\n'


def var(n: int, name: str) -> str:
    return f"Player.MakeScope.GetVariable('cc_xp_school_{n}_{name}')"


def eq(n: int, name: str, value: int) -> str:
    return f"[EqualTo_CFixedPoint({var(n, name)}.GetValue, '(CFixedPoint){value}')]"


def ind(text: str, depth: int) -> str:
    """Indent every non-empty line of a block by depth tabs."""
    return '\n'.join((T * depth + line) if line else line for line in text.split('\n'))


def tier_texts(n: int, name: str, prefix: str) -> str:
    """One text per tier, each visible only in its quarter of 0-100."""
    rows = []
    v = f'{var(n, name)}.GetValue'
    for idx, (lo, key) in enumerate(TIERS):
        conds = [f"GreaterThanOrEqualTo_CFixedPoint({v}, '(CFixedPoint){lo}')"]
        if idx + 1 < len(TIERS):
            conds.append(f"GreaterThan_CFixedPoint('(CFixedPoint){TIERS[idx + 1][0]}', {v})")
        vis = conds[0] if len(conds) == 1 else f'And({conds[0]}, {conds[1]})'
        rows.append(f'text_single = {{ fontsize = 12  align = left|nobaseline  visible = "[{vis}]"  text = "{prefix}_{key}" }}')
    return '\n'.join(rows)


def label(key: str) -> str:
    return (f'text_single = {{ size = {{ 70 20 }}  autoresize = no  fontsize = 11  default_format = "#weak"  '
            f'align = left|nobaseline  text = "{key}" }}')


def bar(n: int, name: str, texture: str, tooltip: str, label_key: str, tier_prefix: str, extra: str = '') -> str:
    body = f'''hbox = {{
	layoutpolicy_horizontal = expanding
	spacing = 6
	tooltip = "{tooltip}"
	{label(label_key)}
	widget = {{
		size = {{ 140 10 }}
		progressbar = {{
			size = {{ 100% 100% }}
			noprogresstexture = "gfx/interface/progressbars/progress_bar_grey_alt.dds"
			progresstexture = "gfx/interface/progressbars/{texture}"
			texture_density = 2
			spriteType = Corneredstretched
			spriteborder = {{ 12 0 }}
			min = 0
			max = 100
			value = "[FixedPointToFloat({var(n, name)}.GetValue)]"
		}}
	}}
	text_single = {{ fontsize = 12  align = left|nobaseline  raw_text = "[{var(n, name)}.GetValue|0]" }}
{ind(tier_texts(n, name, tier_prefix), 1)}
{ind(extra, 1) + chr(10) if extra else ''}	expand = {{}}
}}'''
    return body


def portrait(n: int, name: str, label_key: str, tooltip: str, dead_note: bool) -> str:
    dead = '''
		text_single = {
			fontsize = 10
			default_format = "#weak"
			align = left|nobaseline
			visible = "[Not(Character.IsAlive)]"
			text = "CC_XP_SCHOOL_FOUNDER_DEAD"
			tooltip = "CC_XP_SCHOOL_FOUNDER_DEAD_TT"
		}''' if dead_note else ''
    return f'''hbox = {{
	layoutpolicy_horizontal = expanding
	spacing = 6
	visible = "[{var(n, name)}.IsSet]"
	datacontext = "[{var(n, name)}.GetCharacter]"
	portrait_standard_head_framed_button = {{
		size = {{ 46 52 }}
		onclick = "[ShowCharacter(Character.Self)]"
	}}
	vbox = {{
		layoutpolicy_horizontal = expanding
		text_single = {{ layoutpolicy_horizontal = expanding  fontsize = 10  default_format = "#weak"  align = left|nobaseline  text = "{label_key}"  tooltip = "{tooltip}" }}
		text_single = {{ layoutpolicy_horizontal = expanding  fontsize = 13  align = left|nobaseline  text = "[Character.GetShortNameWithNoTooltip]" }}{dead}
	}}
}}'''


def choice_row(n: int, label_key: str, name: str, count: int, key_fmt: str, tooltip_fmt: str | None, extra: str = '') -> str:
    texts = []
    for i in range(1, count + 1):
        tt = f'  tooltip = "{tooltip_fmt.format(i)}"' if tooltip_fmt else ''
        texts.append(f'\ttext_single = {{ fontsize = 12  align = left|nobaseline  visible = "{eq(n, name, i)}"  text = "{key_fmt.format(i)}"{tt} }}')
    return (f'hbox = {{\n\tlayoutpolicy_horizontal = expanding\n\tspacing = 6\n\t{label(label_key)}\n'
            + '\n'.join(texts) + '\n' + (ind(extra, 1) + '\n' if extra else '') + '\texpand = {}\n}')


def funding_row(cost: str) -> str:
    """Funding follows the realm's Culture budget slider, so it reads realm variables."""
    no_culture = "Player.MakeScope.GetVariable('cc_xp_school_no_culture')"
    return f'''hbox = {{
	layoutpolicy_horizontal = expanding
	spacing = 6
	{label('CC_XP_SCHOOL_FUNDING_LABEL')}
	text_single = {{ fontsize = 12  align = left|nobaseline  visible = "[Not({no_culture}.IsSet)]"  text = "CC_XP_SCHOOL_FUNDING_CULTURE"  tooltip = "CC_XP_SCHOOL_FUNDING_TT" }}
	text_single = {{ fontsize = 12  align = left|nobaseline  visible = "[{no_culture}.IsSet]"  text = "CC_XP_SCHOOL_FUNDING_CUSTOMARY"  tooltip = "CC_XP_SCHOOL_FUNDING_CUSTOMARY_TT" }}
{ind(cost, 1)}
	expand = {{}}
}}'''


def button(n: int, key: str, label_key: str, size: str = '92 28') -> str:
    return f'''card_header_button_01 = {{
	size = {{ {size} }}
	scripted_action_tooltip = {{
		click_type = left
		click_mode = single
		action_name = "cc_xp_school_{n}_{key}"
		actor = "[Player]"
	}}
	enabled = "[PdxGuiWidget.IsUberButtonEnabled]"
	tooltipwidget = {{ using = action_tooltip_pop_out }}
	text_single = {{
		parentanchor = center
		align = center
		fontsize = 10
		text = "{label_key}"
	}}
}}'''


def admission_row(n: int) -> str:
    """Admission as a radio group: one round checkbox per level, pressed for the current one.
    Same widget vanilla uses for the trade policy strategy (automation_lateralview.gui)."""
    radios = []
    for i in range(1, ADMISSIONS + 1):
        radios.append(f'''hbox = {{
	spacing = 3
	checkbox_round_alt = {{
		size = {{ 20 20 }}
		down = "{eq(n, 'apt', i)}"
		scripted_action_tooltip = {{
			click_type = left
			click_mode = single
			action_name = "cc_xp_school_{n}_admission_{i}"
			actor = "[Player]"
		}}
		enabled = "[PdxGuiWidget.IsUberButtonEnabled]"
		tooltipwidget = {{ using = action_tooltip_pop_out }}
	}}
	text_single = {{ fontsize = 12  align = left|nobaseline  text = "CC_XP_SCHOOL_ADMISSION_{i}"  tooltip = "CC_XP_SCHOOL_ADMISSION_{i}_TT" }}
}}''')
    return (f'hbox = {{\n\tlayoutpolicy_horizontal = expanding\n\tspacing = 10\n'
            f'\t{label("CC_XP_SCHOOL_ADMISSION_LABEL")}\n'
            + '\n'.join(ind(r, 1) for r in radios) + '\n\texpand = {}\n}')


def emit_card(n: int) -> str:
    kinds = '\n'.join(
        f'text_single = {{ fontsize = 19  align = left|nobaseline  visible = "{eq(n, "kind", k)}"  text = "CC_XP_SCHOOL_KIND_{k}" }}'
        for k in range(1, KINDS + 1))
    tracks = '\n'.join(
        f'text_single = {{ fontsize = 13  align = right|nobaseline  visible = "{eq(n, "track", t)}"  text = "{key}"  tooltip = "CC_XP_SCHOOL_TRACK_TT" }}'
        for t, key in TRACKS.items())
    standing = (f'text_single = {{ fontsize = 11  default_format = "#weak"  align = left|nobaseline  '
                f'visible = "[GreaterThan_CFixedPoint({var(n, "standing")}.GetValue, \'(CFixedPoint)0\')]"  '
                f'text = "CC_XP_SCHOOL_{n}_STANDING"  tooltip = "CC_XP_SCHOOL_STANDING_TT" }}')
    cost = (f'text_single = {{ fontsize = 11  default_format = "#weak"  align = left|nobaseline  '
            f'visible = "[GreaterThan_CFixedPoint({var(n, "cost")}.GetValue, \'(CFixedPoint)0\')]"  '
            f'text = "CC_XP_SCHOOL_{n}_COST" }}')
    members = (f'hbox = {{\n\tlayoutpolicy_horizontal = expanding\n\tspacing = 6\n\t{label("CC_XP_SCHOOL_MEMBERS_LABEL")}\n'
               f'\ttext_single = {{ fontsize = 12  align = left|nobaseline  text = "CC_XP_SCHOOL_{n}_MEMBERS"  tooltip = "CC_XP_SCHOOL_{n}_MEMBERS_TT" }}\n'
               f'\texpand = {{}}\n}}')
    admission = admission_row(n)
    no_rector = f'''hbox = {{
	layoutpolicy_horizontal = expanding
	spacing = 6
	visible = "[Not({var(n, 'rector')}.IsSet)]"
	widget = {{
		size = {{ 46 52 }}
		background = {{ using = color_whiteish_texture  alpha = 0.06 }}
	}}
	text_single = {{
		fontsize = 11
		default_format = "#weak"
		align = left|nobaseline
		text = "CC_XP_SCHOOL_NO_RECTOR"
		tooltip = "CC_XP_SCHOOL_RECTOR_TT"
	}}
	expand = {{}}
}}'''
    buttons = '\n'.join(button(n, key, lbl) for key, _, _, _, lbl in ACTIONS if key not in ROW_ACTIONS)

    left = '\n\n'.join([
        portrait(n, 'founder', 'CC_XP_SCHOOL_FOUNDER_LABEL', 'CC_XP_SCHOOL_FOUNDER_TT', True),
        portrait(n, 'rector', 'CC_XP_SCHOOL_RECTOR_LABEL', 'CC_XP_SCHOOL_RECTOR_TT', False),
        no_rector,
        'expand = {}',
    ])
    right = '\n\n'.join([
        bar(n, 'renown', 'progress_bar_goldish.dds', f'CC_XP_SCHOOL_{n}_RENOWN_TT', 'CC_XP_SCHOOL_RENOWN_LABEL', 'CC_XP_SCHOOL_RENOWN_TIER', standing),
        bar(n, 'quality', 'progress_bar_green.dds', f'CC_XP_SCHOOL_{n}_QUALITY_TT', 'CC_XP_SCHOOL_QUALITY_LABEL', 'CC_XP_SCHOOL_QUALITY_TIER'),
        choice_row(n, 'CC_XP_SCHOOL_CURRICULUM_LABEL', 'curriculum', CURRICULA, 'CC_XP_CURRICULUM_{}', 'CC_XP_CURRICULUM_{}_TT'),
        funding_row(cost),
        members,
        admission,
        'expand = {}',
    ])

    return f'''template cc_xp_school_card_{n} {{
	layoutpolicy_horizontal = expanding
	size = {{ -1 262 }}
	background = {{ using = color_whiteish_texture  alpha = 0.10 }}

	vbox = {{
		layoutpolicy_horizontal = expanding
		layoutpolicy_vertical = expanding
		margin = {{ 12 8 }}
		spacing = 6

		# ---- Header: kind, seat, discipline ----
		hbox = {{
			layoutpolicy_horizontal = expanding
			spacing = 6

{ind(kinds, 3)}

			text_single = {{ fontsize = 15  default_format = "#weak"  align = left|nobaseline  text = "CC_XP_SCHOOL_OF" }}

			# The seat. Click selects it and opens its window, double-click pans the map to
			# it: vanilla pairs onclick with ondoubleclick and never gives a widget two onclicks.
			button = {{
				size = {{ 180 26 }}
				datacontext = "[{var(n, 'loc')}.GetLocation]"
				onclick = "[SelectLocation(Location.Self)]"
				ondoubleclick = "[PanToLocation(Location.Self)]"
				tooltipwidget = {{ using = location_simple_tooltip }}
				text_single = {{
					parentanchor = left|vcenter
					fontsize = 19
					align = left|nobaseline
					text = "[Location.GetNameWithNoTooltip]"
				}}
			}}

			expand = {{}}

{ind(tracks, 3)}
		}}

		# ---- Founding year and status ----
		hbox = {{
			layoutpolicy_horizontal = expanding
			spacing = 8
			text_single = {{
				fontsize = 11
				default_format = "#weak"
				align = left|nobaseline
				visible = "[{var(n, 'founded')}.IsSet]"
				text = "CC_XP_SCHOOL_{n}_FOUNDED"
			}}
			text_single = {{
				fontsize = 11
				align = left|nobaseline
				visible = "[{var(n, 'exile')}.IsSet]"
				text = "CC_XP_SCHOOL_IN_EXILE"
				tooltip = "CC_XP_SCHOOL_IN_EXILE_TT"
			}}
			text_single = {{
				fontsize = 11
				align = left|nobaseline
				visible = "[{var(n, 'dormant')}.IsSet]"
				text = "CC_XP_SCHOOL_DORMANT"
				tooltip = "CC_XP_SCHOOL_DORMANT_TT"
			}}
			expand = {{}}
		}}

		# ---- Body: people on the left, standing on the right ----
		hbox = {{
			layoutpolicy_horizontal = expanding
			layoutpolicy_vertical = expanding
			spacing = 12

			vbox = {{
				size = {{ 170 -1 }}
				layoutpolicy_vertical = expanding
				spacing = 6

{ind(left, 4)}
			}}

			vbox = {{
				layoutpolicy_horizontal = expanding
				layoutpolicy_vertical = expanding
				spacing = 5

{ind(right, 4)}
			}}
		}}

		# ---- Actions ----
		hbox = {{
			layoutpolicy_horizontal = expanding
			spacing = 3

{ind(buttons, 3)}

			expand = {{}}
		}}
	}}
}}
'''


def emit_gui() -> str:
    head = f'''######################################################################
{GENERATED.rstrip()}
#
# Flavorium Universalis: one card per founded school, for the Schools tab of the court
# panel (cc_cabinet_court.gui). A realm holds at most three, so each card is large: the
# three together fill most of the panel. One template per slot, because each reads its
# own cc_xp_school_N_* variables and drives its own cc_xp_school_N_* actions.
#
# Properties are declared at top level, not wrapped in a widget: `using = <template>`
# merges a template's contents into the widget it is used on, and an extra layer here
# collapses to zero size and takes its children's mouse input with it.
######################################################################

'''
    return '﻿' + head + '\n\n'.join(emit_card(n) for n in SLOTS)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true', help='report stale outputs and exit 1 instead of writing')
    args = ap.parse_args()

    outputs = {ACTIONS_OUT: emit_actions(), GUI_OUT: emit_gui(), LOC_OUT: emit_loc()}
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
