# Plan: Expand cc_invasion_mexico Situation

## Context

The `cc_invasion_mexico` situation was built in a prior session with a solid foundation (events 1–36, 4 generic actions, confederation IO, CBs, map colors). Three gaps remain:

1. **No situation icon** — the game auto-resolves `gfx/interface/icons/situations/{situation_id}.dds`; the file doesn't exist yet, so the panel shows a blank/default icon.
2. **Actions are thin** — only 2 per side; the situation panel needs more player agency.
3. **Monthly event variety is low** — only 2 monthly loops (events 10 and 25); no event chains. Events 11 and 12 are defined but orphaned (never added to `on_monthly`).

---

## 1. GUI Icon (Mesoamerican Religion Icon)

**Mechanism:** The engine's `GetIcon()` scripted function constructs the path `gfx/interface/icons/situations/{situation_id}.dds` from the situation key. No field in the `.txt` definition is needed — just place the file at the right path.

**Action:** Copy vanilla mesoamerican religion icon to mod's situations icon folder.
- **Source:** `F:\SteamLibrary\steamapps\common\Europa Universalis V\game\main_menu\gfx\interface\icons\religion\mesoamerican.dds`
- **Destination:** `main_menu\gfx\interface\icons\situations\cc_invasion_mexico.dds`
  (directory `main_menu\gfx\interface\icons\situations\` needs to be created)

**Panel image block:** The GUI panel currently has `blockoverride "situation_panel_image" {}` (empty). Add a simple static background using the same icon file:
```
blockoverride "situation_panel_image" {
    icon = {
        texture = "gfx/interface/icons/situations/cc_invasion_mexico.dds"
        size = { 100 100 }
        parentanchor = top|hcenter
        position = { 0 10 }
    }
}
```

---

## 2. Fix Orphaned Events

Events 11 and 12 are defined but never triggered. Add them to `on_monthly` in `cc_invasion_mexico.txt`:
- **Event 11** ("Strains Within the Confederation") — add to the confederation-member monthly loop (2% chance), limit: non-leader members
- **Event 12** ("The Colonizers Demand Tribute") — add a new loop (3% chance) for non-confederation Mesoamerican natives with a colonial neighbor

---

## 3. New Generic Actions (4)

File: `in_game/common/generic_actions/cc_invasion_mexico.txt`

### Native Action 3 — Fortify Sacred Sites (`ccim_fortify_sacred_sites`)
- **Potential:** `is_capital_mesoamerica = yes`, `is_subject = no`
- **Allow:** `gold >= 60`, no cooldown var, situation active
- **Effect:** Pay 60 gold → apply `ccim_sacred_fortifications` modifier to self (5 years) + if in confederation, apply `ccim_divine_blessing` (3 years) to all confederation members
- **Cooldown:** `ccim_recently_fortified_sacred_sites` — 8 years
- **AI weight:** base 10, +30 if enemy border present

### Native Action 4 — Seek Tribal Alliance (`ccim_seek_tribal_alliance`)
- **Potential:** `is_capital_mesoamerica = yes`, `is_subject = no`, in confederation
- **Allow:** no cooldown var, at_war = no, situation active
- **Effect:** Fire `cc_invasion_mexico.43` (tribal alliance request) to a random neighboring native who is NOT in confederation and IS independent
- **Cooldown:** `ccim_recently_sought_tribal_alliance` — 10 years
- **AI weight:** base 15

### Colonial Action 3 — Extract Tribute (`ccim_extract_tribute`)
- **Potential:** non-mesoamerican, owns any location in mesoamerica_region
- **Allow:** no cooldown var, situation active
- **Effect:** `add_gold` equal to `(count of owned locations in mesoamerica_region) * 15` using `every_owned_location` loop + prestige bonus + apply `ccim_tribute_windfall` to self (3 years)
- **Cooldown:** `ccim_recently_extracted_tribute` — 8 years
- **AI weight:** base 30 (always attractive)

### Colonial Action 4 — Bribe Noble Faction (`ccim_bribe_noble_faction`)
- **Potential:** non-mesoamerican, has presence near mesoamerica
- **Allow:** `gold >= 80`, no cooldown var, at_war = no, situation active
- **Select trigger:** choose target native (is_capital_mesoamerica, is_subject = no, not at war with actor)
- **Effect:** Pay 80 gold → apply `ccim_native_weakness` modifier to target native (4 years) + add opinion modifier `opinion_ccim_bribed_noble` toward actor
- **Cooldown:** `ccim_recently_bribed_nobles` — 10 years
- **AI weight:** base 5, +25 if target is strong

---

## 4. New Events (6 events in 2 chains + 2 standalone)

File: `in_game/events/cc_invasion_mexico.txt`

### Native Chain A — "The High Priest Urges Action" (events 40–41)

**Event 40** (triggers monthly, 3% chance, for `is_capital_mesoamerica = yes AND NOT is_member_of_international_organization = cc_mesoamerican_confederation`):
- Title: "The High Priest Urges Action"
- Desc: Religious leaders call for sacred ceremonies to rally warriors against the foreign invaders
- Illustration: `interior` + `happy`
- Option A (ai: 65%): "Honor the old rites." → apply `ccim_divine_blessing` (3 years), trigger event 41 after 20 days
- Option B (ai: 35%): "Our warriors need steel, not prayer." → add_manpower small bonus

**Event 41** (chained from 40 Option A, no trigger block needed):
- Title: "Signs in the Sacred Smoke"
- Desc: The ceremony concludes; priests interpret the omens for what lies ahead
- Illustration: `interior` + `professional`
- Option A (ai: 70%): "A favorable omen — the gods are with us!" → prestige bonus (weak), apply `ccim_confederation_solidarity` if member, else offer to join confederation
- Option B (ai: 30%): "Dark signs — prepare for the worst." → apply `ccim_defensive_preparations` (3 years)

### Native Standalone — "Border Refugees" (event 42)

**Event 42** (triggers monthly, 2% chance, for confederation members with colonial neighbor):
- Title: "Refugees from Fallen Lands"
- Desc: Survivors from conquered neighboring peoples arrive, bringing news of the colonizers' tactics and strength
- Illustration: `exterior` + `angry`
- Option A (ai: 50%): "Integrate them into our warriors." → `max_manpower` modifier (`ccim_refugee_influx`, 3 years)
- Option B (ai: 50%): "Interrogate them for intelligence." → apply `ccim_expedition_morale` equivalent bonus + small prestige

### Colonial Chain B — "A Bold Captain Steps Forward" (events 50–51)

**Event 50** (triggers monthly, 3% chance, for colonizers with presence + colonial neighbor):
- Title: "A Bold Captain Steps Forward"
- Desc: A veteran captain volunteers to lead a daring expedition into the interior; the risk is real but the reward could be immense
- Illustration: `exterior` + `army`
- Trigger limit: no `ccim_captain_chain_cooldown` var
- Option A (ai: 55%): "Commission his expedition. [Root.GetTreasuryCost(50)|Y]" → pay 50 gold, `set_variable ccim_captain_chain_cooldown years = 8`, trigger event 51 after 15 days
- Option B (ai: 45%): "The timing is not right." → nothing

**Event 51** (chained from 50 Option A, no trigger block):
- Title: "The Captain's Report"
- Desc: `first_valid` — uses `immediate` to set var `ccim_captain_success` randomly (60% yes / 40% no)
  - If success: "The captain returns with detailed maps and intelligence — and tales of gold."
  - If failure: "The expedition met fierce resistance and retreated, though not without hard-won lessons."
- Illustration: `exterior` + `military`
- Option A (success path): "Excellent — we press our advantage." → add CB `cc_seize_mexico_native` for 6 years + apply `ccim_expedition_morale` (3 years)
- Option A (failure path): "A costly lesson." → lose prestige (weak penalty) + small manpower loss

> Note: EU5 doesn't easily branch single-option events based on immediate random vars for the option block. Use `first_valid` in desc and two explicit option blocks with `trigger = { has_variable = ccim_captain_success }` / `trigger = { NOT = { has_variable = ccim_captain_success } }` respectively.

### Colonial Standalone — "Gold Fever" (event 52)

**Event 52** (triggers monthly, 2% chance, for colonizers with owned mesoamerican locations):
- Title: "Gold Fever Grips the Camp"
- Desc: Soldiers grow restless, driven by rumors of vast treasure awaiting plunder
- Illustration: `economy` + `interior`
- Option A (ai: 60%): "Promise them a share of the spoils." → add gold 20 + `ccim_expedition_morale` (2 years) but lose prestige small
- Option B (ai: 40%): "Maintain discipline. Glory comes through order." → add prestige weak + small manpower bonus

---

## 5. New Static Modifiers (4)

File: `main_menu/common/static_modifiers/cc_event_modifiers.txt` — append new blocks:

| Modifier | Effect | Duration | Applied by |
|---|---|---|---|
| `ccim_divine_blessing` | +5% land morale, +5% max manpower | 3 years, decaying | native event 40A, fortify action |
| `ccim_sacred_fortifications` | +5% fort defense, +3% land morale | 5 years, decaying | fortify action (self) |
| `ccim_native_weakness` | -5% land morale, -5% max manpower | 4 years, decaying | bribe action (on target) |
| `ccim_tribute_windfall` | +2% monthly income | 3 years, decaying | extract tribute action |
| `ccim_refugee_influx` | +8% max manpower | 3 years, decaying | event 42 option A |

---

## 6. New Opinion Modifier

File: `in_game/common/biases/cc_invasion_mexico.txt` — append:

```
opinion_ccim_bribed_noble = {
    value = 10
    decaying_value_per_year = -3
}
```

---

## 7. Localization

File: `in_game/localization/english/cc_invasion_mexico_l_english.yml` — append all new keys:
- 4 generic action names + descriptions
- Events 40–42 (titles, descs, options)
- Events 50–52 (titles, descs, options)
- 5 new modifier names + descriptions
- 1 new opinion modifier name
- 4 action choice target prompts

---

## Files Modified / Created

| File | Change |
|---|---|
| `main_menu\gfx\interface\icons\situations\cc_invasion_mexico.dds` | **CREATE** (copy of mesoamerican.dds) |
| `in_game\gui\panels\situation\cc_invasion_mexico.gui` | Add panel image block |
| `in_game\common\situations\cc_invasion_mexico.txt` | Add events 11, 12, 40, 42, 50, 52 to `on_monthly`; add events 41, 51 via chain (no on_monthly entry needed) |
| `in_game\common\generic_actions\cc_invasion_mexico.txt` | Add 4 new actions |
| `in_game\events\cc_invasion_mexico.txt` | Add events 40–42, 50–52 |
| `main_menu\common\static_modifiers\cc_event_modifiers.txt` | Add 5 new modifiers |
| `in_game\common\biases\cc_invasion_mexico.txt` | Add `opinion_ccim_bribed_noble` |
| `in_game\localization\english\cc_invasion_mexico_l_english.yml` | Add all new loc keys |

---

## Verification

1. Launch EU V with the mod enabled
2. Start as Spain or a Mesoamerican nation (e.g., Aztec)
3. Advance to ~1490 and ensure colonial presence triggers the situation
4. Open the situation panel — confirm the mesoamerican icon appears on the tab
5. Check all 4 new generic actions appear in the action bar for the correct country types
6. Use "Extract Tribute" and "Bribe Noble Faction" as Spain; confirm gold flow and modifier appearance
7. Wait a few months — confirm events 40, 42, 50, 52 fire randomly; check events 41 and 51 chain correctly from options A
8. Check game log (`%USERPROFILE%\Documents\Paradox Interactive\Europa Universalis V\logs\`) for script errors
