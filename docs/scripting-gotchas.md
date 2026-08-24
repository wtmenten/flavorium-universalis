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
- **`court_spending_cost_modifier`** — **RENAMED in 1.3** → `court_spending_efficiency` (sign-flipped: old `-0.08` = new `0.08`)
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

- **No `scope:` prefix inside `[...]` loc tags.** Script-side scope references use `scope:ward`, but localization interpolation drops the prefix: write `[ward.GetName]`, never `[scope:ward.GetName]`. The `scope:` prefix is invalid in `.yml` and will display as a literal string or error in-game.
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
| `fort_maintenance_modifier` | `fort_maintenance_efficiency` | country modifier (renamed in 1.3; sign-flipped from old `fort_maintenance_cost`) |
| `fort_maintenance_cost` | `fort_maintenance_efficiency` | renamed in 1.3; negate value |
| `stability_cost` | `stability_cost_efficiency` | renamed in 1.3; negate value |
| `global_bureaucracy_maintenance_cost_modifier` | `global_bureaucracy_maintenance_efficiency` | renamed in 1.3; negate value |
| `court_spending_cost_modifier` | `court_spending_efficiency` | renamed in 1.3; negate value |
| `local_build_buildings_cost` | `local_build_buildings_efficiency` | renamed in 1.3; negate value |
| `global_build_buildings_cost` | `global_build_buildings_efficiency` | renamed in 1.3; negate value |
| `diplomatic_annexation_cost` | `diplomatic_annexation_efficiency` | renamed in 1.3; negate value |
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

### `*_in_<container>` iterators are entered FROM the container, never given it as a parameter

This is the single easiest scope mistake to make, because the wrong form reads perfectly
naturally. Any iterator named `*_in_region`, `*_in_area`, `*_in_scripted_geography`,
`*_in_province_definition` takes the container as its **input scope**, not as a key inside the
block:

```
# WRONG — logs "Inconsistent trigger scopes (country vs. region)"
any_area_in_region = {
    region = region:italy_region
    any_location_in_area = { ... }
}

# RIGHT
region:italy_region = {
    any_area_in_region = {
        any_location_in_area = { ... }
    }
}
```

Same for geographies (vanilla does this at `on_action/country_four_yearly.txt:334`):

```
scripted_geography:my_geography = {
    ordered_province_definition_in_scripted_geography = { ... }
}
```

`root` inside the nested block is still the original scope, so ownership tests like
`owner ?= root` keep working after the fix.

**To check any iterator's contract**, the offline wiki tables end each row with
`| <input scope> | <output scope> |`:
```
grep -hoE "\|any_area_in_region\|[^|]*\|[^|]*\|[^|]*\|[^|]*" docs/offline-wiki/core/trigger.md
# ...|region|area   <- input region, output area
```
Worth doing for every iterator in a new file, since these fail at load with a clear message
but only for code paths the engine actually parses.

### `change_variable` / `clamp_variable` on an unset variable errors

Distinct from reading one in a trigger, and it has no guard to hide behind: this happens in an
**effect**, usually after the player has clicked an option, so the variable simply has to
exist first.

```
[jomini_script_system.cpp:252]: Script system error!
  Script location: events/<file>.txt:<line>
```

Note the error text is often **blank** apart from the location, unlike the trigger-read case
which names the variable. The line number is the only clue.

**Lazily-initialised scores make this easy to get wrong**, because the initialiser lives in
one event's `immediate` and correctness then depends on firing order. Two ways it bites:

1. **A sibling event fires first.** The initialiser sat in the event hanging off
   `on_bureaucracy_added`; another event in the same thread hung off `on_maintenance_changed`,
   which fires during game start before any bureau is added.
2. **An event writes another thread's score.** A Levant event that touches `cc_byz_strain`
   needs the *debt* initialiser, not the Levant one.

**Rule: every event that writes a score calls that score's initialiser in its own `immediate`,
regardless of which thread the event belongs to.** Do not rely on another event having run.

Auditing for it is mechanical, and worth doing after adding any event:

```
# for each event: collect cc_byz_init_*_effect calls, then check every
# change_variable/clamp_variable name against a var -> owning-initialiser map
```

