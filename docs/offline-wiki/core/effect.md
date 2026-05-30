# Effect

**Source:** https://eu5.paradoxwikis.com/Effect

---

Effects change the current game state – such as creating or killing a character, changing the ownership of a state, and much else.

Effects come in two basic types, inline and block. Inline effects take a simple target, such as a scope, script value, or defined type. Block effects are more complex and often take multiple targets, such as a scope and script value.

All effects require a certain scope. Some effects can be used in any scope (noted as "none" in the follow tables), others only function when in the correct scope. Some effects change the current scope.

The tables below are generated from the script documentation (*script_docs* console command).

## Iterator effects

Iterators examine all relevant scopes and output one or more.

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

## Flow effects

Flow effects control how other effects are used. This includes conditionals and loops as well as tooltips. They can always be used in any scope

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|else|Executes enclosed effects if limit criteria of preceding 'if' or 'else_if' is not met|if = { limit = { <triggers> } <effects> } else = { <effects> }|none||
|else_if|Executes enclosed effects if limit criteria of preceding 'if' or 'else_if' is not met, and its own limit is met|if = { limit = { <triggers> } <effects> } else_if = { limit = { <triggers> } <effects> }|none||
|if|Executes enclosed effects if limit criteria are met|if = { limit = { <triggers> } <effects> }|none||
|random|run an effect depending on a random chance, do nothing otherwise.|random = { chance = 0-100 # random chance in percent. can also be a script value or complex math modifier = { ... } # optional MTTH-style modifier for the chance effects... # effects to run if the random roll succeeds }|none||
|random_list|randomly choose effects from a list|random_list = { 10 = { # defines an option with base chance 10 trigger = { ... } # optional trigger to enable/disable this option modifier = { ... } # optional MTTH-style modifier for the chance. Any special modifiers work here as well min = 5 # optional number to constrain this option's chance after applying modifiers max = 20 # optional number to constrain this option's chance after applying modifiers desc = loc_key # optional loc key to insert into this option's effect description show_chance = yes/no # whether to show this option's chance in the effect description, default is yes effects... # effects to run if this option is picked } 5 = { ... } # another option with base chance 5, so half as likely as the first one desc = loc_key # optional way to override the default header for the effect description pick = 3 # how many options to pick, default is 1 unique = yes/no # require picked entries to be unique, if pick > 1, default is no }|none||
|switch|Switch on a trigger for the evaluation of another trigger with an optional fallback trigger.|switch = { trigger = simple_assign_trigger case_1 = { <effects> } case_2 = { <effects> } case_n = { <effects> } fallback = { <effects> } }|none||
|while|Repeats enclosed effects while limit criteria are met or until set iteration count is reached|while = { limit = { <triggers> } <effects> } while = { count = 3 <effects> } Default max of 1000.|none||

## Log effects

Log effects output a message for testing and debugging purposes. They can always be used in any scope.

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|debug_log|Log a string to the debug log when this effect executes, the message can be a localization string with ROOT, SCOPE and PREV available|debug_log = message|none||
|debug_log_date|Logs the current date to the debug.log||none||
|debug_log_scopes|Log the current scope to the debug log when this effect executes|debug_log_scopes = yes # log full scope info debug_log_scopes = no # log only current scope|none||
|error_log|Log a string to the error log when this effect executes, error_log = message, the message can be a localization string with ROOT, SCOPE and PREV available||none||
|random_log_scopes|Log the current scope to the random log when this effect executes.|Only use temprorarily for debugging purposes as it can introduce localized strings into the random log. random_log_scopes = yes # log full scope info random_log_scopes = no # log only current scope|none||
|test_log|Log a string to the test log when this effect executes, test_log = message, the message can be a localization string with ROOT, SCOPE and PREV available.|test_log = { name = <test_key> text = <custom_log_message> }|none||

## Variable effects

Variable effects set or change the value of a variable. They can always be used in any scope, but may require a certain scope to affect the correct variable.

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|add_to_global_variable_list|Adds the event target to a global variable list for the given duration|add_to_global_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_global_variable_map|Adds the event target to a global variable map for the given duration|add_to_global_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_local_variable_list|Adds the event target to a local variable list for the given duration|add_to_local_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_local_variable_map|Adds the event target to a local variable map for the given duration|add_to_local_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_variable_list|Adds the event target to a variable list for the given duration|add_to_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_variable_map|Adds the event target to a variable map for the given duration|add_to_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|change_global_variable|Changes the value or a numeric variable|change_variable = { name = <variable_name> <operation> = <value> } Valid operations are add, subtract, multiply, divide, modulo, min and max|none||
|change_local_variable|Changes the value or a numeric variable|change_variable = { name = <variable_name> <operation> = <value> } Valid operations are add, subtract, multiply, divide, modulo, min and max|none||
|change_variable|Changes the value or a numeric variable|change_variable = { name = <variable_name> <operation> = <value> } Valid operations are add, subtract, multiply, divide, modulo, min and max|none||
|clamp_global_variable|Clamps a variable the specified max and min|clamp_variable = { name = <variable_name> max = <script_value> min = <script_value> }|none||
|clamp_local_variable|Clamps a variable the specified max and min|clamp_variable = { name = <variable_name> max = <script_value> min = <script_value> }|none||
|clamp_variable|Clamps a variable the specified max and min|clamp_variable = { name = <variable_name> max = <script_value> min = <script_value> }|none||
|clear_global_variable_list|Empties the list|clear_global_variable_list = variable_name|none||
|clear_global_variable_map|Empties the map|clear_global_variable_map = variable_name|none||
|clear_local_variable_list|Empties the list|clear_local_variable_list = variable_name|none||
|clear_local_variable_map|Empties the map|clear_local_variable_map = variable_name|none||
|clear_saved_scope|Clears a saved scope from the top scope|save_scope_as = cool_scope -> clear_saved_scope = cool_scope|none||
|clear_variable_list|Empties the list|clear_variable_list = variable_name|none||
|clear_variable_map|Empties the map|clear_variable_map = variable_name|none||
|every_in_global_list|Iterate through all items in global list.|every_in_global_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_in_list|Iterate through all items in list.|every_in_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_in_local_list|Iterate through all items in local list.|every_in_local_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_key_in_global_variable_map|Iterate through all items in global variable map.|every_key_in_global_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|every_key_in_local_variable_map|Iterate through all items in local variable map.|every_key_in_local_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|every_key_in_variable_map|Iterate through all items in variable map.|every_key_in_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|ordered_in_global_list|Iterate through all items in global list.|ordered_in_global_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_in_list|Iterate through all items in list.|ordered_in_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_in_local_list|Iterate through all items in local list.|ordered_in_local_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_key_in_global_variable_map|Iterate through all keys in a global variable map.|ordered_key_in_global_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_key_in_local_variable_map|Iterate through all keys in a local variable map.|ordered_key_in_local_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_key_in_variable_map|Iterate through all keys in a variable map.|ordered_key_in_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|random_in_global_list|Iterate through all items in global list.|random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_in_list|Iterate through all items in list.|random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_in_local_list|Iterate through all items in local list.|random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_key_in_global_variable_map|Iterate through all items in global variable map.|random_key_in_global_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_key_in_local_variable_map|Iterate through all items in local variable map.|random_key_in_local_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_key_in_variable_map|Iterate through all items in variable map.|random_key_in_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|remove_from_global_variable_map|Removes the target key and its value from a global variable map|remove_from_global_variable_map = { name = X key = Y }|none||
|remove_from_local_variable_map|Removes the target key and its value from a local variable map|remove_from_local_variable_map = { name = X key = Y }|none||
|remove_from_variable_map|Removes the target key and its value from a variable map|remove_from_variable_map = { name = X key = Y }|none||
|remove_global_variable|Removes a variable|remove_variable = variable_name|none||
|remove_list_global_variable|Removes the target from a global variable list|remove_list_global_variable = { name = <variable_name> target = <event_target> }|none||
|remove_list_local_variable|Removes the target from a local variable list|remove_list_local_variable = { name = <variable_name> target = <event_target> }|none||
|remove_list_variable|Removes the target from a variable list|remove_list_variable = { name = <variable_name> target = <event_target> }|none||
|remove_local_variable|Removes a variable|remove_variable = variable_name|none||
|remove_variable|Removes a variable|remove_variable = variable_name|none||
|round_global_variable|Rounds a variable to the nearest specified value|round_variable = { name = <variable_name> nearest = <script_value> }|none||
|round_local_variable|Rounds a variable to the nearest specified value|round_variable = { name = <variable_name> nearest = <script_value> }|none||
|round_variable|Rounds a variable to the nearest specified value|round_variable = { name = <variable_name> nearest = <script_value> }|none||
|set_global_variable|Sets a variable|set_variable = { name = <variable_name> value = <scope>/<value>/<flag:str> days = <script_value> (optional) } This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })|none||
|set_local_variable|Sets a variable|set_variable = { name = <variable_name> value = <scope>/<value>/<flag:str> days = <script_value> (optional) } This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })|none||
|set_variable|Sets a variable|set_variable = { name = <variable_name> value = <scope>/<value>/<flag:str> days = <script_value> (optional) } This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })|none||
|sort_global_variable_list|Sorts a global_variable list|sort_global_variable_list = { name = <variable_name> order = <script_value> }|none||
|sort_local_variable_list|Sorts a local variable list|sort_local_variable_list = { name = <variable_name> order = <script_value> }|none||
|sort_variable_list|Sorts a variable list|sort_variable_list = { name = <variable_name> order = <script_value> }|none||

