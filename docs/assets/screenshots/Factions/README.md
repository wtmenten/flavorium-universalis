# Image stubs for the "Factions" dev diary

The diary at `docs/dev_diaries/factions.md` references the files below.
Until they exist the generated page will show broken images, so drop them in here and
re-run `python tools/generate_dev_diaries.py`.

## In-game screenshots to capture

Naming follows the other diaries: `EUV_<gameversion>_FU_Factions_<modversion>_<name>.png`.
If you capture on a different game build, rename the `1.4.x` part consistently in both the
files and the diary. The `0.1.0` part should match the submod version that ships.

**Getting a save worth photographing.** Load Flavorium Universalis and the Factions submod
and play or observe a tracked country (yours, a great power, or 100+ development). Parties
are seeded at game start, and the first silent review lands 6 to 18 months in. To skip the
wait, open the console (the key left of 1; if it does not open, add `-debug_mode` to the
game's Steam launch options) and run these. `effect` runs a script in your own country's scope;
there is no outer `effect = { }` block:

- `effect cc_pty_sat_pass = yes` runs a satisfaction review now: power, moods, agendas,
  escalation, Liberal Thought.
- `effect cc_pty_realign_pass = yes` recounts the seats and reselects the four parties.
- `effect remove_variable = cc_pty_popup_cd` clears the event budget so the next review can
  announce an agenda.
- `event cc_pty.40` (or .41, .42, .43) shows an escalation outcome directly. Firing .41
  for real starts a civil war, so screenshot it and pick the concession.
- `activate_disaster cc_pty_praetorian_coup` (or `cc_pty_liberal_uprising`) starts a disaster
  for the disaster panel.

Liberal Thought only exists from the Age of Absolutism. An observer run to about 1650 gives
a map with enough variation to read.

| Status | File | What to capture |
|---|---|---|
|---| `EUV_1.4.x_FU_Factions_0.1.0_politics_panel.png` | The Factions panel's chamber: the seat grid with all four parties' icons, four cards each showing a leader portrait, an agenda across the top, and the five-button action bar. Ideally one party marked Leading and a mix of moods. A mid-sized realm (chamber of 50-70 seats) shows both filled and empty seats. |
|---| `EUV_1.4.x_FU_Factions_0.1.0_member_badge.png` | A minister's character window or tooltip with the party badge (for example "Merchant Interest") and a party mood modifier ("Party Pleased" or "Party Discontent") both visible. |
|---| `EUV_1.4.x_FU_Factions_0.1.0_agenda_event.png` | The agenda event (cc_pty.20) with the party name and agenda line readable, and the hover tooltip of the first option open if it fits. |
|---| `EUV_1.4.x_FU_Factions_0.1.0_action_tooltip.png` | The Bribe or Attack button tooltip on the action bar, showing the political influence cost. A disabled Appoint Leader with its requirement shown is a good alternative. |
|---| `EUV_1.4.x_FU_Factions_0.1.0_escalation_warning.png` | A party card marked Escalating (War Party, Regional Party or Liberal Party, angry with a fifth of the seats). Hover the marker so its tooltip shows. |
|---| `EUV_1.4.x_FU_Factions_0.1.0_liberal_thought_map.png` | The Factions situation map mode after 1650 with cities shaded by Liberal Thought, and the legend visible. |
|---| `EUV_1.4.x_FU_Factions_0.1.0_hooks_and_cods.png` | The Factions panel as Holland (HOL) before the Age of Reformation, with the Hook Party and the Cod Party both listed. The Aristocratic Faction and the Merchant Interest both have to be among the four, which they usually are at start. |

## Optional extras if they photograph well

None of these are referenced by the diary, so they are additions rather than gaps. If any
turn out well, the diary section they belong to is named beside each one.

| File | What to capture | Diary section |
|---|---|---|
| `EUV_1.4.x_FU_Factions_0.1.0_realignment_event.png` | The New Parties event (cc_pty.10) listing four party names. Easiest with the realignment console command after the age changes. | Four parties out of eleven |
| `EUV_1.4.x_FU_Factions_0.1.0_defection_event.png` | Crossing the Floor (cc_pty.30), with the minister's name and both party names readable. Needs an angry party with a seated minister. | Every minister belongs to a party |
| `EUV_1.4.x_FU_Factions_0.1.0_coup_event.png` | The Officers Move (cc_pty.40) or the coup disaster panel. | Parties you cannot ignore |
| `EUV_1.4.x_FU_Factions_0.1.0_term_limits.png` | The Term Limits event (cc_pty.60), or the panel's Cabinet line showing Term limits. | Liberal Thought |
| `EUV_1.4.x_FU_Factions_0.1.0_hats_and_caps.png` | Sweden after 1650 with the Hat Party and the Cap Party listed. | Names |

## Notes

- The panel and its numbers update at each review, not monthly. If a screenshot needs a
  particular mood, bribe or attack the party: both apply at once.
- The situation icon is vanilla's Royal Academy of Arts building icon, copied to
  `submods/factions/main_menu/gfx/interface/icons/situations/cc_pty_factions.dds`. There is
  no header illustration yet; when there is one,
  `python tools/make_dds.py <art>.png --slot situation-bg --key cc_pty_factions --submod factions`
  places it, and the panel picks it up by name.
