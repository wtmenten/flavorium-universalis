# Pillar 09 — Dynamic Cabinet Composition Auto-Modifiers

**Related pillars:** [02 Estate Factions](pillar-02-estate-factions.md) (balanced_court modifier lives here), [12 Stepping Stone Traits](pillar-12-stepping-stone-traits.md) (stepping stone traits feed into military-heavy/scholar triggers)

---

## Theme

The sum of the cabinet should feel different depending on its composition. v0.1 handles individual traits and synergy pairs. v2.0 adds *aggregate* auto-modifiers that respond to the overall cabinet profile — no events required, just live dynamic conditions.

---

## What It Adds

All entries live in a single new file: `common/auto_modifiers/cc_cabinet_composition.txt`

Auto-modifiers are applied automatically based on live conditions, without explicit `add_modifier` effects.

### A. Military-Heavy Cabinet — `warlord_court`

- **Trigger:** 3+ cabinet members with military-type traits (`standing_army_advocate`, `siege_engineer`, `cavalry_marshal`, `commissariat_officer`, `elite_trainer`, `mass_levy_commander`, `offensive_strategist`, `defensive_commander`, `supreme_commander`, `outdated_general`)
- **Effects:** +discipline, +army morale recovery, -diplomatic reputation, -estate satisfaction (estates fear a coup)

### B. Commercial Cabinet — `merchant_republic_spirit`

- **Trigger:** 3+ cabinet members with trade/economic traits (`merchant_syndic`, `trade_consortium_minister`, `merchant_of_the_crown`, `prosperity_herald`, `capitalist_minister`, `free_market_advocate`, `mercantilist_official`)
- **Effects:** +trade efficiency, +income from subjects, -manpower recovery, -noble estate satisfaction

### C. Scholar Cabinet — `enlightened_court`

- **Trigger:** 2+ empiricist/rationalist traits (`empiricist_counselor`, `renaissance_humanist`, `humanist_philosopher`, `progressive_rationalist`, `chief_cartographer`, `enlightenment_herald`)
- **Effects:** +technology cost reduction, +development growth, -prestige from military victories

### D. Divided Cabinet — `court_paralysis` (negative)

- **Trigger:** Cabinet contains 2+ traits from *opposing* societal-axis poles (e.g., `royal_absolutist` + `liberal_reformer`, `hawk_minister` + `peacemaker_counselor`)
- **Effects:** +decision cooldown, -stability recovery speed; but +probability of unique "compromise" events from [Pillar 01](pillar-01-court-rivalry.md)

### E. Ancient Cabinet — `entrenched_court`

- **Trigger:** Proxy: all cabinet members are age 55+ (representing a long-tenured, ossified court)
- **Effects:** +stability, -reform progress speed, -adaptiveness modifier. Represents the fossilization of aristocratic courts.

### F. Balanced Court — `balanced_court`

- **Trigger:** No single estate has more than 1 estate-aligned minister (Family G from [Pillar 02](pillar-02-estate-factions.md)); AND no military/commercial/scholar threshold is met
- **Effects:** Small bonuses across ADM, DIP, MIL efficiency — the reward for a generalist cabinet

---

## Historical Echoes

- The fossilization of the Ottoman Divan in the late 16th century — `entrenched_court` in action
- The "military party" vs. "peace party" in Philip II's council — `court_paralysis` producing policy deadlock
- The Walpolean commercial Whig cabinet — `merchant_republic_spirit` at its peak
- The Encyclopédiste-influenced French cabinet of the 1770s — `enlightened_court`

---

## New Files Needed

| File | Purpose |
|------|---------|
| `common/auto_modifiers/cc_cabinet_composition.txt` | All 6 auto-modifiers above |
| Localization `.yml` | Modifier names and descriptions |

---

## Implementation Notes

- This is the **lowest-risk, highest-reward pillar** to implement first. No events, no interactions — purely declarative data.
- Auto-modifiers use `potential_trigger` for complex logic and `limit` for simple inequalities only (CLAUDE.md gotcha: `limit` in auto_modifiers doesn't support full trigger syntax).
- `court_paralysis` opposing trait check: may require counting via multiple `any_cabinet_character` blocks since `count_cabinet_characters` doesn't exist (CLAUDE.md gotcha).
- `entrenched_court` age proxy: use `NOT = { any_cabinet_character = { age < 55 } }` — fires only when no cabinet member is under 55.
- Modifier descriptions should be evocative, not mechanical: "The council speaks with one martial voice..." not "army_morale +0.1".
