# Trait modding

**Source:** https://eu5.paradoxwikis.com/Trait_modding

---

**Traits modding** covers the creation and modification of character traits in Europa Universalis V. Traits define personality and abilities of rulers, generals, admirals, and other characters.

Traits are stored in /Europa Universalis V/game/in_game/common/traits/ as `.txt` files organized by character type.

## Trait structure

A trait definition specifies conditions, category, and modifiers:

```
trait_name = {
    allow = {
        # Conditions for trait to be available
        adm > 33
        NOT = { has_trait = conflicting_trait }
    }

    category = ruler                    # Character type
    flavor = personality                # Trait type

    modifier = {
        # Modifiers provided by trait
        global_estate_target_satisfaction = tiny_permanent_target_satisfaction
        monthly_towards_free_subjects = societal_value_minor_monthly_move
        peace_offer_fairness = 0.2
        stability_importance_modifier = 0.1
    }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`allow`|Trigger block for when trait can be assigned|
|`category`|Character type: `ruler`, `general`, `admiral`, `artist`, `child`, `religious_figure`|
|`flavor`|Trait flavor: `personality`, `education`, `interests`, `government_approach`|
|`modifier`|Modifiers applied when character has trait|

## Trait categories

- `ruler` - Rulers and heirs
- `general` - Army commanders
- `admiral` - Naval commanders
- `artist` - Court artists
- `child` - Children and heirs
- `religious_figure` - Religious characters

## Trait flavors

- `personality` - Character personality traits
- `education` - Traits from education/training
- `interests` - Character interests and hobbies
- `government_approach` - Governing style

## Allow block

Conditions for trait availability:

```
allow = {
    # Stat requirements
    adm > 33
    dip >= 50
    mil < 80

    # Incompatible traits
    NOT = { has_trait = cruel }
    NOT = { has_trait = zealot }

    # Context requirements
    owner ?= {
        government_type = government_type:monarchy
    }

    # Always available/unavailable
    always = yes
    always = no
}
```

## Common modifiers

### Government

```
country_cabinet_efficiency = 0.1
legislative_efficiency = 0.1
stability_cost = -0.1
court_spending_cost = -0.01
```

### Military

```
military_tactics = 0.05
discipline = 0.05
land_morale_modifier = 0.05
army_initiative = 0.2
```

### Diplomacy

```
diplomatic_reputation = 1
improve_relation_impact = 0.2
peace_offer_fairness = 0.1
peace_offer_negotiation_power = 0.25
```

### AI behavior

```
aggressiveness_modifier = 0.1
carefulness_modifier = 0.1
win_war_chance_threshold = -0.1
war_declaration_stab_hit_tolerance = 20
antagonism_tolerance = 10
bias_for_militarist_policies = 25
```

### Societal values

```
monthly_towards_innovative = societal_value_monthly_move
monthly_towards_traditionalist = societal_value_minor_monthly_move
monthly_towards_belligerent = societal_value_monthly_move
```

## Base game trait types

### Positive personality

`just`, `righteous`, `kind_hearted`, `calm`, `benevolent`, `tolerant`

### Negative personality

`cruel`, `malevolent`, `greedy`, `naive`, `craven`, `drunkard`

### Education

`tactical_genius`, `bold_fighter`, `intricate_web_weaver`, `charismatic_negotiator`, `silver_tongue`

### Government approach

`zealot`, `free_thinker`, `conqueror`, `expansionist`, `well_connected`

### Interests

`scholar`, `entrepreneur`, `lawgiver`, `martial_educator`, `architectural_visionary`

## Example

```
my_custom_trait = {
    allow = {
        adm >= 50
        NOT = { has_trait = incompatible_trait }
        owner ?= {
            government_type = government_type:republic
        }
    }

    category = ruler
    flavor = government_approach

    modifier = {
        research_speed_modifier = 0.15
        stability_cost = -0.15
        monthly_towards_innovative = societal_value_monthly_move
        global_estate_target_satisfaction = small_permanent_target_satisfaction
        institution_importance_modifier = 0.2
        bias_for_administrative_policies = 25
    }
}
```

## Special traits

Some traits have special effects:

```
unsuited_for_country_ruling = {
    allow = { always = no }    # Only given by events
    category = ruler
    modifier = {
        blocked_from_being_ruler = yes
    }
}

eunuch = {
    allow = { always = no }    # Only given by events
    category = ruler
    modifier = {
        character_life_expectancy = 10
        blocked_from_marriage = yes
        character_fertility = -1000
    }
}
```

## References


