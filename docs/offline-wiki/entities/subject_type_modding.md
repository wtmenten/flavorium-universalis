# Subject type modding

**Source:** https://eu5.paradoxwikis.com/Subject_type_modding

---

**Subject type modding** covers the creation and modification of subject relationships in Europa Universalis V. Subject types define how overlords and subjects interact.

Subject types are stored in /Europa Universalis V/game/in_game/common/subject_types/ as individual `.txt` files.

## Subject type structure

A subject type defines the relationship between overlord and subject:

```
subject_type_name = {
    subject_pays = subject_pays_vassal  # Payment script value
    color = subject_vassal              # Color for UI
    level = 2                           # Hierarchy level

    # Visibility triggers
    visible_through_diplomacy = { trigger }
    visible_through_treaty = { trigger }
    creation_visible = { trigger }

    # War participation
    join_offensive_wars_always = { trigger }
    join_offensive_wars_can_call = { trigger }
    join_defensive_wars_always = { trigger }

    # Diplomatic costs
    diplomatic_capacity_cost_scale = 1.0

    # Military balance
    strength_vs_overlord = -0.5

    # Annexation settings
    annexation_speed = 1
    annexation_min_years_before = 10
    annexation_min_opinion = 150
    annexation_stall_opinion = 125
    overlord_can_cancel = yes

    # Overlord abilities
    can_overlord_build_roads = yes
    can_overlord_build_buildings = yes
    can_overlord_build_rgos = yes

    # Subject restrictions
    has_limited_diplomacy = yes
    has_overlords_ruler = no
    can_change_rank = no
    can_change_heir_selection = yes
    food_access = yes

    # Opinion requirements
    minimum_opinion_for_offer = 150

    # Great power mechanics
    great_power_score_transfer = 0.25

    # Institution spread
    institution_spread_to_overlord = monthly_institution_spread_mild
    institution_spread_to_subject = monthly_institution_spread_mild

    # Modifiers
    overlord_modifier = {
        monthly_prestige = 0.01
    }
    subject_modifier = {
        country_cabinet_efficiency = 0.05
    }

    # Effects
    on_enable = { effect }
    on_disable = { effect }

    # War declaration
    allow_declaring_wars = { trigger }

    # AI decision making
    diplo_chance_accept_subject = { factors }
    diplo_chance_accept_overlord = { factors }
    ai_wants_to_be_overlord = { factors }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`subject_pays`|Script value for subject payments|
|`color`|UI color identifier|
|`level`|Subject hierarchy level (1-5)|
|`diplomatic_capacity_cost_scale`|Diplomatic capacity cost multiplier|
|`strength_vs_overlord`|Military strength modifier against overlord|
|`annexation_speed`|Rate of integration|
|`annexation_min_years_before`|Years before annexation possible|
|`annexation_min_opinion`|Opinion required to annex|
|`great_power_score_transfer`|GP score transferred to overlord|
|`has_limited_diplomacy`|If yes, subject has diplomatic restrictions|
|`has_overlords_ruler`|If yes, shares overlord's ruler|

## War participation

```
join_offensive_wars_always = {
    NOT = { scope:actor ?= { is_subject_of = scope:recipient } }
}
join_offensive_wars_can_call = {
    scope:actor ?= { is_subject_of = scope:recipient }
}
join_defensive_wars_always = {
    always = yes
}
```

## Diplomatic acceptance

Factors affecting AI acceptance:

```
diplo_chance_accept_subject = {
    base = -90
    current_strength = 0.2
    border_distance = -0.3
    negative_opinion = -5
    positive_opinion = 0.25
    rank_difference = -5
    royal_ties = 1
    different_religion = -20
    same_common_language = 5
    different_government_type = -25
    competing_power = -200
    tax_base = -0.25
}
```

## Modifiers

### overlord_modifier

Applied to the overlord:

```
overlord_modifier = {
    monthly_prestige = 0.01
    diplomatic_reputation = 0.5
}
```

### subject_modifier

Applied to the subject:

```
subject_modifier = {
    country_cabinet_efficiency = 0.05
    army_maintenance_cost = -0.1
}
```

## Base game subject types

- `vassal` - Standard vassal relationship
- `tributary` - Pays tribute but maintains independence
- `colonial_nation` - Overseas colonial territory
- `march` - Military buffer state
- `fiefdom` - Personal land holding
- `samanta` - Indian feudal vassal

## Example

```
my_custom_subject = {
    subject_pays = subject_pays_custom
    color = subject_custom
    level = 2

    visible_through_diplomacy = {
        country_rank_level >= scope:target.country_rank_level
    }

    join_offensive_wars_can_call = {
        scope:actor ?= { is_subject_of = scope:recipient }
    }
    join_defensive_wars_always = {
        always = yes
    }

    diplomatic_capacity_cost_scale = 0.5
    strength_vs_overlord = -0.25

    annexation_speed = 0.5
    annexation_min_years_before = 20
    annexation_min_opinion = 200

    can_overlord_build_buildings = yes
    has_limited_diplomacy = no
    food_access = yes

    great_power_score_transfer = 0.1

    overlord_modifier = {
        monthly_prestige = 0.02
        diplomatic_capacity = 1
    }

    subject_modifier = {
        army_maintenance_cost = -0.15
        research_speed_modifier = 0.1
    }

    diplo_chance_accept_subject = {
        base = -50
        positive_opinion = 0.5
        same_religion = 20
        royal_ties = 10
    }
}
```

## References


