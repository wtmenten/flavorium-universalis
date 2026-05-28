# Disease modding

**Source:** https://eu5.paradoxwikis.com/Disease_modding

---

**Disease modding** is used to create new disease types and to customize their spread rate and the negative consequences. Diseases are a system extremely reliant on dynamically calculated script values.

## Spawning a disease

Diseases can be made to appear in a certain location using spawn_disease effect. Besides script enforced spawning, diseases may spontaneously appear using monthly chance with `monthly_spawn_chance` - a script value.

The spawn chance is checked once per month per each disease - if it spawns, it will fire the `spawn` effect - this is where the script system is supposed to add the disease presence to a random eligible location.

Both `monthly_spawn_chance` and `spawn` do not have a `ROOT`, but have been provided with `scope:disease` with the `disease` scope.

When a disease enters a country, it will fire `on_spread_to_country` effect, where `ROOT` is the country and `scope:disease` is the `disease` scope.

## Location modifier

When a disease impacts a location, it will add local modifiers set in `location_modifier` instances. Those are triggered modifiers - they accept a `potential_trigger` for when they can be used and a `scale` to scale the modifiers inside.
All of those are in `location` scope. This is further scaled by the disease's local impact modifier, e.g `local_typhus_impact_modifier` for disease of key `typhus`. It is also scaled by local disease impact, calculated as infection percentage divided by (1 + (Local disease resistance + local_disease_resistance + global_disease_resistance + (If applicable, rural_disease_resistance))

## R0 - basic reproduction rate

R0 is known as the basic reproduction rate and it is the most important value for disease spread. `r0` is a script value calculated on a location basis with `location` ROOT scope and `scope:disease` provided.

R0 is what will be used to decide the virality of the disease and how it spreads to neighboring locations, to units, from locations to units and so forth.

The disease is spread once every amount of days decided by the `calc_interval_days` script value with `scope:disease` provided as `disease` scope. The default value is 30.

## Mortality rate

Every day, infected pops may die from the disease. The share of pops who will "fight for their life" is decided by the `percentage_to_meet_their_fate_on_calc` script value, which has no `ROOT` scope, but it does have `scope:disease` provided.

`mortality_rate` is the rate at which pops die from this disease. It is a script value with no `ROOT` scope, but it does have `scope:disease` provided. This value is calculated once every day - but is disease wide.

However, mortality can still be impacted in another way - per each type of pop - using `specific_pop_type_effect` - each one of those can be made to have a disease affect different pop types with different severity:

```
specific_pop_type_effect = {
	pop_type = nobles		# Key of the pop type
	multiplier = 0.3		# How much % of this pop type should die compared to the baseline? 0.3 means 30% pops will die compared to the base value - a 70% decrease for nobles.
}
```

`pop_type` and `multiplier` are the only fields that are accepted - the former accepts a key of the pop type and the latter - a floating point number. If multiple are made for a pop type, only the first one will be used.

Pops that are chosen by the "meet their fate" calculation and are able to survive the mortality dice roll will become resistant to the disease.

### Character death

Characters may also die of the disease.

Every month, there is a chance a random character owned by a country ravaged by a disease may die of the disease. For this, the disease must be present in the nation's capital.
This chance of death is governed via `character_mortality_chance` script value whose `ROOT` is the location, with `scope:disease` provided as the disease, `scope:disease_outbreak` providing the disease_outbreak scope, and `scope:current_presence` pointing to local % infection presence.

This also means that character that are not physically in the capital (are leading an army elsewhere) - may die of the disease. Also, for clarification - only one character may die per month and the chance for any such death occuring is what the script value is deciding.

## Disease spread

Disease spread is governed via R0.

A disease might require a certain amount of presence in a location before it can move on - this behavior can be set using `location_infection_spread_threshold` script value, whose `ROOT` is the location, with `scope:disease` provided as the disease, `scope:disease_outbreak` providing the disease_outbreak scope, and `scope:current_presence` pointing to local % infection presence.

