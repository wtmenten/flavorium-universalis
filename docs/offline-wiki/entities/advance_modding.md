# Advance modding

**Source:** https://eu5.paradoxwikis.com/Advance_modding

---

**Advance** modding involves the creation of new advances - the Europa Universalis V representation of technological progress.

## Technical details

Advance definitions are stored in `common/advances`. They are usually placed in the `common` top folder.

Example of such a file:

in_game/common/advances/0_age_of_discovery.txt

## Syntax

Most advances are comprised of the following syntax:

```
ostentatious_clothing = {		# Key of the advance
	icon = fla_cloth
	age = age_5_absolutism
	
	requires = lead_ore_dressing
	
	global_alum_output_modifier = 0.1
	global_dyes_output_modifier = 0.1
}
```

### Age requirement

Every advance requires the `age` argument to determine which age tab the advance belongs to.

### Modifiers

Advances are implicit modifier blocks, which allow modifier types that affect the nation once the advance has been researched.

An advance can also be given modifier types that are applied during the research process though - using `modifier_while_progressing` blocks. There can be a number of these blocks which can hold any number of modifier types. Each block has a `scale` value, a script value that determines the strength of the modifier, and `potential_trigger`, which determines if the modifier applies at all. E.g:

```
modifier_while_progressing = {
	scale = {
		value = 1 	# 100% of the modifier is given at a time
		add = {	 	# which can be increased by another 100% based on legitimacy
			value = legitimacy
			divide = 100
		}
	}
	potential_trigger = {	# but only if the country is a monarchy
		government_type = government_type:monarchy
	}
	monthly_prestige = 0.05
}
```

### Other requirements

Advances can have only a single prerequisite advance. This creates a simple tree structure with a number of "root" advances that branch out to a number of "children". Prerequisite advances are defined using `requires` and must be defined before the advance requiring it. Advances without a defined prerequisite are semi-randomly assigned to the tree. To ensure that a given advance never becomes a "parent" `allow_children = no` can be used. This prevents randomly assigned child advances and throws an error if another advance lists it as a prerequisite.

Advances also have `potential` and `allow` trigger blocks, with the researching country as the root scope. `potential` determines whether the advance is visible and `allow` determines if the advance can be researched. Most base game advances have neither; some "regional" advances use `potential` to limit the advance to that geographical region while most "root" advances use `allow` to require the related institution to be embraced.

While an advance can "graphically" require only one advance, other advances can be required in the `allow` trigger block.

Besides that, there are special flags for certain types of requirements, namely government and country type. These are referenced in the content tab as well as highlighted with an icon.

|Token name|Right-side argument|Right-side argument source|GUI script function|Additional information|
|---|---|---|---|---|
|**government**|Government Type|`common/government_types`|`AdvanceItem.IsGovernmentUnlock`|Requires the country to have the selected government type for potential and shows up under the "Government Type" bonuses in main menu content tab|
|**country_type**|Country Type|`location`, `building`, `pop`, `army`, `navy`|`AdvanceItem.IsCountryTypeUnlock`|Requires the country to be of the country type for potential and shows up under the "Country Type" bonuses in main menu content tab|

Additionally, the game implicitly assigns advances to additional categories based on triggers in `potential`:

|Category|Trigger|GUI script function|Other information|
|---|---|---|---|
|"Country" advance|Presence of `tag` or `has_or_had_tag` triggers in `potential`.|`AdvanceItem.IsCountryUnlock`||
|"Religion" advance|Presence of religion comparison triggers in the `potential`|`AdvanceItem.IsReligionUnlock`||

*Note for using culture_group requirenment: The Content tab in country selection only shows advancements belonging to alphabethically first culture group the country's culture belongs into.*

### Controlling tree generation

Advance trees are generated and cannot be structured on their own. There are, however, several factors to influence how the tree gets generated, though.

`depth` is an integer that is used to determine at which level the advance will be placed. The lowest value is 0, which is used to place the advance at the top. Using any other integers is usually futile, as the placement of those is to be generated using `requires` statement. Required advances must be loaded before the advance that requires them.

### Controlling AI bias

There are two ways to control what the AI will research - `ai_weight` and `ai_preference_tags`.

`ai_weight` is a scripted value evaluated on the country which adds additional weight for the country AI to research this advance specifically.

`ai_preference_tags` is a set of preference tags that are combined with country's setup research preferences to increase the AI's likelihood to research this advance by that amount.

### Research cost

Every advance has its research cost. The base research cost is determined by the BASE_RESEARCH_COST define (Vanilla value: `25`), but can be further modified using `research_cost` which accepts a floating point value, which then gets added on top of the original cost - `research_cost = 1.0` will give a penalty of +100.0%. Moreover, there is also a hardcoded research cost increase based on ages. If an advance for an outdated age is being researched, a reduction of PREVIOUS_AGE_REDUCTION define (Vanilla value: `−8`) is applied. Additionally, every age ahead of traditions gets a penalty of AGE_RESEARCH_MODIFIER define (Vanilla value: `0.15`) times the amount of ages that passed.

