# Adversarial Code Review, August 2026

Scope: whole mod at even depth (in_game, main_menu, submods), with extra attention to
situations and late-game subject types. Findings are ranked correctness first, then
design completeness. Every claim below was checked against the live vanilla files at
`F:\SteamLibrary\steamapps\common\Europa Universalis V\game`.

Method: cross-reference sweeps (localisation keys, event IDs, `type:value` references,
modifier names, variable reads vs writes, duplicate keys in a block) plus a manual read
of `cc_subject_types.txt`, `cc_balance_of_power.txt`, `cc_invasion_mexico.txt`,
`cc_subject_bonds.txt`, `cc_subject_advances.txt`, `cc_bop_effects.txt`,
`cc_parliament_issues.txt` and the bond effect/monitor layer.

**What came back clean.** 510 events, no duplicate IDs, no dangling `trigger_event` targets,
no unreachable events, no missing localisation keys against 4,720 mod keys, no invalid
modifier names, no invalid trait/advance/privilege/bias/game-rule references, UTF-8 BOM
present everywhere, no inverted clamps. The existing tooling and discipline are working.

Two fixes were applied while writing this (see [Fixes applied](#fixes-applied)).

---

## Severity 1: broken or self-cancelling

### 1.1 The vanilla `policy_vote` override had drifted out of sync

**Status: fixed by deleting the override. The mod no longer shadows any vanilla file.**

`in_game/common/resolutions/policy_vote.txt` (removed)

`CLAUDE.md` flagged this file as the mod's one intentional vanilla override and warned that a
Paradox patch would be silently masked. That had already happened. Diffing the mod's copy
against the current vanilla file showed three vanilla blocks the copy was missing:

| Vanilla lines | What the mod's copy dropped |
|---|---|
| 655-667 | The whole `trigger_else_if` that denies Italian League Sponsors a vote on IO laws |
| 316-323 | The `AND` wrapper around `resolution_is_active` that adds the `previewed_vote` checks |
| 862-885 | The `previewed_vote` / `forbid_multiple_policies_vote` AI voting bias chunk |

Effect with the mod enabled: Italian League Sponsors regained a vote Paradox had removed, and
the AI's law-preview voting logic reverted to an older version.

**There is a per-IO hook for vote weight after all**, and the mod was already using it
elsewhere. Vanilla `policy_vote`'s `votes` block has an `else_if` for
`uses_parliament_for_law_votes_trigger = yes`
(`has_parliament = yes` plus `modifier:uses_parliament_for_law_votes = yes`, set by the
parliament type) that reads `country_combined_special_status_power(scope:recipient)`.
`special_status_power` accepts a full script value in country scope; vanilla
`union.txt:106` uses `value = country_economical_base`, and the mod's own
`cc_concert_assembly` parliament type already routes Concert votes this way.

Rewired the coalition to the same mechanism and deleted the copy:

| File | Change |
|---|---|
| `script_values/cc_bop_values.txt` | New. `cc_bop_congress_weight = country_tax_base + 0.5 × great_power_score`, `min = 1` |
| `international_organization_special_statuses/cc_bop_coalition.txt` | `cc_bop_chief_balancer` power now uses that value; added `cc_bop_coalition_seat` for non-leader members |
| `parliament_types/cc_bop_parliament.txt` | `cc_bop_coalition_assembly` gains `uses_parliament_for_law_votes = yes` and both `*_can_participate_in_parliament` flags |
| `modifier_type_definitions/cc_coalition_parliament.txt` | Registered `cc_bop_coalition_seat_can_participate_in_parliament` and `_agenda_impact` |
| `international_organizations/cc_bop_coalition.txt` | `special_statuses_implemented` now lists both statuses |
| `resolutions/policy_vote.txt` | Deleted |

The weighting formula is unchanged. The `min = 1` floor is new and load-bearing: vanilla's
`can_vote` block on this branch requires
`country_combined_special_status_power(scope:recipient) > 0`, so without it a member whose tax
base and great-power score both round to zero would be silently disenfranchised. The old
override's branch had no such guard because the old code path never checked.

Two deliberate behaviour changes come with the flag, both of which the Concert has always run
under:

- Vanilla will not start a coalition law debate while a coalition parliament issue is ongoing
  (`policy_vote.txt:92`).
- Resolving a law vote now ends or recalculates the parliament (`policy_vote.txt:470, 520, 563,
  602`).

The dormant parliament type deliberately does **not** set the flag, so nothing changes before
the chief balancer convenes the congress.

### 1.2 The naval administration parliament issue could pass and do nothing

**Status: confirmed as a defect and fixed, residual mismatch included.**

`in_game/common/parliament_issues/cc_parliament_issues.txt:70`

`allow` and `on_debate_passed` disagreed on the location they were looking for:

```
allow (line 89):
    NOT = { OR = { location_rank = location_rank:rural_settlement  is_capital = no } }
    -> not rural AND IS the capital

on_debate_passed (line 132):
    NOT = { OR = { location_rank = location_rank:rural_settlement  is_capital = yes } }
    -> not rural AND is NOT the capital
```

The `is_capital` polarity was inverted between the two. `allow` also omitted `is_port = yes`
(commented out at line 88). So the issue only became proposable when the qualifying location
was the capital, while the effect only fired when a qualifying location was *not* the capital.
Both could hold only for a country with two distinct qualifying locations, and even then the
`is_port` mismatch could strand it. The common outcome was a debate that passed and produced
no subject.

`allow` now mirrors `on_debate_passed`: `is_port = yes` and
`NOT = { OR = { location_rank = location_rank:rural_settlement  is_capital = yes } }`.

A residual mismatch was then closed as well: `allow` carried
`dominant_culture = { is_primary_or_accepted_in = ROOT }` that neither `on_debate_passed`'s
`if` limit nor its `random_owned_location` limit checked, so the issue was gated on holding a
culturally accepted port while the effect could seat the administration on any qualifying port.
The check is now mirrored into both limits.

All three location predicates (the `allow` gate, the `if` guard, and the selection weight's
limit) now test the same five conditions:

```
continent = ROOT.capital.continent
is_port = yes
NOT = { OR = { location_rank = location_rank:rural_settlement  is_capital = yes } }
dominant_culture = { is_primary_or_accepted_in = ROOT }
```

Keep them in lockstep. The failure mode here was never a script error, only a debate that
passed and did nothing, which is invisible in the logs.

### 1.3 Debug-scale parliament bias

**Status: fixed. `add = 1000`, matching vanilla's hard-force magnitude.**

`in_game/common/parliament_issues/cc_parliament_issues.txt:101`

```
wants_this_parliament_issue_bias = { add = 100000000 }
```

Vanilla uses `±1000` as its hard-veto/hard-force magnitude (see
`02_crown_estate_parliament_issues.txt:566`). 100,000,000 was five orders of magnitude past
that, so whenever `allow` passed this issue monopolised the crown estate's agenda and crowded
out every vanilla crown issue. Combined with 1.2, the player saw the same dead issue proposed
over and over.

### 1.4 `cc_promote_integration` duplicates a vanilla issue at 10x strength

**Status: reviewed and confirmed intentional. No action.**

`in_game/common/parliament_issues/cc_parliament_issues.txt:1`

The block is a near-verbatim copy of vanilla `promote_integration`
(`03_nobles_estate_parliament_issues.txt:561`) under a new key, with two numbers changed:

| | vanilla | mod |
|---|---|---|
| `global_integration_speed_modifier` | 0.2 | 2 |
| `change_integration_progress` | 20 | 33 |

Because the key differs this does not override vanilla; both issues load side by side with the
same estate, `allow` and `chance`, giving the nobles two near-identical agenda entries. That is
the intended design, and the `2` is a deliberate value rather than a decimal slip.

Recorded here only so a future reviewer does not re-open it.

### 1.5 Chartered company compared a sub-continent to a continent

**Status: fixed.**

`in_game/common/subject_types/cc_subject_types.txt:960-974`

```
subject_creation_enabled = {
    NOT = { scope:target_province = { sub_continent = root.capital.continent } }
}
```

The comment above it reads "Subject must be on a different sub-continent than overlord
capital". `sub_continent` was being compared against a `continent` value, which never matches,
so the `NOT` was always true and the geographic restriction never applied. Chartered companies
could be chartered on the overlord's own doorstep.

Changed to `sub_continent = root.capital.sub_continent` in both `subject_creation_enabled` and
`release_country_enabled`. That is the vanilla idiom, used 11 times across
`game/in_game/`.

### 1.6 The Concert of Europe ending did not create the Concert

**Status: fixed. The equilibrium ending now founds a Concert seating both blocs.**

`in_game/common/scripted_effects/cc_bop_effects.txt`

`cc_bop_form_concert` was called from exactly one place: the **coalition victory** branch of
`cc_bop_apply_ending`, and only when the bloc voted `policy:cc_bop_enact_concert`.

The ending actually *named* Concert of Europe is the `cc_bop_flag_concert` branch, set by the
situation's `on_monthly` (age 6, 40+ years, share between 40 and 60). That branch stamped the
restart year, fired event `.76` at the balancer, and handed out `cc_bop_concert_of_europe`
country modifiers. It never touched `cc_bop_form_concert`, so the whole Concert institution
(`cc_bop_concert.txt`, its four policies, parliament type, issues, special statuses, election
resolution and readmission pulse) was unreachable from the ending named for it. Event `.74`'s
own text promises otherwise: "matured into a lasting concert".

**The two endings differ in whether anyone lost,** which is why this is not a one-line call.
After a coalition victory there is a beaten aspirant to exclude and readmit; after forty years
of held equilibrium both poles are intact and nobody was defeated. `cc_bop_form_concert` is now
parameterised on `$MODE$` and the shared work (president, five seats ordered by
`great_power_score`, dissolving the poles) stays in one place:

| | `victory` | `equilibrium` |
|---|---|---|
| Pool | Coalition members | Coalition **and** preponderance members |
| Excluded | Former hegemon | Nobody |
| Readmission | Stamped 50-75 years out | None; `cc_concert_readmit_year` stays unset, so `cc_concert_readmission_pulse` never fires |

Two supporting changes were needed:

- The concert branch is now `else_if` on `has_variable = cc_bop_flag_concert` rather than a
  catch-all `else`. It founds a real institution, so a catch-all would found one for any future
  end that reached it without a flag. `can_end` already requires one of the six flags.
- `on_start`'s "balance re-forming from a lapsed concert" branch now actually dissolves the
  standing `cc_bop_concert` IO and clears the pending readmission stamps. The equilibrium
  ending sets only the 25-year cooldown and **not** `cc_bop_concluded`, so a second balance may
  form later; without this the old Concert would still be sitting while its own members
  re-divided into the two new poles. The victory ending sets `cc_bop_concluded` and so never
  reaches this path.

Ordering is load-bearing in both branches: `cc_bop_form_concert` destroys both poles, so it
must run after any `every_country` loop that reads bloc membership. Both call sites are last in
their branch and commented as such.

### 1.7 The balance of power could start and conclude in the same month

**Status: fixed. Five-year floor on the revolution ending, and the three non-war breaks are now
mutually exclusive.**

`in_game/common/situations/cc_balance_of_power.txt`

```
if = {
    limit = { is_situation_active = situation:the_revolution }
    situation:cc_balance_of_power = { set_variable = cc_bop_flag_revolution }
}
```

Every other ending is guarded. Deluge and concert both require
`years_since_situation_start > 5` (or 40) and `NOT = { has_variable = cc_bop_*_primed }`.
The revolution branch has no duration floor, no primed check, and no other-flag check.
`can_start` (line 15) also does not exclude `the_revolution` being active, and
`cc_bop_doctrine_or_era` auto-satisfies once age 6 opens.

Failure case: a game reaches the Age of Revolutions with `the_revolution` already active and
the balance of power not yet started. The situation spawns, fires its grand announcement
(`.1`) plus both role intros and every alignment prompt, and on its first `on_monthly` sets
`cc_bop_flag_revolution`, satisfying `can_end`. The player gets the whole opening ceremony and
the "Revolutionary collapse" close (`.73`) back to back.

This also broke the invariant stated in the file's own comment ("no break flag may be set while
another flag is set or a counter is primed"). Deluge, revolution and concert were three
independent `if` blocks that guarded against `*_primed` but not against each other, so a month
satisfying two of them set two flags and `cc_bop_apply_ending` silently resolved whichever
branch it tested first.

**Fix applied.** The revolution branch gained `years_since_situation_start > 5`, matching
deluge. The three branches were then folded into one `if / else_if / else_if` chain wrapped in
a guard that no flag is set yet, which also covers `cc_bop_flag_stagnation` set earlier in the
same tick by the priming block. Precedence follows the original source order (deluge,
revolution, concert), so behaviour is unchanged in every case that was already unambiguous.

`can_start` was deliberately **not** given a `the_revolution` exclusion. `cc_bop_doctrine_or_era`
auto-satisfies once age 6 opens, and revolutions run long, so excluding it would stop the
balance forming at all in many games. The situation may now begin during a revolution; it
simply cannot be ended by one until it has run five years.

The invariant comment at the head of the ticker section now names both chains and says
explicitly that splitting either back into independent `if` blocks reintroduces the bug.

### 1.8 Naval administration is reachable only through parliament

**Status: reviewed and confirmed intentional. Parliament-only is the design.**

`in_game/common/subject_types/cc_subject_types.txt:1302`

```
creation_visible          = { always = no }
visible_through_treaty    = { always = no }
visible_through_diplomacy = { always = no }
```

Every diplomatic, treaty and release path is deliberately shut. The sole route in is the
`cc_create_naval_administration` parliament issue, which is why 1.2 mattered: with that issue
broken the type was unobtainable in practice, not just restricted. With 1.2 and 1.3 fixed the
design works as intended.

The gating is coherent end to end. `naval_charter_advance` (age 3) carries
`unlock_subject_type = naval_administration`, which is what permits the issue's
`make_subject_of` to name the type at all, and the issue's `allow` requires the same advance.
The one-per-realm limit lives in the issue's `allow` rather than in `creation_visible`, which
is the right place given creation cannot happen anywhere else.

**Optional tidy-up:** the one-per-realm, culture and privilege checks commented out inside
`visible` (lines 1310-1314) and `creation_visible` (1318-1319) are now dead weight, and a
future reader will reasonably wonder whether they were meant to be restored. Deleting them and
leaving a one-line comment saying the type is parliament-only would make the intent obvious.
Also note the culture check among them was never enforced anywhere; if a culture restriction is
wanted, it belongs in the issue's `allow` alongside the existing `dominant_culture` test.

### 1.9 A known-broken line shipped in the enclave signature mechanic

**Status: fixed. The trait is applied to the saved scope after creation.**

`in_game/common/scripted_effects/cc_subject_effects.txt`

```
add_trait = trait:hussar_commander # this doesnt work
```

Inside `create_character` in `cc_spawn_noble_commander`, the elite enclave / palatinate payoff.
The commander spawned with only the random general trait from `trait_category = general`, so
the mechanic half-worked and the intended cavalry flavour never landed.

Correction to an earlier draft of this review, which claimed no vanilla `create_character` uses
`add_trait`. It does: `flavor_plc.txt:719` grants `hussar_commander` inline, alongside
`trait_category = general`, in the same shape. So the inline form is supported in principle and
the original diagnosis was wrong about the cause. Two further facts worth recording, since both
were candidate explanations and neither holds:

- `hussar_commander` is `allow = { always = no }` in vanilla, commented "Can only be given with
  events and mechanics". `allow` gates the ordinary acquisition path, not scripted `add_trait`,
  so this is exactly the intended way to grant it.
- Characters may hold more than one trait of a category. The trigger
  `num_of_traits_of_category` returns a count, and vanilla pairs the explicit grant with
  `trait_category = general` regardless.

Rather than chase the difference against vanilla's block, the grant now runs after creation on
`scope:cc_noble_commander`, which is unambiguous and leaves `trait_category = general` free to
roll its own trait alongside it. If the inline form was in fact working all along, the outcome
is identical.

---

## Severity 2: dead gates and unenforced restrictions

### 2.1 `creation_visible` read a `scope:target` that does not exist there

**Status: fixed. Both lines removed.**

The vanilla readme (`game/in_game/common/subject_types/readme.txt`) is explicit:

```
creation_visible = <trigger> can this subject type be created in general. root = overlord
```

No `target`. Two mod types read one anyway:

- `elite_enclave` line 626: `scope:target ?= { culture = root.culture }`
- `artists_commune` line 1073: `scope:target ?= { culture = root.culture }`

The `?=` keeps it out of the error log, but the culture gate is silently skipped. Both types
also set `only_overlord_or_kindred_culture = yes`, which covers the same ground, so the
practical impact is small; the lines are misleading rather than harmful.

**Fixed.** Both `scope:target` lines were deleted and a comment now states why the check
cannot live there. Culture remains enforced by `only_overlord_or_kindred_culture = yes`, which
the engine applies on every creation path.

Note this is marginally looser than the dead line claimed: kindred cultures are a superset of
`culture = root.culture`. The `visible` blocks still test exact culture, so the diplomacy path
is stricter than release and peace-treaty creation. Both types are one-town flavour subjects,
so this was judged not worth tightening to `only_overlord_culture = yes`; say so if you would
rather they matched exactly.

### 2.2 `release_country_enabled` read `scope:target_province` unguarded

**Status: fixed. Rewritten through the documented `scope:target`.**

Per the readme, `release_country_enabled` gets `root = overlord, target = potential subject`.
Only `subject_creation_enabled` documents `target_province`. Vanilla `colonial_nation.txt:109`
still reads `scope:target_province` there but guards it with `?=`. Four mod types read it
bare:

| Type | Line |
|---|---|
| `chartered_company` | 968 |
| `provincial_governorate` | 1881 |
| `tax_farm` | 2001 |
| `military_march` | 2111 |

**Fixed** by the second vanilla idiom rather than the defensive one. `appanage.txt:114` reads
the same class of geographic rule off `scope:target`'s capital, which actually enforces the
restriction on the release path instead of skipping it when the scope is absent:

```
release_country_enabled = {
    scope:target = {
        capital = { continent = root.capital.continent }
    }
}
```

`subject_creation_enabled` still uses `scope:target_province`, which is its documented scope.
`chartered_company` uses `sub_continent` in both, per 1.5.

### 2.3 Military academy's "one per realm" was not enforced on creation

**Status: fixed.**

`in_game/common/subject_types/cc_subject_types.txt:1769`

The header comment says "One per realm, culture-locked". Both restrictions live in `visible`
(lines 1777-1778) and neither appears in `creation_visible` (lines 1780-1782), which only
checks the advance. `visible` gates the diplomacy list; `creation_visible` gates the release
and peace-treaty paths. Compare `artists_commune` and `scientific_college`, which correctly
put their one-per-realm `NOT = { any_subject = ... }` in `creation_visible`.

**Fixed.** The one-per-realm check and the estate privilege requirement were duplicated into
`creation_visible`; the check stays in `visible` too, since the two gate different paths.

The exact-culture test could not be duplicated across, for the reason in 2.1: `creation_visible`
has no target scope. `only_overlord_or_kindred_culture = yes` covers the creation path.

### 2.4 The federal upgrade cooldown was inverted and therefore dead

**Status: fixed. Armed by `imperial_council_member`, the tier it gates.**

`in_game/common/subject_types/cc_subject_types.txt:2301` and `:2413`

`equal_federal_member` and `lesser_federal_member` both check
`scope:target = { NOT = { has_variable = imperial_council_cooldown } }` in
`enabled_through_diplomacy`, and both **set** that variable in their own `on_enable`.
`imperial_council_member`, the type you upgrade *from*, never sets it.

So on the intended path (council member -> equal/lesser) the variable is never present and the
25-year maturation gate is a no-op. It only becomes relevant after the upgrade, at which point
`visible_through_diplomacy` already requires `is_subject_type = imperial_council_member` and
the option is hidden regardless.

Compare the enclave chain, which gets this right: `elite_enclave.on_enable` sets
`enclave_cooldown`, and `palatinate.enabled_through_diplomacy` checks it.

**Fixed.** `imperial_council_member` gained an `on_enable` that arms the cooldown, and the
redundant writes were removed from the two upgraded tiers so there is exactly one writer. This
is now the same shape as `elite_enclave` arming `enclave_cooldown` for `palatinate`, where only
the base tier writes and only the upgrade reads.

The gate is live for the first time, so the 25-year maturation delay on federal upgrades will
now actually be felt.

### 2.5 `puppet_state_advance` never actually required its prerequisites

**Status: fixed. `allow` now uses `has_advance`.**

`in_game/common/advances/cc_subject_advances.txt:412-417`

```
allow = {
    OR = {
        has_advance_available = shadow_diplomacy_advance
        has_advance_available = client_state_advance
    }
}
```

`has_advance_available` means "can be researched", not "has been researched". Since both
prerequisites are `age_2`/`age_3` advances with only a `cc_subject_types_available` potential,
they are available to almost everyone, so `allow` passes without either being taken. The
sibling advance `naval_administration_advance` (line 376) and `military_march_advance`
(line 520) both use `has_advance` in `allow` and `has_advance_available` in `potential`, which
is the correct split.

**Fixed.** `allow` now uses `has_advance`; `potential` keeps `has_advance_available`, which is
the correct split and the one `naval_administration_advance` and `military_march_advance`
already used. The advance chain documented in the file header holds for the first time, so
puppet states now genuinely require a shadow state or client state line behind them.

### 2.6 `equal_federal_member` set annexation parameters it can never use

**Status: fixed. Kept `can_be_annexed = no`, dropped the four dead settings.**

`in_game/common/subject_types/cc_subject_types.txt:2333-2338`

`can_be_annexed = no` followed by `annexation_speed`, `annexation_min_years_before`,
`annexation_min_opinion` and `annexation_stall_opinion`. The four settings are dead. No other
`can_be_annexed = no` type in the file does this.

### 2.7 Palatinate carries very large cultural modifiers

**Status: reviewed and confirmed intentional. No action.**

`in_game/common/subject_types/cc_subject_types.txt`

```
cultural_influence = 500
cultural_tradition = 500
```

`elite_enclave`, the tier it upgrades from, grants 8 and 8, and `artists_commune` grants 10, so
this reads at first glance like a leftover debug value. It is not: the palatinate is the
mod's cultural beacon subject, and saturating both values is the point of the tier. The gap
against the tier below is the reward for the upgrade, not an oversight.

Recorded here so a future reviewer does not re-open it. If the numbers ever do need revisiting
it is a balance decision, not a defect.

### 2.8 The subject-bond ledger can never lapse

**Status: resolved as documentation. The ledger is permanent by design.**

`in_game/common/situations/cc_subject_bonds.txt:24-32`

```
can_end = {
    always = no
    # NOT = { any_country = { is_overlord = yes  any_subject = { has_variable = cc_bond_initialized } } }
}
```

The comment two lines above says "Lapses when no overlord anywhere still tracks a bond
(e.g. game rule turned off mid-game, or every dependency lost). Re-spawns automatically when
one returns." The code says the opposite. The `visible` block does keep the panel hidden from
players without tracked bonds, so this is mostly a documentation defect plus a permanently
resident situation entry.

**Resolved as documentation.** The ledger is permanent by design: it is an informational
panel, not a crisis, and tying its lifetime to "does any overlord still track a bond" would
make it spawn and despawn as dependencies come and go. The commented-out block was deleted and
the comment above `can_end` rewritten to say so, noting that `visible` already hides it from
every court with nothing to show, so a resident situation with no viewers costs nothing.

### 2.9 Invasion of Mexico painted the entire world map

**Status: fixed. Both branches now test theatre presence.**

`in_game/common/situations/cc_invasion_mexico.txt:504-509` and `:482-487`

```
else_if = {
    limit = { owner ?= { NOT = { is_capital_mesoamerica = yes } } }
    value = owner.country_color
}
```

That predicate matches every owned location on Earth whose owner's capital is not in
Mesoamerica, so the situation map mode colours and tooltips the whole globe, and
`ccim_colonial_power_tt` is shown for locations with no connection to the invasion. The
`tooltip` block has the same catch-all.

Every vanilla situation narrows its final branch to actual participants
(`italian_wars`, `colonial_revolution`, `reformation`, `golden_age_of_piracy` all checked),
and the mod's own `cc_balance_of_power` narrows its third branch to
`cc_bop_eligible_country = yes`.

**Fixed.** Both third branches now carry the same presence test the `visible` block uses, so
they match only countries actually in the theatre. Everything outside falls through to
`define:NMapColors|DEFAULT_COLOR`, as it already did for unowned land.

### 2.10 Invasion of Mexico had no start-year ceiling

**Status: fixed. `can_start` requires `current_year < 1580`.**

`in_game/common/situations/cc_invasion_mexico.txt:11` vs `:53`

`can_end` fires on `current_year > 1600`, but `can_start` has no upper bound. A game where a
qualifying power first establishes Mesoamerican presence after 1600 will spawn the situation
and satisfy `can_end` immediately, firing the announcement (`.1`), the three federation
requests, the defensive-preparation events and then `.35`/`.36` in short order.

**Fixed** with `current_year < 1580` rather than 1600, so a late start still gets twenty
years before the backstop closes it. A cutoff at 1600 would remove the instant end but still
allow a one-year situation. A foothold established after 1580 is too late to be the invasion
this situation models.

---

## Severity 3: dead state and unfinished threads

### 3.1 Variables written but never read

Verified with `tools/var_refs.py` plus a manual `.gui` sweep (the `cc_bop_*_pct` variables are
read by `cc_balance_of_power.gui`, so they are not on this list).

| Variable | Written at | Note |
|---|---|---|
| `cc_bond_loyal_primed` | `cc_bond_monitor.txt:206` | The whole "priming flags" block (section 7, lines 199-244) computes three states nothing consumes |
| `cc_bond_disloyal_primed` | `cc_bond_monitor.txt:227` | as above |
| `cc_bond_revolutionary_primed` | `cc_bond_monitor.txt:234` | as above |
| `cc_bond_betrayal_count` | `cc_bond_pulse.txt:581` | Incremented on betrayal, initialised to 0, never read |
| `lesser_partner_maturation` | `cc_subject_types.txt:237` | Set and removed by `lesser_partner`; the parallel `junior_partner_maturation` *is* read, so this is the stub of a tier above `lesser_partner` that was never built |
| `cc_bond_chain_b_active` | `cc_bond_chain_b.txt:73` | Documented in the file header as "chain is in progress"; nothing checks it, so chain B has no re-entrancy guard |
| `cc_bond_mem_crisis_managed` | `cc_bond_chain_b.txt:381,413,450,477,511` | Set by all five options of `cc_bonds.112`, so it does not discriminate anyway, and `cc_bonds.113` never reads it |
| `cc_bond_mem_merchant_rival` | `cc_bond_chain_b.txt:276` | Header documents it as "111 option C chosen (obstructed)"; unread |
| `cc_bond_mem_second_is_foreign` | `cc_bond_chain_b.txt:169` | Header documents it; unread |
| `cc_bond_trade_post_target` | `cc_bond_chain_b.txt:673` | Set then removed 110 lines later without an intervening read |
| `cc_minister_resentful` | `cc_cabal_events.txt:191` and 5 more | Six writes, no reads |
| `cc_patron_of_faith_active` | `cc_subject_events.txt:4952,4965,4978` | Set, never removed, never read |
| `cc_cabinet_character` | `cc_duty_free_hands.txt:25` | Set from `cabinet_member`, removed, never read |

Chain B is the notable cluster: its header (lines 11-21) documents an eleven-variable memory
model, of which four are never consumed. Chains A, C, D and the per-type files use the same
`cc_bond_mem_*` pattern correctly (checked `cc_bond_mem_fort_*`, `cc_bond_mem_council`,
`cc_bond_mem_heir_at_court`, `cc_bond_mem_cultures_differ`), so chain B is the outlier, not the
pattern.

### 3.2 `cc_bop_war_footing` is fully built and never applied

**Status: reviewed. Intentionally disabled for now; keep the modifier and its localisation.**

The static modifier is defined (`main_menu/common/static_modifiers/cc_event_modifiers.txt:1687`)
and localised in English, French, German and Spanish
(`cc_modifiers_l_*.yml:271-272`). Its only reference in script is inside the commented-out
`every_country` block at `cc_balance_of_power.txt:190-199`.

The grant is switched off deliberately, not by oversight, so the modifier and its eight
localisation lines stay put against the block being switched back on. Recorded here only so a
future dead-content sweep does not delete them.

### 3.3 The `italian_wars` start gate was commented out but still documented

**Status: resolved as documentation. The gate stays out; the comment now says why.**

`in_game/common/situations/cc_balance_of_power.txt`

The comment claimed "no stable balance can form while Italy is still contested or the wars of
religion rage", but `situation:italian_wars = { situation_is_active = no }` was commented out
and only the war-of-religions half was live.

Restoring it would have been dead weight. Vanilla `italian_wars.can_end` reduces to
`years_since_situation_start > 50`: the final clause of its `OR` repeats the outer `AND`
condition verbatim, so every other clause is redundant and the situation always closes fifty
years after it opens. It cannot start before 1450, and `age_5_absolutism` is date-gated to
**1637** (`in_game/common/age/00_default.txt:231`), which is the earliest the balance of power
can become eligible. The Italian Wars are therefore always long over by then, and a gate on
them could never bind in any game.

The commented line was deleted and the comment rewritten to record that reasoning, so the next
reader does not restore it. The `war_of_religions` gate stays: it starts from 1590 and ends
only by peace treaty, by Westphalia, or by the age-6 fallback in `war_of_religions_end_trigger`,
so it genuinely can still be running when the balance would otherwise form.

### 3.4 Balance-of-power ending payoffs were uneven

**Status: fixed. Hegemony now pays out to four audiences; the deluge crowns exactly one power.**

`in_game/common/scripted_effects/cc_bop_effects.txt`

Two separate problems. Hegemony rewarded only the winner and the losers, leaving the bloc that
backed the winner and the courts that stayed out with nothing after decades in the situation.
The deluge did the opposite, sweeping every eligible eastern great power with
`cc_bop_scourge_of_the_west` and event `.72`, so two or three powers could be crowned at once.

**Hegemony ending, who now sees what:**

| Audience | Modifier | Event |
|---|---|---|
| Preponderance leader | `cc_bop_master_of_europe` (100 yr) | `.70` |
| Preponderance members | `cc_bop_hegemons_client` (40 yr), new | `.79`, new |
| Coalition members | `cc_bop_humbled_power` (40 yr) | `.71` |
| Engaged unaligned | `cc_bop_unaligned_broker` (40 yr), new | `.69`, new |

`cc_bop_hegemons_client` grants `court_spending_efficiency = 0.15`,
`antagonism_received_modifier = -0.15` and a little prestige: sheltering under the new master
is cheap and nobody dares resent you, but the standing is the hegemon's.
`cc_bop_unaligned_broker` grants `diplomatic_reputation = 1`.

"Neutral" means `has_variable = cc_bop_engaged` and membership of neither pole, so the reward
goes to courts the situation actually drew in and that then kept their hands free, not to every
bystander on the map.

**Deluge ending:** `cc_bop_scourge_of_the_west` and `.72` now go only to the eastern power that
led the preponderant bloc. The modifier was raised to the same weight as
`cc_bop_master_of_europe` but kept in eastern coin (manpower and momentum rather than
diplomacy) and its duration raised from 60 to 100 years to match. Non-leader eastern great
powers get nothing: one power broke the balance, the rest merely stood on the same side of the
map. The `cc_bop_western_bulwark` loop for non-eastern powers is unchanged.

**One implementation trap worth knowing.** `cc_bop_cleanup` destroys both pole IOs immediately
after `cc_bop_apply_ending` fires these events, so `.69` and `.79` cannot look the hegemon up
through `international_organization:cc_bop_preponderance.leader_country` when their `immediate`
runs. They instead resolve it by `has_country_modifier = cc_bop_master_of_europe`, which is on
exactly one country and persists. This is the same pattern `.70` already used for its
`bop_humbled` lookup. Both loops are additionally guarded on a surviving leader, because both
events name it in their text.

### 3.5 `cc_bop_eastern_power` had two unreachable clauses

**Status: fixed. Both removed, provably without behaviour change.**

`in_game/common/scripted_triggers/cc_bop_triggers.txt`

The trigger accepted `sub_continent:north_asia` and `sub_continent:central_asia`, but all three
call sites pair it with `cc_bop_eligible_country`, which accepts only `western_europe`,
`eastern_europe`, `north_africa`, `crescent_region` and `anatolia_region`.

Checked against `in_game/map_data/definitions.txt`, the sub-continents resolve as:

| Sub-continent | Regions | Eligible? |
|---|---|---|
| `eastern_europe` | carpathia, baltic, ruthenia, caucasus, steppes, russian, ural, balkan | all |
| `middle_east` | **anatolia**, **crescent**, arabia, persia | first two only |
| `north_asia` | west_siberia, east_siberia | none |
| `central_asia` | khorasan | none |

So the effective eastern set was already `eastern_europe` plus the Ottomans and Levantine
powers, which is exactly the intended flavour. `north_asia` and `central_asia` contributed
nothing and are gone.

All three call sites were verified to pair with `cc_bop_eligible_country`, including the
negated `cc_bop_eastern_power = no` in the deluge branch's western-bulwark loop, so the removal
cannot change any evaluation.

The comment above the trigger now spells out the intersection and notes that widening the
deluge to Persia or the steppe khanates means adding their regions to `cc_bop_eligible_country`
first, not re-adding clauses here.

### 3.6 98 bond events omit `outcome`

Every event in `cc_bond_aor`, `cc_bond_chain_a`-`e`, `cc_bond_colonial_nation`,
`cc_bond_dependency`, `cc_bond_federal`, `cc_bond_governorate`, `cc_bond_march`,
`cc_bond_palatinate`, `cc_bond_puppet`, `cc_bond_red_herrings` and `cc_bond_status_reveals`
lacks an `outcome` line. Vanilla sets it on essentially every non-hidden event (7,434
`outcome` against 7,409 `title`), and the rest of the mod does too, including all 130
balance-of-power events. Cosmetic, but it makes the bond subsystem read differently from
everything else in the frame styling.

### 3.7 Minor

**Status: all three fixed.**

- `naval_administration` was indented with spaces where the rest of
  `cc_subject_types.txt` uses tabs. Seven lines converted.
- The second `modifier` block inside the `.47` entry of the marriage-of-state `random_list`
  (`situations/cc_balance_of_power.txt`) sat one tab deeper than its sibling, which made it
  read as nested inside the first. Re-indented to match.
- `cc_bop_apply_ending`'s final `else` doubled as both the concert ending and a catch-all for
  "situation ended with no flag set". Already resolved as part of 1.6: it is now
  `else_if = { limit = { situation:cc_balance_of_power = { has_variable = cc_bop_flag_concert } } }`,
  which mattered once that branch started founding a real institution.

A sweep for the same space-indent defect turned up two more files outside the original finding,
`on_action/cc_game_start.txt` and `on_action/cc_legacy_pulse.txt` (three lines each), fixed at
the same time. No space-indented lines remain anywhere in `in_game/` or `main_menu/`.

---

## Fixes applied

**The `policy_vote` override was deleted** and the coalition congress rewired to the vanilla
`special_status_power` hook. See 1.1 for the full change list.

**Chartered company sub-continent gate** (1.5), `in_game/common/subject_types/cc_subject_types.txt`
lines 964 and 971. `sub_continent = root.capital.continent` compared mismatched geography
types and never matched, disabling the restriction entirely. Changed to
`root.capital.sub_continent`.

**Truncated dot-chain in chain C**, `in_game/events/cc_bond_chain_c.txt:48`. The `limit` in
`cc_bonds.120`'s `immediate` block is meant to mirror its `trigger` block, but read
`capital.continent = root.capital` (comparing a continent against a country scope) where the
trigger at line 23 correctly reads `root.capital.continent`. The `OR` still passed via
`total_development > 100`, so `random_subject` was selecting from a different population than
the trigger had validated. Corrected to match line 23.

Two further identifier defects were corrected while writing the review.

**`estate_type:military` does not exist** (4 occurrences, `in_game/events/cc_hyw_events.txt`
lines 103, 156, 333, 745). Vanilla defines seven estates
(`nobles`, `clergy`, `burghers`, `peasants`, `dhimmi`, `tribes`, `cossacks`) and never uses
`estate_type:military` anywhere. The engine logs an unknown-estate error and the illustration
background falls back. Changed to `estate_type:nobles_estate`, matching each event's
foreground.

**Duplicate `annexation_min_years_before`** in `artists_commune` and `scientific_college`
(`in_game/common/subject_types/cc_subject_types.txt`). Each set it twice, `15` near the top and
`75` further down; the engine takes the last silently, so `75` was already the live value. The
dead `15` lines were removed and a comment now points at the surviving assignment. No behaviour
change.

---

## Suggested order of work

1. Decide keep-or-cut on the dead state in 3.1. The largest single item is the
   `cc_bond_monitor` priming block, which computes three states nothing reads.
2. Optional: the 98 bond events missing `outcome` in 3.6, and the dead commented gates in
   `naval_administration` noted under 1.8.

**Severity 1 is clear.** 1.1 (override deleted, coalition rewired to the vanilla
`special_status_power` hook), 1.2 and 1.3 (fixed, including the mirrored culture check), 1.4
(intentional), 1.5 (fixed), 1.6 (fixed, equilibrium concert founded from both blocs), 1.7
(fixed, five-year floor plus mutual exclusion), 1.8 (intentional, parliament-only by design),
1.9 (fixed), plus the `cc_bond_chain_c` dot-chain listed under
[Fixes applied](#fixes-applied).

**Severity 2 is clear.** 2.1 through 2.6 and 2.8 through 2.10 resolved: seven code fixes plus
2.8 resolved as documentation. 2.7 reviewed and confirmed intentional.

**Severity 3: 3.3, 3.4, 3.5 and 3.7 resolved, 3.2 confirmed intentional.** What remains is
dead state (3.1) and one cosmetic consistency gap (3.6). Neither affects a running game.

## Worth re-testing in game

The three balance-of-power fixes change end-state behaviour and none of it is visible in the
error log, so a broken one will look like a quiet ending rather than a failure:

- Reach the equilibrium ending (age 6, 40+ years, share held between 40 and 60) and confirm the
  Concert IO is actually created, seats five powers drawn from **both** blocs, and that both
  poles disappear.
- Reach the coalition victory ending with `policy:cc_bop_enact_concert` passed and confirm the
  former hegemon is excluded and returns 50-75 years later via `cc_concert_readmission_pulse`.
- Let an equilibrium concert lapse and a second balance form 25 years on: the old Concert IO
  should be dissolved by `on_start`, not left standing beside the new poles.
- Enter age 6 with `the_revolution` already active and confirm the situation now runs rather
  than opening and closing in one month.

Two severity-2 fixes also change gating that no log will report:

- 2.4 arms a maturation gate that had never fired. Upgrading an `imperial_council_member` to
  either federal tier should now be refused for 25 years after the council membership begins.
- 2.2 and 2.3 tighten the release and peace-treaty creation paths. Confirm you can still create
  a `provincial_governorate`, `tax_farm` or `military_march` by releasing a country on your own
  continent, and a `chartered_company` only off your capital's sub-continent.
- 3.4 adds two events. On a hegemony ending, confirm `.79` reaches the preponderant bloc's
  rank and file and `.69` reaches the engaged unaligned, and that both render the hegemon's
  name rather than a blank, which is what the modifier-based scope lookup is there to prevent.
