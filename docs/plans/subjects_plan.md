Lets plan out an expansion of the games subject types.

Lets start by looking at the existing game subject definitions and then craft some new flavorful ones of our own. We should include associated advances, government reforms, estate priledges, events and beauraucracies to unlock them. Consider complex chains of interaction to unlock them - like events which mutate existing estate priveleges or laws, and require certain combiniations of laws, priveledges, estate power, religion, religion_group, etc.
some subject types are upgradeable, earlier versions should be unlocked in early ages and are generally less-beneficial and more independent etc.

the existing game subject defines are here: F:\SteamLibrary\steamapps\common\Europa Universalis V\game\in_game\common\subject_types

the game advances are here: F:\SteamLibrary\steamapps\common\Europa Universalis V\game\in_game\common\advances
dont read all of them initially just the template and the core age advances.

look for interesting contry modifiers here: F:\SteamLibrary\steamapps\common\Europa Universalis V\game\main_menu\common\modifier_type_definitions

Currently I'm thinking of a few subject ideas, flesh these out fully and then include more of your own.


### Junior Partner  
junior partners can only be created from non senior partners in your union diplomatically or through treaties with the same conditions as the normal claim throne cb
independent diplomacy fiefdom, can declare war
both always join defensive wars
both can call to offensive wars
annexation_speed = .75, annexation_min_years_before = 50
strength_vs_overlord = -0.3, diplomatic_capacity_cost_scale = 0.2 
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
subject_pays = {
    scaled_gold = 0.2
	scaled_sailors = 0.1
	scaled_manpower = 0.1
    ignore_inflation = yes
}
overlord_modifier = {
    monthly_prestige = 0.1
    cultural_influence_modifier = 0.1
}
subject_modifier = {
    monthly_legitimacy = 0.15
    monthly_stability = 0.2
}

### Lesser Partner
junior partner can upgrade to lesser partner after 50 years
limited diplomacy fiefdom, 
both always join defensive wars
can call to offensive wars
annexation_speed = 2, annexation_min_years_before = 50
strength_vs_overlord = -0.15, diplomatic_capacity_cost_scale = 0.1 
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
overlord_modifier = {
    monthly_prestige = 0.1
    cultural_influence_modifier = 0.1
}
subject_pays = {
    scaled_gold = 0.3
	scaled_sailors = 0.2
	scaled_manpower = 0.2
    ignore_inflation = yes
}
subject_modifier = {
    monthly_legitimacy = 0.15
    monthly_stability = 0.2
}

### Shadow State 
can only be created from existing free states through treaties, not through released provinces.
age of rennaissance advance unlock
independent diplomacy vassal, 
both can call to defensive wars,
overlord can call to offensive wars, 
annexation_speed = 0, 
strength_vs_overlord = -0.1, diplomatic_capacity_cost_scale = 0.2 
subject_pays = {
    scaled_gold = 0.1
    ignore_inflation = yes
}
institution_spread_to_overlord = monthly_institution_spread_mild
institution_spread_to_subject = monthly_institution_spread_mild
overlord_modifier = {
    power_projection = 10
}
subject_modifier = {
    monthly_legitimacy = 0.15
    monthly_stability = 0.2
}

### Client State
can be created through treaty or through province release
independent diplomacy vassal, 
age of discovery advance unlock
both can call to defensive wars,
overlord can call to offensive wars, 
annexation_speed = 0.2, annexation_min_years_before = 50 
strength_vs_overlord = -0.25, diplomatic_capacity_cost_scale = 0.2 
institution_spread_to_overlord = monthly_institution_spread_mild
institution_spread_to_subject = monthly_institution_spread_mild
overlord_modifier = {
    power_projection = 10
    # TODO more
}
subject_modifier = {
    # TODO more
}

### Puppet State
Shadow States can upgrade to Puppet States
Client States can upgrade to Puppet States
age of absolutism advance unlock
limited diplomacy vassal, can declare wars, 
always joins defensive wars, overlord can call to offensive wars, 
annexation_speed = 0.5, annexation_min_years_before = 50
strength_vs_overlord = -0.15, diplomatic_capacity_cost_scale = 0.33 
subject_pays = {
	scaled_gold = 0.2
	scaled_sailors = 0.1
	scaled_manpower = 0.1
	ignore_inflation = yes
}
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
overlord_modifier = {
    power_projection = 20
    # TODO more
}
subject_modifier = {
    monthly_legitimacy = 0.15
    monthly_stability = 0.3
}