### Unlocking capabilities

Advances provide an easy interface for unlocking many different scripted types. These do not require any `allow` and `potential` checks and the tooltip for the advance is automatically updated to mention the types:

|Unlock key|Type unlocked|Type location|Additional Info|
|---|---|---|---|
|**unlock_road_type**|Road type|`common/road_types`||
|**unlock_employment_system**|Employment system|`common/employment_systems`||
|**unlock_unit**|Unit type|`common/unit_types`||
|**unlock_ability**|Unit ability|`common/unit_abilities`||
|**unlock_interaction**|Character interaction|`common/character_interactions`||
|**unlock_country_interaction**|Country interaction|`common/country_interactions`||
|**unlock_estate_privilege**|Estate privilege|`common/estate_privileges`||
|**unlock_relation_type**|Relation type|`common/scripted_relations`||
|**unlock_building**|Building type|`common/building_types`||
|**unlock_law**|Law|`common/laws`||
|**unlock_policy**|Policy|`common/laws`||
|**unlock_levy**|levy type|`common/levies`||
|**unlock_heir_selection**|Heir selection|`common/heir_selections`||
|**unlock_government_reform**|Government reform|`common/government_reforms`||
|**unlock_casus_belli**|Casus belli|`common/casus_belli`||
|**unlock_cabinet_action**|Cabinet action|`common/cabinet_actions`||
|**unlock_subject_type**|Subject type|`common/subject_types`||
|**unlock_production_method**|Production method|`common/building_types`||
|**unlock_diplomacy**|Diplomatic action|Not extendable|Uses different syntax - lists. This is also the case if there is only one diplomatic action to be unlocked.|

### Starting technology level

`starting_technology_level` is an integer that is used to setup starting research for countries.

### Icon

||**This section requires verification emperical tests to determine how the unit and levy icons are assigned(Or link to a wiki page which describes it properly).. Please add appropriate references.** See the Icon priority section on the talk page for details about what needs verification.|

The game looks for an icon in the following order:

- first `unlock_unit` line (some part of the illustration of the unit which seems to be based on the category and the gfx_tags)
- first `unlock_levy` line (probably uses a similar algorithm as unlock_unit)
- building icon of the first `unlock_building` line
- icon of the output good of the first `unlock_production_method` line
- last icon line
- `.dds` file named after the advance

#### Icon attribute

`icon` attribute is used to set a custom icon key for the advance if none of the `unlock_` attributes exist which give an icon.

#### Advance key as filename

Otherwise, the advance key is used as the icon name.

#### Icon path

Advance icons are stored in ADVANCE_ICON_PATH define (Vanilla value: `"gfx/interface/advance"`).

In order to have an icon assigned, a new `.dds` entry entitled with the key must be added there.

#### Example

For example:

```
zan_gold_trade_of_africa = {
	...
}
```

```
coffea_arabica = {
	icon = origin_of_coffee
	...
}
```

The first advance uses `zan_gold_trade_of_africa.dds` as its icon, while the latter uses `origin_of_coffee.dds`.

### Ages event and new unlocks

`for` attribute is used to set an advance as unlocked by a specific chosen age preference. It, therefore, accepts one of three values:

- `adm`
- `dip`
- `mil`
Age-preference advances get a special texture in the GUI, which is done with `AdvanceItem.IsChoiceUnlock`.

#### Setting age preference

Age preference is set using set_age_preference effect, which sets the age preference for the current age.

It accepts the same values as the `for` advance attribute.

## Localization

Advances only need two keys for localization:

- `<key>`
- `<key>_desc`

## Script involving advances

- research_advance effect in `country` scope researches the `advance` scope on the right-hand side:
- advance_type: is a global data scope link used to fetch the advance type for a given key.
- can_research_advance is a `country` scope trigger that checks if the country can research a not-yet researched advance scope on the right.
- has_advance is a `country` scope trigger that checks if the country has the advance identified by the key.
- has_advance_available is a `country` scope trigger that checks if the country has the advance identified by the key researched or it is available to research.
- num_of_advances_researched is a `country` scope value trigger that checks if the country has researched a certain amount of advances.
- has_advance_for_employment_system is a `country` scope value trigger that checks if the country has researched an advance that has a `unlock_employment_system` that * points towards towards the scope on the right that evalutes to an `employment_system`.
- has_advance_for_succession_law is a `country` scope value trigger that checks if the country has researched an advance that has a `unlock_heir_selection` that points towards towards the scope on the right that evalutes to an `heir_selection`.

## References


