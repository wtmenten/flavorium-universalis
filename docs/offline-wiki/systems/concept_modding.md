# Concept modding

**Source:** https://eu5.paradoxwikis.com/Concept_modding

---

**Concept** modding involves the creation of new game concepts to be usable in Europa Universalis V.

## Technical details

Game concepts are located in `common/game_concepts`, usually in the `main_menu` top folder.

For example:

common/game_concepts/example_file.txt

## Syntax

Here is example of a simple game concept definition:

```
reformation = {
	alias = { protestant protestants }
	texture = "gfx/interface/icons/situations/reformation.dds"
}
```

`reformation` represents the name of the game concept. It is the key that needs to be localized both with a title and description in localization.
Below are the aliases, which, when used, will be shown in text with their alias localization. When hovered over, the main concept tooltip will use the original title and description.

Last is the `texture` field, which points to the icon texture to be used. There is no implicit icon assignment, the icon must be assigned for each game concept using this field.

### Family and parent

Game concept can be set in a "family" of another game concept using the `family` attribute. As a result, the game concept of the "family" parent will be shown in the tooltip for this concept. 

Game concept can also have a "parent" game concept set using `parent`. However, this is unused. Were this to be used, it can be accessed in GUI script using `GameConceptTooltip.GetParentText`.

### Europedia and loading screen entries

By default, all game concepts are shown in the Europedia. This behavior can be turned off using `shown_in_encyclopedia = no`. 

On the contrary, game concepts will not be shown in the loading screen by default. This behavior can be toggled on using `shown_in_loading_screen = yes`.

### Map mode

Game concept can be set to override current mapmode shown using `tooltip_map_mode`. The keys of mapmodes available can be found in the map mode definitions `gfx/map/map_modes/`.

## Localization

Every game concept needs to have the following localized:

- `game_concept_<key>`
- `game_concept_<key>_desc`
Moreover, every alias needs to be additionally localized:

- `game_concept_<alias_key>`
No description is required, as the alias will use the same description as the main one.

Game concepts and their aliases can be referred to in localization using `[<concept_key>]`, but they are mostly used with the `[<concept_key>|e]`. Both print the respective concept name/alias name alongside providing a tooltip when hovered. The `|e` tag additionally colors the text to the distinct "concept light blue" color.

Game concepts have other references in the datacontext `GC( Arg0 )` global promote which accepts the game concept key and returns a tooltip for game concept, used mainly in GUI. 

`Concept( Arg0, Arg1 )` can be used to create a concept tooltip with different than one expected from alias. Arg0 is the concept key, while Arg1 is the text that will be shown. 

`SelectGameConcept( Arg0, Arg1, Arg2 )` is used to select between two concepts shown based on a condition. Arg0 is the conditional statement, Arg1 is key of the game concept that should be shown if the condition is true, Arg2 is key of the game concept shown otherwise.

## References


