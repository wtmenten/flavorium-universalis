# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Flavorium Universalis** is a Europa Universalis V mod (v0.1, compatible with EU V 1.2.*) focused on enhancing cabinet member gameplay with new traits and dynamic events.

EU V Modding Documentation: https://eu5.paradoxwikis.com/Modding

**Documentation references (check in this order):**
1. [docs/eu5-modding-reference.md](docs/eu5-modding-reference.md) — Internal summarized modding reference
2. [docs/offline-wiki/](docs/offline-wiki/) — Offline copy of EU5 Paradox Wiki modding pages (40 pages, ~1.5MB)
3. [tools/wiki_search.py](tools/wiki_search.py) — Fast search tool for offline docs

**Shipping a release?** Follow [docs/release-process.md](docs/release-process.md) — the full checklist for version bump, change note, workshop/web-docs description generators (which read fixed file lists you must register new content in), and upload. Do not hand-edit `*_upload.*` files, `docs/*.html`, or content inside `<!-- GEN:… -->` markers; rerun the generators instead.

## Copywriting & web design conventions

All customer-facing copy (workshop descriptions, dev diaries, change notes, in-game loc that surfaces in those, web docs) must read as **plain, direct documentation**, not marketing. Avoid these "LLM-ism" tells:

- **No em-dashes.** Use a period, semicolon, comma, colon, parentheses, or recast the sentence. For `[b]Label[/b] — description` list items use a **colon** (`[b]Label:[/b] description`). This applies to source files *and* to any generator code that emits separators — fix it at the generator (e.g. `generate_workshop.py` builds list lines with `: `, not ` — `), not just the output.
- **No flowery / marketing language.** Cut metaphors and hyperbole ("weaving a web... spider envious", "memorable characters", "read a room in three languages", "learns to outlive its own ending"). State the mechanic plainly. Rich language earns emphasis only when used sparingly.
- **Trim other tells:** rule-of-three triplets, "isn't just X, it's Y" / "no longer just", "at its core / at the heart of", "whether you're... or...", hedging ("unfortunately", "a bit", "subject to change"), and bold-for-emphasis on ordinary text (bold a mechanic name once, not every clause).
- **Web design:** do **not** use the colored `border-left` (or `border-top`) accent-stripe card pattern. Cards use a uniform `1px var(--card-border)` border with the accent expressed as a small-caps colored **eyebrow** above the title plus a short colored **underline rule** (`::after`) beneath it. All site CSS lives in the `TEMPLATE`/`EXTRA_CSS` of `tools/generate_index.py` and `tools/generate_dev_diaries.py`.
- **After editing any source that feeds a generator**, rerun the generators and `grep -c "—"` the regenerated `*_upload.*` and `docs/*.html` to confirm em-dashes introduced via loc/generator code didn't leak back in.
- **Out of scope unless asked:** `README.md` (developer guide) and the historical `assets/workshop/change-notes.bbcode` archive.

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

## Mod variable reference search

**Use `tools/var_refs.py` to find where any scripted variable is read, written, or checked** across the whole mod. Use this before adding new variable logic to see the existing access pattern, or when debugging a `Variable not of the 'value' scope type` / `returned an invalid object` error.

```
# Show all references to a specific variable:
python tools/var_refs.py cc_bond_initialized

# Substring match — all vars containing a prefix:
python tools/var_refs.py cc_bond_cul

# Just list all variable names and reference counts:
python tools/var_refs.py --list

# Filter to specific operation types (set/change/clamp/has/remove/map_add/map_ref/var):
python tools/var_refs.py cc_bond --op set,remove

# Group results by file instead of by variable:
python tools/var_refs.py cc_bond --group file

# Search a single file only:
python tools/var_refs.py --file in_game/events/cc_bond_chain_d.txt
```

Output format: `file:line  op  event_or_block > section[option_name]`

## Art assets

**Use `tools/make_dds.py` to convert PNG art into DDS.** Never hand-export DDS from an image
editor: the engine needs a full mipmap chain down to 1x1, and a file without one logs
`Streamed texture has no mipmaps` and streams the full surface every frame. The tool builds the
chain and writes a header byte-compatible with vanilla.

```
python tools/make_dds.py --list-slots                                  # size/format/path per art slot
python tools/make_dds.py hero.png --slot trait --key war_hawk          # convert and place in the mod
python tools/make_dds.py art/*.png --slot generic-action               # batch; filename becomes the key
python tools/make_dds.py x.png --slot situation-icon --key k --submod rhomania
python tools/make_dds.py in.png --size 1080x440 --format BC1 -o out.dds # ad-hoc, no mod placement
python tools/make_dds.py --verify                                      # audit every DDS in the mod
python tools/make_dds.py --verify --fix-mips                           # re-encode the broken ones
```

