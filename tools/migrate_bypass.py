#!/usr/bin/env python3
"""Close the ladder bypass in the pre-XP court events.

THE PROBLEM. 47 of the 63 ladder traits could be granted directly by a random event,
bypassing the experience system entirely. 36 of those are higher rungs, including four
tier-3 capstones: a player could be handed supreme_commander by a monthly roll without
ever having earned mil tier 3.

THE FIX. Every option that grants a ladder rung is split in two by `is_ai`:

  the AI option    keeps the original name and the original effect, unchanged
  the human option gets a generated name and awards experience in the rung's track

Only one is ever visible, so a player sees the same number of options as before and no
event can overflow the option list. AI courts are untouched, because nothing offers an
AI a choice and the random path is the only path it has; an AI still climbs afterwards
through cc_xp_ladder_advance.

WHY NOT AN if/else INSIDE THE EFFECT. It would be a smaller diff, but the option text
names the trait ("Appoint [minister.GetName] as [ShowTraitName('cavalry_marshal')]"),
so a human choosing it and not receiving it would be a lie. The generated human option
says what actually happens: they train toward it.

WHY NOT SIMPLY ZERO THE DISPATCHER BRANCH. Only 18 of the 24 events are dispatcher-fired.
The rest come from other pulses, and 7 of the 18 mix ladder-rung options with off-ladder
options that must keep firing, so zeroing the branch would kill those too.

WHAT IS LEFT ALONE, and why each is not a bypass:

  Already gated       Options carrying cc_xp_dispatch_ready / cc_xp_tier_at_least. They
                      require the tier before granting the rung, so they are a shortcut
                      past the one-year advance wait, not a way around the tier.
  create_character    A newly created NPC arriving with a starting trait. Nothing is
                      being handed to a minister the player has been developing.
  Multi-grant options An if/else_if chain granting whichever trait a dying elder held
                      (cc_legacy.1). That is a TRANSFER inside the court, paid for with
                      the elder, not a grant from nothing. Collapsing the chain into one
                      experience award would also destroy it. These are reported rather
                      than rewritten, so a new one cannot slip through unnoticed.

Idempotent: an option already carrying the generated marker is skipped, so re-running
after adding new events only touches the new ones.

    python tools/migrate_bypass.py            # dry run, prints every rewrite
    python tools/migrate_bypass.py --apply
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVENTS = REPO / "in_game" / "events"
LOC = REPO / "in_game" / "localization" / "english"
OUT_LOC = LOC / "cc_xp_toward_l_english.yml"
OUT_AWARD_LOC = LOC / "cc_xp_award_l_english.yml"
VALUES = REPO / "in_game" / "common" / "script_values" / "cc_xp_values.txt"

MARKER = "cc_xp_toward_"

# Rung index -> (script value, human-readable band) for the experience award.
BAND = {
    0: "cc_xp_field_award_entry",
    1: "cc_xp_field_award_low",
    2: "cc_xp_field_award_mid",
    3: "cc_xp_field_award_high",
}

TRACK_NAME = {"adm": "administrative", "dip": "diplomatic", "mil": "military"}

GATE_RE = re.compile(r"cc_xp_(dispatch_ready|tier_at_least|level_at_least)")
TRAIT_RE = re.compile(r"add_trait = trait:([a-zA-Z_0-9]+)")

# The single-line form every gated rung option in the mod uses. Captured whole so the
# fallback can negate it verbatim: rebuilding it from the parsed parts would drift the
# moment somebody writes the gate differently.
GATE_LINE_RE = re.compile(
    r"^(?P<indent>\t+)(?P<gate>scope:(?P<scope>[a-zA-Z_0-9]+) = \{ "
    r"cc_xp_dispatch_ready = \{ TRACK = (?P<track>adm|dip|mil)\s+TIER = (?P<tier>\d) \} \})"
    r"[ \t]*$", re.M)


def award_key(track: str, band: str) -> str:
    """Loc key for the tooltip on an experience award."""
    return "cc_xp_award_%s_%s" % (track, band.rsplit("_", 1)[-1])


def wrap_award(indent: str, track: str, band: str, why: str) -> str:
    """The experience award, with a tooltip that says what it grants.

    WHY THE TOOLTIP IS NOT OPTIONAL. cc_xp_gain_* is three change_variable calls on
    cc_xp_adm / cc_xp_total, and the engine renders a raw variable write as nothing a
    player can read. Playtesting: "cc_cond.20 and cc_cond.24 are firing with only the
    dismiss option ... im guessing they are giving xp or something but its not explained
    in the button tooltip". Half of that report is the missing options below; this is the
    other half, and it applies to every generated option, not only the new ones.

    custom_tooltip with a body replaces the auto-generated text for everything inside it,
    which is exactly the substitution wanted here: one readable line instead of three
    unreadable ones. Block form from vanilla civil_war.txt:32.
    """
    return (f"{indent}# {why}\n"
            f"{indent}custom_tooltip = {{\n"
            f"{indent}\ttext = {award_key(track, band)}\n"
            f"{indent}\tcc_xp_gain_{track} = {{ AMOUNT = {band} }}\n"
            f"{indent}\tcc_xp_recompute = yes\n"
            f"{indent}}}")


def load_award_values() -> dict:
    """The four band script values, read rather than hardcoded.

    The tooltip loc states the number, so it has to come from the same place the effect
    does. cc_xp_values.txt calls these "the only place the conversion's balance lives";
    a retune there rewrites the loc on the next run instead of silently lying.
    """
    text = VALUES.read_text(encoding="utf-8-sig")
    out = {}
    for m in re.finditer(r"^(cc_xp_field_award_\w+)\s*=\s*\{\s*value\s*=\s*(\d+)\s*\}",
                         text, re.M):
        out[m.group(1)] = int(m.group(2))
    missing = set(BAND.values()) - set(out)
    if missing:
        raise SystemExit("ERROR: could not read award values from cc_xp_values.txt: "
                         + ", ".join(sorted(missing)))
    return out


def load_ladders():
    spec = importlib.util.spec_from_file_location(
        "gen_ladders", Path(__file__).resolve().parent / "generate_ladders.py")
    mod = importlib.util.module_from_spec(spec)
    saved, sys.argv = sys.argv, ["generate_ladders.py", "--check"]
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    finally:
        sys.argv = saved
    out = {}
    for ladder in mod.LADDERS:
        for rung, traits in enumerate(ladder["rungs"]):
            for t in traits:
                out[t] = (ladder["track"], rung)
    return out


def split_options(text: str, ladder: dict, report: list, filename: str):
    """Rewrite every ungated ladder-rung option in one file's text."""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    touched = 0
    used_traits: set[str] = set()
    cur_event = "?"

    while i < len(lines):
        m = re.match(r"^([a-zA-Z_0-9]+\.\d+) = \{", lines[i])
        if m:
            cur_event = m.group(1)

        if re.match(r"^\toption = \{", lines[i]):
            depth, body, j = 0, [], i
            while j < len(lines):
                depth += lines[j].count("{") - lines[j].count("}")
                body.append(lines[j])
                j += 1
                if depth <= 0:
                    break
            block = "\n".join(body)

            traits = [t for t in TRAIT_RE.findall(block) if t in ladder]
            gated = bool(GATE_RE.search(block))

            # Idempotency has to look at BOTH halves of an already-split pair. The human
            # half carries the marker, but the AI half keeps its original name and still
            # holds an ungated add_trait, so checking only the marker re-splits the AI
            # option on every run and produces `trigger = { is_ai = yes  is_ai = yes }`.
            already = MARKER in block or "is_ai = yes" in block or "is_ai = no" in block

            if len(set(traits)) > 1 and not already:
                SKIPPED.append((filename, cur_event, sorted(set(traits)),
                                "multi-grant chain, treated as a transfer"))

            if len(set(traits)) == 1 and not already and not gated:
                trait = traits[0]
                track, rung = ladder[trait]
                name_m = re.search(r"^\t\tname = ([A-Za-z_0-9.]+)", block, re.M)
                oname = name_m.group(1) if name_m else "?"

                ai_block = inject_trigger(body, "is_ai = yes")
                human_block = build_human_option(body, trait, track, rung)

                out.extend(ai_block)
                out.append("")
                out.extend(human_block)
                out.append("")
                touched += 1
                used_traits.add(trait)
                report.append((filename, cur_event, oname, trait, track, rung,
                               BAND[rung]))
                i = j
                continue

            out.extend(body)
            i = j
            continue

        out.append(lines[i])
        i += 1

    return "\n".join(out), touched, used_traits


