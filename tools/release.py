"""
Release script for Flavorium Universalis.

Stages a clean copy of the mod (game content only) into release/,
then runs pdx-workshop-manager to upload it to Steam Workshop.

Usage:
    python tools/release.py
"""

import json
import os
import shutil
import subprocess
import sys

MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELEASE_DIR = os.path.join(MOD_ROOT, "release")
METADATA_PATH = os.path.join(MOD_ROOT, ".metadata", "metadata.json")
WORKSHOP_EXE = os.path.join(MOD_ROOT, "tools", "workshop_manager", "pdx-workshop-manager.exe")

INCLUDE = [
    ".metadata",
    "in_game",
    "main_menu",
    "loading_screen",
    "thumbnail.png",
]

EXCLUDE_NAMES = {
    ".git", ".claude", "docs", "tools", "assets",
    "release", "__pycache__",
}


def read_version():
    with open(METADATA_PATH, encoding="utf-8-sig") as f:
        meta = json.load(f)
    return meta.get("version", "unknown"), meta.get("name", "unknown")


def stage_release():
    if os.path.exists(RELEASE_DIR):
        shutil.rmtree(RELEASE_DIR)
    os.makedirs(RELEASE_DIR)

    for item in INCLUDE:
        src = os.path.join(MOD_ROOT, item)
        dst = os.path.join(RELEASE_DIR, item)
        if not os.path.exists(src):
            print(f"  [skip] {item} (not found)")
            continue
        if os.path.isdir(src):
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*EXCLUDE_NAMES))
        else:
            shutil.copy2(src, dst)
        print(f"  [copy] {item}")


def run_workshop_manager():
    exe_dir = os.path.join(MOD_ROOT, "tools", "workshop_manager")
    result = subprocess.run(
        [WORKSHOP_EXE],
        cwd=exe_dir,
    )
    return result.returncode


def main():
    version, name = read_version()

    print(f"\n=== Flavorium Universalis — Release {version} ===")
    print(f"Mod name : {name}")
    print(f"Staging  : {RELEASE_DIR}")
    print(f"Includes : {', '.join(INCLUDE)}")
    print()

    answer = input("Stage release and upload to Steam Workshop? [y/N] ").strip().lower()
    if answer != "y":
        print("Aborted.")
        sys.exit(0)

    print("\nStaging release folder...")
    stage_release()
    print("Done.\n")

    print("Running pdx-workshop-manager...")
    code = run_workshop_manager()
    if code != 0:
        print(f"\n[ERROR] Workshop manager exited with code {code}")
        sys.exit(code)
    print("\nUpload complete.")


if __name__ == "__main__":
    main()
