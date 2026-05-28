# Institution modding

**Source:** https://eu5.paradoxwikis.com/Institution_modding

---

**Institutions modding** covers the creation and modification of institutions in Europa Universalis V. Institutions represent major societal developments that spread across the world over time.

Institutions are stored in /Europa Universalis V/game/in_game/common/institution/ as `.txt` files organized by age.

## Institution structure

An institution definition specifies spawn conditions and spread mechanics:

```
institution_name = {
    age = age_1_traditions              # Age when institution becomes available

    can_spawn = {
        # Conditions for institution to first appear
        continent = continent:europe
        has_owner = yes
        num_pop_type:nobles > 0.1
    }

    promote_chance = {
        # Factors affecting spawn probability
        add = {
            value = num_pop_type:nobles
            multiply = 10
        }
    }

    # Spread mechanics (hardcoded for optimization)
    spread_from_friendly_coast_border_location = {
        value = institution_base_spread_from_friendly_neighbor_with_early
        add = {
            value = num_pop_type:nobles
            multiply = 0.5
        }
    }
    spread_from_any_coast_border_location = institution_base_spread_from_neighbor_with_early
    spread_from_any_import = institution_trade_spread_value_early
    spread_scale_on_control_if_owner_embraced = 2
    spread_embraced_to_capital = institution_total_embraced_to_capital_early
    spread_to_market_member = institution_spread_to_market_member_early
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`age`|Age when institution can spawn: `age_1_traditions` through `age_6_revolutions`|
|`can_spawn`|Trigger block - conditions for institution to first appear in a location|
|`promote_chance`|Script value - factors that increase spawn probability|

## Spread mechanics

|Attribute|Description|
|---|---|
|`spread_from_friendly_coast_border_location`|Spread from friendly neighboring coastal locations|
|`spread_from_any_coast_border_location`|Spread from any neighboring coastal location|
|`spread_from_any_import`|Spread through trade routes|
|`spread_scale_on_control_if_owner_embraced`|Multiplier when owner has embraced|
|`spread_embraced_to_capital`|Spread rate to capital when country embraces|
|`spread_to_market_member`|Spread rate to market members|

## Spread script values

Common script values for spread rates:

- `institution_base_spread_from_friendly_neighbor_with_early`
- `institution_base_spread_from_neighbor_with_early`
- `institution_trade_spread_value_early`
- `institution_total_embraced_to_capital_early`
- `institution_spread_to_market_member_early`

## Ages

- `age_1_traditions` - Age of Traditions (game start)
- `age_2_renaissance` - Renaissance
- `age_3_discovery` - Age of Discovery
- `age_4_reformation` - Reformation
- `age_5_absolutism` - Age of Absolutism
- `age_6_revolutions` - Age of Revolutions

## Base game institutions

### Age 1 (Traditions)

- `feudalism` - European feudal system
- `legalism` - Legal systems and bureaucracy
- `meritocracy` - Asian merit-based governance

## Example

```
my_custom_institution = {
    age = age_3_discovery

    can_spawn = {
        continent = continent:europe
        has_owner = yes
        owner ?= { root = capital }
        location_rank = location_rank:city
        development >= 20
    }

    promote_chance = {
        add = {
            value = development
            multiply = 0.5
        }
        add = {
            value = num_pop_type:burghers
            multiply = 10
        }
    }

    spread_from_friendly_coast_border_location = institution_base_spread_from_friendly_neighbor_with_early
    spread_from_any_coast_border_location = institution_base_spread_from_neighbor_with_early
    spread_from_any_import = institution_trade_spread_value_early
    spread_scale_on_control_if_owner_embraced = 2
    spread_embraced_to_capital = institution_total_embraced_to_capital_early
    spread_to_market_member = institution_spread_to_market_member_early
}
```

## References


