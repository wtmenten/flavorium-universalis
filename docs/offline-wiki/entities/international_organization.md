# International organization modding

**Source:** https://eu5.paradoxwikis.com/International_organization_modding

---

**International organization modding** covers the creation and modification of international organizations in Europa Universalis V. These include organizations like the Holy Roman Empire, coalitions, crusades, and defensive leagues.

International organizations are stored in /Europa Universalis V/game/in_game/common/international_organizations/ as individual `.txt` files.

## Organization structure

An international organization definition is complex and includes membership, leadership, and governance:

```
organization_name = {
    has_target = no                     # Whether org targets a country
    unique = yes                        # Only one instance can exist
    expel_members_who_are_targets_of_other_members = no

    show_leave_message = no
    use_laws_as_join_reason = no

    # Leadership configuration
    has_leader_country = yes
    leader_title_key = "LEADER_TITLE"
    use_regnal_number = yes
    leader_type = character             # character or country
    leader_change_trigger_type = rulerchange
    leader_change_method = vote
    disband_if_no_leader = no

    # Parliament configuration
    has_parliament = yes
    parliament_type = assembly_type
    resolution_widget = parliament
    has_dynastic_power = yes

    # War mechanics
    only_leader_country_joins_defensive_wars = yes
    gives_military_access_to_all_when_at_war = yes

    join_defensive_wars_always = { trigger }
    join_defensive_wars_auto_call = { trigger }
    can_declare_war = { trigger }

    # Membership modifiers
    modifier = {
        block_from_change_to_kingdom_rank = yes
    }
    leader_modifier = {
        diplomatic_capacity = 1
    }
    international_organization_modifier = {
        max_elector = 4
    }

    # Membership triggers
    create_visible_trigger = { trigger }
    invite_visible_trigger = { trigger }
    can_lead_trigger = { trigger }
    can_join_trigger = { trigger }
    can_leave_trigger = { trigger }
    auto_leave_trigger = { trigger }
    auto_disband_trigger = { trigger }
    can_vote_in_parliament = { trigger }

    # Effects
    on_joined = { effect }
    on_left = { effect }
    monthly_effect = { effect }

    # Variables
    variables = {
        variable_name = {
            format = "FORMAT_KEY"
            min = 0
            max = 100
            monthly_change = { script_value }
        }
    }

    # Special statuses
    special_statuses_implemented = {
        status_1
        status_2
    }

    # AI decision making
    ai_desire_to_join = { script_value }
    ai_desire_to_allow_new_member = { script_value }
    ai_issue_voting_bias = { script_value }

    # Land ownership rules
    land_ownership_rule = rule_name
    antagonism_modifier_for_taking_land_from_fellow_member = 0.75
    no_cb_price_modifier_for_fellow_member = 0.75
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`has_target`|Whether organization targets specific countries|
|`unique`|If true, only one instance can exist|
|`has_leader_country`|Whether organization has a leading country|
|`leader_type`|`character` or `country`|
|`leader_change_method`|How leader changes: `vote`, `hereditary`|
|`has_parliament`|Whether organization has voting parliament|
|`parliament_type`|Type of parliament assembly|
|`has_dynastic_power`|Whether dynasties have power in organization|

## Modifier blocks

### modifier

Applied to all member countries:

```
modifier = {
    block_from_change_to_kingdom_rank = yes
    reject_subjugation_reasons = 25
}
```

### leader_modifier

Applied only to the leading country:

```
leader_modifier = {
    diplomatic_capacity = 1
    great_power_score_exempt_from_forfeit = 250
}
```

### international_organization_modifier

Applied to the organization itself:

```
international_organization_modifier = {
    hre_max_elector = 4
    hre_max_archbishop_elector = 3
}
```

## Variables

Organizations can track custom variables with monthly changes:

```
variables = {
    imperial_authority = {
        format = "IMPERIAL_AUTHORITY_DISPLAY"
        change_format = "VARIABLE_CHANGE_FORMAT"
        min = 0
        max = 100
        monthly_change = {
            add = {
                desc = "INTERNAL_PEACE"
                if = {
                    limit = { international_organization_has_internal_peace = no }
                    value = 0
                }
                else = {
                    value = 0.05
                }
            }
        }
    }
}
```

## Special statuses

Define special positions within the organization:

```
special_statuses_implemented = {
    emperor
    elector
    archbishop_elector
    free_city
}
```

## Parliament

For an IO parliament to be functional, at least one issue should be applicable. Otherwise the parliament will try to call upon country-specific parliament issues, printing many errors in the log.

## Base game organizations

- `hre` - Holy Roman Empire
- `catholic_church` - Catholic Church
- `coalition` - Anti-aggressor coalitions
- `crusade` - Religious crusades
- `defensive_league` - Defensive alliances
- `independence_movement` - Independence wars

## Example

```
my_custom_league = {
    has_target = no
    unique = no

    has_leader_country = yes
    leader_title_key = "LEAGUE_LEADER"
    leader_type = country
    leader_change_method = vote
    disband_if_no_leader = yes

    modifier = {
        defensive_war_morale = 0.1
    }

    leader_modifier = {
        diplomatic_reputation = 1
    }

    can_join_trigger = {
        is_neighbor_of_international_organization = scope:recipient
    }

    can_leave_trigger = {
        NOT = { is_leader_of_international_organization = scope:recipient }
    }

    on_joined = {
        add_prestige = 5
    }

    ai_desire_to_join = {
        add = {
            desc = "THREATENED"
            if = {
                limit = { any_neighbor_country = { is_threat_to = root } }
                value = 50
            }
        }
    }
}
```

## References


