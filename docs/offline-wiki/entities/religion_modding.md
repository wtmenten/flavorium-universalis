# Religion modding

**Source:** https://eu5.paradoxwikis.com/Religion_modding

---

**Religion modding** involves the creation of new religions, their modification. Addition of new religious mechanics, their modification. Adding new holy sites to existing religions.

## Religion definitions

Religion definitions are the most important in religion modding. They define the basic aspects of religions to be used in gameplay. The religions used on game start are "built" out of those, and so editing of those religions might not always be visible in savefiles.

### Example

```
anglican = { 
	color = color_anglican
	group = christian
	
	enable = 9999.1.1 #historically 1534.11.3
	
	religious_aspects = 3
	has_religious_influence = yes

	ai_wants_convert = yes
	
	definition_modifier = {
		global_max_literacy = 5
		global_build_buildings_cost = -0.05
		
		monthly_religious_influence = 0.1

		maximum_religious_influence = 400
	}
	
	opinions = {
	}

	unique_names = {
		name_aaron name_abraham 
		name_bartholomew name_benjamin 
		name_cornelius
		name_elias Ezra
		name_gabriel 
		name_isaac 
		name_james Jason name_jeremiah name_jonas Jonathan name_jordan name_joseph name_joshua Josiah 
		name_moses 
		Nathan Nathaniel 
		name_samuel name_salomon
		name_timothy
		name_zechariah	
	}

	tags = { protestant_gfx western_christian_gfx christian_gfx abrahamic_gfx }
	custom_tags = { protestant church_aspects }
}
```

### Basic syntax

`color` is a color attribute that determines what color this religion will have in the religion-associated mapmodes.

`group` is an attribute that accepts a Religion group key - it links this religion to a religion group.

`definition_modifier` is set of `religion` category modifiers. If country modifiers are inserted here, they will proliferate to every nation following this religion.

### Religious currency settings

There are numerous attributes which, when set to yes, will create a religious currency for this religion:

- `has_religious_influence = yes`
- `has_karma = yes`
- `has_yanantin = yes`
- `has_doom = yes`
- `has_honor = yes`
- `has_purity = yes`
- `has_rite_power = yes`

### Tags

Religions can be given tags by using `custom_tags`, which accept a list of strings:

```
custom_tags = {
	lategame_manufactory
	guild
}
```

Those can then be checked using has_tag trigger.

### Religion opinions

Religions can have relations with each other using the religion opinion system. The setup for game start is set in each religion using `opinions` attribute, which accepts religion keys alongside the opinion "value", the following opinions are available in order of how negative to how positive they are:

```
opinions = {
	bogomilism = enemy
	bosnian_church = negative
	catharism = neutral
	hussite = positive
	orthodox = kindred
}
```

The default value for each religion permutation is `neutral` so setting it to neutral can be omitted.

### Fixed liturgical language

A religion can set a fixed liturgical language using `language` - where the right side is a key of that language. When a liturgical language is fixed, all nations following this faith will have their liturgical language set to it without possibility to change it to a different one.

### Tying religious reforms

Religions can have religious focuses - "advances" that can be "researched" by the nations of the religion as part of their religious mechanics for their own benefit. Religion focuses tied to this religion are included in the `religious_focuses` attribute, which is a list of keys of the focuses.

Nations with religious focuses may "reform" their religion when they reach enough reforms as set by `num_religious_focuses_needed_for_reform`, which accepts an integer representing the amount of reforms needed. When the amount of focuses exceeds that, the game may change the nations' religion to the religion provided in `reform_to_religion` if that attribute is present. `reform_to_religion` accepts a religion key of target religion.

### Tying religious aspects

Religions might have religious aspects - selectable group of bonuses nation following that religion might pick from. The max amount is determined by `religious_aspects`, which accepts an integer. Aspects are tied to religions in the aspects themselves.

### Tying religious schools

Religions can also have religious schools within them which may act as a kind of subdivision. Each of those religious schools should be tied to the religion by using `religious_school` attribute - the right hand side accepting a key of the religious school.

Each religious school needs an entry like the following:

```
religious_school = ismaili_school	
religious_school = jafari_school
religious_school = zaidi_school
```

### Tying religious factions

Religions can have religious factions tied to them. They are inserted using `factions` attribute with a list of keys.

### Unique character names

One can make certain character names associated with a religion using `unique_names`, which accepts a set of strings representing each of those names.

### Enabling religion

Religions can be given `enabled` date. When that date is defined and is in the future, the religion will be considered "inactive". Whether a religion is enabled can be checked via is_religion_enabled trigger and can be enabled  via enable_religion effect.

### Other syntax

`use_icons = yes` will define this religion as using icons. If a religion is not using icons, the game will hide the religious_icon_power_modifier modifier type.

