#!/usr/bin/env python3
"""
vanilla_search.py — Search EU5 vanilla game files for modding reference.

Subcommands
-----------
  modifier <name>          Check if a modifier name is valid; show close matches and usage.
  values   <type_key>      List every type:value identifier used in vanilla common files.
                           e.g.  values religion_group
                                 values government_type
                                 values sub_continent
                                 values estate_type
  examples <term>          Show vanilla usage snippets for a trigger, effect, or key.
                           Add --events to search events/ instead of common/.
  biases                   List every defined bias / opinion modifier name.

Examples
--------
  python tools/vanilla_search.py modifier embrace_institution_cost_modifier
  python tools/vanilla_search.py modifier global_institution_spread          # partial OK
  python tools/vanilla_search.py values religion_group
  python tools/vanilla_search.py examples declare_war_with_cb --events
  python tools/vanilla_search.py biases
"""

import argparse
import os
import re
import sys

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

GAME_ROOT = r"F:\SteamLibrary\steamapps\common\Europa Universalis V\game"
IN_GAME   = os.path.join(GAME_ROOT, "in_game")
MAIN_MENU = os.path.join(GAME_ROOT, "main_menu")

STATIC_MODIFIERS_DIR  = os.path.join(MAIN_MENU, "common", "static_modifiers")
MODIFIER_TYPES_DIR    = os.path.join(MAIN_MENU, "common", "modifier_type_definitions")
IN_GAME_COMMON        = os.path.join(IN_GAME,   "common")
IN_GAME_EVENTS        = os.path.join(IN_GAME,   "events")
TRAITS_DIR            = os.path.join(IN_GAME_COMMON, "traits")
BIASES_DIR            = os.path.join(IN_GAME_COMMON, "biases")


def _check_game_root():
    if not os.path.isdir(GAME_ROOT):
        sys.exit(f"Game root not found: {GAME_ROOT}\nUpdate GAME_ROOT in tools/vanilla_search.py")


def _rel(path):
    """Return path relative to GAME_ROOT for readable output."""
    try:
        return os.path.relpath(path, GAME_ROOT)
    except ValueError:
        return path


# ---------------------------------------------------------------------------
# Core search helpers
# ---------------------------------------------------------------------------

def _iter_txt(root):
    """Yield every .txt file under root."""
    if not os.path.isdir(root):
        return
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".txt"):
                yield os.path.join(dirpath, name)


def _read(path):
    try:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
            return f.readlines()
    except OSError:
        return []


def _grep(root, pattern, context=0, max_hits=20):
    """
    Search files under root for pattern.
    Yields (path, 1-based line_num, matched_line, before_lines, after_lines).
    """
    rx = re.compile(pattern)
    hits = 0
    for path in _iter_txt(root):
        if hits >= max_hits:
            break
        lines = _read(path)
        for i, line in enumerate(lines):
            if hits >= max_hits:
                break
            if rx.search(line):
                before = [l.rstrip() for l in lines[max(0, i - context):i]]
                after  = [l.rstrip() for l in lines[i + 1 : i + 1 + context]]
                yield path, i + 1, line.rstrip(), before, after
                hits += 1


# ---------------------------------------------------------------------------
# modifier
# ---------------------------------------------------------------------------

def cmd_modifier(args):
    """
    1. Look for <name> defined as a top-level key in static_modifiers and
       modifier_type_definitions (those are the two canonical sources of
       valid modifier names).
    2. If not found exactly, try a fuzzy (partial) search for close matches.
    3. Either way, show usage examples from vanilla traits.
    """
    _check_game_root()
    name = args.name

    # Regex: name at start of non-comment content, followed by = or {
    exact_pattern = r"^\s{0,8}" + re.escape(name) + r"\s*[={]"

    # --- Search definition files ---
    defs = []
    for d in (STATIC_MODIFIERS_DIR, MODIFIER_TYPES_DIR):
        for path, lnum, line, _, _ in _grep(d, exact_pattern, max_hits=10):
            defs.append((path, lnum, line))

    if defs:
        print(f"[VALID]  '{name}' is defined in vanilla ({len(defs)} match(es)):")
        for path, lnum, line in defs[:6]:
            print(f"  {_rel(path)}:{lnum}  {line.strip()}")
    else:
        # Fuzzy: search for the name as a substring anywhere in the def files
        fuzzy = []
        for d in (STATIC_MODIFIERS_DIR, MODIFIER_TYPES_DIR):
            for path, lnum, line, _, _ in _grep(d, re.escape(name), max_hits=8):
                stripped = line.strip()
                if not stripped.startswith("#"):
                    fuzzy.append((path, lnum, stripped))

        print(f"[INVALID] '{name}' NOT found in static_modifiers or modifier_type_definitions.")
        if fuzzy:
            print(f"\n  Close matches containing '{name}':")
            for path, lnum, line in fuzzy[:6]:
                print(f"    {_rel(path)}:{lnum}  {line}")
        else:
            print(f"  No partial matches found either.")

    # --- Usage examples in vanilla traits ---
    print()
    examples = list(_grep(TRAITS_DIR, re.escape(name) + r"\s*[=<>!]", context=0, max_hits=5))
    if examples:
        print(f"Usage in vanilla traits ({len(examples)} shown):")
        for path, lnum, line, _, _ in examples:
            print(f"  {_rel(path)}:{lnum}  {line.strip()}")
    else:
        print("Not used in any vanilla trait definitions.")


