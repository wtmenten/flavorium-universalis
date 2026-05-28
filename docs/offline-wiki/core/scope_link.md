# Scope link

**Source:** https://eu5.paradoxwikis.com/Scope_link

---

**Scope links** – often called *event targets* or colloquially just *scopes* – are object, scope, or value references used in Europa Universalis V's game script. Most scope links can be used as target of an effect or trigger when it refers to an appropriate scope, object, or value. Similarly, scope links can be used as scopes or the left side of a value comparison.

Scope links that represent scopes can generally be used in dot chains as for example: `p:xF98DA3.state.owner.capital` which looks at the given province, then chains to that province's state, that state's owning country, and finally to that country's capital state.

## Data scope links

These scope links require additional input, such as a scripted type or specified scope. This generally takes the form of `event_target:data`; some use the format `event_target(data)`, this type must be enclosed in quotation marks, including any dot scoped elements, e.g. `"scope:power_bloc.power_bloc_leader.market.market_number_goods_shortages_with(scope:with_country)"`.

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

## Value scope links

These scope links return a numerical or boolean value. This allows them to be used in comparisons or script values.

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

## Wild card scope links

These scope links refer to a type of scope link, rather than a specifically named scope link. For example, the scope link `compare_value` refers to any simple, inline trigger which checks a numerical value such as `free_arable_land`. Similarly, `named_script_value` refers to the calculated script value by its name.

|Scope link|Description|To scope|
|---|---|---|
|compare_complex_value|A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies)|value|
|compare_date|A comparison trigger that will return its date in the context it is used eg: root.gold|date|
|compare_value|A comparison trigger that will return its value in the context it is used eg: root.gold|value|
|named_script_value|A script value that will calculate and returns its value in the context it is used|color, value|

## Scope links by scope

||Please help improve this article or section by expanding it with: more lists by scope.|

The following tables list scope links by their required scope. Some scope links are repeated as they can be used in multiple scopes. Scope links that can be used in any scope are indicated with `none`.

### None scope/scopeless

