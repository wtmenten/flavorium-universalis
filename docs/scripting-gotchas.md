# EU5 Scripting Gotchas & Verified Patterns

Lessons from sessions building traits, events, estate privileges, advances, buildings, and on_actions.

---

## Modifier Key Validity

Always verify modifier names in vanilla before using them. Common pitfalls:

- **`global_estate_satisfaction_equilibrium`** — does NOT exist. Use `global_estate_target_satisfaction = -0.02` (accepts raw floats)
- **`navy_tradition`** — does NOT exist as a country modifier. Use `monthly_navy_tradition = 0.05`
- **`local_navy_tradition_from_battles`** — does NOT exist. Use `navy_tradition_from_battle` (country) + `harbor_suitability` (local)
- **`monthly_inflation`** — valid country modifier ✓
- **`monthly_legitimacy`** — valid country modifier ✓
- **`court_spending_cost_modifier`** — valid country modifier ✓
- **`free_building_levels`** — valid as a **location** static modifier (NOT country) ✓
- **`antagonism_taking_land_giving_modifier`** — valid country modifier (makes taking land generate more antagonism) ✓
- **`num_naval_governors`** — valid in country_modifier blocks for estate privileges, advances, and government reforms ✓

Quick verify command: `grep -r "modifier_name" "f:/SteamLibrary/steamapps/common/Europa Universalis V/game/main_menu/common/static_modifiers/" 2>/dev/null | head -5`

---

## Buildings

### Location rank filters — TWO different syntaxes depending on context

In **building definitions** (`.txt` building type files), rank is set by direct flags on the building:
```
city = yes
megalopolis = yes
# (no town = yes means it can't be placed in towns)
```

In **event triggers / scripted triggers**, use:
```
NOT = { location_rank = location_rank:rural_settlement }
# or
location_rank = location_rank:city
```

### country_modifier vs capital_country_modifier in buildings

- `modifier = {}` — location-level effects only (local sailors, harbor_suitability, local_navy_attrition)
- `capital_country_modifier = {}` — country-level effects, but ONLY applies when the building is in the capital
- There is NO generic `country_modifier` that applies from any location for non-unique buildings

### Estate buildings

- Estate buildings use `construction_demand = estate_construct_building` — this has **no gold cost**, only a goods cost through production methods. "Building cost" proxies in events should use `monthly_income_trade_and_tax * N` or `estate_tax_base * N`
- `estate_category` is a valid building category (defined in `building_categories/00_default.txt`)
- To check if an estate has buildings: `num_buildings_owned_by_estate > 0` (trigger on estate scope)
- To iterate/destroy estate buildings from an estate scope:
  ```
  ordered_building_owned_by_estate = {
      max = 1
      location = { destroy_building = prev }
  }
  ```

---

## Events

### Hidden events (no UI popup)
```
type = country_event
title = empty_text
desc = empty_text
hidden = yes
```
Use `immediate = { }` for effects. No `option` blocks needed.

### Alphanumeric event IDs
**WRONG — do NOT use.** `cc_wealth.3a`, `cc_cond.3b` etc. are INVALID. The engine rejects any ID where the part after the namespace dot is not a pure integer. Use `cc_foo.3`, `cc_foo.30`, `cc_foo.31` etc. Plan your ID ranges in advance.

### Stacking modifiers
- Use `mode = add_and_extend` to stack and extend duration
- To cap at N stacks: use N separately named modifiers (`cc_modifier_1` through `cc_modifier_N`), check `NOT = { has_country_modifier = cc_modifier_N }` in the trigger
- Without `mode`: reapplying a modifier just resets its duration (does NOT stack)

### Scripted math in triggers
`gold >= { value = monthly_income_trade_and_tax multiply = 100 }` — verify this works in country_event triggers. It works in effect blocks; triggers may require a `check_variable` workaround if not.

### Estate gold effects — two valid syntaxes
```
# From country scope, gives gold to an estate type:
add_gold_to_estate = {
    estate_type = estate_type:nobles_estate
    value = 100
}

# From estate scope, adds/removes gold from that estate:
"estate(estate_type:burghers_estate)" = {
    estate_add_gold = {
        value = { value = root.monthly_income_trade_and_tax multiply = 5 }
    }
}
```

