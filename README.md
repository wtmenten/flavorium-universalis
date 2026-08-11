# Flavorium Universalis — Developer Guide

**Version:** 0.2.0 (dev: 0.3.0-pre) | **Game compatibility:** EU5 1.2.* | **Multiplayer:** synchronized

A Europa Universalis V mod that expands cabinet gameplay with a dynamic minister trait system, synergy events, legacy mechanics, custom subject types, era-specific advances, subject bond tracking, court rivalry/cabal, cabinet duties, war council, estate factions, stepping stone trait chains, and colonial posting. All content is additive (no `replace_paths`).

---

## Repo layout

```
in_game/          content loaded alongside vanilla (additive)
main_menu/        content loaded on the main-menu screen only
submods/          optional submods, each with their own .metadata/ and in_game/
tools/            Python scripts for modding workflow
docs/             reference documentation
loading_screen/   loading screen graphics
.metadata/        mod descriptor (metadata.json)
```

Mirror vanilla's subfolder structure when adding new files. Game files are at `F:\SteamLibrary\steamapps\common\Europa Universalis V\game`.

---

## Content inventory

### Traits — `in_game/common/traits/`

| File | Category | Contents |
|------|----------|----------|
| `cc_cabinet_traits.txt` | Core cabinet traits | ~30 traits: Tier 1 (simple), Tier 2 (kiss-curse), Tier 3 (attribute-scaled triads) |
| `cc_age_traits.txt` | Age-specific traits | ~50 traits granted through age events (Renaissance → Revolutions) + 6 feudal era traits |
| `cc_conditional_traits.txt` | Conditionally spawned | 115+ traits: dev-gated (Family A), societal-value axes (Family B, 17 axes), regional/religious (C), military specialist (D), parliamentary (E), action-forged (F), legendary specials |
| `cc_negative_traits.txt` | Underperformance traits | 10 removable negative traits with rehabilitation paths |
| `cc_progression_traits.txt` | Stepping stone traits | 6 Tier 0 entry traits + chain endpoints: `fumbling_reformist`, `tentative_envoy`, `green_adjutant`, `clumsy_accountant`, and advanced chain endpoints (Pillar 12) |
| `cc_estate_faction_traits.txt` | Estate faction traits | 7 Family G traits (`category = health`) — estate-affiliation overlay: `noble_champion_of_court`, `merchant_of_the_crown`, `court_prelate`, and 4 others (Pillar 2) |

Icons go in `main_menu/gfx/interface/icons/traits/`.

### Events — `in_game/events/`