def add_gated_fallbacks(text: str, ladder: dict, report: list, filename: str):
    """Give every tier-gated rung option a partner for the case where the tier is short.

    THE BUG THIS CLOSES, reported from playtesting: "cc_cond.20 and cc_cond.24 are firing
    with only the dismiss option".

    The first pass deliberately leaves gated options alone, and the docstring at the top
    of this file explains why: they demand the tier before granting the rung, so they are
    not a bypass. That reasoning is still right, and it has a side effect nobody costed.
    An option whose trigger fails is not greyed out, it is ABSENT, so a minister who has
    not reached the tier removes the option from the event entirely. cc_cond.24's six
    options were all gated and none of them were split, so a player whose selected
    minister was below tier saw an event with one button on it that did nothing.

    42 options across 9 events were in that state, and 20 of the 42 sit in .20 and .24.

    THE FIX is a partner option rather than an is_ai split, because these two cases are
    genuinely different outcomes and both are worth offering:

        tier earned      the original option, unchanged, grants the trait
        tier not earned  train toward it: experience in the gate's own track

    The gate line is negated verbatim into the partner's trigger, so exactly one of the
    pair is ever visible and the event has the same button count it always had. No is_ai
    condition: an AI below the tier was getting nothing here either, and progress toward
    the rung is strictly better for it than a dismissal.

    THE AWARD FOLLOWS THE GATE, not the ladder. The gate says which track and tier the
    option is asking for, so that is the track the experience goes into and the band it is
    worth. Where the ladder disagrees with the gate the mismatch is reported rather than
    silently resolved, since it means one of the two is wrong about the trait.

    LADDER MEMBERSHIP IS NOT REQUIRED HERE, unlike in the first pass. 34 of the 42 grant a
    trait that is not a rung at all: the tier gate on those is a seniority requirement for
    an appointment, not a ladder position. A bypass tool has no reason to look at them and
    that is why they were missed, but the player-facing failure is identical, and it is
    where nearly all of it is (every option in .21, .22, .23 and .24 on this list is a
    non-rung trait). The only difference is what the fallback means, which is carried in
    the generated comment: a rung the ladder will eventually hand over on its own, against
    standing the minister has to reach before the event can offer the post again.
    """
    lines = text.split("\n")

    # IDEMPOTENCY, and it needs its own pass. The partner is a SEPARATE option block, so the
    # original gated option still looks exactly as it did before it was partnered: it carries no
    # marker and no is_ai condition. Matching on the block alone therefore re-fires on every run
    # and a second --apply would give every gated option a second partner.
    #
    # The precise test is whether this event already contains a marker option for this trait
    # whose trigger carries a NEGATED gate. Testing for a marker option alone would be wrong:
    # cc_cond.20 has a cc_xp_toward_legal_scholar from the is_ai split, and a gated option for
    # the same trait in the same event would still need partnering.
    partnered: set = set()
    ev = "?"
    for k, line in enumerate(lines):
        m = re.match(r"^([a-zA-Z_0-9]+\.\d+) = \{", line)
        if m:
            ev = m.group(1)
        m = re.match(r"^\t\tname = %s(\w+)" % MARKER, line)
        if m:
            window = "\n".join(lines[k:k + 12])
            if re.search(r"NOT = \{ scope:\w+ = \{ cc_xp_dispatch_ready", window):
                partnered.add((ev, m.group(1)))

    out: list[str] = []
    i = 0
    touched = 0
    used_traits: set[str] = set()
    cur_event = "?"

    while i < len(lines):
        m = re.match(r"^([a-zA-Z_0-9]+\.\d+) = \{", lines[i])
        if m:
            cur_event = m.group(1)

        if re.match(r"^\toption = \{", lines[i]):
            depth, body, j = 0, [], i
            while j < len(lines):
                depth += lines[j].count("{") - lines[j].count("}")
                body.append(lines[j])
                j += 1
                if depth <= 0:
                    break
            block = "\n".join(body)

            traits = sorted(set(TRAIT_RE.findall(block)))
            gate = GATE_LINE_RE.search(block)
            # is_ai = yes options are the AI half of an already-split pair and have a
            # human partner already. MARKER means this IS a generated partner.
            already = (MARKER in block or "is_ai = yes" in block
                       or (len(traits) == 1 and (cur_event, traits[0]) in partnered))

            if len(traits) == 1 and gate and not already:
                trait = traits[0]
                track, tier = gate.group("track"), int(gate.group("tier"))
                band = BAND[tier]
                if trait in ladder:
                    l_track, l_rung = ladder[trait]
                    if (l_track, l_rung) != (track, tier):
                        SKIPPED.append((filename, cur_event, [trait],
                                        f"gate says {track} tier {tier}, ladder says "
                                        f"{l_track} rung {l_rung}; award follows the gate"))
                    why = ("Ladder rung withheld: the ladder grants it once the tier is "
                           "earned.")
                else:
                    why = ("Not a ladder rung. The tier is a standing requirement for the "
                           "post, so this buys standing, not the post.")

                out.extend(body)
                out.append("")
                out.extend(build_fallback_option(body, gate, trait, track, band, why))
                out.append("")
                touched += 1
                used_traits.add(trait)
                name_m = re.search(r"^\t\tname = ([A-Za-z_0-9.]+)", block, re.M)
                report.append((filename, cur_event,
                               name_m.group(1) if name_m else "?", trait, track, tier,
                               band))
                i = j
                continue

            out.extend(body)
            i = j
            continue

        out.append(lines[i])
        i += 1

    return "\n".join(out), touched, used_traits


