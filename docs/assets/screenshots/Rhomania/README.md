# Image stubs for the "Rhomania" dev diary

The diary at `docs/dev_diaries/rhomania.md` references the files below.
Until they exist the generated page will show broken images, so drop them in here and
re-run `python tools/generate_dev_diaries.py`.

## Setup for capturing these

Everything here needs **Fate of the Phoenix** enabled and the **Flavorium Universalis - Rhomania**
submod active. Start as BYZ in 1337. Several shots need mid or late game state, so a console
run is the practical way to get them:

- `event cc_byz_union.20` and similar to force a specific event without playing to it.
- The exarchate needs the `cc_byz_renovatio_imperii` advance (age 2) and 75% ownership of an
  Italian or Maghreb area.
- The mission tree only appears with the **Mission Packs** game rule set to enabled. The
  theatre actions only appear with it **disabled**, so those two shots need separate runs.
- The Levantine Confrontation needs `rise_of_the_ottomans` to have ended and 15+ Anatolian
  locations owned.
- The eastern branch of the tree hangs off **The Sinai Road**, which sits at the end of the
  Levant chain (Antioch, Jerusalem, Egypt, the Sinai). The theatre trigger needs Alexandria,
  Cairo **and** `sinai_desert` held together; holding Egypt without the Sinai will not open it.
- Stepping stones gate the cornerstones, so a console run that jumps straight to owning Italy
  will show the Italy cornerstone still locked until its stones are done. That is intended,
  and worth knowing before assuming the tree is broken.

## In-game screenshots to capture

Naming follows the Balance of Power convention: `EUV_<gameversion>_FU_Rhomania_<modversion>_<name>.png`.
If you capture on a different game build, rename the `1.3.x` part consistently in both the
files and the diary.

| Status | File | What to capture |
|---|---|---|
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_societal_values_both_axes.png` | The societal values panel with **both** axes visible: vanilla's Latinitas/Rhomanismos and the new Taxis/Dynatoi. Ideally hover one pole so the modifier list is showing. This is the single most important shot, since it proves the custom axis loaded. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_appoint_exarch.png` | The **Appoint an Exarch** character interaction, with the three selection columns populated: a character, one of the three terms of appointment, and a target area. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_exarchate_map.png` | The exarchate as a live subject. Either the map with its borders in Italy and Constantinople still the capital, or the subject panel showing its type and government reform. A shot that makes the capital point obvious is better. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_union_promulgation.png` | `cc_byz_union.20`, the promulgation in Hagia Sophia. The `desc_hostile` variant reads best (needs anti-unionist resistance at 3+). Failing that, `cc_byz_union.21` "What the City Did" with the divided or rejected description. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_bureaucracy_entrenchment.png` | A bureaucracy card with its tooltip open, showing the funding scale and the entrenchment line. Best is an **unfunded, highly entrenched** office so the malus scaling is visible. A side-by-side with a funded one would be ideal if the UI allows it. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_mission_tree.png` | The **Renovatio Imperii** pack zoomed out far enough to show its shape: 71 tasks, five roots, three parallel pillars, and the branches reconverging. This is the shot that has to sell the tree as a network rather than a list, so frame width over legibility. Needs Mission Packs enabled. Task icons are not yet supplied and will render blank. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_stepping_stones.png` | Close on **the three pillars** (Fisc, Faith, Sword) running side by side into The State Restored. Hovering The State Restored so its two-of-three tooltip is visible is the single most useful detail here, since it shows the subset requirement working. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_exclusive_fork.png` | Any one of the five exclusive forks with **both** options still visible and neither taken: Venice/Genoa, end/vassalise the Turks, Tagmata/Pronoia, treaty/Pentarchy War, or monopoly/company. Must be captured before choosing, because taking one hides the other permanently. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_mamluk_situation.png` | The **Levantine Confrontation** situation panel showing both progress tracks. Phase 1 is fine; phase 2 with the Pentarchy War underway is better. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_exarch_demand.png` | `cc_byz_demand.1` "The Exarch's Request". Worth setting up so **all four** options are visible, which needs either a capable ruler or the right cabinet member: a `charismatic_negotiator`, `fierce_negotiator` or `silver_tongue` for option c, an `administrator` for option d. The `desc_after_seizure` variant is the best-written one but needs the thread run to `.3` first. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_eastern_branch.png` | The **eastern branch** of the mission tree: the four tasks from the Red Sea strait through to the spice islands, framed to show them growing out of **The Sinai Road** at the end of the Levant spine rather than standing apart. Needs the Levant chain complete: Antioch, Jerusalem, Egypt and the Sinai. |
|---| `EUV_1.3.x_FU_Rhomania_0.1.0_spice_trade.png` | `cc_byz_east.30` "The Source". Three description variants: the `desc_monopoly` one (after closing the strait to Latin shipping) is the most dramatic, `desc_treaty` the most characterful. Option c only appears on the monopoly path with a capable ruler. |

### Optional extras, if they photograph well

| File | What to capture |
|---|---|
| `EUV_1.3.x_FU_Rhomania_0.1.0_theatre_actions.png` | The theatre generic actions in the religious panel, with Mission Packs **disabled**. Worth having because it is the path most players see, and the diary claims parity between the two front-ends. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_tagmata.png` | Tagmata regiments in the recruitment list, or the Rhomanismos advance line with the Greek-gated entries unlocked. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_papal_guard.png` | `cc_byz_papal.10` "The Last of the Patrimony", the Western Schism guard. Three options, and the third one is the destructive choice. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_creditor_leverage.png` | `cc_byz_debt.2` "The Exemption in Writing", or `cc_byz_debt.5` "The Quarter Across the Water" with the captured ending. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_exarch_ending.png` | `cc_byz_exarch.5`, ideally the `desc_dynasty` variant where the exarchate has become hereditary. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_strain_event.png` | `cc_byz_reconquest.51` "The Army of the West", or `.50` with the `desc_ruined` variant naming Italy as the reason the account does not balance. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_exarch_prompt.png` | `cc_byz_exarch.10` "Who Governs Italy?", the prompt that offers an exarchate unasked. The `desc_rome` variant fires when Rome itself is held. Shows the nominated cabinet character and the three terms of appointment as options. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_malabar.png` | `cc_byz_east.20` "The Malabar Coast". The `desc_force` variant, which fires if you arrived with a fleet, is the better read of the two. |
| `EUV_1.3.x_FU_Rhomania_0.1.0_indian_charter.png` | A colonial charter actually planted on the Malabar coast or in the spice islands by the eastern theatre effects, seen on the map or in the charter list. Useful because it proves the `create_colonial_charter` call resolved to a real province definition. |

