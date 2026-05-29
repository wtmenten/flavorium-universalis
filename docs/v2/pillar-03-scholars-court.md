# Pillar 03 — The Scholar's Court (Scientific Revolution)

**Related pillars:** [01 Court Rivalry](pillar-01-court-rivalry.md) (scholastic vs. empiricist clash), [06 Religious Tensions](pillar-06-religious-tensions.md) (Church condemns the empiricist), [11 Cabinet Duties](pillar-11-cabinet-duties.md) (cc_duty_scholarly_inquiry)

---

## Theme

Ages 5 and 6 brought absolutism and revolution — but also Galileo, Newton, Descartes, and the Royal Society. This expansion adds an *empiricist court* event chain for countries that cultivate rational cabinet members, culminating in a Scientific Academy building.

---

## What It Adds

### A. The Rationalist Chain (Age 5–6 Events)

Fires for countries with 2+ empiricism-adjacent cabinet members (existing traits: `empiricist_counselor`, `industrial_visionary`, `humanist_philosopher`, `renaissance_humanist`):

**Act I: "A Treatise Arrives at Court"**
A foreign scholar submits a work. Options:
- Fund the research → +1 empiricist trait chance for a cabinet member
- Dismiss it → safe, no effect
- Consult the clergy → triggers clergy displeasure if Reformation is active (see [Pillar 06](pillar-06-religious-tensions.md))

**Act II: "The Demonstration"**
The empiricist minister stages a public experiment. Outcomes vary:
- Rivals in cabinet mock it → rivalry trigger ([Pillar 01](pillar-01-court-rivalry.md))
- Ruler is impressed → unique country modifier `enlightened_curiosity` (5 years)
- The Church condemns it → religious tension, possible `discredited_empiricist` negative trait

**Act III: "The Royal Academy Decision"**
If Acts I and II resolved favorably, unlocks a decision to found the `royal_academy` building. The decision button fires from this event, bypassing the need for a standalone decisions file.

### B. The Scholastic Backlash

If 2+ theology/religion-aligned cabinet members are present *while* the rationalist chain is active, a counter-chain fires:
- The scholastic minister formally accuses the empiricist of heresy
- Ruler must choose sides — one or both ministers may be removed
- New negative trait: `discredited_empiricist` — available for the "survivor" of the accusation

### C. New Building: Royal Academy of Sciences

| Property | Value |
|----------|-------|
| Requires | Age 5 advance (scholarly orders line) |
| Location | Capital only |
| Modifier type | `capital_country_modifier` |
| Effects | +monthly development, +heir education speed, accelerates empiricist trait grant |
| Flavor basis | France's Académie (1666), England's Royal Society (1660), Prussia's Akademie (1700) |

---

## Historical Echoes

- Leibniz at the Brandenburg-Prussian court — patron-supported scholarship as state policy
- Colbert's patronage of sciences in France — the Academy was a tool of absolutist prestige
- Peter the Great importing Western empiricists — modernization driven by court-level decisions
- The Galileo affair — patronage of empiricism was always contested by ecclesiastical power

---

## New Files Needed

| File | Purpose |
|------|---------|
| `events/cc_scholar_events.txt` | Rationalist chain (Acts I–III) + scholastic backlash |
| `common/building_types/cc_academy_building.txt` | Royal Academy of Sciences building |
| Localization `.yml` | Event text, building name, modifier names |

---

## Implementation Notes

- The `royal_academy` building is capital-only; use `capital_country_modifier` not `modifier`. See CLAUDE.md gotcha: `modifier = {}` is location-only.
- `enlightened_curiosity` is a timed static modifier (5 years), manually added/removed.
- `discredited_empiricist` is a new negative trait — add to `cc_negative_traits.txt` with a rehabilitation path.
- Duty boost: ministers on `cc_duty_scholarly_inquiry` ([Pillar 11](pillar-11-cabinet-duties.md)) should have Act I fire at 2× frequency.
