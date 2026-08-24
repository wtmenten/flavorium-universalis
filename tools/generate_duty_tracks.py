#!/usr/bin/env python3
"""Generate the cabinet-duty -> XP-track lookup used by the cabinet experience system.

Every cabinet_action definition carries an `ability = adm|dip|mil` line, but the engine
exposes no script trigger to read a duty's ability type at runtime (`IsAbilityType` exists
only in GUI script). So we bake the mapping out of the source files into a scripted effect
that tests `cabinet_action = cabinet_action:<name>` against three OR blocks.

Sources, later ones overriding earlier ones by action name:
  1. vanilla   <game>/in_game/common/cabinet_actions/
  2. main mod  in_game/common/cabinet_actions/
  3. submods   submods/*/in_game/common/cabinet_actions/

Rerun after any EU5 update, since a patch that adds or retunes a cabinet action changes
which track its service credits. Output is overwritten wholesale; do not hand-edit it.

    python tools/generate_duty_tracks.py
    python tools/generate_duty_tracks.py --check    # exit 1 if the output is stale
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VANILLA = Path(r"F:\SteamLibrary\steamapps\common\Europa Universalis V\game")
OUT = REPO / "in_game" / "common" / "scripted_effects" / "cc_xp_duty_tracks.txt"

TRACKS = ("adm", "dip", "mil")

# Actions that carry an `ability` tag but represent a minister doing nothing in particular.
# They are dropped from the lookup so idling never accrues duty experience. Passive tenure
# (cc_xp_yearly_tenure) is the only thing an unoccupied minister earns.
EXCLUDE = {
    "cc_duty_free_hands",
}

# Top-level `some_key = {` at column zero. Cabinet action files declare one or more of these.
TOP_LEVEL = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\{")
ABILITY = re.compile(r"^\s*ability\s*=\s*(adm|dip|mil)\b")


def strip_comments(line: str) -> str:
    """Drop a trailing # comment. Cabinet action files contain no # inside strings."""
    return line.split("#", 1)[0]


def parse_file(path: Path) -> dict[str, str]:
    """Return {action_name: track} for every top-level action defined in one file.

    Tracks brace depth so that an `ability = ` nested inside ai_will_do or a
    sub-block is never mistaken for the action's own declaration.
    """
    found: dict[str, str] = {}
    depth = 0
    current: str | None = None

    for raw in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        line = strip_comments(raw)

        if depth == 0:
            match = TOP_LEVEL.match(line)
            if match:
                current = match.group(1)
        elif depth == 1 and current:
            match = ABILITY.match(line)
            if match:
                found[current] = match.group(1)

        depth += line.count("{") - line.count("}")
        if depth <= 0:
            depth = 0
            current = None

    return found


def collect() -> tuple[dict[str, str], list[str]]:
    """Merge every source directory in precedence order. Returns (mapping, source notes)."""
    sources: list[tuple[str, Path]] = [
        ("vanilla", VANILLA / "in_game" / "common" / "cabinet_actions"),
        ("main mod", REPO / "in_game" / "common" / "cabinet_actions"),
    ]
    for submod in sorted((REPO / "submods").glob("*/in_game/common/cabinet_actions")):
        sources.append((f"submod {submod.parents[3].name}", submod))

    mapping: dict[str, str] = {}
    notes: list[str] = []

    for label, directory in sources:
        if not directory.is_dir():
            notes.append(f"{label}: directory not found, skipped ({directory})")
            continue
        count = 0
        for path in sorted(directory.glob("*.txt")):
            for name, track in parse_file(path).items():
                if name in EXCLUDE:
                    continue
                mapping[name] = track
                count += 1
        notes.append(f"{label}: {count} actions from {len(list(directory.glob('*.txt')))} files")

    if EXCLUDE:
        notes.append("excluded as idle: " + ", ".join(sorted(EXCLUDE)))

    return mapping, notes


def render(mapping: dict[str, str], notes: list[str]) -> str:
    by_track: dict[str, list[str]] = {track: [] for track in TRACKS}
    for name, track in sorted(mapping.items()):
        by_track[track].append(name)

    lines: list[str] = []
    add = lines.append

    add("\ufeff###############################################################################")
    add("# GENERATED FILE. Do not edit by hand.")
    add("#   python tools/generate_duty_tracks.py")
    add("#")
    add("# Maps each cabinet action to the experience track its service credits, because")
    add("# the engine gives no script trigger for a duty's ability type. Regenerate after")
    add("# any EU5 update: a patch that adds or retunes a cabinet action changes this.")
    add("#")
    for note in notes:
        add(f"#   {note}")
    add(f"#   total: {len(mapping)} actions "
        f"({len(by_track['adm'])} adm, {len(by_track['dip'])} dip, {len(by_track['mil'])} mil)")
    add("#")
    add("# Called in CHARACTER scope from cc_xp_monthly_service (cc_xp_pulse.txt) for a")
    add("# minister currently holding a duty. Awards nothing when the duty is unrecognised,")
    add("# which is the correct behaviour for an action added by a mod we do not know about.")
    add("###############################################################################")
    add("")
    add("cc_xp_duty_track_award = {")

    for index, track in enumerate(TRACKS):
        names = by_track[track]
        if not names:
            continue
        keyword = "if" if index == 0 else "else_if"
        add(f"\t{keyword} = {{")
        add("\t\tlimit = {")
        add("\t\t\tOR = {")
        for name in names:
            add(f"\t\t\t\tcabinet_action = cabinet_action:{name}")
        add("\t\t\t}")
        add("\t\t}")
        add(f"\t\tcc_xp_gain_{track} = {{ AMOUNT = cc_xp_duty_tick }}")
        add("\t}")

    add("}")
    add("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                       help="exit 1 if the generated file is missing or stale")
    args = parser.parse_args()

    mapping, notes = collect()
    if not mapping:
        print("error: no cabinet actions found, refusing to write an empty lookup",
              file=sys.stderr)
        return 2

    rendered = render(mapping, notes)

    if args.check:
        if not OUT.exists():
            print(f"stale: {OUT.relative_to(REPO)} does not exist", file=sys.stderr)
            return 1
        if OUT.read_text(encoding="utf-8-sig") != rendered.lstrip("\ufeff"):
            print(f"stale: {OUT.relative_to(REPO)} differs from generated output",
                  file=sys.stderr)
            return 1
        print(f"up to date: {OUT.relative_to(REPO)}")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8")

    for note in notes:
        print(note)
    print(f"wrote {OUT.relative_to(REPO)}: {len(mapping)} actions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