### biyearly_country_pulse structure
- `random_events = {}` — fires ONE random event per trigger. Events suppress themselves if their trigger block fails.
- `events = {}` — fires ALL listed events every trigger. Use for hidden passive effects.
- `chance_to_happen = 33` means 33% chance the pulse fires at all each biyearly tick
- Both blocks can coexist in the same pulse definition

### on_game_start scope
`on_game_start` `effect = {}` runs at **world scope** (not country scope). Use `every_country = { ... }` or `c:TAG = { ... }` to scope into specific countries. Reference: `game/in_game/common/on_action/_hardcoded.txt`

---

## Estate Privileges

- Estate privileges **cannot** grant `num_naval_governors` in vanilla — but **can** in mod files (verified to parse correctly; test in-game for confirmation)
- `"estate_power(estate_type:nobles_estate)" >= 0.40` — use this exact string-quoted syntax for estate power triggers in `allow` blocks
- Monarchy check in allow: `government_type = government_type:monarchy`

---

## Advances

- `unlock_estate_privilege = ep_privilege_name` — makes the privilege appear when the advance is taken
- `unlock_government_reform = cc_reform_name` — makes a reform available after taking the advance
- **Cross-age `requires` is broken**: `requires = other_advance` logs an error if the required advance is in a different age. Use `potential` + `allow` with `has_advance` instead:
  ```
  potential = { has_advance = naval_charter_advance }
  allow    = { has_advance = naval_charter_advance }
  ```
- `has_advance = advance_key` — country trigger, checks if the advance has been researched
- `has_advance_available = advance_key` — country trigger, checks researched OR available to research

---

## Antagonism / Biases

- **Biases file location**: `in_game/common/biases/`
- `add_antagonism = { target = c:TAG modifier = modifier_name }` — adds antagonism FROM the current scope TOWARD the target
- To give Burgundy antagonism against France, scope into Burgundy (`every_neighbor_country`) and call `add_antagonism { target = c:FRA modifier = ... }`
- Bias modifiers: `value = 200, yearly_decay = 1` → decays to 0 in 200 years (integer math, safe)
- Avoid fractional `yearly_decay` — may be clipped to integers

---

## Localization

- All `.yml` files **must** have UTF-8 BOM (`\xef\xbb\xbf` as first bytes). The engine silently ignores files without it.
- Write with Python: `f.write(b'\xef\xbb\xbf'); f.write(content.encode('utf-8'))`
- Static modifier display names: try both `cc_modifier_name:` and `STATIC_MODIFIER_NAME_cc_modifier_name:` — the mod currently uses the un-prefixed form and it works

---

## Where to Look for Verified Syntax

| What you need | Where to look |
|---|---|
| Governor slot grants | `game/in_game/common/government_reforms/common.txt` |
| Estate building destruction | `game/in_game/common/generic_actions/estates.txt` |
| Building category names | `game/in_game/common/building_categories/00_default.txt` |
| Location rank names | `game/in_game/common/location_ranks/00_default.txt` |
| Antagonism modifier structure | `game/in_game/common/biases/05_antagonism_hardcoded.txt` |
| on_game_start scope examples | `game/in_game/common/on_action/_hardcoded.txt` |
| Hidden event format | `game/in_game/events/ai_area_conqest_events/hidden_events_for_ai_conquest.txt` |
| Estate gold effects | `game/in_game/events/pirate_events.txt` (lines ~370+) |
| random = { chance = X } in effects | `game/in_game/events/diplomacy/espionage_events.txt` (lines ~44+) |
| Building iteration in locations | `game/in_game/common/generic_actions/japanese_shogunate.txt` |
| Static modifier keys (location) | `game/main_menu/common/static_modifiers/location.txt` |
| Static modifier keys (country) | `game/main_menu/common/static_modifiers/country.txt` |

---

## Trigger & Effect Name Quick Reference

Names that look obvious but are wrong, with verified replacements:

