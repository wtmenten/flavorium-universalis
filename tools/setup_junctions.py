"""
Create Windows directory junctions so EU5 can load submods directly from
the mod/ folder while their source files live under submods/ in this repo.

Run once after cloning, and again whenever a new submod is added:
    python tools/setup_junctions.py
"""

import json
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)   # cabinets-and-choices/
MOD_DIR = os.path.dirname(ROOT_DIR)      # mod/
SUBMODS_DIR = os.path.join(ROOT_DIR, "submods")


def load_submod_name(submod_dir):
    meta_path = os.path.join(submod_dir, ".metadata", "metadata.json")
    try:
        with open(meta_path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"  Warning: no metadata.json at {meta_path} — skipping.")
        return None
    except Exception as e:
        print(f"  Warning: failed to read {meta_path}: {e} — skipping.")
        return None

    name = data.get("name")
    if not name or not str(name).strip():
        print(f"  Warning: no 'name' field in {meta_path} — skipping.")
        return None
    return str(name).strip()


def junction_target(path):
    """Return the target of a junction/symlink, or None if not a junction."""
    try:
        return os.readlink(path)
    except (OSError, NotImplementedError):
        return None


def create_junction(link_path, target_path):
    existing_target = junction_target(link_path)
    if existing_target is not None:
        if os.path.normcase(os.path.abspath(existing_target)) == os.path.normcase(os.path.abspath(target_path)):
            print(f"    Already up to date.")
            return True
        print(f"    Removing stale junction (was → {existing_target})")
        try:
            os.rmdir(link_path)
        except Exception as e:
            print(f"    Error: could not remove stale junction: {e}")
            return False
    elif os.path.exists(link_path):
        print(f"    Error: {link_path} exists as a real directory — remove it manually.")
        return False

    result = subprocess.run(
        f'mklink /J "{link_path}" "{target_path}"',
        shell=True,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        msg = (result.stderr or result.stdout).strip()
        print(f"    Error: mklink failed: {msg}")
        return False
    return True


def main():
    if sys.platform != "win32":
        print("This script is Windows-only (uses mklink /J).")
        return 1

    if not os.path.isdir(SUBMODS_DIR):
        print(f"No submods/ directory found at {SUBMODS_DIR}.")
        return 0

    folders = sorted(
        e for e in os.listdir(SUBMODS_DIR)
        if os.path.isdir(os.path.join(SUBMODS_DIR, e))
    )
    if not folders:
        print("No submod folders found.")
        return 0

    print(f"Mod folder : {MOD_DIR}")
    print(f"Submods    : {SUBMODS_DIR}")
    print()

    errors = 0
    for folder in folders:
        submod_dir = os.path.join(SUBMODS_DIR, folder)
        mod_name = load_submod_name(submod_dir)
        if mod_name is None:
            errors += 1
            continue

        link_path = os.path.join(MOD_DIR, mod_name)
        print(f"  {mod_name}  (submods/{folder})")
        if create_junction(link_path, submod_dir):
            print(f"    {link_path}")
        else:
            errors += 1

    print()
    if errors:
        print(f"Done — {errors} error(s).")
        return 1
    print("Done — all junctions in place.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
