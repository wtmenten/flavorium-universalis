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

Rung 0 is entered the same way: a minister who returns from paid training holding no rung
trait at all is offered a career in the track they trained in. That offer is generated
here too, as one event per track (cc_xp.90/.91/.92) plus the effect that opens it.

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
OUT_CAREER_EVENTS = REPO / "in_game" / "events" / "cc_xp_career_events.txt"

# Branch-choice events are numbered from here, in ladder order.
BRANCH_EVENT_BASE = 20

# One career-entry event per track, opened from the matching training return event.
CAREER_EVENT = {"adm": "cc_xp.90", "dip": "cc_xp.91", "mil": "cc_xp.92"}

# How many of a track's careers are offered at once. Always fewer than the track has, so
# the court is offering what it can rather than presenting a catalogue: a player who wants
# a Navigator and is shown four other things trains again. The window rotates, so the same
# minister trained twice is unlikely to see the same list.
CAREER_OFFER_WINDOW = 4
CAREER_OFFER_MIN_WITHHELD = 1

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


def career_offer_plan() -> dict[str, dict]:
    """Per track: the ladders on it, and which offer rolls put each one on the menu.

    The roll picks a starting point in the track's ladder list and the window runs forward
    from there, wrapping. So there are exactly as many possible menus as the track has
    ladders, every ladder appears on the same number of them, and at least one career is
    always withheld. Expressing it as a rotation rather than as every combination keeps the
    generated option triggers to a handful of comparisons instead of ten apiece.
    """
    plan: dict[str, dict] = {}

    for track in ("adm", "dip", "mil"):
        ladders = [l for l in LADDERS if l["track"] == track]
        count = len(ladders)
        window = min(CAREER_OFFER_WINDOW, count - CAREER_OFFER_MIN_WITHHELD)

        # An offer roll of `o` (1-based) shows the ladders at index o-1 .. o-2+window,
        # wrapping. Inverted here: which rolls show ladder i.
        offers = {
            index: sorted(((index - step) % count) + 1 for step in range(window))
            for index in range(count)
        }

        plan[track] = {"ladders": ladders, "count": count,
                       "window": window, "offers": offers}

    return plan


# The mod's permission token. A trait gated on it is asking to be granted only by script
# that means to grant it, which every career option here does. It must NOT be copied into
# an option's trigger: the trigger runs before the effect sets it, so the option would be
# hidden forever.
GRANTING_TOKEN = "has_variable = cc_granting_trait"


def _strip_comments(text: str) -> str:
    return "\n".join(line.split("#", 1)[0] for line in text.splitlines())


def _blocks(text: str, indented: bool):
    """Yield (key, body) for every `key = { ... }` at the given indentation."""
    pattern = re.compile(
        (r"^[ \t]*" if indented else r"^") + r"([a-z_][a-z0-9_]*)\s*=\s*\{", re.M)
    index = 0
    while True:
        match = pattern.search(text, index)
        if not match:
            return
        depth = 0
        cursor = match.end() - 1
        while cursor < len(text):
            if text[cursor] == "{":
                depth += 1
            elif text[cursor] == "}":
                depth -= 1
                if depth == 0:
                    break
            cursor += 1
        yield match.group(1), text[match.end():cursor]
        index = cursor + 1


def _clauses(body: str) -> list[str]:
    """Split a trigger body into top-level clauses, keeping nested braces intact."""
    found: list[str] = []
    current = ""
    depth = 0
    for char in body:
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        current += char
        if depth == 0 and char == "}":
            found.append(" ".join(current.split()))
            current = ""
    for line in current.splitlines():
        line = line.strip()
        if line:
            found.append(" ".join(line.split()))
    return [c for c in found if c]