`--slot` sets size, compression, fit and destination folder in one go, so prefer it over
`--size`/`--format`. Downsampling is linear-light with premultiplied alpha, which is what keeps
soft-edged icons from picking up a dark fringe. `--verify` exits non-zero, so it works in a hook.

[docs/art-asset-gaps.md](docs/art-asset-gaps.md) is the standing inventory: how the engine
resolves each art path (there is no `.gfx` declaration step, only naming convention), the
resolution and format table, and every mod key currently resolving to art that does not exist.

**Use `tools/dds_to_png.py` to look at DDS art.** The inverse of `make_dds.py`, and a viewing
tool only: its output is decoded from BC blocks, so never feed a PNG it wrote back in as a
source. Writes to `tools/dds_preview/` by default (gitignored).

```
python tools/dds_to_png.py icon.dds -o out/icon.png            # one file, named target
python tools/dds_to_png.py main_menu/gfx -r -d out/            # a whole tree
python tools/dds_to_png.py trait.dds -d out/ --background checker --scale 3   # see an icon
python tools/dds_to_png.py bg.dds -d out/ --mip 3              # what the engine streams
python tools/dds_to_png.py main_menu/gfx -r --info             # sizes, formats, mip counts
```

It reads vanilla art too. Point it at the game install and it mirrors the last two folders of
the source path under the output dir.

## Localization translation

**Use `tools/translate.py` to machine-translate localization.** Never hand-write translated `.yml` files or edit them for content; re-run the tool instead.

**SUPPORTED LANGUAGES ARE ENGLISH, FRENCH, GERMAN AND SPANISH. Nothing else.** `translate.py` will happily target all ten folders EU5 ships, and without `-l` it does exactly that, creating seven language folders this project does not maintain and cannot proofread. **Always pass `-l french,german,spanish`.**

```
python tools/translate.py -m -l french,german,spanish   # main mod
python tools/translate.py -s -l french,german,spanish   # main mod + every submod
python tools/translate.py -wp -cn -l french,german,spanish   # Steam page title/description and change notes
```

- **Backends** are set in `tools/config.toml`: `local` (OpenAI-compatible server, the default, no API key), `deepl`, or `gemini-3-flash`. The `local_*` keys configure the server; `local_disable_thinking = true` is required for reasoning models or throughput drops ~8x. Check the configured `local_model` is actually loaded (`curl http://127.0.0.1:9292/v1/models`) before starting a long run.
- **No Italian.** EU5 ships no `italian` localization folder, so `l_italian` never loads. It is not one of the ten valid targets, and it is not one of our three either.
- **Runs are incremental.** Per-key hashes in `tools/dependencies/.translate_hashes.json` mean re-runs only touch changed/missing keys. To force specific strings to be redone, delete their lines from the target `.yml` and re-run: keys missing from a target are always re-translated.
- **Markup is validated, not trusted.** Translations that drop a `[scope.Function]`/`$VAR$`/`@icon!`/`#colour…#!` token, *or invent one the source lacks*, are retried then fall back to English. Invented tokens are the dangerous case: a model will turn "they" into `[minister.GetSheHe]` in a key where that scope doesn't exist, which errors in-game.
- **Protecting text:** `# NO-TRANSLATE` on a source line, `# NO-TRANSLATE BELOW`/`# NO-TRANSLATE END` around a source block, or `# LOCK` on a line in a *target* file to keep a hand-corrected translation from being overwritten.

## Development Environment