| File | Namespace | ~Count | Purpose |
|------|-----------|--------|---------|
| `cc_cabinet_events.txt` | `cc_cabinet` | 18 | Ruler–minister counsel, estate relations, diplomatic situations, provincial affairs |
| `cc_trait_events.txt` | `cc_traits` | 18 | New age trait acquisition, ruler teaching, peer learning |
| `cc_trait_dispatch_events.txt` | `cc_trait_dispatch` | 1 | Hidden monthly dispatcher — routes per-minister trait assignment through a single event to avoid pulse collision |
| `cc_conditional_trait_events.txt` | `cc_cond` | 15 | Conditional trait spawning based on realm state |
| `cc_synergy_events.txt` | `cc_synergy` | 26 | Trait synergy pairs — bonus modifiers when ministers share matching trait families |
| `cc_negative_trait_events.txt` | `cc_neg` | 17 | Underperformance events (grant negative traits) + rehabilitation checks (remove them) |
| `cc_wealth_events.txt` | `cc_wealth` | 10 | Minister enrichment, wealth hoarding stacks (inflation / corruption) |
| `cc_dual_synergy_events.txt` | `cc_dual` | 10 | Cabinet × religious_figure dual-role synergies |
| `cc_intl_synergy_events.txt` | `cc_intl` | 12 | Cross-country minister interactions with neighbors |
| `cc_feudal_events.txt` | `cc_feudal` | 8 | Feudal age court events |
| `cc_legacy_events.txt` | `cc_legacy` | 3 | Senior minister retirement and legacy passing |
| `cc_legend_events.txt` | `cc_legend` | 6 | Legendary trait quest chains |
| `cc_subject_events.txt` | — | — | Subject drawback events (governor ambitions, tax farm revolts, march raids, etc.) |
| `cc_bond_*.txt` (15 files) | `cc_bonds` | 98+ | Subject bond system — per-type chain events, monitor, status reveals, AoR payoffs |
| `cc_rivalry_events.txt` | `cc_rival` | 3 | Court rivalry escalation: complaint → letter unsealed → faction hardens |
| `cc_cabal_events.txt` | `cc_cabal` | 2 | Cabinet alliance formation: alliance forms → joint reform proposal |
| `cc_war_council_events.txt` | `cc_wc` | 7 | War council: active-war events, post-war reform proposals, outdated general retirement |
| `cc_estate_faction_events.txt` | `cc_fac` | 3 | Estate faction events when one estate dominates the cabinet |
| `cc_progression_events.txt` | `cc_prog` | 19 | Stepping stone trait progression chains (Paths A/C/D/F/E) |
| `cc_colonial_events.txt` | `cc_colonial` | 6 | Colonial divan: charter company events + decolonization crisis chain |
| `cc_colonial_posting_events.txt` | `cc_posting` | 4 | Colonial posting duty events: dispatch, corruption, native uprising, fever |
| `cc_hyw_events.txt` | `cc_hyw` | 11 | Hundred Years War flavor — FRA/ENG war outcomes, observer reactions, vassal defection pressure |
| `cc_personality_events.txt` | `cc_personality` | 18 | Dynamic AI personality inflection events — key historical turning points |
| `cc_hus_events.txt` | `cc_hus` | 1 | Hussite Wars — papal loan event (One Small Loan) |
| `cc_invasion_mexico.txt` | `cc_invasion_mexico` | 28 | Mexican Conquest situation — expedition decisions, Mesoamerican reactions, confederation events, conquest resolution |

### Cabinet Duties (Actions) — `in_game/common/cabinet_actions/`

7 assignable duty types. When a minister is on a duty, related event systems fire at boosted rates and the minister provides a country modifier while assigned.

| File | Duty | Ability | Effect |
|------|------|---------|--------|
| `cc_duty_war_council.txt` | War Council | mil | +discipline, +land morale recovery; boosts `cc_wc.*` events while at war |
| `cc_duty_domestic_reform.txt` | Domestic Reform | adm | -stability cost; 2× stepping stone progression rate |
| `cc_duty_diplomatic_mission.txt` | Diplomatic Mission | dip | diplomatic effect; boosts diplomatic interaction events |
| `cc_duty_scholarly_inquiry.txt` | Scholarly Inquiry | adm | research effect; boosts Scholar's Court events |
| `cc_duty_religious_oversight.txt` | Religious Oversight | adm | religious effect; boosts confessional tension events |
| `cc_duty_colonial_posting.txt` | Colonial Posting | dip | posts minister overseas; drives `cc_posting.*` events |
| `cc_duty_free_hands.txt` | Free Hands | adm | default duty; all idle cabinet events fire at baseline rate; multiple ministers may share this duty |

### Cabinet Composition Auto-Modifiers — `in_game/common/auto_modifiers/cc_cabinet_composition.txt`

9 aggregate modifiers that activate live when the cabinet matches a composition profile (`requires_real = yes`). They use `potential_trigger` so they activate and deactivate as traits change.

| Modifier | Trigger | Effect summary |
|----------|---------|----------------|
| `warlord_court` | 2+ military specialist traits | +discipline, +morale recovery, -diplomatic rep |
| `merchant_republic_spirit` | 2+ commercial/fiscal traits | +trade, -stability cost |
| `enlightened_court` | 2+ scholarly/empiricist traits | +research, +literacy |
| `court_paralysis` | conflicting ideological pair present | -stability, -legislative efficiency |
| `entrenched_court` | 3+ conservative/traditional traits | -reform progress, +stability |
| `balanced_court` | no single trait category dominant | small bonuses across all areas |
| `nobles_court_captured` | 2+ noble-aligned Family G traits | +prestige, +noble estate power |
| `burghers_court_captured` | 2+ burgher-aligned Family G traits | +trade, +burgher estate power |
| `clergy_court_captured` | 2+ clergy-aligned Family G traits | +religious influence, +clergy estate power |

