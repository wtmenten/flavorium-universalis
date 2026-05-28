# Macro

**Source:** https://eu5.paradoxwikis.com/Macro

---

**Macros** are blocks of script that can be reused. There are two main types of macros: **scripted effects** and **scripted triggers**. A macro is usually equivalent to copying the script from where it is defined to where it is used. They are useful for maintaining commonly used effects and triggers, as only one script block needs to be updated to update the effect or triggers across multiple uses.

## Scripted effects and triggers

Scripted effects and triggers are defined in their respective folders: /common/scripted_effects/ and /common/scripted_triggers/

A scripted effect or trigger is defined as a script name and a block of script, for example:

```
setup_colonial_nation = {
	change_government_type = government_type:republic
	add_gold = 100
	capital.province = { change_province_integration = integrated }
	add_reform = government_reform:colonial_subject
	every_owned_location = {
		change_control = control_radical_bonus
	}
	
	add_country_modifier = {
		modifier = new_colonial_nation_founded
		years = 50
		mode = add_and_extend
	}
}
```

This particular scripted effect is used for setting up colonial nations.

A scripted effect is a regular effect block and can use any effect scripting as required. Similarly, a scripted trigger is a regular trigger block and can use any trigger scripting as required. This includes the use of scripted effects and triggers within other scripted effects and triggers.

### Inline scripted effects and triggers

In event files, scripted effects and triggers can be defined for use in that file only. These should not have the same name as a "global" scripted effect or trigger. A name conflict raises an error.

### Localization

By default, using a scripted effect or trigger generates the same tooltip as if it were scripted in place.

This behavior can be overridden by adding a respective entry to `effect_localization` and `trigger_localization`. The entry must bear the same name as the scripted effect/trigger.

However, those entries can be lacking in scope access. Thus, it is often convenient to wrap the macro script in a `hidden_effect/hidden_trigger = { }`, `custom_tooltip = { }`, or `custom_description = { }` block. These script blocks function similarly, by hiding the auto-generated tooltip. The first, `hidden_effect/hidden_trigger = { }`, simply prevents any contained script from generating tooltips. The second, `custom_tooltip = { }`, prevents auto tooltips and instead displays a specified localization string. The last, `custom_description = { }`, also sets up a full effect or trigger localization set. It must be ensured that the `text` entry in the `custom_description` must be different as to avoid a conflict with the scripted_effect/trigger name.

### Arguments

Arguments or parameters can be inserted into scripted effects and triggers using $<arg>$. Here is a definition of such a scripted effect that defines a singular argument - `target`:

```
add_character_to_random_open_cabinet = {
	random_cabinet = {
		limit = {
			NOT = { 
				exists = cabinet_member
			}
		}
		add_to_cabinet = $target$
	}
}
```

When the scripted effect is used, it **must** be provided with all the arguments:

```
add_character_to_random_open_cabinet = {
	target = character:maj_gajah_mada
}
```

Note the usage of `$` in the scripted effect definition but not in the call.

Argument names can be anything and are case sensitive.

Arguments can also be inserted inside regular text:

```
add_currency_to_each_country = {
	add_$currency$ = $value$
}
```

then called with

```
add_currency_to_each_country = {
	currency = gold
	value = 15
}
```

These arguments work as literal text replacement, which is why `add_$currency$` can be used. There is no way to pass a value, so for example if an effect or trigger expects a raw integer, it cannot be given the value of a variable this way.

#### Metascripting

As scripted effects arguments are text that is copy-pasted, you can therefore insert whole script blocks into them:

```
metascripting_example = {
	every_owned_location = { 
		limit = {
			$limit$
		}
		change_development = 100
	}
}
```

This can be used for example as the following. Note that quote marks are necessary as the passed text contains white space, both spaces and line returns.

```
metascripting_example = {
	limit = "
		province_definition = root.capital.province_definition
	"
}
```

