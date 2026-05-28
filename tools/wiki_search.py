#!/usr/bin/env python3
"""
wiki_search.py — Search offline EU5 modding wiki docs for effects, triggers, scope links, modifiers.

Subcommands
-----------
  effect <name> [<name> ...]
      Search the offline effect docs for effect name(s).
      Shows matching rows from the consolidated effect tables.

  trigger <name> [<name> ...]
      Search the offline trigger docs for trigger name(s).

  scope_link <name> [<name> ...]
      Search the offline scope_link docs for scope link name(s).

  modifier <name> [<name> ...]
      Search the offline modifier_types docs for modifier type name(s).

  on_action <name> [<name> ...]
      Search the offline on_actions docs for on-action name(s).

  all <term> [<term> ...]
      Search all offline docs for term(s).

Examples
--------
  python tools/wiki_search.py effect every_country
  python tools/wiki_search.py trigger has_war has_advance
  python tools/wiki_search.py scope_link overlord
  python tools/wiki_search.py modifier cabinet_efficiency
  python tools/wiki_search.py on_action on_game_start
  python tools/wiki_search.py all declare_war
"""

import argparse
import os
import re
import sys

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(ROOT_DIR)
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs", "offline-wiki")

DOC_FILES = {
    "effect": "core/effect.md",
    "trigger": "core/trigger.md",
    "scope_link": "core/scope_link.md",
    "modifier": "concepts/modifier_types.md",
    "on_action": "concepts/on_actions.md",
}

# Precompiled patterns for iterator consolidation display
ITERATOR_RE = re.compile(r"(every_|ordered_|random_|any_)([a-z_]+)")


def find_doc_file(key):
    """Resolve a doc file path."""
    rel = DOC_FILES.get(key)
    if rel:
        path = os.path.join(DOCS_DIR, rel)
        if os.path.isfile(path):
            return path
    return None


def search_file(filepath, terms, context=2):
    """
    Search a markdown file for term(s).
    Returns list of (line_num, line, context_lines_before, context_lines_after).
    """
    results = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return results

    patterns = [re.compile(re.escape(t), re.IGNORECASE) for t in terms]

    for i, line in enumerate(lines):
        for pat in patterns:
            if pat.search(line):
                before = [l.rstrip() for l in lines[max(0, i - context):i]]
                after = [l.rstrip() for l in lines[i + 1: min(len(lines), i + context + 1)]]
                results.append((i + 1, line.rstrip(), before, after))
                break  # Don't double-count same line for multiple terms

    return results


def format_results(results, filepath, term):
    """Format search results for display."""
    if not results:
        print(f"No matches for '{term}' in {os.path.basename(filepath)}.")
        return

    rel_path = os.path.relpath(filepath, PROJECT_ROOT)
    print(f"Matches for '{term}' in {rel_path} ({len(results)} found):")

    for lnum, line, before, after in results:
        print(f"\n  [{rel_path}:{lnum}]")
        for b in before:
            print(f"    | {b}")
        print(f"  >>| {line}")
        for a in after:
            print(f"    | {a}")


def search_table_column(filepath, terms, column=0):
    """
    Search specifically the first column of markdown tables for exact/partial matches.
    More precise for effect/trigger/scope_link lookups.
    """
    results = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return results

    patterns = [re.compile(re.escape(t), re.IGNORECASE) for t in terms]

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Only match table rows (start with |)
        if not stripped.startswith("|"):
            continue
        # Skip separator rows
        if re.match(r"^\|[\s\-|]+\|$", stripped):
            continue

        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if not cells:
            continue

        # Check first cell (the effect/trigger/scope_link name)
        first_cell = cells[0]
        for pat in patterns:
            if pat.search(first_cell):
                # Also check if consolidated iterator (e.g., every/any_country)
                results.append((i + 1, stripped, cells))
                break

    return results


