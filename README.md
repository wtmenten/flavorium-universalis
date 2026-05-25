# Cabinets and Choices — Developer Guide

**Version:** 0.1 | **Game compatibility:** EU5 1.2.* | **Multiplayer:** synchronized

A Europa Universalis V mod that expands cabinet gameplay with a dynamic minister trait system, synergy events, legacy mechanics, custom subject types, and era-specific advances. All content is additive (no `replace_paths`).

---

## Repo layout

```
in_game/          content loaded alongside vanilla (additive)
main_menu/        content loaded on the main-menu screen only
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

Icons go in `main_menu/gfx/interface/icons/traits/`.

### Events — `in_game/events/`

| File | Namespace | ~Count | Purpose |
|------|-----------|--------|---------|
| `cc_cabinet_events.txt` | `cc_cabinet` | 16 | Ruler–minister counsel, estate relations, diplomatic situations, provincial affairs |
| `cc_trait_events.txt` | `cc_traits` | 18 | New age trait acquisition, ruler teaching, peer learning |
| `cc_conditional_trait_events.txt` | `cc_cond` | 15 | Conditional trait spawning based on realm state |
| `cc_synergy_events.txt` | `cc_synergy` | 26 | Trait synergy pairs — bonus modifiers when ministers share matching trait families |
| `cc_negative_trait_events.txt` | `cc_neg` | 17 | Underperformance events (grant negative traits) + rehabilitation checks (remove them) |
| `cc_wealth_events.txt` | `cc_wealth` | 10 | Minister enrichment, wealth hoarding stacks (inflation / corruption) |
| `cc_dual_synergy_events.txt` | `cc_dual` | 10 | Cabinet × religious_figure dual-role synergies |
| `cc_intl_synergy_events.txt` | `cc_intl` | 12 | Cross-country minister interactions with neighbors |
| `cc_feudal_events.txt` | `cc_feudal` | 8 | Feudal age court events |
| `cc_legacy_events.txt` | `cc_legacy` | 3 | Senior minister retirement and legacy passing |
| `cc_legend_events.txt` | `cc_legend` | 6 | Legendary trait quest chains |
| `cc_subject_events.txt` | — | — | Placeholder; subject events fire from `cc_subject_pulse.txt` |

### Advances — `in_game/common/advances/`

| File | Contents |
|------|----------|
| `cc_subject_advances.txt` | 27 subject-type unlock advances (Ages 2–5), enabling the 18 custom subject types |
| `cc_late_era_advances.txt` | 40+ idea-tree advances (Ages 3–6): research, trade, colonial, religious, administrative |

### Subject types — `in_game/common/subject_types/cc_subject_types.txt`

18 custom subject types spanning 5 chains: Personal Union (junior_partner, lesser_partner), Shadow/Client (shadow_state → client_state → puppet_state), Elite/Cultural (elite_enclave, palatinate, artists_commune, scientific_college, naval_administration), Trade (associated_republic, chartered_company), and Governance (protectorate, crown_dependency, holy_protectorate, provincial_governorate, tax_farm, military_march).

### Modifiers — `main_menu/common/static_modifiers/`

| File | Contents |
|------|----------|
| `cc_event_modifiers.txt` | ~455 modifiers: cabinet event effects, 18 synergy bonuses, 8 dual-synergy bonuses, wealth hoarding stacks (5 inflation + 5 corruption), intl synergy bonuses, feudal holy war, legend quest modifiers, country start modifiers |
| `cc_legacy_modifiers.txt` | ~68 modifiers: Track B (legendary minister death legacies × 5 types), Track C (retired legend legacies × 11 types), each with normal + consecrated variant |

### On-action hooks — `in_game/common/on_action/`

| File | Hook | Purpose |
|------|------|---------|
| `cc_game_start.txt` | `on_game_start` | One-time world effects: France Containment, Mamluk start, Ottoman start |
| `cc_cabinet_pulse.txt` | `yearly/monthly/biyearly_country_pulse` | Drives all cabinet and trait events (see below) |
| `cc_legacy_pulse.txt` | `on_cabinet_death` | Fires legacy events when a minister with legendary or retired_legend traits dies |
| `cc_subject_pulse.txt` | `yearly_country_pulse` | Fires subject drawback events (governor ambitions, tax farm revolts, march raids, etc.) |

### Biases — `in_game/common/biases/`

| File | Contents |
|------|----------|
| `cc_biases.txt` | 14 opinion modifiers (diplomatic favor/insult, estate resentment, intl scholarly/trade/military/religious bonds, etc.) |
| `cc_antagonism.txt` | 2 antagonism modifiers (`cc_fra_hegemony_threat` for France Containment, `antagonism_cc_force_shadow_state`) |

### Game rules — `main_menu/common/game_rules/cc_game_rules.txt`

4 toggleable rules (all default on): France Containment, Wealth Events, Mamluk Start, Ottoman No-Colonization.

---

## Event firing system (pulse architecture)

All recurring events fire through three pulse hooks in `cc_cabinet_pulse.txt`:

**`yearly_country_pulse`** (30% random chance for legacy event):
- Elder minister succession (`cc_legacy.1`)
- All 26 synergy checks (`cc_synergy.*`) and 10 dual-synergy checks (`cc_dual.*`)
- Legend quest checks (`cc_legend.1–5, .8`)
- Negative trait grants (`cc_neg.1/.2/.4/.6/.8`) and rehabilitation checks (`cc_neg.11–19`)
- 12 cross-country intl synergy events (`cc_intl.*`)
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

**`on_cabinet_death`** (via `cc_legacy_pulse.txt`):
- If minister had legendary traits → `cc_legacy.2` (permanent modifier legacy)
- If minister had `retired_legend` trait → `cc_legacy.3` (legacy modifier event)

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
3. Add the event ID to the correct pulse block in `cc_cabinet_pulse.txt` (or `cc_subject_pulse.txt` for subject events)
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

### New static modifier
- Cabinet/event modifier → `cc_event_modifiers.txt`
- Legacy/death modifier → `cc_legacy_modifiers.txt`

### New bias
- Opinion modifier → `cc_biases.txt`
- Antagonism modifier → `cc_antagonism.txt`

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

### `tools/fix_bom.py` — UTF-8 BOM fixer

```bash
python tools/fix_bom.py          # fix all missing BOMs
python tools/fix_bom.py --check  # report only, exit 1 if any missing
```

Run automatically by the git pre-commit hook. All `.txt` and `.yml` files need UTF-8 BOM or the game silently ignores them.

### `tools/generate_workshop.py` — Workshop description generator

```bash
python tools/generate_workshop.py            # regenerate all sections in WORKSHOP_DESCRIPTION.md
python tools/generate_workshop.py --section trait-summary  # one section only
python tools/generate_workshop.py --dry-run  # print to stdout without writing
```

Parses mod files and updates `<!-- GEN:name -->...<!-- /GEN:name -->` sections in `WORKSHOP_DESCRIPTION.md`. Run after adding new traits, subject types, advances, or game rules.

---

## Testing

1. Enable the mod in the EU V launcher
2. Start a new game (or load a save)
3. Check `%USERPROFILE%\Documents\Paradox Interactive\Europa Universalis V\logs\` for errors
4. Script errors show as `[ERROR] ... Unknown trigger/effect` — fix the exact key name with `vanilla_search.py`

---

## Reference docs

- [docs/scripting-gotchas.md](docs/scripting-gotchas.md) — verified patterns and a named table of things that don't exist
- [docs/eu5-modding-reference.md](docs/eu5-modding-reference.md) — summarized EU5 modding reference
- [CLAUDE.md](CLAUDE.md) — Claude Code guidance for AI-assisted development
- [EU5 Modding Wiki](https://eu5.paradoxwikis.com/Modding) — official documentation
