# Plan: Household Offices, then the pre-XP Event Migration

Two workstreams, decided together in one session. Offices ship first; the event migration
follows. `cc_feudal.1` is touched by both, which is why the order matters: offices delete the
six traits that event grants, so the migration inherits an already-simplified file.

## Why this exists

The cabinet experience rework (phases 1-7) moved trait progression onto XP ladders, but the
older systems it was meant to replace are still live. Measured across the mod:

- 63 ladder traits exist. **47 of them can still be granted directly by a random event**,
  bypassing XP entirely. 36 of those are higher rungs, including four tier-3 capstones.
- 164 trait-granting event options exist across the 180 pre-XP events. **156 carry no
  experience gate.**
- 77 events read a minister's traits and pay out without ever checking whether that minister
  earned the trait or was handed it by a monthly roll.

Separately, the six household office traits (`seneschal`, `marshal_of_the_court`,
`master_of_coin`, `herald_of_arms`, `court_chaplain`, `court_astrologer`) are unreachable
after roughly 1500, because all six carry `allow = { current_age = age_1_traditions }`, and
four of them collide with a minister's career trait through
`allow = { NOT = { has_trait_category = cabinet } }`.

---

# WORKSTREAM 1: HOUSEHOLD OFFICES

## The model

An office is not a trait. It is four things:

1. **A country variable** naming the holder (`cc_office_<key>`), plus a flag on the holder so
   the panel can print a name and the pulse can find them.
2. **An `auto_modifier`** whose `potential_trigger` requires the unlock advance, a living
   seated holder, and no obsoleting advance.
3. **An unlock advance**, and usually **an obsoleting advance**.
4. **An appointment path**: one character interaction targeting the minister, which fires one
   event listing the offices that minister currently qualifies for.

### Why auto_modifiers rather than traits

**Non-stacking is structural.** An `auto_modifier` is a single named country entry that is
either applied or not. It cannot stack with itself. Nothing has to enforce this.

`in_game/common/auto_modifiers/cc_cabinet_composition.txt` already uses this shape
(`requires_real = yes` plus `potential_trigger`), so it is an established pattern in the mod
rather than a new one.

Vanilla's `auto_modifiers/readme.txt` confirms the available fields: `category`, `type`,
`icon`, `requires_real`, `potential_trigger`, `scales_with`, `limit`, `hide_effects`, `alert`.
`potential_trigger` takes arbitrary country triggers: vanilla uses `has_variable`,
`has_societal_value`, `any_subject`, `any_known_country`, `culture`, `religion`,
`has_culture_group`, `at_war`, `has_regent` and more. `has_advance` is a standard country
trigger and will work, though no vanilla auto_modifier happens to use it.

### The potential_trigger reads country variables, not characters

The obvious trigger is `any_character = { has_variable = cc_office_seneschal  is_alive = yes }`,
which would make death cleanup free as well. **Do not do this.** `potential_trigger` is
evaluated continuously for every real country, and the mod's existing nine composition entries
already perform 37 `any_cabinet_character` iterations. Adding forty more per-character
iterations multiplies that cost by roughly five.

Instead each office's trigger reads country variables only:

```
potential_trigger = {
    has_variable = cc_office_seneschal_filled
    has_advance = state_administration_advance
    NOT = { has_advance = chancery_records }
}
```

That is cheap, and it matches the constraint the whole system is built around: store a flag or
a number on the side the pulse iterates, never a character reference script has to dereference.

**The cost is that death cleanup is no longer free.** It becomes an explicit vacate, hooked
where the mod already listens:

- `on_cabinet_death` (already hooked in `cc_legacy_pulse.txt` for `cc_xp_on_death`)
- `on_cabinet_removed` (already hooked as `cc_xp_on_removed`)
- plus a monthly backstop sweep for human courts

Because offices require a seated minister, both hooks fire for every way a holder can leave.

### Scaling by holder level

The chosen behaviour is a capped multiplier keyed to the holder's level (1-10), clamped to
roughly 1.0x-2.5x. `scales_with` takes a country-scope script value, and **script cannot
dereference a character held in a variable**. So the monthly pulse must publish each holder's
level to a country variable first, the same way `cc_xp_publish_school_capacity` already does.

```
cc_xp_publish_office_levels = yes    # in cc_xp_monthly_service, human courts only
```

## Roster: ~40 offices

Full breadth: core, government form, religion, culture group, region.

### Core, universal, age-driven

