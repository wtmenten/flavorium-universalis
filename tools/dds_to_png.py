#!/usr/bin/env python3
"""
dds_to_png.py - Decode EU5 DDS art back to PNG, for looking at it.

The inverse of make_dds.py, and deliberately much smaller: this is a viewing and
reference tool, not part of the art pipeline. Nothing it writes should be checked
in or fed back into make_dds.py as a source, because a DDS has already been through
BC block compression and re-encoding a decoded one compounds the loss.

Pillow decodes BC1/BC3 (DXT1/DXT5) DDS directly, which covers every file the mod
and the base game ship in gfx/interface. Files it cannot decode are reported and
skipped rather than aborting a batch.

Usage:
    # One file, next to a chosen output
    python tools/dds_to_png.py icon.dds -o ~/Desktop/icon.png

    # Any number of files or globs into one folder
    python tools/dds_to_png.py main_menu/gfx/interface/icons/traits/*.dds -d out/

    # A whole tree
    python tools/dds_to_png.py main_menu/gfx -r -d out/

    # Vanilla art, for comparison
    python tools/dds_to_png.py "$EU5/game/main_menu/gfx/interface/icons/traits" -r -d out/

    # Icons are transparent; put them on something to actually see them
    python tools/dds_to_png.py trait.dds -d out/ --background "#1b1b1b"
    python tools/dds_to_png.py trait.dds -d out/ --background checker

    # What the engine streams at distance, rather than the full surface
    python tools/dds_to_png.py bg.dds -d out/ --mip 3

    # Read the headers without writing anything
    python tools/dds_to_png.py main_menu/gfx -r --info

Requires Pillow (pip install pillow).
"""

import argparse
import glob
import os
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("dds_to_png.py needs Pillow. Install it with: pip install pillow")

# read_dds_info and the path helpers already exist next door. make_dds.py defines
# only constants and functions at module level, so importing it is free.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_dds import read_dds_info, mod_root, display_path, mip_count  # noqa: E402

DEFAULT_OUT = os.path.join("tools", "dds_preview")


# --------------------------------------------------------------------------
# Input collection
# --------------------------------------------------------------------------

def collect(inputs, recursive):
    """Expand files, globs and directories into a de-duplicated list of DDS paths."""
    found = []
    for item in inputs:
        if os.path.isdir(item):
            pattern = os.path.join(item, "**", "*.dds") if recursive else os.path.join(item, "*.dds")
            found += glob.glob(pattern, recursive=recursive)
        elif any(c in item for c in "*?["):
            found += [p for p in glob.glob(item, recursive=recursive)
                      if p.lower().endswith(".dds")]
        else:
            found.append(item)

    seen, out = set(), []
    for p in found:
        key = os.path.normcase(os.path.abspath(p))
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


def mirror_dir(src):
    """The sub-path under the output dir that mirrors this source's location.

    Mod files keep their full mod-relative folder. Files from anywhere else, which
    in practice means the game install on another drive, keep only the last two
    folders: enough to tell icons/traits from icons/situations without rebuilding
    an absolute path (and without a drive letter, which cannot be joined onto an
    output dir anyway).
    """
    root = mod_root()
    full = os.path.abspath(src)
    try:
        if os.path.commonpath([full, root]) == root:
            return os.path.dirname(os.path.relpath(full, root))
    except ValueError:
        pass                                    # different drive; fall through
    parts = os.path.dirname(full).replace("\\", "/").split("/")
    return os.path.join(*parts[-2:]) if len(parts) >= 2 else ""


def output_path(src, out_dir, flatten_tree, mip):
    """Where one source file's PNG goes.

    Mirrors the source tree under out_dir by default, because a flat dump of a
    recursive run collides the moment two folders both hold e.g. default.dds.
    """
    stem = os.path.splitext(os.path.basename(src))[0]
    if mip:
        stem += ".mip%d" % mip
    if flatten_tree:
        return os.path.join(out_dir, stem + ".png")
    return os.path.join(out_dir, mirror_dir(src), stem + ".png")


# --------------------------------------------------------------------------
# Backgrounds
#
# Almost everything in icons/ is transparent, and a transparent PNG opened over a
# white viewer and a dark viewer looks like two different pieces of art. These put
# something known behind it.
# --------------------------------------------------------------------------

def parse_background(spec):
    """None, the string "checker", or an RGB tuple."""
    if spec is None:
        return None
    if spec.lower() == "checker":
        return "checker"
    try:
        rgb = Image.new("RGB", (1, 1), spec).getpixel((0, 0))
    except ValueError:
        raise SystemExit("dds_to_png.py: unrecognised colour %r. Use a name like 'black', "
                         "'#1b1b1b', or the word 'checker'." % spec)
    return rgb