|Scope link|Description|To scope|
|---|---|---|
|advance_type|Unknown, add something in code registration|advance_type|
|age|Unknown, add something in code registration|age|
|ai_personality|Unknown, add something in code registration|ai_personality|
|area|Unknown, add something in code registration|area|
|array_define|Name\|Index. Index is 0-based.|value|
|artist_type|Unknown, add something in code registration|artist_type|
|avatar|Unknown, add something in code registration|avatar|
|bias_value|Unknown, add something in code registration|value|
|building_type|Unknown, add something in code registration|building_type|
|bureaucracy_type|Unknown, add something in code registration|bureaucracy_type|
|c|Scope to the specified country TAG|country|
|cabinet_action|The cabinet action a character is performing|cabinet_action|
|casus_belli|Unknown, add something in code registration|casus_belli|
|character|Unknown, add something in code registration|character|
|character_interaction|Unknown, add something in code registration|character_interaction|
|child_education|Unknown, add something in code registration|child_education|
|climate|Unknown, add something in code registration|climate|
|compare_complex_value|A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies)|value|
|compare_date|A comparison trigger that will return its date in the context it is used eg: root.gold|date|
|compare_value|A comparison trigger that will return its value in the context it is used eg: root.gold|value|
|continent|Unknown, add something in code registration|continent|
|country_interaction|Unknown, add something in code registration|country_interaction|
|country_rank|Unknown, add something in code registration|country_rank|
|culture|Unknown, add something in code registration|culture|
|culture_group|Unknown, add something in code registration|culture_group|
|default_price|The default price for a goods|value|
|define|Name|color, date, value|
|demand|Unknown, add something in code registration|demand|
|dialect|Unknown, add something in code registration|dialect|
|disaster_type|Unknown, add something in code registration|disaster_type|
|disease|Unknown, add something in code registration|disease|
|dynasty|Unknown, add something in code registration|dynasty|
|employment_system|Unknown, add something in code registration|employment_system|
|estate_privilege|Unknown, add something in code registration|estate_privilege|
|estate_type|Unknown, add something in code registration|estate_type|
|ethnicity|Unknown, add something in code registration|ethnicity|
|flag|Flag literals eg: flag:the_boss|flag|
|formable_country|Unknown, add something in code registration|formable_country|
|generic_action|Unknown, add something in code registration|generic_action|
|gfx_culture|The graphical culture from a culture scope|graphical_culture|
|global_var|Reference a previous set global variable via its name eg: global_var:important_thing|varies|
|global_variable_map|c:FRA)"|varies|
|god|Unknown, add something in code registration|god|
|goods|Unknown, add something in code registration|goods|
|government_reform|Unknown, add something in code registration|government_reform|
|government_type|Unknown, add something in code registration|government|
|hegemony|Unknown, add something in code registration|hegemony|
|heir_selection|Unknown, add something in code registration|heir_selection|
|holy_site_definition|Unknown, add something in code registration|holy_site_definition|
|holy_site_type|Unknown, add something in code registration|holy_site_type|
|institution|Unknown, add something in code registration|institution|
|international_organization|Unknown, add something in code registration|international_organization|
|international_organization_type|Unknown, add something in code registration|international_organization_type|
|land_ownership_rule|Unknown, add something in code registration|land_ownership_rule|
|language|Unknown, add something in code registration|language|
|language_family|Unknown, add something in code registration|language_family|
|law|Unknown, add something in code registration|law|
|levy_setup|Unknown, add something in code registration|levy_setup|
|local_var|Reference a previous set local variable via its name eg: local_var:person_of_interest|varies|
|local_variable_map|c:FRA)"|varies|
|location|Unknown, add something in code registration|location|
|location_rank|Unknown, add something in code registration|location_rank|
|max_great_powers|Unknown, add something in code registration|value|
|mission|Unknown, add something in code registration|mission|
|mission_task|Unknown, add something in code registration|mission_task|
|movement_definition|Unknown, add something in code registration|movement_definition|
|named_script_value|A script value that will calculate and returns its value in the context it is used|color, value|
|no|Boolean literal for false values|boolean|
|omen|Unknown, add something in code registration|omen|
|parliament_agenda|Unknown, add something in code registration|parliament_agenda|
|parliament_issue|Unknown, add something in code registration|parliament_issue|
|parliament_type|Unknown, add something in code registration|parliament_type|
|payment|Unknown, add something in code registration|payment|
|peace_treaty|Unknown, add something in code registration|peace_treaty|
|policy|Unknown, add something in code registration|policy|
|pop_type|Unknown, add something in code registration|pop_type|
|prev|The previous scope|varies|
|price|Unknown, add something in code registration|price|
|produced_in_world|The amount of goods produced in the world|value|
|production_method|Unknown, add something in code registration|production_method|
|province_definition|Unknown, add something in code registration|province_definition|
|recruitment_method|Unknown, add something in code registration|recruitment_method|
|regency_type|Unknown, add something in code registration|regency_type|
|region|Unknown, add something in code registration|region|
|relation_type|Unknown, add something in code registration|relation_type|
|religion|Unknown, add something in code registration|religion|
|religion_group|Unknown, add something in code registration|group|
|religious_aspect|Unknown, add something in code registration|religious_aspect|
|religious_faction|Unknown, add something in code registration|religious_faction|
|religious_figure|Unknown, add something in code registration|religious_figure|
|religious_focus|Unknown, add something in code registration|religious_focus|
|religious_school|Unknown, add something in code registration|religious_school|
|resolution|Unknown, add something in code registration|resolution|
|resolution_vote|<international organization>\|<resolution>)|vote|
|revolutionary_target|Unknown, add something in code registration|country|
|road_type|Unknown, add something in code registration|road_type|
|root|The head of the current top scope eg: reciever of an event, taker of a decision|varies|
|scope|Reference a previously saved scope via its name eg: scope:target|varies|
|scriptable_hint_definition|Unknown, add something in code registration|scriptable_hint_definition|
|scripted_geography|Unknown, add something in code registration|scripted_geography|
|situation|Unknown, add something in code registration|situation|
|societal_value_type|Unknown, add something in code registration|societal_value_type|
|special_status|Unknown, add something in code registration|special_status|
|sub_continent|Unknown, add something in code registration|sub_continent|
|sub_unit_category|Unknown, add something in code registration|sub_unit_category|
|subject_military_stance|Unknown, add something in code registration|military_stance|
|subject_type|Unknown, add something in code registration|subject_type|
|this|The current scope|varies|
|topography|Unknown, add something in code registration|topography|
|town_rights_type|Unknown, add something in code registration|town_rights_type|
|trait|Unknown, add something in code registration|trait|
|unit_ability|Unknown, add something in code registration|unit_ability|
|unit_formation_preference|Unknown, add something in code registration|unit_formation_preference|
|unit_type|Unknown, add something in code registration|unit_type|
|value|A numeric literal value eg: 1, 5.2, -6|value|
|var|Reference a previous set variable via its name eg: var:mortal_enemy|varies|
|variable_map|c:FRA)"|varies|
|vegetation|Unknown, add something in code registration|vegetation|
|work_of_art|Unknown, add something in code registration|work_of_art|
|work_of_art_type|Unknown, add something in code registration|work_of_art_type|
|yes|Boolean literal for true values|boolean|

### Building scope

|Scope link|Description|To scope|
|---|---|---|
|building_type|Unknown, add something in code registration|building_type|
|estate_type|Unknown, add something in code registration|estate_type|
|linked_pop|Unknown, add something in code registration|pop|
|location|Unknown, add something in code registration|location|
|owner|Unknown, add something in code registration|country|

### Character scope

