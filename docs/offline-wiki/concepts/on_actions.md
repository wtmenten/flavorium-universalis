# On actions

**Source:** https://eu5.paradoxwikis.com/On_actions

---

**On actions** are effects called by specific circumstances. Common examples are pulses which happen on a regular period, such as monthly or yearly. Other examples include various game occurrences such as starting or ending a war, gaining a new ruler, or a character dying.

## On action structure

On actions have the following structure with several optional blocks. Most on actions have a specified root scope, some have additional scopes as well.

```
on_action_name = {
	trigger = {			# On_actions can have triggers. If an on_action fires and its trigger returns false, nothing happens
		trigger_conditions = yes
	}

	weight_multiplier = {	# Used to manipulate the weight of this on_action if it is a candidate in a random_on_actions list (see below)
		base = 1
		modifier = {
			add = 1
			trigger_conditions = yes
		}
	}

	events = {		# Events listed in "events" brackets will always fire as long as their trigger evaluates to true
		event_id.1
		delay = { days = 365 }		# A delay will mean that all events listed after it will only be fired after the delay has passed. NOTE: For performance reasons, an event will only successfully fire if it is valid both when the on_action is executed AND once the delay is complete. All firing entries support delays, whether for events or on_actions.
		event_id.2
		delay = { months = { 6 12 } }	# Setting a new delay overrides a previous delay. Delays support random ranges
		event_id.3
	}
	
	random_events = {	# A single event will be picked to fire
		
		chance_to_happen = 25	# A percentage chance determining whether the events involved will be evaluated at all

		chance_of_no_event = { 	# An entry that can be formatted as a script value (and therefore have conditional entries). Separated from "chance_to_happen" for performance reasons. Will only be evaluated if chance_to_happen is true.
			value = 0
			if = {
				limit = { trigger_conditions = yes }
				add = 10
			}
		}

		100 = event_id.1 	# The number is the weight for picking a specific event. The weight is factored by the event's weight_multiplier entry. (If no weight_multiplier is defined for the event, it is 1)
		200 = event_id.2
		100 = 0		# Having a "0" entry means that there is a chance no event fires, even if there are other valid events. Good for making sure that rare events don't always fire just because every other possible event is invalid.
	}

	first_valid = {		# Pick the first event for which the trigger returns true
		event_id.1
		event_id.2
		fallback_event_without_trigger
	}

	on_actions = {	# An on_action can fire other on_actions, following the same rules as with events
		on_action_1
		on_action_2
		on_action_3
	}

	random_on_actions = {	# Same as with events. On_actions are also factored by their weight_multipliers, which defaults to 1
		100 = on_action_1
		200 = on_action_2
		100 = 0
	}

	first_valid_on_action = {
		on_action_1
		on_action_2
	}

	effect = { 	# An on_action can run effects. It can access the same default or saved scopes as the script chain/code functionality it was fired from. Note that it happens concurrently to events triggered by the on_action, NOT before. Effects run here create a separate chain than events the on_action fires, so you can for example not manipulate values in the effect, and then reliably access those in an event that was fired at the same time. Scopes or local variables set in the effect here will not carry over to any event fired by the on_action.
		effects = yes
	}

	fallback = another_on_action 	# on_actions can define a fallback on_action. If no events/on_actions are run by the on_action, the fallback gets called instead. Avoid creating infinite fallback loops, or the game may be prevented from advancing time!
}
```

|Block|Description|
|---|---|
|trigger|Triggers that determine if the on action can fire when called|
|events|List of events that are called when the on action fires|
|random_event|A single valid event is called from the list, selected by weighted random|
|first_valid|The first valid event is called from the list, determined by the triggers of the called events|
|on_actions|List of on actions that are called when the on action fires|
|random_on_actions|A single valid on action is called from the list, selected by weighted random|
|first_valid_on_action|The first valid on action is called from the list, determined by the triggers of the called on_actions|
|effect|Effects that are fired with the on action|
|weight_multiplier|A MTTH block that modifies the weight of the on action for use with a random_on_actions block|
|fallback|A single on action that is called if no effects, events, or on actions are fired by this this on action|

