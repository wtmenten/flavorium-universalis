# Variable

**Source:** https://eu5.paradoxwikis.com/Variable

---

**Variables** are special scope links that can hold values or scopes. Variables are set, removed, and modified by effects. They can be checked with triggers and also used as scopes.

## Variable types

There are three types of variables: "regular", global, and local.

|Variable type|Scoped|Persistent|Event target|
|---|---|---|---|
|"regular"|||`var:`|
|global|||`global_var:`|
|local|||`local_var:`|

### Variable usage

Once a variable has been set, its value can be used in many effects and triggers. Any script where a scope or script value can be used can generally accept a variable as well.

Variables can hold a numerical or boolean value, a game object as a scope, or a localization key. When saving a scope, variables can be used to set scope to that object as well.

Regular variables are saved to a game object and can only be referenced from that object's scope. Global and local variables are saved to no scope and can be referenced anywhere.

Local variables are temporary and are automatically removed at the end of the effect or event chain that created them. Regular and global variables are persistent and are not removed unless specifically scripted to.

### Variable values

The typical way to assign a value to a variable is to use the `set_variable` effect.

```
set_variable = {
  name = my_variable
  value = 1
}
```

Instead of a literal, the set of values mentioned above can also be used (booleans, scopes, script values, and other variables). Accessing the value of a variable, for comparisons or as a literal, can be done using `var:my_variable`.

In addition to static or script values, variables can also get their value from triggers that return a value. For example, to store the number of advances a country has in a variable, one can use

```
set_variable = {
  name = my_variable
  value = num_of_advances_researched
}
```

All triggers that can be used this way are listed below:

