#!/usr/bin/env python3
"""
vanilla_search.py — Search EU5 vanilla game files for modding reference.

Subcommands
-----------
  modifier <name> [<name> ...]
      Check if modifier name(s) are valid; show close matches and trait usage.
      All names are verified in a single traversal of definition files.

  values <type_key> [<type_key> ...]
      List every type:value identifier used in vanilla common/events files.
      Matches both  type_key:value  and  is_type_key = value  forms.
      All type keys are collected in a single traversal.

  examples <term> [<term> ...]
      Show vanilla usage snippets for trigger/effect/key name(s).
      Add --events to search events/ instead of common/.
      All terms are matched in a single traversal.

  biases
      List every defined bias / opinion modifier name.

Examples
--------
  python tools/vanilla_search.py modifier embrace_institution_cost_modifier
  python tools/vanilla_search.py modifier global_trade_power fort_maintenance_cost stability_cost
  python tools/vanilla_search.py values religion_group government_type sub_continent
  python tools/vanilla_search.py values subject_type estate_type
  python tools/vanilla_search.py examples declare_war_with_cb
  python tools/vanilla_search.py examples has_advance has_advance_available --events
  python tools/vanilla_search.py biases
"""

import argparse
import os
import re
import sys

from game_paths import game_root

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

GAME_ROOT = game_root()
IN_GAME   = os.path.join(GAME_ROOT, "in_game")
MAIN_MENU = os.path.join(GAME_ROOT, "main_menu")
DLC_ROOT  = os.path.join(GAME_ROOT, "dlc")

STATIC_MODIFIERS_DIR  = os.path.join(MAIN_MENU, "common", "static_modifiers")
MODIFIER_TYPES_DIR    = os.path.join(MAIN_MENU, "common", "modifier_type_definitions")
IN_GAME_COMMON        = os.path.join(IN_GAME,   "common")
IN_GAME_EVENTS        = os.path.join(IN_GAME,   "events")
TRAITS_DIR            = os.path.join(IN_GAME_COMMON, "traits")
BIASES_DIR            = os.path.join(IN_GAME_COMMON, "biases")


def _check_game_root():
    if not os.path.isdir(GAME_ROOT):
        sys.exit(f"Game root not found: {GAME_ROOT}\nUpdate GAME_ROOT in tools/vanilla_search.py")


def _dlc_equiv(base_dir):
    """Yield the equivalent directory inside each installed DLC."""
    if not os.path.isdir(DLC_ROOT):
        return
    try:
        rel = os.path.relpath(base_dir, GAME_ROOT)
    except ValueError:
        return
    for dlc_name in sorted(os.listdir(DLC_ROOT)):
        candidate = os.path.join(DLC_ROOT, dlc_name, rel)
        if os.path.isdir(candidate):
            yield candidate


def _all_roots(base_dir):
    """Yield base_dir (if it exists) then all DLC equivalents."""
    if os.path.isdir(base_dir):
        yield base_dir
    yield from _dlc_equiv(base_dir)


def _rel(path):
    """Return path relative to GAME_ROOT for readable output."""
    try:
        return os.path.relpath(path, GAME_ROOT)
    except ValueError:
        return path


# ---------------------------------------------------------------------------
# Core file helpers
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


# ---------------------------------------------------------------------------
# modifier
# ---------------------------------------------------------------------------

def cmd_modifier(args):
    """
    For each name: look for it defined as a top-level key in static_modifiers
    and modifier_type_definitions.  If not found exactly, show fuzzy matches.
    Also show usage examples from vanilla traits.
    All names are checked in a single traversal of each directory tree.
    """
    _check_game_root()
    names = args.names

    # Per-name compiled patterns
    exact_rxs = {n: re.compile(r"^\s{0,8}" + re.escape(n) + r"\s*[={]") for n in names}
    fuzzy_rxs = {n: re.compile(re.escape(n))                              for n in names}
    trait_rxs = {n: re.compile(re.escape(n) + r"\s*[=<>!]")              for n in names}

    defs  = {n: [] for n in names}   # exact hits in def files
    fuzzy = {n: [] for n in names}   # fuzzy hits in def files (only if no exact)
    trait_hits = {n: [] for n in names}

    # Single traversal of definition directories
    for d in (STATIC_MODIFIERS_DIR, MODIFIER_TYPES_DIR):
        for root in _all_roots(d):
            for path in _iter_txt(root):
                lines = _read(path)
                rel   = _rel(path)
                for i, line in enumerate(lines, 1):
                    stripped = line.strip()
                    if stripped.startswith("#"):
                        continue
                    for n in names:
                        if len(defs[n]) < 10 and exact_rxs[n].search(line):
                            defs[n].append((rel, i, stripped))
                        elif len(fuzzy[n]) < 8 and fuzzy_rxs[n].search(line):
                            fuzzy[n].append((rel, i, stripped))

    # Single traversal of traits
    for root in _all_roots(TRAITS_DIR):
        for path in _iter_txt(root):
            lines = _read(path)
            rel   = _rel(path)
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                if stripped.startswith("#"):
                    continue
                for n in names:
                    if len(trait_hits[n]) < 5 and trait_rxs[n].search(line):
                        trait_hits[n].append((rel, i, stripped))

    # Output grouped by name
    for idx, n in enumerate(names):
        if idx > 0:
            print()
        if defs[n]:
            print(f"[VALID]  '{n}' is defined in vanilla ({len(defs[n])} match(es)):")
            for fpath, lnum, line in defs[n][:6]:
                print(f"  {fpath}:{lnum}  {line}")
        else:
            print(f"[INVALID] '{n}' NOT found in static_modifiers or modifier_type_definitions.")
            if fuzzy[n]:
                print(f"\n  Close matches containing '{n}':")
                for fpath, lnum, line in fuzzy[n][:6]:
                    print(f"    {fpath}:{lnum}  {line}")
            else:
                print(f"  No partial matches found either.")

        print()
        if trait_hits[n]:
            print(f"Usage in vanilla traits ({len(trait_hits[n])} shown):")
            for fpath, lnum, line in trait_hits[n]:
                print(f"  {fpath}:{lnum}  {line}")
        else:
            print("Not used in any vanilla trait definitions.")


