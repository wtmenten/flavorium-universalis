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

GAME_COMMON_DIR = GAME_ADVANCES_DIR.parent
MOD_COMMON_DIR  = MOD_ADVANCES_DIR.parent

# Keys that belong to the advance definition itself, not counted as effects
SKIP_KEYS = {
    "age", "icon", "requires", "for", "depth", "ai_weight",
    "potential", "allow", "ai_preference_tags", "research_cost",
    "starting_technology_level", "allow_children", "has_cultural_maintenance",
}

# -- unlock definition parser ------------------------------------------------
# Block keys that are scripted conditions/events — skip their sub-blocks
_COND_KEYS: set[str] = {
    "potential", "allow", "trigger", "limit", "visible", "creation_visible",
    "join_offensive_wars_always", "join_offensive_wars_can_call",
    "join_defensive_wars_always", "join_defensive_wars_can_call",
    "diplo_chance_accept_subject", "diplo_chance_accept_overlord",
    "ai_wants_to_be_overlord", "ai_wants_to_be_subject",
    "on_enable", "on_disable", "on_activate", "on_revoke", "can_revoke",
    "can_pass", "location_potential", "country_potential", "remove_if",
    "unique_production_methods", "possible_production_methods",
    "construction_demand", "graphical_tags", "estate_preferences",
    "enabled_through_diplomacy", "visible_through_diplomacy",
    "allow_declaring_wars", "ai_will_do", "start_effect", "select_trigger",
    "hidden", "map", "diplo_chance_accept", "visible_through_nation_designer",
    "combat", "maintenance_demand",
}


def _parse_dict(tokens: list[str], start: int) -> tuple[dict, int]:
    """Recursive descent: parse key=value pairs from start until matching '}'."""
    result: dict = {}
    i = start
    n = len(tokens)
    while i < n:
        t = tokens[i]
        if t == "}":
            return result, i + 1
        if t == "{":
            # bare anonymous block — skip
            i += 1
            depth = 1
            while i < n and depth:
                if tokens[i] == "{":
                    depth += 1
                elif tokens[i] == "}":
                    depth -= 1
                i += 1
            continue
        if i + 1 < n and tokens[i + 1] == "=":
            key = t
            i += 2
            if i < n and tokens[i] == "{":
                i += 1  # consume '{'
                if key in _COND_KEYS:
                    depth = 1
                    while i < n and depth:
                        if tokens[i] == "{":
                            depth += 1
                        elif tokens[i] == "}":
                            depth -= 1
                        i += 1
                else:
                    sub, i = _parse_dict(tokens, i)
                    existing = result.get(key)
                    if existing is None:
                        result[key] = sub
                    elif isinstance(existing, list):
                        existing.append(sub)
                    else:
                        result[key] = [existing, sub]
            else:
                val = tokens[i] if i < n else ""
                i += 1
                existing = result.get(key)
                if existing is None:
                    result[key] = val
                elif isinstance(existing, list):
                    existing.append(val)
                else:
                    result[key] = [existing, val]
        else:
            i += 1
    return result, i


def _parse_defs_from_file(path: Path) -> dict[str, dict]:
    """Parse named top-level blocks from a Clausewitz file → {name: block_dict}."""
    try:
        text = path.read_text(encoding="utf-8-sig")
    except Exception:
        try:
            text = path.read_text(encoding="cp1252")
        except Exception:
            return {}
    text = re.sub(r"#[^\n]*", "", text)
    tokens = re.findall(r'"[^"]*"|\{|\}|=|[^\s{}="]+', text)
    defs: dict[str, dict] = {}
    i = 0
    n = len(tokens)
    while i < n:
        if i + 2 < n and tokens[i + 1] == "=" and tokens[i + 2] == "{":
            name = tokens[i]
            i += 3
            block, i = _parse_dict(tokens, i)
            defs[name] = block
        else:
            i += 1
    return defs


def _flat_modifier(block) -> list[tuple[str, str]]:
    """Flatten a modifier dict to [(key, value)] keeping only scalar string values."""
    if not isinstance(block, dict):
        return []
    out = []
    for k, v in block.items():
        if isinstance(v, str):
            out.append((k, v))
        elif isinstance(v, list) and v and all(isinstance(x, str) for x in v):
            out.append((k, ", ".join(v)))
    return out


