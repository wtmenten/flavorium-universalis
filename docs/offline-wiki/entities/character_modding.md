# Character modding

**Source:** https://eu5.paradoxwikis.com/Character_modding

---

**Character modding** covers character interactions in Europa Universalis V. Character interactions are actions that can be performed on or by characters such as rulers, heirs, and nobles.

Character interactions are stored in /Europa Universalis V/game/in_game/common/character_interactions/ as individual `.txt` files.

## Character interaction structure

An interaction defines conditions, costs, and effects:

```
interaction_name = {
    message = yes                   # Show notification
    is_consort_action = no          # Whether this affects consorts
    on_own_nation = yes             # Can be used within own nation

    price = price:interaction_price # Script value for cost

    price_modifier = {
        # Dynamic price adjustments
        add = 1
        if = {
            limit = { scope:recipient ?= { age_in_years > 40 } }
            subtract = {
                desc = "CHAR_AGE_LABEL"
                value = age_in_years
                subtract = 40
                multiply = 0.02
            }
        }
    }

    potential = {
        # Conditions for interaction to appear
    }

    allow = {
        # Conditions to enable interaction
        scope:actor = {
            has_heir = yes
        }
    }

    select_trigger = {
        # Target selection UI
        looking_for_a = character
        source = actor
        target_flag = recipient
        name = "choose_character"
        column = {
            data = name
        }
        visible = { trigger }
        enabled = { trigger }
    }

    effect = {
        # What happens when interaction is used
        scope:actor = {
            set_new_ruler = heir
        }
    }

    ai_tick = daily
    ai_tick_frequency = 120         # How often AI checks this

    ai_will_do = {
        # AI decision weight
        add = {
            desc = "REASON"
            value = some_value
        }
    }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`message`|Whether to show a notification message|
|`is_consort_action`|If true, interaction involves consorts|
|`on_own_nation`|If true, can only target own nation's characters|
|`price`|Cost to perform the interaction (uses price definition)|
|`price_modifier`|Dynamic modifications to the price|
|`potential`|Triggers for when interaction appears|
|`allow`|Triggers for when interaction can be used|
|`effect`|Effects executed when interaction is performed|
|`ai_tick`|How often AI evaluates: `daily`, `monthly`|
|`ai_tick_frequency`|Days between AI evaluations|
|`ai_will_do`|AI decision weight calculation|

## Select trigger

||Please help with verifying or updating this section. It was last verified for version 1.0.|

Used to let players choose character targets:

```
select_trigger = {
    looking_for_a = character
    source = actor
    target_flag = recipient
    name = "localization_key"
    column = {
        data = name
    }
    visible = {
        scope:actor = {
            ruler ?= root
        }
    }
    enabled = {
        is_adult = yes
    }
}
```

## Common character scopes

- `scope:actor` - The country initiating the action
- `scope:recipient` - The character being acted upon
- `root` - The current character in iteration

## Example

```
grant_title = {
    message = yes
    on_own_nation = yes

    price = price:grant_title_price

    potential = {
        scope:actor = {
            government_type = government_type:monarchy
        }
    }

    allow = {
        scope:recipient = {
            is_adult = yes
            NOT = { has_title = yes }
        }
    }

    select_trigger = {
        looking_for_a = character
        source = actor
        target_flag = recipient
        name = "select_noble"
        column = {
            data = name
        }
        visible = {
            estate_type = estate_type:nobles_estate
        }
        enabled = {
            is_adult = yes
        }
    }

    effect = {
        scope:recipient = {
            add_character_modifier = {
                modifier = titled_noble
                years = -1
            }
        }
        scope:actor = {
            add_estate_satisfaction = {
                type = estate_type:nobles_estate
                value = 0.05
            }
        }
    }

    ai_tick = monthly
    ai_tick_frequency = 60

    ai_will_do = {
        add = 10
        multiply = {
            value = scope:recipient.total_abilities
            multiply = 0.01
        }
    }
}
```

## References


