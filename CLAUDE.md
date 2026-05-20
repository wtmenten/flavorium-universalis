# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Cabinets and Choices** is a Europa Universalis V mod (v0.1, compatible with EU V 1.2.*) focused on enhancing cabinet member gameplay with new traits and dynamic events.

EU V Modding Documentation: https://eu5.paradoxwikis.com/Modding

## Development Environment

- **Game files location**: `F:\SteamLibrary\steamapps\common\Europa Universalis V\game` — reference these when checking vanilla definitions, scripting syntax, or effect/trigger scopes.
- **No build step**: Paradox mods are plain text files loaded directly by the game engine. There is no compilation, linting tool, or test runner.
- **Testing**: Load the mod in-game via the EU V launcher. The game logs errors to `%USERPROFILE%\Documents\Paradox Interactive\Europa Universalis V\logs\`.

## Mod Structure

The mod uses two parallel content directories:

- `in_game/` — content that loads alongside vanilla (additive). Place new traits, events, decisions, etc. here.
- `main_menu/` — content that applies on the main menu screen only (e.g., UI graphics).

Paradox script files use the `.txt` extension and follow a Clausewitz scripting syntax (key-value pairs with `{}` blocks). Mirror the subfolder structure of the vanilla `game/` directory when adding new files.

### Key paths

| Path | Purpose |
|---|---|
| `in_game/common/traits/` | Character trait definitions |
| `main_menu/gfx/interface/icons/traits/` | Trait icon assets |
| `.metadata/metadata.json` | Mod descriptor (name, version, game compatibility, replace_paths) |

`replace_paths` in `metadata.json` controls which vanilla directories are completely replaced rather than merged. Add a path here only when the mod must prevent vanilla entries from loading.

## Scripting Conventions

EU V uses Clausewitz script. When writing traits, events, or decisions, follow the patterns found in the vanilla game files at `F:\SteamLibrary\steamapps\common\Europa Universalis V\game\common\` and `game\events\`. Key scoping rules, trigger names, and effect names must match vanilla exactly — the engine gives no helpful errors for typos in script keys.

Localisation strings go in `in_game/localization/<language>/` as `.yml` files (UTF-8 BOM required by the engine).
