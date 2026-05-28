# Scope

**Source:** https://eu5.paradoxwikis.com/Scope

---

**Scopes** are game objects used with most effects and triggers. Scopes represent game object types - a `country` scope represents a country, and all effects that are on a country scope will therefore expect to be fired on a country. Relationships between scopes are defined using event targets and, when used in triggers and effects - #Iterators. Scopes are set in a few ways. Most scripted content sets a certain scope, such as `country` as the base or **root** scope.

Most scopes are a particular instance of a game object, determined when the scope is called. Certain scopes refer to game object *types* instead.

## Scopes and scripting

Most scripting is done "in scope" meaning that an effect or trigger must be run in a relevant scoped object in order to correctly check or affect the gamestate. For example, an effect that changes a character's ability stats functions only if it is in a character scope. Similarly, a trigger that checks national tax base does not function outside of a country scope.

Some effects and triggers work in multiple scope types, and others do not require a specific scope at all, meaning they can be used nearly anywhere. Scopeless script is sometimes referred to as "global", "any", or "none" scope. In the effect, trigger, and scope link tables, script that does not require a specific scope is noted with "none".

## Base scope

Each scripted element in the game files that runs effects or triggers may contain a base scope, which is callable with `root`. Some may contain additional scopes, saved as `saved scope` and referred to using `scope:` datalink.

## Iterators

**Iterators** – also called lists – are effects or triggers which iterate through all eligible scopes of a certain type, returning them for checking triggers or executing effects.

There are four types of iterators, one for triggers and three for effects.

|Prefix|Description|
|---|---|
|any_<name>|Trigger scope, checks that any returned scope returns true for contained triggers. Can use count <operator> <scripted value> or percent <operator> <scripted value> to check a specified amount or ratio With count = all or percent = 1, it requires all scopes to return true Can use filter = { <triggers> } with count or percent to limit returned scopes|
|every_<name>|Effect scope, executes effects on all returned scopes Can use limit = { <triggers> } to narrow the scopes returned|
|ordered_<name>|Effect scope, executes effects on returned scope, by default first scope in ordering is returned Uses order_by = value to determine the ordering Can use limit = { <triggers> } to narrow the scopes returned Can use position = int to select a different position in order, 0-indexed Can use min = int and max = value to limit which and how many scopes are returned in the ordering Can use check_range_bounds = no to prevent error logging if the number of returned scopes is less than the range betweem min and max|
|random_<name>|Effect scope, executes effects on a single random returned scope Can use limit = { <triggers> } to narrow the scopes returned Can use weight = { mtth_blocks } to weight the random selection|

### Trigger iterators

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

Trigger iterators all start with `any_` and return true if any scope meets the contained triggers. This behavior can be changed with the parameter `count op int value` or `percent op value [0-1]` when then requires at least the specified number or percent of the scope to meet the contained triggers. These use the usual comparison operators.

If `count` or `percent` are used, another parameter `filter` can be used to limit which scopes are considered.

When negated, trigger iterators behave like `count = all` is set by default, such that it returns true if no scope meets the contained triggers; actually setting `count = all`, however, inverts the behavior back to returning true if any scope does not meet the contained triggers.

