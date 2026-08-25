#!/usr/bin/env python3
"""
make_dds.py - Convert PNG source art into EU5-ready DDS with a full mipmap chain.

EU5 reads BC1 (DXT1) and BC3 (DXT5) DDS files and expects a complete mipmap chain
down to 1x1. A file without mips still renders, but the engine logs
"Streamed texture has no mipmaps" and streams the full-resolution surface every
frame. Pillow can encode BC blocks but writes a single surface, so this tool builds
the chain and the header itself. Output is byte-compatible with vanilla headers
(flags 0xA1007, depth 1, caps 0x401008).

Downsampling is done in linear light with premultiplied alpha, so icons do not pick
up dark halos around soft edges and backgrounds do not lose midtone contrast.

Usage:
    # Convert to a named art slot and drop it in the right mod folder
    python tools/make_dds.py hero.png --slot trait --key war_hawk
    python tools/make_dds.py bg.png --slot situation-bg --key cc_cabinet_court

    # Same, but into a submod
    python tools/make_dds.py x.png --slot situation-icon --key cc_byz_the_west --submod rhomania

    # Batch: every PNG in a folder, filename stem becomes the key
    python tools/make_dds.py art/traits/*.png --slot trait

    # Convert without placing it in the mod
    python tools/make_dds.py in.png --slot trait -o out.dds
    python tools/make_dds.py in.png --size 1080x440 --format BC1 -o out.dds

    # Reference and auditing
    python tools/make_dds.py --list-slots
    python tools/make_dds.py --verify              # check every DDS in the mod
    python tools/make_dds.py --verify --fix-mips   # re-encode any that are wrong

Requires Pillow (pip install pillow). numpy is used when present for a faster and
slightly more accurate resize, but is not required.
"""

import argparse
import glob
import io
import os
import struct
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("make_dds.py needs Pillow. Install it with: pip install pillow")

try:
    import numpy as np
except ImportError:
    np = None


# --------------------------------------------------------------------------
# Slot table. Sizes and formats are measured from vanilla assets; see
# docs/art-asset-gaps.md for how each path is resolved by the engine.
# fit defaults to "contain" for icons (pad rather than crop a logo) and
# "cover" for wide art (fill the frame, crop the overhang).
# --------------------------------------------------------------------------

SLOTS = {
    # key:                (w,    h,   fourcc, subdir under gfx/interface,                          fit)
    "trait":              (128,  128, "DXT5", "icons/traits",                                      "contain"),
    "situation-icon":     (128,  128, "DXT5", "icons/situations",                                  "contain"),
    "situation-bg":       (1080, 440, "DXT1", "illustrations/situation",                           "cover"),
    "societal-icon":      (128,  128, "DXT5", "icons/societal_values",                             "contain"),
    "societal-art":       (674,  134, "DXT1", "illustrations/societal_values",                     "cover"),
    "subject-type":       (128,  128, "DXT5", "icons/subject_types",                               "contain"),
    "bureaucracy":        (128,  128, "DXT5", "icons/bureaucracy",                                 "contain"),
    "law":                (128,  128, "DXT5", "icons/laws",                                        "contain"),
    "cabinet-action":     (128,  128, "DXT5", "icons/cabinet_actions",                             "contain"),
    "character-action":   (128,  128, "DXT5", "icons/character_interactions",                      "contain"),
    "generic-action":     (128,  128, "DXT5", "icons/generic_actions",                             "contain"),
    "casus-belli":        (128,  128, "DXT5", "icons/casus_belli",                                 "contain"),
    "io-icon":            (128,  128, "DXT5", "icons/international_organizations",                 "contain"),
    "io-status":          (128,  128, "DXT5", "icons/international_organizations/special_statuses", "contain"),
    "io-bg":              (1080, 440, "DXT1", "illustrations/international_organization_types",    "cover"),
    "parliament-type":    (128,  128, "DXT5", "icons/parliament_types",                            "contain"),
    "privilege":          (64,   90,  "DXT1", "icons/privileges",                                  "cover"),
    "gov-reform":         (64,   90,  "DXT1", "icons/government_reforms/illustrations",            "cover"),
    "advance":            (256,  256, "DXT5", "advance",                                           "contain"),
    "mission-task":       (256,  256, "DXT5", "advance",                                           "contain"),
    "modifier":           (64,   64,  "DXT5", "icons/modifier_types",                              "contain"),
    "mission-banner":     (1932, 264, "DXT1", "illustrations/missions",                            "cover"),
    "event-bg":           (1080, 440, "DXT1", "illustrations/event/backgrounds/special",           "cover"),
}