Each block can have any number of `delay` blocks. Any events, on actions, or effects after the delay waits until the delay passes.

On actions can also be called with the effect `trigger_event` as such:

```
trigger_event_(non_)silently = {
		on_action = on_action_name
		days/months/years = X  	# Optional, to delay the firing time
	}
```

### Modding on actions

On actions can easily modded by calling a new scripted on action from a hardcoded on action. Only a new `on_actions` block can be added to existing on actions. Adding other blocks to an existing on action causes errors.

For example, to add new effects to the monthly country pulse, use the following template:

```
monthly_country_pulse = {
	on_actions = {
    	new_on_action #the name should be unique, but does not need to follow any strict pattern
    }
}
new_on_action = {
	effect = {
		newly added effects
	}
}
```

This makes the base game on-action call the modded on-action whenever it fires.

Note: For compatibility with other mods, and as a general good practice, please add a somewhat unique prefix related to your on_action to reduce the chance of two mods having the same one.

### Parallelisation

The events block called by an on_action is parallelised. This means that when the game is evaluating the events block of the on_action, it will do so for multiple scopes simultaneously, at least for as many as there are available threads with which to do so- the more of the scopes which are to be evaluated that can be simultaneously processed, the closer the time to evaluate all of the scopes will be to the time it takes to evaluate just one scope.

A single thread is still used to evaluate the events block for each scope.

#### Practical implications

It is potentially better from a performance standpoint, despite the overhead of constructing and calling a separate event, to use an event to apply effects to many scopes at the same time, rather than using the effects block of the same on_action.

Additionally, scopes affected by the same event from the same on_action block may be so affected in an arbitrary sequence- if it is desirable that one scope's event be evaluated or occur after another, the the earlier event shall need to be called by the later, or be called after the other in an ordered list effect. In either case the process calling the events will not benefit from parallelism.

## List of on actions

The given scope is `root` unless otherwise indicated