### Situations — `in_game/common/situations/`

| File | Contents |
|------|----------|
| `cc_invasion_mexico.txt` | **Invasion of Mexico** — fires when a colonial or foreign power establishes a foothold in Mesoamerica (or adjacent Caribbean/Central America by 1540). Lasts until all native Mesoamerican powers are subjugated or 1600 is reached. |

### International Organizations — `in_game/common/international_organizations/`

| File | Contents |
|------|----------|
| `cc_mesoamerican_confederation.txt` | **Mesoamerican Confederation** — defensive alliance IO for native Mesoamerican powers during the Invasion of Mexico situation. Leader-based, unique, military-access sharing. Created via events or the `ccim_call_confederation` generic action; never from the IO screen directly. |

### Casus Belli — `in_game/common/casus_belli/`

| File | Contents |
|------|----------|
| `cc_invasion_mexico.txt` | Expedition CBs for colonial/foreign powers pressing territorial claims against Mesoamerican states during the Invasion of Mexico situation |

### Generic Actions — `in_game/common/generic_actions/`

| File | Contents |
|------|----------|
| `cc_invasion_mexico.txt` | Actions for the Mexico situation: `ccim_call_confederation` (Mesoamerican leader), `ccim_press_terms`, `ccim_offer_settlement` (colonial powers) |

### Building Types — `in_game/common/building_types/`

| File | Contents |
|------|----------|
| `cc_foreign_buildings.txt` | `cc_merchant_trade_post` — foreign-owned building placed in a subject's market center by bond chain B events (bond.113). Grants stronger power projection. Removed after 20–40 years by bond.115. Cannot be built from the UI. |
| `cc_library_override.txt` | `REPLACE_OR_CREATE:library` — overrides vanilla library to grant per-estate literacy (nobles, clergy, burghers) instead of generic `local_max_literacy`. All other fields match vanilla. |

### Scripted Relations — `in_game/common/scripted_relations/`

| File | Contents |
|------|----------|
| `cc_merchant_trade_boost.txt` | Relation that tracks merchant trade activity between overlord and subject (used by bond chain B) |
| `cc_colonial_monopoly_boost.txt` | Relation tracking colonial monopoly positioning (used by bond chain B) |

### Laws — `in_game/common/laws/`

| File | Contents |
|------|----------|
| `cc_culture_capacity_nerfs.txt` | Law adjustments that reduce culture capacity; complements the culture capacity nerf advances |

### Estate Privileges — `in_game/common/estate_privileges/`

| File | Contents |
|------|----------|
| `cc_nobles_privileges.txt` | `magyar_supremacy` — Nobles estate privilege for Hungary: noble satisfaction, estate power, cavalry bonus, culture capacity penalty |

### Advances — `in_game/common/advances/`

| File | Contents |
|------|----------|
| `cc_subject_advances.txt` | 27 subject-type unlock advances (Ages 2–5), enabling the 18 custom subject types |
| `cc_late_era_advances.txt` | 40+ idea-tree advances (Ages 3–6): research, trade, colonial, religious, administrative |
| `cc_literacy_advances.txt` | 4 regional literacy catch-up advances (Ages 2 & 4): Western Europe (×2), colonial powers, East Asia — partial offsets to the global literacy baseline nerf |
| `1_cc_literacy_overrides.txt` | Advance overrides that apply the global literacy baseline nerf (loads with `1_` prefix to fire early) |
| `cc_culture_capacity_nerfs.txt` | Advances that reduce culture capacity across various age branches |

### Subject types — `in_game/common/subject_types/cc_subject_types.txt`

18 custom subject types spanning 5 chains: Personal Union (junior_partner, lesser_partner), Shadow/Client (shadow_state → client_state → puppet_state), Elite/Cultural (elite_enclave, palatinate, artists_commune, scientific_college, naval_administration), Trade (associated_republic, chartered_company), and Governance (protectorate, crown_dependency, holy_protectorate, provincial_governorate, tax_farm, military_march).

Subject price definitions in `in_game/common/prices/cc_subject_pays.txt` and `main_menu/common/modifier_type_definitions/cc_subject_prices.txt`.

