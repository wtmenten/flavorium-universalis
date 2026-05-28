# Modifier modding

**Source:** https://eu5.paradoxwikis.com/Modifier_modding

---

**Modifier modding** involves techniques that allow for application of modifier types to countries and other entities. These modifiers then help to define what the nation can do and with what efficiency.

Modifiers is ubiquitous and many game objects can hold modifier types; this article focuses on two types of modifier blocks – static modifiers and auto modifiers.

## Static modifiers

Static modifiers are the backbone mechanism for adding dynamic modifiers during gameplay. They are easily added and removed via effects and provide utility in terms of AI and UI support.

### Technical details

Static modifiers are located in `common/static_modifiers`, usually in the `main_menu` top folder.

For example:

common/static_modifiers/example_file.txt

### Making modifiers

A basic static modifier is comprised of a set of modifiers and the values assigned to them:

```
my_modifier = {
	country_cabinet_efficiency = 0.1
	auto_conquer_at_war = yes
}
```

The values on the right side should match what the modifier type on the left expects, a number or a boolean. The value can also be a static scripted value; that is, it must evaluate to a number or boolean directly – it cannot be dynamically calculated. For example:

```
my_modifier = {
	modifier_type_1 = test_value_1   # 0.2 underneath
	modifier_type_2 = test_value_2   # will NOT work, a dynamic value is underneath.
}
```

With the following script value definitions:

```
test_value_1 = 0.2  		# will work
test_value_2 = { 		# will NOT work - no calculations on the fly
	value = 0.1
	multiply = war_exhaustion
}
```

Besides modifier types, a static modifier also accepts a `game_data` field.

### Game data

Game data contains two fields; the required `category` and the optional `decaying`.

`category` is used to determine the scope of the modifier. If it is set to `country`, then the modifier is applied on countries using `add_country_modifier`.
Here are the following available categories:

- `character`
- `country`
- `international_organization`
- `location`
- `mercenary`
- `province`
- `rebel`
- `religion`
- `unit`
`decaying` is an optional attribute which, when set to `yes`, reduces the effects of the modifiers based on remaining time in a linear fashion.
If a modifier is 50% towards its expiration, it has 50% of the strength.

Example:

```
test_modifier = {
	game_data = {
		decaying = yes
		category = country
	}
	...
}
```

### Applying and removing modifiers during the game

Modifiers can be applied during the course of the game by using `add_<type>_modifier = { }` effects, which all follow the same general syntax:

```
add_<type>_modifier = {
	mode = add_and_replace
	modifier = <key>
	years = 25
	# and others... See Add modifier parameters
}
```

Modifiers can be removed using `remove_<type>_modifier` effects, for instance remove_country_modifier.

Here is the full list of modifier effects:

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|add_character_modifier|add a modifier to a character|add_character_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|character||
|add_country_modifier|add a modifier to a country|add_country_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|country||
|add_international_organization_modifier|add a modifier to an international organization|add_international_organization_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|international_organization||
|add_location_modifier|add a modifier to a location|add_location_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|location||
|add_mercenary_modifier|add a modifier to a mercenary|add_mercenary_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|mercenary||
|add_movement_modifier|add a modifier to a movement|add_movement_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|movement||
|add_province_modifier|add a modifier to a unit|add_province_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|province||
|add_rebel_modifier|add a modifier to a rebel|add_rebel_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|rebels||
|add_religion_modifier|add a modifier to a unit|add_religion_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|religion||
|add_unit_modifier|add a modifier to a unit|add_unit_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }|unit||
|change_character_modifier_size|Change the strength of a modifier applied to the scope character|change_character_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|character||
|change_country_modifier_size|Change the strength of a modifier applied to the scope country|change_country_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|country||
|change_dynasty_modifier_size|Change the strength of a modifier applied to the scope dynasty|change_dynasty_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|dynasty||
|change_international_organization_modifier_size|Change the strength of a modifier applied to the scope international organization|change_international_organization_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|international_organization||
|change_location_modifier_size|Change the strength of a modifier applied to the scope location|change_location_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|location||
|change_mercenary_modifier_size|Change the strength of a modifier applied to the scope mercenary|change_mercenary_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|mercenary||
|change_province_modifier_size|Change the strength of a modifier applied to the scope province|change_province_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|province||
|change_rebel_modifier_size|Change the strength of a modifier applied to the scope rebel|change_rebel_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|rebels||
|change_religion_modifier_size|Change the strength of a modifier applied to the scope religion|change_religion_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|religion||
|change_unit_modifier_size|Change the strength of a modifier applied to the scope unit|change_unit_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|unit||

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|change_character_modifier_size|Change the strength of a modifier applied to the scope character|change_character_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|character||
|change_country_modifier_size|Change the strength of a modifier applied to the scope country|change_country_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|country||
|change_dynasty_modifier_size|Change the strength of a modifier applied to the scope dynasty|change_dynasty_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|dynasty||
|change_international_organization_modifier_size|Change the strength of a modifier applied to the scope international organization|change_international_organization_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|international_organization||
|change_location_modifier_size|Change the strength of a modifier applied to the scope location|change_location_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|location||
|change_mercenary_modifier_size|Change the strength of a modifier applied to the scope mercenary|change_mercenary_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|mercenary||
|change_province_modifier_size|Change the strength of a modifier applied to the scope province|change_province_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|province||
|change_rebel_modifier_size|Change the strength of a modifier applied to the scope rebel|change_rebel_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|rebels||
|change_religion_modifier_size|Change the strength of a modifier applied to the scope religion|change_religion_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|religion||
|change_unit_modifier_size|Change the strength of a modifier applied to the scope unit|change_unit_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }|unit||
|remove_character_modifier|Remove a modifier from a character|remove_character_modifier = name|character||
|remove_country_modifier|Remove a modifier from a country|remove_country_modifier = name|country||
|remove_international_organization_modifier|Remove a modifier from an international organization|remove_international_organization_modifier = name|international_organization||
|remove_location_modifier|Remove a modifier from a location|remove_location_modifier = name|location||
|remove_mercenary_modifier|Remove a modifier from a mercenary|remove_mercenary_modifier = name|mercenary||
|remove_movement_modifier|Remove a modifier from a movement|remove_movement_modifier = name|movement||
|remove_province_modifier|Remove a modifier from a province|remove_province_modifier = name|province||
|remove_rebel_modifier|Remove a modifier from a rebel|remove_rebel_modifier = name|rebels||
|remove_religion_modifier|Remove a modifier from a religion|remove_religion_modifier = name|religion||
|remove_unit_modifier|Remove a modifier from a unit|remove_unit_modifier = name|unit||