|Name|Given scope|Description|Other Notes|
|---|---|---|---|
|biyearly_country_pulse|country|Bi-yearly pulse is primarily for religious flavor events|once every two years|
|colonial_charter_monthly_pulse|root = country scope:target = colonial_charter|||
|country_pulse_for_high_infamy|country|||
|earthquake_location_pulse|location|checks one random location each month.. yay.||
|four_yearly_country_pulse|country|once every four years||
|government_flavor_pulse|country|||
|in_battle|character|every tick while a character is the supreme commander of a battle.||
|in_regency_yearly_pulse|country|yearly while has regency||
|monthly_country_pulse|country|||
|on_accepted_call_to_arms|scope:actor = caller scope:recipient = callee scope:war = war|||
|on_annex|root = country doing the annexing scope:target = country being annexed|fired before the annexation happens||
|on_annexation_cancel|root = country doing the annexing scope:target = country being annexed|||
|on_annexation_start|root = country doing the annexing scope:target = country being annexed|||
|on_annexed|root = country doing the annexing scope:target = country being annexed|fired after the annexation has happened||
|on_annexing_subject_monthly_pulse|root = overlord scope:target = subject|||
|on_bankruptcy|country|||
|on_battle_lost|root = actor scope:actor = winning "unit" scope:target = losing "unit" scope:killed_land_units -> Num soldiers killed in land battle scope:killed_navy_units -> Num ships destroyed in navy battle scope:lost_land_units -> Num soldiers lost in land battle scope:lost_navy_units -> Num ships lost in navy battle scope:war_score -> Num war score the loser loses from battle|Scopes after target are float values||
|on_battle_lost_character|character|||
|on_battle_won|root = actor scope:actor = winning "unit" scope:target = losing "unit" scope:killed_land_units -> Num soldiers killed in land battle scope:killed_navy_units -> Num ships destroyed in navy battle scope:lost_land_units -> Num soldiers lost in land battle scope:lost_navy_units -> Num ships lost in navy battle scope:war_score -> Num war score the loser loses from battle|Scopes after target are float values||
|on_battle_won_character|character|||
|on_become_revolution_target|country|||
|on_becoming_free|root = country scope:overlord = former overlord|||
|on_cabinet_assigned|root = country scope:target = character who got assigned to the cabinet|||
|on_cabinet_removed|root = country scope:target = character who got removed from the cabinet|Is called BEFORE on_cabinet_assigned if you replace a cabinet character with a new one|Is NOT fired when a character in the cabinet dies|
|on_capital_moved|root = country scope:old_capital = old capital location scope:new_capital = new capital location|||
|on_character_birth|root = country scope:character = newborn|||
|on_character_created|character|only from create_character effect||
|on_character_death|root = country scope:target = character who dies|||
|on_character_divorce|root = primary character who divorces scope:target = secondary character who gets divorced|||
|on_character_estate_change|character|||
|on_character_marriage|root = primary character who marries scope:target = secondary character who gets married|NOTE: if you get confused why the wrong character gets the effects applied, check in which scope marry_character is used.||
|on_character_moved_country|root = character scope:target = new country scope:owner = old country|||
|on_civil_war_annex|root = country doing the annexing scope:target = country being annexed|fired before the annexation happens||
|on_civil_war_annexed|root = country doing the annexing scope:target = country being annexed|fired after the annexation has happened||
|on_civil_war_lost|root and scope:winner = winner scope:loser = loser|||
|on_civil_war_start|root = original country which gets targeted by the civil war scope:target = rebel country which declares the war scope:war = the civil war scope:rebel is the rebel|||
|on_civil_war_won|root and scope:winner = winner scope:loser = loser|||
|on_colonial_charter_failed|root = country scope:target = province_definition scope:attacker = the other country|||
|on_colonial_charter_finished|root = country scope:target = province|||
|on_command_gained|root = character scope:unit = unit|||
|on_command_lost|root = character scope:unit = unit|||
|on_country_rank_change|country|||
|on_dependency_gained|root = country scope:overlord = new overlord|||
|on_diplomatic_annex|root = country doing the annexing scope:target = country being annexed|fired before the annexation happens||
|on_diplomatic_annexed|root = country doing the annexing scope:target = country being annexed|fired after the annexation has happened||
|on_election|country|||
|on_embrace_revolution|country|||
|on_ending_war|root = country (after winning and losing, for both) scope:winner = country scope:loser = country scope:war = war|||
|on_exploration_monthly_pulse|exploration|||
|on_exploration_success|root = country scope:target = area scope:actor = character|||
|on_gain_great_power_status|country|||
|on_game_start|none||This runs before country selection, thus triggers like `is_ai` will not work as no player country has been selected yet. You can add a delay like so:on_game_start = { on_actions = { delay = { days = 1 } your_on_action } }to run your action after the first-day tick, so that this runs after nation selection has already occurred.|
|on_gift_sent|root & scope:actor = sender scope:recipient = receiver scope:target = amount of gold sent|||
|on_government_type_change|root = country scope:from = old type scope:to = new type|||
|on_great_battle_lost|root = actor scope:actor = winning "unit" scope:target = losing "unit" scope:killed_land_units -> Num soldiers killed in land battle scope:killed_navy_units -> Num ships destroyed in navy battle scope:lost_land_units -> Num soldiers lost in land battle scope:lost_navy_units -> Num ships lost in navy battle scope:war_score -> Num war score the loser loses from battle|Scopes after target are float values||
|on_great_battle_won|root = actor scope:actor = winning "unit" scope:target = losing "unit" scope:killed_land_units -> Num soldiers killed in land battle scope:killed_navy_units -> Num ships destroyed in navy battle scope:lost_land_units -> Num soldiers lost in land battle scope:lost_navy_units -> Num ships lost in navy battle scope:war_score -> Num war score the loser loses from battle|Scopes after target are float values||
|on_heir_selection_changed|root = country scope:old_heir_selection scope:heir_selection|||
|on_institution_embraced|root = country scope:target = institution|||
|on_insult|root & scope:actor = sender scope:recipient = receiver|||
|on_integrated_in_union_removal|none|||
|on_international_organization_changed_leader|root = new_ruler scope:target = IO scope:old_ruler = previous leader|||
|on_international_organization_creation|root = int org scope:actor = creator scope:target = target|||
|on_international_organization_disbanded|country|sent to each country that's a member of an IO when it's disbanded||
|on_international_organization_disbanding|root = int org actor = instigator|sent just before an IO disbands||
|on_international_organization_parliament_agenda_accepted|international_organization|||
|on_international_organization_policy_changed|international_organization|||
|on_io_parliament_failed|root = io scope:target = parliament issue scope:location = parliament seat location|||
|on_io_parliament_passed|root = io scope:target = parliament issue scope:location = parliament seat location|||
|on_io_parliament_started|root = io scope:location = parliament seat location|||
|on_join_war|country|||
|on_loan_renewed|root = country scope:target = loan scope:owner = lender|check with exists = scope:owner first before doing effects with it||
|on_loan_repaid|root = country scope:target = loan scope:owner = lender|check with exists = scope:owner first before doing effects with it||
|on_loan_taken|root = country scope:target = loan scope:owner = lender|check with exists = scope:owner first before doing effects with it||
|on_location_changed_owner|root= location scope:loser = previous owner scope:winner = new owner|||
|on_location_changed_rank|location|||
|on_location_lost||||
|on_location_occupied|root = country scope:target = location scope:character = leading general character|When a location without fort changes controller after an occupation process||
|on_lose_great_power_status|country|||
|on_lose_revolution|country|||
|on_lose_revolution_target|country|||
|on_losing_war|root = country scope:winner = country scope:loser = country scope:war = war|||
|on_made_saint|root = country scope:recipient = character|||
|on_marriage_union_formation|root = union scope:ruler = ruling character consorts list = the list of all consort characters|||
|on_max_doom_reached|country|||
|on_military_annex|root = country doing the annexing scope:target = country being annexed|fired before the annexation happens||
|on_military_annexed|root = country doing the annexing scope:target = country being annexed|fired after the annexation has happened||
|on_mission_abort|country|||
|on_mission_completion|country|||
|on_mission_start|country|||
|on_mission_task_bypass|country|||
|on_mission_task_completion|country|||
|on_mission_task_start|country|||
|on_nation_changing|country|||
|on_new_age|country|this is done for ALL active countries when a new nation is picked.||
|on_new_country_formed|newly formed country|||
|on_new_ruler|root = country scope:old_ruler = character scope:new_ruler = character|||
|on_overrun_imprisoned|root = unit of prisoners scope:winner = country that was victorious|||
|on_parliament_failed|root = country scope:target = parliament issue scope:location = parliament seat location|||
|on_parliament_passed|root = country scope:target = parliament issue scope:location = parliament seat location|||
|on_parliament_started|root = country scope:location = parliament seat location|||
|on_policy_changed|country|||
|on_pre_ending_war|root = country scope:winner = country scope:loser = country scope:war = war|after winning and losing, for both, but before peace terms were executed||
|on_pre_losing_war|root = country scope:winner = country scope:loser = country scope:war = war|||
|on_pre_winning_war|root = country scope:winner = country scope:loser = country scope:war = war|||
|on_raw_material_changed|root = location scope:old_goods = previous trade goods scope:new_goods = new trade goods|||
|on_reform_change||||
|on_regency_end||||
|on_regency_start||||
|on_rejected_call_to_arms|scope:actor = caller scope:recipient = callee scope:war = war|||
|on_released_country|root = released country scope:overlord = overlord|||
|on_religion_changed|root = country scope:old_religion = old religion|||
|on_royal_marriage|root & scope:actor = sender scope:recipient = receiver scope:target_1 = character of scope:actor who gets married scope:target_2 = character of scope:recipient|||
|on_ruler_death|root = country scope:old_ruler is the one who died|||
|on_shatter_country|country|||
|on_siege_lost||||
|on_siege_won|root = country scope:target = location scope:character = leading general character|When a location with fort changes controller after a siege.||
|on_storm_reached_location|root = location scope:weather_system = weather system|||
|on_subject_type_changed|root = subject scope:overlord = overlord scope:subject_type = current subject type scope:old_subject_type = subject type before the changed|Is triggered when a subject changes its subject type via diplomacy||
|on_took_location_in_peace_treaty|root = winner scope:location = location scope:winner = new owner scope:loser = old owner|||
|on_union_formation|root = new union IO scope:ruler = ruling character or heir scope:first_leader = the first union leader country from the merge scope:second_leader = the second union leader country from the merge|sent after the new union is setup||
|on_union_merging|root = the union IO which is potentially part of the merge scope:ruler = leader character of the union|sent right before unions are about to merge|NOTE: this on_action is also called even if it is only a single Union. It would just be applied to that union then. Basically, gets called always when any union shenanigans are about to happen|
|on_union_split|scope:first_ruler = first character scope:second_ruler = second character|||
|on_war_declared|root = country scope:actor = country who declares the war scope:recipient = country who gets declared on scope:war = war|||
|on_winning_war|root = country scope:winner = country scope:loser = country scope:war = war|||
|on_work_of_art_created|work of art|||
|on_work_of_art_destroyed|work of art|||
|on_work_of_art_looted|root = work of art scope:target = new location scope:location = old location|Is NOT called by the move_art effect||
|on_work_of_art_moved|root = work of art scope:target = new location scope:location = old location|gets called by the move_art effect||
|parliament_monthly_pulse|country|This is only active during an active parliament session||
|religion_flavor_pulse|country|||
|volcano_location_pulse|location|checks every location in the default.map list of volcano locations monthly||
|weather_monthly_pulse|none|||
|yearly_country_pulse|country|||