### Subject Bonds — `in_game/common/on_action/cc_bond_pulse.txt` + `in_game/events/cc_bond_*.txt`

Tracks 5 relationship dimensions per subject (economic, military, political, cultural, personal) on a [-5, +5] scale. Driven by the `cc_bonds_*_pulse` on-action hooks off `yearly_country_pulse`. 15 event files (98 events) organized by subject type:

- `cc_bond_monitor.txt` — hidden 10-year monitor; accumulates bond scores
- `cc_bond_status_reveals.txt` — periodic reveals of the hidden bond state to the player
- `cc_bond_chain_a/b/c/d.txt` — narrative bond event chains (A–D story arcs)
- `cc_bond_colonial_nation.txt` / `cc_bond_governorate.txt` / `cc_bond_palatinate.txt` / `cc_bond_puppet.txt` / `cc_bond_dependency.txt` / `cc_bond_march.txt` / `cc_bond_federal.txt` — per-subject-type bond events
- `cc_bond_red_herrings.txt` — deceptive events that obscure bond state
- `cc_bond_aor.txt` — Age of Revolutions payoff events (one-shot; resolve how long-term bond state translates to AoR outcomes)

Gated by `has_game_rule = cc_subject_bonds_on`.

### Modifiers — `main_menu/common/static_modifiers/`

| File | Contents |
|------|----------|
| `cc_event_modifiers.txt` | ~455+ modifiers: cabinet event effects, 18 synergy bonuses, 8 dual-synergy bonuses, wealth hoarding stacks, intl synergy bonuses, feudal holy war, legend quest modifiers, country start modifiers, war council modifiers, colonial posting modifiers |
| `cc_legacy_modifiers.txt` | ~68 modifiers: Track B (legendary minister death legacies × 5 types), Track C (retired legend legacies × 11 types), each with normal + consecrated variant |
| `cc_province_modifiers.txt` | Province-level modifiers for colonial and posting events |

### On-action hooks — `in_game/common/on_action/`

| File | Hook | Purpose |
|------|------|---------|
| `cc_game_start.txt` | `on_game_start` | One-time world effects: France Containment, Mamluk start, Ottoman start |
| `cc_cabinet_pulse.txt` | `yearly/monthly/biyearly_country_pulse` | Drives all cabinet, trait, rivalry, estate faction, colonial, and war council events |
| `cc_legacy_pulse.txt` | `on_cabinet_death` | Fires legacy events when a minister with legendary or retired_legend traits dies |
| `cc_subject_pulse.txt` | `yearly_country_pulse` | Fires subject drawback events (governor ambitions, tax farm revolts, march raids, etc.) |
| `cc_bond_pulse.txt` | `yearly_country_pulse` | Drives all subject bond tracking (monitor, per-type chain events, AoR payoffs) |
| `cc_war_on_actions.txt` | `on_war_won` | Sets `cc_military_reform_opportunity` flag after winning a war, enabling post-war reform proposals |
| `cc_on_actions.txt` | various | Miscellaneous on-action hooks |
| `cc_cabinet_pulse.txt` | `monthly_country_pulse` | Also drives `cc_cabinet_monthly_trait_dispatch` — a hidden single-event dispatcher (`cc_trait_dispatch.1`) that routes per-minister trait assignment for the monthly tick without pulse collision |

### Biases — `in_game/common/biases/`

| File | Contents |
|------|----------|
| `cc_biases.txt` | 14 opinion modifiers (diplomatic favor/insult, estate resentment, intl scholarly/trade/military/religious bonds, etc.) |
| `cc_antagonism.txt` | 2 antagonism modifiers (`cc_fra_hegemony_threat` for France Containment, `antagonism_cc_force_shadow_state`) |
| `cc_court_relations.txt` | Court relation modifiers for rivalry/court tension and cabal compact |

### Scripted Triggers — `in_game/common/scripted_triggers/cc_cabinet_triggers.txt`

| Trigger | Purpose |
|---------|---------|
| `cc_minister_is_available` | True when a cabinet character is on `cc_duty_free_hands` or has no duty assigned |

### Game rules — `main_menu/common/game_rules/cc_game_rules.txt`