## Effects by scope

The following tables list effects by their required scope. Iterators are excluded for space. They can be seen above or below. Some effects are repeated as they can be used in multiple scopes.

### None/any scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|abandon_colonial_charter|Abandons a colonial charter||colonial_charter|
|activate_situation|activates a situation||situation|
|add_extended_winter|Adds extended winter to target area||area|
|add_internal_flag|adds effect to be read internally (no effect in the gamestate)|||
|add_migration|sets up a migration|add_migration = { <from = provdef> <from_location = location> <to = provdef> <to_location = location> <culture = x> <religion = y> <type = z> months = x amount = y }||
|add_to_global_variable_list|Adds the event target to a global variable list for the given duration|add_to_global_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }||
|add_to_global_variable_map|Adds the event target to a global variable map for the given duration|add_to_global_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }||
|add_to_list|Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the (unbroken) event chain|add_to_list = <name_of_list> add_to_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a permanent target to a temporary list, the whole list becomes permanent||
|add_to_local_variable_list|Adds the event target to a local variable list for the given duration|add_to_local_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }||
|add_to_local_variable_map|Adds the event target to a local variable map for the given duration|add_to_local_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }||
|add_to_temporary_list|Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the same effect|add_to_temporary_list = <name_of_list> add_to_temporary_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a temporary target to a permanent list, the list will stay permanent||
|add_to_variable_list|Adds the event target to a variable list for the given duration|add_to_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }||
|add_to_variable_map|Adds the event target to a variable map for the given duration|add_to_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }||
|assert_if|Conditionally cause an assert during run time|assert_if = { limit = { <trigger> } text = <string> }||
|assert_read|Conditionally cause an assert during read time|assert_read = X, where X is yes or the string to be printed in the assert||
|cancel_exploration|cancels the target exploration||exploration|
|cancel_loan|cancels a loan||loan|
|change_global_variable|Changes the value or a numeric variable|change_variable = { name = <variable_name> <operation> = <value> } Valid operations are add, subtract, multiply, divide, modulo, min and max||
|change_local_variable|Changes the value or a numeric variable|change_variable = { name = <variable_name> <operation> = <value> } Valid operations are add, subtract, multiply, divide, modulo, min and max||
|change_variable|Changes the value or a numeric variable|change_variable = { name = <variable_name> <operation> = <value> } Valid operations are add, subtract, multiply, divide, modulo, min and max||
|clamp_global_variable|Clamps a variable the specified max and min|clamp_variable = { name = <variable_name> max = <script_value> min = <script_value> }||
|clamp_local_variable|Clamps a variable the specified max and min|clamp_variable = { name = <variable_name> max = <script_value> min = <script_value> }||
|clamp_variable|Clamps a variable the specified max and min|clamp_variable = { name = <variable_name> max = <script_value> min = <script_value> }||
|clear_global_variable_list|Empties the list|clear_global_variable_list = variable_name||
|clear_global_variable_map|Empties the map|clear_global_variable_map = variable_name||
|clear_local_variable_list|Empties the list|clear_local_variable_list = variable_name||
|clear_local_variable_map|Empties the map|clear_local_variable_map = variable_name||
|clear_saved_scope|Clears a saved scope from the top scope|save_scope_as = cool_scope -> clear_saved_scope = cool_scope||
|clear_variable_list|Empties the list|clear_variable_list = variable_name||
|clear_variable_map|Empties the map|clear_variable_map = variable_name||
|close_all_views|Closes all views. close_all_views = yes|||
|conditional_effect|An effect which works similar to a simple if effect, but it will always display the effect and conditions for the effect to happen. Also has an else section in case the conditions are not met.|conditional_effect = { effect = <effects> limit = <triggers> [else = <effects>] }||
|copy_country_color|Copy the color of the target country and apply it to the current country scope||country|
|copy_country_flag|Copy the flag of the target country and apply it to the current country scope||country|
|copy_country_name_and_adjective|Copy the name and adjective of the target country and apply it to the current country scope||country|
|create_holy_site|Creates a holy site||holy_site|
|create_international_organization|Creates an empty international organization, changing the scope to the created IO. Make sure to use add_country_to_international_organization / set_leader_country to set up the leader if needed.|create_international_organization = { type = <type_id> [creator = <country> (country which would found the IO)] [target = <country>] }|international_organization|
|create_market|creates a market.|create_market = { builder = <country> location = <location> price = <link_to_price> instant = <yes/no> price_modifier = <script_value> }||
|create_mercenary|Creates a mercenary company.|create_mercenary = { name = <name_of_the_company> borrower = <country that is the customer> cost_multiplier = <cost> home = <home_location> area = < area they're based> <sub_unit_definition> = adds a unit of this type (tags in unit_types) <sub_unit_category> = <number> adds <number> of the best unit available of this type in the home location (category tags listed in unit_categories) }|mercenary|
|create_relation|Creates a relation with the target country.|create_relation = { type = <scripted relation type key> first = <country> second = <country> [years/months/days = <script_integer> for expiring relations ] }||
|create_route|Finds route between a select start and end location.|create_route = { start = <location> end = <location> limit = <location_trigger> with scope:from provided for previous location and scope:distance for distance weight = <location_scriptvalue> that modifies the provided scope:distance and has scope:to location effect = <location_effect> which fires for every location in the resulting path with scope:from and scope:to provided when possible. }||
|custom_description|Wraps effects that get a custom description instead of the auto-generated one|custom_description = { text = <effect_localization_key> subject = <optional_subject_scope> #defaults to current scope object = <optional_object_scope> value = <optional_script_value> ... effects ... }||
|custom_description_no_bullet|Wraps effects that get a custom description instead of the auto-generated one. Also ensures no bullet point appears|custom_description_no_bullet = { text = <effect_localization_key> subject = <optional_subject_scope> #defaults to current scope object = <optional_object_scope> value = <optional_script_value> ... effects ... }||
|custom_label|just a tooltip, the scope as object (for grouping, localization).|custom_label = key alternatively custom_label = { text = key subject = scope (optional) <hidden_effects> }||
|custom_tooltip|just a tooltip, the scope as subject (for grouping, localization).|custom_tooltip = key alternatively custom_tooltip = { text = key subject = scope (optional) <hidden_effects> }||
|debug_log|Log a string to the debug log when this effect executes, the message can be a localization string with ROOT, SCOPE and PREV available|debug_log = message||
|debug_log_date|Logs the current date to the debug.log|||
|debug_log_scopes|Log the current scope to the debug log when this effect executes|debug_log_scopes = yes # log full scope info debug_log_scopes = no # log only current scope||
|destroy_art|destroys the target art|destroy_art = work_of_art:name_key|work_of_art|
|destroy_building_country|destroys building based country removing all their buildings and releasing subjects.|destroy_building_country = <country>|country|
|destroy_colonial_charter|destroys the target colonial_charter||colonial_charter|
|destroy_holy_site|destroys the target holy site||holy_site|
|destroy_international_organization_no_instigator|destroys the target international organization.|destroy_international_organization_no_instigator = { target = <io_scope> reason = <loc key for reason> }||
|destroy_mercenary|Mercenary gets routed and scatters||mercenary|
|destroy_pop|destroys a pop||pop|
|destroy_rebel|Destroys the target rebel||rebels|
|end_situation|End a situation||situation|
|error_log|Log a string to the error log when this effect executes, error_log = message, the message can be a localization string with ROOT, SCOPE and PREV available|||
|every_country_of_country_type|Iterate through all countries of the specified type.|every_country_of_country_type = { limit = { <triggers> } <effects> }|country|
|execute_propose_effect|Execute the popose_effect of any implementable object (policies, avatar, cabinet_action, estate_privilege, god, government_reform).|execute_propose_effect = { source = <implementable object id> [<flag> = <scope>] }||
|find_route|Finds route between start location and closest eligible end location|find_route = { start = <location> end = <location_trigger> limit = <location_trigger> with scope:from provided for previous location and scope:distance for distance weight = <location_scriptvalue> that modifies the provided scope:distance and has scope:to location effect = <location_effect> which fires for every location in the resulting path with scope:from and scope:to provided when possible. }||
|fire_generic_action|fires a generic action with the country as the actor and the supplied thing as the recipient|||
|force_city_gfx_rebuild|Rebuilds the city gfx||location|
|force_recalc_country_active_status|Recalculates active country status||country|
|force_refresh_culture_and_religion|Recalculates dominant relgion and culture in a location||location|
|hidden_effect|Enclosed effects are not shown in tooltips|hidden_effect = { <more_effects> }||
|international_organization_chooses_new_leader|international organization chooses a new leader||international_organization|
|io_recalculate_leader|force an international organization to recalculate its character leader from the current ruler of the leader country||internation_organization|
|kill_character|Kills the target character.|kill_character = <character> or kill_character = { target = <character> [location = <location>] [disease = <disease>] [killer = <character>] [reason = <reason>] }|character|
|kill_character_silently|Kills the target character without message popups.|kill_character = <character> or kill_character = { target = <character> [location = <location>] [disease = <disease>] [killer = <character>] [reason = <reason>] }|character|
|ordered_country_of_country_type|Iterate through all countries of the specified type.|ordered_country_of_country_type = { limit = { <triggers> } order_by = script_value (position = int) (min = int) (max = script_value) (check_range_bounds = no) # If you don't want an error logged if the list is smaller than the min/max <effects> }|country|
|post_audio_event|Runs an audio even on a "persistent" audio object|post_audio_event = { persistent_object = [object_name] # For example music_manager event = [audio_event] # For example start_debug_music parameters = { noise = 3.14 } switches = { toggle_1 = on another_switch = hello_world } }||
|propose_resolution|proposes a new resolution. type = <resolution_key> actor = <proposer_country> recipient = <international organisation or situation>|||
|random_country_of_country_type|Iterate through all countries of the specified type.|random_country_of_country_type = { limit = { <triggers> } (weight = { <mean time to happen value> }) <effects> }|country|
|random_log_scopes|Log the current scope to the random log when this effect executes.|Only use temprorarily for debugging purposes as it can introduce localized strings into the random log. random_log_scopes = yes # log full scope info random_log_scopes = no # log only current scope||
|refresh_map_colors|Refreshes the map colours|||
|remove_colonial_claim|Removed the colonial claim in the target province_definition||province_definition|
|remove_commander|removes the target character from his unit||character|
|remove_extended_winter|Removed extended winter to target area||area|
|remove_from_global_variable_map|Removes the target key and its value from a global variable map|remove_from_global_variable_map = { name = X key = Y }||
|remove_from_list|Removes the current scope from a named list|remove_from_list = <string>||
|remove_from_local_variable_map|Removes the target key and its value from a local variable map|remove_from_local_variable_map = { name = X key = Y }||
|remove_from_variable_map|Removes the target key and its value from a variable map|remove_from_variable_map = { name = X key = Y }||
|remove_global_variable|Removes a variable|remove_variable = variable_name||
|remove_list_global_variable|Removes the target from a global variable list|remove_list_global_variable = { name = <variable_name> target = <event_target> }||
|remove_list_local_variable|Removes the target from a local variable list|remove_list_local_variable = { name = <variable_name> target = <event_target> }||
|remove_list_variable|Removes the target from a variable list|remove_list_variable = { name = <variable_name> target = <event_target> }||
|remove_local_variable|Removes a variable|remove_variable = variable_name||
|remove_migration|removes a migration|remove_migration = { <from = provdef> <from_location = location> <to = provdef> <to_location = location> <culture = x> <religion = y> <type = z> months = x amount = y }||
|remove_relation|Removes a relation with the target country|||
|remove_variable|Removes a variable|remove_variable = variable_name||
|revoke_town_rights|Revoke a specific town rights||town_rights|
|round_global_variable|Rounds a variable to the nearest specified value|round_variable = { name = <variable_name> nearest = <script_value> }||
|round_local_variable|Rounds a variable to the nearest specified value|round_variable = { name = <variable_name> nearest = <script_value> }||
|round_variable|Rounds a variable to the nearest specified value|round_variable = { name = <variable_name> nearest = <script_value> }||
|save_scope_as|Saves the current scope as an arbitrarily-named target to be referenced later in the (unbroken) event chain|save_scope_as = <string>||
|save_scope_value_as|Saves a numerical or bool value as an arbitrarily-named target to be referenced later in the (unbroken) event chain|save_scope_value_as = { name = <string> value = x }||
|save_temporary_scope_as|Saves the current scope as an arbitrarily-named temporary target to be referenced later in the same effect|save_temporary_scope_as = <string>||
|save_temporary_scope_value_as|Saves a numerical or bool value as an arbitrarily-named temporary target to be referenced later in the same effect|save_temporary_scope_value_as = { name = <string> value = x }||
|set_collection_pin|Sets collection pin.|||
|set_country_military_stance|Sets the country's military stance||military_stance|
|set_global_variable|Sets a variable|set_variable = { name = <variable_name> value = <scope>/<value>/<flag:str> days = <script_value> (optional) } This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })||
|set_local_variable|Sets a variable|set_variable = { name = <variable_name> value = <scope>/<value>/<flag:str> days = <script_value> (optional) } This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })||
|set_tutorial_var|Sets tutorial var.|||
|set_variable|Sets a variable|set_variable = { name = <variable_name> value = <scope>/<value>/<flag:str> days = <script_value> (optional) } This variable will be accessible with <type_>var:X. With type being in a scope object or in a top scope Can also be used as set_variable = X (equivalent to set_variable = { name = X value = yes })||
|show_as_tooltip|Enclosed effects are only shown in tooltips (but are not actually executed)|show_as_tooltip = { <more_effects> }||
|sort_global_variable_list|Sorts a global_variable list|sort_global_variable_list = { name = <variable_name> order = <script_value> }||
|sort_local_variable_list|Sorts a local variable list|sort_local_variable_list = { name = <variable_name> order = <script_value> }||
|sort_variable_list|Sorts a variable list|sort_variable_list = { name = <variable_name> order = <script_value> }||
|spawn_army_levy_unit|Spawn an army levy unit for the target country in the current location scope||country|
|spawn_navy_levy_unit|Spawn a navy levy unit for the target country in the current location scope||country|
|start_tutorial_lesson|Starts the tutorial lesson with the given key. Does nothing if the tutorial is not running, the lesson is completed (or already running), or the lesson cannot be triggered (e.g. trigger fails)|||
|start_weather_system|Starts off a new weather system.|start_weather_system = { width = <pixels> length = <pixels> strength = [0..1] speed = <pixels_per_day> type = <front/cyclone/tornado> location = <start_location> location = <waypoint> [location = <waypoint>...] }|weather_system|
|stop_tutorial|Stops the tutorial.|||
|test_log|Log a string to the test log when this effect executes, test_log = message, the message can be a localization string with ROOT, SCOPE and PREV available.|test_log = { name = <test_key> text = <custom_log_message> }||
|trigger_event_non_silently|triggers an event or on_action, but shows the name of the event|trigger_event_non_silently = { id = X days/months/years = Y } (for events)||
|trigger_event_silently|triggers an event or on_action|trigger_event_silently = { id = X days/months/years = Y } (for events) or trigger_event_silently = { on_action = X days/months/years = Y } (for on_actions) Days/months/years are optional and equal to 0 if not specified. If specified, Y can be a value or an inclusive interval "{ A B }" from which the duration will be picked randomly.||
|update_leadership|Update the leadership panel of the target international organization.||international_organization|
|white_peace|forces a white peace in the target war||war|

### Building scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|change_building_level|change the level of a building|||
|change_building_owner|assigns a new owner to a building||country|
|set_subsidized|change whether a building is subsidised or not|||

### Character scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|add_adm|Adds adm ability|||
|add_artist_skill|gives (or takes) artist_skill to a character|||
|add_character_modifier|add a modifier to a character|add_character_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }||
|add_dip|Adds dip ability|||
|add_fertility|gives (or takes) fertility to a character|||
|add_mil|Adds mil ability|||
|add_random_trait_from_category|adds a random trait to a character from a category (admiral, artist, explorer, general, child, ruler)|||
|add_trait|adds a trait to a character||trait|
|adopt_character|makes a character adopt another||character|
|change_character_allegiance|change rebel allegiance of Character to target Rebel||rebels|
|change_character_culture|changes character's culture||culture|
|change_character_estate|changes character's estate||estate_type|
|change_character_modifier_size|Change the strength of a modifier applied to the scope character|change_character_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }||
|change_character_religion|Changes religion for a character||religion|
|change_dynasty|changes dynasty to target dynasty||dynasty|
|change_father|changes father to target character||character|
|change_mother|changes mother to target character||character|
|divorce_character|Marries character to target character||character|
|found_dynasty|Makes the character found a new dynasty. If no name is specified, it will be named after the character's birth Location, but the effect still needs to be inside curly brackets|||
|impregnate|Impregnates a target character||character|
|make_saint|Makes a character a saint||country|
|make_saint_in_character_religion|Makes a character a saint in their religion, regardless of the country's religion||country|
|marry_character|Marries character to target character||character|
|marry_character_ignore_blocks|Marries character to target character, ignoring social restrictions such as estate, modifiers and same sex ban||character|
|move_country|Moves character to target country||country|
|remove_character_allegiance|Remove the character scope from the rebel group they are part of.|||
|remove_character_modifier|Remove a modifier from a character|remove_character_modifier = name||
|remove_ruler|Removes the character as ruler from the target country||country|
|remove_trait|removes a trait to a character||trait|
|remove_traits_of_category|Removes all traits of a specified category. Supports the categories: ruler, general, admiral, artist, explorer, child, religious_figure|||
|reset_ruler_title|resets a ruler's title so it gets generated again|||
|set_child_education|Set the education type of a child|set_child_education = education|child_education|
|set_ethnicity|Set the ethnicity of a character||ethnicity|
|set_first_name|Set the first name of a character to the defined string or scoped character|||
|set_lowborn|The character gets removed from its current dynasty, making it a lowborn|||
|set_nickname|Set the nickname of a character to the defined string|||
|set_to_limited_random_stat|Sets the stats of the character scope to a random value between a min and max value.|set_to_limited_random_stat = { ability = adm/dip/mil max = <scripted value> min = <scripted value> }||
|start_work_of_art|Makes the target character start working on some art.|start_work_of_art = { work_of_art_type = work_of_art_type:<type> (optional, will start a random type of WoA if not set) quality = <calc> (optional, will take artist skill into consideration if unset) show_quality = yes/no (by default no, shows the probable quality of the WoA before it is finished) }||

