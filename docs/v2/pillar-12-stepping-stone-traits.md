# Pillar 12 — Stepping Stone Traits (Progressive Trait Chains)

**Related pillars:** [01 Court Rivalry](pillar-01-court-rivalry.md) (rival pairs reference chains), [04 War Council](pillar-04-war-council.md) (military chain traits gate events), [07 Colonial Cabinet](pillar-07-colonial-cabinet.md) (Chain E), [11 Cabinet Duties](pillar-11-cabinet-duties.md) (domestic reform duty accelerates chains)
**Priority:** Tier 1 (implement before other pillars write events that reference chain traits)

---

## Theme

Not every great minister was born great. Some traits should be *earned* through struggle — a minister who fumbles an early assignment and learns from it; a veteran of many wars who slowly hardens into a master of his craft. This pillar adds trait progression chains, where weaker traits are prerequisites for reaching more powerful later ones.

This also prompts a structural reconsideration of existing "flat" traits that could benefit from being part of a chain.

---

## Technical Foundation

Traits cannot have `on_gain` effect blocks — chains are implemented via *events*:
1. A Tier 0 stepping stone trait's `allow` block makes it available (and makes the next tier *not* available yet)
2. When progression conditions are met, an event fires: `remove_trait = stone_trait`, `add_trait = advanced_trait`
3. The advanced trait's `allow` block checks for a flag set by the progression event (proving the minister went through the chain)

Skill score changes use `add_adm`, `add_dip`, `add_mil` (character-scoped effects, confirmed in `cc_legacy_events.txt`).

---

## Skill Score Progression

A core design goal: minister skill scores should grow through events, not just static assignment.

| Outcome | Effect |
|---------|--------|
| Successful stepping stone event | Random bump in **1–5 range** for the relevant skill |
| Chain advancement (Tier 0 → Tier 1) | Random bump in **1–5 range** (reliable on chain advance) |
| Disaster/failure outcome | Random reduction in **1–5 range**, OR gain a negative trait (player's choice where available) |

**Implementation:** Use `random_list` with equal-weight 1–5 entries if `add_adm = { min = 1 max = 5 }` syntax is not supported — verify before implementation.

**Goal:** A minister who started as a `fumbling_reformist` with ADM 45 might reach `master_reformer` with ADM 55+ after a full career. Progression feels earned through play.

**Duty interaction:** Ministers on `cc_duty_domestic_reform` ([Pillar 11](pillar-11-cabinet-duties.md)) accumulate progression events at ~2× rate. Specializing speeds growth but narrows the minister.

---

## Progression Chains

### Chain A — The Reformer's Path (Administrative)

```
fumbling_reformist (new, Tier 0)
    ↓  [5–10 years + reform events]
law_reformer (existing, Tier 1)
    ↓  [5–10 years + successful events]
progressive_reformist (existing, Tier 2, kiss-curse)
    ↓  [10+ years as progressive_reformist]
master_reformer (new, Tier 3)
```

- `fumbling_reformist` (Tier 0): minister attempting reform but causing confusion. Mild stability penalty.
- `master_reformer` (Tier 3): legendary reform architect, unlocked only after holding `progressive_reformist` for 10+ years.

---

### Chain B — The Integrator's Path (Administrative)

The existing `fumbling_integrator → able_integrator → master_integrator → iron_integrator` progression already exists but is currently awarded by attribute score alone. This chain should be partially **event-driven** — requiring the minister to have managed an integration cabinet action to unlock `able_integrator` and beyond.

**Change:** Update `allow` blocks on `able_integrator` to also check for a flag set when the minister completes an `integrate_province` or `integrate_area` action.

---

### Chain C — The Diplomat's Ascent (Diplomatic)

```
tentative_envoy (new, Tier 0)
    ↓  [3–8 years + diplomatic events]
tactful_envoy (existing, Tier 1)  ──or──  diplomatic_attache (existing, conditional)
    ↓  [further events + cc_duty_diplomatic_mission]
master_statesman (existing, Tier 2)
```

- `tentative_envoy` (Tier 0): inexperienced negotiator; small diplomatic reputation penalty.
- Branch at Tier 1: `tactful_envoy` (generalist) or `diplomatic_attache` (posted specialist, requires duty assignment).

---

### Chain D — The Military Hardening (Military)

```
green_adjutant (new, Tier 0)
    ↓  [5+ years + war exposure events]
tactical_advisor (existing, Tier 1)
    ↓  [war council events + specific decisions]
standing_army_advocate (existing, conditional)  ──or──  defensive_commander (existing)
    ↓  [continued military events]
supreme_commander (existing, conditional)
```

- `green_adjutant` (Tier 0): newly appointed military minister; minor discipline penalty. Granted at country entry into Age 2 for military-priority countries.
- `standing_army_advocate` requires `tactical_advisor` as prerequisite (update `allow` block).

---

### Chain E — The Colonial Pioneer (Exploration)

```
restless_pioneer (existing, Tier 3)
    → [becomes a stepping stone, not a flat trait]
    ↓  [colonial posting events via Pillar 07]
frontier_administrator (existing, conditional)
    ↓  [10 years of colonial posting + crisis events]
returned_colonial_governor (new, Tier 3+)
```

- `restless_pioneer` is currently flat; it becomes the entry point for the colonial path.
- `returned_colonial_governor` (new): strong colonial modifiers, earned only through a completed `cc_duty_colonial_posting` posting.

---

### Chain F — The Fiscal Path (Administrative)

```
clumsy_accountant (new, Tier 0)
    ↓  [5–8 years + treasury events]
loyal_steward (existing, Tier 1)
    ↓  branch:
    ├── prosperity_planner (existing, Tier 1 → Tier 2 branch)
    └── [continued fiscal events]
        ↓
        treasury_enforcer (existing, action-forged)
```

- `clumsy_accountant` (Tier 0): new to treasury work; small income penalty.
- `prosperity_planner` and `loyal_steward` are currently parallel; `loyal_steward` becomes the gateway.

---

## Design Rules

- All Tier 0 traits should have a **mild negative modifier** — they're not where you want to stay
- Progression to Tier 1: 5–10 years under `cc_duty_domestic_reform`; 10–15 years on free hands
- Each chain branches at Tier 2 so the player doesn't feel railroaded
- Existing traits becoming chain-linked need their `allow` blocks updated to check for the prerequisite flag
- Never remove trait access entirely — a high-attribute character can still get Tier 1+ directly (the chains are an *alternative* path, not a gate)

---

## New Files Needed

| File | Purpose |
|------|---------|
| `common/traits/cc_progression_traits.txt` | New Tier 0 traits (`fumbling_reformist`, `tentative_envoy`, `green_adjutant`, `clumsy_accountant`) + new endpoints (`master_reformer`, `returned_colonial_governor`) |
| `events/cc_progression_events.txt` | Progression event chains for all 6 chains; includes `add_adm/dip/mil` bumps |
| Update `common/traits/cabinet.txt` | Update `allow` blocks on existing traits that become chain members |
| Update `common/traits/cc_conditional_traits.txt` | Update `allow` blocks on existing conditional traits |
| Localization `.yml` | New trait names, event text |
