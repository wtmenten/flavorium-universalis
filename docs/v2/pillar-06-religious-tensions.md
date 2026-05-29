# Pillar 06 — Religious Cabinet Tensions (Reformation Expansion)

**Related pillars:** [01 Court Rivalry](pillar-01-court-rivalry.md) (confessional clash is a rivalry trigger), [03 Scholar's Court](pillar-03-scholars-court.md) (Church condemns empiricist), [11 Cabinet Duties](pillar-11-cabinet-duties.md) (cc_duty_religious_oversight)

---

## Theme

The Reformation split courts across Europe. Cabinets didn't just advise on faith — they *were* the battleground. This expansion adds cabinet-driven religious conflict events, especially powerful in Ages 4–5.

---

## What It Adds

### A. The Confessional Cabinet (New Traits — expand Family C)

5 new conditional traits for religious alignment, added to `cc_conditional_traits.txt`:

| Trait | Condition | Age |
|-------|-----------|-----|
| `lutheran_consistory_advisor` | Country religion = Protestant | Age 4+ |
| `tridentine_reformist` | Country religion = Catholic + post-1545 | Age 4+ |
| `calvinist_disciplinarian` | Country religion = Reformed | Age 4–5 |
| `sufi_court_mystic` | Country religion = Sunni/Shia | Age 3–5 |
| `brahmin_orthodox` | Country religion = Hindu | Age 3+ |

These are `category = cabinet` traits (occupy the main cabinet slot) — they are the minister's *defining identity*, not a secondary tag like Family G.

### B. The Confession Clash Events

Fires when a cabinet contains members of different confessional traits, or when a confessional minister is present in a country undergoing religious change:

**"A Debate at Court"**
The Catholic minister and the secretly-Protestant minister are found arguing theology. Options:
- Mediate → religious unity maintained, cabinet loyalty neutral
- Side with the Catholic → Protestant minister leaves or gains negative trait
- Side with the Protestant → Catholic minister leaves, Pope/clergy opinion hit

**"The Secret Correspondence"**
A cabinet member is found corresponding with foreign heretics/reformers. Options:
- Execute → prestige gain, martyrdom chain may fire (international opinion event)
- Expel → opinion hit with the minister's aligned country
- Cover it up → corruption risk, negative trait `cynical_courtier` for the ruler's court

**"The Conversion"**
A cabinet member converts. Options depend on country tolerance level:
- Intolerant country → forced choice: fire them or accept religious tensions
- Tolerant country → keep them with a minor unity hit

### C. The Inquisitor's Report

For countries where a `zealous_inquisitor` cabinet member (v0.1) is present: new cabinet action `cc_inquisitorial_review`. The minister runs a formal examination of the court's religious conformity.
- Costs: chance to remove another valuable minister (random target with faith-adjacent suspicion)
- Benefits: +religious unity, +devotion (Catholic) or +fervor (Protestant)
- Duration: 5-year cooldown

---

## Historical Echoes

- The Saxon Crypto-Calvinist crisis (1591) — cabinet members secretly converted; the great purge followed
- Cardinal Granvelle in Philip II's Netherlands cabinet — his presence alone radicalized Protestant opposition
- The Ottoman Şeyhülislam — the Grand Mufti's formal role in authorizing (or blocking) policy
- The English Privy Council during the Reformation — cabinet members executed for their faith under Henry, Edward, and Mary

---

## New Files Needed

| File | Purpose |
|------|---------|
| `common/traits/cc_confessional_traits.txt` | 5 new confessional traits (add to Family C) |
| `events/cc_reformation_events.txt` | Confession clash events + Inquisitor chain |
| `common/cabinet_actions/cc_inquisitorial_review.txt` | Inquisitorial review cabinet action |
| Localization `.yml` | Trait names, event text, action name |

---

## Implementation Notes

- Confessional traits require `potential` blocks checking both religion AND age: `has_game_started_with_age = age:age_of_reformation` or similar.
- The `secret_correspondence` event should use a hidden flag `cc_secret_correspondence_known` to prevent re-firing.
- `cc_duty_religious_oversight` ([Pillar 11](pillar-11-cabinet-duties.md)) boosts confession clash event frequency.
- The inquisitorial review is a progress-based cabinet action: the minister works over time, not an instant effect.