def format_table_results(results, filepath, terms):
    """Format table search results."""
    if not results:
        terms_str = " ".join(terms)
        print(f"No matches for '{terms_str}' in {os.path.basename(filepath)}.")
        return

    rel_path = os.path.relpath(filepath, PROJECT_ROOT)
    terms_str = " ".join(terms)
    print(f"Matches for '{terms_str}' in {rel_path} ({len(results)} found):")

    for lnum, line, cells in results:
        # Expand consolidated iterator notation
        first_cell = cells[0]
        expanded = ITERATOR_RE.sub(lambda m: f"{m.group(1)}{m.group(2)}", first_cell)

        print(f"\n  [{lnum}] {first_cell}")
        if len(cells) >= 2 and cells[1]:
            print(f"  Description: {cells[1]}")
        if len(cells) >= 3 and cells[2]:
            print(f"  {' | '.join(cells[2:])}")


def cmd_effect(args):
    """Search effects."""
    path = find_doc_file("effect")
    if not path:
        print(f"Effect docs not found. Run 'python tools/wiki_scraper.py' first.")
        return
    results = search_table_column(path, args.names)
    if results:
        format_table_results(results, path, args.names)
    else:
        # Fallback to full text search
        for name in args.names:
            results = search_file(path, [name])
            format_results(results, path, name)


def cmd_trigger(args):
    """Search triggers."""
    path = find_doc_file("trigger")
    if not path:
        print(f"Trigger docs not found. Run 'python tools/wiki_scraper.py' first.")
        return
    results = search_table_column(path, args.names)
    if results:
        format_table_results(results, path, args.names)
    else:
        for name in args.names:
            results = search_file(path, [name])
            format_results(results, path, name)


def cmd_scope_link(args):
    """Search scope links."""
    path = find_doc_file("scope_link")
    if not path:
        print(f"Scope link docs not found. Run 'python tools/wiki_scraper.py' first.")
        return
    results = search_table_column(path, args.names)
    if results:
        format_table_results(results, path, args.names)
    else:
        for name in args.names:
            results = search_file(path, [name])
            format_results(results, path, name)


def cmd_modifier(args):
    """Search modifier types."""
    path = find_doc_file("modifier")
    if not path:
        print(f"Modifier docs not found. Run 'python tools/wiki_scraper.py' first.")
        return
    results = search_table_column(path, args.names)
    if results:
        format_table_results(results, path, args.names)
    else:
        for name in args.names:
            results = search_file(path, [name])
            format_results(results, path, name)


def cmd_on_action(args):
    """Search on-actions."""
    path = find_doc_file("on_action")
    if not path:
        print(f"On-action docs not found. Run 'python tools/wiki_scraper.py' first.")
        return
    results = search_table_column(path, args.names)
    if results:
        format_table_results(results, path, args.names)
    else:
        for name in args.names:
            results = search_file(path, [name])
            format_results(results, path, name)


def cmd_all(args):
    """Search all offline docs."""
    for name, rel in DOC_FILES.items():
        path = os.path.join(DOCS_DIR, rel)
        if not os.path.isfile(path):
            continue
        for term in args.terms:
            results = search_file(path, [term], context=1)
            if results:
                format_results(results, path, term)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True, metavar="subcommand")

    p = sub.add_parser("effect", help="Search effect docs")
    p.add_argument("names", nargs="+", help="Effect name(s) to search for")

    p = sub.add_parser("trigger", help="Search trigger docs")
    p.add_argument("names", nargs="+", help="Trigger name(s) to search for")

    p = sub.add_parser("scope_link", help="Search scope link docs")
    p.add_argument("names", nargs="+", help="Scope link name(s) to search for")

    p = sub.add_parser("modifier", help="Search modifier type docs")
    p.add_argument("names", nargs="+", help="Modifier type name(s) to search for")

    p = sub.add_parser("on_action", help="Search on-action docs")
    p.add_argument("names", nargs="+", help="On-action name(s) to search for")

    p = sub.add_parser("all", help="Search all offline docs")
    p.add_argument("terms", nargs="+", help="Term(s) to search for")

    args = parser.parse_args()
    {
        "effect": cmd_effect,
        "trigger": cmd_trigger,
        "scope_link": cmd_scope_link,
        "modifier": cmd_modifier,
        "on_action": cmd_on_action,
        "all": cmd_all,
    }[args.cmd](args)


if __name__ == "__main__":
    main()
