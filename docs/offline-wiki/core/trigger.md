# Trigger

**Source:** https://eu5.paradoxwikis.com/Trigger

---

**Triggers** are conditions that read the current game state – such as the ideology of a character, the ownership of a state, and much else – and determine whether an event can occur, an action is available, or if an effect can be done, among more.

Triggers come in two basic types, *inline* and *block*. Inline triggers take a simple target, such as a scope link, script value, or defined game object key. Block triggers are more complex and often take multiple targets, such as a scope link *and* a script value.

All triggers require a certain scope. Some triggers can be used in any scope (noted as "none" in the following tables), others only function when in the correct scope. Some triggers change the current scope.

The tables below are generated from the script documentation (*script_docs* console command).

## Comparison triggers

Comparisons are a common type of trigger, comparing two numerical values or game objects. Many triggers in the tables below are a comparison trigger (indicated with target `value`), but comparisons can also be made directly between values or objects using script values, variables, and scope links.

Comparisons use one of the comparison operators:

|Operator|Meaning|Inverted meaning|Use|
|---|---|---|---|
|`<`|(Strict) less than|Greater than or equals|Left side is strictly less than right side|
|`<=`|Less than or equals|(Strict) greater than|Left side is less than or equal to right side|
|`=`|(Strict) equals|Not equals|Left side is exactly equal to the right side (usable with non-numerical values)|
|`!=`|Not equals|(Strict) equals|Left side is not equal to the right side (usable with non-numerical values)|
|`>`|(Strict) greater than|Less than or equals|Left side if strictly greater than the right side|
|`>=`|Greater than or equals|(Strict) less than|Left side is greater than or equal to the right side.|

If a comparison is used inside a negative block (e.g. `NOT = { }`), it uses its inverted meaning.

Note that `=` is also used as the operator for non-comparison triggers, as well as effects and blocks. In these cases, the `=` represents an assignment or simple syntactic requirement rather than a comparison.

### Scope links as triggers

Scope links can be used as either the left or right side of a comparison trigger. For example, `army_size > c:FRA.army_size` returns true if the army size of the current scope is larger than the army size of France. For scope links that return a scope, only equality can be checked, while scope links that return a value can be used with inequality comparisons, too.

|Scope link|Description|From scope|
|---|---|---|
|array_define|Name\|Index. Index is 0-based.|none|
|bias_value|Unknown, add something in code registration|none|
|building_base_cost_in_gold|The Building base price in gold|building_type|
|compare_complex_value|A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies)|none|
|compare_value|A comparison trigger that will return its value in the context it is used eg: root.gold|none|
|default_price|The default price for a goods|none|
|define|Name|none|
|estate_power|The power of an estate|country|
|estate_satisfaction|The satisfaction of an estate|country|
|estate_target_satisfaction|The target satisfaction of an estate|country|
|estate_tax_base|The base tax of an estate|country, estate|
|estate_tax_percentage|The tax percentage levied on an estate|country|
|institution_progress|The progress towards an institution of a location|location|
|known_in_country|The amount of goods known to a speficic Country|country|
|market_price|The price a goods has in a market|market|
|max_great_powers|Unknown, add something in code registration|none|
|modifier|Scope to the value of the modifier type of specified key belonging to the current object|character, country, dynasty, international_organization, location, province, religion, unit|
|named_script_value|A script value that will calculate and returns its value in the context it is used|none|
|num_estate_privileges|The amount of privileges an estate has|country|
|num_location_rank|Count the amount of owned locations of a specific rank|country|
|num_pop_type|The amount of pops of a specific type at location|location|
|num_pop_type_in_country|The amount of pops of a specific type in a country|country|
|num_pop_type_in_province|The amount of pops of a specific type at Province|province|
|num_possible_estate_privileges|The amount of possible privileges an estate can get|country|
|percentage_pop_type_in_country|The percentage of pops of a specific type in a country|country|
|percentage_pop_type_in_location|The percentage of pops of a specific type in a location|location|
|produced_in_country|The amount of goods produced in a specific Country|country|
|produced_in_market|The amount of goods produced in a speficic market|market|
|produced_in_world|The amount of goods produced in the world|none|
|societal_value|The value of a societal value of a country|country|
|stockpile_in_market|The amount of goods stockpiled in a specific market|market|
|sub_unit_count|Checks the amount of a subunit-type inside a unit (in regiments)|unit|
|sub_unit_fraction|Checks the fraction of a subunit-type inside a unit (in regiments)|unit|
|sub_unit_strength|Checks the strength of a subunit-type inside a unit (in regiments)|unit|
|target_price|The target price a goods has in a market|market|
|total_building_levels_including_construction|The amount of total building levels including construction in a speficic Country|country|
|total_effective_building_levels|The amount of total effective building levels in a speficic Country|country|
|total_sub_unit_category_in_unit|Checks the total strength of a subunit-category for a unit|unit|
|total_sub_unit_count|Checks the amount of a subunit-category that a country has (in regiments/ships)|country|
|total_sub_unit_strength|Checks the total strength of a subunit-category for a unit|country|
|total_sub_unit_type_count|Checks the amount of a subunit-type that a country has (in regiments/ships)|country|
|total_sub_unit_type_strength|Checks the total strength of a subunit-type for a country|unit|
|traded_in_market|The amount of goods traded in a specific market|market|
|value|A numeric literal value eg: 1, 5.2, -6|none|

## Iterator triggers

Iterators examine all relevant scopes and output one or more. By default, iterators examine only one of the relevant scopes, but can be forced to examine more with the `count` or `percent` parameters

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|any_accepted_culture|Iterate through all accepted cultures in a country|any_accepted_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_active_disaster|Iterate through all active disasters for a country|any_active_disaster = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|disaster|
|any_active_estate|Iterate through all active estates (non-crown)|any_active_estate = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|estate_type|
|any_active_resolution|Iterate through all currently active resolutions in an international organization or situation|any_active_resolution = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization, situation|active_resolution|
|any_adjacent_ports_to_area|Iterate through all adjacent ports of an seazone area|any_adjacent_ports_to_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|location|
|any_advance_definition|Iterate through all advance definitions|any_advance_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|advance_type|
|any_allowed_estate_in_heir_selection|Iterate through all allowed estates a HeirSelection has|any_allowed_estate_in_heir_selection = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|heir_selection|estate_type|
|any_ancestor|Iterate through all ancestors (parents, grandparents etc) of a character|any_ancestor = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_area|Iterate through all existing areas|any_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|area|
|any_area_in_region|Iterate through all areas in a region|any_area_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|area|
|any_area_in_scripted_geography|Iterate through all areas in a scripted geography|any_area_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|area|
|any_area_with_core|Iterate through all areas with cored locations in a country|any_area_with_core = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|area|
|any_area_with_owned_province|Iterate through all areas with owned provinces in a country|any_area_with_owned_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|area|
|any_army|Iterate through all armies in a country|any_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|unit|
|any_artist|Iterate through all artists in a country|any_artist = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_attacker|Iterate through all attackers of a war|any_attacker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|war|country|
|any_avatar_for_god|Iterate through all Avatars of a God|any_avatar_for_god = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|god|avatar|
|any_besieging_units|Iterate through all units participating in a siege|any_besieging_units = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|siege|unit|
|any_border_location|Iterate through all owned location in a country which border locations not owned by the current country scope.|any_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_buildable_building_type|Iterate through all the building types a country can build|any_buildable_building_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|building_type|
|any_building_type|Iterate through all the building types|any_building_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|building_type|
|any_buildings_in_location|Iterate through all buildings in a location|any_buildings_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|building|
|any_cabinet|Iterate through all actions in a country's cabinet|any_cabinet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|cabinet|
|any_cabinet_action|Iterate through all actions in a country's cabinet actions|any_cabinet_action = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|cabinet_action|
|any_cabinet_character|Iterate through all characters in a country that is in the cabinet|any_cabinet_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_cardinal_in_country|Iterate through all Cardinals in a country|any_cardinal_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|cardinal|
|any_cardinal_in_religion|Iterate through all Cardinals in a Religion|any_cardinal_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|cardinal|
|any_casus_belli_on_us|Iterate through all countries have a casus belli on us|any_casus_belli_on_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_casus_belli_target|Iterate through all countries we have a casus belli on|any_casus_belli_target = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_center|Iterate through all subunits on the center of a combat-side|any_center = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_character|Iterate through all characters in a country|any_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_character_in_dynasty|Iterate through all living characters in a Dynasty|any_character_in_dynasty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|dynasty|character|
|any_character_supporting_rebel|Iterate through all characters supporting a rebel|any_character_supporting_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|rebels|character|
|any_child|Iterate through all children of a character|any_child = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_close_relative|Iterate through all close relatives of a character|any_close_relative = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_coast_border_location|Iterate through all bordering, or across one seazone of a location|any_coast_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_colonial_charter|Iterate through all colonial charters in a country|any_colonial_charter = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|colonial_charter|
|any_colonial_claim_province_definition|Iterate through all province definitions with colonial claims from the scope country.|any_colonial_claim_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|province_definition|
|any_colonial_country|Iterate through all colonial countries in the world|any_colonial_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_colonial_overlord|Iterate through all colonial overlord countries in the world|any_colonial_overlord = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_colonial_top_overlord|Iterate through all countries in the world that have a colonial country among their subjects or their subjects subjects and so on|any_colonial_top_overlord = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_connected_location|Iterate through all locations in the same country as the scope location that are connected by land or strait|any_connected_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_construction_material_for_building_type|Iterate through all goods required to construct a building type|any_construction_material_for_building_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|building_type|goods|
|any_continent|Iterate through all existing continents|any_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|continent|
|any_continent_in_scripted_geography|Iterate through all continents in a scripted geography|any_continent_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|continent|
|any_controlled_location|Iterate through all controlled location in a country|any_controlled_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_core_in_location|Iterate through all cores in a location|any_core_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|country|
|any_core_location|Iterate through all core locations in a country|any_core_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_country|Iterate through all existing countries|any_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_country_annexing_us|Iterate through all countries which are currently annexing the current country scope.|any_country_annexing_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_at_war_with|Iterate through all countries at war with|any_country_at_war_with = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_in_culture|Iterate through all countries with this primary culture|any_country_in_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture|country|
|any_country_in_culture_group|Iterate through all countries in a culture group.|any_country_in_culture_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture_group|country|
|any_country_in_diplomatic_range|Iterate through all countries in diplomatic range|any_country_in_diplomatic_range = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_in_dynasty|Iterate through all countries in a Dynasty|any_country_in_dynasty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|dynasty|country|
|any_country_in_hierarchy|Iterate through every country in the entire overlord/subject hierarchy, from the independent top overlord to the deepest subjects|any_country_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_in_religion|Iterate through all countries in a religion|any_country_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|country|
|any_country_in_religion_group|Iterate through all countries in a religion group.|any_country_in_religion_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|group|country|
|any_country_in_religious_school|Iterate through all countries within a school|any_country_in_religious_school = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religious_school|country|
|any_country_lent_to|Iterate through all countries a country has lent to|any_country_lent_to = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_of_country_type|Iterate through all countries of the specified type.|any_country_of_country_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_country_sub_unit|Iterate through all subunits in all units in a country|any_country_sub_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|sub_unit|
|any_country_supporting_rebel|Iterate through all countries supporting a rebel|any_country_supporting_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|rebels|country|
|any_country_that_can_be_called_defensively|Iterate through all countries that may be called into a defensive war.|any_country_that_can_be_called_defensively = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_that_can_be_called_offensively|Iterate through all countries that may be called into an offensive war.|any_country_that_can_be_called_offensively = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_together_in_war_with|Iterate through all countries which are an ally in any of the country scope's wars|any_country_together_in_war_with = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_we_are_annexing|Iterate through all countries which are currently annexed by the current country scope.|any_country_we_are_annexing = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_with_capital_in_geography|Iterate through all countries which have their capital in the specified geography|any_country_with_capital_in_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|any_country_with_cardinals|Iterate through all countries with cardinals in a religion|any_country_with_cardinals = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|country|
|any_country_with_coalition_grade_antagonism_against_us|Iterate through all countries who have coalition grade antagonism against us|any_country_with_coalition_grade_antagonism_against_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_with_relation_that_can_be_annulled|Iterate through all countries which have an annullable relation with the scope country.|any_country_with_relation_that_can_be_annulled = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_with_special_status_of_type|Iterate through all countries in the international organization which have the specified special status|any_country_with_special_status_of_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_country_with_succession_law|Iterate through all countries with a cached succession law (set cached = yes in the heir_selection to use this)|any_country_with_succession_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_culture|Iterate through all cultures|any_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|culture|
|any_culture_group|Iterate through all culture groups the culture is in.|any_culture_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture|culture_group|
|any_culture_in_culture_group|Iterate through all cultures in a culture group.|any_culture_in_culture_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture_group|culture|
|any_current_avatars|Iterate through all Avatars a country has|any_current_avatars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|avatar|
|any_current_gods|Iterate through all Gods a country worships|any_current_gods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|god|
|any_current_law|Iterate through all laws of a country.|any_current_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|law|
|any_current_law_in_international_organization|Iterate through all laws that are codified in the international organization|any_current_law_in_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|law|
|any_current_policy|Iterate through all policies that are codified in the country|any_current_policy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|policy|
|any_current_policy_in_international_organization|Iterate through all policies that are codified in the international organization|any_current_policy_in_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|policy|
|any_current_reforms|Iterate through all Government Reforms a country has|any_current_reforms = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|government_reform|
|any_current_war|Iterate through all wars of a country|any_current_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|war|
|any_defender|Iterate through all defenders of a war|any_defender = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|war|country|
|any_descendant|Iterate through all descendants (children, grandchildren etc) of a character|any_descendant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_disloyal_subject|Iterate through all loyal subject countries|any_disloyal_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_dynasty|Iterate through all dynasties in a country|any_dynasty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|dynasty|
|any_east_of_province_definition|Iterate through all province-definitions east of a province-definition|any_east_of_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province_definition|
|any_election_candidates|Iterate through all election candidates of a country with elections!|any_election_candidates = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_enemy|Iterate through all Enemy countries|any_enemy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_enemy_war_leader|Iterate through all countries which are leading a war against the scope|any_enemy_war_leader = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_estate|Iterate through all estates in a country|any_estate = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|estate|
|any_estate_privilege|Iterate through all current estate privileges of a Country|any_estate_privilege = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|estate_privilege|
|any_estate_type_preferring|Iterate through all estate types that a prefer a policy|any_estate_type_preferring = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|policy|estate_type|
|any_exploration_from_country|Iterate through all Explorations a country has|any_exploration_from_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|exploration|
|any_export|Iterate through all exports in a market|any_export = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|trade|
|any_export_from_location|Iterate through all exports from location|any_export_from_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_foreign_building_countries_in_location|Iterate through all foreign building countries in a location|any_foreign_building_countries_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|country|
|any_foreign_buildings_in_location|Iterate through all foreign buildings in a location|any_foreign_buildings_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|building|
|any_fort_in_country|Iterate through all Forts in a country|any_fort_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_friendly_coast_border_location|Iterate through all friendly bordering, or across one seazone of a location|any_friendly_coast_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_friendly_country|Iterate through all countries with relations marked as friendly|any_friendly_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_friendly_or_high_opinion_country|Iterate through all countries with relations marked as friendly or that we have a high opinion of set in defines|any_friendly_or_high_opinion_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_friendly_to_friendly_country|Iterate through all friends of our friends|any_friendly_to_friendly_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_friendly_to_hostile_country|Iterate through all friends of our enemies|any_friendly_to_hostile_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_god_in_religion|Iterate through all Gods in a Religion|any_god_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|god|
|any_good_in_demand|Iterate through all goods in a goods demand|any_good_in_demand = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|demand|goods|
|any_goods|Iterate through all types of goods|any_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|any_graphical_culture_in_culture|Iterate through all graphical culture in a culture|any_graphical_culture_in_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture|graphical_culture|
|any_great_power|Iterate through all great powers|any_great_power = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_heathen_location|Iterate through all heathen locations in a country|any_heathen_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_heretic_location|Iterate through all Heretic locations in a country|any_heretic_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_hired_mercenary|Iterate through mercenaries a country has hired|any_hired_mercenary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|mercenary|
|any_historical_enemy|Iterate through all historical Enemy countries|any_historical_enemy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_historical_rival|Iterate through all historical rival countries|any_historical_rival = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_holy_site_in_country|Iterate through all Holy Sites in a country|any_holy_site_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|holy_site|
|any_holy_site_in_religion|Iterate through all Holy Sites in a Religion|any_holy_site_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|holy_site|
|any_hostile_country|Iterate through all countries with relations marked as hostile|any_hostile_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_hostile_or_low_opinion_country|Iterate through all countries with relations marked as hostile or that we have a low opinion of set in defines|any_hostile_or_low_opinion_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_hostile_to_friendly_country|Iterate through all enemies of our friends|any_hostile_to_friendly_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_hostile_to_hostile_country|Iterate through all enemies of our enemies|any_hostile_to_hostile_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_import|Iterate through all imports in a market|any_import = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|trade|
|any_import_from_location|Iterate through all Imports from location|any_import_from_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_in_global_list|Iterate through all items in global list.|any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_list|Iterate through all items in list.|any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_local_list|Iterate through all items in local list.|any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_institutions_embraced|Iterate through all institutions a country has embraced|any_institutions_embraced = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|institution|
|any_international_organization|Iterate through all international organizations|any_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|international_organization|
|any_international_organization_elector|Iterate through all countries with an elector special status in the international organization|any_international_organization_elector = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_enemy|Iterate through all countries that are enemies of the international organization|any_international_organization_enemy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_member|Iterate through all countries that are members of the international organization|any_international_organization_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_owned_location|Iterate through all locations that are owned by the international organization|any_international_organization_owned_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|location|
|any_international_organization_owner|Iterate through all international organizations which own the location scope|any_international_organization_owner = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|international_organization|
|any_international_organization_parliament_opposers|Iterate through all countries that have voted AGAINST the parliament issue in the in the parliament of the international organization and support the current debate|any_international_organization_parliament_opposers = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_parliament_supporter|Iterate through all countries that have voted FOR the parliament issue in the parliament of the international organization and support the current debate|any_international_organization_parliament_supporter = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organizations_member_of|Iterate through all international organizations a country is a member of|any_international_organizations_member_of = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|international_organization|
|any_international_organizations_target_of|Iterate through all international organizations a country is a target of|any_international_organizations_target_of = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|international_organization|
|any_invited_religious_figure|Iterate through all invited religious figures in a Country|any_invited_religious_figure = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_key_in_global_variable_map|Iterate through all items in global variable map.|any_key_in_global_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_local_variable_map|Iterate through all items in local variable map.|any_key_in_local_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_variable_map|Iterate through all items in variable map.|any_key_in_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_known_country|Iterate through all known countries|any_known_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_known_institution|Iterate through all institutions a country knows of|any_known_institution = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|institution|
|any_left_flank|Iterate through all subunits on the left-flank of a combat-side|any_left_flank = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_lent_loan|Iterate through all loans that a country lent|any_lent_loan = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|loan|
|any_loan|Iterate through all loans in a country|any_loan = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|loan|
|any_loan_lent_to_country|Iterate through all loans a country has lent to the supplied borrower country|any_loan_lent_to_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|loan|
|any_location_in_area|Iterate through all Locations in a area|any_location_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|location|
|any_location_in_continent|Iterate through all Locations in a continent|any_location_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|continent|location|
|any_location_in_market|Iterate through all locations in a market|any_location_in_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|location|
|any_location_in_province|Iterate through all Locations in a province|any_location_in_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province|location|
|any_location_in_province_definition|Iterate through all Locations in a province definition|any_location_in_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|location|
|any_location_in_region|Iterate through all Locations in a region|any_location_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|location|
|any_location_in_scripted_geography|Iterate through all Locations in a scripted geography|any_location_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|location|
|any_location_in_sub_continent|Iterate through all Locations in a sub-continent|any_location_in_sub_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|sub_continent|location|
|any_location_in_the_world|Iterate through all location|any_location_in_the_world = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|location|
|any_loyal_subject|Iterate through all loyal subject countries|any_loyal_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_maritime_area|Iterate through all maritime areas for a country|any_maritime_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|area|
|any_market_center_in_country|Iterate through all markets in a country which market centers are owned by the country|any_market_center_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|market|
|any_market_in_world|Iterate through all markets in the world|any_market_in_world = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|market|
|any_market_present_in_country|Iterate through all markets in a country|any_market_present_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|market|
|any_market_with_merchants|Iterate through all markets a country has active merchants|any_market_with_merchants = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|market|
|any_mercenary|Iterate through all mercenaries in the world|any_mercenary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|mercenary|
|any_mercenary_sub_unit|Iterate through all subunits in a Mercenary|any_mercenary_sub_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|mercenary|sub_unit|
|any_merchant_in_market|Iterate through all merchants in a market|any_merchant_in_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|country|
|any_navy|Iterate through all navies in a country|any_navy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|unit|
|any_neighbor_area|Iterate through all neighboring areas in a area|any_neighbor_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|area|
|any_neighbor_country|Iterate through all neighbour countries|any_neighbor_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_neighbor_location|Iterate through all neighbors of a location|any_neighbor_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_neighbor_province_definition|Iterate through all neighboring ProvinceDefinitions in a ProvinceDefinition|any_neighbor_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province_definition|
|any_new_world_goods|Iterate through all new-world goods|any_new_world_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|any_nomad_countries_in_location|Iterate through all nomad pop countries in a location|any_nomad_countries_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|country|
|any_non_state_religion_location|Iterate through all NonStateReligion locations in a country|any_non_state_religion_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_old_world_goods|Iterate through all old-world goods|any_old_world_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|any_other_core_country|Iterate through all other countries which have a core on the current country|any_other_core_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_other_country|Iterate through all other countries|any_other_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_other_great_power|Iterate through all other great powers|any_other_great_power = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_other_religion_in_same_group|Iterate through all other religions that has the same group as Religion|any_other_religion_in_same_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|religion|
|any_other_revolutionary|Iterate through all other revolutionary countries|any_other_revolutionary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_overlord_or_above|Iterate through your overlord, your overlord's overlord, and so on|any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_ownable_location|Iterate through all ownable location|any_ownable_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|location|
|any_ownable_location_in_area|Iterate through all ownable Locations in an area|any_ownable_location_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|location|
|any_ownable_location_in_continent|Iterate through all ownable Locations in a continent|any_ownable_location_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|continent|location|
|any_ownable_location_in_province_definition|Iterate through all ownable Locations in a province definition|any_ownable_location_in_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|location|
|any_ownable_location_in_region|Iterate through all ownable Locations in a region|any_ownable_location_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|location|
|any_ownable_location_in_scripted_geography|Iterate through all ownable Locations in a scripted geography|any_ownable_location_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|location|
|any_ownable_location_in_sub_continent|Iterate through all ownable Locations in a sub continent|any_ownable_location_in_sub_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|sub_continent|location|
|any_owned_building|Iterate through all the owned buildings in a country|any_owned_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|building|
|any_owned_foreign_building|Iterate through all the owned foreign buildings in a country|any_owned_foreign_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|building|
|any_owned_foreign_building_location|Iterate through all the location of owned foreign buildings in a country|any_owned_foreign_building_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owned_foreign_building_region|Iterate through all the regions of owned foreign buildings in a country|any_owned_foreign_building_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|region|
|any_owned_location|Iterate through all owned location in a country|any_owned_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owned_nomad_pop|Iterate through all owned nomad pops in a country|any_owned_nomad_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|pop|
|any_owned_non_rural_location|Iterate through all owned non-rural locations in a country|any_owned_non_rural_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owned_rural_location|Iterate through all owned rural locations in a country|any_owned_rural_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owner_in_region|Iterate through all the countries that own locations in a region|any_owner_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|country|
|any_parent|Iterate through parents (order: father, mother) of a character.|any_parent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_participating_countries|Iterate through all Countrys participating in 1 side of a combat|any_participating_countries = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|country|
|any_participating_units|Iterate through all units participating in 1 side of a combat|any_participating_units = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|unit|
|any_past_liturgical_dialect|Iterate through all liturgical dialects a country has had before|any_past_liturgical_dialect = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_policy_in_law|Iterate through all policies that are part of the law scope|any_policy_in_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|law|policy|
|any_political_border_location|Iterate through all owned location in a country which border another country.|any_political_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_pop|Iterate through all pops in a location or country|any_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country, location|pop|
|any_pops_supporting_rebel|Iterate through all pops supporting a rebel|any_pops_supporting_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|rebels|pop|
|any_port_in_country|Iterate through all Ports in a country|any_port_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_possible_disaster|Iterate through all possible disasters for a country|any_possible_disaster = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|disaster|
|any_possible_parliament_issue|Iterate through all possible parliament issues in a country's or an international organization's parliament|any_possible_parliament_issue = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country, international_organization|parliament_issue|
|any_possible_policy|Iterate through all possible policies of a Country that is not currently implemeted|any_possible_policy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|policy|
|any_possible_privilege|Iterate through all possible & allowed estate privileges of a Country that is not currently implemeted|any_possible_privilege = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|estate|estate_privilege|
|any_possible_recruit_location|Iterate through all possible recruit locations in a country|any_possible_recruit_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_present_country|Iterate through all countries in the specified geography|any_present_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|any_present_culture_in_country|Iterate through all cultures present in the country.|any_present_culture_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_present_culture_in_location|Iterate through all cultures present in the location.|any_present_culture_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|culture|
|any_present_overlord|Iterate through all countries which have a subject in the specified geography|any_present_overlord = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|any_present_religion_in_country|Iterate through all religions present in the country.|any_present_religion_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|religion|
|any_present_religion_in_location|Iterate through all religions present in the location.|any_present_religion_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|religion|
|any_primary_or_accepted_culture|Iterate through primary culture and all accepted cultures in a country. Primary is ordered first.|any_primary_or_accepted_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_primary_or_accepted_or_tolerated_culture|Iterate through primary culture and all accepted and all tolerated cultures in a country. Primary is ordered first.|any_primary_or_accepted_or_tolerated_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_privateer|Iterate through all privateers in the world|any_privateer = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|privateer|
|any_privateer_from_country|Iterate through all privateers a country has|any_privateer_from_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|privateer|
|any_privateer_in_area|Iterate through all privateers in a area|any_privateer_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|privateer|
|any_production_method|Iterate through all types of production methods.|any_production_method = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|production_method|
|any_production_method_of_building|Iterate through all available production methods of the building.|any_production_method_of_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|building|production_method|
|any_province|Iterate through all provinces in a country|any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|province|
|any_province_definition|Iterate through all existing province_definition|any_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|province_definition|
|any_province_definition_in_area|Iterate through all province-definitions in an area|any_province_definition_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|province_definition|
|any_province_definition_in_scripted_geography|Iterate through all province-definitions in a scripted geography|any_province_definition_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|province_definition|
|any_province_in_area|Iterate through all provinces in an area|any_province_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|province|
|any_province_in_province_definition|Iterate through all provinces in a province-definition|any_province_in_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province|
|any_rebel|Iterate through all Rebels in a country|any_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|rebels|
|any_region|Iterate through all existing regions|any_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|region|
|any_region_in_continent|Iterate through all regions in a sub-continent|any_region_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|sub_continent|region|
|any_region_in_scripted_geography|Iterate through all regions in a scripted geography|any_region_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|region|
|any_related_country|Iterate through all related countries|any_related_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_religion|Iterate through all religions|any_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|religion|
|any_religion_for_god|Iterate through all Religions of a God|any_religion_for_god = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|god|religion|
|any_religion_in_religion_group|Iterate through all religions in a religion group.|any_religion_in_religion_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|group|religion|
|any_religion_international_organization|Iterate through all international organisations of a religion|any_religion_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|international_organization|
|any_religious_aspect|Iterate through all religious aspects of a Country|any_religious_aspect = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|religious_aspect|
|any_religious_focus|Iterate through all completed religious focuses of a Country|any_religious_focus = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|religious_focus|
|any_religious_school_in_religion|Iterate through all Religious Schools in a Religion|any_religious_school_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|religious_school|
|any_rented_out_mercenary|Iterate through mercenaries a country has rented out to the market|any_rented_out_mercenary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|mercenary|
|any_required_goods|Iterate through all goods required by the scope production method.|any_required_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|production_method|goods|
|any_reserves|Iterate through all subunits on the reserve of a combat-side|any_reserves = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_retreated|Iterate through all subunits on the retreated of a combat-side|any_retreated = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_revolutionary|Iterate through all revolutionary states|any_revolutionary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_right_flank|Iterate through all subunits on the right-flank of a combat-side|any_right_flank = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_rival|Iterate through all rival countries|any_rival = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_road_type|Iterate through all the road types|any_road_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|road_type|
|any_royal_marriage|Iterate through all royal married countries|any_royal_marriage = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_ruler|Iterate through all characters that have ever been rulers in a country, including the dead|any_ruler = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_ruling_countries|Iterate through countries a character rulers|any_ruling_countries = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|country|
|any_sound_toll_in_country|Iterate through all Sound Tolls in a country|any_sound_toll_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_spouse|Iterate through all spouses of a character|any_spouse = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_spy_network_built_in_us|Iterate through all countries building spy networks|any_spy_network_built_in_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_sub_continent|Iterate through all existing sub_continents|any_sub_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|sub_continent|
|any_sub_continent_in_continent|Iterate through all sub-continents in a continent|any_sub_continent_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|continent|sub_continent|
|any_sub_continent_in_scripted_geography|Iterate through all sub-continents in a scripted geography|any_sub_continent_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|sub_continent|
|any_sub_unit|Iterate through all subunits in a unit|any_sub_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|unit|sub_unit|
|any_subject|Iterate through all subject countries|any_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_subject_or_below|Iterate through all subject countries and their subject countries, and so on|any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_tolerated_culture|Iterate through all Tolerated cultures in a country|any_tolerated_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_trade|Iterate through all trades in a Country|any_trade = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|trade|
|any_union_partner|Iterate through all countries which are in a personal union with the current country scope.|any_union_partner = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_unit|Iterate through all units in a country|any_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|unit|
|any_unit_in_location|Iterate through all units in a location|any_unit_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|unit|
|any_valid_religion_for_aspect|Iterate through all religion that an aspect can be for|any_valid_religion_for_aspect = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religious_aspect|religion|
|any_voter|Iterate through all voters in an active resolution|any_voter = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|active_resolution|country|
|any_war|Iterate through all wars going on globally|any_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|war|
|any_war_participant|Iterate through all participants of a war|any_war_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|war|country|
|any_weather_system_in_location|Iterate through all weather systems in a location|any_weather_system_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|weather_system|
|any_west_of_province_definition|Iterate through all province-definitions west of a province-definition|any_west_of_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province_definition|
|any_work_of_art|Iterate through all WorkOfArts in the world|any_work_of_art = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|work_of_art|
|any_work_of_art_by_creator|Iterate through all work_of_art by a particular artist|any_work_of_art_by_creator = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|work_of_art|
|any_work_of_art_in_country|Iterate through all work_of_art in a country|any_work_of_art_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|work_of_art|
|any_work_of_art_in_location|Iterate through all work_of_art in a location|any_work_of_art_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|work_of_art|

## Flow triggers

Flow triggers control how other triggers are used. This includes conditionals and loops as well as tooltips. They can always be used in any scope

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|all_false|true if all children are false (equivalent to NOR)||none||
|and|all inside trigger must be true||none||
|any_false|true if any child is false (equivalent to NAND)||none||
|any_food_goods|Iterate through all food-goods|any_food_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|calc_true_if|Returns true if the specified number of sub-triggers return true|calc_true_if = { amount = 2 <trigger> <trigger> <trigger> }|none||
|custom_description|Wraps triggers that get a custom description instead of the auto-generated one|custom_description = { text = <trigger_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... triggers ... }|none||
|custom_tooltip|Replaces the tooltips for the enclosed triggers with a custom text|custom_tooltip = { text = <text> subject = <scope> (optional) <trigger> }|none||
|nand|a negated AND trigger||none||
|nor|a negated OR trigger||none||
|not|negates content of trigger||none||
|or|at least one entry inside trigger must be true||none||
|switch|Switch on a trigger for the evaluation of another trigger with an optional fallback trigger.|switch = { trigger = simple_assign_trigger case_1 = { <triggers> } case_2 = { <triggers> } case_n = { <triggers> } fallback = { <triggers> } }|none||
|trigger_else|Evaluates the display_triggers if the triggers of preceding 'trigger_if' or 'trigger_else_if' is not met|trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else = { <display_triggers> }|none||
|trigger_else_if|Evaluates the enclosed display_triggers if the triggers of the preceding `trigger_if` or `trigger_else_if` is not met and its own trigger of the limit is met|trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else_if = { limit = { <triggers> } <display_triggers> }|none||
|trigger_if|Evaluates the display_triggers if the triggers of the limit are met|trigger_if = { limit = { <triggers> } <display_triggers> }|none||
|weighted_calc_true_if|Returns true if the sum of weights of fulfilled sub-triggers amount to the specified sum|weighted_calc_true_if = { amount = 10 5 = { <trigger> } 15 = { <trigger> } 7 = { <trigger> } }|none||

## Variable triggers

Variable triggers check a variable. They can always be used in any scope, but may require a certain scope to read the correct variable.

|Trigger|Description|Example|Targets|
|---|---|---|---|
|any_in_global_list|Iterate through all items in global list.|any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list||
|any_in_list|Iterate through all items in list.|any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list||
|any_in_local_list|Iterate through all items in local list.|any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list||
|any_key_in_global_variable_map|Iterate through all items in global variable map.|any_key_in_global_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }||
|any_key_in_local_variable_map|Iterate through all items in local variable map.|any_key_in_local_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }||
|any_key_in_variable_map|Iterate through all items in variable map.|any_key_in_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }||
|global_variable_list_size|Checks the size of a global variable list|global_variable_list_size = { name = <variable_name value >= <script_value> }||
|global_variable_map_size|Checks the size of a global variable map|global_variable_map_size = { name = <variable_name value >= <script_value> }||
|has_global_variable|Checks whether the specified global variable is set|has_global_variable = name||
|has_global_variable_list|Checks whether the specified global variable list is set|has_global_variable_list = name||
|has_global_variable_map|Checks whether the specified global variable map is set|has_global_variable_map = name||
|has_local_variable|Checks whether the specified local variable is set|has_local_variable = name||
|has_local_variable_list|Checks whether the specified local variable list is set|has_local_variable_list = name||
|has_local_variable_map|Checks whether the specified local variable map is set|has_local_variable_map = name||
|has_variable|Checks whether the current scope has the specified variable set|has_variable = name||
|has_variable_list|Checks whether the current scope has the specified variable list set|has_variable_list = name||
|has_variable_map|Checks whether the current scope has the specified variable map set|has_variable_map = name||
|is_key_in_global_variable_map|Checks if a target is a key in a global variable map|is_key_in_global_variable_map = { name = <global_variable_map> target = <key to check> }||
|is_key_in_local_variable_map|Checks if a target is a key in a local variable map|is_key_in_local_variable_map = { name = <local_variable_map> target = <key to check> }||
|is_key_in_variable_map|Checks if a target is a key in a variable map|is_key_in_variable_map = { name = <variable_map> target = <key to check> }||
|is_target_in_global_variable_list|Checks if a target is in a global variable list|is_target_in_global_variable_list = { name = <variable_name> target = <event_target> }||
|is_target_in_local_variable_list|Checks if a target is in a local variable list|is_target_in_local_variable_list = { name = <variable_name> target = <event_target> }||
|is_target_in_variable_list|Checks if a target is in a variable list|is_target_in_variable_list = { name = <variable_name> target = <event_target> }||
|is_value_in_global_variable_map|Checks if a target is a value in a global variable map|is_value_in_global_variable_map = { name = <global_variable_map> target = <value to check> }||
|is_value_in_local_variable_map|Checks if a target is a value in a local variable map|is_value_in_local_variable_map = { name = <local_variable_map> target = <value to check> }||
|is_value_in_variable_map|Checks if a target is a value in a variable map|is_value_in_variable_map = { name = <variable_map> target = <value to check> }||
|local_variable_list_size|Checks the size of a local variable list|local_variable_list_size = { name = <variable_name> value >= <script_value> }||
|local_variable_map_size|Checks the size of a local variable map|local_variable_map_size = { name = <variable_name> value >= <script_value> }||
|variable_list_size|Checks the size of a variable list|variable_list_size = { name = <variable_name> value >= <script_value> }||
|variable_map_size|Checks the size of a variable map|variable_map_size = { name = <variable_name> value >= <script_value> }||