| Office | Appears with | Retired by |
|---|---|---|
| Seneschal | game start | `chancery_records` |
| Master of Coin | game start | `standardized_coins` |
| Herald of Arms | game start | `diplomatic_training` |
| Marshal of the Court | game start | `absolutist_court` |
| Chancellor of the Rolls | `chancery_records` | `modern_bureaucracy` |
| Master of the Mint | `standardized_coins` | none |
| Court Chamberlain | `regulate_court_procedures` | none |
| Master of Protocol | `diplomatic_training` | none |
| Intendant | `absolutist_court` | none |
| Permanent Secretary | `modern_bureaucracy` | none |
| Director of Public Instruction | `enlightened_court` | none |

### Government form

Constable (`noble_officers`, monarchy), Consul of Merchants (`free_merchants`, republic),
Chancellor of the See (`state_of_clerics`, theocracy), Keeper of the Kurultai
(`kurultai_advance`, horde).

### Religious

Court Chaplain and Court Astrologer (existing, converted), Grand Inquisitor
(`inquisition_advance`), Patriarchal Legate (`structured_patriarchates`), Qadi of the Court
(`islamic_courts`), Court Purohita (`varna_system`), Sangha Preceptor
(`monastic_communities`), Consistory Superintendent (`protestant_administration_tax`).

### Culture group and region

Drawn from the larger culture and region advance files: `culture_group_greek` (35 advances),
`culture_group_german` (30), `culture_group_romanian` (29), `culture_tuscan` (29),
`culture_venetian` (23), `culture_median` (23), `region_north_america` (43), `region_asia`
(19), `region_africa` (15), `region_iberia` (12). Exact office list to be drafted against
these files during implementation.

## The slot cap

Any number of offices may be unlocked. A court may fill at most **6**. The cap is a script
value counting filled offices, checked in the appointment event's option triggers, so an
over-capacity court sees the offices listed but cannot appoint until it vacates one.

This is what keeps the roster honest: a Catholic monarchy in age 3 has seven offices available
(Chancellor of the Rolls, Master of the Mint, Court Chamberlain, Master of Protocol, Court
Chaplain, Grand Inquisitor, Constable) and must choose six.

## Obsolescence

When an advance retires an office, the office vacates and the holder is freed. The modifier
ends, the variable clears, the minister goes back to being an ordinary cabinet member, and the
successor office needs a fresh paid appointment. One code path, no successor-inheritance
special cases, and each age transition becomes a moment where the player re-staffs.

## Appointment

A character interaction targeting a seated minister, which fires an event listing the offices
that minister qualifies for as options.

**Why not one interaction per office.** A `character_interaction` has one target. Appointing
minister X to office Y needs two values. The documented mod constraint is that a GUI button
cannot open an interaction's `select_trigger` picker, but here the minister *is* on a row in
the character interaction menu, so `select_trigger` picks the minister and event options pick
the office. That is one interaction and one event instead of forty interactions.

Cost is charged through `in_game/common/prices/cc_xp_prices.txt` like every other court
action, and each office requires **tier 1** in its track from the appointee.

## Panel

A Household tab on `cc_cabinet_court.gui`, alongside Patronage and Schools, with six slots.
Uses the existing slot-sync variable pattern, since there is no datamodel for this and GUI is
the only place that can dereference a stored character (`GetVariable(...).GetCharacter`).

## Tooltips

Each office needs three loc keys, matching what `warlord_court` already does:

- `<key>` the office name
- `<key>_desc` what it does and why it is available now
- `AUTO_MODIFIER_NAME_<key>` the condition line

Plus `custom_tooltip` blocks on the appointment interaction explaining the unlock advance and
the obsoleting advance. Eight existing court interactions already use `custom_tooltip`.

## Migration of the six existing traits

A one-time migration converts a held trait into the office variable and removes the trait.

**The traits could not simply be deleted.** `cc_office_backfill` has to read `has_trait` and
call `remove_trait` on a minister in an existing save, and neither works against a trait the
mod no longer defines. Deleting the entries outright would make the migration impossible
rather than unnecessary. They are therefore kept as shells with no modifier and
`allow = { always = no }`, which is vanilla's own way of retiring a trait
(`00_ruler.txt:895`). Nothing can grant them, because `cc_feudal.1`, the only thing that ever
did, was removed in the same change. **Delete the shells once a release has shipped with the
backfill in it.**

The backfill runs from `cc_office_monthly` behind a `cc_office_migrated` flag, not from
`cc_xp_init`: it is country scope and `cc_xp_init` is character scope. `on_game_start` would
be wrong for the same reason it was wrong for `cc_xp_ladder_backfill`, namely that it does not
run when an existing save is loaded.