def build_fallback_option(body: list[str], gate, trait: str, track: str,
                          band: str, why: str) -> list[str]:
    """The partner shown when the minister has not reached the gated tier."""
    out: list[str] = []
    for line in body:
        if re.match(r"^\t\tname = ", line):
            out.append(f"\t\tname = {MARKER}{trait}")
            continue
        # Negate the gate in place, so the partner keeps every other condition the
        # original had (the societal-value test, an estate check, whatever it is).
        gm = GATE_LINE_RE.match(line)
        if gm:
            out.append(f"{gm.group('indent')}NOT = {{ {gm.group('gate')} }}")
            continue
        out.append(line)

    text = "\n".join(out)

    text, n_line = re.subn(
        r"^(\t+)add_trait = trait:%s[ \t]*$" % re.escape(trait),
        lambda m: wrap_award(m.group(1), track, band, why), text, flags=re.M)
    if n_line == 0:
        # The inline form (`scope:x = { add_trait = trait:y }`) cannot carry a multi-line
        # custom_tooltip, so it gets the award without one rather than a broken block.
        text, n_inline = re.subn(
            r"add_trait = trait:%s\b" % re.escape(trait),
            f"cc_xp_gain_{track} = {{ AMOUNT = {band} }}  cc_xp_recompute = yes", text)
        if n_inline == 0:
            raise SystemExit(f"ERROR: could not rewrite the grant of {trait}; "
                             f"the option's shape is not one this tool handles.")
    return text.split("\n")