# -- per-type extractors -------------------------------------------------------

def _extract_subject_type(_name: str, block: dict) -> list[dict]:
    sections = []
    for key, label in [("overlord_modifier", "Overlord"), ("subject_modifier", "Subject")]:
        entries = _flat_modifier(block.get(key))
        if entries:
            sections.append({"label": label, "entries": entries})
    STAT_KEYS = {
        "strength_vs_overlord", "diplomatic_capacity_cost_scale",
        "annexation_min_opinion", "annexation_min_years_before",
        "institution_spread_to_overlord", "institution_spread_to_subject",
        "great_power_score_transfer", "subject_pays",
    }
    stats = [(k, v) for k, v in block.items() if k in STAT_KEYS and isinstance(v, str)]
    if stats:
        sections.append({"label": "Stats", "entries": stats})
    return sections


def _extract_estate_privilege(_name: str, block: dict) -> list[dict]:
    sections = []
    entries = _flat_modifier(block.get("country_modifier"))
    if entries:
        sections.append({"label": "Country", "entries": entries})
    return sections


def _extract_government_reform(_name: str, block: dict) -> list[dict]:
    sections = []
    entries = _flat_modifier(block.get("country_modifier"))
    if entries:
        meta = []
        if "age" in block:
            meta.append(("age", block["age"]))
        if "years" in block:
            meta.append(("duration", f"{block['years']} years"))
        if meta:
            sections.append({"label": "Info", "entries": meta})
        sections.append({"label": "Modifier", "entries": entries})
    return sections


def _extract_building(_name: str, block: dict) -> list[dict]:
    sections = []
    loc = _flat_modifier(block.get("modifier"))
    if loc:
        sections.append({"label": "Location", "entries": loc})
    cap = _flat_modifier(block.get("capital_country_modifier"))
    if cap:
        sections.append({"label": "Country (capital)", "entries": cap})
    INFO_KEYS = {"max_levels", "pop_type", "category", "build_time"}
    info = [(k, v) for k, v in block.items() if k in INFO_KEYS and isinstance(v, str)]
    if info:
        sections.append({"label": "Info", "entries": info})
    return sections


def _extract_law(_name: str, block: dict) -> list[dict]:
    sections = []
    INFO_KEYS = {"law_category", "law_gov_group"}
    info = [(k, v) for k, v in block.items() if k in INFO_KEYS and isinstance(v, str)]
    if info:
        sections.append({"label": "Info", "entries": info})
    # Named variant sub-blocks each containing country_modifier
    for key, val in block.items():
        if isinstance(val, dict):
            entries = _flat_modifier(val.get("country_modifier"))
            if entries:
                label = key.replace("_", " ").title()
                sections.append({"label": label, "entries": entries})
    return sections


def _extract_casus_belli(_name: str, block: dict) -> list[dict]:
    KEYS = {"war_goal_type", "no_cb", "badboy"}
    entries = [(k, v) for k, v in block.items() if k in KEYS and isinstance(v, str)]
    if entries:
        return [{"label": "CB", "entries": entries}]
    return []


def _extract_unit(_name: str, block: dict) -> list[dict]:
    KEYS = {"copy_from", "strength_damage_taken", "morale_damage_taken", "buildable"}
    entries = [(k, v) for k, v in block.items() if k in KEYS and isinstance(v, str)]
    if entries:
        return [{"label": "Unit", "entries": entries}]
    return []


def _extract_levy(_name: str, block: dict) -> list[dict]:
    KEYS = {"unit", "size", "allowed_pop_type"}
    entries = []
    for k, v in block.items():
        if k not in KEYS:
            continue
        if isinstance(v, str):
            entries.append((k, v))
        elif isinstance(v, list) and all(isinstance(x, str) for x in v):
            entries.append((k, ", ".join(v)))
    if entries:
        return [{"label": "Levy", "entries": entries}]
    return []


