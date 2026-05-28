# Pop modding

**Source:** https://eu5.paradoxwikis.com/Pop_modding

---

**Pops modding** covers the creation and modification of population types in Europa Universalis V. Pops represent different social classes and occupations in society.

Pop types are stored in /Europa Universalis V/game/in_game/common/pop_types/ as `.txt` files.

## Pop type structure

A pop type definition specifies behavior, estate assignment, and modifiers:

```
pop_type_name = {
    color = pop_color                   # Color for UI display

    editor = 0.05                       # Editor spawn weight

    assimilation_conversion_factor = 0.05   # Speed of cultural/religious change

    pop_food_consumption = 20.0         # Food consumed per pop

    city_graphics = 1.0                 # Contribution to city appearance

    # Estate assignments (conditions for which estate)
    dhimmi_estate = { is_dhimmi = yes }
    tribes_estate = { is_gaelic_clans = yes }
    nobles_estate = {}

    promotion_factor = 0.1              # Speed of promotion to other types
    migration_factor = 0.5              # Willingness to migrate

    upper = yes                         # Is upper class
    has_cap = yes                       # Has population cap
    grow = yes                          # Can grow naturally

    counts_towards_market_language = yes    # Affects market language

    # Promotion paths
    promote_to = burghers
    promote_to = clergy
    promote_to = nobles

    # Literacy effects
    literacy_impact = {
        local_cultural_tradition = 0.2
        local_monthly_control = 0.01
    }

    # Pop percentage effects
    pop_percentage_impact = {
        local_distance_from_capital_cost_modifier = 0.5
    }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`color`|Color identifier for UI display|
|`editor`|Weight for spawning in map editor|
|`assimilation_conversion_factor`|Speed of cultural/religious conversion|
|`pop_food_consumption`|Food consumed per pop unit|
|`city_graphics`|Contribution to city visual appearance|
|`promotion_factor`|Rate at which pops promote|
|`migration_factor`|Willingness to migrate|
|`upper`|If yes, considered upper class|
|`has_cap`|If yes, has a maximum population|
|`grow`|If yes, can grow naturally|
|`tribal_rules`|If yes, uses special tribal promotion|
|`promote_to`|Pop types this can promote to|
|`counts_towards_market_language`|Affects market language determination|

## Estate assignments

Pops can belong to different estates based on conditions:

```
# Default assignment (empty condition)
nobles_estate = {}

# Conditional assignment
dhimmi_estate = { is_dhimmi = yes }
tribes_estate = { is_gaelic_clans = yes }
cossacks_estate = { is_cossacks = yes }
```

## Impact modifiers

### literacy_impact

Modifiers scaled by literacy level:

```
literacy_impact = {
    local_cultural_tradition = 0.2
    local_monthly_control = 0.01
    local_production_efficiency = medium_production_efficiency_bonus
}
```

### pop_percentage_impact

Modifiers scaled by pop percentage:

```
pop_percentage_impact = {
    local_distance_from_capital_cost_modifier = 0.5
    local_unrest = 0.2
}
```

## Base game pop types

### Upper Class

- `nobles` - Aristocracy, military leadership
- `clergy` - Religious figures, scholars
- `burghers` - Merchants, urban middle class

### Working Class

- `laborers` - Urban workers, craftsmen
- `soldiers` - Military personnel
- `peasants` - Rural farmers (base pop type, promotes to others)

### Special

- `tribesmen` - Tribal peoples (can promote to peasants)
- `slaves` - Enslaved population

## Promotion chains

```
tribesmen -> peasants -> laborers/soldiers/burghers/clergy/nobles
```

## Example

```
my_custom_pop = {
    color = custom_pop_color

    editor = 0.2

    assimilation_conversion_factor = 0.2

    pop_food_consumption = 2.0

    city_graphics = 0.5

    # Belongs to burghers estate
    burghers_estate = {}

    promotion_factor = 0.3
    migration_factor = 0.2

    upper = no
    has_cap = yes
    grow = no

    promote_to = burghers

    literacy_impact = {
        local_production_efficiency = 0.1
        local_monthly_development_modifier = 0.05
    }
}
```

## References


