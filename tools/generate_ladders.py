#!/usr/bin/env python3
"""Generate the cabinet advancement ladders from the table below.

A ladder is one career: an ordered list of rungs, each holding one or more traits. The
rung index IS the track tier required to reach it, so a minister on rung 0 of an
administrative ladder needs cc_tier_adm >= 1 to reach rung 1, and so on. This replaces
the five hand-written chains in cc_progression_events.txt (cc_prog.1-40), which encoded
the same idea as four bespoke events each and could not be extended without writing four
more.

Where a rung lists several traits the ladder branches. Phase 2 picks between them with an
even random_list; phase 3 replaces that coin-flip with a player choice through the
training interactions.

Validation runs before anything is written, and any failure aborts without touching the
output. It checks that every named trait actually exists, that no trait appears on two
ladders (which would make "which ladder is this minister on" ambiguous), and that no
carve-out trait is used as a rung.

CARVE-OUTS, by source file rather than by tag:
  cc_age_traits.txt          era-granted, not earned
  cc_negative_traits.txt     afflictions inflicted by events, never a career step
  cc_estate_faction_traits.txt   who a minister is loyal to, not what they trained in
  plus anything tagged `legendary`

Note the deliberate exception: the malus entry traits in cabinet.txt and
cc_progression_traits.txt (fumbling_integrator, provocateur, timid_landlubber,
fumbling_reformist, ...) ARE tagged `negative` but are not in cc_negative_traits.txt.
Those are exactly the kiss-curse starting points the ladders are built on, so they are
allowed as rung 0. The nine genuine afflictions stay event-only.

    python tools/generate_ladders.py
    python tools/generate_ladders.py --check
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TRAIT_DIR = REPO / "in_game" / "common" / "traits"
OUT = REPO / "in_game" / "common" / "scripted_effects" / "cc_xp_ladders.txt"
OUT_TRIGGERS = REPO / "in_game" / "common" / "scripted_triggers" / "cc_xp_ladder_triggers.txt"
OUT_EVENTS = REPO / "in_game" / "events" / "cc_xp_branch_events.txt"

# Branch-choice events are numbered from here, in ladder order.
BRANCH_EVENT_BASE = 20

CARVE_OUT_FILES = {
    "cc_age_traits.txt",
    "cc_negative_traits.txt",
    "cc_estate_faction_traits.txt",
}

# Traits reached only through the legend quest chains in cc_legend_events.txt.
# Tagged `legendary` or gated on has_variable = cc_granting_trait.
CARVE_OUT_TRAITS = {
    "grand_vizier_legendary",
    "tribune_of_the_people",
    "philosopher_king",
    "legendary_navigator",
    "retired_legend",
}


###############################################################################
# THE LADDERS
#
# rungs[0] is the entry trait, granted by the trait dispatcher like any other.
# rungs[N] requires tier N in the ladder's track.
###############################################################################

LADDERS = [
    # ---------------------------------------------------------------- ADM ---
    {
        "key": "reform",
        "track": "adm",
        "name": "The Reformer's Path",
        "rungs": [
            ["fumbling_reformist"],
            ["law_reformer"],
            ["progressive_reformist"],
            ["master_reformer"],
        ],
    },
    {
        "key": "fiscal",
        "track": "adm",
        "name": "The Treasury",
        "rungs": [
            ["clumsy_accountant"],
            ["loyal_steward"],
            ["prosperity_planner", "treasury_enforcer"],
            ["development_patron"],
        ],
    },
    {
        "key": "learning",
        "track": "adm",
        "name": "The Scholar's Path",
        "rungs": [
            ["learned_courtier"],
            ["learned_counselor"],
            ["progressive_rationalist"],
            ["enlightenment_herald", "humanist_philosopher"],
        ],
    },
    {
        "key": "urbanism",
        "track": "adm",
        "name": "The Builder",
        "rungs": [
            ["urban_planner"],
            ["master_urbanist"],
            ["grand_architect"],
        ],
    },
    {
        "key": "law",
        "track": "adm",
        "name": "The Jurist",
        "rungs": [
            ["legal_scholar"],
            ["efficiency_administrator"],
            ["estate_guardian", "regional_magnate"],
        ],
    },
    {
        "key": "integration",
        "track": "adm",
        "name": "The Integrator",
        "rungs": [
            ["fumbling_integrator"],
            ["able_integrator"],
            ["seasoned_integrator"],
            ["master_integrator", "iron_integrator"],
        ],
    },
    # ---------------------------------------------------------------- DIP ---
    {
        "key": "envoy",
        "track": "dip",
        "name": "The Diplomat's Ascent",
        "rungs": [
            ["tentative_envoy"],
            ["tactful_envoy", "diplomatic_attache"],
            ["master_statesman"],
            ["grand_chancellor"],
        ],
    },
    {
        "key": "colonial",
        "track": "dip",
        "name": "The Colonial Hand",
        "rungs": [
            ["frontier_administrator"],
            ["new_world_pioneer"],
            ["colonial_planner"],
            ["returned_colonial_governor"],
        ],
    },
    {
        "key": "trade",
        "track": "dip",
        "name": "The Merchant's Road",
        "rungs": [
            ["merchant_syndic"],
            ["mercantilist_official", "free_market_advocate"],
            ["maritime_champion"],
            ["merchant_prince"],
        ],
    },
    {
        "key": "exploration",
        "track": "dip",
        "name": "The Navigator",
        "rungs": [
            ["timid_landlubber"],
            ["capable_explorer"],
            ["restless_pioneer"],
            ["admiral_counselor"],
        ],
    },
    {
        "key": "intrigue",
        "track": "dip",
        "name": "The Shadow",
        "rungs": [
            ["provocateur"],
            ["espionage_director"],
            ["shadow_counselor"],
        ],
    },
    # ---------------------------------------------------------------- MIL ---
    {
        "key": "command",
        "track": "mil",
        "name": "The Military Hardening",
        "rungs": [
            ["green_adjutant"],
            ["tactical_advisor"],
            ["offensive_strategist", "defensive_commander"],
            ["supreme_commander", "continental_marshal"],
        ],
    },
    {
        "key": "drill",
        "track": "mil",
        "name": "The Drillmaster",
        "rungs": [
            ["infantry_drillmaster"],
            ["elite_trainer"],
            ["iron_disciplinarian"],
            ["mass_levy_commander"],
        ],
    },
    {
        "key": "siege",
        "track": "mil",
        "name": "The Engineer",
        "rungs": [
            ["military_engineer"],
            ["siege_engineer"],
            ["commissariat_officer"],
        ],
    },
    {
        "key": "cavalry",
        "track": "mil",
        "name": "The Horse",
        "rungs": [
            ["scout_captain"],
            ["master_of_horse"],
            ["cavalry_marshal"],
        ],
    },
]


###############################################################################

TOP_LEVEL = re.compile(r"^([a-z_][a-z0-9_]*)\s*=\s*\{")


def branch_points() -> list[dict]:
    """Every rung transition whose destination offers a choice, in stable ladder order.

    Each gets its own event id so the event's immediate block can identify the minister
    by the trait they are leaving. Two ministers branching in the same year therefore
    resolve independently instead of racing for one saved scope.
    """
    found: list[dict] = []
    for ladder in LADDERS:
        for index in range(len(ladder["rungs"]) - 1):
            destinations = ladder["rungs"][index + 1]
            if len(destinations) < 2:
                continue
            for current in ladder["rungs"][index]:
                found.append({
                    "ladder": ladder["key"],
                    "name": ladder["name"],
                    "track": ladder["track"],
                    "tier": index + 1,
                    "from": current,
                    "to": destinations,
                    "event": f"cc_xp.{BRANCH_EVENT_BASE + len(found)}",
                })
    return found


def load_traits() -> tuple[dict[str, str], set[str]]:
    """Return ({trait: source filename}, {carved out traits})."""
    where: dict[str, str] = {}
    carved: set[str] = set(CARVE_OUT_TRAITS)

    for path in sorted(TRAIT_DIR.glob("*.txt")):
        depth = 0
        for raw in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            line = raw.split("#", 1)[0]
            if depth == 0:
                match = TOP_LEVEL.match(line)
                if match:
                    name = match.group(1)
                    where[name] = path.name
                    if path.name in CARVE_OUT_FILES:
                        carved.add(name)
            depth += line.count("{") - line.count("}")
            if depth < 0:
                depth = 0

    return where, carved


def validate(where: dict[str, str], carved: set[str]) -> list[str]:
    problems: list[str] = []
    seen: dict[str, str] = {}

    for ladder in LADDERS:
        key = ladder["key"]

        if ladder["track"] not in ("adm", "dip", "mil"):
            problems.append(f"{key}: track must be adm/dip/mil, got {ladder['track']!r}")

        if len(ladder["rungs"]) < 2:
            problems.append(f"{key}: a ladder needs at least two rungs")

        if len(ladder["rungs"]) > 4:
            problems.append(
                f"{key}: {len(ladder['rungs'])} rungs, but tiers only run 0-3")

        for index, rung in enumerate(ladder["rungs"]):
            if not rung:
                problems.append(f"{key}: rung {index} is empty")
            for trait in rung:
                if trait not in where:
                    problems.append(f"{key} rung {index}: trait {trait!r} does not exist")
                elif trait in carved:
                    problems.append(
                        f"{key} rung {index}: {trait!r} is a carve-out "
                        f"(from {where[trait]}) and cannot be a ladder rung")
                if trait in seen:
                    problems.append(
                        f"{key} rung {index}: {trait!r} is already on ladder {seen[trait]!r}")
                else:
                    seen[trait] = key

    return problems


def render_effects() -> str:
    lines: list[str] = []
    add = lines.append

    branches = branch_points()
    event_for = {(b["ladder"], b["tier"] - 1, b["from"]): b["event"] for b in branches}

    total_rungs = sum(len(l["rungs"]) for l in LADDERS)

    add("﻿###############################################################################")
    add("# GENERATED FILE. Do not edit by hand.")
    add("#   python tools/generate_ladders.py")
    add("#")
    add("# Cabinet advancement ladders. Each ladder is one career; a rung's index is the")
    add("# track tier required to reach it. Replaces the five hand-written chains that")
    add("# used to live in cc_progression_events.txt as cc_prog.1-40.")
    add("#")
    add(f"#   {len(LADDERS)} ladders, {total_rungs} rungs, {len(branches)} branch points")
    for ladder in LADDERS:
        path = " -> ".join("|".join(r) for r in ladder["rungs"])
        add(f"#   [{ladder['track']}] {ladder['key']}: {path}")
    add("#")
    add("# Called in CHARACTER scope from cc_xp_yearly_advance (cc_xp_pulse.txt). Advances")
    add("# at most one rung per call: the if/else_if chain stops at the first match, and the")
    add("# cooldown stamped at the end keeps a minister who has banked several tiers from")
    add("# sprinting up the whole ladder in consecutive years.")
    add("#")
    add("# Branch rungs put the choice to the player through one event per branch point")
    add("# (cc_xp_branch_events.txt). AI courts still roll for it, so the pulse never stalls")
    add("# waiting on a decision nobody is there to make.")
    add("###############################################################################")
    add("")
    add("cc_xp_ladder_advance = {")

    first = True
    for ladder in LADDERS:
        track = ladder["track"]
        add("")
        add(f"\t# ---- {ladder['key']} ({track}): {ladder['name']} ----")

        for index in range(len(ladder["rungs"]) - 1):
            here = ladder["rungs"][index]
            nxt = ladder["rungs"][index + 1]
            required = index + 1

            for current in here:
                keyword = "if" if first else "else_if"
                first = False

                add(f"\t{keyword} = {{")
                add("\t\tlimit = {")
                add(f"\t\t\thas_trait = {current}")
                add(f"\t\t\tcc_xp_tier_at_least = {{ TRACK = {track}  TIER = {required} }}")
                add("\t\t}")
                if len(nxt) == 1:
                    # Several destination traits carry allow = { has_variable = cc_granting_trait },
                    # the mod's permission token: without it the engine silently refuses the
                    # add_trait and the minister ends up holding nothing at all. Set it around
                    # every grant rather than only the ones that currently need it, so adding a
                    # gated trait to a ladder later cannot quietly break this.
                    add(f"\t\tremove_trait = trait:{current}")
                    add("\t\tset_variable = { name = cc_granting_trait  value = yes }")
                    add(f"\t\tadd_trait = trait:{nxt[0]}")
                    add("\t\tremove_variable = cc_granting_trait")
                    add("\t\tcc_xp_stamp_advance = yes")
                else:
                    event = event_for[(ladder["key"], index, current)]
                    add("\t\t# Branch. A human court is asked; an AI court decides for itself.")
                    add("\t\tif = {")
                    add("\t\t\tlimit = { scope:cc_xp_court ?= { is_ai = no } }")
                    add("\t\t\tset_variable = { name = cc_xp_branch_pending  value = yes  months = 2 }")
                    add(f"\t\t\tscope:cc_xp_court ?= {{ trigger_event_silently = {{ id = {event} }} }}")
                    add("\t\t}")
                    add("\t\telse = {")
                    add(f"\t\t\tremove_trait = trait:{current}")
                    add("\t\t\tset_variable = { name = cc_granting_trait  value = yes }")
                    add("\t\t\trandom_list = {")
                    for destination in nxt:
                        add(f"\t\t\t\t1 = {{ add_trait = trait:{destination} }}")
                    add("\t\t\t}")
                    add("\t\t\tremove_variable = cc_granting_trait")
                    add("\t\t\tcc_xp_stamp_advance = yes")
                    add("\t\t}")

                add("\t}")

    add("}")
    add("")
    add("###############################################################################")
    add("# Bookkeeping applied after any successful advancement. Split out so the chain")
    add("# above stays readable and so there is one place to add a notification later.")
    add("###############################################################################")
    add("")
    add("cc_xp_stamp_advance = {")
    # Literal, not a script value: the engine parses duration fields as raw tokens, and a
    # script value here fails SILENTLY (unlike trigger_event, which at least errors).
    # See the note in script_values/cc_xp_values.txt.
    add("\tset_variable = { name = cc_xp_advance_cd  value = yes  years = 4 }")
    add("\tset_variable = { name = cc_xp_advanced_recently  value = yes  months = 2 }")
    add("}")
    add("")

    # ---------------------------------------------------------------- backfill ---
    # Group by (track, tier) so a minister holding any rung-N trait of a track gets that
    # track floored at tier N, rather than emitting one branch per trait.
    seeds: dict[tuple[str, int], list[str]] = {}
    for ladder in LADDERS:
        for index, rung in enumerate(ladder["rungs"]):
            if index == 0:
                continue  # rung 0 is the entry trait: no experience implied
            seeds.setdefault((ladder["track"], index), []).extend(rung)

    add("###############################################################################")
    add("# ONE-TIME SEEDING")
    add("#")
    add("# Called from cc_xp_init the first time a character enters the system. A minister")
    add("# who already holds a rung-N ladder trait is credited with enough experience in")
    add("# that track to sit at tier N, so they carry on from where their career actually")
    add("# is instead of restarting at zero.")
    add("#")
    add("# This is what carries an existing save across the phase 2 change. The old chains")
    add("# tracked progress in cc_prog_* counters that nothing reads any more; a minister")
    add("# who finished one is recognised here by the TRAIT they ended up with, which is")
    add("# the part that survived. Without it, a minister who spent twelve years becoming")
    add("# a progressive_reformist would need decades more to advance again.")
    add("#")
    add("# It also does the right thing for a fresh grant: a trait event that hands out a")
    add("# rung-2 trait directly leaves that minister correctly placed on the ladder.")
    add("#")
    add("# Floors rather than overwrites, so a minister who has genuinely earned more keeps it.")
    add("###############################################################################")
    add("")
    add("cc_xp_ladder_backfill = {")

    for (track, tier) in sorted(seeds):
        traits = sorted(set(seeds[(track, tier)]))
        add("")
        add(f"\t# {track} rung {tier}")
        add("\tif = {")
        add("\t\tlimit = {")
        add("\t\t\tOR = {")
        for trait in traits:
            add(f"\t\t\t\thas_trait = {trait}")
        add("\t\t\t}")
        add(f"\t\t\tvar:cc_xp_{track} < cc_xp_tier_{tier}_at")
        add("\t\t}")
        add(f"\t\tset_variable = {{ name = cc_xp_{track}  value = cc_xp_tier_{tier}_at }}")
        add("\t}")

    add("")
    add("\tcc_xp_resum = yes")
    add("}")
    add("")
    add("###############################################################################")
    add("# Recompute the stored total from the three tracks. Needed after any effect that")
    add("# writes a track variable directly instead of going through cc_xp_gain_*.")
    add("###############################################################################")
    add("")
    add("cc_xp_resum = {")
    add("\tset_variable    = { name = cc_xp_total  value = var:cc_xp_adm }")
    add("\tchange_variable = { name = cc_xp_total  add   = var:cc_xp_dip }")
    add("\tchange_variable = { name = cc_xp_total  add   = var:cc_xp_mil }")
    add("}")
    add("")

    return "\n".join(lines)


def render_triggers() -> str:
    lines: list[str] = []
    add = lines.append

    add("﻿###############################################################################")
    add("# GENERATED FILE. Do not edit by hand.")
    add("#   python tools/generate_ladders.py")
    add("#")
    add("# Mirror of the cc_xp_ladder_advance chain, as a trigger. Used by the yearly")
    add("# advancement pulse to answer \"is there anything to do here\" before entering the")
    add("# effect, and by the notification event to find the minister who just advanced.")
    add("#")
    add("# Called in CHARACTER scope.")
    add("###############################################################################")
    add("")
    add("cc_xp_can_advance = {")
    add("\tNOT = { has_variable = cc_xp_advance_cd }")
    add("\tOR = {")

    for ladder in LADDERS:
        track = ladder["track"]
        add(f"\t\t# {ladder['key']} ({track})")
        for index in range(len(ladder["rungs"]) - 1):
            required = index + 1
            for current in ladder["rungs"][index]:
                add("\t\tAND = {")
                add(f"\t\t\thas_trait = {current}")
                add(f"\t\t\tcc_xp_tier_at_least = {{ TRACK = {track}  TIER = {required} }}")
                add("\t\t}")

    add("\t}")
    add("}")
    add("")

    return "\n".join(lines)


def render_events() -> str:
    branches = branch_points()
    lines: list[str] = []
    add = lines.append

    add("﻿namespace = cc_xp")
    add("")
    add("###############################################################################")
    add("# GENERATED FILE. Do not edit by hand.")
    add("#   python tools/generate_ladders.py")
    add("#")
    add("# One event per ladder branch point. Fired by cc_xp_ladder_advance when a HUMAN")
    add("# court's minister has earned a rung that offers a choice of destination.")
    add("#")
    add("# The advancement has NOT happened yet when this opens: each option performs its")
    add("# own trait swap. There is deliberately no dismiss option, because closing the")
    add("# event without choosing would strand the minister on the old rung with the")
    add("# cooldown unspent, and the event would simply fire again next year.")
    add("#")
    add("# Each event identifies its minister by the trait they are LEAVING as well as the")
    add("# cc_xp_branch_pending flag, so two ministers branching in the same year cannot")
    add("# resolve into each other.")
    add("#")
    for b in branches:
        add(f"#   {b['event']:10s} [{b['track']}] {b['ladder']}: "
            f"{b['from']} -> {' | '.join(b['to'])}")
    add("###############################################################################")

    for b in branches:
        add("")
        add("")
        add(f"# {b['name']}: {b['from']} -> {' or '.join(b['to'])}")
        add(f"{b['event']} = {{")
        add("\ttype = country_event")
        add(f"\ttitle = {b['event']}.title")
        add(f"\tdesc = {b['event']}.desc")
        add("\toutcome = positive")
        add("")
        add("\tillustration_tags = {")
        add("\t\t10 = interior")
        add("\t}")
        add("")
        add("\ttrigger = {")
        add("\t\tany_character = {")
        add(f"\t\t\thas_trait = {b['from']}")
        add("\t\t\thas_variable = cc_xp_branch_pending")
        add("\t\t}")
        add("\t}")
        add("")
        add("\timmediate = {")
        add("\t\trandom_character = {")
        add("\t\t\tlimit = {")
        add(f"\t\t\t\thas_trait = {b['from']}")
        add("\t\t\t\thas_variable = cc_xp_branch_pending")
        add("\t\t\t}")
        add("\t\t\tremove_variable = cc_xp_branch_pending")
        add("\t\t\tsave_scope_as = cc_xp_subject")
        add("\t\t}")
        add("\t}")

        for suffix, destination in zip("abcd", b["to"]):
            add("")
            add("\toption = {")
            add(f"\t\tname = {b['event']}.{suffix}")
            add("\t\tscope:cc_xp_subject = {")
            add(f"\t\t\tremove_trait = trait:{b['from']}")
            add("\t\t\tset_variable = { name = cc_granting_trait  value = yes }")
            add(f"\t\t\tadd_trait = trait:{destination}")
            add("\t\t\tremove_variable = cc_granting_trait")
            add("\t\t\tcc_xp_stamp_advance = yes")
            add("\t\t}")
            add("\t}")

        add("}")

    add("")
    return "\n".join(lines)


def report_loc_keys() -> None:
    branches = branch_points()
    print("\nlocalisation keys required by the branch events:")
    for b in branches:
        print(f"  {b['event']}.title / .desc  ({b['ladder']}: {b['from']})")
        for suffix, destination in zip("abcd", b["to"]):
            print(f"    {b['event']}.{suffix}  -> {destination}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                       help="exit 1 if the generated files are missing or stale")
    args = parser.parse_args()

    where, carved = load_traits()
    if not where:
        print("error: no traits found, refusing to generate", file=sys.stderr)
        return 2

    problems = validate(where, carved)
    if problems:
        print(f"error: {len(problems)} problem(s) in the ladder table:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 2

    outputs = [
        (OUT, render_effects()),
        (OUT_TRIGGERS, render_triggers()),
        (OUT_EVENTS, render_events()),
    ]

    if args.check:
        stale = False
        for path, rendered in outputs:
            if not path.exists():
                print(f"stale: {path.relative_to(REPO)} does not exist", file=sys.stderr)
                stale = True
            elif path.read_text(encoding="utf-8-sig") != rendered.lstrip("﻿"):
                print(f"stale: {path.relative_to(REPO)} differs", file=sys.stderr)
                stale = True
        if stale:
            return 1
        print("up to date")
        return 0

    for path, rendered in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO)}")

    covered = sum(len(r) for l in LADDERS for r in l["rungs"])
    print(f"{len(LADDERS)} ladders covering {covered} traits, validated against "
          f"{len(where)} defined traits ({len(carved)} carved out)")
    report_loc_keys()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