|Trigger|Description|Example|Scopes|
|---|---|---|---|
|add_estate_satisfaction_utility|Utility of adding however much estate satisfaction to the country|add_estate_satisfaction_utility(<estate>\|<amount>) or add_estate_satisfaction_utility = { type = <estate type> amount = <amount> value <operator><threshold> }|country|
|add_static_modifier_utility|Checks the AI utility of adding a static modifier to the scoped object|add_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|character, country, location|
|adm|The adm ability of the character||character|
|age_in_days|How old is a character???||character|
|age_in_years|How old is a character???||character|
|ai_issue_voting_bias|gets the AI evaluation score for voting bias from the international organization||none|
|ai_parliament_issue_resolution_vote_bias|gets the AI evaluation score for resolution voting bias from the parliament issue||parliament_issue|
|ai_policy_reason_to_join|Gets the AI evaluation score for joining an IO due to its policies|ai_policy_reason_to_join = { actor = <country scope> international_organization = <international organization scope> value = <script_value> } OR ai_policy_reason_to_join(<country scope>\|<international organization scope>) = <script_value>|policy|
|ai_policy_resolution_keep_bias|Gets the AI evaluation score for keeping the policy in a vote|ai_policy_resolution_keep_bias = { actor = <country scope> international_organization = <international organization scope> value = <script_value> } OR ai_policy_resolution_keep_bias(<country scope>\|<international organization scope>) = <script_value>|policy|
|ai_policy_resolution_propose_bias|gets the AI evaluation score for proposing the policy in a vote||policy|
|ai_policy_resolution_vote_bias|gets the AI evaluation score for resolution voting bias from the policy||policy|
|ai_unlock_unit_score|Returns the score for AI to unlock a unit||country|
|ai_will_do|gets the AI evaluation score of the supplied generic action ofr the supplied country||none|
|annexation_cost|How much does the target country cost for the current country to annex?|annexation_cost = { target = <target country> value = <script_value> } or annexation_cost(<target country>)|country|
|antagonism|is the country's antagonism towards the target greater or equal than the value?|antagonism = { target = X value <operator> Y or value = { min max } }|country|
|area_average_control|Checks the average_control of an area||area|
|area_average_integration|Checks the average_integration of an area||area|
|area_exploration_progress|gets the exploration progress (0..1) for a country in the scope area||area|
|army_maintenance|What is the xx position (0-1) the country has?||country|
|army_size|Checks if a country has a certain army size||country|
|army_size_percentage|Checks if a country has a certain percentage of regiments compared to expected size||country|
|army_tradition|How much army tradition does the country/IO have?||country, international_organization|
|army_tradition_percentage|How high the percentage of the current army tradition compared to the maximum does the country/IO have?||country, international_organization|
|art_progress|The amount of progress an artist has made on a work of art||character|
|art_quality|Checks the quality of the artwork||work_of_art|
|artist_skill|The artist skill of the character||character|
|available_merchant_capacity|gets the market available merchant capacity for a country in the scope market||market|
|average_control_in_home_region|Checks the average control in the home region||country|
|average_country_literacy|Checks if a country has a certain average_literacy||country|
|average_estate_satisfaction|How high is the average estate satisfaction in the country? The crown estate gets ignored here.||country|
|average_location_literacy|Checks if a location has a certain average literacy||location|
|average_satisfaction|Checks if a location has a certain average satisfaction of its pops||location|
|average_special_status_power|Get the average political power of the target special status.|average_special_status_power = { type = <special status> value <operator> <float> } or average_special_status_power(<special status>)|international_organization|
|besieger_strength|Check the total strength of the besiegers for the siege in scope||siege|
|border_distance_to|gets distance between borders of two nations or a location and a nation.|border_distance_to = { country = x value [operator] y } or border_distance_to(country)|country, location|
|building_efficiency|does the location have the specific efficiency of a building||location|
|building_employed_amount|What's the current effective amount of employed workers?||building|
|building_employment_size_amount|What's the max workers amount?||building|
|building_goods_input|Check how much goods the scope building requires.||building|
|building_index|Checks building index (order in which it was built)||building|
|building_level|Check the level of this Building?||building|
|building_levels_under_construction|Check the level of this Building?||building|
|building_manpower_produced|Checks how much manpower the building type produces||building_type|
|building_max_level|Gets the max level for a building||building|
|building_potential_profit|Checks how much profit the building could make if at full worker capacity||building|
|building_profit|Checks building profit||building|
|building_sailors_produced|Checks how many sailors the building type produces||building_type|
|building_type_max_level|Gets the max level for a building type in a location.|building_type_max_level = { building_type = <building type scope> [owner = <country scope>] value <operator> <compare value> }|location|
|cancel_exploration_utility|Utility of an cancelling and exploration to the country|cancel_exploration_utility(<area>) or exploration_utility = { area = <area> value <operator><threshold> }|country|
|cb_creation_progress_against|Checks the progress of the casus belli creation against the target country in percentage.|cb_creation_progress_against = { target = <country scope> value = <script_value> } or cb_creation_progress_against(<country scope>)|country|
|colonial_charter_progress|Progress of a colonial charter|colonial_charter_progress(<province definition>) or colonial_charter_progress = { province_definition = <province definition> value <operator><threshold> }|country|
|colonial_charter_utility|Utility of a colonial charter|colonial_charter_utility(<province definition>\|<source province>) or colonial_charter_utility = { province_definition = <province definition> source = <source province> value <operator><threshold> }|country|
|colonial_charter_value|value of the colonial charter||colonial_charter|
|colonial_maintenance|What is the xx position (0-1) the country has?||country|
|colonial_range|The colonial range of the country||country|
|combat_side_strength|Checks the strength of the combat side in scope||combat_side|
|combined_special_status_power|Get the combined special status power of ALL special statuses in the international organization||international_organization|
|combined_unique_special_status_power|Get the combined special status power of all countries with their highest ranking special status in the international organization||international_organization|
|compare_value|Compare the current value.||value|
|complacency|How much complacency does the country/IO have?||country, international_organization|
|complacency_percentage|How high the percentage of the current complacency compared to the maximum does the country/IO have?||country, international_organization|
|conquer_desire|Gets how much the AI wants to conquer the supplied country|conquer_desire(<target>) or conquer_desire = { target = <country link> value <operator> <amount> }|country|
|conquistador_utility|Utility of a conquistador|conquistador_utility(<area>) or conquistador_utility = { area = <area> value <operator><threshold> }|country|
|country_art_quality|Checks the total art quality in a Country||country|
|country_combined_special_status_power|Get the political power of the country within the target international organization with all of its special statuses combined.|country_combined_special_status_power = { international_organization = <IO> value <operator> <float> } or country_combined_special_status_power(<IO>)|country|
|country_combined_special_status_power_fraction|Get the political power fraction of the country within the target international organization with all of its special statuses combined.|country_combined_special_status_power = { international_organization = <IO> value <operator> <float> } or country_combined_special_status_power(<IO>)|country|
|country_economical_base|Checks the total economical base of a country||country|
|country_estate_loan_size|Checks the size of a loan given by the estates to a country||country|
|country_has_been_member_for_years|Checks if the country has been in the current international organization scope for x years.|country_has_been_member_for_years = { country = <country scope> value = <years> } or country_has_been_member_for_years(country)|international_organization|
|country_highest_rated_special_status_power|Get the political power of the country within the target international organization of its highest prioritized special status.|highest_rated_special_status_power = { international_organization = <IO> value <operator> <float> } or highest_rated_special_status_power(<IO>)|country|
|country_interaction_acceptance|How high is the target country's AI value of accepting the country interaction done by the current country scope? Always return 0 if the target is a player|country_interaction_acceptance = { type = <country interaction> target = <country> value = <script_value> } or country_interaction_acceptance(<country interaction>\|<country>)|country|
|country_loan_capacity|Checks how much more money a country can borrow||country|
|country_rank_level|level of the country rank of a country||country|
|country_rank_level_on_date|level of the country rank of a country on a particular date||country|
|country_strength|Strength of a country, including their troop numbers as well as tax base and manpower||country|
|country_tax_base|Checks the total tax base of a country||country|
|country_total_army_levy_size|Gets the total number of army levies available to the country||country|
|country_total_navy_levy_size|Gets the total number of navy levies available to the country||country|
|court_language_utility|Utility of a court language accorting to Ai||dialect, language|
|court_maintenance|What is the xx position (0-1) the country has?||country|
|create_market_utility|Utility of creating a market|create_market_utility(<location>) or create_market_utility = { location = <location> value <operator><threshold> }|country|
|cultural_influence|How much influence does the culture have?||culture|
|cultural_maintenance|What is the xx position (0-1) the country has?||country|
|cultural_tradition|How much tradition does the culture have?||culture|
|cultural_unity|Checks the fraction of the population sharing the country's primary culture||country|
|culture_group_percentage|Gets the percentage of the population that follow a particular culture group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_group_population_percentage = { culture_group = <culture group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|culture_group_percentage_in_country|The percentage of a specific culture group in the current country||country|
|culture_group_population|Gets the absolute number of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_group_population = { culture_group = <culture group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|culture_group_population_in_country|The number of pops of a specific culture group in the current country||country|
|culture_opinion_impact|Opinion impact of a particular culture on another|culture_opinion_impact(<culture link>) or culture_percentage = { culture = <culture link> value <operator> <amount> }|culture|
|culture_percentage|Gets the percentage of the population that follow a particular culture in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_population_percentage = { culture = <culture> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|culture_percentage_in_area|gets the percentage of the population that follow a particular culture in the area|culture_percentage_in_area = { country = <country> culture = <culture> value <operator> <script_value> }|area|
|culture_percentage_in_country|The percentage of a specific culture in the current country||country|
|culture_population|Gets the absolute number of the population that follow a particular culture in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|culture_population = { culture = <culture> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|culture_population_in_country|The number of pops of a specific culture in the current country||country|
|currency_percentage_towards_limit|Gets currency progress towards specified limit||country, international_organization|
|currency_utility|Utility of an amount of currency to the country|currency_utility(<currency>\|<amount>) or currency_utility = { currency = <currency> amount = <amount> }|country|
|current_month|Compare the current ingame month (1..12)||none|
|current_ruler_term_years|Checks the current ruler term length in years.||country|
|current_tooltip_depth|What is the number of tooltips open right now?||none|
|current_year|Compare the current ingame year||none|
|days_as_rebel|Check how many days the character has been a rebel.||character|
|days_of_service_as_admiral|Check how many days the character has served as an admiral.||character|
|days_of_service_as_general|Check how many days the character has served as a general.||character|
|days_of_service_in_cabinet|Check how many days the character has served in a cabinet.||character|
|days_since_disaster_end|Checks if x days have passed since the end of the disaster. Returns -1 if the disaster has never ended.||disaster|
|days_since_disaster_start|Checks if x days have passed since the start of the disaster. Returns -1 if the disaster has never started.||disaster|
|days_since_situation_end|Checks if x days have passed since the end of the situation. Returns -1 if the situation has never ended.||situation|
|days_since_situation_start|Checks if x days have passed since the start of the situation. Returns -1 if the situation has never started.||situation|
|defensive_alliance_strength|Strength of a defensive alliance, including the nation with all countries giving defensive support and those that can be called in for defensive wars||country|
|dependency_length_days|returns the number of days a country has been in a dependency (overlord/subject) relationship with the target country.|dependency_length_days = { target = <country> value <comparator> <script_value> }|country|
|destroy_market_utility|Utility of destroying a market|destroy_market_utility(<location>) or destroy_market_utility = { location = <location> value <operator><threshold> }|country|
|development|Checks if a location has a certain Development||location|
|devotion|How much devotion does the country/IO have?||country, international_organization|
|devotion_percentage|How high the percentage of the current devotion compared to the maximum does the country/IO have?||country, international_organization|
|dip|The dip ability of the character||character|
|diplomatic_capacity_of_new_relation|Diplomatic capacity that will be used if the country obtains this diplomatic relation||country|
|diplomatic_capacity_without_maintenance|Diplomatic capacity that country would have without paying anything for maintenance||country|
|diplomatic_maintenance|What is the xx position (0-1) the country has?||country|
|diplomatic_range|Is the target country within diplomatic range?||country|
|discount_needed_for_law_change|Checks how much more discount % is needed for Ai to change a law||country|
|disease_country_deaths|Checks the number of deaths from a disease in a country.|disease_country_deaths(<disease>) disease_country_deaths = { target = <disease> value <comparator> <real> }|country|
|disease_outbreak_country_deaths|Checks the number of deaths from an outbreak in a country.|disease_outbreak_country_deaths(<disease_outbreak>) disease_outbreak_country_deaths = { disease_outbreak = <disease_outbreak> value <comparator> <real> }|country|
|disease_outbreak_presence|Checks the presence of a disease in a location or subunit.|disease_outbreak_presence(<disease_outbreak>) or disease_outbreak_presence = { disease_outbreak = <disease_outbreak> value <comparator> <real> }|location, sub_unit|
|disease_outbreak_total_deaths|How many people have been killed by this disease outbreak?||disease_outbreak|
|disease_presence|Checks the presence of a disease in a location or subunit.|disease_presence(<disease>) or disease_presence = { disease = <disease> value <comparator> <real> }|location, sub_unit|
|disease_resistance|Checks the resistance to a disease in a location or subunit.|disease_resistance(<disease>) or disease_resistance = { target = <disease> value <comparator> <real> }|location, sub_unit|
|disease_total_deaths|How many people have been killed by this disease?||disease|
|distance_to|gets distance between locations||location|
|distance_to_area|gets distance between a location and an area||location|
|distance_to_squared|gets distance squared as the crow flies between locations (much quicker than distance_to, useful if you're just comparing)||location|
|doom|How much doom does the country/IO have?||country, international_organization|
|doom_percentage|How high the percentage of the current doom compared to the maximum does the country/IO have?||country, international_organization|
|dynastic_power|Returns the dynastic power of the scope dynasty or country. For countries, check ruler dynasty or heir dynasty if in regency.|dynastic_power = { international_organization = <IO> value <operator> <script_value> } or dynastic_power(<IO>)|country, dynasty|
|effective_skill|Check the skill level of this cabinet||cabinet|
|employment_percentage|Checks if a location has a certain unemployement percentage||location|
|employment_size|Returns the employment size of a building type per building level||building_type|
|employment_system_desire|returns how much the country wants the target employment system.|employment_system_desire = { target = <employment system> value <comparator> <script_value> }|country|
|estate_gold|The gold of an estate||estate|
|estate_loan_interest|Checks the interest of a loan||country|
|estate_max_tax|the current max-tax of an estate in a country|estate_max_tax(<estate_type link>) or estate_max_tax = { estate_type = <estate_type link> value <operator> <amount> }|country|
|estate_opinion|the current opinion that an estate in a country has of another country|estate_opinion(<estate_type link>\|<country>) or estate_opinion = { estate_type = <estate_type link> target = country value <operator> <amount> }|country|
|estate_satisfaction|the current satisfaction of an estate in a country|estate_satisfaction(<estate_type link>) or estate_satisfaction = { estate_type = <estate_type link> value <operator> <amount> }|country|
|estate_tax|The current tax the estate has to pay||estate|
|estate_tax_rate|The current percentage of tax the estate has to pay. Returns 1 if the estate gets fully taxed even if the max possible tax is below 100%||estate|
|estate_taxable_income|The taxable income of an estate||estate|
|expected_army_size|Checks if a country has a certain expected army size||country|
|expected_navy_size|Checks if a country expects to have a certain amount of ships||country|
|experience_percentage|How many percent experience does this unit have???||unit|
|exploration_expected_cost|gets the exploration expected cost for a country in the scope area||area|
|exploration_maintenance|What is the xx position (0-1) the country has?||country|
|exploration_monthly_cost|what is the monthly cost of an exploration?||exploration|
|exploration_monthly_progress|what is the monthly progress of an exploration?||exploration|
|exploration_needed_time|gets the exploration needed time (months) for a country in the scope area||area|
|exploration_progress|what is the progress of an exploration?||exploration|
|exploration_time|what is the total needed progress of an exploration?||exploration|
|exploration_utility|Utility of an exploration to the country|exploration_utility(<area>\|<character>) or exploration_utility = { area = <area> character = <character> value <operator><threshold> }|country|
|favors|How much favors does the country have in the target?|favors = { target = X value <operator> Y or value = { min max } }|country|
|favors_needed_to_annul_relations_with|Gets the number of favours needed to annul relations with the target country diplomatically|"favors_needed_to_annul_relations_with(<target>)" or favors_needed_to_annul_relations_with = { target = <country link> value <operator> <amount> }|country|
|fertility|The fertility of the character||character|
|food_consumption|Amount of consumed food||location|
|food_maintenance|What is the xx position (0-1) the country has?||country|
|food_percentage|How many percent of food does this unit have???||unit|
|food_price|Checks how much the food in the current market costs||market|
|food_production|Amount of food production||location|
|food_value|Check the food value of the goods scope.||goods|
|fort_maintenance|What is the xx position (0-1) the country has?||country|
|garrison_percentage|Checks the garrison percentage of the location in scope||location|
|garrison_strength|Checks the garrison strength of the location in scope||location|
|get_antagonism|how much of an antagonism type does the country have towards another country?||country|
|get_opinion|how much of an opinion type does the country have towards another country?||country|
|get_trust|how much of a trust type does the country have towards another country?||country|
|gold|How much gold does the country/IO have?||country, international_organization|
|gold_percentage|How high the percentage of the current gold compared to the maximum does the country/IO have?||country, international_organization|
|goods_demand_in_market|Checks how much demand exists of a good in the market.|goods_demand_in_market = { goods = <goods> value = <script_value> } or goods_demand_in_market(<goods>)|market|
|goods_output|Check how much goods the scope location produces.||location|
|goods_supply_in_market|Checks how much supply exists of a good in the market.|goods_supply_in_market = { goods = <goods> value = <script_value> } or goods_supply_in_market(<goods>)|market|
|government_power|How much government power does the country/IO have?||country, international_organization|
|government_power_percentage|How high the percentage of the current government power compared to the maximum does the country/IO have?||country, international_organization|
|great_power_ranking|Country's position in the list of great powers||country|
|great_power_score|Checks if a country has a certain Great Power Score||country|
|had_disaster_for_years|Check if the country scope had the specified disaster type for a specific amount of years.|had_disaster_for_years = { disaster_type = <disaster type> years = <years> } or had_disaster_for_years(<disaster type>)|country|
|harmony|How much harmony does the country/IO have?||country, international_organization|
|harmony_percentage|How high the percentage of the current harmony compared to the maximum does the country/IO have?||country, international_organization|
|heathen_population_fraction|Checks the fraction of the population having a different religious group than the country||country|
|heir_candidates_count|Checks amount of heirs in heir selection for country||heir_selection|
|heir_position|Character's position in line for its country's throne||character|
|heir_score|Get the hypothetical heir score of the character for the target country, even if the character in question could not be an heir.||character|
|heir_score_country|Get the hypothetical heir score of the target character for the current country, even if the character in question could not be an heir.||country|
|heir_score_home|Get the hypothetical heir score of the character in the country they currently reside in.||character|
|heretic_population_fraction|Checks the fraction of the population having a different religion in the same group as the country||country|
|higher_temporary_taxes_needed|Checks how much more max tax a country wants||country|
|hire_price|how much would it cost to hire this unit as a merc.|hire_price(<cost multiplier>\|<duration in months>)|unit|
|honor|How much honor does the country/IO have?||country, international_organization|
|honor_percentage|How high the percentage of the current honor compared to the maximum does the country/IO have?||country, international_organization|
|horde_unity|How much horde_unity does the country/IO have?||country, international_organization|
|horde_unity_percentage|How high the percentage of the current horde_unity compared to the maximum does the country/IO have?||country, international_organization|
|implementation_progress_percentage|Checks if the current government reform/avatar/estate privilege /god/policy/law/cabinet action scope has been implemented in percentage.||avatar, cabinet_action, estate_privilege, god, government_reform, law, policy|
|inflation|How much inflation does the country/IO have?||country, international_organization|
|inflation_percentage|How high the percentage of the current inflation compared to the maximum does the country/IO have?||country, international_organization|
|integration_progress|Checks the integration progress of a location||location|
|international_organization_leader_count|Checks how many leaders (defined as 'leaders' in the IO type) are currently present in the current international organization||international_organization|
|international_organization_leader_reign|Checks if the ruler of an international organization has ruled for x years||international_organization|
|international_organization_leader_reign_in_days|Checks if the ruler of an international organization has ruled for x days||international_organization|
|international_organization_lifetime|Checks if the international organization has existed for x years||international_organization|
|international_organization_lifetime_in_days|Checks if the international organization has existed for x days||international_organization|
|international_organization_locations_owned_percentage|The percentage of the locations of an international organization owned by a country||international_organization|
|international_organization_num_locations|Checks if an international organization has a certain amount of owned locations||international_organization|
|international_organization_population|Checks if an international organization has a certain population based on the locations it owns||international_organization|
|intrinsic_disease_resistance|Checks the intrinsic disease resistance in a location (e.g. from buildings)||location|
|is_in_surplus_in_market|Gets the possible trade surplus of the scope goods in the target market.||goods|
|join_organization_ai_desire|Returns the AI desire to join the specified target international organization.|join_organization_ai_desire = { international_organization = <IO scope> value = <script_value> } or join_organization_ai_desire(<IO scope>)|country|
|karma|How much karma does the country/IO have?||country, international_organization|
|karma_percentage|How high the percentage of the current karma compared to the maximum does the country/IO have?||country, international_organization|
|language_percentage_in_country|The percentage of speakers of a specific language in the current country||country|
|language_power|How much power does the language has (percent of best)?||dialect, language|
|leader_special_status_power|Get the special status power of all special statuses with the 'leader' trait||international_organization|
|leader_special_status_power_fraction|Get the fraction of the special status power of all special statuses with the 'leader' trait||international_organization|
|legitimacy|How much legitimacy does the country/IO have?||country, international_organization|
|legitimacy_percentage|How high the percentage of the current legitimacy compared to the maximum does the country/IO have?||country, international_organization|
|liberty_desire|Checks the amount of liberty desire a country has||country|
|list_size|Checks the size of a list|list_size = { name = <list_name> value >= <script_value> }|none|
|liturgical_language_utility|Utility of a liturgical language accorting to Ai||dialect, language|
|loan_amount|Checks the amount of a loan||loan|
|loan_interest|Checks the interest of a loan||loan|
|local_control|Checks if a location has a certain control||location|
|local_cultural_unity|Checks the percentage the dominant-culture has in a location||location|
|local_estate_power|Checks the raw local estate power in location||location|
|local_political_power_fraction|Checks the fraction this location has of the total political power of a country||location|
|local_relative_estate_power|Checks the relative local estate power in location||location|
|local_religious_unity|Checks the percentage the dominant-religion has in a location||location|
|location_art_quality|Checks the total art quality in a location||location|
|location_building_level|Checks if a location has a building type at a certain level (with optional owner)||location|
|location_counter|Checks if the province/province_defintion/area/region / subcontinent/continent/scripted_geography has this amount of location||area, continent, province, province_definition, region, scripted_geography, sub_continent|
|location_maritime_merchant_power|gets the maritime merchant power for a country in the scope location||location|
|location_maritime_presence_power|gets the maritime presence power for a country in the scope location.|location_maritime_presence_power = { country = <country scope> value <operator> <number> }|location|
|location_max_population|Checks if a location has a certain pixel count||location|
|location_net_building_profit|Checks the net profit from buildings in a location||location|
|location_num_holy_sites|Number of holy sites in the location||location|
|location_num_works_of_art|Checks if a location has a certain number of works of art||location|
|location_peace_cost|gets the peace cost for the location according to giver and taker countries|usage in trigger: location_peace_cost = { giver = <country> taker = <country> value <operand> <threshold> #ex: value < 10 } usage in scripted value: location_peace_cost(<giver>\|<taker>)|location|
|location_population_percentage|Checks if a location has a certain percentage of population capacity||location|
|location_privateer_power|gets the maritime privateeer power for a country in the scope location||location|
|location_progress_for_formable|Checks the progress of the country scope to form the specified formable in percentage.|location_progress_for_formable = { formable_country = <formable scope> value = <script_value> } or location_progress_for_formable(<formable scope>)|country|
|location_size|Checks if a location has a certain pixel count||location|
|location_tax_base|Checks the tax-base of a location||location|
|location_unemployed_population_for_building_type|Checks if a location has a certain unemployed population for the supplied building type (with optional owner)||location|
|location_works_of_art_star_rating|Checks if a country has a certain amount of work of arts||location|
|long_term_trigger_currency_utility|Checks the AI utility of adding an amount of a certain trigger every month to the scoped object|long_term_trigger_currency_utility = { trigger = <trigger> size = <size> target = <optional target> value >= <script_value> }|country|
|lowest_prosperity|Find the location in a province with the lowest prosperity||province|
|lowest_war_score|Checks the lowest war score of ongoing wars||country|
|manpower|How much Manpower does the country/IO have?||country, international_organization|
|manpower_percentage|Checks the percentage of manpower a country has compared to its maximum||country|
|market_access|Checks if a location has certain market access||location|
|market_food|Checks how much food is in the market stockpile||market|
|market_food_deficit|Checks how much food is missing in the market||market|
|market_food_percentage|Checks how much food is in the market stockpile percentage wise||market|
|market_food_traded|Checks how much food is traded in the market||market|
|market_max_food|Checks how much food can be stockpiled in the market||market|
|market_monthly_food_balance|Checks what the food balance is in the market||market|
|market_population|Checks how many pops are in the market||market|
|market_possible_goods_trade_surplus|gets the possible trade surplus for the goods in the scope market||market|
|max_control|Checks the max control in a location||location|
|max_countries_with_special_status|gets the max number of countries with a specific special status in an international organization||international_organization|
|max_garrison_strength|Checks the max garrison strength of the location in scope||location|
|max_manpower|Checks if a country has a certain Max manpower||country|
|max_possible_candidates|Maximum number of candidates for the heir selection.i.e. the number of choices the player will have when an election occurs|max_possible_candidates <operator> <amount>|heir_selection|
|max_religious_aspects|Checks the amount of church aspects the religion has||religion|
|max_rgo_workers|Checks if a location has a certain max number of RGO workers||location|
|max_sailors|Checks if a country has a certain Max Sailors||country|
|max_sects|number of sects available per country from the scope religion||religion|
|merchant_capacity|gets the market merchant capacity for a country in the scope market||market|
|merchant_power_in_market|gets the market merchant power for a country in the scope market||market|
|migration_attraction|Checks if a location has a certain migration_attraction||location|
|mil|The mil ability of the character||character|
|military_strength|Checks the total military strength (max manpower, army size, levy power) of a country||country|
|military_tech_level|Checks if a country has a certain level of military tech||country|
|modifier_utility|Checks the AI utility of a modifier||avatar, character, country, god, government_reform, international_organization, location, policy, province, religion, religious_aspect, religious_school, unit|
|modifier_utility_include_locations|Checks the AI utility of a modifier with location checks||avatar, character, country, god, government_reform, international_organization, location, policy, province, religion, religious_aspect, religious_school, unit|
|monthly_balance|Checks the monthly balance of a country||country|
|monthly_conversion|Checks if a location has an potential conversion of X per month||location|
|monthly_cost|Checks the monthly cost of a mercenary||mercenary|
|monthly_income_total|Checks if a country has a certain income||country|
|monthly_income_trade_and_tax|Checks if a country has a certain trade and tax income||country|
|monthly_manpower|Checks if a country has a certain monthly manpower||country|
|monthly_sailors|Checks if a country has a certain monthly Sailors||country|
|monthly_trade_income|Checks if a country has a certain income from trade||country|
|months_between_leader_changes|Checks if a country has a specific reform||international_organization|
|months_left|Checks the months left of loan||loan|
|months_since_last_parliament_called|Checks how many months its been since the country / international organization last called a parliament||country, international_organization|
|months_since_peace|Checks how many months its been since a country was at peace||country|
|months_since_war|Checks how many months its been since a country was at War||country|
|morale_percentage|How many percent morale does this unit have???||unit|
|naval_range|The naval range of the country||country|
|navy_maintenance|What is the xx position (0-1) the country has?||country|
|navy_size|Checks if a country has a certain amount of ships||country|
|navy_size_percentage|Checks if a country has a certain percentage of ships compared to expected size||country|
|navy_tradition|How much navy tradition does the country/IO have?||country, international_organization|
|navy_tradition_percentage|How high the percentage of the current navy tradition compared to the maximum does the country/IO have?||country, international_organization|
|needs_opinion_with|Determines if a country needs X more relations with another nation.|needs_opinion_with = { target = <country> value <comparator> <script_value> }|country|
|num_adult_capable_characters|Checks if a country has a certain amount of adult characters who can do cabinet or military stuff||country|
|num_affected_locations|How many locations are affected?||disease_outbreak|
|num_army_constructions|Check how many army_constructions a location has||location|
|num_artists|Checks if a country has a certain amount of artists||country|
|num_avatars|Checks if a country has a certain amount of avatars||country|
|num_buildings|Checks if a location has a certain amount of buildings||location|
|num_cardinals|Checks if a country has a certain amount of Cardinals||country|
|num_characters|Checks if a country has a certain amount of living characters||country|
|num_civil_constructions|Check how many civil_constructions a location has||location|
|num_colonial_charters|Checks if a country has a certain amount of colonial charters||country|
|num_countries_in_religion|number of countries in the religion||religion|
|num_countries_with_special_status|gets the number of countries with a particular special status in an international organization||international_organization|
|num_embraced_institutions|Checks if a country has a certain number of institutions embraced||country|
|num_explorations|Checks if a country has a certain amount of Explorations||country|
|num_foreign_buildings|Checks if a location has a certain amount of foreign buildings||location|
|num_forts|Checks if a country has a certain amount of forts||country|
|num_known_institutions|Checks if a country knows a certain number of institutions||country|
|num_loans|Checks if a country has a certain amount of loans||country|
|num_locations|Checks if a country has a certain amount of owned locations||country|
|num_locations_owned_or_owned_by_subjects|Checks if a country or its direct subjects has a certain amount of owned locations||country|
|num_locations_owned_or_owned_by_subjects_or_below|Checks if a country, its subjects or its subjects' subjects has a certain amount of owned locations||country|
|num_navy_constructions|Check how many navy_constructions a location has||location|
|num_of_active_parliament_agendas|Check how many parliament agendas are currently available to the country or international organization.||country, international_organization|
|num_of_advances_researched|Checks how many advances a country currently has researched.||country|
|num_of_children|The number of children of the character||character|
|num_of_diplomats|Checks if a country has an amount of diplomats||country|
|num_of_electors|Checks how many electors the international organization has||international_organization|
|num_of_locations_owned_by_io|Checks if a country has an amount of locations owned by certain IO||country|
|num_of_markets_with_merchants|Checks if a country has merchants in the specified amount of markets.||country|
|num_of_non_rural|Checks if a country has an amount of towns and cities||country|
|num_of_non_rural_ports|Checks if a country has an amount of non-rural ports||country|
|num_of_ports|Checks if a country has an amount of ports||country|
|num_of_rebel_characters|Get the amount of characters which support the rebel||rebels|
|num_of_rebel_supporters|Get the amount of countries which support the rebel||rebels|
|num_of_religious_aspects|Gets the total amount of church aspects in the country||country|
|num_of_spouses|The number of spouses of the character||character|
|num_of_trades|Checks if a country has an amount of trades active||country|
|num_of_traits|The number of traits the character has||character|
|num_of_traits_of_category|The number of traits of a specified category the character has.|num_of_trait_by_category(<trait_category>) or num_of_trait_by_category = { type = <trait_category> value <comparator> <integer> }|character|
|num_open_reform_slots|Checks if a country has a certain amount of open government reform slots||country|
|num_owned_foreign_buildings_in_location|The number of foreign buildings in a location owned by a count||location|
|num_possible_privileges|Checks if the scope country or estate has a certain amount of privileges||country, estate|
|num_possible_rivals|Checks if a country has a certain amount of possible rivals||country|
|num_privileges|Checks if the scope country or estate has a certain amount of privileges||country, estate|
|num_province_definitions_in_area|Checks if an area has a certain amount of province definitions||area|
|num_provinces|Checks if a country has a certain amount of provinces||country|
|num_rebels|Checks if a country has a certain amount of Rebels||country|
|num_reforms|Checks if a country has a certain amount of government reforms||country|
|num_regiments|Checks if a country has a certain amount of regiments||country|
|num_relations_above_limit|Amount above relations limit||country|
|num_rivals|Checks if a country has a certain amount of rivals||country|
|num_roads|Check how many roads a location has||location|
|num_subjects|Checks the total number of subjects of a country||country|
|num_subunits|How many sub units does this unit have?||unit|
|num_union_countries|Return the number of countries under any union ruled by the scoped dynasty||dynasty|
|num_unions|Return the number of unions ruled by the scoped dynasty||dynasty|
|num_works_of_art|Checks if a country has a certain number of works of art||country|
|offensive_alliance_strength|Strength of an offensive alliance, including the nation with all countries giving offensive support and those that can be called in for offensive wars||country|
|offer_relation_acceptance|How high is the target country's AI value of accepting the scripted relation offered by the current country scope?|offer_relation_acceptance = { type = <scripted relation type> target = <country> value <operator> <value> } or "offer_relation_acceptance(<scripted relation type>\|<country>)"|country|
|opinion|is the country's opinion of the target greater or equal than the value?|opinion = { target = X value <operator> Y or value = { min max } }|country|
|opinion_difference_between|Get the opinion of the current country scope against the first target country and subtract it with the opinion the current scope has of the second country.|opinion_difference_between = { first = <country> second = <country> value = <script_value> } or opinion_difference_between(<country>\|<country>)|country|
|organization_strength_relative_to_country|Gets the relative strength of the scope organization to the supplied country|organization_strength_relative_to_country(<target>\|<bool exclude_target>) or organization_strength_relative_to_country = { target = <country link> value <operator> <amount> exclude_target = <bool> }|international_organization|
|parliament_issue_chance|The chance an issue will be selected||country, international_organization|
|parliament_issue_support|The current support in parliament for an issue||country, international_organization|
|parliament_type_utility|Utility of a parliament type that can subtract the utility of current parliament modifiers|parliament_type_utility(<type>\|<bool>) or parliament_type_utility = { parliament_type = <type> subtract_current = <bool> value <operator><threshold> }|country|
|payment_contribution|Gets how much the country has to pay for the specified IO and payment type.|payment_contribution = { international_organization = <> payment = <> }|country|
|payment_maintenance|gets the payment maintenance level for a country in an international organization.|payment_maintenance = { international_organization = <> payment = <> }|country|
|peasant_enfranchisment|Checks the level of peasant enfranchisement in a location||location|
|policy_level|Check the defined level of the policy||policy|
|pop_character_chance|How likely are characters to spawn from this pop?||pop|
|pop_literacy|How literate is this pop?||pop|
|pop_satisfaction|How satisfied is this pop?||pop|
|pop_size|How big is this pop?||pop|
|pop_type_percentage_in_country|The percentage of the specific pop type in the current country||country|
|pop_type_population_in_country|The number of the specific pop type in the current country||country|
|population|Checks if the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography has a certain population||area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|population_in_area|gets the amount of population in an area||area|
|possible_military_leaders|Checks if a country has a certain amount of possible military leaders||country|
|power|The power of an estate||estate|
|power_projection|Checks if a country has a power projection||country|
|prestige|How much prestige does the country/IO have?||country, international_organization|
|prestige_percentage|How high the percentage of the current prestige compared to the maximum does the country/IO have?||country, international_organization|
|prev_antagonism_towards_this|Gets the previous scope country's antagonism towards the current scope country||country|
|prev_opinion_of_this|Gets the previous scope country's opinion of the current scope country||country|
|prev_trust_of_this|Gets the previous scope country's trust of the current scope country||country|
|price_in_market|Gets the price of the scoped goods in the supplied market|price_in_market = { market = <market_name> value >= <script_value> }|goods|
|prisoner_strength|gets the total strength of the prisoners in the unit||unit|
|privateer_power|How much power does a privateer has?||privateer|
|privateer_utility|How useful is a privateer here?||area|
|production_method_profit|Checks production method profit||production_method|
|proper_culture_nobles|Checks the proportion of your population that is primary or accepted culture nobles||country|
|prosperity|Checks if a location has a certain prosperity||location|
|province_army_levy_size|Total army levies that can be had from a province||province|
|province_average_control|Checks the average_control of a province||province|
|province_average_development|Checks the average_development of a province||province|
|province_average_integration|Checks the average_integration of a province||province|
|province_cultural_unity|Checks the cultural_unity of a province||province|
|province_food|Checks the food of a province||province|
|province_food_percentage|Checks the food percentage of capacity in a province||province|
|province_max_food|Checks the maximum amount of food the province can have||province|
|province_monthly_food_production|Checks how much food the province produces per month||province|
|province_navy_levy_size|Total navy levies that can be had from a province||province|
|province_population|Checks if a Province has a certain population||province|
|province_possible_institutions|Checks the number of institutions that can be promoted in a province||province|
|province_prosperity|Checks if a Province has a certain level of average prosperity||province|
|province_rebel_progress|Checks if a Province has a certain rebel progress||province|
|province_religious_unity|Checks the religious_unity of a province||province|
|province_satisfaction|Checks if a Province has a certain level of average satisfaction||province|
|province_tax_base|Checks if a Province has a certain total tax base||province|
|proximity|Checks the proximity to owner capital in a location||location|
|purity|How much purity does the country/IO have?||country, international_organization|
|purity_percentage|How high the percentage of the current purity compared to the maximum does the country/IO have?||country, international_organization|
|random_integer|Uniformly random integer between 0 and 2^31-1. It will be the same if evaluated on the same scope and day.||none|
|rank_index|Checks if a location has a Location Rank of a certain index||location|
|raw_material_amount|Check how many locations in the province_defintion/area / region/subcontinent/continent produce the specified raw material.|raw_material_amount = { goods = <goods scope> value = <script_value> } or raw_material_amount(<goods scope>)|area, continent, market, province_definition, region, sub_continent|
|raw_material_occurrence|Check how many locations world wide produce this raw material||goods|
|raw_material_output|Check how much raw material the scope location produces.||location|
|rebel_last_months_progress|Check last month's progress of a rebel||rebels|
|rebel_locations|Get the total amount of locations supporting the rebel||rebels|
|rebel_progress|Check the progress of a rebel||rebels|
|rebel_size|Get the total amount of population supporting the rebel||rebels|
|reform_desire|Checks the reform desire of the religion||religion|
|regular_army_size|Checks if a country has a certain army size of regulars (maximum strength)||country|
|regular_navy_size|Checks if a country has a certain navy size of regular ships||country|
|relative_defensive_alliance_strength|Gets the relative strength of the scope country including defensive alliances to the supplied one|relative_defensive_alliance_strength(<target>) <operator> <script_value> OR relative_defensive_alliance_strength = { target = <country scope> value <operator> <script_value> }|country|
|relative_military_strength|calculates the relative military strength of the scope country to the target.|relative_military_strength = { target = <country scope> value <operator> <script_value> or value = { min max } }|country|
|relative_raw_material_price|Checks the price of a location's raw material in its market as a percentage of the base price of that material||location|
|relative_strength|Gets the relative strength of the scope country to the supplied one|relative_strength(<target>) or relative_strength = { target = <country link> value <operator> <amount> }|country|
|religion_group_percentage|Gets the percentage of the population that follow a particular religion group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_group_population_percentage = { religion_group = <religion group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|religion_group_percentage_in_country|The percentage of a specific religion group in the current country||country|
|religion_group_population|Gets the absolute number of the population that follow a particular religion group in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_group_population = { religion_group = <religion group> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|religion_percentage|Gets the percentage of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_population_percentage = { religion = <religion> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|religion_percentage_in_country|The percentage of a specific religion in the current country||country|
|religion_population|Gets the absolute number of the population that follow a particular religion in the location/province/province_defintion/area / region/subcontinent/continent/scripted_geography|religion_population = { religion = <religion> value <operator> <script_value> }|area, continent, location, province, province_definition, region, scripted_geography, sub_continent|
|religion_population_in_country|The number of pops with a specific religion in the current country||country|
|religious_influence|How much religious influence does the country/IO have?||country, international_organization|
|religious_influence_percentage|How high the percentage of the current religious influence compared to the maximum does the country/IO have?||country, international_organization|
|religious_unity|Checks the fraction of the population sharing the country's religion||country|
|relocate_market_utility|Utility of relocating a market|relocate_market_utility(<location>,<location>) or relocate_market_utility = { location = <location> new_location = <location> value <operator><threshold> }|country|
|remaining_debt|Checks the remaining debt of a loan||loan|
|remaining_parliament_days|Checks how many days are left in the parliament of the country / international organization before it concludes. Returns -1 when there is no parliament active.||country, international_organization|
|remove_static_modifier_utility|Checks the AI utility of removing a static modifier from the scoped object|remove_static_modifier_utility = { modifier = <modifier_name> value >= <script_value> }|character, country, location|
|republican_tradition|How much republican_tradition does the country/IO have?||country, international_organization|
|republican_tradition_percentage|How high the percentage of the current republican_tradition compared to the maximum does the country/IO have?||country, international_organization|
|research_progress|Checks the progress of the current research in the country||country|
|resolution_opinion|Gets the current scope country's opinion of a resolution.|resolution_opinion(<IO>\|<resolution>\|<vote>) <operator> <script_value> OR resolution_opinion = { international_organization = <international organization> resolution = <resolution> vote = <vote scope> value <operator> <script_value> }|country|
|reverse_country_interaction_acceptance|How high is the current country's AI value of accepting the country interaction done by the specified country scope? Always return 0 if the scope is a player|reverse_country_interaction_acceptance = { type = <country interaction> target = <country> value = <script_value> } or reverse_country_interaction_acceptance(<country interaction>\|<country>)|country|
|rgo_workers|Checks if a location has a certain number of RGO workers||location|
|righteousness|How much righteousness does the country/IO have?||country, international_organization|
|righteousness_percentage|How high the percentage of the current righteousness compared to the maximum does the country/IO have?||country, international_organization|
|rite_power|How much rite power does the country/IO have?||country, international_organization|
|rite_power_percentage|How high the percentage of the current rite power compared to the maximum does the country/IO have?||country, international_organization|
|ruler_reign|Checks if the ruler of a country has ruled for x years||country|
|ruler_reign_in_days|Checks if the ruler or regent of a country has ruled for x days||country|
|sailors|How much Sailors does the country/IO have?||country, international_organization|
|sailors_percentage|Checks the percentage of Sailors a country has compared to its maximum||country|
|satisfaction|The satisfaction of an estate||estate|
|self_control|How much self control does the country/IO have?||country, international_organization|
|self_control_percentage|How high the percentage of the current self control compared to the maximum does the country/IO have?||country, international_organization|
|short_term_trigger_currency_utility|Checks the AI utility of adding an amount of a certain trigger to the scoped object|short_term_trigger_currency_utility = { trigger = <trigger> size = <size> target = <optional target> value >= <script_value> }|country|
|slider_minting_value|How much minting is going on (0..1)||country|
|societal_value_progress|Gets progress towards societal value||country|
|special_status_power|Get the political power of the specified country in an organization with that specified special status.|special_status_power = { country = <country> type = <special status> value <operator> <float> } or special_status_power(<country>\|<special status>)|international_organization|
|special_status_power_fraction|Get the political power fraction of the specified country in an organization with that specified special status.|special_status_power_fraction = { country = <country> type = <special status> value <operator> <float> } or special_status_power(<country>\|<special status>)|international_organization|
|spy_network|How much spy-network does the country have in the target?|spy_network = { target = X value <operator> Y or value = { min max } }|country|
|stability|How much Stability does the country/IO have?||country, international_organization|
|stability_percentage|How high the percentage of the current Stability compared to the maximum does the country/IO have?||country, international_organization|
|state_religion_clergy|Checks the proportion of your population that is true faith clergy||country|
|strength_percentage|How many percent strength does this unit have???||unit|
|subject_level|Get the level of the subject type.||subject_type|
|subject_loyalty|Checks a country's subject loyalty||country|
|subject_type_annullment_favours_required|returns the favours needed to annul this relation diplomatically||subject_type|
|subjects_relative_power|Compares to relative power of all subjects combined||country|
|subunit_morale|How many morale does this subunit have???||sub_unit|
|subunit_morale_percentage|How many percent morale does this subunit have???||sub_unit|
|subunit_number|What is the regimental number for this subnunit||sub_unit|
|subunit_strength|How many strength does this subunit have???||sub_unit|
|subunit_strength_percentage|How many percent strength does this subunit have???||sub_unit|
|target_satisfaction|The target satisfaction of an estate||estate|
|this_antagonism_towards_prev|Gets the current scope country's antagonism towards the previous scope country||country|
|this_opinion_of_prev|Gets the current scope country's opinion of the previous scope country||country|
|this_trust_of_prev|Gets the current scope country's trust of the previous scope country||country|
|threat_level_to|Return the threat level the scope country has towards the target country scope.|threat_level_to = { country = <country scope> value = <script_value> } or threat_level_to(<country scope>)|country|
|tithe|Checks the tithe percentage of the religion||religion|
|total_abilities|The total ability of the character||character|
|total_accepted_culture_population|Checks if a country has an acceputed or primary culture population size of the specified value||country|
|total_building_levels|Checks if a location has a certain total amount of building levels||location|
|total_cardinals|Checks the total amount of cardinals of the religion||religion|
|total_control_scaled_population|Checks if a country has value that is population * local_control its in||country|
|total_debt|Checks how much a country has in total debt||country|
|total_development|Gets the total amount of development in the country||country|
|total_dynastic_power|Check the total amount of dynastic power the scoped dynasty or country has. In case of country, the dynasty of the ruler or of the heir in case of regency is taken.||country, dynasty|
|total_effective_goods_production_buildings|Returns the number of effective building levels which produce the specified good.|total_effective_goods_production_buildings = { goods = <goods> value <comparator> <script_value> }|country|
|total_enemies|counts the number of enemies of an international organization||international_organization|
|total_foreign_buildings_levels|Checks the total number of foreign buildings of a country||country|
|total_goods_traded|Check the total amount of goods that went through this market last month||market|
|total_goods_value_traded|Check the total value of goods that went through this market last month||market|
|total_heathen_population|Checks if a country has a heathen population size of the specified value||country|
|total_heretic_population|Checks if a country has a heretic population size of the specified value||country|
|total_locations_owned|counts the number of locations owned by an international organization||international_organization|
|total_members|counts the number of members in an international organization||international_organization|
|total_merchant_capacity|Checks if a country has a certain total merchant capacity||country|
|total_merchant_power|Check the level of this Building?||market|
|total_not_tolerated_culture_population|Checks if a country has an intolerated culture population size of the specified value||country|
|total_payment_contribution|Gets the sum all member countries have to pay for the specified IO and payment type.|total_payment_contribution = { payment = <> }|international_organization|
|total_population|Checks if a country has a certain population||country|
|total_population_in_international_organization|Checks if the country has the defined amount of pops in the target IO.|total_population_in_international_organization = { international_organization = <IO> value <operator> <script_value> } or total_population_in_international_organization(<IO>)|country|
|total_population_in_international_organization_percentage|Checks if the country has the defined amount of pops in the target IO.|total_population_in_international_organization_percentage = { international_organization = <IO> value <operator> <script_value> } or total_population_in_international_organization_percentage(<IO>)|country|
|total_primary_culture_population|Checks if a country has a primary culture population size of the specified value||country|
|total_special_status_power|Get the political power of all countries in an organization with that specified special status.|total_special_status_power = { type = <special status> value <operator> <float> } or total_special_status_power(<special status>)|international_organization|
|total_special_status_power_fraction|Get the percentage political power of the target special status compared to the total amount of political power of all special statuses combined.|special_status_power_fraction = { type = <special status> value <operator> <float> } or special_status_power_fraction(<special status>)|international_organization|
|total_tolerated_culture_population|Checks if a country has a tolerated culture population size of the specified value||country|
|total_true_faith_population|Checks if a country has a true faith population size of the specified value||country|
|total_unique_special_status_power|Get the political power of all countries in an organization with that specified special status.|total_special_status_power = { type = <special status> value <operator> <float> } or total_special_status_power(<special status>)|international_organization|
|trade_buy|What is the current price for the buy of a trade?||trade|
|trade_capacity_usage_percent|How much of the assigned capacity is being used?||trade|
|trade_profit|What is the current profit of a trade?||trade|
|trade_sell|What is the current price for the sell of a trade?||trade|
|trade_volume|How big volume was traded by this trade?||trade|
|tribal_cohesion|How much tribal_cohesion does the country/IO have?||country, international_organization|
|tribal_cohesion_percentage|How high the percentage of the current tribal_cohesion compared to the maximum does the country/IO have?||country, international_organization|
|trust|is the country's trust towards the target greater or equal than the value?|trust = { target = X value <operator> Y or value = { min max } }|country|
|union_length_days|returns the number of days a country has been in a union with the target country.|union_length_days = { target = <country> value <comparator> <script_value> }|country|
|unit_strength|Check the strength of the unit in scope||unit|
|upkeep_maintenance|What is the xx position (0-1) the country has?||country|
|used_cultures_capacity|Checks if a country has a certain cost of cultures accepted & tolerated||country|
|used_diplomatic_capacity|Diplomatic capacity used by the country||country|
|used_fort_limit|How much Fort Limit is currently being used?||country|
|used_fort_limit_percentage|What percentage of our Fort Limit is currently being used?||country|
|used_merchant_capacity|gets the market used merchant capacity for a country in the scope market||market|
|vote_impact_in_resolution|Check how much vote impact the current country scope would make when voting in the target resolution of the target IO.|vote_impact_in_resolution = { international_organization = <IO> resolution = <resolution> value <operator> <real> } or vote_impact_in_resolution(<IO>\|<resolution>)|country|
|vote_percentage_impact_in_resolution|Check how much vote percentage impact the current country scope would make when voting in the target resolution of the target IO.|vote_percentage_impact_in_resolution = { international_organization = <IO> resolution = <resolution> value <operator> <real> } or vote_percentage_impact_in_resolution(<IO>\|<resolution>)|country|
|votes_for_resolution|Checks the number of votes for a particular outcome of a resolution.|votes_for_resolution(<resolution_key>\|<thing>) or votes_for_resolution = { resolution = <resolution_key> outcome = <thing> value <comparator> <real> }|international_organization, situation|
|war_enthusiasm|The war enthusiasm of the current country scope in the target war.|war_enthusiasm = { war = <war scope> value = <script_value> } or war_enthusiasm(<war scope>)|country|
|war_exhaustion|How much WarExhaustion does the country/IO have?||country, international_organization|
|war_exhaustion_percentage|How high the percentage of the current WarExhaustion compared to the maximum does the country/IO have?||country, international_organization|
|war_length|Checks how many months the current war has been going.||war|
|war_length_in_years|Checks how many years the current war has been going.||war|
|war_score_in_war|Check how much war score the current country has in the target war.|war_score_in_war = { war = <war> value <operator> <real> } or "war_score_in_war(<war>)"|country|
|war_score_in_war_whole_side|Check how much war score the war side of the current country has in the target war.|war_score_in_war_whole_side = { war = <war> value <operator> <real> } or "war_score_in_war_whole_side(<war>)"|country|
|war_score_of_country|Check how much war score the target country has in the current war.|war_score_of_country = { country = <country> value <operator> <real> } or war_score_of_country(<country>)|war|
|war_score_of_country_side|Check how much war score the war side of the target country has in the current war.|war_score_of_country_side = { country = <country> value <operator> <real> } or war_score_of_country_side(<country>)|war|
|war_score_versus|Gets the war score of the scope country against the supplied one|war_score_versus(<target>) or war_score_versus = { target = <country link> value <operator> <amount> }|country|
|war_stalling_length|Checks how many months with no action have passed in the current war.||war|
|war_stalling_length_in_years|Checks how many years with no action have passed in the current war.||war|
|winter_power|||location|
|world_art_quality|Checks the total art quality in the world||none|
|world_culture_group_percentage|Gets the percentage of the population that follow a particular culture group in the world|world_culture_group_percentage = { culture_group = <culture_group> value <operator> <script_value> }|none|
|world_culture_group_population|Gets the absolute number of the population that follow a particular culture group in the world|world_culture_group_population = { culture_group = <culture_group> value <operator> <script_value> }|none|
|world_culture_percentage|Gets the percentage of the population that follow a particular culture in the world|world_culture_percentage = { culture = <culture> value <operator> <script_value> }|none|
|world_culture_population|Gets the absolute number of the population that follow a particular culture in the world|world_culture_population = { culture = <culture> value <operator> <script_value> }|none|
|world_religion_group_percentage|Gets the percentage of the population that follow a particular religion group in the world|world_religion_group_percentage = { religion_group = <religion_group> value <operator> <script_value> }|none|
|world_religion_group_population|Gets the absolute number of the population that follow a particular religion group in the world|world_religion_group_population = { religion_group = <religion_group> value <operator> <script_value> }|none|
|world_religion_percentage|Gets the percentage of the population that follow a particular religion in the world|world_religion_percentage = { religion = <religion> value <operator> <script_value> }|none|
|world_religion_population|Gets the absolute number of the population that follow a particular religion in the world|world_religion_population = { religion = <religion> value <operator> <script_value> }|none|
|yanantin|How much yanantin does the country/IO have?||country, international_organization|
|yanantin_percentage|How high the percentage of the current yanantin compared to the maximum does the country/IO have?||country, international_organization|
|yearly_gold|How much gold does the country get per year?||country|
|yearly_manpower|How many Manpower does the country get per year?||country|
|yearly_sailors|How many Sailors does the country get per year?||country|
|yearly_salary|The yearly salary of the character||character|
|years_active|Checks how long a religion has been enabled||religion|
|years_as_rebel|Check how many years the character has been a rebel.||character|
|years_in_international_organization|Checks if the country has been in the current international organization scope for x years.|years_in_international_organization = { country = <country scope> value = <years> } or years_in_international_organization(country)|country|
|years_of_service_as_admiral|Check how many years the character has served as an admiral.||character|
|years_of_service_as_general|Check how many years the character has served as a general.||character|
|years_of_service_in_cabinet|Check how many years the character has served in a cabinet.||character|
|years_since_disaster_end|Checks if x years have passed since the end of the disaster. Returns -1 if the disaster has never ended.||disaster|
|years_since_disaster_start|Checks if x years have passed since the start of the disaster. Returns -1 if the disaster has never started.||disaster|
|years_since_situation_end|Checks if x years have passed since the end of the situation. Returns -1 if the situation has never ended.||situation|
|years_since_situation_start|Checks if x years have passed since the start of the situation. Returns -1 if the situation has never started.||situation|

### Flag and variables

Variables can hold localization keys by setting the value with `flag:loc_key`. This is useful for interface modding and localization as the function `GetFlagName` returns the key's localized string.

The following script snippets illustrate how flag variables work. Given a localization key and string and variable set to that key.

```
foo: "bar"
```

```
set_variable = {
  name = test
  value = flag:foo
}
```

The data function `[Var('test').GetFlagName]` returns the string "bar".

Variables can also be compared for equality against flags, so that `var:test = flag:foo` would return true in the above example.

The variable itself does not contain the localized string, just the key.

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
Other scopes cannot hold variables, but they can be saved to a variable. Variable maps can work around this limitation by using the scope as a key.

## Lists

**Lists** are temporary collections of scopes built during effect execution.

There are two variants, following the same pattern as `save_scope_as` and `save_temporary_scope_as`:

- `add_to_list` — the list persists for the entire top-level effect execution (i.e. across an event's `immediate` and `option` blocks).[1]
- `add_to_temporary_list` — the list only persists within the current block and its children.[2]

### List usage

Lists are built by adding scopes during effect execution and used by iterating over them.

```
# Build a list of neighboring countries at war
every_neighbor_country = {
	limit = { is_at_war = yes }
	add_to_list = warring_neighbors
}

# Later, iterate the list
every_in_list = {
	list = warring_neighbors
	# this = each neighboring country at war
}
```

### List effects

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|add_to_list|Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the (unbroken) event chain|add_to_list = <name_of_list> add_to_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a permanent target to a temporary list, the whole list becomes permanent|none||
|add_to_temporary_list|Adds the current scope to an arbitrarily-named list (or creates the list if not already present) to be referenced later in the same effect|add_to_temporary_list = <name_of_list> add_to_temporary_list = { name = <name_of_list> value = <script_value> } NOTE, if adding a temporary target to a permanent list, the list will stay permanent|none||
|every_in_list|Iterate through all items in list.|every_in_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|ordered_in_list|Iterate through all items in list.|ordered_in_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|random_in_list|Iterate through all items in list.|random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|remove_from_list|Removes the current scope from a named list|remove_from_list = <string>|none||

### List triggers

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|add_to_temporary_list|Saves a temporary target for use during the trigger execution|This is used to build lists in triggers. If used within an any-trigger, placement within the trigger is quite important. The game will iterate through every instance of the any-trigger until it finds a single instance that fulfills the requirements, and then it will stop. In order to add every instance of a scope that fulfills certain conditions, use "count = all" while also placing this "effect" at the very end of the any-trigger (so that every condition is evaluated for every iteration).|none||
|any_in_list|Iterate through all items in list.|any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|is_in_list|Checks if a target in in a list||none||
|list_size|Checks the size of a list|list_size = { name = <list_name> value >= <script_value> }|none|value|

## Variable lists

**Variable lists** are persistent, ordered collections of scopes stored as named lists. Unlike temporary lists, variable lists persist across effect executions and can be modified.[3][4]

### Variable list types

Variable lists follow the same three-type pattern as variables:

|Type|Scoped|Persistent|Effect prefix|Trigger prefix|
|---|---|---|---|---|
|"regular"|||`add_to_variable_list`|`is_target_in_variable_list`|
|global|||`add_to_global_variable_list`|`is_target_in_global_variable_list`|
|local|||`add_to_local_variable_list`|`is_target_in_local_variable_list`|

### Variable list usage

Unlike temporary lists, variable lists persist across effect executions. They are commonly used to track collections of scopes over time, such as which countries have joined a coalition or which provinces have been affected by a disaster.

```
# Track provinces affected by a plague
add_to_variable_list = {
	name = plague_provinces
	target = location:roma
}

# Check if a province is already tracked
is_target_in_variable_list = {
	name = plague_provinces
	target = location:roma     # returns yes if already in the list
}

# Iterate all tracked provinces
every_in_list = {
	variable = plague_provinces
	# this = each province
}
```

### Variable list iterators

Variable lists are iterated using the same iterator effects and triggers as temporary lists, but using the `variable` parameter instead of `list`. For global and local variable lists, the iterator name includes the scope prefix.

|Type|Effect iterators|Trigger iterator|
|---|---|---|
|"regular"|`every_in_list`, `random_in_list`, `ordered_in_list`|`any_in_list`|
|global|`every_in_global_list`, `random_in_global_list`, `ordered_in_global_list`|`any_in_global_list`|
|local|`every_in_local_list`, `random_in_local_list`, `ordered_in_local_list`|`any_in_local_list`|

```
every_in_list = {
	variable = my_list
	# effects run on each item (this), i.e. add_prestige = 5
}
random_in_global_list = {
	variable = my_list
	limit = { ... }          # optional filter, i.e. limit = { is_alive = yes }
	# effects run on one random matching item, i.e. save_scope_as = my_scope
}
ordered_in_local_list = {
	variable = my_list
	position = 0             # specific index (0-based)
	# effects run on the item at that position, i.e. save_scope_as = my_scope
}
any_in_global_list = {       # trigger
	variable = my_list
	# triggers checked against each item, i.e. is_at_war = yes
}
```

### Variable list effects

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|add_to_global_variable_list|Adds the event target to a global variable list for the given duration|add_to_global_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_local_variable_list|Adds the event target to a local variable list for the given duration|add_to_local_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_variable_list|Adds the event target to a variable list for the given duration|add_to_variable_list = { name = <variable_name> target = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|clear_global_variable_list|Empties the list|clear_global_variable_list = variable_name|none||
|clear_local_variable_list|Empties the list|clear_local_variable_list = variable_name|none||
|clear_variable_list|Empties the list|clear_variable_list = variable_name|none||
|every_in_global_list|Iterate through all items in global list.|every_in_global_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_in_list|Iterate through all items in list.|every_in_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|every_in_local_list|Iterate through all items in local list.|every_in_local_list = { limit = { <triggers> } list = name or variable = name <effects> }|none||
|ordered_in_global_list|Iterate through all items in global list.|ordered_in_global_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_in_list|Iterate through all items in list.|ordered_in_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_in_local_list|Iterate through all items in local list.|ordered_in_local_list = { list = name or variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|random_in_global_list|Iterate through all items in global list.|random_in_global_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_in_list|Iterate through all items in list.|random_in_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_in_local_list|Iterate through all items in local list.|random_in_local_list = { list = name or variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|remove_list_global_variable|Removes the target from a global variable list|remove_list_global_variable = { name = <variable_name> target = <event_target> }|none||
|remove_list_local_variable|Removes the target from a local variable list|remove_list_local_variable = { name = <variable_name> target = <event_target> }|none||
|remove_list_variable|Removes the target from a variable list|remove_list_variable = { name = <variable_name> target = <event_target> }|none||
|sort_global_variable_list|Sorts a global_variable list|sort_global_variable_list = { name = <variable_name> order = <script_value> }|none||
|sort_local_variable_list|Sorts a local variable list|sort_local_variable_list = { name = <variable_name> order = <script_value> }|none||
|sort_variable_list|Sorts a variable list|sort_variable_list = { name = <variable_name> order = <script_value> }|none||

### Variable list triggers

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|any_in_global_list|Iterate through all items in global list.|any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_list|Iterate through all items in list.|any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_local_list|Iterate through all items in local list.|any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|global_variable_list_size|Checks the size of a global variable list|global_variable_list_size = { name = <variable_name value >= <script_value> }|none||
|has_global_variable_list|Checks whether the specified global variable list is set|has_global_variable_list = name|none||
|has_local_variable_list|Checks whether the specified local variable list is set|has_local_variable_list = name|none||
|has_variable_list|Checks whether the current scope has the specified variable list set|has_variable_list = name|none||
|is_in_list|Checks if a target in in a list||none||
|is_target_in_global_variable_list|Checks if a target is in a global variable list|is_target_in_global_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_target_in_local_variable_list|Checks if a target is in a local variable list|is_target_in_local_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_target_in_variable_list|Checks if a target is in a variable list|is_target_in_variable_list = { name = <variable_name> target = <event_target> }|none||
|local_variable_list_size|Checks the size of a local variable list|local_variable_list_size = { name = <variable_name> value >= <script_value> }|none||
|variable_list_size|Checks the size of a variable list|variable_list_size = { name = <variable_name> value >= <script_value> }|none||

## Variable maps

**Variable maps** are associative arrays that map relationships between two scopes, where one scope (the key) links to another (the value). [5]

### Variable map types

Variable maps follow the same three-type pattern as variables and variable lists:

|Type|Scoped|Persistent|Effect prefix|Scope link|
|---|---|---|---|---|
|"regular"|||`add_to_variable_map`|`"variable_map(name\|key)"`|
|global|||`add_to_global_variable_map`|`"global_variable_map(name\|key)"`|
|local|||`add_to_local_variable_map`|`"local_variable_map(name\|key)"`|

### Variable map usage

To add an entry, use `add_to_variable_map` with a name, key, and value:

```
add_to_variable_map = {
	name = rival_map         # the map name, a string identifier
	key = c:FRA              # any scope (countries, locations, characters, etc.) or a number (1, 2, 3)
	value = c:ENG            # any scope or number — what the key maps to
}
```

To look up a value by its key, use the variable map scope link:

```
# Scopes to the value associated with c:FRA in rival_map
"variable_map(rival_map|c:FRA)" = {
	# this = c:ENG (the stored value)
	add_prestige = -10
}
```

**Adding a key that already exists does not overwrite the existing entry.** The `add_to_variable_map` effect silently does nothing if the key is already present. To update an entry, the old key must be removed first, then re-added with the new value:

```
# This does NOT update — the existing c:ENG value is kept
add_to_variable_map = {
	name = rival_map
	key = c:FRA              # key already exists in the map
	value = c:SPA            # ignored — the existing value (c:ENG) remains
}

# Correct: remove the key first, then re-add with the new value
remove_from_variable_map = {
	name = rival_map
	key = c:FRA
}
add_to_variable_map = {
	name = rival_map
	key = c:FRA
	value = c:SPA            # now correctly set to c:SPA
}
```

### Variable map iterators

Variable maps can be iterated over their keys using `every_key_in_variable_map` and `ordered_key_in_variable_map` as effects, and `any_key_in_variable_map` as a trigger. Inside the iterator, `this` refers to the current key, and the corresponding value can be accessed using the variable map scope link with `this` as the key argument.

`ordered_key_in_variable_map` defaults to selecting only **one** key (the first by sort order). Use the `max` parameter to iterate over multiple keys.

|Type|Effect iterators|Trigger iterator|
|---|---|---|
|"regular"|`every_key_in_variable_map`, `ordered_key_in_variable_map`|`any_key_in_variable_map`|
|global|`every_key_in_global_variable_map`, `ordered_key_in_global_variable_map`|`any_key_in_global_variable_map`|
|local|`every_key_in_local_variable_map`, `ordered_key_in_local_variable_map`|`any_key_in_local_variable_map`|

```
every_key_in_global_variable_map = {
	variable = my_map
	"global_variable_map(my_map|this)" = {
		# this = the value; prev = the key
	}
}

# ordered defaults to 1 key — use max to iterate more
ordered_key_in_global_variable_map = {
	variable = my_map
	order_by = total_development
	max = 10                 # iterate up to 10 keys; without this, only the first is selected
	"global_variable_map(my_map|this)" = {
		# this = the value; prev = the key
	}
}
```

### Variable map scope link

The value associated with a key in a variable map can be accessed using the `variable_map` scope link. The syntax takes the map name as the first argument and an event target expression for the key as the second argument, separated by `|`. Because of this special syntax, the entire expression must be enclosed in quotation marks.

```
# scopes to the value for the given key
"global_variable_map(my_map|c:ENG)" = {
	# effects run on the value scope, i.e. add_gold = 25
}

# retrieves a numerical value stored in the map i.e.
add_gold = {
	value = "variable_map(my_map|location:krakow)"
}
```

Because the expression is enclosed in quotation marks, scripted effect and scripted trigger arguments (`$arg$`) are not resolved inside it. To pass a dynamic key, save the argument to a local variable first:

```
# Does NOT work — $key$ is not resolved inside quotes
"global_variable_map(my_map|$key$)" = { ... }

# Workaround: save the argument to a local variable
set_local_variable = {
	name = temp_key
	value = $key$            # resolved outside quotes, saved as local_var:temp_key
}
"global_variable_map(my_map|local_var:temp_key)" = { ... }
```

This workaround only applies to the key (second argument). The map name (first argument) is a identifier, not a scope, so it cannot be parameterized through variables or arguments:

```
# Neither of these work
"global_variable_map($my_map$|c:ENG)" = { ... }
"global_variable_map(local_var:map_name|c:ENG)" = { ... }
```

### Variable map effects

|Effect|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|add_to_global_variable_map|Adds the event target to a global variable map for the given duration|add_to_global_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_local_variable_map|Adds the event target to a local variable map for the given duration|add_to_local_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|add_to_variable_map|Adds the event target to a variable map for the given duration|add_to_variable_map = { name = <variable_name> key = <event_target> value = <event_target> days/weeks/months/years = <script_value> (optional) }|none||
|clear_global_variable_map|Empties the map|clear_global_variable_map = variable_name|none||
|clear_local_variable_map|Empties the map|clear_local_variable_map = variable_name|none||
|clear_variable_map|Empties the map|clear_variable_map = variable_name|none||
|every_key_in_global_variable_map|Iterate through all items in global variable map.|every_key_in_global_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|every_key_in_local_variable_map|Iterate through all items in local variable map.|every_key_in_local_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|every_key_in_variable_map|Iterate through all items in variable map.|every_key_in_variable_map = { limit = { <triggers> } variable = name <effects> }|none||
|ordered_key_in_global_variable_map|Iterate through all keys in a global variable map.|ordered_key_in_global_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_key_in_local_variable_map|Iterate through all keys in a local variable map.|ordered_key_in_local_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|ordered_key_in_variable_map|Iterate through all keys in a variable map.|ordered_key_in_variable_map = { variable = name limit = { <triggers> } order_by = script_value position = int min = int max = script_value check_range_bounds = no # If you don't want an error logged if the list is smaller than the min/max <effects> }|none||
|random_key_in_global_variable_map|Iterate through all items in global variable map.|random_key_in_global_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_key_in_local_variable_map|Iterate through all items in local variable map.|random_key_in_local_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|random_key_in_variable_map|Iterate through all items in variable map.|random_key_in_variable_map = { variable = name limit = { <triggers> } (optional) weight = { mtth } <effects> }|none||
|remove_from_global_variable_map|Removes the target key and its value from a global variable map|remove_from_global_variable_map = { name = X key = Y }|none||
|remove_from_local_variable_map|Removes the target key and its value from a local variable map|remove_from_local_variable_map = { name = X key = Y }|none||
|remove_from_variable_map|Removes the target key and its value from a variable map|remove_from_variable_map = { name = X key = Y }|none||

### Variable map triggers

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|any_key_in_global_variable_map|Iterate through all items in global variable map.|any_key_in_global_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_local_variable_map|Iterate through all items in local variable map.|any_key_in_local_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_variable_map|Iterate through all items in variable map.|any_key_in_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|global_variable_map_size|Checks the size of a global variable map|global_variable_map_size = { name = <variable_name value >= <script_value> }|none||
|has_global_variable_map|Checks whether the specified global variable map is set|has_global_variable_map = name|none||
|has_local_variable_map|Checks whether the specified local variable map is set|has_local_variable_map = name|none||
|has_variable_map|Checks whether the current scope has the specified variable map set|has_variable_map = name|none||
|is_key_in_global_variable_map|Checks if a target is a key in a global variable map|is_key_in_global_variable_map = { name = <global_variable_map> target = <key to check> }|none||
|is_key_in_local_variable_map|Checks if a target is a key in a local variable map|is_key_in_local_variable_map = { name = <local_variable_map> target = <key to check> }|none||
|is_key_in_variable_map|Checks if a target is a key in a variable map|is_key_in_variable_map = { name = <variable_map> target = <key to check> }|none||
|is_value_in_global_variable_map|Checks if a target is a value in a global variable map|is_value_in_global_variable_map = { name = <global_variable_map> target = <value to check> }|none||
|is_value_in_local_variable_map|Checks if a target is a value in a local variable map|is_value_in_local_variable_map = { name = <local_variable_map> target = <value to check> }|none||
|is_value_in_variable_map|Checks if a target is a value in a variable map|is_value_in_variable_map = { name = <variable_map> target = <value to check> }|none||
|local_variable_map_size|Checks the size of a local variable map|local_variable_map_size = { name = <variable_name> value >= <script_value> }|none||
|variable_map_size|Checks the size of a variable map|variable_map_size = { name = <variable_name> value >= <script_value> }|none||

### Variable map GUI functions

Variable maps can be accessed in GUI files using the following data functions:

|Function|Description|
|---|---|
|`Scope.GetMapKeys('<name>')`|Returns a datamodel of all keys in the map stored on a scope.|
|`GetGlobalMapKeys('<name>')`|Returns a datamodel of all keys in a global map.|
|`Scope.GetVariableFromVariableMap('<name>', Scope)`|Returns the value for a given key in the map. The second argument is the key, provided as a scope (use `.MakeScope` if needed).|
|`GetVariableFromGlobalVariableMap('<name>', Scope)`|Returns the value for a given key in a global map.|

### Variable map properties

Variable maps have several properties that distinguish them from other data structures:

- **Scope substitution:** Some scopes in the game do not accept variables to be stored on them. Global variable maps can work around this by using the scope as a key and storing associated data as the value.
- **Performance at scale:** Accessing a value by key and checking whether a key exists are relatively fast operations. These benefits become more significant as the data structure grows larger. For systems that operate on many scopes (e.g. a large proportion of countries, locations, or pops), variable maps may offer performance improvements over variable lists.
- **Unordered:** Variable maps are unordered. Regardless of insertion order, iterating through a map produces a fixed, internal order. Sorting is still possible using `ordered_key_in_variable_map`.
- **Any scope as key or value:** Besides game objects (countries, characters, locations, etc.), variable maps can use numerical values, boolean values, and other expressions the game considers scopes as both keys and values.
- **Usable as arrays:** Since integer values can be used as map keys, variable maps can serve as indexed arrays where the key is the position.
```
# Save the top 10 great powers indexed by rank
clear_global_variable_map = great_powers_by_score
set_local_variable = {
	name = increment
	value = 1
}
ordered_great_power = {
	order_by = great_power_score
	max = 10
	add_to_global_variable_map = {
		name = great_powers_by_score
		key = local_var:increment
		value = this
	}
	change_local_variable = {
		name = increment
		add = 1
	}
}

# Access the 3rd great power by score
"global_variable_map(great_powers_by_score|3)" = {
	add_prestige = 25
}
```

## Variable effects

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

## Variable triggers

|Trigger|Description|Example|Scopes|Targets|
|---|---|---|---|---|
|any_in_global_list|Iterate through all items in global list.|any_in_global_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_list|Iterate through all items in list.|any_in_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_in_local_list|Iterate through all items in local list.|any_in_local_list = { list = name / variable = name <count=num/all> / <percent=fixed_point> <triggers> } Use "list" for lists created by add_to_(temporary)_list Use "variable" for lists created by add_to_(global/local)_variable_list|none||
|any_key_in_global_variable_map|Iterate through all items in global variable map.|any_key_in_global_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_local_variable_map|Iterate through all items in local variable map.|any_key_in_local_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|any_key_in_variable_map|Iterate through all items in variable map.|any_key_in_variable_map = { variable = name <count=num/all> / <percent=fixed_point> <triggers> }|none||
|global_variable_list_size|Checks the size of a global variable list|global_variable_list_size = { name = <variable_name value >= <script_value> }|none||
|global_variable_map_size|Checks the size of a global variable map|global_variable_map_size = { name = <variable_name value >= <script_value> }|none||
|has_global_variable|Checks whether the specified global variable is set|has_global_variable = name|none||
|has_global_variable_list|Checks whether the specified global variable list is set|has_global_variable_list = name|none||
|has_global_variable_map|Checks whether the specified global variable map is set|has_global_variable_map = name|none||
|has_local_variable|Checks whether the specified local variable is set|has_local_variable = name|none||
|has_local_variable_list|Checks whether the specified local variable list is set|has_local_variable_list = name|none||
|has_local_variable_map|Checks whether the specified local variable map is set|has_local_variable_map = name|none||
|has_variable|Checks whether the current scope has the specified variable set|has_variable = name|none||
|has_variable_list|Checks whether the current scope has the specified variable list set|has_variable_list = name|none||
|has_variable_map|Checks whether the current scope has the specified variable map set|has_variable_map = name|none||
|is_key_in_global_variable_map|Checks if a target is a key in a global variable map|is_key_in_global_variable_map = { name = <global_variable_map> target = <key to check> }|none||
|is_key_in_local_variable_map|Checks if a target is a key in a local variable map|is_key_in_local_variable_map = { name = <local_variable_map> target = <key to check> }|none||
|is_key_in_variable_map|Checks if a target is a key in a variable map|is_key_in_variable_map = { name = <variable_map> target = <key to check> }|none||
|is_target_in_global_variable_list|Checks if a target is in a global variable list|is_target_in_global_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_target_in_local_variable_list|Checks if a target is in a local variable list|is_target_in_local_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_target_in_variable_list|Checks if a target is in a variable list|is_target_in_variable_list = { name = <variable_name> target = <event_target> }|none||
|is_value_in_global_variable_map|Checks if a target is a value in a global variable map|is_value_in_global_variable_map = { name = <global_variable_map> target = <value to check> }|none||
|is_value_in_local_variable_map|Checks if a target is a value in a local variable map|is_value_in_local_variable_map = { name = <local_variable_map> target = <value to check> }|none||
|is_value_in_variable_map|Checks if a target is a value in a variable map|is_value_in_variable_map = { name = <variable_map> target = <value to check> }|none||
|local_variable_list_size|Checks the size of a local variable list|local_variable_list_size = { name = <variable_name> value >= <script_value> }|none||
|local_variable_map_size|Checks the size of a local variable map|local_variable_map_size = { name = <variable_name> value >= <script_value> }|none||
|variable_list_size|Checks the size of a variable list|variable_list_size = { name = <variable_name> value >= <script_value> }|none||
|variable_map_size|Checks the size of a variable map|variable_map_size = { name = <variable_name> value >= <script_value> }|none||

## References

- ↑ game/in_game/events/character/dynastic.txt (v1.1.10) — uses add_to_list in immediate and iterates in option, thus cross-block list persistence.
- ↑ game/in_game/events/DHE/flavor_BOH.txt (v1.1.10) — uses add_to_temporary_list to build and consume a list within a single option block. This is the only game file use of it, so the difference is assumed to be the same as save_scope_as vs save_temporary_scope_as
- ↑ game/in_game/events/DHE/flavor_chi_treasure_expedition.txt (v1.1.10) — extensive variable list usage.
- ↑ game/in_game/events/wokou_events.txt (v1.1.10) — global variable list usage.
- ↑ Tinto Talks Extra: Modding in 1.1 "Rossbach" — developer diary introducing variable maps.

