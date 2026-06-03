"""
Release script for Flavorium Universalis.

Builds and uploads the mod to Steam Workshop via upload.py.

Usage:
    python tools/release.py           # upload mod content (default)
    python tools/release.py -wp       # upload workshop pages only
    python tools/release.py -m -wp    # upload mod + workshop pages
    python tools/release.py -d        # upload dev item
    python tools/release.py -cn       # upload change notes
"""

import json
import os
import subprocess
import sys

MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METADATA_PATH = os.path.join(MOD_ROOT, ".metadata", "metadata.json")
UPLOAD_SCRIPT = os.path.join(MOD_ROOT, "tools", "upload.py")


def read_version():
    with open(METADATA_PATH, encoding="utf-8-sig") as f:
        meta = json.load(f)
    return meta.get("version", "unknown"), meta.get("name", "unknown")


def main():
    version, name = read_version()

    print(f"\n=== {name} — Release {version} ===")
    print()

    answer = input("Build and upload to Steam Workshop? [y/N] ").strip().lower()
    if answer != "y":
        print("Aborted.")
        sys.exit(0)

    print()
    result = subprocess.run([sys.executable, UPLOAD_SCRIPT] + sys.argv[1:])
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