### Country scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|abandon_location|Abandons the target location!||location|
|add_accepted_culture|Adds an accepted culture to a country||culture|
|add_antagonism|Adds an antagonism modifier|add_antagonism = { modifier = <scripted_modifier> target = Z scale = {script value} }||
|add_area_preference|Adds an area preference to the AI of a country|||
|add_army_tradition|Adds army tradition|||
|add_avatar|adds an avatar to a country||avatar|
|add_bureaucracy|Adds a new bureaucracy of the supplied type to the country's government.||bureaucracy_type|
|add_casus_belli|Adds a casus belli for the current country scope against the target country.|add_casus_belli = { target = <country_scope> type = <casus_belli_type> [province = <province>] [days/weeks/months/years = <script_value> (-1 means permanently)] }||
|add_colonial_claim|Add a colonial claim to the target province_definition.|add_colonial_claim = { province_definition = <province_definition> reason = <reason_loc> [category = <exclusive/same_religion>] }||
|add_complacency|Adds complacency|||
|add_cooldown|adds a cooldown for a country or international organization.|add_cooldown = { type = <token> days/weeks/months/years = <integer> }||
|add_country_modifier|add a modifier to a country|add_country_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }||
|add_devotion|Adds devotion|||
|add_diplomats|gives (or takes) diplomats for a country|||
|add_doom|Adds doom|||
|add_estate_satisfaction|Changes the satisfaction of an estate|||
|add_favors|Adds favors|add_favors = { target = x value = y }||
|add_god|adds a god to a country||god|
|add_gold|Adds gold|||
|add_gold_to_estate|Changes the gold of an estate|||
|add_government_power|Adds government power|||
|add_harmony|Adds Harmony|||
|add_historical_rival|adds target country as an historical rival||country|
|add_honor|Adds honor|||
|add_horde_unity|Adds horde_unity|||
|add_inflation|Adds inflation|||
|add_karma|Adds karma|||
|add_legitimacy|Adds legitimacy|||
|add_liberty_desire|gives (or takes) liberty desire for a (subject) country|||
|add_location_as_core|Adds the target location as core||location|
|add_manpower|Adds Manpower|||
|add_navy_tradition|Adds navy tradition|||
|add_opinion|Adds an opinion modifier|add_opinion = { modifier = <modifier_name> target = Z scale = {script value} }||
|add_policy|Add a policy to a country.||policy|
|add_policy_wanted_by_estate|For the country in scope, set the policy wanted by the input estate in the input law|||
|add_prestige|Adds prestige|||
|add_purity|Adds purity|||
|add_reform|adds a government reform.||government_reform|
|add_religious_aspect|adds a religious_aspect to a country||religious_aspect|
|add_religious_focus|Add a completed religious focus to the country scope||religious_focus|
|add_religious_focus_progress|Change the progress for the current religious focus to the country scope|||
|add_religious_influence|Adds religious influence|||
|add_republican_tradition|Adds republican_tradition|||
|add_research_progress|gives (or takes) research progress for a country|||
|add_righteousness|Adds Righteousness|||
|add_rite_power|Adds rite power|||
|add_rival|adds target country as a rival||country|
|add_sailors|Adds sailors|||
|add_self_control|Adds Self Control|||
|add_spy_network|Adds spy_network (target = x value = y}|||
|add_stability|Adds stability|||
|add_tolerated_culture|Adds an Tolerated culture to a country||culture|
|add_tribal_cohesion|Adds tribal_cohesion|||
|add_truce_with|Adds a truce with the target country.|add_truce_with = { target = <target_country> [days/months/years = x] [mutual = yes] }||
|add_trust|Adds trust|add_trust = { target = X scale = {script value} }||
|add_trust_equilibrium|Adds a trust equilibriam modifier|add_trust_equilibrium = { modifier = <modifier_name> target = Z scale = {script value} }||
|add_war_exhaustion|Adds WarExhaustion|||
|add_yanantin|Adds yanantin|||
|add_yearly_gold|Adds a proportion of your yearly gold|||
|add_yearly_manpower|Adds a proportion of your yearly Manpower|||
|add_yearly_sailors|Adds a proportion of your yearly sailors|||
|align_societal_values_to|Aligns the societal values of the current country scope to the ones of the target country.||country|
|annex_country|annexes the target country.|annex_country = { country = <country> [reason = <Diplomatic\|CivilWar\|MilitaryConquest>] [transfer = yes] }||
|block_treaties|Block all possible treaties with the target country||country|
|bribe_estate|The current country scope bribes the estate of the target country using the specified parliament agenda.|bribe_estate = { type = <parliament_agenda> estate_type = <estate_type> target = <country> }||
|bypass_mission_task|The country scope bypasses the specified mission task. Does not do anything if the mission task is not part of the currently active mission and if it is not visible.||mission_task|
|cancel_area_exploration|country stops exploring the target_area||area|
|cancel_subject|cancel the subject status of the target||country|
|change_annexation_progress|Changes the progress of annexation for the current country scope against the target country. No effect if there is no active annexation going on already.|change_annexation_progress = { target = <country_scope> value = <script_value> }||
|change_casus_belli_creation_progress|Changes the progress when creating a casus belli against a target country.|change_casus_belli_creation_progress = { target = <country> value = <value> }||
|change_country_adjective|changes the adjective of a country|||
|change_country_color|changes the color of a country|||
|change_country_dynastic_name|Changes the name, adjective, and flag of a country to the dynasty of the ruler|||
|change_country_flag|changes the flag of a country|change_country_flag = <coat_of_arms>|coat_of_arms|
|change_country_modifier_size|Change the strength of a modifier applied to the scope country|change_country_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }||
|change_country_name|changes the name of a country|||
|change_country_type|Changes the country type!|||
|change_culture|Changes culture for a country||culture|
|change_explorer|sets a new explorer for an exploration in the current country|change_explorer { area = x character = y }||
|change_government_type|Changes government-type for a country||government|
|change_heir_selection|Changes heir_selection for a country||heir_selection|
|change_parliament_issue_support|gives (or takes) support for the issue in parliament|||
|change_player|Changes the player in the current country scope to play another country||country|
|change_religion|Changes religion for a country||religion|
|change_score|gives (or takes) score a country|||
|change_societal_value|Changes societal value|||
|change_subject_type|Change the subject type for the current country scope to the specified subject type||subject_type|
|complete_mission_task|The country scope completes the specified mission task. Does not do anything if the mission task is not part of the currently active mission and if it is not visible.||mission_task|
|construct_road|starts the construction of a road from A to B owned by the scope country.|construct_road = { road_type = scoped road type from = location to = location }||
|create_character|Creates a character for a country||character|
|create_colonial_charter|Creates a colonial charter in the target province_definition|||
|create_country_from_cores_in_our_locations|creates the country from its cores||country|
|create_estate_loan|scope country takes a specialized estate loan|create_estate_loan = { amount = gold interest = percent months = months }|loan|
|create_named_dynasty|creates a dynasty with the specificed name|||
|create_rebel|Creates a new rebel with in the current country|create_rebel = { name = x data = { category = x <government = t> <culture = y> <religion = x> <estate = z> } }|rebels|
|create_trade|creates a trade.|create_trade { from = <market> to = <market> merchant = <market where the merchant is> goods = <goods> locked = <locked> desired = <desired merchant capacity to use> }||
|create_union|Current country scope creates a union with the target scope. Unions get merged if either country has a union already.||country|
|declare_war|declares a war with the target country. The country scope will leave all wars they fight together with the target country.||country|
|declare_war_with_cb|declares a war with a specific cb. The country scope will leave all wars they fight together with the target country.|declare_war_with_cb = { target = <country> type = <cb_type> }||
|define_unique_country_tag|defines a unique country tag for a dynamic country|||
|demote_accepted_culture|Removes an accepted culture and adds it as tolerated, with a single pop status update||culture|
|destroy_international_organization|destroys the target international organization.|destroy_international_organization = { target = <io_scope> reason = <loc key for reason> }||
|discover_area|country discovers the target_area||area|
|dismiss_mercenary|dismisses a mercenary for the target country||mercenary|
|distribute_gold_to_banking_estates|Distributes gold proportionally to all banking estates in a country|||
|drop_antagonism_bomb|Drops an antagonism bomb at a location, causing antagonism with surrounding countries depending on how they feel about you and the target.|drop_antagonism_bomb = { target = <location> value = <script_value for base antagonism> modifier = <antagonism_bias> [is_taking_value = yes <calculates antagonism as if the target would be taken>] }||
|end_mission|The country scope ends its currently active mission. If set yes, it will complete it, otherwise it will abort the mission.|||
|end_parliament|End the current parliament session. If set 'yes', pass the issue, if set 'no' then fail the issue instead.|||
|extend_regency|extends the regency by X years|||
|force_union|Current country scope forces a union with the target scope. In case of a union merge, the country which forces the union keeps the ruler.||country|
|form_country|Forms a new country (using formable system)||formable_country|
|form_new_culture|Creates a new culture in this country from the primary culture|||
|give_loan|gives a loan|give_loan = { target = country amount = gold interest = percent months = months }|loan|
|grant_estate_privilege|grants a special estate priviledge.||estate_privilege|
|grant_parliament_agenda|Accept the specified target parliament agenda.||parliament_agenda|
|grant_parliament_agenda_for_estate|Accept the parliament agenda of the target estate type.||estate_type|
|hire_mercenary|hires a mercenary for the target country||mercenary|
|join_war_against|joins the target war as an enemy of the target country.|join_war_against = { war = war scope target = country scope call_in_subjects = yes/no ignore_rules = yes/no notify_opposing_side = yes/no }||
|join_war_as_attacker|joins the target war as an attacker.|join_war_as_attacker = { war = war scope call_in_subjects = yes/no ignore_rules = yes/no }||
|join_war_as_defender|joins the target war as a defender.|join_war_as_defender = { war = war scope call_in_subjects = yes/no ignore_rules = yes/no }||
|join_war_with|joins the target war as an ally of the target country.|join_war_with = { war = war scope target = country scope call_in_subjects = yes/no ignore_rules = yes/no notify_opposing_side = yes/no }||
|leave_all_wars_with|The current country scope will leave every war with or against the target country.||country|
|leave_war|leaves a war, forced by another country.|leave_war = { war = <war> actor = <country forcing them to do it> }||
|lift_fog_of_war|lifts fog of war for a year on the target country||country|
|loot_location|The unit or country scope will loot the target location.||location|
|make_subject_of|Becomes a subject of the target country|make_subject_of = { target = x type = y }||
|merge_culture_group|Merges the primary culture's culture group in this country||culture_group|
|pay_off_loans|pays off % of the current loans.|pay_off_loans = { fraction = <script_number> [payer = <country_scope>] }||
|pay_policy_price_effect|executes the policy price effect on the current scope||policy|
|pay_price|Pays a Price from a country||price|
|perform_diplomatic_action||perform_diplomatic_action = { type = <diploaction or country interaction type> actor/receipent/target/target_1... = country/province/location/character/whatever [mode = propose/accept/decline #determines if the action is a proposal (default), a forced acceptance or a forced decline] [hidden = yes #it will be hidden if the diplo action is a proposal / will be accepted / declined] }||
|raise_all_levies|The country scope will raise all its levies of the specified type.|raise_all_levies = { type = army/navy [instant = yes] }||
|refund_price|Refund a Price to a country||price|
|release_non_cores|releases all non-core provinces|||
|remove_accepted_culture|Removes an accepted culture from a country||culture|
|remove_all_area_preferences|Removes all area preferences from the AI of a country|||
|remove_all_casus_belli|removes all casus belli on the target country||country|
|remove_antagonism|Removes an antagonism modifier|remove_antagonism = { modifier = <modifier_name> target = Z scale = {script value} }||
|remove_area_preference|Removes an area preferences from the AI of a country|||
|remove_avatar|removed an avatar from a country||avatar|
|remove_bureaucracy|remove the supplied bureaucracy from the country's government.||bureaucracy|
|remove_casus_belli|Removes casus_belli|remove_casus_belli = { target = x type = y <province = prov> }||
|remove_cooldown|Removes a cooldown for a country or international organization.|remove_cooldown = <cooldown_token>||
|remove_country_modifier|Remove a modifier from a country|remove_country_modifier = name||
|remove_from_cabinet|Removes the character from the cabinet||character|
|remove_god|removed a god from a country||god|
|remove_historical_rival|removes target country as an historical rival||country|
|remove_law|Makes a law get no options, which may make it disappear||law|
|remove_omen|removes an omen from a country||omen|
|remove_opinion|Removes an opinion modifier|remove_opinion = { modifier = <modifier_name> target = Z scale = {script value} }||
|remove_policy|Remove a policy from a country.||policy|
|remove_reform|removes the government reform desired.||government_reform|
|remove_religious_aspect|removed a religious_aspect from a country||religious_aspect|
|remove_religious_focus|Remove a completed religious focus from the country scope||religious_focus|
|remove_rival|removes target country as a rival||country|
|remove_tolerated_culture|Removes an Tolerated culture from a country||culture|
|remove_truce_with|Removes the truce with the target country||country|
|remove_trust_equilibrium|Removes a trust equilibriam modifier|remove_trust_equilibrium = { modifier = <modifier_name> target = Z scale = {script value} }||
|research_advance|Research a specific advance|research_advance = name|advance_type|
|reset_regency|performs the start_effect of a regency again|||
|reverse_add_antagonism|Adds a reverse antagonism modifier|reverse_add_antagonism = { modifier = <modifier_name> target = Z scale = {script value} }||
|reverse_add_opinion|Adds an reverse opinion modifier|reverse_add_opinion = { modifier = <modifier_name> target = Z scale = {script value} }||
|reverse_add_trust_equilibrium|Adds a reverse trust equilibrium modifier|reverse_add_trust_equilibrium = { modifier = <modifier_name> target = Z scale = {script value} }||
|revoke_estate_privilege|revokes a special estate priviledge.||estate_privilege|
|set_age_preference|Sets age preference for this age for a country|||
|set_army_tradition|Sets army tradition|||
|set_as_designated_heir|Sets the target character as the designated heir for the scope country.|set_as_designated_heir = <character> or set_as_designated_heir = { target = <character> [reason = <reason>] }|character|
|set_automated_system|Activate or deactivate the automation of a system for one country. Will only have an effect if this country is played or will be played by a player.|ARA = { set_automated_system = { system = finances } set_automated_system = { system = research activate = no } }||
|set_bankruptcy|Make the country either bankrupt if set to yes, or get it out of its current bankruptcy if set to no.|||
|set_capital|Sets the target location as capital of the country||location|
|set_complacency|Sets complacency|||
|set_country_employment_system|Sets the country's employment system||employment_system|
|set_country_rank|Sets the country rank||country_rank|
|set_court_language|Sets the court_language to the target dialect||dialect|
|set_devotion|Sets devotion|||
|set_doom|Sets doom|||
|set_gold|Sets gold|||
|set_government_power|Sets government power|||
|set_harmony|Sets Harmony|||
|set_honor|Sets honor|||
|set_horde_unity|Sets horde_unity|||
|set_inflation|Sets inflation|||
|set_karma|Sets karma|||
|set_legitimacy|Sets legitimacy|||
|set_liturgical_language|Sets the Liturgical_language to the target language||dialect|
|set_manpower|Sets Manpower|||
|set_navy_tradition|Sets navy tradition|||
|set_new_foreign_ruler|Makes the target_character the new ruler without forcing them to move to the country||character|
|set_new_foreign_ruler_no_update|Makes the target_character the new ruler without forcing them to move to the country, without updating any unions or fiefdom-like titles the character has||character|
|set_new_ruler|Makes the target_character the new ruler||character|
|set_new_ruler_no_update|Makes the target_character the new ruler, without updating any unions or fiefdom-like titles the character has||character|
|set_parliament_active|Set parliament active or not. The issue of the parliament will be removed without triggering any of its effects if set to no.|||
|set_parliament_issue|Set the specified issue as the topic of the parliament.||parliament_issue|
|set_parliament_issue_support|sets base support for the issue when calling a parliament|||
|set_parliament_location|Sets the parliament location. Use immediately before 'set_parliament_active = yes'||location|
|set_parliament_type|Set the specified parliament type for a country||parliament_type|
|set_participated_in_parliament|Mark the country as having participated in the parliament of the target international organization. Is automatically set when a country votes in a parliament which has the resolution.||international_organization|
|set_personality|Sets the AI personality for a country||ai_personality|
|set_prestige|Sets prestige|||
|set_purity|Sets purity|||
|set_regent|Makes the target_character the acting regent||character|
|set_religious_influence|Sets religious influence|||
|set_religious_school|Sets the religious_school to the target school||religious_school|
|set_republican_tradition|Sets republican_tradition|||
|set_revolution|Make the country either revolutionary if set to yes, or get remove its revoutionary status if set to no.|||
|set_revolution_target|Make the country to the target of the revolution if set to yes, or remove it when set to no.|||
|set_righteousness|Sets Righteousness|||
|set_rite_power|Sets rite power|||
|set_sailors|Sets sailors|||
|set_self_control|Sets Self Control|||
|set_societal_value|Sets societal value|||
|set_stability|Sets stability|||
|set_tribal_cohesion|Sets tribal_cohesion|||
|set_war_exhaustion|Sets WarExhaustion|||
|set_yanantin|Sets yanantin|||
|start_conquistador|Creates a new conquistador in the current country|start_conquistador = { area = <area> location = <location in area to make capital> character = <character> price = <price> price_modifier = <number> }||
|start_exploration|Creates a new exploration in the current country|start_exploration = { area = <area> character = <character> price = <price> price_modifier = <number> }||
|start_mission|The country starts immediately the specified mission. Will not do anything if a mission is active already.|start_mission = { mission = <mission_scope> [optional any parameters to pass in, eg target = x] }||
|stop_annexing_country|scope country stops annexing the target country||country|
|support_rebel|scope country starts supporting the target rebel||rebels|
|take_over_all_wars|takes over all wars where target country is warleader||country|
|transfer_subject|Transfers scope subject to target country's overlordship||country|
|transfer_yearly_gold|Transfers a proportion of your yearly gold to the target country|||
|transfer_yearly_manpower|Transfers a proportion of your yearly Manpower to the target country|||
|transfer_yearly_sailors|Transfers a proportion of your yearly sailors to the target country|||
|unset_participated_in_parliament|Remove the mark of the country as having participated in the parliament of the target international organization.||international_organization|

### Culture scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|add_cultural_influence|gives (or takes) cultural_influence to a culture|||
|add_cultural_tradition|gives (or takes) cultural_tradition to a culture|||
|change_cultural_view|Changes the cultural view of target.|change_cultural_view = { target = x change = relation_change }||
|change_language|changes the language of a culture||dialect|
|reverse_change_cultural_view|Sets the targets cultural view of current culture.|reverse_change_cultural_view = { target = x value = relation_change }||
|reverse_set_cultural_view|Sets the targets cultural view of current culture.|reverse_set_cultural_view = { target = x value = relation_level }||
|set_cultural_view|Sets the cultural view of target.|set_cultural_view = { target = x value = relation_level }||

### Goods scope

|Effect|Description|Example|Targets|

### Institution scope

|Effect|Description|Example|Targets|

### International organization scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|add_army_tradition|Adds army tradition|||
|add_complacency|Adds complacency|||
|add_cooldown|adds a cooldown for a country or international organization.|add_cooldown = { type = <token> days/weeks/months/years = <integer> }||
|add_country_to_international_organization|add a country to an international organization||country|
|add_country_to_international_organization_no_update|add a country to an international organization without updating diplo statuses||country|
|add_devotion|Adds devotion|||
|add_doom|Adds doom|||
|add_enemy_to_international_organization|add a country to an international organization||country|
|add_gold|Adds gold|||
|add_government_power|Adds government power|||
|add_harmony|Adds Harmony|||
|add_honor|Adds honor|||
|add_horde_unity|Adds horde_unity|||
|add_inflation|Adds inflation|||
|add_international_organization_modifier|add a modifier to an international organization|add_international_organization_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }||
|add_karma|Adds karma|||
|add_legitimacy|Adds legitimacy|||
|add_location_to_international_organization|add a location to an international organization||location|
|add_manpower|Adds Manpower|||
|add_navy_tradition|Adds navy tradition|||
|add_policy_to_international_organization|add a policy to an international organization||policy|
|add_prestige|Adds prestige|||
|add_purity|Adds purity|||
|add_religious_influence|Adds religious influence|||
|add_republican_tradition|Adds republican_tradition|||
|add_righteousness|Adds Righteousness|||
|add_rite_power|Adds rite power|||
|add_sailors|Adds sailors|||
|add_self_control|Adds Self Control|||
|add_stability|Adds stability|||
|add_tribal_cohesion|Adds tribal_cohesion|||
|add_war_exhaustion|Adds WarExhaustion|||
|add_yanantin|Adds yanantin|||
|change_international_organization_modifier_size|Change the strength of a modifier applied to the scope international organization|change_international_organization_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }||
|change_parliament_issue_support|gives (or takes) support for the issue in parliament|||
|end_parliament|End the current parliament session. If set 'yes', pass the issue, if set 'no' then fail the issue instead.|||
|end_vote|Sets the final winning vote for a resolution.|end_vote = { resolution = <resolution> vote = <vote> }||
|finalize_resolution|End the target resolution for the current situation or international organization.||resolution|
|grant_parliament_agenda|Accept the specified target parliament agenda.||parliament_agenda|
|grant_parliament_agenda_for_special_status|Accept the parliament agenda of the target special status type.||special_status|
|international_organization_add_special_status|international organization bestows special status on a country|||
|international_organization_remove_special_status|international organization removes special status from a country|||
|pay_policy_price_effect|executes the policy price effect on the current scope||policy|
|remove_cooldown|Removes a cooldown for a country or international organization.|remove_cooldown = <cooldown_token>||
|remove_country_from_international_organization|removes a country from an international organization||country|
|remove_enemy_from_international_organization|removes a country from an international organization||country|
|remove_international_organization_modifier|Remove a modifier from an international organization|remove_international_organization_modifier = name||
|remove_law_from_international_organization|remove a law from an international organization||law|
|remove_location_from_international_organization|remove a location from an international organization||location|
|remove_policy_from_international_organization|remove a policy from an international organization||policy|
|remove_vote|Removes the vote for a country on a resolution in an international organization or situation.|remove_vote = { voter = <country> resolution = <resolution> }||
|set_army_tradition|Sets army tradition|||
|set_devotion|Sets devotion|||
|set_doom|Sets doom|||
|set_gold|Sets gold|||
|set_government_power|Sets government power|||
|set_harmony|Sets Harmony|||
|set_honor|Sets honor|||
|set_horde_unity|Sets horde_unity|||
|set_inflation|Sets inflation|||
|set_karma|Sets karma|||
|set_leader_country|set the leader country of an international organization||country|
|set_legitimacy|Sets legitimacy|||
|set_manpower|Sets Manpower|||
|set_navy_tradition|Sets navy tradition|||
|set_parliament_active|Set parliament active or not. The issue of the parliament will be removed without triggering any of its effects if set to no.|||
|set_parliament_issue|Set the specified issue as the topic of the parliament.||parliament_issue|
|set_parliament_issue_support|sets base support for the issue when calling a parliament|||
|set_parliament_location|Sets the parliament location. Use immediately before 'set_parliament_active = yes'||location|
|set_parliament_type|Set the specified parliament type for a country||parliament_type|
|set_prestige|Sets prestige|||
|set_purity|Sets purity|||
|set_religious_influence|Sets religious influence|||
|set_republican_tradition|Sets republican_tradition|||
|set_righteousness|Sets Righteousness|||
|set_rite_power|Sets rite power|||
|set_sailors|Sets sailors|||
|set_self_control|Sets Self Control|||
|set_stability|Sets stability|||
|set_target_of_international_organization|Sets the target of an international organization||country|
|set_tribal_cohesion|Sets tribal_cohesion|||
|set_vote|Sets the vote for a country on a resolution in an international organization or situation.|set_vote = { voter = <country> resolution = <resolution> vote = <whatever> [locked = yes/no] }||
|set_war_exhaustion|Sets WarExhaustion|||
|set_yanantin|Sets yanantin|||

