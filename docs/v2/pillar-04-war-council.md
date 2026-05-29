# Pillar 04 — The War Council (Military Cabinet Expansion)

**Related pillars:** [05 Succession Crisis](pillar-05-succession-crisis.md) (succession war events share cabinet choices), [11 Cabinet Duties](pillar-11-cabinet-duties.md) (cc_duty_war_council boosts event rates), [12 Stepping Stone Traits](pillar-12-stepping-stone-traits.md) (military chain traits gate events)

---

## Theme

Cabinets in this era were intimately involved in military administration — not just tactics but logistics, recruitment, financing war, managing generals. This expansion adds a *War Council* event system that fires during wars and links cabinet composition to military outcomes.

---

## What It Adds

### A. War Council Events

Fire on `on_war_declared` and `yearly_country_pulse` while at war. Each event draws on which military-adjacent cabinet traits are present:

**"The Council of War"** (yearly while at war)
Options shaped by which cabinet members are present:
- `standing_army_advocate` → push for risky offensive (army morale bonus, war support risk)
- `defensive_commander` → counsel patience (fort defense buff, war support stable)
- `hawk_minister` → demand no peace short of total victory (locks peace options for 2 years, prestige reward)
- No military traits present → generic options only

**"Financing the War"** (fires if treasury < 3× monthly income during war)
- `efficiency_administrator` / `treasury_enforcer` → squeeze population (manpower + unrest)
- `merchant_of_the_crown` (Family G) → recommend war loans (interest cost, no manpower hit)
- Neither present → plain gold drain options only

**"The General's Request"** (fires if a `supreme_commander` or `outdated_general` is present)
- Refuse → general gains negative relationship
- Accept → costs gold, army gets temporary morale buff

### A2. Cabinet Duties Integration

Ministers on `cc_duty_war_council` generate War Council events at **2× base rate**. Ministers on `cc_duty_free_hands` generate them at base rate. This is the primary way a player signals they are in a war-footing. See [Pillar 11](pillar-11-cabinet-duties.md).

### B. Military Reform Chain (Post-War)

After winning a major war (>50 war score), a `military_reform_opportunity` flag is set for 5 years. Within that window, cabinet members with military traits trigger reform proposals:

| Minister Trait | Reform Proposal | Cost | Reward |
|----------------|----------------|------|--------|
| `standing_army_advocate` | Standing army reform | Noble estate displeasure | Army maintenance modifier |
| `commissariat_officer` | Supply reform | Bureaucracy impact | Attrition reduction modifier |
| `siege_engineer` | Fortification doctrine | Treasury | Fort maintenance modifier |

Each reform is a 2–3 event chain inspired by the military revolution of 1560–1660.

### C. Outdated General Resolution

The existing `outdated_general` negative trait (v0.1) gains a resolution path: War Council events give specific options to "retire" the outdated general through a formal council decision, clearing the negative trait.

---

## Historical Echoes

- Louvois under Louis XIV — the war minister's systematic reform of French army administration
- Maurice of Nassau's military revolution — Dutch council-driven doctrine changes
- Gustavus Adolphus's war council — cabinet and commander working in concert
- The Habsburg Hofkriegsrat — the institutionalized war council with formal ministerial roles

---

## New Files Needed

| File | Purpose |
|------|---------|
| `events/cc_war_council_events.txt` | War council event chains (A + B + C) |
| `common/on_action/cc_war_on_actions.txt` | Hook into `on_war_declared` for initial council event |
| Localization `.yml` | Event text, modifier names |

---

## Implementation Notes

- Use `at_war = yes` trigger in biyearly/yearly pulse limiters — not `has_war_with`.
- The `military_reform_opportunity` flag is a country-level variable set via effect, checked by biyearly pulse.
- Military reform chain modifiers are timed static modifiers (10–20 years), not permanent.
- War Council events should check `NOT = { is_in_siegable_fort = yes }` to avoid awkward timing (if that trigger exists; verify against vanilla).
