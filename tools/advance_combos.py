#!/usr/bin/env python3
"""
advance_combos.py - parse all EU5 advances and enumerate every full-game branch combo.

A "combination" is one branch choice (adm/dip/mil) per age, across ALL ages at once.
With 6 ages and 3 branches each that is up to 3^6 = 729 combinations.

Usage:
    python tools/advance_combos.py [--only-unlocks] [--mod-only] [--combo FILTER]
    python tools/advance_combos.py --json [OUTPUT.js]

    --only-unlocks      skip plain stat modifiers, show only unlock_* effects
    --mod-only          only print combos that include at least one mod advance
    --combo FILTER      substring filter on combo label, e.g. "ADM,DIP,MIL,ADM,DIP,MIL"
    --json [FILE]       generate JS data file for advance_explorer.html
                        (default: tools/advance_data.js)
                        Open tools/advance_explorer.html in a browser to explore.
"""

import re
import sys
import json
import argparse
from pathlib import Path
from itertools import product
from collections import defaultdict

# -- paths -------------------------------------------------------------------
MOD_ADVANCES_DIR  = Path(r"C:\Users\wtmen\OneDrive\Documents\Paradox Interactive\Europa Universalis V\mod\cabinets-and-choices\in_game\common\advances")
GAME_ADVANCES_DIR = Path(r"F:\SteamLibrary\steamapps\common\Europa Universalis V\game\in_game\common\advances")

BRANCHES = ("adm", "dip", "mil")

AGE_ORDER = [
    "age_1_traditions",
    "age_2_renaissance",
    "age_3_discovery",
    "age_4_reformation",
    "age_5_absolutism",
    "age_6_revolutions",
]

AGE_LABELS = {
    "age_1_traditions":   "Age of Traditions",
    "age_2_renaissance":  "Age of Renaissance",
    "age_3_discovery":    "Age of Discovery",
    "age_4_reformation":  "Age of Reformation",
    "age_5_absolutism":   "Age of Absolutism",
    "age_6_revolutions":  "Age of Revolutions",
}

# Keys that belong to the advance definition itself, not counted as effects
SKIP_KEYS = {
    "age", "icon", "requires", "for", "depth", "ai_weight",
    "potential", "allow", "ai_preference_tags", "research_cost",
    "starting_technology_level", "allow_children", "has_cultural_maintenance",
}

# -- parser ------------------------------------------------------------------

def parse_advances_from_file(path: Path, is_mod: bool) -> list[dict]:
    """Lightweight Clausewitz parser. Returns advance dicts with _effects list."""
    try:
        text = path.read_text(encoding="utf-8-sig")
    except Exception:
        try:
            text = path.read_text(encoding="cp1252")
        except Exception:
            return []

    clean_lines = []
    for line in text.splitlines():
        idx = line.find("#")
        clean_lines.append(line[:idx] if idx >= 0 else line)
    text = "\n".join(clean_lines)

    token_re = re.compile(r'"[^"]*"|\{|\}|=|[^\s{}=]+')
    tokens = token_re.findall(text)

    advances = []
    i = 0
    n = len(tokens)

    def skip_block():
        nonlocal i
        depth = 1
        while i < n and depth:
            if tokens[i] == "{":
                depth += 1
            elif tokens[i] == "}":
                depth -= 1
            i += 1

    while i < n:
        if i + 2 < n and tokens[i + 1] == "=" and tokens[i + 2] == "{":
            adv_name = tokens[i]
            i += 3
            adv: dict = {
                "_name": adv_name,
                "_mod": is_mod,
                "_file": path.name,
            }
            depth = 1
            while i < n and depth:
                t = tokens[i]
                if t == "{":
                    depth += 1
                    i += 1
                elif t == "}":
                    depth -= 1
                    i += 1
                elif i + 1 < n and tokens[i + 1] == "=":
                    key = t
                    i += 2
                    if i < n and tokens[i] == "{":
                        i += 1
                        skip_block()
                    else:
                        val = tokens[i] if i < n else ""
                        i += 1
                        if key not in SKIP_KEYS:
                            adv.setdefault("_effects", []).append((key, val))
                        else:
                            adv[key] = val
                else:
                    i += 1
            if "age" in adv:
                advances.append(adv)
        else:
            i += 1

    return advances