# ---------------------------------------------------------------------------
# values
# ---------------------------------------------------------------------------

def cmd_values(args):
    """
    For each type_key: collect every type_key:identifier and is_type_key = value
    occurrence across in_game/common and in_game/events.
    All type keys are gathered in a single traversal.
    """
    _check_game_root()
    type_keys = args.type_keys

    # Per-type-key compiled patterns
    patterns = {
        tk: (
            re.compile(re.escape(tk) + r":([a-z0-9_]+)", re.IGNORECASE),
            re.compile(
                r"\bis_" + re.escape(tk) + r"\s*=\s*(?:" + re.escape(tk) + r":)?([a-z0-9_]+)",
                re.IGNORECASE,
            ),
        )
        for tk in type_keys
    }

    values = {tk: set() for tk in type_keys}

    for base in (IN_GAME_COMMON, IN_GAME_EVENTS):
        for root in _all_roots(base):
            for path in _iter_txt(root):
                lines = _read(path)
                for line in lines:
                    if line.strip().startswith("#"):
                        continue
                    for tk in type_keys:
                        p_prefixed, p_is = patterns[tk]
                        for m in p_prefixed.finditer(line):
                            values[tk].add(m.group(0).lower())
                        for m in p_is.finditer(line):
                            values[tk].add(f"{tk.lower()}:{m.group(1).lower()}")

    for idx, tk in enumerate(type_keys):
        if idx > 0:
            print()
        if not values[tk]:
            print(f"No '{tk}:...' identifiers found in vanilla.")
            print("Common type keys: religion_group, government_type, sub_continent,")
            print("  estate_type, culture_group, subject_type, area, ideology, age")
        else:
            print(f"'{tk}' values used in vanilla ({len(values[tk])}):")
            for v in sorted(values[tk]):
                print(f"  {v}")


# ---------------------------------------------------------------------------
# examples
# ---------------------------------------------------------------------------

def cmd_examples(args):
    """
    Show vanilla usage snippets for one or more trigger/effect/key names.
    All terms are matched in a single traversal.
    """
    _check_game_root()
    terms = args.terms

    if args.events:
        base_root = IN_GAME_EVENTS
        label     = "in_game/events"
    else:
        base_root = IN_GAME_COMMON
        label     = "in_game/common"

    patterns = {t: re.compile(re.escape(t)) for t in terms}
    results  = {t: [] for t in terms}   # term -> [(rel_path, lnum, line, before, after)]

    for root in _all_roots(base_root):
        for path in _iter_txt(root):
            if all(len(results[t]) >= 10 for t in terms):
                break
            lines = _read(path)
            rel   = _rel(path)
            for i, line in enumerate(lines):
                for t in terms:
                    if len(results[t]) >= 10:
                        continue
                    if patterns[t].search(line):
                        before = [l.rstrip() for l in lines[max(0, i - 2):i]]
                        after  = [l.rstrip() for l in lines[i + 1 : i + 3]]
                        results[t].append((rel, i + 1, line.rstrip(), before, after))

    for idx, t in enumerate(terms):
        if idx > 0:
            print()
        if not results[t]:
            print(f"No examples of '{t}' found in {label}.")
            if not args.events:
                print("Try adding --events to search the events directory.")
        else:
            print(f"Examples of '{t}' in {label} ({len(results[t])} found):")
            for rel_path, lnum, line, before, after in results[t]:
                print(f"\n  [{rel_path}:{lnum}]")
                for b in before:
                    print(f"      {b}")
                print(f"  >>> {line}")
                for a in after:
                    print(f"      {a}")


# ---------------------------------------------------------------------------
# biases
# ---------------------------------------------------------------------------

def cmd_biases(_):
    """List every top-level key defined in common/biases/ (opinions, antagonisms)."""
    _check_game_root()

    top_key = re.compile(r"^([a-z][a-z0-9_]+)\s*=\s*\{")
    names   = {}   # name -> (rel_path, lnum)

    for root in _all_roots(BIASES_DIR):
        for path in _iter_txt(root):
            for i, line in enumerate(_read(path), 1):
                m = top_key.match(line)
                if m:
                    names[m.group(1)] = (_rel(path), i)

    if not names:
        print(f"No bias definitions found in {BIASES_DIR}")
        return

    print(f"Defined bias/opinion/antagonism names ({len(names)}):")
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

    p = sub.add_parser("modifier", help="Check if modifier name(s) are valid in vanilla")
    p.add_argument("names", nargs="+", metavar="name",
                   help="One or more modifier names (partial names OK)")

    p = sub.add_parser("values", help="List all type:value identifiers for one or more type keys")
    p.add_argument("type_keys", nargs="+", metavar="type_key",
                   help="One or more type prefixes, e.g. religion_group subject_type")

    p = sub.add_parser("examples", help="Show vanilla usage snippets for one or more terms")
    p.add_argument("terms", nargs="+", metavar="term",
                   help="One or more trigger/effect/modifier names")
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