### Effect iterators

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|every_accepted_culture|Iterate through all accepted cultures in a country|every_accepted_culture = { limit = { <triggers> } <effects> }|country|culture|
|every_active_disaster|Iterate through all active disasters for a country|every_active_disaster = { limit = { <triggers> } <effects> }|country|disaster|
|every_active_estate|Iterate through all active estates (non-crown)|every_active_estate = { limit = { <triggers> } <effects> }|none|estate_type|
|every_active_resolution|Iterate through all currently active resolutions in an international organization or situation|every_active_resolution = { limit = { <triggers> } <effects> }|international_organization, situation|active_resolution|
|every_adjacent_ports_to_area|Iterate through all adjacent ports of an seazone area|every_adjacent_ports_to_area = { limit = { <triggers> } <effects> }|area|location|
|every_advance_definition|Iterate through all advance definitions|every_advance_definition = { limit = { <triggers> } <effects> }|none|advance_type|
|every_allowed_estate_in_heir_selection|Iterate through all allowed estates a HeirSelection has|every_allowed_estate_in_heir_selection = { limit = { <triggers> } <effects> }|heir_selection|estate_type|
|every_ancestor|Iterate through all ancestors (parents, grandparents etc) of a character|every_ancestor = { limit = { <triggers> } <effects> }|character|character|
|every_area|Iterate through all existing areas|every_area = { limit = { <triggers> } <effects> }|none|area|
|every_area_in_region|Iterate through all areas in a region|every_area_in_region = { limit = { <triggers> } <effects> }|region|area|
|every_area_in_scripted_geography|Iterate through all areas in a scripted geography|every_area_in_scripted_geography = { limit = { <triggers> } <effects> }|scripted_geography|area|
|every_area_with_core|Iterate through all areas with cored locations in a country|every_area_with_core = { limit = { <triggers> } <effects> }|country|area|
|every_area_with_owned_province|Iterate through all areas with owned provinces in a country|every_area_with_owned_province = { limit = { <triggers> } <effects> }|country|area|
|every_army|Iterate through all armies in a country|every_army = { limit = { <triggers> } <effects> }|country|unit|
|every_artist|Iterate through all artists in a country|every_artist = { limit = { <triggers> } <effects> }|country|character|
|every_attacker|Iterate through all attackers of a war|every_attacker = { limit = { <triggers> } <effects> }|war|country|
|every_available_dynasty_member|Iterate through adult dynasty members who are not a ruler or heir (cached)|every_available_dynasty_member = { limit = { <triggers> } <effects> }|dynasty|character|
|every_avatar_for_god|Iterate through all Avatars of a God|every_avatar_for_god = { limit = { <triggers> } <effects> }|god|avatar|
|every_besieging_units|Iterate through all units participating in a siege|every_besieging_units = { limit = { <triggers> } <effects> }|siege|unit|
|every_border_location|Iterate through all owned location in a country which border locations not owned by the current country scope.|every_border_location = { limit = { <triggers> } <effects> }|country|location|
|every_buildable_building_type|Iterate through all the building types a country can build|every_buildable_building_type = { limit = { <triggers> } <effects> }|country|building_type|
|every_building_owned_by_estate|Iterate through all buildings that an estate has|every_building_owned_by_estate = { limit = { <triggers> } <effects> }|estate|building|
|every_building_type|Iterate through all the building types|every_building_type = { limit = { <triggers> } <effects> }|none|building_type|
|every_buildings_in_location|Iterate through all buildings in a location|every_buildings_in_location = { limit = { <triggers> } <effects> }|location|building|
|every_cabinet|Iterate through all actions in a country's cabinet|every_cabinet = { limit = { <triggers> } <effects> }|country|cabinet|
|every_cabinet_action|Iterate through all actions in a country's cabinet actions|every_cabinet_action = { limit = { <triggers> } <effects> }|country|cabinet_action|
|every_cabinet_character|Iterate through all characters in a country that is in the cabinet|every_cabinet_character = { limit = { <triggers> } <effects> }|country|character|
|every_cardinal_in_country|Iterate through all Cardinals in a country|every_cardinal_in_country = { limit = { <triggers> } <effects> }|country|cardinal|
|every_cardinal_in_religion|Iterate through all Cardinals in a Religion|every_cardinal_in_religion = { limit = { <triggers> } <effects> }|religion|cardinal|
|every_casus_belli_on_us|Iterate through all countries have a casus belli on us|every_casus_belli_on_us = { limit = { <triggers> } <effects> }|country|country|
|every_casus_belli_target|Iterate through all countries we have a casus belli on|every_casus_belli_target = { limit = { <triggers> } <effects> }|country|country|
|every_center|Iterate through all subunits on the center of a combat-side|every_center = { limit = { <triggers> } <effects> }|combat_side|sub_unit|
|every_character|Iterate through all characters in a country|every_character = { limit = { <triggers> } <effects> }|country|character|
|every_character_in_dynasty|Iterate through all living characters in a Dynasty|every_character_in_dynasty = { limit = { <triggers> } <effects> }|dynasty|character|
|every_character_supporting_rebel|Iterate through all characters supporting a rebel|every_character_supporting_rebel = { limit = { <triggers> } <effects> }|rebels|character|
|every_child|Iterate through all children of a character|every_child = { limit = { <triggers> } <effects> }|character|character|
|every_close_relative|Iterate through all close relatives of a character|every_close_relative = { limit = { <triggers> } <effects> }|character|character|
|every_coast_border_location|Iterate through all bordering, or across one seazone of a location|every_coast_border_location = { limit = { <triggers> } <effects> }|location|location|
|every_colonial_charter|Iterate through all colonial charters in a country|every_colonial_charter = { limit = { <triggers> } <effects> }|country|colonial_charter|
|every_colonial_claim_province_definition|Iterate through all province definitions with colonial claims from the scope country.|every_colonial_claim_province_definition = { limit = { <triggers> } <effects> }|country|province_definition|
|every_colonial_country|Iterate through all colonial countries in the world|every_colonial_country = { limit = { <triggers> } <effects> }|none|country|
|every_colonial_overlord|Iterate through all colonial overlord countries in the world|every_colonial_overlord = { limit = { <triggers> } <effects> }|none|country|
|every_colonial_top_overlord|Iterate through all countries in the world that have a colonial country among their subjects or their subjects subjects and so on|every_colonial_top_overlord = { limit = { <triggers> } <effects> }|none|country|
|every_connected_location|Iterate through all locations in the same country as the scope location that are connected by land or strait|every_connected_location = { limit = { <triggers> } <effects> }|location|location|
|every_construction_material_for_building_type|Iterate through all goods required to construct a building type|every_construction_material_for_building_type = { limit = { <triggers> } <effects> }|building_type|goods|
|every_continent|Iterate through all existing continents|every_continent = { limit = { <triggers> } <effects> }|none|continent|
|every_continent_in_scripted_geography|Iterate through all continents in a scripted geography|every_continent_in_scripted_geography = { limit = { <triggers> } <effects> }|scripted_geography|continent|
|every_controlled_location|Iterate through all controlled location in a country|every_controlled_location = { limit = { <triggers> } <effects> }|country|location|
|every_core_in_location|Iterate through all cores in a location|every_core_in_location = { limit = { <triggers> } <effects> }|location|country|
|every_core_location|Iterate through all core locations in a country|every_core_location = { limit = { <triggers> } <effects> }|country|location|
|every_country|Iterate through all existing countries|every_country = { limit = { <triggers> } <effects> }|none|country|
|every_country_annexing_us|Iterate through all countries which are currently annexing the current country scope.|every_country_annexing_us = { limit = { <triggers> } <effects> }|country|country|
|every_country_at_war_with|Iterate through all countries at war with|every_country_at_war_with = { limit = { <triggers> } <effects> }|country|country|
|every_country_in_culture|Iterate through all countries with this primary culture|every_country_in_culture = { limit = { <triggers> } <effects> }|culture|country|
|every_country_in_culture_group|Iterate through all countries in a culture group.|every_country_in_culture_group = { limit = { <triggers> } <effects> }|culture_group|country|
|every_country_in_diplomatic_range|Iterate through all countries in diplomatic range|every_country_in_diplomatic_range = { limit = { <triggers> } <effects> }|country|country|
|every_country_in_dynasty|Iterate through all countries in a Dynasty|every_country_in_dynasty = { limit = { <triggers> } <effects> }|dynasty|country|
|every_country_in_hierarchy|Iterate through every country in the entire overlord/subject hierarchy, from the independent top overlord to the deepest subjects|every_country_in_hierarchy = { limit = { <triggers> } <effects> }|country|country|
|every_country_in_religion|Iterate through all countries in a religion|every_country_in_religion = { limit = { <triggers> } <effects> }|religion|country|
|every_country_in_religion_group|Iterate through all countries in a religion group.|every_country_in_religion_group = { limit = { <triggers> } <effects> }|group|country|
|every_country_in_religious_school|Iterate through all countries within a school|every_country_in_religious_school = { limit = { <triggers> } <effects> }|religious_school|country|
|every_country_lent_to|Iterate through all countries a country has lent to|every_country_lent_to = { limit = { <triggers> } <effects> }|country|country|
|every_country_sub_unit|Iterate through all subunits in all units in a country|every_country_sub_unit = { limit = { <triggers> } <effects> }|country|sub_unit|
|every_country_supporting_rebel|Iterate through all countries supporting a rebel|every_country_supporting_rebel = { limit = { <triggers> } <effects> }|rebels|country|
|every_country_that_can_be_called_defensively|Iterate through all countries that may be called into a defensive war.|every_country_that_can_be_called_defensively = { limit = { <triggers> } <effects> }|country|country|
|every_country_that_can_be_called_offensively|Iterate through all countries that may be called into an offensive war.|every_country_that_can_be_called_offensively = { limit = { <triggers> } <effects> }|country|country|
|every_country_together_in_war_with|Iterate through all countries which are an ally in any of the country scope's wars|every_country_together_in_war_with = { limit = { <triggers> } <effects> }|country|country|
|every_country_we_are_annexing|Iterate through all countries which are currently annexed by the current country scope.|every_country_we_are_annexing = { limit = { <triggers> } <effects> }|country|country|
|every_country_with_antagonism_against_us|Iterate through all countries who have antagonism against us|every_country_with_antagonism_against_us = { limit = { <triggers> } <effects> }|country|country|
|every_country_with_capital_in_geography|Iterate through all countries which have their capital in the specified geography|every_country_with_capital_in_geography = { limit = { <triggers> } <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|every_country_with_cardinals|Iterate through all countries with cardinals in a religion|every_country_with_cardinals = { limit = { <triggers> } <effects> }|religion|country|
|every_country_with_coalition_grade_antagonism_against_us|Iterate through all countries who have coalition grade antagonism against us|every_country_with_coalition_grade_antagonism_against_us = { limit = { <triggers> } <effects> }|country|country|
|every_country_with_relation_that_can_be_annulled|Iterate through all countries which have an annullable relation with the scope country.|every_country_with_relation_that_can_be_annulled = { limit = { <triggers> } <effects> }|country|country|
|every_country_with_special_status_of_type|Iterate through all countries in the international organization which have the specified special status|every_country_with_special_status_of_type = { limit = { <triggers> } <effects> }|international_organization|country|
|every_country_with_succession_law|Iterate through all countries with a cached succession law (set cached = yes in the heir_selection to use this)|every_country_with_succession_law = { limit = { <triggers> } <effects> }|none|country|
|every_culture|Iterate through all cultures|every_culture = { limit = { <triggers> } <effects> }|none|culture|
|every_culture_group|Iterate through all culture groups the culture is in.|every_culture_group = { limit = { <triggers> } <effects> }|culture|culture_group|
|every_culture_in_culture_group|Iterate through all cultures in a culture group.|every_culture_in_culture_group = { limit = { <triggers> } <effects> }|culture_group|culture|
|every_current_avatars|Iterate through all Avatars a country has|every_current_avatars = { limit = { <triggers> } <effects> }|country|avatar|
|every_current_bureaucracy|Iterate through all Bureaucracies a country has|every_current_bureaucracy = { limit = { <triggers> } <effects> }|country|bureaucracy|
|every_current_bureaucracy_type|Iterate through all Bureaucracy types a country has|every_current_bureaucracy_type = { limit = { <triggers> } <effects> }|country|bureaucracy_type|
|every_current_gods|Iterate through all Gods a country worships|every_current_gods = { limit = { <triggers> } <effects> }|country|god|
|every_current_law|Iterate through all laws of a country.|every_current_law = { limit = { <triggers> } <effects> }|country|law|
|every_current_law_in_international_organization|Iterate through all laws that are codified in the international organization|every_current_law_in_international_organization = { limit = { <triggers> } <effects> }|international_organization|law|
|every_current_policy|Iterate through all policies that are codified in the country|every_current_policy = { limit = { <triggers> } <effects> }|country|policy|
|every_current_policy_in_international_organization|Iterate through all policies that are codified in the international organization|every_current_policy_in_international_organization = { limit = { <triggers> } <effects> }|international_organization|policy|
|every_current_reforms|Iterate through all Government Reforms a country has|every_current_reforms = { limit = { <triggers> } <effects> }|country|government_reform|
|every_current_war|Iterate through all wars of a country|every_current_war = { limit = { <triggers> } <effects> }|country|war|
|every_defender|Iterate through all defenders of a war|every_defender = { limit = { <triggers> } <effects> }|war|country|
|every_descendant|Iterate through all descendants (children, grandchildren etc) of a character|every_descendant = { limit = { <triggers> } <effects> }|character|character|
|every_disloyal_subject|Iterate through all loyal subject countries|every_disloyal_subject = { limit = { <triggers> } <effects> }|country|country|
|every_dynasty|Iterate through all dynasties in a country|every_dynasty = { limit = { <triggers> } <effects> }|country|dynasty|
|every_east_of_province_definition|Iterate through all province-definitions east of a province-definition|every_east_of_province_definition = { limit = { <triggers> } <effects> }|province_definition|province_definition|
|every_election_candidates|Iterate through all election candidates of a country with elections!|every_election_candidates = { limit = { <triggers> } <effects> }|country|character|
|every_enemy|Iterate through all Enemy countries|every_enemy = { limit = { <triggers> } <effects> }|country|country|
|every_enemy_war_leader|Iterate through all countries which are leading a war against the scope|every_enemy_war_leader = { limit = { <triggers> } <effects> }|country|country|
|every_estate|Iterate through all estates in a country|every_estate = { limit = { <triggers> } <effects> }|country|estate|
|every_estate_privilege|Iterate through all current estate privileges of a Country|every_estate_privilege = { limit = { <triggers> } <effects> }|country|estate_privilege|
|every_estate_type_preferring|Iterate through all estate types that a prefer a policy|every_estate_type_preferring = { limit = { <triggers> } <effects> }|policy|estate_type|
|every_estate_type_that_dislikes_bureaucracy|Iterate through all estate types that do NOT prefer a bureaucracy|every_estate_type_that_dislikes_bureaucracy = { limit = { <triggers> } <effects> }|bureaucracy_type|estate_type|
|every_estate_type_that_likes_bureaucracy|Iterate through all estate types that a prefer a bureaucracy|every_estate_type_that_likes_bureaucracy = { limit = { <triggers> } <effects> }|bureaucracy_type|estate_type|
|every_exploration_from_country|Iterate through all Explorations a country has|every_exploration_from_country = { limit = { <triggers> } <effects> }|country|exploration|
|every_export|Iterate through all exports in a market|every_export = { limit = { <triggers> } <effects> }|market|trade|
|every_export_from_location|Iterate through all exports from location|every_export_from_location = { limit = { <triggers> } <effects> }|location|location|
|every_food_goods|Iterate through all food goods|every_food_goods = { limit = { <triggers> } <effects> }|none|goods|
|every_foreign_building_countries_in_location|Iterate through all foreign building countries in a location|every_foreign_building_countries_in_location = { limit = { <triggers> } <effects> }|location|country|
|every_foreign_buildings_in_location|Iterate through all foreign buildings in a location|every_foreign_buildings_in_location = { limit = { <triggers> } <effects> }|location|building|
|every_fort_in_country|Iterate through all Forts in a country|every_fort_in_country = { limit = { <triggers> } <effects> }|country|location|
|every_friendly_coast_border_location|Iterate through all friendly bordering, or across one seazone of a location|every_friendly_coast_border_location = { limit = { <triggers> } <effects> }|location|location|
|every_friendly_country|Iterate through all countries with relations marked as friendly|every_friendly_country = { limit = { <triggers> } <effects> }|country|country|
|every_friendly_or_high_opinion_country|Iterate through all countries with relations marked as friendly or that we have a high opinion of set in defines|every_friendly_or_high_opinion_country = { limit = { <triggers> } <effects> }|country|country|
|every_friendly_to_friendly_country|Iterate through all friends of our friends|every_friendly_to_friendly_country = { limit = { <triggers> } <effects> }|country|country|
|every_friendly_to_hostile_country|Iterate through all friends of our enemies|every_friendly_to_hostile_country = { limit = { <triggers> } <effects> }|country|country|
|every_god_in_religion|Iterate through all Gods in a Religion|every_god_in_religion = { limit = { <triggers> } <effects> }|religion|god|
|every_good_in_demand|Iterate through all goods in a goods demand|every_good_in_demand = { limit = { <triggers> } <effects> }|demand|goods|
|every_goods|Iterate through all types of goods|every_goods = { limit = { <triggers> } <effects> }|none|goods|
|every_graphical_culture_in_culture|Iterate through all graphical culture in a culture|every_graphical_culture_in_culture = { limit = { <triggers> } <effects> }|culture|graphical_culture|
|every_great_power|Iterate through all great powers|every_great_power = { limit = { <triggers> } <effects> }|none|country|
|every_heathen_location|Iterate through all heathen locations in a country|every_heathen_location = { limit = { <triggers> } <effects> }|country|location|
|every_heretic_location|Iterate through all Heretic locations in a country|every_heretic_location = { limit = { <triggers> } <effects> }|country|location|
|every_hired_mercenary|Iterate through mercenaries a country has hired|every_hired_mercenary = { limit = { <triggers> } <effects> }|country|mercenary|
|every_historical_enemy|Iterate through all historical Enemy countries|every_historical_enemy = { limit = { <triggers> } <effects> }|country|country|
|every_historical_rival|Iterate through all historical rival countries|every_historical_rival = { limit = { <triggers> } <effects> }|country|country|
|every_holy_site_in_country|Iterate through all Holy Sites in a country|every_holy_site_in_country = { limit = { <triggers> } <effects> }|country|holy_site|
|every_holy_site_in_religion|Iterate through all Holy Sites in a Religion|every_holy_site_in_religion = { limit = { <triggers> } <effects> }|religion|holy_site|
|every_hostile_country|Iterate through all countries with relations marked as hostile|every_hostile_country = { limit = { <triggers> } <effects> }|country|country|
|every_hostile_or_low_opinion_country|Iterate through all countries with relations marked as hostile or that we have a low opinion of set in defines|every_hostile_or_low_opinion_country = { limit = { <triggers> } <effects> }|country|country|
|every_hostile_to_friendly_country|Iterate through all enemies of our friends|every_hostile_to_friendly_country = { limit = { <triggers> } <effects> }|country|country|
|every_hostile_to_hostile_country|Iterate through all enemies of our enemies|every_hostile_to_hostile_country = { limit = { <triggers> } <effects> }|country|country|
|every_import|Iterate through all imports in a market|every_import = { limit = { <triggers> } <effects> }|market|trade|
|every_import_from_location|Iterate through all Imports from location|every_import_from_location = { limit = { <triggers> } <effects> }|location|location|
|every_in_global_list|Iterate through all items in global list.|every_in_global_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_in_list|Iterate through all items in list.|every_in_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_in_local_list|Iterate through all items in local list.|every_in_local_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_institutions_embraced|Iterate through all institutions a country has embraced|every_institutions_embraced = { limit = { <triggers> } <effects> }|country|institution|
|every_international_organization|Iterate through all international organizations|every_international_organization = { limit = { <triggers> } <effects> }|none|international_organization|
|every_international_organization_elector|Iterate through all countries with an elector special status in the international organization|every_international_organization_elector = { limit = { <triggers> } <effects> }|international_organization|country|
|every_international_organization_enemy|Iterate through all countries that are enemies of the international organization|every_international_organization_enemy = { limit = { <triggers> } <effects> }|international_organization|country|
|every_international_organization_member|Iterate through all countries that are members of the international organization|every_international_organization_member = { limit = { <triggers> } <effects> }|international_organization|country|
|every_international_organization_owned_location|Iterate through all locations that are owned by the international organization|every_international_organization_owned_location = { limit = { <triggers> } <effects> }|international_organization|location|
|every_international_organization_owner|Iterate through all international organizations which own the location scope|every_international_organization_owner = { limit = { <triggers> } <effects> }|location|international_organization|
|every_international_organization_parliament_opposers|Iterate through all countries that have voted AGAINST the parliament issue in the in the parliament of the international organization and support the current debate|every_international_organization_parliament_opposers = { limit = { <triggers> } <effects> }|international_organization|country|
|every_international_organization_parliament_supporter|Iterate through all countries that have voted FOR the parliament issue in the parliament of the international organization and support the current debate|every_international_organization_parliament_supporter = { limit = { <triggers> } <effects> }|international_organization|country|
|every_international_organizations_member_of|Iterate through all international organizations a country is a member of|every_international_organizations_member_of = { limit = { <triggers> } <effects> }|country|international_organization|
|every_international_organizations_target_of|Iterate through all international organizations a country is a target of|every_international_organizations_target_of = { limit = { <triggers> } <effects> }|country|international_organization|
|every_invited_religious_figure|Iterate through all invited religious figures in a Country|every_invited_religious_figure = { limit = { <triggers> } <effects> }|country|character|
|every_key_in_global_variable_map|Iterate through all items in global variable map.|every_key_in_global_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|every_key_in_local_variable_map|Iterate through all items in local variable map.|every_key_in_local_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|every_key_in_variable_map|Iterate through all items in variable map.|every_key_in_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|every_known_country|Iterate through all known countries|every_known_country = { limit = { <triggers> } <effects> }|country|country|
|every_known_institution|Iterate through all institutions a country knows of|every_known_institution = { limit = { <triggers> } <effects> }|country|institution|
|every_left_flank|Iterate through all subunits on the left-flank of a combat-side|every_left_flank = { limit = { <triggers> } <effects> }|combat_side|sub_unit|
|every_lent_loan|Iterate through all loans that a country lent|every_lent_loan = { limit = { <triggers> } <effects> }|country|loan|
|every_loan|Iterate through all loans in a country|every_loan = { limit = { <triggers> } <effects> }|country|loan|
|every_loan_lent_to_country|Iterate through all loans a country has lent to the supplied borrower country|every_loan_lent_to_country = { limit = { <triggers> } <effects> }|country|loan|
|every_location_in_area|Iterate through all Locations in a area|every_location_in_area = { limit = { <triggers> } <effects> }|area|location|
|every_location_in_continent|Iterate through all Locations in a continent|every_location_in_continent = { limit = { <triggers> } <effects> }|continent|location|
|every_location_in_market|Iterate through all locations in a market|every_location_in_market = { limit = { <triggers> } <effects> }|market|location|
|every_location_in_province|Iterate through all Locations in a province|every_location_in_province = { limit = { <triggers> } <effects> }|province|location|
|every_location_in_province_definition|Iterate through all Locations in a province definition|every_location_in_province_definition = { limit = { <triggers> } <effects> }|province_definition|location|
|every_location_in_region|Iterate through all Locations in a region|every_location_in_region = { limit = { <triggers> } <effects> }|region|location|
|every_location_in_scripted_geography|Iterate through all locations in a scripted geography|every_location_in_scripted_geography = { limit = { <triggers> } <effects> }|scripted_geography|location|
|every_location_in_sub_continent|Iterate through all Locations in a sub-continent|every_location_in_sub_continent = { limit = { <triggers> } <effects> }|sub_continent|location|
|every_location_in_the_world|Iterate through all location|every_location_in_the_world = { limit = { <triggers> } <effects> }|none|location|
|every_location_with_movement|Iterate through all locations affected by the scope movement|every_location_with_movement = { limit = { <triggers> } <effects> }|movement|location|
|every_location_with_town_rights_in_country|Iterate through all locations with Town Rights in a country|every_location_with_town_rights_in_country = { limit = { <triggers> } <effects> }|country|location|
|every_loyal_subject|Iterate through all loyal subject countries|every_loyal_subject = { limit = { <triggers> } <effects> }|country|country|
|every_maritime_area|Iterate through all maritime areas for a country|every_maritime_area = { limit = { <triggers> } <effects> }|country|area|
|every_market_center_in_country|Iterate through all markets in a country which market centers are owned by the country|every_market_center_in_country = { limit = { <triggers> } <effects> }|country|market|
|every_market_in_world|Iterate through all markets in the world|every_market_in_world = { limit = { <triggers> } <effects> }|none|market|
|every_market_present_in_country|Iterate through all markets in a country|every_market_present_in_country = { limit = { <triggers> } <effects> }|country|market|
|every_market_with_merchants|Iterate through all markets a country has active merchants|every_market_with_merchants = { limit = { <triggers> } <effects> }|country|market|
|every_mercenary|Iterate through all mercenaries in the world|every_mercenary = { limit = { <triggers> } <effects> }|none|mercenary|
|every_mercenary_sub_unit|Iterate through all subunits in a Mercenary|every_mercenary_sub_unit = { limit = { <triggers> } <effects> }|mercenary|sub_unit|
|every_merchant_in_market|Iterate through all merchants in a market|every_merchant_in_market = { limit = { <triggers> } <effects> }|market|country|
|every_movement|Iterate through all movements|every_movement = { limit = { <triggers> } <effects> }|none|movement|
|every_movement_in_country|Iterate through all movements in a country|every_movement_in_country = { limit = { <triggers> } <effects> }|country|movement|
|every_movement_in_culture|Iterate through all movements in a culture|every_movement_in_culture = { limit = { <triggers> } <effects> }|culture|movement|
|every_movement_in_religion|Iterate through all movements in a religion|every_movement_in_religion = { limit = { <triggers> } <effects> }|religion|movement|
|every_navy|Iterate through all navies in a country|every_navy = { limit = { <triggers> } <effects> }|country|unit|
|every_neighbor_area|Iterate through all neighboring areas in a area|every_neighbor_area = { limit = { <triggers> } <effects> }|area|area|
|every_neighbor_country|Iterate through all neighbour countries|every_neighbor_country = { limit = { <triggers> } <effects> }|country|country|
|every_neighbor_location|Iterate through all neighbors of a location|every_neighbor_location = { limit = { <triggers> } <effects> }|location|location|
|every_neighbor_province_definition|Iterate through all neighboring ProvinceDefinitions in a ProvinceDefinition|every_neighbor_province_definition = { limit = { <triggers> } <effects> }|province_definition|province_definition|
|every_new_world_goods|Iterate through all new-world goods|every_new_world_goods = { limit = { <triggers> } <effects> }|none|goods|
|every_nomad_countries_in_location|Iterate through all nomad pop countries in a location|every_nomad_countries_in_location = { limit = { <triggers> } <effects> }|location|country|
|every_non_state_religion_location|Iterate through all NonStateReligion locations in a country|every_non_state_religion_location = { limit = { <triggers> } <effects> }|country|location|
|every_old_world_goods|Iterate through all old-world goods|every_old_world_goods = { limit = { <triggers> } <effects> }|none|goods|
|every_omen_in_country|Iterate through all Omens active in a country|every_omen_in_country = { limit = { <triggers> } <effects> }|country|omen|
|every_omen_in_god|Iterate through all Omens associated with a God|every_omen_in_god = { limit = { <triggers> } <effects> }|god|omen|
|every_omen_in_religion|Iterate through all Omens in a religion|every_omen_in_religion = { limit = { <triggers> } <effects> }|religion|omen|
|every_other_core_country|Iterate through all other countries which have a core on the current country|every_other_core_country = { limit = { <triggers> } <effects> }|country|country|
|every_other_country|Iterate through all other countries|every_other_country = { limit = { <triggers> } <effects> }|country|country|
|every_other_great_power|Iterate through all other great powers|every_other_great_power = { limit = { <triggers> } <effects> }|country|country|
|every_other_religion_in_same_group|Iterate through all other religions that has the same group as Religion|every_other_religion_in_same_group = { limit = { <triggers> } <effects> }|religion|religion|
|every_other_revolutionary|Iterate through all other revolutionary countries|every_other_revolutionary = { limit = { <triggers> } <effects> }|country|country|
|every_overlord_or_above|Iterate through your overlord, your overlord's overlord, and so on|every_overlord_or_above = { limit = { <triggers> } <effects> }|country|country|
|every_ownable_location|Iterate through all ownable location|every_ownable_location = { limit = { <triggers> } <effects> }|none|location|
|every_ownable_location_in_area|Iterate through all ownable Locations in an area|every_ownable_location_in_area = { limit = { <triggers> } <effects> }|area|location|
|every_ownable_location_in_continent|Iterate through all ownable Locations in a continent|every_ownable_location_in_continent = { limit = { <triggers> } <effects> }|continent|location|
|every_ownable_location_in_province_definition|Iterate through all ownable Locations in a province definition|every_ownable_location_in_province_definition = { limit = { <triggers> } <effects> }|province_definition|location|
|every_ownable_location_in_region|Iterate through all ownable Locations in a region|every_ownable_location_in_region = { limit = { <triggers> } <effects> }|region|location|
|every_ownable_location_in_scripted_geography|Iterate through all ownable locations in a scripted geography|every_ownable_location_in_scripted_geography = { limit = { <triggers> } <effects> }|scripted_geography|location|
|every_ownable_location_in_sub_continent|Iterate through all ownable Locations in a sub continent|every_ownable_location_in_sub_continent = { limit = { <triggers> } <effects> }|sub_continent|location|
|every_owned_building|Iterate through all the owned buildings in a country|every_owned_building = { limit = { <triggers> } <effects> }|country|building|
|every_owned_foreign_building|Iterate through all the owned foreign buildings in a country|every_owned_foreign_building = { limit = { <triggers> } <effects> }|country|building|
|every_owned_foreign_building_location|Iterate through all the location of owned foreign buildings in a country|every_owned_foreign_building_location = { limit = { <triggers> } <effects> }|country|location|
|every_owned_foreign_building_region|Iterate through all the regions of owned foreign buildings in a country|every_owned_foreign_building_region = { limit = { <triggers> } <effects> }|country|region|
|every_owned_location|Iterate through all owned location in a country|every_owned_location = { limit = { <triggers> } <effects> }|country|location|
|every_owned_nomad_pop|Iterate through all owned nomad pops in a country|every_owned_nomad_pop = { limit = { <triggers> } <effects> }|country|pop|
|every_owned_non_rural_location|Iterate through all owned non-rural locations in a country|every_owned_non_rural_location = { limit = { <triggers> } <effects> }|country|location|
|every_owned_rural_location|Iterate through all owned rural locations in a country|every_owned_rural_location = { limit = { <triggers> } <effects> }|country|location|
|every_owner_in_region|Iterate through all the countries that own locations in a region|every_owner_in_region = { limit = { <triggers> } <effects> }|region|country|
|every_parent|Iterate through parents (order: father, mother) of a character.|every_parent = { limit = { <triggers> } <effects> }|character|character|
|every_participating_countries|Iterate through all Countrys participating in 1 side of a combat|every_participating_countries = { limit = { <triggers> } <effects> }|combat_side|country|
|every_participating_units|Iterate through all units participating in 1 side of a combat|every_participating_units = { limit = { <triggers> } <effects> }|combat_side|unit|
|every_past_liturgical_dialect|Iterate through all liturgical dialects a country has had before|every_past_liturgical_dialect = { limit = { <triggers> } <effects> }|country|country|
|every_policy_in_law|Iterate through all policies that are part of the law scope|every_policy_in_law = { limit = { <triggers> } <effects> }|law|policy|
|every_political_border_location|Iterate through all owned location in a country which border another country.|every_political_border_location = { limit = { <triggers> } <effects> }|country|location|
|every_pop|Iterate through all pops in a location or country|every_pop = { limit = { <triggers> } <effects> }|country, location|pop|
|every_pops_supporting_rebel|Iterate through all pops supporting a rebel|every_pops_supporting_rebel = { limit = { <triggers> } <effects> }|rebels|pop|
|every_port_in_country|Iterate through all Ports in a country|every_port_in_country = { limit = { <triggers> } <effects> }|country|location|
|every_possible_disaster|Iterate through all possible disasters for a country|every_possible_disaster = { limit = { <triggers> } <effects> }|country|disaster|
|every_possible_parliament_issue|Iterate through all possible parliament issues in a country's or an international organization's parliament|every_possible_parliament_issue = { limit = { <triggers> } <effects> }|country, international_organization|parliament_issue|
|every_possible_policy|Iterate through all possible policies of a Country that is not currently implemeted|every_possible_policy = { limit = { <triggers> } <effects> }|country|policy|
|every_possible_privilege|Iterate through all possible & allowed estate privileges of a Country that is not currently implemeted|every_possible_privilege = { limit = { <triggers> } <effects> }|estate|estate_privilege|
|every_possible_recruit_location|Iterate through all possible recruit locations in a country|every_possible_recruit_location = { limit = { <triggers> } <effects> }|country|location|
|every_present_country|Iterate through all countries in the specified geography|every_present_country = { limit = { <triggers> } <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|every_present_culture_in_country|Iterate through all cultures present in the country.|every_present_culture_in_country = { limit = { <triggers> } <effects> }|country|culture|
|every_present_culture_in_location|Iterate through all cultures present in the location.|every_present_culture_in_location = { limit = { <triggers> } <effects> }|location|culture|
|every_present_overlord|Iterate through all countries which have a subject in the specified geography|every_present_overlord = { limit = { <triggers> } <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|every_present_religion_in_country|Iterate through all religions present in the country.|every_present_religion_in_country = { limit = { <triggers> } <effects> }|country|religion|
|every_present_religion_in_location|Iterate through all religions present in the location.|every_present_religion_in_location = { limit = { <triggers> } <effects> }|location|religion|
|every_primary_or_accepted_culture|Iterate through primary culture and all accepted cultures in a country. Primary is ordered first.|every_primary_or_accepted_culture = { limit = { <triggers> } <effects> }|country|culture|
|every_primary_or_accepted_or_tolerated_culture|Iterate through primary culture and all accepted and all tolerated cultures in a country. Primary is ordered first.|every_primary_or_accepted_or_tolerated_culture = { limit = { <triggers> } <effects> }|country|culture|
|every_privateer|Iterate through all privateers in the world|every_privateer = { limit = { <triggers> } <effects> }|none|privateer|
|every_privateer_from_country|Iterate through all privateers a country has|every_privateer_from_country = { limit = { <triggers> } <effects> }|country|privateer|
|every_privateer_in_area|Iterate through all privateers in a area|every_privateer_in_area = { limit = { <triggers> } <effects> }|area|privateer|
|every_production_method|Iterate through all types of production methods.|every_production_method = { limit = { <triggers> } <effects> }|none|production_method|
|every_production_method_of_building|Iterate through all available production methods of the building.|every_production_method_of_building = { limit = { <triggers> } <effects> }|building|production_method|
|every_province|Iterate through all provinces in a country|every_province = { limit = { <triggers> } <effects> }|country|province|
|every_province_definition|Iterate through all existing province_definition|every_province_definition = { limit = { <triggers> } <effects> }|none|province_definition|
|every_province_definition_in_area|Iterate through all province-definitions in an area|every_province_definition_in_area = { limit = { <triggers> } <effects> }|area|province_definition|
|every_province_definition_in_scripted_geography|Iterate through all province-definitions in a scripted geography|every_province_definition_in_scripted_geography = { limit = { <triggers> } <effects> }|scripted_geography|province_definition|
|every_province_in_area|Iterate through all provinces in an area|every_province_in_area = { limit = { <triggers> } <effects> }|area|province|
|every_province_in_province_definition|Iterate through all provinces in a province-definition|every_province_in_province_definition = { limit = { <triggers> } <effects> }|province_definition|province|
|every_rebel|Iterate through all Rebels in a country|every_rebel = { limit = { <triggers> } <effects> }|country|rebels|
|every_region|Iterate through all existing regions|every_region = { limit = { <triggers> } <effects> }|none|region|
|every_region_in_continent|Iterate through all regions in a sub-continent|every_region_in_continent = { limit = { <triggers> } <effects> }|sub_continent|region|
|every_region_in_province_definition|Iterate through all regions in a province-definition|every_region_in_province_definition = { limit = { <triggers> } <effects> }|province_definition|region|
|every_related_country|Iterate through all related countries|every_related_country = { limit = { <triggers> } <effects> }|country|country|
|every_religion|Iterate through all religions|every_religion = { limit = { <triggers> } <effects> }|none|religion|
|every_religion_for_god|Iterate through all Religions of a God|every_religion_for_god = { limit = { <triggers> } <effects> }|god|religion|
|every_religion_in_religion_group|Iterate through all religions in a religion group.|every_religion_in_religion_group = { limit = { <triggers> } <effects> }|group|religion|
|every_religion_international_organization|Iterate through all international organisations of a religion|every_religion_international_organization = { limit = { <triggers> } <effects> }|religion|international_organization|
|every_religious_aspect|Iterate through all religious aspects of a Country|every_religious_aspect = { limit = { <triggers> } <effects> }|country|religious_aspect|
|every_religious_focus|Iterate through all completed religious focuses of a Country|every_religious_focus = { limit = { <triggers> } <effects> }|country|religious_focus|
|every_religious_school_in_religion|Iterate through all Religious Schools in a Religion|every_religious_school_in_religion = { limit = { <triggers> } <effects> }|religion|religious_school|
|every_rented_out_mercenary|Iterate through mercenaries a country has rented out to the market|every_rented_out_mercenary = { limit = { <triggers> } <effects> }|country|mercenary|
|every_required_goods|Iterate through all goods required by the scope production method.|every_required_goods = { limit = { <triggers> } <effects> }|production_method|goods|
|every_reserves|Iterate through all subunits on the reserve of a combat-side|every_reserves = { limit = { <triggers> } <effects> }|combat_side|sub_unit|
|every_retreated|Iterate through all subunits on the retreated of a combat-side|every_retreated = { limit = { <triggers> } <effects> }|combat_side|sub_unit|
|every_revolutionary|Iterate through all revolutionary states|every_revolutionary = { limit = { <triggers> } <effects> }|none|country|
|every_right_flank|Iterate through all subunits on the right-flank of a combat-side|every_right_flank = { limit = { <triggers> } <effects> }|combat_side|sub_unit|
|every_rival|Iterate through all rival countries|every_rival = { limit = { <triggers> } <effects> }|country|country|
|every_road_type|Iterate through all the road types|every_road_type = { limit = { <triggers> } <effects> }|none|road_type|
|every_royal_marriage|Iterate through all royal married countries|every_royal_marriage = { limit = { <triggers> } <effects> }|country|country|
|every_ruled_international_organization|Iterate through IOs a character rules|every_ruled_international_organization = { limit = { <triggers> } <effects> }|character|international_organization|
|every_ruler|Iterate through all characters that have ever been rulers in a country, including the dead|every_ruler = { limit = { <triggers> } <effects> }|country|character|
|every_ruling_countries|Iterate through countries a character rulers|every_ruling_countries = { limit = { <triggers> } <effects> }|character|country|
|every_sound_toll_in_country|Iterate through all Sound Tolls in a country|every_sound_toll_in_country = { limit = { <triggers> } <effects> }|country|location|
|every_spouse|Iterate through all spouses of a character|every_spouse = { limit = { <triggers> } <effects> }|character|character|
|every_spy_network_built_in_us|Iterate through all countries building spy networks|every_spy_network_built_in_us = { limit = { <triggers> } <effects> }|country|country|
|every_sub_continent|Iterate through all existing sub_continents|every_sub_continent = { limit = { <triggers> } <effects> }|none|sub_continent|
|every_sub_continent_in_continent|Iterate through all sub-continents in a continent|every_sub_continent_in_continent = { limit = { <triggers> } <effects> }|continent|sub_continent|
|every_sub_continent_in_scripted_geography|Iterate through all sub-continents in a scripted geography|every_sub_continent_in_scripted_geography = { limit = { <triggers> } <effects> }|scripted_geography|sub_continent|
|every_sub_unit|Iterate through all subunits in a unit|every_sub_unit = { limit = { <triggers> } <effects> }|unit|sub_unit|
|every_subject|Iterate through all subject countries|every_subject = { limit = { <triggers> } <effects> }|country|country|
|every_subject_or_below|Iterate through all subject countries and their subject countries, and so on|every_subject_or_below = { limit = { <triggers> } <effects> }|country|country|
|every_tolerated_culture|Iterate through all Tolerated cultures in a country|every_tolerated_culture = { limit = { <triggers> } <effects> }|country|culture|
|every_town_rights_in_country|Iterate through all Town Rights in a country|every_town_rights_in_country = { limit = { <triggers> } <effects> }|country|town_rights|
|every_town_rights_in_location|Iterate through all Town Rights in a location|every_town_rights_in_location = { limit = { <triggers> } <effects> }|location|town_rights|
|every_trade|Iterate through all trades in a Country|every_trade = { limit = { <triggers> } <effects> }|country|trade|
|every_trait|Iterate through all traits of a character|every_trait = { limit = { <triggers> } <effects> }|character|trait|
|every_union_partner|Iterate through all countries which are in a personal union with the current country scope.|every_union_partner = { limit = { <triggers> } <effects> }|country|country|
|every_unit|Iterate through all units in a country|every_unit = { limit = { <triggers> } <effects> }|country|unit|
|every_unit_in_location|Iterate through all units in a location|every_unit_in_location = { limit = { <triggers> } <effects> }|location|unit|
|every_valid_religion_for_aspect|Iterate through all religion that an aspect can be for|every_valid_religion_for_aspect = { limit = { <triggers> } <effects> }|religious_aspect|religion|
|every_voter|Iterate through all voters in an active resolution|every_voter = { limit = { <triggers> } <effects> }|active_resolution|country|
|every_war|Iterate through all wars going on globally|every_war = { limit = { <triggers> } <effects> }|none|war|
|every_war_participant|Iterate through all participants of a war|every_war_participant = { limit = { <triggers> } <effects> }|war|country|
|every_weather_system_in_location|Iterate through all weather systems in a location|every_weather_system_in_location = { limit = { <triggers> } <effects> }|location|weather_system|
|every_west_of_province_definition|Iterate through all province-definitions west of a province-definition|every_west_of_province_definition = { limit = { <triggers> } <effects> }|province_definition|province_definition|
|every_work_of_art|Iterate through all WorkOfArts in the world|every_work_of_art = { limit = { <triggers> } <effects> }|none|work_of_art|
|every_work_of_art_by_creator|Iterate through all work_of_art by a particular artist|every_work_of_art_by_creator = { limit = { <triggers> } <effects> }|character|work_of_art|
|every_work_of_art_in_country|Iterate through all work_of_art in a country|every_work_of_art_in_country = { limit = { <triggers> } <effects> }|country|work_of_art|
|every_work_of_art_in_location|Iterate through all work_of_art in a location|every_work_of_art_in_location = { limit = { <triggers> } <effects> }|location|work_of_art|
|ordered_accepted_culture|Iterate through all accepted cultures in a country|ordered_accepted_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|culture|
|ordered_active_disaster|Iterate through all active disasters for a country|ordered_active_disaster = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|disaster|
|ordered_active_estate|Iterate through all active estates (non-crown)|ordered_active_estate = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|estate_type|
|ordered_active_resolution|Iterate through all currently active resolutions in an international organization or situation|ordered_active_resolution = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization, situation|active_resolution|
|ordered_adjacent_ports_to_area|Iterate through all adjacent ports of an seazone area|ordered_adjacent_ports_to_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area|location|
|ordered_advance_definition|Iterate through all advance definitions|ordered_advance_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|advance_type|
|ordered_allowed_estate_in_heir_selection|Iterate through all allowed estates a HeirSelection has|ordered_allowed_estate_in_heir_selection = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|heir_selection|estate_type|
|ordered_ancestor|Iterate through all ancestors (parents, grandparents etc) of a character|ordered_ancestor = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|character|
|ordered_area|Iterate through all existing areas|ordered_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|area|
|ordered_area_in_region|Iterate through all areas in a region|ordered_area_in_region = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|region|area|
|ordered_area_in_scripted_geography|Iterate through all areas in a scripted geography|ordered_area_in_scripted_geography = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|scripted_geography|area|
|ordered_area_with_core|Iterate through all areas with cored locations in a country|ordered_area_with_core = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|area|
|ordered_area_with_owned_province|Iterate through all areas with owned provinces in a country|ordered_area_with_owned_province = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|area|
|ordered_army|Iterate through all armies in a country|ordered_army = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|unit|
|ordered_artist|Iterate through all artists in a country|ordered_artist = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|character|
|ordered_attacker|Iterate through all attackers of a war|ordered_attacker = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|war|country|
|ordered_available_dynasty_member|Iterate through adult dynasty members who are not a ruler or heir (cached)|ordered_available_dynasty_member = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|dynasty|character|
|ordered_avatar_for_god|Iterate through all Avatars of a God|ordered_avatar_for_god = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|god|avatar|
|ordered_besieging_units|Iterate through all units participating in a siege|ordered_besieging_units = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|siege|unit|
|ordered_border_location|Iterate through all owned location in a country which border locations not owned by the current country scope.|ordered_border_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_buildable_building_type|Iterate through all the building types a country can build|ordered_buildable_building_type = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|building_type|
|ordered_building_owned_by_estate|Iterate through all buildings that an estate has|ordered_building_owned_by_estate = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|estate|building|
|ordered_building_type|Iterate through all the building types|ordered_building_type = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|building_type|
|ordered_buildings_in_location|Iterate through all buildings in a location|ordered_buildings_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|building|
|ordered_cabinet|Iterate through all actions in a country's cabinet|ordered_cabinet = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|cabinet|
|ordered_cabinet_action|Iterate through all actions in a country's cabinet actions|ordered_cabinet_action = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|cabinet_action|
|ordered_cabinet_character|Iterate through all characters in a country that is in the cabinet|ordered_cabinet_character = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|character|
|ordered_cardinal_in_country|Iterate through all Cardinals in a country|ordered_cardinal_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|cardinal|
|ordered_cardinal_in_religion|Iterate through all Cardinals in a Religion|ordered_cardinal_in_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|cardinal|
|ordered_casus_belli_on_us|Iterate through all countries have a casus belli on us|ordered_casus_belli_on_us = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_casus_belli_target|Iterate through all countries we have a casus belli on|ordered_casus_belli_target = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_center|Iterate through all subunits on the center of a combat-side|ordered_center = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|combat_side|sub_unit|
|ordered_character|Iterate through all characters in a country|ordered_character = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|character|
|ordered_character_in_dynasty|Iterate through all living characters in a Dynasty|ordered_character_in_dynasty = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|dynasty|character|
|ordered_character_supporting_rebel|Iterate through all characters supporting a rebel|ordered_character_supporting_rebel = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|rebels|character|
|ordered_child|Iterate through all children of a character|ordered_child = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|character|
|ordered_close_relative|Iterate through all close relatives of a character|ordered_close_relative = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|character|
|ordered_coast_border_location|Iterate through all bordering, or across one seazone of a location|ordered_coast_border_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|location|
|ordered_colonial_charter|Iterate through all colonial charters in a country|ordered_colonial_charter = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|colonial_charter|
|ordered_colonial_claim_province_definition|Iterate through all province definitions with colonial claims from the scope country.|ordered_colonial_claim_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|province_definition|
|ordered_colonial_country|Iterate through all colonial countries in the world|ordered_colonial_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|country|
|ordered_colonial_overlord|Iterate through all colonial overlord countries in the world|ordered_colonial_overlord = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|country|
|ordered_colonial_top_overlord|Iterate through all countries in the world that have a colonial country among their subjects or their subjects subjects and so on|ordered_colonial_top_overlord = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|country|
|ordered_connected_location|Iterate through all locations in the same country as the scope location that are connected by land or strait|ordered_connected_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|location|
|ordered_construction_material_for_building_type|Iterate through all goods required to construct a building type|ordered_construction_material_for_building_type = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|building_type|goods|
|ordered_continent|Iterate through all existing continents|ordered_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|continent|
|ordered_continent_in_scripted_geography|Iterate through all continents in a scripted geography|ordered_continent_in_scripted_geography = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|scripted_geography|continent|
|ordered_controlled_location|Iterate through all controlled location in a country|ordered_controlled_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_core_in_location|Iterate through all cores in a location|ordered_core_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|country|
|ordered_core_location|Iterate through all core locations in a country|ordered_core_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_country|Iterate through all existing countries|ordered_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|country|
|ordered_country_annexing_us|Iterate through all countries which are currently annexing the current country scope.|ordered_country_annexing_us = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_at_war_with|Iterate through all countries at war with|ordered_country_at_war_with = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_in_culture|Iterate through all countries with this primary culture|ordered_country_in_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|culture|country|
|ordered_country_in_culture_group|Iterate through all countries in a culture group.|ordered_country_in_culture_group = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|culture_group|country|
|ordered_country_in_diplomatic_range|Iterate through all countries in diplomatic range|ordered_country_in_diplomatic_range = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_in_dynasty|Iterate through all countries in a Dynasty|ordered_country_in_dynasty = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|dynasty|country|
|ordered_country_in_hierarchy|Iterate through every country in the entire overlord/subject hierarchy, from the independent top overlord to the deepest subjects|ordered_country_in_hierarchy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_in_religion|Iterate through all countries in a religion|ordered_country_in_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|country|
|ordered_country_in_religion_group|Iterate through all countries in a religion group.|ordered_country_in_religion_group = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|group|country|
|ordered_country_in_religious_school|Iterate through all countries within a school|ordered_country_in_religious_school = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religious_school|country|
|ordered_country_lent_to|Iterate through all countries a country has lent to|ordered_country_lent_to = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_sub_unit|Iterate through all subunits in all units in a country|ordered_country_sub_unit = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|sub_unit|
|ordered_country_supporting_rebel|Iterate through all countries supporting a rebel|ordered_country_supporting_rebel = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|rebels|country|
|ordered_country_that_can_be_called_defensively|Iterate through all countries that may be called into a defensive war.|ordered_country_that_can_be_called_defensively = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_that_can_be_called_offensively|Iterate through all countries that may be called into an offensive war.|ordered_country_that_can_be_called_offensively = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_together_in_war_with|Iterate through all countries which are an ally in any of the country scope's wars|ordered_country_together_in_war_with = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_we_are_annexing|Iterate through all countries which are currently annexed by the current country scope.|ordered_country_we_are_annexing = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_with_antagonism_against_us|Iterate through all countries who have antagonism against us|ordered_country_with_antagonism_against_us = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_with_capital_in_geography|Iterate through all countries which have their capital in the specified geography|ordered_country_with_capital_in_geography = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|ordered_country_with_cardinals|Iterate through all countries with cardinals in a religion|ordered_country_with_cardinals = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|country|
|ordered_country_with_coalition_grade_antagonism_against_us|Iterate through all countries who have coalition grade antagonism against us|ordered_country_with_coalition_grade_antagonism_against_us = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_with_relation_that_can_be_annulled|Iterate through all countries which have an annullable relation with the scope country.|ordered_country_with_relation_that_can_be_annulled = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_country_with_succession_law|Iterate through all countries with a cached succession law (set cached = yes in the heir_selection to use this)|ordered_country_with_succession_law = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|country|
|ordered_culture|Iterate through all cultures|ordered_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|culture|
|ordered_culture_group|Iterate through all culture groups the culture is in.|ordered_culture_group = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|culture|culture_group|
|ordered_culture_in_culture_group|Iterate through all cultures in a culture group.|ordered_culture_in_culture_group = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|culture_group|culture|
|ordered_current_avatars|Iterate through all Avatars a country has|ordered_current_avatars = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|avatar|
|ordered_current_bureaucracy|Iterate through all Bureaucracies a country has|ordered_current_bureaucracy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|bureaucracy|
|ordered_current_bureaucracy_type|Iterate through all Bureaucracy types a country has|ordered_current_bureaucracy_type = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|bureaucracy_type|
|ordered_current_gods|Iterate through all Gods a country worships|ordered_current_gods = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|god|
|ordered_current_law|Iterate through all laws of a country.|ordered_current_law = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|law|
|ordered_current_law_in_international_organization|Iterate through all laws that are codified in the international organization|ordered_current_law_in_international_organization = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|law|
|ordered_current_policy|Iterate through all policies that are codified in the country|ordered_current_policy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|policy|
|ordered_current_policy_in_international_organization|Iterate through all policies that are codified in the international organization|ordered_current_policy_in_international_organization = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|policy|
|ordered_current_reforms|Iterate through all Government Reforms a country has|ordered_current_reforms = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|government_reform|
|ordered_current_war|Iterate through all wars of a country|ordered_current_war = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|war|
|ordered_defender|Iterate through all defenders of a war|ordered_defender = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|war|country|
|ordered_descendant|Iterate through all descendants (children, grandchildren etc) of a character|ordered_descendant = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|character|
|ordered_disloyal_subject|Iterate through all loyal subject countries|ordered_disloyal_subject = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_dynasty|Iterate through all dynasties in a country|ordered_dynasty = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|dynasty|
|ordered_east_of_province_definition|Iterate through all province-definitions east of a province-definition|ordered_east_of_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|province_definition|province_definition|
|ordered_election_candidates|Iterate through all election candidates of a country with elections!|ordered_election_candidates = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|character|
|ordered_enemy|Iterate through all Enemy countries|ordered_enemy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_enemy_war_leader|Iterate through all countries which are leading a war against the scope|ordered_enemy_war_leader = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_estate|Iterate through all estates in a country|ordered_estate = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|estate|
|ordered_estate_privilege|Iterate through all current estate privileges of a Country|ordered_estate_privilege = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|estate_privilege|
|ordered_estate_type_preferring|Iterate through all estate types that a prefer a policy|ordered_estate_type_preferring = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|policy|estate_type|
|ordered_estate_type_that_dislikes_bureaucracy|Iterate through all estate types that do NOT prefer a bureaucracy|ordered_estate_type_that_dislikes_bureaucracy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|bureaucracy_type|estate_type|
|ordered_estate_type_that_likes_bureaucracy|Iterate through all estate types that a prefer a bureaucracy|ordered_estate_type_that_likes_bureaucracy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|bureaucracy_type|estate_type|
|ordered_exploration_from_country|Iterate through all Explorations a country has|ordered_exploration_from_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|exploration|
|ordered_export|Iterate through all exports in a market|ordered_export = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|market|trade|
|ordered_export_from_location|Iterate through all exports from location|ordered_export_from_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|location|
|ordered_food_goods|Iterate through all food-goods|ordered_food_goods = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|food|
|ordered_foreign_building_countries_in_location|Iterate through all foreign building countries in a location|ordered_foreign_building_countries_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|country|
|ordered_foreign_buildings_in_location|Iterate through all foreign buildings in a location|ordered_foreign_buildings_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|building|
|ordered_fort_in_country|Iterate through all Forts in a country|ordered_fort_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_friendly_coast_border_location|Iterate through all friendly bordering, or across one seazone of a location|ordered_friendly_coast_border_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|location|
|ordered_friendly_country|Iterate through all countries with relations marked as friendly|ordered_friendly_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_friendly_or_high_opinion_country|Iterate through all countries with relations marked as friendly or that we have a high opinion of set in defines|ordered_friendly_or_high_opinion_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_friendly_to_friendly_country|Iterate through all friends of our friends|ordered_friendly_to_friendly_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_friendly_to_hostile_country|Iterate through all friends of our enemies|ordered_friendly_to_hostile_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_god_in_religion|Iterate through all Gods in a Religion|ordered_god_in_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|god|
|ordered_good_in_demand|Iterate through all goods in a goods demand|ordered_good_in_demand = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|demand|goods|
|ordered_goods|Iterate through all types of goods|ordered_goods = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|goods|
|ordered_graphical_culture_in_culture|Iterate through all graphical culture in a culture|ordered_graphical_culture_in_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|culture|graphical_culture|
|ordered_great_power|Iterate through all great powers|ordered_great_power = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|country|
|ordered_heathen_location|Iterate through all heathen locations in a country|ordered_heathen_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_heretic_location|Iterate through all Heretic locations in a country|ordered_heretic_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_hired_mercenary|Iterate through mercenaries a country has hired|ordered_hired_mercenary = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|mercenary|
|ordered_historical_enemy|Iterate through all historical Enemy countries|ordered_historical_enemy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_historical_rival|Iterate through all historical rival countries|ordered_historical_rival = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_holy_site_in_country|Iterate through all Holy Sites in a country|ordered_holy_site_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|holy_site|
|ordered_holy_site_in_religion|Iterate through all Holy Sites in a Religion|ordered_holy_site_in_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|holy_site|
|ordered_hostile_country|Iterate through all countries with relations marked as hostile|ordered_hostile_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_hostile_or_low_opinion_country|Iterate through all countries with relations marked as hostile or that we have a low opinion of set in defines|ordered_hostile_or_low_opinion_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_hostile_to_friendly_country|Iterate through all enemies of our friends|ordered_hostile_to_friendly_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_hostile_to_hostile_country|Iterate through all enemies of our enemies|ordered_hostile_to_hostile_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_import|Iterate through all imports in a market|ordered_import = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|market|trade|
|ordered_import_from_location|Iterate through all Imports from location|ordered_import_from_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|location|
|ordered_in_global_list|Iterate through all items in global list.|ordered_in_global_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_in_list|Iterate through all items in list.|ordered_in_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_in_local_list|Iterate through all items in local list.|ordered_in_local_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_institutions_embraced|Iterate through all institutions a country has embraced|ordered_institutions_embraced = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|institution|
|ordered_international_organization|Iterate through all international organizations|ordered_international_organization = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|international_organization|
|ordered_international_organization_elector|Iterate through all countries with an elector special status in the international organization|ordered_international_organization_elector = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|country|
|ordered_international_organization_enemy|Iterate through all countries that are enemies of the international organization|ordered_international_organization_enemy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|country|
|ordered_international_organization_member|Iterate through all countries that are members of the international organization|ordered_international_organization_member = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|country|
|ordered_international_organization_owned_location|Iterate through all locations that are owned by the international organization|ordered_international_organization_owned_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|location|
|ordered_international_organization_owner|Iterate through all international organizations which own the location scope|ordered_international_organization_owner = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|international_organization|
|ordered_international_organization_parliament_opposers|Iterate through all countries that have voted AGAINST the parliament issue in the in the parliament of the international organization and support the current debate|ordered_international_organization_parliament_opposers = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|country|
|ordered_international_organization_parliament_supporter|Iterate through all countries that have voted FOR the parliament issue in the parliament of the international organization and support the current debate|ordered_international_organization_parliament_supporter = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|international_organization|country|
|ordered_international_organizations_member_of|Iterate through all international organizations a country is a member of|ordered_international_organizations_member_of = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|international_organization|
|ordered_international_organizations_target_of|Iterate through all international organizations a country is a target of|ordered_international_organizations_target_of = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|international_organization|
|ordered_invited_religious_figure|Iterate through all invited religious figures in a Country|ordered_invited_religious_figure = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|character|
|ordered_key_in_global_variable_map|Iterate through all keys in a global variable map.|ordered_key_in_global_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_key_in_local_variable_map|Iterate through all keys in a local variable map.|ordered_key_in_local_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_key_in_variable_map|Iterate through all keys in a variable map.|ordered_key_in_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_known_country|Iterate through all known countries|ordered_known_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_known_institution|Iterate through all institutions a country knows of|ordered_known_institution = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|institution|
|ordered_left_flank|Iterate through all subunits on the left-flank of a combat-side|ordered_left_flank = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|combat_side|sub_unit|
|ordered_lent_loan|Iterate through all loans that a country lent|ordered_lent_loan = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|loan|
|ordered_loan|Iterate through all loans in a country|ordered_loan = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|loan|
|ordered_loan_lent_to_country|Iterate through all loans a country has lent to the supplied borrower country|ordered_loan_lent_to_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|loan|
|ordered_location_in_area|Iterate through all Locations in a area|ordered_location_in_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area|location|
|ordered_location_in_continent|Iterate through all Locations in a continent|ordered_location_in_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|continent|location|
|ordered_location_in_market|Iterate through all locations in a market|ordered_location_in_market = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|market|location|
|ordered_location_in_province|Iterate through all Locations in a province|ordered_location_in_province = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|province|location|
|ordered_location_in_province_definition|Iterate through all Locations in a province definition|ordered_location_in_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|province_definition|location|
|ordered_location_in_region|Iterate through all Locations in a region|ordered_location_in_region = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|region|location|
|ordered_location_in_scripted_geography|Iterate through all locations in a scripted geography|ordered_location_in_scripted_geography = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|region|scripted_geography|
|ordered_location_in_sub_continent|Iterate through all Locations in a sub-continent|ordered_location_in_sub_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|sub_continent|location|
|ordered_location_in_the_world|Iterate through all location|ordered_location_in_the_world = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|location|
|ordered_location_with_movement|Iterate through all locations affected by the scope movement|ordered_location_with_movement = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|movement|location|
|ordered_location_with_town_rights_in_country|Iterate through all locations with Town Rights in a country|ordered_location_with_town_rights_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_loyal_subject|Iterate through all loyal subject countries|ordered_loyal_subject = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_maritime_area|Iterate through all maritime areas for a country|ordered_maritime_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|area|
|ordered_market_center_in_country|Iterate through all markets in a country which market centers are owned by the country|ordered_market_center_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|market|
|ordered_market_in_world|Iterate through all markets in the world|ordered_market_in_world = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|market|
|ordered_market_present_in_country|Iterate through all markets in a country|ordered_market_present_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|market|
|ordered_market_with_merchants|Iterate through all markets a country has active merchants|ordered_market_with_merchants = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|market|
|ordered_mercenary|Iterate through all mercenaries in the world|ordered_mercenary = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|mercenary|
|ordered_mercenary_sub_unit|Iterate through all subunits in a Mercenary|ordered_mercenary_sub_unit = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|mercenary|sub_unit|
|ordered_merchant_in_market|Iterate through all merchants in a market|ordered_merchant_in_market = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|market|country|
|ordered_movement|Iterate through all movements|ordered_movement = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|movement|
|ordered_movement_in_country|Iterate through all movements in a country|ordered_movement_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|movement|
|ordered_movement_in_culture|Iterate through all movements in a culture|ordered_movement_in_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|culture|movement|
|ordered_movement_in_religion|Iterate through all movements in a religion|ordered_movement_in_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|movement|
|ordered_navy|Iterate through all navies in a country|ordered_navy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|unit|
|ordered_neighbor_area|Iterate through all neighboring areas in a area|ordered_neighbor_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area|area|
|ordered_neighbor_country|Iterate through all neighbour countries|ordered_neighbor_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_neighbor_location|Iterate through all neighbors of a location|ordered_neighbor_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|location|
|ordered_neighbor_province_definition|Iterate through all neighboring ProvinceDefinitions in a ProvinceDefinition|ordered_neighbor_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|province_definition|province_definition|
|ordered_new_world_goods|Iterate through all new-world goods|ordered_new_world_goods = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|goods|
|ordered_nomad_countries_in_location|Iterate through all nomad pop countries in a location|ordered_nomad_countries_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|country|
|ordered_non_state_religion_location|Iterate through all NonStateReligion locations in a country|ordered_non_state_religion_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_old_world_goods|Iterate through all old-world goods|ordered_old_world_goods = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|goods|
|ordered_omen_in_country|Iterate through all Omens active in a country|ordered_omen_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|omen|
|ordered_omen_in_god|Iterate through all Omens associated with a God|ordered_omen_in_god = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|god|omen|
|ordered_omen_in_religion|Iterate through all Omens in a religion|ordered_omen_in_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|omen|
|ordered_other_core_country|Iterate through all other countries which have a core on the current country|ordered_other_core_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_other_country|Iterate through all other countries|ordered_other_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_other_great_power|Iterate through all other great powers|ordered_other_great_power = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_other_religion_in_same_group|Iterate through all other religions that has the same group as Religion|ordered_other_religion_in_same_group = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|religion|
|ordered_other_revolutionary|Iterate through all other revolutionary countries|ordered_other_revolutionary = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_overlord_or_above|Iterate through your overlord, your overlord's overlord, and so on|ordered_overlord_or_above = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_ownable_location|Iterate through all ownable location|ordered_ownable_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|location|
|ordered_ownable_location_in_area|Iterate through all ownable Locations in an area|ordered_ownable_location_in_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area|location|
|ordered_ownable_location_in_continent|Iterate through all ownable Locations in a continent|ordered_ownable_location_in_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|continent|location|
|ordered_ownable_location_in_province_definition|Iterate through all ownable Locations in a province definition|ordered_ownable_location_in_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|province_definition|location|
|ordered_ownable_location_in_region|Iterate through all ownable Locations in a region|ordered_ownable_location_in_region = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|region|location|
|ordered_ownable_location_in_scripted_geography|Iterate through all ownable Locations in a scripted geography|ordered_ownable_location_in_scripted_geography = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|scripted_geography|location|
|ordered_ownable_location_in_sub_continent|Iterate through all ownable Locations in a sub continent|ordered_ownable_location_in_sub_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|sub_continent|location|
|ordered_owned_building|Iterate through all the owned buildings in a country|ordered_owned_building = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|building|
|ordered_owned_foreign_building|Iterate through all the owned foreign buildings in a country|ordered_owned_foreign_building = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|building|
|ordered_owned_foreign_building_location|Iterate through all the location of owned foreign buildings in a country|ordered_owned_foreign_building_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_owned_foreign_building_region|Iterate through all the regions of owned foreign buildings in a country|ordered_owned_foreign_building_region = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|region|
|ordered_owned_location|Iterate through all owned location in a country|ordered_owned_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_owned_nomad_pop|Iterate through all owned nomad pops in a country|ordered_owned_nomad_pop = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|pop|
|ordered_owned_non_rural_location|Iterate through all owned non-rural locations in a country|ordered_owned_non_rural_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_owned_rural_location|Iterate through all owned rural locations in a country|ordered_owned_rural_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_owner_in_region|Iterate through all the countries that own locations in a region|ordered_owner_in_region = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|region|country|
|ordered_parent|Iterate through parents (order: father, mother) of a character.|ordered_parent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|character|
|ordered_participating_countries|Iterate through all Countrys participating in 1 side of a combat|ordered_participating_countries = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|combat_side|country|
|ordered_participating_units|Iterate through all units participating in 1 side of a combat|ordered_participating_units = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|combat_side|unit|
|ordered_past_liturgical_dialect|Iterate through all liturgical dialects a country has had before|ordered_past_liturgical_dialect = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_policy_in_law|Iterate through all policies that are part of the law scope|ordered_policy_in_law = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|law|policy|
|ordered_political_border_location|Iterate through all owned location in a country which border another country.|ordered_political_border_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_pop|Iterate through all pops in a location or country|ordered_pop = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country, location|pop|
|ordered_pops_supporting_rebel|Iterate through all pops supporting a rebel|ordered_pops_supporting_rebel = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|rebels|pop|
|ordered_port_in_country|Iterate through all Ports in a country|ordered_port_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_possible_disaster|Iterate through all possible disasters for a country|ordered_possible_disaster = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|disaster|
|ordered_possible_parliament_issue|Iterate through all possible parliament issues in a country's or an international organization's parliament|ordered_possible_parliament_issue = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country, international_organization|parliament_issue|
|ordered_possible_policy|Iterate through all possible policies of a Country that is not currently implemeted|ordered_possible_policy = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|policy|
|ordered_possible_privilege|Iterate through all possible & allowed estate privileges of a Country that is not currently implemeted|ordered_possible_privilege = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|estate|estate_privilege|
|ordered_possible_recruit_location|Iterate through all possible recruit locations in a country|ordered_possible_recruit_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_present_country|Iterate through all countries in the specified geography|ordered_present_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|ordered_present_culture_in_country|Iterate through all cultures present in the country.|ordered_present_culture_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|culture|
|ordered_present_culture_in_location|Iterate through all cultures present in the location.|ordered_present_culture_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|culture|
|ordered_present_overlord|Iterate through all countries which have a subject in the specified geography|ordered_present_overlord = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|ordered_present_religion_in_country|Iterate through all religions present in the country.|ordered_present_religion_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|religion|
|ordered_present_religion_in_location|Iterate through all religions present in the location.|ordered_present_religion_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|religion|
|ordered_primary_or_accepted_culture|Iterate through primary culture and all accepted cultures in a country. Primary is ordered first.|ordered_primary_or_accepted_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|culture|
|ordered_primary_or_accepted_or_tolerated_culture|Iterate through primary culture and all accepted and all tolerated cultures in a country. Primary is ordered first.|ordered_primary_or_accepted_or_tolerated_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|culture|
|ordered_privateer|Iterate through all privateers in the world|ordered_privateer = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|privateer|
|ordered_privateer_from_country|Iterate through all privateers a country has|ordered_privateer_from_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|privateer|
|ordered_privateer_in_area|Iterate through all privateers in a area|ordered_privateer_in_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area|privateer|
|ordered_production_method|Iterate through all types of production methods.|ordered_production_method = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|production_method|
|ordered_production_method_of_building|Iterate through all available production methods of the building.|ordered_production_method_of_building = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|building|production_method|
|ordered_province|Iterate through all provinces in a country|ordered_province = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|province|
|ordered_province_definition|Iterate through all existing province_definition|ordered_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|province_definition|
|ordered_province_definition_in_area|Iterate through all province-definitions in an area|ordered_province_definition_in_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area|province_definition|
|ordered_province_definition_in_scripted_geography|Iterate through all province_definitions in a scripted geography|ordered_province_definition_in_scripted_geography = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|scripted_geography|province_definition|
|ordered_province_in_area|Iterate through all provinces in an area|ordered_province_in_area = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|area|province|
|ordered_province_in_province_definition|Iterate through all provinces in a province-definition|ordered_province_in_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|province_definition|province|
|ordered_rebel|Iterate through all Rebels in a country|ordered_rebel = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|rebels|
|ordered_region|Iterate through all existing regions|ordered_region = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|region|
|ordered_region_in_continent|Iterate through all regions in a sub-continent|ordered_region_in_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|sub_continent|region|
|ordered_region_in_scripted_geography|Iterate through all regions in a scripted_geography|ordered_region_in_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|scripted_geography|region|
|ordered_related_country|Iterate through all related countries|ordered_related_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_religion|Iterate through all religions|ordered_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|religion|
|ordered_religion_for_god|Iterate through all Religions of a God|ordered_religion_for_god = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|god|religion|
|ordered_religion_in_religion_group|Iterate through all religions in a religion group.|ordered_religion_in_religion_group = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|group|religion|
|ordered_religion_international_organization|Iterate through all international organisations of a religion|ordered_religion_international_organization = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|international_organization|
|ordered_religious_aspect|Iterate through all religious aspects of a Country|ordered_religious_aspect = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|religious_aspect|
|ordered_religious_focus|Iterate through all completed religious focuses of a Country|ordered_religious_focus = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|religious_focus|
|ordered_religious_school_in_religion|Iterate through all Religious Schools in a Religion|ordered_religious_school_in_religion = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religion|religious_school|
|ordered_rented_out_mercenary|Iterate through mercenaries a country has rented out to the market|ordered_rented_out_mercenary = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|mercenary|
|ordered_required_goods|Iterate through all goods required by the scope production method.|ordered_required_goods = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|production_method|goods|
|ordered_reserves|Iterate through all subunits on the reserve of a combat-side|ordered_reserves = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|combat_side|sub_unit|
|ordered_retreated|Iterate through all subunits on the retreated of a combat-side|ordered_retreated = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|combat_side|sub_unit|
|ordered_revolutionary|Iterate through all revolutionary states|ordered_revolutionary = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|country|
|ordered_right_flank|Iterate through all subunits on the right-flank of a combat-side|ordered_right_flank = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|combat_side|sub_unit|
|ordered_rival|Iterate through all rival countries|ordered_rival = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_road_type|Iterate through all the road types|ordered_road_type = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|road_type|
|ordered_royal_marriage|Iterate through all royal married countries|ordered_royal_marriage = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_ruled_international_organization|Iterate through IOs a character rules|ordered_ruled_international_organization = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|international_organization|
|ordered_ruler|Iterate through all characters that have ever been rulers in a country, including the dead|ordered_ruler = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|character|
|ordered_ruling_countries|Iterate through countries a character rulers|ordered_ruling_countries = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|country|
|ordered_sound_toll_in_country|Iterate through all Sound Tolls in a country|ordered_sound_toll_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|location|
|ordered_spouse|Iterate through all spouses of a character|ordered_spouse = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|character|
|ordered_spy_network_built_in_us|Iterate through all countries building spy networks|ordered_spy_network_built_in_us = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_sub_continent|Iterate through all existing sub_continents|ordered_sub_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|sub_continent|
|ordered_sub_continent_in_continent|Iterate through all sub-continents in a continent|ordered_sub_continent_in_continent = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|continent|sub_continent|
|ordered_sub_continent_in_scripted_geography|Iterate through all sub-continents in a scripted geography|ordered_sub_continent_in_scripted_geography = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|scripted_geography|sub_continent|
|ordered_sub_unit|Iterate through all subunits in a unit|ordered_sub_unit = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|unit|sub_unit|
|ordered_subject|Iterate through all subject countries|ordered_subject = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_subject_or_below|Iterate through all subject countries and their subject countries, and so on|ordered_subject_or_below = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_tolerated_culture|Iterate through all Tolerated cultures in a country|ordered_tolerated_culture = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|culture|
|ordered_town_rights_in_country|Iterate through all Town Rights in a country|ordered_town_rights_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|town_rights|
|ordered_town_rights_in_location|Iterate through all Town Rights in a location|ordered_town_rights_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|town_rights|
|ordered_trade|Iterate through all trades in a Country|ordered_trade = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|trade|
|ordered_trait|Iterate through all traits of a character|ordered_trait = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|trait|
|ordered_union_partner|Iterate through all countries which are in a personal union with the current country scope.|ordered_union_partner = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|country|
|ordered_unit|Iterate through all units in a country|ordered_unit = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|unit|
|ordered_unit_in_location|Iterate through all units in a location|ordered_unit_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|unit|
|ordered_valid_religion_for_aspect|Iterate through all religion that an aspect can be for|ordered_valid_religion_for_aspect = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|religious_aspect|religion|
|ordered_voter|Iterate through all voters in an active resolution|ordered_voter = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|active_resolution|country|
|ordered_war|Iterate through all wars going on globally|ordered_war = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|war|
|ordered_war_participant|Iterate through all participants of a war|ordered_war_participant = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|war|country|
|ordered_weather_system_in_location|Iterate through all weather systems in a location|ordered_weather_system_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|weather_system|
|ordered_west_of_province_definition|Iterate through all province-definitions west of a province-definition|ordered_west_of_province_definition = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|province_definition|province_definition|
|ordered_work_of_art|Iterate through all WorkOfArts in the world|ordered_work_of_art = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|none|work_of_art|
|ordered_work_of_art_by_creator|Iterate through all work_of_art by a particular artist|ordered_work_of_art_by_creator = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|character|work_of_art|
|ordered_work_of_art_in_country|Iterate through all work_of_art in a country|ordered_work_of_art_in_country = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|work_of_art|
|ordered_work_of_art_in_location|Iterate through all work_of_art in a location|ordered_work_of_art_in_location = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|location|work_of_art|
|random_accepted_culture|Iterate through all accepted cultures in a country|random_accepted_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|culture|
|random_active_disaster|Iterate through all active disasters for a country|random_active_disaster = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|disaster|
|random_active_estate|Iterate through all active estates (non-crown)|random_active_estate = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|estate_type|
|random_active_resolution|Iterate through all currently active resolutions in an international organization or situation|random_active_resolution = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization, situation|active_resolution|
|random_adjacent_ports_to_area|Iterate through all adjacent ports of an seazone area|random_adjacent_ports_to_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area|location|
|random_advance_definition|Iterate through all advance definitions|random_advance_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|advance_type|
|random_allowed_estate_in_heir_selection|Iterate through all allowed estates a HeirSelection has|random_allowed_estate_in_heir_selection = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|heir_selection|estate_type|
|random_ancestor|Iterate through all ancestors (parents, grandparents etc) of a character|random_ancestor = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|character|
|random_area|Iterate through all existing areas|random_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|area|
|random_area_in_region|Iterate through all areas in a region|random_area_in_region = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|region|area|
|random_area_in_scripted_geography|Iterate through all areas in a scripted geography|random_area_in_scripted_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|scripted_geography|area|
|random_area_with_core|Iterate through all areas with cored locations in a country|random_area_with_core = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|area|
|random_area_with_owned_province|Iterate through all areas with owned provinces in a country|random_area_with_owned_province = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|area|
|random_army|Iterate through all armies in a country|random_army = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|unit|
|random_artist|Iterate through all artists in a country|random_artist = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|character|
|random_attacker|Iterate through all attackers of a war|random_attacker = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|war|country|
|random_available_dynasty_member|Iterate through adult dynasty members who are not a ruler or heir (cached)|random_available_dynasty_member = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|dynasty|character|
|random_avatar_for_god|Iterate through all Avatars of a God|random_avatar_for_god = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|god|avatar|
|random_besieging_units|Iterate through all units participating in a siege|random_besieging_units = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|siege|unit|
|random_border_location|Iterate through all owned location in a country which border locations not owned by the current country scope.|random_border_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_buildable_building_type|Iterate through all the building types a country can build|random_buildable_building_type = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|building_type|
|random_building_owned_by_estate|Iterate through all buildings that an estate has|random_building_owned_by_estate = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|estate|building|
|random_building_type|Iterate through all the building types|random_building_type = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|building_type|
|random_buildings_in_location|Iterate through all buildings in a location|random_buildings_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|building|
|random_cabinet|Iterate through all actions in a country's cabinet|random_cabinet = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|cabinet|
|random_cabinet_action|Iterate through all actions in a country's cabinet actions|random_cabinet_action = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|cabinet_action|
|random_cabinet_character|Iterate through all characters in a country that is in the cabinet|random_cabinet_character = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|character|
|random_cardinal_in_country|Iterate through all Cardinals in a country|random_cardinal_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|cardinal|
|random_cardinal_in_religion|Iterate through all Cardinals in a Religion|random_cardinal_in_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|cardinal|
|random_casus_belli_on_us|Iterate through all countries have a casus belli on us|random_casus_belli_on_us = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_casus_belli_target|Iterate through all countries we have a casus belli on|random_casus_belli_target = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_center|Iterate through all subunits on the center of a combat-side|random_center = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|combat_side|sub_unit|
|random_character|Iterate through all characters in a country|random_character = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|character|
|random_character_in_dynasty|Iterate through all living characters in a Dynasty|random_character_in_dynasty = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|dynasty|character|
|random_character_supporting_rebel|Iterate through all characters supporting a rebel|random_character_supporting_rebel = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|rebels|character|
|random_child|Iterate through all children of a character|random_child = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|character|
|random_close_relative|Iterate through all close relatives of a character|random_close_relative = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|character|
|random_coast_border_location|Iterate through all bordering, or across one seazone of a location|random_coast_border_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|location|
|random_colonial_charter|Iterate through all colonial charters in a country|random_colonial_charter = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|colonial_charter|
|random_colonial_claim_province_definition|Iterate through all province definitions with colonial claims from the scope country.|random_colonial_claim_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|province_definition|
|random_colonial_country|Iterate through all colonial countries in the world|random_colonial_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|country|
|random_colonial_overlord|Iterate through all colonial overlord countries in the world|random_colonial_overlord = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|country|
|random_colonial_top_overlord|Iterate through all countries in the world that have a colonial country among their subjects or their subjects subjects and so on|random_colonial_top_overlord = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|country|
|random_connected_location|Iterate through all locations in the same country as the scope location that are connected by land or strait|random_connected_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|location|
|random_construction_material_for_building_type|Iterate through all goods required to construct a building type|random_construction_material_for_building_type = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|building_type|goods|
|random_continent|Iterate through all existing continents|random_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|continent|
|random_continent_in_scripted_geography|Iterate through all continents in a scripted geography|random_continent_in_scripted_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|scripted_geography|continent|
|random_controlled_location|Iterate through all controlled location in a country|random_controlled_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_core_in_location|Iterate through all cores in a location|random_core_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|country|
|random_core_location|Iterate through all core locations in a country|random_core_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_country|Iterate through all existing countries|random_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|country|
|random_country_annexing_us|Iterate through all countries which are currently annexing the current country scope.|random_country_annexing_us = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_at_war_with|Iterate through all countries at war with|random_country_at_war_with = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_in_culture|Iterate through all countries with this primary culture|random_country_in_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|culture|country|
|random_country_in_culture_group|Iterate through all countries in a culture group.|random_country_in_culture_group = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|culture_group|country|
|random_country_in_diplomatic_range|Iterate through all countries in diplomatic range|random_country_in_diplomatic_range = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_in_dynasty|Iterate through all countries in a Dynasty|random_country_in_dynasty = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|dynasty|country|
|random_country_in_hierarchy|Iterate through every country in the entire overlord/subject hierarchy, from the independent top overlord to the deepest subjects|random_country_in_hierarchy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_in_religion|Iterate through all countries in a religion|random_country_in_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|country|
|random_country_in_religion_group|Iterate through all countries in a religion group.|random_country_in_religion_group = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|group|country|
|random_country_in_religious_school|Iterate through all countries within a school|random_country_in_religious_school = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religious_school|country|
|random_country_lent_to|Iterate through all countries a country has lent to|random_country_lent_to = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_sub_unit|Iterate through all subunits in all units in a country|random_country_sub_unit = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|sub_unit|
|random_country_supporting_rebel|Iterate through all countries supporting a rebel|random_country_supporting_rebel = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|rebels|country|
|random_country_that_can_be_called_defensively|Iterate through all countries that may be called into a defensive war.|random_country_that_can_be_called_defensively = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_that_can_be_called_offensively|Iterate through all countries that may be called into an offensive war.|random_country_that_can_be_called_offensively = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_together_in_war_with|Iterate through all countries which are an ally in any of the country scope's wars|random_country_together_in_war_with = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_we_are_annexing|Iterate through all countries which are currently annexed by the current country scope.|random_country_we_are_annexing = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_with_antagonism_against_us|Iterate through all countries who have antagonism against us|random_country_with_antagonism_against_us = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_with_capital_in_geography|Iterate through all countries which have their capital in the specified geography|random_country_with_capital_in_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|random_country_with_cardinals|Iterate through all countries with cardinals in a religion|random_country_with_cardinals = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|country|
|random_country_with_coalition_grade_antagonism_against_us|Iterate through all countries who have coalition grade antagonism against us|random_country_with_coalition_grade_antagonism_against_us = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_country_with_special_status_of_type|Iterate through all countries in the international organization which have the specified special status|random_country_with_special_status_of_type = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|country|
|random_country_with_succession_law|Iterate through all countries with a cached succession law (set cached = yes in the heir_selection to use this)|random_country_with_succession_law = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|country|
|random_culture|Iterate through all cultures|random_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|culture|
|random_culture_group|Iterate through all culture groups the culture is in.|random_culture_group = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|culture|culture_group|
|random_culture_in_culture_group|Iterate through all cultures in a culture group.|random_culture_in_culture_group = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|culture_group|culture|
|random_current_avatars|Iterate through all Avatars a country has|random_current_avatars = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|avatar|
|random_current_bureaucracy|Iterate through all Bureaucracies a country has|random_current_bureaucracy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|bureaucracy|
|random_current_bureaucracy_type|Iterate through all Bureaucracy types a country has|random_current_bureaucracy_type = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|bureaucracy_type|
|random_current_gods|Iterate through all Gods a country worships|random_current_gods = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|god|
|random_current_law|Iterate through all laws of a country.|random_current_law = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|law|
|random_current_law_in_international_organization|Iterate through all laws that are codified in the international organization|random_current_law_in_international_organization = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|law|
|random_current_policy|Iterate through all policies that are codified in the country|random_current_policy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|policy|
|random_current_policy_in_international_organization|Iterate through all policies that are codified in the international organization|random_current_policy_in_international_organization = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|policy|
|random_current_reforms|Iterate through all Government Reforms a country has|random_current_reforms = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|government_reform|
|random_current_war|Iterate through all wars of a country|random_current_war = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|war|
|random_defender|Iterate through all defenders of a war|random_defender = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|war|country|
|random_descendant|Iterate through all descendants (children, grandchildren etc) of a character|random_descendant = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|character|
|random_disloyal_subject|Iterate through all loyal subject countries|random_disloyal_subject = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_dynasty|Iterate through all dynasties in a country|random_dynasty = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|dynasty|
|random_east_of_province_definition|Iterate through all province-definitions east of a province-definition|random_east_of_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|province_definition|province_definition|
|random_election_candidates|Iterate through all election candidates of a country with elections!|random_election_candidates = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|character|
|random_enemy|Iterate through all Enemy countries|random_enemy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_enemy_war_leader|Iterate through all countries which are leading a war against the scope|random_enemy_war_leader = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_estate|Iterate through all estates in a country|random_estate = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|estate|
|random_estate_privilege|Iterate through all current estate privileges of a Country|random_estate_privilege = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|estate_privilege|
|random_estate_type_preferring|Iterate through all estate types that a prefer a policy|random_estate_type_preferring = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|policy|estate_type|
|random_exploration_from_country|Iterate through all Explorations a country has|random_exploration_from_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|exploration|
|random_export|Iterate through all exports in a market|random_export = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|market|trade|
|random_export_from_location|Iterate through all exports from location|random_export_from_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|location|
|random_food_goods|Iterate through all food-goods|random_food_goods = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|goods|
|random_foreign_building_countries_in_location|Iterate through all foreign building countries in a location|random_foreign_building_countries_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|country|
|random_foreign_buildings_in_location|Iterate through all foreign buildings in a location|random_foreign_buildings_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|building|
|random_fort_in_country|Iterate through all Forts in a country|random_fort_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_friendly_coast_border_location|Iterate through all friendly bordering, or across one seazone of a location|random_friendly_coast_border_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|location|
|random_friendly_country|Iterate through all countries with relations marked as friendly|random_friendly_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_friendly_or_high_opinion_country|Iterate through all countries with relations marked as friendly or that we have a high opinion of set in defines|random_friendly_or_high_opinion_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_friendly_to_friendly_country|Iterate through all friends of our friends|random_friendly_to_friendly_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_friendly_to_hostile_country|Iterate through all friends of our enemies|random_friendly_to_hostile_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_god_in_religion|Iterate through all Gods in a Religion|random_god_in_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|god|
|random_good_in_demand|Iterate through all goods in a goods demand|random_good_in_demand = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|demand|goods|
|random_goods|Iterate through all types of goods|random_goods = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|goods|
|random_graphical_culture_in_culture|Iterate through all graphical culture in a culture|random_graphical_culture_in_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|culture|graphical_culture|
|random_great_power|Iterate through all great powers|random_great_power = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|country|
|random_heathen_location|Iterate through all heathen locations in a country|random_heathen_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_heretic_location|Iterate through all Heretic locations in a country|random_heretic_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_hired_mercenary|Iterate through mercenaries a country has hired|random_hired_mercenary = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|mercenary|
|random_historical_enemy|Iterate through all historical Enemy countries|random_historical_enemy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_historical_rival|Iterate through all historical rival countries|random_historical_rival = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_holy_site_in_country|Iterate through all Holy Sites in a country|random_holy_site_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|holy_site|
|random_holy_site_in_religion|Iterate through all Holy Sites in a Religion|random_holy_site_in_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|holy_site|
|random_hostile_country|Iterate through all countries with relations marked as hostile|random_hostile_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_hostile_or_low_opinion_country|Iterate through all countries with relations marked as hostile or that we have a low opinion of set in defines|random_hostile_or_low_opinion_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_hostile_to_friendly_country|Iterate through all enemies of our friends|random_hostile_to_friendly_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_hostile_to_hostile_country|Iterate through all enemies of our enemies|random_hostile_to_hostile_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_import|Iterate through all imports in a market|random_import = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|market|trade|
|random_import_from_location|Iterate through all Imports from location|random_import_from_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|location|
|random_in_global_list|Iterate through all items in global list.|random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_in_list|Iterate through all items in list.|random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_in_local_list|Iterate through all items in local list.|random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_institutions_embraced|Iterate through all institutions a country has embraced|random_institutions_embraced = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|institution|
|random_international_organization|Iterate through all international organizations|random_international_organization = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|international_organization|
|random_international_organization_elector|Iterate through all countries with an elector special status in the international organization|random_international_organization_elector = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|country|
|random_international_organization_enemy|Iterate through all countries that are enemies of the international organization|random_international_organization_enemy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|country|
|random_international_organization_member|Iterate through all countries that are members of the international organization|random_international_organization_member = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|country|
|random_international_organization_owned_location|Iterate through all locations that are owned by the international organization|random_international_organization_owned_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|location|
|random_international_organization_owner|Iterate through all international organizations which own the location scope|random_international_organization_owner = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|international_organization|
|random_international_organization_parliament_opposers|Iterate through all countries that have voted AGAINST the parliament issue in the in the parliament of the international organization and support the current debate|random_international_organization_parliament_opposers = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|country|
|random_international_organization_parliament_supporter|Iterate through all countries that have voted FOR the parliament issue in the parliament of the international organization and support the current debate|random_international_organization_parliament_supporter = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|international_organization|country|
|random_international_organizations_member_of|Iterate through all international organizations a country is a member of|random_international_organizations_member_of = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|international_organization|
|random_international_organizations_target_of|Iterate through all international organizations a country is a target of|random_international_organizations_target_of = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|international_organization|
|random_invited_religious_figure|Iterate through all invited religious figures in a Country|random_invited_religious_figure = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|character|
|random_key_in_global_variable_map|Iterate through all items in global variable map.|random_key_in_global_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_key_in_local_variable_map|Iterate through all items in local variable map.|random_key_in_local_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_key_in_variable_map|Iterate through all items in variable map.|random_key_in_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_known_country|Iterate through all known countries|random_known_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_known_institution|Iterate through all institutions a country knows of|random_known_institution = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|institution|
|random_left_flank|Iterate through all subunits on the left-flank of a combat-side|random_left_flank = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|combat_side|sub_unit|
|random_lent_loan|Iterate through all loans that a country lent|random_lent_loan = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|loan|
|random_loan|Iterate through all loans in a country|random_loan = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|loan|
|random_loan_lent_to_country|Iterate through all loans a country has lent to the supplied borrower country|random_loan_lent_to_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|loan|
|random_location_in_area|Iterate through all Locations in a area|random_location_in_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area|location|
|random_location_in_continent|Iterate through all Locations in a continent|random_location_in_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|continent|location|
|random_location_in_market|Iterate through all locations in a market|random_location_in_market = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|market|location|
|random_location_in_province|Iterate through all Locations in a province|random_location_in_province = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|province|location|
|random_location_in_province_definition|Iterate through all Locations in a province definition|random_location_in_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|province_definition|location|
|random_location_in_region|Iterate through all Locations in a region|random_location_in_region = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|region|location|
|random_location_in_scripted_geography|Iterate through all Locations in a scripted geography|random_location_in_scripted_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|scripted_geography|location|
|random_location_in_sub_continent|Iterate through all Locations in a sub-continent|random_location_in_sub_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|sub_continent|location|
|random_location_in_the_world|Iterate through all location|random_location_in_the_world = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|location|
|random_location_with_movement|Iterate through all locations affected by the scope movement|random_location_with_movement = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|movement|location|
|random_location_with_town_rights_in_country|Iterate through all locations with Town Rights in a country|random_location_with_town_rights_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_loyal_subject|Iterate through all loyal subject countries|random_loyal_subject = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_maritime_area|Iterate through all maritime areas for a country|random_maritime_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|area|
|random_market_center_in_country|Iterate through all markets in a country which market centers are owned by the country|random_market_center_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|market|
|random_market_in_world|Iterate through all markets in the world|random_market_in_world = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|market|
|random_market_present_in_country|Iterate through all markets in a country|random_market_present_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|market|
|random_market_with_merchants|Iterate through all markets a country has active merchants|random_market_with_merchants = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|market|
|random_mercenary|Iterate through all mercenaries in the world|random_mercenary = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|mercenary|
|random_mercenary_sub_unit|Iterate through all subunits in a Mercenary|random_mercenary_sub_unit = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|mercenary|sub_unit|
|random_merchant_in_market|Iterate through all merchants in a market|random_merchant_in_market = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|market|country|
|random_movement|Iterate through all movements|random_movement = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|movement|
|random_movement_in_country|Iterate through all movements in a country|random_movement_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|movement|
|random_movement_in_culture|Iterate through all movements in a culture|random_movement_in_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|culture|movement|
|random_movement_in_religion|Iterate through all movements in a religion|random_movement_in_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|movement|
|random_navy|Iterate through all navies in a country|random_navy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|unit|
|random_neighbor_area|Iterate through all neighboring areas in a area|random_neighbor_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area|area|
|random_neighbor_country|Iterate through all neighbour countries|random_neighbor_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_neighbor_location|Iterate through all neighbors of a location|random_neighbor_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|location|
|random_neighbor_province_definition|Iterate through all neighboring ProvinceDefinitions in a ProvinceDefinition|random_neighbor_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|province_definition|province_definition|
|random_new_world_goods|Iterate through all new-world goods|random_new_world_goods = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|goods|
|random_nomad_countries_in_location|Iterate through all nomad pop countries in a location|random_nomad_countries_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|country|
|random_non_state_religion_location|Iterate through all NonStateReligion locations in a country|random_non_state_religion_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_old_world_goods|Iterate through all old-world goods|random_old_world_goods = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|goods|
|random_omen_in_country|Iterate through all Omens active in a country|random_omen_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|omen|
|random_omen_in_god|Iterate through all Omens associated with a God|random_omen_in_god = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|god|omen|
|random_omen_in_religion|Iterate through all Omens in a religion|random_omen_in_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|omen|
|random_other_core_country|Iterate through all other countries which have a core on the current country|random_other_core_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_other_country|Iterate through all other countries|random_other_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_other_great_power|Iterate through all other great powers|random_other_great_power = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_other_religion_in_same_group|Iterate through all other religions that has the same group as Religion|random_other_religion_in_same_group = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|religion|
|random_other_revolutionary|Iterate through all other revolutionary countries|random_other_revolutionary = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_overlord_or_above|Iterate through your overlord, your overlord's overlord, and so on|random_overlord_or_above = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_ownable_location|Iterate through all ownable location|random_ownable_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|location|
|random_ownable_location_in_area|Iterate through all ownable Locations in an area|random_ownable_location_in_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area|location|
|random_ownable_location_in_continent|Iterate through all ownable Locations in a continent|random_ownable_location_in_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|continent|location|
|random_ownable_location_in_province_definition|Iterate through all ownable Locations in a province definition|random_ownable_location_in_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|province_definition|location|
|random_ownable_location_in_region|Iterate through all ownable Locations in a region|random_ownable_location_in_region = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|region|location|
|random_ownable_location_in_scripted_geography|Iterate through all ownable Locations in a scripted geography|random_ownable_location_in_scripted_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|region|scripted_geography|
|random_ownable_location_in_sub_continent|Iterate through all ownable Locations in a sub continent|random_ownable_location_in_sub_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|sub_continent|location|
|random_owned_building|Iterate through all the owned buildings in a country|random_owned_building = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|building|
|random_owned_foreign_building|Iterate through all the owned foreign buildings in a country|random_owned_foreign_building = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|building|
|random_owned_foreign_building_location|Iterate through all the location of owned foreign buildings in a country|random_owned_foreign_building_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_owned_foreign_building_region|Iterate through all the regions of owned foreign buildings in a country|random_owned_foreign_building_region = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|region|
|random_owned_location|Iterate through all owned location in a country|random_owned_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_owned_nomad_pop|Iterate through all owned nomad pops in a country|random_owned_nomad_pop = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|pop|
|random_owned_non_rural_location|Iterate through all owned non-rural locations in a country|random_owned_non_rural_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_owned_rural_location|Iterate through all owned rural locations in a country|random_owned_rural_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_owner_in_region|Iterate through all the countries that own locations in a region|random_owner_in_region = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|region|country|
|random_parent|Iterate through parents (order: father, mother) of a character.|random_parent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|character|
|random_participating_countries|Iterate through all Countrys participating in 1 side of a combat|random_participating_countries = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|combat_side|country|
|random_participating_units|Iterate through all units participating in 1 side of a combat|random_participating_units = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|combat_side|unit|
|random_past_liturgical_dialect|Iterate through all liturgical dialects a country has had before|random_past_liturgical_dialect = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_policy_in_law|Iterate through all policies that are part of the law scope|random_policy_in_law = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|law|policy|
|random_political_border_location|Iterate through all owned location in a country which border another country.|random_political_border_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_pop|Iterate through all pops in a location or country|random_pop = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country, location|pop|
|random_pops_supporting_rebel|Iterate through all pops supporting a rebel|random_pops_supporting_rebel = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|rebels|pop|
|random_port_in_country|Iterate through all Ports in a country|random_port_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_possible_disaster|Iterate through all possible disasters for a country|random_possible_disaster = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|disaster|
|random_possible_parliament_issue|Iterate through all possible parliament issues in a country's or an international organization's parliament|random_possible_parliament_issue = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country, international_organization|parliament_issue|
|random_possible_policy|Iterate through all possible policies of a Country that is not currently implemeted|random_possible_policy = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|policy|
|random_possible_privilege|Iterate through all possible & allowed estate privileges of a Country that is not currently implemeted|random_possible_privilege = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|estate|estate_privilege|
|random_possible_recruit_location|Iterate through all possible recruit locations in a country|random_possible_recruit_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_present_country|Iterate through all countries in the specified geography|random_present_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|random_present_culture_in_country|Iterate through all cultures present in the country.|random_present_culture_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|culture|
|random_present_culture_in_location|Iterate through all cultures present in the location.|random_present_culture_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|culture|
|random_present_overlord|Iterate through all countries which have a subject in the specified geography|random_present_overlord = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area, continent, location, province_definition, region, scripted_geography, sub_continent|country|
|random_present_religion_in_country|Iterate through all religions present in the country.|random_present_religion_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|religion|
|random_present_religion_in_location|Iterate through all religions present in the location.|random_present_religion_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|religion|
|random_primary_or_accepted_culture|Iterate through primary culture and all accepted cultures in a country. Primary is random first.|random_primary_or_accepted_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|culture|
|random_primary_or_accepted_or_tolerated_culture|Iterate through primary culture and all accepted and all tolerated cultures in a country. Primary is random first.|random_primary_or_accepted_or_tolerated_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|culture|
|random_privateer|Iterate through all privateers in the world|random_privateer = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|privateer|
|random_privateer_from_country|Iterate through all privateers a country has|random_privateer_from_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|privateer|
|random_privateer_in_area|Iterate through all privateers in a area|random_privateer_in_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area|privateer|
|random_production_method|Iterate through all types of production methods.|random_production_method = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|production_method|
|random_production_method_of_building|Iterate through all available production methods of the building.|random_production_method_of_building = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|building|production_method|
|random_province|Iterate through all provinces in a country|random_province = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|province|
|random_province_definition|Iterate through all existing province_definition|random_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|province_definition|
|random_province_definition_in_area|Iterate through all province-definitions in an area|random_province_definition_in_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area|province_definition|
|random_province_definition_in_scripted_geography|Iterate through all provinces in a scripted geography|random_province_definition_in_scripted_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|scripted_geography|province|
|random_province_in_area|Iterate through all provinces in an area|random_province_in_area = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|area|province|
|random_province_in_province_definition|Iterate through all provinces in a province-definition|random_province_in_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|province_definition|province|
|random_rebel|Iterate through all Rebels in a country|random_rebel = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|rebels|
|random_region|Iterate through all existing regions|random_region = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|region|
|random_region_in_continent|Iterate through all regions in a sub-continent|random_region_in_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|sub_continent|region|
|random_region_in_scripted_geography|Iterate through all regions in a scripted geography|random_region_in_scripted_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|scripted_geography|region|
|random_related_country|Iterate through all related countries|random_related_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_religion|Iterate through all religions|random_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|religion|
|random_religion_for_god|Iterate through all Religions of a God|random_religion_for_god = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|god|religion|
|random_religion_in_religion_group|Iterate through all religions in a religion group.|random_religion_in_religion_group = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|group|religion|
|random_religion_international_organization|Iterate through all international organisations of a religion|random_religion_international_organization = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|international_organization|
|random_religious_aspect|Iterate through all religious aspects of a Country|random_religious_aspect = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|religious_aspect|
|random_religious_focus|Iterate through all completed religious focuses of a Country|random_religious_focus = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|religious_focus|
|random_religious_school_in_religion|Iterate through all Religious Schools in a Religion|random_religious_school_in_religion = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religion|religious_school|
|random_rented_out_mercenary|Iterate through mercenaries a country has rented out to the market|random_rented_out_mercenary = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|mercenary|
|random_required_goods|Iterate through all goods required by the scope production method.|random_required_goods = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|production_method|goods|
|random_reserves|Iterate through all subunits on the reserve of a combat-side|random_reserves = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|combat_side|sub_unit|
|random_retreated|Iterate through all subunits on the retreated of a combat-side|random_retreated = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|combat_side|sub_unit|
|random_revolutionary|Iterate through all revolutionary states|random_revolutionary = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|country|
|random_right_flank|Iterate through all subunits on the right-flank of a combat-side|random_right_flank = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|combat_side|sub_unit|
|random_rival|Iterate through all rival countries|random_rival = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_road_type|Iterate through all the road types|random_road_type = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|road_type|
|random_royal_marriage|Iterate through all royal married countries|random_royal_marriage = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_ruled_international_organization|Iterate through IOs a character rules|random_ruled_international_organization = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|international_organization|
|random_ruler|Iterate through all characters that have ever been rulers in a country, including the dead|random_ruler = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|character|
|random_ruling_countries|Iterate through countries a character rulers|random_ruling_countries = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|country|
|random_sound_toll_in_country|Iterate through all Sound Tolls in a country|random_sound_toll_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|location|
|random_spouse|Iterate through all spouses of a character|random_spouse = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|character|
|random_spy_network_built_in_us|Iterate through all countries building spy networks|random_spy_network_built_in_us = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_sub_continent|Iterate through all existing sub_continents|random_sub_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|sub_continent|
|random_sub_continent_in_continent|Iterate through all sub-continents in a continent|random_sub_continent_in_continent = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|continent|sub_continent|
|random_sub_continent_in_scripted_geography|Iterate through all sub-continents in a scripted geography|random_sub_continent_in_scripted_geography = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|continent|scripted_geography|
|random_sub_unit|Iterate through all subunits in a unit|random_sub_unit = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|unit|sub_unit|
|random_subject|Iterate through all subject countries|random_subject = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_subject_or_below|Iterate through all subject countries and their subject countries, and so on|random_subject_or_below = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_tolerated_culture|Iterate through all Tolerated cultures in a country|random_tolerated_culture = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|culture|
|random_town_rights_in_country|Iterate through all Town Rights in a country|random_town_rights_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|town_rights|
|random_town_rights_in_location|Iterate through all Town Rights in a location|random_town_rights_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|town_rights|
|random_trade|Iterate through all trades in a Country|random_trade = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|trade|
|random_trait|Iterate through all traits of a character|random_trait = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|trait|
|random_union_partner|Iterate through all countries which are in a personal union with the current country scope.|random_union_partner = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|country|
|random_unit|Iterate through all units in a country|random_unit = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|unit|
|random_unit_in_location|Iterate through all units in a location|random_unit_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|unit|
|random_valid_religion_for_aspect|Iterate through all religion that an aspect can be for|random_valid_religion_for_aspect = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|religious_aspect|religion|
|random_voter|Iterate through all voters in an active resolution|random_voter = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|active_resolution|country|
|random_war|Iterate through all wars going on globally|random_war = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|war|
|random_war_participant|Iterate through all participants of a war|random_war_participant = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|war|country|
|random_weather_system_in_location|Iterate through all weather systems in a location|random_weather_system_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|weather_system|
|random_west_of_province_definition|Iterate through all province-definitions west of a province-definition|random_west_of_province_definition = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|province_definition|province_definition|
|random_work_of_art|Iterate through all WorkOfArts in the world|random_work_of_art = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|none|work_of_art|
|random_work_of_art_by_creator|Iterate through all work_of_art by a particular artist|random_work_of_art_by_creator = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|character|work_of_art|
|random_work_of_art_in_country|Iterate through all work_of_art in a country|random_work_of_art_in_country = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|work_of_art|
|random_work_of_art_in_location|Iterate through all work_of_art in a location|random_work_of_art_in_location = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|location|work_of_art|

Effect iterators begin with `every_`, `ordered_`, and `random_`. `every_` iterators apply their effects to all returned scopes, `ordered_` iterators order their returned scopes by a value comparison and apply their effects to the first in the ordering, and `random_` iterators apply their effects to a single random returned scope.

All three can use the parameter `limit` to apply triggers that limit which scopes are returned. If the limit triggers are specific enough, such that they return only a single scope, all three types of iterator are effectively identical.

`ordered_` iterators can return a scope besides the first by using the parameter `position = int` which is 0-indexed. Additionally, the parameters `min = int` and `max = value` can be used to limit how many and which scopes are returned in the ordering. `min` sets the "top" position, using the same 0-indexing as `position`, while `max` determines the number of scopes to return, from the floored value given. If not specified, `min = 0` and `max = 1`. Setting `min` without setting `max` considers `max` as equal to the iterator's list size. Use `check_range_bounds = no` to prevent error logging when using min or max, otherwise using a min or max higher than the list size gives and error.

`random_` iterators can weight the returned scopes so that certain scopes are more likely to be selected. This uses `weight = { <mtth blocks> }`. Without a modified weighting, all returned scopes are equally weighted.

#### Multiple random scopes

Often it is useful to return multiple random or semi-random scopes. This can be implemented in a few different ways. The most straightforward is multiple uses of a `random_` iterator. To ensure that the same scope is not returned twice, set a variable on each scope as part of its effects and check that the variable has not been set in order to return the next scope.

```
random_country = {
    limit = {
        NOT = { has_variable = blocker_var }
        <other limit triggers>
    }
    set_variable = blocker_var
    <effects>
}
<repeat above as desired>
```

This style can be made more succinct by using a scripted effect or a while loop, so that the actual effect only needs to be defined once.

An alternative approach uses a single `ordered_` iterator with a semi-random ordering. This ensures each returned scope is unique without having to check for variables, as well as keeping the amount of script used to a minimum. It makes use of the script value function `modulo` to give a semi-random ordering.

```
ordered_country = {
    limit = { } # if desired
    order_by = {
        value = total_population
        modulo = { 1 10 }
    }
    max = 10
    <effects>
}
```

This example returns 10 countries which are ordered by a randomized modulo of total population. The `modulo` range can be set to any values desired and can also used `fixed_range` or `integer_range` in order to make use of other scripted values, and other values can be used as the basis, such as gold, prestige, or any reasonably unique value set.

## Event targets

|Scope link|Description|From scope|To scope|
|---|---|---|---|
|active_mission|Unknown, add something in code registration|country|mission|
|advance_age|Unknown, add something in code registration|advance_type|age|
|attacker_leader|Unknown, add something in code registration|war|country|
|autocephalous_patriarchate|Unknown, add something in code registration|country|international_organization|
|birth_location|Unknown, add something in code registration|character|location|
|borrower|Unknown, add something in code registration|loan|country|
|building_base_cost_in_gold|The Building base price in gold|building_type|value|
|cabinet_member|Unknown, add something in code registration|cabinet|character|
|capacity_market|Unknown, add something in code registration|trade|market|
|capital|Unknown, add something in code registration|area, country, dynasty, province|location|
|cardinal|Unknown, add something in code registration|location|cardinal|
|civil_war|Unknown, add something in code registration|country|war|
|civil_war_opponent|Unknown, add something in code registration|country|country|
|combat|Unknown, add something in code registration|combat_side, location, unit|combat|
|combat_attacker|Unknown, add something in code registration|combat|combat_side|
|combat_defender|Unknown, add something in code registration|combat|combat_side|
|commander|Unknown, add something in code registration|combat_side|country|
|commanding_country|Unknown, add something in code registration|combat_side|country|
|compare_date|A comparison trigger that will return its date in the context it is used eg: root.gold|none|date|
|compare_value|A comparison trigger that will return its value in the context it is used eg: root.gold|none|value|
|consort|Unknown, add something in code registration|country|character|
|controller|Unknown, add something in code registration|location, sub_unit|country|
|country_color|Unknown, add something in code registration|country|color|
|country_stance|Unknown, add something in code registration|country|military_stance|
|court_dialect|Unknown, add something in code registration|country|dialect|
|court_language|Unknown, add something in code registration|country|language|
|creator|Unknown, add something in code registration|work_of_art|character|
|current_mission_task|Unknown, add something in code registration|country|mission_task|
|customer|Unknown, add something in code registration|mercenary|country|
|defender_leader|Unknown, add something in code registration|war|country|
|dominant_country|Unknown, add something in code registration|culture|country|
|dominant_culture|Unknown, add something in code registration|country, location, province|culture|
|dominant_dialect|Unknown, add something in code registration|country, location|dialect|
|dominant_language|Unknown, add something in code registration|country, location|language|
|dominant_religion|Unknown, add something in code registration|country, location, province|religion|
|dominant_upper_class_culture|Unknown, add something in code registration|country|culture|
|dynasty_head|Unknown, add something in code registration|dynasty|character|
|dynasty_home|Unknown, add something in code registration|dynasty|location|
|employer|Employer of the character|character|country|
|enemy_side|Unknown, add something in code registration|combat_side|combat_side|
|exploration|Unknown, add something in code registration|character|exploration|
|father|Unknown, add something in code registration|character|character|
|first_spouse|Unknown, add something in code registration|character|character|
|from_market|Unknown, add something in code registration|trade|market|
|group|Unknown, add something in code registration|religion|group|
|heir|Unknown, add something in code registration|country|character|
|holy_site|Unknown, add something in code registration|avatar, god|holy_site|
|international_organization_target|Unknown, add something in code registration|international_organization|country|
|largest_army|The largest army controlled by the country|country|unit|
|largest_navy|The largest navy controlled by the country|country|unit|
|last_dynasty_in_location|Unknown, add something in code registration|location|dynasty|
|last_leader_country|Unknown, add something in code registration|international_organization|country|
|last_valid_ruler|Unknown, add something in code registration|country|character|
|leader|Unknown, add something in code registration|exploration, unit|character|
|leader_country|Unknown, add something in code registration|international_organization|country|
|leadership_election_resolution|Unknown, add something in code registration|international_organization|resolution|
|leading_unit|Unknown, add something in code registration|combat_side|unit|
|linked_pop|Unknown, add something in code registration|building|pop|
|liturgical_dialect|Unknown, add something in code registration|country|dialect|
|liturgical_language|Unknown, add something in code registration|country|language|
|low_control_best_tax_base|get the best low control tax base|country|province|
|market|Unknown, add something in code registration|location|market|
|marriage_union|Unknown, add something in code registration|country|international_organization|
|max_great_powers|Unknown, add something in code registration|none|value|
|mercenary_home|Unknown, add something in code registration|mercenary|location|
|most_powerful_merchant|Unknown, add something in code registration|market|country|
|mother|Unknown, add something in code registration|character|character|
|movement_type|Unknown, add something in code registration|movement|movement_definition|
|name_culture|Unknown, add something in code registration|sub_unit|culture|
|named_script_value|A script value that will calculate and returns its value in the context it is used|none|color, value|
|origin|Unknown, add something in code registration|disease, disease_outbreak, institution, work_of_art|location|
|original_attacker_leader|Unknown, add something in code registration|war|country|
|original_capital|Unknown, add something in code registration|country|location|
|original_defender_leader|Returns the country which was the original defender. In cases where the war is started against a subject country, defender_leader would return the overlord while original_defender_leader would return the subject country. Returns the current defender war leader as fallback.|war|country|
|original_outbreak|Unknown, add something in code registration|disease|disease_outbreak|
|overlord|Unknown, add something in code registration|country|country|
|owner|Unknown, add something in code registration|building, cabinet, cardinal, character, colonial_charter, disaster, estate, exploration, loan, location, market, mercenary, pop, privateer, province, rebels, sub_unit, trade, unit, work_of_art|country|
|owning_unit|Unknown, add something in code registration|sub_unit|unit|
|parliament_seat|Unknown, add something in code registration|country, international_organization|location|
|prev|The previous scope|none|varies|
|previous_owner|Unknown, add something in code registration|location|country|
|previous_ruler|Unknown, add something in code registration|country|character|
|produced_goods|Unknown, add something in code registration|production_method|goods|
|province_capital|Unknown, add something in code registration|province|location|
|raw_material|Unknown, add something in code registration|location|goods|
|raw_material_location|Unknown, add something in code registration|location|goods|
|rebel|Unknown, add something in code registration|character, pop|rebels|
|regent|Unknown, add something in code registration|country|character|
|religious_head|Unknown, add something in code registration|religion|country|
|resolution_proposer|Unknown, add something in code registration|active_resolution|country|
|revolutionary_target|Unknown, add something in code registration|none|country|
|root|The head of the current top scope eg: reciever of an event, taker of a decision|none|varies|
|ruler|Unknown, add something in code registration|country|character|
|ruler_or_heir_if_regent|Unknown, add something in code registration|country|character|
|ruler_or_regent|Unknown, add something in code registration|country|character|
|sea_zone|Unknown, add something in code registration|location|location|
|second_best_market|Unknown, add something in code registration|location|market|
|secondary_culture|Unknown, add something in code registration|location|culture|
|secondary_otherwise_primary_culture|Unknown, add something in code registration|location|culture|
|siege|Unknown, add something in code registration|location, unit|siege|
|siege_defender|the siege defender country|siege|country|
|siege_main_attacker|the siege main attacker country|siege|country|
|subunit_home|Unknown, add something in code registration|sub_unit|location|
|succession_law|Unknown, add something in code registration|country|heir_selection|
|this|The current scope|none|varies|
|to_market|Unknown, add something in code registration|trade|market|
|top_overlord|Unknown, add something in code registration|country|country|
|top_overlord_or_this|Unknown, add something in code registration|country|country|
|top_owner|Unknown, add something in code registration|location|country|
|traded_goods|Unknown, add something in code registration|trade|goods|
|union|Unknown, add something in code registration|country|international_organization|
|unit|Unknown, add something in code registration|character|unit|
|unit_destination|Unknown, add something in code registration|unit|location|
|unit_location|Unknown, add something in code registration|unit|location|
|unit_next_location|Unknown, add something in code registration|unit|location|
|upgrade_demand|Unknown, add something in code registration|production_method|demand|
|war_goal_province|Links to the war goal of the war. If no war goal is set or is unrelated to locations (such as superiority) the link returns the capital of the defender war leader|war|province|

|Scope link|Description|From scope|To scope|
|---|---|---|---|
|active_outbreak|gets the active outbreak for a disease in a location or subunit - usage active_outbreak(<disease>)|location, sub_unit|disease_outbreak|
|active_resolution|gets the active resolution of the type specified in the scope international organization or situation - usage active_resolution(<resolution>)|international_organization, situation|active_resolution|
|advance_type|Unknown, add something in code registration|none|advance_type|
|age|Unknown, add something in code registration|none|age|
|ai_personality|Unknown, add something in code registration|country, none|ai_personality|
|area|Unknown, add something in code registration|exploration, location, none, privateer, province, province_definition|area|
|area_exploration|Links to an exploration in the scope area for the suppled country. Usage: area_exploration:<country> or area_exploration(<country>)|area|exploration|
|array_define|Name\|Index. Index is 0-based.|none|value|
|artist_type|Unknown, add something in code registration|none|artist_type|
|avatar|Unknown, add something in code registration|holy_site, none|avatar|
|bias_value|Unknown, add something in code registration|none|value|
|building|Unknown, add something in code registration|location|building|
|building_type|Unknown, add something in code registration|building, none|building_type|
|bureaucracy_type|Unknown, add something in code registration|bureaucracy, none|bureaucracy_type|
|c|Scope to the specified country TAG|none|country|
|cabinet_action|The cabinet action a character is performing|cabinet, character, none|cabinet_action|
|cast_vote_in_active_resolution|gets the cast vote in a resolution, returns nothing if the vote isn't explicit - usage cast_vote_in_resolution(<country>)|active_resolution|vote|
|casus_belli|Unknown, add something in code registration|none, war|casus_belli|
|character|Unknown, add something in code registration|none|character|
|character_interaction|Unknown, add something in code registration|none|character_interaction|
|child_education|Unknown, add something in code registration|none|child_education|
|climate|Unknown, add something in code registration|none|climate|
|compare_complex_value|A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies)|none|value|
|continent|Unknown, add something in code registration|area, location, none, province, province_definition, region, sub_continent|continent|
|country_government_reform_fully_implemented_date|Unknown, add something in code registration|country|date|
|country_government_reform_implementation_date|Unknown, add something in code registration|country|date|
|country_interaction|Unknown, add something in code registration|none|country_interaction|
|country_rank|Unknown, add something in code registration|country, none|country_rank|
|country_rank_on_date|Unknown, add something in code registration|country|country_rank|
|culture|Unknown, add something in code registration|character, country, dynasty, mercenary, none, pop, rebels, sub_unit|culture|
|culture_group|Unknown, add something in code registration|none|culture_group|
|default_price|The default price for a goods|none|value|
|define|Name|none|color, date, value|
|demand|Unknown, add something in code registration|none|demand|
|dialect|Unknown, add something in code registration|character, culture, dynasty, market, none, pop, religion|dialect|
|disaster_type|Unknown, add something in code registration|disaster, none|disaster_type|
|disease|Unknown, add something in code registration|disease_outbreak, none|disease|
|dynasty|Unknown, add something in code registration|character, none|dynasty|
|employment_system|Unknown, add something in code registration|none|employment_system|
|estate|Links to a particular estate. Usage: estate:<estate_type_link> or estate(<estate_type_link>)|country|estate|
|estate_power|The power of an estate|country|value|
|estate_privilege|Unknown, add something in code registration|none|estate_privilege|
|estate_satisfaction|The satisfaction of an estate|country|value|
|estate_target_satisfaction|The target satisfaction of an estate|country|value|
|estate_tax_base|The base tax of an estate|country, estate|value|
|estate_tax_percentage|The tax percentage levied on an estate|country|value|
|estate_type|Unknown, add something in code registration|building, character, estate, estate_privilege, none, parliament_issue, pop, rebels|estate_type|
|ethnicity|Unknown, add something in code registration|character, none|ethnicity|
|flag|Flag literals eg: flag:the_boss|none|flag|
|formable_country|Unknown, add something in code registration|none|formable_country|
|generic_action|Unknown, add something in code registration|none|generic_action|
|gfx_culture|The graphical culture from a culture scope|culture, none|graphical_culture|
|global_var|Reference a previous set global variable via its name eg: global_var:important_thing|none|varies|
|global_variable_map|c:FRA)"|none|varies|
|god|Unknown, add something in code registration|avatar, holy_site, none, omen|god|
|goods|Unknown, add something in code registration|none|goods|
|government_reform|Unknown, add something in code registration|none|government_reform|
|government_type|Unknown, add something in code registration|country, none|government|
|hegemony|Unknown, add something in code registration|none|hegemony|
|heir_selection|Unknown, add something in code registration|none|heir_selection|
|holy_site_definition|Unknown, add something in code registration|none|holy_site_definition|
|holy_site_type|Unknown, add something in code registration|none|holy_site_type|
|implementation_price|Unknown, add something in code registration|bureaucracy, bureaucracy_type|price|
|institution|Unknown, add something in code registration|none|institution|
|institution_progress|The progress towards an institution of a location|location|value|
|interaction_target|Unknown, add something in code registration|cabinet|varies|
|international_organization|Unknown, add something in code registration|none|international_organization|
|international_organization_type|Unknown, add something in code registration|international_organization, none|international_organization_type|
|known_in_country|The amount of goods known to a speficic Country|country|value|
|land_ownership_rule|Unknown, add something in code registration|international_organization, none|land_ownership_rule|
|language|Unknown, add something in code registration|character, country, culture, dialect, dynasty, market, none, religion, sub_unit|language|
|language_family|Unknown, add something in code registration|language, none|language_family|
|law|Unknown, add something in code registration|none, policy|law|
|law_policy|gets the policy chosen for a particular law in the scope international organization or country - usage law_policy(<law>)|country, international_organization|policy|
|leader_at_index|Scopes to the leader characters of the IO which are defined in leader = {}. In case of countries instead, their ruler, heir or regent (in that order) gets returned instead. Usage: leader_at_index(<int>|international_organization|character|
|levy_setup|Unknown, add something in code registration|none|levy_setup|
|local_var|Reference a previous set local variable via its name eg: local_var:person_of_interest|none|varies|
|local_variable_map|c:FRA)"|none|varies|
|location|Unknown, add something in code registration|building, cardinal, character, combat, exploration, holy_site, market, none, pop, siege, town_rights, work_of_art|location|
|location_rank|Unknown, add something in code registration|location, none|location_rank|
|market_price|The price a goods has in a market|market|value|
|mission|Unknown, add something in code registration|none|mission|
|mission_task|Unknown, add something in code registration|none|mission_task|
|modifier|Scope to the value of the modifier type of specified key belonging to the current object|character, country, dynasty, international_organization, location, province, religion, unit|boolean, value|
|movement_definition|Unknown, add something in code registration|none|movement_definition|
|num_estate_privileges|The amount of privileges an estate has|country|value|
|num_location_rank|Count the amount of owned locations of a specific rank|country|value|
|num_pop_type|The amount of pops of a specific type at location|location|value|
|num_pop_type_in_country|The amount of pops of a specific type in a country|country|value|
|num_pop_type_in_province|The amount of pops of a specific type at Province|province|value|
|num_possible_estate_privileges|The amount of possible privileges an estate can get|country|value|
|omen|Unknown, add something in code registration|none|omen|
|parliament_agenda|Unknown, add something in code registration|none|parliament_agenda|
|parliament_issue|Unknown, add something in code registration|country, international_organization, none|parliament_issue|
|parliament_type|Unknown, add something in code registration|country, international_organization, none|parliament_type|
|payment|Unknown, add something in code registration|none|payment|
|peace_treaty|Unknown, add something in code registration|none|peace_treaty|
|percentage_pop_type_in_country|The percentage of pops of a specific type in a country|country|value|
|percentage_pop_type_in_location|The percentage of pops of a specific type in a location|location|value|
|policy|Unknown, add something in code registration|none|policy|
|pop_type|Unknown, add something in code registration|none, pop|pop_type|
|price|Unknown, add something in code registration|none, policy|price|
|produced_in_country|The amount of goods produced in a specific Country|country|value|
|produced_in_market|The amount of goods produced in a speficic market|market|value|
|produced_in_world|The amount of goods produced in the world|none|value|
|production_method|Unknown, add something in code registration|none|production_method|
|province|Unknown, add something in code registration|country, location|province|
|province_definition|Unknown, add something in code registration|colonial_charter, location, none, province|province_definition|
|recruitment_method|Unknown, add something in code registration|none|recruitment_method|
|regency_type|Unknown, add something in code registration|country, none|regency_type|
|region|Unknown, add something in code registration|area, location, none, province, province_definition|region|
|relation_type|Unknown, add something in code registration|none|relation_type|
|religion|Unknown, add something in code registration|character, country, dynasty, mercenary, none, pop, rebels, sub_unit|religion|
|religion_group|Unknown, add something in code registration|none|group|
|religious_aspect|Unknown, add something in code registration|none|religious_aspect|
|religious_faction|Unknown, add something in code registration|none|religious_faction|
|religious_figure|Unknown, add something in code registration|none|religious_figure|
|religious_focus|Unknown, add something in code registration|none|religious_focus|
|religious_school|Unknown, add something in code registration|character, country, none|religious_school|
|removal_price|Unknown, add something in code registration|bureaucracy, bureaucracy_type|price|
|resolution|Unknown, add something in code registration|active_resolution, none|resolution|
|resolution_target|Links to the named parameter (from the select_triggers) in the scope active resolution|active_resolution|varies|
|resolution_vote|<international organization>\|<resolution>)|none|vote|
|road_type|Unknown, add something in code registration|none|road_type|
|rule_end_date|Unknown, add something in code registration|character|date|
|scope|Reference a previously saved scope via its name eg: scope:target|none|varies|
|scriptable_hint_definition|Unknown, add something in code registration|none|scriptable_hint_definition|
|scripted_geography|Unknown, add something in code registration|none|scripted_geography|
|situation|Unknown, add something in code registration|none|situation|
|societal_value|The value of a societal value of a country|country|value|
|societal_value_type|Unknown, add something in code registration|none|societal_value_type|
|special_status|Unknown, add something in code registration|none, parliament_issue|special_status|
|stockpile_in_market|The amount of goods stockpiled in a specific market|market|value|
|sub_continent|Unknown, add something in code registration|area, location, none, province, province_definition, region|sub_continent|
|sub_unit_category|Unknown, add something in code registration|none, sub_unit|sub_unit_category|
|sub_unit_count|Checks the amount of a subunit-type inside a unit (in regiments)|unit|value|
|sub_unit_fraction|Checks the fraction of a subunit-type inside a unit (in regiments)|unit|value|
|sub_unit_strength|Checks the strength of a subunit-type inside a unit (in regiments)|unit|value|
|subject_military_stance|Unknown, add something in code registration|none|military_stance|
|subject_type|Unknown, add something in code registration|country, none|subject_type|
|target_price|The target price a goods has in a market|market|value|
|topography|Unknown, add something in code registration|none|topography|
|total_building_levels_including_construction|The amount of total building levels including construction in a speficic Country|country|value|
|total_effective_building_levels|The amount of total effective building levels in a speficic Country|country|value|
|total_sub_unit_category_in_unit|Checks the total strength of a subunit-category for a unit|unit|value|
|total_sub_unit_count|Checks the amount of a subunit-category that a country has (in regiments/ships)|country|value|
|total_sub_unit_strength|Checks the total strength of a subunit-category for a unit|country|value|
|total_sub_unit_type_count|Checks the amount of a subunit-type that a country has (in regiments/ships)|country|value|
|total_sub_unit_type_strength|Checks the total strength of a subunit-type for a country|unit|value|
|town_rights_type|Unknown, add something in code registration|none, town_rights|town_rights_type|
|traded_in_market|The amount of goods traded in a specific market|market|value|
|trait|Unknown, add something in code registration|none|trait|
|unit_ability|Unknown, add something in code registration|none|unit_ability|
|unit_formation_preference|Unknown, add something in code registration|none|unit_formation_preference|
|unit_type|Unknown, add something in code registration|none|unit_type|
|var|Reference a previous set variable via its name eg: var:mortal_enemy|none|varies|
|variable_map|c:FRA)"|none|varies|
|vegetation|Unknown, add something in code registration|none|vegetation|
|vote_in_active_resolution|gets the active resolution of the type specified in the scope active resolution - usage vote_in_active_resolution(<country>)|active_resolution|vote|
|war_with_country|Gets the current war of the country scope against the specified target country - usage war_with_country(<country>)|country|war|
|work_of_art|Unknown, add something in code registration|none|work_of_art|
|work_of_art_type|Unknown, add something in code registration|none, work_of_art|work_of_art_type|