FORMAT_ALIASES = {
    "BC1": "DXT1", "DXT1": "DXT1",
    "BC3": "DXT5", "DXT5": "DXT5",
}

BLOCK_BYTES = {"DXT1": 8, "DXT5": 16}
MODE_FOR = {"DXT1": "RGB", "DXT5": "RGBA"}


# --------------------------------------------------------------------------
# DDS container
# --------------------------------------------------------------------------

def mip_count(width, height):
    """Number of mip levels down to 1x1, matching every vanilla asset measured."""
    n, d = 1, max(width, height)
    while d > 1:
        d //= 2
        n += 1
    return n


def mip_size(width, height, level):
    return max(1, width >> level), max(1, height >> level)


def surface_bytes(width, height, fourcc):
    blocks = ((width + 3) // 4) * ((height + 3) // 4)
    return blocks * BLOCK_BYTES[fourcc]


def _dds_header(width, height, fourcc, mips):
    DDSD = 0x1 | 0x2 | 0x4 | 0x1000 | 0x20000 | 0x80000   # CAPS HEIGHT WIDTH PIXELFORMAT MIPMAPCOUNT LINEARSIZE
    CAPS = 0x1000 | 0x8 | 0x400000                        # TEXTURE COMPLEX MIPMAP
    h = bytearray()
    h += b"DDS "
    h += struct.pack("<7I", 124, DDSD, height, width,
                     surface_bytes(width, height, fourcc), 1, mips)
    h += b"\0" * 44                                       # dwReserved1[11]
    h += struct.pack("<2I", 32, 0x4)                      # pixelformat size, DDPF_FOURCC
    h += fourcc.encode("ascii")
    h += b"\0" * 20                                       # bitcount + 4 channel masks
    h += struct.pack("<4I", CAPS, 0, 0, 0)
    h += b"\0" * 4                                        # dwReserved2
    assert len(h) == 128, len(h)
    return bytes(h)


def _encode_surface(im, fourcc):
    """Return raw BC block data for one surface, via Pillow's bcn encoder."""
    im = im.convert(MODE_FOR[fourcc])
    buf = io.BytesIO()
    im.save(buf, format="DDS", pixel_format=fourcc)
    return buf.getvalue()[128:]


def write_dds(path, levels, fourcc):
    """levels: list of PIL images, largest first, each half the previous."""
    w, h = levels[0].size
    payload = b"".join(_encode_surface(im, fourcc) for im in levels)
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(_dds_header(w, h, fourcc, len(levels)))
        f.write(payload)
    return len(levels), len(payload) + 128


def read_dds_info(path):
    """(width, height, format, mipcount) or None if not a readable DDS."""
    try:
        with open(path, "rb") as f:
            d = f.read(148)
        if d[:4] != b"DDS ":
            return None
        height, width = struct.unpack("<2I", d[12:20])
        mips = struct.unpack("<I", d[28:32])[0]
        pf_flags = struct.unpack("<I", d[80:84])[0]
        fourcc = d[84:88]
        if fourcc == b"DX10":
            fmt = "DX10/dxgi%d" % struct.unpack("<I", d[128:132])[0]
        elif not pf_flags & 0x4:
            fmt = "uncompressed"
        else:
            fmt = fourcc.decode("ascii", "replace").rstrip("\0")
        return width, height, fmt, max(1, mips)
    except OSError:
        return None


# --------------------------------------------------------------------------
# Image processing
# --------------------------------------------------------------------------

def _srgb_to_linear(a):
    return np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)