|Scope link|Description|To scope|
|---|---|---|
|birth_location|Unknown, add something in code registration|location|
|cabinet_action|The cabinet action a character is performing|cabinet_action|
|culture|Unknown, add something in code registration|culture|
|dialect|Unknown, add something in code registration|dialect|
|dynasty|Unknown, add something in code registration|dynasty|
|employer|Employer of the character|country|
|estate_type|Unknown, add something in code registration|estate_type|
|ethnicity|Unknown, add something in code registration|ethnicity|
|exploration|Unknown, add something in code registration|exploration|
|father|Unknown, add something in code registration|character|
|first_spouse|Unknown, add something in code registration|character|
|language|Unknown, add something in code registration|language|
|location|Unknown, add something in code registration|location|
|modifier|Scope to the value of the modifier type of specified key belonging to the current object|boolean, value|
|mother|Unknown, add something in code registration|character|
|owner|Unknown, add something in code registration|country|
|rebel|Unknown, add something in code registration|rebels|
|religion|Unknown, add something in code registration|religion|
|religious_school|Unknown, add something in code registration|religious_school|
|rule_end_date|Unknown, add something in code registration|date|
|unit|Unknown, add something in code registration|unit|

### Country scope

|Scope link|Description|To scope|
|---|---|---|
|active_mission|Unknown, add something in code registration|mission|
|ai_personality|Unknown, add something in code registration|ai_personality|
|autocephalous_patriarchate|Unknown, add something in code registration|international_organization|
|capital|Unknown, add something in code registration|location|
|civil_war|Unknown, add something in code registration|war|
|civil_war_opponent|Unknown, add something in code registration|country|
|consort|Unknown, add something in code registration|character|
|country_color|Unknown, add something in code registration|color|
|country_government_reform_fully_implemented_date|Unknown, add something in code registration|date|
|country_government_reform_implementation_date|Unknown, add something in code registration|date|
|country_rank|Unknown, add something in code registration|country_rank|
|country_rank_on_date|Unknown, add something in code registration|country_rank|
|country_stance|Unknown, add something in code registration|military_stance|
|court_dialect|Unknown, add something in code registration|dialect|
|court_language|Unknown, add something in code registration|language|
|culture|Unknown, add something in code registration|culture|
|current_mission_task|Unknown, add something in code registration|mission_task|
|dominant_culture|Unknown, add something in code registration|culture|
|dominant_dialect|Unknown, add something in code registration|dialect|
|dominant_language|Unknown, add something in code registration|language|
|dominant_religion|Unknown, add something in code registration|religion|
|dominant_upper_class_culture|Unknown, add something in code registration|culture|
|estate|Links to a particular estate. Usage: estate:<estate_type_link> or estate(<estate_type_link>)|estate|
|estate_power|The power of an estate|value|
|estate_satisfaction|The satisfaction of an estate|value|
|estate_target_satisfaction|The target satisfaction of an estate|value|
|estate_tax_base|The base tax of an estate|value|
|estate_tax_percentage|The tax percentage levied on an estate|value|
|government_type|Unknown, add something in code registration|government|
|heir|Unknown, add something in code registration|character|
|known_in_country|The amount of goods known to a speficic Country|value|
|language|Unknown, add something in code registration|language|
|largest_army|The largest army controlled by the country|unit|
|largest_navy|The largest navy controlled by the country|unit|
|last_valid_ruler|Unknown, add something in code registration|character|
|law_policy|gets the policy chosen for a particular law in the scope international organization or country - usage law_policy(<law>)|policy|
|liturgical_dialect|Unknown, add something in code registration|dialect|
|liturgical_language|Unknown, add something in code registration|language|
|low_control_best_tax_base|get the best low control tax base|province|
|marriage_union|Unknown, add something in code registration|international_organization|
|modifier|Scope to the value of the modifier type of specified key belonging to the current object|boolean, value|
|num_estate_privileges|The amount of privileges an estate has|value|
|num_location_rank|Count the amount of owned locations of a specific rank|value|
|num_pop_type_in_country|The amount of pops of a specific type in a country|value|
|num_possible_estate_privileges|The amount of possible privileges an estate can get|value|
|original_capital|Unknown, add something in code registration|location|
|overlord|Unknown, add something in code registration|country|
|parliament_issue|Unknown, add something in code registration|parliament_issue|
|parliament_seat|Unknown, add something in code registration|location|
|parliament_type|Unknown, add something in code registration|parliament_type|
|percentage_pop_type_in_country|The percentage of pops of a specific type in a country|value|
|previous_ruler|Unknown, add something in code registration|character|
|produced_in_country|The amount of goods produced in a specific Country|value|
|province|Unknown, add something in code registration|province|
|regency_type|Unknown, add something in code registration|regency_type|
|regent|Unknown, add something in code registration|character|
|religion|Unknown, add something in code registration|religion|
|religious_school|Unknown, add something in code registration|religious_school|
|ruler|Unknown, add something in code registration|character|
|ruler_or_heir_if_regent|Unknown, add something in code registration|character|
|ruler_or_regent|Unknown, add something in code registration|character|
|societal_value|The value of a societal value of a country|value|
|subject_type|Unknown, add something in code registration|subject_type|
|succession_law|Unknown, add something in code registration|heir_selection|
|top_overlord|Unknown, add something in code registration|country|
|top_overlord_or_this|Unknown, add something in code registration|country|
|total_building_levels_including_construction|The amount of total building levels including construction in a speficic Country|value|
|total_effective_building_levels|The amount of total effective building levels in a speficic Country|value|
|total_sub_unit_count|Checks the amount of a subunit-category that a country has (in regiments/ships)|value|
|total_sub_unit_strength|Checks the total strength of a subunit-category for a unit|value|
|total_sub_unit_type_count|Checks the amount of a subunit-type that a country has (in regiments/ships)|value|
|union|Unknown, add something in code registration|international_organization|
|war_with_country|Gets the current war of the country scope against the specified target country - usage war_with_country(<country>)|war|