Note `court_chaplain` and `court_astrologer` are `category = religious_figure`, not `cabinet`,
so they never collided with a career trait. They are converted for consistency, not because
they were broken.

## Build order and status

1. **Done.** `tools/generate_offices.py`, 43 offices (13 core, 10 religion, 9 culture,
   6 government, 5 region). Validation aborts without writing if any named advance is absent
   from the vanilla files, any modifier name is absent from `modifier_type_definitions`, an
   office is unlocked and obsoleted by the same advance, an obsoleting advance precedes its
   unlock, or a key or name repeats. It also reports offices available per age for eight
   archetype courts, which is the check behind the 3-6 target. Emits the auto_modifiers,
   triggers, script values, effects, picker event and English loc.
2. **Done.** `cc_office_pulse.txt`: monthly retire plus level publish, and
   `cc_office_on_departure` chained into both `on_cabinet_death` (via `cc_legacy_pulse.txt`)
   and `on_cabinet_removed` (via `cc_xp_pulse.txt`). No periodic orphan sweep: the two
   lifecycle hooks cover every way a holder can leave, and a sweep would mean iterating the
   cabinet once per office.
3. **Done.** `cc_office_appoint_to_household` interaction plus `price:cc_office_appointment`.
4. **Done.** Household tab on the Court Ledger, generated into `cc_office_household.gui`.
   One block per office rather than six generic slots: which posts exist is per-country, so a
   generic slot would still need a number-to-name mapping in GUI, which is the same 43
   visibility checks with an extra indirection. Needs `cc_office_publish_roster`, because GUI
   has no by-key `has_advance` lookup (`IsResearched` exists only on an `AdvanceItem` from the
   advances screen's own datamodel). No appoint button on the panel: a button supplies no
   target, so it could not open the interaction's character picker.
5. **Done.** `cc_feudal.1` and `cc_feudal.10` deleted, their pulse entries removed, 60
   `has_trait` reads across four event files rewritten to `has_variable = cc_office_held_*`,
   `cc_legacy.1`'s office inheritance removed, trait shells left for the backfill, stale loc
   pruned in all four languages.
6. **Done.** `translate.py -m -l french,german,spanish`. 238 keys in each of the four
   languages, markup tokens verified at parity. `CC_OFFICE_TAB_NOTE` was reworded at the
   English source first: "Advances open posts" reads as an imperative once translated, and the
   German came back as "Besetzt offene Aemter". Naming research as the subject fixed it in all
   three.
7. **Done.** `EVENT_INFO` gained a `cc_office` row and a new `household-offices` GEN section
   was added, with markers in `WORKSHOP_DESCRIPTION.bbcode` placed against the existing quote
   about the one-cabinet-trait limit, since offices are the answer to it. The section imports
   the roster from `generate_offices.py` rather than re-parsing the generated output, so the
   counts cannot drift. `gen_trait_summary` now counts through `count_live_traits`, which
   skips `allow = { always = no }` entries: without it the description advertised 37 age
   traits when six were retired shells. All outputs regenerated, zero em-dashes.

`docs/tmp/selfcheck.py` covers brace balance, unresolved `cc_office_*` symbols, missing loc
keys, the `@trigger_no!` prefix requirement, em-dashes in generated player-facing loc, and
dangling references to the deleted events. All pass. None of it has been run in game.

Unrelated pre-existing condition found along the way: `tools/generate_duty_tracks.py --check`
reports `cc_xp_duty_tracks.txt` stale. It predates this work and was left alone.

---

# WORKSTREAM 2: THE PRE-XP EVENT MIGRATION

180 events. They are not one kind of thing, and each bucket gets different treatment.

| Bucket | Events | Treatment |
|---|---|---|
| All grants are age-file traits | 23 | Leave. Carve-out. |
| Grants ladder rungs only | 16 | Convert grant to XP award for humans |
| Mixed: ladder rungs plus off-ladder | 9 | Per-option: rungs to XP, off-ladder gated |
| Off-ladder only | 2 | Gate on tier and track |
| Legend quest | 4 | Leave. Carve-out. |
| Affliction grant / rehabilitation | 10 / 9 | Leave. Carve-out. |
| Grants nothing, reads cabinet traits | 77 | Tier-gate and scale reward |
| Grants nothing, reads no cabinet trait | 39 | Out of scope. Not cabinet content. |

## 1. Close the ladder bypass (56 options across 24 events)

A ladder-rung option keeps its text and its place, but for a human court the `add_trait` is
replaced with an XP award in that rung's track, sized so a rung-2 option is worth roughly a
tier. AI courts keep the trait grant, because nothing offers an AI a choice and the random
path is the only path it has.

```
option = {
    name = cc_cond.6.a
    trigger = { scope:minister = { <ai court> } }
    scope:minister = { add_trait = trait:supreme_commander }
}
option = {
    name = cc_cond.6.a_xp
    trigger = { scope:minister = { NOT = { <ai court> } } }
    scope:minister = { cc_xp_gain_mil = { AMOUNT = cc_xp_field_award_high } }
}
```

The rung itself becomes unreachable for a player except through the ladder. AI still advances,
because it earns XP and then climbs via `cc_xp_ladder_advance`.

Eight of these options already carry `cc_xp_dispatch_ready` and need no change.

**Why not simply zero the dispatcher branch.** Only 18 of the 24 events are dispatcher-fired.
The other 8 fire from other pulses (`cc_synergy.1/.6/.24`, `cc_legacy.1`, `cc_cabinet.1`,
`cc_feudal.6/.10`, `cc_neg.19`). And 7 of the 18 (`cc_cond.1/.4/.5/.20/.21/.22/.23`) mix
ladder-rung options with off-ladder options that must keep firing, so zeroing the branch would
kill the off-ladder path too.

## 2. Gate the 38 off-ladder options

These stay random. Each gets a tier gate **graded by track relevance**: each trait is assigned
a specific track (religious and cultural ones to adm or dip by `custom_tags`, military ones to
mil) and a tier (1-3) graded by modifier strength, so the gate reads the matching track rather
than any track.

The grading will be generated from the trait definitions and **listed for review before it is
applied**. It is 38 balance judgements and should not be made silently.

## 3. Tier-gate and scale the 77 payoff events

Each gets a `cc_xp_tier_at_least` requirement matching the trait it reads, and its payout
scaled by the holder's level through a single shared script value clamped to roughly
1.0x-2.5x. One shared value, called from all 77, so the curve is tunable in one place.

## 4. Dispatcher

Migrated branches get `factor = 0` for `is_ai = no`, extending the pattern five branches
already use at `factor = 0.3`. No event deletions, no save-migration risk.

## Commit split and status

All four landed on master, each with its own tool that can be re-run and re-verified.

1. `d21d97f` **Household offices.** `tools/generate_offices.py`.
2. `17e1617` **Bypass closure.** `tools/migrate_bypass.py`. 50 options split AI/human across
   6 files, 38 generated loc keys, translated.
3. `789307c` **Off-ladder gating.** `tools/migrate_offladder_gates.py`. 34 options gated,
   16 at tier 1 and 18 at tier 2, across adm 24 / dip 6 / mil 4.
4. `351e647` **Payoff scaling.** `tools/migrate_payoff_scaling.py`. 78 events, 214 payouts.

Each tool is idempotent and carries `--verify` or an equivalent dry run. None of it has
been run in game.

### What each tool deliberately does not touch

Recorded here because these are the judgement calls, and a later contributor re-running a
tool will otherwise assume the gaps are bugs.

- **`create_character` blocks.** A newly built NPC arriving with a starting trait is not a
  bypass; nothing is being handed to a minister the player developed.
- **`cc_legacy.1`'s inheritance chain.** Its `if/else_if` passes on whichever trait a dying
  elder held. That is a transfer inside the court, paid for with the elder. Both the bypass
  tool and the gating tool exempt it, and both report rather than hide it. Collapsing the
  chain into one award would also have destroyed it.
- **Already-gated options.** Eight ladder-rung options carried a tier gate before any of
  this. They are a shortcut past the one-year advance wait, not a way around the tier.
- **`add_opinion` and `change_variable`.** The first carries its magnitude in the bias
  definition; the second drives cooldowns and counters that would corrupt if multiplied.
- **Block-form `add_gold`.** Already carries its own `multiply` with `min`/`max` clamps
  calibrated against it, and is nearly always negative. Scaling would make a good court pay
  more for the same thing.
- **Hybrid grant-and-payout events** (`cc_synergy.1/.6/.24`). Handled by the bypass tool;
  their decline options go unscaled.

### Known consequence: careers are now bought

Rung-0 grants were converted along with the rest, and `cc_xp.90/.91/.92` are reached only
from the training return events. A court that never pays for training therefore gets no
careers at all. Experience still accrues and banks, so a minister trained late climbs fast.
If that reads badly in game, the one-line fix is to offer a career when an unladdered
minister crosses tier 1 on the yearly pulse.

---

## Open items to confirm during implementation

- Does `has_advance` work inside an auto_modifier `potential_trigger`? Test before scaling.
- The 38 off-ladder track/tier gradings need review before they are applied.
- Culture-group and region office list is not yet drafted.