**Event targets** are scope identifiers that return a specific scope from context or specification. Event targets can be used to set the scope or as the target of an effect or trigger. When setting the scope, event targets can be used either for triggers or for effects, unlike iterators which are specified only for triggers or effects, but not both.

Scope event targets come in two types, contextual or specified. Contextual event targets almost always must be used in a relevant scope, as they refer to scopes relevant to the current scope, such as the capital state or ruler of a country. Specified event targets are often scopeless as they refer to a specific object. Some specified event targets still require a certain scope as they refer to an instance of a type, rather than a unique object.

Specified scope event targets typically use a colon `:` followed by a script key, such as a building type, country tag, or area. Some use parentheses instead.

### Scope stacking

Scope stacking, also known as dot chaining, is a method of quickly going from one scope to another without having to insert multiple event target blocks. This allows for quickly changing through scopes without having to create a new block for each scope level. They follow the format of `<preceding event_target>.<next_event_target>`.

While scope stacking seems to produce a technically equivalent result, there is one caveat - the previous scope (`PREV`) is set to the scope before the chain.
For example, to check if any country has a capital in a certain region, either of the following methods return the same result,

Without scope stacking

```
any_country = {
    capital = {
        region = region:<region_name>
    }
}
```

With scope stacking

```
any_country = {
    capital.region = region:<region_name>
}
```

