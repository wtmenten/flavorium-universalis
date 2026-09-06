"""
Locate the installed EU5 game files.

Every tool that reads vanilla script should get its path from here rather than
hardcoding one, so the repo works on any workstation without edits.

    from game_paths import game_root
    GAME_ROOT = game_root()          # .../Europa Universalis V/game

Resolution order:
    1. the EU5_GAME_DIR environment variable
    2. every Steam library in steamapps/libraryfolders.vdf, with Steam's own
       location taken from the registry
    3. a short list of common install paths

Only directories that actually exist are returned. Steam keeps libraries on
removable/absent drives listed in libraryfolders.vdf indefinitely, so a
registered path is not evidence the files are there.
"""

import os
import re

APP_SUBPATH = os.path.join("steamapps", "common", "Europa Universalis V")

FALLBACK_STEAM_DIRS = [
    r"C:\Program Files (x86)\Steam",
    r"C:\Program Files\Steam",
    r"F:\SteamLibrary",
    r"E:\SteamLibrary",
    r"G:\SteamLibrary",
    r"H:\SteamLibrary",
    r"D:\SteamLibrary",
]


def _steam_install_dir():
    """Steam's own install directory, from the registry when available."""
    try:
        import winreg

        for hive, key_path, value in (
            (winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam", "SteamPath"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam", "InstallPath"),
        ):
            try:
                with winreg.OpenKey(hive, key_path) as key:
                    path, _ = winreg.QueryValueEx(key, value)
                if path:
                    return os.path.normpath(path)
            except OSError:
                continue
    except ImportError:
        pass
    return None


def _library_dirs():
    """Every Steam library root listed in libraryfolders.vdf, plus fallbacks."""
    roots = []
    steam_dir = _steam_install_dir()
    if steam_dir:
        roots.append(steam_dir)
    roots.extend(FALLBACK_STEAM_DIRS)

    libraries = []
    seen = set()

    def add(path):
        key = os.path.normcase(os.path.normpath(path))
        if key not in seen:
            seen.add(key)
            libraries.append(path)

    for root in roots:
        add(root)
        vdf = os.path.join(root, "steamapps", "libraryfolders.vdf")
        try:
            with open(vdf, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        # Lines look like:  "path"   "C:\\Program Files (x86)\\Steam"
        for raw in re.findall(r'"path"\s*"([^"]+)"', text):
            add(raw.replace("\\\\", "\\"))

    return libraries


def find_game_dir():
    """The 'Europa Universalis V' install folder, or None if not found."""
    env = os.environ.get("EU5_GAME_DIR")
    if env:
        env = os.path.abspath(env)
        # Accept either the install folder or the game/ folder inside it.
        if os.path.basename(env).lower() == "game":
            env = os.path.dirname(env)
        if os.path.isdir(env):
            return env

    for library in _library_dirs():
        candidate = os.path.join(library, APP_SUBPATH)
        if os.path.isdir(os.path.join(candidate, "game")):
            return candidate

    return None


def game_root(required=True):
    """The game/ folder holding vanilla script (in_game/, main_menu/, ...)."""
    install = find_game_dir()
    if install is None:
        if required:
            raise FileNotFoundError(
                "Could not locate the Europa Universalis V install. "
                "Set the EU5_GAME_DIR environment variable to the game folder, "
                "e.g. EU5_GAME_DIR=\"D:/Steam/steamapps/common/Europa Universalis V\"."
            )
        return None
    return os.path.join(install, "game")


if __name__ == "__main__":
    install = find_game_dir()
    if install is None:
        print("EU5 install: NOT FOUND")
        print("Libraries searched:")
        for library in _library_dirs():
            print(f"  {library}")
        raise SystemExit(1)
    print(f"EU5 install : {install}")
    print(f"Game root   : {game_root()}")
