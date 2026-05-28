# EU5 Modding Wiki (Offline)

Offline copy of the [EU5 Paradox Wiki](https://eu5.paradoxwikis.com/) modding pages,
reorganized for AI agent reference. Content preserved from original; layout reorganized.

## Structure

### [core-scripting/](core-scripting/) — Core scripting

- [Effect](core/effect.md)
- [Trigger](core/trigger.md)
- [Scope](core/scope.md)
- [Scope link](core/scope_link.md)

### [concepts/](concepts/) — Concepts

- [Defines](concepts/defines.md)
- [Modifier types](concepts/modifier_types.md)
- [Variable](concepts/variable.md)
- [Macro](concepts/macro.md)
- [Script value](concepts/script_value.md)
- [Mean time to happen](concepts/mtth.md)
- [On actions](concepts/on_actions.md)
- [Color](concepts/color.md)

### [interface/](interface/) — Interface

- [Interface modding guide](interface/interface_modding.md)
- [GUI script](interface/gui_script.md)
- [Scripted gui](interface/scripted_gui.md)
- [Localization](interface/localization.md)

### [entities/](entities/) — Entities

- [Advance modding](entities/advance_modding.md)
- [Building modding](entities/building_modding.md)
- [Character modding](entities/character_modding.md)
- [Culture modding](entities/culture_modding.md)
- [Disaster modding](entities/disaster_modding.md)
- [Disease modding](entities/disease_modding.md)
- [Estate modding](entities/estate_modding.md)
- [Event modding](entities/event_modding.md)
- [Goods modding](entities/goods_modding.md)
- [Institution modding](entities/institution_modding.md)
- [International organization modding](entities/international_organization.md)
- [Law modding](entities/law_modding.md)
- [Mission modding](entities/mission_modding.md)
- [Modifier modding](entities/modifier_modding.md)
- [Pop modding](entities/pop_modding.md)
- [Religion modding](entities/religion_modding.md)
- [Situation modding](entities/situation_modding.md)
- [Subject type modding](entities/subject_type_modding.md)
- [Trait modding](entities/trait_modding.md)
- [Unit modding](entities/unit_modding.md)
- [War modding](entities/war_modding.md)

### [systems/](systems/) — Systems

- [Action modding](systems/action_modding.md)
- [Concept modding](systems/concept_modding.md)
- [Setup modding](systems/setup_modding.md)

## Quick Search

Use `python tools/wiki_search.py` for fast lookups:

```
python tools/wiki_search.py effect <name>       # search effects
python tools/wiki_search.py trigger <name>      # search triggers
python tools/wiki_search.py scope_link <name>   # search scope links
python tools/wiki_search.py modifier <name>     # search modifier types
python tools/wiki_search.py on_action <name>    # search on-actions
```

## Source

Scraped from https://eu5.paradoxwikis.com/ — run `python tools/wiki_scraper.py` to refresh.
