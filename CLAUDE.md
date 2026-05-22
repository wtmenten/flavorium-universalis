# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Cabinets and Choices** is a Europa Universalis V mod (v0.1, compatible with EU V 1.2.*) focused on enhancing cabinet member gameplay with new traits and dynamic events.

EU V Modding Documentation: https://eu5.paradoxwikis.com/Modding

look for documentation reference excerpts in the website summarized docs first.
[docs/eu5-modding-reference.md](Internal summarized modding reference)

# lookup tools

use this powershell command from the game/in_game/common dir or something similar in grep to search for type values in vanilla files quickly:
`Get-ChildItem -Recurse -File | Select-String -Pattern "YOUR_TYPE_NAME_HERE:\w+" | ForEach-Object { $_.Matches.Value } | Select-Object -Unique`
`grep -roh "YOUR_TYPE_NAME_HERE:[a-z_]* [><=!]* *[0-9-]*" "f:/SteamLibrary/steamapps/common/Europa Universalis V/game/in_game/common" 2>/dev/null | sort -u`
works for types like: societal_value,government_type,religion_group,sub_continent,government_reform,policy,estate_privilege and others.
DO NOT do this from the root `/game` directory it will take a very long time.

## Development Environment

- **Game files location**: `F:\SteamLibrary\steamapps\common\Europa Universalis V\game` — reference these when checking vanilla definitions, scripting syntax, or effect/trigger scopes.
- **No build step**: Paradox mods are plain text files loaded directly by the game engine. There is no compilation, linting tool, or test runner.
- **Testing**: Load the mod in-game via the EU V launcher. The game logs errors to `%USERPROFILE%\Documents\Paradox Interactive\Europa Universalis V\logs\`.

## Mod Structure

The mod uses two parallel content directories:

- `in_game/` — content that loads alongside vanilla (additive). Place new traits, events, decisions, etc. here.
- `main_menu/` — content that applies on the main menu screen only (e.g., UI graphics).

Paradox script files use the `.txt` extension and follow a Clausewitz scripting syntax (key-value pairs with `{}` blocks). Mirror the subfolder structure of the vanilla `game/` directory when adding new files.

### Key paths

| Path | Purpose |
|---|---|
| `in_game/common/traits/` | Character trait definitions |
| `main_menu/gfx/interface/icons/traits/` | Trait icon assets |
| `.metadata/metadata.json` | Mod descriptor (name, version, game compatibility, replace_paths) |

`replace_paths` in `metadata.json` controls which vanilla directories are completely replaced rather than merged. Add a path here only when the mod must prevent vanilla entries from loading.

## Scripting Conventions

EU V uses Clausewitz script. When writing traits, events, or decisions, follow the patterns found in the vanilla game files at `F:\SteamLibrary\steamapps\common\Europa Universalis V\game\`. Key scoping rules, trigger names, and effect names must match vanilla exactly — the engine gives no helpful errors for typos in script keys.

DO not get stuck looking for things in `game\common` directories when you should be looking in `game\in_game\common\` or `game\main_menu\common\` instead.

Localisation strings go in `in_game/localization/<language>/` as `.yml` files (UTF-8 BOM required by the engine).

See [docs/scripting-gotchas.md](docs/scripting-gotchas.md) for verified patterns and a list of things that do NOT exist.

## Critical Gotchas (short list)

- **Modifier names**: always grep vanilla before using. Many intuitive names don't exist. `navy_tradition` → `monthly_navy_tradition`. `global_estate_satisfaction_equilibrium` → `global_estate_target_satisfaction`. `local_navy_tradition_from_battles` → doesn't exist. `global_trade_power` → `global_trade_center_power`. `fort_maintenance_modifier` → `fort_maintenance_cost`. `missionary_strength` → `global_pop_conversion_speed_modifier`. No global dev cost modifier exists.
- **Building modifiers**: `modifier = {}` is location-only. Country-level effects from buildings require `capital_country_modifier = {}` (only active in capital). No generic non-capital country modifier on buildings.
- **Location rank syntax differs by context**: in building `.txt` files use `city = yes` / `megalopolis = yes` flags. In events/triggers use `location_rank = location_rank:city`.
- **Localization BOM**: all `.yml` files need UTF-8 BOM or they're silently ignored. Write via Python `f.write(b'\xef\xbb\xbf')`.
- **Estate gold**: two effects — `add_gold_to_estate = { estate_type = ... value = ... }` (from country scope) and `estate_add_gold = { value = ... }` (from estate scope). Check `pirate_events.txt:373` for examples.
- **`on_game_start` scope**: world scope, not country scope. Must use `c:TAG = { }` or `every_country = { }` to reach countries.
- **`num_naval_governors`**: granted by advances and government reforms (and estate privilege `country_modifier` blocks — verify in-game).
- **Per-location income**: no scripted value exists. Use `scope:location.development` as a proxy for location wealth.
- **Estate building cost**: `estate_construct_building` has no gold cost — it's goods-only. Proxy "building cost" with `monthly_income_trade_and_tax * N` or `estate_tax_base * N`.
- **Stacking modifiers**: use N separately named modifiers (`cc_foo_1` … `cc_foo_5`) to cap stacks, since each modifier name can only stack via `mode = add_and_extend`; checking `NOT { has_country_modifier = cc_foo_5 }` caps the chain.
- **Event IDs must be pure integers** after the namespace dot. `cc_foo.3a` and `cc_foo.3b` are INVALID — the engine rejects non-integer IDs silently.
- **Opinion effects**: `add_opinion_modifier` does NOT exist. Use `add_opinion = { target = X modifier = Y }`. No `years` param — duration is set in the opinion modifier definition.
- **War triggers**: `has_war_with` → `is_at_war_with`. `is_at_war` → `at_war`. Both `at_war_with` and `is_at_war_with` exist.
- **Sub-continent check**: `is_in_sub_continent` does NOT exist. Use dot-chain: `capital.sub_continent = sub_continent:western_europe` (from country scope).
- **Area check on capital**: `capital = { is_in_area = area:xxx }` is INVALID. Use `capital.area = area:xxx` (dot-chain from country scope).
- **Culture group check from country scope**: `has_culture_group = culture_group:sinitic` is valid in country scope directly. For culture scope: `culture = { has_culture_group = X }`.
- **`add_cultural_tradition` / `add_cultural_influence`** need culture scope — call from country scope as `culture = { add_cultural_tradition = X }`.
- **`has_estate` is character-scope only** (checks estate affiliation). In country scope use `any_estate = { estate_type = estate_type:nobles_estate }` to check if an estate exists.
- **No `count_cabinet_characters` or `all_cabinet_character`** triggers. Use multiple `any_cabinet_character` blocks to approximate "at least N with trait X". `every_cabinet_character` exists (effect iteration only).
- **`count_subjects`** doesn't exist as an iterator. Use `num_subjects >= N` (total count, no type filter) or `any_subject = { ... }` (at least one).
- **Conditional effects inside option blocks**: use `if = { limit = { ... } effect }`, NOT `trigger = { ... }` (that's a trigger keyword, not an effect).
- **`subtract` in weight_multiplier modifiers**: use `add = -N` instead.
- **`any_owned_province`** doesn't exist. Use `any_owned_location`.
- **Script value names**: `prestige_strong_bonus` → `prestige_severe_bonus`. `liberty_desire_mild_increase` → `liberty_desire_mild_plus`. Pattern: `_plus` / `_minus` suffixes, sizes: weak/mild/severe/extreme/ultimate.
- **See [docs/scripting-gotchas.md](docs/scripting-gotchas.md)** for the full reference table of valid/invalid names.