8 toggleable rules (all default on):

| Rule | Default | Purpose |
|------|---------|---------|
| France Containment | on | Elevated Lowlands antagonism toward France at game start |
| Wealth Events | on | Wealth hoarding events above 100× monthly income |
| Mamluk Start | on | Foreign rule strain penalties for the Mamluks |
| Ottoman No-Colonization | on | Prevents Ottoman colonization |
| Dynamic AI Personalities | Dynamic Historical + Drift | AI country personality evolution |
| HYW Flavor | on | Hundred Years War starting modifiers and event chains |
| Overlord-Subject Bonds | on | Multi-dimensional bond tracking across long-term subjects |
| Hussites — One Small Loan | on | Papal loan event during the Hussite Wars situation |

---

## Event firing system (pulse architecture)

All recurring events fire through three pulse hooks in `cc_cabinet_pulse.txt`:

**`yearly_country_pulse`** (30% random chance for legacy event):
- Elder minister succession (`cc_legacy.1`)
- All 26 synergy checks (`cc_synergy.*`) and 10 dual-synergy checks (`cc_dual.*`)
- Legend quest checks (`cc_legend.1–5, .8`)
- Negative trait grants (`cc_neg.1/.2/.4/.6/.8`) and rehabilitation checks (`cc_neg.11–19`)
- 12 cross-country intl synergy events (`cc_intl.*`)
- War council events while at war (`cc_wc.1/.2/.3`) + post-war reform proposals (`cc_wc.10–12`) via `cc_military_reform_opportunity`
- Colonial charter company events (`cc_colonial.1/.3`) and colonial posting events (`cc_posting.1–4`)
- Stepping stone progression events (`cc_prog.1/.10/.20/.30`) + chain advance events (`cc_prog.2–4`, etc.)
- Subject bond system events (via `cc_bond_pulse.txt`: monitor, per-type chains, AoR payoffs)
- Subject drawback and shadow compact events (via `cc_subject_pulse.txt`)

**`monthly_country_pulse`** (20% base, 30% no-event guard):
- Age-specific trait spawning (Renaissance Humanist, Age of Discovery, Reformation, Absolutism, Revolutions variants)
- Ruler–minister counsel events (`cc_cabinet.1/.2/.4`)
- Estate interaction events (`cc_cabinet.10/.11`)
- Feudal transition event (`cc_feudal.10`)

**`biyearly_country_pulse`** (33% base, 10% no-event guard):
- Integration trait grant (`cc_traits.1`)
- Conditional trait spawning for Families A–F (`cc_cond.*`)
- Teachable traits (`cc_traits.20/.21`)
- Estate interactions (`cc_cabinet.12/.13`)
- Neighboring-country diplomatic events (`cc_cabinet.20–23`)
- Province interactions (`cc_cabinet.30–33`)
- Feudal court events (`cc_feudal.1–7`)
- Negative trait events (`cc_neg.3/.5/.7`)
- Action-forged trait grants (`cc_cond.30–34`)
- Wealth hoarding events (`cc_wealth.1–8`) + hidden inflation/corruption stacks (`.9/.10`)
- Court rivalry accumulation + `cc_rival.*` escalation events
- Estate faction events (`cc_fac.1–3`)
- Colonial divan events (`cc_colonial.2`, biyearly charter checks)
- War council outdated general retirement (`cc_wc.20`)

**`on_cabinet_death`** (via `cc_legacy_pulse.txt`):
- If minister had legendary traits → `cc_legacy.2` (permanent modifier legacy)
- If minister had `retired_legend` trait → `cc_legacy.3` (legacy modifier event)

**`on_war_won`** (via `cc_war_on_actions.txt`):
- Sets `cc_military_reform_opportunity` on the winning country, enabling post-war reform proposal events (`cc_wc.10–12`)

---

## How to add new content

### New trait
1. Add block to the appropriate `in_game/common/traits/*.txt` file
2. Add localization key `trait_<id>`, `trait_<id>_desc` to the matching `.yml` file
3. If it should spawn via event: add the event to the relevant event file + trigger in `cc_cabinet_pulse.txt`
4. If it needs a custom icon: add PNG to `main_menu/gfx/interface/icons/traits/`