### `has_variable` does NOT guard a sibling `var:` read

Every trigger in a block is evaluated. Putting `has_variable = X` beside `var:X` does not
prevent the `var:` read from running against an unset variable, and the log fills with:

```
Failed to fetch variable for 'X' due to not being set
Event target link 'var' returned an unset scope
Invalid left side during comparison 'var'
```

Use `trigger_if`, which is vanilla's idiom (`character_interactions/banish_character.txt:9`):

```
# WRONG — errors every evaluation until the variable is first written
has_variable = cc_byz_union_stage
var:cc_byz_union_stage = 2

# RIGHT
trigger_if = {
    limit = { has_variable = cc_byz_union_stage }
    var:cc_byz_union_stage = 2
}
trigger_else = { always = no }
```

**Where this actually bites.** A read is only unsafe if it is evaluated *before* anything
initialises the variable:

| context | safe? | why |
|---|---|---|
| `generic_action` / `potential` | **no** | evaluated every tick from game start |
| on_action `trigger` | **no** | evaluated every pulse |
| event top-level `trigger` | **no** | evaluated before `immediate` runs |
| situation `can_start` / `can_end` | **no** | evaluated outside the event flow |
| event `desc` / `triggered_desc` | yes | renders after `immediate` |
| `option` / `trigger` | yes | evaluated after `immediate` |
| `immediate` / `after` inner `limit` | yes | the init effect already ran |

So lazily-initialised score variables are fine inside events and dangerous everywhere else.
`var:X ?= N` exists but is **equality only**, so it is not a substitute for a guarded `>=`.

### Never put an iterator inside `order_by` (silent failure)

`order_by` is a script value. A bare `add` inside an iterator does **not** reach the enclosing
value; the vanilla accumulator idiom is `root = { add = 1 }` (`script_values/byz_values.txt:17`),
which only works when `root` *is* the thing being accumulated into. Inside an `order_by` it is
not. Vanilla never does this anywhere.

```
# WRONG — does not error, every entry scores 0, and the "best" pick is arbitrary
ordered_area_in_region = {
    order_by = { value = 0  every_location_in_area = { add = development } }
    max = 1
}

# RIGHT — if the limit already guarantees viability, just pick one
random_area_in_region = {
    limit = { any_location_in_area = { percent >= 0.75  owner ?= root } }
}
```

This is worse than a crash: the code reads as though it selects the best candidate and
actually selects an arbitrary one.

### `order_by` must compare a value valid in the ITERATED scope

`development` is **location** scope. Sorting province definitions by it fails at runtime with
`Wrong scope for trigger for compare trigger 'development' (got province_definition, expected
location)`. A province definition is not a location and has no development of its own. If
there is no sensible sort key for the scope, use `random_*`, which needs no `order_by`.

Useful side effect: that error message is also how you settle output-scope questions the
offline wiki gets wrong. The tables list `random_province_definition_in_scripted_geography` as
yielding `province` while `every_`/`ordered_` yield `province_definition`; the engine error
proves the family yields `province_definition`, so the `random_` row is a typo.

### `ordered_*` has no ascending option
The documented parameters are `limit`, `order_by`, `position`, `min`, `max` and
`check_range_bounds`. It always takes the **highest** `order_by` value. To take the lowest,
negate the sort value:
```
ordered_owned_location = {
    order_by = { value = 0  subtract = development }   # least developed
    max = 1
}
```

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

`interior`, `exterior`, `military`, `army`, `economy`, `bank`, `burghers`, `fire`, `angry`, `armed`, `happy`, `professional`, `regular`, `ages`, `interior_peasant`

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

## Trait Allow blocks

Vanilla traits use an `allow = { alway = no }` in many traits. This causes them to be dead code and un-assignable - even in events, despite them being commented otherwise.

---

## Character Creation in Events

Characters cannot be created within options of events they must be created beforehand in an immediate block. then moved into the country again in the 'keep' options and killed in any discard options with a hidden_effect = { kill_character_silently = scope:char_scope }

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