### Location scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|add_core|makes the location a core of the target country||country|
|add_location_modifier|add a modifier to a location|add_location_modifier = { modifier = <static_modifier_name> days/months/years=<script_value/int> #negative values are permanent duration (mode = add/extend/replace/add_and_extend/set_to_largest/set_to_largest_and_extend) (size = <script_value/int>) # multiplies the effect of the modifier (desc = <localization_key>) # desc replaces the description of how long the modifier lasts (recalculate_immediately = yes) #forces game to update effects immediately }||
|add_pop|sets up a pop culture/religion/type/literacy/size possible to set.|||
|add_road_to|adds a road from the scope location to the target location.|add_road_to = { target = <target_location> type = <road_type> }||
|add_vfx|Adds VFX effects on the map|||
|change_building_level_in_location|changes building level in location|change_building_level_in_location = { building = <type> value = <change> {owner = country} }||
|change_control|changes control|||
|change_development|changes development|||
|change_disease_presence|Adds a value to the presence of a disease in a location or subunit. Disease must already be present there.|change_disease_presence = { disease = <source_disease> value = <script_value> }||
|change_garrison_size|Changes the garrison size of the target location by the specified value.|||
|change_institution_progress|changes Institution progress in location|change_institution_progress = { type = <institution> value = <change> }||
|change_integration_level|changes the name of a location|||
|change_integration_progress|changes the current integration progress|||
|change_location_controller|change controller of Location to target country||country|
|change_location_modifier_size|Change the strength of a modifier applied to the scope location|change_location_modifier_size = { modifier = <modifier> value = <script math> [recalculate_immediately = yes] }||
|change_location_owner|change owner of Location to target country||country|
|change_location_rank|changes the location_rank of the location (ie, makes it a city, town, rural_settlement etc||location_rank|
|change_maritime_presence_power|Add or remove maritime presence power for the specified country in the current location scope.|change_maritime_presence_power = { country = <country_scope> value = <script_value> }||
|change_max_raw_material_workers|increases rgo size|||
|change_prosperity|changes prosperity|||
|change_raw_material|changes the raw-material produced in a location||goods|
|change_siege_progress|Advances the siege by the given script value|||
|construct_building|starts the construction of the specified building in the location.|construct_building = { building_type = scoped building type cost_multiplier = value cost_multiplier_reason = loc key demand_multiplier = value instant = yes/no owner = country # defaults to location owner payer = country # defaults to building owner }||
|construct_estate_building|starts the construction of the specified building by an estate in the location|construct_estate_building = { building_type = x estate_type = x }||
|construct_location_rank|starts a construction to change the location_rank of the location (ie, makes it a city, town, rural_settlement etc||location_rank|
|construct_rgo_upgrade|starts the construction of an RGO upgrade in the location.|||
|create_army_country_in_location|Creates a new army country in the relevant country and then scopes to the new country||country|
|create_art|creates a piece of art in the current location|create_art = { type = <type> artist = <char> location = <location> quality = <calc> key = name_key (if not, it uses the random generation) date = <date> (if you want another date than current date }|work_of_art|
|create_building_country_in_location|Creates a new building country in the relevant country and then scopes to the new country||country|
|create_country_from_location|Creates a new country with the current location scope as capital and then scopes to the new country||country|
|create_dynasty_from_location|Creates a new dynasty with the desired name|||
|create_navy_country_in_location|Creates a new navy country in the relevant country and then scopes to the new country||country|
|create_num_sub_unit|creates # of the specified subunit|||
|create_num_sub_unit_of_category|creates # of the best subunit of the specified category|||
|create_sub_unit|creates the specified subunit||unit_type|
|create_sub_unit_of_category|creates the best subunit of the specified category||sub_unit_category|
|create_sub_unit_with_owner|spawns a subunit in location|create_sub_unit_with_owner = { type = <type> owner = country origin = location (for generating culture) }||
|destroy_all_buildings_of_type|destroys the specified building in the location||building_type|
|destroy_building|destroys the specified building in the location. Does nothing and is not shown in the tooltip if the target building is indestructible.||building|
|destroy_building_forcefully|destroys the specified building in the location||building|
|discover_location|target country discoves this location||country|
|floodfill_locations|Generates a list of floodfilled locations from adjacencies. Needs a limit specified to avoid floodfilling everything.|||
|remove_core|makes the location no longer a core of the target country||country|
|remove_from_international_organization|remove a location from an international organization||international_organization|
|remove_location_modifier|Remove a modifier from a location|remove_location_modifier = name||
|remove_vfx|Removes VFX effects on the map|||
|rename_location|changes the name of a location|||
|revoke_town_rights_of_type|Revoke town-rights of a type from a location||town_rights_type|
|set_disease_presence|sets the presence of a disease in a location or subunit.|set_disease_presence = { disease = <source_disease_outbreak> value = <script_value> }||
|set_garrison_size|Sets the garrison size of the target location to the specified value.|||
|spawn_disease|Spawns a disease in a location or on a subunit.|spawn_disease = { disease = <disease> value = <script_value> }|disease_outbreak|
|spawn_movement|Spawns a movement in a location|spawn_movement = { movement_definition = <movement_definition> supporters = <script value> }|movement|
|transfer_location_occupation|Transfers occupation of a Location to the target country||country|

### Market scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|add_goods_supply|Adds goods to a market's stockpile.|add_goods_supply = { goods = <goods> amount = <amount> }||
|add_merchant_power|Adds temporary power to a merchant|add_merchant_power = { country = <country> power = value key = localisation months = y }||
|add_temporary_demand|Adds a temporary demand to a market|add_temporary_demand = { type = demand scale = x months = months }||
|destroy_market|destroys the market|||
|relocate_market|moves the market to the target location||location|
|remove_merchant_power|Removes temporary power to a merchant|remove_merchant_power = { country = <country> key = localisation }||
|remove_temporary_demand|Remove a temporary demand in a market||demand|
|sell_goods_from_location|Adds goods to a market's stockpile, selling them from a specific location, and the location's owner country selling them will get the sale value.|sell_goods_from_location = { goods = <goods> amount = <amount> location = <location> }||

### Pop scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|add_pop_satisfaction|change the Satisfaction of a pop|||
|add_pop_size|change the size of a pop|||
|change_pop_allegiance|change rebel allegiance of pop to target Rebel||rebels|
|change_pop_culture|Changes culture for a pop|every_pop = { limit = { NOT = { culture = { is_accepted_in = root } } } change_pop_culture = culture:turkish_culture }|culture|
|change_pop_owner|change owner of pop to target country||country|
|change_pop_religion|Changes religion for a pop|random_pop = { limit = { religion = religion:sunni } change_pop_religion = religion:catholic }|religion|
|change_pop_type|changes pop type of the pop||pop_type|
|remove_pop_allegiance|removed allegienace of a pop|||
|split_pop|Splits a pop and makes changes to it. If both size and fraction are scripted, it will use the largest.|split_pop = { size = <fixed_num> fraction = <percentage_of_size> religion = x type = poptype culture = y location = z }||

### War scope

|Effect|Description|Example|Targets|
|---|---|---|---|
|add_bonus_warscore|adds some bonus war score to the supplied country.|add_bonus_warscore = { country = country scope amount = script value }||

## All effects

Use this table to search for all effects.
**Lua error: Internal error: The interpreter has terminated with signal "24".**

## References

- To update these tables, see Module:Script docs/Effects/Updates
|Documentation|Defines • Effects • Scopes • Scope links • Triggers Colors • Macros • Mean time to happen • Modifier types • On actions • Script value • Variables GUI script • Localization|

|Scripted content|Actions • Disasters • Events • Missions • Modifiers • Scripted gui • Setup • Situations • Customizable localization|

|Scripted types|Advances • Art • Buildings • Bureaucracies • Casus belli • Characters • Concepts • Countries • Culture • Diplomacy • Diseases • Estates • Goods • Institutions • International organizations • Laws • Movements • Peace treaties • Pops • Religion • Subject types • Traits • Units • Wargoals|

|Map|Map • Map modes • Terrain|

|Graphics|3D Models • Interface • Graphical assets • Fonts • Flags|

|Audio|Music • Sound|

|Other|AI • Console commands • Checksum • Mods • Mod compatibility • Mod structure • Troubleshooting|

|Guides|Interface modding guide • Mod translation • Save-game editing • Settlement position modding guide|

|Tools|Arcanum • PDX DeepL • PDX Workshop Manager • Community Mod Toolkit • **Add Your Tool to the Wiki**|