def _linear_to_srgb(a):
    return np.where(a <= 0.0031308, a * 12.92, 1.055 * (a ** (1 / 2.4)) - 0.055)


def _resize_linear(im, size):
    """Downsample in linear light with premultiplied alpha.

    Without the linear step, halving a checkerboard of black and white in sRGB
    gives 0.5 (188 sRGB) instead of the correct 0.73. Without premultiplication,
    the RGB of fully transparent pixels bleeds into the edges of an icon and
    shows up as a dark fringe once the alpha is restored.
    """
    if np is None:
        return im.resize(size, Image.LANCZOS)

    has_alpha = im.mode == "RGBA"
    arr = np.asarray(im.convert("RGBA" if has_alpha else "RGB"), dtype=np.float32) / 255.0
    rgb = _srgb_to_linear(arr[..., :3])
    alpha = arr[..., 3:4] if has_alpha else None
    if has_alpha:
        rgb = rgb * alpha

    planes = [rgb[..., 0], rgb[..., 1], rgb[..., 2]]
    if has_alpha:
        planes.append(alpha[..., 0])
    out = [
        np.asarray(Image.fromarray(np.ascontiguousarray(p)).resize(size, Image.LANCZOS),
                   dtype=np.float32)
        for p in planes
    ]

    rgb_o = np.stack(out[:3], axis=-1)
    if has_alpha:
        a_o = np.clip(out[3], 0.0, 1.0)
        rgb_o = np.divide(rgb_o, a_o[..., None], out=np.zeros_like(rgb_o), where=a_o[..., None] > 1e-6)

    rgb_o = _linear_to_srgb(np.clip(rgb_o, 0.0, 1.0))
    chans = [rgb_o[..., 0], rgb_o[..., 1], rgb_o[..., 2]]
    if has_alpha:
        chans.append(a_o)
    res = np.clip(np.stack(chans, axis=-1) * 255.0 + 0.5, 0, 255).astype(np.uint8)
    return Image.fromarray(res)