def _extract_interaction(_name: str, block: dict) -> list[dict]:
    KEYS = {"type", "category"}
    entries = [(k, v) for k, v in block.items() if k in KEYS and isinstance(v, str)]
    if entries:
        return [{"label": "Interaction", "entries": entries}]
    return []


def _extract_ability(_name: str, block: dict) -> list[dict]:
    KEYS = {"toggle", "army_only", "navy_only"}
    entries = [(k, v) for k, v in block.items() if k in KEYS and isinstance(v, str)]
    if entries:
        return [{"label": "Ability", "entries": entries}]
    return []


# Map unlock_type → (directories to search, extractor function)
_UNLOCK_EXTRACTOR_CONFIG: list[tuple[str, list[Path], object]] = [
    ("unlock_subject_type",
     [GAME_COMMON_DIR / "subject_types", MOD_COMMON_DIR / "subject_types"],
     _extract_subject_type),
    ("unlock_estate_privilege",
     [GAME_COMMON_DIR / "estate_privileges", MOD_COMMON_DIR / "estate_privileges"],
     _extract_estate_privilege),
    ("unlock_government_reform",
     [GAME_COMMON_DIR / "government_reforms", MOD_COMMON_DIR / "government_reforms"],
     _extract_government_reform),
    ("unlock_building",
     [GAME_COMMON_DIR / "building_types", MOD_COMMON_DIR / "building_types"],
     _extract_building),
    ("unlock_law",
     [GAME_COMMON_DIR / "laws", MOD_COMMON_DIR / "laws"],
     _extract_law),
    ("unlock_casus_belli",
     [GAME_COMMON_DIR / "casus_belli", MOD_COMMON_DIR / "casus_belli"],
     _extract_casus_belli),
    ("unlock_unit",
     [GAME_COMMON_DIR / "unit_types", MOD_COMMON_DIR / "unit_types"],
     _extract_unit),
    ("unlock_levy",
     [GAME_COMMON_DIR / "levies", MOD_COMMON_DIR / "levies"],
     _extract_levy),
    ("unlock_interaction",
     [GAME_COMMON_DIR / "country_interactions", MOD_COMMON_DIR / "country_interactions"],
     _extract_interaction),
    ("unlock_ability",
     [GAME_COMMON_DIR / "unit_abilities", MOD_COMMON_DIR / "unit_abilities"],
     _extract_ability),
]


def load_unlock_defs(advances: list[dict]) -> dict:
    """Parse game/mod files and return tooltip data only for IDs referenced in advances."""
    # Collect the exact IDs each unlock type needs
    needed: dict[str, set[str]] = defaultdict(set)
    for adv in advances:
        for k, v in adv.get("_effects", []):
            if k.startswith("unlock_"):
                needed[k].add(v)

    result: dict[str, dict] = {}
    for unlock_type, dirs, extractor in _UNLOCK_EXTRACTOR_CONFIG:
        ids_needed = needed.get(unlock_type)
        if not ids_needed:
            continue
        type_defs: dict[str, dict] = {}
        for d in dirs:
            if not d.exists():
                continue
            for path in sorted(d.glob("*.txt")):
                if path.stem.lower() == "readme":
                    continue
                for name, block in _parse_defs_from_file(path).items():
                    if name in ids_needed and name not in type_defs:
                        sections = extractor(name, block)
                        if sections:
                            type_defs[name] = {"sections": sections}
        if type_defs:
            result[unlock_type] = type_defs
    return result


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


def generate_data_js(
    groups: dict, mod_names: set[str], target_ages: list[str], advances: list[dict]
) -> str:
    data         = build_data(groups, mod_names, target_ages)
    data_json    = json.dumps(data, separators=(",", ":"))
    unlock_defs  = load_unlock_defs(advances)
    defs_json    = json.dumps(unlock_defs, separators=(",", ":"))
    return f"const D = {data_json};\nconst UNLOCK_DEFS = {defs_json};\n"


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
        print("  Loading unlock definitions...", file=sys.stderr)
        out_path.write_text(
            generate_data_js(groups, mod_names, target_ages, advances),
            encoding="utf-8",
        )
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