### Elite Enclave
limited diplomacy vassal, 
does not come to war,
age of rennaisance advance unlock -> noble estate privledge
shares culture or kindred
strength_vs_overlord = -3, diplomatic_capacity_cost_scale = 0.1 
limited to one province, # if possible otherwise continue to use high negative strength_vs_overlord
limited to one of this type or its upgrades
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
subject_pays = {
	scaled_gold = 0.33
	scaled_sailors = 0.2
	scaled_manpower = 0.2
	ignore_inflation = yes
}
overlord_modifier = {
    monthly_prestige = 0.1
    power_projection = 20
    cultural_influence = 100
    cultural_tradition = 100
    nobles_estate_target_satisfaction = 0.05
}
subject_modifier = {
    # TODO more
}

### Palatinate
Elite Enclave upgrades to Palatinate
age of reformation advance unlock
limited diplomacy vassal, can declare war,
shares culture or kindred
both always join defensive wars,
both can call to offensive wars,
strength_vs_overlord = -3, diplomatic_capacity_cost_scale = 0.1 
limited to one of this type or its upgrades
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
subject_pays = {
	scaled_gold = 0.2
	scaled_sailors = 0.1
	scaled_manpower = 0.1
	ignore_inflation = yes
}
overlord_modifier = {
    monthly_prestige = 0.2
    power_projection = 50
    cultural_influence = 500
    cultural_tradition = 500
    nobles_estate_target_satisfaction = 0.1
}
subject_modifier = {
    # TODO more
}



### Associated Republic

independent diplomacy vassal, 
age of rennaissance advance unlock,
overlord always joins defensive wars,
subject must be republic type,
strength_vs_overlord = -0.15, diplomatic_capacity_cost_scale = 0.33 
institution_spread_to_overlord = monthly_institution_spread_mild
institution_spread_to_subject = monthly_institution_spread_mild
subject_pays = {
	scaled_gold = 0.15
	ignore_inflation = yes
}
overlord_modifier = {
    research_speed = 0.1
    ## TODO more
}
subject_modifier = {
    # TODO more
}

### Trade Company
limited vassal
age of absolutism advance unlock -> law?
shares culture or kindred
overlord always joins defensive wars, subject can be called to defensive wars.
both can call to offensive wars
subject can only be created on non-capital sub-continents
strength_vs_overlord = -0.15, diplomatic_capacity_cost_scale = 0.33 
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
subject_pays = {
	scaled_gold = 0.15
	scaled_sailors = 0.15
	scaled_manpower = 0.15
	ignore_inflation = yes
}
subject_modifier = {
    monthly_legitimacy = 0.12
    monthly_stability = 0.12
    monthly_rebel_growth = -0.012
    cultures_capacity = 2
    cultures_capacity_modifier = .25
}
overlord_modifier = {
    research_speed = 0.1
    ## TODO more
}


### Artists Commune
limited diplomacy fiefdom,
shares culture or kindred
does not join wars,
age of rennaissance advance unlock,
strength_vs_overlord = -4, diplomatic_capacity_cost_scale = 0.1 
limit to one province or use high neg strength_vs_overlord
limited to one subject of type
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
subject_pays = {
	scaled_gold = 0.05
	ignore_inflation = yes
}
subject_modifier = {
    monthly_legitimacy = 0.12
    monthly_stability = 0.12
    monthly_rebel_growth = -0.02
}
overlord_modifier = {
    cultural_influence = 100
    cultural_influence_modifier = 1
    research_speed = 0.2
}

# Scientific College
limited diplomacy vassal
shares culture or kindred
age of reformation advance unlock -> clergy estate priveledge.
vassal must be government_type:theocracy
does not join wars
strength_vs_overlord = -4, diplomatic_capacity_cost_scale = 0.1 
limit to one province or use high neg strength_vs_overlord
limited to one subject of type
institution_spread_to_overlord = monthly_institution_spread_severe
institution_spread_to_subject = monthly_institution_spread_severe
subject_pays = {
	scaled_gold = 0.05
	ignore_inflation = yes
}
subject_modifier = {
    monthly_legitimacy = 0.12
    monthly_stability = 0.12
    monthly_rebel_growth = -0.02
    embrace_institution_cost_modifier = -0.2
    global_institution_growth_modifier = 0.1
    global_disease_resistance = 0.1
}
overlord_modifier = {
    embrace_institution_cost_modifier = -0.2
    global_institution_growth_modifier = 0.1
    research_speed = 0.2
    research_speed_modifier = 0.15
    global_disease_resistance = 0.1
}


## Naval Administration
limited diplomacy fiefdom
shares culture or kindred
age of discovery advance unlock -> burger estate priveledge.
does not join wars
strength_vs_overlord = -4, diplomatic_capacity_cost_scale = 0.1 
limit to one province or use high neg strength_vs_overlord
limited to one subject of type
institution_spread_to_overlord = monthly_institution_spread_mild
institution_spread_to_subject = monthly_institution_spread_severe
subject_pays = {
	scaled_gold = 0.15
	scaled_sailors = 0.3
	scaled_manpower = 0.15
	ignore_inflation = yes
}
overlord_modifier = {
    num_naval_governors = 1
    research_speed = 0.2
}