def load_all_advances() -> tuple[list[dict], set[str]]:
    """Returns (all_advances, mod_advance_names)."""
    advances: list[dict] = []
    mod_names: set[str] = set()

    for path in sorted(GAME_ADVANCES_DIR.glob("*.txt")):
        advances.extend(parse_advances_from_file(path, is_mod=False))

    for path in sorted(MOD_ADVANCES_DIR.glob("*.txt")):
        new = parse_advances_from_file(path, is_mod=True)
        for a in new:
            mod_names.add(a["_name"])
        advances.extend(new)

    return advances, mod_names


# -- grouping ----------------------------------------------------------------

def group_advances(advances: list[dict]) -> dict:
    """Returns {age: {branch_or_empty: [advance, ...]}}."""
    groups: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for adv in advances:
        age    = adv.get("age", "unknown")
        branch = adv.get("for", "")
        groups[age][branch].append(adv)
    return groups


def sorted_ages(groups: dict) -> list[str]:
    known = [a for a in AGE_ORDER if a in groups]
    extra = sorted(a for a in groups if a not in AGE_ORDER)
    return known + extra


# -- helpers -----------------------------------------------------------------

def age_display(age: str) -> str:
    return AGE_LABELS.get(age, age.replace("age_", "").replace("_", " ").title())


def is_unlock(key: str) -> bool:
    return key.startswith("unlock_")


# -- combination enumeration -------------------------------------------------

def build_combos(groups: dict, target_ages: list[str]) -> list[dict]:
    """
    A combo is ONE branch choice per age, across ALL target_ages simultaneously.
    Returns list of {label, detail, per_age: [(age, branch, [advance])]}
    """
    per_age_options: list[list[tuple]] = []
    for age in target_ages:
        age_groups = groups.get(age, {})
        opts = [(b, age_groups[b]) for b in BRANCHES if age_groups.get(b)]
        if not opts:
            opts = [("--", [])]
        per_age_options.append(opts)

    combos = []
    for chosen_tuple in product(*per_age_options):
        short_parts = []
        detail_parts = []
        for age, (branch, _) in zip(target_ages, chosen_tuple):
            short_parts.append(branch.upper())
            detail_parts.append(f"{age_display(age)}={branch.upper()}")

        combos.append({
            "label":   ", ".join(short_parts),
            "detail":  "  ->  ".join(detail_parts),
            "per_age": [
                (age, branch, adv_list)
                for age, (branch, adv_list) in zip(target_ages, chosen_tuple)
            ],
        })

    return combos


# -- CLI text rendering ------------------------------------------------------

def render_combos(
    combos: list[dict],
    groups: dict,
    mod_names: set[str],
    only_unlocks: bool,
    mod_only: bool,
    combo_filter: str | None,
) -> None:

    def should_show(key: str) -> bool:
        return is_unlock(key) if only_unlocks else True

    def mod_tag(name: str) -> str:
        return " [MOD]" if name in mod_names else ""

    SEP  = "=" * 80
    SEP2 = "-" * 80

    total = len(combos)
    shown = 0

    for combo in combos:
        label  = combo["label"]
        detail = combo["detail"]

        if combo_filter and combo_filter.upper() not in label.upper():
            continue

        per_age = combo["per_age"]

        if mod_only:
            if not any(
                adv["_name"] in mod_names
                for _, _, adv_list in per_age
                for adv in adv_list
            ):
                continue

        shown += 1

        print(f"\n{SEP}")
        print(f"  COMBO [{shown}]: {label}")
        print(f"  {detail}")
        print(SEP)

        all_unlocks:   list[tuple[str, str, str, str]] = []
        all_modifiers: list[tuple[str, str, str, str]] = []

        for age, branch, adv_list in per_age:
            age_disp = age_display(age)
            age_groups = groups.get(age, {})
            universal = age_groups.get("", [])

            print(f"\n  [{age_disp}]  branch: {branch.upper()}")
            print(f"  {'.' * 40}")

            univ_fx = [
                (adv, [(k, v) for k, v in adv.get("_effects", []) if should_show(k)])
                for adv in universal
            ]
            if any(fx for _, fx in univ_fx):
                print(f"    (universal)")
                for adv, fx in univ_fx:
                    if not fx:
                        continue
                    name = adv["_name"]
                    print(f"      {name}{mod_tag(name)}")
                    for k, v in fx:
                        print(f"        {k} = {v}")
                        if is_unlock(k):
                            all_unlocks.append((k, v, name, age_disp))
                        else:
                            all_modifiers.append((k, v, name, age_disp))

            if adv_list:
                print(f"    ({branch.upper()} branch)")
                for adv in adv_list:
                    name = adv["_name"]
                    fx = [(k, v) for k, v in adv.get("_effects", []) if should_show(k)]
                    if fx or not only_unlocks:
                        print(f"      {name}{mod_tag(name)}")
                    for k, v in fx:
                        print(f"        {k} = {v}")
                        if is_unlock(k):
                            all_unlocks.append((k, v, name, age_disp))
                        else:
                            all_modifiers.append((k, v, name, age_disp))

        print(f"\n{SEP2}")
        print(f"  SUMMARY: {label}")
        print(SEP2)

        if all_unlocks:
            print("  Unlocks (all ages):")
            by_age: dict[str, list] = defaultdict(list)
            for k, v, src, age_d in all_unlocks:
                by_age[age_d].append((k, v, src))
            for age_d, items in by_age.items():
                print(f"    [{age_d}]")
                for k, v, src in items:
                    print(f"      {k} = {v}  (from {src}{mod_tag(src)})")

        if all_modifiers and not only_unlocks:
            print("  Modifiers (all ages):")
            by_age = defaultdict(list)
            for k, v, src, age_d in all_modifiers:
                by_age[age_d].append((k, v, src))
            for age_d, items in by_age.items():
                print(f"    [{age_d}]")
                for k, v, src in items:
                    print(f"      {k} = {v}  (from {src}{mod_tag(src)})")

        if not all_unlocks and (only_unlocks or not all_modifiers):
            print("  (no effects to show)")

    print(f"\n{SEP}", file=sys.stderr)
    print(f"  Shown {shown} of {total} combinations.", file=sys.stderr)