### New event
1. Add `country_event = {}` block to the appropriate `in_game/events/*.txt` file (or create a new file mirroring vanilla event folder structure)
2. Add localization to matching `.yml` file
3. Add the event ID to the correct pulse block in `cc_cabinet_pulse.txt` (or `cc_subject_pulse.txt` for subject events, `cc_bond_pulse.txt` for bond events)
4. If the event applies modifiers: add them to `cc_event_modifiers.txt`
5. If the event uses `add_opinion`: define the bias in `cc_biases.txt` or `cc_antagonism.txt` first

### New advance
1. Add block to `cc_late_era_advances.txt` (idea-tree) or `cc_subject_advances.txt` (subject unlock)
2. Add localization to `main_menu/localization/english/cc_advances_l_english.yml`
3. If it unlocks a new subject type: create the type in `cc_subject_types.txt` and add its localization to `cc_new_subjects_l_english.yml`
4. **Cross-age `requires`**: don't use `requires = X` across age boundaries — use `potential = { has_advance = X }` + `allow = { has_advance = X }` instead

### New subject type
1. Add block to `in_game/common/subject_types/cc_subject_types.txt`
2. Add the unlock advance to `cc_subject_advances.txt`
3. Add localization to `cc_new_subjects_l_english.yml`
4. Add bond chain events to the appropriate `cc_bond_*.txt` file and hook into `cc_bond_pulse.txt`

### New static modifier
- Cabinet/event modifier → `cc_event_modifiers.txt`
- Legacy/death modifier → `cc_legacy_modifiers.txt`
- Province modifier → `cc_province_modifiers.txt`

### New bias
- Opinion modifier → `cc_biases.txt`
- Antagonism modifier → `cc_antagonism.txt`
- Court relation modifier → `cc_court_relations.txt`

### New cabinet duty
1. Add `<duty_name> = {}` block to a new file in `in_game/common/cabinet_actions/`
2. Set `ability = adm/dip/mil`, define `country_modifier`, `allow`, `potential`
3. Add localization to `cc_duties_and_modifiers_l_english.yml`
4. Hook any new events it should boost into the relevant pulse block in `cc_cabinet_pulse.txt`, gated by `any_cabinet_character = { cabinet_action = <duty_name> }`

### New auto-modifier
1. Add block to `in_game/common/auto_modifiers/cc_cabinet_composition.txt`
2. Set `requires_real = yes` and define `potential_trigger` using trait checks
3. Add localization key to the matching yml file

### New situation
1. Add situation block to a new file in `in_game/common/situations/`
2. Add a game rule toggle in `main_menu/common/game_rules/cc_game_rules.txt` and its localization
3. Add events to `in_game/events/` with a matching namespace
4. Hook the situation's `can_start` behind `has_enabled_situation_trigger = { type = ... }`
5. If the situation needs an IO: add it to `in_game/common/international_organizations/`
6. If it needs a CB: add it to `in_game/common/casus_belli/`
7. Add GUI panel if needed: `in_game/gui/panels/situation/`
8. Add icon DDS to `main_menu/gfx/interface/icons/situations/` and illustration to `main_menu/gfx/interface/illustrations/situation/`
9. Add all localization to a new `cc_<name>_l_english.yml`

---

## Tools

### `tools/vanilla_search.py` — Vanilla reference lookup

```bash
# Validate a modifier name (partial name OK):
python tools/vanilla_search.py modifier global_trade_power

# List all valid values for a type key:
python tools/vanilla_search.py values government_type
python tools/vanilla_search.py values religion_group

# Show vanilla usage snippets for a trigger/effect:
python tools/vanilla_search.py examples add_opinion
python tools/vanilla_search.py examples has_advance --events

# List all defined bias/antagonism names:
python tools/vanilla_search.py biases
```

**Always use this before writing a modifier name, type value, or bias** — typos fail silently.

### `tools/advance_combos.py` — Advance combination explorer

```bash
# Show all mod advance combinations with effects:
python tools/advance_combos.py --mod-only

# Generate interactive advance explorer HTML:
python tools/advance_combos.py --json tools/advance_data.js && open tools/advance_explorer.html
```

