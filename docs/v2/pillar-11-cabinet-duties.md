# Pillar 11 — The Cabinet Duties Action System

**Related pillars:** All pillars — duties boost event rates for every domain system
**Priority:** Tier 1 (implement first — enables all other pillars)

---

## Theme

Currently cabinet members are "on" or "off" — they're in the cabinet and events fire around them. This pillar gives players an explicit assignment choice: *what is this minister doing?* It's a meta-system that gates and boosts other Pillar content, and makes the decision to specialize a minister feel meaningful.

---

## Technical Foundation

Cabinet actions have **no native sub-option support**. `cabinet_duties` must be implemented as **separate cabinet action entries** — one action per duty type. The player assigns the minister to whichever duty fits their needs. Each duty action is `allow`-gated by its relevant condition.

Existing cabinet actions (develop_province, integrate_area, etc.) remain unchanged. Duty actions are an additional *optional* assignment category.

---

## Duty Actions

### `cc_duty_free_hands` — Free Hands (Default)

The catch-all assignment. All event systems fire at their *baseline* rates. A tiny country modifier represents the well-rounded generalist doing whatever is needed.

| Property | Value |
|----------|-------|
| `allow` | None (always available) |
| `select_trigger` | None — applies to the minister's country |
| `country_modifier` | Tiny ADM + DIP + MIL efficiency (+0.02 each) |
| Purpose | The current implicit state made explicit and rewarded |

### `cc_duty_war_council` — War Council

Minister is formally tasked with prosecuting a war.

| Property | Value |
|----------|-------|
| `allow` | `at_war = yes` |
| `select_trigger` | None |
| `country_modifier` | Minor discipline or army morale recovery |
| Pillar boost | [Pillar 04](pillar-04-war-council.md) events fire at 2× rate for this minister |

### `cc_duty_diplomatic_mission` — Diplomatic Mission

Minister is on a foreign assignment, building relationships with a specific court.

| Property | Value |
|----------|-------|
| `allow` | At peace (not at war with target) |
| `select_trigger` | `looking_for_a = country` (foreign countries only) |
| `country_modifier` | Minor diplomatic reputation vs. target |
| Pillar boost | International synergy events with target country at 2× rate; enables colonial posting ([Pillar 07](pillar-07-colonial-cabinet.md)) |

### `cc_duty_domestic_reform` — Domestic Reform

Minister is focused on internal governance — reform proposals, law drafting, bureaucratic restructuring. Distinct from vanilla `appease_estate` (which targets a distressed estate's satisfaction recovery and fires only when satisfaction < 50%).

| Property | Value |
|----------|-------|
| `allow` | None (always available) |
| `select_trigger` | None |
| `country_modifier` | Minor reform progress speed |
| Pillar boost | [Pillar 12](pillar-12-stepping-stone-traits.md) progression events fire at 2× rate; [Pillar 02](pillar-02-estate-factions.md) faction events boosted |

### `cc_duty_scholarly_inquiry` — Scholarly Inquiry

Minister is engaged in intellectual work — correspondence with scholars, patronage of learning.

| Property | Value |
|----------|-------|
| `allow` | Age 4+ (Renaissance and beyond) |
| `select_trigger` | None |
| `country_modifier` | Minor development growth in capital |
| Pillar boost | [Pillar 03](pillar-03-scholars-court.md) rationalist chain events at 2× rate |

### `cc_duty_colonial_posting` — Colonial Posting

Minister is posted overseas to a colonial subject. Replaces the standalone `cc_post_minister_overseas` interaction from [Pillar 07](pillar-07-colonial-cabinet.md).

| Property | Value |
|----------|-------|
| `allow` | Has at least one colonial subject (colonial_nation, chartered_company, or provincial_governorate) |
| `select_trigger` | `looking_for_a = country` filtered to colonial subjects |
| `country_modifier` | Applied to subject, not overlord — minor loyalty bonus |
| Pillar boost | [Pillar 07](pillar-07-colonial-cabinet.md) colonial events at 2× rate for this minister |

### `cc_duty_religious_oversight` — Religious Oversight

Minister is focused on confessional affairs — managing religious conformity or inter-faith relations.

| Property | Value |
|----------|-------|
| `allow` | None (but event content gated by confessional traits) |
| `select_trigger` | None |
| `country_modifier` | Minor religious unity recovery |
| Pillar boost | [Pillar 06](pillar-06-religious-tensions.md) confession clash events at 2× rate |

---

## Historical Echoes

- The Ottoman Divan — each vizier had a formal portfolio (finance, military, justice, foreign affairs)
- Colbert's multi-portfolio ministry in France — one minister, multiple formal responsibilities
- The Habsburg court's "referate" system — councillors formally assigned to specific policy areas
- The English Privy Council's committee system — standing committees for specific domains

---

## New Files Needed

| File | Purpose |
|------|---------|
| `common/cabinet_actions/cc_duty_free_hands.txt` | Default assignment |
| `common/cabinet_actions/cc_duty_war_council.txt` | War domain |
| `common/cabinet_actions/cc_duty_diplomatic_mission.txt` | Diplomatic domain |
| `common/cabinet_actions/cc_duty_domestic_reform.txt` | Reform domain |
| `common/cabinet_actions/cc_duty_scholarly_inquiry.txt` | Intellectual domain |
| `common/cabinet_actions/cc_duty_colonial_posting.txt` | Colonial domain |
| `common/cabinet_actions/cc_duty_religious_oversight.txt` | Religious domain |
| Localization `.yml` | Action names, descriptions |

---

## Implementation Notes

- All duty actions should be mutually exclusive: a minister assigned to one duty should not be able to take another simultaneously. Use `is_doing_cabinet_action = cc_duty_*` in `allow` blocks.
- Boost mechanism: duty events use a country flag `cc_minister_X_on_duty_Y` (set by the action's start effect, cleared on finish/dismiss) in their trigger conditions.
- The boost rate (2×) is implemented by adding a second parallel trigger block in each pillar's event MTTH, checking for the duty flag.
- `allow_multiple = no` on all duty actions — only one minister should be able to hold each duty type at a time (except `cc_duty_free_hands`).
