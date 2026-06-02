#!/usr/bin/env python3
"""
generate_workshop.py — Regenerate GEN: sections in WORKSHOP_DESCRIPTION.bbcode.
Reads mod files to produce up-to-date BBCode content for the Steam Workshop description.

Usage:
    python tools/generate_workshop.py                       # regenerate all sections
    python tools/generate_workshop.py --section advances    # one section only
    python tools/generate_workshop.py --dry-run             # print to stdout, don't write
    python tools/generate_workshop.py --clean               # write marker-stripped copy ready for paste

The source file (WORKSHOP_DESCRIPTION.bbcode) keeps <!-- GEN:name --> markers so the
generator can be re-run. Use --clean to emit a paste-ready file with markers removed.
"""

import argparse
import re
import sys
from pathlib import Path

MOD_ROOT = Path(__file__).resolve().parent.parent
WORKSHOP_FILE = MOD_ROOT / "WORKSHOP_DESCRIPTION.bbcode"

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

AGE_NAMES: dict[str, tuple[str, int]] = {
    "age_2_renaissance": ("Age of Renaissance", 2),
    "age_3_discovery":   ("Age of Discovery",   3),
    "age_4_reformation": ("Age of Reformation", 4),
    "age_5_absolutism":  ("Age of Absolutism",  5),
    "age_6_revolutions": ("Age of Revolutions", 6),
}

SUBJECT_CHAINS: list[tuple[str, list[str]]] = [
    ("Personal Union",   ["junior_partner", "lesser_partner"]),
    ("Shadow / Client",  ["shadow_state", "client_state", "puppet_state"]),
    ("Elite & Cultural", ["elite_enclave", "palatinate", "artists_commune",
                          "scientific_college", "naval_administration"]),
    ("Trade",            ["associated_republic", "chartered_company"]),
    ("Governance",       ["protectorate", "crown_dependency", "holy_protectorate",
                          "provincial_governorate", "tax_farm", "military_march"]),
]

SUBJECT_AGES: dict[str, int] = {
    "junior_partner": 2,       "lesser_partner": 2,
    "shadow_state": 2,         "client_state": 3,         "puppet_state": 5,
    "elite_enclave": 2,        "palatinate": 4,           "artists_commune": 2,
    "scientific_college": 4,   "naval_administration": 3,
    "associated_republic": 2,  "chartered_company": 5,
    "protectorate": 3,         "crown_dependency": 2,     "holy_protectorate": 4,
    "provincial_governorate": 5, "tax_farm": 5,           "military_march": 5,
}

TRAIT_FILES: list[tuple[str, str, str]] = [
    ("cabinet.txt",
     "Core Cabinet Traits",
     "Tier 1 simple traits, Tier 2 kiss-curse trade-offs with real downsides, "
     "Tier 3 attribute-scaled triads covering integration, antagonism, exploration, and more"),
    ("cc_age_traits.txt",
     "Age Traits",
     "Era-specific traits granted through historical period events — "
     "Renaissance humanists, Reformation theologians, Absolutist administrators, Revolutionary agitators"),
    ("cc_conditional_traits.txt",
     "Conditional Traits",
     "Dynamic traits that spawn based on your realm's development level, societal value axes (17 ideological pairs), "
     "regional/religious context, military specialization, parliamentary activity, and specific game actions"),
    ("cc_negative_traits.txt",
     "Negative Traits",
     "Acquired through underperformance events; each has a dedicated rehabilitation chain "
     "that removes the trait when you address the underlying problem"),
]

