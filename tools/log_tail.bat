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
$exclusions = @(
    "Unknown formatting tag 'l'",
    "Too low relation use_count == 2",
    "Could not push the provided stack context",
    "waves_vfx",
    "foam_stop",
    "sakuya",
    "country_parliament_mod.txt",
    "cheat_menu_l_english",
    "kaiserreich_austria_l_english",
    "MBHW_",
    "OHL_",
    "fred_generic_",
    "Missing Icon for Modifier",
    "Streamed texture has no mipmaps",
    "auto_marry",
    "kaiserreich_",
    "hab_",
    "00_default_parliament_mod",
    "ohl_",
    "HBMW_",
    "ism_disable_interactions",
    "rise_of_the_ottomans",
    "_types/ab",
    "ab_events",
    "_ism_",
    "production_method has",
    "nd_bnh",
    "nd_rom",
    "D008_fate_of_the_phoenix_actions",
    "generic_actions/hundred_years_war",
    "Country 'AU",
    "'AUE' has no ",
    "'AUH' has no ",
    "situations/hussite_wars",
    "_kaiserreich.txt' should be in utf8-bom",
    "does not match game version",
    "file: common/subject_types/tributary.txt",
    "Subject type 'tributary' is invalid for '",
    "They will Core on the first monthly tick",
    "has no pops of its official religion",
    "nd_nin",
    "is not explicitly listed in an ai list",
    "Failed to find message type:",
    " ism_",
    "localization_util.cpp",
    "great_turkish_war",
    "hegemony_",
    "has a too high efficiency for ",
    "gui/town_rights.gui",
    "has no pops of its primary culture",
    "but the dominant culture for",
    "has no society values scripted",
    "has no parliament_type scripted",
    "Event nd_",
    "Variable 'nd_",
    "pops in the setup",
    " wrong ruler-term defined for its current",
    "common/subject_types/dominion.txt:68",
    "is set but is never used.",
    "The advance 'chancery_records'",
    "bramod",
    " common/formable_countries/00_formable_countries.txt",
    "_parliament_mod.txt",
    "setup/countries/austria",
    "ace_debug",
    "00_austria_formables",
    "country_TEU",
    "_kaiserreich.txt",
    "country_HAB_kaiserreich",
    "ace",
    "DHE/00",
    "country_HAB",
    "country_VEN",
    "country_CRO",
    "country_AUE",
    "country_AUH",
    "monthly_towards_pru_",
    "AUE has the name 'empire'",
    "automarry_on_actions",
    "/on_action/_hardcoded.txt",
    "on_action/country_four_yearly.txt",
    ".gui:",
    "location with no owner",
    "ask_join_war_for_favors",
    "used but is never set.",
    "context pointer",
    "missing an outcome",
    "/00_event_illustration_effects.txt",
    "lombardo_venezia",
    "boehmen_kronjuwel",
    "prager_hof_kanzlei",
    "duplicated production method name 'naval_governor_maintenance'",
    "Duplicated key ribeira_das_naus",
    "should be in utf8-bom encoding",
    "zzz_hre",
    "decline_of_empire.9",
    "audio2_wwise.cpp:757",
    "audio2_wwise.cpp:1970",
    "state_event.h:391",
    "Trying to reshape data model with negative count -1",
    "No context supplied (Use SetDataContext),",
    "FetchData failed for 'RowList.GetTitle'",
    "PdxDataFetchLocalizedData",
    "Promote 'INTERNATIONAL_ORGANIZATION' returned nullptr",
    "FetchData failed for 'INTERNATIONAL_ORGANIZATION.GetName'",
    "NOT_HAS_SPECIAL_STATUS_IN_INTERNATIONAL_ORGANIZATION_TRIGGER",
    "flavor_brapru.txt:883"
)

if (Test-Path $logFile) {
    Write-Host "Streaming log file: $(Resolve-Path $logFile)" -ForegroundColor Cyan
    Write-Host "Press [Ctrl + C] to stop streaming.`n" -ForegroundColor Yellow
    
    # The '-Wait' switch tells PowerShell to keep tracking the file live
    Get-Content $logFile -Wait | ForEach-Object {
        $line = $_
        
        $matched = $false
        foreach ($exclude in $exclusions) {
            if ($line.Contains($exclude)) {
                $matched = $true
                break
            }
        }
        
        if (-not $matched) {
            if ($line -match '^[^\]]*\](.*)$') {
                Write-Output $Matches[1].TrimStart()
            }
        }
    }
} else {
    Write-Error "Could not find file: $logFile"
}