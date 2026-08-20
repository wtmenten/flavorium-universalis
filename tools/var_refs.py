#!/usr/bin/env python3
"""
Scan mod .txt files for Clausewitz variable references.

Usage:
  python tools/var_refs.py                       # list all variable names + counts
  python tools/var_refs.py cc_bond_cul           # refs for this variable (substring match)
  python tools/var_refs.py cc_bond               # all vars containing 'cc_bond'
  python tools/var_refs.py --op set,change       # filter by operation type
  python tools/var_refs.py --group file          # group output by file (default: by variable)
  python tools/var_refs.py --list                # just list variable names and counts
  python tools/var_refs.py --file in_game/events/cc_bond_chain_d.txt

Operation short names for --op filter:
  set        set_variable
  change     change_variable
  clamp      clamp_variable
  has        has_variable
  remove     remove_variable
  map_add    add_to_variable_map
  map_ref    any/random/every_key_in_variable_map  (the map name)
  var        var:X  (variable value read)
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

MOD_ROOT = Path(__file__).resolve().parent.parent
SEARCH_DIRS = ["in_game", "main_menu"]

SECTION_KEYS = frozenset(["option", "trigger", "immediate", "effect"])
MAP_OP_KEYS = frozenset([
    "any_key_in_variable_map",
    "random_key_in_variable_map",
    "every_key_in_variable_map",
])

OP_SHORT = {
    "set_variable":         "set",
    "change_variable":      "change",
    "clamp_variable":       "clamp",
    "has_variable":         "has",
    "remove_variable":      "remove",
    "add_to_variable_map":  "map_add",
    "variable_map":         "map_ref",
    "var:":                 "var",
}
SHORT_TO_OP = {v: k for k, v in OP_SHORT.items()}


# ── Parsing helpers ──────────────────────────────────────────────────────────

def strip_bom(data: bytes) -> bytes:
    return data[3:] if data[:3] == b"\xef\xbb\xbf" else data


def strip_inline_comment(line: str) -> str:
    idx = line.find("#")
    return line[:idx] if idx >= 0 else line


def extract_block_key(text_before_brace: str) -> str:
    """Return the identifier that opened a block, given text to the left of '{'."""
    t = text_before_brace.rstrip()
    # Remove trailing operator (= or ?=)
    t = re.sub(r"\s*\??=\s*$", "", t).rstrip()
    m = re.search(r"([\w.:]+)\s*$", t)
    return m.group(1) if m else "?"


def get_context(frames: list) -> tuple:
    """
    Return (top_block, section_str) from the current frame stack.
    top_block: name of the depth-1 block (event ID or scripted block name)
    section_str: first SECTION_KEYS frame above depth 1, e.g. 'option[cc_bonds.130.a]'
    """
    if not frames:
        return "?", None
    top_block = frames[0]["name"]
    section = None
    for frame in frames[1:]:
        key = frame["key"]
        if key in SECTION_KEYS:
            name = frame["name"]
            section = f"{key}[{name}]" if name != key else key
            break
    return top_block, section


# ── Variable reference extraction ────────────────────────────────────────────

# Matches single-line named ops: set/change/clamp_variable = { name = X ... }
_NAMED_OP_RE = re.compile(
    r"\b(set_variable|change_variable|clamp_variable)\s*=\s*\{[^}]*?\bname\s*=\s*(\w+)"
)
# Matches single-line add_to_variable_map = { name = X ... }
_MAP_ADD_RE = re.compile(
    r"\badd_to_variable_map\s*=\s*\{[^}]*?\bname\s*=\s*(\w+)"
)
# Matches single-line any/random/every_key_in_variable_map = { variable = X ... }
_MAP_OP_INLINE_RE = re.compile(
    r"\b(?:any|random|every)_key_in_variable_map\s*=\s*\{[^}]*?\bvariable\s*=\s*(\w+)"
)
_HAS_VAR_RE  = re.compile(r"\bhas_variable\s*=\s*(\w+)")
_REM_VAR_RE  = re.compile(r"\bremove_variable\s*=\s*(\w+)")
_VAR_REF_RE  = re.compile(r"\bvar:(\w+)")
# variable = X inside a multi-line map op block (detected via frame context)
_VARNAME_RE  = re.compile(r"(?<!\w)variable\s*=\s*(\w+)")
# Inline "variable_map(X|...)" comparison
_MAP_INLINE_STR_RE = re.compile(r'"variable_map\((\w+)\|')

# name = X inside a multi-line named op block (detected via frame context).
#
# _NAMED_OP_RE above only matches when the whole op fits on one line, because references are
# extracted line by line. The equally common block form
#     set_variable = {
#         name = cc_byz_union_stage
#         value = 2
#     }
# was therefore invisible, which silently undercounted WRITES. That is the dangerous
# direction for this tool: a variable written only in block form and never read produced no
# output at all rather than being reported as write-only, which is the exact failure the
# audit exists to catch.
_NAMED_OP_KEYS = {
    "set_variable",
    "change_variable",
    "clamp_variable",
    "add_to_variable_map",
}
_NAME_ASSIGN_RE = re.compile(r"(?<!\w)name\s*=\s*(\w+)")


def find_var_refs_on_line(line: str, frames: list) -> list:
    """Return list of (op, var_name) for all variable references on this line."""
    refs = []

    for m in _NAMED_OP_RE.finditer(line):
        refs.append((m.group(1), m.group(2)))

    for m in _MAP_ADD_RE.finditer(line):
        refs.append(("add_to_variable_map", m.group(1)))

    # Single-line map op with variable= on the same line
    for m in _MAP_OP_INLINE_RE.finditer(line):
        refs.append(("variable_map", m.group(1)))

    for m in _HAS_VAR_RE.finditer(line):
        refs.append(("has_variable", m.group(1)))

    for m in _REM_VAR_RE.finditer(line):
        refs.append(("remove_variable", m.group(1)))

    for m in _VAR_REF_RE.finditer(line):
        refs.append(("var:", m.group(1)))

    # Multi-line map op: we're inside an open map op block, so variable= here is the map name
    in_map_op = any(f["key"] in MAP_OP_KEYS for f in frames)
    if in_map_op:
        for m in _VARNAME_RE.finditer(line):
            # Don't double-count if already caught by _MAP_OP_INLINE_RE above
            refs.append(("variable_map", m.group(1)))

    for m in _MAP_INLINE_STR_RE.finditer(line):
        refs.append(("variable_map", m.group(1)))

    # Multi-line named op: the innermost open block is set/change/clamp_variable or
    # add_to_variable_map, so a bare `name = X` on this line names the variable.
    #
    # Checks the INNERMOST frame rather than any open frame, so that an option's own
    # `name = <loc key>` is not mistaken for a variable when a named op appears later in the
    # same option. Single-line ops cannot reach here: their frame is pushed and popped during
    # the character walk that runs before this function, so _NAMED_OP_RE keeps those and
    # there is no double count.
    if frames and frames[-1]["key"] in _NAMED_OP_KEYS:
        for m in _NAME_ASSIGN_RE.finditer(line):
            refs.append((frames[-1]["key"], m.group(1)))

    return refs


# ── File parser ───────────────────────────────────────────────────────────────

def parse_file(path: Path) -> list:
    """
    Parse one file. Returns list of dicts:
    { file, lineno, op, var, top_block, section }
    """
    rel = path.relative_to(MOD_ROOT).as_posix()
    try:
        raw = path.read_bytes()
        content = strip_bom(raw).decode("utf-8", errors="replace")
    except OSError:
        return []

    lines = content.splitlines()
    depth = 0
    frames: list = []  # [{'depth', 'key', 'name', 'awaiting_name'}, ...]
    results = []

    for lineno, raw_line in enumerate(lines, 1):
        line = strip_inline_comment(raw_line)

        # Walk characters to track depth and push/pop frames
        for pos, ch in enumerate(line):
            if ch == "{":
                depth += 1
                key = extract_block_key(line[:pos])
                frames.append({
                    "depth": depth,
                    "key": key,
                    "name": key,
                    "awaiting_name": key == "option",
                })
            elif ch == "}":
                # Pop any frames at the current depth before decrementing
                while frames and frames[-1]["depth"] >= depth:
                    frames.pop()
                depth -= 1

        # Resolve pending option name from 'name = X' assignment
        for frame in reversed(frames):
            if frame.get("awaiting_name"):
                m = re.search(r"\bname\s*=\s*(\S+)", line)
                if m:
                    frame["name"] = m.group(1)
                    frame["awaiting_name"] = False
                break

        # Extract variable references on this line
        for op, var_name in find_var_refs_on_line(line, frames):
            top_block, section = get_context(frames)
            results.append({
                "file":      rel,
                "lineno":    lineno,
                "op":        op,
                "var":       var_name,
                "top_block": top_block,
                "section":   section,
            })

    return results


# ── Output helpers ────────────────────────────────────────────────────────────

def format_context(ref: dict) -> str:
    top = ref["top_block"]
    sec = ref["section"]
    return f"{top} > {sec}" if sec else top


def print_grouped_by_var(refs: list) -> None:
    by_var: dict = defaultdict(list)
    for r in refs:
        by_var[r["var"]].append(r)

    for var_name in sorted(by_var):
        group = sorted(by_var[var_name], key=lambda x: (x["file"], x["lineno"]))
        count = len(group)
        print(f"\n{var_name}  [{count} reference{'s' if count != 1 else ''}]")
        for r in group:
            op_str = OP_SHORT.get(r["op"], r["op"])
            ctx    = format_context(r)
            print(f"  {r['file']}:{r['lineno']:<6}  {op_str:<10}  {ctx}")


def print_grouped_by_file(refs: list) -> None:
    by_file: dict = defaultdict(list)
    for r in refs:
        by_file[r["file"]].append(r)

    for filepath in sorted(by_file):
        print(f"\n{filepath}")
        for r in sorted(by_file[filepath], key=lambda x: x["lineno"]):
            op_str = OP_SHORT.get(r["op"], r["op"])
            ctx    = format_context(r)
            print(f"  :{r['lineno']:<6} {op_str:<10}  {r['var']:<40}  {ctx}")


def print_list(refs: list) -> None:
    counts: dict = defaultdict(int)
    for r in refs:
        counts[r["var"]] += 1
    max_len = max(len(n) for n in counts) if counts else 0
    for name in sorted(counts):
        print(f"{name:<{max_len}}  {counts[name]:>4}")


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find variable references in mod .txt files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "filter", nargs="?", default=None,
        help="Variable name filter (substring match). Omit to show all.",
    )
    parser.add_argument(
        "--op", default=None,
        help="Comma-separated op filter: set,change,clamp,has,remove,map_add,map_ref,var",
    )
    parser.add_argument(
        "--group", choices=["var", "file"], default="var",
        help="Group output by 'var' (default) or 'file'",
    )
    parser.add_argument(
        "--list", action="store_true",
        help="Just list variable names and reference counts",
    )
    parser.add_argument(
        "--file", default=None,
        help="Search only this file (relative path from mod root)",
    )
    args = parser.parse_args()

    # Resolve op filter
    op_filter = None
    if args.op:
        op_filter = set()
        for token in args.op.split(","):
            token = token.strip()
            if token in SHORT_TO_OP:
                op_filter.add(SHORT_TO_OP[token])
            elif token in OP_SHORT:
                op_filter.add(token)
            else:
                valid = ", ".join(sorted(OP_SHORT.values()))
                print(f"Unknown op '{token}'. Valid: {valid}", file=sys.stderr)
                sys.exit(1)

    # Collect files
    if args.file:
        target = MOD_ROOT / args.file
        if not target.exists():
            print(f"File not found: {target}", file=sys.stderr)
            sys.exit(1)
        files = [target]
    else:
        files = []
        for d in SEARCH_DIRS:
            p = MOD_ROOT / d
            if p.exists():
                files.extend(sorted(p.rglob("*.txt")))

    # Parse
    all_refs = []
    for f in files:
        all_refs.extend(parse_file(f))

    # Filter
    if args.filter:
        all_refs = [r for r in all_refs if args.filter in r["var"]]
    if op_filter:
        all_refs = [r for r in all_refs if r["op"] in op_filter]

    if not all_refs:
        msg = "No variable references found"
        if args.filter:
            msg += f" matching '{args.filter}'"
        print(msg + ".")
        return

    if args.list:
        print_list(all_refs)
    elif args.group == "file":
        print_grouped_by_file(all_refs)
    else:
        print_grouped_by_var(all_refs)


if __name__ == "__main__":
    main()
