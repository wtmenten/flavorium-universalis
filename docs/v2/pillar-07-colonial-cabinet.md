# Pillar 07 — The Colonial Divan (Overseas Cabinet)

**Related pillars:** [02 Estate Factions](pillar-02-estate-factions.md) (burgher-aligned minister pushes company expansion), [11 Cabinet Duties](pillar-11-cabinet-duties.md) (cc_duty_colonial_posting), [12 Stepping Stone Traits](pillar-12-stepping-stone-traits.md) (Chain E: colonial pioneer path)

**Prerequisite:** v0.1 subject types must be active (`chartered_company`, `colonial_nation`, `provincial_governorate`)

---

## Theme

As European powers expanded overseas, their cabinets didn't stay home — they were tasked with managing new worlds. This expansion adds colonial-specific cabinet mechanics for nations with chartered companies, colonial nations, and governorates.

---

## What It Adds

### A. The Colonial Posting Mechanic

A new/reworked cabinet action: `cc_post_minister_overseas`. A cabinet member can be posted to a colonial nation or chartered company subject. While posted:

- The depending on the  minister's trait,  apply a country modifier to the colonial subject (e.g., `capable_explorer` accelerates reduces exploration cost ; `efficiency_administrator` boosts subject income, pop growth, etc.) use a small handful of semi generic modifiers mapped to traits
- Yearly event fires: *"The Governor's Dispatch"* — flavor report from the colony with choices
- Risk events may fire: corruption, native revolt, or disease (which can grant negative traits)
- After 10 years of posting, the minister may return with a *colonial experience* trait:
  - `frontier_administrator` (already exists in v0.1) — earned through administrative success
  - `returned_colonial_governor` *(new)* — strong colonial modifiers, earned through any completed posting
  - set this duration in the cabinet action.

See [Chain E in Pillar 12](pillar-12-stepping-stone-traits.md) for the full `restless_pioneer → frontier_administrator → returned_colonial_governor` progression.

### B. Charter Company Events

For countries with the `chartered_company` subject type:

**"The Company's Accounts"** (yearly if chartered company exists + `merchant_of_the_crown` or `efficiency_administrator` in cabinet)
The minister reviews the charter company ledgers. Options reveal corruption or profit. Outcomes range from windfall income to an investigation that removes a corrupt governor.

**"A Monopoly Dispute"** (fires if burgher-aligned minister is present)
The burgher estate petitions to expand trading rights. The `merchant_of_the_crown` minister pushes for it; noble-aligned ministers resist. Ruler mediates or takes sides.

**"The Governor's Letter"** (fires if a minister is posted overseas)
The posted minister requests more troops or funding. Choice affects colonial loyalty dimension (links to v0.1 bond tracking system).

### C. The Decolonization Crisis (Age 6)

If a colonial nation has high liberty desire AND a `revolutionary_agitator` cabinet member (in either the colonial nation or the mother country), a crisis chain fires:
- *"The Colonial Petition"* — the colonial cabinet member writes a formal demand for greater autonomy
- *"The Defection"* — if the crisis is ignored, the revolutionary minister may defect to the independence movement
- *"The Compromise"* — granting autonomy prevents defection but grants the colonial nation a special upgrade path

---

## Historical Echoes

- The VOC's Heren XVII board directing governors in Batavia — home-cabinet control over distant colonies
- The East India Company's dual civilian/military structure — a posted cabinet creating its own power base
- Colbert's Compagnie des Indes — state-directed colonialism through ministerial appointment
- The Marquis de Pombal's Portuguese colonial reforms — a single minister transforming empire from the cabinet
- The American colonial crisis — governors loyal to crown vs. local assemblies

---

## New Files Needed

| File | Purpose |
|------|---------|
| `events/cc_colonial_events.txt` | Charter company events (B), decolonization crisis (C) |
| `events/cc_colonial_posting_events.txt` | Annual posting dispatch + risk events (A) |
| `common/country_interactions/cc_post_minister_overseas.txt` | Overseas posting interaction |
| Localization `.yml` | Event text, interaction name, new trait |

---

## Implementation Notes

- `returned_colonial_governor` is a new trait — add to `cc_conditional_traits.txt` (Family F action-forged traits).
- The posting interaction needs to select a subject (select_trigger = `looking_for_a = country` filtered to colonial subjects).
- Liberty desire triggers: verify exact trigger name — from CLAUDE.md, `has_war_with` → `is_at_war_with`. Confirm liberty desire trigger exists.
- Bond tracking integration: posted minister's choices should shift the relevant bond dimension using the existing v0.1 bond variable system.
