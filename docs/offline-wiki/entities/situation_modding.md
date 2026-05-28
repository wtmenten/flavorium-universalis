# Situation modding

**Source:** https://eu5.paradoxwikis.com/Situation_modding

---

**Situations** in Europa Universalis V represent complex political, economic and societal phenomena. They are visible to a certain subset of countries, are represented via an alert, and provide an interface for various interactions.

## Technical details

Situation entries can hold variables and are a valid scope.

Though a situation may not be active at a time, any existing situation can be scoped to in script using the situation data scope link - one may therefore save variables on a situation before it is even active.

Situations get activated when their `can_start` field is fulfilled. They can also be forcefully started using activate_situation effect. Analogously, they end when their `can_end` trigger is fulfilled and can be forcefully ended with end_situation effect.

## Situation structure

```
example_situation = {
	monthly_spawn_chance = 1

	can_start = {
		country_exists = c:FRA
		current_year >= 1400
	}

	can_end = {
		OR = {
			current_year > 1500
			NOT = { country_exists = c:FRA }
		}
	}

	visible = {
		exists = c:FRA
		knows_country = c:FRA
	}

	on_start = {
		set_variable = {
			name = targetted_country
			value = c:FRA
		}
	}

	on_monthly = {
		var:targetted_country = {
			random_list = {
				11 = { }
				1 = {
					fire_example_situation_event = yes
				}
			}
		}
	}

	map_color = {
		if = {
			limit = {
				owner ?= c:FRA
			}
			value = map_FRA
		}
	}
}
```

### Starting a situation

In order for a situation to start, the `can_start` field needs to be fulfilled and then every month, the game will have a chance equal to `monthly_spawn_chance` to activate the situation. Once a situation has naturally ended, it may not refire without being forcefully activated with a script effect or a console command. When a situation fires, it executes the effect provided in `on_start`.

Both `can_start` and `on_start` fields are on situation scope, so variables checked/saved on them are based on the situation:

```
test_situation = {
	on_start = {
		set_variable = situation_has_fired #This variable will be saved on test_situation.
	}
}
```

`monthly_spawn_chance` as a field accepts any value between 0-1 representing a monthly percentage chance for the situation to begin. Moreover, it accepts a scripted value, so the chance can be made dynamic based on current game conditions:

```
monthly_spawn_chance = {
	value = 0
	if = {
		limit = {
			current_year >= 1338
		}
		value = 1
	}
}
```

### Situation visibility

`visible` is a trigger field that determines which countries can see the situation at a given time. If a country fulfills the conditions, it will get the alert and will be able to interact with the situation.

```
visible = {
	knows_country = c:ULM
}
```

### Executing monthly effects

`on_monthly` is an effect field that executes monthly. It is executed on the situation, so it can be easily used to calculate the internal variables as well as to affect every any country desired.
Example:

```
on_monthly = {
	every_country = {
		limit = {
			can_see_situation = root	# ROOT is the situation.
		}
		random_list = {
			11 = { }
			1 = {
				trigger_event_silently = test_situation_events.1
 			}
		}
	}
}
```

### Ending a situation

The situation will end when the `can_end` trigger field is fulfilled. `can_end` is on the situation scope.

Once the situation begins to end, it will execute `on_ending` effect field and `on_ended` effects. The first one is fired while the situation is still considered active. Both of those effects are on situation scope. If the situation has a lot of variables which will have no more use, it is recommended to use `on_ended` to remove them from the situation to reduce savefile size.

### Situation mapmode

Viewing a situation panel will bring up its own respective mapmode which can be customized in the situation script via `map_color`, `secondary_map_color` and `tooltip`. All 3 are evaluated in regards to the location, with `scope:target` provided as a scope to the situation.

`map_color` represents the main color on the map, `secondary_map_color` is used for whenever one wants to have striped color on a location. `tooltip` is used to fetch effects that will be shown when hovering over a location, usually custom_tooltips to display text!
Both `map_color` and `secondary_map_color` use scripted color syntax.

Additionally, situations accept `legend_key` fields which allow adding entries to a legend for colors on the mapmode.

Example:

```
map_color = {
	if = {
		limit = {
			owner ?= c:CAS
		}
		value = map_CAS	# Named Color from common/named_colors
	}
	# Game will automatically fallback to a “default” color.
}
secondary_map_color = {
	if = {
		limit = {
			exists = c:CAS
			owner ?= {
				is_allied_with = { who = c:CAS }
			}
		}
		value = rgb { 255 0 0 } # nations allied with Castile are striped red
	}
}
tooltip = {
	if = {
		limit = {
			owner ?= c:CAS
		}
		custom_tooltip = test_situation_cas_ownership
	}
	#change_development = 3 this can technically work and will not execute.
}

legend_key = {
	color = map_CAS 		# color for legend entry
	require_color_on_map = yes 	# no by default
	desc = cas_legend_key	# localizable string to be displayed in the entry
}

legend_key = { 			# second entry example
	color = rgb { 255 0 0 }	
	require_color_on_map = yes
	desc = cas_ally_key
}
```

Additionally, there is a `is_data_map` property, which, when set to yes, will use `situation_data` mapmode as the base instead of `situation`.

### Graphical interface

In order to add a GUI for our situation, we need to create a `.gui` file that is in the following folder and whose key corresponds to the situation key:

/Europa Universalis V/game/in_game/gui/panels/situation/<key>.gui

Within that file, we need to add a `situation_panel` widget within which we will add our UI elements. Within the panel, `SituationView` datacontext is available, allowing to fetch the Situation for the currently viewed panel with `SituationView.GetActiveSituation`.

### Creating events

One can have a situation icon added at the top of an event window by using category = situation in the event. The icon is pulled according to the namespace: the namespace must be the same as the situation key.

### Additional parameters

There are a few more fields used mainly for UI (SituationView):

- `international_organization_type` is a field that accepts an international organization key on the right. The IO must be unique.
- `resolution` must be a resolution key.
- `voters` represents the key of a global variable list for voting countries.

### Creating hints

A scriptable_hint can be assigned to a situation with `hint_tag` field. It will be visible in the alert and the user will be able to open with the hint by shift-pressing the alert.

## References


