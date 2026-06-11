<# : batch_initiator
@echo off
set "LOG_PATH=%~1"
set "BAT_PATH=%~f0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-Expression (Get-Content $env:BAT_PATH -Raw)"
exit /b
#>

# --- PowerShell Code Starts Here ---

# Grabs the path from the batch file argument, defaults to "error.log" if empty
$logFile = if ($env:LOG_PATH) { $env:LOG_PATH } else { "error.log" }

# Define the array of strings to exclude
# If any line in a log chunk (all lines sharing a timestamp) matches, the whole chunk is suppressed.
$exclusions = @(
    "waves_vfx", "foam_stop",
    "sakuya", "ace_debug", "cheat_menu_l_english",

    "00_default_parliament_mod", "country_parliament_mod.txt", "_parliament_mod.txt",

    "HBMW_", "MBHW_",

    "rise_of_the_ottomans", "ohl_", "OHL_",
    "_types/ab", "ab_events",

    "production_method has",
    "nd_bnh", "nd_rom",
    "D008_fate_of_the_phoenix_actions",
    "generic_actions/hundred_years_war",
    "situations/hussite_wars",

    "nd_nin", " ism_", "_ism_", "ism_disable_interactions",
    "is not explicitly listed in an ai list", "Failed to find message type:", "does not match game version",

    "localization_util.cpp", "should be in utf8-bom encoding",

    "Event nd_", "Variable 'nd_",
    "great_turkish_war", "hegemony_",
    "They will Core on the first monthly tick", "has no pops of its official religion", "has a too high efficiency for ",
    "has no pops of its primary culture", "but the dominant culture for", "has no society values scripted", "has no parliament_type scripted", "pops in the setup",

    "Subject type 'tributary' is invalid for '",
    " wrong ruler-term defined for its current",
    "file: common/subject_types/tributary.txt",
    "common/subject_types/dominion.txt:68",

    "The advance 'chancery_records'",

    " common/formable_countries/00_formable_countries.txt",
    "common/formable_countries/99_nd_dnm.txt",

    "DHE/00", "bramod", "monthly_towards_pru_",

    "Country 'AU", "'AUE' has no ", "'AUH' has no ", "kaiserreich_", "hab_", "kaiserreich_austria_l_english", "_kaiserreich.txt' should be in utf8-bom",

    "country_HAB", "country_VEN", "country_CRO", "country_AUE", "country_AUH", "country_HAB_kaiserreich",
    "country_TEU", "00_austria_formables", "_kaiserreich.txt", "setup/countries/austria", "AUE has the name 'empire'",
    "zzz_hre",

    ".gui:", "gui/town_rights.gui",

    "automarry_on_actions", "auto_marry",

    "/on_action/_hardcoded.txt",
    "on_action/country_four_yearly.txt",

    "ask_join_war_for_favors",

    "used but is never set.", "is set but is never used.", "missing an outcome", "location with no owner",
    "duplicated production method name 'naval_governor_maintenance'",

    "decline_of_empire.9",
    "/00_event_illustration_effects.txt",
    "lombardo_venezia", "boehmen_kronjuwel", "prager_hof_kanzlei", "Duplicated key ribeira_das_naus",
    "fred_generic_",
    

    "events/character/noble_marriage.txt:400", "events/character/artist_events.txt:2835", 
    "events/government/parliaments.txt:3129", "events/government/parliaments.txt:22",
    "common/scripted_triggers/country_triggers.txt:1300",
    "common/generic_actions/treaty_of_tordesillas.txt",
    "common/generic_actions/italian_wars.txt:1",
    "common/international_organizations/hre.txt:1047",
    "events/disaster/succession_crisis.txt:875", "trying to assign a pop",
    "events/wokou_events.txt:285",
    "Failed to convert statement for argument '0' for call '",
    "Failed converting statement for 'Select_int32(InjectedButton.HasLabel",
    "Malformed token: [Select_int32(InjectedButton.HasLabel",
    "BuildInLocationLateralView",
    "InjectedButtonsRegistry",
    "InjectedButton",
    "JominiNotification.IsPassword",
    "GetCustomGui",
    "twilight_of_the_tsardom.txt:504",
    "common/building_types/rural_buildings.txt:23",
    "events/government/societal_values.txt:1634",
    "Script location: <unknown>:0",
    "events/mercs.txt:",
    "turmoil_in_brandenburg",
    "buddhism_events", "fall_of_delhi",
    "earthquake_events", "volcano_events",
    "06_peasants_estate_parliament_issues",
    "04_culture_religion",

    "Failed to read key reference: : , near line: 3",
    "common/international_organizations/hre.txt:3",
    "decline_of_empire_events.txt:",
    "events/imperial_circles_events.txt",
    "events/religion/hussite_flavor",
    "common/on_action/character_death_pulses",
    "events/government/parliaments.txt",
    "common/scripted_effects/country_effects.txt:144",
    "events/DHE/flavor_tim",
    "events/disaster/decline_of_mali",
    "events/situations/western_schism",
    "events/DHE/flavor_chi_treasure_expedition",
    "events/DHE/flavor_ira.txt:832",

    "common/heir_selections/specialized.txt:339",
    "common/building_types/rural_buildings.txt:22",
    "common/coat_of_arms/template_lists/colored_emblem_lists.txt",
    "events/disaster/byzantine_succession_crisis.txt:",
    "events/situations/black_death.txt:",
    "common/coat_of_arms/template_lists/",
    "common/scripted_triggers/country_triggers.txt:13",
    "to increase their 'accepted_cultures_capacity'",
    "scaligeri_peace_treaties.txt",
    "common/situations/nanbokuchou.txt:31",
    "events/hre.txt",
    "situations/red_turban_rebellions",
    "government/steppe_horde.txt",
    "/culture/culture_religion_events.txt",
    "/DHE/flavor_vij",
    ".MakeScope.GetVariable('strongest_beylik_variable')",
    "strongest_beylik_has_over_75_locations",
    "events/DHE/flavor_chi.txt:55",
    "events/character/artist_events.txt:",
    "events/DHE/flavor_JAP.txt:296",
    "events/DHE/flavor_bav.txt:2173",
    "common/scripted_effects/situation_effects.txt:206",
    "common/disasters/decline_of_mali.txt",
    "common/scripted_triggers/disaster_triggers.txt:607",
    "common/laws/23_lordship_of_ireland.txt:107",
    "events/DHE/flavor_flo.txt",
    "events/DHE/flavor_TUR.txt",
    "common/parliament_agendas/03_buildings",
    "events/religion/lutheranism_events.txt",
    "gfx/interface/icons/unit_actions/lend_unit_to_ally.dds",
    "events/wokou_events.txt",
    "common/generic_actions/create_province_subject.txt",
    "common/scripted_triggers/international_organization_triggers",
    "events/religion/muslim_flavor.txt",
    "events/DHE/flavor_SCO.txt",
    "events/DHE/flavor_JAP.txt",
    "[movement.cpp:156]",
    "events/situations/italian_wars.txt:",
    "common/scripted_effects/on_action_effects.txt",
    "events/religion/autocephalous_patriarchates",
    "common/generic_actions/western_schism.txt",
    "common/generic_actions/war_of_religions.txt",
    "common/generic_actions/rise_of_timur.txt",
    "common/generic_actions/the_revolution.txt",
    "common/generic_actions/red_turban_rebellions.txt",
    "common/generic_actions/hussite_wars_actions.txt",
    "common/generic_actions/guelphs_and_ghibellines.txt",
    "common/generic_actions/golden_age_of_piracy.txt",
    "common/generic_actions/reformation.txt",
    "common/generic_actions/colonial_revolution.txt",
    "events/government/societal_values.txt",
    "common/peace_treaties/hegemon_demands.txt",
    "common/country_interactions/italian_wars_country_interactions.txt:59",
    "common/situations/italian_wars.txt",
    "common/customizable_localization/character_title.txt",
    "Error: Event target link 'scope' returned an invalid object",
    "events/religion/nahuatl_events",
    "common/generic_actions/languages.txt",
    "common/country_interactions/catholic_interactions.txt",
    "common/generic_actions/parliament.txt",
    "common/country_interactions/intervene_in_union_civil_war",


    "Unknown formatting tag 'l'", "Too low relation use_count == 2", "Missing Icon for Modifier", "Streamed texture has no mipmaps",
    "audio2_wwise.cpp:757", "audio2_wwise.cpp:1970", "state_event.h:391", "context pointer", "Could not push the provided stack context",
    "Trying to reshape data model with negative count -1", "No context supplied (Use SetDataContext),", "FetchData failed for 'RowList.GetTitle'", "PdxDataFetchLocalizedData",
    "Promote 'INTERNATIONAL_ORGANIZATION' returned nullptr", "FetchData failed for 'INTERNATIONAL_ORGANIZATION.GetName'", "NOT_HAS_SPECIAL_STATUS_IN_INTERNATIONAL_ORGANIZATION_TRIGGER",
    " FetchData failed for 'CanBuildOrExpandBuildingInfo(ConstructScoreRanking.GetBuildingType,", "FetchData failed for 'BuildingType.GetName'",
    "invalid type for the country: iconographer", "Ruler term has overlapping dates, please fix.", " Ruler term is active but there are subsequent ruler terms",
    "flavor_brapru.txt:883"
)