### Base game scripted on actions

The following on actions are not called from game code, but instead by an effect or other on action.

|Name|Given scope|Description|Other Notes|
|---|---|---|---|
|chinese_expedition_event_pulse|root = Country scope:expedition_initiator = country||Root is nation harboring the treasure voyage Expedition initiator is the nation from which the expedition originates|
|chinese_expedition_movement_events|country||Root is the Expedition Initiator|
|delhi_four_yearly_pulse|country|||
|four_yearly_country_pulse_25_percent|country||This on_action has a 25% chance of triggering on four year pulse|
|four_yearly_country_pulse_50_percent|country||This on_action has a 50% chance of triggering on four year pulse|
|france_naples_administration_broken|none|||
|on_cabinet_death||||
|on_country_specific_pulse|country|||
|on_disloyal_independent_appanage|none|||
|on_former_independent_appanage|none|||
|on_four_yearly_check_for_script|country|||
|on_fraticide_underage_succession_waiting|none|||
|on_horde_pretender_death|none|||
|on_milanese_library_occupied|country|||
|on_new_appanage|none|||
|on_papacy_reform_removed|none|||
|on_papal_opinion_added|none|||
|on_papal_opinion_removed|none|||
|on_prussian_crusader_death|none|||
|on_ruler_death_delhi_tombs_construction|country|||
|on_settle_the_frontier_monthly_pulse|country|||
|on_tamil_rebel_death|none|||
|on_timurid_governor_death|country|||
|on_timurid_occupy_location|none|||
|on_timurid_occupy_location_horde|none|||
|on_timurid_ruler_death|none|||
|on_vassalized_appanage|none|||
|wor_on_wallenstein_prison_occupation|none|||
|wor_on_wallenstein_prison_timeout|none|||

## References