`has_canonization = yes` will define this religion as allowing canonization of characters as saints. This can be checked using has_canonization trigger. Countries with state religion that has canonization will receive `saints_from_country` static modifier that is scaled to how much of total saint skills their country has out of all countries with their religion. If that religion has 3 saints, each one with 100/100/100 stats, and the considered country has 1 of those saints, they would get `saints_from_country` scaled with 300 / 900.

`ai_wants_convert = yes` will define this religion as one that ai will want to convert to. Mainly used by ai_wants_convert trigger in convert_religion generic action.

`has_avatars = yes` determines that this religion has avatars. This is used by `Religion.HasAvatars` boolean GUI function.

`needs_reform = yes` ties this religion to reform desire mechanic. Reform desire will tick up for this religion according to monthly_reform_desire religion modifier type.

`has_patriarchs = yes` defines this religion as using patriarchs. This can be checked using has_patriarchs trigger or `Reeligion.HasPatriarchs` boolean data function.

`tithe` can be used to define the tithe amount of a religion that can be then fetched in script using tithe trigger. Accepts a floating point number representing a fraction.

`has_religious_head = yes` defines this religion as having a religious head. Can be checked via has_religious_head trigger. Meant to be used in conjunction with `important_country`.

`important_country` is used to define an important tag which is also used to determine who the religious head. The tag provided on the RHS will be used to determine the important country.

`has_cardinals = yes` will define this country as having cardinal system. Every country with this religion will have `num_cardinals` static modifier scaled with amount of cardinals in the country. Similarly, every country will have `total_cardinals_in_religion` static modifier applied with total amount of cardinals in the religion.

`culture_locked = yes` marks pops of this religion as being tied to the culture. Assimilation of pops with this religion will be blocked, so they must be converted first.

`has_autocephalous_patriarchates = yes` is used to set this religion as having autocephalous patriarchates. It can be checked via has_autocephalous_patriarchates trigger.

`max_sects` is an attribute with an integer that sets a maximum amount of sects for this religion. Can be checked via max_sects trigger.

### Graphical tags

`tags` is a set of strings that represent graphical culture tags used by this religion.

### Religious figures

Religions can have religious figures tied to them. Religious figures are characters that have access to special religious figure traits and can be invited by countries. They are strongly tied to Religious schools

The amount of religious figures is determined by `max_religious_figures_for_religion` - a script value with `religion` as ROOT. This determines the max amount of religious figures that are part of this religion religion-wide.

### Localisation

Every religion needs the following keys localized:

- `<key>`
- `<key>_ADJ`
- `<key>_desc`

### Religion groups

**Religion groups** are sets of religions that share some common characteristic. The `religion_group` scope can be accessed by calling group on `religion`. The group religion belongs to is provided in the religion and the religions are defined in their own file.

#### Example

```
muslim = {
	color = religion_sunni
	allow_slaves_of_same_group = no
	convert_slaves_at_start = yes
	modifier = {
		allow_rgo_slave_demand = yes
	}
}
```

#### Syntax

`color` is used to define a common color to be used for mapmodes relating to religion.

`allow_slaves_of_same_group = no` is used to prevent slaves that share the same religion group with country's religion. By default this is set to true and such slaves will not be liberated.

`convert_slaves_at_start = yes` is used to make countries of this religion group attempt to enslave non-accepted pops at game start.

`modifier` field is used to set country modifiers that every country of this religion group will receive.

#### Localisation

Every religion group needs the following keys localized:

- `<key>`
- `<key>_ADJ`
- `<key>_desc`

## Religious schools

Religious schools are subdivisions within religions. Religious schools have opinions with each other, offer different bonuses and offer more subdivision within a religious block.

### Example

```
upkesa_gaccha_school = {
	color = rgb { 46 91 95 }

	enabled_for_country = {
		religion = religion:jain
	}
	enabled_for_character = {
		religion = religion:jain
	}
	
	modifier = {
		monthly_legitimacy = 0.1
	}
}
```

### Syntax

Religious schools have 4 attributes.

`color` uses color notation to define a color this religious school will have in religious school mapmode.

`modifier` is a set of country modifiers that countries with this religious school set as primary will receive as well as any countries that invite a religious figure of this religious school.

`enabled_for_character` is a set of triggers on `character` scope that must be fulfilled for that character to become a religious figure.

`enabled_for_country` is a set of triggers on `country` scope that must be fulfilled for that character to become a religious figure.

### Localisation

Every religious school should be localized with:

- `<key>`
- `<key>_desc`

## Religious aspects

Religious aspects are certain modifiers that nations may activate if their religious has such an aspect enabled.

### Example

