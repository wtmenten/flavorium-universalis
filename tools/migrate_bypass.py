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
OUT_LOC = REPO / "in_game" / "localization" / "english" / "cc_xp_toward_l_english.yml"

MARKER = "cc_xp_toward_"

# Rung index -> (script value, human-readable band) for the experience award.
BAND = {
    0: "cc_xp_field_award_entry",
    1: "cc_xp_field_award_low",
    2: "cc_xp_field_award_mid",
    3: "cc_xp_field_award_high",
}

GATE_RE = re.compile(r"cc_xp_(dispatch_ready|tier_at_least|level_at_least)")
TRAIT_RE = re.compile(r"add_trait = trait:([a-zA-Z_0-9]+)")


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
        indent = m.group(1)
        return (f"{indent}# Ladder rung withheld: the ladder grants it once the tier is "
                f"earned.\n"
                f"{indent}cc_xp_gain_{track} = {{ AMOUNT = {BAND[rung]} }}\n"
                f"{indent}cc_xp_recompute = yes")

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


LADDER: dict = {}
SKIPPED: list = []


def main() -> int:
    global LADDER
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write the changes")
    args = ap.parse_args()

    LADDER = load_ladders()
    print(f"loaded {len(LADDER)} ladder rung traits")

    report: list = []
    all_traits: set[str] = set()
    changes: list[tuple[Path, str]] = []

    for path in sorted(EVENTS.glob("*.txt")):
        if path.name.startswith("cc_xp_"):
            continue                                   # the XP system's own events
        text = path.read_text(encoding="utf-8-sig")
        if not TRAIT_RE.search(text):
            continue
        new, n, traits = split_options(text, LADDER, report, path.name)
        if n:
            changes.append((path, new))
            all_traits |= traits

    if not report:
        print("nothing to do: every ladder-rung option is already split or gated.")
        return 0

    print(f"\n{len(report)} options in {len(changes)} files\n")
    print("%-32s %-16s %-14s %-26s %-5s %s" %
          ("file", "event", "option", "trait", "rung", "award"))
    for f, ev, oname, trait, track, rung, band in report:
        print("%-32s %-16s %-14s %-26s %s%-4d %s" %
              (f.replace("cc_", "").replace("_events.txt", ""), ev,
               oname.split(".")[-1], trait, track, rung, band))

    if SKIPPED:
        print("\nLEFT ALONE (reported, not rewritten):")
        for f, ev, traits, why in SKIPPED:
            print("  %-34s %-16s %s" % (f, ev, why))
            print("      " + " ".join(traits))

    by_rung: dict = {}
    for *_, rung, _b in report:
        by_rung[rung] = by_rung.get(rung, 0) + 1
    print("\nby rung: " + ", ".join(f"rung {k}: {v}" for k, v in sorted(by_rung.items())))
    print(f"distinct traits needing loc: {len(all_traits)}")

    if not args.apply:
        print("\ndry run, nothing written (pass --apply)")
        return 0

    for path, new in changes:
        path.write_text(new, encoding="utf-8-sig", newline="")
        print(f"  rewrote {path.relative_to(REPO)}")
    OUT_LOC.write_text(emit_loc(all_traits), encoding="utf-8")
    print(f"  wrote   {OUT_LOC.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
