# Pillar 02 — Estate-Aligned Cabinet Factions

**Related pillars:** [01 Court Rivalry](pillar-01-court-rivalry.md) (estate ministers fuel feuds), [09 Auto-Modifiers](pillar-09-auto-modifiers.md) (estate-captured modifier), [11 Cabinet Duties](pillar-11-cabinet-duties.md) (cc_duty_parliament_management)

---

## Theme

Real historical cabinets were not neutral technocrats — they were the spokesmen of landed nobles, wealthy merchants, or powerful clergy. This system ties each cabinet member to an estate, making the cabinet a site of *factional politics*.

---

## What It Adds

### A. Estate Affiliation Trait Family (Family G)

7 new traits marking estate allegiance, one per estate slot.

**Critical technical note:** These use **`category = health`** — not `category = cabinet`. This allows a character to hold *both* their main cabinet trait and an estate affiliation trait simultaneously without overwriting. Health traits are always active while the character is alive in the country, so **all direct modifiers must be tiny** (±0.05 or less). The real gameplay impact comes from the events they gate and the estate power amplification they provide.

| Trait | Estate | Tiny Modifier | Primary Effect |
|-------|--------|---------------|----------------|
| `noble_champion_of_court` | Nobles | +0.05 prestige/month | Noble estate power greatly amplified by this minister's cabinet presence |
| `merchant_of_the_crown` | Burghers | +0.05 trade efficiency | Burgher estate power greatly amplified |
| `court_prelate` | Clergy | +0.05 devotion/month | Clergy estate power greatly amplified |
| `tribune_of_the_commons` | Peasants | +0.02 stability/month | Gates peasant-faction events |
| `steppe_voice` | Tribes | +0.05 horde unity | Nomad-only |
| `dhimmi_advocate` | Dhimmi | +0.02 tolerance | Gates minority tension events |
| `cossack_hetman_liaison` | Cossacks | +0.02 loyalty | Ukrainian/Polish corridor countries only |

The primary gameplay impact: an estate-aligned minister **greatly amplifies the power that estate gains from cabinet representation** — they are overtly the creature of their estate, not merely sympathetic.

### B. Cabinet Faction Balance Events

If 3+ cabinet members are aligned to the *same* estate, a `cabinet_captured` static modifier fires on the country. The captured estate gains disproportionate power. Periodic events test the ruler's control:

- *"The Nobles Demand"* — the noble faction pushes a sweeping privilege; refuse and risk losing a minister
- *"The Merchant Compact"* — burgher-aligned ministers propose selling a subject for treasury gain
- *"The Holy Inquisition in the Cabinet"* — clergy ministers push for forced conversion of a court member

### C. The Balanced Cabinet Bonus

If no single estate holds more than 1 aligned minister: `balanced_court` auto-modifier fires (see [Pillar 09](pillar-09-auto-modifiers.md)), providing small bonuses across all categories. Historically, the most effective rulers were those who played estates against each other.

---

## Historical Echoes

- The Swedish Riksdag — four estates each had formal cabinet representation
- The Spanish Council of Castile — noble, ecclesiastical, and commercial interests fought for council seats
- The Ottoman Divan — devshirme (slave-soldier) viziers vs. Turkish noble faction was a constant structural tension

---

## New Files Needed

| File | Purpose |
|------|---------|
| `common/traits/cc_estate_faction_traits.txt` | Family G traits (category = health, tiny modifiers only) |
| `events/cc_estate_faction_events.txt` | Faction balance events, captured cabinet chains |
| `common/auto_modifiers/cc_cabinet_balance.txt` | balanced_court + cabinet_captured auto-modifiers |
| Localization `.yml` | Trait names, event text |

---

## Implementation Notes

- Do NOT use `category = cabinet` for Family G — must be `category = health` to avoid slot conflict.
- Verify that health-category traits show in the character portrait tooltip alongside cabinet traits.
- `cabinet_captured` modifier: country-scope auto-modifier, trigger = `count_family_g_aligned_to_same_estate >= 3` (use scripted values or stacked `any_cabinet_character` checks).
- `balanced_court` modifier lives in `cc_cabinet_composition.txt` alongside other auto-modifiers from Pillar 9.