| Wrong name | Correct name | Notes |
|---|---|---|
| `global_trade_power` | `global_trade_center_power` | country modifier |
| `fort_maintenance_modifier` | `fort_maintenance_cost` | country modifier |
| `missionary_strength` | `global_pop_conversion_speed_modifier` | conversion speed |
| `global_monthly_development_cost_modifier` | **does not exist** | no global dev cost modifier |
| `has_war_with` | `is_at_war_with` | trigger; also `at_war_with` works |
| `is_at_war` | `at_war` | country scope trigger |
| `add_opinion_modifier` | `add_opinion` | effect; syntax: `{ target = X modifier = Y }` — no `years` param |
| `is_in_sub_continent` | `capital.sub_continent = sub_continent:xxx` | dot-chain from country scope; no block wrapper |
| `capital = { is_in_area = area:xxx }` | `capital.area = area:xxx` | dot-chain, no block wrapper |
| `culture.group = root.culture.group` | `culture = { has_culture_group = root.culture.culture_group }` | culture scope needed |
| `is_in_culture_group` | `has_culture_group` | valid in culture and country scope |
| `estate_has_active_privilege` | **does not exist** | use `has_estate_privilege = estate_privilege:xxx` (country scope) |
| `count_cabinet_characters` | **does not exist** | use two `any_cabinet_character` blocks to check "at least 2" |
| `all_cabinet_character` | **does not exist** | invert: `NOT = { any_cabinet_character = { NOT = { ... } } }` |
| `count_subjects` | `num_subjects` (total only) or `any_subject` | no filtered count by type |
| `any_owned_province` | `any_owned_location` | locations = provinces in EU5 |
| `current_action` | **does not exist** | no trigger for character's current action |
| `join_war` | **does not exist as simple event effect** | complex war effects require specific war scope |
| `subtract = N` in weight modifier | `add = -N` | weight_multiplier modifier blocks |
| `trigger = { ... }` as an effect | `if = { limit = { ... } ... }` | conditional effects inside options |
| `is_courtier = yes` in `create_character` | `create_in_limbo = yes` | creates without assigning a role |
| `has_estate = estate_type:X` in country scope | `any_estate = { estate_type = estate_type:X }` | `has_estate` is character-scope only |
| `add_cultural_tradition` in country scope | `culture = { add_cultural_tradition = X }` | must be in culture scope |
| `add_cultural_influence` in country scope | `culture = { add_cultural_influence = X }` | must be in culture scope |
| `prestige_strong_bonus` | `prestige_severe_bonus` | scripted value; see size table below |
| `liberty_desire_mild_increase` | `liberty_desire_mild_plus` | scripted value; see table below |
| `global_institution_spread_modifier` | **does not exist** | use `embrace_institution_cost_modifier` (negative value) or `institution_importance_modifier` |
| `has_culture_group = X` in country scope | `culture = { has_culture_group = X }` | requires culture scope even from country scope |
| `has_custom_tag = foo` on characters | **does not exist** | trait `custom_tags = {}` values cannot be queried from triggers |
| `target = scope_name` in `declare_war_with_cb` | `target = scope:scope_name` | must include `scope:` prefix |
| `requires = advance_from_other_age` | `potential/allow = { has_advance = X }` | cross-age `requires` logs an error; gate with potential+allow instead |

### Scripted value naming patterns

Prestige: `prestige_weak_bonus` (5), `prestige_mild_bonus` (10), `prestige_severe_bonus` (15), `prestige_extreme_bonus` (20), `prestige_ultimate_bonus` (50). Penalty variants use `_penalty`.

Liberty desire: `liberty_desire_weak_plus` (5), `liberty_desire_mild_plus` (10), `liberty_desire_severe_plus` (20), `liberty_desire_extreme_plus` (50), `liberty_desire_ultimate_plus` (100). Decrease uses `_minus`.

---

## Scope Rules

### Culture effects
`add_cultural_tradition` and `add_cultural_influence` require **culture scope**. From a country-scope event:
```
culture = { add_cultural_tradition = cultural_tradition_mild_bonus }
culture = { add_cultural_influence = cultural_influence_mild_bonus }
```

