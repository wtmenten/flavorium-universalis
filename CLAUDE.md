# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Flavorium Universalis** is a Europa Universalis V mod (v0.1, compatible with EU V 1.2.*) focused on enhancing cabinet member gameplay with new traits and dynamic events.

EU V Modding Documentation: https://eu5.paradoxwikis.com/Modding

**Documentation references (check in this order):**
1. [docs/eu5-modding-reference.md](docs/eu5-modding-reference.md) — Internal summarized modding reference
2. [docs/offline-wiki/](docs/offline-wiki/) — Offline copy of EU5 Paradox Wiki modding pages (40 pages, ~1.5MB)
3. [tools/wiki_search.py](tools/wiki_search.py) — Fast search tool for offline docs

# lookup tools

## Vanilla game file search

**Prefer `tools/vanilla_search.py` over raw grep for all vanilla lookups.** It handles path scoping, BOM encoding, and result formatting automatically.

```
# Check if a modifier name is valid in vanilla (partial name OK):
python tools/vanilla_search.py modifier <name>

# List all type:value identifiers used in vanilla common files:
python tools/vanilla_search.py values <type_key>
# e.g. values religion_group / values government_type / values sub_continent / values estate_type

# Show vanilla usage snippets for any trigger, effect, or key (--events to search events/ instead):
python tools/vanilla_search.py examples <term>
python tools/vanilla_search.py examples <term> --events

# List every defined bias/opinion modifier name:
python tools/vanilla_search.py biases
```

Use these instead of ad-hoc grep when verifying modifier names, finding valid type values, checking trigger/effect syntax in context, or looking up bias names before calling `add_opinion`. Fall back to raw grep only for patterns the tool doesn't cover.

## Offline wiki docs search

**Use `tools/wiki_search.py` to search the offline EU5 modding wiki docs** ([docs/offline-wiki/](docs/offline-wiki/)). Faster than web fetching, works offline.

```
# Search effects by name (partial match, case-insensitive):
python tools/wiki_search.py effect every_country
python tools/wiki_search.py effect add_trait

# Search triggers:
python tools/wiki_search.py trigger has_advance
python tools/wiki_search.py trigger is_at_war

# Search scope links:
python tools/wiki_search.py scope_link overlord

# Search modifier types:
python tools/wiki_search.py modifier cabinet_efficiency

# Search on-actions:
python tools/wiki_search.py on_action on_game_start

# Search all offline docs for a term:
python tools/wiki_search.py all declare_war
```

**Reading docs files directly:** If you want to load some document reference excerpts into context directly, filter the file during read to exlude any lines starting with |, as there are some very long md formatted tables in the docs (defines, modifier_types, effect, scope_link, trigger, gui_script, action_modding).

**Refreshing the docs:** Run `python tools/wiki_scraper.py` to re-download all wiki pages. Requires `beautifulsoup4` and `requests` (`pip install beautifulsoup4 requests`).

## Development Environment