### `tools/var_refs.py` — Variable reference search

Find where any scripted variable is set, changed, checked, or removed across all mod files. Output shows the file, line, operation type, and event/block + option context.

```bash
# All references to a specific variable:
python tools/var_refs.py cc_bond_initialized

# Substring match — all vars containing a prefix:
python tools/var_refs.py cc_bond_cul

# List all variable names and total reference counts:
python tools/var_refs.py --list

# Filter by operation type (set/change/clamp/has/remove/map_add/map_ref/var):
python tools/var_refs.py cc_bond --op set,remove

# Group output by file instead of by variable:
python tools/var_refs.py cc_bond --group file

# Search a single file:
python tools/var_refs.py --file in_game/events/cc_bond_chain_d.txt
```

### `tools/fix_bom.py` — UTF-8 BOM fixer

```bash
python tools/fix_bom.py          # fix all missing BOMs
python tools/fix_bom.py --check  # report only, exit 1 if any missing
```

Run automatically by the git pre-commit hook. All `.txt` and `.yml` files need UTF-8 BOM or the game silently ignores them.

### `tools/setup_junctions.py` — Submod junction setup (run once after cloning)

EU5 only loads mods from the top-level `mod/` folder. This script creates Windows directory junctions there so the game can find each submod while its files stay under `submods/` in the repo.

```bash
python tools/setup_junctions.py
```

Run once after cloning, again whenever a new submod is added, and after **renaming** a submod (for example when promoting a `1.3 Beta ...` submod to its stable `Flavorium Universalis - ...` name). It reads the `name` field from each submod's `.metadata/metadata.json` and creates `mod/<name>/` → `submods/<folder>/`. Safe to re-run: up-to-date junctions are skipped.

The script also **prunes stale junctions**. After every submod name resolves cleanly, any junction directly under `mod/` that points into this repo's `submods/` tree but no longer matches a current submod `name` is removed. This is what clears out old links after a rename (the leftover `1.3 Beta ...` junctions from the beta line). Only reparse points resolving inside `submods/` are touched; real directories (like `cabinets-and-choices`) and unrelated links are left alone, and the prune is skipped entirely if any submod name failed to load, so a transient read error can never delete a still-valid link.

### `tools/generate_workshop.py` — Workshop description generator

```bash
python tools/generate_workshop.py            # regenerate all sections in WORKSHOP_DESCRIPTION.md
python tools/generate_workshop.py --section trait-summary  # one section only
python tools/generate_workshop.py --dry-run  # print to stdout without writing
```

Parses mod files and updates `<!-- GEN:name -->...<!-- /GEN:name -->` sections in `WORKSHOP_DESCRIPTION.md`. Run after adding new traits, subject types, advances, or game rules.

### `tools/translate.py` — Localization machine translation

Translates `localization/english/*.yml` into the other languages EU5 supports, and optionally the Steam page title/description and change notes.

```bash
python tools/translate.py -m                              # mod localization, all languages
python tools/translate.py -m -l french,german,spanish     # limit to specific languages
python tools/translate.py -s                              # main mod + every submod
python tools/translate.py -wp -cn                         # Steam page and change notes
```

Valid `-l` values: `braz_por`, `french`, `german`, `japanese`, `korean`, `polish`, `russian`, `simp_chinese`, `spanish`, `turkish`. There is no Italian: EU5 ships no `italian` localization folder, so an `l_italian` file would never load.

**Backends** are set in `tools/config.toml` (`localization_translator`, `workshop_title_translator`, `workshop_description_translator`):

- `local` — an OpenAI-compatible server (llama.cpp, llama-swap, LM Studio, Ollama). Configured by the `local_*` keys; no API key or per-character cost. This is the default.
- `deepl` — needs `pip install deepl` and `DEEPL_API_KEY` in `.env`.
- `gemini-3-flash` — needs `GEMINI_API_KEY` in `.env`.

Set `local_disable_thinking = true` for reasoning models. Without it the model spends its whole token budget thinking about each string and runs roughly eight times slower. Tune `local_batch_size` and `local_concurrency` to your server's parallel slot count.

