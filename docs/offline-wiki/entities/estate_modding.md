# Estate modding

**Source:** https://eu5.paradoxwikis.com/Estate_modding

---

**Estates modding** covers the creation and modification of estates in Europa Universalis V. Estates represent the major power groups within a country: Crown, Nobles, Clergy, Burghers, Peasants, and others.

Estates are stored in /Europa Universalis V/game/in_game/common/estates/ as `.txt` files.

## Estate structure

An estate definition specifies power calculations, modifiers, and opinion factors:

```
estate_name = {
    color = estate_color                    # Color identifier for UI

    power_per_pop = 25                      # Power gained per pop
    tax_per_pop = 150                       # Tax income per pop

    rival = -0.01                           # Rivalry factor with other estates
    alliance = 0.01                         # Alliance factor with other estates

    revolt_court_language = court_language  # Language used in revolts

    # Character spawning rules
    characters_have_dynasty = always        # always, sometimes, never
    can_spawn_random_characters = yes
    can_generate_mercenary_leaders = yes
    use_diminutive = no

    bank = yes                              # Can loan money

    # Ruler estate specific
    ruler = yes
    priority_for_dynasty_head = yes

    # Satisfaction modifiers (multiplied by satisfaction - threshold)
    satisfaction = {
        counter_espionage = 0.2
        monthly_prestige = 0.2
    }

    # High power modifiers (when power > threshold)
    high_power = {
        nobles_estate_max_tax = -0.5
        levy_combat_efficiency_modifier = 1.0
    }

    # Low power modifiers (when power < threshold)
    low_power = {
        nobles_estate_max_tax = 0.5
    }

    # Power-based modifiers (scaled by power)
    power = {
        parliament_base_support = 0.5
        trade_income = 1.0
    }

    # Opinion calculations for diplomacy
    opinion = {
        add = {
            desc = "ESTATE_OPINION_BASE"
            value = "opinion(scope:target)"
            multiply = 0.05
        }
    }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`color`|Color identifier for UI display|
|`power_per_pop`|Estate power gained per pop of this type|
|`tax_per_pop`|Tax income generated per pop|
|`rival`|Natural rivalry with other estates (negative = rivalry)|
|`alliance`|Natural alliance with other estates|
|`revolt_court_language`|Language rebels use: `court_language`, `common_language`, `liturgical_language`|
|`characters_have_dynasty`|`always`, `sometimes`, `never`|
|`can_generate_mercenary_leaders`|Whether estate can provide mercenary leaders|
|`bank`|Whether estate can provide loans|
|`ruler`|If true, this is the ruling estate (crown)|
|`use_diminutive`|Use diminutive names for characters|

## Modifier blocks

### satisfaction

Modifiers scaled by `(satisfaction - LOW_SATISFACTION_THRESHOLD)`

### high_power

Modifiers applied when `(relative_power - LOW_POWER_THRESHOLD) > 0`

### low_power

Modifiers applied when `(relative_power - LOW_POWER_THRESHOLD) < 0`

### power

Static modifiers scaled by estate power

## Opinion block

Calculates diplomatic opinion from this estate toward other countries:

```
opinion = {
    add = {
        desc = "DESCRIPTION_KEY"
        value = some_value
        multiply = 0.05
    }

    if = {
        limit = { condition }
        add = {
            desc = "CONDITIONAL_OPINION"
            value = 10
        }
    }
}
```

## Base game estates

- `crown_estate` - The ruling power
- `nobles_estate` - Aristocracy
- `clergy_estate` - Religious leaders
- `burghers_estate` - Merchant class
- `peasants_estate` - Common farmers
- `dhimmi_estate` - Protected religious minorities
- `tribes_estate` - Tribal peoples
- `cossacks_estate` - Cossack communities

## Example

```
my_custom_estate = {
    color = custom_estate_color
    power_per_pop = 5
    tax_per_pop = 50
    rival = -0.01
    alliance = 0.01

    revolt_court_language = common_language
    characters_have_dynasty = sometimes
    can_generate_mercenary_leaders = yes

    satisfaction = {
        global_unrest = -0.5
        research_speed_modifier = 0.1
    }

    high_power = {
        global_monthly_development_modifier = 0.1
        monthly_towards_innovative = societal_value_significant_monthly_move
    }

    low_power = {
        global_monthly_development_modifier = -0.1
    }

    opinion = {
        add = {
            desc = "ESTATE_OPINION_BASE"
            value = "opinion(scope:target)"
            multiply = 0.05
        }
    }
}
```

## References