## Public-domain art to source

All well out of copyright; Wikimedia Commons has high-resolution scans. Downscale to roughly
1200px wide to match the existing `battle_of_leipzig.jpg` in the BoP folder.

| File | Suggested work |
|---|---|
| `art_justinian_san_vitale.jpg` | The Justinian mosaic panel from the Basilica of San Vitale, Ravenna (c. 547). Referenced by the diary. Ravenna is also an exarchal seat and a mission target, so it does double duty. The Theodora panel opposite is an alternative if the Justinian one crops badly. |

### If you want more art than the diary currently uses

| Suggested work | Where it would fit |
|---|---|
| Benozzo Gozzoli, *Procession of the Magi* (1459), the John VIII Palaiologos figure | The union section. Gozzoli painted the emperor from life at the Council of Florence, which makes it the most directly relevant surviving image of the union. |
| Gentile Bellini or the *Hagia Sophia interior* engravings by Gaspare Fossati (1852) | The promulgation section, if the union column needs a second image. |
| The Barberini Ivory, or any Justinianic consular diptych | The reconquest section, as a counterpart to San Vitale. |
| A period portolan chart of the eastern Mediterranean | The Levant section, and it would suit the trade and frontier material better than a battle scene. |

Avoid anything depicting 1453. The whole premise of this submod is an empire that does not
end there, and leading a section with the fall would work against the copy.

## Mission and situation art still missing from the submod itself

Separate from the diary, these are referenced by the submod's own script and render **blank
without logging an error**, so they need checking by eye rather than in `error.log`:

- `submods/rhomania/main_menu/gfx/interface/icons/missions/cc_byz_renovatio_campaign.dds`
- `submods/rhomania/main_menu/gfx/interface/icons/missions/cc_byz_task_{illyricum,italy,africa,spania,mare_nostrum}.dds`
- `submods/rhomania/main_menu/gfx/interface/icons/missions/cc_byz_task_{red_sea,horn,india,spice_islands}.dds`
- 25 stepping-stone icons: `cc_byz_task_{walls,hippodrome,council,bureaus,arsenal}.dds`,
  `cc_byz_task_{no_second_emperor,duchy_dissolved,despotate,greek_again}.dds`,
  `cc_byz_task_{beylik_ended,themes,pronoia_host}.dds`,
  `cc_byz_task_{antioch,holy_city,patriarch,egypt,lighthouse,sinai_road}.dds`,
  `cc_byz_task_{adriatic,exarch_seated,carthage,pillars}.dds`,
  `cc_byz_task_{galata,merchant_fleet,spice_dues}.dds`
- `submods/rhomania/main_menu/gfx/interface/illustrations/missions/cc_byz_renovatio_campaign.dds`

Seventy-three files in total: one pack icon, one pack illustration and seventy-one task icons.

Three visual registers would carry the tree's structure better than one set of shields:
the nine cornerstones want weight and can share a frame; the eastern four want trade imagery
(a ship, a chart, a warehouse, a spice bale) since that branch is commerce rather than
conquest; and the smaller tasks want to read as clearly *lighter* than a cornerstone at a
glance, because that distinction is what tells the player which tasks are the campaign and
which are the housekeeping.

The three pillar capstones (Logothete of the Course, the Ecumenical Throne, the Field Army
Restored) and the four reconvergences want to sit visually between the two, since they are
structurally important without being theatres.

The ten exclusive-fork icons are worth pairing deliberately: Venice against Genoa, Tagmata
against Pronoia. A player seeing them side by side should read them as two answers to one
question.

If the full set is too much to commission at once, the order is: pack icon, nine cornerstones,
three pillar capstones, ten fork options, then everything else. A blank filler task is untidy;
a blank cornerstone or a blank fork is the player not knowing what the tree is about or what
they are choosing between.

The six societal-value icons and illustrations for Taxis/Dynatoi **are** in place, but they are
placeholders copied from vanilla's `centralization_vs_decentralization` set and should be
replaced before release.