#### Add modifier parameters

The most important aspect of any modifier addition is the `modifier` which determines which modifier gets added. Modifier addition also needs to have a duration set by either `years`, `months`, `weeks` or `days`, which all accept scripted values evaluated based on the current scope and saved scopes.
If the duration evaluates to -1, the modifier will be permanent.

The `mode` is an important part of defining how the modifier addition will function, and accepts the following:

|Mode type|Behavior|
|---|---|
|**replace**|Removes the modifier and reapplies it for the whole duration provided.|
|**add**|Duration will not be changed and the modifiers will be added onto existing modifier.|
|**extend**|Duration of an existing modifier will be extended by the provided duration.|
|**add_and_extend**|Stacks the modifiers together and extends the length by the duration.|
|**set_to_largest**|If the modifier strength (`size`) is stronger than the current modifier applied, set it to new size.|
|**set_to_largest_and_extend**|If the modifier strength (`size`) is stronger than the current modifier applied, set it to new size. Additionally, extend the duration.|

The default is `extend`.

The strength of the modifier added can also be dynamically calculated using the `size` parameter, which accepts a script value, calculated similarly to how the duration value is calculated.

If one wishes to override the text that is shown in the modifier addition text, one may use `desc` to set a localizable description:

```
add_country_modifier = {
	modifier = $estate$_head_of_cabinet_influence
	days = -1
	mode = add_and_extend
	desc = head_of_cabinet_influence_desc
}
```

This results in text like "We gain <modifier> for <head_of_cabinet_influence_desc>"

Lastly, `recalculate_immediately = yes` can be used to force the game to recalculate all modifiers after the effect. This will make the game recognize new changes immediately.

### Applying modifiers in startup

Static modifiers can also be applied to various game objects during startup using `timed_modifiers`.

### Localisation

To localize a static modifier, `STATIC_MODIFIER_NAME_<key>` must be localized. `STATIC_MODIFIER_DESC_<key>` is also supported to represent the description, but can be left empty (set as "").

Defined modifiers can be retrieved for localization and GUI using `ShowModifier( 'modifier_name' )` and `ShowModifierWithNoTooltip( 'modifier_name' )`.

### Triggers

There are two types of triggers related to modifiers: one that allows for checking their presence, for instance has_country_modifier and its equivalents for other types.

The other, add_static_modifier_utility is a complex trigger that returns a numerical value representing the AI's perceived value of the adding the static modifier provided. It accepts `country`, `character` and `character` scopes:

```
value = "add_static_modifier_utility(joined_order_of_the_band)"
```

Additionally, a second numerical argument can be provided to indicate the size parameter of the modifier to be evaluated:

```
value = "add_static_modifier_utility(joined_order_of_the_band|0.5)"
```