```
adoptionism = {
	religion = bogomilism
	religion = catharism
	religion = lollardy
	religion = paulicianism

	enabled = {
		NOT = {
			has_religious_aspect = religious_aspect:modalism
		}
	}

	modifier = {
		global_clergy_desired_pop = 0.01
		stability_cost = -0.1
		monthly_religious_influence = 0.1
		monthly_towards_communalism = societal_value_monthly_move
	}

	opinions = {
		adoptionism = 10

		modalism = -20
	}
}
```

### Syntax

`icon` is used to overwrite the key of the icon. By default the key is the same as the aspect key (so `adoptionism` will look for `adoptionism.dds`, `icon = test` can be made to look for `test.dds`)

`religion` is used to denote the religions this aspect is available to.

`visible` is a `country` trigger that determines when the religious aspect will show up. `enabled` is then used to determine when it can be used.

`modifier` is the country modifiers that this aspect will give when active.

`opinions` field is used to add or decrease opinion with other countries that may have the defined religion aspects.

### Localisation

Every religious aspect needs to have its title and description localized with the keys:

- `<key>`
- `<key>_desc`

## Religious figures

### Example

muslim_scholar = {
	enabled_for_religion = {
		group = religion_group:muslim
	}
}

### Syntax

The only available attribute is `enabled_for_religion`, which is a `religion` trigger that determines which religions may have religious figures of this type.

### Localisation

Every religious figure should be localized with:

- `<key>`
- `<key>_desc`

## Religious focuses

Religious focuses are, in a sense, advances that can be research by countries for progress within their religion. They are somewhat alike to religious reforms from Europa Universalis IV.

### Example

```
elevate_patron_god = {
	monthly_progress = {
		add = {
			desc = "DIPLOREASON_BASE"
			value = 0.25
		}
		add = {
			desc = "[crown_power|e]"
			value = "estate_power(estate_type:crown_estate)"
			multiply = 0.1
		}
		add = {
			desc = "clergy_estate_power"
			value = "estate_power(estate_type:clergy_estate)"
			multiply = 0.5
		}
		add = {
			desc = "game_concept_doom"
			value = doom
			multiply = -0.005
		}
		if = {
			limit = { has_ruler = yes }
			add = {
				desc = "[ruler|e] [total_ability|e]"
				value = ruler.total_abilities
				multiply = 0.0015	#~0.5 if our ruler or regent is a 300-stat god
			}
		}
		if = {
			limit = {
				capital = { has_location_modifier = nahuatl_temple_expansion_modifier }
			}
			add = {
				desc = "nahuatl_temple_expansion_modifier"
				value = 0.2
			}
		}
		min = 0
	}
	
	modifier_while_progressing = {
		tolerance_own = -1
	}

	modifier_on_completion = {
		global_pop_conversion_speed_modifier = 0.2
	}

	ai_will_do = {
		add = 1
	}
}
```

### Potential & allow

`potential` is a country trigger that determines if this country may see this religious focus.

`allow` is also a country trigger - this one determines when the country may select this religious focus.

### Modifiers

`modifier_while_progressing` is a country modifier field for modifiers that are applied when the religious focus is being "researched".

Once the focus is fully activated, the modifiers in `modifier_on_completion` will be used.

### Progress and completion

Every month while a focus is progressing, the monthly progress is determined by the `monthly_progress` script value. The `ROOT` in that script value is `country` doing the focus.

The focus is completed when it reaches the number defined in RELIGIOUS_FOCUS_COST define (Vanilla value: `100`) (scaled down by 100 to percentage form).

When completed, the focus will fire `effect_on_completion` effect, which is a `country` effect.

### Ai weighting

The AI likelihood to pick a focus to focus on is dependent on `ai_will_do` script value, provided with the `country` as ROOT.

The AI will pick the focus which returns the highest value in the AI will do field, and if no focus has a value above 0, will pick nothing. If a currently "researched" focus gets down to 0 or below 0, AI will cancel it and will try to contemplate picking another one.

### Localisation

Every religious focus should be localized with:

- `<key>`
- `<key>_desc`

## Religious faction

Religious factions are, in a sense, different categories for generic actions that are used in religious contexts.

### Example

```
imperial_court = {
	visible = {
		religion:shinto = {
			any_country_in_religion = {
				has_reform = government_reform:japanese_imperial_family
			}
		}
	}

	enabled = {
	}

	actions = {
		get_claim_from_imperial_court
		get_marriage_from_imperial_court
		become_shogun_from_imperial_court
	}
}
```

### Syntax

`visible` and `enabled` are trigger fields which determine when the factions are visible and when they can be used. They are both checked on `international_organization` scope, as they are visible from international organization view.

`actions` is a list of generic action keys that are available as part of this faction.

