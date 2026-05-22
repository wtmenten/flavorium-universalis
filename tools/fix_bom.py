#!/usr/bin/env python3
"""
fix_bom.py — Ensure UTF-8 BOM on all EU5 mod script and localization files.

EU5 requires UTF-8 BOM on .txt and .yml files or it silently ignores them.
Run manually or via the git pre-commit hook.

Usage:
    python tools/fix_bom.py           # fix + report
    python tools/fix_bom.py --check   # report only, exit 1 if any missing
"""

import argparse
import os
import sys

BOM = b"\xef\xbb\xbf"
EXTENSIONS = {".txt", ".yml"}
SCAN_DIRS = ["in_game", "main_menu"]


def find_mod_root():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here)


def scan(root, check_only):
    missing = []
    fixed = []

    for scan_dir in SCAN_DIRS:
        base = os.path.join(root, scan_dir)
        if not os.path.isdir(base):
            continue
        for dirpath, _, filenames in os.walk(base):
            for name in filenames:
                if os.path.splitext(name)[1].lower() not in EXTENSIONS:
                    continue
                path = os.path.join(dirpath, name)
                with open(path, "rb") as f:
                    content = f.read()
                if content.startswith(BOM):
                    continue
                rel = os.path.relpath(path, root)
                if check_only:
                    missing.append(rel)
                else:
                    with open(path, "wb") as f:
                        f.write(BOM + content)
                    fixed.append(rel)

    return fixed, missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report missing BOMs without fixing; exit 1 if any found.",
    )
    args = parser.parse_args()

    root = find_mod_root()
    fixed, missing = scan(root, args.check)

    if args.check:
        if missing:
            print(f"Missing BOM on {len(missing)} file(s):")
            for p in missing:
                print(f"  {p}")
            sys.exit(1)
        else:
            print("All files have UTF-8 BOM.")
    else:
        if fixed:
            print(f"Added BOM to {len(fixed)} file(s):")
            for p in fixed:
                print(f"  {p}")
        else:
            print("All files already have UTF-8 BOM.")


if __name__ == "__main__":
    main()