remove_static_modifier_utility is opposite version of the above, utilizing the same syntax but calculating the value of removing the static modifier instead.

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|add_static_modifier_utility|Checks the AI utility of adding a static modifier to the scoped object|add_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|character, country, location|value|
|has_character_modifier|Does the scoped character have a given modifier|has_character_modifier = name|character||
|has_country_modifier|Does the scoped country have a given modifier|has_country_modifier = name|country||
|has_international_organization_modifier|Does the scoped international organization have a given modifier|has_international_organization_modifier = name|international_organization||
|has_location_modifier|Does the scoped province have a given modifier|has_location_modifier = name|location||
|has_mercenary_modifier|Does the scoped mercenary have a given modifier|has_mercenary_modifier = name|mercenary||
|has_province_modifier|Does the scoped province have a given modifier|has_province_modifier = name|province||
|has_religion_modifier|Does the scoped religion have a given modifier|has_religion_modifier = name|religion||
|has_unit_modifier|Does the scoped unit have a given modifier|has_unit_modifier = name|unit||
|remove_static_modifier_utility|Checks the AI utility of removing a static modifier from the scoped object|remove_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|character, country, location|value|

### Hardcoded static modifiers

Many static modifiers double as an hook into internal game modifiers and can therefore be used to modify hardcoded systems. Those modifiers are used by the code of the game and should not be removed:

|Static Modifier Name|Modifier Category|
|---|---|
|is_exiled|unit|
|army_leaderless|unit|
|navy_leaderless|unit|
|in_combat|unit|
|in_siege|unit|
|is_blockading|unit|
|is_army_levy|unit|
|is_army_mercenary|unit|
|is_army_regular|unit|
|is_navy_levy|unit|
|is_navy_mercenary|unit|
|is_navy_regular|unit|
|religious_unity|country|
|country_coastal_population|country|
|army_experience|country|
|navy_experience|country|
|average_literacy|country|
|army_maintenance_mod|country|
|army_maintenance_reverse_mod|country|
|navy_maintenance_mod|country|
|navy_maintenance_reverse_mod|country|
|fort_maintenance_reverse_mod|country|
|fort_maintenance_mod|country|
|colonial_maintenance_mod|country|
|exploration_maintenance_mod|country|
|diplomatic_maintenance_mod|country|
|recovery_motivation|country|
|call_for_peace|country|
|unsupported_cultures|country|
|annexing_countries|country|
|spy_networks|country|
|is_bankrupt|country|
|is_subject|country|
|is_great_power|country|
|num_hegemonies|country|
|num_embraced_institutions|country|
|power_relative_to_overlord|country|
|country_art|country|
|num_of_market_centers_in_country|country|
|percent_liturgical_speakers_in_country|country|
|liturgical_language_power|country|
|powerful_court_language|country|
|court_language_is_common|country|
|court_language_is_market_language|country|
|other_court_language|country|
|liturgical_language_is_court|country|
|invited_religious_figures|country|
|non_accepted_religious_figures|country|
|num_cardinals|country|
|total_cardinals_in_religion|country|
|saints_from_country|country|
|relation_improvements|country|
|current_army_size|country|
|current_navy_size|country|
|refused_favors|country|
|professed_trust|country|
|war_declared_on_us|country|
|total_occupied|country|
|total_blockaded|country|
|trade_vs_tax|country|
|wealth|country|
|parliament_in_session|country|
|parliament_not_called|country|
|parliament_in_capital|country|
|parliament_outside_capital|country|
|unsupported_diplomatic_capacity|country|
|average_development|country|
|average_control|country|
|religious_tolerance|country|
|religious_intolerance|country|
|dynasty_seat|location|
|location_base_values|location|
|is_occupied|location|
|devastation|location|
|prosperity|location|
|development|location|
|rgo_level|location|
|control|location|
|control_50|location|
|inverse_control|location|
|location_size_impact|location|
|location_closeness_to_equator_impact|location|
|has_ongoing_colonial_charter_migration|location|
|movement_cost|location|
|capital|location|
|province_capital|location|
|is_port|location|
|has_road|location|
|is_blockaded_by_enemies|location|
|is_blockaded_by_ice|location|
|proximity_to_capital|location|
|overpopulation|location|
|river_flowing_through|location|
|river_flowing_through_coast|location|
|coastal|location|
|total_population|location|
|looted|location|
|under_siege|location|
|location_art|location|
|expensive_food_in_location|location|
|cheap_food_in_location|location|
|raw_material_relative_price|location|
|harbor|location|
|surplus_jobs|location|
|location_imports|location|
|location_exports|location|
|location_template_natural_harbor_suitability_location|location|
|location_template_natural_harbor_suitability|location|
|location_template_natural_harbor_suitability_poor|location|
|location_template_natural_harbor_suitability_good|location|
|average_satisfaction_inverted|location|
|average_satisfaction|location|
|present_troops|location|
|hostile_troops|location|
|provincial_troops|location|
|market_center|location|
|building_levels|location|
|unsupported_building_levels|location|
|raised_levies|location|
|available_free_land|location|
|abundant_free_land|location|
|parliament_location|location|
|possible_promotion_percentage|location|
|tribals_expelled|location|
|heavy_rain_in_location|location|
|snow_storm_in_location|location|
|storm_surge_in_location|location|
|high_winds_in_location|location|
|sandstorm_in_location|location|
|tornado_in_location|location|
|character_base_values|character|
|is_explorer|character|
|head_of_the_cabinet_modifier|character|
|positive_province_food_growth|province|
|province_starving|province|
|province_base|province|
|integration_none|location|
|integration_conquered|location|
|integration_colonized|location|
|integration_integrated|location|
|integration_core|location|
|winter_none|location|
|winter_mild|location|
|winter_normal|location|
|winter_severe|location|
|general_adm|character|
|general_dip|character|
|general_mil|character|
|ruler_adm|character|
|ruler_dip|character|
|ruler_mil|character|
|admiral_adm|character|
|admiral_dip|character|
|admiral_mil|character|
|explorer_adm|character|
|explorer_dip|character|
|explorer_mil|character|
|difficulty_player_very_easy|country|
|difficulty_player_easy|country|
|difficulty_player_normal|country|
|difficulty_player_hard|country|
|difficulty_player_very_hard|country|
|difficulty_ai_very_easy|country|
|difficulty_ai_easy|country|
|difficulty_ai_normal|country|
|difficulty_ai_hard|country|
|difficulty_ai_very_hard|country|

