"""
Create Windows directory junctions so EU5 can load this mod and its submods
from the game's mod/ folder while the source files live in this repo.

Run once after cloning, and again whenever a new submod is added:
    python tools/setup_junctions.py

The mod folder is resolved in this order:
    1. --mod-dir "<path>"
    2. the EU5_MOD_DIR environment variable
    3. the repo's parent, if it is itself named "mod" (repo cloned inside mod/)
    4. <Documents>/Paradox Interactive/Europa Universalis V/mod, with Documents
       read from the registry so a OneDrive-redirected Documents is found
When the repo is not inside the mod folder, the main mod is junctioned too.
"""

import json
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)   # flavorium-universalis/
SUBMODS_DIR = os.path.join(ROOT_DIR, "submods")

EU5_USER_SUBPATH = os.path.join("Paradox Interactive", "Europa Universalis V", "mod")


def documents_dir():
    """The user's Documents folder, honouring a OneDrive/known-folder redirect."""
    try:
        import winreg

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
        )
        with key:
            value, _ = winreg.QueryValueEx(key, "Personal")
        return os.path.expandvars(value)
    except Exception:
        return os.path.join(os.path.expanduser("~"), "Documents")


def resolve_mod_dir(argv):
    if "--mod-dir" in argv:
        i = argv.index("--mod-dir")
        if i + 1 >= len(argv):
            print("Error: --mod-dir needs a path argument.")
            return None
        return os.path.abspath(argv[i + 1])

    env = os.environ.get("EU5_MOD_DIR")
    if env:
        return os.path.abspath(env)

    parent = os.path.dirname(ROOT_DIR)
    if os.path.basename(parent).lower() == "mod":
        return parent

    return os.path.join(documents_dir(), EU5_USER_SUBPATH)


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


def normalize_path(path):
    """Normalize a path for comparison. os.readlink on a Windows junction can
    return a target with a \\\\?\\ or \\??\\ prefix; strip it so path comparisons
    against a plain absolute path succeed."""
    for prefix in ("\\\\?\\", "\\??\\"):
        if path.startswith(prefix):
            path = path[len(prefix):]
            break
    return os.path.normcase(os.path.abspath(path))


def create_junction(link_path, target_path):
    existing_target = junction_target(link_path)
    if existing_target is not None:
        if normalize_path(existing_target) == normalize_path(target_path):
            print(f"    Already up to date.")
            return True
        print(f"    Removing stale junction (was -> {existing_target})")
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


def prune_stale_junctions(mod_dir, valid_names):
    """Remove junctions in mod_dir that point into this repo but whose name is no
    longer a current mod name. This is what clears out renamed links (e.g. old
    '1.3 Beta ...' names) after a submod is renamed. Only reparse points that
    resolve inside this repo are touched — real directories and unrelated links
    are left alone."""
    repo_root = normalize_path(ROOT_DIR)
    removed = 0
    for entry in sorted(os.listdir(mod_dir)):
        link_path = os.path.join(mod_dir, entry)
        target = junction_target(link_path)
        if target is None:
            continue  # real directory or not a reparse point
        target_abs = normalize_path(target)
        if target_abs != repo_root and not target_abs.startswith(repo_root + os.sep):
            continue  # junction points outside this repo — not ours
        if entry in valid_names:
            continue  # matches a current submod name — keep
        print(f"  Pruning stale junction: {entry}")
        print(f"    (was -> {target})")
        try:
            os.rmdir(link_path)
            removed += 1
        except Exception as e:
            print(f"    Error: could not remove {link_path}: {e}")
    return removed


def main(argv):
    if sys.platform != "win32":
        print("This script is Windows-only (uses mklink /J).")
        return 1

    if not os.path.isdir(SUBMODS_DIR):
        print(f"No submods/ directory found at {SUBMODS_DIR}.")
        return 0

    mod_dir = resolve_mod_dir(argv)
    if mod_dir is None:
        return 1
    if not os.path.isdir(mod_dir):
        try:
            os.makedirs(mod_dir)
            print(f"Created mod folder: {mod_dir}")
        except Exception as e:
            print(f"Error: could not create mod folder {mod_dir}: {e}")
            return 1

    folders = sorted(
        e for e in os.listdir(SUBMODS_DIR)
        if os.path.isdir(os.path.join(SUBMODS_DIR, e))
    )
    if not folders:
        print("No submod folders found.")
        return 0

    print(f"Mod folder : {mod_dir}")
    print(f"Repo       : {ROOT_DIR}")
    print()

    errors = 0
    valid_names = set()

    # When the repo lives outside the mod folder, the main mod needs a link too.
    repo_is_inside_mod_dir = normalize_path(os.path.dirname(ROOT_DIR)) == normalize_path(mod_dir)
    link_dirs = [(ROOT_DIR, None)] if not repo_is_inside_mod_dir else []
    link_dirs += [(os.path.join(SUBMODS_DIR, f), f) for f in folders]

    for source_dir, folder in link_dirs:
        mod_name = load_submod_name(source_dir)
        if mod_name is None:
            errors += 1
            continue

        valid_names.add(mod_name)
        link_path = os.path.join(mod_dir, mod_name)
        where = f"submods/{folder}" if folder else "main mod"
        print(f"  {mod_name}  ({where})")
        if create_junction(link_path, source_dir):
            print(f"    {link_path}")
        else:
            errors += 1

    # Only prune once every submod name resolved cleanly, so a transient read
    # error can't make us delete a still-valid link.
    print()
    if errors:
        print(f"Skipping stale-junction prune ({errors} name error(s) above).")
    else:
        pruned = prune_stale_junctions(mod_dir, valid_names)
        print(f"Pruned {pruned} stale junction(s).")

    print()
    if errors:
        print(f"Done — {errors} error(s).")
        return 1
    print("Done — all junctions in place.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
