# Color

**Source:** https://eu5.paradoxwikis.com/Color

---

**Colors** are script features that allow for representation of colors in ingame script.

## Color modes

Just like real computer graphics, the game has more than one way to represent a color. In order to do that, the game uses color modes before a color definition. Below is a set of examples that represent each one.

### RGB

The most common and basic representation of a color in Europa Universalis V is RGB, represented via `rgb`:

```
map_example = rgb { 255 0 255 }
```

The first value in such a sequence represents the value of red on a scale from 0 to 255 included. Analogically, the second represents green and the third represents blue.

RGB values can also be scaled down and represented on a basis of scale from 0 to 1 - if all numbers are <= 1 the game will assume the color is in this scale:

```
map_example = rgb { 0.5 0 0.5 }
```

This is equivalent to `map_example = rgb { 127 0 127 }`.

Moreover, when the color mode is ommitted, the color definition is also treated as RGB - it is however recommended to always use the explicit form for collaboration projects.

### HSV

The other commonly used model for color values is HSV, represented via `hsv`:

```
map_example = hsv { 0.66 0.33 0.38 }
```

The first value represents hue in scale of 0 to 1, the second is saturation from scale of 0 to 1 and third is value on scale of 0 to 1.

### HSV360

`hsv360` is an alternative way of representing a HSV value:

```
map_example = hsv360 { 355 70 90 }
```

The first integer represents hue on scale of 0 to 360, the second is saturation on scale of 0 to 100 and the third one is value on scale of 0 to 100.

### HEX

The last way to represent a color is to represent an RGBA value in hexadecimal using `hex`. This format requires the alpha value to be provided but for most intents and purposes it can be represented as `ff`.

The following are therefore, equivalent:

```
map_example = hex { ff7f00ff }
map_example = rgb { 255 127 0 255 }
```

### Alpha values

`rgb`, `hsv` and `hsv360` values were previously shown as three number combinations but all of them also have a fourth, optional value - alpha - the degree of how transparent the color is. If those formats omit the fourth number, the alpha is set to maximum, making the color fully opaque. There is no known use for non-opaque colors in Europa Universalis V at the moment.

```
map_example = rgb { 0.5 0 0.5 0.5 }
map_example = hsv { 0.66 0.33 0.38 0.5 }
map_example = hsv360 { 355 70 90 50 } # the alpha channel is on scale from 0 to 1
```

## Colors as scopes

Technically, colors are also scopes and can be saved in variables, with the main way being done via country_color

```
set_variable = {
	name = example
	value = c:FRA.country_color
}
```

However, such calls do not recognize the color mode constructions ( rgb { } ), leading to severe syntax errors.

Moreover, few spots actually support color scopes, the notable being the value statements of Scripted math with colors.

## Named colors

Colors can be saved under certain keys in named colors folder. The keys of those named colors can then be inserted in the place of actual usage to allow for reuse.

All colors in `named_colors` need to be inserted inside `colors`.

Named colors only serve as color definitions. They cannot use scripted math logic for colors.

### Example

```
colors = {
	map_debug = rgb { 255 0 255 }
	map_arpitan = rgb { 235 196 231 }
	map_austrian = rgb { 220 220 220 }
	map_german = hsv360 { 180 10 50 }
	<...>
}
```

## Scripted math with colors

Some fields, mainly those utilizing colors for mapmodes, will allow the use of using scripted math for assigning colors:

```
map_color = {
	if = {
		limit = {
			owner ?= { 
				OR = {
					overlord ?= { is_member_of_international_organization = international_organization:foreign_league_france }
					is_member_of_international_organization = international_organization:foreign_league_france
				}
			}
		}
		value = map_french_league_leader
	}
	# Iberian League
	else_if = {
		limit = {
			owner ?= { 
				OR = {
					overlord ?= { is_member_of_international_organization = international_organization:foreign_league_iberia }
					is_member_of_international_organization = international_organization:foreign_league_iberia
				}
			}
		}
		value = map_iberian_league_leader
	}
}
```

Syntax wise, scripted color math is similar to script value math, except it does not allow for mathematical formulae. Here is a list of what is permitted, though:

|Name|Description|
|---|---|
|value|Sets the current value to the color on RHS|
|lerp|See lerp|
|if|See Conditionals on Script value|
|else_if|See Conditionals on Script value|
|else|See Conditionals on Script value|
|save_temporary_scope_as|See Script value page|
|save_temporary_value_as|See Script value page|

### Lerp

Lerp is a special operator that can be used in place of `value` for scripted color math - it calculates a color between two set colors using a Script value in `factor`. Lerp has 3 different modes based on arguments provided, with some allowing for additional control using `mid_point`.

When lerp is inserted, it will set the color value to the result of the internal math.

#### Min color, max color

Min color and max color mode is the most common mode for lerp, it calculates a color between color in `min_color` and `max_color` based on 0-1 value from `factor` script value.

```
lerp = {
	min_color = define:NMapColors|MAP_COLOR_LOW
	max_color = define:NMapColors|MAP_COLOR_HIGH
	factor = {
		value = location_works_of_art_star_rating
		divide = 5
	}
}
```

#### Min color, middle color, max color

Min color, middle color and max color is a mode that works similarly to min color, max color but also utilizes a color to be used in the middle point - `mid_color`. The middle point is, by default, 0.5, but can be specified using `mid_point` script value.

```
lerp = {
	min_color = map_red
	mid_color = map_yellow
	max_color = map_green
	factor = {
		value = location_works_of_art_star_rating
		divide = 5
	}
}
```

An example with `mid_point`:

```
lerp = {
	min_color = map_red
	mid_color = map_yellow
	mid_point = 0.25 # 0 - 0.25 will be colors going from red to yellow and 0.25-1 will be yellow going to green. This also means that rate of change is going to be faster in the first quarter than in last 3 quarters.
	max_color = map_green 
	factor = {
		value = location_works_of_art_star_rating
		divide = 5
	}
}
```

#### Min color, middle color, max color with valley points

By using `valley_start` and `valley_end` script values instead of `middle_point` we can define a range of values where the color will "sit" at the middle color point:

```
lerp = {
	min_color = map_red
	mid_color = map_yellow
	max_color = map_green 
	valley_start = 0.25	# 0 - 0.25 will be red turning to yellow
	# 0.25 - 0.75 will be yellow
	valley_start = 0.75
	# 0.75 - 1.00 will be yellow turning to green
	factor = {
		value = location_works_of_art_star_rating
		divide = 5
	}
}
```

#### Min color, low color, middle color, high color, max color

This five color mode allows for transition through through 5 different colors.

```
lerp = {
	min_color = map_red
	# from 0 to 0.25: red to yellow transition
	low_color = map_yellow
	# from 0.25 to 0.5: yellow to green
	mid_color = map_green 
	# from 0.5 to 0.75: green to blue
	high_color = map_blue
	# from 0.75 to 1.00: blue to red
	max_color = map_red 
	factor = {
		value = location_works_of_art_star_rating
		divide = 5
	}
}
```

There's also a variation with `mid_point` script value available, which will change the logic in the following:

```
lerp = {
	mid_point = 0.4

	min_color = map_red
	# from 0 to 0.2: red to yellow transition
	low_color = map_yellow
	# from 0.2 to 0.4: yellow to green
	mid_color = map_green 
	# from 0.4 to 0.7: green to blue
	high_color = map_blue
	# from 0.7 to 1.00: blue to red
	max_color = map_red 
	factor = {
		value = location_works_of_art_star_rating
		divide = 5
	}
}
```

## References