- ~~**Situation `can_end` block (1.3+)**: bare triggers are INVALID; must wrap each condition in `end_reason = { trigger = { ... } desc = "lockey" }`.~~ **This entry was wrong and has been retracted.** `end_reason` does not appear anywhere in the game files: zero hits across all of `in_game/`. `can_end` is a plain trigger, documented as `can_end = <trigger>` in `common/situations/readme.txt:10`, and vanilla writes it bare (`western_schism.txt:18` is a single scripted trigger call). Following the retracted advice would have broken every situation it touched.

---

## Situation panels and situation UI

**A situation panel does not come from the situation definition.** Every vanilla situation ships its own `in_game/gui/panels/situation/<situation_name>.gui`, and `panels/situation/readme.txt` says so explicitly. Ship a situation without one and the panel opens **empty**: not broken, not an error in the log, just blank. This is the single easiest way to make a finished system look unfinished.

Keys that vanilla sets on essentially every situation and that are easy to omit:

| Key | Coverage in vanilla | What breaks without it |
|---|---|---|
| `hint_tag` | 22 of 22 | The "?" button in the situation tooltip is absent (`shared/situation_tooltips.gui:13` gates it on `Situation.HasHint`). Needs a matching entry in `common/scriptable_hints/`, plus loc for `<tag>` and `<tag>_hint_text`. |
| `tooltip` | 21 of 22 | Hovering a map location coloured by the situation explains nothing. Root is the **location**, `scope:target` is the situation. |
| `legend_key` | 79 entries across 22 | The situation's map colours appear in the legend as nothing. Repeatable; `color =` accepts `blue`, `red`, `green`, `yellow`, `yellow_dark`, `purple`, `rgb { }` and `define:`. |

**Situation-panel actions are `type = situation`, not `type = owncountry`.** 155 of vanilla's generic actions use it; an `owncountry` action lands in the country action list instead and the situation panel's action card stays empty. The `select_trigger` is required, not decoration. It binds `scope:recipient` to the situation, which is the parameter the panel button passes (`shared/cards.gui`, `parameter_value = SituationView.GetActiveSituation.GetSituation`):

```
type = situation
select_trigger = {
    looking_for_a = situation
    target_flag = recipient
    name = "choose_situation"
    column = { data = name }
    visible = {
        situation:my_situation = this
        situation_is_active = yes
    }
}
```

**Do not put `player_automated_category` on a `type = situation` action.** Zero of vanilla's 91 situation actions carry one; it belongs to the `owncountry`, `religious` and `parliament` families.

### GUI datafunctions are not script triggers

The GUI layer has its own vocabulary and it is much smaller than script's. Verified by grepping every vanilla `.gui`:

- **`GetLocation('key')` does not exist.** Neither does **`IsSameCountry`**. There is no way to ask the GUI whether the player owns a given location. Mirror the fact into a variable from script and read that instead.
- **`GetNumberOfMembers` does not exist.** `InternationalOrganization` exposes `GetMembers`, `GetMembersAmount`, `GetMembersText`, `GetMembersInfo` and `IsCountryMember`.
- **`HasModifier('name')` does exist** and is the way to test a country modifier from GUI. Country *variables* use `Player.MakeScope.GetVariable('x')`; situation variables use `SituationView.GetActiveSituation.GetSituation.MakeScope.GetVariable('x')`.
- Numeric comparison needs the fixed-point helpers: `GreaterThan_CFixedPoint(a, '(CFixedPoint)0')`, `EqualTo_CFixedPoint`, `FixedPointToInt`, `FixedPointToFloat`.

### GUI assets that don't exist

- **Progress bar textures.** The full set under `main_menu/gfx/interface/progressbars` is `green`, `green_alt`, `grey_alt`, `red`, `red_alt`, `orange`, `yellange`, `yellow`, `brown_alt`, `goldish`, `whiteish` and the rotated variants. There is **no purple and no blue** (`progress_bar_blue_alt.dds` exists only under `loading_screen/`'s own gfx root).
- **Text format tags.** `#color_yellow`, `#color_green`, `#color_red` and `#weak` are defined. **`#color_purple` is not.**
