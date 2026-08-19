# Image stubs for the "Subjects, and the Reckoning" dev diary

The diary at `docs/dev_diaries/subjects-and-the-reckoning.md` references the files below.
Until they exist the generated page will show broken images, so drop them in here and
re-run `python tools/generate_dev_diaries.py`.

## In-game screenshots to capture

Naming follows the Balance of Power convention: `EUV_<gameversion>_FU_Bonds_<modversion>_<name>.png`.
If you capture on a different game build, rename the `1.3.x` part consistently in both the
files and the diary.

Status | File | What to capture |
|---|---|---|
|-X-| `EUV_1.3.x_FU_Bonds_0.3.11_ledger_overview.png` | The Subject Relations Ledger with several subjects listed, ideally a mix of positive and negative scores, showing the establishment dates. |
|-X-| `EUV_1.3.x_FU_Bonds_0.3.11_subject_type_list.png` | The subject type selection UI showing the expanded roster. A view with several mod types visible at once is best. |
|-X-| `EUV_1.3.x_FU_Bonds_0.3.11_commune_artwork.png` | An Artists' Commune event delivering a work of art, or the resulting artwork in the capital's art view with the attributed court artist. |
|-X-| `EUV_1.3.x_FU_Bonds_0.3.11_ledger_actions.png` | The action row under one subject (Underwrite / Review / Charter / Festival / Envoy / Tribute / Reprimand), ideally with one tooltip open showing a cost. |
|-X-| `EUV_1.3.x_FU_Bonds_0.3.11_ledger_dimension_tooltip.png` | A dimension score hovered so the "raised by / lowered by" tooltip is visible. |
|-X-| `EUV_1.3.x_FU_Bonds_0.3.11_chain_event_ward.png` | The march lord's heir arriving at court (cc_bonds.100 "The Young Heir", or cc_bonds.66 "The March Lord's Heir"). |
|---| `EUV_1.3.x_FU_Bonds_0.3.11_aor_loyal_colony.png` | cc_bonds.90 "A Loyal Colony in Turbulent Times". Ideally the `voice` variant, which fires when the colony was granted an assembly. |
|---| `EUV_1.3.x_FU_Bonds_0.3.11_aor_colony_revolt.png` | cc_bonds.91 "The Colony Finds Its Voice", showing all three options including the release option (needs the top severity band). |
|---| `EUV_1.3.x_FU_Bonds_0.3.11_aor_march_banner.png` | cc_bonds.97 "The March Lord Raises His Own Banner", ideally with the third option visible (cut him loose as a revolutionary state). |

Optional extras if they photograph well: a Federal Member promotion (cc_bonds.144),
the Federal Charter unravelling (cc_bonds.143), or the Palatinate declaring armed
neutrality (cc_bonds.95).

## Public-domain art to source

Both are well out of copyright; Wikimedia Commons has high-resolution scans. Downscale to
roughly 1200px wide to match the existing `battle_of_leipzig.jpg`.

| File | Suggested work |
|---|---|
| `art_storming_of_the_bastille.jpg` | Jean-Pierre Houël, *Prise de la Bastille* (1789). The Charles Thevenin version is a more dramatic alternative. |
| `art_signing_of_the_constitution.jpg` | Howard Chandler Christy, *Scene at the Signing of the Constitution of the United States* (1940, depicting 1787). John Trumbull's *Declaration of Independence* works too, but reads as secession rather than federation, so it fits the revolutionary column better than the federal one. |

If you would rather lead the federal column with something European, the *Congress of Vienna*
engraving by Jean-Baptiste Isabey is period-correct, though it is already thematically
claimed by the Balance of Power diary.