def retooltip(text: str, filename: str, report: list):
    """Put a readable tooltip on awards the earlier passes emitted without one.

    The first pass shipped 22 generated options whose whole visible effect was three
    change_variable writes, which render as nothing. Rewriting them in place keeps every
    player-facing experience award saying the same thing, and it is idempotent: an award
    already inside a custom_tooltip does not match.
    """
    pat = re.compile(
        r"^(?P<indent>\t+)# Ladder rung withheld: the ladder grants it once the tier is "
        r"earned\.\n"
        r"(?P=indent)cc_xp_gain_(?P<track>adm|dip|mil) = \{ AMOUNT = "
        r"(?P<band>cc_xp_field_award_\w+) \}\n"
        r"(?P=indent)cc_xp_recompute = yes[ \t]*$", re.M)

    n = 0
    used: set = set()

    def repl(m):
        nonlocal n
        n += 1
        used.add((m.group("track"), m.group("band")))
        return wrap_award(m.group("indent"), m.group("track"), m.group("band"),
                          "Ladder rung withheld: the ladder grants it once the tier is "
                          "earned.")

    new = pat.sub(repl, text)
    if n:
        report.append((filename, n))
    return new, n, used


def inject_trigger(body: list[str], cond: str) -> list[str]:
    """Add `cond` to an option's trigger block, creating one if absent."""
    body = list(body)
    for k, line in enumerate(body):
        if re.match(r"^\t\ttrigger = \{\s*$", line):
            body.insert(k + 1, f"\t\t\t{cond}")
            return body
        m = re.match(r"^\t\ttrigger = \{(.+)\}\s*$", line)
        if m:
            body[k] = f"\t\ttrigger = {{ {cond}  {m.group(1).strip()} }}"
            return body
    # No trigger block. Put one straight after `name = ...`, or after `option = {`.
    for k, line in enumerate(body):
        if re.match(r"^\t\tname = ", line):
            body.insert(k + 1, f"\t\ttrigger = {{ {cond} }}")
            return body
    body.insert(1, f"\t\ttrigger = {{ {cond} }}")
    return body


