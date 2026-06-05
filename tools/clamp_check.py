#!/usr/bin/env python3
"""
Scan EU5 mod script files for inverted min/max clamp errors on negative values.

When a script-value block contains both  min = -A  and  max = -B  as literal
negative numbers and min > max (i.e. min is less negative than max), the clamp
range is logically backwards — the more-negative value belongs in min.

  BAD:  min = -25   max = -100   (min -25 > max -100 → impossible range)
  OK:   min = -100  max = -25

The fix is to swap the two numeric values in-place.

Detection uses brace-depth tracking so only values inside the same {} block
are paired; nested blocks are handled independently.

Usage:
    python tools/clamp_check.py                  # dry-run, scan in_game/
    python tools/clamp_check.py --fix            # fix in-place
    python tools/clamp_check.py [--fix] <path>   # specific file or directory
"""

import re
import sys
from pathlib import Path

MOD_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCAN = MOD_ROOT / "in_game"

MIN_RE = re.compile(r"(\bmin\s*=\s*)(-\d+(?:\.\d+)?)")
MAX_RE = re.compile(r"(\bmax\s*=\s*)(-\d+(?:\.\d+)?)")


def _fmt(v: float) -> str:
    return str(int(v)) if v == int(v) else str(v)


def _rel(path: Path) -> Path:
    try:
        return path.relative_to(MOD_ROOT)
    except ValueError:
        return path


def scan_file(path: Path, fix: bool = False) -> int:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except Exception as e:
        print(f"  [skip] {path}: {e}")
        return 0

    lines = text.splitlines(keepends=True)
    depth = 0
    # pending[depth] = {'min': (line_idx, float_val), 'max': (line_idx, float_val)}
    pending: dict[int, dict] = {}
    errors: list[tuple[int, int, float, float]] = []

    for idx, line in enumerate(lines):
        code = line.split("#")[0]  # strip inline comments

        m = MIN_RE.search(code)
        if m:
            pending.setdefault(depth, {})["min"] = (idx, float(m.group(2)))

        m = MAX_RE.search(code)
        if m:
            pending.setdefault(depth, {})["max"] = (idx, float(m.group(2)))

        depth += code.count("{") - code.count("}")

        # After depth decreases, close any blocks now deeper than current depth.
        # Sequential sibling blocks reuse the same depth slot cleanly because
        # we pop the entry when closing.
        for d in [k for k in list(pending) if k > depth]:
            block = pending.pop(d)
            if "min" in block and "max" in block:
                min_idx, min_val = block["min"]
                max_idx, max_val = block["max"]
                if min_val < 0 and max_val < 0 and min_val > max_val:
                    errors.append((min_idx, max_idx, min_val, max_val))

    if not errors:
        return 0

    rel = _rel(path)
    for min_idx, max_idx, min_val, max_val in errors:
        tag = "[FIX]" if fix else "[ERR]"
        print(
            f"  {tag}  {rel}:{min_idx + 1}"
            f"  min={_fmt(min_val)}  max={_fmt(max_val)}"
            f"  ->  min={_fmt(max_val)}  max={_fmt(min_val)}"
        )

    if fix:
        for min_idx, max_idx, min_val, max_val in errors:
            lines[min_idx] = MIN_RE.sub(
                lambda m, v=max_val: m.group(1) + _fmt(v), lines[min_idx]
            )
            lines[max_idx] = MAX_RE.sub(
                lambda m, v=min_val: m.group(1) + _fmt(v), lines[max_idx]
            )
        path.write_text("".join(lines), encoding="utf-8-sig")

    return len(errors)


def collect_files(paths: list[str]) -> list[Path]:
    targets: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            targets.append(p)
        elif p.is_dir():
            targets.extend(sorted(p.rglob("*.txt")))
        else:
            print(f"  [warn] path not found: {p}")
    return targets


def main() -> None:
    argv = sys.argv[1:]
    fix = "--fix" in argv
    raw_paths = [a for a in argv if not a.startswith("--")]
    targets = collect_files(raw_paths or [str(DEFAULT_SCAN)])

    if not targets:
        print("No .txt files found.")
        return

    total = sum(scan_file(f, fix=fix) for f in targets)

    print()
    if total == 0:
        print("No inverted clamp errors found.")
    elif fix:
        print(f"Fixed {total} error(s).")
    else:
        print(f"Found {total} error(s).  Run with --fix to correct them.")


if __name__ == "__main__":
    main()
