# Mission modding

**Source:** https://eu5.paradoxwikis.com/Mission_modding

---

**Mission modding** covers the creation and modification of missions in Europa Universalis V. Missions are task trees that guide countries through specific objectives with rewards.

Missions are stored in /Europa Universalis V/game/in_game/common/missions/ as `.txt` files containing one or more mission definitions.

## Mission structure

A mission pack defines visibility conditions, tasks, and rewards:

```
mission_pack_name = {
    icon = mission_icon_name
    repeatable = yes                    # Whether mission can be done again
    player_playstyle = administrative   # Categorization for player preferences

    visible = {
        # Conditions for mission to appear
        game_has_missions_enabled = yes
        has_enabled_mission_trigger = { type = mission_pack_name }
    }

    enabled = {
        # Conditions for mission to be available
        exists = capital.market
    }

    chance = 3600    # AI weight to pick this mission

    select_trigger = {
        # Optional selection UI for mission targets
        looking_for_a = market
        target_flag = mission_target_market
        name = "mission_select_market"
    }

    on_start = {
        # Effects when mission is started
    }

    on_completion = {
        # Effects when all tasks complete
    }

    on_abort = {
        # Cleanup when mission is abandoned
    }

    # Mission tasks defined below
    mission_task_name = {
        icon = task_icon
        requires = { previous_task }
        enabled = { trigger }
        duration = 365              # Days to complete (0 = instant)
        on_completion = { effect }
    }
}
```

## Mission task structure

Tasks are the individual objectives within a mission:

```
task_name = {
    icon = icon_name
    requires = { prerequisite_task_1 prerequisite_task_2 }

    visible = { trigger }           # When task appears in tree
    enabled = { trigger }           # Conditions to complete task
    bypass = { trigger }            # Conditions to skip task

    duration = 365                  # Days required (0 = instant completion)
    final = yes                     # If yes, completing this ends mission

    highlight = { trigger }         # Highlight locations on map

    modifier_while_progressing = {
        # Modifiers applied during duration countdown
    }

    on_start = { effect }
    on_completion = { effect }
    on_persistent_completion = { effect }   # Also runs for select_trigger
    on_monthly = { effect }

    select_trigger = {
        # Optional: choose target when completing
        looking_for_a = location
        target_flag = target_location
    }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`icon`|Icon identifier for mission/task display|
|`repeatable`|Whether mission can be undertaken multiple times|
|`player_playstyle`|Category: `administrative`, `diplomatic`, `military`|
|`chance`|AI selection weight|
|`requires`|List of prerequisite tasks that must complete first|
|`duration`|Days to complete task (0 for instant)|
|`final`|If true, completing this task completes the mission|
|`bypass`|Conditions that allow skipping this task|

## Select trigger options

Used to let players choose targets:

```
select_trigger = {
    looking_for_a = location|market|goods|character
    source = actor
    target_flag = scope_name
    name = "localization_key"
    none_available_msg_key = "no_options_key"
    column = {
        data = name|population|development
    }
    visible = { trigger }
    enabled = { trigger }
}
```

## Playstyle categories

- `administrative` - Economy and development focused
- `diplomatic` - Relations and expansion focused
- `military` - War and conquest focused

## Example

```
my_custom_mission = {
    icon = my_mission_icon
    repeatable = no
    player_playstyle = military

    visible = {
        game_has_missions_enabled = yes
        tag = ENG
    }

    enabled = {
        army_size >= 10
    }

    chance = 1000

    on_completion = {
        add_prestige = 10
    }

    task_build_army = {
        icon = military_icon
        requires = { }
        enabled = {
            army_size >= 20
        }
        duration = 0
        on_completion = {
            add_military_power = 50
        }
    }

    task_win_battle = {
        icon = battle_icon
        requires = { task_build_army }
        enabled = {
            has_won_battle = yes
        }
        duration = 0
        final = yes
        on_completion = {
            add_country_modifier = {
                modifier = victorious_army
                years = 10
            }
        }
    }
}
```

## References