# ---------------------------------------------------------------------------
# values
# ---------------------------------------------------------------------------

def cmd_values(args):
    """
    Collect every occurrence of  type_key:identifier  across in_game/common,
    deduplicate, and print sorted.  Works for any TYPE prefix:
      religion_group, government_type, sub_continent, estate_type,
      culture_group, area, ideology, casus_belli, age, location_rank …
    """
    _check_game_root()
    type_key = args.type_key
    pattern  = re.compile(re.escape(type_key) + r":([a-z0-9_]+)", re.IGNORECASE)

    values = set()
    for path in _iter_txt(IN_GAME_COMMON):
        lines = _read(path)
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            for m in pattern.finditer(line):
                values.add(m.group(0).lower())

    if not values:
        print(f"No '{type_key}:...' identifiers found in in_game/common.")
        print("Common type keys: religion_group, government_type, sub_continent,")
        print("  estate_type, culture_group, area, ideology, casus_belli, age, location_rank")
        return

    print(f"'{type_key}' values used in vanilla common files ({len(values)}):")
    for v in sorted(values):
        print(f"  {v}")


# ---------------------------------------------------------------------------
# examples
# ---------------------------------------------------------------------------

def cmd_examples(args):
    """
    Show vanilla usage snippets for any trigger, effect, or key name.
    Defaults to in_game/common; pass --events for events/.
    """
    _check_game_root()
    term    = args.term
    pattern = re.escape(term)

    if args.events:
        root  = IN_GAME_EVENTS
        label = "in_game/events"
    else:
        root  = IN_GAME_COMMON
        label = "in_game/common"

    results = list(_grep(root, pattern, context=2, max_hits=10))

    if not results:
        print(f"No examples of '{term}' found in {label}.")
        if not args.events:
            print("Try adding --events to search the events directory.")
        return

    print(f"Examples of '{term}' in {label} ({len(results)} found):")
    for path, lnum, line, before, after in results:
        print(f"\n  [{_rel(path)}:{lnum}]")
        for b in before:
            print(f"      {b}")
        print(f"  >>> {line}")
        for a in after:
            print(f"      {a}")


# ---------------------------------------------------------------------------
# biases
# ---------------------------------------------------------------------------

def cmd_biases(args):
    """List every top-level key defined in common/biases/ (opinions, antagonisms)."""
    _check_game_root()

    # Top-level keys: lines that start a block at column 0
    top_key = re.compile(r"^([a-z][a-z0-9_]+)\s*=\s*\{")
    names   = {}   # name -> (file, lnum)

    for path in _iter_txt(BIASES_DIR):
        for i, line in enumerate(_read(path), 1):
            m = top_key.match(line)
            if m:
                names[m.group(1)] = (_rel(path), i)

    if not names:
        print(f"No bias definitions found in {BIASES_DIR}")
        return

    print(f"Defined bias/opinion/antagonism names ({len(names)}):")

    # Group by source file for readability
    by_file = {}
    for name, (fpath, lnum) in names.items():
        by_file.setdefault(fpath, []).append((lnum, name))

    for fpath in sorted(by_file):
        print(f"\n  {fpath}:")
        for lnum, name in sorted(by_file[fpath]):
            print(f"    {name}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="cmd", required=True, metavar="subcommand")

    p = sub.add_parser("modifier", help="Check if a modifier name is valid in vanilla")
    p.add_argument("name", help="Modifier name (or partial) to look up")

    p = sub.add_parser("values", help="List all type:value identifiers used in vanilla")
    p.add_argument("type_key", help="Type prefix, e.g. religion_group / government_type")

    p = sub.add_parser("examples", help="Show vanilla usage snippets for a term")
    p.add_argument("term", help="Trigger/effect/modifier name to find examples of")
    p.add_argument("--events", action="store_true", help="Search events/ instead of common/")

    sub.add_parser("biases", help="List all defined bias/opinion modifier names")

    args = parser.parse_args()
    {
        "modifier": cmd_modifier,
        "values":   cmd_values,
        "examples": cmd_examples,
        "biases":   cmd_biases,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