## Auto modifiers

Auto modifiers are automatically applied to countries or international organizations when certain criteria are met and can be scaled at will. They need not be explicitly added to every country, as they are automatically applied if possible.

Because of this, they need to be used sparingly as they can have serious performance consequences if misused.

### Technical details

Auto modifiers are located in `common/auto_modifiers`, usually in the `in_game` top folder.

### Auto modifier example

Here is an example of an auto modifier:

```
war_exhaustion_impact = {
	scales_with = war_exhaustion

	land_morale_modifier = -0.02
	naval_morale_modifier = -0.02

	global_production_efficiency = scaled_production_efficiency_penalty
	trade_efficiency = scaled_trade_efficiency_penalty
	global_population_growth = -0.0003
}
```

### Auto modifier category and scope

By default, all auto modifiers are country modifiers based on country scope. The modifier category and scope type can be adjusted using `category` and `type` respectively:

```
auto_modifier_example = {
	type = international_organization
	category = international_organization
	...
}
```

Currently, the only other supported type is `international_organization`.

### Additional parameters

`requires_real = no` is used to apply the country auto modifier on "non-real" countries like the Pirate, Rebel or Mercenary tags.

`hide_effects = yes` can be used to make this modifier hidden.

### Triggers and scaling

To check whether an auto_modifier should appear, use `potential_trigger` and `limit`. Both conditions must evaluate to true for the auto_modifier to apply; it will be removed when either becomes false.

Based on empirical testing, the auto_modifier `limit` field only supports basic inequality checks (<, >, <=, >=) and is likely more efficient for evaluating these conditions. Some examples of what do not work within the limit field are `=`, `AND`, `OR`, and `NOT`. Thus, `limit = { legitimacy >= 50 }` will work correctly, while `limit = { NOT = { legitimacy > 50 } }` will not, with the result always defaulting to true. The `potential_trigger` does not have this limitation and can accept all standard triggers and comparisons.

The strength of the auto modifier is calculated dynamically using `scales_with` script value.

### Localisation and datacontext

Auto modifiers can be localized similarly to static modifiers under the following strings:

- `AUTO_MODIFIER_NAME_<key>` for the title
- `AUTO_MODIFIER_DESC_<key>` for the desc
Auto modifiers can also be used in datacontext with the following:

- `StaticAutoModifier` Type
- `ShowAutoModifierEffect( 'auto_modifier' )` Function
- `ShowAutoModifierEffectForCountry( 'auto_modifier' )` Function
- `ShowAutoModifierEffectForLocation( 'auto_modifier' )` Function

## New modifier types

Unlike in Europa Universalis IV modding, new modifier types can be added in `common/modifier_type_definitions`. They are best placed in the `main_menu` top folder.

Their values can then be used in multiple ways, but are most commonly referenced using `modifier:` datalink.

## References