Here is an example showcasing how `PREV` works:
Without scope stacking

```
any_country = {
	ruler = {
		birth_location = {
			owner = PREV		#PREV is ruler here. The ruler will not own the location!
		}
	}
}
```

With scope stacking

```
any_country = {
	ruler.birth_location = {
		owner = PREV			#PREV is country here. The country may own the location!
	}
}
```

### Scope existence checks and ?= operator

Trying to fire effects or check triggers on scopes that do not exist will lead to results and unintended behavior, so it is critical to have certainty that the object behind the scope exists.
This can be done using some regular triggers like has_capital, or, more generally, **exists**.

The `?=` existence operator can be combined with Event targets to ease this process.

In triggers, `?=` means that the scope must exist and must fulfill the requirements:

```
scope:target ?= {
	gold >= 100
}
```

is equivalent to:

```
AND = {
	exists = scope:target
	scope:target = {
		gold >= 100
	}
}
```

It must be specified that in comparison contexts, `?=` only checks for the left-hand side:

```
ruler ?= scope:target
```

If ruler does not exist, the block will evaluate to false, if scope:target does not exist, an error will be printed and the check might have unexpected behavior.
Alternative ways to do the two-sided existance check:

```
ruler ?= {
	scope:target ?= this
}

AND = {
	exists = scope:target
	ruler ?= scope:target
}
```