### Location scope

|Scope link|Description|To scope|
|---|---|---|
|active_outbreak|gets the active outbreak for a disease in a location or subunit - usage active_outbreak(<disease>)|disease_outbreak|
|area|Unknown, add something in code registration|area|
|building|Unknown, add something in code registration|building|
|cardinal|Unknown, add something in code registration|cardinal|
|combat|Unknown, add something in code registration|combat|
|continent|Unknown, add something in code registration|continent|
|controller|Unknown, add something in code registration|country|
|dominant_culture|Unknown, add something in code registration|culture|
|dominant_dialect|Unknown, add something in code registration|dialect|
|dominant_language|Unknown, add something in code registration|language|
|dominant_religion|Unknown, add something in code registration|religion|
|institution_progress|The progress towards an institution of a location|value|
|last_dynasty_in_location|Unknown, add something in code registration|dynasty|
|location_rank|Unknown, add something in code registration|location_rank|
|market|Unknown, add something in code registration|market|
|modifier|Scope to the value of the modifier type of specified key belonging to the current object|boolean, value|
|num_pop_type|The amount of pops of a specific type at location|value|
|owner|Unknown, add something in code registration|country|
|percentage_pop_type_in_location|The percentage of pops of a specific type in a location|value|
|previous_owner|Unknown, add something in code registration|country|
|province|Unknown, add something in code registration|province|
|province_definition|Unknown, add something in code registration|province_definition|
|raw_material|Unknown, add something in code registration|goods|
|raw_material_location|Unknown, add something in code registration|goods|
|region|Unknown, add something in code registration|region|
|sea_zone|Unknown, add something in code registration|location|
|second_best_market|Unknown, add something in code registration|market|
|secondary_culture|Unknown, add something in code registration|culture|
|secondary_otherwise_primary_culture|Unknown, add something in code registration|culture|
|siege|Unknown, add something in code registration|siege|
|sub_continent|Unknown, add something in code registration|sub_continent|
|top_owner|Unknown, add something in code registration|country|

### Market scope

|Scope link|Description|To scope|
|---|---|---|
|dialect|Unknown, add something in code registration|dialect|
|language|Unknown, add something in code registration|language|
|location|Unknown, add something in code registration|location|
|market_price|The price a goods has in a market|value|
|most_powerful_merchant|Unknown, add something in code registration|country|
|owner|Unknown, add something in code registration|country|
|produced_in_market|The amount of goods produced in a speficic market|value|
|stockpile_in_market|The amount of goods stockpiled in a specific market|value|
|target_price|The target price a goods has in a market|value|
|traded_in_market|The amount of goods traded in a specific market|value|

### Pop scope

|Scope link|Description|To scope|
|---|---|---|
|culture|Unknown, add something in code registration|culture|
|dialect|Unknown, add something in code registration|dialect|
|estate_type|Unknown, add something in code registration|estate_type|
|location|Unknown, add something in code registration|location|
|owner|Unknown, add something in code registration|country|
|pop_type|Unknown, add something in code registration|pop_type|
|rebel|Unknown, add something in code registration|rebels|
|religion|Unknown, add something in code registration|religion|

### War scope

|Scope link|Description|To scope|
|---|---|---|
|attacker_leader|Unknown, add something in code registration|country|
|casus_belli|Unknown, add something in code registration|casus_belli|
|defender_leader|Unknown, add something in code registration|country|
|original_attacker_leader|Unknown, add something in code registration|country|
|original_defender_leader|Returns the country which was the original defender. In cases where the war is started against a subject country, defender_leader would return the overlord while original_defender_leader would return the subject country. Returns the current defender war leader as fallback.|country|
|war_goal_province|Links to the war goal of the war. If no war goal is set or is unrelated to locations (such as superiority) the link returns the capital of the defender war leader|province|

## All scope links

