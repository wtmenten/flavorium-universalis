# Mean time to happen

**Source:** https://eu5.paradoxwikis.com/Mean_time_to_happen

---

Mean time to happen notation represents a calculation syntax that is often used when calculating frequencies of events happening and weights in various cases.
Notable uses include `spread` in institutions, weight in events, weight in on_actions and weight in random_ iterator.

## Syntax

A mean time to happen field is usually comprised of the base value (usually defined using `base` or `factor`) and a set of modifiers that will modify it (much like formulae in script values).

### Example

Here is an example of mean time to happen in practice, used by a `weight` in a random_character iterator:

```
weight = {
	factor = 1						# Base value which will be modified by the modifiers
	modifier = {					# A modifier that will...
		factor = 10					# Multiply the current value by a factor of 10.
		trigger = {					# But only if the current scope (character) is in a cabinet.
			in_cabinet = yes
		}
	}
	modifier = {					# The value might be further modified by...
		factor = 5					# multiplication by 5
		trigger = {					# if the character is either a general, artist or an admiral.
			OR = {
				is_general = yes
				is_artist = yes
				is_admiral = yes
			}
		}
	}
}
```

### Setting the base value

The base value of a mean time to happen field can be set with several ways. The most common ways is by using `factor` and `base`, which are equivalent to each other. 

The basic value can also be set using `days`, `months` and `years`. The latter two are multiplied by 30 and 365 respectively to get the value equivalent to the number in `days` and other formats.

The following definitions are equivalent to each other:

```
weight = {
	factor = 10950		# (30 years in days)
}
weight = {
	base = 10950		# (30 years in days)
}
weight = {
	days = 10950		# (30 years in days)
}
weight = {
	months = 360		# (30 years in months)
}
weight = {
	years = 30		# (30 years)
}
```

Scripted values are NOT allowed in the base value definition.

If not defined, the base value is 1.

### Basic modifiers

The most common and universal modifier is the basic `modifier`, which accepts a trigger and may multiply/add by a certain value.

In order to have a `modifier` multiply a value, a `factor` must be provided. In order to add a value, `add` must be provided. Both values are scripted values - they utilize scripted math evaluated in the mean time to happen math.

```
weight = {
	factor = 1
	modifier = {
		add = 5			# adds 5 to the current value
	}
	modifier = {
		factor = 10 		# multiplies the current value by 10
	}
	modifier = {
		factor = {		# multiplies the current value by the result of this scripted math
			value = 2
			add = {
				value = prestige
				divide = 100
			}
			if = {
				limit = {
					is_great_power = yes
				}
				multiply = 2
			}
		}
	}
}
```

Because the base values do not accept script values but modifiers do, the simplest way to have a random iterator weight that is equal to a trigger value is the following:

```
weight = {
	factor = 1
	modifier = {
		multiply = prestige
	}
}
```

To make a `modifier` only apply conditionally, `trigger` can be used, but is not necessary. Any triggers placed inside the `modifier` will also be treated as triggers. Therefore the following two are equivalent:

```
modifier = {
	factor = 10

	is_general = yes
}

modifier = {
	factor = 10

	trigger = {
		is_general = yes
	}
}
```

### First valid

`first_valid` is a modifier node that contains basic `modifier`s inside and only utilizes the one whose trigger evaluates true first.

In the following example, if the target character is a ruler, the factor of 1 will be multiplied by a factor of 10. If the character is not a ruler, but is a general, it will be multiplied by a factor of 5. If the character is both a ruler and a general, the factor will only be multiplied by a factor of 10, as the first valid modifier node was hit and nothing is checked inside `first_valid` after that, and if character is neither a ruler nor a general, nothing will happen:

```
weight = {
	factor = 1
	first_valid = {
		modifier = {
			factor = 10

			is_ruler = yes
		}
		modifier = {
			factor = 5

			is_general = yes
		}
	}
}
```

### Compare modifiers

Compare modifiers are an alternative of doing math in modifiers compared to doing basic `modifier`s with scripted values.

Definition of a compare modifier looks like this:

```
compare_modifier = {
	target = global_var:hre_emperor
	value = total_abilities
	multiplier = 2
	offset = 100
	step = 5
	min = 100
	max = 600
}
```

`value` and `factor` are used to determine the basis for calculations. They are script values that are evaluated based on the current scope, or, if `target` is provided, the scope link inside determines evaluation in those. If `value` is provided, the compare modifier will add, while if `factor` is provided, it will multiply. Here is some examples:

```
compare_modifier = {
	target = global_var:hre_emperor
	value = total_abilities
}
```

This compare modifier will add total abilities of the character under global_var:hre_emperor to the weight calculation.

```
compare_modifier = {
	target = capital
	factor = development
}
```

This compare modifier will multiply the current math value by the development of this country's capital.

```
compare_modifier = {
	value = {
		value = prestige
		multiply = 2
	}
}
```

This compare modifier will add the double of this country's prestige.

`target` is ONLY used for evaluation of `value` and `factor`!

`offset` is a script value that is used to add the value inside to the currently evaluated value. Offset of 100 will add 100 to the math inside this compare modifier node. 

Analogically, `multiplier` as a script value will modify it by the value of the script value inside.

In practice, the mechanics of `offset` and `multiplier` can be represented inside the `value`/`factor` script value itself.

The `step` scripted value is used to round to the nearest multiple of the step value. For the following:

```
compare_modifier = {
	value = prestige
	step = 5
}
```

This compare modifier will add 0 prestige if prestige >= 0 and < 5, if prestige is >= 5 and < 10, and so forth.

Lastly, the results of the math in compare modifier can be clamped using `min` and `max` script values.

```
compare_modifier = {
	value = prestige
	min = 20
	max = 80
}
```

This compare modifier will add values between 20 and 80. If prestige is below 20, it will add 20, and if above 80, it will add 80.

Aspects of compare modifier are not formulas, they are not evaluated in order!

### Descs

Every modifier can be accompanied with a `desc` field which can be used to set a localizable string to be displayed in tooltips.

There is little use of this, as those are only visible in institution spread tooltips when `spread` is used.

### Macros

Mean time to happen can use macros much like effects and triggers field. More information about it can be found in scripted modifiers.

## Scripted modifiers

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