In effects, `?=` evaluates to a check that makes the effects inside fire only if the scope exists.

```
scope:target ?= {
	add_gold = 100
}
```

is equivalent to:

```
if = {
	limit = {
		exists = scope:target
	}
	scope:target = {
		add_gold = 100
	}
}
```

### Value triggers

Some triggers can be used in value comparison triggers - those triggers can also be used as scope links that return `value` scope and can therefore be used at the end of scope stacking. 

Such triggers will usually have the following line in their documentation: 

`Traits: <, <=, =, !=, >, >=`

## Common scope examples

WIP

## Scope types

Here are all recognizable scope types in the game. Effects, triggers, and scope links listed on this wiki note which scopes they can be used in.

- active_resolution
- advance_type
- age
- any/none
- area
- artist_type
- audio_culture
- avatar
- bool
- building
- building_type
- cabinet
- cabinet_action
- cardinal
- casus_belli
- character
- character_interaction
- child_education
- climate
- colonial_charter
- color
- combat
- combat_side
- continent
- country
- country_interaction
- country_rank
- culture
- culture_group
- date
- dialect
- disaster
- disaster_type
- disease
- disease_outbreak
- dynasty
- employment_system
- estate
- estate_privilege
- estate_type
- ethnicity
- exploration
- formable_country
- generic_action
- god
- goods
- goods_demand
- government_reform
- government_type
- graphical_culture
- hegemony
- heir_selection
- holy_site
- holy_site_definition
- holy_site_type
- institution
- integer_flag
- international_organization
- international_organization_type
- land_ownerhip_rule
- language
- language_family
- law
- levy_setup
- loan
- location
- location_rank
- market
- mercenary
- military_stance
- mission
- mission_task
- parliament_agenda
- parliament_issue
- parliament_type
- payment
- peace_treaty
- policy
- pop
- pop_type
- price
- privateer
- production_method
- province
- province_definition
- rebel
- recruitment_method
- regency_type
- region
- relation_type
- religion
- religion_group
- religious_aspect
- religious_faction
- religious_figure
- religious_focus
- religious_school
- resolution
- road_type
- scriptable_hint_definition
- siege
- situation
- societal_value_type
- special_status
- sub_continent
- sub_unit_category
- subject_type
- subunit
- topography
- trade
- trait
- unit
- unit_ability
- unit_type
- value
- vegetation
- war
- weather_system
- work_of_art
- work_of_art_type

### Scopes with variables

Some game objects can hold variables and variable lists on them. Here is the list of such scopes:

- cabinet
- character
- colonial_charter
- country
- culture
- disaster
- dynasty
- international_organization
- location
- province
- rebel
- religion
- active_situation
- unit
- war

## References