|Scope link|Description|From scope|To scope|
|---|---|---|---|
|active_mission|Unknown, add something in code registration|country|mission|
|active_outbreak|gets the active outbreak for a disease in a location or subunit - usage active_outbreak(<disease>)|location, sub_unit|disease_outbreak|
|active_resolution|gets the active resolution of the type specified in the scope international organization or situation - usage active_resolution(<resolution>)|international_organization, situation|active_resolution|
|advance_age|Unknown, add something in code registration|advance_type|age|
|advance_type|Unknown, add something in code registration|none|advance_type|
|age|Unknown, add something in code registration|none|age|
|ai_personality|Unknown, add something in code registration|country, none|ai_personality|
|area|Unknown, add something in code registration|exploration, location, none, privateer, province, province_definition|area|
|area_exploration|Links to an exploration in the scope area for the suppled country. Usage: area_exploration:<country> or area_exploration(<country>)|area|exploration|
|array_define|Name\|Index. Index is 0-based.|none|value|
|artist_type|Unknown, add something in code registration|none|artist_type|
|attacker_leader|Unknown, add something in code registration|war|country|
|autocephalous_patriarchate|Unknown, add something in code registration|country|international_organization|
|avatar|Unknown, add something in code registration|holy_site, none|avatar|
|bias_value|Unknown, add something in code registration|none|value|
|birth_location|Unknown, add something in code registration|character|location|
|borrower|Unknown, add something in code registration|loan|country|
|building|Unknown, add something in code registration|location|building|
|building_base_cost_in_gold|The Building base price in gold|building_type|value|
|building_type|Unknown, add something in code registration|building, none|building_type|
|bureaucracy_type|Unknown, add something in code registration|bureaucracy, none|bureaucracy_type|
|c|Scope to the specified country TAG|none|country|
|cabinet_action|The cabinet action a character is performing|cabinet, character, none|cabinet_action|
|cabinet_member|Unknown, add something in code registration|cabinet|character|
|capacity_market|Unknown, add something in code registration|trade|market|
|capital|Unknown, add something in code registration|area, country, dynasty, province|location|
|cardinal|Unknown, add something in code registration|location|cardinal|
|cast_vote_in_active_resolution|gets the cast vote in a resolution, returns nothing if the vote isn't explicit - usage cast_vote_in_resolution(<country>)|active_resolution|vote|
|casus_belli|Unknown, add something in code registration|none, war|casus_belli|
|character|Unknown, add something in code registration|none|character|
|character_interaction|Unknown, add something in code registration|none|character_interaction|
|child_education|Unknown, add something in code registration|none|child_education|
|civil_war|Unknown, add something in code registration|country|war|
|civil_war_opponent|Unknown, add something in code registration|country|country|
|climate|Unknown, add something in code registration|none|climate|
|combat|Unknown, add something in code registration|combat_side, location, unit|combat|
|combat_attacker|Unknown, add something in code registration|combat|combat_side|
|combat_defender|Unknown, add something in code registration|combat|combat_side|
|commander|Unknown, add something in code registration|combat_side|country|
|commanding_country|Unknown, add something in code registration|combat_side|country|
|compare_complex_value|A comparison trigger that needs a parsable string parameter that will return its value in the context it is used eg: scope:root.number_of(armies)|none|value|
|compare_date|A comparison trigger that will return its date in the context it is used eg: root.gold|none|date|
|compare_value|A comparison trigger that will return its value in the context it is used eg: root.gold|none|value|
|consort|Unknown, add something in code registration|country|character|
|continent|Unknown, add something in code registration|area, location, none, province, province_definition, region, sub_continent|continent|
|controller|Unknown, add something in code registration|location, sub_unit|country|
|country_color|Unknown, add something in code registration|country|color|
|country_government_reform_fully_implemented_date|Unknown, add something in code registration|country|date|
|country_government_reform_implementation_date|Unknown, add something in code registration|country|date|
|country_interaction|Unknown, add something in code registration|none|country_interaction|
|country_rank|Unknown, add something in code registration|country, none|country_rank|
|country_rank_on_date|Unknown, add something in code registration|country|country_rank|
|country_stance|Unknown, add something in code registration|country|military_stance|
|court_dialect|Unknown, add something in code registration|country|dialect|
|court_language|Unknown, add something in code registration|country|language|
|creator|Unknown, add something in code registration|work_of_art|character|
|culture|Unknown, add something in code registration|character, country, dynasty, mercenary, none, pop, rebels, sub_unit|culture|
|culture_group|Unknown, add something in code registration|none|culture_group|
|current_mission_task|Unknown, add something in code registration|country|mission_task|
|customer|Unknown, add something in code registration|mercenary|country|
|default_price|The default price for a goods|none|value|
|defender_leader|Unknown, add something in code registration|war|country|
|define|Name|none|color, date, value|
|demand|Unknown, add something in code registration|none|demand|
|dialect|Unknown, add something in code registration|character, culture, dynasty, market, none, pop, religion|dialect|
|disaster_type|Unknown, add something in code registration|disaster, none|disaster_type|
|disease|Unknown, add something in code registration|disease_outbreak, none|disease|
|dominant_country|Unknown, add something in code registration|culture|country|
|dominant_culture|Unknown, add something in code registration|country, location, province|culture|
|dominant_dialect|Unknown, add something in code registration|country, location|dialect|
|dominant_language|Unknown, add something in code registration|country, location|language|
|dominant_religion|Unknown, add something in code registration|country, location, province|religion|
|dominant_upper_class_culture|Unknown, add something in code registration|country|culture|
|dynasty|Unknown, add something in code registration|character, none|dynasty|
|dynasty_head|Unknown, add something in code registration|dynasty|character|
|dynasty_home|Unknown, add something in code registration|dynasty|location|
|employer|Employer of the character|character|country|
|employment_system|Unknown, add something in code registration|none|employment_system|
|enemy_side|Unknown, add something in code registration|combat_side|combat_side|
|estate|Links to a particular estate. Usage: estate:<estate_type_link> or estate(<estate_type_link>)|country|estate|
|estate_power|The power of an estate|country|value|
|estate_privilege|Unknown, add something in code registration|none|estate_privilege|
|estate_satisfaction|The satisfaction of an estate|country|value|
|estate_target_satisfaction|The target satisfaction of an estate|country|value|
|estate_tax_base|The base tax of an estate|country, estate|value|
|estate_tax_percentage|The tax percentage levied on an estate|country|value|
|estate_type|Unknown, add something in code registration|building, character, estate, estate_privilege, none, parliament_issue, pop, rebels|estate_type|
|ethnicity|Unknown, add something in code registration|character, none|ethnicity|
|exploration|Unknown, add something in code registration|character|exploration|
|father|Unknown, add something in code registration|character|character|
|first_spouse|Unknown, add something in code registration|character|character|
|flag|Flag literals eg: flag:the_boss|none|flag|
|formable_country|Unknown, add something in code registration|none|formable_country|
|from_market|Unknown, add something in code registration|trade|market|
|generic_action|Unknown, add something in code registration|none|generic_action|
|gfx_culture|The graphical culture from a culture scope|culture, none|graphical_culture|
|global_var|Reference a previous set global variable via its name eg: global_var:important_thing|none|varies|
|global_variable_map|c:FRA)"|none|varies|
|god|Unknown, add something in code registration|avatar, holy_site, none, omen|god|
|goods|Unknown, add something in code registration|none|goods|
|government_reform|Unknown, add something in code registration|none|government_reform|
|government_type|Unknown, add something in code registration|country, none|government|
|group|Unknown, add something in code registration|religion|group|
|hegemony|Unknown, add something in code registration|none|hegemony|
|heir|Unknown, add something in code registration|country|character|
|heir_selection|Unknown, add something in code registration|none|heir_selection|
|holy_site|Unknown, add something in code registration|avatar, god|holy_site|
|holy_site_definition|Unknown, add something in code registration|none|holy_site_definition|
|holy_site_type|Unknown, add something in code registration|none|holy_site_type|
|implementation_price|Unknown, add something in code registration|bureaucracy, bureaucracy_type|price|
|institution|Unknown, add something in code registration|none|institution|
|institution_progress|The progress towards an institution of a location|location|value|
|interaction_target|Unknown, add something in code registration|cabinet|varies|
|international_organization|Unknown, add something in code registration|none|international_organization|
|international_organization_target|Unknown, add something in code registration|international_organization|country|
|international_organization_type|Unknown, add something in code registration|international_organization, none|international_organization_type|
|known_in_country|The amount of goods known to a speficic Country|country|value|
|land_ownership_rule|Unknown, add something in code registration|international_organization, none|land_ownership_rule|
|language|Unknown, add something in code registration|character, country, culture, dialect, dynasty, market, none, religion, sub_unit|language|
|language_family|Unknown, add something in code registration|language, none|language_family|
|largest_army|The largest army controlled by the country|country|unit|
|largest_navy|The largest navy controlled by the country|country|unit|
|last_dynasty_in_location|Unknown, add something in code registration|location|dynasty|
|last_leader_country|Unknown, add something in code registration|international_organization|country|
|last_valid_ruler|Unknown, add something in code registration|country|character|
|law|Unknown, add something in code registration|none, policy|law|
|law_policy|gets the policy chosen for a particular law in the scope international organization or country - usage law_policy(<law>)|country, international_organization|policy|
|leader|Unknown, add something in code registration|exploration, unit|character|
|leader_at_index|Scopes to the leader characters of the IO which are defined in leader = {}. In case of countries instead, their ruler, heir or regent (in that order) gets returned instead. Usage: leader_at_index(<int>|international_organization|character|
|leader_country|Unknown, add something in code registration|international_organization|country|
|leadership_election_resolution|Unknown, add something in code registration|international_organization|resolution|
|leading_unit|Unknown, add something in code registration|combat_side|unit|
|levy_setup|Unknown, add something in code registration|none|levy_setup|
|linked_pop|Unknown, add something in code registration|building|pop|
|liturgical_dialect|Unknown, add something in code registration|country|dialect|
|liturgical_language|Unknown, add something in code registration|country|language|
|local_var|Reference a previous set local variable via its name eg: local_var:person_of_interest|none|varies|
|local_variable_map|c:FRA)"|none|varies|
|location|Unknown, add something in code registration|building, cardinal, character, combat, exploration, holy_site, market, none, pop, siege, town_rights, work_of_art|location|
|location_rank|Unknown, add something in code registration|location, none|location_rank|
|low_control_best_tax_base|get the best low control tax base|country|province|
|market|Unknown, add something in code registration|location|market|
|market_price|The price a goods has in a market|market|value|
|marriage_union|Unknown, add something in code registration|country|international_organization|
|max_great_powers|Unknown, add something in code registration|none|value|
|mercenary_home|Unknown, add something in code registration|mercenary|location|
|mission|Unknown, add something in code registration|none|mission|
|mission_task|Unknown, add something in code registration|none|mission_task|
|modifier|Scope to the value of the modifier type of specified key belonging to the current object|character, country, dynasty, international_organization, location, province, religion, unit|boolean, value|
|most_powerful_merchant|Unknown, add something in code registration|market|country|
|mother|Unknown, add something in code registration|character|character|
|movement_definition|Unknown, add something in code registration|none|movement_definition|
|movement_type|Unknown, add something in code registration|movement|movement_definition|
|name_culture|Unknown, add something in code registration|sub_unit|culture|
|named_script_value|A script value that will calculate and returns its value in the context it is used|none|color, value|
|no|Boolean literal for false values|none|boolean|
|num_estate_privileges|The amount of privileges an estate has|country|value|
|num_location_rank|Count the amount of owned locations of a specific rank|country|value|
|num_pop_type|The amount of pops of a specific type at location|location|value|
|num_pop_type_in_country|The amount of pops of a specific type in a country|country|value|
|num_pop_type_in_province|The amount of pops of a specific type at Province|province|value|
|num_possible_estate_privileges|The amount of possible privileges an estate can get|country|value|
|omen|Unknown, add something in code registration|none|omen|
|origin|Unknown, add something in code registration|disease, disease_outbreak, institution, work_of_art|location|
|original_attacker_leader|Unknown, add something in code registration|war|country|
|original_capital|Unknown, add something in code registration|country|location|
|original_defender_leader|Returns the country which was the original defender. In cases where the war is started against a subject country, defender_leader would return the overlord while original_defender_leader would return the subject country. Returns the current defender war leader as fallback.|war|country|
|original_outbreak|Unknown, add something in code registration|disease|disease_outbreak|
|overlord|Unknown, add something in code registration|country|country|
|owner|Unknown, add something in code registration|building, cabinet, cardinal, character, colonial_charter, disaster, estate, exploration, loan, location, market, mercenary, pop, privateer, province, rebels, sub_unit, trade, unit, work_of_art|country|
|owning_unit|Unknown, add something in code registration|sub_unit|unit|
|parliament_agenda|Unknown, add something in code registration|none|parliament_agenda|
|parliament_issue|Unknown, add something in code registration|country, international_organization, none|parliament_issue|
|parliament_seat|Unknown, add something in code registration|country, international_organization|location|
|parliament_type|Unknown, add something in code registration|country, international_organization, none|parliament_type|
|payment|Unknown, add something in code registration|none|payment|
|peace_treaty|Unknown, add something in code registration|none|peace_treaty|
|percentage_pop_type_in_country|The percentage of pops of a specific type in a country|country|value|
|percentage_pop_type_in_location|The percentage of pops of a specific type in a location|location|value|
|policy|Unknown, add something in code registration|none|policy|
|pop_type|Unknown, add something in code registration|none, pop|pop_type|
|prev|The previous scope|none|varies|
|previous_owner|Unknown, add something in code registration|location|country|
|previous_ruler|Unknown, add something in code registration|country|character|
|price|Unknown, add something in code registration|none, policy|price|
|produced_goods|Unknown, add something in code registration|production_method|goods|
|produced_in_country|The amount of goods produced in a specific Country|country|value|
|produced_in_market|The amount of goods produced in a speficic market|market|value|
|produced_in_world|The amount of goods produced in the world|none|value|
|production_method|Unknown, add something in code registration|none|production_method|
|province|Unknown, add something in code registration|country, location|province|
|province_capital|Unknown, add something in code registration|province|location|
|province_definition|Unknown, add something in code registration|colonial_charter, location, none, province|province_definition|
|raw_material|Unknown, add something in code registration|location|goods|
|raw_material_location|Unknown, add something in code registration|location|goods|
|rebel|Unknown, add something in code registration|character, pop|rebels|
|recruitment_method|Unknown, add something in code registration|none|recruitment_method|
|regency_type|Unknown, add something in code registration|country, none|regency_type|
|regent|Unknown, add something in code registration|country|character|
|region|Unknown, add something in code registration|area, location, none, province, province_definition|region|
|relation_type|Unknown, add something in code registration|none|relation_type|
|religion|Unknown, add something in code registration|character, country, dynasty, mercenary, none, pop, rebels, sub_unit|religion|
|religion_group|Unknown, add something in code registration|none|group|
|religious_aspect|Unknown, add something in code registration|none|religious_aspect|
|religious_faction|Unknown, add something in code registration|none|religious_faction|
|religious_figure|Unknown, add something in code registration|none|religious_figure|
|religious_focus|Unknown, add something in code registration|none|religious_focus|
|religious_head|Unknown, add something in code registration|religion|country|
|religious_school|Unknown, add something in code registration|character, country, none|religious_school|
|removal_price|Unknown, add something in code registration|bureaucracy, bureaucracy_type|price|
|resolution|Unknown, add something in code registration|active_resolution, none|resolution|
|resolution_proposer|Unknown, add something in code registration|active_resolution|country|
|resolution_target|Links to the named parameter (from the select_triggers) in the scope active resolution|active_resolution|varies|
|resolution_vote|<international organization>\|<resolution>)|none|vote|
|revolutionary_target|Unknown, add something in code registration|none|country|
|road_type|Unknown, add something in code registration|none|road_type|
|root|The head of the current top scope eg: reciever of an event, taker of a decision|none|varies|
|rule_end_date|Unknown, add something in code registration|character|date|
|ruler|Unknown, add something in code registration|country|character|
|ruler_or_heir_if_regent|Unknown, add something in code registration|country|character|
|ruler_or_regent|Unknown, add something in code registration|country|character|
|scope|Reference a previously saved scope via its name eg: scope:target|none|varies|
|scriptable_hint_definition|Unknown, add something in code registration|none|scriptable_hint_definition|
|scripted_geography|Unknown, add something in code registration|none|scripted_geography|
|sea_zone|Unknown, add something in code registration|location|location|
|second_best_market|Unknown, add something in code registration|location|market|
|secondary_culture|Unknown, add something in code registration|location|culture|
|secondary_otherwise_primary_culture|Unknown, add something in code registration|location|culture|
|siege|Unknown, add something in code registration|location, unit|siege|
|siege_defender|the siege defender country|siege|country|
|siege_main_attacker|the siege main attacker country|siege|country|
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
|subunit_home|Unknown, add something in code registration|sub_unit|location|
|succession_law|Unknown, add something in code registration|country|heir_selection|
|target_price|The target price a goods has in a market|market|value|
|this|The current scope|none|varies|
|to_market|Unknown, add something in code registration|trade|market|
|top_overlord|Unknown, add something in code registration|country|country|
|top_overlord_or_this|Unknown, add something in code registration|country|country|
|top_owner|Unknown, add something in code registration|location|country|
|topography|Unknown, add something in code registration|none|topography|
|total_building_levels_including_construction|The amount of total building levels including construction in a speficic Country|country|value|
|total_effective_building_levels|The amount of total effective building levels in a speficic Country|country|value|
|total_sub_unit_category_in_unit|Checks the total strength of a subunit-category for a unit|unit|value|
|total_sub_unit_count|Checks the amount of a subunit-category that a country has (in regiments/ships)|country|value|
|total_sub_unit_strength|Checks the total strength of a subunit-category for a unit|country|value|
|total_sub_unit_type_count|Checks the amount of a subunit-type that a country has (in regiments/ships)|country|value|
|total_sub_unit_type_strength|Checks the total strength of a subunit-type for a country|unit|value|
|town_rights_type|Unknown, add something in code registration|none, town_rights|town_rights_type|
|traded_goods|Unknown, add something in code registration|trade|goods|
|traded_in_market|The amount of goods traded in a specific market|market|value|
|trait|Unknown, add something in code registration|none|trait|
|union|Unknown, add something in code registration|country|international_organization|
|unit|Unknown, add something in code registration|character|unit|
|unit_ability|Unknown, add something in code registration|none|unit_ability|
|unit_destination|Unknown, add something in code registration|unit|location|
|unit_formation_preference|Unknown, add something in code registration|none|unit_formation_preference|
|unit_location|Unknown, add something in code registration|unit|location|
|unit_next_location|Unknown, add something in code registration|unit|location|
|unit_type|Unknown, add something in code registration|none|unit_type|
|upgrade_demand|Unknown, add something in code registration|production_method|demand|
|value|A numeric literal value eg: 1, 5.2, -6|none|value|
|var|Reference a previous set variable via its name eg: var:mortal_enemy|none|varies|
|variable_map|c:FRA)"|none|varies|
|vegetation|Unknown, add something in code registration|none|vegetation|
|vote_in_active_resolution|gets the active resolution of the type specified in the scope active resolution - usage vote_in_active_resolution(<country>)|active_resolution|vote|
|war_goal_province|Links to the war goal of the war. If no war goal is set or is unrelated to locations (such as superiority) the link returns the capital of the defender war leader|war|province|
|war_with_country|Gets the current war of the country scope against the specified target country - usage war_with_country(<country>)|country|war|
|work_of_art|Unknown, add something in code registration|none|work_of_art|
|work_of_art_type|Unknown, add something in code registration|none, work_of_art|work_of_art_type|
|yes|Boolean literal for true values|none|boolean|

## References

- To update these tables, see Module:Script docs/Scope links/Updates

