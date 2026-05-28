# Scripted gui

**Source:** https://eu5.paradoxwikis.com/Scripted_gui

---

**Scripted GUI** covers the creation of custom GUI elements that execute script effects in Europa Universalis V. Scripted GUIs allow modders to add interactive buttons and elements to the interface.

Scripted GUI definitions are stored in /Europa Universalis V/game/in_game/common/scripted_guis/ as `.txt` files. The actual GUI layout files are in /Europa Universalis V/game/<top_folder>/gui/.

## Scripted GUI structure

A scripted GUI definition connects triggers and effects to GUI elements:

```
scripted_gui_key = {
    scope = country                     # Scope type for the SGUI

    is_shown = {
        # Trigger: when SGUI is visible
        trigger
    }

    is_valid = {
        # Trigger: when SGUI can be activated
        trigger
    }

    effect = {
        # Effect: what happens on activation
        effect
    }

    saved_scopes = { scopes }           # Scopes to save for use in triggers/effects

    notification_key = key              # Notification when activated

    confirm_title = { }                 # Confirmation window title
    confirm_text = { }                  # Confirmation window text

    ai_is_valid = {
        # Trigger: whether AI can use this
        trigger
    }

    ai_chance = {
        # MTTH value 1-100: AI activation chance
    }

    ai_frequency = {
        # Script value: months between AI evaluations
    }
}
```

## Key attributes

|Attribute|Description|
|---|---|
|`scope`|Scope type: `country`, `character`, `location`, etc.|
|`is_shown`|Trigger block - when element is visible|
|`is_valid`|Trigger block - when element can be clicked|
|`effect`|Effect block - what happens on click|
|`saved_scopes`|List of scope names to make available in triggers/effects|
|`notification_key`|Notification key when activated|
|`confirm_title`|Localization for confirmation dialog title|
|`confirm_text`|Localization for confirmation dialog text|
|`ai_is_valid`|Whether AI can use this SGUI|
|`ai_chance`|AI probability of using (1-100)|
|`ai_frequency`|Months between AI checks|

## Scope types

- `country` - Country scope
- `character` - Character scope
- `location` - Province/location scope
- `war` - War scope
- `army` - Army scope
- `navy` - Navy scope
- `international_organization` - Organization scope

## Connecting to GUI

Scripted GUIs are referenced in GUI files using `scripted_gui`:

```
button = {
    using = default_button
    onclick = "[ScriptedGui.Execute(GuiScope.SetRoot(GetScriptedGui('my_scripted_gui')).End)]"
    visible = "[ScriptedGui.IsShown(GuiScope.SetRoot(GetScriptedGui('my_scripted_gui')).End)]"
    enabled = "[ScriptedGui.IsValid(GuiScope.SetRoot(GetScriptedGui('my_scripted_gui')).End)]"
}
```

## Saved scopes

Define scopes to use across is_shown, is_valid, and effect:

```
my_scripted_gui = {
    scope = country
    saved_scopes = { target_country target_character }

    is_valid = {
        scope:target_country = { is_at_war = no }
    }

    effect = {
        scope:target_character = {
            add_trait = rewarded
        }
    }
}
```

These additional scopes are then passed from the GUI definition file with AddScope :

```
onclick = "[GetScriptedGui('my_scripted_gui').Execute(GuiScope.SetRoot(Country.MakeScope).AddScope('target_country', ...).AddScope('target_character', ...).End)]"
```

## AI usage

AI chance uses mean time to happen syntax.

```
my_ai_scripted_gui = {
    scope = country

    is_shown = { always = yes }
    is_valid = { gold >= 100 }

    effect = {
        add_gold = -100
        add_prestige = 10
    }

    ai_is_valid = {
        gold >= 500    # AI needs more gold than minimum
    }

    ai_chance = {
        base = 5
        
        modifier = {
            add = 60
            trigger = {
                OR = {
                    NOT = { has_variable = tge_research }
                    var:tge_research < 0.3
                }
                monthly_income_trade_and_tax > 5
            }
        }
    }

    ai_frequency = 6 
}
```

## Example

```
my_custom_button = {
    scope = country

    is_shown = {
        has_variable = custom_feature_enabled
    }

    is_valid = {
        gold >= 50
        stability >= 0
        is_at_war = no
    }

    effect = {
        add_gold = -50
        add_stability = 0.5
        add_country_modifier = {
            modifier = custom_modifier
            years = 5
        }
    }

    saved_scopes = { }

    notification_key = custom_button_notification

    confirm_title = {
        first_valid = {
            triggered_desc = {
                desc = "CUSTOM_BUTTON_CONFIRM_TITLE"
            }
        }
    }

    confirm_text = {
        first_valid = {
            triggered_desc = {
                desc = "CUSTOM_BUTTON_CONFIRM_TEXT"
            }
        }
    }

    ai_is_valid = {
        gold >= 200
    }

    ai_chance = {
        base = 25
    }

    ai_frequency = 12
}
```

## GUI file integration

Create a matching GUI file in <mod>/gui/:

```
types MyCustomTypes {
    type my_custom_button_widget = widget {
        size = { 200 50 }

        button = {
            using = default_button
            size = { 100% 100% }

            text = "MY_BUTTON_TEXT"

            onclick = "[ScriptedGui.Execute(GuiScope.SetRoot(GetScriptedGui('my_custom_button')).End)]"
            visible = "[ScriptedGui.IsShown(GuiScope.SetRoot(GetScriptedGui('my_custom_button')).End)]"
            enabled = "[ScriptedGui.IsValid(GuiScope.SetRoot(GetScriptedGui('my_custom_button')).End)]"

            tooltip = "MY_BUTTON_TOOLTIP"
        }
    }
}
```

## Common patterns

### Toggle button

```
toggle_feature = {
    scope = country

    is_shown = { always = yes }

    is_valid = { always = yes }

    effect = {
        if = {
            limit = { has_variable = feature_enabled }
            remove_variable = feature_enabled
        }
        else = {
            set_variable = feature_enabled
        }
    }
}
```

### Cooldown button

```
cooldown_action = {
    scope = country

    is_shown = { always = yes }

    is_valid = {
        NOT = { has_variable = action_cooldown }
        gold >= 100
    }

    effect = {
        add_gold = -100
        set_variable = {
            name = action_cooldown
            years = 5
        }
    }
}
```

## References