## Triggers by scope

The following tables list triggers by their required scope. Some triggers are repeated as they can be used in multiple scopes. All `any_` triggers are listed under Iterator triggers.

### None/any scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|add_to_temporary_list|Saves a temporary target for use during the trigger execution|This is used to build lists in triggers. If used within an any-trigger, placement within the trigger is quite important. The game will iterate through every instance of the any-trigger until it finds a single instance that fulfills the requirements, and then it will stop. In order to add every instance of a scope that fulfills certain conditions, use "count = all" while also placing this "effect" at the very end of the any-trigger (so that every condition is evaluated for every iteration).||
|ai_issue_voting_bias|gets the AI evaluation score for voting bias from the international organization||value|
|ai_will_do|gets the AI evaluation score of the supplied generic action ofr the supplied country||value|
|always|checks if the assigned yes/no value is true|always = yes # always succeeds always = no # always fails always = scope:a_boolean_value # evaluated at runtime|boolean|
|assert_if|Conditionally cause an assert during run time|assert_if = { limit = { <trigger> } text = <string> }||
|assert_read|Conditionally cause an assert during read time|assert_read = yes/<string>||
|can_add_relation|Can the country have the specified scripted relation with another country.|can_add_relation = { first = <country> second = <country> type = <relation type> }||
|can_start_tutorial_lesson|Can the specified tutorial lesson be started?|can_start_tutorial_lesson = reactive_advice_succession||
|country_exists|Does the country exist?||country|
|current_age|Checks if it is a certain age!|||
|current_date|Compare the current ingame date.||date|
|current_month|Compare the current ingame month (1..12)||value|
|current_tooltip_depth|What is the number of tooltips open right now?||value|
|current_year|Compare the current ingame year||value|
|debug_log|Log whether the parent trigger succeeded or failed|||
|debug_log_details|Log whether the parent trigger succeeded or failed. Log which children succeeded or failed|||
|debug_only|Checks if the game is in debug mode or not.||boolean|
|disease_is_active|Checks if a disease is active in the world.||disease|
|disease_outbreak_is_active|Checks if a disease outbreak is active in the world.||disease_outbreak|
|dynasty_exists|does a tag exist|||
|exists|Checks whether the specified scope target exists (check for not being the null object)|exists = from.owner.var:cool_var.mother||
|global_variable_list_size|Checks the size of a global variable list|global_variable_list_size = { name = <variable_name value >= <script_value> }||
|global_variable_map_size|Checks the size of a global variable map|global_variable_map_size = { name = <variable_name value >= <script_value> }||
|has_dlc|Does the host have this DLC|||
|has_fired_unique_event|Checks if the game has already fired the unique event|||
|has_game_rule|Is the given game rule setting enabled?|has_game_rule = faster_conversion||
|has_global_variable|Checks whether the specified global variable is set|has_global_variable = name||
|has_global_variable_list|Checks whether the specified global variable list is set|has_global_variable_list = name||
|has_global_variable_map|Checks whether the specified global variable map is set|has_global_variable_map = name||
|has_local_dlc|Does the host have this DLC|||
|has_local_variable|Checks whether the specified local variable is set|has_local_variable = name||
|has_local_variable_list|Checks whether the specified local variable list is set|has_local_variable_list = name||
|has_local_variable_map|Checks whether the specified local variable map is set|has_local_variable_map = name||
|has_multiple_players|Does the game have at least two players currently connected?||boolean|
|has_newsletter_subscription|Has the player subscribed to the newsletter?||boolean|
|has_variable|Checks whether the current scope has the specified variable set|has_variable = name||
|has_variable_list|Checks whether the current scope has the specified variable list set|has_variable_list = name||
|has_variable_map|Checks whether the current scope has the specified variable map set|has_variable_map = name||
|hidden_trigger|Enclosed triggers are not shown in tooltips|hidden_trigger = { <more triggers> }||
|international_organization_can_add_land|Can we add a location to the scope international organization?||international_organization|
|international_organization_can_remove_land|Can we remove a location from the scope international organization?||international_organization|
|ironman|Checks if the game is running in ironman.||boolean|
|is_alert_shown|Is the alert with the specified name shown?|||
|is_alert_triggered|Is the alert with the specified name triggered?|||
|is_camera_in_zoom_level|Is camera in a specified zoom level? SMALL / MEDIUM / LARGE|||
|is_gamestate_tutorial_active|Is the gamestate tutorial active? See save_progress_in_gamestate in tutorial_lesson_chains documentation.||boolean|
|is_in_list|Checks if a target in in a list|||
|is_key_in_global_variable_map|Checks if a target is a key in a global variable map|is_key_in_global_variable_map = { name = <global_variable_map> target = <key to check> }||
|is_key_in_local_variable_map|Checks if a target is a key in a local variable map|is_key_in_local_variable_map = { name = <local_variable_map> target = <key to check> }||
|is_key_in_variable_map|Checks if a target is a key in a variable map|is_key_in_variable_map = { name = <variable_map> target = <key to check> }||
|is_map_mode_active|Is map mode active?|||
|is_multiplayer_session|Is the current game session multiplayer?||boolean|
|is_set|Checks whether the specified scope target has been set (includes being the null object)|is_set = from.owner.var:cool_var.mother||
|is_situation_active|Checks if the target situation is currently active||situation|
|is_target_in_global_variable_list|Checks if a target is in a global variable list|is_target_in_global_variable_list = { name = <variable_name> target = <event_target> }||
|is_target_in_local_variable_list|Checks if a target is in a local variable list|is_target_in_local_variable_list = { name = <variable_name> target = <event_target> }||
|is_target_in_variable_list|Checks if a target is in a variable list|is_target_in_variable_list = { name = <variable_name> target = <event_target> }||
|is_tooltip_with_name_open|Is the tooltip with the specified name open?|||
|is_tutorial_active|Is the tutorial active?||boolean|
|is_tutorial_lesson_active|Is this the current tutorial lesson?|is_tutorial_lesson_active = reactive_advice_succession||
|is_tutorial_lesson_chain_completed|Has the tutorial lesson chain with the specified key been finished?|||
|is_tutorial_lesson_completed|has the tutorial lesson with the specified name been finished?|||
|is_tutorial_lesson_step_completed|Has the tutorial lesson step been finished?|is_tutorial_lesson_step_completed = lesson_key:step_key||
|is_value_in_global_variable_map|Checks if a target is a value in a global variable map|is_value_in_global_variable_map = { name = <global_variable_map> target = <value to check> }||
|is_value_in_local_variable_map|Checks if a target is a value in a local variable map|is_value_in_local_variable_map = { name = <local_variable_map> target = <value to check> }||
|is_value_in_variable_map|Checks if a target is a value in a variable map|is_value_in_variable_map = { name = <variable_map> target = <value to check> }||
|is_widgetid_open|Is the widget with the specified `widgetid` open (visible and not animating)? The fastest and safest way to check. (replaces old `is_widget_open` functionality, which operated on names.)|||
|list_size|Checks the size of a list|list_size = { name = <list_name> value >= <script_value> }|value|
|local_variable_list_size|Checks the size of a local variable list|local_variable_list_size = { name = <variable_name> value >= <script_value> }||
|local_variable_map_size|Checks the size of a local variable map|local_variable_map_size = { name = <variable_name> value >= <script_value> }||
|random_integer|Uniformly random integer between 0 and 2^31-1. It will be the same if evaluated on the same scope and day.||value|
|release_only|Checks if the game is in release mode or not.||boolean|
|save_temporary_scope_as|Saves a temporary target for use during the trigger execution|||
|save_temporary_scope_value_as|Saves a numerical or bool value as an arbitrarily-named temporary target to be referenced later in the same effect|save_temporary_scope_value_as = { name = <string> value = x }||
|scope_type|Checks the type of the scope object|||
|tag_exists|Does the country tag exist; does NOT accept scopes|tag_exists = FRA|tag|
|time_of_year|Check if the current date is within the bounds|time_of_year = { min = 11.1 # default: beginning of year max = 2.29 # default: end of year } Dates are formatted as "<month>.<day>" or just "<month>". The check includes the min and max dates. min can be larger than max, in this case we wrap around to the next year (i.e., February is between October and March).||
|unique_international_organization_type_exists|Does an international organization of this type exist?||international_organization_type|
|variable_list_size|Checks the size of a variable list|variable_list_size = { name = <variable_name> value >= <script_value> }||
|variable_map_size|Checks the size of a variable map|variable_map_size = { name = <variable_name> value >= <script_value> }||
|world_art_quality|Checks the total art quality in the world||value|
|world_culture_group_percentage|Gets the percentage of the population that follow a particular culture group in the world|world_culture_group_percentage = { culture_group = <culture_group> value <operator> <script_value> }|value|
|world_culture_group_population|Gets the absolute number of the population that follow a particular culture group in the world|world_culture_group_population = { culture_group = <culture_group> value <operator> <script_value> }|value|
|world_culture_percentage|Gets the percentage of the population that follow a particular culture in the world|world_culture_percentage = { culture = <culture> value <operator> <script_value> }|value|
|world_culture_population|Gets the absolute number of the population that follow a particular culture in the world|world_culture_population = { culture = <culture> value <operator> <script_value> }|value|
|world_religion_group_percentage|Gets the percentage of the population that follow a particular religion group in the world|world_religion_group_percentage = { religion_group = <religion_group> value <operator> <script_value> }|value|
|world_religion_group_population|Gets the absolute number of the population that follow a particular religion group in the world|world_religion_group_population = { religion_group = <religion_group> value <operator> <script_value> }|value|
|world_religion_percentage|Gets the percentage of the population that follow a particular religion in the world|world_religion_percentage = { religion = <religion> value <operator> <script_value> }|value|
|world_religion_population|Gets the absolute number of the population that follow a particular religion in the world|world_religion_population = { religion = <religion> value <operator> <script_value> }|value|

### Building scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|building_can_be_destroyed_by|Check if the target country scope is capable of destroying the current building scope||country|
|building_can_be_upgraded_by|Checks if a building can be upgraded by the target country||country|
|building_category|Checks if a building is linked to a certain category|||
|building_employed_amount|What's the current effective amount of employed workers?||value|
|building_employment_size_amount|What's the max workers amount?||value|
|building_goods_input|Check how much goods the scope building requires.||value|
|building_index|Checks building index (order in which it was built)||value|
|building_level|Check the level of this Building?||value|
|building_levels_under_construction|Check the level of this Building?||value|
|building_max_level|Gets the max level for a building||value|
|building_pop_type|Checks if a building is linked to a certain pop type|||
|building_potential_profit|Checks how much profit the building could make if at full worker capacity||value|
|building_produced_goods|Checks if a building produces a certain good||goods|
|building_profit|Checks building profit||value|
|has_tag|Check if that object has the specified tag.|||
|is_at_max_level|Checks if a building is working at full capacity||boolean|
|is_building_owned_by|Checks if a building is owned by a country||country|
|is_full_capacity|Checks if a building is working at full capacity||boolean|
|is_lacking_goods|Checks if a building is lacking goods||boolean|
|is_max_level|Checks if a building is at maximum level||boolean|
|is_not_profitable|Checks if a building is not profitable or not has prfot at all||boolean|
|is_opened|Checks if a building is opened||boolean|
|is_profitable|Checks if a building is profitable||boolean|
|is_special_building|Checks if a building is special||boolean|
|is_subsidized|Checks if a building is subsidized||boolean|

### Character scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|add_static_modifier_utility|Checks the AI utility of adding a static modifier to the scoped object|add_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|value|
|adm|The adm ability of the character||value|
|age_in_days|How old is a character???||value|
|age_in_years|How old is a character???||value|
|art_progress|The amount of progress an artist has made on a work of art||value|
|artist_skill|The artist skill of the character||value|
|artist_type|Checks if a character is a specific type of artist|||
|birth_age|What Age was the character born in? E.g. age_1_traditions||age|
|can_serve_in_cabinet_of|Checks if the character can serve in the cabinet of the target country||country|
|character_modifier_strength|Does the scoped character have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|character_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "character_modifier_strength(<modifier key>)"||
|character_nickname|Check if the character has the same name key as their nickname|||
|days_as_rebel|Check how many days the character has been a rebel.||value|
|days_of_service_as_admiral|Check how many days the character has served as an admiral.||value|
|days_of_service_as_general|Check how many days the character has served as a general.||value|
|days_of_service_in_cabinet|Check how many days the character has served in a cabinet.||value|
|dip|The dip ability of the character||value|
|education|Checks if a character has a specific education|||
|fertility|The fertility of the character||value|
|gfx_culture_applicable|Checks if a culture gfx applies to the scope object|||
|has_art_in_progress|Checks if an artist is currently working on something||boolean|
|has_available_marriage_slot|Has the character got a slot available for another marriage? (i.e. are they unmarried for non-polygamous people, or have they got less than the max number of spouses for polygamous people)||boolean|
|has_cabinet_action|is doing something in the cabinet||boolean|
|has_character_modifier|Does the scoped character have a given modifier|has_character_modifier = name||
|has_child_education|Does the scoped child have a given education|has_child_education = education||
|has_child_education_selected|Does the scoped child have any given education|has_child_education_selected = yes|boolean|
|has_dynasty|character is in a Dynasty||boolean|
|has_estate|Checks if a character is of a specific Estate||estate_type|
|has_exploration|character/country is currently exploring||boolean|
|has_exploration_construction|character is currently preparing to explore||boolean|
|has_nickname|Check if the character has any nick name set||boolean|
|has_trait|Checks if a character has a specified trait|||
|has_trait_category|Checks if any of the character's traits belongs to the specified category.|||
|has_unit|character is assigned to a unit||boolean|
|heir_position|Character's position in line for its country's throne||value|
|heir_score|Get the hypothetical heir score of the character for the target country, even if the character in question could not be an heir.||value|
|heir_score_home|Get the hypothetical heir score of the character in the country they currently reside in.||value|
|in_cabinet|character is in cabinet||boolean|
|is_admiral|character is an admiral||boolean|
|is_admiral_of|Character is admiral of the target country.||country|
|is_adolescent|character is Adolescent||boolean|
|is_adult|character is Adult||boolean|
|is_alive|character is alive||boolean|
|is_artist|character is Artist||boolean|
|is_artist_of|Character is artist of the target country.||country|
|is_child|character is Child||boolean|
|is_child_of|Is the character a child of the target character?||character|
|is_close_relative|Is the character a close relative (Child, Parent, Sibling/Half-sibling, Nephew/Niece, Aunt/Uncle, Grandparent or Grandchild) of the target character?||character|
|is_consort|character is Consort||boolean|
|is_consort_of|Character is consort of the target country.||country|
|is_courtier|Character is a courtier and has no roles assigned||boolean|
|is_dynastic_descendant_of|Is the character a dynastic descendant of the target dynasty?||dynasty|
|is_dynasty_head|character is DynastyHead||boolean|
|is_eligible_heir|Checks if the character can be an eligible heir for the specified country||country|
|is_eligible_heir_baseline|Checks if the character can be an eligible heir for the specified country without checking the heir selection law||country|
|is_eligible_military_leader|Checks if the character can be an eligible military leader for the specified country||country|
|is_explorer|character is an explorer||boolean|
|is_explorer_of|Character is explorer of the target country.||country|
|is_female|character is Female||boolean|
|is_general|character is a general||boolean|
|is_general_of|Character is general of the target country.||country|
|is_heir|character is Heir||boolean|
|is_heir_of|Character is heir of the target country.||country|
|is_immortal|character is immortal||boolean|
|is_infant|character is Infant||boolean|
|is_loyal|character is loyal to their ruler||boolean|
|is_married|character is Married||boolean|
|is_matrilineal_descendant_of|Is the character a dynastic descendant of the target dynasty via a matrilineal line??||dynasty|
|is_mercenary_leader|character is a mercenary leader||boolean|
|is_mercenary_of|Character is mercenary of the target country.||country|
|is_parent_of|Is the character a parent of the target character?||character|
|is_patrilineal_descendant_of|Is the character a dynastic descendant of the target dynasty via a patrilineal line??||dynasty|
|is_pregnant|character is Pregnant||boolean|
|is_regent|character is Regent||boolean|
|is_regent_of|Character is regent of the target country.||country|
|is_religious_figure|character is religious figure||boolean|
|is_ruler|character is Ruler||boolean|
|is_ruler_of|Character is ruler of the target country.||country|
|is_saint|Checks if a character is a saint in any religion||boolean|
|is_saint_of|Checks if a character is a saint in the specific religion||religion|
|is_same_gender|Is the character same gender as target character?||character|
|is_sibling_of|Is the character a sibling of the target character?||character|
|is_spouse_of|Is the character a spouse of the target character?||character|
|is_valid_for_exploration|character is valid for an exploration||boolean|
|mil|The mil ability of the character||value|
|modifier_utility|Checks the AI utility of a modifier||value|
|modifier_utility_include_locations|Checks the AI utility of a modifier with location checks||value|
|num_of_children|The number of children of the character||value|
|num_of_spouses|The number of spouses of the character||value|
|num_of_traits|The number of traits the character has||value|
|num_of_traits_of_category|The number of traits of a specified category the character has.|num_of_trait_by_category(<trait_category>) or num_of_trait_by_category = { type = <trait_category> value <comparator> <integer> }|value|
|religious_figure_type|Checks if a character is a specific type of religious figure|||
|remove_static_modifier_utility|Checks the AI utility of removing a static modifier from the scoped object|remove_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|value|
|ruled_country_on_or_after|Checks if the character ruled the country on or after a given date?|||
|total_abilities|The total ability of the character||value|
|valid_estate_for_heir_selection|Checks if the character's estate is allowed for the target heir selection||heir_selection|
|yearly_salary|The yearly salary of the character||value|
|years_as_rebel|Check how many years the character has been a rebel.||value|
|years_of_service_as_admiral|Check how many years the character has served as an admiral.||value|
|years_of_service_as_general|Check how many years the character has served as a general.||value|
|years_of_service_in_cabinet|Check how many years the character has served in a cabinet.||value|

### Country scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|active_religious_focus|Checks if a country is researching a certain religious focus|||
|add_estate_satisfaction_utility|Utility of adding however much estate satisfaction to the country|add_estate_satisfaction_utility(<estate>\|<amount>) or add_estate_satisfaction_utility = { type = <estate type> amount = <amount> value <operator><threshold> }|value|
|add_static_modifier_utility|Checks the AI utility of adding a static modifier to the scoped object|add_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|value|
|advance_no_longer_activated|Checks if a country has researched a certain advance but it's not useable at the moment because of conditions|||
|age_preference|checks a countries age preference for current age|||
|ai_unlock_unit_score|Returns the score for AI to unlock a unit||value|
|allows_female_rulers|country allows female rulers||boolean|
|allows_male_rulers|country allows male rulers||boolean|
|annexation_cost|How much does the target country cost for the current country to annex?|annexation_cost = { target = <target country> value = <script_value> } or annexation_cost(<target country>)|value|
|antagonism|is the country's antagonism towards the target greater or equal than the value?|antagonism = { target = X value <operator> Y or value = { min max } }|value|
|army_maintenance|What is the xx position (0-1) the country has?||value|
|army_size|Checks if a country has a certain army size||value|
|army_size_percentage|Checks if a country has a certain percentage of regiments compared to expected size||value|
|army_tradition|How much army tradition does the country/IO have?||value|
|army_tradition_percentage|How high the percentage of the current army tradition compared to the maximum does the country/IO have?||value|
|at_war|country is at war||boolean|
|average_control_in_home_region|Checks the average control in the home region||value|
|average_country_literacy|Checks if a country has a certain average_literacy||value|
|average_estate_satisfaction|How high is the average estate satisfaction in the country? The crown estate gets ignored here.||value|
|border_distance_to|gets distance between borders of two nations or a location and a nation.|border_distance_to = { country = x value [operator] y } or border_distance_to(country)|value|
|building_type_is_obsolete|Checks if the specified building type is obsolete for the scope country.||building_type|
|can_build_building|Checks if the location/country can build the specified building. Location only checks local requirements, country checks the country scope requirements.||building_type|
|can_build_unit_type|Checks if the country can build the specified unit type.||unit_type|
|can_build_units_of_category|Checks if the country can build units of the specified category.||sub_unit_category|
|can_create_casus_belli_of_type_on|Can the country see and create a cb of the supplied type on the target?|can_create_casus_belli_of_type_on = { type = <cb type key> target = <country> }||
|can_declare_no_cb_war_on|Can the country declare a war without any casus belli on the target country?||country|
|can_declare_war_on|Check if the current country could declare war on the target country||country|
|can_do_generic_action|Is the country capable of doing the specified generic action right now?|can_do_generic_action = { generic_action = <generic action> <parameters> }||
|can_find_trade_route|can the country find a trade route from market a to market b?|can_find_trade_route = { from = <market> to = <market> }||
|can_form|Checks if the country can form the specified formable country.||formable_country|
|can_join_defensive_war_with|Can the country join in a defensive war with the scope country?||country|
|can_join_international_organization|Can we join the supplied international organization?||international_organization|
|can_join_offensive_war_with|Can the country join in an offensive war with the scope country?||country|
|can_lead_international_organization|Can the country lead the specified international organization?||international_organization|
|can_leave_international_organization|Can we leave the supplied international organization?||international_organization|
|can_make_subject_of|Can the country in scope become a subject of the target country ? Same checks as the peace treaty become-subject.|can_make_subject_of = { target = <country> type = <subject_type> [ignore_war_limitation = yes] #use to ignore allowed_subjugation of the war }||
|can_pay_price|Can the country pay the specified price?||price|
|can_raise_army_levies|Checks if the country can raise army levies||boolean|
|can_raise_levies|Checks if the country can raise any kind of levies||boolean|
|can_raise_navy_levies|Checks if the country can raise navy levies||boolean|
|can_research_advance|Checks if a country can research but has not yet researched a specific advance.|||
|can_rival|Could the current country scope rival the target country ignoring slots and range?||country|
|can_see_religious_aspect|Checks if the input religious aspect is visible for the country in scope.||religious_aspect|
|can_see_situation|Checks if the 'visible' trigger of the target situation is fulfilled for the country scope.||situation|
|can_share_maps_with|Country can share maps with the supplied country?||country|
|can_use_agenda_bribe|Checks if estate type is allowed in parliament|||
|can_vote_in_parliament|Can the countrs scope vote in the target international organization?||international_organization|
|cancel_exploration_utility|Utility of an cancelling and exploration to the country|cancel_exploration_utility(<area>) or exploration_utility = { area = <area> value <operator><threshold> }|value|
|cb_creation_progress_against|Checks the progress of the casus belli creation against the target country in percentage.|cb_creation_progress_against = { target = <country scope> value = <script_value> } or cb_creation_progress_against(<country scope>)|value|
|climate_count|Returns the amount of owned locations with the specified climate.|climate_count = { type = <climate scope> value <operator> <value> } or "climtae_count(<climate scope>)"||
|climate_percent|Returns the percentage of owned locations with the specified climate.|climate_percent = { type = <climate scope> value <operator> <value> } or "climate_percent(<climate scope>)"||
|colonial_charter_progress|Progress of a colonial charter|colonial_charter_progress(<province definition>) or colonial_charter_progress = { province_definition = <province definition> value <operator><threshold> }|value|
|colonial_charter_utility|Utility of a colonial charter|colonial_charter_utility(<province definition>\|<source province>) or colonial_charter_utility = { province_definition = <province definition> source = <source province> value <operator><threshold> }|value|
|colonial_maintenance|What is the xx position (0-1) the country has?||value|
|colonial_range|The colonial range of the country||value|
|complacency|How much complacency does the country/IO have?||value|
|complacency_percentage|How high the percentage of the current complacency compared to the maximum does the country/IO have?||value|
|conquer_desire|Gets how much the AI wants to conquer the supplied country|conquer_desire(<target>) or conquer_desire = { target = <country link> value <operator> <amount> }|value|
|conquistador_utility|Utility of a conquistador|conquistador_utility(<area>) or conquistador_utility = { area = <area> value <operator><threshold> }|value|
|controls|Does the country control a specific location?||location|
|country_art_quality|Checks the total art quality in a Country||value|
|country_can_join_international_organization|Can we add a country to the supplied international organization?||international_organization|
|country_combined_special_status_power|Get the political power of the country within the target international organization with all of its special statuses combined.|country_combined_special_status_power = { international_organization = <IO> value <operator> <float> } or country_combined_special_status_power(<IO>)|value|
|country_combined_special_status_power_fraction|Get the political power fraction of the country within the target international organization with all of its special statuses combined.|country_combined_special_status_power = { international_organization = <IO> value <operator> <float> } or country_combined_special_status_power(<IO>)|value|
|country_economical_base|Checks the total economical base of a country||value|
|country_estate_loan_size|Checks the size of a loan given by the estates to a country||value|
|country_has_disease|Checks the presence of a disease in a country.|country_has_disease = <disease>|disease|
|country_has_disease_outbreak|Checks the presence of a disease outbreak in a country.|country_has_disease_outbreak = <disease>|disease_outbreak|
|country_has_estate|Checks if the country has the specific Estate||estate_type|
|country_highest_rated_special_status_power|Get the political power of the country within the target international organization of its highest prioritized special status.|highest_rated_special_status_power = { international_organization = <IO> value <operator> <float> } or highest_rated_special_status_power(<IO>)|value|
|country_interaction_acceptance|How high is the target country's AI value of accepting the country interaction done by the current country scope? Always return 0 if the target is a player|country_interaction_acceptance = { type = <country interaction> target = <country> value = <script_value> } or country_interaction_acceptance(<country interaction>\|<country>)|value|
|country_loan_capacity|Checks how much more money a country can borrow||value|
|country_modifier_strength|Does the scoped country have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|country_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "country_modifier_strength(<modifier key>)"||
|country_rank_level|level of the country rank of a country||value|
|country_rank_level_on_date|level of the country rank of a country on a particular date||value|
|country_strength|Strength of a country, including their troop numbers as well as tax base and manpower||value|
|country_tax_base|Checks the total tax base of a country||value|
|country_total_army_levy_size|Gets the total number of army levies available to the country||value|
|country_total_navy_levy_size|Gets the total number of navy levies available to the country||value|
|country_type|Checks what type a country is (location, pop, building, army, navy)|||
|court_maintenance|What is the xx position (0-1) the country has?||value|
|create_market_utility|Utility of creating a market|create_market_utility(<location>) or create_market_utility = { location = <location> value <operator><threshold> }|value|
|cultural_maintenance|What is the xx position (0-1) the country has?||value|
|cultural_unity|Checks the fraction of the population sharing the country's primary culture||value|
|culture_group_percentage_in_country|The percentage of a specific culture group in the current country||value|
|culture_group_population_in_country|The number of pops of a specific culture group in the current country||value|
|culture_percentage_in_country|The percentage of a specific culture in the current country||value|
|culture_population_in_country|The number of pops of a specific culture in the current country||value|
|currency_percentage_towards_limit|Gets currency progress towards specified limit||value|
|currency_utility|Utility of an amount of currency to the country|currency_utility(<currency>\|<amount>) or currency_utility = { currency = <currency> amount = <amount> }|value|
|current_mission_task|Checks if the country has the specified mission task in progress.||mission_task|
|current_ruler_term_years|Checks the current ruler term length in years.||value|
|defensive_alliance_strength|Strength of a defensive alliance, including the nation with all countries giving defensive support and those that can be called in for defensive wars||value|
|dependency_length_days|returns the number of days a country has been in a dependency (overlord/subject) relationship with the target country.|dependency_length_days = { target = <country> value <comparator> <script_value> }|value|
|destroy_market_utility|Utility of destroying a market|destroy_market_utility(<location>) or destroy_market_utility = { location = <location> value <operator><threshold> }|value|
|devotion|How much devotion does the country/IO have?||value|
|devotion_percentage|How high the percentage of the current devotion compared to the maximum does the country/IO have?||value|
|diplomatic_capacity_of_new_relation|Diplomatic capacity that will be used if the country obtains this diplomatic relation||value|
|diplomatic_capacity_without_maintenance|Diplomatic capacity that country would have without paying anything for maintenance||value|
|diplomatic_maintenance|What is the xx position (0-1) the country has?||value|
|diplomatic_range|Is the target country within diplomatic range?||value|
|discount_needed_for_law_change|Checks how much more discount % is needed for Ai to change a law||value|
|disease_country_deaths|Checks the number of deaths from a disease in a country.|disease_country_deaths(<disease>) disease_country_deaths = { target = <disease> value <comparator> <real> }|value|
|disease_outbreak_country_deaths|Checks the number of deaths from an outbreak in a country.|disease_outbreak_country_deaths(<disease_outbreak>) disease_outbreak_country_deaths = { disease_outbreak = <disease_outbreak> value <comparator> <real> }|value|
|does_estate_want_other_policy|Checks if a country has at least one law for which the input estate want another policy|||
|doom|How much doom does the country/IO have?||value|
|doom_percentage|How high the percentage of the current doom compared to the maximum does the country/IO have?||value|
|dynastic_power|Returns the dynastic power of the scope dynasty or country. For countries, check ruler dynasty or heir dynasty if in regency.|dynastic_power = { international_organization = <IO> value <operator> <script_value> } or dynastic_power(<IO>)|value|
|employment_system_desire|returns how much the country wants the target employment system.|employment_system_desire = { target = <employment system> value <comparator> <script_value> }|value|
|estate_loan_interest|Checks the interest of a loan||value|
|estate_max_tax|the current max-tax of an estate in a country|estate_max_tax(<estate_type link>) or estate_max_tax = { estate_type = <estate_type link> value <operator> <amount> }|value|
|estate_opinion|the current opinion that an estate in a country has of another country|estate_opinion(<estate_type link>\|<country>) or estate_opinion = { estate_type = <estate_type link> target = country value <operator> <amount> }|value|
|estate_satisfaction|the current satisfaction of an estate in a country|estate_satisfaction(<estate_type link>) or estate_satisfaction = { estate_type = <estate_type link> value <operator> <amount> }|value|
|estate_type_allowed_in_cabinet|Checks if estate type is allowed in cabinet|||
|estate_type_allowed_in_command|Checks if estate type is allowed in command of a unit|||
|estate_type_allowed_in_parliament|Checks if estate type is allowed in parliament|||
|expected_army_size|Checks if a country has a certain expected army size||value|
|expected_navy_size|Checks if a country expects to have a certain amount of ships||value|
|exploration_maintenance|What is the xx position (0-1) the country has?||value|
|exploration_utility|Utility of an exploration to the country|exploration_utility(<area>\|<character>) or exploration_utility = { area = <area> character = <character> value <operator><threshold> }|value|
|favors|How much favors does the country have in the target?|favors = { target = X value <operator> Y or value = { min max } }|value|
|favors_needed_to_annul_relations_with|Gets the number of favours needed to annul relations with the target country diplomatically|"favors_needed_to_annul_relations_with(<target>)" or favors_needed_to_annul_relations_with = { target = <country link> value <operator> <amount> }|value|
|food_maintenance|What is the xx position (0-1) the country has?||value|
|fort_maintenance|What is the xx position (0-1) the country has?||value|
|get_antagonism|how much of an antagonism type does the country have towards another country?||value|
|get_opinion|how much of an opinion type does the country have towards another country?||value|
|get_trust|how much of a trust type does the country have towards another country?||value|
|gfx_culture_applicable|Checks if a culture gfx applies to the scope object|||
|gives_fleet_basing_rights_to|Does the scope country give fleet basing rights to the specified country?||country|
|gives_food_access_to|Does the scope country give food access to the specified country?||country|
|gives_isolation_exemption_to|Does the scope country give a trade isolation exemption to specified country?||country|
|gives_military_access_to|Does the scope country give military access to the specified country?||country|
|giving_scripted_relation|Checks for giving scripted relation.|giving_scripted_relation = { target = country type = <scripted type> }||
|giving_scripted_relation_of_type|Checks if that scripted relation is given by the country scope to any other country.||relation_type|
|gold|How much gold does the country/IO have?||value|
|gold_percentage|How high the percentage of the current gold compared to the maximum does the country/IO have?||value|
|government_power|How much government power does the country/IO have?||value|
|government_power_percentage|How high the percentage of the current government power compared to the maximum does the country/IO have?||value|
|great_power_ranking|Country's position in the list of great powers||value|
|great_power_score|Checks if a country has a certain Great Power Score||value|
|had_disaster_for_years|Check if the country scope had the specified disaster type for a specific amount of years.|had_disaster_for_years = { disaster_type = <disaster type> years = <years> } or had_disaster_for_years(<disaster type>)|value|
|harmony|How much harmony does the country/IO have?||value|
|harmony_percentage|How high the percentage of the current harmony compared to the maximum does the country/IO have?||value|
|has_accepted_culture|Check if a country has a culture as an accepted culture||culture|
|has_advance|Checks if a country has a certain advance|||
|has_advance_available|Checks if a country has a certain advance available to research. Returns true if the advance has been researched already.|||
|has_advance_for_employment_system|Does the country have the necessary advance to be able to adopt the supplied employment system?||employment_system|
|has_advance_for_succession_law|Does the country have the necessary advance to be able to adopt the supplied succession law?||heir_selection|
|has_antagonism|does the country have an antagonism type towards another country?|||
|has_any_active_disaster|country has at least an active disaster||boolean|
|has_any_mission_active|Checks if the country has the specified mission as its currently active mission.||boolean|
|has_any_possible_disaster|Country has at least one possible disaster about to strike||boolean|
|has_avatar|checks if a country has a particular avatar||avatar|
|has_been_influenced_by_parliament_agenda|Checks if the country scope has already been influenced by an accepted parliament agenda in the target international organization's parliament.||international_organization|
|has_blocked_treaties|Is the country blocked from doing treaties with country?||country|
|has_casus_belli_of_type_on|Does the country have a cb of the supplied type on the target?|has_casus_belli_of_type_on = { type = <cb type key> target = <country> }||
|has_casus_belli_on|Does the country have a cb on the target?||country|
|has_claim_on_province|Does the country have a casus belli targetting the specified province?||province|
|has_colonial_charter_in|Does the country have a colonial charter in the target province_definition?||province_definition|
|has_colonial_charters|Does the country have colonial charters?||boolean|
|has_colonial_claim|country has a claim on a province definition?|has_colonial_claim = <province definition>|province_definition|
|has_completed_religious_focus|Checks if a country has completed a certain religious focus|||
|has_consort|country has a Consort||boolean|
|has_cooldown|Does a country have a particular cooldown active|||
|has_core|Does the country has a core of a specific location?||location|
|has_countries_with_antagonism|Country has antagonism towards them from other countries||boolean|
|has_countries_with_coalition_grade_antagonism|Country has antagonism towards them from other countries to the point where they could form a coalition against them||boolean|
|has_countries_with_near_coalition_grade_antagonism|Country has antagonism towards them from other countries to the point where they are thinking of forming a coalition against them||boolean|
|has_countries_with_timed_antagonism|Country has temporary antagonism towards them from other countries||boolean|
|has_country_modifier|Does the scoped country have a given modifier|has_country_modifier = name||
|has_diplomacy_with|Does the country have a certain type of diplomatic relation with another.|has_diplomacy_with = { country = <country> type = <type> }||
|has_discovered|Has the country discovered a specific location?||location|
|has_discovered_area|Has the country fully discovered the area?||area|
|has_doom|country has doom mechanics||boolean|
|has_embraced_institution|Checks if a country has embraced an institution||institution|
|has_employment_system|Does the country has the supplied employment system?||employment_system|
|has_estate_privilege|Checks if a country has a certain estate privilege||estate_privilege|
|has_exploration|character/country is currently exploring||boolean|
|has_gifted_gold_to|Has the country an active gold gift cooldown with the target country?||country|
|has_heir|country has a Heir||boolean|
|has_highest_rated_special_status_in_international_organization_of_type|Does the country have the specified special status as its highest ranking?|||
|has_historical_rival|Does the scope country have the specified country as an historical rival?||country|
|has_historical_rivals|Does the scope country have historical rivals?||boolean|
|has_insulted|Has the country an active insult cooldown with the target country?||country|
|has_invited_religious_figure|country has invited religious figures to work with them||boolean|
|has_law|Checks if a country has a certain law enabled|has_law = <law_key>|law|
|has_limited_diplomacy|Check if the country has limited diplomacy||boolean|
|has_markets|country has market centers||boolean|
|has_mission_task|Checks if the country has the specified mission task visible in its current mission.||mission_task|
|has_mutual_scripted_relation|Checks for a mutual scripted relation.|has_mutual_scripted_relation = { target = country type = <scripted type> }||
|has_mutual_scripted_relation_of_type|Checks if that scripted relation exists between the country scope and any other country.||relation_type|
|has_ongoing_parliament_debate|Country / international organization has an active parliament debate||boolean|
|has_opinion|does the country have an opinion type towards another country?|||
|has_or_had_tag|Is the scoped country the specific historical tag or was ever it; does NOT accept scopes|has_or_had_tag = GER|tag|
|has_origin_in_new_world|Check if a goods has origin in the new world||boolean|
|has_origin_in_old_world|Check if a goods has origin in the old world||boolean|
|has_parliament|Checks if the country / international organization has a parliament||boolean|
|has_participated_in_parliament|Checks if the country scope has already participated in the target international organization's parliament.||international_organization|
|has_policy|Checks if a country has a certain policy for a then policy's law|||
|has_ports|country has ports?||boolean|
|has_positive_opinion|Does the country have a positive opinion?||country|
|has_possible_nomad_targets|Does the country have any possible nearby places to migrate to?||province_definition|
|has_potential_royal_marriage|Could the country do a royal marriage with the specified country?||country|
|has_presence_in|country has a presence in the geography supplied?|||
|has_primary_or_accepted_culture|Check if a country has a culture as a primary or an accepted culture||culture|
|has_primary_or_accepted_or_tolerated_culture|Check if a country has a culture as a primary or an accepted or a tolerated culture||culture|
|has_raised_army_levies|Check if the country has raised army levies||boolean|
|has_raised_levies|Check if the country has raised levies||boolean|
|has_raised_navy_levies|Check if the country has raised navy levies||boolean|
|has_reform|Checks if a country has a specific reform||government_reform|
|has_regent|country has a regent||boolean|
|has_regular_elections|does the country have regular elections||boolean|
|has_religious_aspect|Checks if a country has a certain religious aspect||religious_aspect|
|has_royal_marriage_with|Does the country have a royal marriage with specified country?||country|
|has_ruler|country has a ruler||boolean|
|has_scripted_relation|Checks if that scripted relation exists between these two countries.|has_scripted_relation = { target = country type = <scripted type> }||
|has_scripted_relation_of_type|Checks if that scripted relation exists for the country scope with any other country.||relation_type|
|has_societal_value|Checks if the country has a specific societal value||societal_value_type|
|has_sound_tolls|country has sound tolls||boolean|
|has_special_status_in_international_organization|Does the country have a special status in the supplied international organization?|||
|has_target_casus_belli_on_us|Does the target have a cb on the country?||country|
|has_tolerated_culture|Check if a country has a culture as an Tolerated culture||culture|
|has_trade_treaty_with|Does the country have a trade agreement with a specified country?||country|
|has_truce_with|Is the country at truce with a specified country?||country|
|has_trust|does the country have a trust type towards another country?|||
|has_unlocked_any_unit_of_category|Has the country unlocked any unit of the specified category?|||
|has_voted_for_issue_in_parliament|Checks if the country scope has voted for the issue in the target international organization's parliament. Returns false if they have voted against it or have not voted at all.||international_organization|
|heathen_population_fraction|Checks the fraction of the population having a different religious group than the country||value|
|heir_score_country|Get the hypothetical heir score of the target character for the current country, even if the character in question could not be an heir.||value|
|heretic_population_fraction|Checks the fraction of the population having a different religion in the same group as the country||value|
|higher_temporary_taxes_needed|Checks how much more max tax a country wants||value|
|honor|How much honor does the country/IO have?||value|
|honor_percentage|How high the percentage of the current honor compared to the maximum does the country/IO have?||value|
|horde_unity|How much horde_unity does the country/IO have?||value|
|horde_unity_percentage|How high the percentage of the current horde_unity compared to the maximum does the country/IO have?||value|
|in_civil_war|country is in civil war||boolean|
|in_marriage_union_with|Is the country in a marriage union with specified country?||country|
|in_union_with|Is the country in a union with specified country?||country|
|in_war_of_casus_belli|Is the country in any war with the specified casus belli?||casus_belli|
|inflation|How much inflation does the country/IO have?||value|
|inflation_percentage|How high the percentage of the current inflation compared to the maximum does the country/IO have?||value|
|is_a_threat_for_us|Is the country views the target country as a threat?||country|
|is_active_parliament|country has an active parliament called||boolean|
|is_ai|country is run by AI||boolean|
|is_annexing|Is the country annexing the specified country?||country|
|is_annexing_any_country|Is the country annexing any other country?||boolean|
|is_at_war_with|Is the country at war with a specified country?||country|
|is_auto_raise_taxrate_for_all_estates|Check if all estates have auto raise taxrates?||boolean|
|is_being_annexed|Is the country being annexed by any other country?||boolean|
|is_being_annexed_by|Is the country getting annexed by the specified country?||country|
|is_colonial_overlord|Country is an overlord of a colonial subject||boolean|
|is_colonial_subject|Country is a type of colonial subject||boolean|
|is_colonial_top_overlord|Country is the top overlord of a colonial subject||boolean|
|is_creating_cb_against|Checks if the current country scope is creating a casus belli against the target country.||country|
|is_creating_cb_of_type|Checks if the current country scope is creating a casus belli of the specified type against the target country.|is_creating_cb_of_type = { target = <country scope> type = <casus belli type> }||
|is_discovered_by|Is the scope location/country discovered by the target country?||country|
|is_disloyal_subject|Is the country a disloyal subject?||boolean|
|is_dominant_country_of|Check if a country is the dominant country of a culture||culture|
|is_during_bankruptcy|country is having a bankruptcy||boolean|
|is_elector_in_international_organization|Checks if the country is an elector in the target international organization.||international_organization|
|is_embargoed_by|Is the country embargoed by the specified country?||country|
|is_embargoing|Is the country embargoing the specified country?||country|
|is_enemy_of|Is the country a enemy of a specified country?||country|
|is_enemy_of_international_organization|Is the country an enemy of the supplied international organization?||international_organization|
|is_fighting_war_together_with|Is the country fighting a war together with a specified country?||country|
|is_friendly_with|Is the country friendly with specified country?||country|
|is_great_power|country is a great power||boolean|
|is_hegemon|country is a Hegemon||boolean|
|is_hegemon_type|Is the country a Hegemon of the specified type?||hegemony|
|is_historical_rival_of|Is the country an historical rival of a specified country?||country|
|is_hostile_with|Is the country hostile of specified country?||country|
|is_human|country is controlled by a human||boolean|
|is_in_any_same_international_organization|Is the country in any same international organization as the target country?||country|
|is_in_losing_war|Country is currently in a war with less than 0 war score.||boolean|
|is_in_same_international_organization|Is the country in the same international organization as the target country?|is_in_same_international_organization = { international_organization = <IO scope> target = <country> }||
|is_integrating|Is the country integrating any of its owned locations in province?||province_definition|
|is_known_by_country|Checks if the country is known by the specified country||country|
|is_leader_of_international_organization|Is the country the Leader of the specified international organization?||international_organization|
|is_member_of_international_organization|Is the country in the supplied international organization?||international_organization|
|is_member_of_international_organization_of_type|Is the country in an international organization of the specified type?|is_member_of_international_organization_of_type = { type = x target = <country> }||
|is_neighbor_of|Is the country or location a Neighbor to the specified country?||country|
|is_neighbor_of_international_organization|Is the country or location a neighbor to the specified international organization?||international_organization|
|is_overlord|country is an overlord||boolean|
|is_player_playstyle|Player has only one playstyle and is equal to MILITARY, ADMINISTRATIVE or DIPLOMATIC|||
|is_real_country|Checks if a country is a real country as opposed to rebels, mercenaries, pirates||boolean|
|is_rebel_country|Checks if a country is a rebel country created from a civil war||boolean|
|is_regency_extended|country has an extended regency?||boolean|
|is_religious_aspect_enabled|Checks if the input religious aspect is enabled for the country in scope. Meaning if the allow trigger in religious aspect DB object returns true.|c:ARA = { is_religious_aspect_enabled = religious_aspect:gomarism }|religious_aspect|
|is_revolution_target|Check if the country is the target of the revolution||boolean|
|is_revolutionary|Check if the country is revolutionary||boolean|
|is_rival_of|Is the country a rival of a specified country?||country|
|is_subject|country is a subject||boolean|
|is_subject_of|Is the country a subject to the specified country?||country|
|is_subject_or_below_of|Is the country a subject of (or subject of a subject of) the specified country?||country|
|is_subject_type|Is the country a subject of the specified type?|||
|is_target_of_international_organization_of_type|Is the country a target of an international organization of the specified type?|||
|is_threat_to|Current country scope is a threat and have a casus belli to the target country||country|
|is_valid_colonial_charter|is this colonial charter valid, or blocked by a recognised claim?||province_definition|
|is_war_leader_of|Checks if the current country scope is a war leader of the target war||war|
|join_organization_ai_desire|Returns the AI desire to join the specified target international organization.|join_organization_ai_desire = { international_organization = <IO scope> value = <script_value> } or join_organization_ai_desire(<IO scope>)|value|
|karma|How much karma does the country/IO have?||value|
|karma_percentage|How high the percentage of the current karma compared to the maximum does the country/IO have?||value|
|knows_about_institution|Checks if a country has knows about an institution||institution|
|knows_country|Checks if the country knows of the specified country||country|
|language_percentage_in_country|The percentage of speakers of a specific language in the current country||value|
|legitimacy|How much legitimacy does the country/IO have?||value|
|legitimacy_percentage|How high the percentage of the current legitimacy compared to the maximum does the country/IO have?||value|
|liberty_desire|Checks the amount of liberty desire a country has||value|
|location_progress_for_formable|Checks the progress of the country scope to form the specified formable in percentage.|location_progress_for_formable = { formable_country = <formable scope> value = <script_value> } or location_progress_for_formable(<formable scope>)|value|
|long_term_trigger_currency_utility|Checks the AI utility of adding an amount of a certain trigger every month to the scoped object|long_term_trigger_currency_utility = { trigger = <trigger> size = <size> target = <optional target> value >= <script_value> }|value|
|lowest_war_score|Checks the lowest war score of ongoing wars||value|
|manpower|How much Manpower does the country/IO have?||value|
|manpower_percentage|Checks the percentage of manpower a country has compared to its maximum||value|
|max_manpower|Checks if a country has a certain Max manpower||value|
|max_sailors|Checks if a country has a certain Max Sailors||value|
|military_strength|Checks the total military strength (max manpower, army size, levy power) of a country||value|
|military_tech_level|Checks if a country has a certain level of military tech||value|
|mission_completed|Checks if the country has completed the mission.||mission|
|mission_task_bypassed|Checks if the country has bypassed the mission task.||mission_task|
|mission_task_completed|Checks if the country has completed the mission task.||mission_task|
|modifier_utility|Checks the AI utility of a modifier||value|
|modifier_utility_include_locations|Checks the AI utility of a modifier with location checks||value|
|monthly_balance|Checks the monthly balance of a country||value|
|monthly_income_total|Checks if a country has a certain income||value|
|monthly_income_trade_and_tax|Checks if a country has a certain trade and tax income||value|
|monthly_manpower|Checks if a country has a certain monthly manpower||value|
|monthly_sailors|Checks if a country has a certain monthly Sailors||value|
|monthly_trade_income|Checks if a country has a certain income from trade||value|
|months_since_last_parliament_called|Checks how many months its been since the country / international organization last called a parliament||value|
|months_since_peace|Checks how many months its been since a country was at peace||value|
|months_since_war|Checks how many months its been since a country was at War||value|
|naval_range|The naval range of the country||value|
|navy_maintenance|What is the xx position (0-1) the country has?||value|
|navy_size|Checks if a country has a certain amount of ships||value|
|navy_size_percentage|Checks if a country has a certain percentage of ships compared to expected size||value|
|navy_tradition|How much navy tradition does the country/IO have?||value|
|navy_tradition_percentage|How high the percentage of the current navy tradition compared to the maximum does the country/IO have?||value|
|needs_opinion_with|Determines if a country needs X more relations with another nation.|needs_opinion_with = { target = <country> value <comparator> <script_value> }|value|
|num_adult_capable_characters|Checks if a country has a certain amount of adult characters who can do cabinet or military stuff||value|
|num_artists|Checks if a country has a certain amount of artists||value|
|num_avatars|Checks if a country has a certain amount of avatars||value|
|num_cardinals|Checks if a country has a certain amount of Cardinals||value|
|num_characters|Checks if a country has a certain amount of living characters||value|
|num_colonial_charters|Checks if a country has a certain amount of colonial charters||value|
|num_embraced_institutions|Checks if a country has a certain number of institutions embraced||value|
|num_explorations|Checks if a country has a certain amount of Explorations||value|
|num_forts|Checks if a country has a certain amount of forts||value|
|num_known_institutions|Checks if a country knows a certain number of institutions||value|
|num_loans|Checks if a country has a certain amount of loans||value|
|num_locations|Checks if a country has a certain amount of owned locations||value|
|num_locations_owned_or_owned_by_subjects|Checks if a country or its direct subjects has a certain amount of owned locations||value|
|num_locations_owned_or_owned_by_subjects_or_below|Checks if a country, its subjects or its subjects' subjects has a certain amount of owned locations||value|
|num_of_active_parliament_agendas|Check how many parliament agendas are currently available to the country or international organization.||value|
|num_of_advances_researched|Checks how many advances a country currently has researched.||value|
|num_of_diplomats|Checks if a country has an amount of diplomats||value|
|num_of_locations_owned_by_io|Checks if a country has an amount of locations owned by certain IO||value|
|num_of_markets_with_merchants|Checks if a country has merchants in the specified amount of markets.||value|
|num_of_non_rural|Checks if a country has an amount of towns and cities||value|
|num_of_non_rural_ports|Checks if a country has an amount of non-rural ports||value|
|num_of_ports|Checks if a country has an amount of ports||value|
|num_of_religious_aspects|Gets the total amount of church aspects in the country||value|
|num_of_trades|Checks if a country has an amount of trades active||value|
|num_open_reform_slots|Checks if a country has a certain amount of open government reform slots||value|
|num_possible_privileges|Checks if the scope country or estate has a certain amount of privileges||value|
|num_possible_rivals|Checks if a country has a certain amount of possible rivals||value|
|num_privileges|Checks if the scope country or estate has a certain amount of privileges||value|
|num_provinces|Checks if a country has a certain amount of provinces||value|
|num_rebels|Checks if a country has a certain amount of Rebels||value|
|num_reforms|Checks if a country has a certain amount of government reforms||value|
|num_regiments|Checks if a country has a certain amount of regiments||value|
|num_relations_above_limit|Amount above relations limit||value|
|num_rivals|Checks if a country has a certain amount of rivals||value|
|num_subjects|Checks the total number of subjects of a country||value|
|num_works_of_art|Checks if a country has a certain number of works of art||value|
|offensive_alliance_strength|Strength of an offensive alliance, including the nation with all countries giving offensive support and those that can be called in for offensive wars||value|
|offer_relation_acceptance|How high is the target country's AI value of accepting the scripted relation offered by the current country scope?|offer_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "offer_relation_acceptance(<scripted relation type>\|<country>)"|value|
|opinion|is the country's opinion of the target greater or equal than the value?|opinion = { target = X value <operator> Y or value = { min max } }|value|
|opinion_difference_between|Get the opinion of the current country scope against the first target country and subtract it with the opinion the current scope has of the second country.|opinion_difference_between = { first = <country> second = <country> value = <script_value> } or opinion_difference_between(<country>\|<country>)|value|
|own_entire_area|Does the country own all locations in area?||area|
|own_entire_province|Does the country own all locations in province?||province_definition|
|owns|Does the country own a specific location?||location|
|owns_any_foreign_buildings_in|Does the country own any foreign buildings in the target country?||country|
|owns_most_foreign_buildings_in_location|Does the country own the majority of the foreign buildings in the target location?||location|
|owns_or_has_subject_in|country has a presence in the geography supplied?|||
|owns_or_non_sovereign_subject_owns|Does the country or any of its direct non-sovereign subjects own a specific location?||location|
|parliament_issue_chance|The chance an issue will be selected||value|
|parliament_issue_support|The current support in parliament for an issue||value|
|parliament_issue_will_pass|Check if the parliament issue of the country / international in debate will pass||boolean|
|parliament_type_is_enabled_in|Is a parliament type enabled in the scope country?||parliament_type|
|parliament_type_is_locked_in|Is a parliament type locked in the scope country?||parliament_type|
|parliament_type_utility|Utility of a parliament type that can subtract the utility of current parliament modifiers|parliament_type_utility(<type>\|<bool>) or parliament_type_utility = { parliament_type = <type> subtract_current = <bool> value <operator><threshold> }|value|
|parliament_type_visible_in|Can we see a parliament type in the scope country?||parliament_type|
|payment_contribution|Gets how much the country has to pay for the specified IO and payment type.|payment_contribution = { international_organization = <> payment = <> }|value|
|payment_maintenance|gets the payment maintenance level for a country in an international organization.|payment_maintenance = { international_organization = <> payment = <> }|value|
|peace_treaty_antagonism|Get how much antagonism the specified peace treaty type would cause for the current country scope against the target country.|peace_treaty_antagonism = { peace_treaty = <scripted peace treaty scope> loser = <losing country scope> [target = <thing>] value <comparator> <real> } or "peace_treaty_antagonism(<peace treaty scope>\|<loser>\|<thing>)"||
|peace_treaty_war_score_cost|Get how much war score the specified peace treaty type would cost for the current country scope against the target country.|peace_treaty_war_score_cost = { peace_treaty = <scripted peace treaty scope> loser = <losing country scope> [target = <thing>] value <comparator> <real> } or "peace_treaty_war_score_cost(<peace treaty scope>\|<loser>\|<thing>)"||
|player_proficiency|Is player proficiency equal to NOVICE, EXPERIENCED, ADVANCED or EXPERT?|||
|player_proficiency_greater|Is player proficiency greater than NOVICE, EXPERIENCED, ADVANCED or EXPERT?|||
|player_proficiency_greater_eq|Is player proficiency greater or equal to NOVICE, EXPERIENCED, ADVANCED or EXPERT?|||
|player_proficiency_less|Is player proficiency less than NOVICE, EXPERIENCED, ADVANCED or EXPERT?|||
|player_proficiency_less_eq|Is player proficiency less or equal to NOVICE, EXPERIENCED, ADVANCED or EXPERT?|||
|pop_type_percentage_in_country|The percentage of the specific pop type in the current country||value|
|pop_type_population_in_country|The number of the specific pop type in the current country||value|
|possible_military_leaders|Checks if a country has a certain amount of possible military leaders||value|
|power_projection|Checks if a country has a power projection||value|
|prestige|How much prestige does the country/IO have?||value|
|prestige_percentage|How high the percentage of the current prestige compared to the maximum does the country/IO have?||value|
|prev_antagonism_towards_this|Gets the previous scope country's antagonism towards the current scope country||value|
|prev_opinion_of_this|Gets the previous scope country's opinion of the current scope country||value|
|prev_trust_of_this|Gets the previous scope country's trust of the current scope country||value|
|proper_culture_nobles|Checks the proportion of your population that is primary or accepted culture nobles||value|
|purity|How much purity does the country/IO have?||value|
|purity_percentage|How high the percentage of the current purity compared to the maximum does the country/IO have?||value|
|receives_fleet_basing_rights_from|Does the scope country receive fleet basing rights from the specified country?||country|
|receives_food_access_from|Does the scope country receive food access from the specified country?||country|
|receives_isolation_exemption_from|Does the scope country receive a trade isolation exemption from the specified country?||country|
|receives_military_access_from|Does the scope country receive military access from the specified country?||country|
|receiving_scripted_relation|Checks for receiving scripted relation.|receiving_scripted_relation = { target = country type = <scripted type> }||
|receiving_scripted_relation_of_type|Checks if that scripted relation is received by the country scope from any other country.||relation_type|
|regular_army_size|Checks if a country has a certain army size of regulars (maximum strength)||value|
|regular_navy_size|Checks if a country has a certain navy size of regular ships||value|
|relative_defensive_alliance_strength|Gets the relative strength of the scope country including defensive alliances to the supplied one|relative_defensive_alliance_strength(<target>) <operator> <script_value> OR relative_defensive_alliance_strength = { target = <country scope> value <operator> <script_value> }|value|
|relative_military_strength|calculates the relative military strength of the scope country to the target.|relative_military_strength = { target = <country scope> value <operator> <script_value> or value = { min max } }|value|
|relative_strength|Gets the relative strength of the scope country to the supplied one|relative_strength(<target>) or relative_strength = { target = <country link> value <operator> <amount> }|value|
|relevant_countries|Do we have any diplomatic action with the target country?||country|
|religion_group_percentage_in_country|The percentage of a specific religion group in the current country||value|
|religion_percentage_in_country|The percentage of a specific religion in the current country||value|
|religion_population_in_country|The number of pops with a specific religion in the current country||value|
|religious_influence|How much religious influence does the country/IO have?||value|
|religious_influence_percentage|How high the percentage of the current religious influence compared to the maximum does the country/IO have?||value|
|religious_unity|Checks the fraction of the population sharing the country's religion||value|
|relocate_market_utility|Utility of relocating a market|relocate_market_utility(<location>,<location>) or relocate_market_utility = { location = <location> new_location = <location> value <operator><threshold> }|value|
|remaining_parliament_days|Checks how many days are left in the parliament of the country / international organization before it concludes. Returns -1 when there is no parliament active.||value|
|remove_static_modifier_utility|Checks the AI utility of removing a static modifier from the scoped object|remove_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|value|
|republican_tradition|How much republican_tradition does the country/IO have?||value|
|republican_tradition_percentage|How high the percentage of the current republican_tradition compared to the maximum does the country/IO have?||value|
|request_relation_acceptance|How high is the target country's AI value of accepting the scripted relation requested by the current country scope?|request_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "request_relation_acceptance(<scripted relation type>\|<country>)"||
|research_progress|Checks the progress of the current research in the country||value|
|resolution_opinion|Gets the current scope country's opinion of a resolution.|resolution_opinion(<IO>\|<resolution>\|<vote>) <operator> <script_value> OR resolution_opinion = { international_organization = <international organization> resolution = <resolution> vote = <vote scope> value <operator> <script_value> }|value|
|reverse_country_interaction_acceptance|How high is the current country's AI value of accepting the country interaction done by the specified country scope? Always return 0 if the scope is a player|reverse_country_interaction_acceptance = { type = <country interaction> target = <country> value = <script_value> } or reverse_country_interaction_acceptance(<country interaction>\|<country>)|value|
|reverse_offer_relation_acceptance|How high is the current country's AI value of accepting the scripted relation offered by the specified country scope?|reverse_offer_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "reverse_offer_relation_acceptance(<scripted relation type>\|<country>)"||
|reverse_request_relation_acceptance|How high is the current country's AI value of accepting the scripted relation requested by the specified country scope?|reverse_request_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "reverse_request_relation_acceptance(<scripted relation type>\|<country>)"||
|righteousness|How much righteousness does the country/IO have?||value|
|righteousness_percentage|How high the percentage of the current righteousness compared to the maximum does the country/IO have?||value|
|rite_power|How much rite power does the country/IO have?||value|
|rite_power_percentage|How high the percentage of the current rite power compared to the maximum does the country/IO have?||value|
|ruler_reign|Checks if the ruler of a country has ruled for x years||value|
|ruler_reign_in_days|Checks if the ruler or regent of a country has ruled for x days||value|
|ruler_term_start_date|Gets the start date of the current ruler term||date|
|sailors|How much Sailors does the country/IO have?||value|
|sailors_percentage|Checks the percentage of Sailors a country has compared to its maximum||value|
|self_control|How much self control does the country/IO have?||value|
|self_control_percentage|How high the percentage of the current self control compared to the maximum does the country/IO have?||value|
|short_term_trigger_currency_utility|Checks the AI utility of adding an amount of a certain trigger to the scoped object|short_term_trigger_currency_utility = { trigger = <trigger> size = <size> target = <optional target> value >= <script_value> }|value|
|slider_minting_value|How much minting is going on (0..1)||value|
|societal_value_progress|Gets progress towards societal value||value|
|spy_network|How much spy-network does the country have in the target?|spy_network = { target = X value <operator> Y or value = { min max } }|value|
|stability|How much Stability does the country/IO have?||value|
|stability_percentage|How high the percentage of the current Stability compared to the maximum does the country/IO have?||value|
|state_religion_clergy|Checks the proportion of your population that is true faith clergy||value|
|subject_loyalty|Checks a country's subject loyalty||value|
|subjects_relative_power|Compares to relative power of all subjects combined||value|
|supports_rebel|Checks if a country supports the target rebel||rebels|
|tag|Is the scoped country the specific country tag; does NOT accept scopes|tag = ENG|tag|
|this_antagonism_towards_prev|Gets the current scope country's antagonism towards the previous scope country||value|
|this_opinion_of_prev|Gets the current scope country's opinion of the previous scope country||value|
|this_trust_of_prev|Gets the current scope country's trust of the previous scope country||value|
|threat_level_to|Return the threat level the scope country has towards the target country scope.|threat_level_to = { country = <country scope> value = <script_value> } or threat_level_to(<country scope>)|value|
|topography_count|Returns the amount of owned locations with the specified topography.|topography_count = { type = <topography scope> value <operator> <value> } or "topography_count(<topography scope>)"||
|topography_percent|Returns the percentage of owned locations with the specified topography.|topography_percent = { type = <topography scope> value <operator> <value> } or "topography_percent(<topography scope>)"||
|total_accepted_culture_population|Checks if a country has an acceputed or primary culture population size of the specified value||value|
|total_control_scaled_population|Checks if a country has value that is population * local_control its in||value|
|total_debt|Checks how much a country has in total debt||value|
|total_development|Gets the total amount of development in the country||value|
|total_dynastic_power|Check the total amount of dynastic power the scoped dynasty or country has. In case of country, the dynasty of the ruler or of the heir in case of regency is taken.||value|
|total_effective_goods_production_buildings|Returns the number of effective building levels which produce the specified good.|total_effective_goods_production_buildings = { goods = <goods> value <comparator> <script_value> }|value|
|total_foreign_buildings_levels|Checks the total number of foreign buildings of a country||value|
|total_heathen_population|Checks if a country has a heathen population size of the specified value||value|
|total_heretic_population|Checks if a country has a heretic population size of the specified value||value|
|total_merchant_capacity|Checks if a country has a certain total merchant capacity||value|
|total_not_tolerated_culture_population|Checks if a country has an intolerated culture population size of the specified value||value|
|total_population|Checks if a country has a certain population||value|
|total_population_in_international_organization|Checks if the country has the defined amount of pops in the target IO.|total_population_in_international_organization = { international_organization = <IO> value <operator> <script_value> } or total_population_in_international_organization(<IO>)|value|
|total_population_in_international_organization_percentage|Checks if the country has the defined amount of pops in the target IO.|total_population_in_international_organization_percentage = { international_organization = <IO> value <operator> <script_value> } or total_population_in_international_organization_percentage(<IO>)|value|
|total_primary_culture_population|Checks if a country has a primary culture population size of the specified value||value|
|total_tolerated_culture_population|Checks if a country has a tolerated culture population size of the specified value||value|
|total_true_faith_population|Checks if a country has a true faith population size of the specified value||value|
|tribal_cohesion|How much tribal_cohesion does the country/IO have?||value|
|tribal_cohesion_percentage|How high the percentage of the current tribal_cohesion compared to the maximum does the country/IO have?||value|
|trust|is the country's trust towards the target greater or equal than the value?|trust = { target = X value <operator> Y or value = { min max } }|value|
|union_length_days|returns the number of days a country has been in a union with the target country.|union_length_days = { target = <country> value <comparator> <script_value> }|value|
|upkeep_maintenance|What is the xx position (0-1) the country has?||value|
|used_cultures_capacity|Checks if a country has a certain cost of cultures accepted & tolerated||value|
|used_diplomatic_capacity|Diplomatic capacity used by the country||value|
|used_fort_limit|How much Fort Limit is currently being used?||value|
|used_fort_limit_percentage|What percentage of our Fort Limit is currently being used?||value|
|uses_government_power|Checks if a country has a certain government_power (e.g. 'legitimacy')|||
|vegetation_count|Returns the amount of owned locations with the specified vegetation.|vegetation_count = { type = <vegetation scope> value <operator> <value> } or "vegetation_count(<vegetation scope>)"||
|vegetation_percent|Returns the percentage of owned locations with the specified vegetation.|vegetation_percent = { type = <vegetation scope> value <operator> <value> } or "vegetation_percent(<vegetation scope>)"||
|vote_impact_in_resolution|Check how much vote impact the current country scope would make when voting in the target resolution of the target IO.|vote_impact_in_resolution = { international_organization = <IO> resolution = <resolution> value <operator> <real> } or vote_impact_in_resolution(<IO>\|<resolution>)|value|
|vote_percentage_impact_in_resolution|Check how much vote percentage impact the current country scope would make when voting in the target resolution of the target IO.|vote_percentage_impact_in_resolution = { international_organization = <IO> resolution = <resolution> value <operator> <real> } or vote_percentage_impact_in_resolution(<IO>\|<resolution>)|value|
|wants_casus_belli_with|Does country want a casus belli with another nation? Only for Ai||country|
|wants_military_access_in|country wants military access in this other country?||country|
|wants_opinion_with|Does country want more opinion with another nation? Only for Ai||country|
|wants_to_give_away_any_province|Country wants to give any province to a subject?||boolean|
|wants_to_subjugate|country wants to subjugate another country?||country|
|war_enthusiasm|The war enthusiasm of the current country scope in the target war.|war_enthusiasm = { war = <war scope> value = <script_value> } or war_enthusiasm(<war scope>)|value|
|war_exhaustion|How much WarExhaustion does the country/IO have?||value|
|war_exhaustion_percentage|How high the percentage of the current WarExhaustion compared to the maximum does the country/IO have?||value|
|war_score_in_war|Check how much war score the current country has in the target war.|war_score_in_war = { war = <war> value <operator> <real> } or "war_score_in_war(<war>)"|value|
|war_score_in_war_whole_side|Check how much war score the war side of the current country has in the target war.|war_score_in_war_whole_side = { war = <war> value <operator> <real> } or "war_score_in_war_whole_side(<war>)"|value|
|war_score_versus|Gets the war score of the scope country against the supplied one|war_score_versus(<target>) or war_score_versus = { target = <country link> value <operator> <amount> }|value|
|within_diplomatic_range|Is the target country within diplomatic range?||country|
|yanantin|How much yanantin does the country/IO have?||value|
|yanantin_percentage|How high the percentage of the current yanantin compared to the maximum does the country/IO have?||value|
|yearly_gold|How much gold does the country get per year?||value|
|yearly_manpower|How many Manpower does the country get per year?||value|
|yearly_sailors|How many Sailors does the country get per year?||value|
|years_in_international_organization|Checks if the country has been in the current international organization scope for x years.|years_in_international_organization = { country = <country scope> value = <years> } or years_in_international_organization(country)|value|

### Culture scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|cultural_influence|How much influence does the culture have?||value|
|cultural_tradition|How much tradition does the culture have?||value|
|cultural_view|does the culture have the specified opinion of the target?|cultural_view = { target = <target culture> value <operator> <script_value> }||
|culture_opinion_impact|Opinion impact of a particular culture on another|culture_opinion_impact(<culture link>) or culture_percentage = { culture = <culture link> value <operator> <amount> }|value|
|gfx_culture_applicable|Checks if a culture gfx applies to the scope object|||
|has_any_culture_group|If a culture belongs to any culture group.||boolean|
|has_culture_group|If a culture belongs to a specific culture group.||culture_group|
|has_culture_with_tag|Checks if a culture has the specified tags|||
|has_graphical_culture|Check if a culture has a graphical culture|||
|has_shared_culture_group|If a culture belongs to a specific culture group.||culture|
|is_accepted_in|If a culture is accepted in the target country?||country|
|is_merged_culture_group|If a culture has been merged from a culture group.||boolean|
|is_merged_culture_group_of|If a culture has been merged from this specific culture group.||culture_group|
|is_primary_in|If a culture is a primary culture in the target country?||country|
|is_primary_or_accepted_in|If a culture is a primary culture or accepted in the target country?||country|
|is_tolerated_in|If a culture is tolerated in the target country?||country|
|reverse_cultural_view|does the target have the specified opinion of the culture?|reverse_cultural_view = { target = <target culture> value <operator> <script_value> }||

### Goods scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|food_value|Check the food value of the goods scope.||value|
|goods_category|tests the goods category - raw_material or produced|||
|goods_method|tests the goods method - mining/farming/hunting/gathering|||
|has_tag|Check if that object has the specified tag.|||
|is_demanded_in_market|Check if the goods scope is demanded in the target market.||market|
|is_demanded_in_market_by_buildings|Check if the goods scope is demanded in the target market by buildings.||market|
|is_demanded_in_market_by_burgher_trades|Check if the goods scope is demanded in the target market by burgher trades.||market|
|is_demanded_in_market_by_constructions|Check if the goods scope is demanded in the target market by constructions.||market|
|is_demanded_in_market_by_pops|Check if the goods scope is demanded in the target market by pops.||market|
|is_demanded_in_market_by_roads|Check if the goods scope is demanded in the target market by roads.||market|
|is_demanded_in_market_by_trades|Check if the goods scope is demanded in the target market by trades.||market|
|is_demanded_in_market_by_units|Check if the goods scope is demanded in the target market by units.||market|
|is_food|Check if a goods is food||boolean|
|is_in_surplus_in_market|Gets the possible trade surplus of the scope goods in the target market.||value|
|is_produced_by_production_method|Returns true if the trade good is produced by the specified production method.||production_method|
|is_used_by_production_method|Returns true if the trade good is used by the specified production method.||production_method|
|price_in_market|Gets the price of the scoped goods in the supplied market|price_in_market = { market = <market_name> value >= <script_value> }|value|
|raw_material_occurrence|Check how many locations world wide produce this raw material||value|

### Institution scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|has_spawned|Has the institution spawned anywhere?||boolean|
|is_embraced_for|Is the institution embraced by the target country?||country|

### International organization scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|army_tradition|How much army tradition does the country/IO have?||value|
|army_tradition_percentage|How high the percentage of the current army tradition compared to the maximum does the country/IO have?||value|
|average_special_status_power|Get the average political power of the target special status.|average_special_status_power = { type = <special status> value <operator> <float> } or average_special_status_power(<special status>)|value|
|can_annex_members|Can a country annex members in the scope international organization?||country|
|can_initiate_policy_votes|Can a country initiate votes in the scope international organization?||country|
|combined_special_status_power|Get the combined special status power of ALL special statuses in the international organization||value|
|combined_unique_special_status_power|Get the combined special status power of all countries with their highest ranking special status in the international organization||value|
|complacency|How much complacency does the country/IO have?||value|
|complacency_percentage|How high the percentage of the current complacency compared to the maximum does the country/IO have?||value|
|country_has_been_member_for_years|Checks if the country has been in the current international organization scope for x years.|country_has_been_member_for_years = { country = <country scope> value = <years> } or country_has_been_member_for_years(country)|value|
|country_has_special_status|Does the country have a special status in this international organization?|||
|currency_percentage_towards_limit|Gets currency progress towards specified limit||value|
|devotion|How much devotion does the country/IO have?||value|
|devotion_percentage|How high the percentage of the current devotion compared to the maximum does the country/IO have?||value|
|doom|How much doom does the country/IO have?||value|
|doom_percentage|How high the percentage of the current doom compared to the maximum does the country/IO have?||value|
|gold|How much gold does the country/IO have?||value|
|gold_percentage|How high the percentage of the current gold compared to the maximum does the country/IO have?||value|
|government_power|How much government power does the country/IO have?||value|
|government_power_percentage|How high the percentage of the current government power compared to the maximum does the country/IO have?||value|
|harmony|How much harmony does the country/IO have?||value|
|harmony_percentage|How high the percentage of the current harmony compared to the maximum does the country/IO have?||value|
|has_active_resolution|Does the scope international organization/situation have any active resolutions?||boolean|
|has_cached_or_cast_vote_for|Has the supplied country voted or has a cached vote from previous month on the supplied resolution for a specific target in the scope international organization/situation?|||
|has_cooldown|Does a country have a particular cooldown active|||
|has_elections|Checks if an international organization has electors||boolean|
|has_enabled_currency|Checks what currency has been enabled for the international organization (manpower, sailors, gold)|||
|has_international_organization_modifier|Does the scoped international organization have a given modifier|has_international_organization_modifier = name||
|has_land_ownership_rule|Checks if the international organization has a landownership rule set||boolean|
|has_location|Is the supplied location owned by the scope international organization?||location|
|has_member|Checks if an international organization has a certain member||country|
|has_ongoing_parliament_debate|Country / international organization has an active parliament debate||boolean|
|has_parliament|Checks if the country / international organization has a parliament||boolean|
|has_special_status_available|Checks if an international organization has a particular special status available||special_status|
|has_voted|Has the supplied country voted on the supplied resolution in the scope international organization/situation?|||
|has_voted_for|Has the supplied country voted on the supplied resolution for a specific target in the scope international organization/situation?|||
|honor|How much honor does the country/IO have?||value|
|honor_percentage|How high the percentage of the current honor compared to the maximum does the country/IO have?||value|
|horde_unity|How much horde_unity does the country/IO have?||value|
|horde_unity_percentage|How high the percentage of the current horde_unity compared to the maximum does the country/IO have?||value|
|inflation|How much inflation does the country/IO have?||value|
|inflation_percentage|How high the percentage of the current inflation compared to the maximum does the country/IO have?||value|
|international_organization_can_own_land|Can the international organization own land?||boolean|
|international_organization_has_internal_peace|Checks if no member country is in a direct war with another member country||boolean|
|international_organization_has_law|Has the scope international organization enacted a policy for the supplied law?||law|
|international_organization_has_laws|Has the scope international organization enacted a policy for the supplied law?||boolean|
|international_organization_has_leader|Does the international organization have a leader country?||boolean|
|international_organization_has_policy|Has the scope international organization enacted the supplied policy?||policy|
|international_organization_leader_count|Checks how many leaders (defined as 'leaders' in the IO type) are currently present in the current international organization||value|
|international_organization_leader_reign|Checks if the ruler of an international organization has ruled for x years||value|
|international_organization_leader_reign_in_days|Checks if the ruler of an international organization has ruled for x days||value|
|international_organization_lifetime|Checks if the international organization has existed for x years||value|
|international_organization_lifetime_in_days|Checks if the international organization has existed for x days||value|
|international_organization_locations_owned_percentage|The percentage of the locations of an international organization owned by a country||value|
|international_organization_modifier_strength|Does the scoped international_organization have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|international_organization_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "international_organization_modifier_strength(<modifier key>)"||
|international_organization_num_locations|Checks if an international organization has a certain amount of owned locations||value|
|international_organization_population|Checks if an international organization has a certain population based on the locations it owns||value|
|io_within_diplomatic_range|Is the target international organization within diplomatic range?||country|
|is_active_parliament|country has an active parliament called||boolean|
|is_international_organization_annullable|Is the international organization able to be annulled by treaty?||boolean|
|is_international_organization_unique|Is the international organization unique?||boolean|
|is_relevant|Checks if an international organization is relevant to the supplied country||country|
|karma|How much karma does the country/IO have?||value|
|karma_percentage|How high the percentage of the current karma compared to the maximum does the country/IO have?||value|
|law_enabled_to_international_organization|Can we select a policy for a law in the scope international organization?||law|
|law_is_locked_in_international_organization|Is a law locked in the scope international organization?||law|
|law_visible_to_international_organization|Can we see a policy for a law in the scope international organization?||law|
|leader_change_method|Check if the international organization has the specified leader changed method (rotation/vote/lottery/none)|||
|leader_change_trigger_type|Check if the international organization has the specified leader changed trigger type (rulerchang/timed/none)|||
|leader_special_status_power|Get the special status power of all special statuses with the 'leader' trait||value|
|leader_special_status_power_fraction|Get the fraction of the special status power of all special statuses with the 'leader' trait||value|
|leader_type|Check if the international organization has the specified leader type (character/country/none)|||
|legitimacy|How much legitimacy does the country/IO have?||value|
|legitimacy_percentage|How high the percentage of the current legitimacy compared to the maximum does the country/IO have?||value|
|location_can_be_added_to_international_organization|Can we add a location to the scope international organization?||location|
|location_can_be_removed_from_international_organization|Can we remove a location from the scope international organization?||location|
|manpower|How much Manpower does the country/IO have?||value|
|max_countries_with_special_status|gets the max number of countries with a specific special status in an international organization||value|
|modifier_utility|Checks the AI utility of a modifier||value|
|modifier_utility_include_locations|Checks the AI utility of a modifier with location checks||value|
|months_between_leader_changes|Checks if a country has a specific reform||value|
|months_since_last_parliament_called|Checks how many months its been since the country / international organization last called a parliament||value|
|navy_tradition|How much navy tradition does the country/IO have?||value|
|navy_tradition_percentage|How high the percentage of the current navy tradition compared to the maximum does the country/IO have?||value|
|num_countries_with_special_status|gets the number of countries with a particular special status in an international organization||value|
|num_of_active_parliament_agendas|Check how many parliament agendas are currently available to the country or international organization.||value|
|num_of_electors|Checks how many electors the international organization has||value|
|organization_strength_relative_to_country|Gets the relative strength of the scope organization to the supplied country|organization_strength_relative_to_country(<target>\|<bool exclude_target>) or organization_strength_relative_to_country = { target = <country link> value <operator> <amount> exclude_target = <bool> }|value|
|parliament_issue_chance|The chance an issue will be selected||value|
|parliament_issue_support|The current support in parliament for an issue||value|
|parliament_issue_will_pass|Check if the parliament issue of the country / international in debate will pass||boolean|
|parliament_type_enabled_in_international_organization|Is a parliament type enabled in the scope international organization?||parliament_type|
|parliament_type_is_locked_in_international_organization|Is a parliament type locked in the scope international organization?||parliament_type|
|parliament_type_visible_in_international_organization|Can we see a parliament type in the scope international organization?||parliament_type|
|policy_enabled_to_international_organization|Can we enact a policy in the scope international organization?||policy|
|policy_is_locked_in_international_organization|Is a policy locked in the scope international organization?||policy|
|policy_visible_to_international_organization|Can we see a policy in the scope international organization?||policy|
|prestige|How much prestige does the country/IO have?||value|
|prestige_percentage|How high the percentage of the current prestige compared to the maximum does the country/IO have?||value|
|purity|How much purity does the country/IO have?||value|
|purity_percentage|How high the percentage of the current purity compared to the maximum does the country/IO have?||value|
|religious_influence|How much religious influence does the country/IO have?||value|
|religious_influence_percentage|How high the percentage of the current religious influence compared to the maximum does the country/IO have?||value|
|remaining_parliament_days|Checks how many days are left in the parliament of the country / international organization before it concludes. Returns -1 when there is no parliament active.||value|
|republican_tradition|How much republican_tradition does the country/IO have?||value|
|republican_tradition_percentage|How high the percentage of the current republican_tradition compared to the maximum does the country/IO have?||value|
|resolution_is_active|Is the resolution currently being debated in the scope international organization/situation?||resolution|
|righteousness|How much righteousness does the country/IO have?||value|
|righteousness_percentage|How high the percentage of the current righteousness compared to the maximum does the country/IO have?||value|
|rite_power|How much rite power does the country/IO have?||value|
|rite_power_percentage|How high the percentage of the current rite power compared to the maximum does the country/IO have?||value|
|sailors|How much Sailors does the country/IO have?||value|
|self_control|How much self control does the country/IO have?||value|
|self_control_percentage|How high the percentage of the current self control compared to the maximum does the country/IO have?||value|
|special_status_can_be_bestowed|Can the supplied special status be bestowed on the supplied country in the scope international organization?|||
|special_status_power|Get the political power of the specified country in an organization with that specified special status.|special_status_power = { country = <country> type = <special status> value <operator> <float> } or special_status_power(<country>\|<special status>)|value|
|special_status_power_fraction|Get the political power fraction of the specified country in an organization with that specified special status.|special_status_power_fraction = { country = <country> type = <special status> value <operator> <float> } or special_status_power(<country>\|<special status>)|value|
|stability|How much Stability does the country/IO have?||value|
|stability_percentage|How high the percentage of the current Stability compared to the maximum does the country/IO have?||value|
|total_enemies|counts the number of enemies of an international organization||value|
|total_locations_owned|counts the number of locations owned by an international organization||value|
|total_members|counts the number of members in an international organization||value|
|total_payment_contribution|Gets the sum all member countries have to pay for the specified IO and payment type.|total_payment_contribution = { payment = <> }|value|
|total_special_status_power|Get the political power of all countries in an organization with that specified special status.|total_special_status_power = { type = <special status> value <operator> <float> } or total_special_status_power(<special status>)|value|
|total_special_status_power_fraction|Get the percentage political power of the target special status compared to the total amount of political power of all special statuses combined.|special_status_power_fraction = { type = <special status> value <operator> <float> } or special_status_power_fraction(<special status>)|value|
|total_unique_special_status_power|Get the political power of all countries in an organization with that specified special status.|total_special_status_power = { type = <special status> value <operator> <float> } or total_special_status_power(<special status>)|value|
|tribal_cohesion|How much tribal_cohesion does the country/IO have?||value|
|tribal_cohesion_percentage|How high the percentage of the current tribal_cohesion compared to the maximum does the country/IO have?||value|
|vote_is_locked|Is a country's vote locked in the scope international organization/situation?|||
|votes_for_resolution|Checks the number of votes for a particular outcome of a resolution.|votes_for_resolution(<resolution_key>\|<thing>) or votes_for_resolution = { resolution = <resolution_key> outcome = <thing> value <comparator> <real> }|value|
|war_exhaustion|How much WarExhaustion does the country/IO have?||value|
|war_exhaustion_percentage|How high the percentage of the current WarExhaustion compared to the maximum does the country/IO have?||value|
|yanantin|How much yanantin does the country/IO have?||value|
|yanantin_percentage|How high the percentage of the current yanantin compared to the maximum does the country/IO have?||value|

### Location scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|add_static_modifier_utility|Checks the AI utility of adding a static modifier to the scoped object|add_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|value|
|adjacent_to_owned_by|is the area/location adjacent to an area with a country's presence in it?||country|
|adjacent_to_owned_or_owned_by_subject|is the area/location adjacent to an area with a country's or one of its subjects' presence in it?||country|
|average_location_literacy|Checks if a location has a certain average literacy||value|
|average_satisfaction|Checks if a location has a certain average satisfaction of its pops||value|
|border_distance_to|gets distance between borders of two nations or a location and a nation.|border_distance_to = { country = x value [operator] y } or border_distance_to(country)|value|
|building_efficiency|does the location have the specific efficiency of a building||value|
|building_type_max_level|Gets the max level for a building type in a location.|building_type_max_level = { building_type = <building type scope> [owner = <country scope>] value <operator> <compare value> }|value|
|can_become_rank|Check if a location can become the supplied location rank||location_rank|
|can_build_building|Checks if the location/country can build the specified building. Location only checks local requirements, country checks the country scope requirements.||building_type|
|climate|Checks if a location is of a specific climate|||
|culture_group_percentage|Gets the percentage of the population that follow a particular culture group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_group_population_percentage = { culture_group = <culture group> value <operator> <script_value> }|value|
|culture_group_population|Gets the absolute number of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_group_population = { culture_group = <culture group> value <operator> <script_value> }|value|
|culture_percentage|Gets the percentage of the population that follow a particular culture in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_population_percentage = { culture = <culture> value <operator> <script_value> }|value|
|culture_population|Gets the absolute number of the population that follow a particular culture in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_population = { culture = <culture> value <operator> <script_value> }|value|
|development|Checks if a location has a certain Development||value|
|disease_affects_pops_here|Checks if a disease is affecting some migrated pops here.||disease|
|disease_has_outbreak_here|Checks if a disease has an outbreak in a location or subunit.||disease|
|disease_has_stagnated|Checks if a disease has stagnated in a location or subunit.||disease|
|disease_outbreak_presence|Checks the presence of a disease in a location or subunit.|disease_outbreak_presence(<disease_outbreak>) or disease_outbreak_presence = { disease_outbreak = <disease_outbreak> value <comparator> <real> }|value|
|disease_presence|Checks the presence of a disease in a location or subunit.|disease_presence(<disease>) or disease_presence = { disease = <disease> value <comparator> <real> }|value|
|disease_resistance|Checks the resistance to a disease in a location or subunit.|disease_resistance(<disease>) or disease_resistance = { target = <disease> value <comparator> <real> }|value|
|distance_to|gets distance between locations||value|
|distance_to_area|gets distance between a location and an area||value|
|distance_to_squared|gets distance squared as the crow flies between locations (much quicker than distance_to, useful if you're just comparing)||value|
|employment_percentage|Checks if a location has a certain unemployement percentage||value|
|food_consumption|Amount of consumed food||value|
|food_production|Amount of food production||value|
|garrison_percentage|Checks the garrison percentage of the location in scope||value|
|garrison_strength|Checks the garrison strength of the location in scope||value|
|gfx_culture_applicable|Checks if a culture gfx applies to the scope object|||
|goods_output|Check how much goods the scope location produces.||value|
|has_any_convertable_pops|Check if a location has any pops that can be converted to state religion||boolean|
|has_any_disease_present|Checks if the location or subunit is affected by ANY disease active.||boolean|
|has_building|Checks if a location has a specific building||building_type|
|has_building_with_at_least_one_level|Checks if a location has a specific building and it has at least one level|||
|has_building_with_graphical_tag|Checks if a location has a building with the specified graphical tags|||
|has_building_with_graphical_tag_and_at_least_one_level|Checks if a location has a building with the specified graphical tags and at least one level|||
|has_combat|Check if a location has a combat||boolean|
|has_earthquakes|Check if a location has a Earthquakes||boolean|
|has_exports|Check if a location has a Exports||boolean|
|has_fort|Check if a location has any fort||boolean|
|has_imports|Check if a location has a imports||boolean|
|has_institution|Checks if a country has an institution||institution|
|has_latest_road_to|Check if a location has the latest available road to the target location. Latest is determined by the owner of the location and what buildable road type has the highest level.||location|
|has_location_modifier|Does the scoped province have a given modifier|has_location_modifier = name||
|has_market_construction|Is the location building a market?||boolean|
|has_owned_buildings|Has the target country got some buildings here?||country|
|has_owner|Check if a location has a Owner||boolean|
|has_privateers_from|Does the location has privateers of the target country?||country|
|has_river|Check if a location has a river||boolean|
|has_road_constructions|Check whether location has road constructions||boolean|
|has_road_of_type_to|Check if a location has a road to the target location of the specified type.|has_road_of_type_to = { target = <target location> type = <road type> }||
|has_road_to|Check if a location has a road to the target location||location|
|has_siege|Check if a location has a siege||boolean|
|has_volcano|Check if a location has a volcano||boolean|
|hemisphere|Check if a location is either in the northern or southern hemisphere.|hemisphere = northern/southern||
|in_zone_of_control|Check if a location is in the zone of control of a friendly fort||boolean|
|integration_level|Checks the integration level of a location|||
|integration_progress|Checks the integration progress of a location||value|
|intrinsic_disease_resistance|Checks the intrinsic disease resistance in a location (e.g. from buildings)||value|
|is_adjacent_to_lake|Check if a location is a adjacent to a lake||boolean|
|is_border|Check if a location borders another country||boolean|
|is_burgher_positive_deficit|Checks if a building location does not have negative burgher deficit||boolean|
|is_capital|Check if a location is a capital||boolean|
|is_city|Check if a location is a city||boolean|
|is_coastal|Check if a location is coastal||boolean|
|is_connected_to|Check if a location is connected by land/strait to another location in the same country||location|
|is_core_of|Is the location a core of the target country?||country|
|is_currently_being_integrated|Check if a location is currently being integrated||boolean|
|is_discovered_by|Is the scope location/country discovered by the target country?||country|
|is_east_of|Check if a location is east of another location||location|
|is_full_expanded_rgo|Check if a location has its RGO fully expanded||boolean|
|is_in_scripted_geography|Checks if the scope is part of the scripted geography on RHS scope|is_in_scripted_geography = <scripted geography scope>|scripted_geography|
|is_labourer_positive_deficit|Checks if a building location does not have negative labourer deficit||boolean|
|is_land|Check if a location is land||boolean|
|is_location_holy_site_for|Is the location a holy site for the target religion?||religion|
|is_looted|Check if a location is looted||boolean|
|is_market_center|Check if a location is a market center||boolean|
|is_mining_rgo|Check if a location has a mining_rgo||boolean|
|is_neighbor_of|Is the country or location a Neighbor to the specified country?||country|
|is_neighbor_of_international_organization|Is the country or location a neighbor to the specified international organization?||international_organization|
|is_neighbor_of_location|Check if a location is neighbour to another||location|
|is_neighbor_of_location_or_across_one_seazone|Check if a location is neighbour to another or just across a single seazone||location|
|is_overseas_for_owner|Check if a location or province is overseas for owber||boolean|
|is_ownable|Check if a location is ownable, i.e. not sea, lake or an impassable||boolean|
|is_owned_by_any_international_organization|Check if a location is owned by any international organization||boolean|
|is_owned_by_international_organization|Check if a location is owned by an international organization||international_organization|
|is_owned_or_owned_by_subjects_of|Check if the location is owned by the target country or its subjects||country|
|is_owned_or_owned_by_subjects_or_below_of|Check if the location is owned by the target country or its subjects or the subjects' subject||country|
|is_passable|Check if a location is passable||boolean|
|is_port|Check if a location has a port||boolean|
|is_produced_in_location_market|Checks if a specific goods in produced in the location market||goods|
|is_province_capital|Check if a location is the province capital||boolean|
|is_required_for_formable|Check if the location scope is required by the formable||formable_country|
|is_unified_culture|Check if a location has culture unified with the owner||boolean|
|local_control|Checks if a location has a certain control||value|
|local_cultural_unity|Checks the percentage the dominant-culture has in a location||value|
|local_estate_power|Checks the raw local estate power in location||value|
|local_political_power_fraction|Checks the fraction this location has of the total political power of a country||value|
|local_relative_estate_power|Checks the relative local estate power in location||value|
|local_religious_unity|Checks the percentage the dominant-religion has in a location||value|
|location_art_quality|Checks the total art quality in a location||value|
|location_building_level|Checks if a location has a building type at a certain level (with optional owner)||value|
|location_key|Checks if a location is the specific one (from named_location)|||
|location_maritime_merchant_power|gets the maritime merchant power for a country in the scope location||value|
|location_maritime_presence_power|gets the maritime presence power for a country in the scope location.|location_maritime_presence_power = { country = <country scope> value <operator> <number> }|value|
|location_max_population|Checks if a location has a certain pixel count||value|
|location_max_winter_level|Checks the maximum winter level of a location|||
|location_modifier_strength|Does the scoped location have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|location_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "location_modifier_strength(<modifier key>)"||
|location_net_building_profit|Checks the net profit from buildings in a location||value|
|location_num_holy_sites|Number of holy sites in the location||value|
|location_num_works_of_art|Checks if a location has a certain number of works of art||value|
|location_peace_cost|gets the peace cost for the location according to giver and taker countries|usage in trigger: location_peace_cost = { giver = <country> taker = <country> value <operand> <threshold> #ex: value < 10 } usage in scripted value: location_peace_cost(<giver>\|<taker>)|value|
|location_population_percentage|Checks if a location has a certain percentage of population capacity||value|
|location_privateer_power|gets the maritime privateeer power for a country in the scope location||value|
|location_size|Checks if a location has a certain pixel count||value|
|location_tax_base|Checks the tax-base of a location||value|
|location_unemployed_population_for_building_type|Checks if a location has a certain unemployed population for the supplied building type (with optional owner)||value|
|location_within_range|Checks if a location has a certain population within range||country|
|location_works_of_art_star_rating|Checks if a country has a certain amount of work of arts||value|
|market_access|Checks if a location has certain market access||value|
|max_control|Checks the max control in a location||value|
|max_garrison_strength|Checks the max garrison strength of the location in scope||value|
|max_rgo_workers|Checks if a location has a certain max number of RGO workers||value|
|migration_attraction|Checks if a location has a certain migration_attraction||value|
|modifier_utility|Checks the AI utility of a modifier||value|
|modifier_utility_include_locations|Checks the AI utility of a modifier with location checks||value|
|monthly_conversion|Checks if a location has an potential conversion of X per month||value|
|num_army_constructions|Check how many army_constructions a location has||value|
|num_buildings|Checks if a location has a certain amount of buildings||value|
|num_civil_constructions|Check how many civil_constructions a location has||value|
|num_foreign_buildings|Checks if a location has a certain amount of foreign buildings||value|
|num_navy_constructions|Check how many navy_constructions a location has||value|
|num_owned_foreign_buildings_in_location|The number of foreign buildings in a location owned by a count||value|
|num_roads|Check how many roads a location has||value|
|peasant_enfranchisment|Checks the level of peasant enfranchisement in a location||value|
|population|Checks if the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography has a certain population||value|
|population_with_traits|Checks if the location has x amount of population with specific pop traits.|population_with_traits = { limit = { <pop triggers> } OR scripted_trigger = <scripted trigger key> value = <script_value> } or population_with_traits(<scripted trigger key>)|pop|
|prosperity|Checks if a location has a certain prosperity||value|
|proximity|Checks the proximity to owner capital in a location||value|
|rank_index|Checks if a location has a Location Rank of a certain index||value|
|raw_material_output|Check how much raw material the scope location produces.||value|
|relative_raw_material_price|Checks the price of a location's raw material in its market as a percentage of the base price of that material||value|
|religion_group_percentage|Gets the percentage of the population that follow a particular religion group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_group_population_percentage = { religion_group = <religion group> value <operator> <script_value> }|value|
|religion_group_population|Gets the absolute number of the population that follow a particular religion group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_group_population = { religion_group = <religion group> value <operator> <script_value> }|value|
|religion_percentage|Gets the percentage of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_population_percentage = { religion = <religion> value <operator> <script_value> }|value|
|religion_population|Gets the absolute number of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_population = { religion = <religion> value <operator> <script_value> }|value|
|remove_static_modifier_utility|Checks the AI utility of removing a static modifier from the scoped object|remove_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|value|
|rgo_workers|Checks if a location has a certain number of RGO workers||value|
|topography|Checks if a location is of a specific Topography type|||
|total_building_levels|Checks if a location has a certain total amount of building levels||value|
|vegetation|Checks if a location is of a specific Vegetation type|||
|winter_level|winter level check|||
|winter_power|||value|
|within_colonial_range_of|Is the location within Colonial range of the target country?||country|
|within_naval_range_of|Is the location within naval range of the target country?||country|

### Market scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|available_merchant_capacity|gets the market available merchant capacity for a country in the scope market||value|
|demands_goods|Check if the market scope has a demand for the target goods.||goods|
|demands_goods_by_pops|Check if the market has any pop demand for the target goods.||goods|
|food_price|Checks how much the food in the current market costs||value|
|goods_demand_in_market|Checks how much demand exists of a good in the market.|goods_demand_in_market = { goods = <goods> value = <script_value> } or goods_demand_in_market(<goods>)|value|
|goods_supply_in_market|Checks how much supply exists of a good in the market.|goods_supply_in_market = { goods = <goods> value = <script_value> } or goods_supply_in_market(<goods>)|value|
|has_merchant|checks if the market has a merchant of the specific country.||country|
|has_merchant_power|does the market have a merchant power for?|has_merchant_power = { country = country key = key }||
|has_new_world_goods_in_market|Checks if a market has a supply of any new-world goods||boolean|
|has_temporary_demand|Checks if a market has a certain temporary demand||demand|
|has_temporary_demands|Checks if a market has a certain temporary demand||boolean|
|in_trade_range_of|Is the market within trading range of a merchant the target country?||country|
|is_export_banned|Checks if export of specific goods is banned in this market||goods|
|is_import_banned|Checks if import of specific goods is banned in this market||goods|
|is_produced_in_market|Checks if a specific goods in produced in this market||goods|
|is_projected_to_run_out_of_food_stockpile|Checks if a market is projected to run out of food||boolean|
|is_traded_in_market|Checks if a specific goods in traded in this market||goods|
|market_food|Checks how much food is in the market stockpile||value|
|market_food_deficit|Checks how much food is missing in the market||value|
|market_food_percentage|Checks how much food is in the market stockpile percentage wise||value|
|market_food_traded|Checks how much food is traded in the market||value|
|market_max_food|Checks how much food can be stockpiled in the market||value|
|market_monthly_food_balance|Checks what the food balance is in the market||value|
|market_population|Checks how many pops are in the market||value|
|market_possible_goods_trade_surplus|gets the possible trade surplus for the goods in the scope market||value|
|merchant_capacity|gets the market merchant capacity for a country in the scope market||value|
|merchant_power_in_market|gets the market merchant power for a country in the scope market||value|
|raw_material_amount|Check how many locations in the province_defintion/area / region/subcontinent/continent produce the specified raw material.|raw_material_amount = { goods = <goods scope> value = <script_value> } or raw_material_amount(<goods scope>)|value|
|total_goods_traded|Check the total amount of goods that went through this market last month||value|
|total_goods_value_traded|Check the total value of goods that went through this market last month||value|
|total_merchant_power|Check the level of this Building?||value|
|used_merchant_capacity|gets the market used merchant capacity for a country in the scope market||value|

### Pop scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|gfx_culture_applicable|Checks if a culture gfx applies to the scope object|||
|has_rebel|Check if a pop has allegiance to a rebel||boolean|
|is_linked_to_foreign_building|Check if a pop is linked to a foreign building||boolean|
|is_upper_class|Check if a pop is upper class or not||boolean|
|pop_character_chance|How likely are characters to spawn from this pop?||value|
|pop_knows_about_goods|Checks if a pop knows about a goods enough to demand it||goods|
|pop_literacy|How literate is this pop?||value|
|pop_satisfaction|How satisfied is this pop?||value|
|pop_size|How big is this pop?||value|

### War scope

|Trigger|Description|Example|Targets|
|---|---|---|---|
|can_join_as_attacker|Can the target country join the war in scope as attacker ?||country|
|can_join_as_defender|Can the target country join the war in scope as defender ?||country|
|has_casus_belli|Checks if that war has a CB specified at all||boolean|
|is_a_defender|Is the target country a defender in the war?||country|
|is_an_attacker|Is the target country an attacker in the war?||country|
|is_civil_war_for|Is the current war a civil war for the target country?||country|
|is_in_war|Is the target country in the war?||country|
|is_no_cb_war|Checks if that war was started without any casus belli ('no cb')||boolean|
|is_on_opposite_sides|Check if the two countries are in opposing sides.|is_on_opposite_sides = { country = <country> target = <target> }||
|is_on_same_side|Check if the two countries are on the same side.|is_on_same_side = { country = <country> target = <target> }||
|join_war_reason|Checks the reason for a country joining a war.|||
|war_goal_type|Check if the war goal type of the war is the specified type.|||
|war_length|Checks how many months the current war has been going.||value|
|war_length_in_years|Checks how many years the current war has been going.||value|
|war_score_of_country|Check how much war score the target country has in the current war.|war_score_of_country = { country = <country> value <operator> <real> } or war_score_of_country(<country>)|value|
|war_score_of_country_side|Check how much war score the war side of the target country has in the current war.|war_score_of_country_side = { country = <country> value <operator> <real> } or war_score_of_country_side(<country>)|value|
|war_stalling_length|Checks how many months with no action have passed in the current war.||value|
|war_stalling_length_in_years|Checks how many years with no action have passed in the current war.||value|

## All triggers

Use this table to search for all triggers.

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|active_religious_focus|Checks if a country is researching a certain religious focus||country||
|add_estate_satisfaction_utility|Utility of adding however much estate satisfaction to the country|add_estate_satisfaction_utility(<estate>\|<amount>) or add_estate_satisfaction_utility = { type = <estate type> amount = <amount> value <operator><threshold> }|country|value|
|add_static_modifier_utility|Checks the AI utility of adding a static modifier to the scoped object|add_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|character, country, location|value|
|add_to_temporary_list|Saves a temporary target for use during the trigger execution|This is used to build lists in triggers. If used within an any-trigger, placement within the trigger is quite important. The game will iterate through every instance of the any-trigger until it finds a single instance that fulfills the requirements, and then it will stop. In order to add every instance of a scope that fulfills certain conditions, use "count = all" while also placing this "effect" at the very end of the any-trigger (so that every condition is evaluated for every iteration).|none||
|adjacent_to_owned_by|is the area/location adjacent to an area with a country's presence in it?||area, location|country|
|adjacent_to_owned_or_owned_by_subject|is the area/location adjacent to an area with a country's or one of its subjects' presence in it?||area, location|country|
|adm|The adm ability of the character||character|value|
|advance_no_longer_activated|Checks if a country has researched a certain advance but it's not useable at the moment because of conditions||country||
|age_in_days|How old is a character???||character|value|
|age_in_years|How old is a character???||character|value|
|age_preference|checks a countries age preference for current age||country||
|agenda_for_estate_type|Check if the parliament agenda can be available for the specified estate type||parliament_agenda|estate_type|
|agenda_for_special_status|Check if the parliament agenda can be available for the specified special status||parliament_agenda|estate_type|
|ai_issue_voting_bias|gets the AI evaluation score for voting bias from the international organization||none|value|
|ai_parliament_issue_resolution_vote_bias|gets the AI evaluation score for resolution voting bias from the parliament issue||parliament_issue|value|
|ai_policy_reason_to_join|Gets the AI evaluation score for joining an IO due to its policies|ai_policy_reason_to_join = { actor = <country scope> international_organization = <international organization scope> value = <script_value> } OR ai_policy_reason_to_join(<country scope>\|<international organization scope>) = <script_value>|policy|value|
|ai_policy_resolution_keep_bias|Gets the AI evaluation score for keeping the policy in a vote|ai_policy_resolution_keep_bias = { actor = <country scope> international_organization = <international organization scope> value = <script_value> } OR ai_policy_resolution_keep_bias(<country scope>\|<international organization scope>) = <script_value>|policy|value|
|ai_policy_resolution_propose_bias|gets the AI evaluation score for proposing the policy in a vote||policy|value|
|ai_policy_resolution_vote_bias|gets the AI evaluation score for resolution voting bias from the policy||policy|value|
|ai_unlock_unit_score|Returns the score for AI to unlock a unit||country|value|
|ai_wants_convert|religion is one AI wants||religion|boolean|
|ai_will_do|gets the AI evaluation score of the supplied generic action ofr the supplied country||none|value|
|all_false|true if all children are false (equivalent to NOR)||none||
|allows_female_rulers|country allows female rulers||country|boolean|
|allows_male_rulers|country allows male rulers||country|boolean|
|always|checks if the assigned yes/no value is true|always = yes # always succeeds always = no # always fails always = scope:a_boolean_value # evaluated at runtime|none|boolean|
|always_loyal|if estate type is crown||estate_type|boolean|
|and|all inside trigger must be true||none||
|annexation_cost|How much does the target country cost for the current country to annex?|annexation_cost = { target = <target country> value = <script_value> } or annexation_cost(<target country>)|country|value|
|antagonism|is the country's antagonism towards the target greater or equal than the value?|antagonism = { target = X value <operator> Y or value = { min max } }|country|value|
|any_accepted_culture|Iterate through all accepted cultures in a country|any_accepted_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_active_disaster|Iterate through all active disasters for a country|any_active_disaster = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|disaster|
|any_active_estate|Iterate through all active estates (non-crown)|any_active_estate = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|estate_type|
|any_active_resolution|Iterate through all currently active resolutions in an international organization or situation|any_active_resolution = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization, situation|active_resolution|
|any_adjacent_ports_to_area|Iterate through all adjacent ports of an seazone area|any_adjacent_ports_to_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|location|
|any_advance_definition|Iterate through all advance definitions|any_advance_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|advance_type|
|any_allowed_estate_in_heir_selection|Iterate through all allowed estates a HeirSelection has|any_allowed_estate_in_heir_selection = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|heir_selection|estate_type|
|any_ancestor|Iterate through all ancestors (parents, grandparents etc) of a character|any_ancestor = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_area|Iterate through all existing areas|any_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|area|
|any_area_in_region|Iterate through all areas in a region|any_area_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|area|
|any_area_in_scripted_geography|Iterate through all areas in a scripted geography|any_area_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|area|
|any_area_with_core|Iterate through all areas with cored locations in a country|any_area_with_core = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|area|
|any_area_with_owned_province|Iterate through all areas with owned provinces in a country|any_area_with_owned_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|area|
|any_army|Iterate through all armies in a country|any_army = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|unit|
|any_artist|Iterate through all artists in a country|any_artist = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_attacker|Iterate through all attackers of a war|any_attacker = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|war|country|
|any_avatar_for_god|Iterate through all Avatars of a God|any_avatar_for_god = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|god|avatar|
|any_besieging_units|Iterate through all units participating in a siege|any_besieging_units = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|siege|unit|
|any_border_location|Iterate through all owned location in a country which border locations not owned by the current country scope.|any_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_buildable_building_type|Iterate through all the building types a country can build|any_buildable_building_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|building_type|
|any_building_type|Iterate through all the building types|any_building_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|building_type|
|any_buildings_in_location|Iterate through all buildings in a location|any_buildings_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|building|
|any_cabinet|Iterate through all actions in a country's cabinet|any_cabinet = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|cabinet|
|any_cabinet_action|Iterate through all actions in a country's cabinet actions|any_cabinet_action = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|cabinet_action|
|any_cabinet_character|Iterate through all characters in a country that is in the cabinet|any_cabinet_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_cardinal_in_country|Iterate through all Cardinals in a country|any_cardinal_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|cardinal|
|any_cardinal_in_religion|Iterate through all Cardinals in a Religion|any_cardinal_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|cardinal|
|any_casus_belli_on_us|Iterate through all countries have a casus belli on us|any_casus_belli_on_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_casus_belli_target|Iterate through all countries we have a casus belli on|any_casus_belli_target = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_center|Iterate through all subunits on the center of a combat-side|any_center = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_character|Iterate through all characters in a country|any_character = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_character_in_dynasty|Iterate through all living characters in a Dynasty|any_character_in_dynasty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|dynasty|character|
|any_character_supporting_rebel|Iterate through all characters supporting a rebel|any_character_supporting_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|rebels|character|
|any_child|Iterate through all children of a character|any_child = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_close_relative|Iterate through all close relatives of a character|any_close_relative = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_coast_border_location|Iterate through all bordering, or across one seazone of a location|any_coast_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_colonial_charter|Iterate through all colonial charters in a country|any_colonial_charter = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|colonial_charter|
|any_colonial_claim_province_definition|Iterate through all province definitions with colonial claims from the scope country.|any_colonial_claim_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|province_definition|
|any_colonial_country|Iterate through all colonial countries in the world|any_colonial_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_colonial_overlord|Iterate through all colonial overlord countries in the world|any_colonial_overlord = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_colonial_top_overlord|Iterate through all countries in the world that have a colonial country among their subjects or their subjects subjects and so on|any_colonial_top_overlord = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_connected_location|Iterate through all locations in the same country as the scope location that are connected by land or strait|any_connected_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_construction_material_for_building_type|Iterate through all goods required to construct a building type|any_construction_material_for_building_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|building_type|goods|
|any_continent|Iterate through all existing continents|any_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|continent|
|any_continent_in_scripted_geography|Iterate through all continents in a scripted geography|any_continent_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|continent|
|any_controlled_location|Iterate through all controlled location in a country|any_controlled_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_core_in_location|Iterate through all cores in a location|any_core_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|country|
|any_core_location|Iterate through all core locations in a country|any_core_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_country|Iterate through all existing countries|any_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_country_annexing_us|Iterate through all countries which are currently annexing the current country scope.|any_country_annexing_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_at_war_with|Iterate through all countries at war with|any_country_at_war_with = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_in_culture|Iterate through all countries with this primary culture|any_country_in_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture|country|
|any_country_in_culture_group|Iterate through all countries in a culture group.|any_country_in_culture_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture_group|country|
|any_country_in_diplomatic_range|Iterate through all countries in diplomatic range|any_country_in_diplomatic_range = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_in_dynasty|Iterate through all countries in a Dynasty|any_country_in_dynasty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|dynasty|country|
|any_country_in_hierarchy|Iterate through every country in the entire overlord/subject hierarchy, from the independent top overlord to the deepest subjects|any_country_in_hierarchy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_in_religion|Iterate through all countries in a religion|any_country_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|country|
|any_country_in_religion_group|Iterate through all countries in a religion group.|any_country_in_religion_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|group|country|
|any_country_in_religious_school|Iterate through all countries within a school|any_country_in_religious_school = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religious_school|country|
|any_country_lent_to|Iterate through all countries a country has lent to|any_country_lent_to = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_of_country_type|Iterate through all countries of the specified type.|any_country_of_country_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_country_sub_unit|Iterate through all subunits in all units in a country|any_country_sub_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|sub_unit|
|any_country_supporting_rebel|Iterate through all countries supporting a rebel|any_country_supporting_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|rebels|country|
|any_country_that_can_be_called_defensively|Iterate through all countries that may be called into a defensive war.|any_country_that_can_be_called_defensively = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_that_can_be_called_offensively|Iterate through all countries that may be called into an offensive war.|any_country_that_can_be_called_offensively = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_together_in_war_with|Iterate through all countries which are an ally in any of the country scope's wars|any_country_together_in_war_with = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_we_are_annexing|Iterate through all countries which are currently annexed by the current country scope.|any_country_we_are_annexing = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_with_capital_in_geography|Iterate through all countries which have their capital in the specified geography|any_country_with_capital_in_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|any_country_with_cardinals|Iterate through all countries with cardinals in a religion|any_country_with_cardinals = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|country|
|any_country_with_coalition_grade_antagonism_against_us|Iterate through all countries who have coalition grade antagonism against us|any_country_with_coalition_grade_antagonism_against_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_with_relation_that_can_be_annulled|Iterate through all countries which have an annullable relation with the scope country.|any_country_with_relation_that_can_be_annulled = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_country_with_special_status_of_type|Iterate through all countries in the international organization which have the specified special status|any_country_with_special_status_of_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_country_with_succession_law|Iterate through all countries with a cached succession law (set cached = yes in the heir_selection to use this)|any_country_with_succession_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_culture|Iterate through all cultures|any_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|culture|
|any_culture_group|Iterate through all culture groups the culture is in.|any_culture_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture|culture_group|
|any_culture_in_culture_group|Iterate through all cultures in a culture group.|any_culture_in_culture_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture_group|culture|
|any_current_avatars|Iterate through all Avatars a country has|any_current_avatars = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|avatar|
|any_current_gods|Iterate through all Gods a country worships|any_current_gods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|god|
|any_current_law|Iterate through all laws of a country.|any_current_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|law|
|any_current_law_in_international_organization|Iterate through all laws that are codified in the international organization|any_current_law_in_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|law|
|any_current_policy|Iterate through all policies that are codified in the country|any_current_policy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|policy|
|any_current_policy_in_international_organization|Iterate through all policies that are codified in the international organization|any_current_policy_in_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|policy|
|any_current_reforms|Iterate through all Government Reforms a country has|any_current_reforms = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|government_reform|
|any_current_war|Iterate through all wars of a country|any_current_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|war|
|any_defender|Iterate through all defenders of a war|any_defender = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|war|country|
|any_descendant|Iterate through all descendants (children, grandchildren etc) of a character|any_descendant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_disloyal_subject|Iterate through all loyal subject countries|any_disloyal_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_dynasty|Iterate through all dynasties in a country|any_dynasty = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|dynasty|
|any_east_of_province_definition|Iterate through all province-definitions east of a province-definition|any_east_of_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province_definition|
|any_election_candidates|Iterate through all election candidates of a country with elections!|any_election_candidates = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_enemy|Iterate through all Enemy countries|any_enemy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_enemy_war_leader|Iterate through all countries which are leading a war against the scope|any_enemy_war_leader = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_estate|Iterate through all estates in a country|any_estate = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|estate|
|any_estate_privilege|Iterate through all current estate privileges of a Country|any_estate_privilege = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|estate_privilege|
|any_estate_type_preferring|Iterate through all estate types that a prefer a policy|any_estate_type_preferring = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|policy|estate_type|
|any_exploration_from_country|Iterate through all Explorations a country has|any_exploration_from_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|exploration|
|any_export|Iterate through all exports in a market|any_export = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|trade|
|any_export_from_location|Iterate through all exports from location|any_export_from_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_false|true if any child is false (equivalent to NAND)||none||
|any_food_goods|Iterate through all food-goods|any_food_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|any_foreign_building_countries_in_location|Iterate through all foreign building countries in a location|any_foreign_building_countries_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|country|
|any_foreign_buildings_in_location|Iterate through all foreign buildings in a location|any_foreign_buildings_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|building|
|any_fort_in_country|Iterate through all Forts in a country|any_fort_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_friendly_coast_border_location|Iterate through all friendly bordering, or across one seazone of a location|any_friendly_coast_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_friendly_country|Iterate through all countries with relations marked as friendly|any_friendly_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_friendly_or_high_opinion_country|Iterate through all countries with relations marked as friendly or that we have a high opinion of set in defines|any_friendly_or_high_opinion_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_friendly_to_friendly_country|Iterate through all friends of our friends|any_friendly_to_friendly_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_friendly_to_hostile_country|Iterate through all friends of our enemies|any_friendly_to_hostile_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_god_in_religion|Iterate through all Gods in a Religion|any_god_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|god|
|any_good_in_demand|Iterate through all goods in a goods demand|any_good_in_demand = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|demand|goods|
|any_goods|Iterate through all types of goods|any_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|any_graphical_culture_in_culture|Iterate through all graphical culture in a culture|any_graphical_culture_in_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|culture|graphical_culture|
|any_great_power|Iterate through all great powers|any_great_power = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_heathen_location|Iterate through all heathen locations in a country|any_heathen_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_heretic_location|Iterate through all Heretic locations in a country|any_heretic_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_hired_mercenary|Iterate through mercenaries a country has hired|any_hired_mercenary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|mercenary|
|any_historical_enemy|Iterate through all historical Enemy countries|any_historical_enemy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_historical_rival|Iterate through all historical rival countries|any_historical_rival = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_holy_site_in_country|Iterate through all Holy Sites in a country|any_holy_site_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|holy_site|
|any_holy_site_in_religion|Iterate through all Holy Sites in a Religion|any_holy_site_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|holy_site|
|any_hostile_country|Iterate through all countries with relations marked as hostile|any_hostile_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_hostile_or_low_opinion_country|Iterate through all countries with relations marked as hostile or that we have a low opinion of set in defines|any_hostile_or_low_opinion_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_hostile_to_friendly_country|Iterate through all enemies of our friends|any_hostile_to_friendly_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_hostile_to_hostile_country|Iterate through all enemies of our enemies|any_hostile_to_hostile_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_import|Iterate through all imports in a market|any_import = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|trade|
|any_import_from_location|Iterate through all Imports from location|any_import_from_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_in_global_list|Iterate through all items in global list.|any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_list|Iterate through all items in list.|any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_local_list|Iterate through all items in local list.|any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_institutions_embraced|Iterate through all institutions a country has embraced|any_institutions_embraced = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|institution|
|any_international_organization|Iterate through all international organizations|any_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|international_organization|
|any_international_organization_elector|Iterate through all countries with an elector special status in the international organization|any_international_organization_elector = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_enemy|Iterate through all countries that are enemies of the international organization|any_international_organization_enemy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_member|Iterate through all countries that are members of the international organization|any_international_organization_member = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_owned_location|Iterate through all locations that are owned by the international organization|any_international_organization_owned_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|location|
|any_international_organization_owner|Iterate through all international organizations which own the location scope|any_international_organization_owner = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|international_organization|
|any_international_organization_parliament_opposers|Iterate through all countries that have voted AGAINST the parliament issue in the in the parliament of the international organization and support the current debate|any_international_organization_parliament_opposers = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organization_parliament_supporter|Iterate through all countries that have voted FOR the parliament issue in the parliament of the international organization and support the current debate|any_international_organization_parliament_supporter = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|international_organization|country|
|any_international_organizations_member_of|Iterate through all international organizations a country is a member of|any_international_organizations_member_of = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|international_organization|
|any_international_organizations_target_of|Iterate through all international organizations a country is a target of|any_international_organizations_target_of = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|international_organization|
|any_invited_religious_figure|Iterate through all invited religious figures in a Country|any_invited_religious_figure = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_key_in_global_variable_map|Iterate through all items in global variable map.|any_key_in_global_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_local_variable_map|Iterate through all items in local variable map.|any_key_in_local_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_variable_map|Iterate through all items in variable map.|any_key_in_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_known_country|Iterate through all known countries|any_known_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_known_institution|Iterate through all institutions a country knows of|any_known_institution = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|institution|
|any_left_flank|Iterate through all subunits on the left-flank of a combat-side|any_left_flank = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_lent_loan|Iterate through all loans that a country lent|any_lent_loan = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|loan|
|any_loan|Iterate through all loans in a country|any_loan = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|loan|
|any_loan_lent_to_country|Iterate through all loans a country has lent to the supplied borrower country|any_loan_lent_to_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|loan|
|any_location_in_area|Iterate through all Locations in a area|any_location_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|location|
|any_location_in_continent|Iterate through all Locations in a continent|any_location_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|continent|location|
|any_location_in_market|Iterate through all locations in a market|any_location_in_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|location|
|any_location_in_province|Iterate through all Locations in a province|any_location_in_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province|location|
|any_location_in_province_definition|Iterate through all Locations in a province definition|any_location_in_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|location|
|any_location_in_region|Iterate through all Locations in a region|any_location_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|location|
|any_location_in_scripted_geography|Iterate through all Locations in a scripted geography|any_location_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|location|
|any_location_in_sub_continent|Iterate through all Locations in a sub-continent|any_location_in_sub_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|sub_continent|location|
|any_location_in_the_world|Iterate through all location|any_location_in_the_world = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|location|
|any_loyal_subject|Iterate through all loyal subject countries|any_loyal_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_maritime_area|Iterate through all maritime areas for a country|any_maritime_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|area|
|any_market_center_in_country|Iterate through all markets in a country which market centers are owned by the country|any_market_center_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|market|
|any_market_in_world|Iterate through all markets in the world|any_market_in_world = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|market|
|any_market_present_in_country|Iterate through all markets in a country|any_market_present_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|market|
|any_market_with_merchants|Iterate through all markets a country has active merchants|any_market_with_merchants = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|market|
|any_mercenary|Iterate through all mercenaries in the world|any_mercenary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|mercenary|
|any_mercenary_sub_unit|Iterate through all subunits in a Mercenary|any_mercenary_sub_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|mercenary|sub_unit|
|any_merchant_in_market|Iterate through all merchants in a market|any_merchant_in_market = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|market|country|
|any_navy|Iterate through all navies in a country|any_navy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|unit|
|any_neighbor_area|Iterate through all neighboring areas in a area|any_neighbor_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|area|
|any_neighbor_country|Iterate through all neighbour countries|any_neighbor_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_neighbor_location|Iterate through all neighbors of a location|any_neighbor_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|location|
|any_neighbor_province_definition|Iterate through all neighboring ProvinceDefinitions in a ProvinceDefinition|any_neighbor_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province_definition|
|any_new_world_goods|Iterate through all new-world goods|any_new_world_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|any_nomad_countries_in_location|Iterate through all nomad pop countries in a location|any_nomad_countries_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|country|
|any_non_state_religion_location|Iterate through all NonStateReligion locations in a country|any_non_state_religion_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_old_world_goods|Iterate through all old-world goods|any_old_world_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|goods|
|any_other_core_country|Iterate through all other countries which have a core on the current country|any_other_core_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_other_country|Iterate through all other countries|any_other_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_other_great_power|Iterate through all other great powers|any_other_great_power = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_other_religion_in_same_group|Iterate through all other religions that has the same group as Religion|any_other_religion_in_same_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|religion|
|any_other_revolutionary|Iterate through all other revolutionary countries|any_other_revolutionary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_overlord_or_above|Iterate through your overlord, your overlord's overlord, and so on|any_overlord_or_above = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_ownable_location|Iterate through all ownable location|any_ownable_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|location|
|any_ownable_location_in_area|Iterate through all ownable Locations in an area|any_ownable_location_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|location|
|any_ownable_location_in_continent|Iterate through all ownable Locations in a continent|any_ownable_location_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|continent|location|
|any_ownable_location_in_province_definition|Iterate through all ownable Locations in a province definition|any_ownable_location_in_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|location|
|any_ownable_location_in_region|Iterate through all ownable Locations in a region|any_ownable_location_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|location|
|any_ownable_location_in_scripted_geography|Iterate through all ownable Locations in a scripted geography|any_ownable_location_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|location|
|any_ownable_location_in_sub_continent|Iterate through all ownable Locations in a sub continent|any_ownable_location_in_sub_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|sub_continent|location|
|any_owned_building|Iterate through all the owned buildings in a country|any_owned_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|building|
|any_owned_foreign_building|Iterate through all the owned foreign buildings in a country|any_owned_foreign_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|building|
|any_owned_foreign_building_location|Iterate through all the location of owned foreign buildings in a country|any_owned_foreign_building_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owned_foreign_building_region|Iterate through all the regions of owned foreign buildings in a country|any_owned_foreign_building_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|region|
|any_owned_location|Iterate through all owned location in a country|any_owned_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owned_nomad_pop|Iterate through all owned nomad pops in a country|any_owned_nomad_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|pop|
|any_owned_non_rural_location|Iterate through all owned non-rural locations in a country|any_owned_non_rural_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owned_rural_location|Iterate through all owned rural locations in a country|any_owned_rural_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_owner_in_region|Iterate through all the countries that own locations in a region|any_owner_in_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|region|country|
|any_parent|Iterate through parents (order: father, mother) of a character.|any_parent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_participating_countries|Iterate through all Countrys participating in 1 side of a combat|any_participating_countries = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|country|
|any_participating_units|Iterate through all units participating in 1 side of a combat|any_participating_units = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|unit|
|any_past_liturgical_dialect|Iterate through all liturgical dialects a country has had before|any_past_liturgical_dialect = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_policy_in_law|Iterate through all policies that are part of the law scope|any_policy_in_law = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|law|policy|
|any_political_border_location|Iterate through all owned location in a country which border another country.|any_political_border_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_pop|Iterate through all pops in a location or country|any_pop = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country, location|pop|
|any_pops_supporting_rebel|Iterate through all pops supporting a rebel|any_pops_supporting_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|rebels|pop|
|any_port_in_country|Iterate through all Ports in a country|any_port_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_possible_disaster|Iterate through all possible disasters for a country|any_possible_disaster = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|disaster|
|any_possible_parliament_issue|Iterate through all possible parliament issues in a country's or an international organization's parliament|any_possible_parliament_issue = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country, international_organization|parliament_issue|
|any_possible_policy|Iterate through all possible policies of a Country that is not currently implemeted|any_possible_policy = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|policy|
|any_possible_privilege|Iterate through all possible & allowed estate privileges of a Country that is not currently implemeted|any_possible_privilege = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|estate|estate_privilege|
|any_possible_recruit_location|Iterate through all possible recruit locations in a country|any_possible_recruit_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_present_country|Iterate through all countries in the specified geography|any_present_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|any_present_culture_in_country|Iterate through all cultures present in the country.|any_present_culture_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_present_culture_in_location|Iterate through all cultures present in the location.|any_present_culture_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|culture|
|any_present_overlord|Iterate through all countries which have a subject in the specified geography|any_present_overlord = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|any_present_religion_in_country|Iterate through all religions present in the country.|any_present_religion_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|religion|
|any_present_religion_in_location|Iterate through all religions present in the location.|any_present_religion_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|religion|
|any_primary_or_accepted_culture|Iterate through primary culture and all accepted cultures in a country. Primary is ordered first.|any_primary_or_accepted_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_primary_or_accepted_or_tolerated_culture|Iterate through primary culture and all accepted and all tolerated cultures in a country. Primary is ordered first.|any_primary_or_accepted_or_tolerated_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_privateer|Iterate through all privateers in the world|any_privateer = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|privateer|
|any_privateer_from_country|Iterate through all privateers a country has|any_privateer_from_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|privateer|
|any_privateer_in_area|Iterate through all privateers in a area|any_privateer_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|privateer|
|any_production_method|Iterate through all types of production methods.|any_production_method = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|production_method|
|any_production_method_of_building|Iterate through all available production methods of the building.|any_production_method_of_building = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|building|production_method|
|any_province|Iterate through all provinces in a country|any_province = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|province|
|any_province_definition|Iterate through all existing province_definition|any_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|province_definition|
|any_province_definition_in_area|Iterate through all province-definitions in an area|any_province_definition_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|province_definition|
|any_province_definition_in_scripted_geography|Iterate through all province-definitions in a scripted geography|any_province_definition_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|province_definition|
|any_province_in_area|Iterate through all provinces in an area|any_province_in_area = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|area|province|
|any_province_in_province_definition|Iterate through all provinces in a province-definition|any_province_in_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province|
|any_rebel|Iterate through all Rebels in a country|any_rebel = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|rebels|
|any_region|Iterate through all existing regions|any_region = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|region|
|any_region_in_continent|Iterate through all regions in a sub-continent|any_region_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|sub_continent|region|
|any_region_in_scripted_geography|Iterate through all regions in a scripted geography|any_region_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|region|
|any_related_country|Iterate through all related countries|any_related_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_religion|Iterate through all religions|any_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|religion|
|any_religion_for_god|Iterate through all Religions of a God|any_religion_for_god = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|god|religion|
|any_religion_in_religion_group|Iterate through all religions in a religion group.|any_religion_in_religion_group = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|group|religion|
|any_religion_international_organization|Iterate through all international organisations of a religion|any_religion_international_organization = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|international_organization|
|any_religious_aspect|Iterate through all religious aspects of a Country|any_religious_aspect = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|religious_aspect|
|any_religious_focus|Iterate through all completed religious focuses of a Country|any_religious_focus = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|religious_focus|
|any_religious_school_in_religion|Iterate through all Religious Schools in a Religion|any_religious_school_in_religion = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religion|religious_school|
|any_rented_out_mercenary|Iterate through mercenaries a country has rented out to the market|any_rented_out_mercenary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|mercenary|
|any_required_goods|Iterate through all goods required by the scope production method.|any_required_goods = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|production_method|goods|
|any_reserves|Iterate through all subunits on the reserve of a combat-side|any_reserves = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_retreated|Iterate through all subunits on the retreated of a combat-side|any_retreated = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_revolutionary|Iterate through all revolutionary states|any_revolutionary = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|country|
|any_right_flank|Iterate through all subunits on the right-flank of a combat-side|any_right_flank = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|combat_side|sub_unit|
|any_rival|Iterate through all rival countries|any_rival = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_road_type|Iterate through all the road types|any_road_type = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|road_type|
|any_royal_marriage|Iterate through all royal married countries|any_royal_marriage = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_ruler|Iterate through all characters that have ever been rulers in a country, including the dead|any_ruler = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|character|
|any_ruling_countries|Iterate through countries a character rulers|any_ruling_countries = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|country|
|any_sound_toll_in_country|Iterate through all Sound Tolls in a country|any_sound_toll_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|location|
|any_spouse|Iterate through all spouses of a character|any_spouse = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|character|
|any_spy_network_built_in_us|Iterate through all countries building spy networks|any_spy_network_built_in_us = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_sub_continent|Iterate through all existing sub_continents|any_sub_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|sub_continent|
|any_sub_continent_in_continent|Iterate through all sub-continents in a continent|any_sub_continent_in_continent = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|continent|sub_continent|
|any_sub_continent_in_scripted_geography|Iterate through all sub-continents in a scripted geography|any_sub_continent_in_scripted_geography = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|scripted_geography|sub_continent|
|any_sub_unit|Iterate through all subunits in a unit|any_sub_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|unit|sub_unit|
|any_subject|Iterate through all subject countries|any_subject = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_subject_or_below|Iterate through all subject countries and their subject countries, and so on|any_subject_or_below = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_tolerated_culture|Iterate through all Tolerated cultures in a country|any_tolerated_culture = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|culture|
|any_trade|Iterate through all trades in a Country|any_trade = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|trade|
|any_union_partner|Iterate through all countries which are in a personal union with the current country scope.|any_union_partner = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|country|
|any_unit|Iterate through all units in a country|any_unit = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|unit|
|any_unit_in_location|Iterate through all units in a location|any_unit_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|unit|
|any_valid_religion_for_aspect|Iterate through all religion that an aspect can be for|any_valid_religion_for_aspect = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|religious_aspect|religion|
|any_voter|Iterate through all voters in an active resolution|any_voter = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|active_resolution|country|
|any_war|Iterate through all wars going on globally|any_war = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|war|
|any_war_participant|Iterate through all participants of a war|any_war_participant = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|war|country|
|any_weather_system_in_location|Iterate through all weather systems in a location|any_weather_system_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|weather_system|
|any_west_of_province_definition|Iterate through all province-definitions west of a province-definition|any_west_of_province_definition = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|province_definition|province_definition|
|any_work_of_art|Iterate through all WorkOfArts in the world|any_work_of_art = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|none|work_of_art|
|any_work_of_art_by_creator|Iterate through all work_of_art by a particular artist|any_work_of_art_by_creator = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|character|work_of_art|
|any_work_of_art_in_country|Iterate through all work_of_art in a country|any_work_of_art_in_country = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|country|work_of_art|
|any_work_of_art_in_location|Iterate through all work_of_art in a location|any_work_of_art_in_location = { filter = { <triggers> } (optional) <count=num/all> / <percent=fixed_point> (optional) <triggers> }|location|work_of_art|
|area_average_control|Checks the average_control of an area||area|value|
|area_average_integration|Checks the average_integration of an area||area|value|
|area_exploration_progress|gets the exploration progress (0..1) for a country in the scope area||area|value|
|army_maintenance|What is the xx position (0-1) the country has?||country|value|
|army_size|Checks if a country has a certain army size||country|value|
|army_size_percentage|Checks if a country has a certain percentage of regiments compared to expected size||country|value|
|army_tradition|How much army tradition does the country/IO have?||country, international_organization|value|
|army_tradition_percentage|How high the percentage of the current army tradition compared to the maximum does the country/IO have?||country, international_organization|value|
|art_progress|The amount of progress an artist has made on a work of art||character|value|
|art_quality|Checks the quality of the artwork||work_of_art|value|
|artist_skill|The artist skill of the character||character|value|
|artist_type|Checks if a character is a specific type of artist||character||
|assert_if|Conditionally cause an assert during run time|assert_if = { limit = { <trigger> } text = <string> }|none||
|assert_read|Conditionally cause an assert during read time|assert_read = yes/<string>|none||
|at_war|country is at war||country|boolean|
|available_merchant_capacity|gets the market available merchant capacity for a country in the scope market||market|value|
|average_control_in_home_region|Checks the average control in the home region||country|value|
|average_country_literacy|Checks if a country has a certain average_literacy||country|value|
|average_estate_satisfaction|How high is the average estate satisfaction in the country? The crown estate gets ignored here.||country|value|
|average_location_literacy|Checks if a location has a certain average literacy||location|value|
|average_satisfaction|Checks if a location has a certain average satisfaction of its pops||location|value|
|average_special_status_power|Get the average political power of the target special status.|average_special_status_power = { type = <special status> value <operator> <float> } or average_special_status_power(<special status>)|international_organization|value|
|besieger_strength|Check the total strength of the besiegers for the siege in scope||siege|value|
|birth_age|What Age was the character born in? E.g. age_1_traditions||character|age|
|blocks_full_annexation|Checks if the peace treaty blocks full annexation.||peace_treaty|boolean|
|border_distance_to|gets distance between borders of two nations or a location and a nation.|border_distance_to = { country = x value [operator] y } or border_distance_to(country)|country, location|value|
|building_can_be_destroyed_by|Check if the target country scope is capable of destroying the current building scope||building|country|
|building_can_be_upgraded_by|Checks if a building can be upgraded by the target country||building|country|
|building_category|Checks if a building is linked to a certain category||building||
|building_efficiency|does the location have the specific efficiency of a building||location|value|
|building_employed_amount|What's the current effective amount of employed workers?||building|value|
|building_employment_size_amount|What's the max workers amount?||building|value|
|building_goods_input|Check how much goods the scope building requires.||building|value|
|building_index|Checks building index (order in which it was built)||building|value|
|building_level|Check the level of this Building?||building|value|
|building_levels_under_construction|Check the level of this Building?||building|value|
|building_manpower_produced|Checks how much manpower the building type produces||building_type|value|
|building_max_level|Gets the max level for a building||building|value|
|building_pop_type|Checks if a building is linked to a certain pop type||building||
|building_potential_profit|Checks how much profit the building could make if at full worker capacity||building|value|
|building_produced_goods|Checks if a building produces a certain good||building|goods|
|building_profit|Checks building profit||building|value|
|building_sailors_produced|Checks how many sailors the building type produces||building_type|value|
|building_type_is_obsolete|Checks if the specified building type is obsolete for the scope country.||country|building_type|
|building_type_max_level|Gets the max level for a building type in a location.|building_type_max_level = { building_type = <building type scope> [owner = <country scope>] value <operator> <compare value> }|location|value|
|cabinet_action_type|Checks the type of cabinet action (ADM/DIP/MIL)||cabinet_action||
|calc_true_if|Returns true if the specified number of sub-triggers return true|calc_true_if = { amount = 2 <trigger> <trigger> <trigger> }|none||
|can_add_relation|Can the country have the specified scripted relation with another country.|can_add_relation = { first = <country> second = <country> type = <relation type> }|none||
|can_annex_members|Can a country annex members in the scope international organization?||international_organization|country|
|can_be_bribe|Check if the parliament agenda can also serve as a bribe||parliament_agenda|boolean|
|can_be_force_broken_in_peace_treaty|Check if a subject type can be force broken in a peace treaty||subject_type|boolean|
|can_become_rank|Check if a location can become the supplied location rank||location|location_rank|
|can_build_building|Checks if the location/country can build the specified building. Location only checks local requirements, country checks the country scope requirements.||country, location|building_type|
|can_build_unit_type|Checks if the country can build the specified unit type.||country|unit_type|
|can_build_units_of_category|Checks if the country can build units of the specified category.||country|sub_unit_category|
|can_create_casus_belli_of_type_on|Can the country see and create a cb of the supplied type on the target?|can_create_casus_belli_of_type_on = { type = <cb type key> target = <country> }|country||
|can_declare_no_cb_war_on|Can the country declare a war without any casus belli on the target country?||country|country|
|can_declare_war_on|Check if the current country could declare war on the target country||country|country|
|can_do_generic_action|Is the country capable of doing the specified generic action right now?|can_do_generic_action = { generic_action = <generic action> <parameters> }|country||
|can_execute_prisoners|can the prisoners in this unit be executed||unit|boolean|
|can_find_trade_route|can the country find a trade route from market a to market b?|can_find_trade_route = { from = <market> to = <market> }|country||
|can_form|Checks if the country can form the specified formable country.||country|formable_country|
|can_hire_prisoners_as_mercenaries|can we hire the prisoners in this unit as mercenaries||unit|boolean|
|can_initiate_policy_votes|Can a country initiate votes in the scope international organization?||international_organization|country|
|can_join_as_attacker|Can the target country join the war in scope as attacker ?||war|country|
|can_join_as_defender|Can the target country join the war in scope as defender ?||war|country|
|can_join_defensive_war_with|Can the country join in a defensive war with the scope country?||country|country|
|can_join_international_organization|Can we join the supplied international organization?||country|international_organization|
|can_join_offensive_war_with|Can the country join in an offensive war with the scope country?||country|country|
|can_lead_international_organization|Can the country lead the specified international organization?||country|international_organization|
|can_leave_international_organization|Can we leave the supplied international organization?||country|international_organization|
|can_make_subject_of|Can the country in scope become a subject of the target country ? Same checks as the peace treaty become-subject.|can_make_subject_of = { target = <country> type = <subject_type> [ignore_war_limitation = yes] #use to ignore allowed_subjugation of the war }|country||
|can_pay_price|Can the country pay the specified price?||country|price|
|can_raise_army_levies|Checks if the country can raise army levies||country|boolean|
|can_raise_levies|Checks if the country can raise any kind of levies||country|boolean|
|can_raise_navy_levies|Checks if the country can raise navy levies||country|boolean|
|can_ransom_prisoners|can the prisoners in this unit be ransomed||unit|boolean|
|can_research_advance|Checks if a country can research but has not yet researched a specific advance.||country||
|can_rival|Could the current country scope rival the target country ignoring slots and range?||country|country|
|can_see_religious_aspect|Checks if the input religious aspect is visible for the country in scope.||country|religious_aspect|
|can_see_situation|Checks if the 'visible' trigger of the target situation is fulfilled for the country scope.||country|situation|
|can_sell_prisoners_into_slavery|can the prisoners in this unit be sold as slaves||unit|boolean|
|can_serve_in_cabinet_of|Checks if the character can serve in the cabinet of the target country||character|country|
|can_share_maps_with|Country can share maps with the supplied country?||country|country|
|can_start_tutorial_lesson|Can the specified tutorial lesson be started?|can_start_tutorial_lesson = reactive_advice_succession|none||
|can_upgrade_subunit|returns trus if the subunit can be upgraded||unit|boolean|
|can_upgrade_unit|returns trus if the unit can be upgraded||unit|boolean|
|can_use_agenda_bribe|Checks if estate type is allowed in parliament||country||
|can_vote_in_parliament|Can the countrs scope vote in the target international organization?||country|international_organization|
|cancel_exploration_utility|Utility of an cancelling and exploration to the country|cancel_exploration_utility(<area>) or exploration_utility = { area = <area> value <operator><threshold> }|country|value|
|care_about_producing_heirs|Check if a government type cares about heirs||government|boolean|
|cb_creation_progress_against|Checks the progress of the casus belli creation against the target country in percentage.|cb_creation_progress_against = { target = <country scope> value = <script_value> } or cb_creation_progress_against(<country scope>)|country|value|
|character_modifier_strength|Does the scoped character have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|character_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "character_modifier_strength(<modifier key>)"|character||
|character_nickname|Check if the character has the same name key as their nickname||character||
|climate|Checks if a location is of a specific climate||location||
|climate_count|Returns the amount of owned locations with the specified climate.|climate_count = { type = <climate scope> value <operator> <value> } or "climtae_count(<climate scope>)"|country||
|climate_percent|Returns the percentage of owned locations with the specified climate.|climate_percent = { type = <climate scope> value <operator> <value> } or "climate_percent(<climate scope>)"|country||
|colonial_charter_progress|Progress of a colonial charter|colonial_charter_progress(<province definition>) or colonial_charter_progress = { province_definition = <province definition> value <operator><threshold> }|country|value|
|colonial_charter_utility|Utility of a colonial charter|colonial_charter_utility(<province definition>\|<source province>) or colonial_charter_utility = { province_definition = <province definition> source = <source province> value <operator><threshold> }|country|value|
|colonial_charter_value|value of the colonial charter||colonial_charter|value|
|colonial_maintenance|What is the xx position (0-1) the country has?||country|value|
|colonial_range|The colonial range of the country||country|value|
|combat_side_strength|Checks the strength of the combat side in scope||combat_side|value|
|combined_special_status_power|Get the combined special status power of ALL special statuses in the international organization||international_organization|value|
|combined_unique_special_status_power|Get the combined special status power of all countries with their highest ranking special status in the international organization||international_organization|value|
|compare_value|Compare the current value.||value|value|
|complacency|How much complacency does the country/IO have?||country, international_organization|value|
|complacency_percentage|How high the percentage of the current complacency compared to the maximum does the country/IO have?||country, international_organization|value|
|conquer_desire|Gets how much the AI wants to conquer the supplied country|conquer_desire(<target>) or conquer_desire = { target = <country link> value <operator> <amount> }|country|value|
|conquistador_utility|Utility of a conquistador|conquistador_utility(<area>) or conquistador_utility = { area = <area> value <operator><threshold> }|country|value|
|controls|Does the country control a specific location?||country|location|
|country_art_quality|Checks the total art quality in a Country||country|value|
|country_can_join_international_organization|Can we add a country to the supplied international organization?||country|international_organization|
|country_combined_special_status_power|Get the political power of the country within the target international organization with all of its special statuses combined.|country_combined_special_status_power = { international_organization = <IO> value <operator> <float> } or country_combined_special_status_power(<IO>)|country|value|
|country_combined_special_status_power_fraction|Get the political power fraction of the country within the target international organization with all of its special statuses combined.|country_combined_special_status_power = { international_organization = <IO> value <operator> <float> } or country_combined_special_status_power(<IO>)|country|value|
|country_economical_base|Checks the total economical base of a country||country|value|
|country_estate_loan_size|Checks the size of a loan given by the estates to a country||country|value|
|country_exists|Does the country exist?||none|country|
|country_has_been_member_for_years|Checks if the country has been in the current international organization scope for x years.|country_has_been_member_for_years = { country = <country scope> value = <years> } or country_has_been_member_for_years(country)|international_organization|value|
|country_has_disease|Checks the presence of a disease in a country.|country_has_disease = <disease>|country|disease|
|country_has_disease_outbreak|Checks the presence of a disease outbreak in a country.|country_has_disease_outbreak = <disease>|country|disease_outbreak|
|country_has_estate|Checks if the country has the specific Estate||country|estate_type|
|country_has_special_status|Does the country have a special status in this international organization?||international_organization||
|country_highest_rated_special_status_power|Get the political power of the country within the target international organization of its highest prioritized special status.|highest_rated_special_status_power = { international_organization = <IO> value <operator> <float> } or highest_rated_special_status_power(<IO>)|country|value|
|country_interaction_acceptance|How high is the target country's AI value of accepting the country interaction done by the current country scope? Always return 0 if the target is a player|country_interaction_acceptance = { type = <country interaction> target = <country> value = <script_value> } or country_interaction_acceptance(<country interaction>\|<country>)|country|value|
|country_loan_capacity|Checks how much more money a country can borrow||country|value|
|country_modifier_strength|Does the scoped country have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|country_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "country_modifier_strength(<modifier key>)"|country||
|country_rank_level|level of the country rank of a country||country|value|
|country_rank_level_on_date|level of the country rank of a country on a particular date||country|value|
|country_strength|Strength of a country, including their troop numbers as well as tax base and manpower||country|value|
|country_tax_base|Checks the total tax base of a country||country|value|
|country_total_army_levy_size|Gets the total number of army levies available to the country||country|value|
|country_total_navy_levy_size|Gets the total number of navy levies available to the country||country|value|
|country_type|Checks what type a country is (location, pop, building, army, navy)||country||
|court_language_utility|Utility of a court language accorting to Ai||dialect, language|value|
|court_maintenance|What is the xx position (0-1) the country has?||country|value|
|create_market_utility|Utility of creating a market|create_market_utility(<location>) or create_market_utility = { location = <location> value <operator><threshold> }|country|value|
|cultural_influence|How much influence does the culture have?||culture|value|
|cultural_maintenance|What is the xx position (0-1) the country has?||country|value|
|cultural_tradition|How much tradition does the culture have?||culture|value|
|cultural_unity|Checks the fraction of the population sharing the country's primary culture||country|value|
|cultural_view|does the culture have the specified opinion of the target?|cultural_view = { target = <target culture> value <operator> <script_value> }|culture||
|culture_group_percentage|Gets the percentage of the population that follow a particular culture group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_group_population_percentage = { culture_group = <culture group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|culture_group_percentage_in_country|The percentage of a specific culture group in the current country||country|value|
|culture_group_population|Gets the absolute number of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_group_population = { culture_group = <culture group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|culture_group_population_in_country|The number of pops of a specific culture group in the current country||country|value|
|culture_opinion_impact|Opinion impact of a particular culture on another|culture_opinion_impact(<culture link>) or culture_percentage = { culture = <culture link> value <operator> <amount> }|culture|value|
|culture_percentage|Gets the percentage of the population that follow a particular culture in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_population_percentage = { culture = <culture> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|culture_percentage_in_area|gets the percentage of the population that follow a particular culture in the area|culture_percentage_in_area = { country = <country> culture = <culture> value <operator> <script_value> }|area|value|
|culture_percentage_in_country|The percentage of a specific culture in the current country||country|value|
|culture_population|Gets the absolute number of the population that follow a particular culture in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_population = { culture = <culture> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|culture_population_in_country|The number of pops of a specific culture in the current country||country|value|
|currency_percentage_towards_limit|Gets currency progress towards specified limit||country, international_organization|value|
|currency_utility|Utility of an amount of currency to the country|currency_utility(<currency>\|<amount>) or currency_utility = { currency = <currency> amount = <amount> }|country|value|
|current_age|Checks if it is a certain age!||none||
|current_date|Compare the current ingame date.||none|date|
|current_mission_task|Checks if the country has the specified mission task in progress.||country|mission_task|
|current_month|Compare the current ingame month (1..12)||none|value|
|current_ruler_term_years|Checks the current ruler term length in years.||country|value|
|current_tooltip_depth|What is the number of tooltips open right now?||none|value|
|current_year|Compare the current ingame year||none|value|
|custom_description|Wraps triggers that get a custom description instead of the auto-generated one|custom_description = { text = <trigger_localization_key> subject = <optional subject scope> #defaults to current scope object = <optional object scope> value = <optional script value> ... triggers ... }|none||
|custom_tooltip|Replaces the tooltips for the enclosed triggers with a custom text|custom_tooltip = { text = <text> subject = <scope> (optional) <trigger> }|none||
|days_as_rebel|Check how many days the character has been a rebel.||character|value|
|days_of_service_as_admiral|Check how many days the character has served as an admiral.||character|value|
|days_of_service_as_general|Check how many days the character has served as a general.||character|value|
|days_of_service_in_cabinet|Check how many days the character has served in a cabinet.||character|value|
|days_since_disaster_end|Checks if x days have passed since the end of the disaster. Returns -1 if the disaster has never ended.||disaster|value|
|days_since_disaster_start|Checks if x days have passed since the start of the disaster. Returns -1 if the disaster has never started.||disaster|value|
|days_since_situation_end|Checks if x days have passed since the end of the situation. Returns -1 if the situation has never ended.||situation|value|
|days_since_situation_start|Checks if x days have passed since the start of the situation. Returns -1 if the situation has never started.||situation|value|
|debug_log|Log whether the parent trigger succeeded or failed||none||
|debug_log_details|Log whether the parent trigger succeeded or failed. Log which children succeeded or failed||none||
|debug_only|Checks if the game is in debug mode or not.||none|boolean|
|defensive_alliance_strength|Strength of a defensive alliance, including the nation with all countries giving defensive support and those that can be called in for defensive wars||country|value|
|definition_is_for_levy|subunit definition is for levies||sub_unit|boolean|
|demands_goods|Check if the market scope has a demand for the target goods.||market|goods|
|demands_goods_by_pops|Check if the market has any pop demand for the target goods.||market|goods|
|dependency_length_days|returns the number of days a country has been in a dependency (overlord/subject) relationship with the target country.|dependency_length_days = { target = <country> value <comparator> <script_value> }|country|value|
|destroy_market_utility|Utility of destroying a market|destroy_market_utility(<location>) or destroy_market_utility = { location = <location> value <operator><threshold> }|country|value|
|development|Checks if a location has a certain Development||location|value|
|devotion|How much devotion does the country/IO have?||country, international_organization|value|
|devotion_percentage|How high the percentage of the current devotion compared to the maximum does the country/IO have?||country, international_organization|value|
|dip|The dip ability of the character||character|value|
|diplomatic_capacity_of_new_relation|Diplomatic capacity that will be used if the country obtains this diplomatic relation||country|value|
|diplomatic_capacity_without_maintenance|Diplomatic capacity that country would have without paying anything for maintenance||country|value|
|diplomatic_maintenance|What is the xx position (0-1) the country has?||country|value|
|diplomatic_range|Is the target country within diplomatic range?||country|value|
|disaster_has_ended|Check if a Disaster has ended||disaster|boolean|
|disaster_is_active|Check if a Disaster is active||disaster|boolean|
|discount_needed_for_law_change|Checks how much more discount % is needed for Ai to change a law||country|value|
|disease_affects_pops_here|Checks if a disease is affecting some migrated pops here.||location|disease|
|disease_country_deaths|Checks the number of deaths from a disease in a country.|disease_country_deaths(<disease>) disease_country_deaths = { target = <disease> value <comparator> <real> }|country|value|
|disease_has_outbreak_here|Checks if a disease has an outbreak in a location or subunit.||location, sub_unit|disease|
|disease_has_stagnated|Checks if a disease has stagnated in a location or subunit.||location, sub_unit|disease|
|disease_is_active|Checks if a disease is active in the world.||none|disease|
|disease_outbreak_country_deaths|Checks the number of deaths from an outbreak in a country.|disease_outbreak_country_deaths(<disease_outbreak>) disease_outbreak_country_deaths = { disease_outbreak = <disease_outbreak> value <comparator> <real> }|country|value|
|disease_outbreak_is_active|Checks if a disease outbreak is active in the world.||none|disease_outbreak|
|disease_outbreak_presence|Checks the presence of a disease in a location or subunit.|disease_outbreak_presence(<disease_outbreak>) or disease_outbreak_presence = { disease_outbreak = <disease_outbreak> value <comparator> <real> }|location, sub_unit|value|
|disease_outbreak_total_deaths|How many people have been killed by this disease outbreak?||disease_outbreak|value|
|disease_presence|Checks the presence of a disease in a location or subunit.|disease_presence(<disease>) or disease_presence = { disease = <disease> value <comparator> <real> }|location, sub_unit|value|
|disease_resistance|Checks the resistance to a disease in a location or subunit.|disease_resistance(<disease>) or disease_resistance = { target = <disease> value <comparator> <real> }|location, sub_unit|value|
|disease_total_deaths|How many people have been killed by this disease?||disease|value|
|distance_to|gets distance between locations||location|value|
|distance_to_area|gets distance between a location and an area||location|value|
|distance_to_squared|gets distance squared as the crow flies between locations (much quicker than distance_to, useful if you're just comparing)||location|value|
|does_estate_want_other_policy|Checks if a country has at least one law for which the input estate want another policy||country||
|does_owner_want_to_give_away|Check if a province's owner wants to give it away to a subject||province|boolean|
|doom|How much doom does the country/IO have?||country, international_organization|value|
|doom_percentage|How high the percentage of the current doom compared to the maximum does the country/IO have?||country, international_organization|value|
|dynastic_power|Returns the dynastic power of the scope dynasty or country. For countries, check ruler dynasty or heir dynasty if in regency.|dynastic_power = { international_organization = <IO> value <operator> <script_value> } or dynastic_power(<IO>)|country, dynasty|value|
|dynasty_exists|does a tag exist||none||
|dynasty_modifier_strength|Does the scoped dynasty have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|dynasty_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "dynasty_modifier_strength(<modifier key>)"|dynasty||
|dynasty_name|if a dynasty a special name-key||dynasty||
|education|Checks if a character has a specific education||character||
|effective_skill|Check the skill level of this cabinet||cabinet|value|
|eligible_for_cabinet|Is this estate type eligible for the cabinet in the target country?|eligible_for_cabinet = { target = <target country> }|estate_type||
|employment_percentage|Checks if a location has a certain unemployement percentage||location|value|
|employment_size|Returns the employment size of a building type per building level||building_type|value|
|employment_system_desire|returns how much the country wants the target employment system.|employment_system_desire = { target = <employment system> value <comparator> <script_value> }|country|value|
|estate_gold|The gold of an estate||estate|value|
|estate_loan_interest|Checks the interest of a loan||country|value|
|estate_max_tax|the current max-tax of an estate in a country|estate_max_tax(<estate_type link>) or estate_max_tax = { estate_type = <estate_type link> value <operator> <amount> }|country|value|
|estate_opinion|the current opinion that an estate in a country has of another country|estate_opinion(<estate_type link>\|<country>) or estate_opinion = { estate_type = <estate_type link> target = country value <operator> <amount> }|country|value|
|estate_satisfaction|the current satisfaction of an estate in a country|estate_satisfaction(<estate_type link>) or estate_satisfaction = { estate_type = <estate_type link> value <operator> <amount> }|country|value|
|estate_tax|The current tax the estate has to pay||estate|value|
|estate_tax_rate|The current percentage of tax the estate has to pay. Returns 1 if the estate gets fully taxed even if the max possible tax is below 100%||estate|value|
|estate_taxable_income|The taxable income of an estate||estate|value|
|estate_type_allowed_in_cabinet|Checks if estate type is allowed in cabinet||country||
|estate_type_allowed_in_command|Checks if estate type is allowed in command of a unit||country||
|estate_type_allowed_in_parliament|Checks if estate type is allowed in parliament||country||
|exists|Checks whether the specified scope target exists (check for not being the null object)|exists = from.owner.var:cool_var.mother|none||
|expected_army_size|Checks if a country has a certain expected army size||country|value|
|expected_navy_size|Checks if a country expects to have a certain amount of ships||country|value|
|experience_percentage|How many percent experience does this unit have???||unit|value|
|exploration_expected_cost|gets the exploration expected cost for a country in the scope area||area|value|
|exploration_maintenance|What is the xx position (0-1) the country has?||country|value|
|exploration_monthly_cost|what is the monthly cost of an exploration?||exploration|value|
|exploration_monthly_progress|what is the monthly progress of an exploration?||exploration|value|
|exploration_needed_time|gets the exploration needed time (months) for a country in the scope area||area|value|
|exploration_progress|what is the progress of an exploration?||exploration|value|
|exploration_time|what is the total needed progress of an exploration?||exploration|value|
|exploration_utility|Utility of an exploration to the country|exploration_utility(<area>\|<character>) or exploration_utility = { area = <area> character = <character> value <operator><threshold> }|country|value|
|favors|How much favors does the country have in the target?|favors = { target = X value <operator> Y or value = { min max } }|country|value|
|favors_needed_to_annul_relations_with|Gets the number of favours needed to annul relations with the target country diplomatically|"favors_needed_to_annul_relations_with(<target>)" or favors_needed_to_annul_relations_with = { target = <country link> value <operator> <amount> }|country|value|
|fertility|The fertility of the character||character|value|
|food_consumption|Amount of consumed food||location|value|
|food_maintenance|What is the xx position (0-1) the country has?||country|value|
|food_percentage|How many percent of food does this unit have???||unit|value|
|food_price|Checks how much the food in the current market costs||market|value|
|food_production|Amount of food production||location|value|
|food_value|Check the food value of the goods scope.||goods|value|
|forbids_sovereign_diplomacy|Check if a subject type restricts diplomacy||subject_type|boolean|
|fort_maintenance|What is the xx position (0-1) the country has?||country|value|
|garrison_percentage|Checks the garrison percentage of the location in scope||location|value|
|garrison_strength|Checks the garrison strength of the location in scope||location|value|
|get_antagonism|how much of an antagonism type does the country have towards another country?||country|value|
|get_opinion|how much of an opinion type does the country have towards another country?||country|value|
|get_trust|how much of a trust type does the country have towards another country?||country|value|
|gfx_culture_applicable|Checks if a culture gfx applies to the scope object||character, country, culture, dynasty, graphical_culture, location, pop, religion||
|gives_fleet_basing_rights|Check if a subject type gives fleet basing rights||subject_type|boolean|
|gives_fleet_basing_rights_to|Does the scope country give fleet basing rights to the specified country?||country|country|
|gives_food_access|Check if a subject type gives food access||subject_type|boolean|
|gives_food_access_to|Does the scope country give food access to the specified country?||country|country|
|gives_isolation_exemption_to|Does the scope country give a trade isolation exemption to specified country?||country|country|
|gives_military_access_to|Does the scope country give military access to the specified country?||country|country|
|giving_scripted_relation|Checks for giving scripted relation.|giving_scripted_relation = { target = country type = <scripted type> }|country||
|giving_scripted_relation_of_type|Checks if that scripted relation is given by the country scope to any other country.||country|relation_type|
|global_variable_list_size|Checks the size of a global variable list|global_variable_list_size = { name = <variable_name value >= <script_value> }|none||
|global_variable_map_size|Checks the size of a global variable map|global_variable_map_size = { name = <variable_name value >= <script_value> }|none||
|gold|How much gold does the country/IO have?||country, international_organization|value|
|gold_percentage|How high the percentage of the current gold compared to the maximum does the country/IO have?||country, international_organization|value|
|goods|Checks which good is in this trade||trade|goods|
|goods_category|tests the goods category - raw_material or produced||goods||
|goods_demand_in_market|Checks how much demand exists of a good in the market.|goods_demand_in_market = { goods = <goods> value = <script_value> } or goods_demand_in_market(<goods>)|market|value|
|goods_method|tests the goods method - mining/farming/hunting/gathering||goods||
|goods_output|Check how much goods the scope location produces.||location|value|
|goods_supply_in_market|Checks how much supply exists of a good in the market.|goods_supply_in_market = { goods = <goods> value = <script_value> } or goods_supply_in_market(<goods>)|market|value|
|government_power|How much government power does the country/IO have?||country, international_organization|value|
|government_power_percentage|How high the percentage of the current government power compared to the maximum does the country/IO have?||country, international_organization|value|
|great_power_ranking|Country's position in the list of great powers||country|value|
|great_power_score|Checks if a country has a certain Great Power Score||country|value|
|had_disaster_for_years|Check if the country scope had the specified disaster type for a specific amount of years.|had_disaster_for_years = { disaster_type = <disaster type> years = <years> } or had_disaster_for_years(<disaster type>)|country|value|
|harmony|How much harmony does the country/IO have?||country, international_organization|value|
|harmony_percentage|How high the percentage of the current harmony compared to the maximum does the country/IO have?||country, international_organization|value|
|has_accepted_culture|Check if a country has a culture as an accepted culture||country|culture|
|has_accessible_coastline|Does the area have a coastline with a port or not?||area|boolean|
|has_active_resolution|Does the scope international organization/situation have any active resolutions?||international_organization, situation|boolean|
|has_advance|Checks if a country has a certain advance||country||
|has_advance_available|Checks if a country has a certain advance available to research. Returns true if the advance has been researched already.||country||
|has_advance_for_employment_system|Does the country have the necessary advance to be able to adopt the supplied employment system?||country|employment_system|
|has_advance_for_succession_law|Does the country have the necessary advance to be able to adopt the supplied succession law?||country|heir_selection|
|has_antagonism|does the country have an antagonism type towards another country?||country||
|has_any_active_disaster|country has at least an active disaster||country|boolean|
|has_any_convertable_pops|Check if a location has any pops that can be converted to state religion||location|boolean|
|has_any_culture_group|If a culture belongs to any culture group.||culture|boolean|
|has_any_disease_present|Checks if the location or subunit is affected by ANY disease active.||location, sub_unit|boolean|
|has_any_mission_active|Checks if the country has the specified mission as its currently active mission.||country|boolean|
|has_any_possible_disaster|Country has at least one possible disaster about to strike||country|boolean|
|has_art_in_progress|Checks if an artist is currently working on something||character|boolean|
|has_assigned_explorer|does the country have an assigned explorer in this area?||area|country|
|has_autocephalous_patriarchates|religion has autocephalous patriarchates||religion|boolean|
|has_available_marriage_slot|Has the character got a slot available for another marriage? (i.e. are they unmarried for non-polygamous people, or have they got less than the max number of spouses for polygamous people)||character|boolean|
|has_avatar|checks if a country has a particular avatar||country|avatar|
|has_been_formed|Checks if the formable has been formed already||formable_country|boolean|
|has_been_influenced_by_parliament_agenda|Checks if the country scope has already been influenced by an accepted parliament agenda in the target international organization's parliament.||country|international_organization|
|has_blocked_treaties|Is the country blocked from doing treaties with country?||country|country|
|has_breach|siege has breach||siege|boolean|
|has_building|Checks if a location has a specific building||location|building_type|
|has_building_with_at_least_one_level|Checks if a location has a specific building and it has at least one level||location||
|has_building_with_graphical_tag|Checks if a location has a building with the specified graphical tags||location||
|has_building_with_graphical_tag_and_at_least_one_level|Checks if a location has a building with the specified graphical tags and at least one level||location||
|has_cabinet_action|is doing something in the cabinet||cabinet, character|boolean|
|has_cached_or_cast_vote_for|Has the supplied country voted or has a cached vote from previous month on the supplied resolution for a specific target in the scope international organization/situation?||international_organization, situation||
|has_canonization|religion has canonization||religion|boolean|
|has_cardinals|religion has Cardinals||religion|boolean|
|has_casus_belli|Checks if that war has a CB specified at all||war|boolean|
|has_casus_belli_of_type_on|Does the country have a cb of the supplied type on the target?|has_casus_belli_of_type_on = { type = <cb type key> target = <country> }|country||
|has_casus_belli_on|Does the country have a cb on the target?||country|country|
|has_character_modifier|Does the scoped character have a given modifier|has_character_modifier = name|character||
|has_child_education|Does the scoped child have a given education|has_child_education = education|character||
|has_child_education_selected|Does the scoped child have any given education|has_child_education_selected = yes|character|boolean|
|has_claim_on_province|Does the country have a casus belli targetting the specified province?||country|province|
|has_colonial_charter|does the province definition have a colonial charter belonging to the specified country||province_definition|country|
|has_colonial_charter_in|Does the country have a colonial charter in the target province_definition?||country|province_definition|
|has_colonial_charters|Does the country have colonial charters?||country|boolean|
|has_colonial_claim|country has a claim on a province definition?|has_colonial_claim = <province definition>|country|province_definition|
|has_combat|Check if a location has a combat||location|boolean|
|has_commander|unit has a commander||unit|boolean|
|has_completed_religious_focus|Checks if a country has completed a certain religious focus||country||
|has_consort|country has a Consort||country|boolean|
|has_cooldown|Does a country have a particular cooldown active||country, international_organization||
|has_core|Does the country has a core of a specific location?||country|location|
|has_countries_with_antagonism|Country has antagonism towards them from other countries||country|boolean|
|has_countries_with_coalition_grade_antagonism|Country has antagonism towards them from other countries to the point where they could form a coalition against them||country|boolean|
|has_countries_with_near_coalition_grade_antagonism|Country has antagonism towards them from other countries to the point where they are thinking of forming a coalition against them||country|boolean|
|has_countries_with_timed_antagonism|Country has temporary antagonism towards them from other countries||country|boolean|
|has_country_modifier|Does the scoped country have a given modifier|has_country_modifier = name|country||
|has_culture_group|If a culture belongs to a specific culture group.||culture|culture_group|
|has_culture_with_tag|Checks if a culture has the specified tags||culture||
|has_customer|Check if a mercenary has a customer||mercenary|boolean|
|has_diplomacy_with|Does the country have a certain type of diplomatic relation with another.|has_diplomacy_with = { country = <country> type = <type> }|country||
|has_discovered|Has the country discovered a specific location?||country|location|
|has_discovered_area|Has the country fully discovered the area?||country|area|
|has_dlc|Does the host have this DLC||none||
|has_doom|country has doom mechanics||country|boolean|
|has_dynasty|character is in a Dynasty||character|boolean|
|has_earthquakes|Check if a location has a Earthquakes||location|boolean|
|has_elections|Checks if an international organization has electors||international_organization|boolean|
|has_embraced_institution|Checks if a country has embraced an institution||country|institution|
|has_employment_system|Does the country has the supplied employment system?||country|employment_system|
|has_enabled_currency|Checks what currency has been enabled for the international organization (manpower, sailors, gold)||international_organization||
|has_estate|Checks if a character is of a specific Estate||character|estate_type|
|has_estate_privilege|Checks if a country has a certain estate privilege||country|estate_privilege|
|has_exploration|character/country is currently exploring||character, country|boolean|
|has_exploration_construction|character is currently preparing to explore||character|boolean|
|has_exports|Check if a location has a Exports||location|boolean|
|has_extended_winter|does the area have extended winter or not?||area|boolean|
|has_fired_unique_event|Checks if the game has already fired the unique event||none||
|has_fixed_liturgical_language|religion has a set liturgical language||religion|boolean|
|has_fort|Check if a location has any fort||location|boolean|
|has_game_rule|Is the given game rule setting enabled?|has_game_rule = faster_conversion|none||
|has_gifted_gold_to|Has the country an active gold gift cooldown with the target country?||country|country|
|has_global_variable|Checks whether the specified global variable is set|has_global_variable = name|none||
|has_global_variable_list|Checks whether the specified global variable list is set|has_global_variable_list = name|none||
|has_global_variable_map|Checks whether the specified global variable map is set|has_global_variable_map = name|none||
|has_graphical_culture|Check if a culture has a graphical culture||culture||
|has_graphical_religion|Check if a religion has a graphical culture||religion||
|has_heir|country has a Heir||country|boolean|
|has_highest_rated_special_status_in_international_organization_of_type|Does the country have the specified special status as its highest ranking?||country||
|has_historical_rival|Does the scope country have the specified country as an historical rival?||country|country|
|has_historical_rivals|Does the scope country have historical rivals?||country|boolean|
|has_holy_sites|religion has holy sites||religion|boolean|
|has_honor|religion has honor||religion|boolean|
|has_imports|Check if a location has a imports||location|boolean|
|has_institution|Checks if a country has an institution||location|institution|
|has_insulted|Has the country an active insult cooldown with the target country?||country|country|
|has_international_organization_modifier|Does the scoped international organization have a given modifier|has_international_organization_modifier = name|international_organization||
|has_invited_religious_figure|country has invited religious figures to work with them||country|boolean|
|has_karma|religion has karma||religion|boolean|
|has_land_ownership_rule|Checks if the international organization has a landownership rule set||international_organization|boolean|
|has_latest_road_to|Check if a location has the latest available road to the target location. Latest is determined by the owner of the location and what buildable road type has the highest level.||location|location|
|has_law|Checks if a country has a certain law enabled|has_law = <law_key>|country|law|
|has_leader|Does the exploration have a leader?||exploration|boolean|
|has_levies|unit has levies||unit|boolean|
|has_limited_diplomacy|Check if the country has limited diplomacy||country|boolean|
|has_loc_key|Checks if certain key is assigned to a loan||loan||
|has_local_dlc|Does the host have this DLC||none||
|has_local_variable|Checks whether the specified local variable is set|has_local_variable = name|none||
|has_local_variable_list|Checks whether the specified local variable list is set|has_local_variable_list = name|none||
|has_local_variable_map|Checks whether the specified local variable map is set|has_local_variable_map = name|none||
|has_location|Is the supplied location owned by the scope international organization?||international_organization|location|
|has_location_modifier|Does the scoped province have a given modifier|has_location_modifier = name|location||
|has_market_construction|Is the location building a market?||location|boolean|
|has_markets|country has market centers||country|boolean|
|has_member|Checks if an international organization has a certain member||international_organization|country|
|has_mercenaries|unit has mercenaries||unit|boolean|
|has_mercenary_modifier|Does the scoped mercenary have a given modifier|has_mercenary_modifier = name|mercenary||
|has_merchant|checks if the market has a merchant of the specific country.||market|country|
|has_merchant_power|does the market have a merchant power for?|has_merchant_power = { country = country key = key }|market||
|has_migration|Check if a province definition has a migration going on||province_definition|boolean|
|has_mission_task|Checks if the country has the specified mission task visible in its current mission.||country|mission_task|
|has_multiple_players|Does the game have at least two players currently connected?||none|boolean|
|has_mutual_scripted_relation|Checks for a mutual scripted relation.|has_mutual_scripted_relation = { target = country type = <scripted type> }|country||
|has_mutual_scripted_relation_of_type|Checks if that scripted relation exists between the country scope and any other country.||country|relation_type|
|has_new_world_goods_in_market|Checks if a market has a supply of any new-world goods||market|boolean|
|has_newsletter_subscription|Has the player subscribed to the newsletter?||none|boolean|
|has_nickname|Check if the character has any nick name set||character|boolean|
|has_ongoing_parliament_debate|Country / international organization has an active parliament debate||country, international_organization|boolean|
|has_opinion|does the country have an opinion type towards another country?||country||
|has_or_had_tag|Is the scoped country the specific historical tag or was ever it; does NOT accept scopes|has_or_had_tag = GER|country|tag|
|has_origin_in_new_world|Check if a goods has origin in the new world||country|boolean|
|has_origin_in_old_world|Check if a goods has origin in the old world||country|boolean|
|has_overlords_ruler|Check if a subject type has to have its overlord's ruler||subject_type|boolean|
|has_owned_buildings|Has the target country got some buildings here?||location|country|
|has_owner|Check if a location has a Owner||location|boolean|
|has_parliament|Checks if the country / international organization has a parliament||country, international_organization|boolean|
|has_participated_in_parliament|Checks if the country scope has already participated in the target international organization's parliament.||country|international_organization|
|has_passable_land|Check if a province definition has passable land||province_definition|boolean|
|has_patriarchs|religion has Patriarchs||religion|boolean|
|has_periphora|Check if art is on a periphora or not||work_of_art|boolean|
|has_policy|Checks if a country has a certain policy for a then policy's law||country||
|has_ports|country has ports?||country|boolean|
|has_positive_opinion|Does the country have a positive opinion?||country|country|
|has_possible_institution_spawn|Check if a province has an institution that can be promoted to spawn||province|boolean|
|has_possible_nomad_targets|Does the country have any possible nearby places to migrate to?||country|province_definition|
|has_potential_royal_marriage|Could the country do a royal marriage with the specified country?||country|country|
|has_presence_in|country has a presence in the geography supplied?||country||
|has_primary_or_accepted_culture|Check if a country has a culture as a primary or an accepted culture||country|culture|
|has_primary_or_accepted_or_tolerated_culture|Check if a country has a culture as a primary or an accepted or a tolerated culture||country|culture|
|has_prisoners|returns trus if the unit contains prisoners||unit|boolean|
|has_privateers_from|Does the location has privateers of the target country?||area, location, province|country|
|has_province_modifier|Does the scoped province have a given modifier|has_province_modifier = name|province||
|has_purity|religion has purity||religion|boolean|
|has_raised_army_levies|Check if the country has raised army levies||country|boolean|
|has_raised_levies|Check if the country has raised levies||country|boolean|
|has_raised_navy_levies|Check if the country has raised navy levies||country|boolean|
|has_rebel|Check if a pop has allegiance to a rebel||pop|boolean|
|has_reform|Checks if a country has a specific reform||country|government_reform|
|has_regent|country has a regent||country|boolean|
|has_regular_elections|does the country have regular elections||country|boolean|
|has_regulars|unit has regulars||unit|boolean|
|has_religion_modifier|Does the scoped religion have a given modifier|has_religion_modifier = name|religion||
|has_religious_aspect|Checks if a country has a certain religious aspect||country|religious_aspect|
|has_religious_factions|religion has religious factions||religion|boolean|
|has_religious_focuses|religion has religious focuses||religion|boolean|
|has_religious_head|religion has ReligiousHead||religion|boolean|
|has_religious_influence|religion has ReligiousInfluence||religion|boolean|
|has_religious_schools|religion has religious schools||religion|boolean|
|has_river|Check if a location has a river||location|boolean|
|has_road_constructions|Check whether location has road constructions||location|boolean|
|has_road_of_type_to|Check if a location has a road to the target location of the specified type.|has_road_of_type_to = { target = <target location> type = <road type> }|location||
|has_road_to|Check if a location has a road to the target location||location|location|
|has_road_to_capital|Check if a location has a road to capital||boolean|location|
|has_royal_marriage_with|Does the country have a royal marriage with specified country?||country|country|
|has_ruler|country has a ruler||country|boolean|
|has_scripted_relation|Checks if that scripted relation exists between these two countries.|has_scripted_relation = { target = country type = <scripted type> }|country||
|has_scripted_relation_of_type|Checks if that scripted relation exists for the country scope with any other country.||country|relation_type|
|has_sects|religion has sects||religion|boolean|
|has_shared_culture_group|If a culture belongs to a specific culture group.||culture|culture|
|has_siege|Check if a location has a siege||location|boolean|
|has_societal_value|Checks if the country has a specific societal value||country|societal_value_type|
|has_sound_tolls|country has sound tolls||country|boolean|
|has_spawned|Has the institution spawned anywhere?||institution|boolean|
|has_special_status_available|Checks if an international organization has a particular special status available||international_organization|special_status|
|has_special_status_in_international_organization|Does the country have a special status in the supplied international organization?||country||
|has_support_from|Checks if a rebel has support froma certain pop type||rebels|pop_type|
|has_tag|Check if that object has the specified tag.||building, building_type, casus_belli, goods, heir_selection, law, peace_treaty, policy, religion||
|has_target_casus_belli_on_us|Does the target have a cb on the country?||country|country|
|has_temporary_demand|Checks if a market has a certain temporary demand||market|demand|
|has_temporary_demands|Checks if a market has a certain temporary demand||market|boolean|
|has_tolerated_culture|Check if a country has a culture as an Tolerated culture||country|culture|
|has_trade_treaty_with|Does the country have a trade agreement with a specified country?||country|country|
|has_trait|Checks if a character has a specified trait||character||
|has_trait_category|Checks if any of the character's traits belongs to the specified category.||character||
|has_truce_with|Is the country at truce with a specified country?||country|country|
|has_trust|does the country have a trust type towards another country?||country||
|has_unit|character is assigned to a unit||character|boolean|
|has_unit_modifier|Does the scoped unit have a given modifier|has_unit_modifier = name|unit||
|has_unlocked_any_unit_of_category|Has the country unlocked any unit of the specified category?||country||
|has_variable|Checks whether the current scope has the specified variable set|has_variable = name|none||
|has_variable_list|Checks whether the current scope has the specified variable list set|has_variable_list = name|none||
|has_variable_map|Checks whether the current scope has the specified variable map set|has_variable_map = name|none||
|has_volcano|Check if a location has a volcano||location|boolean|
|has_voted|Has the supplied country voted on the supplied resolution in the scope international organization/situation?||international_organization, situation||
|has_voted_for|Has the supplied country voted on the supplied resolution for a specific target in the scope international organization/situation?||international_organization, situation||
|has_voted_for_issue_in_parliament|Checks if the country scope has voted for the issue in the target international organization's parliament. Returns false if they have voted against it or have not voted at all.||country|international_organization|
|has_yanantin|religion has yanantin||religion|boolean|
|heathen_population_fraction|Checks the fraction of the population having a different religious group than the country||country|value|
|heir_candidates_count|Checks amount of heirs in heir selection for country||heir_selection|value|
|heir_position|Character's position in line for its country's throne||character|value|
|heir_score|Get the hypothetical heir score of the character for the target country, even if the character in question could not be an heir.||character|value|
|heir_score_country|Get the hypothetical heir score of the target character for the current country, even if the character in question could not be an heir.||country|value|
|heir_score_home|Get the hypothetical heir score of the character in the country they currently reside in.||character|value|
|hemisphere|Check if a location is either in the northern or southern hemisphere.|hemisphere = northern/southern|location||
|heretic_population_fraction|Checks the fraction of the population having a different religion in the same group as the country||country|value|
|hidden_trigger|Enclosed triggers are not shown in tooltips|hidden_trigger = { <more triggers> }|none||
|higher_temporary_taxes_needed|Checks how much more max tax a country wants||country|value|
|hire_price|how much would it cost to hire this unit as a merc.|hire_price(<cost multiplier>\|<duration in months>)|unit|value|
|honor|How much honor does the country/IO have?||country, international_organization|value|
|honor_percentage|How high the percentage of the current honor compared to the maximum does the country/IO have?||country, international_organization|value|
|horde_unity|How much horde_unity does the country/IO have?||country, international_organization|value|
|horde_unity_percentage|How high the percentage of the current horde_unity compared to the maximum does the country/IO have?||country, international_organization|value|
|implementation_progress_percentage|Checks if the current government reform/avatar/estate privilege /god/policy/law/cabinet action scope has been implemented in percentage.||avatar, cabinet_action, estate_privilege, god, government_reform, law, policy|value|
|in_assault|siege is in assault||siege|boolean|
|in_cabinet|character is in cabinet||character|boolean|
|in_civil_war|country is in civil war||country|boolean|
|in_combat|unit is in combat||unit|boolean|
|in_marriage_union_with|Is the country in a marriage union with specified country?||country|country|
|in_retreat|unit is in Retreat||unit|boolean|
|in_siege|unit is in Siege||unit|boolean|
|in_trade_range_of|Is the market within trading range of a merchant the target country?||market|country|
|in_union_with|Is the country in a union with specified country?||country|country|
|in_war_of_casus_belli|Is the country in any war with the specified casus belli?||country|casus_belli|
|in_zone_of_control|Check if a location is in the zone of control of a friendly fort||location|boolean|
|inflation|How much inflation does the country/IO have?||country, international_organization|value|
|inflation_percentage|How high the percentage of the current inflation compared to the maximum does the country/IO have?||country, international_organization|value|
|integration_level|Checks the integration level of a location||location||
|integration_progress|Checks the integration progress of a location||location|value|
|international_organization_can_add_land|Can we add a location to the scope international organization?||none|international_organization|
|international_organization_can_own_land|Can the international organization own land?||international_organization|boolean|
|international_organization_can_remove_land|Can we remove a location from the scope international organization?||none|international_organization|
|international_organization_has_internal_peace|Checks if no member country is in a direct war with another member country||international_organization|boolean|
|international_organization_has_law|Has the scope international organization enacted a policy for the supplied law?||international_organization|law|
|international_organization_has_laws|Has the scope international organization enacted a policy for the supplied law?||international_organization|boolean|
|international_organization_has_leader|Does the international organization have a leader country?||international_organization|boolean|
|international_organization_has_policy|Has the scope international organization enacted the supplied policy?||international_organization|policy|
|international_organization_leader_count|Checks how many leaders (defined as 'leaders' in the IO type) are currently present in the current international organization||international_organization|value|
|international_organization_leader_reign|Checks if the ruler of an international organization has ruled for x years||international_organization|value|
|international_organization_leader_reign_in_days|Checks if the ruler of an international organization has ruled for x days||international_organization|value|
|international_organization_lifetime|Checks if the international organization has existed for x years||international_organization|value|
|international_organization_lifetime_in_days|Checks if the international organization has existed for x days||international_organization|value|
|international_organization_locations_owned_percentage|The percentage of the locations of an international organization owned by a country||international_organization|value|
|international_organization_modifier_strength|Does the scoped international_organization have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|international_organization_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "international_organization_modifier_strength(<modifier key>)"|international_organization||
|international_organization_num_locations|Checks if an international organization has a certain amount of owned locations||international_organization|value|
|international_organization_population|Checks if an international organization has a certain population based on the locations it owns||international_organization|value|
|intrinsic_disease_resistance|Checks the intrinsic disease resistance in a location (e.g. from buildings)||location|value|
|io_within_diplomatic_range|Is the target international organization within diplomatic range?||international_organization|country|
|ironman|Checks if the game is running in ironman.||none|boolean|
|is_a_defender|Is the target country a defender in the war?||war|country|
|is_a_threat_for_us|Is the country views the target country as a threat?||country|country|
|is_accepted_in|If a culture is accepted in the target country?||culture|country|
|is_active_parliament|country has an active parliament called||country, international_organization|boolean|
|is_adjacent_to_lake|Check if a location is a adjacent to a lake||location|boolean|
|is_admiral|character is an admiral||character|boolean|
|is_admiral_of|Character is admiral of the target country.||character|country|
|is_adolescent|character is Adolescent||character|boolean|
|is_adult|character is Adult||character|boolean|
|is_ai|country is run by AI||country|boolean|
|is_alert_shown|Is the alert with the specified name shown?||none||
|is_alert_triggered|Is the alert with the specified name triggered?||none||
|is_alive|character is alive||character|boolean|
|is_allowed_for|Returns true if the current database object is allowed (but not necessarily visible) for the target country.||artist_type, avatar, building_type, cabinet_action, estate_privilege, formable_country, god, government_reform, heir_selection, law, levy_setup, mission, mission_task, parliament_agenda, parliament_issue, parliament_type, policy, production_method, regency_type, religious_aspect, road_type, unit_ability, unit_type|country|
|is_allowed_for_international_organization|Returns true if the current database object is available to the target international organization.||law, parliament_agenda, parliament_issue, parliament_type, policy|international_organization|
|is_already_merged|If a culture_group is already merged.||culture_group|boolean|
|is_an_attacker|Is the target country an attacker in the war?||war|country|
|is_annexing|Is the country annexing the specified country?||country|country|
|is_annexing_any_country|Is the country annexing any other country?||country|boolean|
|is_area_coastal_sea|is the area coastal sea or not?||area|boolean|
|is_area_fully_discovered|is the area fully discovered or not?||area|country|
|is_area_passable|is the area passable or not?||area|boolean|
|is_area_sea|is the area sea or not?||area|boolean|
|is_army|unit is Army||unit|boolean|
|is_art_destroyed|Check if art is destroyed or not||work_of_art|boolean|
|is_artist|character is Artist||character|boolean|
|is_artist_of|Character is artist of the target country.||character|country|
|is_at_max_level|Checks if a building is working at full capacity||building|boolean|
|is_at_war_with|Is the country at war with a specified country?||country|country|
|is_auto_raise_taxrate_for_all_estates|Check if all estates have auto raise taxrates?||country|boolean|
|is_available_for|Returns true if the current database object is available to the target country.||artist_type, avatar, building_type, cabinet_action, estate_privilege, formable_country, god, government_reform, heir_selection, law, levy_setup, mission, mission_task, parliament_agenda, parliament_issue, parliament_type, policy, production_method, regency_type, religious_aspect, road_type, unit_ability, unit_type|country|
|is_available_for_international_organization|Returns true if the current database object is available to the target international organization.||law, parliament_agenda, parliament_issue, parliament_type, policy|international_organization|
|is_being_annexed|Is the country being annexed by any other country?||country|boolean|
|is_being_annexed_by|Is the country getting annexed by the specified country?||country|country|
|is_being_explored|is the area being explored by a country?||area|country|
|is_bombard_phase|Check if a combat is currently in the bombard phase||combat|boolean|
|is_border|Check if a location borders another country||location|boolean|
|is_building_owned_by|Checks if a building is owned by a country||building|country|
|is_burgher_positive_deficit|Checks if a building location does not have negative burgher deficit||location|boolean|
|is_camera_in_zoom_level|Is camera in a specified zoom level? SMALL / MEDIUM / LARGE||none||
|is_capital|Check if a location is a capital||location|boolean|
|is_carrying_troops|unit is carrying troops||unit|boolean|
|is_child|character is Child||character|boolean|
|is_child_of|Is the character a child of the target character?||character|character|
|is_city|Check if a location is a city||location|boolean|
|is_civil_war_for|Is the current war a civil war for the target country?||war|country|
|is_close_relative|Is the character a close relative (Child, Parent, Sibling/Half-sibling, Nephew/Niece, Aunt/Uncle, Grandparent or Grandchild) of the target character?||character|character|
|is_coastal|Check if a location is coastal||location|boolean|
|is_colonial_overlord|Country is an overlord of a colonial subject||country|boolean|
|is_colonial_subject|Country is a type of colonial subject||country|boolean|
|is_colonial_top_overlord|Country is the top overlord of a colonial subject||country|boolean|
|is_connected_to|Check if a location is connected by land/strait to another location in the same country||location|location|
|is_consort|character is Consort||character|boolean|
|is_consort_of|Character is consort of the target country.||character|country|
|is_core_of|Is the location a core of the target country?||location|country|
|is_courtier|Character is a courtier and has no roles assigned||character|boolean|
|is_creating_cb_against|Checks if the current country scope is creating a casus belli against the target country.||country|country|
|is_creating_cb_of_type|Checks if the current country scope is creating a casus belli of the specified type against the target country.|is_creating_cb_of_type = { target = <country scope> type = <casus belli type> }|country||
|is_crossing|Check if a combat has any crossing (river, strait, sea landing||combat|boolean|
|is_currently_being_integrated|Check if a location is currently being integrated||location|boolean|
|is_cut_down_in_size_cb|is it a cut down in size CB||casus_belli|boolean|
|is_demanded_in_market|Check if the goods scope is demanded in the target market.||goods|market|
|is_demanded_in_market_by_buildings|Check if the goods scope is demanded in the target market by buildings.||goods|market|
|is_demanded_in_market_by_burgher_trades|Check if the goods scope is demanded in the target market by burgher trades.||goods|market|
|is_demanded_in_market_by_constructions|Check if the goods scope is demanded in the target market by constructions.||goods|market|
|is_demanded_in_market_by_pops|Check if the goods scope is demanded in the target market by pops.||goods|market|
|is_demanded_in_market_by_roads|Check if the goods scope is demanded in the target market by roads.||goods|market|
|is_demanded_in_market_by_trades|Check if the goods scope is demanded in the target market by trades.||goods|market|
|is_demanded_in_market_by_units|Check if the goods scope is demanded in the target market by units.||goods|market|
|is_discovered_by|Is the scope location/country discovered by the target country?||country, location|country|
|is_disloyal_subject|Is the country a disloyal subject?||country|boolean|
|is_dominant_country_of|Check if a country is the dominant country of a culture||country|culture|
|is_during_bankruptcy|country is having a bankruptcy||country|boolean|
|is_dynastic_descendant_of|Is the character a dynastic descendant of the target dynasty?||character|dynasty|
|is_dynasty_head|character is DynastyHead||character|boolean|
|is_east_of|Check if a location is east of another location||location|location|
|is_elector_in_international_organization|Checks if the country is an elector in the target international organization.||country|international_organization|
|is_eligible_heir|Checks if the character can be an eligible heir for the specified country||character|country|
|is_eligible_heir_baseline|Checks if the character can be an eligible heir for the specified country without checking the heir selection law||character|country|
|is_eligible_military_leader|Checks if the character can be an eligible military leader for the specified country||character|country|
|is_embargoed_by|Is the country embargoed by the specified country?||country|country|
|is_embargoing|Is the country embargoing the specified country?||country|country|
|is_embraced_for|Is the institution embraced by the target country?||institution|country|
|is_enemy_of|Is the country a enemy of a specified country?||country|country|
|is_enemy_of_international_organization|Is the country an enemy of the supplied international organization?||country|international_organization|
|is_exiled|unit is Exiled||unit|boolean|
|is_explorer|character is an explorer||character|boolean|
|is_explorer_of|Character is explorer of the target country.||character|country|
|is_export|Check if a trade is an export||trade|boolean|
|is_export_banned|Checks if export of specific goods is banned in this market||market|goods|
|is_female|character is Female||character|boolean|
|is_fighting_war_together_with|Is the country fighting a war together with a specified country?||country|country|
|is_food|Check if a goods is food||goods|boolean|
|is_foreign|Checks if a building can be built in foreign locations (not owned)||building_type|boolean|
|is_friendly_with|Is the country friendly with specified country?||country|country|
|is_full_capacity|Checks if a building is working at full capacity||building|boolean|
|is_full_expanded_rgo|Check if a location has its RGO fully expanded||location|boolean|
|is_fully_implemented_in|Checks if the current government reform/avatar/estate privilege / god/policy/law/cabinet action scope has been fully implemented in the specified country||avatar, cabinet_action, estate_privilege, god, government_reform, law, policy|country|
|is_gamestate_tutorial_active|Is the gamestate tutorial active? See save_progress_in_gamestate in tutorial_lesson_chains documentation.||none|boolean|
|is_general|character is a general||character|boolean|
|is_general_of|Character is general of the target country.||character|country|
|is_great_power|country is a great power||country|boolean|
|is_hegemon|country is a Hegemon||country|boolean|
|is_hegemon_type|Is the country a Hegemon of the specified type?||country|hegemony|
|is_heir|character is Heir||character|boolean|
|is_heir_of|Character is heir of the target country.||character|country|
|is_historical_rival_of|Is the country an historical rival of a specified country?||country|country|
|is_holy_site_for|Is the holy site relevant to the target religion?||holy_site|religion|
|is_hostile_with|Is the country hostile of specified country?||country|country|
|is_human|country is controlled by a human||country|boolean|
|is_immortal|character is immortal||character|boolean|
|is_implementable_in|Checks if the current government reform/avatar/estate privilege / god/policy/law/cabinet action scope can be implemented in the specified country. Does not check if it has already been implemented or not though.||avatar, cabinet_action, estate_privilege, god, government_reform, law, policy|country|
|is_import_banned|Checks if import of specific goods is banned in this market||market|goods|
|is_in_any_same_international_organization|Is the country in any same international organization as the target country?||country|country|
|is_in_list|Checks if a target in in a list||none||
|is_in_losing_war|Country is currently in a war with less than 0 war score.||country|boolean|
|is_in_same_international_organization|Is the country in the same international organization as the target country?|is_in_same_international_organization = { international_organization = <IO scope> target = <country> }|country||
|is_in_scripted_geography|Checks if the scope is part of the scripted geography on RHS scope|is_in_scripted_geography = <scripted geography scope>|area, continent, location, province_definition, region, sub_continent|scripted_geography|
|is_in_surplus_in_market|Gets the possible trade surplus of the scope goods in the target market.||goods|value|
|is_in_war|Is the target country in the war?||war|country|
|is_infant|character is Infant||character|boolean|
|is_integrating|Is the country integrating any of its owned locations in province?||country|province_definition|
|is_international_organization_annullable|Is the international organization able to be annulled by treaty?||international_organization|boolean|
|is_international_organization_unique|Is the international organization unique?||international_organization|boolean|
|is_key_in_global_variable_map|Checks if a target is a key in a global variable map|is_key_in_global_variable_map = { name = <global_variable_map> target = <key to check> }|none||
|is_key_in_local_variable_map|Checks if a target is a key in a local variable map|is_key_in_local_variable_map = { name = <local_variable_map> target = <key to check> }|none||
|is_key_in_variable_map|Checks if a target is a key in a variable map|is_key_in_variable_map = { name = <variable_map> target = <key to check> }|none||
|is_known_by_country|Checks if the country is known by the specified country||country|country|
|is_labourer_positive_deficit|Checks if a building location does not have negative labourer deficit||location|boolean|
|is_lacking_goods|Checks if a building is lacking goods||building|boolean|
|is_land|Check if a location is land||location|boolean|
|is_latest_road_type_for|Check if a road type is the latest one for a country||road_type|country|
|is_leader_of_international_organization|Is the country the Leader of the specified international organization?||country|international_organization|
|is_levy|subunit is levy||sub_unit|boolean|
|is_linked_to_foreign_building|Check if a pop is linked to a foreign building||pop|boolean|
|is_location_holy_site_for|Is the location a holy site for the target religion?||location|religion|
|is_locked|Check if a trade is locked||trade|boolean|
|is_locked_for|Returns true if the current database object is locked for the target country.||government_reform, heir_selection, law, parliament_type, policy|country|
|is_locked_for_international_organization|Returns true if the current database object is locked for the target international organization.||law, parliament_type, policy|international_organization|
|is_looted|Check if a location is looted||location|boolean|
|is_loyal|character is loyal to their ruler||character|boolean|
|is_major_reform|Checks if the government reform is major||government_reform|boolean|
|is_map_mode_active|Is map mode active?||none||
|is_market_center|Check if a location is a market center||location|boolean|
|is_married|character is Married||character|boolean|
|is_matrilineal_descendant_of|Is the character a dynastic descendant of the target dynasty via a matrilineal line??||character|dynasty|
|is_max_level|Checks if a building is at maximum level||building|boolean|
|is_member_of_international_organization|Is the country in the supplied international organization?||country|international_organization|
|is_member_of_international_organization_of_type|Is the country in an international organization of the specified type?|is_member_of_international_organization_of_type = { type = x target = <country> }|country||
|is_mercenary|subunit is Mercenary||sub_unit|boolean|
|is_mercenary_hired_by|Check if a mercenary is hired by a specific country||mercenary|country|
|is_mercenary_leader|character is a mercenary leader||character|boolean|
|is_mercenary_of|Character is mercenary of the target country.||character|country|
|is_mercenary_owned_by|Check if a mercenary is owned by a specific country||mercenary|country|
|is_merged_culture_group|If a culture has been merged from a culture group.||culture|boolean|
|is_merged_culture_group_of|If a culture has been merged from this specific culture group.||culture|culture_group|
|is_mining_rgo|Check if a location has a mining_rgo||location|boolean|
|is_movement_locked|unit is movement locked||unit|boolean|
|is_moving|unit is moving||unit|boolean|
|is_multiplayer_session|Is the current game session multiplayer?||none|boolean|
|is_naval_combat|Check if a combat is between navies on the sea||combat|boolean|
|is_navy|unit is Navy||unit|boolean|
|is_neighbor_of|Is the country or location a Neighbor to the specified country?||country, location|country|
|is_neighbor_of_international_organization|Is the country or location a neighbor to the specified international organization?||country, location|international_organization|
|is_neighbor_of_location|Check if a location is neighbour to another||location|location|
|is_neighbor_of_location_or_across_one_seazone|Check if a location is neighbour to another or just across a single seazone||location|location|
|is_neighbor_of_province_definition|Check if a province definition is neighbour to another||province_definition|province_definition|
|is_no_cb|is it no CB||casus_belli|boolean|
|is_no_cb_war|Checks if that war was started without any casus belli ('no cb')||war|boolean|
|is_not_profitable|Checks if a building is not profitable or not has prfot at all||building|boolean|
|is_on_opposite_sides|Check if the two countries are in opposing sides.|is_on_opposite_sides = { country = <country> target = <target> }|war||
|is_on_same_side|Check if the two countries are on the same side.|is_on_same_side = { country = <country> target = <target> }|war||
|is_opened|Checks if a building is opened||building|boolean|
|is_overlord|country is an overlord||country|boolean|
|is_overseas_for_owner|Check if a location or province is overseas for owber||location, province|boolean|
|is_ownable|Check if a location is ownable, i.e. not sea, lake or an impassable||location|boolean|
|is_owned_by_any_international_organization|Check if a location is owned by any international organization||location|boolean|
|is_owned_by_country|Returns true if the rebel is owned by the target country||rebels|country|
|is_owned_by_international_organization|Check if a location is owned by an international organization||location|international_organization|
|is_owned_or_owned_by_subjects_of|Check if the location is owned by the target country or its subjects||location|country|
|is_owned_or_owned_by_subjects_or_below_of|Check if the location is owned by the target country or its subjects or the subjects' subject||location|country|
|is_parent_of|Is the character a parent of the target character?||character|character|
|is_passable|Check if a location is passable||location|boolean|
|is_patrilineal_descendant_of|Is the character a dynastic descendant of the target dynasty via a patrilineal line??||character|dynasty|
|is_player_playstyle|Player has only one playstyle and is equal to MILITARY, ADMINISTRATIVE or DIPLOMATIC||country||
|is_port|Check if a location has a port||location|boolean|
|is_pregnant|character is Pregnant||character|boolean|
|is_primary_in|If a culture is a primary culture in the target country?||culture|country|
|is_primary_or_accepted_in|If a culture is a primary culture or accepted in the target country?||culture|country|
|is_produced_by_production_method|Returns true if the trade good is produced by the specified production method.||goods|production_method|
|is_produced_in_location_market|Checks if a specific goods in produced in the location market||location|goods|
|is_produced_in_market|Checks if a specific goods in produced in this market||market|goods|
|is_profitable|Checks if a building is profitable||building|boolean|
|is_projected_to_run_out_of_food_stockpile|Checks if a market is projected to run out of food||market|boolean|
|is_province_capital|Check if a location is the province capital||location|boolean|
|is_real_country|Checks if a country is a real country as opposed to rebels, mercenaries, pirates||country|boolean|
|is_rebel_country|Checks if a country is a rebel country created from a civil war||country|boolean|
|is_regency_extended|country has an extended regency?||country|boolean|
|is_regent|character is Regent||character|boolean|
|is_regent_of|Character is regent of the target country.||character|country|
|is_regiment|unit is regiment||sub_unit|boolean|
|is_relevant|Checks if an international organization is relevant to the supplied country||international_organization|country|
|is_religion_enabled|is the religion enabled or not||religion|boolean|
|is_religious_aspect_enabled|Checks if the input religious aspect is enabled for the country in scope. Meaning if the allow trigger in religious aspect DB object returns true.|c:ARA = { is_religious_aspect_enabled = religious_aspect:gomarism }|country|religious_aspect|
|is_religious_figure|character is religious figure||character|boolean|
|is_required_for_formable|Check if the location scope is required by the formable||location|formable_country|
|is_revolution_target|Check if the country is the target of the revolution||country|boolean|
|is_revolutionary|Check if the country is revolutionary||country|boolean|
|is_rival_of|Is the country a rival of a specified country?||country|country|
|is_river_crossing|Check if a combat has a river crossing||combat|boolean|
|is_ruler|character is Ruler||character|boolean|
|is_ruler_of|Character is ruler of the target country.||character|country|
|is_saint|Checks if a character is a saint in any religion||character|boolean|
|is_saint_of|Checks if a character is a saint in the specific religion||character|religion|
|is_same_gender|Is the character same gender as target character?||character|character|
|is_sea_landing|Check if a combat has an amphibious landing||combat|boolean|
|is_selectable_issue_for|Check if the parliament issue scope is selectable by country in the target international organization.|is_selectable_issue_for = { actor = <country scope> international_organization = <IO scope> }|parliament_issue||
|is_set|Checks whether the specified scope target has been set (includes being the null object)|is_set = from.owner.var:cool_var.mother|none||
|is_ship|subunit is Ship||sub_unit|boolean|
|is_sibling_of|Is the character a sibling of the target character?||character|character|
|is_situation_active|Checks if the target situation is currently active||none|situation|
|is_special_building|Checks if a building is special||building|boolean|
|is_spouse_of|Is the character a spouse of the target character?||character|character|
|is_starving|Check if a province is starving||province|boolean|
|is_strait_crossing|Check if a combat has a strait crossing||combat|boolean|
|is_subject|country is a subject||country|boolean|
|is_subject_of|Is the country a subject to the specified country?||country|country|
|is_subject_or_below_of|Is the country a subject of (or subject of a subject of) the specified country?||country|country|
|is_subject_type|Is the country a subject of the specified type?||country||
|is_subject_type_annullable|Check if a subject type can be annulled by a peace treaty||subject_type|boolean|
|is_subsidized|Checks if a building is subsidized||building|boolean|
|is_supported_by_character|Returns true if the rebel is supported by the target character||rebels|character|
|is_supported_by_country|Returns true if the rebel is supported by the target country||rebels|country|
|is_target_in_global_variable_list|Checks if a target is in a global variable list|is_target_in_global_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_target_in_local_variable_list|Checks if a target is in a local variable list|is_target_in_local_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_target_in_variable_list|Checks if a target is in a variable list|is_target_in_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_target_of_international_organization_of_type|Is the country a target of an international organization of the specified type?||country||
|is_threat_to|Current country scope is a threat and have a casus belli to the target country||country|country|
|is_tolerated_in|If a culture is tolerated in the target country?||culture|country|
|is_tooltip_with_name_open|Is the tooltip with the specified name open?||none||
|is_trade_cb|is it a trade CB||casus_belli|boolean|
|is_traded_in_market|Checks if a specific goods in traded in this market||market|goods|
|is_tutorial_active|Is the tutorial active?||none|boolean|
|is_tutorial_lesson_active|Is this the current tutorial lesson?|is_tutorial_lesson_active = reactive_advice_succession|none||
|is_tutorial_lesson_chain_completed|Has the tutorial lesson chain with the specified key been finished?||none||
|is_tutorial_lesson_completed|has the tutorial lesson with the specified name been finished?||none||
|is_tutorial_lesson_step_completed|Has the tutorial lesson step been finished?|is_tutorial_lesson_step_completed = lesson_key:step_key|none||
|is_unified_culture|Check if a location has culture unified with the owner||location|boolean|
|is_unique_reform|Checks if the government reform is unique||government_reform|boolean|
|is_unit_locked|Check if a Unit is locked||unit|boolean|
|is_upgradeable|Checks if a building is upgradeable||building_type|boolean|
|is_upgraded_level|Checks if a building could have been upgraded||building_type|boolean|
|is_upper_class|Check if a pop is upper class or not||pop|boolean|
|is_used_by_production_method|Returns true if the trade good is used by the specified production method.||goods|production_method|
|is_valid_colonial_charter|is this colonial charter valid, or blocked by a recognised claim?||country|province_definition|
|is_valid_for_exploration|character is valid for an exploration||character|boolean|
|is_value_in_global_variable_map|Checks if a target is a value in a global variable map|is_value_in_global_variable_map = { name = <global_variable_map> target = <value to check> }|none||
|is_value_in_local_variable_map|Checks if a target is a value in a local variable map|is_value_in_local_variable_map = { name = <local_variable_map> target = <value to check> }|none||
|is_value_in_variable_map|Checks if a target is a value in a variable map|is_value_in_variable_map = { name = <variable_map> target = <value to check> }|none||
|is_visible_for|Returns true if the current database object is visible (but not necessarily allowed) to the target country.||artist_type, avatar, building_type, cabinet_action, estate_privilege, formable_country, god, government_reform, heir_selection, law, levy_setup, mission, mission_task, parliament_agenda, parliament_issue, parliament_type, policy, production_method, regency_type, religious_aspect, road_type, unit_ability, unit_type|country|
|is_visible_for_international_organization|Returns true if the current database object is available to the target international organization.||law, parliament_agenda, parliament_issue, parliament_type, policy|international_organization|
|is_war_leader_of|Checks if the current country scope is a war leader of the target war||country|war|
|is_widgetid_open|Is the widget with the specified `widgetid` open (visible and not animating)? The fastest and safest way to check. (replaces old `is_widget_open` functionality, which operated on names.)||none||
|join_organization_ai_desire|Returns the AI desire to join the specified target international organization.|join_organization_ai_desire = { international_organization = <IO scope> value = <script_value> } or join_organization_ai_desire(<IO scope>)|country|value|
|join_war_reason|Checks the reason for a country joining a war.||war||
|karma|How much karma does the country/IO have?||country, international_organization|value|
|karma_percentage|How high the percentage of the current karma compared to the maximum does the country/IO have?||country, international_organization|value|
|knows_about_institution|Checks if a country has knows about an institution||country|institution|
|knows_country|Checks if the country knows of the specified country||country|country|
|language_percentage_in_country|The percentage of speakers of a specific language in the current country||country|value|
|language_power|How much power does the language has (percent of best)?||dialect, language|value|
|law_enabled_to_international_organization|Can we select a policy for a law in the scope international organization?||international_organization|law|
|law_is_locked_in_international_organization|Is a law locked in the scope international organization?||international_organization|law|
|law_visible_to_international_organization|Can we see a policy for a law in the scope international organization?||international_organization|law|
|leader_change_method|Check if the international organization has the specified leader changed method (rotation/vote/lottery/none)||international_organization||
|leader_change_trigger_type|Check if the international organization has the specified leader changed trigger type (rulerchang/timed/none)||international_organization||
|leader_special_status_power|Get the special status power of all special statuses with the 'leader' trait||international_organization|value|
|leader_special_status_power_fraction|Get the fraction of the special status power of all special statuses with the 'leader' trait||international_organization|value|
|leader_type|Check if the international organization has the specified leader type (character/country/none)||international_organization||
|legitimacy|How much legitimacy does the country/IO have?||country, international_organization|value|
|legitimacy_percentage|How high the percentage of the current legitimacy compared to the maximum does the country/IO have?||country, international_organization|value|
|liberty_desire|Checks the amount of liberty desire a country has||country|value|
|list_size|Checks the size of a list|list_size = { name = <list_name> value >= <script_value> }|none|value|
|liturgical_language_utility|Utility of a liturgical language accorting to Ai||dialect, language|value|
|loan_amount|Checks the amount of a loan||loan|value|
|loan_interest|Checks the interest of a loan||loan|value|
|local_control|Checks if a location has a certain control||location|value|
|local_cultural_unity|Checks the percentage the dominant-culture has in a location||location|value|
|local_estate_power|Checks the raw local estate power in location||location|value|
|local_political_power_fraction|Checks the fraction this location has of the total political power of a country||location|value|
|local_relative_estate_power|Checks the relative local estate power in location||location|value|
|local_religious_unity|Checks the percentage the dominant-religion has in a location||location|value|
|local_variable_list_size|Checks the size of a local variable list|local_variable_list_size = { name = <variable_name> value >= <script_value> }|none||
|local_variable_map_size|Checks the size of a local variable map|local_variable_map_size = { name = <variable_name> value >= <script_value> }|none||
|location_art_quality|Checks the total art quality in a location||location|value|
|location_building_level|Checks if a location has a building type at a certain level (with optional owner)||location|value|
|location_can_be_added_to_international_organization|Can we add a location to the scope international organization?||international_organization|location|
|location_can_be_removed_from_international_organization|Can we remove a location from the scope international organization?||international_organization|location|
|location_counter|Checks if the province/province_defintion/area/region / subcontinent/continent/scripted_geography has this amount of location||area, continent, province, province_definition, region, scripted_geography, sub_continent|value|
|location_key|Checks if a location is the specific one (from named_location)||location||
|location_maritime_merchant_power|gets the maritime merchant power for a country in the scope location||location|value|
|location_maritime_presence_power|gets the maritime presence power for a country in the scope location.|location_maritime_presence_power = { country = <country scope> value <operator> <number> }|location|value|
|location_max_population|Checks if a location has a certain pixel count||location|value|
|location_max_winter_level|Checks the maximum winter level of a location||location||
|location_modifier_strength|Does the scoped location have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|location_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "location_modifier_strength(<modifier key>)"|location||
|location_net_building_profit|Checks the net profit from buildings in a location||location|value|
|location_num_holy_sites|Number of holy sites in the location||location|value|
|location_num_works_of_art|Checks if a location has a certain number of works of art||location|value|
|location_peace_cost|gets the peace cost for the location according to giver and taker countries|usage in trigger: location_peace_cost = { giver = <country> taker = <country> value <operand> <threshold> #ex: value < 10 } usage in scripted value: location_peace_cost(<giver>\|<taker>)|location|value|
|location_population_percentage|Checks if a location has a certain percentage of population capacity||location|value|
|location_privateer_power|gets the maritime privateeer power for a country in the scope location||location|value|
|location_progress_for_formable|Checks the progress of the country scope to form the specified formable in percentage.|location_progress_for_formable = { formable_country = <formable scope> value = <script_value> } or location_progress_for_formable(<formable scope>)|country|value|
|location_size|Checks if a location has a certain pixel count||location|value|
|location_tax_base|Checks the tax-base of a location||location|value|
|location_unemployed_population_for_building_type|Checks if a location has a certain unemployed population for the supplied building type (with optional owner)||location|value|
|location_within_range|Checks if a location has a certain population within range||location|country|
|location_works_of_art_star_rating|Checks if a country has a certain amount of work of arts||location|value|
|long_term_trigger_currency_utility|Checks the AI utility of adding an amount of a certain trigger every month to the scoped object|long_term_trigger_currency_utility = { trigger = <trigger> size = <size> target = <optional target> value >= <script_value> }|country|value|
|lowest_prosperity|Find the location in a province with the lowest prosperity||province|value|
|lowest_war_score|Checks the lowest war score of ongoing wars||country|value|
|manpower|How much Manpower does the country/IO have?||country, international_organization|value|
|manpower_percentage|Checks the percentage of manpower a country has compared to its maximum||country|value|
|market_access|Checks if a location has certain market access||location|value|
|market_food|Checks how much food is in the market stockpile||market|value|
|market_food_deficit|Checks how much food is missing in the market||market|value|
|market_food_percentage|Checks how much food is in the market stockpile percentage wise||market|value|
|market_food_traded|Checks how much food is traded in the market||market|value|
|market_max_food|Checks how much food can be stockpiled in the market||market|value|
|market_monthly_food_balance|Checks what the food balance is in the market||market|value|
|market_population|Checks how many pops are in the market||market|value|
|market_possible_goods_trade_surplus|gets the possible trade surplus for the goods in the scope market||market|value|
|max_control|Checks the max control in a location||location|value|
|max_countries_with_special_status|gets the max number of countries with a specific special status in an international organization||international_organization|value|
|max_garrison_strength|Checks the max garrison strength of the location in scope||location|value|
|max_manpower|Checks if a country has a certain Max manpower||country|value|
|max_possible_candidates|Maximum number of candidates for the heir selection.i.e. the number of choices the player will have when an election occurs|max_possible_candidates <operator> <amount>|heir_selection|value|
|max_religious_aspects|Checks the amount of church aspects the religion has||religion|value|
|max_rgo_workers|Checks if a location has a certain max number of RGO workers||location|value|
|max_sailors|Checks if a country has a certain Max Sailors||country|value|
|max_sects|number of sects available per country from the scope religion||religion|value|
|mercenary_has_owner|Check if a mercenary has an owner||mercenary|boolean|
|mercenary_modifier_strength|Does the scoped mercenary have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|mercenary_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "mercenary_modifier_strength(<modifier key>)"|mercenary||
|merchant_capacity|gets the market merchant capacity for a country in the scope market||market|value|
|merchant_power_in_market|gets the market merchant power for a country in the scope market||market|value|
|migration_attraction|Checks if a location has a certain migration_attraction||location|value|
|mil|The mil ability of the character||character|value|
|military_strength|Checks the total military strength (max manpower, army size, levy power) of a country||country|value|
|military_tech_level|Checks if a country has a certain level of military tech||country|value|
|mission_completed|Checks if the country has completed the mission.||country|mission|
|mission_task_bypassed|Checks if the country has bypassed the mission task.||country|mission_task|
|mission_task_completed|Checks if the country has completed the mission task.||country|mission_task|
|modifier_utility|Checks the AI utility of a modifier||avatar, character, country, god, government_reform, international_organization, location, policy, province, religion, religious_aspect, religious_school, unit|value|
|modifier_utility_include_locations|Checks the AI utility of a modifier with location checks||avatar, character, country, god, government_reform, international_organization, location, policy, province, religion, religious_aspect, religious_school, unit|value|
|monthly_balance|Checks the monthly balance of a country||country|value|
|monthly_conversion|Checks if a location has an potential conversion of X per month||location|value|
|monthly_cost|Checks the monthly cost of a mercenary||mercenary|value|
|monthly_income_total|Checks if a country has a certain income||country|value|
|monthly_income_trade_and_tax|Checks if a country has a certain trade and tax income||country|value|
|monthly_manpower|Checks if a country has a certain monthly manpower||country|value|
|monthly_sailors|Checks if a country has a certain monthly Sailors||country|value|
|monthly_trade_income|Checks if a country has a certain income from trade||country|value|
|months_between_leader_changes|Checks if a country has a specific reform||international_organization|value|
|months_left|Checks the months left of loan||loan|value|
|months_since_last_parliament_called|Checks how many months its been since the country / international organization last called a parliament||country, international_organization|value|
|months_since_peace|Checks how many months its been since a country was at peace||country|value|
|months_since_war|Checks how many months its been since a country was at War||country|value|
|morale_percentage|How many percent morale does this unit have???||unit|value|
|nand|a negated AND trigger||none||
|naval_range|The naval range of the country||country|value|
|navy_maintenance|What is the xx position (0-1) the country has?||country|value|
|navy_size|Checks if a country has a certain amount of ships||country|value|
|navy_size_percentage|Checks if a country has a certain percentage of ships compared to expected size||country|value|
|navy_tradition|How much navy tradition does the country/IO have?||country, international_organization|value|
|navy_tradition_percentage|How high the percentage of the current navy tradition compared to the maximum does the country/IO have?||country, international_organization|value|
|need_reforms|religion needs reforms||religion|boolean|
|needs_opinion_with|Determines if a country needs X more relations with another nation.|needs_opinion_with = { target = <country> value <comparator> <script_value> }|country|value|
|nor|a negated OR trigger||none||
|not|negates content of trigger||none||
|num_adult_capable_characters|Checks if a country has a certain amount of adult characters who can do cabinet or military stuff||country|value|
|num_affected_locations|How many locations are affected?||disease_outbreak|value|
|num_army_constructions|Check how many army_constructions a location has||location|value|
|num_artists|Checks if a country has a certain amount of artists||country|value|
|num_avatars|Checks if a country has a certain amount of avatars||country|value|
|num_buildings|Checks if a location has a certain amount of buildings||location|value|
|num_cardinals|Checks if a country has a certain amount of Cardinals||country|value|
|num_characters|Checks if a country has a certain amount of living characters||country|value|
|num_civil_constructions|Check how many civil_constructions a location has||location|value|
|num_colonial_charters|Checks if a country has a certain amount of colonial charters||country|value|
|num_countries_in_religion|number of countries in the religion||religion|value|
|num_countries_with_special_status|gets the number of countries with a particular special status in an international organization||international_organization|value|
|num_embraced_institutions|Checks if a country has a certain number of institutions embraced||country|value|
|num_explorations|Checks if a country has a certain amount of Explorations||country|value|
|num_foreign_buildings|Checks if a location has a certain amount of foreign buildings||location|value|
|num_forts|Checks if a country has a certain amount of forts||country|value|
|num_known_institutions|Checks if a country knows a certain number of institutions||country|value|
|num_loans|Checks if a country has a certain amount of loans||country|value|
|num_locations|Checks if a country has a certain amount of owned locations||country|value|
|num_locations_owned_or_owned_by_subjects|Checks if a country or its direct subjects has a certain amount of owned locations||country|value|
|num_locations_owned_or_owned_by_subjects_or_below|Checks if a country, its subjects or its subjects' subjects has a certain amount of owned locations||country|value|
|num_navy_constructions|Check how many navy_constructions a location has||location|value|
|num_of_active_parliament_agendas|Check how many parliament agendas are currently available to the country or international organization.||country, international_organization|value|
|num_of_advances_researched|Checks how many advances a country currently has researched.||country|value|
|num_of_children|The number of children of the character||character|value|
|num_of_diplomats|Checks if a country has an amount of diplomats||country|value|
|num_of_electors|Checks how many electors the international organization has||international_organization|value|
|num_of_locations_owned_by_io|Checks if a country has an amount of locations owned by certain IO||country|value|
|num_of_markets_with_merchants|Checks if a country has merchants in the specified amount of markets.||country|value|
|num_of_non_rural|Checks if a country has an amount of towns and cities||country|value|
|num_of_non_rural_ports|Checks if a country has an amount of non-rural ports||country|value|
|num_of_ports|Checks if a country has an amount of ports||country|value|
|num_of_rebel_characters|Get the amount of characters which support the rebel||rebels|value|
|num_of_rebel_supporters|Get the amount of countries which support the rebel||rebels|value|
|num_of_religious_aspects|Gets the total amount of church aspects in the country||country|value|
|num_of_spouses|The number of spouses of the character||character|value|
|num_of_trades|Checks if a country has an amount of trades active||country|value|
|num_of_traits|The number of traits the character has||character|value|
|num_of_traits_of_category|The number of traits of a specified category the character has.|num_of_trait_by_category(<trait_category>) or num_of_trait_by_category = { type = <trait_category> value <comparator> <integer> }|character|value|
|num_open_reform_slots|Checks if a country has a certain amount of open government reform slots||country|value|
|num_owned_foreign_buildings_in_location|The number of foreign buildings in a location owned by a count||location|value|
|num_possible_privileges|Checks if the scope country or estate has a certain amount of privileges||country, estate|value|
|num_possible_rivals|Checks if a country has a certain amount of possible rivals||country|value|
|num_privileges|Checks if the scope country or estate has a certain amount of privileges||country, estate|value|
|num_province_definitions_in_area|Checks if an area has a certain amount of province definitions||area|value|
|num_provinces|Checks if a country has a certain amount of provinces||country|value|
|num_rebels|Checks if a country has a certain amount of Rebels||country|value|
|num_reforms|Checks if a country has a certain amount of government reforms||country|value|
|num_regiments|Checks if a country has a certain amount of regiments||country|value|
|num_relations_above_limit|Amount above relations limit||country|value|
|num_rivals|Checks if a country has a certain amount of rivals||country|value|
|num_roads|Check how many roads a location has||location|value|
|num_subjects|Checks the total number of subjects of a country||country|value|
|num_subunits|How many sub units does this unit have?||unit|value|
|num_union_countries|Return the number of countries under any union ruled by the scoped dynasty||dynasty|value|
|num_unions|Return the number of unions ruled by the scoped dynasty||dynasty|value|
|num_works_of_art|Checks if a country has a certain number of works of art||country|value|
|offensive_alliance_strength|Strength of an offensive alliance, including the nation with all countries giving offensive support and those that can be called in for offensive wars||country|value|
|offer_relation_acceptance|How high is the target country's AI value of accepting the scripted relation offered by the current country scope?|offer_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "offer_relation_acceptance(<scripted relation type>\|<country>)"|country|value|
|only_allowed_overlord_court_language|Check if a subject type only allows use of the overlord's court language||subject_type|boolean|
|only_allowed_overlord_primary_culture|Check if a subject type only allows use of the overlord's primary culture||subject_type|boolean|
|only_allowed_overlord_primary_or_kindred_culture|Check if a subject type only allows use of the overlord's primary or kindred culture||subject_type|boolean|
|opinion|is the country's opinion of the target greater or equal than the value?|opinion = { target = X value <operator> Y or value = { min max } }|country|value|
|opinion_difference_between|Get the opinion of the current country scope against the first target country and subtract it with the opinion the current scope has of the second country.|opinion_difference_between = { first = <country> second = <country> value = <script_value> } or opinion_difference_between(<country>\|<country>)|country|value|
|or|at least one entry inside trigger must be true||none||
|organization_strength_relative_to_country|Gets the relative strength of the scope organization to the supplied country|organization_strength_relative_to_country(<target>\|<bool exclude_target>) or organization_strength_relative_to_country = { target = <country link> value <operator> <amount> exclude_target = <bool> }|international_organization|value|
|overlord_can_build_markets|Check if a subject type allows the overlord to build markets||subject_type|boolean|
|overlord_can_destroy_markets|Check if a subject type allows the overlord to destroy markets||subject_type|boolean|
|overlord_can_enforce_peace_on_subject|Check if a subject type allows an overlord to enforce peace on a subject||subject_type|boolean|
|own_entire_area|Does the country own all locations in area?||country|area|
|own_entire_province|Does the country own all locations in province?||country|province_definition|
|owned_by_or_its_subjects|Checks if the geographic scope is completely owned by the target country or its subjects.||area, continent, province_definition, region, sub_continent|country|
|owns|Does the country own a specific location?||country|location|
|owns_any_foreign_buildings_in|Does the country own any foreign buildings in the target country?||country|country|
|owns_most_foreign_buildings_in_location|Does the country own the majority of the foreign buildings in the target location?||country|location|
|owns_or_has_subject_in|country has a presence in the geography supplied?||country||
|owns_or_non_sovereign_subject_owns|Does the country or any of its direct non-sovereign subjects own a specific location?||country|location|
|parliament_issue_chance|The chance an issue will be selected||country, international_organization|value|
|parliament_issue_support|The current support in parliament for an issue||country, international_organization|value|
|parliament_issue_will_pass|Check if the parliament issue of the country / international in debate will pass||country, international_organization|boolean|
|parliament_type_enabled_in_international_organization|Is a parliament type enabled in the scope international organization?||international_organization|parliament_type|
|parliament_type_is_enabled_in|Is a parliament type enabled in the scope country?||country|parliament_type|
|parliament_type_is_locked_in|Is a parliament type locked in the scope country?||country|parliament_type|
|parliament_type_is_locked_in_international_organization|Is a parliament type locked in the scope international organization?||international_organization|parliament_type|
|parliament_type_utility|Utility of a parliament type that can subtract the utility of current parliament modifiers|parliament_type_utility(<type>\|<bool>) or parliament_type_utility = { parliament_type = <type> subtract_current = <bool> value <operator><threshold> }|country|value|
|parliament_type_visible_in|Can we see a parliament type in the scope country?||country|parliament_type|
|parliament_type_visible_in_international_organization|Can we see a parliament type in the scope international organization?||international_organization|parliament_type|
|payment_contribution|Gets how much the country has to pay for the specified IO and payment type.|payment_contribution = { international_organization = <> payment = <> }|country|value|
|payment_maintenance|gets the payment maintenance level for a country in an international organization.|payment_maintenance = { international_organization = <> payment = <> }|country|value|
|peace_treaty_antagonism|Get how much antagonism the specified peace treaty type would cause for the current country scope against the target country.|peace_treaty_antagonism = { peace_treaty = <scripted peace treaty scope> loser = <losing country scope> [target = <thing>] value <comparator> <real> } or "peace_treaty_antagonism(<peace treaty scope>\|<loser>\|<thing>)"|country||
|peace_treaty_war_score_cost|Get how much war score the specified peace treaty type would cost for the current country scope against the target country.|peace_treaty_war_score_cost = { peace_treaty = <scripted peace treaty scope> loser = <losing country scope> [target = <thing>] value <comparator> <real> } or "peace_treaty_war_score_cost(<peace treaty scope>\|<loser>\|<thing>)"|country||
|peasant_enfranchisment|Checks the level of peasant enfranchisement in a location||location|value|
|player_proficiency|Is player proficiency equal to NOVICE, EXPERIENCED, ADVANCED or EXPERT?||country||
|player_proficiency_greater|Is player proficiency greater than NOVICE, EXPERIENCED, ADVANCED or EXPERT?||country||
|player_proficiency_greater_eq|Is player proficiency greater or equal to NOVICE, EXPERIENCED, ADVANCED or EXPERT?||country||
|player_proficiency_less|Is player proficiency less than NOVICE, EXPERIENCED, ADVANCED or EXPERT?||country||
|player_proficiency_less_eq|Is player proficiency less or equal to NOVICE, EXPERIENCED, ADVANCED or EXPERT?||country||
|policy_enabled_to_international_organization|Can we enact a policy in the scope international organization?||international_organization|policy|
|policy_has_ai_join_reason|Check if the policy has an ai join reason to begin with||policy|boolean|
|policy_has_ai_keep_value|Check if the policy has an ai keep value to begin with||policy|boolean|
|policy_has_ai_propose_value|Check if the policy has an ai proposal value to begin with||policy|boolean|
|policy_has_ai_vote_value|Check if the policy has an ai vote value to begin with||policy|boolean|
|policy_is_locked_in_international_organization|Is a policy locked in the scope international organization?||international_organization|policy|
|policy_level|Check the defined level of the policy||policy|value|
|policy_visible_to_international_organization|Can we see a policy in the scope international organization?||international_organization|policy|
|pop_character_chance|How likely are characters to spawn from this pop?||pop|value|
|pop_knows_about_goods|Checks if a pop knows about a goods enough to demand it||pop|goods|
|pop_literacy|How literate is this pop?||pop|value|
|pop_satisfaction|How satisfied is this pop?||pop|value|
|pop_size|How big is this pop?||pop|value|
|pop_type_percentage_in_country|The percentage of the specific pop type in the current country||country|value|
|pop_type_population_in_country|The number of the specific pop type in the current country||country|value|
|population|Checks if the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography has a certain population||area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|population_in_area|gets the amount of population in an area||area|value|
|population_with_traits|Checks if the location has x amount of population with specific pop traits.|population_with_traits = { limit = { <pop triggers> } OR scripted_trigger = <scripted trigger key> value = <script_value> } or population_with_traits(<scripted trigger key>)|location|pop|
|possible_military_leaders|Checks if a country has a certain amount of possible military leaders||country|value|
|power|The power of an estate||estate|value|
|power_projection|Checks if a country has a power projection||country|value|
|prestige|How much prestige does the country/IO have?||country, international_organization|value|
|prestige_percentage|How high the percentage of the current prestige compared to the maximum does the country/IO have?||country, international_organization|value|
|prev_antagonism_towards_this|Gets the previous scope country's antagonism towards the current scope country||country|value|
|prev_opinion_of_this|Gets the previous scope country's opinion of the current scope country||country|value|
|prev_trust_of_this|Gets the previous scope country's trust of the current scope country||country|value|
|price_in_market|Gets the price of the scoped goods in the supplied market|price_in_market = { market = <market_name> value >= <script_value> }|goods|value|
|prisoner_strength|gets the total strength of the prisoners in the unit||unit|value|
|privateer_power|How much power does a privateer has?||privateer|value|
|privateer_utility|How useful is a privateer here?||area|value|
|production_method_profit|Checks production method profit||production_method|value|
|proper_culture_nobles|Checks the proportion of your population that is primary or accepted culture nobles||country|value|
|prosperity|Checks if a location has a certain prosperity||location|value|
|province_army_levy_size|Total army levies that can be had from a province||province|value|
|province_average_control|Checks the average_control of a province||province|value|
|province_average_development|Checks the average_development of a province||province|value|
|province_average_integration|Checks the average_integration of a province||province|value|
|province_cabinet_action|Checks if a cabinet action role affects a province||cabinet_action|boolean|
|province_cultural_unity|Checks the cultural_unity of a province||province|value|
|province_food|Checks the food of a province||province|value|
|province_food_percentage|Checks the food percentage of capacity in a province||province|value|
|province_max_food|Checks the maximum amount of food the province can have||province|value|
|province_modifier_strength|Does the scoped province have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|province_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "province_modifier_strength(<modifier key>)"|province||
|province_monthly_food_production|Checks how much food the province produces per month||province|value|
|province_navy_levy_size|Total navy levies that can be had from a province||province|value|
|province_population|Checks if a Province has a certain population||province|value|
|province_possible_institutions|Checks the number of institutions that can be promoted in a province||province|value|
|province_prosperity|Checks if a Province has a certain level of average prosperity||province|value|
|province_rebel_progress|Checks if a Province has a certain rebel progress||province|value|
|province_religious_unity|Checks the religious_unity of a province||province|value|
|province_satisfaction|Checks if a Province has a certain level of average satisfaction||province|value|
|province_tax_base|Checks if a Province has a certain total tax base||province|value|
|proximity|Checks the proximity to owner capital in a location||location|value|
|purity|How much purity does the country/IO have?||country, international_organization|value|
|purity_percentage|How high the percentage of the current purity compared to the maximum does the country/IO have?||country, international_organization|value|
|random_integer|Uniformly random integer between 0 and 2^31-1. It will be the same if evaluated on the same scope and day.||none|value|
|rank_index|Checks if a location has a Location Rank of a certain index||location|value|
|raw_material_amount|Check how many locations in the province_defintion/area / region/subcontinent/continent produce the specified raw material.|raw_material_amount = { goods = <goods scope> value = <script_value> } or raw_material_amount(<goods scope>)|area, continent, market, province_definition, region, sub_continent|value|
|raw_material_occurrence|Check how many locations world wide produce this raw material||goods|value|
|raw_material_output|Check how much raw material the scope location produces.||location|value|
|rebel_category|Checks if a rebel is of a certain category||rebels||
|rebel_estate_type|Checks if the rebel is from the specified estate type||rebels|estate_type|
|rebel_last_months_progress|Check last month's progress of a rebel||rebels|value|
|rebel_locations|Get the total amount of locations supporting the rebel||rebels|value|
|rebel_modifier_strength|Does the scoped rebel have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|rebel_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "rebel_modifier_strength(<modifier key>)"|rebels||
|rebel_name_key|if a rebel has a specific name key||rebels||
|rebel_progress|Check the progress of a rebel||rebels|value|
|rebel_size|Get the total amount of population supporting the rebel||rebels|value|
|receives_fleet_basing_rights_from|Does the scope country receive fleet basing rights from the specified country?||country|country|
|receives_food_access_from|Does the scope country receive food access from the specified country?||country|country|
|receives_isolation_exemption_from|Does the scope country receive a trade isolation exemption from the specified country?||country|country|
|receives_military_access_from|Does the scope country receive military access from the specified country?||country|country|
|receiving_scripted_relation|Checks for receiving scripted relation.|receiving_scripted_relation = { target = country type = <scripted type> }|country||
|receiving_scripted_relation_of_type|Checks if that scripted relation is received by the country scope from any other country.||country|relation_type|
|reform_desire|Checks the reform desire of the religion||religion|value|
|regular_army_size|Checks if a country has a certain army size of regulars (maximum strength)||country|value|
|regular_navy_size|Checks if a country has a certain navy size of regular ships||country|value|
|relative_defensive_alliance_strength|Gets the relative strength of the scope country including defensive alliances to the supplied one|relative_defensive_alliance_strength(<target>) <operator> <script_value> OR relative_defensive_alliance_strength = { target = <country scope> value <operator> <script_value> }|country|value|
|relative_military_strength|calculates the relative military strength of the scope country to the target.|relative_military_strength = { target = <country scope> value <operator> <script_value> or value = { min max } }|country|value|
|relative_raw_material_price|Checks the price of a location's raw material in its market as a percentage of the base price of that material||location|value|
|relative_strength|Gets the relative strength of the scope country to the supplied one|relative_strength(<target>) or relative_strength = { target = <country link> value <operator> <amount> }|country|value|
|release_only|Checks if the game is in release mode or not.||none|boolean|
|relevant_countries|Do we have any diplomatic action with the target country?||country|country|
|religion_group_percentage|Gets the percentage of the population that follow a particular religion group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_group_population_percentage = { religion_group = <religion group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|religion_group_percentage_in_country|The percentage of a specific religion group in the current country||country|value|
|religion_group_population|Gets the absolute number of the population that follow a particular religion group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_group_population = { religion_group = <religion group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|religion_modifier_strength|Does the scoped religion have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|religion_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "religion_modifier_strength(<modifier key>)"|religion||
|religion_percentage|Gets the percentage of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_population_percentage = { religion = <religion> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|religion_percentage_in_country|The percentage of a specific religion in the current country||country|value|
|religion_population|Gets the absolute number of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_population = { religion = <religion> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|value|
|religion_population_in_country|The number of pops with a specific religion in the current country||country|value|
|religious_figure_type|Checks if a character is a specific type of religious figure||character||
|religious_influence|How much religious influence does the country/IO have?||country, international_organization|value|
|religious_influence_percentage|How high the percentage of the current religious influence compared to the maximum does the country/IO have?||country, international_organization|value|
|religious_unity|Checks the fraction of the population sharing the country's religion||country|value|
|religious_view|does the Religion have the specified opinion of the target?||religion||
|relocate_market_utility|Utility of relocating a market|relocate_market_utility(<location>,<location>) or relocate_market_utility = { location = <location> new_location = <location> value <operator><threshold> }|country|value|
|remaining_debt|Checks the remaining debt of a loan||loan|value|
|remaining_parliament_days|Checks how many days are left in the parliament of the country / international organization before it concludes. Returns -1 when there is no parliament active.||country, international_organization|value|
|remove_static_modifier_utility|Checks the AI utility of removing a static modifier from the scoped object|remove_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|character, country, location|value|
|republican_tradition|How much republican_tradition does the country/IO have?||country, international_organization|value|
|republican_tradition_percentage|How high the percentage of the current republican_tradition compared to the maximum does the country/IO have?||country, international_organization|value|
|request_relation_acceptance|How high is the target country's AI value of accepting the scripted relation requested by the current country scope?|request_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "request_relation_acceptance(<scripted relation type>\|<country>)"|country||
|requires_goods|Returns true if the production method requires the specified trade good.||production_method|goods|
|requires_vote|Does the law require a vote?||law|boolean|
|research_progress|Checks the progress of the current research in the country||country|value|
|resolution_is_active|Is the resolution currently being debated in the scope international organization/situation?||international_organization, situation|resolution|
|resolution_opinion|Gets the current scope country's opinion of a resolution.|resolution_opinion(<IO>\|<resolution>\|<vote>) <operator> <script_value> OR resolution_opinion = { international_organization = <international organization> resolution = <resolution> vote = <vote scope> value <operator> <script_value> }|country|value|
|reverse_country_interaction_acceptance|How high is the current country's AI value of accepting the country interaction done by the specified country scope? Always return 0 if the scope is a player|reverse_country_interaction_acceptance = { type = <country interaction> target = <country> value = <script_value> } or reverse_country_interaction_acceptance(<country interaction>\|<country>)|country|value|
|reverse_cultural_view|does the target have the specified opinion of the culture?|reverse_cultural_view = { target = <target culture> value <operator> <script_value> }|culture||
|reverse_offer_relation_acceptance|How high is the current country's AI value of accepting the scripted relation offered by the specified country scope?|reverse_offer_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "reverse_offer_relation_acceptance(<scripted relation type>\|<country>)"|country||
|reverse_religious_view|does the target have the specified opinion of the Religion?||religion||
|reverse_religious_view_impact|Reverse opinion impact of a particular religion on another|"reverse_religious_view_impact(<religion link>)" or reverse_religious_view_impact = { religion = <religion link> value <operator> <amount> }|religion||
|reverse_request_relation_acceptance|How high is the current country's AI value of accepting the scripted relation requested by the specified country scope?|reverse_request_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "reverse_request_relation_acceptance(<scripted relation type>\|<country>)"|country||
|reverse_school_opinion|does the target have the specified opinion of the school?||religious_school||
|rgo_workers|Checks if a location has a certain number of RGO workers||location|value|
|righteousness|How much righteousness does the country/IO have?||country, international_organization|value|
|righteousness_percentage|How high the percentage of the current righteousness compared to the maximum does the country/IO have?||country, international_organization|value|
|rite_power|How much rite power does the country/IO have?||country, international_organization|value|
|rite_power_percentage|How high the percentage of the current rite power compared to the maximum does the country/IO have?||country, international_organization|value|
|ruled_country_on_or_after|Checks if the character ruled the country on or after a given date?||character||
|ruler_reign|Checks if the ruler of a country has ruled for x years||country|value|
|ruler_reign_in_days|Checks if the ruler or regent of a country has ruled for x days||country|value|
|ruler_term_start_date|Gets the start date of the current ruler term||country|date|
|sailors|How much Sailors does the country/IO have?||country, international_organization|value|
|sailors_percentage|Checks the percentage of Sailors a country has compared to its maximum||country|value|
|satisfaction|The satisfaction of an estate||estate|value|
|save_temporary_scope_as|Saves a temporary target for use during the trigger execution||none||
|save_temporary_scope_value_as|Saves a numerical or bool value as an arbitrarily-named temporary target to be referenced later in the same effect|save_temporary_scope_value_as = { name = <string> value = x }|none||
|school_opinion|does the school have the specified opinion of the target?||religious_school||
|scope_type|Checks the type of the scope object||none||
|self_control|How much self control does the country/IO have?||country, international_organization|value|
|self_control_percentage|How high the percentage of the current self control compared to the maximum does the country/IO have?||country, international_organization|value|
|short_term_trigger_currency_utility|Checks the AI utility of adding an amount of a certain trigger to the scoped object|short_term_trigger_currency_utility = { trigger = <trigger> size = <size> target = <optional target> value >= <script_value> }|country|value|
|situation_has_ended|Check if a situation has ended||situation|boolean|
|situation_is_active|Check if a situation is active||situation|boolean|
|slider_minting_value|How much minting is going on (0..1)||country|value|
|societal_value_cabinet_action|Checks if a cabinet action role has a societal value||cabinet_action|boolean|
|societal_value_progress|Gets progress towards societal value||country|value|
|special_status_can_be_bestowed|Can the supplied special status be bestowed on the supplied country in the scope international organization?||international_organization||
|special_status_power|Get the political power of the specified country in an organization with that specified special status.|special_status_power = { country = <country> type = <special status> value <operator> <float> } or special_status_power(<country>\|<special status>)|international_organization|value|
|special_status_power_fraction|Get the political power fraction of the specified country in an organization with that specified special status.|special_status_power_fraction = { country = <country> type = <special status> value <operator> <float> } or special_status_power(<country>\|<special status>)|international_organization|value|
|spy_network|How much spy-network does the country have in the target?|spy_network = { target = X value <operator> Y or value = { min max } }|country|value|
|stability|How much Stability does the country/IO have?||country, international_organization|value|
|stability_percentage|How high the percentage of the current Stability compared to the maximum does the country/IO have?||country, international_organization|value|
|state_religion_clergy|Checks the proportion of your population that is true faith clergy||country|value|
|strength_percentage|How many percent strength does this unit have???||unit|value|
|sub_unit_type|Checks if a sub_unit is of a specific type||sub_unit|unit_type|
|subject_can_be_annexed|Check if a subject type allows an overlord to annex the subject||subject_type|boolean|
|subject_can_be_created_by|Check if a subject type can be created by the supplied country||subject_type||
|subject_level|Get the level of the subject type.||subject_type|value|
|subject_loyalty|Checks a country's subject loyalty||country|value|
|subject_type_annullment_favours_required|returns the favours needed to annul this relation diplomatically||subject_type|value|
|subjects_relative_power|Compares to relative power of all subjects combined||country|value|
|subunit_morale|How many morale does this subunit have???||sub_unit|value|
|subunit_morale_percentage|How many percent morale does this subunit have???||sub_unit|value|
|subunit_number|What is the regimental number for this subnunit||sub_unit|value|
|subunit_strength|How many strength does this subunit have???||sub_unit|value|
|subunit_strength_percentage|How many percent strength does this subunit have???||sub_unit|value|
|supports_rebel|Checks if a country supports the target rebel||country|rebels|
|switch|Switch on a trigger for the evaluation of another trigger with an optional fallback trigger.|switch = { trigger = simple_assign_trigger case_1 = { <triggers> } case_2 = { <triggers> } case_n = { <triggers> } fallback = { <triggers> } }|none||
|tag|Is the scoped country the specific country tag; does NOT accept scopes|tag = ENG|country|tag|
|tag_exists|Does the country tag exist; does NOT accept scopes|tag_exists = FRA|none|tag|
|target_satisfaction|The target satisfaction of an estate||estate|value|
|this_antagonism_towards_prev|Gets the current scope country's antagonism towards the previous scope country||country|value|
|this_opinion_of_prev|Gets the current scope country's opinion of the previous scope country||country|value|
|this_trust_of_prev|Gets the current scope country's trust of the previous scope country||country|value|
|threat_level_to|Return the threat level the scope country has towards the target country scope.|threat_level_to = { country = <country scope> value = <script_value> } or threat_level_to(<country scope>)|country|value|
|time_of_year|Check if the current date is within the bounds|time_of_year = { min = 11.1 # default: beginning of year max = 2.29 # default: end of year } Dates are formatted as "<month>.<day>" or just "<month>". The check includes the min and max dates. min can be larger than max, in this case we wrap around to the next year (i.e., February is between October and March).|none||
|tithe|Checks the tithe percentage of the religion||religion|value|
|topography|Checks if a location is of a specific Topography type||location||
|topography_count|Returns the amount of owned locations with the specified topography.|topography_count = { type = <topography scope> value <operator> <value> } or "topography_count(<topography scope>)"|country||
|topography_percent|Returns the percentage of owned locations with the specified topography.|topography_percent = { type = <topography scope> value <operator> <value> } or "topography_percent(<topography scope>)"|country||
|total_abilities|The total ability of the character||character|value|
|total_accepted_culture_population|Checks if a country has an acceputed or primary culture population size of the specified value||country|value|
|total_building_levels|Checks if a location has a certain total amount of building levels||location|value|
|total_cardinals|Checks the total amount of cardinals of the religion||religion|value|
|total_control_scaled_population|Checks if a country has value that is population * local_control its in||country|value|
|total_debt|Checks how much a country has in total debt||country|value|
|total_development|Gets the total amount of development in the country||country|value|
|total_dynastic_power|Check the total amount of dynastic power the scoped dynasty or country has. In case of country, the dynasty of the ruler or of the heir in case of regency is taken.||country, dynasty|value|
|total_effective_goods_production_buildings|Returns the number of effective building levels which produce the specified good.|total_effective_goods_production_buildings = { goods = <goods> value <comparator> <script_value> }|country|value|
|total_enemies|counts the number of enemies of an international organization||international_organization|value|
|total_foreign_buildings_levels|Checks the total number of foreign buildings of a country||country|value|
|total_goods_traded|Check the total amount of goods that went through this market last month||market|value|
|total_goods_value_traded|Check the total value of goods that went through this market last month||market|value|
|total_heathen_population|Checks if a country has a heathen population size of the specified value||country|value|
|total_heretic_population|Checks if a country has a heretic population size of the specified value||country|value|
|total_locations_owned|counts the number of locations owned by an international organization||international_organization|value|
|total_members|counts the number of members in an international organization||international_organization|value|
|total_merchant_capacity|Checks if a country has a certain total merchant capacity||country|value|
|total_merchant_power|Check the level of this Building?||market|value|
|total_not_tolerated_culture_population|Checks if a country has an intolerated culture population size of the specified value||country|value|
|total_payment_contribution|Gets the sum all member countries have to pay for the specified IO and payment type.|total_payment_contribution = { payment = <> }|international_organization|value|
|total_population|Checks if a country has a certain population||country|value|
|total_population_in_international_organization|Checks if the country has the defined amount of pops in the target IO.|total_population_in_international_organization = { international_organization = <IO> value <operator> <script_value> } or total_population_in_international_organization(<IO>)|country|value|
|total_population_in_international_organization_percentage|Checks if the country has the defined amount of pops in the target IO.|total_population_in_international_organization_percentage = { international_organization = <IO> value <operator> <script_value> } or total_population_in_international_organization_percentage(<IO>)|country|value|
|total_primary_culture_population|Checks if a country has a primary culture population size of the specified value||country|value|
|total_special_status_power|Get the political power of all countries in an organization with that specified special status.|total_special_status_power = { type = <special status> value <operator> <float> } or total_special_status_power(<special status>)|international_organization|value|
|total_special_status_power_fraction|Get the percentage political power of the target special status compared to the total amount of political power of all special statuses combined.|special_status_power_fraction = { type = <special status> value <operator> <float> } or special_status_power_fraction(<special status>)|international_organization|value|
|total_tolerated_culture_population|Checks if a country has a tolerated culture population size of the specified value||country|value|
|total_true_faith_population|Checks if a country has a true faith population size of the specified value||country|value|
|total_unique_special_status_power|Get the political power of all countries in an organization with that specified special status.|total_special_status_power = { type = <special status> value <operator> <float> } or total_special_status_power(<special status>)|international_organization|value|
|trade_buy|What is the current price for the buy of a trade?||trade|value|
|trade_capacity_usage_percent|How much of the assigned capacity is being used?||trade|value|
|trade_profit|What is the current profit of a trade?||trade|value|
|trade_sell|What is the current price for the sell of a trade?||trade|value|
|trade_volume|How big volume was traded by this trade?||trade|value|
|tribal_cohesion|How much tribal_cohesion does the country/IO have?||country, international_organization|value|
|tribal_cohesion_percentage|How high the percentage of the current tribal_cohesion compared to the maximum does the country/IO have?||country, international_organization|value|
|trigger_else|Evaluates the display_triggers if the triggers of preceding 'trigger_if' or 'trigger_else_if' is not met|trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else = { <display_triggers> }|none||
|trigger_else_if|Evaluates the enclosed display_triggers if the triggers of the preceding `trigger_if` or `trigger_else_if` is not met and its own trigger of the limit is met|trigger_if = { limit = { <triggers> } <display_triggers> } trigger_else_if = { limit = { <triggers> } <display_triggers> }|none||
|trigger_if|Evaluates the display_triggers if the triggers of the limit are met|trigger_if = { limit = { <triggers> } <display_triggers> }|none||
|trust|is the country's trust towards the target greater or equal than the value?|trust = { target = X value <operator> Y or value = { min max } }|country|value|
|union_length_days|returns the number of days a country has been in a union with the target country.|union_length_days = { target = <country> value <comparator> <script_value> }|country|value|
|unique_international_organization_type_exists|Does an international organization of this type exist?||none|international_organization_type|
|unit_modifier_strength|Does the scoped unit have a given modifier with the compared strength. Default modifiers without any scale changes have a strength value of 1|unit_modifier_strength = { modifier = <modifier> value <comparator> <script math> } or "unit_modifier_strength(<modifier key>)"|unit||
|unit_strength|Check the strength of the unit in scope||unit|value|
|upkeep_maintenance|What is the xx position (0-1) the country has?||country|value|
|used_cultures_capacity|Checks if a country has a certain cost of cultures accepted & tolerated||country|value|
|used_diplomatic_capacity|Diplomatic capacity used by the country||country|value|
|used_fort_limit|How much Fort Limit is currently being used?||country|value|
|used_fort_limit_percentage|What percentage of our Fort Limit is currently being used?||country|value|
|used_merchant_capacity|gets the market used merchant capacity for a country in the scope market||market|value|
|uses_elections|Does this succession law use elections?||heir_selection|boolean|
|uses_government_power|Checks if a country has a certain government_power (e.g. 'legitimacy')||country||
|valid_estate_for_heir_selection|Checks if the character's estate is allowed for the target heir selection||character|heir_selection|
|variable_list_size|Checks the size of a variable list|variable_list_size = { name = <variable_name> value >= <script_value> }|none||
|variable_map_size|Checks the size of a variable map|variable_map_size = { name = <variable_name> value >= <script_value> }|none||
|vegetation|Checks if a location is of a specific Vegetation type||location||
|vegetation_count|Returns the amount of owned locations with the specified vegetation.|vegetation_count = { type = <vegetation scope> value <operator> <value> } or "vegetation_count(<vegetation scope>)"|country||
|vegetation_percent|Returns the percentage of owned locations with the specified vegetation.|vegetation_percent = { type = <vegetation scope> value <operator> <value> } or "vegetation_percent(<vegetation scope>)"|country||
|vote_impact_in_resolution|Check how much vote impact the current country scope would make when voting in the target resolution of the target IO.|vote_impact_in_resolution = { international_organization = <IO> resolution = <resolution> value <operator> <real> } or vote_impact_in_resolution(<IO>\|<resolution>)|country|value|
|vote_is_locked|Is a country's vote locked in the scope international organization/situation?||international_organization, situation||
|vote_percentage_impact_in_resolution|Check how much vote percentage impact the current country scope would make when voting in the target resolution of the target IO.|vote_percentage_impact_in_resolution = { international_organization = <IO> resolution = <resolution> value <operator> <real> } or vote_percentage_impact_in_resolution(<IO>\|<resolution>)|country|value|
|vote_type|Checks the type of the vote in a resolution||resolution||
|votes_for_resolution|Checks the number of votes for a particular outcome of a resolution.|votes_for_resolution(<resolution_key>\|<thing>) or votes_for_resolution = { resolution = <resolution_key> outcome = <thing> value <comparator> <real> }|international_organization, situation|value|
|wants_casus_belli_with|Does country want a casus belli with another nation? Only for Ai||country|country|
|wants_military_access_in|country wants military access in this other country?||country|country|
|wants_opinion_with|Does country want more opinion with another nation? Only for Ai||country|country|
|wants_to_give_away_any_province|Country wants to give any province to a subject?||country|boolean|
|wants_to_subjugate|country wants to subjugate another country?||country|country|
|war_enthusiasm|The war enthusiasm of the current country scope in the target war.|war_enthusiasm = { war = <war scope> value = <script_value> } or war_enthusiasm(<war scope>)|country|value|
|war_exhaustion|How much WarExhaustion does the country/IO have?||country, international_organization|value|
|war_exhaustion_percentage|How high the percentage of the current WarExhaustion compared to the maximum does the country/IO have?||country, international_organization|value|
|war_goal_type|Check if the war goal type of the war is the specified type.||war||
|war_length|Checks how many months the current war has been going.||war|value|
|war_length_in_years|Checks how many years the current war has been going.||war|value|
|war_score_in_war|Check how much war score the current country has in the target war.|war_score_in_war = { war = <war> value <operator> <real> } or "war_score_in_war(<war>)"|country|value|
|war_score_in_war_whole_side|Check how much war score the war side of the current country has in the target war.|war_score_in_war_whole_side = { war = <war> value <operator> <real> } or "war_score_in_war_whole_side(<war>)"|country|value|
|war_score_of_country|Check how much war score the target country has in the current war.|war_score_of_country = { country = <country> value <operator> <real> } or war_score_of_country(<country>)|war|value|
|war_score_of_country_side|Check how much war score the war side of the target country has in the current war.|war_score_of_country_side = { country = <country> value <operator> <real> } or war_score_of_country_side(<country>)|war|value|
|war_score_versus|Gets the war score of the scope country against the supplied one|war_score_versus(<target>) or war_score_versus = { target = <country link> value <operator> <amount> }|country|value|
|war_stalling_length|Checks how many months with no action have passed in the current war.||war|value|
|war_stalling_length_in_years|Checks how many years with no action have passed in the current war.||war|value|
|weighted_calc_true_if|Returns true if the sum of weights of fulfilled sub-triggers amount to the specified sum|weighted_calc_true_if = { amount = 10 5 = { <trigger> } 15 = { <trigger> } 7 = { <trigger> } }|none||
|winter_level|winter level check||location||
|winter_power|||location|value|
|within_colonial_range_of|Is the location within Colonial range of the target country?||area, location, province|country|
|within_diplomatic_range|Is the target country within diplomatic range?||country|country|
|within_naval_range_of|Is the location within naval range of the target country?||area, location, province|country|
|world_art_quality|Checks the total art quality in the world||none|value|
|world_culture_group_percentage|Gets the percentage of the population that follow a particular culture group in the world|world_culture_group_percentage = { culture_group = <culture_group> value <operator> <script_value> }|none|value|
|world_culture_group_population|Gets the absolute number of the population that follow a particular culture group in the world|world_culture_group_population = { culture_group = <culture_group> value <operator> <script_value> }|none|value|
|world_culture_percentage|Gets the percentage of the population that follow a particular culture in the world|world_culture_percentage = { culture = <culture> value <operator> <script_value> }|none|value|
|world_culture_population|Gets the absolute number of the population that follow a particular culture in the world|world_culture_population = { culture = <culture> value <operator> <script_value> }|none|value|
|world_religion_group_percentage|Gets the percentage of the population that follow a particular religion group in the world|world_religion_group_percentage = { religion_group = <religion_group> value <operator> <script_value> }|none|value|
|world_religion_group_population|Gets the absolute number of the population that follow a particular religion group in the world|world_religion_group_population = { religion_group = <religion_group> value <operator> <script_value> }|none|value|
|world_religion_percentage|Gets the percentage of the population that follow a particular religion in the world|world_religion_percentage = { religion = <religion> value <operator> <script_value> }|none|value|
|world_religion_population|Gets the absolute number of the population that follow a particular religion in the world|world_religion_population = { religion = <religion> value <operator> <script_value> }|none|value|
|yanantin|How much yanantin does the country/IO have?||country, international_organization|value|
|yanantin_percentage|How high the percentage of the current yanantin compared to the maximum does the country/IO have?||country, international_organization|value|
|yearly_gold|How much gold does the country get per year?||country|value|
|yearly_manpower|How many Manpower does the country get per year?||country|value|
|yearly_sailors|How many Sailors does the country get per year?||country|value|
|yearly_salary|The yearly salary of the character||character|value|
|years_active|Checks how long a religion has been enabled||religion|value|
|years_as_rebel|Check how many years the character has been a rebel.||character|value|
|years_in_international_organization|Checks if the country has been in the current international organization scope for x years.|years_in_international_organization = { country = <country scope> value = <years> } or years_in_international_organization(country)|country|value|
|years_of_service_as_admiral|Check how many years the character has served as an admiral.||character|value|
|years_of_service_as_general|Check how many years the character has served as a general.||character|value|
|years_of_service_in_cabinet|Check how many years the character has served in a cabinet.||character|value|
|years_since_disaster_end|Checks if x years have passed since the end of the disaster. Returns -1 if the disaster has never ended.||disaster|value|
|years_since_disaster_start|Checks if x years have passed since the start of the disaster. Returns -1 if the disaster has never started.||disaster|value|
|years_since_situation_end|Checks if x years have passed since the end of the situation. Returns -1 if the situation has never ended.||situation|value|
|years_since_situation_start|Checks if x years have passed since the start of the situation. Returns -1 if the situation has never started.||situation|value|

## References

- To update these tables, see Module:Script docs/Triggers/Updates

