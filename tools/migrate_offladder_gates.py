#!/usr/bin/env python3
"""Gate the off-ladder conditional traits on earned experience.

Thirty-four traits that are not ladder rungs could still be handed to any minister by a
random court event. They stay random by design (they describe context: what faith the
realm keeps, what its societal values are, what culture group it belongs to), but an
untrained minister should not receive one.

Each option now carries `cc_xp_dispatch_ready`, which is deliberately NOT
`cc_xp_tier_at_least`: it passes for a minister the system does not track, so minor AI
courts and games with the cabinet experience rule switched off behave exactly as before.

Every affected event carries exactly one ungated `dismiss` option, so gating can never
leave an event with nothing to click. That was checked before this was written and is
re-checked by --verify.

THE TABLE BELOW IS THE DECISION, not a computation. It was generated from trait tags and
modifier magnitudes, reviewed, and then amended:

  Track      the trait's FIRST custom_tag, since the author ordered them by primacy.
             That beats a priority list where they disagree: roman_administrator is
             "administrative diplomatic" (adm), hawk_minister is "military diplomatic"
             (mil), christian_diplomat is "diplomatic religious" (dip). `religious` maps
             to adm because there is no religious track and the Court Chaplain office is
             already adm; `economical` maps to dip because the trade ladders are dip.

  Tier       a strength score, each modifier weighted against what that modifier type
             usually is across every trait in the mod, banded at the 50th percentile.

  Amended    the ceiling is tier 2. The raw grading put seven traits at tier 3, which is
             1200 track XP, a career master. These describe who a minister IS rather than
             how good they are, and locking them behind mastery would have left cc_cond.4
             and cc_cond.24 offering a normal court nothing but the dismiss option. Tier 3
             stays exclusive to ladder rungs, which also keeps the two systems distinct.

  Amended    two track calls overridden by function rather than by tag order:
               dharma_minister      religious,administrative -> dip, not adm.
                                    It is a diplomat in practice.
               capitalist_minister  economical,administrative -> adm, not dip.
                                    Its modifiers are domestic economy, not trade.

    python tools/migrate_offladder_gates.py             # dry run
    python tools/migrate_offladder_gates.py --apply
    python tools/migrate_offladder_gates.py --verify    # check the result
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVENTS = REPO / "in_game" / "events"

GATE = "cc_xp_dispatch_ready"

# trait -> (track, tier).  See the docstring for how these were arrived at.
GRADES: dict[str, tuple[str, int]] = {
    # ---- tier 2 -----------------------------------------------------------
    "ecumenical_patriarch_advisor": ("adm", 2),
    "parliamentary_broker":         ("adm", 2),
    "traditionalist_guardian":      ("adm", 2),
    "revolutionary_herald":         ("adm", 2),
    "confucian_mandarin":           ("adm", 2),
    "royal_absolutist":             ("adm", 2),
    "emancipation_minister":        ("adm", 2),
    "arts_patron":                  ("adm", 2),
    "brahmin_counselor":            ("adm", 2),
    "innovative_counselor":         ("adm", 2),
    "prosperity_herald":            ("adm", 2),
    "renaissance_patron":           ("adm", 2),
    "serf_overseer":                ("adm", 2),
    "caliphate_diplomat":           ("dip", 2),
    "griot_diplomat":               ("dip", 2),
    "expansionist_advisor":         ("dip", 2),
    "dharma_minister":              ("dip", 2),   # overridden from adm
    "hawk_minister":                ("mil", 2),
    # ---- tier 1 -----------------------------------------------------------
    "hellenistic_scholar":          ("adm", 1),
    "mughal_administrator":         ("adm", 1),
    "liberal_reformer":             ("adm", 1),
    "roman_administrator":          ("adm", 1),
    "community_steward":            ("adm", 1),
    "free_spirit_counselor":        ("adm", 1),
    "mystical_patriarch":           ("adm", 1),
    "reform_minded_counselor":      ("adm", 1),
    "mystical_counselor":           ("adm", 1),
    "consolidation_minister":       ("adm", 1),
    "capitalist_minister":          ("adm", 1),   # overridden from dip
    "peacemaker_counselor":         ("dip", 1),
    "christian_diplomat":           ("dip", 1),
    "steppe_strategos":             ("mil", 1),
    "steppe_warlord_advisor":       ("mil", 1),
    "noble_champion":               ("mil", 1),
}

TRAIT_RE = re.compile(r"add_trait = trait:([a-zA-Z_0-9]+)")
GATE_RE = re.compile(r"cc_xp_(dispatch_ready|tier_at_least|level_at_least)")

SKIPPED: list = []


def option_blocks(lines: list[str]):
    """Yield (start, end, block_lines, event_id) for every option in a file."""
    i, cur = 0, "?"
    while i < len(lines):
        m = re.match(r"^([a-zA-Z_0-9]+\.\d+) = \{", lines[i])
        if m:
            cur = m.group(1)
        if re.match(r"^\toption = \{", lines[i]):
            depth, body, j = 0, [], i
            while j < len(lines):
                depth += lines[j].count("{") - lines[j].count("}")
                body.append(lines[j])
                j += 1
                if depth <= 0:
                    break
            yield i, j, body, cur
            i = j
        else:
            i += 1


def scope_of(block: str) -> str | None:
    """Which saved scope the option applies the trait to. Detected, not assumed."""
    m = re.search(r"scope:([a-zA-Z_0-9]+) = \{[^{}]*add_trait", block)
    if m:
        return m.group(1)
    m = re.search(r"scope:([a-zA-Z_0-9]+) = \{", block)
    return m.group(1) if m else None


def gate_line(scope: str, track: str, tier: int, indent: str) -> str:
    return (f"{indent}scope:{scope} = {{ {GATE} = {{ TRACK = {track}  TIER = {tier} }} }}")


def process(path: Path, report: list, apply: bool):
    lines = path.read_text(encoding="utf-8-sig").split("\n")
    out, cursor, touched = [], 0, 0

    for start, end, body, ev in option_blocks(lines):
        block = "\n".join(body)
        traits = [t for t in TRAIT_RE.findall(block) if t in GRADES]
        if not traits or GATE_RE.search(block):
            continue

        # An option that grants several different traits is an if/else_if chain passing on
        # whichever one a dying elder held (cc_legacy.1). Gating the whole option on one of
        # them would silently block the entire handover, and the same option was already
        # exempted from the bypass migration for the same reason: it is a TRANSFER inside
        # the court, paid for with the elder, not a grant from nothing.
        if len(set(TRAIT_RE.findall(block))) > 1:
            SKIPPED.append((path.name, ev, sorted(set(traits)),
                            "multi-grant chain, treated as a transfer"))
            continue

        trait = traits[0]
        track, tier = GRADES[trait]
        scope = scope_of(block)
        if not scope:
            report.append((path.name, ev, trait, "NO SCOPE FOUND", "", ""))
            continue

        new_body = list(body)
        placed = False
        for k, line in enumerate(new_body):
            if re.match(r"^\t\ttrigger = \{\s*$", line):
                new_body.insert(k + 1, gate_line(scope, track, tier, "\t\t\t"))
                placed = True
                break
            m = re.match(r"^\t\ttrigger = \{(.+)\}\s*$", line)
            if m:
                inner = m.group(1).strip()
                new_body[k] = "\t\ttrigger = {"
                new_body.insert(k + 1, f"\t\t\t{inner}")
                new_body.insert(k + 2, gate_line(scope, track, tier, "\t\t\t"))
                new_body.insert(k + 3, "\t\t}")
                placed = True
                break
        if not placed:
            for k, line in enumerate(new_body):
                if re.match(r"^\t\tname = ", line):
                    new_body.insert(k + 1, "\t\ttrigger = {")
                    new_body.insert(k + 2, gate_line(scope, track, tier, "\t\t\t"))
                    new_body.insert(k + 3, "\t\t}")
                    placed = True
                    break
        if not placed:
            report.append((path.name, ev, trait, "NO INSERTION POINT", "", ""))
            continue

        out.extend(lines[cursor:start])
        out.extend(new_body)
        cursor = end
        touched += 1
        report.append((path.name, ev, trait, scope, track, tier))

    out.extend(lines[cursor:])
    if touched and apply:
        path.write_text("\n".join(out), encoding="utf-8-sig", newline="")
    return touched


def verify() -> int:
    problems = []
    for path in sorted(EVENTS.glob("*.txt")):
        text = path.read_text(encoding="utf-8-sig")
        if not TRAIT_RE.search(text):
            continue
        lines = text.split("\n")
        per_event: dict = {}
        for _s, _e, body, ev in option_blocks(lines):
            block = "\n".join(body)
            per_event.setdefault(ev, [0, 0])
            per_event[ev][0] += 1
            if "trigger = {" not in block:
                per_event[ev][1] += 1
            traits = [t for t in TRAIT_RE.findall(block) if t in GRADES]
            multi = len(set(TRAIT_RE.findall(block))) > 1
            if traits and not GATE_RE.search(block) and not multi:
                problems.append(f"{path.name} {ev}: {traits[0]} still ungated")
        for ev, (total, free) in per_event.items():
            if total and free == 0 and any(
                    t in GRADES for _s, _e, b, e2 in option_blocks(lines)
                    if e2 == ev for t in TRAIT_RE.findall("\n".join(b))):
                problems.append(f"{path.name} {ev}: no ungated fallback option")
    d = re.compile(r"#[^\n]*")
    for path in sorted(EVENTS.glob("*.txt")):
        t = d.sub("", path.read_text(encoding="utf-8-sig"))
        if t.count("{") != t.count("}"):
            problems.append(f"{path.name}: braces unbalanced "
                            f"{t.count('{') - t.count('}'):+d}")
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
    for path in sorted(EVENTS.glob("*.txt")):
        total += process(path, report, args.apply)

    if not report:
        print("nothing to do: every off-ladder option is already gated.")
        return 0

    print("%-34s %-12s %-30s %-10s %s" % ("file", "event", "trait", "scope", "gate"))
    for f, ev, trait, scope, track, tier in report:
        print("%-34s %-12s %-30s %-10s %s" %
              (f.replace("cc_", "").replace("_events.txt", ""), ev, trait, scope,
               f"{track} tier {tier}" if track else scope))
    print(f"\n{total} options gated")
    tiers: dict = {}
    for *_r, track, tier in report:
        if track:
            tiers[(track, tier)] = tiers.get((track, tier), 0) + 1
    print("distribution: " + ", ".join(f"{k[0]} tier {k[1]}: {v}"
                                       for k, v in sorted(tiers.items())))
    print("\ndry run, nothing written (pass --apply)" if not args.apply else "\napplied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