### Environmental infection

For environmental diseases like malaria, `environmental_infection` script value is used to infect local pops - for most of local inhabitants there will be resistance - but for any pops from outside, they will be affected.

Within the script value, `ROOT` is the location, with `scope:disease` provided as the disease, `scope:disease_outbreak` providing the disease_outbreak scope, and `scope:current_presence` pointing to local % infection presence.

## Stagnation

Diseases present in locations and subunits may eventually be marked as "stagnating" - a point at which the disease will stop spreading and will slowly dissapate.

Chances for those are governed via `location_stagnation_chance` and `sub_unit_stagnation_chance` script values respectively.

For the former, `ROOT` is the location, with `scope:disease` provided as the disease, `scope:disease_outbreak` providing the disease_outbreak scope, and `scope:current_presence` pointing to local % infection presence.

For the latter, `ROOT` is the subunit, with `scope:disease` provided as the disease, `scope:disease_outbreak` providing the disease_outbreak scope, and `scope:current_presence` pointing to % infection presence in the subunit.

## Resistance decay

Overtime, the resistance of pops tends to decrease. This is governed by `monthly_resistance_reduction` script value that has no `ROOT` but has `scope:disease` provided as the disease. The value of this script value will determine the global resistance decay across the world for this disease.

## Mapmode modding

In disease mapmode and when viewing a disease outbreak, colors for individual diseases are brought up. The colors here are decided using `map_color` attribute, which is a script value which represents the color. In this script value `ROOT` is on `location` with `scope:disease` provided as the disease. This color is only checked for locations which have diseases present - this color will not be evaluated outside of disease's reach. Moreover, if multiple diseases are present - the one with highest presence will be colored in (colors will not mix.).

This usually tends to be a lerp between two disease-specific colors based on the local presence.

Moreover, affected locations can also be given a secondary color (stripes) using `secondary_map_color`, a script value that works analogously - in base game - this is usually locations that are affected by the disease, checked via disease_affects_pops_here.

## Localisation

Every disease should have the following keys localized:

- `<key>` representing the name of the disease.
- `<key>_desc` representing the description of the disease.
- MODIFIER_TYPE_NAME_`local_<key>_impact_modifier` for local modifier title.
- MODIFIER_TYPE_DESC_`local_<key>_impact_modifier` for local modifier desc.

## Disease Setup

`disease_outbreak_manager` is used to add resistance to disease in certain areas, as well as to add outbreaks.

```
disease_outbreak_manager  = {
	add_disease_resistance = {
		type = bubonic_plague	# Disease whose resistance we are adding
		resistance = 0.1		# Resistance we are setting

		# List of areas, regions, subcontinents, continents, province_definitions, locations
		locations = {
			paris london 
		}
		provinces = {
			south_holland_province
			north_holland_province
		}
		areas = {
			north_portugal_area
			south_portugal_area
		}
		regions = {
			italy_region
		}
		sub_continents = {
			eastern_europe
		}
		continents = {
			asia
		}
	}

	add_disease_outbreak = {
		type = influenza		# Disease whose outbreak we are creating
		resistance = 0.1		# floating point representing the % resistance.
		infected = 0.1			# floating point representing the % infected.
		origin = 1000			# location id; internal? TODO: can we get key here.
		

		# List of areas, regions, subcontinents, continents, province_definitions, locations
		locations = {
			paris london 
		}
		provinces = {
			south_holland_province
			north_holland_province
		}
		areas = {
			north_portugal_area
			south_portugal_area
		}
		regions = {
			italy_region
		}
		sub_continents = {
			eastern_europe
		}
		continents = {
			asia
		}
	}
}
```

Contrary to what the name might imply, both of the effect actually set the values, so if you were to add your own resistance to a certain disease, the existing resistance will be replaced.

Additionally; the game seems to add +5% resistance on top of what is declared.

## References