# Second element may be a filename string or a glob pattern (e.g. "cc_bond_*.txt").
EVENT_INFO: list[tuple[str, str, str]] = [
    ("cc_cabinet",          "cc_cabinet_events.txt",            "Minister counsel, estate relations, diplomatic situations, provincial affairs"),
    ("cc_traits",           "cc_trait_events.txt",              "Age trait acquisition, ruler teaching, peer learning"),
    ("cc_cond",             "cc_conditional_trait_events.txt",  "Conditional trait spawning based on realm conditions and actions"),
    ("cc_synergy",          "cc_synergy_events.txt",            "Trait pair synergies — temporary bonuses when ministers share trait families"),
    ("cc_neg",              "cc_negative_trait_events.txt",     "Underperformance events and rehabilitation chains"),
    ("cc_wealth",           "cc_wealth_events.txt",             "Wealth hoarding pressure and minister enrichment"),
    ("cc_dual",             "cc_dual_synergy_events.txt",       "Cabinet × religious figure dual-role synergies"),
    ("cc_intl",             "cc_intl_synergy_events.txt",       "Cross-country interactions between neighboring courts"),
    ("cc_feudal",           "cc_feudal_events.txt",             "Feudal era court events"),
    ("cc_legacy",           "cc_legacy_events.txt",             "Senior minister retirement and legacy transmission"),
    ("cc_legend",           "cc_legend_events.txt",             "Legendary minister quest chains"),
    ("cc_hyw",              "cc_hyw_events.txt",                "Hundred Years War flavor — FRA/ENG war outcomes, observer reactions, vassal defection pressure"),
    ("cc_personality",      "cc_ai_personality_events.txt",     "Dynamic AI personality inflection events — key historical turning points"),
    ("cc_bonds",            "cc_bond_*.txt",                    "Overlord-subject bond system — per-type chain events, monitor, status reveals, AoR payoffs"),
    ("cc_rival",            "cc_rivalry_events.txt",            "Court rivalry escalation: minister complaint → letter unsealed → faction hardens"),
    ("cc_cabal",            "cc_cabal_events.txt",              "Cabinet alliance formation: alliance forms → joint reform proposal"),
    ("cc_wc",               "cc_war_council_events.txt",        "War council: active-war events, post-war reform proposals, outdated general retirement"),
    ("cc_fac",              "cc_estate_faction_events.txt",     "Estate faction capture events"),
    ("cc_prog",             "cc_progression_events.txt",        "Stepping stone trait progression chains (Paths A/C/D/F/E)"),
    ("cc_colonial",         "cc_colonial_events.txt",           "Colonial divan: charter company events + decolonization crisis chain"),
    ("cc_posting",          "cc_colonial_posting_events.txt",   "Colonial posting duty: dispatch, corruption, native uprising, fever"),
    ("cc_hus",              "cc_hus_events.txt",                "Hussite Wars — papal loan event"),
    ("cc_invasion_mexico",  "cc_invasion_mexico.txt",           "Mexican Conquest situation — expedition decisions, Mesoamerican reactions, confederation events, conquest resolution"),
]

HIGHLIGHTED_TRAITS: list[str] = [
    "iron_disciplinarian",
    "shadow_counselor",
    "progressive_reformist",
    "war_hawk",
    "master_integrator",
    "master_statesman",
    "grand_chancellor",
    "tribune_of_the_people",
    "philosopher_king",
]

# ---------------------------------------------------------------------------
# File / localization helpers
# ---------------------------------------------------------------------------

