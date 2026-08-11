"""
Release script for Flavorium Universalis.

Translates localization/workshop text via translate.py and builds/uploads the mod
to Steam Workshop via upload.py.

Usage:
    python tools/release.py                    # upload mod content (default)
    python tools/release.py -wp                # upload workshop pages only
    python tools/release.py -m -wp             # upload mod + workshop pages
    python tools/release.py -d                 # upload dev item
    python tools/release.py -cn                # upload change notes

    python tools/release.py -t                 # translate, then upload
    python tools/release.py -t --translate-only    # translate, skip the upload
    python tools/release.py -t -l french,german    # limit translation languages

Translation flags (-t/--translate, -l/--languages, --translate-only) are consumed
here; every other argument is passed straight through to upload.py.
"""

import argparse
import json
import os
import subprocess
import sys

MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METADATA_PATH = os.path.join(MOD_ROOT, ".metadata", "metadata.json")
UPLOAD_SCRIPT = os.path.join(MOD_ROOT, "tools", "upload.py")
TRANSLATE_SCRIPT = os.path.join(MOD_ROOT, "tools", "translate.py")


def read_version():
    with open(METADATA_PATH, encoding="utf-8-sig") as f:
        meta = json.load(f)
    return meta.get("version", "unknown"), meta.get("name", "unknown")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Translate and/or upload the mod to Steam Workshop.",
        add_help=False,
    )
    parser.add_argument(
        "-t", "--translate",
        action="store_true",
        help="Run tools/translate.py before uploading.",
    )
    parser.add_argument(
        "-l", "--languages",
        metavar="LANGS",
        help="Comma-separated target languages for translation (default: all supported).",
    )
    parser.add_argument(
        "--translate-only",
        action="store_true",
        help="Run translation and stop; do not build or upload. Implies --translate.",
    )
    parser.add_argument(
        "-h", "--help",
        action="store_true",
        help="Show this help message and exit.",
    )
    # Everything else belongs to upload.py / translate.py.
    known, passthrough = parser.parse_known_args()
    if known.help:
        parser.print_help()
        print("\nAll other flags are forwarded to upload.py (-m, -wp, -s, -S, -cn, -d).")
        sys.exit(0)
    return known, passthrough


def build_translate_args(known, passthrough):
    """Map release flags onto translate.py's target flags.

    Translation targets mirror the upload targets so ``-t -wp`` translates the workshop
    pages it is about to upload. With no target flags, translate.py falls back to its
    own config defaults (mod localization).
    """
    args = []
    for flag, translate_flag in (
        ("-m", "-m"), ("--mod", "-m"),
        ("-wp", "-wp"), ("--workshop-pages", "-wp"),
        ("-s", "-s"), ("--submods", "-s"),
        ("-cn", "-cn"), ("--change-notes", "-cn"),
    ):
        if flag in passthrough and translate_flag not in args:
            args.append(translate_flag)
    if known.languages:
        args += ["-l", known.languages]
    return args


def main():
    known, passthrough = parse_args()
    do_translate = known.translate or known.translate_only

    version, name = read_version()

    print(f"\n=== {name} — Release {version} ===")
    if do_translate:
        langs = known.languages or "all supported languages"
        print(f"Translation: enabled ({langs})")
    print()

    if do_translate:
        translate_args = build_translate_args(known, passthrough)
        answer = input("Run translation now? [y/N] ").strip().lower()
        if answer != "y":
            print("Aborted.")
            sys.exit(0)
        print()
        result = subprocess.run([sys.executable, TRANSLATE_SCRIPT] + translate_args)
        if result.returncode != 0:
            print("\nTranslation failed; not uploading.")
            sys.exit(result.returncode)

    if known.translate_only:
        print("\nTranslation complete. Skipping upload (--translate-only).")
        sys.exit(0)

    print()
    answer = input("Build and upload to Steam Workshop? [y/N] ").strip().lower()
    if answer != "y":
        print("Aborted.")
        sys.exit(0)

    print()
    result = subprocess.run([sys.executable, UPLOAD_SCRIPT] + passthrough)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