def build_human_option(body: list[str], trait: str, track: str, rung: int) -> list[str]:
    """The player's version: same conditions, experience instead of the trait."""
    body = inject_trigger(body, "is_ai = no")
    out: list[str] = []
    for line in body:
        if re.match(r"^\t\tname = ", line):
            out.append(f"\t\tname = {MARKER}{trait}")
            continue
        out.append(line)

    text = "\n".join(out)

    # Replace the trait grant with the experience award, keeping indentation and any
    # cooldown variable the original set.
    def repl(m):
        # cc_xp_gain_* calls cc_xp_init itself, so this is safe on a minister who has no
        # experience variables yet. cc_xp_recompute follows the award the same way the
        # training return events do (cc_xp_events.txt:238), so the level and tier move
        # immediately rather than on the next monthly tick.
        return wrap_award(m.group(1), track, BAND[rung],
                          "Ladder rung withheld: the ladder grants it once the tier is "
                          "earned.")

    award = f"cc_xp_gain_{track} = {{ AMOUNT = {BAND[rung]} }}"

    # Two forms occur in the source, and both must be handled. The grant is either on a
    # line of its own, or inline inside a scope block:
    #
    #   \t\t\tadd_trait = trait:supreme_commander
    #   \t\tscope:minister = { add_trait = trait:learned_counselor }
    #
    # Only matching the first shipped three unconverted options in cc_cabinet_events.txt,
    # which is exactly the silent half-migration this tool exists to avoid.
    text, n_line = re.subn(r"^(\t+)add_trait = trait:%s[ \t]*$" % re.escape(trait),
                           repl, text, flags=re.M)
    text, n_inline = re.subn(r"add_trait = trait:%s\b" % re.escape(trait),
                             award + "  cc_xp_recompute = yes", text)

    if n_line + n_inline == 0:
        raise SystemExit(f"ERROR: could not rewrite the grant of {trait}; "
                         f"the option's shape is not one this tool handles.")

    # Deliberately NOT a blanket sweep over every add_trait in the block. Options that
    # grant more than one ladder trait are exempted upstream as transfers, and a
    # non-ladder grant sharing the option (an age trait, an affliction) must survive
    # untouched.
    return text.split("\n")


def emit_loc(traits: set[str]) -> str:
    out = ["﻿", "l_english:\n\n",
           " # GENERATED FILE. Do not edit by hand. python tools/migrate_bypass.py\n",
           " #\n",
           " # The player-facing half of every court-event option that used to hand out a\n",
           " # ladder rung. The AI half keeps the original wording, which names the trait;\n",
           " # this half says what actually happens, which is that the minister gains\n",
           " # experience toward it and the ladder grants it when the tier is earned.\n",
           " #\n",
           " # DELIBERATELY SCOPE-FREE. One key is shared by every event that offers the\n",
           " # same rung, and those events do not agree on what the character is called:\n",
           " # cc_cond.* saves 'minister', cc_traits.20 saves 'student', cc_traits.21\n",
           " # 'learner', cc_neg.19 'rehabilitated_minister', cc_subject_events 'enclave',\n",
           " # 'republic' and 'ward', and cc.165 saves no character at all. A\n",
           " # [minister.GetName] here would be an undefined event target in seven events,\n",
           " # which errors rather than rendering blank. 'them' is correct everywhere.\n\n"]
    for t in sorted(traits):
        out.append(f" {MARKER}{t}: \"Have them train toward [ShowTraitName('{t}')].\"\n")
    return "".join(out)


def emit_award_loc(pairs: set, values: dict) -> str:
    """The tooltip on each experience award, one key per track and band."""
    out = ["﻿", "l_english:\n\n",
           " # GENERATED FILE. Do not edit by hand. python tools/migrate_bypass.py\n",
           " #\n",
           " # What a court-event option actually grants when the ladder rung is withheld.\n",
           " # cc_xp_gain_* is three change_variable writes and the engine renders those as\n",
           " # nothing, so without this the button had no readable effect at all.\n",
           " #\n",
           " # The numbers are read from cc_xp_values.txt at generation time. Retune the\n",
           " # bands there and re-run; do not edit them here, where they would silently\n",
           " # disagree with the effect.\n\n"]
    for track, band in sorted(pairs):
        out.append(" %s: \"Gains %d %s experience.\"\n"
                   % (award_key(track, band), values[band], TRACK_NAME[track]))
    return "".join(out)


