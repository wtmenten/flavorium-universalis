# Law modding

**Source:** https://eu5.paradoxwikis.com/Law_modding

---

**Laws modding** covers the creation and modification of laws in Europa Universalis V. Laws are policies that countries can adopt, providing various modifiers and affecting gameplay.

Laws are stored in /Europa Universalis V/game/in_game/common/laws/ as `.txt` files organized by government type and category.

## Law structure

A law definition specifies categories, options, and modifiers:

```
law_group_name = {
    law_category = administrative       # Law category for UI
    law_gov_group = monarchy            # Government type restriction

    potential = {
        # Conditions for law group to appear
        government_type = government_type:monarchy
    }

    # Law options
    option_name = {
        unique = yes                    # Only one country can have this

        potential = {
            # When this option appears
            tag = XXX
        }

        allow = {
            # Conditions to select this option
            current_age = age_5_absolutism
        }

        country_modifier = {
            # Modifiers applied when selected
            monthly_legitimacy = 0.05
            stability_investment = small_stability_investment
        }

        estate_preferences = {
            # Which estates prefer this option
            clergy_estate
            nobles_estate
        }

        years = 2                       # Cooldown before changing
    }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`law_category`|Category: `administrative`, `military`, `economic`|
|`law_gov_group`|Government type: `monarchy`, `republic`, `theocracy`, `tribe`|
|`potential`|Trigger block for when law group appears|
|`unique`|If yes, only one country can select this option|
|`allow`|Conditions required to select the option|
|`country_modifier`|Modifiers applied when option is active|
|`estate_preferences`|Estates that favor this option|
|`years`|Cooldown years before law can be changed|

## Law categories

- `administrative` - Government and bureaucracy
- `military` - Military organization and levies
- `economic` - Trade and taxation
- `religious` - Religious policies
- `legal` - Legal systems

## Government groups

- `monarchy` - Monarchical governments
- `republic` - Republican governments
- `theocracy` - Religious governments
- `tribe` - Tribal governments

## Estate preferences

Estates that prefer certain law options:

```
estate_preferences = {
    crown_estate
    nobles_estate
    clergy_estate
    burghers_estate
    peasants_estate
}
```

## Base game law groups

### Monarchy Laws

- `feudal_de_jure_law` - Land inheritance (by tradition/by blood)
- `medieval_levy_law` - Military levy organization
- `royal_court_customs_law` - Court policy
- `legitimization_of_power_law` - Rulership philosophy
- `harem_law` - Harem policy (for applicable cultures)

### Military Laws

- `medieval_levy_law` - Levy recruitment policies

## Example

```
my_custom_law = {
    law_category = administrative
    law_gov_group = monarchy

    potential = {
        government_type = government_type:monarchy
    }

    traditional_approach = {
        country_modifier = {
            stability_cost = -0.1
            monthly_towards_traditionalist = societal_value_monthly_move
        }
        estate_preferences = {
            clergy_estate
            nobles_estate
        }
        years = 2
    }

    progressive_approach = {
        country_modifier = {
            research_speed_modifier = 0.1
            monthly_towards_innovative = societal_value_monthly_move
        }
        allow = {
            current_age = age_3_discovery
        }
        estate_preferences = {
            burghers_estate
        }
        years = 2
    }

    unique_country_approach = {
        unique = yes
        potential = {
            tag = ENG
        }
        country_modifier = {
            diplomatic_reputation = 1
            global_monthly_development_modifier = 0.05
        }
        estate_preferences = {
            crown_estate
        }
        years = 2
    }
}
```

## References


