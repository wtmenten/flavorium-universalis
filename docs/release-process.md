# Release Prep Process

The comprehensive checklist for shipping a new version of Flavorium Universalis. Follow it
top-to-bottom — several steps depend on earlier ones (the generators read files you edit by hand).

## Artifact map

The Steam/web text all flows from one hand-edited source through generators. Know which files
are sources (edit these) and which are generated (never hand-edit — they get overwritten):

| File | Role |
|---|---|
| `.metadata/metadata.json` | **Source.** Mod descriptor; holds `version`. |
| `docs/change_notes/<version>.bbcode` | **Source.** Per-release change note (hand-written). `upload.py` prefers this per-version file and falls back to the shared `assets/workshop/change-notes.bbcode` (multi-version, `[b]vX[/b]` headers) when it's absent. The individual file is normalized on upload: a leading `[h1]…[/h1]` title is swapped for the canonical `[b]vX:[/b]` header. **Submods** use the same scheme — `submods/<mod>/workshop/change_notes/<version>.bbcode`, falling back to that submod's shared `workshop/change-notes.bbcode`. |
| `WORKSHOP_DESCRIPTION.bbcode` | **Source.** Full Steam description. Contains `<!-- GEN:name -->…<!-- /GEN:name -->` markers whose contents are auto-regenerated from mod files. Hand-edit only the prose *outside* the markers (Overview bullets, narrative `[h3]` sections). |
| `WORKSHOP_DESCRIPTION_steam.bbcode` | **Source, hand-maintained.** The trimmed description that fits Steam's length cap (the live workshop body). Not generated — update it manually in parallel. |
| `WORKSHOP_DESCRIPTION_upload.bbcode` | **Generated** by `generate_workshop.py --clean` (marker-stripped copy of the full description). |
| `WORKSHOP_DESCRIPTION_upload.md` | **Generated** web-docs Markdown (`bbcode_to_markdown.py`). |
| `docs/index.html` | **Generated** website main page (`generate_index.py`). |
| `docs/dev-diaries.html` | **Generated** from `docs/dev_diaries/*.md` (`generate_dev_diaries.py`). |

## Steps

1. **Bump the version** in `.metadata/metadata.json` (`"version"`). Hotfix = patch bump (e.g. 0.3.6 → 0.3.7).

2. **Write the change note**: `docs/change_notes/<version>.bbcode`. Mirror the format of the latest existing
   one (`[h1]… — vX.Y.Z …[/h1]`, compat line, `[hr][/hr]`, `[h2]` sections with `[list]`).

3. **Register any new content files in the generators.** `generate_workshop.py` reads *fixed file lists*,
   so new advance/privilege/etc. files won't appear in the auto sections until added:
   - `gen_advances` + `gen_privileges_reforms`: add the new advance filename to both advance-file loops.
   - `_load_privilege_data`: add the new privilege filename.
   - `MODIFIER_DISPLAY`: add any new modifier keys you want rendered (unknown keys are silently dropped, not errored).
   Verify with a dry run before committing: `python tools/generate_workshop.py --section advances --dry-run`.

4. **Hand-edit the descriptions** for the headline feature:
   - `WORKSHOP_DESCRIPTION.bbcode`: add an Overview `[*] [b]NEW:[/b] …` bullet and a narrative `[h3]` section
     (place it *outside* any GEN markers). The GEN advance/privilege sections fill in the mechanical detail.
   - `WORKSHOP_DESCRIPTION_steam.bbcode`: add a matching short bullet to the Overview list.

5. **Fix BOM**: `python tools/fix_bom.py` (the pre-commit hook also does this).

6. **Run the generators, in order** (each feeds the next):
   ```
   python tools/generate_workshop.py --clean      # GEN sections + WORKSHOP_DESCRIPTION_upload.bbcode
   python tools/bbcode_to_markdown.py WORKSHOP_DESCRIPTION_upload.bbcode -o WORKSHOP_DESCRIPTION_upload.md
   python tools/generate_index.py                 # docs/index.html
   python tools/generate_dev_diaries.py           # docs/dev-diaries.html (only if dev diaries changed)
   ```
   Sanity-check the outputs contain the new feature (`grep -c "<FeatureName>" WORKSHOP_DESCRIPTION_upload.md docs/index.html`).

7. **Commit** (only when the user asks). Then **upload** via `tools/release.py` (wraps `upload.py`):
   - `python tools/release.py` — mod content (default)
   - `-wp` workshop pages · `-cn` change notes · `-d` dev item · combine flags as needed (e.g. `-m -wp`).

## Dependencies

The generators need `bbcode` and `html2text` (`pip install bbcode html2text`). `markdown` is only required
if you feed `generate_index.py` a `.md` source; the default `.bbcode` path does not need it.

## Notes

- Never hand-edit content between `<!-- GEN:… -->` markers or any `*_upload.*` / `docs/*.html` file — rerun the generator instead.
- Keep numeric values in narrative prose in sync with the actual script (the generators only auto-format the GEN sections, not your hand-written sections).