def load_entry_allows() -> dict[str, list[str]]:
    """The `allow` conditions on every ladder entry trait, as emittable clauses.

    These are NOT decoration. An add_trait whose allow block fails is refused SILENTLY, so
    a career option that ignores them looks like it worked, grants nothing, and eats the
    training that paid for it. Fourteen of the fifteen entry traits carry
    `NOT = { has_trait_category = cabinet }`, which a single age trait is enough to fail;
    seven carry `in_cabinet = yes`, which every protege fails; three want mil > 33 and two
    want all three stats under 33.

    Read from the trait files rather than restated here, so a trait whose allow block is
    edited cannot leave the picker offering something the engine will refuse.
    """
    entry_traits = {ladder["rungs"][0][0] for ladder in LADDERS}
    allows: dict[str, list[str]] = {trait: [] for trait in entry_traits}

    for path in sorted(TRAIT_DIR.glob("*.txt")):
        text = _strip_comments(path.read_text(encoding="utf-8-sig", errors="replace"))
        for name, body in _blocks(text, indented=False):
            if name not in entry_traits:
                continue
            for key, allow_body in _blocks(body, indented=True):
                if key != "allow":
                    continue
                allows[name] = [c for c in _clauses(allow_body)
                                if c.replace(" ", "") != GRANTING_TOKEN.replace(" ", "")]

    return allows


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

    # The career picker offers a rotating window of a track's ladders. A window of one
    # would be a menu with a single item, and a window equal to the track's ladder count
    # would withhold nothing, so both ends need a track with enough careers on it.
    for track, spec in career_offer_plan().items():
        if spec["window"] < 2:
            problems.append(
                f"{track}: only {spec['count']} ladder(s), too few to offer a career choice")

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

    # ------------------------------------------------------------ career offers ---
    plan = career_offer_plan()

    add("###############################################################################")
    add("# CAREER ENTRY")
    add("#")
    add("# Rung 0 used to be reachable only by the monthly trait dispatcher, which meant the")
    add("# player had no say at all in which of the fifteen careers a minister ended up on,")
    add("# and four ladders (reform, fiscal, envoy, exploration) were reachable by nothing:")
    add("# no event in the mod granted their entry trait.")
    add("#")
    add("# These effects are what fixes both. Called in CHARACTER scope from the training")
    add("# return events (cc_xp.30/.31/.32) when the returning minister holds no rung trait")
    add("# at all and the posting did not go badly. They stamp the flag the picker resolves")
    add("# its minister by and roll which careers are on the menu.")
    add("#")
    add("# The flag is timed rather than permanent so a picker the player somehow never sees")
    add("# expires instead of leaving a minister waiting forever. Two months is the same")
    add("# window cc_xp_branch_pending uses.")
    add("###############################################################################")

    for track in ("adm", "dip", "mil"):
        spec = plan[track]
        names = ", ".join(l["key"] for l in spec["ladders"])
        add("")
        add(f"# {track}: {spec['window']} of {spec['count']} offered ({names})")
        add(f"cc_xp_offer_career_{track} = {{")
        add(f"\tset_variable = {{ name = cc_xp_awaiting_career_{track}  value = yes  months = 2 }}")
        add("\trandom_list = {")
        for roll in range(1, spec["count"] + 1):
            shown = " ".join(
                spec["ladders"][index]["key"]
                for index in range(spec["count"])
                if roll in spec["offers"][index])
            add(f"\t\t1 = {{ set_variable = {{ name = cc_xp_career_offer  value = {roll}  months = 2 }} }}   # {shown}")
        add("\t}")
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

    # --------------------------------------------------------------- unladdered ---
    # Named exhaustively rather than through has_trait_category = cabinet, which is far
    # too broad to answer this question: 54 of the age traits and 8 of the afflictions
    # carry that category too, so a minister who once picked up an age trait would read
    # as already having a career and could never be offered one.
    rungs = sorted({trait for l in LADDERS for r in l["rungs"] for trait in r})

    add("###############################################################################")
    add("# Does this character hold no ladder trait at all?")
    add("#")
    add("# One career per minister is an invariant of this system: the cc_xp_ladder_advance")
    add("# chain is if/else_if keyed on trait, so a minister holding two rung traits would")
    add("# only ever climb whichever ladder the chain reaches first. Generation enforces the")
    add("# other half of it by refusing to let one trait sit on two ladders.")
    add("#")
    add("# This trigger is what keeps career ENTRY from breaking the invariant. Called in")
    add("# CHARACTER scope from the training return events.")
    add("###############################################################################")
    add("")
    add("cc_xp_is_unladdered = {")
    add("\tNOR = {")
    for trait in rungs:
        add(f"\t\thas_trait = {trait}")
    add("\t}")
    add("}")
    add("")

    # ------------------------------------------------------- career entry gates ---
    allows = load_entry_allows()
    plan = career_offer_plan()

    add("###############################################################################")
    add("# Could this character actually be given a career on the given track?")
    add("#")
    add("# Mirrors the `allow` block of each of the track's entry traits, which the picker")
    add("# cannot ignore: add_trait against a failing allow is refused SILENTLY, so an")
    add("# option that skipped this would look like it worked, grant nothing, and waste the")
    add("# training that paid for it.")
    add("#")
    add("# The conditions are read out of the trait files by the generator, so a trait whose")
    add("# allow block is edited cannot leave this trigger out of date.")
    add("#")
    add("# Called in CHARACTER scope from the training return events, which is what stops a")
    add("# picker ever opening for someone no career is available to.")
    add("###############################################################################")

    for track in ("adm", "dip", "mil"):
        add("")
        add(f"cc_xp_can_enter_career_{track} = {{")
        add("\tOR = {")
        for ladder in plan[track]["ladders"]:
            entry = ladder["rungs"][0][0]
            conditions = allows[entry]
            add(f"\t\t# {ladder['name']}: {entry}")
            if not conditions:
                # Nothing gates this one beyond the permission token the option supplies.
                add("\t\talways = yes")
                continue
            add("\t\tAND = {")
            for condition in conditions:
                add(f"\t\t\t{condition}")
            add("\t\t}")
        add("\t}")
        add("}")

    add("")

    return "\n".join(lines)


