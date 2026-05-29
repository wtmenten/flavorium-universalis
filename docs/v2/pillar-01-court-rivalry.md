# Pillar 01 — Court Rivalry & Cabinet Intrigue

**Related pillars:** [02 Estate Factions](pillar-02-estate-factions.md) (estate-aligned ministers fuel feuds), [03 Scholar's Court](pillar-03-scholars-court.md) (scholastic/empiricist clashes), [06 Religious Tensions](pillar-06-religious-tensions.md) (confessional clashes), [12 Stepping Stone Traits](pillar-12-stepping-stone-traits.md) (rival trait chains)

---

## Theme

No court is a harmony. Ministers scheme, philosophies clash, egos collide. This system introduces *interpersonal cabinet dynamics* — pairs of cabinet members who develop rivalries or alliances over time, and the dramatic events those relationships create.

---

## What It Adds

### A. The Rivalry System

Cabinet pairs can become rivals if they share opposing conditional traits (e.g., `royal_absolutist` vs `liberal_reformer`, `hawk_minister` vs `peacemaker_counselor`). A hidden variable `cabinet_rivalry_X_Y` accumulates through:
- Opposing votes in parliament issues
- Sharing the same societal-axis pole (competition, not opposition)
- One cabinet member's event outcome publicly humiliating another

Once a threshold is crossed, the country gets a `court_tension` modifier and a new event chain fires:

- *"The Minister's Complaint"* — one minister demands the ruler choose sides
- *"A Letter Unsealed"* — evidence of scheming appears; ruler can purge, reconcile, or exploit
- *"The Faction Hardens"* — if unresolved, the weaker minister may defect to an enemy, spawning a CB or triggering a disaster

### B. Cabinet Alliance (Cabal)

Opposite of rivalry: two cabinet members with *complementary* traits (e.g., `parliamentary_broker` + `master_statesman`) develop a cabal. Benefits:
- Shared trait effects stack harder
- Joint decisions unlock (e.g., "Joint Reform Proposal")
- Estate power effect of the cabal's aligned estate is also greatly increased

Downside: if one is fired, the other's loyalty drops sharply.

### C. The Purge Decision

A new country interaction: `dismiss_rival_minister`. Costs prestige, may trigger estate displeasure if the dismissed member was estate-aligned (see [Pillar 02](pillar-02-estate-factions.md)). Unlocks only when the `court_tension` modifier is present.

---

## Historical Echoes

- Richelieu vs. Marie de Medici — the cardinal systematically purged every rival faction from Louis XIII's court
- Süleyman's Pargalı Ibrahim and Rüstem Pasha — the grand vizier system saw successive favorites rise and fall
- Walpole's patronage politics — the Whig cabinet maintained dominance by systematically excluding Tories
- Cromwell's court — the Army Council vs. civilian Parliament produced constant factional tension

---

## New Files Needed

| File | Purpose |
|------|---------|
| `events/cc_rivalry_events.txt` | Rivalry escalation chain (complaint → letter → faction hardens) |
| `events/cc_cabal_events.txt` | Cabal formation + joint decision unlocks |
| `common/biases/cc_court_relations.txt` | New opinion modifiers for purge/reconcile outcomes |
| Localization `.yml` | Event text, modifier names |

---

## Implementation Notes

- Rivalry seeds are dense in existing content: the societal-axis conditional traits (Family B, 17 axes × 2 poles) provide natural opposition pairs. No new trait definitions required.
- The `court_tension` modifier should be a country-level static modifier (manual add/remove).
- Hidden rivalry variable accumulation: use `change_variable` on the country scope, checked by biyearly pulse.
- Purge interaction file goes in `common/country_interactions/cc_purge_rival.txt`.