# -- data file generation ----------------------------------------------------

def serialize_advance(adv: dict, mod_names: set[str]) -> dict:
    return {
        "name":    adv["_name"],
        "isMod":   adv["_name"] in mod_names,
        "effects": [[k, v] for k, v in adv.get("_effects", [])],
    }


def build_data(groups: dict, mod_names: set[str], target_ages: list[str]) -> dict:
    branches_data: dict = {}
    for age in target_ages:
        age_groups = groups.get(age, {})
        branches_data[age] = {
            "universal": [serialize_advance(a, mod_names) for a in age_groups.get("", [])],
            "adm":       [serialize_advance(a, mod_names) for a in age_groups.get("adm", [])],
            "dip":       [serialize_advance(a, mod_names) for a in age_groups.get("dip", [])],
            "mil":       [serialize_advance(a, mod_names) for a in age_groups.get("mil", [])],
        }
    return {
        "ages":      target_ages,
        "ageLabels": {age: age_display(age) for age in target_ages},
        "branches":  branches_data,
    }


def generate_data_js(groups: dict, mod_names: set[str], target_ages: list[str]) -> str:
    data      = build_data(groups, mod_names, target_ages)
    data_json = json.dumps(data, separators=(",", ":"))
    return f"const D = {data_json};\n"


# -- entry point -------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only-unlocks", action="store_true",
                        help="(CLI) show only unlock_* effects")
    parser.add_argument("--mod-only", action="store_true",
                        help="(CLI) only print combos with at least one mod advance")
    parser.add_argument("--combo", metavar="FILTER",
                        help='(CLI) substring filter on combo label')
    parser.add_argument("--json", metavar="FILE", nargs="?", const="tools/advance_data.js",
                        help="Generate JS data file for advance_explorer.html (default: tools/advance_data.js)")
    args = parser.parse_args()

    print("Loading advances...", file=sys.stderr)
    advances, mod_names = load_all_advances()
    print(f"  {len(advances)} advances loaded, {len(mod_names)} from mod", file=sys.stderr)

    groups    = group_advances(advances)
    all_ages  = sorted_ages(groups)

    target_ages = [a for a in AGE_ORDER if a in groups and
                   any(groups[a].get(b) for b in BRANCHES)]
    if not target_ages:
        target_ages = [a for a in all_ages if any(groups[a].get(b) for b in BRANCHES)]

    print(f"  Ages with branched advances: {target_ages}", file=sys.stderr)

    if args.json:
        out_path = Path(args.json)
        out_path.write_text(generate_data_js(groups, mod_names, target_ages), encoding="utf-8")
        print(f"Written: {out_path.resolve()}", file=sys.stderr)
        print(f"  Open tools/advance_explorer.html in a browser to explore.", file=sys.stderr)
        return

    combos = build_combos(groups, target_ages)
    print(f"  {len(combos)} combinations to enumerate", file=sys.stderr)

    render_combos(
        combos=combos,
        groups=groups,
        mod_names=mod_names,
        only_unlocks=args.only_unlocks,
        mod_only=args.mod_only,
        combo_filter=args.combo,
    )


if __name__ == "__main__":
    main()