def render_career_events() -> str:
    plan = career_offer_plan()
    allows = load_entry_allows()
    lines: list[str] = []
    add = lines.append

    add("﻿namespace = cc_xp")
    add("")
    add("###############################################################################")
    add("# GENERATED FILE. Do not edit by hand.")
    add("#   python tools/generate_ladders.py")
    add("#")
    add("# CHOOSING A CAREER. One event per track, opened from that track's training return")
    add("# event when the minister who came back holds no ladder trait at all. This is the")
    add("# only way onto rung 0 that the player controls, and the only way at all onto the")
    add("# four ladders no event in the mod grants the entry trait for.")
    add("#")
    for track in ("adm", "dip", "mil"):
        spec = plan[track]
        add(f"#   {CAREER_EVENT[track]:10s} [{track}] {spec['window']} of {spec['count']}: "
            f"{', '.join(l['key'] for l in spec['ladders'])}")
    add("#")
    add("# THE MENU IS PARTIAL. Each opening shows a rotating window of the track's careers,")
    add("# rolled by cc_xp_offer_career_<track> at the moment the minister got back, so the")
    add("# court is offering what it can rather than presenting a catalogue. Every option is")
    add("# gated on that roll; the first also passes when the roll is somehow unset, which is")
    add("# the guard against an event with no available option and therefore no way to close")
    add("# it.")
    add("#")
    add("# There is no decline option, for the same reason the events in cc_xp_choice_events")
    add("# have none: the training that opened this was already paid for.")
    add("#")
    add("# The minister is identified by a timed flag rather than a saved scope, as")
    add("# everywhere else in this system. Two ministers back from the same posting in the")
    add("# same month resolve to different people, because selection clears the flag.")
    add("###############################################################################")

    for track in ("adm", "dip", "mil"):
        spec = plan[track]
        event = CAREER_EVENT[track]
        flag = f"cc_xp_awaiting_career_{track}"

        add("")
        add("")
        add(f"# {track.upper()}")
        add(f"{event} = {{")
        add("\ttype = country_event")
        add(f"\ttitle = {event}.title")
        add(f"\tdesc = {event}.desc")
        add("\toutcome = positive")
        add("")
        add("\tillustration_tags = {")
        add("\t\t10 = interior")
        add("\t}")
        add("")
        add("\ttrigger = {")
        add(f"\t\tany_character = {{ has_variable = {flag} }}")
        add("\t}")
        add("")
        add("\timmediate = {")
        add("\t\trandom_character = {")
        add(f"\t\t\tlimit = {{ has_variable = {flag} }}")
        add(f"\t\t\tremove_variable = {flag}")
        add("\t\t\tsave_scope_as = cc_xp_subject")
        add("\t\t}")
        add("\t}")

        for index, ladder in enumerate(spec["ladders"]):
            entry = ladder["rungs"][0][0]
            rolls = spec["offers"][index]

            add("")
            add(f"\t# {ladder['name']} -> {entry}")
            add("\toption = {")
            add(f"\t\tname = {event}.{'abcdefgh'[index]}")
            # trigger_if, not a bare var: read inside an OR. Reading an unset variable
            # errors with "Event target link 'var' returned an unset scope" rather than
            # evaluating false, and an OR does not save you from it: every branch is
            # reached. This is the same guard cc_xp_tier_at_least and its neighbours use.
            add("\t\ttrigger = {")
            add("\t\t\tscope:cc_xp_subject ?= {")
            for condition in allows[entry]:
                add(f"\t\t\t\t{condition}")
            add("\t\t\t\ttrigger_if = {")
            add("\t\t\t\t\tlimit = { has_variable = cc_xp_career_offer }")
            add("\t\t\t\t\tOR = {")
            for roll in rolls:
                add(f"\t\t\t\t\t\tvar:cc_xp_career_offer = {roll}")
            add("\t\t\t\t\t}")
            add("\t\t\t\t}")
            add("\t\t\t\t# The roll is unset only if the write did not commit. Fall back to")
            add("\t\t\t\t# offering everything this person is actually eligible for.")
            add("\t\t\t\ttrigger_else = { always = yes }")
            add("\t\t\t}")
            add("\t\t}")
            add("\t\tscope:cc_xp_subject ?= {")
            # The mod's permission token. No entry trait is gated on it today, but the
            # advancement chain sets it around every grant for the same reason: a gated
            # trait added to a ladder later must not silently fail to apply.
            add("\t\t\tset_variable = { name = cc_granting_trait  value = yes }")
            add(f"\t\t\tadd_trait = trait:{entry}")
            add("\t\t\tremove_variable = cc_granting_trait")
            add("\t\t\tif = {")
            add("\t\t\t\tlimit = { has_variable = cc_xp_career_offer }")
            add("\t\t\t\tremove_variable = cc_xp_career_offer")
            add("\t\t\t}")
            add("\t\t}")
            add("\t}")

        # Always available, and the only thing guaranteeing this event can be closed.
        # The offer gate in the return event means a picker only opens when at least one
        # career is available, but the rotation window is rolled independently of which
        # ones the person is eligible for, so a narrow case can still hide every career.
        # An event with no available option cannot be dismissed at all.
        add("")
        add("\t# No suitable career. Always available.")
        add("\toption = {")
        add(f"\t\tname = {event}.{'abcdefgh'[len(spec['ladders'])]}")
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

    plan = career_offer_plan()
    print("\nlocalisation keys required by the career-entry events:")
    for track in ("adm", "dip", "mil"):
        event = CAREER_EVENT[track]
        print(f"  {event}.title / .desc  ({track})")
        for index, ladder in enumerate(plan[track]["ladders"]):
            print(f"    {event}.{'abcdefgh'[index]}  -> {ladder['name']} "
                  f"({ladder['rungs'][0][0]})")


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
        (OUT_CAREER_EVENTS, render_career_events()),
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