if (Test-Path $logFile) {
    Write-Host "Streaming log file: $(Resolve-Path $logFile)" -ForegroundColor Cyan
    Write-Host "Press [Ctrl + C] to stop streaming.`n" -ForegroundColor Yellow

    $printLine = {
        param($l)
        if ($l.Trim() -eq '') { return }
        if ($l -match '^[^\]]*\](.*)$') { Write-Output $Matches[1].TrimStart() } else { Write-Output $l }
    }

    function Test-ChunkExcluded ($chunk) {
        foreach ($line in $chunk) {
            foreach ($exclude in $exclusions) {
                if ($line.Contains($exclude)) { return $true }
            }
        }
        return $false
    }

    function Flush-Chunk ($chunk) {
        if ($chunk.Count -gt 0 -and -not (Test-ChunkExcluded $chunk)) {
            foreach ($l in $chunk) { & $printLine $l }
        }
        $chunk.Clear()
    }

    $currentChunk = [System.Collections.Generic.List[string]]::new()

    Get-Content $logFile -Wait | ForEach-Object {
        $line = $_
        # A line starting with '[' begins a new log entry / chunk
        if ($line -match '^\[') {
            Flush-Chunk $currentChunk
        }
        $currentChunk.Add($line)
    }

    # Flush remaining buffer on exit
    Flush-Chunk $currentChunk
} else {
    Write-Error "Could not find file: $logFile"
}
