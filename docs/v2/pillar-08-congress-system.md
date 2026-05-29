# Pillar 08 — The Congress System (International Cabinet Diplomacy v2)

**Related pillars:** [12 Stepping Stone Traits](pillar-12-stepping-stone-traits.md) (Chain C diplomat traits gate congress events), [11 Cabinet Duties](pillar-11-cabinet-duties.md) (cc_duty_diplomatic_mission boosts intl synergy)

---

## Theme

v0.1 added international synergy events for pairs of countries with complementary cabinets. v2.0 expands this to multi-party diplomatic theater — the proto-congress, the peace conference, the great power consultation.

---

## What It Adds

### A. Congress Events

New `cc_intl_congress` event chain fires when all these conditions are met:
- 3+ great powers are at peace simultaneously
- At least two of them have `master_statesman` or `diplomatic_attache` cabinet members

**"A Proposal for Consultation"** (fires on the initiating country)
One country's cabinet member dispatches a formal proposal. If 3 great powers respond positively (player-driven options), a `cc_congress_active` flag period of 5 years begins.

During the congress, periodic events offer multi-party tradeoffs:
- Territorial exchange proposals
- Joint guarantee of a third party
- Religious settlement or toleration agreement

**"A Concert of Powers"** (fires at congress end if `peacemaker_counselor` present)
The peacemaker minister pushes for a formal Concert agreement: +opinion among all congress members for 25 years.

### B. The Dynastic Pact

Expanded intl synergy: if two countries have cabinet members of the same dynasty (or closely related culture group), a `dynastic_pact` event fires. This can:
- Establish a soft alliance through the cabinet connection
- Enable an arranged marriage proposed by the ministers themselves
- Create friction if the dynastically-connected minister has divided loyalties

### C. The Trade Court

If two countries both have `merchant_of_the_crown` or `trade_consortium_minister` cabinet members and share a trade node, `cc_intl_trade_court` events fire:

- Negotiate mutual trade power bonuses (timed opinion modifier)
- Establish a joint chartered company (new subject type: `joint_charter` — requires [Pillar 07](pillar-07-colonial-cabinet.md))
- Create friction if one country's merchant minister is outcompeting the other

---

## Historical Echoes

- The Congress of Westphalia (1648) — the first modern congress; diplomats defined European order
- The Congress of Utrecht (1713) — ended the War of Spanish Succession through multi-power negotiation
- The Congress of Vienna (1815) — Metternich's system; cabinets literally ran the congress
- The Hanseatic League merchant councils — trade courts enforcing commercial agreements between member cities

---

## New Files Needed

| File | Purpose |
|------|---------|
| `events/cc_congress_events.txt` | Congress proposal, multi-party events, Concert of Powers |
| `events/cc_dynastic_pact_events.txt` | Dynastic pact + trade court events |
| `common/biases/cc_congress_biases.txt` | Concert of Powers opinion modifier + trade court modifiers |
| Localization `.yml` | Event text, modifier names |

---

## Implementation Notes

- `cc_congress_active` is a flag set on the initiating country; participating countries get a mirrored flag via `every_country` effect.
- Multi-party events: fire on the initiating country, then use `every_country = { limit = { has_country_flag = cc_congress_participant } }` for effects.
- "Great power" check: verify the exact trigger — likely `is_great_power = yes` or similar.
- The `joint_charter` subject type (if built) would live in `cc_subject_types.txt` and need an advance unlock.
- `cc_duty_diplomatic_mission` ([Pillar 11](pillar-11-cabinet-duties.md)) targeting a congress participant country doubles the chance of congress-related synergy events firing.
