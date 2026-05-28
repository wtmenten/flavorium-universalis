# Culture modding

**Source:** https://eu5.paradoxwikis.com/Culture_modding

---

Cultures in Europa Universalis V are highly customisable with a number of different options.

## Culture definition

Cultures are defined in the in_game/common/cultures folder.

Each culture needs a language, a color, tags for graphics, and a culture group.

```
welsh = {  #Script name for the culture. Can be anything but is best matched to the in-game localization.
	language = welsh_dialect #The language or dialect spoken by the culture
	
	color = map_WLS #The map color of the culture. Can either be a reference to a definition in the named_colors folder or a RGB or HSV color.
	
	tags = { welsh_gfx celtic_gfx british_gfx western_european_gfx european_gfx } #The 3D graphics groups used by the culture in game.

	opinions = { # This culture's starting opinion of other cultures. Can be enemy, negative, neutral, positive, or kindred.
		cornish = kindred
		english = negative
		breton = positive
	}

	culture_groups = { # A list of culture groups this culture belongs to,
		celtic_group
		british_group
	}
}
```

## Culture groups

Culture groups are defined in the in_game/common/culture_groups folder.

The only thing a culture group needs is it's script name.

```
celtic_group = {
}
```

A culture can be part of multiple culture groups.

## Languages and dialects

Languages are defined in the in_game/common/languages folder.

```
brythonic_language = { #Script tag for the primary language.

	color = map_WLS #The map colour for the language.

	family = celtic_language_family #The family group of the language.

	male_names = {
		[Male First Names]
	}
	female_names = {
		[Female First Names]
	}
	
	dynasty_names = {
		[Dynasty Names]
	}

	ship_names = {
		[Ship Names]
	}
		
	lowborn = {
		[Lowborn Surnames]
	}

	patronym_prefix_son = "patronym_prefix_welsh_son" #Optional: The patronym prefix for sons. 
	patronym_prefix_son_vowel = "patronym_prefix_welsh_son_vowel" #Optional: The patronym prefix for sons as a vowel if different from the patronym_prefix_son.
	patronym_prefix_daughter = "patronym_prefix_welsh_daughter" #Optional: The patronym prefix for daughters.

	dialects = { #Dilects of the language.
		welsh_dialect = {

		}

		breton_dialect = {
			
		}
	}
}
```

### Patronym properties

Newly generated characters can be named after their parents. Prefixes and suffixes can be applied to these names.

- `patronym_prefix_son` for a patronym prefix for sons. For example "mac" in Gaelic.
- `patronym_prefix_son_vowel` The patronym prefix for sons as a vowel if different from the `patronym_prefix_son`. For example "mág" in Gaelic
- `patronym_prefix_daughter` = The patronym prefix for daughters. For example "nic" in Gaelic.
- `patronym_prefix_daughter_vowel` = The patronym prefix for daughters as a vowel if different from the `patronym_prefix_daughter`. For example "nig" in Gaelic.
- `patronym_suffix_son` for the patronym suffix for sons. For example "sson" in Swedish.
- `patronym_suffix_daughter` for the patronym suffix for daughters. For example "sdotter" in Swedish.

### Location-based name properties

There are six location-based name properties that can be applied to characters. Newly generated character names can be named after a location on the map with the following prefixes and suffixes.

- `location_prefix` a location-based prefix for surnames. For example "de" in French.
- `location_prefix_vowel` a location-based prefix for surnames as a vowel if different from `location_prefix`. For example "d'" in French.
- `location_suffix` a location-based suffix for surnames.
- `location_prefix_elision` a list of location prefixes that the game will check against. If the location the character is being named after has a match to any of the strings in `location_prefix_elision`, then it will not apply the `location_prefix`. This is to prevent things such as an Arabic character being named "al-Al-Basra".

### Dialects

Each dialect can have any of the properties of the language within it, except for its own dialects. The game will read from the dialect's specific properties if they exist, otherwise they will use the same as the parent language.

## References