**Incremental by default.** Per-key source hashes live in `tools/dependencies/.translate_hashes.json`, so re-runs only translate strings whose English text changed, keys missing from a target file, and keys that no longer exist (those get pruned). To force a re-translation of specific strings, delete their lines from the target `.yml` and re-run.

**Markup safety.** Every translation is checked against the source for `[scope.Function]` links, `$VARIABLE$` tokens, `@icon!` sprites, `#colour ... #!` blocks and `\n`. A translation that drops a token or invents one the source never had is retried, then falls back to the English source. Inventing tokens matters: a model will happily turn "they" into `[minister.GetSheHe]` in a key where that scope does not exist, which errors in-game.

Mark text to leave alone with `# NO-TRANSLATE` on a line, `# NO-TRANSLATE BELOW` / `# NO-TRANSLATE END` around a block, or `# LOCK` on a line in a *target* file to protect a hand-corrected translation from being overwritten.

---

## Testing

1. Enable the mod in the EU V launcher
2. Start a new game (or load a save)
3. Check `%USERPROFILE%\Documents\Paradox Interactive\Europa Universalis V\logs\` for errors
4. Script errors show as `[ERROR] ... Unknown trigger/effect` — fix the exact key name with `vanilla_search.py`

---

## Releasing to Steam Workshop

All uploads are handled by `tools/upload.py`. Configure targets in `tools/config.toml`.

`tools/release.py` wraps it with a confirmation prompt and can run translation first. It consumes `-t/--translate`, `-l/--languages` and `--translate-only`, and forwards every other flag to `upload.py`:

```bash
python tools/release.py -t -m -wp        # translate, then upload mod + workshop pages
python tools/release.py -t --translate-only -l french,german,spanish
python tools/release.py -m               # upload only, no translation
```

The translation step mirrors the upload targets, so `-t -wp` translates the workshop pages it is about to upload.

### Common commands

```bash
# Upload everything: main mod + workshop pages + all submods + change notes
python tools/upload.py -m -wp -s -cn

# Main mod content only
python tools/upload.py -m

# Workshop description/title only (main mod + submod pages)
python tools/upload.py -wp -s

# Submods only
python tools/upload.py -s

# Change notes only
python tools/upload.py -cn
```

### Before each release

1. Bump `"version"` in `.metadata/metadata.json` (and each submod's `.metadata/metadata.json`)
2. Update `assets/workshop/change-notes.bbcode` with the new version entry
3. Update `WORKSHOP_DESCRIPTION_steam.bbcode` if the page copy has changed
4. For submods: update `submods/<name>/workshop/change-notes.bbcode` and `submods/<name>/WORKSHOP_DESCRIPTION_steam.bbcode` as needed
5. Run `python tools/upload.py -m -wp -s -cn`

### First upload (new item)

Set `workshop_upload_item_id = 0` in `tools/config.toml`. The script will create a new Workshop item and write the assigned ID back into the config automatically. Commit that change to keep the ID tracked in git. Same applies to submods — set `workshop_id = 0` in the `[[submods]]` block.

### Submod workshop pages

Each submod can have its own `WORKSHOP_DESCRIPTION_steam.bbcode` at `submods/<name>/WORKSHOP_DESCRIPTION_steam.bbcode` and change notes at `submods/<name>/workshop/change-notes.bbcode`. These are uploaded when `-wp` and `-s` (pages) or `-cn` and `-s` (change notes) are passed together.

---

## Reference docs

- [Dev Diaries](docs/dev_diaries/) — feature deep-dives (e.g. [The Balance of Power](docs/dev_diaries/balance-of-power.md)); rendered on the docs site at `dev-diaries.html` (regenerate with `python tools/generate_dev_diaries.py`)
- [docs/scripting-gotchas.md](docs/scripting-gotchas.md) — verified patterns and a named table of things that don't exist
- [docs/eu5-modding-reference.md](docs/eu5-modding-reference.md) — summarized EU5 modding reference
- [docs/v2/v2.md](docs/v2/v2.md) — v2.0 expansion design overview and pillar status
- [CLAUDE.md](CLAUDE.md) — Claude Code guidance for AI-assisted development
- [EU5 Modding Wiki](https://eu5.paradoxwikis.com/Modding) — official documentation