def fit_to(im, width, height, mode, pad_rgb=(0, 0, 0)):
    """Resize im to exactly width x height using the given fit mode."""
    if im.size == (width, height):
        return im
    if mode == "stretch":
        return _resize_linear(im, (width, height))
    if mode == "none":
        raise ValueError(
            "source is %dx%d but the slot needs %dx%d; pass --fit cover/contain/stretch"
            % (im.width, im.height, width, height)
        )

    sw, sh = im.size
    scale = max(width / sw, height / sh) if mode == "cover" else min(width / sw, height / sh)
    nw, nh = max(1, round(sw * scale)), max(1, round(sh * scale))
    im = _resize_linear(im, (nw, nh))

    if mode == "cover":
        left, top = (nw - width) // 2, (nh - height) // 2
        return im.crop((left, top, left + width, top + height))

    has_alpha = im.mode == "RGBA"
    bg = Image.new("RGBA" if has_alpha else "RGB",
                   (width, height),
                   (0, 0, 0, 0) if has_alpha else pad_rgb)
    bg.paste(im, ((width - nw) // 2, (height - nh) // 2))
    return bg


def build_levels(im, width, height, fourcc, fit, mips=True):
    top = fit_to(im, width, height, fit)
    top = top.convert(MODE_FOR[fourcc])
    if not mips:
        return [top]
    levels = [top]
    for lvl in range(1, mip_count(width, height)):
        levels.append(_resize_linear(top, mip_size(width, height, lvl)))
    return levels


# --------------------------------------------------------------------------
# Mod paths
# --------------------------------------------------------------------------

def mod_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def display_path(path):
    """Mod-relative when the file lives in the mod, absolute otherwise.

    commonpath raises ValueError when the two paths are on different Windows
    drives, which is the normal case here: the mod sits on C: and the game
    install on F:. Catching it is what lets these tools be pointed at vanilla art.
    """
    root = mod_root()
    full = os.path.abspath(path)
    try:
        if os.path.commonpath([full, root]) == root:
            return os.path.relpath(full, root).replace("\\", "/")
    except ValueError:
        pass
    return full.replace("\\", "/")


def slot_output_path(slot, key, submod=None):
    root = mod_root()
    if submod:
        root = os.path.join(root, "submods", submod)
    return os.path.join(root, "main_menu", "gfx", "interface", SLOTS[slot][3], key + ".dds")


def slot_for_path(path):
    """Reverse-map a DDS path back to its slot, for --verify."""
    norm = path.replace("\\", "/")
    marker = "/main_menu/gfx/interface/"
    if marker not in norm:
        return None
    rel = os.path.dirname(norm.split(marker, 1)[1])
    best = None
    for name, spec in SLOTS.items():
        if spec[3] == rel and (best is None or name < best):
            best = name
    return best


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_list_slots():
    print("%-18s %-10s %-6s %-8s %s" % ("SLOT", "SIZE", "FMT", "FIT", "PATH under main_menu/gfx/interface/"))
    for name in sorted(SLOTS):
        w, h, fourcc, sub, fit = SLOTS[name]
        label = "BC1" if fourcc == "DXT1" else "BC3"
        print("%-18s %-10s %-6s %-8s %s/<key>.dds" % (name, "%dx%d" % (w, h), label, fit, sub))
    print("\nMip levels are always the full chain to 1x1 (%s)." % "e.g. 128x128 -> 8 levels")


def cmd_convert(args):
    sources = []
    for pattern in args.inputs:
        hits = glob.glob(pattern)
        if not hits:
            print("  skip: no file matches %s" % pattern, file=sys.stderr)
            continue
        sources.extend(sorted(hits))
    if not sources:
        sys.exit("no input files matched")

    if not args.out and not args.slot:
        sys.exit("pass --out to write one file, or --slot to place files in the mod")
    if args.out and len(sources) > 1:
        sys.exit("--out takes a single input; use --slot for batch output")
    if args.key and len(sources) > 1:
        sys.exit("--key takes a single input; batch runs use each filename as the key")

    if args.slot:
        w, h, fourcc, _sub, fit = SLOTS[args.slot]
    else:
        if not args.size or not args.format:
            sys.exit("without --slot you must pass both --size WxH and --format BC1|BC3")
        fit = "cover"
    if args.size:
        try:
            w, h = (int(v) for v in args.size.lower().split("x"))
        except ValueError:
            sys.exit("--size must look like 1080x440")
    if args.format:
        fourcc = FORMAT_ALIASES[args.format.upper()]
    if args.fit:
        fit = args.fit

    failures = 0
    for src in sources:
        key = args.key or os.path.splitext(os.path.basename(src))[0]
        dest = args.out or slot_output_path(args.slot, key, args.submod)
        try:
            im = Image.open(src)
            im.load()
        except Exception as exc:
            print("  FAIL %s: %s" % (src, exc), file=sys.stderr)
            failures += 1
            continue

        if fourcc == "DXT1" and im.mode in ("RGBA", "LA", "P"):
            if im.convert("RGBA").getchannel("A").getextrema()[0] < 255:
                print("  note: %s has transparency but the target is BC1; alpha will be discarded"
                      % os.path.basename(src))

        try:
            levels = build_levels(im, w, h, fourcc, fit, mips=not args.no_mips)
        except ValueError as exc:
            print("  FAIL %s: %s" % (os.path.basename(src), exc), file=sys.stderr)
            failures += 1
            continue
        if args.dry_run:
            total = sum(surface_bytes(*lv.size, fourcc) for lv in levels) + 128
            print("  would write %s  %dx%d %s mips=%d %.1f KB"
                  % (display_path(dest), w, h, fourcc, len(levels), total / 1024))
            continue

        n, size = write_dds(dest, levels, fourcc)
        print("  %-62s %dx%d %s mips=%d %.1f KB" % (display_path(dest), w, h, fourcc, n, size / 1024))

    return 1 if failures else 0


def cmd_verify(args):
    root = mod_root()
    roots = [root] + [
        os.path.join(root, "submods", d)
        for d in sorted(os.listdir(os.path.join(root, "submods")))
        if os.path.isdir(os.path.join(root, "submods", d))
    ] if os.path.isdir(os.path.join(root, "submods")) else [root]

    checked = problems = fixed = 0
    for r in roots:
        base = os.path.join(r, "main_menu", "gfx", "interface")
        for dirpath, _dirs, files in os.walk(base):
            for fn in sorted(files):
                if not fn.lower().endswith(".dds"):
                    continue
                path = os.path.join(dirpath, fn)
                info = read_dds_info(path)
                rel = os.path.relpath(path, root).replace("\\", "/")
                if info is None:
                    print("  BAD HEADER  %s" % rel)
                    problems += 1
                    continue
                checked += 1
                width, height, fmt, mips = info
                slot = slot_for_path(path)
                issues = []
                expected_mips = mip_count(width, height)
                if mips < expected_mips:
                    issues.append("mips=%d, expected %d" % (mips, expected_mips))
                if slot:
                    sw, sh, sfmt, _sub, _fit = SLOTS[slot]
                    if (width, height) != (sw, sh):
                        issues.append("%dx%d, slot '%s' wants %dx%d" % (width, height, slot, sw, sh))
                if not issues:
                    continue
                problems += 1
                print("  %-58s %s" % (rel, "; ".join(issues)))
                if args.fix_mips and mips < expected_mips and fmt in BLOCK_BYTES:
                    try:
                        im = Image.open(path)
                        im.load()
                    except Exception as exc:
                        print("      cannot re-encode: %s" % exc)
                        continue
                    tw, th, tfmt = (SLOTS[slot][0], SLOTS[slot][1], SLOTS[slot][2]) if slot else (width, height, fmt)
                    fit = SLOTS[slot][4] if slot else "cover"
                    levels = build_levels(im, tw, th, tfmt, fit)
                    n, size = write_dds(path, levels, tfmt)
                    print("      rewritten: %dx%d %s mips=%d %.1f KB" % (tw, th, tfmt, n, size / 1024))
                    fixed += 1

    print("\n%d files checked, %d with problems%s"
          % (checked, problems, ", %d rewritten" % fixed if args.fix_mips else ""))
    return 1 if problems and not args.fix_mips else 0


def main():
    ap = argparse.ArgumentParser(
        description="Convert PNG art into EU5-ready DDS with a full mipmap chain.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Run --list-slots for the slot table, or see docs/art-asset-gaps.md.",
    )
    ap.add_argument("inputs", nargs="*", help="source PNG files or glob patterns")
    ap.add_argument("--slot", choices=sorted(SLOTS),
                    help="art slot; sets size, format, fit and output folder")
    ap.add_argument("--key", help="entry key for the output filename (default: input filename)")
    ap.add_argument("--submod", help="write into submods/<name>/ instead of the main mod")
    ap.add_argument("-o", "--out", help="explicit output path; skips mod placement")
    ap.add_argument("--size", help="override size, e.g. 1080x440")
    ap.add_argument("--format", choices=["BC1", "BC3", "DXT1", "DXT5"], help="override compression")
    ap.add_argument("--fit", choices=["cover", "contain", "stretch", "none"],
                    help="how to reconcile source aspect with target")
    ap.add_argument("--no-mips", action="store_true",
                    help="write a single surface (the engine will log a warning)")
    ap.add_argument("--dry-run", action="store_true", help="report what would be written")
    ap.add_argument("--list-slots", action="store_true", help="print the slot table and exit")
    ap.add_argument("--verify", action="store_true",
                    help="check every DDS in the mod against its slot spec")
    ap.add_argument("--fix-mips", action="store_true",
                    help="with --verify, re-encode files that are missing mip levels")
    args = ap.parse_args()

    if args.list_slots:
        cmd_list_slots()
        return 0
    if args.verify:
        return cmd_verify(args)
    if not args.inputs:
        ap.print_help()
        return 0
    return cmd_convert(args)


if __name__ == "__main__":
    sys.exit(main())
