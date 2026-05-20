# EU5 Modding Reference

Summaries of the official EU5 modding wiki pages, with links back to each source.

---

## Table of Contents

1. [Core Scripting](#core-scripting)
   - [Defines](#defines)
   - [Effect](#effect)
   - [Scope](#scope)
   - [Scope Link](#scope-link)
   - [Trigger](#trigger)
   - [Macro (Scripted Effects/Triggers)](#macro-scripted-effectstriggers)
   - [Script Value](#script-value)
   - [Variable](#variable)
   - [Mean Time to Happen (MTTH)](#mean-time-to-happen-mtth)
2. [Interface & Localization](#interface--localization)
   - [Interface Modding Guide](#interface-modding-guide)
   - [Color](#color)
   - [GUI Script](#gui-script)
   - [Scripted GUI](#scripted-gui)
   - [Localization](#localization)
3. [Game Systems](#game-systems)
   - [Modifier Types](#modifier-types)
   - [On Actions](#on-actions)
   - [Modifier Modding](#modifier-modding)
   - [Setup Modding](#setup-modding)
4. [Actions & Events](#actions--events)
   - [Action Modding](#action-modding)
   - [Event Modding](#event-modding)
   - [Disaster Modding](#disaster-modding)
   - [Mission Modding](#mission-modding)
   - [Situation Modding](#situation-modding)
5. [Laws, Organizations & Institutions](#laws-organizations--institutions)
   - [Law Modding](#law-modding)
   - [International Organization Modding](#international-organization-modding)
   - [Institution Modding](#institution-modding)
6. [Character & Society](#character--society)
   - [Character Modding](#character-modding)
   - [Trait Modding](#trait-modding)
   - [Culture Modding](#culture-modding)
   - [Pop Modding](#pop-modding)
   - [Estate Modding](#estate-modding)
   - [Religion Modding](#religion-modding)
7. [Economy & Infrastructure](#economy--infrastructure)
   - [Goods Modding](#goods-modding)
   - [Building Modding](#building-modding)
   - [Advance Modding](#advance-modding)
8. [World Content](#world-content)
   - [Concept Modding](#concept-modding)
   - [Disease Modding](#disease-modding)
9. [Military & Diplomacy](#military--diplomacy)
   - [War Modding](#war-modding)
   - [Unit Modding](#unit-modding)
   - [Subject Type Modding](#subject-type-modding)

---

## Core Scripting

### Defines

**Source:** https://eu5.paradoxwikis.com/Defines

Static global constants controlling core game mechanics (estate thresholds, combat multipliers, AI weights, camera settings). Cannot change during gameplay.

**File location:** `loading_screen/common/defines/` — create `01_mod_defines.txt` with only the values you are changing.

```
NCountry = {
    COUNTRIES_GETTING_SCORE = 12
}
NDiplomacy = {
    CALL_FOR_PEACE_THRESHOLD_MONTHS = 120
}
```

**Key rules:**
- Load order: later filenames override earlier ones.
- Global only — no per-country or per-location overrides.
- 68+ documented sections: `NCountry`, `NDiplomacy`, `NMilitary`, `NAI`, `NGraphics`, etc.
- Changing one value often requires rebalancing related defines.

---

### Effect

**Source:** https://eu5.paradoxwikis.com/Effect

Commands that modify game state. Require correct scope context.

**Iterator pattern:**
```
every_[scope] = {
    limit = { <triggers> }
    <effects>
}
```

**Ordered iterator (sorted):**
```
ordered_[scope] = {
    limit = { <triggers> }
    order_by = script_value
    position = 0          # zero-indexed
    min = 1
    max = script_value
    check_range_bounds = no   # prevents errors if list size < min/max
    <effects>
}
```

Iterator types: `every_` (all matches), `ordered_` (sorted), `random_` (one random).

**Gotcha:** Scope mismatches cause silent failures.

---

### Scope

**Source:** https://eu5.paradoxwikis.com/Scope

Scopes represent game entity types (country, character, location, etc.) and define the context for effects and triggers.

**Key keywords:**
- `root` — top-level scope of the current script block
- `prev` — previous scope in a chain
- `this` — current scope
- `scope:saved_name` — a previously saved scope reference

**Four iterator types:**

| Type | Keyword | Purpose |
|---|---|---|
| Trigger | `any_*` | Check if any/N scopes meet conditions |
| Effect (all) | `every_*` | Apply effects to all matching |
| Effect (sorted) | `ordered_*` | Apply to sorted scopes |
| Effect (random) | `random_*` | Apply to one random scope with optional `weight` |

All support `limit = { <triggers> }`. Trigger iterators support `count`, `percent`, `filter`, `count = all`.

**Gotchas:**
- Use `?=` to safely check if a scope exists before accessing it.
- Negated trigger iterators default to requiring **all** scopes to fail.

---

### Scope Link

**Source:** https://eu5.paradoxwikis.com/Scope_link

Scope links (event targets) reference specific game objects, values, or scopes. Primary cross-scope navigation tool.

```
scope:target_name                    # saved scope reference
p:xF98DA3.state.owner.capital        # chained navigation
active_outbreak(<disease>)           # parameterized link
estate:<estate_type>                 # parameterized link
```

**Three categories:**
1. **Data scope links** — require input parameters
2. **Value scope links** — return a number or boolean
3. **Wildcard scope links** — reference trigger types

**Navigation:** `root`, `prev`, `this`, `scope:saved_name`, `global_var:name`, `local_var:name`, `var:name`

**Gotcha:** Links must match their required "from scope" — e.g., `birth_location` only works from character scope.

---

### Trigger

**Source:** https://eu5.paradoxwikis.com/Trigger

Conditional statements that read game state. Used to determine whether events fire, actions are available, or effects execute.

**Comparison operators:** `<`, `<=`, `=`, `!=`, `>`, `>=`
- `=` checks exact equality (works on non-numerical values too).
- Comparisons invert inside `NOT = { }`.

**Flow triggers:** `and`, `or`, `not`, `nand`, `nor`, `trigger_if`, `trigger_else_if`, `trigger_else`

**Iterator triggers (`any_*`):** Support `filter`, `count`, `count = all`, `percent`

**Scope comparison:** `army_size > c:FRA.army_size`

**Gotchas:**
- `hidden_trigger = { }` hides triggers from tooltips.
- `add_to_temporary_list` placement inside iterators affects which instances are captured.

---

### Macro (Scripted Effects/Triggers)

**Source:** https://eu5.paradoxwikis.com/Macro

Reusable, text-substitution script blocks.

- **Scripted effects:** `common/scripted_effects/`
- **Scripted triggers:** `common/scripted_triggers/`

```
# Definition
add_to_cabinet = {
    random_cabinet = {
        add_to_cabinet = $target$
    }
}

# Usage
add_to_cabinet = {
    target = character:maj_gajah_mada
}
```

Arguments use `$argument_name$` in the definition. Arguments are **literal text replacement** — you cannot pass variable values, only static text/identifiers.

**Other macro types:**
- **Scripted Lists** (`common/scripted_lists`): Filtered iterators with built-in conditions.
- **Script Values** (`common/script_value`): Numerical macros.
- **Scripted Modifiers** (`common/scripted_modifiers`): Reusable MTTH modifier macros.
- **@ Values:** Intra-file number constants, e.g. `@[1/3]` — mainly used in GUI files.

**Gotchas:**
- Argument names are case-sensitive.
- File encoding must be UTF-8 BOM.

---

### Script Value

**Source:** https://eu5.paradoxwikis.com/Script_value

Mathematical calculations producing dynamic numeric or boolean results. Used in effects, triggers, variables, and AI calculations. Recalculated every time invoked.

**Defined in:** `common/script_values/` or inline.

```
example_script_value = {
    value = 10
    multiply = 2
    if = {
        limit = { is_at_war = yes }
        add = 5
    }
}
```

**Operators** (strictly left-to-right — no order of operations):
`value`, `add`, `subtract`, `multiply`, `divide`, `modulo`, `max`, `min`, `round`, `ceiling`, `floor`, `round_to`, `fixed_range`, `integer_range`, `pow`, `abs`

**Gotchas:**
- Maximum 5 decimal places; range ±92233720368547.75807.
- **No order of operations** — structure math accordingly.
- Use `save_temporary_value_as` to store intermediate results, referenced via `scope:`.
- Display in UI: `Scope.ScriptValue('named_value')`.

---

### Variable

**Source:** https://eu5.paradoxwikis.com/Variable

Variables store values or scopes on game objects.

| Type | Syntax | Persistence | Scope |
|---|---|---|---|
| Regular | `var:my_variable` | Persistent | Attached to a game object |
| Global | `global_var:name` | Persistent | Accessible anywhere |
| Local | `local_var:name` | Temporary | Removed at end of effect chain |

```
set_variable = {
    name = my_variable
    value = 1    # number, boolean, scope reference, or script value
}
```

**Lists:**
- `add_to_list` — persists across event blocks
- `add_to_temporary_list` — only lasts the current block
- Iterate with `every_in_list`

**Variable Lists:** Persistent ordered collections saved to objects. `add_to_variable_list`, `clear_variable_list`.

---

### Mean Time to Happen (MTTH)

**Source:** https://eu5.paradoxwikis.com/Mean_time_to_happen

Calculation syntax that determines event frequency and weights. Used in institution spread, event weights, `on_actions`, and `random_*` iterators.

```
weight = {
    factor = 1            # base value (also: base, days, months, years)
    modifier = {
        factor = 10       # multiplier when trigger fires
        trigger = { is_ruler = yes }
    }
    modifier = {
        add = 5           # addition instead of multiply
        prestige >= 50
    }
}
```

**Base value keywords** (all equivalent): `factor`, `base`, `days`, `months`, `years`

**Modifier types:**
- **Basic:** `factor` (multiply) or `add` (add). Triggers optional.
- **Compare modifiers:** Use `value`/`factor` with `offset`, `multiplier`, `step`, `min`, `max` for clamping.
- **First valid:** Block where only the first matching trigger applies.

**Gotchas:**
- Scripted values are **not** allowed in base definitions.
- Compare modifiers are not evaluated in order.

**Scripted Modifiers:** Reusable MTTH modifier macros in `common/scripted_modifiers/`. Invoked with `scripted_modifier_name = yes`.

---

## Interface & Localization

### Interface Modding Guide

**Source:** https://eu5.paradoxwikis.com/Interface_modding_guide

GUI files live in `modfolder/in_game/gui/` (or `main_menu/gui/`).

**Key structural concepts:**
- **Templates** — Reusable property containers: `using = template_name`. Cannot be overridden per-instance.
- **Types** — Reusable widget definitions with overridable `block "..."` sections. Wrapped in `types my_types_name { }`.
- **Windows** — Top-level UI entities. Always need `name`, `parentanchor`, and `size`.
- **Widgets** — Container groupings inside windows.

```
window = {
    name = "mymod_window"
    parentanchor = center
    size = { 100% 100% }
    alwaystransparent = yes
}
```

**Recommended visibility/toggling** via `GetVariableSystem`:
```
visible = "[GetVariableSystem.Exists('mymod_window_open')]"
onclick = "[GetVariableSystem.Toggle('mymod_window_open')]"
```
Map window to key in a scripted_widgets file: `gui/mymod_interface.gui = mymod_window`

**Gotchas:**
- Enable `-debug_mode` launch option for live GUI editing and the "UI Bounds" overlay.
- Scripted variables sometimes only update after a player-triggered event.

---

### Color

**Source:** https://eu5.paradoxwikis.com/Color

| Mode | Syntax | Notes |
|---|---|---|
| RGB | `rgb { 255 0 255 }` | Values 0–255, or 0–1 if all ≤ 1 |
| HSV | `hsv { 0.66 0.33 0.38 }` | All values 0–1 |
| HSV360 | `hsv360 { 355 70 90 }` | H: 0–360, S/V: 0–100 |
| HEX | `hex { ff7f00ff }` | RGBA format |

All modes support an optional 4th alpha channel value.

**Named colors:** `common/named_colors/`, wrapped in a `colors { }` block. No scripted math.

**Scripted color math:** Supports `if`/`else_if`/`else` and `lerp` interpolation (two-color, three-color with `mid_point`, five-color, and `valley_start`/`valley_end` plateau modes).

---

### GUI Script

**Source:** https://eu5.paradoxwikis.com/GUI_script

The scripting language used inside `.gui` files and localization strings to retrieve and transform game data. Always enclosed in `[ ]`, uses CamelCase, chained with `.`:

```
[State.GetJobseekersDesc]
[GetPopTypeByName('peasants').GetName]
```

- Game object arguments use single quotes; numbers/booleans do not.
- **Functions** — retrieve or transform data.
- **Promotes** — convert between data types (analogous to scope transitions).
- `Access...` prefixed = const (read-only); `Get...` prefixed = nonconst (mutable).

**Key types:** `CFixedPoint` (64-bit fixed-point, 5 decimal places), `CString`, `CVector2f/3f/4f`, standard primitives.

---

### Scripted GUI

**Source:** https://eu5.paradoxwikis.com/Scripted_gui

Named script blocks attaching triggers and effects to GUI button elements. Defined in `common/scripted_guis/*.txt`.

```
my_button = {
    scope = country
    is_shown = { has_variable = feature_enabled }
    is_valid = { gold >= 50 }
    effect = { add_gold = -50 }
}
```

**GUI integration (in .gui file):**
```
onclick = "[ScriptedGui.Execute(GuiScope.SetRoot(GetScriptedGui('my_button')).End)]"
```

**Additional features:**
- `saved_scopes` — extra named scopes accessible inside triggers/effects.
- Confirmation dialogs via `confirm_title` and `confirm_text`.
- AI support: `ai_is_valid`, `ai_chance` (1–100), `ai_frequency` (months between evaluations).

**Scope options:** `country`, `character`, `location`, `war`, `army`, `navy`, `international_organization`

---

### Localization

**Source:** https://eu5.paradoxwikis.com/Localization

**File format:** `.yml`, encoded as **UTF-8 with BOM**. Naming: `MODNAME_l_english.yml`.

Files process in **reverse alphabetical order** — prefix with `a` or `0` to load last (highest priority). Use `/replace/` subfolder to override vanilla keys.

```yaml
my_key: "Text displayed to player"
```

**Formatting:**
- Colors: `#R` (red), `#G` (green), `#E` (concept link blue), end with `#!`
- Styles: `#bold`, `#italic`, end with `#!`
- Icons: `@gold!`, `@time!`, `@warning_icon!`
- Inserting other keys: `$other_key$`

**Data functions** (GUI script in loc strings): `[SCOPE.Country.GetName]`
- `|+` modifier — colors positive green/negative red
- `|U` modifier — uppercase first letter

**Saved scopes in localization:**
- Save in script: `save_scope_as = scope_name`
- Reference: `[scope_name.GetName]` or `[SCOPE.sCountry('scope_name').GetName]`

**Customizable localization:** `common/customizable_localization/` — conditional text blocks called from loc strings with `[Custom('custom_localization_name')]`.

---

## Game Systems

### Modifier Types

**Source:** https://eu5.paradoxwikis.com/Modifier_types

Definitions of individual modifier statistics — display format, color polarity, and category. File location: `common/modifier_type_definitions/` (lowercase filenames required).

```
modifier_name = {
    decimals = 2
    color = good        # good, bad, or neutral
    percent = yes       # multiply display by 100
    boolean = no        # yes = display as yes/no
    prefix = MODIFIER_PREFIX_KEY
    suffix = MODIFIER_SUFFIX_KEY
    game_data = { category = country }
}
```

**Rules:**
- Numerical modifiers default to `0` and stack additively.
- Boolean modifiers default to `no`.
- Each type auto-generates two localization keys: `MODIFIER_TYPE_NAME_<key>` and `MODIFIER_TYPE_DESC_<key>`.

---

### On Actions

**Source:** https://eu5.paradoxwikis.com/On_actions

Game event hooks firing on time pulses or discrete occurrences (war declared, ruler death, etc.).

```
on_some_action = {
    trigger = { ... }
    events = { my_event.1 }
    random_events = {
        50 = my_event.2
        50 = my_event.3
    }
    first_valid = { ... }
    on_actions = { ... }       # chain other on_actions
    effect = { ... }
    weight_multiplier = { ... }
    fallback = { ... }
}
```

Delays support fixed or random ranges: `delay = { months = { 6 12 } }`

**Critical rules:**
- Only adding a new `on_actions = { }` block is safe for mods — all other blocks cannot be appended without overwriting.
- Effects run concurrently with events — scopes set in effects do not carry into fired events.
- `on_game_start` fires before player country selection — use `delay = { days = 1 }` to access player country.
- Cabinet member death does **not** trigger `on_cabinet_removed`.
- Fallback chains can create infinite loops.
- Use unique prefixes on custom on action names to avoid cross-mod conflicts.

---

### Modifier Modding

**Source:** https://eu5.paradoxwikis.com/Modifier_modding

Two systems for applying gameplay modifiers: **static** (manually applied/removed) and **auto** (automatically applied based on live conditions).

**Static modifiers** — `common/static_modifiers/`:
```
my_modifier = {
    country_cabinet_efficiency = 0.1
    game_data = {
        category = country
        decaying = yes
    }
}
```

Applied with `add_<type>_modifier`:
- `days/months/years = -1` for permanent
- `mode` = `replace` / `add` / `extend` / `add_and_extend` / `set_to_largest`
- `size` = strength multiplier (supports script values)

**Auto modifiers** — `common/auto_modifiers/`:
```
war_exhaustion_impact = {
    scales_with = war_exhaustion
    land_morale_modifier = -0.02
    potential_trigger = { ... }
    limit = { legitimacy >= 50 }    # inequalities only: <, >, <=, >=
    category = country
}
```

**Gotchas:**
- Static modifier values must be static numbers/booleans — no dynamic calculations.
- Auto modifier `limit` does **not** support `=`, `AND`, `OR`, `NOT` — use `potential_trigger` for complex conditions.
- Never remove hardcoded modifiers (e.g., `in_combat`, `religious_unity`).

---

### Setup Modding

**Source:** https://eu5.paradoxwikis.com/Setup_modding

Configures the initial game world state. Uses specialized managers rather than normal scripting.

**File locations:** `setup/start/`, `setup/countries/`, `setup/templates/`

**Critical encoding rule:**
- `setup/countries/` and `setup/templates/` — UTF-8 **with** BOM
- `setup/start/` — UTF-8 **without** BOM (BOM causes read errors)

**Load order:** Dynasties must be defined before characters reference them. Characters used as spouses/parents must be defined before referencing characters.

**Core managers:**

| Manager | Purpose |
|---|---|
| `institution_manager` | Active institutions and origin locations |
| `religion_manager` | Religious school relations and saint assignments |
| `dynasty_manager` | Dynasty names, types, home locations |
| `character_db` | Starting characters with skills, traits, relationships |
| `work_of_art_manager`, `diplomacy_manager`, `building_manager`, `war_manager` | Additional setup |

**Ownership levels:** `own_control_core`, `own_control_integrated`, `own_control_conquered` (and others).

**Gotchas:**
- Most managers are **additive** — removing an entry requires replacing the entire file.
- Use `-leavepops` launch flag to see raw pop counts before game adjustments.
- `setup/templates/` are referenced by filename, usable only from country setup.

---

## Actions & Events

### Action Modding

**Source:** https://eu5.paradoxwikis.com/Action_modding

Actions are interactions that countries or characters perform. Four sub-types: generic actions, character interactions, country interactions, and cabinet actions.

**Common fields (shared syntax):**
```
my_action = {
    potential = { trigger }
    allow = { trigger }
    effect = { ... }
    ai_will_do = <script_value>
    ai_tick = monthly
    cooldown = { type = unique_id   months = 6 }
    price = price:some_cost
    sound = sfx_key
}
```

**Interaction targets (select_trigger)** — the core mechanism for target selection:
```
select_trigger = {
    looking_for = country
    target_flag = target_country
    source = actor
    visible = { trigger }
    enabled = { trigger }
    allow_null = yes
    allow_self = yes
    column = { data = name   widget = <gui_type> }  # MANDATORY — crashes without it
    max_targets_for_ui = 50
}
```

**For value sliders** (`looking_for = value`): use `min`, `max`, `default`, `step`, `ai_override_value`.

**Sub-types:**

| Type | Location | Key Fields |
|---|---|---|
| Generic Actions | `common/generic_actions` | `type` (owncountry/parliament/religious/etc.) |
| Character Interactions | `common/character_interactions` | `on_other_nation`, `on_own_nation`, `is_consort_action` |
| Country Interactions | `common/country_interactions` | `type` (diplomacy/subject), `accept`, `diplo_chance`, `reject_effect` |
| Cabinet Actions | `common/cabinet_actions` | `type` (adm/dip/mil), `country_modifier`, `monthly_effect`, progress tracking |

**Critical gotchas:**
- `looking_for = country` excludes `scope:actor` by default — add `allow_self = yes` to include it.
- Cabinet actions cannot use common-syntax fields.
- At least one `column` is **mandatory** in any interaction target with a UI list (game crashes without it).

---

### Event Modding

**Source:** https://eu5.paradoxwikis.com/Event_modding

Events present countries or locations with choices or notifications.

**File structure:** `/events/` — each file must start with `namespace = my_namespace`. Event IDs: `namespace.integer` (1–9999).

```
my_events.1 = {
    type = country_event
    title = my_events.1.title
    desc = my_events.1.desc
    trigger = { is_subject = no }
    immediate = { save_scope_as = main_char }  # scopes saved here available in localization
    option = {
        name = my_events.1.a
        ai_will_select = { value = 100 }
        add_gold = 25
    }
    option = { name = my_events.1.b }
}
```

**Event types:** `country_event`, `location_event`, `exploration_event`, `age_event`, `omens_event`

**Core properties:**

| Property | Notes |
|---|---|
| `category` | Adds graphics: `situation_event`, `io_event`, `disaster_event` |
| `immediate` | Effects before display; scopes available in localization |
| `after` | Effects after option is selected |
| `fire_only_once = yes` | Fires once globally, ever |
| `hidden = yes` | Auto-selects an option (no popup) |
| `orphan = yes` | Suppresses "no known fire source" errors |
| `outcome = positive/negative/neutral` | Adds audio cue |

**Dynamic historical events:**
```
dynamic_historical_event = {
    tag = POL
    from = 1444.1.1
    to = 1500.1.1
    monthly_chance = 10
}
```
Requires `fire_only_once = yes`.

**Weight multiplier** (in random lists):
```
weight_multiplier = {
    base = 10
    modifier = { factor = 2   trigger = { legitimacy >= 50 } }
    modifier = { add = 5   trigger = { prestige >= 50 } }
}
```

**Modifying base game events:** Prefix your file name with `0000_` in `/events/`, declare the target namespace, copy only the events you want to change. "Duplicated event ID" errors are harmless.

**Firing methods:** On-actions, direct effects (`trigger_event_silently` / `trigger_event_non_silently`), dynamic historical events.

---

### Disaster Modding

**Source:** https://eu5.paradoxwikis.com/Disaster_modding

Internal crises affecting a single country with monthly spawn chance, active modifiers, monthly effects, and end conditions.

**File structure:**
- Definitions: `common/disasters/`
- Icons: `gfx/interface/icons/disasters/`
- GUI panels: `in_game/gui/panels/disaster/<disaster_key>.gui`

```
my_disaster = {
    monthly_spawn_chance = 0.05
    can_start = { ... }
    modifier = { ... }
    can_end = { ... }
    on_start = { ... }
    on_monthly = { ... }
    on_end = { ... }
    image = "path/to/image.dds"
    fire_only_once = yes
}
```

**Gotchas:**
- Events linked to disasters use `category = disaster` and namespace matching the disaster key.
- GUI panels access the disaster via `DisasterView.GetDisaster()` datacontext.
- `map_mode` references an **existing** mapmode (unlike situations, which define colors inline).

---

### Mission Modding

**Source:** https://eu5.paradoxwikis.com/Mission_modding

Objective trees guiding countries through specific goals with rewards. Location: `common/missions/`.

```
my_mission_pack = {
    icon = mission_icon_name
    player_playstyle = administrative   # administrative | diplomatic | military
    visible = { conditions }
    enabled = { conditions }
    chance = 50                         # AI weight

    my_task = {
        icon = icon_name
        requires = { other_task }
        visible = { trigger }
        enabled = { trigger }
        bypass = { trigger }
        duration = 365                  # in days; 0 = instant
        final = yes                     # completes entire mission
        modifier_while_progressing = { ... }
        on_start = { effect }
        on_completion = { effect }
        on_monthly = { effect }
    }
}
```

**Select triggers in tasks** use the same syntax as action interaction targets.

**Gotchas:**
- Missions require `game_has_missions_enabled = yes` in their `visible` trigger.
- `final = yes` on a task terminates the entire mission on that task's completion.
- `on_persistent_completion` runs for select_trigger interactions, not standard completion.

---

### Situation Modding

**Source:** https://eu5.paradoxwikis.com/Situation_modding

Complex political/economic phenomena visible to specific countries as alerts. Can affect many countries (unlike disasters). Situations are valid scopes that can hold variables even before activation.

**File structure:**
- Definitions: `common/situations/`
- Icons: `gfx/interface/icons/situations/`
- GUI panels: `in_game/gui/panels/situation/<key>.gui`

```
my_situation = {
    monthly_spawn_chance = 0.02
    can_start = { triggers }
    can_end = { triggers }
    visible = { triggers }          # which countries see the alert
    on_start = { effects }
    on_monthly = { effects }
    on_ending = { effects }
    on_ended = { effects }
    map_color = { scripted color logic }
    secondary_map_color = { scripted color logic }
}
```

All scripted blocks execute on **situation scope**, not country scope.

**Map mode:** Situations define their own inline map mode — `map_color`, `secondary_map_color`, `tooltip`, `legend_key`.

**Gotchas:**
- Clean up variables in `on_ended` to prevent savefile bloat.
- `can_start` and `visible` are separate — a country can see a situation without meeting `can_start`.
- Events link to situations using `category = situation`; namespace must match situation key.

---

## Laws, Organizations & Institutions

### Law Modding

**Source:** https://eu5.paradoxwikis.com/Law_modding

Policies organized into mutually exclusive groups by government type and category. Location: `common/laws/`.

```
my_law_group = {
    law_category = administrative      # administrative | military | economic | religious | legal
    law_gov_group = monarchy           # monarchy | republic | theocracy | tribe
    potential = { conditions }

    option_one = {
        allow = { conditions }
        unique = yes                   # only one country can hold this globally
        country_modifier = { tax_income = 0.1 }
        estate_preferences = { nobles_estate   clergy_estate }
        years = 10                     # cooldown before changing
    }
}
```

**Available estates:** `crown_estate`, `nobles_estate`, `clergy_estate`, `burghers_estate`, `peasants_estate`

**Gotchas:**
- Options in one group are mutually exclusive.
- `unique = yes` = only one nation in the entire game can hold it simultaneously.
- Each group must specify exactly one `law_gov_group`.

---

### International Organization Modding

**Source:** https://eu5.paradoxwikis.com/International_organization_modding

Multi-country bodies: HRE, coalitions, crusades, defensive leagues, etc. One file per IO: `common/international_organizations/`.

```
my_org = {
    unique = yes
    has_leader_country = yes
    leader_type = country
    leader_change_method = vote
    has_parliament = yes

    modifier = { ... }                          # all members
    leader_modifier = { diplomatic_capacity = 1 } # leader only
    international_organization_modifier = {     # the IO itself
        hre_max_elector = 4
    }

    variables = {
        my_variable = {
            min = 0   max = 100
            monthly_change = { add = { value = 0.05 } }
        }
    }

    can_join_trigger = { trigger }
    on_joined = { effects }
    monthly_effect = { effects }
    ai_desire_to_join = { script_value }
}
```

**Critical gotcha:** If an IO has `has_parliament = yes`, at least one applicable parliamentary issue must exist — otherwise the game spams log errors.

---

### Institution Modding

**Source:** https://eu5.paradoxwikis.com/Institution_modding

Major societal developments (Renaissance, Reformation, etc.) that spawn in locations and spread across the world. Organized by age. Location: `common/institution/`.

```
my_institution = {
    age = age_2_renaissance

    can_spawn = {
        continent = europe
        owner = { has_reform = merchant_republic }
        location_rank >= city
        development >= 10
    }

    promote_chance = {
        base = 5
        modifier = { add = 3   trigger = { development >= 15 } }
    }

    spread_from_friendly_coast_border_location = "institution_base_spread_from_friendly_neighbor_with_early"
    spread_from_any_import = "institution_base_spread_from_import"
    spread_scale_on_control_if_owner_embraced = 2
}
```

**Ages:** `age_1_traditions`, `age_2_renaissance`, `age_3_discovery`, `age_4_reformation`, `age_5_absolutism`, `age_6_revolutions`

**Gotcha:** Spread mechanics use hardcoded optimization values — custom spread attributes must reference **predefined script value name strings**, not inline calculations.

---

## Character & Society

### Character Modding

**Source:** https://eu5.paradoxwikis.com/Character_modding

Character interactions are actions performed by or on characters. Location: `common/character_interactions/`.

```
interaction_name = {
    message = yes
    on_own_nation = yes
    price = price:interaction_price
    price_modifier = { if = { limit = { ... }   add = 10 } }
    potential = { ... }
    allow = { ... }
    effect = { ... }
    ai_tick = daily
    ai_tick_frequency = 120
    ai_will_do = { add = 10 }
}
```

**Select trigger for target UI:**
```
select_trigger = {
    looking_for_a = character
    source = actor
    target_flag = recipient
    name = "localization_key"
    column = { data = name }
    visible = { trigger }
    enabled = { trigger }
}
```

**Common scopes:** `scope:actor` (initiating country), `scope:recipient` (targeted character)

---

### Trait Modding

**Source:** https://eu5.paradoxwikis.com/Trait_modding

Traits define personalities and abilities of rulers, generals, admirals, artists, and other characters. Location: `common/traits/`.

```
trait_name = {
    allow = {
        adm >= 50
        NOT = { has_trait = incompatible_trait }
        owner ?= { government_type = government_type:monarchy }
    }
    category = ruler       # ruler, general, admiral, artist, child, religious_figure
    flavor = personality   # personality, education, interests, government_approach
    modifier = {
        monthly_prestige = 0.1
        discipline = 0.05
    }
}
```

**Character categories:** `ruler`, `general`, `admiral`, `artist`, `child`, `religious_figure`

**Trait flavors:** `personality`, `education`, `interests`, `government_approach`

**Common modifier categories:**
- Government: `country_cabinet_efficiency`, `legislative_efficiency`, `stability_cost`
- Military: `military_tactics`, `discipline`, `land_morale_modifier`, `army_initiative`
- Diplomatic: `diplomatic_reputation`, `improve_relation_impact`, `peace_offer_fairness`
- AI behavior: `aggressiveness_modifier`, `carefulness_modifier`, `win_war_chance_threshold`
- Societal values: `monthly_towards_innovative`, `monthly_towards_belligerent`

**Event-only traits** (never normally assigned):
```
unsuited_for_country_ruling = {
    allow = { always = no }
    modifier = { blocked_from_being_ruler = yes }
}
```

---

### Culture Modding

**Source:** https://eu5.paradoxwikis.com/Culture_modding

Defines population appearance and behavior, connecting languages, 3D graphics groups, and social characteristics.

**File locations:**
- Cultures: `common/cultures/`
- Culture groups: `common/culture_groups/`
- Languages: `common/languages/`

```
welsh = {
    language = welsh_dialect
    color = map_WLS
    tags = { welsh_gfx celtic_gfx british_gfx }    # 3D graphics groups
    opinions = { cornish = kindred }                 # enemy/negative/neutral/positive/kindred
    culture_groups = { celtic_group british_group }  # multiple groups allowed
}
```

**Language syntax:**
```
welsh = {
    color = map_WLS
    family = celtic_family
    male_names = { Owain Gruffudd ... }
    female_names = { Gwenllian Angharad ... }
    dynasty_names = { ap_Gruffudd ... }
    patronym_prefix_son = "ap "
    location_prefix = "de"
}
```

**Dialects:** Nested within languages, inherit parent properties. Single level of hierarchy only — dialects cannot contain sub-dialects.

---

### Pop Modding

**Source:** https://eu5.paradoxwikis.com/Pop_modding

Creates new population categories. Location: `common/pop_types/`.

```
pop_type_name = {
    color = pop_color
    editor = 0.05
    assimilation_conversion_factor = 0.2
    pop_food_consumption = 2.0
    upper = no
    has_cap = yes
    grow = no

    burghers_estate = {}
    dhimmi_estate = { is_dhimmi = yes }

    promote_to = burghers
    promote_to = clergy

    literacy_impact = {
        local_cultural_tradition = 0.2
    }
    pop_percentage_impact = {
        local_unrest = 0.2
    }
}
```

**Standard promotion chain:** `tribesmen → peasants → laborers / soldiers / burghers / clergy / nobles`

**Base game pop types:**
- Upper class: `nobles`, `clergy`, `burghers`
- Working class: `laborers`, `soldiers`, `peasants`
- Special: `tribesmen`, `slaves`

---

### Estate Modding

**Source:** https://eu5.paradoxwikis.com/Estate_modding

Represents major power groups within a country. Location: `common/estates/`.

```
my_custom_estate = {
    color = some_color
    power_per_pop = 0.01
    tax_per_pop = 0.005
    rival = -0.5
    alliance = 0.3
    bank = no
    ruler = no
}
```

**Modifier blocks:**
- `satisfaction` — scaled by `(satisfaction - LOW_SATISFACTION_THRESHOLD)`
- `high_power` — applied when relative power exceeds `LOW_POWER_THRESHOLD`
- `low_power` — applied when relative power is below threshold
- `power` — static modifiers scaled directly by estate power

**Base game estates:** `crown_estate`, `nobles_estate`, `clergy_estate`, `burghers_estate`, `peasants_estate`, `dhimmi_estate`, `tribes_estate`, `cossacks_estate`

---

### Religion Modding

**Source:** https://eu5.paradoxwikis.com/Religion_modding

Defines faiths, groups, schools, aspects, holy sites, gods, avatars, religious figures, and focuses.

**File locations:** `common/religions/`, `common/religion_groups/`, `common/religious_schools/`, `common/religious_aspects/`, `common/religious_figures/`, `common/religious_focuses/`, `common/holy_sites/`, `common/holy_site_types/`, `common/gods/`, `common/avatars/`

**Religion definition:**
```
my_religion = {
    color = some_color
    group = my_religion_group
    definition_modifier = { ... }
    has_religious_influence = yes
    enable = 1444.1.1
    religious_aspects = 3
    opinions = { catholicism = negative   buddhism = neutral }
}
```

**Religious aspects:**
```
my_aspect = {
    religion = { my_religion other_religion }
    visible = { ... }
    enabled = { ... }
    modifier = { ... }
    opinions = { other_aspect = 10   conflicting_aspect = -20 }
}
```

**Holy site types:**
```
my_site_type = {
    country_modifier = { ... }       # scaled by importance
    location_modifier = { ... }
    religion_modifier = { ... }      # 50% location dominance + 50% owner religion match
}
```

**Localization:** `<key>`, `<key>_ADJ`, `<key>_desc` for religions; `<key>`, `<key>_desc` for most other components.

**Gotchas:**
- Editing religion definitions may not affect existing saves (religions built at game start).
- `RELIGIOUS_FOCUS_COST` is scaled to percentage form.

---

## Economy & Infrastructure

### Goods Modding

**Source:** https://eu5.paradoxwikis.com/Goods_modding

Trade good types, raw material production, and population demands.

**File locations:**
- Good types: `common/goods`
- Good demands: `common/goods_demand`
- Demand categories: `common/goods_demand_category`
- Icons: `gfx/interface/icons/trade_goods`

```
copper = {
    method = mining          # mining, farming, hunting, gathering, forestry
    category = raw_material  # raw_material or produced
    color = goods_copper
    default_market_price = 3
    transport_cost = 2
    food = 1
    base_production = 0.5
}
```

**Auto-generated modifiers per good:**
- `ban_exports_of_<key>`, `ban_imports_of_<key>`
- `local_<key>_output_modifier`, `global_<key>_output_modifier`
- `can_extract_<key>`

**Starting goods** (non-additive, use on-actions for mod compatibility):
```
on_game_start = { on_actions = { mod_goods_change } }
mod_goods_change = {
    effect = { location:stockholm = { change_raw_material = goods:fish } }
}
```

**Gotchas:**
- Exactly one good must have `is_slaves = yes`.
- A good named `tools` is hardcoded and mandatory.
- Raw materials must specify a `method`.

---

### Building Modding

**Source:** https://eu5.paradoxwikis.com/Building_modding

Economic/military structures placed in locations.

**File locations:**
- Building types: `common/building_types/`
- Production methods: `common/production_methods/`
- Employment systems: `employment_systems/`
- Road types: `common/road_types/`

**Core fields:**
```
my_building = {
    pop_type = burghers
    employment_size = 4
    category = commercial_building
    max_levels = 3
    country_potential = { ... }
    location_potential = { ... }
    build_time = 365
}
```

**Modifier types:**

| Type | Scope | Shortage-affected | When |
|---|---|---|---|
| `modifier` | location | yes | always |
| `raw_modifier` | location | no | always |
| `market_center_modifier` | location | yes | market centers only |
| `capital_modifier` | location | yes | owner's capital only |
| `capital_country_modifier` | country | yes | country-level at capital |
| `foreign_country_modifier` | country | yes | foreign builders |

**Production methods:**
```
possible_production_methods = { method_key_1 method_key_2 }

unique_production_method_name = {
    produced = good_key
    output = 1
    good_required = 1.5
}
```

**Road types:**
```
my_road = {
    level = 2
    movement_cost = -0.25
    market_access = -0.25
    price_per_unit_distance = price:road_price
    build_time_per_unit_distance = 30
}
```

---

### Advance Modding

**Source:** https://eu5.paradoxwikis.com/Advance_modding

Technological progress organized into ages. Location: `common/advances/`.

```
advance_key = {
    age = age_identifier
    requires = prerequisite_advance    # one only
    research_cost = 1.5
    unlock_unit = unit_type_key
    unlock_building = building_type_key
    unlock_law = law_key
    unlock_production_method = method_key
    unlock_levy = levy_key
    unlock_road_type = road_key
    unlock_diplomacy = { action_1 action_2 }

    modifier_while_progressing = {
        scale = { value = 1 }
        monthly_prestige = 0.05
    }

    ai_weight = { ... }
    for = adm    # adm, dip, or mil
    depth = 2    # tree level position
}
```

**Research cost:** Base × `research_cost` multiplier, modified by age penalties.

**Script functions:** `research_advance`, `can_research_advance`, `has_advance`, `has_advance_available`, `num_of_advances_researched` (all country scope). Global: `advance_type:<key>`.

**Gotchas:**
- Only one `requires` (graphical layout hint), but `allow` blocks can enforce complex dependencies.
- `unlock_diplomacy` is the only unlock type using list syntax.

---

## World Content

### Concept Modding

**Source:** https://eu5.paradoxwikis.com/Concept_modding

Tooltip-enabled reference objects appearing throughout the UI. Location: `common/game_concepts/`.

```
reformation = {
    alias = { protestant protestants }
    texture = "gfx/interface/icons/situations/reformation.dds"
    family = parent_concept_key
    shown_in_encyclopedia = yes
}
```

**Localization:** `game_concept_<key>` (name), `game_concept_<key>_desc` (description).

**Scripting references:**
- `[<concept_key>]` — inline reference with tooltip
- `[<concept_key>|e]` — concept-colored highlighting
- `GC(Arg0)` — returns tooltip for specified key
- `Concept(Arg0, Arg1)` — tooltip with custom display text

---

### Disease Modding

**Source:** https://eu5.paradoxwikis.com/Disease_modding

Creates new disease types with customizable spread, mortality, and environmental effects. Heavily script-value driven. Location: `common/diseases/`.

**Key script values** (per-disease — scopes vary, check carefully):

| Script Value | ROOT scope | Purpose |
|---|---|---|
| `monthly_spawn_chance` | disease | Monthly chance to appear |
| `R0` | location | Core reproduction rate |
| `mortality_rate` | disease | Daily death rate |
| `character_mortality_chance` | location | Monthly character death chance |
| `map_color` | location | Map rendering |

**Spawning:** `spawn_disease` effect, or `monthly_spawn_chance` checked monthly.

**Pop-type specific mortality:**
```
specific_pop_type_effect = {
    pop_type = nobles
    multiplier = 0.3
}
```

**Setup effects (SET, not ADD):**
```
add_disease_resistance = {
    type = bubonic_plague
    resistance = 0.1
    locations = { paris london }
}
```
Both `add_disease_resistance` and `add_disease_outbreak` **replace**, not stack.

---

## Military & Diplomacy

### War Modding

**Source:** https://eu5.paradoxwikis.com/War_modding

Covers casus bellis, wargoal types, and scripted peace treaties.

**Casus Belli** — `common/casus_belli/`:
```
my_cb = {
    war_goal_type = my_wargoal    # mandatory
    visible = { trigger }
    allow_creation = { trigger }
    speed = 1.0                   # required unless event-driven
    can_expire = no
    years = 5
    allow_declaration = { trigger }
    max_warscore_from_battles = 50
}
```

**Required CBs (cannot remove):** `cb_none`, `cb_subject_broke_free`, `cb_insulted_us`, `cb_rebel_support`, `cb_conquer_province`, etc.

**Wargoal types** — `common/wargoals/`:
```
my_wargoal = {
    type = take_province    # take_province, take_capital, superiority, naval_superiority, independence, destroy_army
    ticking_war_score = 1.0
    attacker = {
        conquer_cost = 0.75
        antagonism = 1.0
        allowed_locations = { ... }
    }
}
```

**Peace treaties** — `common/peace_treaties/`:
```
my_treaty = {
    potential = { ... }
    allow = { ... }
    effect = { ... }
    select_trigger = { ... }
    cost = script_value
    base_antagonism = 0.5
    antagonism_type = type_key
    category = location
}
```

**Gotchas:**
- All CBs must have `war_goal_type`.
- `potential`/`allow` in peace treaties cannot access interaction targets.
- Only one interaction target per peace treaty.

---

### Unit Modding

**Source:** https://eu5.paradoxwikis.com/Unit_modding

Military subunit types with combat stats, behaviors, and recruitment rules.

**File locations:**
- Unit types: `common/unit_types/`
- Unit categories: `common/unit_categories/`
- Unit abilities: `common/unit_abilities/`
- Recruitment methods: `common/recruitment_method/`
- Levies: `common/levies/`

**Unit definition:**
```
unit_key = {
    category = army_infantry
    copy_from = base_unit_template    # must be defined before this unit
    age = 1
    buildable = no                    # levies must be no
    levy = yes
    max_strength = 1000
    combat_power = 50
    combat = { jungle = -0.10   mountains = -0.10 }  # terrain combat_power modifiers
    impact = { desert = -0.05 }                        # terrain display modifiers
    upgrades_to = next_unit_key
    country_potential = { ... }
}
```

**Levies:**
```
levy_longbowmen = {
    size = levy_generic_infantry_size    # static value only
    allowed_pop_type = peasants
    allowed_culture = english
    allow = { ... }          # pop scope
    country_allow = { ... }  # country scope
    unit = a_longbowmen      # must have buildable = no
}
```

Unlock levies via `unlock_levy` in advance definitions.

**Unit abilities:**
```
march_to_sound_of_guns = {
    duration = -1
    toggle = yes
    army_only = yes
    allow = { is_army = yes   has_commander = yes }
    modifier = { army_movement_speed = 0.25 }
    finished_when = { in_retreat = yes }
    ai_will_do = { value = 50 }
}
```

**Gotchas:**
- `copy_from` source must be defined before the unit referencing it.
- Levy `size` is static only — no conditional script values.
- Exactly one category must have `is_garrison = yes`.
- Upgrade target must have a strictly higher age index than source.

---

### Subject Type Modding

**Source:** https://eu5.paradoxwikis.com/Subject_type_modding

Defines overlord–subject relationships: financial obligations, autonomy, war participation, annexation, and modifiers. Location: `common/subject_types/`.

```
subject_type_name = {
    level = 3
    diplomatic_capacity_cost_scale = 0.5
    strength_vs_overlord = -0.3
    annexation_speed = 0.02
    annexation_min_years_before = 10
    annexation_min_opinion = 100
    annexation_stall_opinion = 0

    has_limited_diplomacy = yes
    food_access = yes
    can_overlord_build_buildings = yes

    overlord_modifier = { monthly_prestige = 0.01 }
    subject_modifier = { country_cabinet_efficiency = 0.05 }

    institution_spread_to_overlord = monthly_institution_spread_mild
    institution_spread_to_subject = monthly_institution_spread_mild

    on_enable = { ... }
    on_disable = { ... }

    diplo_chance_accept_subject = {
        base = 10
        different_religion = -10
        royal_ties = 3
    }
}
```

**Base game subject types:** `vassal`, `tributary`, `colonial_nation`, `march`, `fiefdom`, `samanta`

**Gotcha:** `annexation_stall_opinion` pauses integration if opinion drops below the threshold.
