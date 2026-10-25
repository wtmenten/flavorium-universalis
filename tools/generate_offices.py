#!/usr/bin/env python3
"""Generate the household office system from the table below.

An office is a post at court that a seated minister can be appointed to. It is NOT a trait:
the six original office traits (seneschal, master_of_coin, herald_of_arms,
marshal_of_the_court, court_chaplain, court_astrologer) could not overlap, because four of
them carried `allow = { NOT = { has_trait_category = cabinet } }` and so collided with the
minister's career trait. An office is instead:

  a country variable    cc_office_<key>_filled  plus cc_office_<key>_holder for the panel
  an auto_modifier      cc_office_<key>, applied while that variable is set
  an unlock advance     and usually an obsoleting advance
  an appointment path   one interaction plus one picker event

WHY AN AUTO_MODIFIER. Non-stacking is structural: an auto_modifier is a single named country
entry that is either applied or not, so nothing has to enforce "one seneschal's worth of
seneschal". `cc_cabinet_composition.txt` already uses the same shape.

WHY THE POTENTIAL_TRIGGER READS COUNTRY VARIABLES AND NOT CHARACTERS. The tempting trigger is
`any_character = { has_variable = cc_office_x  is_alive = yes }`, which would make death
cleanup free as well. Do not. potential_trigger is evaluated continuously for every real
country, and the mod's existing nine composition entries already perform 37
any_cabinet_character iterations; forty more would multiply that. Offices therefore read a
country variable, and vacating on death is explicit, hooked on on_cabinet_death and
on_cabinet_removed (both already hooked for the XP system).

WHY NO RELIGION OR CULTURE TRIGGER. Vanilla advances self-gate: inquisition_advance carries
`potential = { religion = religion:catholic }`, and the Phanariote advance carries
`culture = { has_culture_group = culture_group:greek_group }`. So `has_advance = X` already
implies the religion, culture or government that X requires, and restating it would be a
second place to keep in sync. The one consequence worth knowing: a realm that changes religion
keeps advances it already researched, so an ex-Catholic realm can retain a Grand Inquisitor.

SCALING. Each office's modifier scales with the holder's level, clamped to 1.0x-2.5x. Script
cannot dereference a character held in a variable, so the monthly pulse publishes each holder's
level into cc_office_<key>_level and scales_with reads that. Same shape as
cc_xp_publish_school_capacity.

Validation runs before anything is written, and any failure aborts without touching the
output. It checks that every advance named exists in the vanilla advance files, that every
modifier name exists in the vanilla modifier_type_definitions, that no office is unlocked and
obsoleted by the same advance, that the obsoleting advance is never in an earlier age than the
unlocking one, and that keys and names are unique.

    python tools/generate_offices.py
    python tools/generate_offices.py --check
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from game_paths import game_root

REPO = Path(__file__).resolve().parent.parent
GAME = Path(game_root())
ADVANCE_DIR = GAME / 'in_game' / 'common' / 'advances'
MODTYPE_DIR = GAME / 'main_menu' / 'common' / 'modifier_type_definitions'

OUT_AUTOMOD = REPO / 'in_game' / 'common' / 'auto_modifiers' / 'cc_offices.txt'
OUT_TRIGGERS = REPO / 'in_game' / 'common' / 'scripted_triggers' / 'cc_office_triggers.txt'
OUT_VALUES = REPO / 'in_game' / 'common' / 'script_values' / 'cc_office_values.txt'
OUT_EFFECTS = REPO / 'in_game' / 'common' / 'scripted_effects' / 'cc_office_generated.txt'
OUT_EVENTS = REPO / 'in_game' / 'events' / 'cc_office_events.txt'
OUT_LOC = REPO / 'in_game' / 'localization' / 'english' / 'cc_offices_l_english.yml'
OUT_GUI = REPO / 'in_game' / 'gui' / 'panels' / 'situation' / 'cc_office_household.gui'

# How many offices a court may hold at once. Any number may be UNLOCKED; this caps how many
# may be FILLED, which is what turns a wide roster into a choice.
SLOT_CAP = 6

# What each FILLED office costs in court upkeep, applied once per office held.
#
# This is a separate auto_modifier scaling on cc_office_filled_count rather than a
# court_spending_efficiency line inside every office's own modifier block, because each
# office's block is multiplied by its holder's level through scales_with. Putting the cost
# there would make a senior holder cost two and a half times as much to keep, which is the
# opposite of the intent: the household costs what it costs, and seniority buys more
# benefit for the same overhead.
#
# It is what stops filling all six slots from being free. A full household runs at -12%
# court spending efficiency against the cap of 6.
UPKEEP_PER_OFFICE = -0.02
UPKEEP_KEY = 'cc_office_household_upkeep'

# Appointment picker event. One event, options generated per office.
PICKER_EVENT = 'cc_office.1'
VACATED_EVENT = 'cc_office.2'
# The other direction: the Household tab's Appoint button on one office, offering the
# most senior eligible ministers as options.
PANEL_APPOINT_EVENT = 'cc_office.3'
PANEL_CANDIDATES = 4

# Tenure. Each year a holder has served adds this much to the office's scale, on top of
# the seniority scale and after its 2.5x clamp, up to TENURE_CAP_YEARS years.
TENURE_PER_YEAR = 0.02
TENURE_CAP_YEARS = 10

OUT_ACTIONS = REPO / 'in_game' / 'common' / 'generic_actions' / 'cc_office_actions.txt'

MODTYPES: dict = {}          # filled by main(); emit_loc renders values with it

TRACKS = {'adm', 'dip', 'mil'}
TRACK_NAMES = {'adm': 'administrative', 'dip': 'diplomatic', 'mil': 'military'}
FAMILIES = {'core', 'religion', 'government', 'culture', 'region'}

AGE_ORDER = ['age_1_traditions', 'age_2_renaissance', 'age_3_discovery',
             'age_4_reformation', 'age_5_absolutism', 'age_6_revolutions']


###############################################################################
# THE OFFICES
#
# key       identifier; drives every generated name (cc_office_<key>_filled, etc)
# name      English display name
# track     which XP track the appointee must have a tier in
# tier      how much of that track is required to be appointed
# family    core | religion | government | culture | region (documentation and panel grouping)
# unlock    advance that makes the office available; None means available from game start
# obsolete  advance that retires the office; None means it never retires
# mod       the auto_modifier body, before level scaling
# desc      loc description, one or two plain sentences
###############################################################################

OFFICES = [
    # ------------------------------------------------------------------ CORE ---
    dict(key='seneschal', name='Seneschal', track='adm', tier=1, family='core',
         unlock=None, obsolete='chancery_records',
         mod={'country_cabinet_efficiency': 0.32, 'court_spending_efficiency': 0.05,
              'nobles_estate_agenda_impact': 0.08},
         desc="Runs the household and the lord's own lands. Superseded once written chancery "
              "records make the office a clerical one."),
    dict(key='master_of_coin', name='Master of Coin', track='adm', tier=1, family='core',
         unlock=None, obsolete='standardized_coins',
         mod={'global_trade_center_power': 0.06, 'court_spending_efficiency': 0.08,
              'burghers_estate_agenda_impact': 0.08},
         desc="Keeps the treasure chest and pays the household's bills. Standardized coinage "
              "turns the post into a mint office."),
    dict(key='herald_of_arms', name='Herald of Arms', track='dip', tier=1, family='core',
         unlock=None, obsolete='diplomatic_training',
         mod={'diplomatic_reputation': 1, 'antagonism_received_modifier': -0.08,
              'diplomatic_capacity_modifier': 0.06},
         desc="Carries declarations, arranges precedence and knows every coat of arms at "
              "court. Trained diplomats make the herald ceremonial."),
    dict(key='marshal_of_the_court', name='Marshal of the Court', track='mil', tier=1,
         family='core', unlock=None, obsolete='absolutist_court',
         mod={'army_light_cavalry_build_cost_modifier': -0.08,
              'army_heavy_cavalry_build_cost_modifier': -0.05, 'land_morale': 0.05},
         desc="Commands the household guard and the stables. An absolutist court replaces him "
              "with a standing establishment."),
    dict(key='clerk_of_the_signet', name='Clerk of the Signet', track='adm', tier=1,
         family='core', unlock='educated_bureaucrats', obsolete='chancery_records',
         mod={'legislative_efficiency': 0.05, 'global_monthly_literacy': 0.005},
         desc="Keeps the ruler's private seal and drafts what it is put to. Absorbed into the "
              "chancery once records are kept systematically."),
    dict(key='keeper_of_the_wardrobe', name='Keeper of the Wardrobe', track='adm', tier=1,
         family='core', unlock='non_inheritable_offices', obsolete='absolutist_court',
         mod={'court_spending_efficiency': 0.10, 'monthly_prestige': 0.02},
         desc="Holds the household purse separately from the treasury, which is what makes it "
              "useful. The absolutist court folds it into the civil list."),
    dict(key='chancellor_of_the_rolls', name='Chancellor of the Rolls', track='adm', tier=2,
         family='core', unlock='chancery_records', obsolete='modern_bureaucracy',
         mod={'legislative_efficiency': 0.08, 'stability_cost_efficiency': 0.10,
              'country_cabinet_efficiency': 0.24},
         desc="Keeps the written record of every grant, charter and judgement the crown has "
              "made. A modern bureaucracy makes the rolls a department rather than a person."),
    dict(key='master_of_the_mint', name='Master of the Mint', track='adm', tier=2,
         family='core', unlock='standardized_coins', obsolete=None,
         mod={'global_trade_center_power': 0.08, 'court_spending_efficiency': 0.06},
         desc="Answers for the weight and fineness of the coin, and for what the crown makes "
              "by striking it."),
    dict(key='court_chamberlain', name='Court Chamberlain', track='adm', tier=2, family='core',
         unlock='regulate_court_procedures', obsolete=None,
         mod={'court_spending_efficiency': 0.12, 'crown_estate_agenda_impact': 0.08},
         desc="Controls access to the ruler and the order of the court day. Regulated "
              "procedure is what gives the office its power."),
    dict(key='master_of_protocol', name='Master of Protocol', track='dip', tier=2,
         family='core', unlock='diplomatic_training', obsolete=None,
         mod={'diplomatic_reputation': 1, 'monthly_diplomats': 0.05,
              'diplomatic_capacity_modifier': 0.08},
         desc="Settles precedence, form of address and the terms on which envoys are received."),
    dict(key='intendant', name='Intendant of the Household', track='adm', tier=3,
         family='core', unlock='absolutist_court', obsolete=None,
         mod={'global_crown_estate_power': 0.05, 'country_cabinet_efficiency': 0.4,
              'global_monthly_control': 0.02},
         desc="A crown servant rather than a courtier, answerable to the ruler alone. The post "
              "exists because the absolutist court no longer trusts hereditary officers."),
    dict(key='permanent_secretary', name='Permanent Secretary', track='adm', tier=3,
         family='core', unlock='modern_bureaucracy', obsolete=None,
         mod={'legislative_efficiency': 0.12, 'country_cabinet_efficiency': 0.4,
              'global_integration_speed_modifier': 0.05},
         desc="Stays in post while ministers come and go, which is the whole point of him."),
    dict(key='director_of_public_instruction', name='Director of Public Instruction',
         track='adm', tier=3, family='core', unlock='enlightened_court', obsolete=None,
         mod={'research_speed': 0.06, 'global_monthly_literacy': 0.015,
              'global_max_literacy': 3},
         desc="Answers for schools, academies and what the realm's subjects are taught."),

    # -------------------------------------------------------------- RELIGION ---
    dict(key='court_chaplain', name='Court Chaplain', track='adm', tier=1, family='religion',
         unlock=None, obsolete=None,
         mod={'global_pop_conversion_speed_modifier': 0.10, 'clergy_estate_agenda_impact': 0.08},
         desc="Says the household's offices and hears the ruler's confession."),
    dict(key='court_astrologer', name='Court Astrologer', track='adm', tier=1,
         family='religion', unlock=None, obsolete='enlightened_court',
         mod={'research_speed': 0.06, 'clergy_estate_agenda_impact': 0.05},
         desc="Reads the heavens for the timing of decisions. The enlightened court stops "
              "asking."),
    dict(key='grand_inquisitor', name='Grand Inquisitor', track='adm', tier=2,
         family='religion', unlock='inquisition_advance', obsolete=None,
         mod={'global_heretic_pop_conversion_speed_modifier': 0.15,
              'clergy_estate_agenda_impact': 0.08, 'stability_cost_efficiency': 0.05},
         desc="Answers for the orthodoxy of the realm's subjects, with the authority to act "
              "on it."),
    dict(key='ecclesiarch', name='Ecclesiarch of the Court', track='adm', tier=2,
         family='religion', unlock='church_guidance', obsolete=None,
         mod={'global_pop_conversion_speed_modifier': 0.08, 'monthly_legitimacy': 0.02,
              'clergy_estate_agenda_impact': 0.08},
         desc="Speaks for the church inside the palace, and for the palace inside the church."),
    dict(key='qadi_of_the_court', name='Qadi of the Court', track='adm', tier=2,
         family='religion', unlock='islamic_courts', obsolete=None,
         mod={'legislative_efficiency': 0.08, 'stability_cost_efficiency': 0.08,
              'clergy_estate_agenda_impact': 0.06},
         desc="Judges according to religious law in the ruler's presence."),
    dict(key='court_ulema', name='Court Ulema', track='adm', tier=3, family='religion',
         unlock='islamic_schoolars', obsolete=None,
         mod={'research_speed': 0.06, 'global_monthly_literacy': 0.01,
              'clergy_estate_agenda_impact': 0.06},
         desc="The learned men the ruler keeps at hand for questions of law and doctrine."),
    dict(key='court_pandit', name='Court Pandit', track='adm', tier=2, family='religion',
         unlock='astika_schools', obsolete=None,
         mod={'research_speed': 0.06, 'global_monthly_literacy': 0.01,
              'clergy_estate_agenda_impact': 0.06},
         desc="Keeps the scriptures and advises on the rites the court owes."),
    dict(key='sangha_preceptor', name='Sangha Preceptor', track='adm', tier=2,
         family='religion', unlock='buddhist_universities', obsolete=None,
         mod={'research_speed': 0.08, 'global_monthly_literacy': 0.01,
              'stability_cost_efficiency': 0.05},
         desc="The monastic teacher a ruler takes instruction from, and the link to the "
              "monasteries."),
    dict(key='consistory_superintendent', name='Consistory Superintendent', track='adm',
         tier=2, family='religion', unlock='protestant_administration_tax', obsolete=None,
         mod={'global_pop_conversion_speed_modifier': 0.08, 'court_spending_efficiency': 0.06,
              'clergy_estate_agenda_impact': 0.08},
         desc="Administers a church the crown has taken responsibility for, including its "
              "revenues."),
    dict(key='confessional_overseer', name='Overseer of the Confession', track='adm', tier=2,
         family='religion', unlock='confessional_court', obsolete=None,
         mod={'global_pop_conversion_speed_modifier': 0.10, 'stability_cost_efficiency': 0.06},
         desc="Answers for the court professing one faith and being seen to."),

    # ------------------------------------------------------------ GOVERNMENT ---
    dict(key='steward_of_the_demesne', name='Steward of the Demesne', track='adm', tier=2,
         family='government', unlock='local_nobility', obsolete=None,
         mod={'global_crown_estate_power': 0.04, 'nobles_estate_agenda_impact': 0.10},
         desc="Manages the crown's own estates and the nobles who hold from them."),
    dict(key='constable', name='Constable', track='mil', tier=2, family='government',
         unlock='noble_officers', obsolete=None,
         mod={'land_morale': 0.06, 'discipline': 0.02, 'nobles_estate_agenda_impact': 0.06},
         desc="Commands in the ruler's name and answers for the conduct of noble officers."),
    dict(key='consul_of_merchants', name='Consul of Merchants', track='dip', tier=2,
         family='government', unlock='free_merchants', obsolete=None,
         mod={'global_trade_center_power': 0.08, 'burghers_estate_agenda_impact': 0.10},
         desc="Speaks for the trading houses in council, and for the council to them."),
    dict(key='chancellor_of_the_see', name='Chancellor of the See', track='adm', tier=2,
         family='government', unlock='state_of_clerics', obsolete=None,
         mod={'legislative_efficiency': 0.08, 'clergy_estate_agenda_impact': 0.10,
              'monthly_legitimacy': 0.02},
         desc="Runs the secular administration of a state whose ruler is a churchman."),
    dict(key='keeper_of_the_kurultai', name='Keeper of the Kurultai', track='mil', tier=2,
         family='government', unlock='kurultai_advance', obsolete=None,
         mod={'land_morale': 0.05, 'nobles_estate_agenda_impact': 0.10,
              'monthly_legitimacy': 0.02},
         desc="Summons the assembly, keeps its precedents and counts its voices."),
    dict(key='master_of_the_yam', name='Master of the Yam', track='dip', tier=2,
         family='government', unlock='yams_of_the_great_khan', obsolete=None,
         mod={'diplomatic_range_modifier': 0.15, 'global_monthly_control': 0.02,
              'monthly_diplomats': 0.05},
         desc="Runs the relay stations, which is how a horde the size of a continent stays "
              "one thing."),

    # --------------------------------------------------------------- CULTURE ---
    dict(key='phanariote_secretary', name='Phanariote Secretary', track='dip', tier=2,
         family='culture', unlock='greek_group_the_phanariote_network_advance', obsolete=None,
         mod={'diplomatic_reputation': 1, 'monthly_diplomats': 0.05,
              'global_burghers_max_literacy': 5},
         desc="A Greek administrator of the kind every chancery in the east ends up hiring."),
    dict(key='hansa_factor', name='Hansa Factor', track='dip', tier=2, family='culture',
         unlock='north_german_hanseatic_traditions', obsolete=None,
         mod={'global_trade_center_power': 0.08, 'global_trade_protection_factor': 0.10},
         desc="Holds the court's interest in the league's counting houses abroad."),
    dict(key='postelnic', name='Postelnic', track='dip', tier=2, family='culture',
         unlock='romanian_the_postelnic_bureaucracy', obsolete=None,
         mod={'diplomatic_reputation': 1, 'antagonism_received_modifier': -0.08,
              'country_cabinet_efficiency': 0.24},
         desc="Chamberlain and foreign secretary in one post, which is how the voivode's court "
              "was actually run."),
    dict(key='voivode_of_the_court', name='Voivode of the Court', track='mil', tier=2,
         family='culture', unlock='voivode_advance', obsolete=None,
         mod={'land_morale': 0.05, 'global_monthly_control': 0.02,
              'nobles_estate_agenda_impact': 0.06},
         desc="Holds military and civil authority together in the ruler's name."),
    dict(key='herald_of_the_table_of_ranks', name='Herald of the Table of Ranks', track='adm',
         tier=3, family='culture', unlock='table_of_ranks', obsolete=None,
         mod={'country_cabinet_efficiency': 0.4, 'nobles_estate_agenda_impact': 0.08,
              'legislative_efficiency': 0.06},
         desc="Decides where every servant of the state stands, which is a great deal of power "
              "for a clerk."),
    dict(key='state_inquisitor', name='State Inquisitor', track='dip', tier=3,
         family='culture', unlock='ven_state_inquisition', obsolete=None,
         mod={'stability_cost_efficiency': 0.10, 'antagonism_received_modifier': -0.06,
              'global_monthly_control': 0.02},
         desc="Watches the republic's own servants. Reports to the council and to nobody else."),
    dict(key='priori_of_the_council', name='Priore of the Council', track='adm', tier=2,
         family='culture', unlock='sie_council_priori', obsolete=None,
         mod={'burghers_estate_agenda_impact': 0.10, 'legislative_efficiency': 0.06,
              'monthly_legitimacy': 0.02},
         desc="Sits for a short term, by rotation, and the shortness is the safeguard."),
    dict(key='jokamachi_warden', name='Warden of the Castle Town', track='adm', tier=2,
         family='culture', unlock='jap_jokamachi', obsolete=None,
         mod={'global_monthly_urban_control': 0.03, 'burghers_estate_agenda_impact': 0.08,
              'global_trade_center_power': 0.05},
         desc="Governs the town that has grown up under the castle walls."),
    dict(key='master_of_siege_works', name='Master of Siege Works', track='mil', tier=2,
         family='culture', unlock='chinese_siege_engineers', obsolete=None,
         mod={'siege_ability': 0.10, 'court_spending_efficiency': 0.04},
         desc="Keeps the engineers and their drawings between wars, which is when they are "
              "actually made."),

    # ---------------------------------------------------------------- REGION ---
    dict(key='keeper_of_the_wampum', name='Keeper of the Wampum', track='dip', tier=1,
         family='region', unlock='wampum', obsolete=None,
         mod={'diplomatic_reputation': 1, 'antagonism_received_modifier': -0.10},
         desc="Holds the belts in which every agreement the people have made is recorded."),
    dict(key='speaker_of_the_elders', name='Speaker of the Elders', track='adm', tier=1,
         family='region', unlock='council_of_elders', obsolete=None,
         mod={'stability_cost_efficiency': 0.10, 'monthly_legitimacy': 0.02},
         desc="Carries the council's decision and is answerable for having carried it "
              "faithfully."),
    dict(key='keeper_of_regnal_chronicles', name='Keeper of the Chronicles', track='adm',
         tier=1, family='region', unlock='regnal_chronicles', obsolete=None,
         mod={'monthly_prestige': 0.03, 'monthly_legitimacy': 0.02,
              'global_monthly_literacy': 0.005},
         desc="Keeps the list of rulers and what each is to be remembered for."),
    dict(key='master_of_the_silk_road', name='Master of the Road', track='dip', tier=2,
         family='region', unlock='silk_road', obsolete=None,
         mod={'global_trade_center_power': 0.08, 'trade_range_modifier': 0.10,
              'diplomatic_range_modifier': 0.10},
         desc="Answers for the caravans, the tolls they pay and the escorts they are owed."),
    dict(key='master_of_ceremonies', name='Master of Ceremonies', track='dip', tier=2,
         family='region', unlock='courtly_competition', obsolete=None,
         mod={'monthly_prestige': 0.04, 'diplomatic_reputation': 1,
              'nobles_estate_agenda_impact': 0.06},
         desc="Stages the court's contests and displays, on which a good deal of its standing "
              "rests."),
]


###############################################################################
# LOADERS
###############################################################################

def load_advances() -> dict:
    """name -> {age, gate}, read from the vanilla advance files.

    `gate` is the advance's own `potential` restriction, flattened to a short string. It is
    what makes restating religion or culture on the office unnecessary: an advance that
    requires Catholicism gates the office that unlocks from it.
    """
    out = {}
    for path in sorted(ADVANCE_DIR.glob('*.txt')):
        fn = path.name
        lines = path.read_text(encoding='utf-8-sig', errors='replace').split('\n')
        i = 0
        while i < len(lines):
            # \s* around the '=' is load-bearing. Vanilla is not consistent about
            # spacing: medieval_administration, government_size_renaissance and four
            # more of the government-size spine are written `name  = {` with two
            # spaces, and a strict ' = ' would leave them out of the index, so a
            # perfectly valid advance name would fail validation.
            m = re.match(r'^([a-zA-Z_0-9]+)\s*=\s*\{', lines[i])
            if m:
                depth, body, j = 0, [], i
                while j < len(lines):
                    depth += lines[j].count('{') - lines[j].count('}')
                    body.append(lines[j])
                    j += 1
                    if depth <= 0:
                        break
                b = '\n'.join(body)
                age = re.search(r'age = (age_\d_\w+)', b)
                gates = re.findall(
                    r'religion(?:\.group)? = (?:religion(?:_group)?:)?(\w+)'
                    r'|has_culture_group = culture_group:(\w+)'
                    r'|is_(protestant) = yes', b)
                flat = [g for tup in gates for g in tup if g]
                if not flat and fn.startswith(('government_', 'region_', 'culture_')):
                    flat = [fn[:-4]]
                out[m.group(1)] = dict(age=age.group(1) if age else None,
                                       gate='/'.join(sorted(set(flat))) or '')
                i = j
            else:
                i += 1
    return out


def load_modifier_types() -> dict:
    """name -> {percent, already_percent, bad}, so a value can be rendered the way the
    engine would render it.

    `percent = yes` means the stored value is a fraction to show as a percentage (0.08 is
    8%). `already_percent = yes` means it is already in percent units and is shown as is.
    `color = bad` inverts what a positive number means, which is why
    army_light_cavalry_build_cost_modifier = -0.08 is a GOOD thing and must not be
    coloured red.
    """
    out: dict = {}
    for path in sorted(MODTYPE_DIR.glob('*.txt')):
        txt = path.read_text(encoding='utf-8-sig', errors='replace')
        lines = txt.split('\n')
        i = 0
        while i < len(lines):
            # Same spacing caution as load_advances:
            # global_bureaucracy_maintenance_efficiency is declared as `name = {`.
            m = re.match(r'^([a-z_0-9]+)\s*=\s*\{', lines[i])
            if m:
                depth, body, j = 0, [], i
                while j < len(lines):
                    depth += lines[j].count('{') - lines[j].count('}')
                    body.append(lines[j])
                    j += 1
                    if depth <= 0:
                        break
                b = '\n'.join(body)
                out[m.group(1)] = dict(
                    percent=bool(re.search(r'\bpercent\s*=\s*yes', b)),
                    already_percent=bool(re.search(r'\balready_percent\s*=\s*yes', b)),
                    bad=bool(re.search(r'\bcolor\s*=\s*bad', b)))
                i = j
            else:
                i += 1
    return out


def format_modifier(name: str, value, modtypes: dict) -> str:
    """One modifier as the player will read it, coloured by whether it is good for them.

    #G / #R are the engine's green and red; the closing #! is required or the colour
    bleeds into everything after it.
    """
    meta = modtypes.get(name, {})
    if meta.get('percent'):
        shown = value * 100
        text = f'{shown:+.10g}%'
    elif meta.get('already_percent'):
        text = f'{value:+.10g}%'
    else:
        text = f'{value:+.10g}'
    beneficial = (value < 0) if meta.get('bad') else (value > 0)
    colour = 'G' if beneficial else 'R'
    return f"[ShowModifierTypeName('{name}')]: #{colour} {text}#!"


def format_modifier_scaled(name: str, value, modtypes: dict, scale_expr: str) -> str:
    """One modifier at its CURRENT strength: base x the office's published scale, computed
    in GUI with Multiply_CFixedPoint. The format code signs and colours it the way the
    engine would: `+=` is green when positive, `-=` green when negative (color = bad
    modifier types, where a negative number is the good direction). `%` renders a fraction
    as a percentage."""
    meta = modtypes.get(name, {})
    sign = '-=' if meta.get('bad') else '+='
    product = f"Multiply_CFixedPoint({scale_expr}, '(CFixedPoint){value:.10g}')"
    if meta.get('percent'):
        shown = f'[{product}|{sign}1%]'
    elif meta.get('already_percent'):
        shown = f'[{product}|{sign}1]%'
    else:
        shown = f'[{product}|{sign}2]'
    return f"[ShowModifierTypeName('{name}')]: {shown}"


###############################################################################
# VALIDATION
###############################################################################

def validate(advances: dict, modtypes: set) -> list:
    errs = []
    seen_keys, seen_names = set(), set()

    for o in OFFICES:
        k = o['key']
        if k in seen_keys:
            errs.append(f'duplicate office key: {k}')
        seen_keys.add(k)
        if o['name'] in seen_names:
            errs.append(f'duplicate office name: {o["name"]}')
        seen_names.add(o['name'])

        if o['track'] not in TRACKS:
            errs.append(f'{k}: unknown track {o["track"]}')
        if not 1 <= o['tier'] <= 3:
            errs.append(f'{k}: tier {o["tier"]} out of range 1-3')
        if o['family'] not in FAMILIES:
            errs.append(f'{k}: unknown family {o["family"]}')
        if not o.get('desc'):
            errs.append(f'{k}: no desc')

        for field in ('unlock', 'obsolete'):
            adv = o[field]
            if adv is not None and adv not in advances:
                errs.append(f'{k}: {field} advance does not exist in vanilla: {adv}')

        if o['unlock'] and o['unlock'] == o['obsolete']:
            errs.append(f'{k}: unlocked and obsoleted by the same advance')

        if o['unlock'] and o['obsolete']:
            au = advances.get(o['unlock'], {}).get('age')
            ao = advances.get(o['obsolete'], {}).get('age')
            if au in AGE_ORDER and ao in AGE_ORDER and AGE_ORDER.index(ao) < AGE_ORDER.index(au):
                errs.append(f'{k}: obsoleted in {ao}, which is before its unlock in {au}')

        if not o['mod']:
            errs.append(f'{k}: empty modifier block')
        for mname in o['mod']:
            if mname not in modtypes:
                errs.append(f'{k}: modifier does not exist in vanilla: {mname}')

    return errs


# Archetype courts used for the coverage report. A gate string from load_advances() counts
# for an archetype if any of the archetype's tokens appears in it. Counting every office in
# every age would be meaningless, because no country is Catholic and Muslim at once.
ARCHETYPES = {
    'Catholic monarchy (French)': ['catholic', 'government_monarchy'],
    'Orthodox Greek monarchy': ['orthodox', 'greek_group', 'government_monarchy'],
    'Sunni sultanate': ['muslim', 'sunni', 'government_monarchy'],
    'Italian republic (Tuscan)': ['catholic', 'government_republic', 'culture_tuscan'],
    'Steppe horde': ['government_steppe_horde', 'region_asia'],
    'Hindu kingdom': ['hindu', 'dharmic', 'government_monarchy', 'region_asia'],
    'Haudenosaunee': ['region_north_america'],
    'West African monarchy': ['muslim', 'region_africa', 'government_monarchy'],
}


def office_age(o: dict, advances: dict, field: str):
    adv = o[field]
    if not adv:
        return AGE_ORDER[0] if field == 'unlock' else None
    age = advances.get(adv, {}).get('age')
    return age if age in AGE_ORDER else AGE_ORDER[0]


def coverage(advances: dict) -> dict:
    """Offices available per age, per archetype court.

    This is the sanity check behind the 3-6 target. An office counts for an archetype only
    if the gate its unlocking advance carries is one that archetype could satisfy.
    """
    out = {}
    for label, tokens in ARCHETYPES.items():
        row = []
        for i, age in enumerate(AGE_ORDER):
            n = 0
            for o in OFFICES:
                gate = advances.get(o['unlock'], {}).get('gate', '') if o['unlock'] else ''
                if gate and not any(t in gate for t in tokens):
                    continue
                au = office_age(o, advances, 'unlock')
                ao = office_age(o, advances, 'obsolete')
                if AGE_ORDER.index(au) > i:
                    continue
                if ao and AGE_ORDER.index(ao) <= i:
                    continue
                n += 1
            row.append(n)
        out[label] = row
    return out


###############################################################################
# EMITTERS
###############################################################################

BOM = '\ufeff'
BANNER = ('# GENERATED FILE. Do not edit by hand.\n'
          '#   python tools/generate_offices.py\n'
          '#\n'
          '# Household offices. See the docstring in the generator for why offices are\n'
          '# auto_modifiers keyed on country variables rather than traits.\n')


def emit_auto_modifiers() -> str:
    out = [BOM, BANNER, '\n']
    for o in OFFICES:
        k = o['key']
        out.append(f'# {o["name"]} [{o["family"]}] {o["track"]} tier {o["tier"]}\n')
        out.append(f'cc_office_{k} = {{\n')
        out.append('\trequires_real = yes\n\n')
        out.append('\tpotential_trigger = {\n')
        out.append(f'\t\thas_variable = cc_office_{k}_filled\n')
        if o['unlock']:
            out.append(f'\t\thas_advance = {o["unlock"]}\n')
        if o['obsolete']:
            out.append(f'\t\tNOT = {{ has_advance = {o["obsolete"]} }}\n')
        out.append('\t}\n\n')
        out.append(f'\tscales_with = {{ value = cc_office_{k}_scale }}\n\n')
        for mname, mval in o['mod'].items():
            out.append(f'\t{mname} = {mval}\n')
        out.append('}\n\n')

    out.append('# Household upkeep. One entry scaling on how many offices are filled, rather\n'
               '# than a cost line inside each office, because an office block is multiplied by\n'
               "# its holder's level and the overhead should not be.\n")
    out.append(f'{UPKEEP_KEY} = {{\n')
    out.append('\trequires_real = yes\n\n')
    out.append('\tpotential_trigger = {\n')
    out.append('\t\tcc_office_filled_count > 0\n')
    out.append('\t}\n\n')
    out.append('\tscales_with = { value = cc_office_filled_count }\n\n')
    out.append(f'\tcourt_spending_efficiency = {UPKEEP_PER_OFFICE}\n')
    out.append('}\n')
    return ''.join(out)


def emit_triggers() -> str:
    out = [BOM, BANNER,
           '#\n'
           '# _exists and _vacant are COUNTRY scope. cc_office_holds_any is CHARACTER scope.\n\n']
    for o in OFFICES:
        k = o['key']
        out.append(f'# {o["name"]}: does this country have the office at all?\n')
        out.append(f'cc_office_{k}_exists = {{\n')
        if o['unlock']:
            out.append(f'\thas_advance = {o["unlock"]}\n')
        if o['obsolete']:
            out.append(f'\tNOT = {{ has_advance = {o["obsolete"]} }}\n')
        if not o['unlock'] and not o['obsolete']:
            out.append('\talways = yes\n')
        out.append('}\n\n')
        out.append(f'# {o["name"]}: available and nobody holds it.\n')
        out.append(f'cc_office_{k}_vacant = {{\n')
        out.append(f'\tcc_office_{k}_exists = yes\n')
        out.append(f'\tNOT = {{ has_variable = cc_office_{k}_filled }}\n')
        out.append('}\n\n')

    out.append('# CHARACTER scope. One minister holds at most one office, otherwise a single\n'
               '# tier-3 star would occupy every slot in the household.\n')
    out.append('cc_office_holds_any = {\n\tOR = {\n')
    for o in OFFICES:
        out.append(f'\t\thas_variable = cc_office_held_{o["key"]}\n')
    out.append('\t}\n}\n\n')

    out.append('# COUNTRY scope. Is there any post at all standing open right now?\n')
    out.append('cc_office_any_vacant = {\n\tOR = {\n')
    for o in OFFICES:
        out.append(f'\t\tcc_office_{o["key"]}_vacant = yes\n')
    out.append('\t}\n}\n\n')

    out.append('# CHARACTER scope. Deliberately coarse: seated, alive, not already posted, and\n'
               '# trained in something. Whether a SPECIFIC office suits them is checked on that\n'
               "# office's option in the picker, because the answer depends on the office. A\n"
               '# minister who qualifies for nothing still opens the picker and is told so,\n'
               '# which reads better than a dead button with no explanation.\n')
    out.append('cc_office_can_be_appointed = {\n')
    out.append('\tin_cabinet = yes\n')
    out.append('\tis_alive = yes\n')
    out.append('\tNOT = { cc_office_holds_any = yes }\n')
    out.append('\tOR = {\n')
    for t in sorted(TRACKS):
        out.append(f'\t\tcc_xp_tier_at_least = {{ TRACK = {t}  TIER = 1 }}\n')
    out.append('\t}\n}\n')
    return ''.join(out)


def emit_values() -> str:
    out = [BOM, BANNER,
           '#\n'
           '# One scale value per office. Reads the level the monthly pulse published into\n'
           f'# cc_office_<key>_level and maps 1-10 onto 1.0x-2.5x. An office with no level\n'
           '# published yet reads as 1.0x rather than 0, which is why the base value is 1.\n\n']
    for o in OFFICES:
        k = o['key']
        out.append(f'cc_office_{k}_scale = {{\n')
        out.append('\tvalue = 1\n')
        out.append('\tif = {\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_{k}_level }}\n')
        out.append('\t\tadd = {\n')
        out.append(f'\t\t\tvalue = var:cc_office_{k}_level\n')
        out.append('\t\t\tsubtract = 1\n')
        out.append('\t\t\tmultiply = 0.1667\n')
        out.append('\t\t}\n')
        out.append('\t}\n')
        out.append('\tmin = 1\n')
        out.append('\tmax = 2.5\n')
        # Tenure on top of seniority, applied after the clamp so seniority still tops out
        # at 2.5x and long service is a separate, smaller reward.
        out.append('\tif = {\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_{k}_since }}\n')
        out.append('\t\tmultiply = {\n')
        out.append('\t\t\tvalue = current_year\n')
        out.append(f'\t\t\tsubtract = var:cc_office_{k}_since\n')
        out.append(f'\t\t\tmin = 0\n\t\t\tmax = {TENURE_CAP_YEARS}\n')
        out.append(f'\t\t\tmultiply = {TENURE_PER_YEAR}\n')
        out.append('\t\t\tadd = 1\n')
        out.append('\t\t}\n')
        out.append('\t}\n')
        out.append('}\n\n')

    out.append('# How many offices this court currently holds, against the cap of '
               f'{SLOT_CAP}.\n')
    out.append('cc_office_filled_count = {\n\tvalue = 0\n')
    for o in OFFICES:
        out.append('\tif = {\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_{o["key"]}_filled }}\n')
        out.append('\t\tadd = 1\n')
        out.append('\t}\n')
    out.append('}\n\n')
    out.append(f'cc_office_slot_cap = {{\n\tvalue = {SLOT_CAP}\n}}\n')
    return ''.join(out)


def emit_effects() -> str:
    out = [BOM, BANNER,
           '#\n'
           '# The appoint and vacate effects are parameterised on $OFFICE$ rather than\n'
           '# generated forty-three times, because Clausewitz substitutes parameters inside\n'
           '# variable names (cc_bond_aor_effects.txt:34 does the same thing).\n'
           '#\n'
           '# WHICH SIDE HOLDS WHAT. The country holds cc_office_<key>_filled (the office is\n'
           '# occupied), cc_office_<key>_level (published for scales_with) and\n'
           '# cc_office_<key>_holder. That last one exists ONLY so the panel can print a name:\n'
           '# GUI can dereference a character held in a variable and script cannot. Nothing in\n'
           '# this file reads it. The holder instead carries cc_office_held_<key>, so every\n'
           '# lookup is an iteration filtered by a flag, which is the same shape mentorship,\n'
           '# patronage, schools and secondment already use.\n'
           '#\n'
           '# All effects here run in COUNTRY scope.\n\n']

    out.append('''# scope:office_holder = the minister being appointed.
cc_office_appoint = {
\tsave_scope_as = cc_office_court

\tset_variable = { name = cc_office_$OFFICE$_filled  value = yes }
\tset_variable = { name = cc_office_$OFFICE$_holder  value = scope:office_holder }

\tscope:office_holder = {
\t\tset_variable = { name = cc_office_held_$OFFICE$  value = yes }
\t}

\t# Tenure starts now. Read by the office's scale value and published for the panel.
\tset_variable = { name = cc_office_$OFFICE$_since  value = current_year }

\tcc_office_publish_levels = yes
}

# Ends the office and clears the holder's flag. The every_character sweep is affordable
# because vacating is rare: it happens on an advance retiring the office, or when the
# holder dies or leaves the cabinet, never on an ordinary tick.
cc_office_vacate = {
\tevery_character = {
\t\tlimit = { has_variable = cc_office_held_$OFFICE$ }
\t\tremove_variable = cc_office_held_$OFFICE$
\t}

\tif = {
\t\tlimit = { has_variable = cc_office_$OFFICE$_filled }
\t\tremove_variable = cc_office_$OFFICE$_filled
\t}
\tif = {
\t\tlimit = { has_variable = cc_office_$OFFICE$_holder }
\t\tremove_variable = cc_office_$OFFICE$_holder
\t}
\tif = {
\t\tlimit = { has_variable = cc_office_$OFFICE$_level }
\t\tremove_variable = cc_office_$OFFICE$_level
\t}
\tif = {
\t\tlimit = { has_variable = cc_office_$OFFICE$_since }
\t\tremove_variable = cc_office_$OFFICE$_since
\t}
}

''')

    out.append('# Publishes every holder\'s level so scales_with can read it. ONE pass over the\n'
               '# cabinet, not one per office: the inner ifs are variable checks on a character\n'
               '# already in scope, which is far cheaper than 43 separate iterations.\n'
               '#\n'
               '# cc_level (not cc_xp_level) is the 1-10 seniority variable; see the contract\n'
               '# in cc_xp_effects.txt.\n')
    out.append('cc_office_publish_levels = {\n')
    out.append('\tsave_scope_as = cc_office_court\n\n')
    out.append('\tevery_cabinet_character = {\n')
    out.append('\t\tlimit = {\n\t\t\tin_cabinet = yes\n\t\t\tis_alive = yes\n')
    out.append('\t\t\thas_variable = cc_level\n\t\t\tcc_office_holds_any = yes\n\t\t}\n')
    out.append('\t\tsave_scope_as = cc_office_seen\n\n')
    for o in OFFICES:
        k = o['key']
        out.append('\t\tif = {\n')
        out.append(f'\t\t\tlimit = {{ has_variable = cc_office_held_{k} }}\n')
        out.append('\t\t\tscope:cc_office_court = {\n')
        out.append('\t\t\t\tset_variable = {\n')
        out.append(f'\t\t\t\t\tname = cc_office_{k}_level\n')
        out.append('\t\t\t\t\tvalue = scope:cc_office_seen.var:cc_level\n')
        out.append('\t\t\t\t}\n')
        out.append('\t\t\t}\n')
        out.append('\t\t}\n')
    out.append('\t}\n}\n\n')

    out.append('# An advance retired one or more offices. Country-level checks only, no\n'
               '# character iteration, so this is cheap enough to run on the monthly pulse.\n'
               '# Fires the notification once if anything was actually wound up.\n')
    out.append('cc_office_retire_obsolete = {\n')
    out.append('\tset_variable = { name = cc_office_retired_any  value = 0 }\n\n')
    for o in OFFICES:
        if not o['obsolete'] and o['unlock'] is None:
            continue
        k = o['key']
        out.append('\tif = {\n')
        out.append('\t\tlimit = {\n')
        out.append(f'\t\t\thas_variable = cc_office_{k}_filled\n')
        out.append(f'\t\t\tNOT = {{ cc_office_{k}_exists = yes }}\n')
        out.append('\t\t}\n')
        out.append(f'\t\tcc_office_vacate = {{ OFFICE = {k} }}\n')
        out.append('\t\tchange_variable = { name = cc_office_retired_any  add = 1 }\n')
        out.append('\t}\n')
    out.append('\n\tif = {\n')
    out.append('\t\tlimit = {\n')
    out.append('\t\t\tis_ai = no\n')
    out.append('\t\t\thas_variable = cc_office_retired_any\n')
    out.append('\t\t\tvar:cc_office_retired_any > 0\n')
    out.append('\t\t}\n')
    out.append(f'\t\ttrigger_event_silently = {{ id = {VACATED_EVENT} }}\n')
    out.append('\t}\n')
    out.append('\tremove_variable = cc_office_retired_any\n')
    out.append('}\n\n')

    out.append('# Publishes which offices are open, for the Household panel tab ONLY.\n'
               '#\n'
               '# The panel cannot work this out for itself. GUI can dereference a character\n'
               '# held in a variable, but it has no way to ask whether a NAMED advance has been\n'
               '# researched: IsResearched exists only on an AdvanceItem handed out by the\n'
               "# advances screen's own datamodel, and there is no by-key lookup. So the roster\n"
               '# has to be pushed out as country variables the panel can test with IsSet.\n'
               '#\n'
               '# Human courts only. No panel ever renders an AI household, and this is the one\n'
               '# effect here that exists purely to feed the UI.\n')
    out.append('cc_office_publish_roster = {\n')
    for o in OFFICES:
        k = o['key']
        out.append('\tif = {\n')
        out.append('\t\tlimit = {\n')
        out.append(f'\t\t\tcc_office_{k}_vacant = yes\n')
        out.append('\t\t}\n')
        out.append(f'\t\tset_variable = {{ name = cc_office_{k}_open  value = yes }}\n')
        out.append('\t}\n')
        out.append('\telse_if = {\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_{k}_open }}\n')
        out.append(f'\t\tremove_variable = cc_office_{k}_open\n')
        out.append('\t}\n')

        # Held: the scale the office is running at and the years served, for the card.
        out.append('\tif = {\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_{k}_filled }}\n')
        out.append(f'\t\tset_variable = {{ name = cc_office_{k}_scale_var  value = cc_office_{k}_scale }}\n')
        out.append('\t\tif = {\n')
        out.append(f'\t\t\tlimit = {{ NOT = {{ has_variable = cc_office_{k}_since }} }}\n')
        out.append('\t\t\t# Held since before tenure existed: count from now.\n')
        out.append(f'\t\t\tset_variable = {{ name = cc_office_{k}_since  value = current_year }}\n')
        out.append('\t\t}\n')
        out.append('\t\tset_variable = {\n')
        out.append(f'\t\t\tname = cc_office_{k}_tenure\n')
        out.append(f'\t\t\tvalue = {{ value = current_year  subtract = var:cc_office_{k}_since  min = 0 }}\n')
        out.append('\t\t}\n')
        out.append('\t}\n')
        out.append('\telse = {\n')
        out.append(f'\t\tremove_variable = cc_office_{k}_scale_var\n')
        out.append(f'\t\tremove_variable = cc_office_{k}_tenure\n')
        out.append('\t}\n')

        # Locked, but the advance that opens it can be researched now.
        if o['unlock']:
            out.append('\tif = {\n')
            out.append('\t\tlimit = {\n')
            out.append(f'\t\t\tNOT = {{ has_advance = {o["unlock"]} }}\n')
            out.append(f'\t\t\tcan_research_advance = {o["unlock"]}\n')
            if o['obsolete']:
                out.append(f'\t\t\tNOT = {{ has_advance = {o["obsolete"]} }}\n')
            out.append('\t\t}\n')
            out.append(f'\t\tset_variable = {{ name = cc_office_{k}_soon  value = yes }}\n')
            out.append('\t}\n')
            out.append(f'\telse = {{ remove_variable = cc_office_{k}_soon }}\n')

        # Open or held, and the advance that retires it can be researched now.
        if o['obsolete']:
            out.append('\tif = {\n')
            out.append('\t\tlimit = {\n')
            out.append(f'\t\t\tcc_office_{k}_exists = yes\n')
            out.append(f'\t\t\tcan_research_advance = {o["obsolete"]}\n')
            out.append('\t\t}\n')
            out.append(f'\t\tset_variable = {{ name = cc_office_{k}_retiring  value = yes }}\n')
            out.append('\t}\n')
            out.append(f'\telse = {{ remove_variable = cc_office_{k}_retiring }}\n')
    out.append('\n\t# The panel prints a count against the cap. GUI reads variables, not\n')
    out.append('\t# script values, so the count has to be materialised here.\n')
    out.append('\tset_variable = { name = cc_office_filled_var  value = cc_office_filled_count }\n')
    out.append('}\n\n')

    out.append('# scope:target = a minister who has just died or left the cabinet. Exact, and\n'
               '# reached only from on_cabinet_death / on_cabinet_removed, so no iteration is\n'
               '# needed to work out which office (if any) they held.\n')
    out.append('cc_office_on_holder_left = {\n')
    for o in OFFICES:
        k = o['key']
        out.append('\tif = {\n')
        out.append(f'\t\tlimit = {{ scope:target ?= {{ has_variable = cc_office_held_{k} }} }}\n')
        out.append(f'\t\tcc_office_vacate = {{ OFFICE = {k} }}\n')
        out.append('\t}\n')
    out.append('}\n\n')

    out.append('# Save migration. Converts a minister still holding one of the six original\n'
               '# office traits into the matching office and removes the trait.\n'
               '#\n'
               '# COUNTRY scope, so it cannot live in cc_xp_init (character scope) the way\n'
               '# cc_xp_ladder_backfill does. It is called from cc_office_monthly behind the\n'
               '# cc_office_migrated flag instead, which runs on the first monthly tick after a\n'
               '# save is loaded. on_game_start would be wrong for the same reason it was wrong\n'
               '# for the ladder backfill: it does not run when an existing save is loaded.\n'
               '#\n'
               '# The six traits are kept as always = no shells in cc_age_traits.txt purely so\n'
               '# this can read and remove them. See the header there.\n')
    out.append('cc_office_backfill = {\n')
    for k in ('seneschal', 'master_of_coin', 'herald_of_arms', 'marshal_of_the_court',
              'court_chaplain', 'court_astrologer'):
        out.append('\tif = {\n')
        out.append('\t\tlimit = {\n')
        out.append(f'\t\t\tany_cabinet_character = {{ in_cabinet = yes  has_trait = {k} }}\n')
        out.append(f'\t\t\tcc_office_{k}_vacant = yes\n')
        out.append('\t\t}\n')
        out.append('\t\trandom_cabinet_character = {\n')
        out.append(f'\t\t\tlimit = {{ in_cabinet = yes  has_trait = {k} }}\n')
        out.append(f'\t\t\tremove_trait = trait:{k}\n')
        out.append('\t\t\tsave_scope_as = office_holder\n')
        out.append('\t\t}\n')
        out.append(f'\t\tcc_office_appoint = {{ OFFICE = {k} }}\n')
        out.append('\t}\n')
    out.append('}\n\n')

    # ---- Appointing from the Household tab ----
    out.append('# APPOINTING FROM THE HOUSEHOLD TAB. Each office\'s Appoint button flags it with\n'
               '# cc_office_panel_<key> and fires ' + PANEL_APPOINT_EVENT + ', whose options are the\n'
               '# most senior ministers eligible for THAT office. A panel button cannot hand an\n'
               '# action a character, so the candidates are offered as options instead, the same\n'
               '# shape as Take On a Protege and Sell a Work. These resolve the flagged office.\n\n')
    out.append('cc_office_panel_clear = {\n')
    for o in OFFICES:
        out.append(f'\tremove_variable = cc_office_panel_{o["key"]}\n')
    out.append('}\n\n')

    out.append('# Saves up to ' + str(PANEL_CANDIDATES) + ' candidates as scope:cc_office_cand_1..N,'
               ' most senior first.\n')
    out.append('cc_office_panel_save_candidates = {\n')
    for i in range(1, PANEL_CANDIDATES + 1):
        out.append(f'\tclear_saved_scope = cc_office_cand_{i}\n')
    for idx, o in enumerate(OFFICES):
        k = o['key']
        kw = 'if' if idx == 0 else 'else_if'
        out.append(f'\t{kw} = {{\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_panel_{k} }}\n')
        for i in range(PANEL_CANDIDATES):
            out.append('\t\tordered_cabinet_character = {\n')
            out.append('\t\t\tlimit = {\n')
            out.append('\t\t\t\tcc_office_can_be_appointed = yes\n')
            out.append(f'\t\t\t\tcc_xp_tier_at_least = {{ TRACK = {o["track"]}  TIER = {o["tier"]} }}\n')
            out.append('\t\t\t}\n')
            out.append('\t\t\torder_by = cc_xp_order_seniority\n')
            out.append(f'\t\t\tposition = {i}\n')
            out.append('\t\t\tcheck_range_bounds = no\n')
            out.append(f'\t\t\tsave_scope_as = cc_office_cand_{i + 1}\n')
            out.append('\t\t}\n')
        out.append('\t}\n')
    out.append('}\n\n')

    out.append('# Shows what the flagged office does, on each candidate option.\n')
    out.append('cc_office_panel_tooltip = {\n')
    for idx, o in enumerate(OFFICES):
        k = o['key']
        kw = 'if' if idx == 0 else 'else_if'
        out.append(f'\t{kw} = {{\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_panel_{k} }}\n')
        out.append(f'\t\tcustom_tooltip = {{ text = cc_office_{k}_tt }}\n')
        out.append('\t}\n')
    out.append('}\n\n')

    out.append('# Appoints $WHO$ to the flagged office.\n')
    out.append('cc_office_panel_appoint = {\n')
    out.append('\t$WHO$ = { save_scope_as = office_holder }\n')
    for idx, o in enumerate(OFFICES):
        k = o['key']
        kw = 'if' if idx == 0 else 'else_if'
        out.append(f'\t{kw} = {{\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_panel_{k} }}\n')
        out.append(f'\t\tcc_office_appoint = {{ OFFICE = {k} }}\n')
        out.append('\t}\n')
    out.append('\thidden_effect = {\n')
    out.append('\t\tcc_office_panel_clear = yes\n')
    out.append('\t\tcc_office_publish_roster = yes\n')
    out.append('\t}\n')
    out.append('}\n')
    return ''.join(out)


def emit_actions() -> str:
    """Appoint and Dismiss, one of each per office, for the Household tab's cards.

    type = owncountry with no select_trigger: a panel button supplies an actor and nothing
    else (see cc_xp_court_actions.txt). Appoint offers its candidates in an event; Dismiss
    needs no candidate, because the office names its own holder.
    """
    out = [BOM, BANNER,
           '#\n'
           '# Household tab card buttons. Appoint fires ' + PANEL_APPOINT_EVENT + ' with the most\n'
           '# senior eligible ministers as options; Dismiss vacates the post.\n\n']
    for o in OFFICES:
        k = o['key']
        out.append(f'# {o["name"]}\n')
        out.append(f'cc_office_{k}_appoint = {{\n')
        out.append('\ttype = owncountry\n')
        out.append('\tprice = price:cc_office_appointment\n')
        out.append('\tai_tick = never\n\n')
        out.append('\tpotential = {\n')
        out.append('\t\tscope:actor = {\n\t\t\tcc_xp_enabled = yes\n')
        out.append(f'\t\t\tcc_office_{k}_exists = yes\n')
        out.append('\t\t}\n\t}\n\n')
        out.append('\tallow = {\n\t\tscope:actor = {\n')
        out.append(f'\t\t\tcc_office_{k}_vacant = yes\n')
        out.append('\t\t\tcustom_tooltip = {\n')
        out.append('\t\t\t\ttext = cc_office_tt_room\n')
        out.append('\t\t\t\tcc_office_filled_count < cc_office_slot_cap\n')
        out.append('\t\t\t}\n')
        out.append('\t\t\tcustom_tooltip = {\n')
        out.append(f'\t\t\t\ttext = cc_office_{k}_tt_candidate\n')
        out.append('\t\t\t\tany_cabinet_character = {\n')
        out.append('\t\t\t\t\tcc_office_can_be_appointed = yes\n')
        out.append(f'\t\t\t\t\tcc_xp_tier_at_least = {{ TRACK = {o["track"]}  TIER = {o["tier"]} }}\n')
        out.append('\t\t\t\t}\n')
        out.append('\t\t\t}\n')
        out.append('\t\t}\n\t}\n\n')
        out.append('\teffect = {\n\t\tscope:actor = {\n')
        out.append(f'\t\t\tcustom_tooltip = {{ text = cc_office_{k}_tt }}\n')
        out.append('\t\t\thidden_effect = {\n')
        out.append('\t\t\t\tcc_office_panel_clear = yes\n')
        out.append(f'\t\t\t\tset_variable = {{ name = cc_office_panel_{k}  value = yes  months = 1 }}\n')
        out.append('\t\t\t}\n')
        out.append(f'\t\t\ttrigger_event_silently = {{ id = {PANEL_APPOINT_EVENT} }}\n')
        out.append('\t\t}\n\t}\n\n')
        out.append('\tai_will_do = {\n\t\tadd = { value = 0 }\n\t}\n}\n\n')

        out.append(f'cc_office_{k}_dismiss = {{\n')
        out.append('\ttype = owncountry\n')
        out.append('\tai_tick = never\n\n')
        out.append('\tpotential = {\n')
        out.append('\t\tscope:actor = {\n\t\t\tcc_xp_enabled = yes\n')
        out.append(f'\t\t\thas_variable = cc_office_{k}_filled\n')
        out.append('\t\t}\n\t}\n\n')
        out.append('\tallow = {\n\t\tscope:actor = {\n')
        out.append(f'\t\t\thas_variable = cc_office_{k}_filled\n')
        out.append('\t\t}\n\t}\n\n')
        out.append('\teffect = {\n\t\tscope:actor = {\n')
        out.append('\t\t\tcustom_tooltip = { text = cc_office_tt_dismiss }\n')
        out.append('\t\t\thidden_effect = {\n')
        out.append(f'\t\t\t\tcc_office_vacate = {{ OFFICE = {k} }}\n')
        out.append('\t\t\t\tcc_office_publish_roster = yes\n')
        out.append('\t\t\t}\n')
        out.append('\t\t}\n\t}\n\n')
        out.append('\tai_will_do = {\n\t\tadd = { value = 0 }\n\t}\n}\n\n')
    return ''.join(out)


def emit_events() -> str:
    out = [BOM, 'namespace = cc_office\n\n', BANNER,
           '#\n'
           '# The appointment picker. A character_interaction targets the minister (they are on\n'
           '# a row, so select_trigger works); this event picks the office, because an\n'
           '# interaction carries one target and appointing X to Y needs two values.\n'
           '#\n'
           '# root = country, scope:office_holder = the minister being appointed.\n\n']

    out.append(f'{PICKER_EVENT} = {{\n')
    out.append('\ttype = country_event\n')
    out.append(f'\ttitle = {PICKER_EVENT}.title\n')
    out.append(f'\tdesc = {PICKER_EVENT}.desc\n')
    out.append('\toutcome = neutral\n\n')
    out.append('\tillustration_tags = {\n\t\t10 = interior\n\t}\n\n')

    for o in OFFICES:
        k = o['key']
        out.append(f'\t# {o["name"]}\n')
        out.append('\toption = {\n')
        out.append(f'\t\tname = {PICKER_EVENT}.{k}\n')
        out.append('\t\ttrigger = {\n')
        out.append(f'\t\t\tcc_office_{k}_vacant = yes\n')
        out.append('\t\t\tcc_office_filled_count < cc_office_slot_cap\n')
        out.append('\t\t\tscope:office_holder = {\n')
        out.append(f'\t\t\t\tcc_xp_tier_at_least = {{ TRACK = {o["track"]}  TIER = {o["tier"]} }}\n')
        out.append('\t\t\t\tNOT = { cc_office_holds_any = yes }\n')
        out.append('\t\t\t}\n')
        out.append('\t\t}\n')
        # What the post does, before the player commits. cc_office_appoint only writes
        # variables, so without this the option's generated tooltip says nothing at all
        # and the choice is made blind. The auto_modifier's own tooltip only appears once
        # the office is already filled, which is too late to be a decision aid.
        out.append(f'\t\tcustom_tooltip = {{ text = cc_office_{k}_tt }}\n')
        out.append(f'\t\tcc_office_appoint = {{ OFFICE = {k} }}\n')
        out.append('\t}\n\n')

    out.append('\t# Nothing available. Always shown last so the event can never present zero\n'
               '\t# options, which would leave the player unable to dismiss it.\n')
    out.append('\toption = {\n')
    out.append(f'\t\tname = {PICKER_EVENT}.none\n')
    out.append('\t}\n')
    out.append('}\n\n')

    out.append('# An office was retired by an advance and its holder released.\n'
               '# root = country.\n')
    out.append(f'{VACATED_EVENT} = {{\n')
    out.append('\ttype = country_event\n')
    out.append(f'\ttitle = {VACATED_EVENT}.title\n')
    out.append(f'\tdesc = {VACATED_EVENT}.desc\n')
    out.append('\toutcome = neutral\n\n')
    out.append('\tillustration_tags = {\n\t\t10 = interior\n\t}\n\n')
    out.append('\toption = {\n')
    out.append(f'\t\tname = {VACATED_EVENT}.a\n')
    out.append('\t}\n')
    out.append('}\n\n')

    out.append('# The Household tab\'s Appoint button on one office: whom to name.\n'
               '# root = country. The office is flagged cc_office_panel_<key>.\n')
    out.append(f'{PANEL_APPOINT_EVENT} = {{\n')
    out.append('\ttype = country_event\n')
    out.append(f'\ttitle = {PANEL_APPOINT_EVENT}.title\n')
    # Nobody may qualify by the time the event fires; say so rather than show a list.
    out.append('\tdesc = {\n\t\tfirst_valid = {\n'
               '\t\t\ttriggered_desc = {\n'
               '\t\t\t\ttrigger = { NOT = { exists = scope:cc_office_cand_1 } }\n'
               f'\t\t\t\tdesc = {PANEL_APPOINT_EVENT}.desc_none\n'
               '\t\t\t}\n'
               f'\t\t\tdesc = {PANEL_APPOINT_EVENT}.desc\n'
               '\t\t}\n\t}\n')
    out.append('\toutcome = neutral\n\n')
    out.append('\tillustration_tags = {\n\t\t10 = interior\n\t}\n\n')
    out.append('\timmediate = {\n\t\tcc_office_panel_save_candidates = yes\n'
               '\t\tcc_xp_dedupe_picks = { P = cc_office_cand }\n\t}\n\n')
    for i in range(1, PANEL_CANDIDATES + 1):
        out.append('\toption = {\n')
        # One name key per option: option text is drawn before any option runs, so each
        # must read its own saved candidate.
        out.append(f'\t\tname = {PANEL_APPOINT_EVENT}.cand_{i}\n')
        out.append(f'\t\ttrigger = {{ exists = scope:cc_office_cand_{i} }}\n')
        out.append('\t\tcc_office_panel_tooltip = yes\n')
        out.append(f'\t\tcc_office_panel_appoint = {{ WHO = scope:cc_office_cand_{i} }}\n')
        out.append('\t}\n')
    out.append('\toption = {\n')
    out.append(f'\t\tname = {PANEL_APPOINT_EVENT}.none\n')
    out.append('\t\thidden_effect = { cc_office_panel_clear = yes }\n')
    out.append('\t}\n')
    out.append('}\n')
    return ''.join(out)


GUI_HEADER = '''######################################################################
# GENERATED FILE. Do not edit by hand.
#   python tools/generate_offices.py
#
# The Household tab of the Court Ledger: one card per office, in a two-column grid.
#
# WHY ONE BLOCK PER OFFICE RATHER THAN GENERIC SLOTS. Which posts exist depends on what the
# realm has researched, so a generic slot would still need a number-to-name mapping in GUI,
# which is the same 43 visibility checks with an extra indirection on top.
#
# WHY IT NEEDS PUBLISHED VARIABLES. GUI cannot ask whether a named advance has been
# researched (IsResearched exists only on the advances screen's own datamodel) and cannot
# read a script value. cc_office_publish_roster pushes out, per office: _open (vacant),
# _soon (its advance can be researched now), _retiring (the advance that ends it can be
# researched now), and for a held office _scale_var and _tenure.
#
# THE GRID is a flowcontainer with wrap_count = 2 and ignoreinvisible = yes, which reflows
# the visible cards into two columns and skips the hidden ones (vanilla: game_rules.gui).
#
# Properties in a template are declared at top level, not wrapped in a widget:
# `using = <template>` merges a template's contents into the widget it is used on, and an
# extra layer collapses to zero size and takes its children's mouse input with it.
######################################################################

# A held office. Expects its holder as the Character datacontext (cc_office_<key>_holder).
template cc_office_held_card {
\tsize = { 230 186 }
\tbackground = { using = color_whiteish_texture  alpha = 0.10 }

\tvbox = {
\t\tlayoutpolicy_horizontal = expanding
\t\tlayoutpolicy_vertical = expanding
\t\tmargin = { 8 6 }
\t\tspacing = 3

\t\thbox = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tspacing = 4
\t\t\ttext_single = {
\t\t\t\tfontsize = 14
\t\t\t\talign = left|nobaseline
\t\t\t\tblock "office_name" {}
\t\t\t}
\t\t\texpand = {}
\t\t\tblock "office_retiring" {}
\t\t\tblock "office_button" {}
\t\t}
\t\ttext_single = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tfontsize = 10
\t\t\tdefault_format = "#weak"
\t\t\talign = left|nobaseline
\t\t\tblock "office_family" {}
\t\t}

\t\thbox = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tspacing = 6
\t\t\tportrait_standard_head_framed_button = {
\t\t\t\tsize = { 38 44 }
\t\t\t\tonclick = "[ShowCharacter(Character.Self)]"
\t\t\t}
\t\t\tvbox = {
\t\t\t\tlayoutpolicy_horizontal = expanding
\t\t\t\ttext_single = { layoutpolicy_horizontal = expanding  fontsize = 12  align = left|nobaseline  text = "[Character.GetShortNameWithNoTooltip]" }
\t\t\t\ttext_single = { layoutpolicy_horizontal = expanding  fontsize = 10  default_format = "#weak"  align = left|nobaseline  text = "CC_OFFICE_CARD_SENIORITY" }
\t\t\t\ttext_single = {
\t\t\t\t\tlayoutpolicy_horizontal = expanding
\t\t\t\t\tfontsize = 10
\t\t\t\t\tdefault_format = "#weak"
\t\t\t\t\talign = left|nobaseline
\t\t\t\t\tblock "office_tenure" {}
\t\t\t\t}
\t\t\t}
\t\t}

\t\t# Effects at the strength this holder gives them.
\t\ttext_multi = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tautoresize = yes
\t\t\tmultiline = yes
\t\t\tmax_width = 212
\t\t\tfontsize = 11
\t\t\tblock "office_effects" {}
\t\t}
\t\ttext_single = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tfontsize = 10
\t\t\tdefault_format = "#weak"
\t\t\talign = left|nobaseline
\t\t\tblock "office_scale" {}
\t\t}

\t\texpand = {}
\t}
}

# An office the realm has but nobody holds.
template cc_office_open_card {
\tsize = { 230 140 }
\tbackground = { using = color_black_texture  alpha = 0.18 }

\tvbox = {
\t\tlayoutpolicy_horizontal = expanding
\t\tlayoutpolicy_vertical = expanding
\t\tmargin = { 8 6 }
\t\tspacing = 3

\t\thbox = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tspacing = 4
\t\t\ttext_single = {
\t\t\t\tfontsize = 14
\t\t\t\tdefault_format = "#weak"
\t\t\t\talign = left|nobaseline
\t\t\t\tblock "office_name" {}
\t\t\t}
\t\t\texpand = {}
\t\t\tblock "office_retiring" {}
\t\t\tblock "office_button" {}
\t\t}
\t\ttext_single = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tfontsize = 10
\t\t\tdefault_format = "#weak"
\t\t\talign = left|nobaseline
\t\t\tblock "office_family" {}
\t\t}

\t\t# Base effects, as a seniority 1 holder would give them.
\t\ttext_multi = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tautoresize = yes
\t\t\tmultiline = yes
\t\t\tmax_width = 212
\t\t\tfontsize = 11
\t\t\tblock "office_effects" {}
\t\t}
\t\ttext_single = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tfontsize = 10
\t\t\tdefault_format = "#weak"
\t\t\talign = left|nobaseline
\t\t\tblock "office_requirement" {}
\t\t}

\t\texpand = {}
\t}
}

# An office this realm can open by researching one advance now.
template cc_office_locked_card {
\tsize = { 230 58 }
\tbackground = { using = color_black_texture  alpha = 0.12 }

\tvbox = {
\t\tlayoutpolicy_horizontal = expanding
\t\tlayoutpolicy_vertical = expanding
\t\tmargin = { 8 5 }
\t\tspacing = 1
\t\ttext_single = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tfontsize = 12
\t\t\tdefault_format = "#weak"
\t\t\talign = left|nobaseline
\t\t\tblock "office_name" {}
\t\t}
\t\ttext_single = {
\t\t\tlayoutpolicy_horizontal = expanding
\t\t\tfontsize = 10
\t\t\tdefault_format = "#weak"
\t\t\talign = left|nobaseline
\t\t\tblock "office_opens" {}
\t\t}
\t\texpand = {}
\t}
}

'''


def _var(k: str, name: str) -> str:
    return f"Player.MakeScope.GetVariable('cc_office_{k}_{name}')"


# Appoint and dismiss are icon buttons in the card's top right: the cabinet hat to appoint,
# the barred cabinet to dismiss. The action's own tooltip names what the button does.
BUTTON_ICONS = {
    'CC_OFFICE_BTN_APPOINT': 'gfx/interface/icons/character_roles/cabinet.dds',
    'CC_OFFICE_BTN_DISMISS': 'gfx/interface/icons/modifier_types/blocked_from_cabinet.dds',
}


def _button(action: str, label: str) -> str:
    return (f'card_header_button_01 = {{\n'
            f'\tsize = {{ 30 26 }}\n'
            f'\tscripted_action_tooltip = {{\n'
            f'\t\tclick_type = left\n'
            f'\t\tclick_mode = single\n'
            f'\t\taction_name = "{action}"\n'
            f'\t\tactor = "[Player]"\n'
            f'\t}}\n'
            f'\tenabled = "[PdxGuiWidget.IsUberButtonEnabled]"\n'
            f'\ttooltipwidget = {{ using = action_tooltip_pop_out }}\n'
            f'\ticon = {{\n'
            f'\t\tparentanchor = center\n'
            f'\t\tsize = {{ 20 20 }}\n'
            f'\t\ttexture = "{BUTTON_ICONS[label]}"\n'
            f'\t}}\n'
            f'}}')


def _retiring(k: str, has_obsolete: bool) -> str:
    if not has_obsolete:
        return ''
    return (f'text_single = {{ fontsize = 10  align = right|nobaseline  '
            f'visible = "[{_var(k, "retiring")}.IsSet]"  text = "CC_OFFICE_RETIRING"  '
            f'tooltip = "cc_office_{k}_retiring_tt" }}')


def _indent(text: str, depth: int) -> str:
    return '\n'.join(('\t' * depth + line) if line else line for line in text.split('\n'))


def _block(name: str, body: str, depth: int) -> str:
    return f'{chr(9) * depth}blockoverride "{name}" {{\n{_indent(body, depth + 1)}\n{chr(9) * depth}}}\n'


def emit_gui() -> str:
    out = [GUI_HEADER]
    # THIS TEMPLATE IS A SCROLLAREA'S BODY, mounted as `scrollarea = { using = ... }` in
    # cc_cabinet_court.gui. Extra tab panels sit outside the situation panel's own
    # scrollarea (common.gui:368) and a grid of cards is taller than the panel, so the tab
    # brings its own. It must not be a scrollarea nested inside a plain `widget`: a plain
    # widget does not size its children, and a scrollarea has no natural size, so it
    # collapses to nothing and the tab renders empty.
    out.append('template cc_office_household_content {\n')
    out.append('\tusing = layoutpolicy_expanding\n')
    out.append('\tscrollbarpolicy_horizontal = always_off\n')
    out.append('\tautoresizeviewport = yes\n')
    out.append('\tviewportwidget = {\n\t\twidget = {\n\t\t\tscissor = yes\n\t\t}\n\t}\n')
    out.append('\tscrollbar_vertical = {\n\t\tusing = Scrollbar_Vertical\n\t}\n')
    out.append('\t\tscrollwidget = {\n')
    out.append('\t\t\tvbox = {\n')
    out.append('\t\t\t\tlayoutpolicy_horizontal = expanding\n')
    out.append('\t\t\t\tusing = bg_secondary_inner_alt\n')
    out.append('\t\t\t\tmargin = { 10 8 }\n')
    out.append('\t\t\t\tspacing = 6\n\n')

    out.append('\t\t\t\t# ---- Summary ----\n')
    out.append('\t\t\t\thbox = {\n')
    out.append('\t\t\t\t\tlayoutpolicy_horizontal = expanding\n')
    out.append('\t\t\t\t\tspacing = 4\n')
    out.append('\t\t\t\t\ttext_single = { fontsize = 12  default_format = "#weak"  text = "CC_OFFICE_FILLED_LABEL" }\n')
    out.append('\t\t\t\t\ttext_single = {\n\t\t\t\t\t\tfontsize = 15\n')
    out.append("\t\t\t\t\t\traw_text = \"[FixedPointToInt(Player.MakeScope.GetVariable('cc_office_filled_var').GetValue)]/"
               + str(SLOT_CAP) + '"\n')
    out.append('\t\t\t\t\t\ttooltip = "CC_OFFICE_FILLED_TT"\n')
    out.append('\t\t\t\t\t}\n')
    out.append('\t\t\t\t\texpand = {}\n')
    # The tab's explainer lives in an info icon at the end of the summary row.
    out.append('\t\t\t\t\ticon = {\n')
    out.append('\t\t\t\t\t\tsize = { 20 20 }\n')
    out.append('\t\t\t\t\t\ttexture = "gfx/interface/icons/flat_icons/tabicons/info_flat_icon.dds"\n')
    out.append('\t\t\t\t\t\ttexture_density = 2\n')
    out.append('\t\t\t\t\t\ttooltipwidget = {\n\t\t\t\t\t\t\tContextualTooltipType = {\n')
    out.append('\t\t\t\t\t\t\t\tblockoverride "title_text" { text = "CC_OFFICE_TAB_HOUSEHOLD" }\n')
    out.append('\t\t\t\t\t\t\t\tblockoverride "tooltip_content" {\n')
    out.append('\t\t\t\t\t\t\t\t\ttext_multi = { autoresize = yes  multiline = yes  max_width = 330  text = "CC_OFFICE_TAB_NOTE" }\n')
    out.append('\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n')
    out.append('\t\t\t\t\t}\n')
    out.append('\t\t\t\t}\n\n')

    def grid(header: str, cards: list, extra_header: str = '') -> None:
        out.append(f'\t\t\t\t# ---- {header} ----\n')
        if extra_header:
            out.append(extra_header)
        else:
            out.append(f'\t\t\t\ttext_single = {{ fontsize = 12  margin_top = 4  text = "{header}" }}\n')
        out.append('\t\t\t\tflowcontainer = {\n')
        out.append('\t\t\t\t\tdirection = horizontal\n')
        out.append('\t\t\t\t\twrap_count = 2\n')
        out.append('\t\t\t\t\tignoreinvisible = yes\n')
        out.append('\t\t\t\t\tspacing = 6\n\n')
        out.extend(cards)
        out.append('\t\t\t\t}\n\n')

    held = []
    for o in OFFICES:
        k = o['key']
        held.append(f'\t\t\t\t\t# {o["name"]}\n')
        held.append('\t\t\t\t\twidget = {\n')
        held.append(f'\t\t\t\t\t\tvisible = "[{_var(k, "holder")}.IsSet]"\n')
        held.append(f'\t\t\t\t\t\tdatacontext = "[{_var(k, "holder")}.GetCharacter]"\n')
        held.append('\t\t\t\t\t\tusing = cc_office_held_card\n')
        held.append(f'\t\t\t\t\t\ttooltip = "cc_office_{k}_tt"\n')
        held.append(f'\t\t\t\t\t\tblockoverride "office_name" {{ text = "cc_office_{k}" }}\n')
        held.append(f'\t\t\t\t\t\tblockoverride "office_family" {{ text = "CC_OFFICE_FAMILY_{o["family"].upper()}" }}\n')
        held.append(f'\t\t\t\t\t\tblockoverride "office_tenure" {{ text = "cc_office_{k}_tenure_line" }}\n')
        held.append(f'\t\t\t\t\t\tblockoverride "office_effects" {{ text = "cc_office_{k}_fx_held" }}\n')
        held.append(f'\t\t\t\t\t\tblockoverride "office_scale" {{ text = "cc_office_{k}_scale_line" }}\n')
        ret = _retiring(k, bool(o['obsolete']))
        if ret:
            held.append(_block('office_retiring', ret, 6))
        held.append(_block('office_button', _button(f'cc_office_{k}_dismiss', 'CC_OFFICE_BTN_DISMISS'), 6))
        held.append('\t\t\t\t\t}\n')
    grid('CC_OFFICE_HELD_HEADER', held)

    open_ = []
    for o in OFFICES:
        k = o['key']
        open_.append(f'\t\t\t\t\t# {o["name"]}\n')
        open_.append('\t\t\t\t\twidget = {\n')
        open_.append(f'\t\t\t\t\t\tvisible = "[{_var(k, "open")}.IsSet]"\n')
        open_.append('\t\t\t\t\t\tusing = cc_office_open_card\n')
        open_.append(f'\t\t\t\t\t\ttooltip = "cc_office_{k}_tt"\n')
        open_.append(f'\t\t\t\t\t\tblockoverride "office_name" {{ text = "cc_office_{k}" }}\n')
        open_.append(f'\t\t\t\t\t\tblockoverride "office_family" {{ text = "CC_OFFICE_FAMILY_{o["family"].upper()}" }}\n')
        open_.append(f'\t\t\t\t\t\tblockoverride "office_effects" {{ text = "cc_office_{k}_fx_base" }}\n')
        open_.append(f'\t\t\t\t\t\tblockoverride "office_requirement" {{ text = "cc_office_{k}_req" }}\n')
        ret = _retiring(k, bool(o['obsolete']))
        if ret:
            open_.append(_block('office_retiring', ret, 6))
        open_.append(_block('office_button', _button(f'cc_office_{k}_appoint', 'CC_OFFICE_BTN_APPOINT'), 6))
        open_.append('\t\t\t\t\t}\n')
    grid('CC_OFFICE_OPEN_HEADER', open_)

    # Locked: offices this realm can open by researching an advance now. Behind an eye
    # toggle (a view variable, per viewer and unsaved), shown by default.
    locked_header = (
        '\t\t\t\thbox = {\n'
        '\t\t\t\t\tlayoutpolicy_horizontal = expanding\n'
        '\t\t\t\t\tmargin_top = 4\n'
        '\t\t\t\t\tspacing = 4\n'
        '\t\t\t\t\ttext_single = { fontsize = 12  text = "CC_OFFICE_LOCKED_HEADER"  tooltip = "CC_OFFICE_LOCKED_TT" }\n'
        '\t\t\t\t\texpand = {}\n'
        '\t\t\t\t\tcard_header_button_01 = {\n'
        '\t\t\t\t\t\tsize = { 26 26 }\n'
        "\t\t\t\t\t\tonclick = \"[GetVariableSystem.Toggle( 'cc_office_hide_locked' )]\"\n"
        '\t\t\t\t\t\ttooltip = "CC_OFFICE_TOGGLE_LOCKED_TT"\n'
        '\t\t\t\t\t\ticon = {\n'
        '\t\t\t\t\t\t\tusing = color_white_texture\n'
        '\t\t\t\t\t\t\talpha = 0.3\n'
        '\t\t\t\t\t\t\tsize = { 100% 100% }\n'
        "\t\t\t\t\t\t\tvisible = \"[Not(GetVariableSystem.Exists( 'cc_office_hide_locked' ))]\"\n"
        '\t\t\t\t\t\t}\n'
        '\t\t\t\t\t\ticon = {\n'
        '\t\t\t\t\t\t\tparentanchor = center\n'
        '\t\t\t\t\t\t\tsize = { 20 20 }\n'
        '\t\t\t\t\t\t\ttexture = "gfx/interface/icons/flat_icons/building_panel/build_visible.dds"\n'
        '\t\t\t\t\t\t}\n'
        '\t\t\t\t\t}\n'
        '\t\t\t\t}\n')
    locked = []
    for o in OFFICES:
        if not o['unlock']:
            continue
        k = o['key']
        locked.append(f'\t\t\t\t\t# {o["name"]}\n')
        locked.append('\t\t\t\t\twidget = {\n')
        locked.append(f'\t\t\t\t\t\tvisible = "[And(Not(GetVariableSystem.Exists( \'cc_office_hide_locked\' )), {_var(k, "soon")}.IsSet)]"\n')
        locked.append('\t\t\t\t\t\tusing = cc_office_locked_card\n')
        locked.append(f'\t\t\t\t\t\ttooltip = "cc_office_{k}_tt"\n')
        locked.append(f'\t\t\t\t\t\tblockoverride "office_name" {{ text = "cc_office_{k}" }}\n')
        locked.append(f'\t\t\t\t\t\tblockoverride "office_opens" {{ text = "cc_office_{k}_opens" }}\n')
        locked.append('\t\t\t\t\t}\n')
    grid('CC_OFFICE_LOCKED_HEADER', locked, locked_header)

    out.append('\t\t\t\texpand = {}\n')
    out.append('\t\t\t}\n')
    out.append('\t\t}\n')
    out.append('}\n')
    return ''.join(out)


def emit_loc() -> str:
    out = [BOM, 'l_english:\n\n']
    out.append(' # GENERATED FILE. Do not edit by hand. python tools/generate_offices.py\n\n')
    out.append(f' {PICKER_EVENT}.title: "A Place at Court"\n')
    out.append(f' {PICKER_EVENT}.desc: "The household has posts to fill, and a minister who '
               'might fill one. Which office suits [Character.GetName]?"\n')
    out.append(f' {PICKER_EVENT}.none: "No suitable office stands open."\n')
    out.append(f' {VACATED_EVENT}.title: "An Office Passes"\n')
    out.append(f' {VACATED_EVENT}.desc: "What the office did is now done another way, and the '
               'post is wound up. Its holder returns to ordinary service."\n')
    out.append(f' {VACATED_EVENT}.a: "So offices end."\n\n')

    # The appointment interaction. Kept here rather than hand-written so the office count
    # in the tooltip cannot drift from the table above.
    out.append(' # Appointment interaction (cc_office_appoint.txt)\n')
    out.append(' cc_office_appoint_to_household: "Appoint to the Household"\n')
    out.append(' cc_office_appoint_to_household_desc: "Raise a minister to a post at court. '
               'Which posts exist depends on what the realm has learned: an advance opens an '
               'office, and a later one closes it again. A minister holds one post at a time, '
               f'and the household supports {SLOT_CAP}."\n')
    out.append(' cc_office_appoint_to_household_desc_specific: '
               '"[SCOPE.sCharacter(\'recipient\').GetName] will be offered whichever posts '
               'their training suits them for."\n')
    out.append(' cc_office_appoint_to_household_act: "$cc_office_appoint_to_household$"\n')
    out.append(' cc_office_appoint_to_household_past: "Raised to the Household"\n')
    out.append(' cc_office_appoint_to_household_act_past: '
               '"[SCOPE.sCharacter(\'recipient\').GetName] has been given a post at court."\n')
    out.append(' cc_office_choose_appointee: "Who is to be raised?"\n')
    out.append(' cc_office_none_appointee: "@trigger_no! No minister is both trained and '
               'free of a post."\n')
    out.append(' cc_office_appoint_tt: "The office carries its benefit while they hold it, '
               'scaled by their seniority."\n')
    out.append(' cc_office_appoint_advance_tt: "Offices are opened by advances. Researching '
               'further will open new posts."\n')
    out.append(' cc_office_appoint_obsolete_tt: "An advance may also close an office. Its '
               'holder is released and the post is not replaced."\n\n')

    out.append(' # Household tab (cc_office_household.gui)\n')
    out.append(' CC_OFFICE_TAB_HOUSEHOLD: "Household"\n')
    out.append(' CC_OFFICE_FILLED_LABEL: "Posts filled"\n')
    out.append(' CC_OFFICE_HELD_HEADER: "In office"\n')
    out.append(' CC_OFFICE_OPEN_HEADER: "Standing open"\n')
    out.append(' CC_OFFICE_SENIORITY: "seniority"\n')
    out.append(' CC_OFFICE_SCALES_TT: "Scales with the holder\'s seniority, up to two and '
               f'a half times, and grows another {TENURE_PER_YEAR * 100:.10g}% for each year in '
               f'office, up to {TENURE_CAP_YEARS} years."\n')
    out.append(' CC_OFFICE_UPKEEP_TT: "for every post filled"\n')
    out.append(f' {UPKEEP_KEY}: "Household Upkeep"\n')
    out.append(f' {UPKEEP_KEY}_desc: "Every post the court fills costs something to keep up. '
               f'A full household of {SLOT_CAP} runs at '
               f'{SLOT_CAP * UPKEEP_PER_OFFICE * 100:+.10g}% court spending efficiency."\n')
    out.append(f' AUTO_MODIFIER_NAME_{UPKEEP_KEY}: "Household posts filled"\n')
    # "Advances open posts" reads as an imperative once translated, which is how the German
    # came back as "Besetzt offene Aemter". Naming research as the subject removes the
    # ambiguity in every target language.
    out.append(' CC_OFFICE_TAB_NOTE: "Researching an advance can open a post at court, and a '
               'later advance can close one. A minister holds one post at a time, and the '
               f'household supports {SLOT_CAP} in all. Appoint from an open post\'s card, or '
               'from a minister\'s own interaction menu."\n')
    # Card and panel strings.
    out.append(' CC_OFFICE_FILLED_TT: "Posts filled, out of the most the household supports. '
               'Each filled post costs court spending efficiency."\n')
    out.append(' CC_OFFICE_LOCKED_HEADER: "Within reach"\n')
    out.append(' CC_OFFICE_LOCKED_TT: "Posts the realm can open by researching one advance it '
               'can research now."\n')
    out.append(' CC_OFFICE_TOGGLE_LOCKED_TT: "Show or hide the posts within reach."\n')
    out.append(' CC_OFFICE_BTN_APPOINT: "Appoint"\n')
    out.append(' CC_OFFICE_BTN_DISMISS: "Dismiss"\n')
    out.append(' CC_OFFICE_RETIRING: "#Y Retiring#!"\n')
    out.append(' CC_OFFICE_CARD_SENIORITY: "Seniority [FixedPointToInt(Character.MakeScope.'
               "GetVariable('cc_level').GetValue)]\"\n")
    for fam, label in (('CORE', 'Household'), ('RELIGION', 'Religious post'),
                       ('GOVERNMENT', 'Government post'), ('CULTURE', 'Cultural post'),
                       ('REGION', 'Regional post')):
        out.append(f' CC_OFFICE_FAMILY_{fam}: "{label}"\n')
    out.append(' cc_office_tt_room: "The household has a post free"\n')
    out.append(' cc_office_tt_dismiss: "The holder leaves the post and returns to ordinary '
               'service. The post stands open."\n')
    out.append(f' {PANEL_APPOINT_EVENT}.title: "An Appointment"\n')
    out.append(f' {PANEL_APPOINT_EVENT}.desc: "A post at court stands open. These ministers are '
               'trained for it and free of other posts, the most senior first."\n')
    for i in range(1, PANEL_CANDIDATES + 1):
        out.append(f' {PANEL_APPOINT_EVENT}.cand_{i}: "[cc_office_cand_{i}.GetName], seniority '
                   f"[cc_office_cand_{i}.MakeScope.GetVariable('cc_level').GetValue|0]\"\n")
    out.append(f' {PANEL_APPOINT_EVENT}.desc_none: "The post stands open, but no minister '
               'is now both trained for it and free of other posts."\n')
    out.append(f' {PANEL_APPOINT_EVENT}.none: "Leave the post open."\n\n')

    for o in OFFICES:
        k, n = o['key'], o['name']
        track = TRACK_NAMES[o['track']]
        out.append(f' # {n} [{o["family"]}]\n')
        out.append(f' cc_office_{k}: "{n}"\n')
        out.append(f' cc_office_{k}_desc: "{o["desc"]}"\n')
        out.append(f' AUTO_MODIFIER_NAME_cc_office_{k}: "{n} appointed"\n')
        out.append(f' {PICKER_EVENT}.{k}: "Name them {n}."\n')
        out.append(f' cc_office_{k}_req: "Needs {track} tier {o["tier"]}."\n')

        # What the post actually does, spelled out before the player commits to it. The
        # auto_modifier generates its own tooltip once the office is FILLED, which is no
        # help at the moment of choosing, so the same information is built here from the
        # office table and hung on both the picker option and the panel row.
        lines = [f'#T {n}#!', f'$cc_office_{k}_desc$', '']
        lines += [format_modifier(mn, mv, MODTYPES) for mn, mv in o['mod'].items()]
        # The upkeep is charged per filled post, not per office, so it belongs in every
        # office's tooltip: the cost of taking THIS one is the same whichever it is.
        lines.append(format_modifier('court_spending_efficiency', UPKEEP_PER_OFFICE,
                                     MODTYPES) + ' $CC_OFFICE_UPKEEP_TT$')
        lines.append('')
        lines.append(f'$cc_office_{k}_req$')
        lines.append('$CC_OFFICE_SCALES_TT$')
        body = '\\n'.join(lines)
        out.append(f' cc_office_{k}_tt: "{body}"\n')

        # Card strings.
        scale = f"Player.MakeScope.GetVariable('cc_office_{k}_scale_var').GetValue"
        held = [format_modifier_scaled(mn, mv, MODTYPES, scale) for mn, mv in o['mod'].items()]
        base = [format_modifier(mn, mv, MODTYPES) for mn, mv in o['mod'].items()]
        out.append(f' cc_office_{k}_fx_held: "' + '\\n'.join(held) + '"\n')
        out.append(f' cc_office_{k}_fx_base: "' + '\\n'.join(base) + '"\n')
        out.append(f' cc_office_{k}_scale_line: "x[{scale}|2] from seniority and years in office"\n')
        out.append(f' cc_office_{k}_tenure_line: "In office '
                   f"[Player.MakeScope.GetVariable('cc_office_{k}_tenure').GetValue|0] years\"\n")
        out.append(f' cc_office_{k}_tt_candidate: "A minister free of other posts, with {track} '
                   f'tier {o["tier"]} or better"\n')
        if o['unlock']:
            out.append(f' cc_office_{k}_opens: "Opens with [ShowAdvanceName(\'{o["unlock"]}\')]"\n')
        # Names for the card buttons' generic actions (cc_office_actions.txt).
        out.append(f' cc_office_{k}_appoint: "Appoint a {n}"\n')
        out.append(f' cc_office_{k}_appoint_desc: "Choose a minister for the post of {n}. You '
                   'will be offered the most senior ministers trained for it."\n')
        out.append(f' cc_office_{k}_dismiss: "Dismiss the {n}"\n')
        out.append(f' cc_office_{k}_dismiss_desc: "Release the {n} from the post. They return '
                   'to ordinary service and the post stands open."\n')
        if o['obsolete']:
            out.append(f' cc_office_{k}_retiring_tt: "Retires when [ShowAdvanceName(\'{o["obsolete"]}\')] '
                       'is researched, which the realm can do now. Its holder is released and the '
                       'post is not replaced."\n')
        out.append('\n')
    return ''.join(out)


###############################################################################
# OFFICE EVENTS
#
# Two per family. Once a year a court with an office filled has OFFICE_EVENT_CHANCE percent
# to raise one, for a filled office picked at random, then waits OFFICE_EVENT_COOLDOWN
# years. The event names the office and its holder; its options lean on the holder:
#   gate 'senior'  the holder is seniority 5 or more
#   gate 'tenure'  the holder has held the post 5 years or more
# A gated option is the better one, and is what a good appointment buys.
#
# Option effects are plain script, written here once. `HOLDER` is replaced by the saved
# holder scope.
###############################################################################

OFFICE_EVENT_FIRST_ID = 10
OFFICE_EVENT_CHANCE = 30
OFFICE_EVENT_COOLDOWN = 3

GOLD_GAIN_2 = 'add_gold = { value = monthly_income_trade_and_tax  multiply = 2  min = 10 }'
GOLD_GAIN_1 = 'add_gold = { value = monthly_income_trade_and_tax  multiply = 1  min = 5 }'
GOLD_COST_2 = 'add_gold = { value = monthly_income_trade_and_tax  multiply = -2  max = -10 }'
GOLD_COST_1 = 'add_gold = { value = monthly_income_trade_and_tax  multiply = -1  max = -5 }'


def _sat(estate, size):
    return f'add_estate_satisfaction = {{ type = estate_type:{estate}_estate  value = estate_satisfaction_{size} }}'


def _xp(amount):
    return f'HOLDER = {{ cc_xp_gain_dominant = {{ AMOUNT = {amount} }} cc_xp_recompute = yes }}'


FAMILY_EVENTS = {
    'core': [
        dict(title='The Household Accounts',
             body='They have been through the household accounts. Money has been leaking out of the kitchens and stables for years, and the people taking it are well connected.',
             options=[
                 ('Stop it, whoever it offends.', None, [GOLD_GAIN_2, _sat('nobles', 'weak_penalty'), _xp(15)]),
                 ('Quietly, and without names.', None, [GOLD_GAIN_1]),
                 ('Let them reorganise the household.', 'senior', [GOLD_GAIN_2, _xp(25)]),
             ]),
        dict(title='A Quarrel over Precedence',
             body='They are at odds with the great families over who walks first at court, and both sides expect the crown to settle it.',
             options=[
                 ('Back the officer.', None, ['add_prestige = prestige_weak_bonus', _sat('nobles', 'weak_penalty'), _xp(10)]),
                 ('Back the families.', None, [_sat('nobles', 'weak_bonus'), 'add_prestige = prestige_weak_penalty']),
                 ('Their long service settles it.', 'tenure', ['add_prestige = prestige_weak_bonus', _xp(10)]),
             ]),
    ],
    'religion': [
        dict(title='A Sermon at Court',
             body='They preached before the whole court, and the sermon is being repeated in every church in the capital.',
             options=[
                 ('Have it printed.', None, ['add_religious_influence = religious_influence_mild_bonus', _xp(10)]),
                 ('A good sermon. Nothing more.', None, ['add_stability = stability_weak_bonus']),
                 ('Have them preach it across the realm.', 'senior', ['add_religious_influence = religious_influence_mild_bonus', 'add_stability = stability_weak_bonus', _xp(20)]),
             ]),
        dict(title='A Matter of Conscience',
             body='They have refused to endorse a decision of the crown, and say so openly.',
             options=[
                 ('Overrule them.', None, ['add_political_influence = political_influence_weak_bonus', _sat('clergy', 'weak_penalty')]),
                 ('Give way.', None, [_sat('clergy', 'weak_bonus'), 'add_political_influence = political_influence_weak_penalty']),
                 ('They have earned a hearing.', 'tenure', [_sat('clergy', 'weak_bonus'), 'add_stability = stability_weak_bonus', _xp(15)]),
             ]),
    ],
    'government': [
        dict(title='Petitions Pile Up',
             body='Petitions to the crown are piling up in their office faster than they can be read.',
             options=[
                 ('Clear them, however long it takes.', None, ['add_political_influence = political_influence_weak_bonus', _xp(15)]),
                 ('Let them wait.', None, [_sat('burghers', 'weak_penalty')]),
                 ('Have them reform the procedure.', 'senior', ['add_political_influence = political_influence_mild_bonus', _xp(20)]),
             ]),
        dict(title='An Inspection of the Offices',
             body='They want to inspect every office under them, and the clerks have heard.',
             options=[
                 ('Inspect them all.', None, ['add_stability = stability_weak_bonus', _sat('burghers', 'weak_penalty'), _xp(10)]),
                 ('A warning will do.', None, ['add_political_influence = political_influence_weak_bonus']),
                 ('Trust them to know where to look.', 'tenure', ['add_stability = stability_weak_bonus', 'add_political_influence = political_influence_weak_bonus', _xp(15)]),
             ]),
    ],
    'culture': [
        dict(title='A Festival at Court',
             body='They propose a festival in the old manner, with music, plays and a great deal of food.',
             options=[
                 ('Spare no expense.', None, [GOLD_COST_2, 'add_prestige = prestige_mild_bonus', _xp(10)]),
                 ('Keep it modest.', None, ['add_prestige = prestige_weak_bonus']),
                 ('Let them arrange it.', 'senior', [GOLD_COST_1, 'add_prestige = prestige_mild_bonus', _xp(20)]),
             ]),
        dict(title='A Foreign Fashion',
             body='They have taken up a fashion from abroad, and half the court has followed. The other half is offended.',
             options=[
                 ('Adopt it at court.', None, ['add_prestige = prestige_weak_bonus', _sat('nobles', 'weak_penalty')]),
                 ('Forbid it.', None, [_sat('nobles', 'weak_bonus'), 'add_prestige = prestige_weak_penalty']),
                 ('They know what will last.', 'tenure', ['add_prestige = prestige_weak_bonus', _xp(25)]),
             ]),
    ],
    'region': [
        dict(title='News from the Frontier',
             body='They bring news from the frontier provinces: unrest, bad harvests, and officials nobody has checked on in years.',
             options=[
                 ('Act on it now.', None, [GOLD_COST_1, 'add_stability = stability_weak_bonus', _xp(10)]),
                 ('File it for later.', None, [_xp(5)]),
                 ('Send them to deal with it.', 'senior', ['add_stability = stability_weak_bonus', 'add_political_influence = political_influence_weak_bonus', _xp(20)]),
             ]),
        dict(title='The Provincial Notables',
             body='They have brought a delegation of provincial notables to court, who want to be heard.',
             options=[
                 ('Receive them with honour.', None, [GOLD_COST_1, 'add_political_influence = political_influence_weak_bonus']),
                 ('Send them home.', None, [_sat('nobles', 'weak_penalty')]),
                 ('They know these people.', 'tenure', [_sat('nobles', 'weak_bonus'), 'add_political_influence = political_influence_weak_bonus', _xp(15)]),
             ]),
    ],
}
FAMILY_ORDER = ['core', 'religion', 'government', 'culture', 'region']


def office_event_id(family: str, idx: int) -> str:
    return f'cc_office.{OFFICE_EVENT_FIRST_ID + FAMILY_ORDER.index(family) * 2 + idx}'


def emit_office_event_effects() -> str:
    out = ['\n# ---- Office events ----\n'
           '# Yearly. Picks one filled office at random and raises one of its family\'s two\n'
           '# events. The office is flagged cc_office_evt_<key> for the event to find.\n'
           'cc_office_roll_event = {\n'
           '\tif = {\n'
           '\t\tlimit = {\n'
           '\t\t\tis_ai = no\n'
           '\t\t\tNOT = { has_variable = cc_office_event_cd }\n'
           '\t\t\tany_cabinet_character = { cc_office_holds_any = yes }\n'
           '\t\t}\n'
           f'\t\trandom = {{\n\t\t\tchance = {OFFICE_EVENT_CHANCE}\n'
           f'\t\t\tset_variable = {{ name = cc_office_event_cd  value = yes  years = {OFFICE_EVENT_COOLDOWN} }}\n'
           '\t\t\trandom_list = {\n']
    for o in OFFICES:
        k = o['key']
        fam = o['family']
        out.append(f'\t\t\t\t1 = {{\n')
        out.append(f'\t\t\t\t\ttrigger = {{ has_variable = cc_office_{k}_filled }}\n')
        out.append(f'\t\t\t\t\tset_variable = {{ name = cc_office_evt_{k}  value = yes  months = 2 }}\n')
        out.append('\t\t\t\t\trandom_list = {\n')
        out.append(f'\t\t\t\t\t\t1 = {{ trigger_event_non_silently = {office_event_id(fam, 0)} }}\n')
        out.append(f'\t\t\t\t\t\t1 = {{ trigger_event_non_silently = {office_event_id(fam, 1)} }}\n')
        out.append('\t\t\t\t\t}\n')
        out.append('\t\t\t\t}\n')
    out.append('\t\t\t}\n\t\t}\n\t}\n}\n\n')

    out.append('# In an office event\'s immediate: save the flagged office\'s holder and tenure.\n'
               'cc_office_take_event = {\n'
               '\tclear_saved_scope = cc_office_evt_holder\n'
               '\tset_variable = { name = cc_office_evt_tenure  value = 0 }\n')
    for idx, o in enumerate(OFFICES):
        k = o['key']
        kw = 'if' if idx == 0 else 'else_if'
        out.append(f'\t{kw} = {{\n')
        out.append(f'\t\tlimit = {{ has_variable = cc_office_evt_{k} }}\n')
        out.append('\t\tevery_cabinet_character = {\n')
        out.append(f'\t\t\tlimit = {{ has_variable = cc_office_held_{k} }}\n')
        out.append('\t\t\tsave_scope_as = cc_office_evt_holder\n')
        out.append('\t\t}\n')
        out.append(f'\t\tif = {{\n\t\t\tlimit = {{ has_variable = cc_office_{k}_since }}\n')
        out.append('\t\t\tset_variable = {\n\t\t\t\tname = cc_office_evt_tenure\n')
        out.append(f'\t\t\t\tvalue = {{ value = current_year  subtract = var:cc_office_{k}_since  min = 0 }}\n')
        out.append('\t\t\t}\n\t\t}\n')
        out.append('\t}\n')
    out.append('}\n')
    return ''.join(out)


def emit_office_events() -> str:
    out = ['\n\n###############################################################################\n'
           '# OFFICE EVENTS (generated from FAMILY_EVENTS). Fired by cc_office_roll_event.\n'
           '###############################################################################\n\n']
    for fam in FAMILY_ORDER:
        offices = [o for o in OFFICES if o['family'] == fam]
        for idx, ev in enumerate(FAMILY_EVENTS[fam]):
            eid = office_event_id(fam, idx)
            out.append(f'# {ev["title"]} ({fam})\n')
            out.append(f'{eid} = {{\n')
            out.append('\ttype = country_event\n')
            out.append(f'\ttitle = {eid}.title\n')
            # The office's own line first, then the shared body. first_valid picks the one
            # line for the flagged office; a bare triggered_desc list would render them all.
            out.append('\tdesc = {\n\t\tfirst_valid = {\n')
            for o in offices:
                out.append(f'\t\t\ttriggered_desc = {{\n'
                           f'\t\t\t\ttrigger = {{ has_variable = cc_office_evt_{o["key"]} }}\n'
                           f'\t\t\t\tdesc = cc_office_evt_line_{o["key"]}\n'
                           f'\t\t\t}}\n')
            out.append('\t\t}\n')
            out.append(f'\t\tdesc = {eid}.desc\n')
            out.append('\t}\n')
            out.append('\toutcome = neutral\n')
            out.append('\tillustration_tags = {\n\t\t10 = interior\n\t\t10 = professional\n\t}\n\n')
            out.append('\ttrigger = {\n\t\tOR = {\n')
            for o in offices:
                out.append(f'\t\t\thas_variable = cc_office_evt_{o["key"]}\n')
            out.append('\t\t}\n\t}\n\n')
            out.append('\timmediate = {\n\t\tcc_office_take_event = yes\n\t}\n\n')
            for oi, (_, gate, effects) in enumerate(ev['options']):
                out.append('\toption = {\n')
                out.append(f'\t\tname = {eid}.{"abc"[oi]}\n')
                if gate == 'senior':
                    out.append('\t\ttrigger = {\n\t\t\tcustom_tooltip = {\n\t\t\t\ttext = cc_office_evt_tt_senior\n'
                               '\t\t\t\tscope:cc_office_evt_holder ?= { cc_xp_level_at_least = { LEVEL = 5 } }\n'
                               '\t\t\t}\n\t\t}\n')
                elif gate == 'tenure':
                    out.append('\t\ttrigger = {\n\t\t\tcustom_tooltip = {\n\t\t\t\ttext = cc_office_evt_tt_tenure\n'
                               '\t\t\t\tvar:cc_office_evt_tenure >= 5\n'
                               '\t\t\t}\n\t\t}\n')
                for e in effects:
                    out.append('\t\t' + e.replace('HOLDER', 'scope:cc_office_evt_holder ?') .replace('scope:cc_office_evt_holder ? =', 'scope:cc_office_evt_holder ?=') + '\n')
                out.append('\t}\n')
            out.append('}\n\n')
    return ''.join(out)


def emit_office_event_loc() -> str:
    out = ['\n # Office events\n',
           ' cc_office_evt_tt_senior: "The holder is of seniority 5 or more"\n',
           ' cc_office_evt_tt_tenure: "The holder has held the post 5 years or more"\n']
    for o in OFFICES:
        out.append(f' cc_office_evt_line_{o["key"]}: "[cc_office_evt_holder.GetName], the realm\'s {o["name"]}. "\n')
    for fam in FAMILY_ORDER:
        for idx, ev in enumerate(FAMILY_EVENTS[fam]):
            eid = office_event_id(fam, idx)
            out.append(f' {eid}.title: "{ev["title"]}"\n')
            out.append(f' {eid}.desc: "{ev["body"]}"\n')
            for oi, (label, _, _) in enumerate(ev['options']):
                out.append(f' {eid}.{"abc"[oi]}: "{label}"\n')
    return ''.join(out)


###############################################################################
# MAIN
###############################################################################

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='validate and report coverage without writing anything')
    args = ap.parse_args()

    if not ADVANCE_DIR.is_dir():
        print(f'ERROR: vanilla advances not found at {ADVANCE_DIR}', file=sys.stderr)
        return 2

    global MODTYPES
    advances = load_advances()
    modtypes = load_modifier_types()
    MODTYPES = modtypes
    print(f'loaded {len(advances)} vanilla advances, {len(modtypes)} modifier types')

    errs = validate(advances, modtypes)
    if errs:
        print(f'\nVALIDATION FAILED ({len(errs)} problems). Nothing was written.\n',
              file=sys.stderr)
        for e in errs:
            print('  ' + e, file=sys.stderr)
        return 1

    fam = {}
    for o in OFFICES:
        fam[o['family']] = fam.get(o['family'], 0) + 1
    print(f'{len(OFFICES)} offices validated: '
          + ', '.join(f'{v} {k}' for k, v in sorted(fam.items())))

    print('\noffices available per age, by archetype court (target 3-6, cap '
          f'{SLOT_CAP}):')
    print('  %-28s %s' % ('', ''.join(f'{a.split("_")[1][:5]:>7}' for a in AGE_ORDER)))
    thin = []
    for label, row in coverage(advances).items():
        marks = ''.join(f'{n:>7}' for n in row)
        print(f'  {label:<28}{marks}')
        for age, n in zip(AGE_ORDER, row):
            if n < 3:
                thin.append(f'{label} in {age}: {n}')
    if thin:
        print('\n  UNDER 3 AVAILABLE:')
        for t in thin:
            print('    ' + t)
    else:
        print('\n  every archetype has at least 3 offices in every age.')
    print('  counts above the cap are the pool a court chooses from, which is intended.')

    if args.check:
        print('\n--check: nothing written.')
        return 0

    for path, text in [(OUT_AUTOMOD, emit_auto_modifiers()),
                       (OUT_TRIGGERS, emit_triggers()),
                       (OUT_VALUES, emit_values()),
                       (OUT_EFFECTS, emit_effects() + emit_office_event_effects()),
                       (OUT_EVENTS, emit_events() + emit_office_events()),
                       (OUT_LOC, emit_loc() + emit_office_event_loc()),
                       (OUT_GUI, emit_gui()),
                       (OUT_ACTIONS, emit_actions())]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        print(f'wrote {path.relative_to(REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