LADDER: dict = {}
SKIPPED: list = []


def main() -> int:
    global LADDER
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write the changes")
    args = ap.parse_args()

    LADDER = load_ladders()
    values = load_award_values()
    print(f"loaded {len(LADDER)} ladder rung traits, "
          f"{len(values)} award bands from cc_xp_values.txt")

    split_report: list = []
    gate_report: list = []
    tip_report: list = []
    changes: list[tuple[Path, str]] = []
    final: dict = {}

    for path in sorted(EVENTS.glob("*.txt")):
        if path.name.startswith("cc_xp_"):
            continue                                   # the XP system's own events
        text = path.read_text(encoding="utf-8-sig")
        if not TRAIT_RE.search(text) and MARKER not in text:
            continue
        new, n_split, _ = split_options(text, LADDER, split_report, path.name)
        new, n_gate, _ = add_gated_fallbacks(new, LADDER, gate_report, path.name)
        new, n_tip, _ = retooltip(new, path.name, tip_report)
        final[path] = new
        if n_split + n_gate + n_tip:
            changes.append((path, new))

    if split_report:
        print(f"\nUNGATED RUNGS SPLIT BY is_ai: {len(split_report)}\n")
        print("%-30s %-14s %-14s %-26s %-5s %s" %
              ("file", "event", "option", "trait", "rung", "award"))
        for f, ev, oname, trait, track, rung, band in split_report:
            print("%-30s %-14s %-14s %-26s %s%-4d %s" %
                  (f.replace("cc_", "").replace("_events.txt", ""), ev,
                   oname.split(".")[-1], trait, track, rung, band))

    if gate_report:
        print(f"\nGATED RUNGS GIVEN A BELOW-TIER PARTNER: {len(gate_report)}\n")
        print("%-30s %-14s %-16s %-26s %-5s %s" %
              ("file", "event", "option", "trait", "gate", "award"))
        for f, ev, oname, trait, track, tier, band in gate_report:
            print("%-30s %-14s %-16s %-26s %s%-4d %s" %
                  (f.replace("cc_", "").replace("_events.txt", ""), ev,
                   oname.split(".")[-1], trait, track, tier, band))
        per_event: dict = {}
        for f, ev, *_ in gate_report:
            per_event[ev] = per_event.get(ev, 0) + 1
        print("\nby event: " + ", ".join(f"{k}: {v}"
                                         for k, v in sorted(per_event.items())))

    if tip_report:
        print("\nAWARDS GIVEN A TOOLTIP: "
              + ", ".join(f"{f} x{n}" for f, n in tip_report))

    if SKIPPED:
        print("\nLEFT ALONE (reported, not rewritten):")
        for f, ev, traits, why in SKIPPED:
            print("  %-34s %-14s %s" % (f, ev, why))
            print("      " + " ".join(traits))

    if not changes:
        print("\nnothing to do: every ladder-rung option is split, partnered "
              "and tooltipped.")

    # LOC IS EMITTED FROM THE FINAL STATE OF EVERY FILE, not from this run's changes.
    # Deriving it from `changes` meant a second run, which by construction changes
    # nothing, would regenerate both files from an empty set and delete every key in
    # them. The generated files describe what the events currently say; that has to be
    # read back off the events.
    traits: set = set()
    pairs: set = set()
    for path, text in final.items():
        traits |= set(re.findall(r"^\t\tname = %s(\w+)" % MARKER, text, re.M))
        for t, b in re.findall(r"text = cc_xp_award_(adm|dip|mil)_(\w+)", text):
            pairs.add((t, "cc_xp_field_award_" + b))
    print(f"\nloc: {len(traits)} rung keys, {len(pairs)} award keys")

    if not args.apply:
        print("\ndry run, nothing written (pass --apply)")
        return 0

    for path, new in changes:
        path.write_text(new, encoding="utf-8-sig", newline="")
        print(f"  rewrote {path.relative_to(REPO)}")
    OUT_LOC.write_text(emit_loc(traits), encoding="utf-8")
    print(f"  wrote   {OUT_LOC.relative_to(REPO)}")
    OUT_AWARD_LOC.write_text(emit_award_loc(pairs, values), encoding="utf-8")
    print(f"  wrote   {OUT_AWARD_LOC.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