### Estate existence check (country scope)
`has_estate` is a **character-scope** trigger (checks if character is affiliated with an estate). To check if an estate type exists in country scope:
```
any_estate = { estate_type = estate_type:nobles_estate }
```
```
country_has_estate =  estate_type:nobles_estate 
```

### Sub-continent / area checks (country scope)
```
# Sub-continent — dot-chain, no block
capital.sub_continent = sub_continent:western_europe

# Area — dot-chain, no block
capital.area = area:brabant_area

# Culture group — must be in culture scope even from country scope
culture = { has_culture_group = culture_group:sinitic }

# Dynamic culture group comparison (e.g. "same culture group as root") doesn't work:
# root.culture.culture_group is parsed as an event target link and fails.
# Enforce with only_overlord_or_kindred_culture = yes on the subject type instead.
```

### Conditional effects inside options
```
# WRONG:
scope:minister = {
    trigger = { NOT = { has_trait = siege_engineer } }
    add_trait = trait:siege_engineer
}

# CORRECT:
scope:minister = {
    if = {
        limit = { NOT = { has_trait = siege_engineer } }
        add_trait = trait:siege_engineer
    }
}
```

---

## Illustration Tags

Valid tags for `illustration_tags = { 10 = TAG }` in events:

`interior`, `exterior`, `military`, `army`, `economy`, `bank`, `burghers`, `discussing`, `fire`, `angry`, `armed`, `happy`, `professional`, `regular`, `ages`, `interior_peasant`

`combat` is **NOT** a valid tag (common mistake — use `military` instead).

---

## Bureaucracies

Each custom bureaucracy named `cc_foo_bureau` needs a corresponding modifier type definition or the game asserts on load:

```
# main_menu/common/modifier_type_definitions/cc_bureaucracies.txt
cc_foo_bureau_impact_modifier = {
    percent=yes
    game_data={
        category=country
    }
}
```

Vanilla pattern: `game/main_menu/common/modifier_type_definitions/01_byz.txt`.
The `_impact_modifier` suffix is auto-expected by the bureaucracy system.

---

## on_action — Multiple `effect` Blocks

If two files each define `on_game_start = { effect = {} }`, the engine warns "more than one 'effect' defined, using most recent" and only runs the last one. **Keep all effects for the same on_action in a single file.** See `in_game/common/on_action/cc_game_start.txt`.

---

## Opinion Modifiers (Biases)

`add_opinion = { target = X modifier = my_modifier }` — the modifier must be defined in `common/biases/` first. "Unknown bias type" in the log means it's missing from that folder.

- Duration is set on the bias definition (`yearly_decay = N`), not in the effect call
- `add_opinion_modifier` does NOT exist
- Vanilla bias files to reference: `03_opinion_from_events.txt`, `02_opinion_subject_types.txt`

---

## Things That Don't Exist (Don't Waste Time Searching)

- Per-location monthly income as a scripted value — use `scope:location.development` as a proxy
- `province_location_wealth` as a scripted effect value — it's a GUI sort key only
- `country_modifier = {}` on non-unique buildings — use `capital_country_modifier` or `modifier` (location-level)
- `add_estate_satisfaction` with `type = estate_type:X` directly — the correct key is `type = estate_type:nobles_estate` (not `estate_type = ...`)
- Global development cost modifier — no `global_monthly_development_cost_modifier` or equivalent exists
- `count_cabinet_characters` — no character iterator count trigger; approximate with multiple `any_cabinet_character` checks
- `current_action` on characters — cannot check what action a character is currently performing
- `join_war` as a simple event effect — war manipulation requires complex war scope effects
- Alphanumeric event IDs — `cc_foo.3a` is INVALID; must use pure integers like `cc_foo.3`, `cc_foo.30`
- `has_custom_tag` trigger — doesn't exist; trait `custom_tags = {}` values can't be queried
- Dynamic culture-group comparison — `root.culture.culture_group` as a dot-chain accessor is parsed as an event target link and fails; use `only_overlord_or_kindred_culture = yes` on subject types instead
- `illustration_tags = { 10 = combat }` — `combat` tag doesn't exist; use `military`
