# Image stubs for the "A Career at Court" dev diary

The diary at `docs/dev_diaries/a-career-at-court.md` references the files below.
Until they exist the generated page will show broken images, so drop them in here and
re-run `python tools/generate_dev_diaries.py`.

## In-game screenshots to capture

Naming follows the Balance of Power convention: `EUV_<gameversion>_FU_Court_<modversion>_<name>.png`.
If you capture on a different game build, rename the `1.3.x` part consistently in both the
files and the diary. The `0.3.11` part should be bumped to whatever version actually ships
this system.

**Most of these need a mature save.** Seniority 5 takes decades, and the weariness and
rivalry events need a minister twenty years in post. An observer-mode run fast-forwarded
to the 1600s is the quickest way to get a court worth photographing.

| Status | File | What to capture |
|---|---|---|
|---| `EUV_1.3.x_FU_Court_0.3.11_court_panel.png` | The Court panel's default tab with a full cabinet and at least one protege, so both sections are visible. Ideally a mix of levels, and at least one minister showing an `away` or `mentored` status mark. |
|---| `EUV_1.3.x_FU_Court_0.3.11_ladder_fork.png` | Any of the nine branch events (cc_xp.20 to cc_xp.28), with one option hovered so the `[ShowTraitName]` tooltip is open and the actual trait modifiers are readable. The Treasury fork (invest or audit) and the command fork (whole establishment or the field army) read best. |
|---| `EUV_1.3.x_FU_Court_0.3.11_service_record.png` | The Read the Service Record event (cc_xp.1) for a minister with uneven tracks, so seniority and specialisation are visibly different numbers. A senior minister with tier 0 in one track is the ideal subject. |
|---| `EUV_1.3.x_FU_Court_0.3.11_schools_tab.png` | The Schools tab. Best case has one school founded and the other two slots showing their unlock requirements, which demonstrates the whole ladder at once. |
|---| `EUV_1.3.x_FU_Court_0.3.11_soiree.png` | The soiree event (cc_xp.50) with all three options visible and their costs readable. |
|---| `EUV_1.3.x_FU_Court_0.3.11_patronage_tab.png` | The Patronage tab with two or more living artists listed, showing the works total and at least one artist mid-commission. A sponsored artist showing the `sponsored` mark would be better still. |

## Optional extras if they photograph well

None of these are referenced by the diary, so they are additions rather than gaps. If any
turn out well, the diary section they belong to is named beside each one.

| File | What to capture | Diary section |
|---|---|---|
| `EUV_1.3.x_FU_Court_0.3.11_posting_return.png` | A posting return (cc_xp.30 to cc_xp.32), ideally the `good` or `poor` variant rather than the ordinary one. | Spending money on people |
| `EUV_1.3.x_FU_Court_0.3.11_weariness.png` | Weariness at the top (cc_xp.40), showing both the leave and the keep-them-working options. | Running out of road |
| `EUV_1.3.x_FU_Court_0.3.11_rivalry.png` | Rivalry of equals (cc_xp.42), which has three options and so fills the frame well. | Running out of road |
| `EUV_1.3.x_FU_Court_0.3.11_envoy_oversteps.png` | The envoy oversteps (cc_xp.61). Needs a minister seconded to a bond-tracked subject. | Sending a minister away |
| `EUV_1.3.x_FU_Court_0.3.11_cabinet_badge.png` | The government view's cabinet tab showing the seniority badge on a minister's card. Only appears if this mod's `cabinet_card_header_content` wins the load order, so it will be absent with Glorp UI loaded after Flavorium. | Two numbers |

## Notes

- The Court panel only appears once a court actually has tracked ministers, and it is
  hidden entirely when the **Cabinet Experience** game rule is off.
- If a panel screenshot shows overlapping rows or clipped buttons, that is a layout bug
  rather than a capture problem. Worth reporting rather than cropping around.