- **Game files location**: the EU5 install varies per workstation, so never hardcode it. Run `python tools/game_paths.py` to print the resolved path, or use `from game_paths import game_root` in a tool. The resolver checks `EU5_GAME_DIR`, then every Steam library in `libraryfolders.vdf`, then common install paths, and only accepts directories that exist. Reference these files when checking vanilla definitions, scripting syntax, or effect/trigger scopes.
- **No build step**: Paradox mods are plain text files loaded directly by the game engine. There is no compilation, linting tool, or test runner.
- **Testing**: Load the mod in-game via the EU V launcher. The game logs errors to `%USERPROFILE%\Documents\Paradox Interactive\Europa Universalis V\logs\`.
- **Submod setup**: EU5 only loads mods from the top-level `mod/` folder. After cloning (or adding a new submod), run `python tools/setup_junctions.py` to create Windows directory junctions from `mod/<mod name>/` into the repo. Safe to re-run. It finds the mod folder by checking `--mod-dir`, then `EU5_MOD_DIR`, then the repo's parent if that parent is named `mod`, and finally `<Documents>/Paradox Interactive/Europa Universalis V/mod` (Documents read from the registry, so a OneDrive-redirected Documents resolves correctly), creating it if absent. When the repo is not itself inside `mod/`, the main mod gets a junction too.

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

EU V uses Clausewitz script. When writing traits, events, or decisions, follow the patterns found in the vanilla game files (see **Game files location** above for how to resolve the path). Key scoping rules, trigger names, and effect names must match vanilla exactly — the engine gives no helpful errors for typos in script keys.

DO not get stuck looking for things in `game\common` directories when you should be looking in `game\in_game\common\` or `game\main_menu\common\` instead.

Localisation strings go in `in_game/localization/<language>/` as `.yml` files (UTF-8 BOM required by the engine). **All `.txt` script files also need UTF-8 BOM** — the engine loads them with a warning if missing. Run `python tools/fix_bom.py` to fix the whole mod at once; the git pre-commit hook does this automatically.

See [docs/scripting-gotchas.md](docs/scripting-gotchas.md) for verified patterns and a list of things that do NOT exist.

## Critical Gotchas (short list)

- **Overriding a vanilla database entry requires a `REPLACE:` directive, not load order.** Declaring a bare `key = { ... }` for a key vanilla already defines does *not* win. The engine refuses it and keeps vanilla, logging `Duplicated key <name> will not be created from file: …` while the mod file looks entirely correct. The supported directives, prefixed onto the key (`REPLACE:my_key = { … }`): `REPLACE:` (entry must exist), `REPLACE_OR_CREATE:`, `TRY_REPLACE:` (skip if absent), `INJECT:` (merge extra keys into an existing entry), `TRY_INJECT:`. **Prefer `INJECT:` whenever the change is purely additive** — it merges at the entry's top level and avoids duplicating vanilla content, but it cannot reach inside an existing nested block (e.g. altering a `scale` inside a `positive_modifier`) and will happily create a second block of a key the entry already has. Reach for `REPLACE:` only when a nested rewrite is genuinely needed.
- **No vanilla file overrides**, with one deliberate, authorised exception (below). The main mod and the `balance`, `disease-hotfix` and `graphical-ui-fixes` submods shadow no vanilla file, and that should stay true.
  - **Authorised exception: `submods/rhomania/in_game/common/bureaucracies/zzz_cc_byz_vanilla_overrides.txt`.** Redefines all eleven Byzantine bureaucracies to add Taxis/Dynatoi drift that scales with funding, a small crown/noble power shift, and the `on_maintenance_changed` hook. Vanilla text is otherwise unmodified and the header lists every edit, so it re-syncs by diffing against `byz.txt`. **Re-check on every EU5 update**, since a patch touching `byz.txt` diverges silently.
- **The engine already scales bureaucracy boons *and* maluses by entrenchment.** `game_concept_bureaucracy_desc` states it ("increasing the power of both positive and negative modifiers"), and the `Entrenchment +N%` footer in a bureaucracy tooltip is the engine's own `ADDITIONAL_MODIFIER_ENTRENCHMENT`. Do **not** multiply a bureaucracy's modifiers by `scope:entrenchment`: it squares the scaling, and in any case **`scope:entrenchment` does not exist in these blocks**. The bureaucracies `readme.txt` lists it next to `scope:maintenance`, but no vanilla bureaucracy uses it anywhere and the engine logs `Undefined event target 'entrenchment'` plus `Got value of type 'none'` for the enclosing `scale`, which then evaluates to none and stops the modifier applying **at all**. This repo shipped that factor on 28 negative scales and the maluses were silently not firing. `scope:maintenance` *is* real (vanilla uses it 22 times in `byz.txt`). To soften a new office, change the modifier **values**, not the scale. IO vote weight in particular does *not* need one: set `uses_parliament_for_law_votes = yes` on the IO's parliament type and vanilla `policy_vote` will read vote weight from each member's `special_status_power`, which can be a full script value in country scope (`value = country_tax_base`, etc). Both `cc_bop_coalition` and `cc_bop_concert` use this. Every voting status also needs a registered `<status>_can_participate_in_parliament` (and paired `<status>_agenda_impact`) modifier type in `main_menu/common/modifier_type_definitions/`, listed in the parliament type's `modifier` block. Note the flag also makes vanilla block law debates while a parliament issue is ongoing and end/recalculate the parliament when a law vote resolves.
- **on_action merge pattern**: redefining a hardcoded on_action (e.g. `on_winning_war`, `on_join_war`) with a direct `effect = {}` *overrides* vanilla and clobbers its logic. Instead chain a custom on_action via `on_winning_war = { on_actions = { my_custom } }` — the `on_actions` sub-list merges, leaving vanilla's effect intact. See `cc_bop_war_outcome.txt` and `cc_bond_pulse.txt`.
- **Modifier names**: always grep vanilla before using — many intuitive names don't exist. `global_trade_power` → `global_trade_center_power`. `fort_maintenance_modifier` *and* `fort_maintenance_cost` → `fort_maintenance_efficiency` (renamed in 1.3, **and the sign flips**: efficiency up means cheaper). Same family: `army_maintenance_efficiency`, `navy_maintenance_efficiency`. `global_institution_spread_modifier` → doesn't exist; use `embrace_institution_cost_modifier`. No global dev cost modifier exists, and **no forcelimit modifier of any kind exists**. See [docs/scripting-gotchas.md](docs/scripting-gotchas.md) for the full table.
- **Building modifiers**: `modifier = {}` is location-only. Country-level effects from buildings require `capital_country_modifier = {}` (only active in capital). No generic non-capital country modifier on buildings.
- **Localization BOM**: all `.yml` files need UTF-8 BOM or they're silently ignored. `.txt` script files also need it (loads with warning if missing). Run `python tools/fix_bom.py` to fix all at once.
- **`on_game_start` scope**: world scope, not country scope. Use `c:TAG = { }` or `every_country = { }`. Also: if multiple files each define `on_game_start = { effect = {} }` only the last one wins — keep all game-start effects in one file (`cc_game_start.txt`).
- **Culture group check**: `has_culture_group` expects culture scope, not country scope. Use `culture = { has_culture_group = culture_group:X }` from country scope. Dynamic comparison (`root.culture.culture_group` as a dot-chain) is parsed as an event target link and fails — use `only_overlord_or_kindred_culture = yes` to enforce the restriction instead.
- **`count = N` on an `any_` iterator means EXACTLY N**, not "at least N", and there is no at-least form. `any_character = { count = 2  X = yes }` stops passing as soon as a third character qualifies. Vanilla depends on the exactness (`count = 0` for "there are none", `count = all` for "all of them"). For a threshold, count in a script value (`every_x = { limit = {…} add = 1 }`) and compare; see `cc_xp_values.txt` section 9. This shipped four dead triggers in this repo before anyone checked.
- **A GUI button cannot open an interaction's `select_trigger` picker.** The engine evaluates the action against the parameters the button supplies, so any `target_flag` the button does not supply leaves the action unperformable: the button is permanently disabled and its tooltip shows only the target-independent parts (effect text, price). It looks identical to a failing `allow` and is not one. Every GUI-invoked interaction in vanilla has exactly one distinct target flag and the GUI always supplies it via `parameter = { parameter_name = "recipient" parameter_value = "[Character.MakeScope]" }`. An action whose target is on no row must declare **no** `select_trigger` and offer candidates as event options (`ordered_x` + `check_range_bounds = no`); see `events/cc_xp_choice_events.txt`. This killed ten panel buttons in this mod.
- **A `character_interaction` must have a `select_trigger`** (all ~60 vanilla ones do, no exceptions). One with none still has the engine ask for `recipient`, spamming `interaction_target.cpp:877 Asking for a flag that's not in the interaction target chooser specified` every frame the panel is open, and the button stays dead. For a target-free action use `common/generic_actions/` with `type = owncountry` (replaces `message` + `on_own_nation`); vanilla's `train_general` and `hire_advisor` are exactly this, driven from panel buttons with no parameter. When converting, drop the message-feed loc suffixes (`_desc_specific`, `_act`, `_past`, `_act_past`, `_concept`) and grep the loc for `SCOPE.sCharacter('target')` — a scope reference to a flag the action no longer declares is an error, not a blank.
- **`none_available_msg_key` loc values must begin with `@trigger_no!`** or the engine rejects them (`interaction_target.cpp:1407 ... doesn't start with trigger_no icon`). Vanilla aliases `$no_valid_provinces$` / `$no_valid_characters$`, which carry the icon.
- **A `select_trigger` with no *enabled* candidate disables the interaction on its own**, outside `allow`, and says nothing unless `none_available_msg_key` names a loc string. Applies where a selector is actually reached, i.e. the character interaction menu.
- **Situation panel art resolves by naming convention** (`main_menu/gfx/interface/illustrations/situation/<key>.dds`) through `GetSituationIllustration` in the default `situation_panel_image` block. Overriding that block with a gradient removes the only call site and the art never appears.
- **`has_custom_tag`** does NOT exist as a trigger. Trait `custom_tags = {}` values cannot be queried from character triggers.
- **Illustration tags**: the complete valid list is `interior`, `exterior`, `regular`, `angry`, `professional`, `happy`, `armed`, `trading`, `military`, `location`, `economy`, `bank`, `army`, `ages`, `institution`, `society`, `renaissance`, `goods` (eighteen; harvested from the `N = <tag>` entries in `loading_screen/gfx/illustrations/database/*.txt`, which is the authoritative source). `combat`, `fire`, `burghers`, `interior_peasant` and **`peasant`** are NOT valid. `peasant` was previously listed here as valid and is not: it cost five `unknown illustration tag` errors before anyone read the database rather than the note.
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
