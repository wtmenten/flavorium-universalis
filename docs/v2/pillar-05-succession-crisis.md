# Pillar 05 — The Succession Crisis Cabinet

**Related pillars:** [02 Estate Factions](pillar-02-estate-factions.md) (estate-aligned ministers push agendas during regency), [04 War Council](pillar-04-war-council.md) (succession war events share cabinet choices)

---

## Theme

Succession was the defining drama of early modern statecraft. Who sits on the council during a regency? Who does the cabinet serve when the king is dying? This expansion ties the cabinet to succession and regency events — making the composition of your court a genuine stake in dynastic politics.

---

## What It Adds

### A. Regency Council Events

Fires when a regency triggers (minor heir). Based on cabinet composition:

**"The Regent's Men"** (fires on regency start)
Each cabinet member either supports the regent or begins scheming. Estate-aligned ministers (Family G from [Pillar 02](pillar-02-estate-factions.md)) push estate agendas during the regency window. Options define the regent's relationship with the cabinet.

**"The Regent's Favorite"** (fires 2 years into regency if regent is present)
One cabinet member (highest DIP score) becomes the regent's favorite. Gains temporary `court_favorite` character modifier:
- +opinion from all estates
- Risk of `court_tension` if there are rivals ([Pillar 01](pillar-01-court-rivalry.md))

**"The Coming of Age"** (fires when ruler reaches majority)
The newly adult ruler assesses the regency council:
- Keep the favorites → builds court loyalty, modest prestige cost
- Dismiss all → prestige loss, but full ruler control restored
- Dismiss rivals only → moderate prestige cost, targeted faction purge

### B. Succession War Cabinet Events

If a PU claim fires or a succession war begins, cabinet choices mirror War Council ([Pillar 04](pillar-04-war-council.md)) but are framed diplomatically:

- `diplomatic_attache` → lobby foreign courts to soften opposition (opinion gain with neutral powers)
- `master_statesman` → negotiate a compromise peace before the war escalates
- `hawk_minister` → push for military resolution — locks early peace options, escalates conflict

### C. The Heir's Mentor

Expansion of the existing legacy/mentorship system (v0.1). A new country interaction: `cc_assign_mentor`. One cabinet member is formally assigned as the heir's mentor. Their traits influence heir education outcomes:

| Mentor Trait | Heir Outcome |
|-------------|-------------|
| `humanist_philosopher` | Scholar ruler (+ADM tendency) |
| `standing_army_advocate` | Martial ruler (+MIL tendency) |
| `court_prelate` | Pious ruler (+religious traits tendency) |
| `master_statesman` | Diplomatic ruler (+DIP tendency) |
| `progressive_reformist` | Reform-minded ruler |

---

## Historical Echoes

- Anne of Austria and Mazarin — the cardinal effectively ruled through the regency, reshaping the cabinet entirely
- Catherine de Medici — managed three sons' reigns, maintaining her own factional position throughout
- The Ottoman Köprülü vizier family — seized control during weak sultans' reigns, reforming and stabilizing the Divan
- Edward VI's regency council in England — the Duke of Somerset vs. the Duke of Northumberland

---

## New Files Needed

| File | Purpose |
|------|---------|
| `events/cc_regency_events.txt` | Regency council events (A), succession war choices (B) |
| `common/country_interactions/cc_assign_mentor.txt` | Heir's mentor assignment |
| Localization `.yml` | Event text, interaction name |

---

## Implementation Notes

- Hook into `on_new_ruler` and the regency on-actions. Verify which on-action fires specifically for regency start (may need `is_regent = yes` check inside a more general character on-action).
- `court_favorite` is a timed character modifier (duration = regency length, or fixed 10 years).
- The mentor interaction should check `has_heir = yes` and that the target character is a cabinet member.
- Mentor effects: use the same `add_adm/dip/mil` mechanism confirmed in `cc_legacy_events.txt`.
