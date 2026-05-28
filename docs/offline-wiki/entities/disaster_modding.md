# Disaster modding

**Source:** https://eu5.paradoxwikis.com/Disaster_modding

---

**Disasters** in Europa Universalis V represent internal situations and turmoil that may befall certain countries. They are represented via an alert and provide a unified interface for dealing with them.

## Disaster structure

```
example_disaster = {
	monthly_spawn_chance = 1

	can_start = {
		stability <= 25
		current_year >= 1400
	}

	modifier = {
		monthly_stability = -0.1
	}

	can_end = {
		OR = {
			current_year > 1500
			var:target_var >= 90
		}
	}

	on_start = {
		set_variable = {
			name = target_var
			value = 0
		}
	}

	on_monthly = {
		random_list = {
			11 = { }
			1 = {
				fire_example_disaster_event = yes
			}
		}
	}

	on_end = {
		remove_variable = target_var
	}
}
```

### Starting a disaster

In order for a disaster to start, the `can_start` field needs to be fulfilled and then every month, the game will have a chance equal to `monthly_spawn_chance` to activate the disaster. Once a disaster has naturally ended, it may not refire without being forcefully activated with a script effect or a console command. When a disaster fires, it executes the effect provided in `on_start`.

Both `can_start` and `on_start` fields are on `country` scope.

Moreover, if `fire_only_once = yes` is set, the disaster will be only able to fire once per country.

`monthly_spawn_chance` as a field accepts any value between 0-1 representing a monthly percentage chance for the disaster to begin. Moreover, it accepts a scripted value, so the chance can be made dynamic based on current game conditions:

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

### Disaster modifier

Disaster might be impact the nation with a modifier - those modifiers are set in `modifier` field.

### Executing monthly effects

`on_monthly` is an effect field that executes monthly. It is executed on the `country` scope, so it can be easily used to calculate variables and to fire events for the disaster.

### Ending a disaster

The disaster will end when the `can_end` trigger field is fulfilled. `can_end` is on the `country` scope, with `scope:disaster` provided with the `disaster type` scope.

When disaster ends, it will fire the `on_end` effect on the `country` scope.

### Mapmode selection

Unlike a situation, disasters do not have unique mapmodes. However, one can force a disaster panel to bring up an existing mapmode using `map_mode` which accepts a mapmode key on the right side.

### Disaster image

Besides manually being assigned icon based on usual icon rules, disasters should also have an image assigned to them using `image`. The right side is a path to the `.dds` illustration.

It can be fetched in GUI system using `GetDisasterIllustration( Arg0 )`, which takes a disaster. If there is no illustration assigned, it will use `"placeholder.dds"` from DISASTER_ILLUSTRATION_PATH define (Vanilla value: `"gfx/interface/illustrations/disaster"`)

### Graphical interface

In order to add a GUI for our disaster, we need to create a `.gui` file that is in the following folder and whose key corresponds to the disaster key:

/Europa Universalis V/game/in_game/gui/panels/disaster/<key>.gui

Within that file, we need to add a `disaster_panel` widget within which we will add our UI elements. Within the panel, `DisasterView` datacontext is available, allowing to fetch the Disaster for the currently viewed panel with `DisasterView.GetDisaster`.

### Creating events

One can have a disaster icon added at the top of an event window by using category = disaster in the event. The icon is pulled according to the namespace: the namespace must be the same as the disaster key.

### Creating hints

A scriptable_hint can be assigned to a disaster with `hint_tag` field. It will be visible in the alert and the user will be able to open with the hint by shift-pressing the alert.

## References