#### Recursion

Scripted effects and triggers can be called recursively but might require a bit of a workaround. There is a base game example for effects, which is implemented as

```
call_recursive_scripted_effect = {
	$effect$
}
```

Example:

```
test_effect = {
	every_neighbor_country = {
		limit = { NOT = { has_variable = is_neighbor_flag } }
		set_variable = is_neighbor_flag
		call_recursive_scripted_effect = {
			effect = "test_effect = yes"
		}
	}
}
```

## Other macros

Beside scripted effects and triggers, there are a few other macro or macro-like script elements.

### GUI function macros

GUI function macros are defined in /data_binding/ in any text file. There are no examples in base Europa Universalis 5 at this time. These macros can be used in GUI and localization functions. GUI macros can use parameterized arguments, where an argument can be passed through the macro to an actual GUI function.

For example:

```
macro = {
    description = "Add a loc key with a trailing newline if a condition is satisfied" #reminder of purpose/function
    definition = "MakeLineIf(Condition, LocKey)" #form of macro for use in interface and localization
    replace_with = "ConcatIfNeitherEmpty(AddLocalizationIf(Condition, LocKey), Localize( 'NEWLINE' ))" #result of macro
}
```

This macro can be called with `[MakeLineIf(boolean, loc key)]`. For example:

```
[MakeLineIf( Not(Country.CanColonize), 'NOT_ABLE_TO_COLONIZE')]
```

This is equivalent to and read by the game as:

```
[ConcatIfNeitherEmpty(AddLocalizationIf( Not(Country.CanColonize), 'NOT_ABLE_TO_COLONIZE'), Localize( 'NEWLINE' )]
```

### Scripted lists

Scripted lists are defined in /common/scripted_lists/. These are customized iterator lists with a built in trigger. They are defined as follows:

```
scripted_list_name = {
	base = base_game_list
	conditions = {
		<triggers>
	}
}
```

A base game list is the same as an iterator/list set without its prefixes. For example, the base game list `country` is used in `any_country`, `every_country`, `ordered_country`, and `random_country`.

Scripted lists filter the base list with given triggers and can be used as `any_<scripted_list_name>`, `every_<scripted_list_name>`, `ordered_<scripted_list_name>`, and `random_<scripted_list_name>`. For example, with a scripted list:

```
general = {
	base = character
	conditions = {
		is_general = yes
	}
}
```

The following example scripts would be equivalent:

```
every_character = {
	limit = {
		is_general = yes
	}
	add_mil = 5
}

every_general = {
    add_mil = 5
}
```

The latter iterator contains the same limit triggers as they are scripted in the list definition.

### Script values

Script values, defined in /common/script_values/, are similar to macros, particularly static script values. In particular, script values can be used in most places that expect a number or numerical value.

### @ values

@ values are intra-file macros. They must be defined in the file where they are used, and can be used in place of most number values.

### Scripted modifiers

Scripted modifiers are macros that can be defined in `common/scripted_modifiers`.

Here is an example of a scripted modifier definition:

```
gold_scaled_by_prestige_modifier = {
	modifier = {
		add = gold
	}
	modifier = {
		factor = {
			value = prestige
			divide = 100
		}
	}
}
```

This scripted modifier can then be used in a mean time to happen field by using `gold_scaled_by_prestige_modifier = yes`:

```
weight = {
	base = 0
	gold_scaled_by_prestige_modifier = yes
}
```

### Arguments

Scripted modifiers are very similar to scripted effects and triggers in that they can also use arguments that are copy pasted.

Here is an example of argumented scripted modifier and how it is used:

```
gold_scaled_by_currency_modifier = {
	modifier = {
		add = gold
	}
	modifier = {
		factor = {
			value = $currency$
			divide = 100
		}
	}
}
```

```
weight = {
	base = 0
	gold_scaled_by_currency_modifier = {
		currency = stability
	}
}
```

## References