## Holy sites

Holy site modding involves the creation of new holy site types (which are responsible for modifiers and shared data) and holy sites (which is setup for holy site data, essentially).

### Example

```
ise_grand_shrine = {
	location = watarai
	type = shrine
	importance = 5
	religions = { shinto }
}
```

### Syntax

Two most basic attributes for a holy site are:

- `location` - the location key where this location definition is.
- `religions` - list of location keys of religions that accept this holy site.
- `importance` - an integer value representing importance of this holy site - an important multiplier for country and location modifiers.
- `type` - key of a holy site type that determines the modifiers of this holy site.

### Other syntax

- `name_key` - a replacement for holy site definition key that is used for illustration and localization.
- `god` - key of a god this holy site is dedicated to. Used for localisation.
- `avatar` - key of a god's avatar this holy site is dedicated to. Used for localisation.

### Localisation

Every holy site should be localized with:

- `<key>`

### Holy site types

#### Example

```
mayan_holy_site = {
	location_modifier = {
		local_clergy_desired_pop = 0.02
		local_monthly_prosperity = 0.001
		local_clergy_max_literacy = 10
		local_production_efficiency = tiny_production_efficiency_bonus
	}
	country_modifier = {
		monthly_religious_influence = 0.02
	}
}
```

#### Syntax

The holy site types only have 3 attributes:

- `country_modifier` - country modifier that is applied to the country that owns a holy site of this type multiplied by its importance for each such holy site
- `location_modifier` - location modifier that is applied to the location with this holy site multiplied by its importance
- `religion_modifier` - religion modifiers that is applied to the religion this holy site belongs to. 50% of this modifier is applied if the location dominant religion matches the right religion and other 50% if the owner's country religion matches.

#### Localisation

Every holy site type should be localized with:

- `<key>`
- `<key>_desc`

## God modding

God modding includes creation of new gods and their avatars, if applicable.

### Example

```
shiva_god = {

	religion = hindu

	potential = {
		any_international_organizations_member_of = {
			international_organization_type = international_organization_type:hindu_branch
			international_organization_has_policy = policy:smartism
		}
	}

	country_modifier = {
		global_population_growth = 0.0001
		potential_trigger = {
			NOT = { has_access_to_god_holy_site = { god = shiva_god } }
			smartism_balanced_gods = yes
			NOT = { is_favoring_god = { god = shiva_god } }
		}
	}

	country_modifier = {
		potential_trigger = {
			OR = {
				is_favoring_god = { god = shiva_god }
				AND = {
					has_access_to_god_holy_site = { god = shiva_god }
					smartism_balanced_gods = yes
				}
			}
		}
		global_life_expectancy = 2
		global_population_growth = 0.0001
	}

	country_modifier = {
		potential_trigger = {
			custom_tooltip = {
				text = disfavoured_god_tt
				smartism_balanced_gods = no
				NOT = { is_favoring_god = { god = shiva_god } }
			}
		}
		global_life_expectancy = -1
		global_population_growth = -0.0001
	}
}
```

### Assigning a god

Gods need to be assigned to religions or religion groups. Such assignments are provided one or more of `religion` and/or `group` tokens:

```
group = christian
religion = norse
```

This notation can also be expanded by providing a `name_key` for a unique key for the god name:

```
group = {
	group = christian
	name_key = CHRISTIAN_GOD
}
```

### Potential and allow

Gods accept `potential` and `allow` trigger fields that dictate when a god is visible and selectable respectively. They are both `country` fields.

### God modifiers

Gods can be assigned modifiers through `country_modifier`. Those modifiers are scaleable and triggered, so they accept a `scale` script value component for scaling and `potential_trigger` for when it should appear. The `ROOT` in both cases is `country`.

Gods can also use `province_modifier` for provinces and `location_modifier` for location modifiers.

### Icon

Key of God icon can be overridden using `icon`.

```
icon = test # The game will look for test.dds
```

### Localisation

Every god should be localized with:

- `<key>`
- `<key>_desc`
- As well as any additional `name_key` entries.

### Avatars

Avatars are different representations of a god. Unlike gods, which are active by default, avatars need to be activated and there can be a maximum amount of them.

In terms of syntax, they follow the same syntax as Gods - besides the Assigning a god section. Instead, they need to be tied to the god they represent using `god` attribute, which accepts the god key as RHS.

#### Example

```
matsya_avatar = {
    god = vishnu_god

    allow = {
        has_ports = yes
    }

    country_modifier = {

    }

    location_modifier = {
        potential_trigger = {
            is_port = yes
        }
        local_monthly_development_modifier = 0.1
    }
}
```

#### Localisation

Every avatar should be localized with:

- `<key>`
- `<key>_desc`

## References


