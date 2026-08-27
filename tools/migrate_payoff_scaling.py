#!/usr/bin/env python3
"""Scale court-event payoffs by the seniority of the minister they are about.

Seventy-four events read a minister's traits and pay out without asking how senior that
minister is: a level 1 minister and a level 10 one bought exactly the same synergy. Each
now publishes that minister's level and multiplies its rewards by cc_xp_payoff_scale,
which maps level 1-10 onto 1.0x-2.5x.

WHAT GETS TOUCHED, and how:

  add_country_modifier   gains `size = cc_xp_payoff_scale`, which the engine documents as
                         "multiplies the effect of the modifier". Durations are left
                         alone: scaling both magnitude and length compounds.
  add_prestige           bare script value becomes
  add_gold               { value = <original>  multiply = cc_xp_payoff_scale }
  add_stability

  add_opinion            NOT scaled. Its magnitude lives in the bias definition, not at
  change_variable        the call site. change_variable drives system state (cooldowns,
                         counters), and multiplying it would corrupt the systems that
                         read it rather than reward the player.

WHY A COUNTRY VARIABLE RATHER THAN A SCOPE. add_country_modifier evaluates `size` in
country scope, and the events do not agree on what the minister is called: 34 save
'minister', 8 'rehabilitated_minister', 8 a 'minister_a'/'minister_b' pair, and the tail
saves 'military_minister', 'muslim_partner' and similar. The scope name is detected per
event and passed to cc_xp_publish_payoff_level, so one shared value serves all of them.
Four events save no character at all and get the _best variant instead.

Negative payouts are scaled too. A penalty that scales with seniority is the same
statement as a bonus that does: the court's best minister is who this is about.

Idempotent: an event already carrying the publish call is skipped.

    python tools/migrate_payoff_scaling.py            # dry run
    python tools/migrate_payoff_scaling.py --apply
    python tools/migrate_payoff_scaling.py --verify
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVENTS = REPO / "in_game" / "events"

FILES = """cc_trait_dispatch_events.txt cc_trait_events.txt cc_conditional_trait_events.txt
cc_negative_trait_events.txt cc_cabinet_events.txt cc_synergy_events.txt
cc_dual_synergy_events.txt cc_intl_synergy_events.txt cc_legacy_events.txt
cc_legend_events.txt cc_estate_faction_events.txt cc_rivalry_events.txt
cc_cabal_events.txt cc_feudal_events.txt cc_war_council_events.txt
cc_colonial_posting_events.txt""".split()

SCALE = "cc_xp_payoff_scale"
PUBLISH = "cc_xp_publish_payoff_level"

# Which minister a given event's payoff is about, when more than one scope is saved.
# Everything else is auto-detected; these are the ones where detection would guess.
SCOPE_PREFERENCE = ["minister", "rehabilitated_minister", "minister_a", "military_minister"]

SCALABLE = ("add_prestige", "add_gold", "add_stability")


def events_in(path: Path):
    lines = path.read_text(encoding="utf-8-sig").split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^([a-zA-Z_0-9]+\.\d+) = \{", lines[i])
        if m:
            depth, j = 0, i
            while j < len(lines):
                depth += lines[j].count("{") - lines[j].count("}")
                j += 1
                if depth <= 0:
                    break
            yield m.group(1), i, j, lines
            i = j
        else:
            i += 1


# Iterators and links that put a CHARACTER in scope. A save_scope_as inside one of these
# names a character; a save inside any_country / any_subject names a country, and reading
# cc_level off it would silently yield the 1.0x floor forever.
CHAR_CONTEXT = re.compile(
    r"(random|every|any|ordered)_(cabinet_)?character|"
    r"(ruler_or_regent|ruler|heir|consort|scope:\w*minister)\s*=\s*\{|"
    r"create_character\s*=\s*\{")


def character_scopes(body: list[str]) -> list[str]:
    """save_scope_as names that are demonstrably characters, by enclosing block."""
    found, stack = [], []
    for line in body:
        opens = line.count("{")
        closes = line.count("}")
        m = re.search(r"([a-zA-Z_0-9:]+)\s*=\s*\{", line)
        is_char = bool(CHAR_CONTEXT.search(line))
        for _ in range(opens):
            stack.append(is_char and m is not None)
            is_char = False          # only the first brace on the line owns the context
        s = re.search(r"save_scope_as = (\w+)", line)
        if s and any(stack):
            found.append(s.group(1))
        for _ in range(closes):
            if stack:
                stack.pop()
    return found


def pick_scope(body: list[str]) -> str | None:
    chars = character_scopes(body)
    if not chars:
        return None
    for pref in SCOPE_PREFERENCE:
        if pref in chars:
            return pref
    return chars[0]


def scale_payouts(body: list[str]) -> tuple[list[str], int]:
    """Add the multiplier to every payout shape that can carry one.

    Three shapes occur and two are handled:

      add_country_modifier = { modifier = x years = 4 }      one line, gains `size`
      add_country_modifier = {                               several lines, gains `size`
          modifier = x
          years = 4
      }
      add_prestige = prestige_mild_bonus                     bare value, gains `multiply`

    NOT handled, deliberately: the block form of add_gold, which in every case here
    already carries its own `multiply` plus `min`/`max` clamps:

      add_gold = { value = monthly_income_trade_and_tax  multiply = -0.50
                   min = -250  max = -75 }

    A second multiplier would fight a clamp that was calibrated against the first, and
    these are nearly all negative: scaling a cost by seniority makes a good court pay
    more for the same thing, which is the opposite of the intent.
    """
    out, n, i = [], 0, 0
    while i < len(body):
        line = body[i]

        m = re.match(r"^(\s*)add_country_modifier = \{(.*)\}\s*$", line)
        if m and "size" not in m.group(2):
            out.append(f"{m.group(1)}add_country_modifier = {{{m.group(2).rstrip()}"
                       f"  size = {SCALE} }}")
            n += 1
            i += 1
            continue

        m = re.match(r"^(\s*)add_country_modifier = \{\s*$", line)
        if m:
            depth, j = 0, i
            while j < len(body):
                depth += body[j].count("{") - body[j].count("}")
                j += 1
                if depth <= 0:
                    break
            chunk = body[i:j]
            if not any("size" in c for c in chunk):
                chunk.insert(len(chunk) - 1, f"{m.group(1)}\tsize = {SCALE}")
                n += 1
            out.extend(chunk)
            i = j
            continue

        m = re.match(r"^(\s*)(%s) = ([A-Za-z_0-9]+)\s*$" % "|".join(SCALABLE), line)
        if m:
            out.append(f"{m.group(1)}{m.group(2)} = {{ value = {m.group(3)}"
                       f"  multiply = {SCALE} }}")
            n += 1
            i += 1
            continue

        out.append(line)
        i += 1
    return out, n


def process(path: Path, report: list, apply: bool) -> int:
    lines = path.read_text(encoding="utf-8-sig").split("\n")
    edits: list[tuple[int, int, list[str]]] = []

    for ev, start, end, _ in events_in(path):
        body = lines[start:end]
        block = "\n".join(body)

        if "add_trait" in block or "has_trait = " not in block:
            continue                      # not a payoff event

        already_published = PUBLISH in block

        scope = pick_scope(body)
        new_body, n = scale_payouts(body)
        if n == 0:
            continue                      # nothing left to scale

        # An event may already publish and still hold an unscaled payout, because the
        # first pass only reached the single-line shapes. Top those up without adding a
        # second publish call.
        if already_published:
            edits.append((start, end, new_body))
            report.append((path.name, ev, (scope or "(cabinet best)") + " [top-up]", n, ""))
            continue

        # Publish the level at the very end of `immediate`, after the event has picked
        # whichever minister it is about.
        call = (f"\t\t{PUBLISH} = {{ SCOPE = {scope} }}" if scope
                else f"\t\t{PUBLISH}_best = yes")
        placed = False
        for k, line in enumerate(new_body):
            if re.match(r"^\timmediate = \{", line):
                depth, j = 0, k
                while j < len(new_body):
                    depth += new_body[j].count("{") - new_body[j].count("}")
                    j += 1
                    if depth <= 0:
                        break
                new_body.insert(j - 1, call)
                placed = True
                break
        if not placed:
            # No immediate block. Create one straight after the illustration/desc header,
            # which for these events means just before the first option.
            for k, line in enumerate(new_body):
                if re.match(r"^\toption = \{", line):
                    new_body[k:k] = ["\timmediate = {", call, "\t}", ""]
                    placed = True
                    break
        if not placed:
            report.append((path.name, ev, scope or "(none)", n, "NO INSERTION POINT"))
            continue

        edits.append((start, end, new_body))
        report.append((path.name, ev, scope or "(cabinet best)", n, ""))

    if not edits:
        return 0
    out, cursor = [], 0
    for start, end, new_body in edits:
        out.extend(lines[cursor:start])
        out.extend(new_body)
        cursor = end
    out.extend(lines[cursor:])
    if apply:
        path.write_text("\n".join(out), encoding="utf-8-sig", newline="")
    return len(edits)


def verify() -> int:
    problems = []
    for name in FILES:
        path = EVENTS / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8-sig")
        d = re.sub(r"#[^\n]*", "", text)
        if d.count("{") != d.count("}"):
            problems.append(f"{name}: braces {d.count('{') - d.count('}'):+d}")
        for ev, start, end, lines in events_in(path):
            block = "\n".join(lines[start:end])
            if PUBLISH not in block:
                continue
            if block.count(PUBLISH) > 1:
                problems.append(f"{name} {ev}: published more than once")
            # every scaled payout must sit in an event that publishes a level
            if SCALE in block and PUBLISH not in block:
                problems.append(f"{name} {ev}: scales without publishing")
            m = re.search(r"%s = \{ SCOPE = (\w+) \}" % PUBLISH, block)
            if m and f"save_scope_as = {m.group(1)}" not in block:
                problems.append(f"{name} {ev}: publishes scope:{m.group(1)}, "
                                f"which the event never saves")
    # a scaled payout anywhere must have a publisher in the same event
    for name in FILES:
        path = EVENTS / name
        if not path.exists():
            continue
        for ev, start, end, lines in events_in(path):
            block = "\n".join(lines[start:end])
            if SCALE in block and PUBLISH not in block:
                problems.append(f"{name} {ev}: scales without publishing")
    for p in problems:
        print("  " + p)
    print("VERIFY OK" if not problems else f"VERIFY FAILED ({len(problems)})")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()
    if args.verify:
        return verify()

    report: list = []
    total = 0
    for name in FILES:
        path = EVENTS / name
        if path.exists():
            total += process(path, report, args.apply)

    if not report:
        print("nothing to do: every payoff event already scales.")
        return 0

    print("%-32s %-14s %-24s %s" % ("file", "event", "scope", "payouts scaled"))
    for f, ev, scope, n, err in report:
        print("%-32s %-14s %-24s %-3d %s" %
              (f.replace("cc_", "").replace("_events.txt", ""), ev, scope, n, err))
    print(f"\n{total} events, {sum(r[3] for r in report)} payouts scaled")
    scopes: dict = {}
    for _f, _e, s, _n, _err in report:
        scopes[s] = scopes.get(s, 0) + 1
    print("scopes used: " + ", ".join(f"{k}: {v}" for k, v in sorted(scopes.items(),
                                                                     key=lambda x: -x[1])))
    print("\ndry run, nothing written (pass --apply)" if not args.apply else "\napplied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