def checkerboard(size, square=8, light=(90, 90, 90), dark=(60, 60, 60)):
    im = Image.new("RGB", size, light)
    d = ImageDraw.Draw(im)
    for y in range(0, size[1], square):
        for x in range(0, size[0], square):
            if (x // square + y // square) % 2:
                d.rectangle([x, y, x + square - 1, y + square - 1], fill=dark)
    return im


def apply_background(im, background):
    if background is None:
        return im
    im = im.convert("RGBA")
    base = checkerboard(im.size) if background == "checker" else Image.new("RGB", im.size, background)
    base = base.convert("RGBA")
    return Image.alpha_composite(base, im).convert("RGB")


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_info(paths):
    print("%-9s %-14s %-5s %s" % ("SIZE", "FORMAT", "MIPS", "FILE"))
    bad = 0
    for p in paths:
        info = read_dds_info(p)
        if info is None:
            print("%-9s %-14s %-5s %s" % ("-", "unreadable", "-", display_path(p)))
            bad += 1
            continue
        w, h, fmt, mips = info
        expected = mip_count(w, h)
        flag = "" if mips == expected else "  (expected %d)" % expected
        print("%-9s %-14s %-5s %s%s" % ("%dx%d" % (w, h), fmt, mips, display_path(p), flag))
    return 1 if bad else 0


def cmd_convert(paths, args):
    background = parse_background(args.background)
    written = skipped = failed = 0

    for src in paths:
        if args.out:
            dst = args.out
        else:
            dst = output_path(src, args.out_dir, args.flat, args.mip)

        if os.path.exists(dst) and not args.overwrite:
            print("skip   %s (exists; --overwrite to replace)" % display_path(dst))
            skipped += 1
            continue

        try:
            im = Image.open(src)
            if args.mip:
                # Pillow exposes mip levels through the standard resolution API.
                # Not every plugin build supports it, so fall back to a plain resize
                # of the base surface rather than failing the file.
                try:
                    im.size = (max(1, im.size[0] >> args.mip), max(1, im.size[1] >> args.mip))
                    im.load()
                except (AttributeError, ValueError, OSError):
                    im = Image.open(src)
                    im.load()
                    im = im.resize((max(1, im.size[0] >> args.mip),
                                    max(1, im.size[1] >> args.mip)), Image.LANCZOS)
            else:
                im.load()
        except Exception as exc:                       # noqa: BLE001 - report and continue
            print("FAIL   %s (%s: %s)" % (display_path(src), type(exc).__name__, exc))
            failed += 1
            continue

        if args.scale and args.scale != 1:
            im = im.resize((max(1, int(im.width * args.scale)),
                            max(1, int(im.height * args.scale))), Image.NEAREST)

        im = apply_background(im, background)

        if args.dry_run:
            print("would   %-9s -> %s" % ("%dx%d" % im.size, display_path(dst)))
            written += 1
            continue

        os.makedirs(os.path.dirname(os.path.abspath(dst)) or ".", exist_ok=True)
        im.save(dst, format="PNG")
        print("wrote  %-9s -> %s" % ("%dx%d" % im.size, display_path(dst)))
        written += 1

    parts = ["%d %s" % (written, "would be written" if args.dry_run else "written")]
    if skipped:
        parts.append("%d skipped" % skipped)
    if failed:
        parts.append("%d failed" % failed)
    print("\n" + ", ".join(parts) + ".")
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(
        description="Decode EU5 DDS art to PNG for reference.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Output is for looking at. Do not feed it back into make_dds.py as a source:\n"
               "a DDS has already been through BC compression and round-tripping compounds it.",
    )
    ap.add_argument("inputs", nargs="+", help="DDS files, glob patterns, or directories")
    ap.add_argument("-o", "--out", metavar="FILE",
                    help="explicit output file; only meaningful for a single input")
    ap.add_argument("-d", "--out-dir", metavar="DIR", default=DEFAULT_OUT,
                    help="output directory (default: %s)" % DEFAULT_OUT)
    ap.add_argument("-r", "--recursive", action="store_true",
                    help="descend into directories given as inputs")
    ap.add_argument("--flat", action="store_true",
                    help="write every PNG straight into the output dir instead of "
                         "mirroring the source tree (collides on same-named files)")
    ap.add_argument("--background", metavar="COLOUR",
                    help="composite transparency onto a colour ('black', '#1b1b1b') "
                         "or onto 'checker'")
    ap.add_argument("--mip", type=int, metavar="N",
                    help="extract mip level N instead of the base surface")
    ap.add_argument("--scale", type=float, metavar="F",
                    help="scale the output by F with nearest-neighbour, for inspecting icons")
    ap.add_argument("--overwrite", action="store_true", help="replace existing PNGs")
    ap.add_argument("--dry-run", action="store_true", help="report what would be written")
    ap.add_argument("--info", action="store_true",
                    help="print size, format and mip count for each input; write nothing")
    args = ap.parse_args()

    paths = collect(args.inputs, args.recursive)
    if not paths:
        print("No .dds files matched. Pass -r if you meant to descend into a directory.")
        return 1

    if args.info:
        return cmd_info(paths)

    if args.out and len(paths) > 1:
        print("--out names a single file but %d inputs matched. Use --out-dir instead."
              % len(paths))
        return 1

    return cmd_convert(paths, args)


if __name__ == "__main__":
    sys.exit(main())