- **Game files location**: `F:\SteamLibrary\steamapps\common\Europa Universalis V\game` — reference these when checking vanilla definitions, scripting syntax, or effect/trigger scopes.
- **No build step**: Paradox mods are plain text files loaded directly by the game engine. There is no compilation, linting tool, or test runner.
- **Testing**: Load the mod in-game via the EU V launcher. The game logs errors to `%USERPROFILE%\Documents\Paradox Interactive\Europa Universalis V\logs\`.
- **Submod setup**: EU5 only loads mods from the top-level `mod/` folder. After cloning (or adding a new submod), run `python tools/setup_junctions.py` to create Windows directory junctions from `mod/<submod name>/` → `submods/<folder>/`. Safe to re-run.

## Mod Structure

The mod uses two parallel content directories:

- `in_game/` — content that loads alongside vanilla (additive). Place new traits, events, decisions, etc. here.
- `main_menu/` — content that applies on the main menu screen only (e.g., UI graphics).

Paradox script files use the `.txt` extension and follow a Clausewitz scripting syntax (key-value pairs with `{}` blocks). Mirror the subfolder structure of the vanilla `game/` directory when adding new files.

### Key paths

| Path | Purpose |
|---|---|
| `in_game/common/traits/` | Character trait definitions |
| `in_game/common/biases/` | Opinion and antagonism modifier definitions |
| `in_game/common/advances/` | Tech advances (unlock subject types, reforms, privileges) |
| `in_game/common/subject_types/` | Subject type definitions |
| `in_game/common/on_action/cc_game_start.txt` | All on_game_start effects (keep in one file) |
| `main_menu/common/game_rules/` | Game rule definitions |
| `main_menu/common/modifier_type_definitions/` | Custom modifier type registrations (required for bureaucracies) |
| `main_menu/gfx/interface/icons/traits/` | Trait icon assets |
| `.metadata/metadata.json` | Mod descriptor (name, version, game compatibility, replace_paths) |

`replace_paths` in `metadata.json` controls which vanilla directories are completely replaced rather than merged. Add a path here only when the mod must prevent vanilla entries from loading.

## Scripting Conventions

EU V uses Clausewitz script. When writing traits, events, or decisions, follow the patterns found in the vanilla game files at `F:\SteamLibrary\steamapps\common\Europa Universalis V\game\`. Key scoping rules, trigger names, and effect names must match vanilla exactly — the engine gives no helpful errors for typos in script keys.

DO not get stuck looking for things in `game\common` directories when you should be looking in `game\in_game\common\` or `game\main_menu\common\` instead.

Localisation strings go in `in_game/localization/<language>/` as `.yml` files (UTF-8 BOM required by the engine). **All `.txt` script files also need UTF-8 BOM** — the engine loads them with a warning if missing. Run `python tools/fix_bom.py` to fix the whole mod at once; the git pre-commit hook does this automatically.

See [docs/scripting-gotchas.md](docs/scripting-gotchas.md) for verified patterns and a list of things that do NOT exist.

## Critical Gotchas (short list)

- **Modifier names**: always grep vanilla before using — many intuitive names don't exist. `global_trade_power` → `global_trade_center_power`. `fort_maintenance_modifier` → `fort_maintenance_cost`. `global_institution_spread_modifier` → doesn't exist; use `embrace_institution_cost_modifier`. No global dev cost modifier exists. See [docs/scripting-gotchas.md](docs/scripting-gotchas.md) for the full table.
- **Building modifiers**: `modifier = {}` is location-only. Country-level effects from buildings require `capital_country_modifier = {}` (only active in capital). No generic non-capital country modifier on buildings.
- **Localization BOM**: all `.yml` files need UTF-8 BOM or they're silently ignored. `.txt` script files also need it (loads with warning if missing). Run `python tools/fix_bom.py` to fix all at once.
- **`on_game_start` scope**: world scope, not country scope. Use `c:TAG = { }` or `every_country = { }`. Also: if multiple files each define `on_game_start = { effect = {} }` only the last one wins — keep all game-start effects in one file (`cc_game_start.txt`).
- **Culture group check**: `has_culture_group` expects culture scope, not country scope. Use `culture = { has_culture_group = culture_group:X }` from country scope. Dynamic comparison (`root.culture.culture_group` as a dot-chain) is parsed as an event target link and fails — use `only_overlord_or_kindred_culture = yes` to enforce the restriction instead.
- **`has_custom_tag`** does NOT exist as a trigger. Trait `custom_tags = {}` values cannot be queried from character triggers.
- **Illustration tags**: valid values are `interior`, `exterior`, `military`, `army`, `economy`, `bank`, `burghers`, `fire`, `angry`, `armed`, `happy`, `professional`, `regular`, `ages`, `interior_peasant`. `combat` is NOT valid.
- **Advance cross-age `requires`**: `requires = other_advance` breaks if the required advance is in a different age. Use `potential = { has_advance = X }` + `allow = { has_advance = X }` instead.
- **Bureaucracy `_impact_modifier` types**: each custom bureaucracy needs a `{name}_impact_modifier` entry in `main_menu/common/modifier_type_definitions/`. Pattern: `percent=yes  game_data={ category=country }`. See `game/main_menu/common/modifier_type_definitions/01_byz.txt`.
- **`declare_war_with_cb` target**: must use `target = scope:X` with the `scope:` prefix, not bare `target = X`.
- **Opinion modifiers**: `add_opinion_modifier` does NOT exist. Use `add_opinion = { target = X modifier = Y }`. The modifier must be defined in `common/biases/` first — "Unknown bias type" means it's missing. No `years` param; duration is set in the bias definition.
- **Event IDs must be pure integers** after the namespace dot. `cc_foo.3a` is INVALID — use `cc_foo.30`, `cc_foo.31` etc. Duplicate IDs in a file: engine uses the last definition silently.
- **War triggers**: `has_war_with` → `is_at_war_with`. `is_at_war` → `at_war`.
- **Sub-continent / area checks**: `is_in_sub_continent` doesn't exist. Use `capital.sub_continent = sub_continent:X` and `capital.area = area:X` (dot-chain from country scope, no block).
- **`has_estate` is character-scope only**. In country scope use `any_estate = { estate_type = estate_type:nobles_estate }`.
- **No `count_cabinet_characters` or `all_cabinet_character`** triggers. Use multiple `any_cabinet_character` blocks. `every_cabinet_character` exists (effect iteration only).
- **`count_subjects`** doesn't exist as an iterator. Use `num_subjects >= N` or `any_subject = { ... }`.
- **Conditional effects inside option blocks**: use `if = { limit = { ... } effect }`, NOT `trigger = { ... }`.
- **`any_owned_province`** doesn't exist. Use `any_owned_location`.
- **Script value names**: sizes are `weak/mild/severe/extreme/ultimate`; suffixes are `_plus/_minus` and `_bonus/_penalty`. E.g. `prestige_severe_bonus`, `liberty_desire_mild_plus`.
- **Per-location income**: no scripted value. Use `scope:location.development` as a proxy.
- **See [docs/scripting-gotchas.md](docs/scripting-gotchas.md)** for detailed patterns, estate gold syntax, building rank flags, stacking modifiers, and the full valid/invalid name table.