def read_bom(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    return data.decode("utf-8", errors="replace")


def load_all_loc() -> dict[str, str]:
    """Load all mod localization .yml files into a single key→string dict."""
    loc: dict[str, str] = {}
    for loc_dir in [
        MOD_ROOT / "in_game" / "localization" / "english",
        MOD_ROOT / "main_menu" / "localization" / "english",
    ]:
        if not loc_dir.exists():
            continue
        for yml in sorted(loc_dir.glob("*.yml")):
            text = read_bom(yml)
            for m in re.finditer(
                r'^\s+([\w.]+):\d*\s+"((?:[^"\\]|\\.)*)"',
                text, re.MULTILINE
            ):
                loc[m.group(1)] = m.group(2)
    return loc


def first_sentence(text: str) -> str:
    """Return the first sentence, stripping Clausewitz markup codes."""
    text = re.sub(r"\[[^\]]+\]", "", text)
    text = re.sub(r"\$[^$]+\$", lambda m: m.group(0)[1:-1].replace("_", " ").title(), text)
    text = text.strip()
    m = re.match(r"([^.!?]+[.!?])", text)
    return m.group(1).strip() if m else text[:140].strip()


def id_to_title(s: str) -> str:
    return s.replace("_", " ").title()


# ---------------------------------------------------------------------------
# Clausewitz tokenizer + shallow block parser
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """Tokenize a Clausewitz script file (comments stripped)."""
    text = re.sub(r"#[^\n]*", "", text)
    return re.findall(r'"[^"]*"|\{|\}|=|[\w:.\-]+', text)


def _flat_parse(tokens: list[str]) -> dict[str, list[str]]:
    """
    Parse a token list at depth 0 only.
    Returns {key: [values]} where nested blocks are represented as '__block__'.
    Repeated keys accumulate into the list.
    """
    result: dict[str, list[str]] = {}
    i = 0
    while i < len(tokens):
        if i + 1 < len(tokens) and tokens[i + 1] == "=":
            key = tokens[i]
            i += 2
            if i < len(tokens) and tokens[i] == "{":
                depth = 1
                i += 1
                while i < len(tokens) and depth > 0:
                    if tokens[i] == "{":
                        depth += 1
                    elif tokens[i] == "}":
                        depth -= 1
                    i += 1
                result.setdefault(key, []).append("__block__")
            elif i < len(tokens):
                result.setdefault(key, []).append(tokens[i].strip('"'))
                i += 1
        else:
            i += 1
    return result


def extract_top_blocks(path: Path) -> list[tuple[str, dict[str, list[str]]]]:
    """Return (id, shallow_dict) for each top-level block in a Clausewitz file."""
    tokens = tokenize(read_bom(path))
    results: list[tuple[str, dict[str, list[str]]]] = []
    i = 0
    while i < len(tokens):
        if (i + 2 < len(tokens)
                and tokens[i + 1] == "="
                and tokens[i + 2] == "{"):
            block_id = tokens[i]
            i += 3
            depth = 1
            block_tokens: list[str] = []
            while i < len(tokens) and depth > 0:
                tok = tokens[i]
                if tok == "{":
                    depth += 1
                elif tok == "}":
                    depth -= 1
                if depth > 0:
                    block_tokens.append(tok)
                i += 1
            results.append((block_id, _flat_parse(block_tokens)))
        else:
            i += 1
    return results


def count_events(path_or_glob: "Path | str", base_dir: "Path | None" = None) -> int:
    """Count country events. Accepts a Path, a filename string, or a glob pattern."""
    if isinstance(path_or_glob, str) and ("*" in path_or_glob or "?" in path_or_glob):
        search_dir = base_dir or Path(".")
        total = 0
        for p in sorted(search_dir.glob(path_or_glob)):
            total += len(re.findall(r"\btype\s*=\s*country_event\b", read_bom(p)))
        return total
    if isinstance(path_or_glob, str):
        p = (base_dir / path_or_glob) if base_dir else Path(path_or_glob)
    else:
        p = path_or_glob
    if not p.exists():
        return 0
    return len(re.findall(r"\btype\s*=\s*country_event\b", read_bom(p)))


# ---------------------------------------------------------------------------
# BBCode helpers
# ---------------------------------------------------------------------------

def bb(tag: str, text: str) -> str:
    return f"[{tag}]{text}[/{tag}]"

def bold(text: str) -> str:
    return bb("b", text)

def italic(text: str) -> str:
    return bb("i", text)

def list_block(items: list[str]) -> str:
    inner = "\n".join(f"[*] {item}" for item in items)
    return f"[list]\n{inner}\n[/list]"

def table_block(headers: list[str], rows: list[list[str]]) -> str:
    header_row = "".join(f"[th]{h}[/th]" for h in headers)
    lines = [f"[table]", f"[tr]{header_row}[/tr]"]
    for row in rows:
        cells = "".join(f"[td]{cell}[/td]" for cell in row)
        lines.append(f"[tr]{cells}[/tr]")
    lines.append("[/table]")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Section generators — all return BBCode strings
# ---------------------------------------------------------------------------

def gen_game_rules(loc: dict[str, str]) -> str:
    path = MOD_ROOT / "main_menu" / "common" / "game_rules" / "cc_game_rules.txt"
    if not path.exists():
        return italic("Game rules file not found.")

    blocks: list[str] = []
    for rule_id, d in extract_top_blocks(path):
        rule_name = loc.get(f"rule_{rule_id}", id_to_title(rule_id))
        rule_desc = loc.get(f"rule_{rule_id}_desc", "")
        default_opt = (d.get("default") or [""])[0]

        section = [bold(rule_name)]
        if rule_desc:
            section.append(rule_desc)

        options: list[str] = []
        for key, vals in d.items():
            if key == "default":
                continue
            if "__block__" in vals:
                opt_name = loc.get(f"setting_{key}", id_to_title(key))
                opt_desc = loc.get(f"setting_{key}_desc", "")
                tag = f" {italic('(default)')}" if key == default_opt else ""
                entry = f"{bold(opt_name)}{tag}"
                if opt_desc:
                    entry += f" — {opt_desc}"
                options.append(entry)

        if options:
            section.append(list_block(options))

        blocks.append("\n".join(section))

    return "\n\n".join(blocks)


def gen_trait_summary(loc: dict[str, str]) -> str:
    traits_dir = MOD_ROOT / "in_game" / "common" / "traits"
    lines: list[str] = []
    total = 0

    for filename, category, desc in TRAIT_FILES:
        path = traits_dir / filename
        count = len(extract_top_blocks(path)) if path.exists() else 0
        total += count
        lines.append(bold(f"{category} ({count})"))
        lines.append(desc + ".")
        lines.append("")

    lines.append(italic(f"Total: {total}+ traits"))
    lines.append("")
    lines.append(bold("Notable traits:"))

    trait_items: list[str] = []
    for trait_id in HIGHLIGHTED_TRAITS:
        name = loc.get(trait_id, id_to_title(trait_id))
        desc = (
            loc.get(f"desc_{trait_id}")
            or loc.get(f"{trait_id}_desc")
            or ""
        )
        entry = bold(name)
        if desc:
            entry += f" — {first_sentence(desc)}"
        trait_items.append(entry)

    lines.append(list_block(trait_items))
    return "\n".join(lines).rstrip()


def gen_event_categories(_loc: dict[str, str]) -> str:
    events_dir = MOD_ROOT / "in_game" / "events"
    total = 0
    rows: list[list[str]] = []
    for ns, filename, desc in EVENT_INFO:
        count = count_events(filename, base_dir=events_dir)
        total += count
        rows.append([ns, str(count), desc])

    return table_block(["Namespace", "Events", "Description"], rows) + \
           f"\n\n{italic(f'~{total} events total')}"


def gen_subject_types(loc: dict[str, str]) -> str:
    blocks: list[str] = []
    for chain_name, subject_ids in SUBJECT_CHAINS:
        items: list[str] = []
        for sid in subject_ids:
            name = (
                loc.get(sid)
                or loc.get(f"AM_{sid}")
                or id_to_title(sid)
            )
            desc = loc.get(f"{sid}_desc", "")
            age = SUBJECT_AGES.get(sid, "?")
            short = first_sentence(desc) if desc else ""
            entry = f"{bold(name)} {italic(f'(unlocks Age {age})')}"
            if short:
                entry += f" — {short}"
            items.append(entry)
        blocks.append(bold(chain_name) + "\n" + list_block(items))
    return "\n\n".join(blocks)


def gen_advances(loc: dict[str, str]) -> str:
    advance_dir = MOD_ROOT / "in_game" / "common" / "advances"

    by_age: dict[str, list[tuple[str, dict[str, list[str]]]]] = {}
    for fname in ["cc_subject_advances.txt", "cc_late_era_advances.txt", "cc_literacy_advances.txt"]:
        path = advance_dir / fname
        if not path.exists():
            continue
        for adv_id, d in extract_top_blocks(path):
            age_vals = d.get("age", [])
            age_key = age_vals[0] if age_vals else "unknown"
            by_age.setdefault(age_key, []).append((adv_id, d))

    blocks: list[str] = []
    for age_key, (age_label, _age_num) in AGE_NAMES.items():
        advances = by_age.get(age_key, [])
        if not advances:
            continue

        items: list[str] = []
        for adv_id, d in advances:
            name = loc.get(adv_id, id_to_title(adv_id))
            desc = loc.get(f"{adv_id}_desc", "")
            short = first_sentence(desc) if desc else ""

            branch_vals = d.get("for", [])
            branch = branch_vals[0].upper() if branch_vals else "All"
            branch_tag = italic(f"[{branch}]")

            unlocks = d.get("unlock_subject_type", [])
            if unlocks:
                unlock_names = [
                    loc.get(u) or loc.get(f"AM_{u}") or id_to_title(u)
                    for u in unlocks
                ]
                entry = f"{branch_tag} {bold(name)} — Unlocks: {bold(', '.join(unlock_names))}."
                if short:
                    entry += f" {short}"
            else:
                entry = f"{branch_tag} {bold(name)}"
                if short:
                    entry += f" — {short}"
            items.append(entry)

        blocks.append(
            bold(f"{age_label}") + f" ({len(advances)} advances)\n" + list_block(items)
        )

    return "\n\n".join(blocks)


def gen_country_starts(_loc: dict[str, str]) -> str:
    entries = [
        (
            "France — Hundred Years War Flavor", "default: on",
            "France begins with historical modifiers reflecting its position at the opening of the Hundred Years War: "
            "levy readiness, estate pressure, and elevated antagonism from its Lowlands-culture neighbors. "
            "The Lowlands antagonism decays over 200 years. France also starts with a permanent modifier "
            "representing its expansionist posture toward the Lowlands."
        ),
        (
            "England — Hundred Years War Flavor", "default: on",
            "England begins with estate and levy modifiers reflecting its precarious continental position at the "
            "start of the Hundred Years War — a kingdom stretched across the Channel with ambitious claims and restless nobles."
        ),
        (
            "Mamluks — Foreign Rule Strain", "default: on",
            "The Mamluks begin with a permanent peasant levy penalty (representing their status as a foreign military "
            "caste ruling over native Egyptian society) and a severe military strain modifier that decays over 200 years. "
            "Combined, these represent the fragility of Mamluk rule and ease as the regime stabilizes — or they don't."
        ),
        (
            "Ottomans — No Colonization", "default: on",
            "The Ottomans are permanently prevented from colonizing overseas. This reflects the historical Ottoman "
            "orientation as a land empire focused on Anatolia, the Balkans, and the Middle East, rather than "
            "competing in Atlantic exploration."
        ),
    ]
    blocks: list[str] = []
    for name, tag, body in entries:
        blocks.append(f"{bold(name)} {italic(f'({tag})')}\n{body}")
    return "\n\n".join(blocks)


def gen_privileges_reforms(loc: dict[str, str]) -> str:
    advance_dir = MOD_ROOT / "in_game" / "common" / "advances"

    privileges: list[tuple[str, str]] = []
    reforms: list[tuple[str, str, str]] = []

    for fname in ["cc_subject_advances.txt", "cc_late_era_advances.txt", "cc_literacy_advances.txt"]:
        path = advance_dir / fname
        if not path.exists():
            continue
        for adv_id, d in extract_top_blocks(path):
            adv_name = loc.get(adv_id, id_to_title(adv_id))
            for priv_id in d.get("unlock_estate_privilege", []):
                priv_name = loc.get(priv_id, id_to_title(priv_id))
                privileges.append((priv_name, adv_name))
            for reform_id in d.get("unlock_government_reform", []):
                reform_name = loc.get(reform_id, id_to_title(reform_id))
                reform_desc = loc.get(f"{reform_id}_desc", "")
                reforms.append((reform_name, reform_desc, adv_name))

    if not privileges and not reforms:
        return italic("No estate privileges or government reforms detected.")

    blocks: list[str] = []
    if privileges:
        priv_items = [f"{bold(name)} {italic(f'(via: {from_adv})')}" for name, from_adv in privileges]
        blocks.append(bold("Estate Privileges") + "\n" + list_block(priv_items))

    if reforms:
        reform_items: list[str] = []
        for name, desc, from_adv in reforms:
            short = first_sentence(desc) if desc else ""
            entry = bold(name)
            if short:
                entry += f" — {short}"
            entry += f" {italic(f'(via: {from_adv})')}"
            reform_items.append(entry)
        blocks.append(bold("Government Reforms") + "\n" + list_block(reform_items))

    return "\n\n".join(blocks)


# ---------------------------------------------------------------------------
# GEN: section injection
# ---------------------------------------------------------------------------

SECTION_GENERATORS: dict[str, object] = {
    "game-rules":         gen_game_rules,
    "trait-summary":      gen_trait_summary,
    "event-categories":   gen_event_categories,
    "subject-types":      gen_subject_types,
    "advances":           gen_advances,
    "country-starts":     gen_country_starts,
    "privileges-reforms": gen_privileges_reforms,
}

GEN_MARKER = re.compile(r"<!-- GEN:\w+ -->.*?<!-- /GEN:\w+ -->", re.DOTALL)


def update_section(text: str, name: str, content: str) -> str:
    pattern = re.compile(
        rf"(<!-- GEN:{re.escape(name)} -->).*?(<!-- /GEN:{re.escape(name)} -->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        print(
            f"  WARNING: GEN:{name} marker not found in {WORKSHOP_FILE.name}",
            file=sys.stderr,
        )
        return text
    return pattern.sub(rf"\1\n{content}\n\2", text)


def strip_markers(text: str) -> str:
    """Remove GEN marker comment lines, leaving only the generated content."""
    text = re.sub(r"<!-- /?GEN:[\w-]+ -->\n?", "", text)
    return text


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--section",
        choices=list(SECTION_GENERATORS),
        metavar="NAME",
        help=f"Regenerate only this section. Choices: {', '.join(SECTION_GENERATORS)}",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated BBCode sections to stdout without writing the file",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="After regenerating, also write a marker-stripped copy to WORKSHOP_DESCRIPTION_upload.bbcode",
    )
    args = parser.parse_args()

    print("Loading localization files...", file=sys.stderr)
    loc = load_all_loc()
    print(f"  Loaded {len(loc)} localization keys.", file=sys.stderr)

    sections = (
        {args.section: SECTION_GENERATORS[args.section]}
        if args.section
        else SECTION_GENERATORS
    )

    if args.dry_run:
        for name, gen_fn in sections.items():
            print(f"\n{'=' * 60}")
            print(f"=== GEN:{name} ===")
            print("=" * 60)
            print(gen_fn(loc))
        return

    if not WORKSHOP_FILE.exists():
        print(f"ERROR: {WORKSHOP_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    text = WORKSHOP_FILE.read_text(encoding="utf-8")
    for name, gen_fn in sections.items():
        print(f"  Generating: {name}...", file=sys.stderr)
        content = gen_fn(loc)
        text = update_section(text, name, content)

    WORKSHOP_FILE.write_text(text, encoding="utf-8")
    print(f"Updated: {WORKSHOP_FILE}", file=sys.stderr)

    if args.clean:
        clean_path = MOD_ROOT / "WORKSHOP_DESCRIPTION_upload.bbcode"
        clean_path.write_text(strip_markers(text), encoding="utf-8")
        print(f"Clean copy: {clean_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
