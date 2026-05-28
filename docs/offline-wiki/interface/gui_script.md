# GUI script

**Source:** https://eu5.paradoxwikis.com/GUI_script

---

||Please help improve this article or section by expanding it with: more tables.|

**GUI script** is the style of scripting used in the game's GUI and localization. This is different from the script used in most other game files, though there are some corresponding objects, such as countries and variables. Similar to game script's scopes, GUI script uses data types; some of these correspond to game scopes while others are used only with GUI script.

GUI script is divded in two types: *Functions* and *Promotes*.

## Common features

All GUI script is written in "CamelCase"[1] – with a few exceptions, where each word in the function or promote is capitalized and no spaces are used. Each piece of GUI script is always enclosed in square brackets. Within the square brackets, the functions and promotes can be chained together with "dot chaining", for example `[State.GetJobseekersDesc]`. When moving from one data type to another, this is similar to dot chaining with scopes.

Some functions and promotes take arguments which are enclosed in parentheses immediately following the function or promote, for example `[GetPopTypeByName('peasants').GetName]`. If the argument is a game script object, it is typically enclosed in single quotes; if it is another data type, function, or promote, it is not. If the function or promote takes multiple arguments, they must be passed in order with each separated by a comma.

Some functions and promotes are "global", meaning they can be used without reference to a data type. All other data type functions and promotes require the correct data type to be in "scope".

## Lists of data types

These tables list all data types used in GUI scripting which have at least one function or promote.

|Type|Description|
|---|---|
|AISettingsMenu||
|AISettingsMenuItem||
|AccountInventory||
|Achievement|Jomini Achievement|
|AchievementPopup||
|AchievementWindow|Jomini Achievement Window|
|ActionGroup||
|ActiveClip||
|ActiveClipEventsKeyframe||
|ActiveHegemon||
|ActiveHegemonItem||
|ActiveInstitution||
|ActiveParliamentAgenda||
|ActiveParliamentAgendaWrap||
|ActiveProductionMethod||
|ActiveResolution||
|ActiveResolutionContainer|Base class for resolution containers|
|ActiveSituation||
|AddFriendWindow|Jomini Friends - Add Friends Window|
|AddUpdateGraphNodeWindow||
|AdjacencyDistanceWrap||
|AdjacencyMarketAccessWrap||
|Advance||
|AdvanceDefinition||
|AdvanceEffectItem||
|AdvanceItem||
|AdvanceLineItem||
|AdvanceNode||
|AdvancesLateralView||
|Age||
|AgeAdvancesWrap||
|AgendaView||
|AiCurrencyClassGlue||
|AiCurrencyGlue||
|AiCurrencyViewer||
|AiDiplomaticObjective||
|AiDiplomaticObjectiveGroup||
|AiDiplomaticObjectivesViewer||
|AiLogistics||
|AiTarget||
|AiTargetType||
|AiTargetsViewer||
|AiTransportTarget||
|AiUtilityWrap||
|AlertActiveIOResolution||
|AlertAnnexingDisloyalSubject||
|AlertArmiesOnIce||
|AlertArmyWithLowFood||
|AlertArmyWithVeryLowFood||
|AlertArmyWithoutLeader||
|AlertAvailableTradeCapacity||
|AlertBlockadedPorts||
|AlertBuildingsMissingInput||
|AlertCanBeTargetOfIO||
|AlertCanInterveneInRivalWar||
|AlertCanJoinTargettedIO||
|AlertClanCanBecomeLanded||
|AlertConstructionMissingInput||
|AlertDangerousRelations||
|AlertDepopulatingLocations||
|AlertExiledUnits||
|AlertFormableCountry||
|AlertHasLowFoodStockpileMarket||
|AlertHasNoSuppliesTrade||
|AlertHasNotEnoughGoodsForAnyShipRepairs||
|AlertHasNotEnoughGoodsForShipRepairs||
|AlertHasRaisedArmyLeviesInPeace||
|AlertHasRaisedNavyLeviesInPeace||
|AlertHasReligiousFocusAvailable||
|AlertHasUneducatedChild||
|AlertHasUnmarriedChildren||
|AlertHasUnprofitableBuildings||
|AlertHasUnraisedLeviesInWar||
|AlertHasWeatherSystem||
|AlertIOBreaking||
|AlertIsAtFortLimit||
|AlertItem||
|AlertLackPopPromotion||
|AlertLackPopRGO||
|AlertManager||
|AlertMemberLeavingUnion||
|AlertMissingExplorer||
|AlertNaviesStuckInIce||
|AlertNavyAttrition||
|AlertNoParliamentDebate||
|AlertOutsideOfNavalRange||
|AlertPopNeeds||
|AlertPossibleLaw||
|AlertRelationAboutToBeBroken||
|AlertRiskStarvingProvinces||
|AlertStarvingProvinces||
|AlertTruceEnding||
|AlertUnintegratedProvinces||
|AlertUnprofitableTrade||
|AlertUnusedCB||
|AnchorItem|Map Editor - Spline Network Tool - Anchor|
|AnimationClip|An animation clip used in animation state machines.|
|AnimationClipReferenceGui|A clip reference in the Animation State Editor|
|AnimationClipsEditor|Animation Clips Editor Window|
|AnimationComplexClipReferenceGui|A Complex clip reference in the Animation State Editor|
|AnimationEditor|Animation Editor Window|
|AnimationEditorCondition|A transition condition in the Animation Editor|
|AnimationEditorConnectionTab|Connection Tab in the Animation Editor|
|AnimationEditorLane|A connection lane in the Animation Editor|
|AnimationEditorMessageTab|Message Tab in teh Animation Editor|
|AnimationEditorState|A state in the Animation State Editor.|
|AnimationEditorStateTab|State Tab in the Animation Editor|
|AnimationEditorTabHelper||
|AnimationEditorVariable|A variable in the animation editor variables panel.|
|AnimationEditorVariablesPanel|Variables panel in the animation editor, providing datamodels and functions for displaying and editing state maching variables.|
|AnimationEditorViewer||
|AnimationRandomClipReferenceGui|A Random clip reference in the Animation State Editor|
|AnimationSimpleClipReferenceGui|A clip reference in the Animation State Editor|
|AnimationState||
|AnimationStateButton|Animation State Button to select active state.|
|AnnexationAlert||
|AnnexationCostWrapper||
|AnnexationMarker||
|AntagonismBombSpec||
|AntagonismBombSpecWrap||
|AntagonismBombsSpec||
|AntagonismTwoCountriesWrap||
|AntagonismWrapper||
|Application||
|ArchetypeEditor|Archetype Editor Tab|
|Area||
|ArmyBuilderLateralView||
|ArmyConstructionMarker||
|ArmyLevyPopBreakdownWrapper||
|ArmyStrength||
|Artist||
|ArtsItem||
|ArtsView||
|AskRepayLoanMessagePopup||
|AssembleEntityWindow|Entity Designer - Assemble Entity Window|
|AttachmentPropertySearchList||
|Attribute|Portrait Editor - Attribute|
|AttributeColumnData||
|AudioCultureType||
|AutocompleteEntry||
|AutomatedMultiSystemItem||
|AutomatedSystemsItem||
|AutomationLateralView||
|AvailabilityEntry|Jomini Friend List - Availibility Entry|
|AvailableMercenaryTypes||
|Avatar||
|BattleParticipant||
|BattleResult||
|BattleResultMessage||
|BattleResultMessageParticipant||
|BattleResultMessageSide||
|BattleSide||
|BattleUnitStats||
|BattleView||
|BiasType||
|BlockList||
|BlockListBlock||
|BlockedVisionMarker||
|BlurThreshold|Map Editor - Blur Threshold|
|BrushBool|Map Editor - Brush bool settings.|
|BrushFloat|Map Editor - Brush float settings.|
|BrushSettings|Map Editor - Brush settings.|
|BrushSettingsDropdown|Map Editor - Brush settings dropdown.|
|BrushSettingsGlobal|Map Editor - Global Brush settings.|
|BuildInLocationLateralView||
|BuildLocationSelectMarket||
|Building||
|BuildingCandidate||
|BuildingCategory||
|BuildingConstructionMarker||
|BuildingItem||
|BuildingPromoteTimeWrapper||
|BuildingSpyNetworkMarker||
|BuildingType||
|BuildingView||
|CDPopEditor||
|CEconomy||
|CEnumValueAnimation||
|CFixedPoint|Number stored with 6 digits of precision.|
|CMapToolTip||
|CPdxEnumValue||
|CPdxFloatRect|Rectangle within an 2D float space.|
|CPdxInputBindingSetting|Jomini Settings - Rebindable Input Binding Setting|
|CPdxIntRect|Rectangle within an 2D integer space.|
|CSceneEditorPreviewPropertiesPanel|Scene Editor Selected Entity Info|
|CString||
|CTest||
|CUTF8String||
|CVector2f|Type containing two float numbers.|
|CVector2i|Type containing two integer numbers.|
|CVector3f|Type containing three float numbers.|
|CVector3i|Type containing three integer numbers.|
|CVector4f|Type containing four float numbers.|
|CVector4i|Type containing four integer numbers.|
|Cabinet||
|CabinetAction||
|CabinetActionMarker||
|CabinetActionProgressTooltipSection||
|CabinetCardModifier||
|CabinetCardModifierEntry||
|CabinetItem||
|CallAllyAlert||
|Cardinal||
|CasusBelli||
|CategoryBuildingTypesItem||
|CategoryTradesItem||
|CharMessage||
|Character||
|CharacterActionItem||
|CharacterInteraction||
|CharacterInteractionItem||
|CharacterItem||
|CharacterLateralview||
|CharacterModifierWrap||
|CharacterRoleMask||
|CharacterRulerData||
|Chat|Jomini Chat - Chat|
|ChatMessage|Jomini Chat - Message|
|ChatNotificationMessage|Jomini Chat - Notification message|
|ChatTab|Jomini Chat - Tab|
|ChatWindow|Jomini Chat - Window|
|ChildAssembleEntityWindow|Entity Designer - Child Assemble Entity Window|
|ChildEducation||
|ChildEducationCandidate||
|ChildGenerator|Portrait Editor - Child Generator|
|ChildItem|Portrait Editor - Child Item|
|CityGraphicsWrap||
|CityMarker||
|Climate||
|CloseSettingsDialogWindow||
|CoatOfArms|Coat of Arms Sprite|
|CoatOfArmsWrapper|Coat of Arms Sprite Wrapper|
|ColonialCharter||
|ColonialCharterItem||
|ColonyCategoryGlue||
|ColonyCharterMarker||
|ColorPaletteNodeWindow||
|ColorPicker||
|Combat||
|CombatImminentMarker||
|CombatMarker||
|CombatModifier||
|CombatSide||
|CombatSideWrap||
|CombatSubUnitArray||
|ConditionLine||
|ConditionList||
|CondottieriItem||
|ConfirmDiplomaticAction||
|ConfirmInsultAction||
|ConfirmOfferLoanAction||
|ConfirmWindow||
|ConquistadorConstructionMarker||
|ConsoleMenuItem|Console Menu Item|
|ConsoleWindow|Console Window|
|ConstructScoreItem||
|ConstructScoreRanking||
|Construction||
|ConstructionItem||
|Container||
|Context||
|ContextMenu||
|ContextMenuItem|Tools Context Menu Item|
|Continent||
|ControlGroupsView||
|CountriesListView||
|CountriesListViewItem||
|Country||
|CountryCountryModifierWrap||
|CountryCultureLateralView||
|CountryCultureLateralViewWorkOfArtItem||
|CountryDiplomaticItem||
|CountryEntry|Country Entry|
|CountryInteraction||
|CountryListFromLocation||
|CountryListOverview||
|CountryMessage||
|CountryModifierWrap||
|CountryNeeds||
|CountryPeopleLateralView||
|CountryPopulationChart||
|CountryRank||
|CountryRankCandidate||
|CountryReligionLateralView||
|CountryRulerData||
|CreateAccount|Create Account View|
|CreateCasusBelliMarker||
|CreateSocialProfileWindow|Jomini Social Profile - Create window|
|CreateSubjectsLateralView||
|CreditsWindow|Jomini Credits Window|
|Culture||
|CultureDefinition||
|CultureGroup||
|CultureItem||
|CulturesLedger||
|CurrencyPriceWrap||
|CurrentNeedsItem||
|CurrentReligiousFocus||
|CurrentResearch||
|CurryingFavorsMarker||
|CurveEditor|Curve Editor|
|CurvePoint|Curve Editor - Curve Point|
|DatabaseModifier||
|DatatypesExplorer||
|Date|Jomini Historical Date|
|DebugUnitSpawner||
|DecalsEditor|Map Editor - Decals Editor Mode|
|DecalsEditorDecalInstance|Map Editor - Decal Instance|
|DecalsEditorDecalInstancesList|Map Editor - List of Decal Instances|
|DecalsEditorDecalSet|Map Editor - Decal Set|
|DecalsEditorDecalSetProperties|Map Editor - Decal Set Properties|
|DecalsEditorDecalSetsList|Map Editor - Decal Sets|
|DecalsEditorSearchFilter|Decals Editor Search filter|
|DecalsEditorSettings|Decals Editor - Settings|
|DecalsEditorSettingsLayer|Decals Editor - Settings Layer|
|DecalsEditorViewport|Map Editor - Decals Editor Viewport|
|DeclareWarAlly||
|DeclareWarLateralView||
|DeclareWarSelectCasusBelli||
|DeclareWarSelectWarGoal||
|DefineProxyNodeWindow|Define proxy node window|
|DemandCategory||
|DemandCategoryWrap||
|DemandsOnMarketWrap||
|DesertConnectionMarker||
|Dialect||
|DialogConfig||
|DiploAlert||
|Diplomacy||
|DiplomacyDialog||
|DiplomacyLateralView||
|DiplomacyMacrobuilderLateralView||
|DiplomacyMacrobuilderSelectCountry||
|DiplomacyStatus||
|DiplomaticActionCategory||
|DiplomaticActionItem||
|DiplomaticObjectiveTypeGlue||
|Disaster||
|DisasterType||
|DisasterView||
|Disease||
|DiseaseOutbreak||
|DiseasesLateralView||
|DlcEntry||
|DockableLayout|Dockable Layout Manager - Layout|
|DockableLayoutManager|Dockable Layout Manager Window|
|DockableWindow|Dockable Window|
|DrawCmdsList|Draw Commands List|
|DrawCmdsViewer|Draw Commands Viewer|
|DummyTechTreeContextItem||
|DynastiesLedger||
|Dynasty||
|DynastyItem||
|DynastyLineItem||
|DynastyMarker||
|DynastyNodeItem||
|DynastyTreeView||
|EconomicSupportWindow||
|EconomyItem||
|EconomyView||
|EcsSceneViewer||
|EcsSceneViewerDockable|EcsSceneViewerDockable|
|EditorSettingCategory|Editor Settings - Category|
|EditorSettingsPage|Editor Settings - Settings Page|
|EditorSettingsWindow|Editor Settings Window|
|EffectNodeWindow||
|EmitterNodeWindow||
|EmploymentSystem||
|Encyclopedia|Jomini Encyclopedia|
|EncyclopediaEntry|Jomini Encyclopedia - Entry|
|EncyclopediaEntryView|Jomini Encyclopedia - Entry View|
|EncyclopediaLateralView||
|EncyclopediaPage|Jomini Encyclopedia - Page|
|EndGameView||
|EndPrepConfirm|Jomini Multiplayer - End preparation confirm|
|EntityDesigner|Entity Designer Window|
|EntityDesignerPlayer||
|EntityDesignerProperties|Entity Designer - Properties|
|EntityDesignerTab|Entity Designer Tab Metadata|
|EntityEditor|Entity Editor|
|EntityEditorAudioEventHandler|Entity Editor - Audio Event Handler|
|EntityEditorEventLayer|Entity Editor - Entity Event Layer|
|EntityEditorKeyframe|Entity Editor - Entity Key Frame|
|EntityEditorTimelineState|Entity Editor - Timeline State|
|EntityViewerProperties|Entity Editor - Properties|
|EnumSettingEntry|Jomini Settings - Enum Setting|
|Estate||
|EstateOpinionWrap||
|EstatePrivilege||
|EstateType||
|EstatesItem||
|Ethnicity|Portrait System - Ethnicity|
|EthnicityItem|Portrait Editor - Ethnicity Item|
|EventInfo||
|EventLayerForEntityEditor|Entity Editor - Entity Event Layer Keyframe|
|EventOption||
|EventTargetSetupContext||
|EventWindow||
|ExpandRawGoodsLateralView||
|ExpandRawGoodsSelectMarket||
|ExpansionLateralView||
|Exploration||
|ExplorationCategoryGlue||
|ExportTool|Map Editor - Export Tool Dockable|
|ExtraTooltipInfo||
|FilterablePropertyList||
|FilteredSortedList||
|FindLocationItem||
|FindLocationView||
|FoodLocationItem||
|FoodOwner||
|FoodProductionLateralView||
|FoodProductionListItem||
|FoodProductionSelectMarket||
|FoodProvinceItem||
|ForeignBuildingLocationItem||
|ForeignCountrySelectCountry||
|ForeignCountryView||
|FormNewCountry||
|FormableCountry||
|FormattedTooltipWrap||
|FortFlipRestoreMarker||
|FortMarker||
|Friend|Jomini Friend List - Friend|
|FriendListWindow|Jomini Friend List - Friendlist window|
|FriendRequest|Jomini Friend List - FriendRequest|
|FriendSearchResult|Jomini Friends - Search Result|
|Friends|Jomini Friend List - Friends manager|
|FrontEndCreditsView|Jomini Frontend Credits View|
|FrontEndLoadView||
|FrontEndMainView||
|FrontEndMultiplayerView|Jomini Multiplayer - Frontendview|
|FrontEndSinglePlayerView||
|FrontEndView||
|GUIAchievement|Jomini Achievement GUI|
|GameConceptTooltip||
|GameDLC||
|GameEncyclopedia||
|GameLobby||
|GameMpSetup||
|GameResignConfirmationWindow||
|GameRule||
|GameRuleSetting||
|GameSaveNameWindow||
|GeneCategory|Portrait System - Gene Category|
|GeneItem|Portrait Editor - Gene Item|
|GeneTemplate|Portrait System - Gene Template|
|GenerationItem|Portrait Editor - Generation Item|
|GenericAction||
|GeographyGlue||
|GfxSkin|GFX Skin|
|God||
|GodWithReligionWrap||
|GoodItem||
|Goods||
|GoodsDemand||
|GoodsDemandEntry||
|GoodsDetailsLateralView||
|GoodsInMarket||
|GoodsItem||
|GoodsMarketEntry||
|GoodsMessage||
|GoodsOnMarketPopWrap||
|GoodsOnMarketWrap||
|GoodsPriceOnMarketWrap||
|GoodsProductionLateralView||
|GoodsProductionSelectMarket||
|GoodsSellPriceWrap||
|GoodsSourceItem||
|GoodsView||
|GovReformOutlinerEntry||
|Government||
|GovernmentReform||
|GovernmentReformItem||
|GovernmentReformsLateralView||
|GovernmentType||
|GovernmentView||
|Graph|Node Editor - Graph|
|GraphInterfaceNodeWindow||
|GraphPanel|Node Editor - Graph Panel|
|GraphicalCultureType||
|GreatPowerItem||
|Group|Jomini Achievement Window - Group|
|GroupItem||
|GuiAnimationCurveEditor|Dockable tool for editing gui animations as a curve graphs.|
|GuiAnimationCurveEditorControlPoint|A control point of a given curve editor line.|
|GuiAnimationCurveEditorLine|A single curve editor line instance.|
|GuiAnimationCurveEditorViewport|Gui Animation Curve Editor Viewport instance.|
|GuiAnimationEditor|Dockable tool for editing gui animations.|
|GuiAnimationEditorAnimSetEntry|Animation-set list entry in the Gui Animation Editor tool.|
|GuiAnimationEditorAnimationEntry|An entry representing an animation for a given anim-set in the Gui Animation Editor.|
|GuiAnimationEditorAvailableTrack|An entry representing a track that is available to add to the given animation in the Gui Animation Editor tool.|
|GuiAnimationEditorKeyframe|An entry representing a single keyframe on the track in the Gui Animation Editor.|
|GuiAnimationEditorMetadataCtx|Tool metadata context of Gui Animation Editor.|
|GuiAnimationEditorPlayer|Instance for managing the playback in Gui Animation Editor.|
|GuiAnimationEditorPlayerSpeedMultiplierEntry|Playback Speed Multiplier Entry in Gui Animation Editor.|
|GuiAnimationEditorRuler|Viewport ruler in the Gui Animation Editor tool.|
|GuiAnimationEditorRulerResolutionEntry|An entry representing a ruler resolution step in the Gui Animation Editor tool.|
|GuiAnimationEditorUniversalTrack|An entry representing an animation for a given anim-set in the Gui Animation Editor.|
|GuiAnimationEditorViewportBase|Base class for the different types of viewports in the GUI Animation Editor dockables|
|GuiAnimationEditorViewportUserInput|Keeps track of the user input over viewports in the GUI Animation Editor dockables|
|GuiAnimationTimelineViewport|Gui Animation Editor Timeline Viewport instance.|
|GuiContext|GUI Context|
|GuiCurrentDrag|For use in drag_widget, inside of draggable_behavior. Contains data regarding current ongoing drag, such as mouse positions|
|GuiDataProfiler|Gui Data Profiler Window|
|GuiDataProfilerEntryNode|Gui Data Profiler tree entry node|
|GuiEditorTooltip|GUI Editor - Tooltip|
|GuiGameRule||
|GuiGameRulePreset||
|GuiTableRow|Generic Table - Row|
|Hegemony||
|HeirSelection||
|HeirSelectionCandidate||
|HeirSelectionValue||
|HintsLateralView||
|HistoricalScore||
|HistoricalScoreItem||
|HistoryViewer||
|HolySite||
|HolySiteDefinition||
|HolySiteGlue||
|HolySiteType||
|IconWrap||
|ImageLookupNode|Image Look up node window|
|Implementable|Base class for implementable game structures|
|ImplementedCabinetAction||
|ImplementedEstatePrivilege||
|ImplementedGovernmentReform||
|ImplementedPolicy||
|ImportExportLateralView||
|ImportExportMarker||
|ImportTool|Map Editor - Import Tool Window|
|Importable|Map Editor - Importable items within a ImportableGroup|
|ImportableGroup|Map Editor - Importable Group|
|ImportantCultureItem||
|ImportantReligionItem||
|ImproveOpinionMarker||
|InGameMissionTaskItem||
|InGameTopbar||
|InfoboxNodeWindow|Node Editor - Infobox Node Window|
|InputActionBinding|Input Context Manager - Input Action|
|InspectorPanel|Map Editor - Spline Network Tool - Anchor Inspector Panel|
|Institution||
|InstitutionEditor||
|InstitutionEntry||
|InstitutionItem||
|InstitutionMessage||
|Insult||
|InsultCandidate||
|InteractionTarget||
|InternationalOrganization||
|InternationalOrganizationLawAlert||
|InternationalOrganizationLawCategory||
|InternationalOrganizationMessagePopup||
|InternationalOrganizationModifierWrap||
|InternationalOrganizationType||
|InternationalOrganizationTypeVariable||
|InternationalOrganizationTypeView||
|InternationalOrganizationsView||
|JominiGUISetting|Jomini Setting|
|JominiGameRules||
|JominiLoadWindow||
|JominiNotification|Jomini Notification Item|
|JominiNotificationOverlay||
|JominiPasswordPopup|Jomini Multiplayer - Password Popup|
|JominiServer|Jomini Multiplayer - Server|
|JominiServerBrowserGui|Jomini Multiplayer - Server Browser|
|JominiSettingsWindow|Jomini Settings Window|
|KeyframeEditor|GUI Editor - Keyframe Editor|
|KeyframeEventEditor|Entity Editor - Event Editor|
|KeyframeWidget|GUI Editor - Keyframe|
|LackingGoodsForRepairEntry||
|LandOwnershipRule||
|Language||
|LanguageFamily||
|LateralView||
|LateralViewHistoryEntry||
|LateralViewManager||
|Law||
|LawCategory||
|LawWithContextWrap||
|Layer|Map Editor - Map Object Layer|
|LayerTreeItem|Map Editor - Map Object Layer Tree Item|
|LeaderCandidate||
|LegalDocsViewer|Legal Documents Viewer|
|LevySetup||
|Loan||
|LoanDurationCandidate||
|LoanEntry||
|LobbyPlayer|Jomini Multiplayer - Lobby Player|
|LobbyView|Multiplayer GUI - Lobby View|
|LocalMod|Mods Gui - Local Mod|
|Location||
|LocationBuildingItem||
|LocationBuildingsWindow||
|LocationCountryDoubleModifierWrap||
|LocationCountryModifierWrap||
|LocationDoubleModifierWrap||
|LocationItem||
|LocationMigrationWrap||
|LocationModifierWrap||
|LocationPercentCountryModifierWrap||
|LocationPopItem||
|LocationPopPieChartTooltipWidget||
|LocationPopulationChart||
|LocationRank||
|LocationReference||
|LocationToBuildItem||
|LocationToRecruitItem||
|LocationView||
|LocationViewSelectProvince||
|LocationsListView||
|LocationsListViewItem||
|LockableInfo||
|LogEntry|Texture Importer - Log Entry|
|LogViewer|Log Viewer Window|
|LogViewerCategory|Log Viewer - Log Category|
|LogViewerEntry|Log Viewer - Log Entry|
|LogViewerType|Log Viewer - Log Entry Type|
|LoginView|Login View|
|MPChatMessage||
|MPConfig|Jomini Multiplayer - Configuration|
|MaintenanceSetting||
|ManageSubjectsLateralView||
|MapColorLedger||
|MapContentEditorMode|Map Editor - Map Content Editor Mode|
|MapContentEditorOptions|Map Editor - Map Content Options Window|
|MapContentEditorViewport|Map Editor - Map Content Viewport|
|MapContentEntryDesc|Map Editor - Map Content Layer Entry|
|MapContentLayerDesc|Map Editor - Map Content Layer|
|MapContentPanel|Map Editor - Map Content Layer List|
|MapContentPropertyGroup|Map Editor - Map Content Property Group|
|MapContentPropertyGroupsGui||
|MapContentSelector|Map Editor - Map Content Selection|
|MapContentSelectorGui|Map Editor - Map Content Selection Interface|
|MapEditor|Map Editor - Main|
|MapEditorGui|Map Editor - Main GUI|
|MapEditorLayerBorder|Map Editor - Map Editor Layer Border|
|MapEditorLayerBorderDockable|Map Editor - Map Editor Layer Border Settings Window|
|MapMarkerSettingItem||
|MapMode||
|MapObjectMask|Map Editor - Map Object Mask|
|MapObjectPainter|Map Editor - Map Object Painter|
|MapObjectPainterMode|Map Editor - Map Object Painter Mode|
|MapObjectPainterOptions|Map Editor - Map Object Painter Options|
|MapObjectTool|Map Editor - Map Object Tool|
|Maritime||
|MaritimeInLocationWrap||
|MaritimeItem||
|MaritimeLateralView||
|MaritimePresence||
|Market||
|MarketAccessWrap||
|MarketCountryNeeds||
|MarketMarker||
|MarketViewSelectMarket||
|MarketingContainer||
|MarketingSlot||
|MarketsView||
|MaskEntry|Map Editor - Texture Mask|
|MaskManagerEntry|Map Editor - Mask Painter - Mask Entry|
|MaskPainterManager|Map Editor - Mask Painter Manager|
|MaskPainterMapContentPanel|Map Editor - Mask Painter Map Content Window|
|MaskPainterMode|Map Editor - Mask Painter mode|
|MaskPainterTool|Map Editor - Mask Painter Tool|
|MaskPainterViewport|Map Editor - Mask Painter Viewport|
|MaterialNodeWindow||
|MemberTypeItem||
|Mercenary||
|MercenaryItem||
|MercenaryModifierWrap||
|MercenaryTypeItem||
|Merchant||
|MerchantCapacityInMarketWrap||
|MerchantPowerInMarketWrap||
|MeshImporter|Mesh Importer Window|
|MeshImporterBrowser|Mesh Importer Browser Window|
|MeshImporterBrowserEntry|Mesh Importer Browser File Entry|
|MeshImporterMaterialEntry||
|MeshImporterMaterials||
|MessageLog||
|MessageMenuItem||
|MessagePopup||
|MessageSettingItem||
|MessageSettings||
|MessageSettingsMenu||
|MetadataWindow|Window to edit metadata of selected nodes.|
|Migration||
|MilitaryObjective||
|MilitaryObjectiveGroupView||
|MilitaryObjectiveGroupsView||
|MissingGoods||
|MissingGoodsOnMarketImpactWrap||
|MissionAlert||
|MissionDefinition||
|MissionItem||
|MissionLateralView||
|MissionLineItem||
|MissionMessage||
|MissionProgress||
|MissionTaskDefinition||
|MissionTaskItem||
|MissionTaskMessage||
|MissionTasksLateralView||
|ModToolItem||
|ModToolsGui||
|ModifierDebugData||
|ModifierDebugInspectorPlugin||
|ModifierItem||
|ModifierSourceWrap||
|ModifierType||
|ModsGui|Mods Gui Data Context|
|ModsPlayset||
|ModsPlaysetEntry||
|MoveTool|Map Editor - Map Object - Move Tool|
|MultiNonoptionalInputNodeWindow||
|MultiUnitSelectUnit||
|MultiUnitWindow||
|MultiplayerChat||
|MultiplayerSetupWindow|Jomini Multiplayer - Setup window|
|MusicPlayer||
|MusicPlayerCategory||
|MusicTrack||
|NavyConstructionMarker||
|NavyStrength||
|NewBornMessage||
|NewCountryCandidate||
|Node|Node Editor - Node|
|NodeEditorSearch||
|NodeError|Node Editor - Node Error|
|NodeLine|Node Editor - Node Line|
|NodePin|Node Editor - Node Pin|
|NodeWindow|Node Editor - Node Window|
|NonDownloadedMod|Mods Gui - Non-Downloaded Mod|
|NonRegisteredDockable|NonRegistered Dockable Window|
|NotificationDummyContext|Jomini Notification Dummy Context|
|Nudger|Map Editor - Map Object Manager (Nudger)|
|NudgerLayerEntryMapObjectDesc|Map Editor - Map Object - Map Content Entry|
|NudgerMapContentGui|Map Editor - Map Object - Map Content Window|
|NudgerMapObjectPropertyListDockable|Map Editor - Map Object|
|NudgerMode|Map Editor - Map Object Mode|
|ObjectBrowser|Object Explorer - Browser|
|ObjectBrowserView|Object Explorer - View|
|ObjectInspector|Object Explorer - Inspector|
|ObjectInspectorDockable|Object Explorer - Inspector Window|
|ObjectInspectorPlugin|Object Explorer - Inspector Plugin|
|ObjectPreset|Object Explorer - Preset|
|ObjectProvider|Object Explorer - Provider|
|OneBuildingInMarketUpkeepWrap||
|OngoingRelationCountry||
|OngoingRelationCountryList||
|OosData|Jomini Multiplayer - Out-of-sync data|
|OosWindow|Jomini Multiplayer - Out-of-sync window|
|OrgItem||
|OutbreakItem||
|OutgoingFriendRequest|Jomini Friend List - Outgoing friend request|
|Outliner||
|OutlinerAgendaEntry||
|OutlinerCabinetEntry||
|OutlinerCategoryEntry||
|OutlinerCategoryHandler||
|OutlinerDiplomacyEntry||
|OutlinerEntry||
|OutlinerPlayerEntry||
|OutlinerSettings||
|OutlinerWarEntry||
|OutputEntry|Texture Importer - Output Entry|
|OverrideEntry||
|Parliament||
|ParliamentAgenda||
|ParliamentAgendaGlue||
|ParliamentAgendaItem||
|ParliamentInSession||
|ParliamentIssue||
|ParliamentIssueWithContextWrap||
|ParliamentMarker||
|ParliamentType||
|ParticleUserData||
|PauseMenu||
|Payment||
|PaymentWithContextWrap||
|PdxAccount||
|PdxCoreSetting|Settings Window - Core Setting|
|PdxEnumSetting|Settings Window - Enum Setting|
|PdxGuiFoldOut|Foldable Item|
|PdxGuiGfxVideoControl||
|PdxGuiTableRow|Generic Tree Table - Row|
|PdxGuiTreeTable|Generic Tree-Table|
|PdxGuiWidget|GUI Widget|
|PdxSetting|Settings Window - Setting|
|PdxSettingsWindow|Settings Window|
|PdxSettingsWindowCategory|Settings Window - Category|
|PdxValueSetting|Settings Window - Value Setting|
|PeaceOfferCategory||
|PeaceOfferLateralView||
|PeaceOfferLateralViewParticipant||
|PeaceOfferWarScoreTreatyGlue||
|PeaceTreaty||
|PeopleDynastyItem||
|PeoplePopItem||
|PeopleRebelItem||
|PerformActionParams||
|Periphora||
|PinCollection||
|PinningManager||
|PlayStyleItem||
|Playable|Jomini Playable|
|PlayerConstruction||
|PlayerEntryForChat||
|PlayerJoinRequest|Jomini Multiplayer - Player Join Request|
|PlayerModifiersLateralView||
|PlayerPlayStyleItem||
|PlayerProficiency||
|PlaystyleHint||
|PlaythroughItem||
|PlotLine||
|Policy||
|PolicyWithContextWrap||
|Pop||
|PopCultureItem||
|PopEditor||
|PopEntry||
|PopPoliticsItem||
|PopReligionItem||
|PopSetupEntry||
|PopTaxItem||
|PopType||
|PopTypeEntry||
|PopTypeItem||
|PopsCountryItem||
|PopsLocationItem||
|PopsOverview||
|PopsPiechartWidget||
|PopsProvinceItem||
|Population||
|PopulationConfiguration||
|PortEditor||
|PortMarker||
|Portrait3dView|Portrait Editor - 3D view window|
|PortraitDataContext|Portrait Editor - Portrait Data|
|PortraitEditorAnimationItem|Portrait Editor - Animation Item|
|PortraitEditorWindow|Portrait Editor Window|
|PortraitTooltip|Portrait Tooltip|
|PossibleDisease||
|PossibleExplorationItem||
|PossibleItem||
|PossibleLeaderItem||
|PossiblePrivateerItem||
|PossibleProductionMethods||
|PossibleProductionMethodsItem||
|PossibleRebel||
|PossibleSubUnitDefinition||
|PossibleTrade||
|PossibleTradesSelectMarket||
|PreviewMaskTexture|Map Editor - Preview Mask|
|Price||
|PriceTooltipWrap||
|Privateer||
|PrivilegeItem||
|ProducedOnMarketWrap||
|ProductionMethod||
|ProductionMethodItem||
|ProductionSelectMarket||
|ProductionView||
|PropertyListCategory|A category in a property list|
|Province||
|ProvinceDefinition||
|ProvinceModifierWrap||
|QuickCabinetCardModifier||
|QuickCharacterActions||
|QuickCultureCountryList||
|QuickDiplomaticActions||
|QuickMarketTrades||
|QuickMissionList||
|QuickRebelLocationList||
|QuickReligionCountryList||
|QuickTemporaryCountryRelations||
|QuickUnitActions||
|QuickVisibleCountries||
|QuickVisibleMarkets||
|RandomizableValueFloat||
|RandomizableValueInt||
|RawGoodLocationItem||
|RawGoodsMarker||
|ReasonItem||
|Rebel||
|RebelDetailsLateralView||
|RecruitInLocationLateralView||
|RecruitScoreRanking||
|RecruitmentMethod||
|ReformItem||
|RegencyType||
|Region||
|RelationDescItem||
|RelationTypeItem||
|RelativePowerTooltipGlue||
|Religion||
|ReligionDefinition||
|ReligionGroup||
|ReligionItem||
|ReligionMessage||
|ReligionModifierWrap||
|ReligionsLedger||
|ReligiousAspect||
|ReligiousAspectGlue||
|ReligiousFaction||
|ReligiousFactionActionGlue||
|ReligiousFactionGlue||
|ReligiousFigure||
|ReligiousFigureGlue||
|ReligiousFocus||
|ReligiousFocusGlue||
|ReligiousSchool||
|RemoveFriendConfirmWindow|Jomini Friend List - Remove friend confirm window|
|RenameDialog||
|ReorgWindow||
|ReportIssueItem||
|ReportIssueWindow||
|RequirementLine||
|RequirementLineAux||
|RequirementsList||
|ResearchMessage||
|ResignConfirmationWindow||
|Resolution||
|ResolutionGlue||
|RiverDirectionWrap||
|RoadBuilder||
|RoadCostCalculation||
|RoadDestinationItem||
|RoadEditor||
|RoadType||
|RoadTypeEntry||
|RoadTypeItem||
|RowList||
|RulerTerm||
|RulerTermEntry||
|RulerTraitEntry||
|RulingHistoryView||
|SaintGlue||
|Savable|Save Dialog - Savable|
|SavableGroup|Save Dialog - Savable Group|
|SaveDialog|Save Dialog|
|SaveGame||
|SaveGameAnalysisView||
|SaveGameAnalyzer||
|SaveGameBlockData||
|SaveGameConfigView||
|SaveGameItem||
|SaveGameListView||
|SaveListWindow||
|SaveNameWindow||
|ScaledStaticModifierWrap||
|Scenario||
|SceneData||
|SceneEditor|Scene Editor Window|
|SceneEditorEnvironmentProperties|Scene Editor Environment Properties|
|SceneEditorHierarchyEntry|Entity Represented in the Scene Editor Hierarchy|
|SceneEntityComponentsEditor|Scene Editor Entity Component Editor|
|SceneHierarchy|Scene Editor Entity Hierarchy|
|ScenePreset|Scene Editor Preset|
|ScenePresetEntity|Scene Editor Preset Entity|
|SceneProfiler|Scene Editor Profiling|
|SceneSelection|Scene Editor Selection|
|SceneTransform||
|Scope||
|ScopeDebugData||
|ScopeDebugInspectorPlugin||
|ScopeObjectEditor||
|ScopeObjectProvider||
|ScopeObjectType||
|ScopedEditorSettingsCategory||
|Score||
|ScoreView||
|ScoreViewItem||
|ScriptProfilerEntry||
|ScriptProfilerFileLine||
|ScriptProfilerGui||
|ScriptRunnerInspector||
|ScriptRunnerResult||
|ScriptableHintDefinition||
|ScriptedGui||
|ScriptedHintItem||
|ScriptedPeaceTreatyType||
|ScriptedRelationType||
|ScriptedRelationTypeWithContextWrap||
|SeaCurrentWrap||
|SeaZoneView||
|SearchBar||
|SearchFilter||
|SearchFilterCategory||
|SearchFilterGroup||
|SearchFilterRange||
|SearchFilterRangeValues||
|SearchListNodeWindow||
|SectionIndex||
|SelectCasusBelli||
|SelectCharacterInteraction||
|SelectChildEducation||
|SelectCountryDiplomacyLateralView||
|SelectCreateCasusBelliWindow||
|SelectHeirSelection||
|SelectHolySite||
|SelectInteractionTargetGlue||
|SelectInteractionTargetView||
|SelectInterveneWindow||
|SelectLateralViewHistory||
|SelectLoanLateralView||
|SelectMissionLateralView||
|SelectParticipant||
|SelectParticleUserDataDialog||
|SelectSearchFilter||
|SelectSocietalValue||
|SelectSubjectTypeLateralView||
|SelectTool|Map Editor - Map Object - Select Tool|
|SelectWar||
|SelectedMarketLateralView||
|SendGiftWindow||
|ServerInformation||
|SettingCategory|Jomini Settings - Category|
|SettingsPage|Jomini Settings - Settings Page|
|SetupCondottieriView||
|SetupEditor||
|SetupEntry||
|SetupMercenaryRequirementsView||
|Siege||
|SiegeRollModifierWrap||
|SiegeRollModifierWrapItem||
|SimpleCustomTagTooltipWrapper||
|SingleUnitSelectUnit||
|SingleUnitWindow||
|Situation||
|SituationMessagePopup||
|SituationView||
|SkinEditor|GFX Skin Editor|
|Social|Jomini Social Manager|
|SocialNotificationWindow|Jomini Friend List - Notification window|
|SocialUI|Jomini Friend List - Social UI|
|SocialWidget|Jomini Social Widget|
|SocietalValue||
|SocietalValueCandidate||
|SocietalValueInCountryWrap||
|SocietalValueItem||
|SocietalValueRequirement||
|SocietalValuesLateralView||
|SortKey||
|SpecialOptionGlue||
|SpecialStatus||
|SpecificGoodsOnMarketWrap||
|SplineAdjustmentTool|Map Editor - Spline Network Adjustment Tool|
|SplineAdjustmentToolMode|Map Editor - Spline Network Adjustment Tool - Mode|
|SplineEntryUi|Map Editor - Universal Spline Entry UI|
|SplineRiverInteractionMode|Map Editor - Spline Ruler Interaction Mode|
|SplineRiverTool|Map Editor - Spline River Tool|
|SplineStripTool|Map Editor - Spline Strip Tool|
|SplineStripToolMode|Map Editor - Spline Strip Tool - Mode|
|SplineToolsMapContentPanel|Map Editor - Spline Strip Tool - Map Content Panel|
|SplineTypeCreateSelectionDropdown|Map Editor - Spline Strip Tool - Create Dropdown|
|SplineTypeItem|Map Editor - Spline Strip Tool - Spline Type|
|SplineTypeSwitchSelectionDropdown|Map Editor - Spline Strip Tool - Type switch dropdown|
|SplineVisibilityDropdown|Map Editor - Spline Visibility Dropdown|
|StatImpactItem||
|StateConnection|A connection in the Animation Edtior|
|StaticAutoModifier||
|StaticModifier||
|StatusWidget|Status Widget|
|StrategicMilitaryObjective||
|StrategicMilitaryObjectiveGlue||
|StrategicMilitaryObjectiveGroup||
|StrategicObjectiveGroupGlue||
|StringPair||
|StringPairList||
|SubContinent||
|SubUnit||
|SubUnitArray||
|SubUnitCategory||
|SubUnitCombatCounts||
|SubUnitCount||
|SubUnitCounts||
|SubUnitPrice||
|SubUnitType||
|SubjectCategoryItem||
|SubjectItem||
|SubjectMilitaryStance||
|SubjectType||
|SubjectTypeItem||
|SupplyDepot||
|SupplyDepotMarker||
|SupplyOnMarketWrap||
|SupportRebelLateralView||
|TableColumn||
|TableColumnList||
|TacticalMilitaryObjectiveGroup||
|TacticalMilitaryObjectiveTypeGlue||
|TacticalObjectiveGroupGlue||
|TagInfo||
|TargettedActionParameters||
|TaxRateSetting||
|TechTreeItem||
|TechTreeOneAge||
|TechnologyLateralView||
|TemporaryDemand||
|TerrainImpactItem||
|TerrainToolButton|Map Editor - Terrain Tool Button|
|TextSearchFilter||
|TextureEntry|Texture Importer - Texture Entry|
|TextureImporter|Texture Importer Window|
|TextureList|Texture List - In-memory texture list|
|TextureListDirectory|Texture Viewer - Directory|
|TextureListTexture|Texture Viewer - Texture|
|TextureNodeWindow|Node Editor - Texture Node Window|
|TextureViewer|Texture Viewer - In-memory texture viewer|
|ThreatenTarget||
|ThreatenWarView||
|TickTaskData||
|TickTaskDebuggerView||
|TickTaskDetailsView||
|TickTaskGraphItem||
|TickTaskGraphLine||
|TickTaskListView||
|TimedModifier||
|TimedModifierOwner||
|TimelineKeyframe|Timeline Widget - Keyframe|
|TitleDescTooltip||
|TollMarker||
|ToolDialog|Tool Dialog|
|ToolDialogButton|Tool Dialog - Button|
|ToolMessageDialog|Tool Message Dialog|
|ToolProgressDialog|Tool Progress Dialog|
|ToolProperty|Tool Property|
|ToolProperty2SearchList||
|ToolPropertyAction|Additional Action available on a given ToolProperty.|
|ToolPropertyBool||
|ToolPropertyCColor|Tool Property Color - CColor|
|ToolPropertyCString||
|ToolPropertyColor|Tool Property Color - Vector4f|
|ToolPropertyCurve||
|ToolPropertyFloat||
|ToolPropertyInt||
|ToolPropertyInt16||
|ToolPropertyInt8||
|ToolPropertyList|Tool Property List|
|ToolPropertySearchList||
|ToolPropertyString|Tool Property UTF8 String|
|ToolPropertyUint||
|ToolPropertyUint16||
|ToolPropertyUint8||
|ToolPropertyUndoableSearchList||
|ToolPropertyVec1fPercent||
|ToolPropertyVec2f||
|ToolPropertyVec2fPercent||
|ToolPropertyVec2i||
|ToolPropertyVec3f||
|ToolPropertyVec3i||
|ToolPropertyVec4i||
|ToolsPropertyDraggableValueFloat|Tools Property Draggable Float|
|ToolsPropertyDraggableValueInt|Tools Property Draggable Int|
|ToolsPropertyDraggableValueVector2f|Tools Property Draggable Vector2 Float|
|ToolsPropertyDraggableValueVector2i|Tools Property Draggable Vector2 Integer|
|ToolsPropertyDraggableValueVector3f|Tools Property Draggable Vector3 Float|
|ToolsPropertyDraggableValueVector3i|Tools Property Draggable Vector3 Integer|
|ToolsPropertyDraggableValueVector4i|Tools Property Draggable Vector4 Integer|
|ToolsPropertyPath|Tools Property Path|
|ToolsPropertyRangedValueFloat|Tools Property Ranged Float|
|ToolsPropertyRangedValueInt|Tools Property Ranged Int|
|ToolsPropertyTextureStringValue|Tools Property Texture Value|
|ToolsPropertyTextureValue|Tools Property Texture|
|ToolsPropertyValueList|Tools property representing a list of elements|
|ToolsPropertyValueListEntry|Single element in the datamodel provided by a ToolsPropertyValueList|
|ToolsPropertyVfsMountPath|Tools Property for Vfs-Mount-Path|
|ToolsSearch|Tools Search (OmniSearch)|
|ToolsSearchResult|Tools Search - Result|
|ToolsUndoableValueBundleBool||
|ToolsUndoableValueBundleCColor||
|ToolsUndoableValueBundleCString||
|ToolsUndoableValueBundleColor||
|ToolsUndoableValueBundleFloat||
|ToolsUndoableValueBundleInt||
|ToolsUndoableValueBundleString||
|ToolsUndoableValueBundleUint||
|ToolsUndoableValueBundleUint16||
|ToolsUndoableValueBundleVec2f||
|ToolsUndoableValueBundleVec2i||
|ToolsUndoableValueBundleVec3f||
|ToolsUndoableValueBundleVec3i||
|ToolsUndoableValueBundleVec4i||
|TooltipInfo||
|TooltipString||
|TopScope||
|Topography||
|Trade||
|TradeDetailsLateralView||
|TradeOverview||
|TradePathItem||
|TradesWrap||
|Trait||
|TraitCategory||
|TransactionProportion||
|TransferUnit||
|TransferUnitType||
|Tutorial||
|TutorialWindow||
|Tweakable|Tweakable field in the Tweaker tool|
|TweakableCategory|A single Tweakable category in the Tweaker Tool|
|TweakableUiEntry|A single Tweakable Entry in the Tweaker Tool|
|TweakablesSnapshot|A snapshot of tweakable values represented in the Tweaker tool|
|Tweaker|Tweaker Tool Window|
|Type|Map Editor - Map Object Type|
|UIAction||
|UIActionProvider||
|UIClickAction||
|UIMessage||
|UIVariables||
|UVSelector||
|UndoHistoryViewerClient||
|UndoStack||
|UneditableString||
|UniqueContentCategory||
|UniqueContentDescription||
|UniqueContentItem||
|UniqueStatItem||
|Unit||
|UnitAbility||
|UnitActionItem||
|UnitActivity||
|UnitDetailsView||
|UnitGlue||
|UnitItem||
|UnitMarker||
|UnitMarkerItem||
|UnitOverview||
|UnitPriceWrap||
|UnitSuppliesWrap||
|UnitTransportStateBag||
|UnitTypeItem||
|UnitTypeLateralView||
|UnitViewer||
|UnitsWrap||
|UniversalSplineEditorEdgeProperties|Map Editor - Universal Spline Editor Selected Edges Properties|
|UniversalSplineEditorMode|Map Editor - Universal Spline Editor Mode|
|UniversalSplineEditorOutliner|Map Editor - Universal Spline Editor Outliner|
|UniversalSplineEditorPointsProperties|Map Editor - Universal Spline Editor Selected Points Properties|
|UniversalSplineEditorProperties|Map Editor - Universal Spline Editor Properties|
|UniversalSplineEditorStructure|Map Editor - Universal Spline Editor Structure of selected spline|
|UniversalSplineEditorTopbarPanel|Map Editor - Universal Spline Editor Topbar|
|UniversalSplineEditorViewport|Map Editor - Universal Spline Editor Viewport|
|UnprofitableBuildingsEntry||
|UserDataNode|Particle Editor - User Data Node|
|VariableEntry||
|VariableInfo||
|VariableInspectorEntry||
|VariableInspectorPlugin||
|VariableInspectorVariable||
|VariableList||
|VariableListEntry||
|VariableListInspectorPlugin||
|VariableListStore||
|VariableStore||
|VariableSystem||
|Vegetation||
|VfsMountPathBrowser|Gui Data Profiler Window|
|VfsMountPathBrowserEntryNode|Gui Data Profiler tree entry node|
|ViewerEntity|Entity Editor - Entity|
|ViewerEntityLodInfo|Entity Editor - Entity LodInfo|
|ViewerEntityState|Entity Editor - Entity State|
|VoteGlue||
|VoteTargetGlue||
|VoterGlue||
|War||
|WarGlue||
|WarGoal||
|WarGoalType||
|WarImpactWrap||
|WarItem||
|WarLateralView||
|WarLateralViewBattle||
|WarLateralViewParticipant||
|WarLosses||
|WarMessage||
|WarParticipant||
|WarParticipantGlue||
|WarSideGlue||
|WarViewer||
|WarsLedger||
|WarsOverviewWar||
|WatchWindow||
|WeatherSystem||
|WillJoinCountryList||
|WorkOfArt||
|WorkOfArtType||
|bool||
|double|Number stored with `double float` precision.|
|float|Number stored with `float` precision.|
|int16||
|int32||
|int64||
|int8||
|uint16||
|uint32||
|uint64||
|uint8||
|void|Unspecified type / empty type.|

|Type|Description|
|---|---|
|ActiveClip||
|ActiveHegemon||
|ActiveHegemonItem||
|ActiveInstitution||
|ActiveParliamentAgenda||
|ActiveParliamentAgendaWrap||
|ActiveProductionMethod||
|ActiveResolution||
|ActiveResolutionContainer|Base class for resolution containers|
|ActiveSituation||
|Advance||
|AdvanceDefinition||
|AdvanceItem||
|AdvanceNode||
|AdvancesLateralView||
|Age||
|AgeAdvancesWrap||
|AgendaView||
|AiCurrencyClassGlue||
|AiCurrencyViewer||
|AiTransportTarget||
|AlertCanJoinTargettedIO||
|AlertFormableCountry||
|AlertManager||
|AlertMemberLeavingUnion||
|AnimationClip|An animation clip used in animation state machines.|
|AnimationClipsEditor|Animation Clips Editor Window|
|AnimationEditor|Animation Editor Window|
|AnimationEditorConnectionTab|Connection Tab in the Animation Editor|
|AnimationEditorState|A state in the Animation State Editor.|
|AnimationEditorStateTab|State Tab in the Animation Editor|
|AnimationEditorViewer||
|AnnexationMarker||
|AntagonismBombSpec||
|AntagonismBombSpecWrap||
|AntagonismTwoCountriesWrap||
|AntagonismWrapper||
|Area||
|ArmyBuilderLateralView||
|ArmyConstructionMarker||
|Artist||
|ArtsItem||
|ArtsView||
|AskRepayLoanMessagePopup||
|AutocompleteEntry||
|AutomationLateralView||
|AvailableMercenaryTypes||
|Avatar||
|BattleParticipant||
|BattleResult||
|BattleResultMessage||
|BattleResultMessageParticipant||
|BattleResultMessageSide||
|BattleSide||
|BattleUnitStats||
|BattleView||
|BlockedVisionMarker||
|BrushSettings|Map Editor - Brush settings.|
|BrushSettingsDropdown|Map Editor - Brush settings dropdown.|
|BuildInLocationLateralView||
|BuildLocationSelectMarket||
|Building||
|BuildingCandidate||
|BuildingConstructionMarker||
|BuildingItem||
|BuildingPromoteTimeWrapper||
|BuildingSpyNetworkMarker||
|BuildingType||
|BuildingView||
|CDPopEditor||
|CEconomy||
|CEnumValueAnimation||
|Cabinet||
|CabinetAction||
|CabinetActionMarker||
|CabinetItem||
|CallAllyAlert||
|Cardinal||
|CasusBelli||
|CategoryBuildingTypesItem||
|CharMessage||
|Character||
|CharacterActionItem||
|CharacterInteraction||
|CharacterInteractionItem||
|CharacterItem||
|CharacterLateralview||
|CharacterRulerData||
|Chat|Jomini Chat - Chat|
|ChatNotificationMessage|Jomini Chat - Notification message|
|ChatTab|Jomini Chat - Tab|
|ChildEducation||
|ChildEducationCandidate||
|CityGraphicsWrap||
|CityMarker||
|Climate||
|ColonialCharter||
|ColonialCharterItem||
|ColonyCharterMarker||
|Combat||
|CombatImminentMarker||
|CombatMarker||
|CombatSide||
|CombatSideWrap||
|CombatSubUnitArray||
|CondottieriItem||
|ConquistadorConstructionMarker||
|ConstructScoreItem||
|ConstructScoreRanking||
|Construction||
|ConstructionItem||
|Context||
|Continent||
|ControlGroupsView||
|CountriesListView||
|CountriesListViewItem||
|Country||
|CountryCultureLateralView||
|CountryCultureLateralViewWorkOfArtItem||
|CountryDiplomaticItem||
|CountryInteraction||
|CountryListOverview||
|CountryMessage||
|CountryPeopleLateralView||
|CountryPopulationChart||
|CountryRank||
|CountryRankCandidate||
|CountryReligionLateralView||
|CreateCasusBelliMarker||
|CreateSubjectsLateralView||
|Culture||
|CultureGroup||
|CultureItem||
|CulturesLedger||
|CurrencyPriceWrap||
|CurrentNeedsItem||
|CurrentReligiousFocus||
|CurrentResearch||
|CurryingFavorsMarker||
|DecalsEditor|Map Editor - Decals Editor Mode|
|DecalsEditorDecalInstance|Map Editor - Decal Instance|
|DecalsEditorDecalInstancesList|Map Editor - List of Decal Instances|
|DecalsEditorDecalSet|Map Editor - Decal Set|
|DecalsEditorDecalSetsList|Map Editor - Decal Sets|
|DeclareWarAlly||
|DeclareWarLateralView||
|DemandCategory||
|DemandCategoryWrap||
|DemandsOnMarketWrap||
|DesertConnectionMarker||
|Dialect||
|DiploAlert||
|Diplomacy||
|DiplomacyDialog||
|DiplomacyLateralView||
|DiplomacyMacrobuilderLateralView||
|DiplomacyMacrobuilderSelectCountry||
|DiplomacyStatus||
|DiplomaticActionItem||
|Disaster||
|DisasterType||
|DisasterView||
|Disease||
|DiseaseOutbreak||
|DiseasesLateralView||
|DockableLayout|Dockable Layout Manager - Layout|
|DockableLayoutManager|Dockable Layout Manager Window|
|DynastiesLedger||
|Dynasty||
|DynastyItem||
|DynastyMarker||
|DynastyNodeItem||
|DynastyTreeView||
|EconomyItem||
|EconomyView||
|EditorSettingsWindow|Editor Settings Window|
|EmploymentSystem||
|Encyclopedia|Jomini Encyclopedia|
|EncyclopediaEntry|Jomini Encyclopedia - Entry|
|EncyclopediaEntryView|Jomini Encyclopedia - Entry View|
|EncyclopediaLateralView||
|EntityDesigner|Entity Designer Window|
|EntityEditor|Entity Editor|
|Estate||
|EstateOpinionWrap||
|EstatePrivilege||
|EstateType||
|EstatesItem||
|Ethnicity|Portrait System - Ethnicity|
|EventTargetSetupContext||
|EventWindow||
|ExpandRawGoodsLateralView||
|ExpandRawGoodsSelectMarket||
|ExpansionLateralView||
|Exploration||
|ExtraTooltipInfo||
|FilteredSortedList||
|FoodLocationItem||
|FoodProductionLateralView||
|FoodProductionListItem||
|FoodProductionSelectMarket||
|FoodProvinceItem||
|ForeignBuildingLocationItem||
|ForeignCountrySelectCountry||
|ForeignCountryView||
|FormNewCountry||
|FormableCountry||
|FormattedTooltipWrap||
|FortFlipRestoreMarker||
|FortMarker||
|FrontEndMainView||
|FrontEndSinglePlayerView||
|FrontEndView||
|GUIAchievement|Jomini Achievement GUI|
|GameLobby||
|GenericAction||
|GeographyGlue||
|God||
|GodWithReligionWrap||
|GoodItem||
|Goods||
|GoodsDemand||
|GoodsDemandEntry||
|GoodsDetailsLateralView||
|GoodsInMarket||
|GoodsItem||
|GoodsMarketEntry||
|GoodsMessage||
|GoodsOnMarketWrap||
|GoodsPriceOnMarketWrap||
|GoodsProductionLateralView||
|GoodsProductionSelectMarket||
|GoodsSellPriceWrap||
|GoodsSourceItem||
|GoodsView||
|GovReformOutlinerEntry||
|Government||
|GovernmentReform||
|GovernmentReformItem||
|GovernmentReformsLateralView||
|GovernmentType||
|GovernmentView||
|Graph|Node Editor - Graph|
|GraphPanel|Node Editor - Graph Panel|
|GreatPowerItem||
|Group|Jomini Achievement Window - Group|
|GroupItem||
|GuiGameRule||
|GuiGameRulePreset||
|Hegemony||
|HeirSelection||
|HeirSelectionCandidate||
|HeirSelectionValue||
|HintsLateralView||
|HistoricalScore||
|HistoricalScoreItem||
|HolySite||
|HolySiteDefinition||
|HolySiteGlue||
|HolySiteType||
|ImplementedCabinetAction||
|ImplementedEstatePrivilege||
|ImplementedGovernmentReform||
|ImplementedPolicy||
|ImportExportLateralView||
|ImportExportMarker||
|ImportantCultureItem||
|ImportantReligionItem||
|ImproveOpinionMarker||
|InGameMissionTaskItem||
|InGameTopbar||
|Institution||
|InstitutionItem||
|InstitutionMessage||
|InteractionTarget||
|InternationalOrganization||
|InternationalOrganizationMessagePopup||
|InternationalOrganizationType||
|InternationalOrganizationTypeView||
|InternationalOrganizationsView||
|JominiGameRules||
|JominiLoadWindow||
|JominiNotification|Jomini Notification Item|
|JominiSettingsWindow|Jomini Settings Window|
|LackingGoodsForRepairEntry||
|LandOwnershipRule||
|Language||
|LanguageFamily||
|LateralView||
|Law||
|LawWithContextWrap||
|Layer|Map Editor - Map Object Layer|
|LayerTreeItem|Map Editor - Map Object Layer Tree Item|
|LeaderCandidate||
|LevySetup||
|Loan||
|LoanEntry||
|LobbyPlayer|Jomini Multiplayer - Lobby Player|
|LobbyView|Multiplayer GUI - Lobby View|
|Location||
|LocationBuildingItem||
|LocationItem||
|LocationPopItem||
|LocationPopPieChartTooltipWidget||
|LocationPopulationChart||
|LocationRank||
|LocationReference||
|LocationToBuildItem||
|LocationToRecruitItem||
|LocationView||
|LocationViewSelectProvince||
|LocationsListView||
|LocationsListViewItem||
|LogViewer|Log Viewer Window|
|MaintenanceSetting||
|ManageSubjectsLateralView||
|MapContentEditorViewport|Map Editor - Map Content Viewport|
|MapEditor|Map Editor - Main|
|MapEditorGui|Map Editor - Main GUI|
|MapObjectPainter|Map Editor - Map Object Painter|
|MapObjectPainterOptions|Map Editor - Map Object Painter Options|
|MapObjectTool|Map Editor - Map Object Tool|
|Maritime||
|MaritimeInLocationWrap||
|MaritimeItem||
|MaritimeLateralView||
|MaritimePresence||
|Market||
|MarketAccessWrap||
|MarketCountryNeeds||
|MarketMarker||
|MarketViewSelectMarket||
|MarketingContainer||
|MarketsView||
|MaskPainterViewport|Map Editor - Mask Painter Viewport|
|MemberTypeItem||
|Mercenary||
|MercenaryItem||
|MercenaryTypeItem||
|Merchant||
|MerchantCapacityInMarketWrap||
|MerchantPowerInMarketWrap||
|MeshImporter|Mesh Importer Window|
|MessagePopup||
|Migration||
|MilitaryObjective||
|MilitaryObjectiveGroupView||
|MilitaryObjectiveGroupsView||
|MissionAlert||
|MissionDefinition||
|MissionItem||
|MissionLateralView||
|MissionMessage||
|MissionProgress||
|MissionTaskDefinition||
|MissionTaskItem||
|MissionTaskMessage||
|MissionTasksLateralView||
|ModifierDebugInspectorPlugin||
|ModifierSourceWrap||
|ModsGui|Mods Gui Data Context|
|ModsPlayset||
|ModsPlaysetEntry||
|MultiUnitSelectUnit||
|MultiUnitWindow||
|MultiplayerSetupWindow|Jomini Multiplayer - Setup window|
|NavyConstructionMarker||
|NewBornMessage||
|NewCountryCandidate||
|OngoingRelationCountry||
|OosData|Jomini Multiplayer - Out-of-sync data|
|OrgItem||
|OutbreakItem||
|Outliner||
|OutlinerCabinetEntry||
|OutlinerDiplomacyEntry||
|OutlinerPlayerEntry||
|OutlinerSettings||
|Parliament||
|ParliamentAgenda||
|ParliamentAgendaGlue||
|ParliamentAgendaItem||
|ParliamentInSession||
|ParliamentIssue||
|ParliamentIssueWithContextWrap||
|ParliamentMarker||
|ParliamentType||
|Payment||
|PaymentWithContextWrap||
|PdxAccount||
|PdxGuiWidget|GUI Widget|
|PdxSetting|Settings Window - Setting|
|PeaceOfferLateralView||
|PeaceOfferLateralViewParticipant||
|PeaceTreaty||
|PeopleDynastyItem||
|PeoplePopItem||
|PeopleRebelItem||
|Periphora||
|PinningManager||
|Playable|Jomini Playable|
|PlayerEntryForChat||
|PlayerModifiersLateralView||
|Policy||
|PolicyWithContextWrap||
|Pop||
|PopCultureItem||
|PopEntry||
|PopPoliticsItem||
|PopReligionItem||
|PopTaxItem||
|PopType||
|PopTypeEntry||
|PopsCountryItem||
|PopsLocationItem||
|PopsOverview||
|PopsProvinceItem||
|PortMarker||
|PortraitEditorWindow|Portrait Editor Window|
|PossibleDisease||
|PossibleExplorationItem||
|PossibleItem||
|PossibleLeaderItem||
|PossiblePrivateerItem||
|PossibleSubUnitDefinition||
|PossibleTrade||
|PossibleTradesSelectMarket||
|Price||
|Privateer||
|PrivilegeItem||
|ProducedOnMarketWrap||
|ProductionMethod||
|ProductionMethodItem||
|ProductionSelectMarket||
|ProductionView||
|Province||
|ProvinceDefinition||
|QuickCabinetCardModifier||
|QuickDiplomaticActions||
|QuickTemporaryCountryRelations||
|QuickUnitActions||
|RawGoodLocationItem||
|RawGoodsMarker||
|Rebel||
|RebelDetailsLateralView||
|RecruitInLocationLateralView||
|RecruitScoreRanking||
|RecruitmentMethod||
|ReformItem||
|RegencyType||
|Region||
|RelationDescItem||
|RelationTypeItem||
|RelativePowerTooltipGlue||
|Religion||
|ReligionGroup||
|ReligionItem||
|ReligionMessage||
|ReligionsLedger||
|ReligiousAspect||
|ReligiousAspectGlue||
|ReligiousFaction||
|ReligiousFactionActionGlue||
|ReligiousFactionGlue||
|ReligiousFigure||
|ReligiousFigureGlue||
|ReligiousFocus||
|ReligiousFocusGlue||
|ReligiousSchool||
|RenameDialog||
|ReorgWindow||
|ReportIssueWindow||
|ResearchMessage||
|Resolution||
|ResolutionGlue||
|RoadBuilder||
|RoadDestinationItem||
|RoadType||
|RoadTypeItem||
|RulerTerm||
|RulerTermEntry||
|RulerTraitEntry||
|RulingHistoryView||
|SaintGlue||
|SaveGame||
|SaveGameAnalysisView||
|ScaledStaticModifierWrap||
|Scenario||
|SceneEditor|Scene Editor Window|
|Scope||
|ScopeDebugInspectorPlugin||
|ScopedEditorSettingsCategory||
|Score||
|ScoreView||
|ScoreViewItem||
|ScriptProfilerGui||
|ScriptRunnerInspector||
|ScriptableHintDefinition||
|ScriptedHintItem||
|ScriptedPeaceTreatyType||
|ScriptedRelationType||
|ScriptedRelationTypeWithContextWrap||
|SeaZoneView||
|SearchBar||
|SearchFilter||
|SearchFilterCategory||
|SelectCasusBelli||
|SelectCharacterInteraction||
|SelectChildEducation||
|SelectCountryDiplomacyLateralView||
|SelectCreateCasusBelliWindow||
|SelectHeirSelection||
|SelectInteractionTargetGlue||
|SelectInteractionTargetView||
|SelectLoanLateralView||
|SelectMissionLateralView||
|SelectParticipant||
|SelectSearchFilter||
|SelectSocietalValue||
|SelectSubjectTypeLateralView||
|SelectedMarketLateralView||
|SetupCondottieriView||
|SetupEditor||
|SetupMercenaryRequirementsView||
|Siege||
|SingleUnitSelectUnit||
|SingleUnitWindow||
|Situation||
|SituationMessagePopup||
|SituationView||
|SocietalValue||
|SocietalValueCandidate||
|SocietalValueItem||
|SocietalValueRequirement||
|SocietalValuesLateralView||
|SpecialStatus||
|SpecificGoodsOnMarketWrap||
|StaticModifier||
|StrategicMilitaryObjective||
|StrategicMilitaryObjectiveGlue||
|StrategicMilitaryObjectiveGroup||
|StrategicObjectiveGroupGlue||
|SubContinent||
|SubUnit||
|SubUnitArray||
|SubUnitCategory||
|SubUnitCombatCounts||
|SubUnitCount||
|SubUnitCounts||
|SubUnitType||
|SubjectItem||
|SubjectMilitaryStance||
|SubjectType||
|SubjectTypeItem||
|SupplyDepot||
|SupplyDepotMarker||
|SupplyOnMarketWrap||
|SupportRebelLateralView||
|TacticalMilitaryObjectiveGroup||
|TacticalObjectiveGroupGlue||
|TargettedActionParameters||
|TaxRateSetting||
|TechnologyLateralView||
|TemporaryDemand||
|TextSearchFilter||
|ThreatenTarget||
|TickTaskDetailsView||
|TickTaskGraphItem||
|TimedModifier||
|TollMarker||
|TopScope||
|Topography||
|Trade||
|TradeDetailsLateralView||
|TradeOverview||
|TradePathItem||
|TradesWrap||
|Trait||
|TransactionProportion||
|TransferUnit||
|TransferUnitType||
|UIMessage||
|UniqueContentItem||
|Unit||
|UnitAbility||
|UnitActionItem||
|UnitDetailsView||
|UnitGlue||
|UnitItem||
|UnitMarker||
|UnitMarkerItem||
|UnitOverview||
|UnitSuppliesWrap||
|UnitTransportStateBag||
|UnitTypeItem||
|UnitTypeLateralView||
|UnitsWrap||
|UnprofitableBuildingsEntry||
|VariableEntry||
|VariableInspectorEntry||
|VariableInspectorPlugin||
|VariableInspectorVariable||
|VariableList||
|VariableListEntry||
|VariableListInspectorPlugin||
|VariableListStore||
|VariableStore||
|Vegetation||
|VfsMountPathBrowser|Gui Data Profiler Window|
|ViewerEntity|Entity Editor - Entity|
|VoteGlue||
|VoteTargetGlue||
|VoterGlue||
|War||
|WarGlue||
|WarGoal||
|WarImpactWrap||
|WarItem||
|WarLateralView||
|WarLateralViewBattle||
|WarLateralViewParticipant||
|WarMessage||
|WarParticipant||
|WarParticipantGlue||
|WarSideGlue||
|WarViewer||
|WarsLedger||
|WarsOverviewWar||
|WeatherSystem||
|WorkOfArt||
|WorkOfArtType||

### Data type descriptions

|Type|Description|Notes|
|---|---|---|
|CFixedValue|64 bit signed fixed point number with 5 decimal places|Max 92233720368547.75807, Min -92233720368547.75808|

## Const vs nonconst

GUI script functions and promotes are categorized into two types: *const* and *nonconst*. These are generally identical in function, but one or the other may be required for certain uses.

Generally, functions and promotes starting with "Access" are used with and return a const type, while those starting with "Get" are used with and return a nonconst type.

## GUI functions

||Please help improve this article or section by expanding it with: more tables.|

GUI functions typically retrieve certain information from the input type or transform it in some way. 
Below are lists of functions available in certain scopes.

|Function|Arguments|Output|Description|
|---|---|---|---|
|Abs_CFixedPoint|unknown|CFixedPoint||
|Abs_float|unknown|float||
|Abs_int32|unknown|int32||
|Abs_int64|unknown|int64||
|AcceptJoinRequests||void||
|AccessActiveDLCs||unknown||
|AccessActiveMods||unknown||
|AccessMapEditorLayerBorders||unknown|Map Editor - Access all Layer borders|
|AccessModsGui||unknown|Access Mods GUI|
|AccessPlayerUnits||unknown||
|AddLocalizationIf|unknown unknown|CString||
|AddTextIf|unknown unknown|CString||
|Add_CFixedPoint|unknown unknown|CFixedPoint||
|Add_CVector2f|unknown unknown|CVector2f||
|Add_float|float float|float||
|Add_int32|unknown unknown|int32||
|Add_int64|unknown unknown|int64||
|Add_uint32|unknown unknown|uint32||
|Add_uint64|unknown unknown|uint64||
|And|unknown unknown|bool|If both arguments are true|
|And3|unknown unknown unknown|bool|If all 3 arguments are true|
|And4|unknown unknown unknown unknown|bool|If all 4 arguments are true|
|And5|unknown unknown unknown unknown unknown|bool|If all 5 arguments are true|
|And6|unknown unknown unknown unknown unknown unknown|bool|If all 6 arguments are true|
|And7|unknown unknown unknown unknown unknown unknown unknown|bool|If all 7 arguments are true|
|And8|unknown unknown unknown unknown unknown unknown unknown unknown|bool|If all 8 arguments are true|
|AndEvalAll|unknown unknown|bool|Evaluates all arguments and then checks if both arguments are true. Using 'And' is preferred.|
|ApplyMilitaryStanceToSubjects|unknown|void||
|ApplySettingsAndIronman||void||
|AreBuildingsClosed|unknown|bool||
|AreBuildingsSubsidized|unknown|bool||
|AreGameRulesEnabled||bool||
|ArrParam|unknown unknown|CString||
|AssaultSiege|unknown|void||
|AssumeControlSiege|unknown|void||
|Audio_PlayEvent|unknown unknown|void||
|AuxVars||unknown||
|BecomeSinglePlayer||void||
|BetweenInclusiveOfMax_CFixedPoint|unknown unknown unknown|bool||
|BetweenInclusiveOfMax_float|unknown unknown unknown|bool||
|BetweenInclusiveOfMax_int32|unknown unknown unknown|bool||
|BetweenInclusiveOfMax_int64|unknown unknown unknown|bool||
|BetweenInclusiveOfMax_uint32|unknown unknown unknown|bool||
|BetweenInclusiveOfMax_uint64|unknown unknown unknown|bool||
|BetweenInclusiveOfMin_CFixedPoint|unknown unknown unknown|bool||
|BetweenInclusiveOfMin_float|unknown unknown unknown|bool||
|BetweenInclusiveOfMin_int32|unknown unknown unknown|bool||
|BetweenInclusiveOfMin_int64|unknown unknown unknown|bool||
|BetweenInclusiveOfMin_uint32|unknown unknown unknown|bool||
|BetweenInclusiveOfMin_uint64|unknown unknown unknown|bool||
|BetweenInclusive_CFixedPoint|unknown unknown unknown|bool||
|BetweenInclusive_float|unknown unknown unknown|bool||
|BetweenInclusive_int32|unknown unknown unknown|bool||
|BetweenInclusive_int64|unknown unknown unknown|bool||
|BetweenInclusive_uint32|unknown unknown unknown|bool||
|BetweenInclusive_uint64|unknown unknown unknown|bool||
|Between_CFixedPoint|unknown unknown unknown|bool||
|Between_float|unknown unknown unknown|bool||
|Between_int32|unknown unknown unknown|bool||
|Between_int64|unknown unknown unknown|bool||
|Between_uint32|unknown unknown unknown|bool||
|Between_uint64|unknown unknown unknown|bool||
|BindFoldOutContext||void|Add a new PdxGuiFoldOut data context to a widget.|
|BoolTo1And2|unknown|int32||
|BoolTo2And1|unknown|int32||
|BribeMercenary|unknown|void||
|BuildModeHasUnfilteredItem|unknown|bool||
|BuildOrExpandBuildingDefault|unknown unknown|void||
|BuildingHasProductionMethodActive|unknown unknown unknown|bool||
|CanAssaultSiege|unknown|bool||
|CanAssumeControlSiege|unknown|bool||
|CanBribeMercenary|unknown|bool||
|CanBuildOrExpandBuilding|unknown unknown|bool||
|CanBuildOrExpandBuildingInfo|unknown unknown|CString||
|CanBuildRoads||bool||
|CanCancelConstruction|unknown|bool||
|CanChangeChildEducation|unknown|bool||
|CanChangeGameSpeed||bool||
|CanChangeMapMode||bool||
|CanChangeToProductionMethod|unknown unknown unknown|bool||
|CanChangeToProductionMethodInfo|unknown unknown unknown|CString||
|CanCloseBuilding|unknown|bool||
|CanCreateMarketInLocation|unknown|bool||
|CanCreateMarketInLocationTooltip|unknown|CString||
|CanDecreaseDesiredMerchantCapacity|unknown|bool||
|CanDelistMercenary|unknown|bool||
|CanDestroyBuilding|unknown|bool||
|CanDestroyMarketInLocation|unknown|bool||
|CanDestroyMarketInLocationTooltip|unknown|CString||
|CanDetachCategory|unknown unknown|bool||
|CanDetachLevies|unknown|bool||
|CanDetachMercenaries|unknown|bool||
|CanDetachRegulars|unknown|bool||
|CanDismissMercenary|unknown|bool||
|CanEditSettingsAfterHost||bool|Multiplayer - If you can edit settings after hosting (depends on MP platform)|
|CanExpandBuilding|unknown|bool||
|CanExtendMercenary|unknown|bool||
|CanGetAchievements||bool||
|CanGoodGetProduced|unknown|bool||
|CanIncreaseDesiredMerchantCapacity|unknown|bool||
|CanMoveUnitBox|unknown unknown|bool||
|CanOpenBuilding|unknown|bool||
|CanPause||bool||
|CanPlayerDoGenericAction|unknown|bool||
|CanPlayerRenameCountry|unknown|bool||
|CanRaiseArmyLevies|unknown|bool||
|CanRaiseNavyLevies|unknown|bool||
|CanRaiseProvinceArmyLevies|unknown|bool||
|CanRaiseProvinceNavyLevies|unknown|bool||
|CanRemove|unknown|bool||
|CanRetreatCombat|unknown|bool||
|CanSelectInternationalOrganizationPolicyNextLaw|unknown unknown|bool||
|CanSelectInternationalOrganizationPolicyPrevLaw|unknown unknown|bool||
|CanSelectNextFocusMarket||bool||
|CanSelectNextMarket|unknown|bool||
|CanSelectNextRelevantCountry|unknown|bool||
|CanSelectNextRelevantLocation|unknown|bool||
|CanSelectNextUnit|unknown|bool||
|CanSelectPolicyNextLaw|unknown|bool||
|CanSelectPolicyPrevLaw|unknown|bool||
|CanSelectPrevFocusMarket||bool||
|CanSelectPrevMarket|unknown|bool||
|CanSelectPrevRelevantCountry|unknown|bool||
|CanSelectPrevRelevantLocation|unknown|bool||
|CanSelectPrevUnit|unknown|bool||
|CanShowConstructionCancellationDialog|unknown|bool||
|CanShowConstructionType|unknown|bool||
|CanShowPauseMenu||bool||
|CanSubsidizeBuilding|unknown|bool||
|CanSubsidizeBuildings|unknown|bool||
|CanTakeOverSiege|unknown|bool||
|CanToggleAllowExtendMercenary|unknown|bool||
|CanToggleBuilding|unknown|bool||
|CanToggleBuildings|unknown|bool||
|CanUnitViewerOpen||bool||
|CanUnpause||bool||
|CanUpgradeSubUnit|unknown|bool||
|CanUpgradeSubUnitTooltip|unknown|CString||
|CanUpgradeToBuilding|unknown unknown|bool||
|CanUpgradeToBuildingInfo|unknown unknown|CString||
|CanViewColonyScreen||bool||
|CancelAllMarketTrades|unknown|void||
|CancelConstruction|unknown|void||
|CancelJoinServer||void||
|CancelMilitaryObjectiveGlobally|unknown|void||
|CancelTrade|unknown|void||
|CancelUnitMilitaryObjective|unknown|void||
|ChangeBuildingProductionMethod|unknown unknown unknown|void||
|ChangeProductionMethod|unknown unknown|void||
|CharactersCanMarry|unknown unknown|bool||
|ClearHostError||void|Multiplayer - Clear host error|
|ClearLobbyTab||void||
|ClearMapModeSelectorVarsInSeconds|unknown|void||
|ClearSelectedInstitution||void||
|CloseAllTooltips||void||
|CloseBuilding|unknown|void||
|CloseSettingsWindow||void||
|ColorToVector3f|unknown|CVector3f||
|ColorToVector3i|unknown|CVector3i||
|ColorToVector4i|unknown|CVector4i||
|CombatRetreat|unknown|void||
|ConcatIfNeitherEmpty|unknown unknown|CString||
|ConcatParams|unknown unknown|CString||
|Concatenate|unknown unknown|CString||
|Concept|unknown unknown|CString||
|ContainsMultipleTypes|unknown|bool||
|CopyServerID||void|Multiplayer - Copy Server ID of current session to clipboard|
|CountYes2|unknown unknown|CString||
|CountYes3|unknown unknown unknown|CString||
|CountYes4|unknown unknown unknown unknown|CString||
|CountYes5|unknown unknown unknown unknown unknown|CString||
|CountYes6|unknown unknown unknown unknown unknown unknown|CString||
|CreateMarketInLocation|unknown|void||
|CurrentAndMaxToProgressbarValueInt32|unknown unknown|float|Get the progress (0.0-100.0) of CurrentArg to MaxArg. Value is clamped between 0 and 100.|
|Custom|unknown|CString||
|DataModelFirst|unknown unknown|unknown||
|DataModelHasItems|unknown|bool||
|DataModelLast|unknown unknown|unknown||
|DataModelRepeatedItem|unknown|unknown|The data function used for mocking empty list items, requires int32 (number of items) as a parameter. Example: datamodel = [RepeatedItem( '(int32)4' )]|
|DataModelSkipFirst|unknown unknown|unknown||
|DataModelSkipLast|unknown unknown|unknown||
|DataModelSubSpan|unknown unknown unknown|unknown||
|DeclinePassword||void||
|DecreaseAutomatedTradeCapacity|unknown unknown|void||
|DecreaseDesiredMerchantCapacity|unknown|void||
|DelistMercenary|unknown|void||
|DeselectUnit|unknown|void||
|DestroyBuilding|unknown|void||
|DestroyMarketInLocation|unknown|void||
|DetachCategory|unknown unknown|void||
|DetachHalfCategory|unknown unknown|void||
|DetachLevies|unknown|void||
|DetachMercenaries|unknown|void||
|DetachRegulars|unknown|void||
|DismissMercenary|unknown|void||
|DisplayPopulationNumber|unknown|CString||
|Divide_CFixedPoint|unknown unknown|CFixedPoint||
|Divide_CVector2f|unknown unknown|CVector2f||
|Divide_float|unknown unknown|float||
|Divide_int32|unknown unknown|int32||
|Divide_int64|unknown unknown|int64||
|Divide_uint32|unknown unknown|uint32||
|Divide_uint64|unknown unknown|uint64||
|DoubleToFloat|unknown|float||
|DowngradeLocationRank|unknown|void||
|Embark|unknown|void||
|EqualTo_CFixedPoint|unknown unknown|bool||
|EqualTo_CVector2f|unknown unknown|bool||
|EqualTo_float|unknown unknown|bool||
|EqualTo_int32|unknown unknown|bool||
|EqualTo_int64|unknown unknown|bool||
|EqualTo_string|unknown unknown|bool||
|EqualTo_uint32|unknown unknown|bool||
|EqualTo_uint64|unknown unknown|bool||
|ErrorTooltip||CString||
|EvaluateTrigger|unknown unknown|bool||
|ExecuteConsoleCommand|unknown|void|Execute a single console command with a given command.|
|ExecuteConsoleCommands|unknown|void|Execute a sequence of console commands split by ';'. And stops the sequence execution if a console command fails.|
|ExecuteConsoleCommandsForced|unknown|void|Execute a sequence of console commands split by ';'. Keeps the sequence execution even if a console command fails.|
|ExpandBuilding|unknown|void||
|ExpandBuildingCtrl|unknown|void||
|ExpandBuildingDefault|unknown|void||
|ExpandBuildingShift|unknown|void||
|ExtendMercenary|unknown|void||
|ExtendRegency|unknown|void||
|FIRRecordedFramesCount||int32||
|FixedPointToFloat|unknown|float||
|FixedPointToFloatPercentageCapped|unknown unknown|float||
|FixedPointToInt|unknown|int32||
|FixedPointToProgressbarValue|unknown|float|Convert to a progress percentage value (by multiplying with 100, unclamped).|
|GameCancelLoadingAndGoToFrontEnd||void||
|GameHasMultiplePlayers||bool||
|GameIsCloudStorageAvailable||bool||
|GameIsCloudStorageOperationInProgress||bool||
|GameIsConnectingMultiplayer||bool||
|GameIsIronman||bool||
|GameIsMultiplayer||bool||
|GateString|unknown unknown|CString||
|GetActiveInstitutions||unknown||
|GetActiveMapMode||unknown||
|GetActiveRebelsList||CString||
|GetAdvanceIcon|unknown|unknown||
|GetAgeEndingDate|unknown|CString||
|GetAgeIcon|unknown|unknown||
|GetAlertOfTypeShowingCount|unknown|uint32||
|GetAllInternationalOrganizations||unknown||
|GetAllPossibleBuildingInfo|unknown|CString||
|GetAllSubUnitCategories||unknown||
|GetArmySizeRatio|unknown unknown|CFixedPoint||
|GetArtistIcon|unknown|unknown||
|GetAssumeControlSiegeTooltip|unknown|CString||
|GetAudioEffect|unknown|unknown||
|GetAutoModifier|unknown|unknown||
|GetAutomatedSystemItem|unknown|unknown||
|GetAutomatedSystemItem2|unknown unknown|unknown||
|GetAutomatedSystemItem3|unknown unknown unknown|unknown||
|GetAutomatedSystemItem4|unknown unknown unknown unknown|unknown||
|GetAutomatedSystemItem5|unknown unknown unknown unknown unknown|unknown||
|GetAutomatedSystemItem6|unknown unknown unknown unknown unknown unknown|unknown||
|GetAutosaveName||CString||
|GetAvatarIcon|unknown|unknown||
|GetBattleUnitIcon|unknown|unknown||
|GetBoolean|unknown|bool||
|GetBribeMercenaryTooltip|unknown|CString||
|GetBuildOrExpandBuildingCost|unknown unknown|CFixedPoint||
|GetBuildOrExpandBuildingCostValue|unknown unknown|CString||
|GetBuildRevision||CString||
|GetBuildRevisionDescription||CString||
|GetBuildRevisionTime||CString||
|GetBuildingCategoryIcon|unknown|unknown||
|GetBuildingIcon|unknown|unknown||
|GetBuildingTypeProfitInLocation|unknown unknown|CFixedPoint||
|GetBuildingTypeProfitInLocationInfo|unknown unknown|CString||
|GetCabinetActionIcon|unknown|unknown||
|GetCabinetActionTooltip|unknown|CString||
|GetCanDecreaseGameSpeedString||CString||
|GetCanGoToFrontend||bool|Multiplayer GUI - Can we go back to the frontend?|
|GetCanGoToFrontendDesc||CString|Multiplayer GUI - Message if we can't go back to the frontend|
|GetCanIncreaseGameSpeedString||CString||
|GetCancelConstructionInfo|unknown|CString||
|GetCardinalsTooltip|unknown|CString||
|GetCasusBelliIcon|unknown|unknown||
|GetChangeChildEducationInfo|unknown|CString||
|GetCharacterInteractionIcon|unknown|unknown||
|GetCharacterQuickActions|unknown|unknown||
|GetClimateFrame|unknown|unknown||
|GetClimateIcon|unknown|unknown||
|GetCloseBuildingInfo|unknown|CString||
|GetColorDLC|unknown|CVector4f||
|GetCompleteVersionInfoString||CString||
|GetConceptTexture|unknown|unknown||
|GetConstructionBuildingOwner|unknown|CString||
|GetConstructionIcon|unknown|unknown||
|GetCountries||unknown||
|GetCountryInteractionIcon|unknown|unknown||
|GetCountryListWithFlags|unknown unknown|CString||
|GetCountryPopulation|unknown|CFixedPoint||
|GetCountryPrimaryColor|unknown|CVector4f||
|GetCountryRankIcon|unknown|unknown||
|GetCountrySecondaryColor|unknown|CVector4f||
|GetCountryTypeIcon|unknown|unknown||
|GetCountryUnitPrimaryColor|unknown unknown|CVector4f||
|GetCountryUnitSecondaryColor|unknown unknown|CVector4f||
|GetCountryUnitTertiaryColor|unknown unknown|CVector4f||
|GetCulturesPenaltyInfo||CString||
|GetCuriaTooltip|unknown|CString||
|GetCurrentAgeAdvancesList|unknown|unknown||
|GetCurrentAgeAdvancesText|unknown|CString||
|GetCurrentAgePercentage||float||
|GetCurrentGameSpeed||int32||
|GetCurrentGameSpeedFrame||int32||
|GetCurrentLoadingScreen||unknown||
|GetCurrentYear||CString||
|GetDataModelSize|unknown|int32||
|GetDateString||CString||
|GetDecreaseDesiredMerchantCapacityInfo|unknown|CString||
|GetDefaultMapMode||unknown||
|GetDefaultServerName||CUTF8String||
|GetDefine|unknown unknown|unknown||
|GetDefineAtIndex|unknown unknown unknown|unknown||
|GetDelistMercenaryTooltip|unknown|CString||
|GetDestroyBuildingInfo|unknown|CString||
|GetDestroyBuildingInfoOnlyWithCosts|unknown|CString||
|GetDetachCategoryInfo|unknown unknown unknown|CString||
|GetDetachCategoryInfoPossible|unknown unknown unknown|CString||
|GetDetachLeviesInfo|unknown|CString||
|GetDetachMercenariesInfo|unknown|CString||
|GetDetachRegularsInfo|unknown|CString||
|GetDiplomaticPendingWithCountryProgress|unknown|float||
|GetDiplomaticPendingWithCountryText|unknown|CString||
|GetDiplomaticPendingWithCountryTooltip|unknown|CString||
|GetDisasterIllustration|unknown|unknown||
|GetDiseaseIcon|unknown|unknown||
|GetDiseases||unknown||
|GetDismissMercenaryTooltip|unknown|CString||
|GetEducationIcon|unknown|unknown||
|GetEmployedTypePercentage|unknown unknown|CFixedPoint||
|GetEnumIndex|unknown|CVector2i|Settings - Get the dropdown index of an enum setting.|
|GetEstateFlatIcon|unknown|unknown||
|GetEstateIcon|unknown|unknown||
|GetEstateName|unknown|CString||
|GetEstateNameWithNoTooltip|unknown|CString||
|GetEstatePrivilegeIcon|unknown|unknown||
|GetEstatePriviligesOverUILimit|unknown|int32||
|GetEstatePriviligesUILimit||int32||
|GetEthnicities||unknown|Portrait System - Get all Ethnicities|
|GetEventMPTimeout||int32||
|GetExpandBuildingInfo|unknown|CString||
|GetExplorationPreparationTimeDays|unknown unknown unknown|CString||
|GetExtendMercenaryTooltip|unknown|CString||
|GetExtraBuildingClickInfo||CString||
|GetFixedPoint|unknown|CFixedPoint||
|GetFortLimitBreakdown|unknown|CString||
|GetFrontEndScene||unknown||
|GetGameDLCs||unknown||
|GetGameRuleIconTooltip|unknown|CString||
|GetGameSpeedTooltip||CString||
|GetGameTimeDifferenceForDiffDays|unknown|CString||
|GetGameTimeDurationDays|unknown|CString||
|GetGameTimeDurationMonths|unknown|CString||
|GetGameVersionDisplay||CString||
|GetGlobalList|unknown|unknown||
|GetGlobalVariable|unknown|unknown||
|GetGodIcon|unknown|unknown||
|GetGoodPriceIcon|unknown unknown|unknown||
|GetGoodsIcon|unknown|unknown||
|GetGoodsIllustration|unknown|unknown||
|GetGovernmentReformIllustration|unknown|unknown||
|GetGovernmentTypeIcon|unknown|unknown||
|GetGraphicalCultureTexture|unknown|unknown||
|GetGraphicalCultureTextureForCountry|unknown unknown|unknown||
|GetGraphicalCultureTextureForCountryPopType|unknown unknown|unknown||
|GetGraphicalCultureTextureForPop|unknown|unknown||
|GetGraphicalCultureTextureForPopType|unknown|unknown||
|GetGreatPowerIcon|unknown|unknown||
|GetGuiPositionFromPercentCoordinates|unknown unknown unknown|unknown||
|GetGuiWidgetIndexIgnoreInvisible|unknown unknown|int32||
|GetHegemonyBorder|unknown|unknown||
|GetHegemonyIcon|unknown|unknown||
|GetHeirSelectionIcon|unknown|unknown||
|GetHighlightAnim|unknown|float||
|GetHighlightTint||CVector4f||
|GetHireMercenaryTooltip|unknown|CString||
|GetHolySiteTypeIcon|unknown|unknown||
|GetHostError||CUTF8String|Multiplayer - Get host error|
|GetIncomeRatio|unknown unknown|CFixedPoint||
|GetIncreaseDesiredMerchantCapacityInfo|unknown|CString||
|GetInstitutionIcon|unknown|unknown||
|GetInstitutionImage|unknown|unknown||
|GetIntegrationLevelIcon|unknown|unknown||
|GetIntegrationLevelIconPath|unknown|CString||
|GetInternationalOrganizationViewName|unknown|CString||
|GetInvParentScale|unknown|float||
|GetInverseZoom||float||
|GetInverseZoom2||CVector2f||
|GetIsChecked|unknown|bool|Settings - If the bool setting is checked|
|GetLackingFromBuildingTypeString|unknown unknown|CString||
|GetLackingPopsFromBuildingType|unknown unknown|CString||
|GetLandCombatPowerTooltipUI|unknown unknown|CString||
|GetLandComparisonTooltipUI|unknown unknown|CString||
|GetLawBgCategoryColor|unknown|unknown||
|GetLawCategoryIcon|unknown|unknown||
|GetLawIcon|unknown|unknown||
|GetLegitimacyIcon|unknown|unknown||
|GetLevyPowerRatio|unknown unknown|CFixedPoint||
|GetLevyUnitIcon||unknown||
|GetListLandCombatPowerTooltipUI|unknown unknown unknown|CString||
|GetListNavalCombatPowerTooltipUI|unknown unknown unknown|CString||
|GetListOfAvailableBuildingsWithModifier|unknown|CString||
|GetListOfGoodsUsingMethod|unknown|CString||
|GetListOnlyLandCombatPowerTooltipUI|unknown unknown|CString||
|GetLoadingScreenConcept||CString||
|GetLoadingScreenConceptName||CString||
|GetLoadingScreenDeveloperText||CString||
|GetLoadingScreenLoadTip||CString||
|GetLoadingScreenProgress||float||
|GetLoadingScreenStatusText||CString||
|GetLocalizedDefine|unknown unknown|CString||
|GetLocalizedDefineAtIndex|unknown unknown unknown|CString||
|GetLocationRankIcon|unknown|unknown||
|GetLossCauseEnum|unknown|unknown||
|GetMPChecksum||unknown||
|GetManpowerDisplay|unknown|CString||
|GetMapColorLedger||unknown||
|GetMapColorLedgerByName|unknown|unknown||
|GetMapMode|unknown|unknown||
|GetMapModeGroupFromCategory|unknown unknown|unknown||
|GetMapModesFromCategory|unknown|unknown||
|GetMarketRangeInfo|unknown|CString||
|GetMaxAllowedReligiousFigures||CFixedPoint||
|GetMaxInDataTrend|unknown|float||
|GetMaxManpowerRatio|unknown unknown|CFixedPoint||
|GetMaxSailorRatio|unknown unknown|CFixedPoint||
|GetMilitaryObjectiveIcon|unknown|unknown||
|GetMilitaryStanceIcon|unknown|unknown||
|GetMilitaryStances||unknown||
|GetMilitaryStrengthRatio|unknown unknown|CFixedPoint||
|GetMinInDataTrend|unknown|float||
|GetMissionIllustration|unknown|unknown||
|GetMissionTaskIcon|unknown|unknown||
|GetModifier|unknown|unknown||
|GetMonthlyMaintenanceInfoForCountry|unknown unknown unknown|CString||
|GetMoveUnitBoxInfo|unknown unknown|CString||
|GetMultiplayerAccessibleString||CString||
|GetMultiplayerSyncInfo||CString||
|GetNavalCombatPowerTooltipUI|unknown unknown|CString||
|GetNavalComparisonTooltipUI|unknown unknown|CString||
|GetNavyLevyPowerRatio|unknown unknown|CFixedPoint||
|GetNavySizeRatio|unknown unknown|CFixedPoint||
|GetNavyStrengthRatio|unknown unknown|CFixedPoint||
|GetNeedInformation|unknown unknown|CString||
|GetNoLawsInfo||CString||
|GetNoRoadsInfo||CString||
|GetNonUniqueInternationalOrganizationTypes||unknown||
|GetNullStringPtr||unknown||
|GetNumberAbove_int32|unknown unknown|int32||
|GetOpenBuildingInfo|unknown|CString||
|GetOurOpinionPlayer|unknown|CFixedPoint||
|GetOurOpinionPlayerTooltip|unknown|CString||
|GetOutCompetedInfo|unknown|CString||
|GetParliamentTypeIcon|unknown|unknown||
|GetPauseTooltip||CString||
|GetPeaceOfferIcon|unknown|unknown||
|GetPinnedMapModes|unknown|unknown||
|GetPlayStyleItem|unknown|unknown||
|GetPlayer||unknown||
|GetPlayerAITooltip|unknown|CString||
|GetPlayerName|unknown|CString||
|GetPlayerNameForStartAnim||CString||
|GetPlayerTargettedActionParams||TargettedActionParameters||
|GetPlayersCount||int32|Multiplayer - No of players of current session|
|GetPolicyIcon|unknown|unknown||
|GetPopIcon|unknown|unknown||
|GetPopTypeByName|unknown|unknown||
|GetPopTypeImpactInfo|unknown|CString||
|GetPopTypes||unknown||
|GetPopulationFromBuilding|unknown|CString||
|GetPopulationFromBuildingType|unknown unknown|CString||
|GetPopulationRatio|unknown unknown|CFixedPoint||
|GetPortraitTextureFromDna|unknown unknown|unknown||
|GetPossibleBuildingInfo|unknown unknown|CString||
|GetPossibleProductionMethodIndex|unknown unknown|int32||
|GetPossibleRGOUpgradeInfo|unknown unknown|CString||
|GetPrimaryCultureSizePercentage|unknown|CFixedPoint||
|GetProductionMethodIcon|unknown|unknown||
|GetProductionMethods||unknown||
|GetQuickMissionList||unknown||
|GetRandomLogInfo||CString||
|GetRankComparisonForCountryInfo|unknown|CString||
|GetRawTextTooltipTag|unknown|CString||
|GetRebelIllustration|unknown|unknown||
|GetRebelsIcon|unknown|unknown||
|GetRecruitMethodIcon|unknown|unknown||
|GetReformsUILimit||int32||
|GetRelationOverUILimit|unknown|int32||
|GetRelationTypeIcon|unknown|unknown||
|GetRelationsUILimit||int32||
|GetRelativePowerDescriptionTooltip|unknown unknown|CString||
|GetRelativePowerPlayerDescription|unknown|CString||
|GetReligionIcon|unknown|unknown||
|GetReligions||unknown||
|GetReligiousAspectIcon|unknown|unknown||
|GetReligiousFactionIcon|unknown|unknown||
|GetReligiousFocusIcon|unknown|unknown||
|GetReligiousOrganizationIcon|unknown|unknown||
|GetResolutionX||float||
|GetResolutionY||float||
|GetResumeLabel||CString||
|GetResumeTooltip||CString||
|GetRetreatCombatTooltip|unknown|CString||
|GetRoadCostCalculationIcon|unknown|unknown||
|GetRoadCostTo|unknown unknown|CString||
|GetRoadCostToTooltip|unknown unknown|CFixedPoint||
|GetRoadDistanceTo|unknown unknown|int32||
|GetRoadTypeIcon|unknown|unknown||
|GetRuleToolTip|unknown|CString||
|GetRulerTraitProgress||float||
|GetRulerTraitProgressInfo||CString||
|GetScreenCenterX||float||
|GetScreenCenterY||float||
|GetScriptedRelationType|unknown|unknown||
|GetSelectedCountryOrByLocation||unknown||
|GetSelectedDiplomaticInformation|unknown|CString||
|GetServer||CString||
|GetShortVersionInfoString||CString||
|GetSiegeAssaultTooltip|unknown|CString||
|GetSituationIllustration|unknown|unknown||
|GetSocietalValues||unknown||
|GetSpecialStatusIcon|unknown|unknown||
|GetSpecialStatusIconFromKey|unknown|unknown||
|GetStringSettingText|unknown|CString|Settings - Get the string setting text|
|GetString_CPdxFloatRect|unknown|CString||
|GetString_CPdxIntRect|unknown|CString||
|GetString_CVector2f|unknown|CString||
|GetString_CVector2i|unknown|CString||
|GetString_CVector3f|unknown|CString||
|GetString_CVector3i|unknown|CString||
|GetString_CVector4f|unknown|CString||
|GetString_CVector4i|unknown|CString||
|GetSubCategory|unknown|unknown||
|GetSubCategoryByIndex|unknown|unknown||
|GetSubCategoryIndex|unknown|int32||
|GetSubDefinition|unknown|unknown||
|GetSubDefinitionByIndex|unknown|unknown||
|GetSubDefinitionIndex|unknown|int32||
|GetSubUnitCategoryFlatIcon|unknown|unknown||
|GetSubUnitCategoryIcon|unknown|unknown||
|GetSubUnitDefinitionIcon|unknown|unknown||
|GetSubUnitDragDrop|unknown|CString||
|GetSubjectTypeIcon|unknown|unknown||
|GetSubsidizeBuildingInfo|unknown|CString||
|GetSubsidizeBuildingsInfo|unknown|CString||
|GetSubunitIllustration|unknown|unknown||
|GetSubunitIllustrationMask|unknown|unknown||
|GetSubunitTypeIllustration|unknown unknown|unknown||
|GetSubunitTypeIllustrationMask|unknown unknown|unknown||
|GetTakeOverSiegeTooltip|unknown|CString||
|GetTextFromSelfOrAnyChildEditbox|unknown|CString||
|GetTheirOpinionPlayer|unknown|CFixedPoint||
|GetTheirOpinionPlayerTooltip|unknown|CString||
|GetToggleBuildingInfo|unknown|CString||
|GetToggleBuildingsInfo|unknown|CString||
|GetToggleSuffix|unknown|CString||
|GetTopographyIcon|unknown|unknown||
|GetTopographyIconBig|unknown|unknown||
|GetTotalArmyLevySize|unknown|CString||
|GetTotalArmyLevySizeTooltip|unknown|CString||
|GetTotalNavyLevySize|unknown|CString||
|GetTotalNavyLevySizeTooltip|unknown|CString||
|GetTotalProvinceArmyLevySize|unknown|CString||
|GetTotalProvinceArmyLevySizeTooltip|unknown|CString||
|GetTotalProvinceNavyLevySize|unknown|CString||
|GetTotalProvinceNavyLevySizeTooltip|unknown|CString||
|GetTraitBackground|unknown|unknown||
|GetTraitIcon|unknown|unknown||
|GetTraitTypeList|unknown|unknown||
|GetUnEmployedFromBuildingType|unknown unknown|CString||
|GetUnEmployedPeasantsFromLocation|unknown|CString||
|GetUnEmployedPeasantsFromLocationValue|unknown|CFixedPoint||
|GetUniqueInternationalOrganizations||unknown||
|GetUnitAbilityIcon|unknown|unknown||
|GetUnitIcon|unknown|unknown||
|GetVarTimeRemaining|unknown unknown|int32||
|GetVegetationIcon|unknown|unknown||
|GetVegetationIconBig|unknown|unknown||
|GetWarGoalIcon|unknown|unknown||
|GetWeatherSystemsInLocation|unknown|unknown||
|GetWillJoinCountryList|unknown unknown|unknown||
|GetWinterIcon|unknown|unknown||
|GetWorkOfArtIcon|unknown|unknown||
|GetWorkOfArtIllustration|unknown|unknown||
|GetWorkOfArtQualityIcon|unknown|unknown||
|GetZoom||float||
|GetZoom2||CVector2f||
|GetZoomStep||int32||
|GfxGetSkins||unknown|Get all skins|
|GfxSetActiveSkin|unknown|void|Set the active GFX skin|
|GfxSkinIsActive|unknown|bool|Test if skin is active|
|GoToCapital||void||
|GoToFrontend||void|Multiplayer GUI - Go back to the frontend|
|GreaterThanOrEqualTo_CFixedPoint|unknown unknown|bool||
|GreaterThanOrEqualTo_float|unknown unknown|bool||
|GreaterThanOrEqualTo_int32|unknown unknown|bool||
|GreaterThanOrEqualTo_int64|unknown unknown|bool||
|GreaterThanOrEqualTo_uint32|unknown unknown|bool||
|GreaterThanOrEqualTo_uint64|unknown unknown|bool||
|GreaterThan_CFixedPoint|unknown unknown|bool||
|GreaterThan_float|unknown unknown|bool||
|GreaterThan_int32|unknown unknown|bool||
|GreaterThan_int64|unknown unknown|bool||
|GreaterThan_uint32|unknown unknown|bool||
|GreaterThan_uint64|unknown unknown|bool||
|HasActiveDLC|unknown|bool||
|HasActiveMod|unknown|bool||
|HasAnyUnitsSelected||bool||
|HasBattleFiredAtHover|unknown|bool||
|HasCountryFlagCoatOfArms|unknown|bool||
|HasDiplomaticPendingWithCountry|unknown|bool||
|HasDlc|unknown|bool||
|HasErrors||bool||
|HasGameRuleFlag|unknown|bool||
|HasGameStartedForTheFirstTime||bool||
|HasHostError||bool|Multiplayer - Does the host have an error|
|HasLackingPopsFromBuildingType|unknown unknown|bool||
|HasLanguage|unknown|bool||
|HasLowFps||bool||
|HasMapColorLedger||bool||
|HasModsView||bool||
|HasPopTypeImpact|unknown|bool||
|HasPossibleBuilding|unknown unknown|bool||
|HasPossibleRGOUpgrade|unknown unknown|bool||
|HasProductionMethodMissingGoods|unknown unknown|bool||
|HasRulerAllTraitsProgress||bool||
|HasWar|unknown unknown|bool||
|HideGameRules||void||
|HideModsView||void||
|ImageLookupNodeIsLoading||bool||
|ImageLookupNodeRefresh||void||
|ImagePathLookupNodeWindowRefresh||void||
|InDebugMode||bool|Is the game in Debug mode?|
|InReleaseMode||bool|Is the game in Release mode?|
|IncreaseAutomatedTradeCapacity|unknown unknown|void||
|IncreaseDesiredMerchantCapacity|unknown|void||
|IntToFixedPoint|unknown|float||
|IntToFloat|unknown|float||
|IntToFrameIndex|unknown|int32|Adds 1 to "unknown".|
|IntToRomanNumeral|unknown|CString||
|IntToUnsigned|unknown|float||
|IsAIDebug||bool||
|IsActionConfirmAndHoldMode||bool||
|IsActionDialogMode||bool||
|IsAnyAlertOfTypeShowing|unknown|bool||
|IsAtWarWithSiegeDefender|unknown|bool||
|IsAutoSaving||bool||
|IsBuildDebug||bool||
|IsBuildingMissingInputGoods|unknown unknown|bool||
|IsBuildingUsingGoods|unknown unknown|bool||
|IsCabinetActionAllowed|unknown|bool||
|IsCameraRestrictionsEnabled||bool|Map Editor - If camera restrictions are on|
|IsCharacterFaved|unknown|bool||
|IsCountryFaved|unknown|bool||
|IsCountryInDataModel|unknown unknown|bool||
|IsCurrentAge|unknown|bool||
|IsCurrentIOLeader|unknown|bool||
|IsDarkColor|unknown|bool||
|IsDataModelEmpty|unknown|bool||
|IsDefaultMapModeSet||bool||
|IsEven_int32|unknown|bool||
|IsEven_int64|unknown|bool||
|IsEven_uint32|unknown|bool||
|IsEven_uint64|unknown|bool||
|IsFaved|unknown unknown|bool||
|IsFocusMarketSelected||bool||
|IsFocusMarketValid||bool||
|IsFutureAge|unknown|bool||
|IsFutureAgeFromName|unknown|bool||
|IsGamePaused||bool||
|IsGamePausedByGame||bool||
|IsGamePausedByOtherPlayer||bool||
|IsGamePausedByPlayer||bool||
|IsGamePreloading||bool||
|IsGamePreloadingComplete||bool||
|IsGameSpeedEqualOrGreaterThan|unknown|bool||
|IsGameViewOpen|unknown|bool||
|IsGoodsFaved|unknown|bool||
|IsHintPriority|unknown|bool||
|IsHost||bool||
|IsIOFaved|unknown|bool||
|IsInDiplomaticRange|unknown|bool||
|IsInGame||bool||
|IsInSameWarAsSiegeOwner|unknown|bool||
|IsInternationalOrganizationTypeViewOpen||bool||
|IsInternationalOrganizationTypeViewOpenForNamedInternationalOrganizationType|unknown|bool||
|IsInternationalOrganizationViewOpen|unknown|bool||
|IsInternationalOrganizationViewOpenForNamedInternationalOrganization|unknown|bool||
|IsJoinServerByIdWithTextWidgetEmpty|unknown|bool||
|IsLateralGroupHighlighted|unknown|bool||
|IsLateralGroupOpened|unknown|bool||
|IsLateralViewFullScreen||bool||
|IsLateralViewMenuFullScreen||bool||
|IsLateralViewOpened|unknown|bool||
|IsLateralViewOpenedWithParams|unknown unknown|bool||
|IsLawsEnabled||bool||
|IsLiveBuild||bool||
|IsLobbyOpen||bool||
|IsLocalPlayer|unknown|bool||
|IsLocalPlayerReplayingCommands||bool||
|IsLocationFaved|unknown|bool||
|IsMapInit||bool||
|IsMarketAutomated|unknown|bool||
|IsMarketFaved|unknown|bool||
|IsMarketInRange|unknown|bool||
|IsMessageLogShown||bool||
|IsMissionsEnabled||bool||
|IsMultiplayerAvailable||bool||
|IsMultiplayerChatShown||bool||
|IsObserving||bool||
|IsObservingWithoutSelectedCountry||bool||
|IsOdd_int32|unknown|bool||
|IsOdd_int64|unknown|bool||
|IsOdd_uint32|unknown|bool||
|IsOdd_uint64|unknown|bool||
|IsOutCompeted|unknown|bool||
|IsOutlinerCategoryShown|unknown|bool||
|IsOutlinerShown||bool||
|IsOwnHiredMercenary|unknown|bool||
|IsOwnMercenary|unknown|bool||
|IsPasswordEmpty||bool||
|IsPauseMenuShown||bool||
|IsPlayStyleEnabled|unknown|bool||
|IsPlayer||bool||
|IsPlayerAIEnabled|unknown|bool||
|IsPlayerAtWarWithOtherPlayer|unknown|bool||
|IsPlayerCountry|unknown|bool||
|IsPlayerEnemy|unknown|bool||
|IsPlayerHotjoining||bool||
|IsPlayerObserver||bool||
|IsPlayerRival|unknown|bool||
|IsPlayerSubject||bool||
|IsPlayerTooltip||CString||
|IsPlayerValid||bool||
|IsPlaythroughSkipped||bool||
|IsPreparationLobby||bool||
|IsRecalculatingCacheData||bool||
|IsRevolutionaryTargetActive||bool||
|IsSaveGame||bool||
|IsSaving||bool||
|IsScreenGrabWorking||bool||
|IsSeazoneFaved|unknown|bool||
|IsSelfOrAnyChildAnEmptyEditbox|unknown|bool||
|IsShowingDialog||bool||
|IsSpecificInternationalOrganizationTypeViewOpen|unknown|bool||
|IsSystemAutomatedByPlayStyle|unknown|bool||
|IsUnitSelected|unknown|bool||
|IsWelcomeNewGameSkipped||bool||
|IsWritingDumps||bool||
|JoinJominiServer|unknown|void||
|JoinServerByIdWithTextWidget|unknown unknown unknown|void||
|JoinText|unknown unknown unknown|CString||
|JominiAccessPlayerJoinRequests||unknown||
|JominiAreAchievementsAvailable||bool|Jomini Achievements - Are achievements available?|
|JominiGetAchievementsNotAvailableString||CString|Jomini Achievements - Get text why achievements are not available|
|JominiGetMultiplayerAccessibleString||CString||
|JominiHasPlayerJoinRequests||bool||
|JominiIsHostOrLocal||bool||
|JominiIsMultiplayerAccessible||bool||
|JominiMultiplayerIsCrossplayEnabled||bool||
|JominiMultiplayerIsCrossplayFilterAvailable||bool||
|JominiPlayer||unknown|Jomini Script Systen - Get generic current playable object|
|KickPlayerOOS||void||
|LastSelectInteractionTargetGlueWasTarget||bool||
|LessThanOrEqualTo_CFixedPoint|unknown unknown|bool||
|LessThanOrEqualTo_float|unknown unknown|bool||
|LessThanOrEqualTo_int32|unknown unknown|bool||
|LessThanOrEqualTo_int64|unknown unknown|bool||
|LessThanOrEqualTo_uint32|unknown unknown|bool||
|LessThanOrEqualTo_uint64|unknown unknown|bool||
|LessThan_CFixedPoint|unknown unknown|bool||
|LessThan_float|unknown unknown|bool||
|LessThan_int32|unknown unknown|bool||
|LessThan_int64|unknown unknown|bool||
|LessThan_uint32|unknown unknown|bool||
|LessThan_uint64|unknown unknown|bool||
|Link|unknown unknown unknown|CString||
|LinkParam|unknown unknown|CString||
|LinkRaw|unknown unknown unknown|CString||
|Localize|unknown|CString||
|LocalizeInputAction|unknown|CString||
|LocationWithInRange_Format|unknown unknown|CString||
|MPChatNewMessage||bool||
|MakeItFail|unknown|CString||
|MakeItFailIf|unknown unknown|CString||
|MakeItFailIfLoc|unknown unknown|CString||
|MakeItFailLoc|unknown|CString||
|MakeScopeBool|unknown|Scope||
|MakeScopeFlag|unknown|Scope||
|MakeScopeValue|unknown|Scope||
|MakeShortcutIcon|unknown|CString||
|MakeShortcutIcons|unknown unknown|CString||
|MapMarkerFlagsVisible||bool||
|Max_CFixedPoint|unknown unknown|CFixedPoint||
|Max_CVector2f|unknown unknown|CVector2f||
|Max_float|unknown unknown|float||
|Max_int32|unknown unknown|int32||
|Max_int64|unknown unknown|int64||
|Max_uint32|unknown unknown|uint32||
|Max_uint64|unknown unknown|uint64||
|Min_CFixedPoint|unknown unknown|CFixedPoint||
|Min_CVector2f|unknown unknown|CVector2f||
|Min_float|unknown unknown|float||
|Min_int32|unknown unknown|int32||
|Min_int64|unknown unknown|int64||
|Min_uint32|unknown unknown|uint32||
|Min_uint64|unknown unknown|uint64||
|Modulo_int32|unknown unknown|int32||
|Modulo_int64|unknown unknown|int64||
|Modulo_uint32|unknown unknown|uint32||
|Modulo_uint64|unknown unknown|uint64||
|MoveUnitBox|unknown unknown|void||
|Multiply_CFixedPoint|unknown unknown|CFixedPoint||
|Multiply_CVector2f|unknown unknown|CVector2f||
|Multiply_float|unknown unknown|float||
|Multiply_int32|unknown unknown|int32||
|Multiply_int64|unknown unknown|int64||
|Multiply_uint32|unknown unknown|uint32||
|Multiply_uint64|unknown unknown|uint64||
|NOP||void|No Operation (dummy callback function)|
|Nbsp||CString||
|Negate_CFixedPoint|unknown|CFixedPoint||
|Negate_float|unknown|float||
|Negate_int32|unknown|int32||
|Negate_int64|unknown|int64||
|Not|unknown|bool|If the argument is not true|
|NotEqualTo_CFixedPoint|unknown unknown|bool||
|NotEqualTo_CVector2f|unknown unknown|bool||
|NotEqualTo_float|unknown unknown|bool||
|NotEqualTo_int32|unknown unknown|bool||
|NotEqualTo_int64|unknown unknown|bool||
|NotEqualTo_uint32|unknown unknown|bool||
|NotEqualTo_uint64|unknown unknown|bool||
|NumberOfErrors||int32||
|ObjectsEqual|unknown unknown|bool||
|OnChangedAutomatedTradeCapacity|unknown|void||
|OnCreateAccount||void|Start the account creation flow|
|OnDecreaseGameSpeed||void||
|OnExpandOutlinerSettings|unknown|void||
|OnFindLocation||void||
|OnIncreaseGameSpeed||void||
|OnPause||void||
|OnPauseMenu||void||
|OnSetGameSpeed|unknown|void||
|OnToggleMusicPlayer||void||
|OnToggleOutliner||void||
|OnToggleOutlinerCategory|unknown|void||
|OnlyContainsLevies|unknown|bool||
|OnlyContainsLeviesTT|unknown|CString||
|OnlyContainsMercenaries|unknown|bool||
|OnlyContainsMercenariesTT|unknown|CString||
|OnlyContainsRegulars|unknown|bool||
|OnlyContainsRegularsTT|unknown|CString||
|OnlyOnePossibleFocusMarket||bool||
|OpenAutomationLateralViewAndReveal|unknown|void||
|OpenBuilding|unknown|void||
|OpenBuildingView|unknown|void||
|OpenDiploAction|unknown|void||
|OpenDiplomacy|unknown|void||
|OpenDiplomacyAndPan|unknown|void||
|OpenEconomyView||void||
|OpenEnforceWarGoal||void||
|OpenErrorLog||void||
|OpenFileDirectory|unknown|void||
|OpenGameRules||void||
|OpenGameView|unknown|void||
|OpenInternationalOrganizationView|unknown|void||
|OpenLateralGroup|unknown|void||
|OpenLateralView|unknown|void||
|OpenLateralViewWithArrayFilter|unknown unknown|void||
|OpenLateralViewWithArrayFilterAndParams|unknown unknown unknown|void||
|OpenLateralViewWithFilter|unknown unknown|void||
|OpenLateralViewWithParams|unknown unknown|void||
|OpenMessageDialog|unknown|void||
|OpenMessageSettings||void||
|OpenModsView||void||
|OpenRenameCountryDialog|unknown|void||
|OpenSelectedAgeAndAdvanceTechnology|unknown unknown|void||
|OpenSelectedAgeTechnology|unknown|void||
|OpenSpecificInternationalOrganizationTypeView|unknown|void||
|Or|unknown unknown|bool|If either argument is true|
|Or3|unknown unknown unknown|bool|If any of 3 arguments are true|
|Or4|unknown unknown unknown unknown|bool|If any of 4 arguments are true|
|Or5|unknown unknown unknown unknown unknown|bool|If any of 5 arguments are true|
|Or6|unknown unknown unknown unknown unknown unknown|bool|If any of 6 arguments are true|
|Or7|unknown unknown unknown unknown unknown unknown unknown|bool|If any of 7 arguments are true|
|Or8|unknown unknown unknown unknown unknown unknown unknown unknown|bool|If any of 8 arguments are true|
|OrEvalAll|unknown unknown|bool|Evaluates all arguments and then checks if either argument is true. Using 'Or' is preferred.|
|PanToCharacter|unknown|void||
|PanToCountry|unknown|void||
|PanToLocation|unknown|void||
|PanToProvince|unknown|void||
|PanToProvinceDefinition|unknown|void||
|PdxClearEditBoxText|unknown|void||
|PdxGetProfilerNames||unknown||
|PdxGetWidgetScreenSize|unknown|CVector2f||
|PdxGuiDestroyWidget|unknown|void|Destroy widget|
|PdxGuiEditboxGetText|unknown|CUTF8String||
|PdxGuiInterruptAllAnimations|unknown|void||
|PdxGuiInterruptThenTriggerAllAnimations|unknown unknown|void||
|PdxGuiTriggerAllAnimations|unknown|void||
|PdxProfilerFilterNext||void||
|PdxProfilerFilterPrev||void||
|PdxProfilerFilterTimers||void||
|PdxProfilerGetCurrentFrame||int32||
|PdxProfilerGetFrameTimeMs||float||
|PdxProfilerGetNsPerTick||float||
|PdxProfilerGuiGraphLinesEnabled||bool||
|PdxProfilerGuiToggleGraphLines||void||
|PdxProfilerGuiToggleStats||void||
|PdxProfilerGuiTrackCurrentFrame||void||
|PdxProfilerGuiWriteFrameCSV||void||
|PdxProfilerIsRecording||bool||
|PdxProfilerSelectThread||void||
|PdxProfilerSetFrame||void||
|PdxProfilerToggleRecording||void||
|PerformGenericAction|unknown|void||
|PerformGenericAction1Param|unknown unknown|void||
|PlayAudioEffect|unknown|void||
|PlayerCanRepayAnyLoan||bool||
|PlayerIsHost||bool|Multiplayer GUI - Is the current player the host?|
|RaiseArmyLevies|unknown|void||
|RaiseNavyLevies|unknown|void||
|RaiseProvinceArmyLevies|unknown|void||
|RaiseProvinceNavyLevies|unknown|void||
|RecruitModeHasRecruitItem|unknown|bool||
|RefreshModsView||void||
|RemoveDirectoryPath|unknown|CString||
|RemoveUIFocusMarket||void||
|ResetHighlightAndMapModeOverrides||void||
|ResetHighlightedTab||void||
|ScrollbarToProgressbarValue|unknown unknown unknown|float||
|SelectAllPlayerUnits|unknown|void||
|SelectCapital||void||
|SelectCountryDiplomacy_HasDiplomaticActionItem|unknown|bool||
|SelectDefaultFocusMarket||void||
|SelectEnumWithString|unknown unknown|void|Settings - Select enum by string input|
|SelectGameConcept|unknown unknown unknown|CString||
|SelectInternationalOrganizationPolicyNextLaw|unknown unknown|void||
|SelectInternationalOrganizationPolicyPrevLaw|unknown unknown|void||
|SelectLocalization|unknown unknown unknown|CString||
|SelectLocation|unknown|void||
|SelectLocationToBuild|unknown unknown|void||
|SelectLocationToBuildDefault|unknown|void||
|SelectLocationToBuildWithLocation|unknown unknown unknown|void||
|SelectLocationToRecruit|unknown unknown|void||
|SelectLocationToRiseArmy||void||
|SelectLocationToRiseNavy||void||
|SelectNextFocusMarket||void||
|SelectNextMarket|unknown|void||
|SelectNextRelevantCountry|unknown|void||
|SelectNextRelevantLocation|unknown|void||
|SelectNextUnit|unknown|void||
|SelectPolicyNextLaw|unknown|void||
|SelectPolicyPrevLaw|unknown|void||
|SelectPrevFocusMarket||void||
|SelectPrevMarket|unknown|void||
|SelectPrevRelevantCountry|unknown|void||
|SelectPrevRelevantLocation|unknown|void||
|SelectPrevUnit|unknown|void||
|SelectUnit|unknown|void||
|SelectUnitAndPan|unknown|void||
|SelectUnitsOnBoard|unknown|void||
|Select_CFixedPoint|unknown unknown unknown|CFixedPoint||
|Select_CString|unknown unknown unknown|CString||
|Select_CVector2f|unknown unknown unknown|CVector2f||
|Select_CVector2i|unknown unknown unknown|CVector2i||
|Select_CVector3f|unknown unknown unknown|CVector3f||
|Select_CVector3i|unknown unknown unknown|CVector3i||
|Select_CVector4f|unknown unknown unknown|CVector4f||
|Select_CVector4i|unknown unknown unknown|CVector4i||
|Select_float|unknown unknown unknown|float||
|Select_int16|unknown unknown unknown|int16||
|Select_int32|unknown unknown unknown|int32||
|Select_int64|unknown unknown unknown|int64||
|Select_int8|unknown unknown unknown|int8||
|Select_uint16|unknown unknown unknown|uint16||
|Select_uint32|unknown unknown unknown|uint32||
|Select_uint64|unknown unknown unknown|uint64||
|Select_uint8|unknown unknown unknown|uint8||
|SetAlertPriorityFromTextContext|unknown|void||
|SetBlockListAndTrimFromTextContext|unknown|void||
|SetBlockListFromTextContext|unknown|void||
|SetBlockListWithTitleFromTextContext|unknown|void||
|SetCStringFromTextContext|unknown|void||
|SetCameraRestrictionsEnabled|unknown|void|Map Editor - Set camera restrictions toggle|
|SetConditionListForceFailFromTextContext|unknown|void||
|SetConditionListFromTextContext|unknown|void||
|SetConditionListOnlyFailCollapseRequirementFromTextContext|unknown|void||
|SetConditionListOnlyFailFromTextContext|unknown|void||
|SetConditionListOnlyPassedAndNeutralFromTextContext|unknown|void||
|SetConditionListOnlyPassedFromTextContext|unknown|void||
|SetConditionListWithTitleForceFailFromTextContext|unknown|void||
|SetConditionListWithTitleFromTextContext|unknown|void||
|SetConditionListWithTitleOnlyFailFromTextContext|unknown|void||
|SetConditionListWithTitleOnlyPassedAndNeutralFromTextContext|unknown|void||
|SetConditionListWithTitleOnlyPassedFromTextContext|unknown|void||
|SetDefaultMapMode||void||
|SetHighlightedTab|unknown|void||
|SetLobbyCountry|unknown|void||
|SetLobbyCountryTag|unknown|void||
|SetMapMode|unknown|void||
|SetRequirementsListFromTextContext|unknown|void||
|SetRequirementsListFromTextContextWithTitle|unknown|void||
|SetRowListFromTextContext|unknown|void||
|SetRowListWithTitleFromTextContext|unknown|void||
|SetSelectedInstitution|unknown|void||
|SetStringPairListAndTrimFromTextContext|unknown|void||
|SetStringPairListFromTextContext|unknown|void||
|SetStringPairListWithTitleAndFooterFromTextContext|unknown|void||
|SetStringPairListWithTitleFromTextContext|unknown|void||
|SetTableColumnListFromTextContext|unknown|void||
|SetTitleDescTooltipFromTextContext|unknown|void||
|SetUIFocusMarket|unknown|void||
|SetupExportWithNeedsLeft|unknown unknown unknown|void||
|SetupExportWithNeedsRight|unknown unknown unknown|void||
|SetupImportWithNeedsLeft|unknown unknown unknown|void||
|SetupImportWithNeedsRight|unknown unknown unknown|void||
|SetupSelectCommanderLeft|unknown|void||
|SetupSelectCommanderRight|unknown|void||
|ShouldFrontEndSceneBeVisible||bool||
|ShouldShowAnimationInfo||bool||
|ShouldShowRulingHistoryForInternationalOrganization|unknown|bool||
|ShouldShowSegmentedControlForSetting|unknown|bool|Settings - Should show segmented control or not?|
|ShowAdultAge||CString||
|ShowAdvanceName|unknown|CString||
|ShowAdvanceNameWithNoTooltip|unknown|CString||
|ShowAgeName|unknown|CString||
|ShowAgeNameWithNoTooltip|unknown|CString||
|ShowAreaName|unknown|CString||
|ShowAreaNameWithNoTooltip|unknown|CString||
|ShowArmyBuilderView||void||
|ShowArmyBuilderViewWithLocation|unknown|void||
|ShowArtistTypeName|unknown|CString||
|ShowArtistTypeNameWithNoTooltip|unknown|CString||
|ShowAutoModifierEffect|unknown|CString||
|ShowAutoModifierEffectForCountry|unknown unknown|CString||
|ShowAutoModifierEffectForLocation|unknown unknown|CString||
|ShowAvatarName|unknown|CString||
|ShowAvatarNameWithNoTooltip|unknown|CString||
|ShowBiasValue|unknown|CFixedPoint||
|ShowBiasValueScoped|unknown unknown unknown unknown|CFixedPoint||
|ShowBribeMercenary|unknown|bool||
|ShowBuilding|unknown|void||
|ShowBuildingCardForLocation|unknown unknown|bool||
|ShowBuildingTypeName|unknown|CString||
|ShowBuildingTypeNameWithNoTooltip|unknown|CString||
|ShowCabinetActionName|unknown|CString||
|ShowCabinetActionNameWithNoTooltip|unknown|CString||
|ShowCabinetTypeDatabase|unknown|CString||
|ShowCasusBelliName|unknown|CString||
|ShowCasusBelliNameWithNoTooltip|unknown|CString||
|ShowCharacter|unknown|void||
|ShowCharacterInDynasty|unknown|void||
|ShowCharacterInteractionName|unknown|CString||
|ShowCharacterInteractionNameWithNoTooltip|unknown|CString||
|ShowClimateName|unknown|CString||
|ShowClimateNameWithNoTooltip|unknown|CString||
|ShowCombat|unknown|void||
|ShowCondottieriViewWithFilter|unknown|void||
|ShowConsortSelection|unknown|void||
|ShowConstructionCancellationDialog|unknown unknown|void||
|ShowConstructionType|unknown|void||
|ShowContinentName|unknown|CString||
|ShowContinentNameWithNoTooltip|unknown|CString||
|ShowCountryInteractionName|unknown|CString||
|ShowCountryInteractionNameWithNoTooltip|unknown|CString||
|ShowCountryPeopleViewWithLocation|unknown unknown|void||
|ShowCountryPeopleViewWithPopFilter|unknown unknown|void||
|ShowCountryRankName|unknown|CString||
|ShowCountryRankNameWithNoTooltip|unknown|CString||
|ShowCulture|unknown|void||
|ShowCultureGroupName|unknown|CString||
|ShowCultureGroupNameWithNoTooltip|unknown|CString||
|ShowCultureName|unknown|CString||
|ShowCultureNameWithNoTooltip|unknown|CString||
|ShowDatabase|unknown|CString||
|ShowDatabaseWithIcon|unknown|CString||
|ShowDelistMercenary|unknown|bool||
|ShowDialectName|unknown|CString||
|ShowDialectNameWithNoTooltip|unknown|CString||
|ShowDiploMacrobuilderWithCountry|unknown|void||
|ShowDiploMacrobuilderWithCountryAndFilter|unknown unknown unknown|void||
|ShowDiploMacrobuilderWithFilter|unknown unknown|void||
|ShowDisaster|unknown|void||
|ShowDisasterName|unknown|CString||
|ShowDisasterNameWithNoTooltip|unknown|CString||
|ShowDiseaseName|unknown|CString||
|ShowDiseaseNameWithNoTooltip|unknown|CString||
|ShowDismissMercenary|unknown|bool||
|ShowDynasty|unknown|void||
|ShowDynastyName|unknown|CString||
|ShowDynastyNameWithNoTooltip|unknown|CString||
|ShowEstatePrivilegeName|unknown|CString||
|ShowEstatePrivilegeNameWithNoTooltip|unknown|CString||
|ShowEstateTypeName|unknown|CString||
|ShowExpandRawGoodLocationsViewWithGoods|unknown unknown|void||
|ShowExpandRawGoodLocationsViewWithMarketAndFilter|unknown unknown unknown|void||
|ShowExpandRawGoodLocationsViewWithMarketAndGoods|unknown unknown unknown|void||
|ShowExtendMercenary|unknown|bool||
|ShowFoodProductionViewWithMarket|unknown unknown|void||
|ShowFoodProductionViewWithProvince|unknown unknown|void||
|ShowForeignCountry|unknown|void||
|ShowFormableCountryName|unknown|CString||
|ShowFormableCountryNameWithNoTooltip|unknown|CString||
|ShowFortProductionInLocation|unknown|void||
|ShowGenericActionName|unknown|CString||
|ShowGenericActionNameWithNoTooltip|unknown|CString||
|ShowGodName|unknown|CString||
|ShowGodNameWithNoTooltip|unknown|CString||
|ShowGoods|unknown|void||
|ShowGoodsDemandName|unknown|CString||
|ShowGoodsDemandNameWithNoTooltip|unknown|CString||
|ShowGoodsName|unknown|CString||
|ShowGoodsNameWithNoTooltip|unknown|CString||
|ShowGoodsProductionViewWithMarketAndFilter|unknown unknown unknown|void||
|ShowGoodsReactive|unknown|void||
|ShowGovernmentReformName|unknown|CString||
|ShowGovernmentReformNameWithNoTooltip|unknown|CString||
|ShowGovernmentTypeName|unknown|CString||
|ShowGovernmentTypeNameWithNoTooltip|unknown|CString||
|ShowGreatPowersSortedBy|unknown|CString||
|ShowHegemonyName|unknown|CString||
|ShowHegemonyNameWithNoTooltip|unknown|CString||
|ShowHeirSelectionName|unknown|CString||
|ShowHeirSelectionNameWithNoTooltip|unknown|CString||
|ShowHireMercenary|unknown|bool||
|ShowHiringArmyMercenariesView||void||
|ShowHiringNavyMercenariesView||void||
|ShowHolySiteDefinitionName|unknown|CString||
|ShowHolySiteDefinitionNameWithNoTooltip|unknown|CString||
|ShowHolySiteTypeName|unknown|CString||
|ShowHolySiteTypeNameWithNoTooltip|unknown|CString||
|ShowInstitutionName|unknown|CString||
|ShowInstitutionNameWithNoTooltip|unknown|CString||
|ShowInternationalOrganizationTypeViewOpen|unknown|bool||
|ShowInternationalOrganizationViewOpen|unknown|bool||
|ShowJominiLegalDocuments||void||
|ShowLandOwnershipRuleName|unknown|CString||
|ShowLandOwnershipRuleNameWithNoTooltip|unknown|CString||
|ShowLanguageFamilyName|unknown|CString||
|ShowLanguageFamilyNameWithNoTooltip|unknown|CString||
|ShowLanguageName|unknown|CString||
|ShowLanguageNameWithNoTooltip|unknown|CString||
|ShowLawName|unknown|CString||
|ShowLawNameWithNoTooltip|unknown|CString||
|ShowLocation|unknown|void||
|ShowLocationName|unknown|CString||
|ShowLocationNameWithNoTooltip|unknown|CString||
|ShowLocationRankName|unknown|CString||
|ShowLocationRankNameWithNoTooltip|unknown|CString||
|ShowManageSubjectType|unknown|void||
|ShowManageSubjects||void||
|ShowManageSubjectsWithFilter|unknown|void||
|ShowMarket|unknown|void||
|ShowMaxAdolescentAge||CString||
|ShowMaxChildAge||CString||
|ShowMaxInfantAge||CString||
|ShowMessageSettings|unknown|void||
|ShowMinAdolescentAge||CString||
|ShowMinChildAge||CString||
|ShowMission|unknown|void||
|ShowMissionName|unknown|CString||
|ShowMissionNameWithNoTooltip|unknown|CString||
|ShowMissionTaskName|unknown|CString||
|ShowMissionTaskNameWithNoTooltip|unknown|CString||
|ShowModifier|unknown|CString||
|ShowModifierEffect|unknown|CString||
|ShowModifierTypeName|unknown|CString||
|ShowModifierTypeNameWithBreakdown|unknown unknown|CString||
|ShowModifierTypeNameWithNoTooltip|unknown|CString||
|ShowModifierWithNoTooltip|unknown|CString||
|ShowMoveCapital|unknown|bool||
|ShowNamedValue|unknown|CFixedPoint||
|ShowNavyBuilderView||void||
|ShowNavyBuilderViewWithLocation|unknown|void||
|ShowParliamentAgendaTypeName|unknown|CString||
|ShowParliamentAgendaTypeNameWithNoTooltip|unknown|CString||
|ShowParliamentIssueTypeName|unknown|CString||
|ShowParliamentIssueTypeNameWithNoTooltip|unknown|CString||
|ShowParliamentTypeName|unknown|CString||
|ShowParliamentTypeNameWithNoTooltip|unknown|CString||
|ShowParliamentTypes||CString||
|ShowPaymentName|unknown|CString||
|ShowPaymentNameWithNoTooltip|unknown|CString||
|ShowPeaceTreatyTypeName|unknown|CString||
|ShowPeaceTreatyTypeNameWithNoTooltip|unknown|CString||
|ShowPolicyName|unknown|CString||
|ShowPolicyNameWithNoTooltip|unknown|CString||
|ShowPopTypeName|unknown|CString||
|ShowPopTypeNameWithNoTooltip|unknown|CString||
|ShowPopsForLocation|unknown|void||
|ShowPopsForProvince|unknown|void||
|ShowProductionMethodName|unknown|CString||
|ShowProductionMethodNameWithNoTooltip|unknown|CString||
|ShowProductionViewWithFilter|unknown unknown|void||
|ShowProductionViewWithLocation|unknown unknown|void||
|ShowProductionViewWithMarketAndFilter|unknown unknown unknown|void||
|ShowProvinceDefinition|unknown|void||
|ShowProvinceDefinitionName|unknown|CString||
|ShowProvinceDefinitionNameWithNoTooltip|unknown|CString||
|ShowRaiseLevies|unknown|bool||
|ShowRebel|unknown|void||
|ShowRegionName|unknown|CString||
|ShowRegionNameWithNoTooltip|unknown|CString||
|ShowRelationTypeName|unknown|CString||
|ShowReligionAdjective|unknown|CString||
|ShowReligionAdjectiveWithNoTooltip|unknown|CString||
|ShowReligionGroupAdjective|unknown|CString||
|ShowReligionGroupAdjectiveWithNoTooltip|unknown|CString||
|ShowReligionGroupName|unknown|CString||
|ShowReligionGroupNameWithNoTooltip|unknown|CString||
|ShowReligionName|unknown|CString||
|ShowReligionNameWithNoTooltip|unknown|CString||
|ShowReligiousAspectName|unknown|CString||
|ShowReligiousAspectNameWithNoTooltip|unknown|CString||
|ShowReligiousFigureName|unknown|CString||
|ShowReligiousFigureNameWithNoTooltip|unknown|CString||
|ShowReligiousFocusName|unknown|CString||
|ShowReligiousFocusNameWithNoTooltip|unknown|CString||
|ShowReligiousSchoolName|unknown|CString||
|ShowReligiousSchoolNameWithNoTooltip|unknown|CString||
|ShowResolutionName|unknown|CString||
|ShowResolutionNameWithNoTooltip|unknown|CString||
|ShowRoadTypeName|unknown|CString||
|ShowRoadTypeNameWithNoTooltip|unknown|CString||
|ShowRoadbuilder|unknown|void||
|ShowRulingHistoryForCountry|unknown|void||
|ShowRulingHistoryForInternationalOrganization|unknown|void||
|ShowScriptedEffect|unknown unknown|CString||
|ShowScriptedEffectForScope|unknown unknown|CString||
|ShowSeaZone|unknown|void||
|ShowSelectCabinetCharacter|unknown unknown|void||
|ShowSelectCabinetForContextMenu||void||
|ShowSelectCabinetToDevelopProvince|unknown|void||
|ShowSelectCabinetToEncourageMigration|unknown|void||
|ShowSelectCabinetToExpelPeople|unknown|void||
|ShowSelectCabinetToIncreaseControl|unknown|void||
|ShowSelectCabinetToRecoverEffort|unknown|void||
|ShowSelectInternationalOrganizationPolicies|unknown|void||
|ShowSelectPolicies|unknown|void||
|ShowSelectRivals||void||
|ShowSelectSuccessionLaw||void||
|ShowShortAgeName|unknown|CString||
|ShowShortAgeNameWithNoTooltip|unknown|CString||
|ShowSimpleCustomTooltip|unknown unknown unknown unknown unknown unknown unknown|CString|Creates a simple custom TagTooltip for the string in the first argument. Other arguments are the loc-key for the title, the icon filename within gfx/interface/icons/, and the loc-keys for concept, body, flavor and list.|
|ShowSimpleCustomTooltipLocalized|unknown unknown unknown unknown unknown unknown unknown|CString|Like ShowSimpleCustomTooltip, except the string in the first argument gets localized.|
|ShowSituation|unknown|void||
|ShowSituationName|unknown|CString||
|ShowSituationNameWithNoTooltip|unknown|CString||
|ShowSocietyDirectionName|unknown|CString||
|ShowSocietyDirectionNameWithNoTooltip|unknown|CString||
|ShowSpecialStatusName|unknown|CString||
|ShowSpecialStatusNamePlural|unknown|CString||
|ShowSpecialStatusNamePluralWithNoTooltip|unknown|CString||
|ShowSpecialStatusNameWithNoTooltip|unknown|CString||
|ShowSubContinentName|unknown|CString||
|ShowSubContinentNameWithNoTooltip|unknown|CString||
|ShowSubjectTypeName|unknown|CString||
|ShowSubjectTypeNameWithNoTooltip|unknown|CString||
|ShowTopographyName|unknown|CString||
|ShowTopographyNameWithNoTooltip|unknown|CString||
|ShowTradeDetails|unknown|void||
|ShowTraitName|unknown|CString||
|ShowTraitNameWithNoTooltip|unknown|CString||
|ShowTransferOccupation|unknown|void||
|ShowTransferProvinceOccupation|unknown|void||
|ShowTriggerConditions|unknown unknown|CString||
|ShowTriggerConditionsForScope|unknown unknown|CString||
|ShowUnitAbilityName|unknown|CString||
|ShowUnitAbilityNameWithNoTooltip|unknown|CString||
|ShowUnitCategoryName|unknown|CString||
|ShowUnitCategoryNameWithNoTooltip|unknown|CString||
|ShowUnitCombat|unknown unknown|void||
|ShowUnitDefinitionName|unknown|CString||
|ShowUnitDefinitionNameWithNoTooltip|unknown|CString||
|ShowUnitMilitaryObjectiveGroups|unknown|void||
|ShowUnitType|unknown|void||
|ShowVegetationName|unknown|CString||
|ShowVegetationNameWithNoTooltip|unknown|CString||
|ShowWar|unknown unknown|void||
|ShowWarPeaceOffer|unknown|void||
|ShowWorkOfArtName|unknown|CString||
|ShowWorkOfArtNameWithNoTooltip|unknown|CString||
|ShowWorkOfArtTypeName|unknown|CString||
|ShowWorkOfArtTypeNameWithNoTooltip|unknown|CString||
|SkipAgenda||bool||
|StartBasicTutorial||void||
|StartLobbyGame||void||
|StartsWith|unknown unknown|bool||
|StatusCanLogin||bool||
|StatusGetLoginStatus||CUTF8String||
|StatusGetUserEmailMasked||CUTF8String||
|StatusGetUserName||CUTF8String||
|StatusIsAccountConnected||bool||
|StatusIsLoggedIn||bool||
|StatusIsLoggingIn||bool||
|StatusIsOffline||bool||
|StatusIsSupportConnectedAccount||bool||
|StatusIsUserNameEmpty||bool||
|StopObservingCountry||void||
|StopTutorial||void||
|StringContains|unknown unknown|bool||
|StringIsEmpty|unknown|bool||
|StringIsWhitespace|unknown|bool||
|SubmitPassword||void||
|SubsidizeBuilding|unknown|void||
|Subtract_CFixedPoint|unknown unknown|CFixedPoint||
|Subtract_CVector2f|unknown unknown|CVector2f||
|Subtract_float|unknown unknown|float||
|Subtract_int32|unknown unknown|int32||
|Subtract_int64|unknown unknown|int64||
|Subtract_uint32|unknown unknown|uint32||
|Subtract_uint64|unknown unknown|uint64||
|TakeOverSiege|unknown|void||
|TextureListFormatSize|unknown|CString||
|TextureListFormatkB|unknown|CString||
|ToString_int16|unknown|CString||
|ToString_int32|unknown|CString||
|ToString_int64|unknown|CString||
|ToString_int8|unknown|CString||
|ToString_uint16|unknown|CString||
|ToString_uint32|unknown|CString||
|ToString_uint64|unknown|CString||
|ToString_uint8|unknown|CString||
|ToggleAllowExtendMercenary|unknown|void||
|ToggleAutoExtendMercenaries||void||
|ToggleAutoMaintenance|unknown|void||
|ToggleAutoRaiseArmyLeviesAtWar||void||
|ToggleAutoRaiseNavyLeviesAtWar||void||
|ToggleBuilding|unknown|void||
|ToggleBuildings|unknown|void||
|ToggleCharacterFav|unknown|void||
|ToggleCountryFav|unknown|void||
|ToggleEncyclopedia||void||
|ToggleFav|unknown unknown|void||
|ToggleGameView|unknown|void||
|ToggleGoodsFav|unknown|void||
|ToggleIOFav|unknown|void||
|ToggleJominiCreateAccount||void||
|ToggleJominiLoginAccount||void||
|ToggleLateralGroup|unknown|void||
|ToggleLateralView|unknown|void||
|ToggleLocationFav|unknown|void||
|ToggleLogViewer||void||
|ToggleMarketAutomation|unknown|void||
|ToggleMarketFav|unknown|void||
|ToggleMessageLog||void||
|ToggleMultiplayerChat||void||
|ToggleOpenModTools||void||
|TogglePlayerAI|unknown|void||
|ToggleSeazoneFav|unknown|void||
|ToggleSelectUnit|unknown|void||
|ToggleSkipAgenda||void||
|ToggleSkipPlaythrough||void||
|ToggleSkipWelcomeNewGame||void||
|ToggleSubsidizeBuildings|unknown|void||
|ToggleTradeLock|unknown|void||
|TransparentIfFalse|unknown|float||
|TransparentIfTrue|unknown|float||
|TransparentIfZero|unknown|float||
|TransparentIfZero_int32|unknown|float||
|TutorialGetVar|unknown|CString||
|TutorialHasVar|unknown|bool||
|TutorialHasVarValue|unknown unknown|bool||
|TutorialIsRunning||bool||
|TutorialIsStepKey|unknown|bool||
|TutorialVarNotExistOrHasValue|unknown unknown|bool||
|Unfocus|unknown|void|Unfocus widget|
|UnselectLobbyCountry||void||
|UpdateVisibilityIfThereIsAnyText|unknown|void||
|UpgradeLocationRank|unknown|void||
|UpgradeSubUnit|unknown|void||
|UseDynamicParliamentName||bool||
|UsesTimerLocking||bool||
|V2SizeHeight|unknown unknown unknown|CVector2f||
|V2SizeWidth|unknown unknown unknown|CVector2f||
|Vector3fToColor|unknown|CVector4f||
|Vector3iToColor|unknown|CVector4f||
|Vector4iToColor|unknown|CVector4f||
|VersionInfoOnClick||void||

### List of all data type functions

The list is on a separate page as it is too large to directly be included on this page. It includes all GUI functions in every scope including those above.

## GUI promotes

||Please help improve this article or section by expanding it with: more tables.|

GUI promotes typically move the "scope" from one type to another.

|Promote|Arguments|Output|Description|
|---|---|---|---|
|ACTIVE_RESOLUTION||ActiveResolution||
|ACTIVE_SITUATION||ActiveSituation||
|ADVANCE||Advance||
|ADVANCE_DEFINITION||AdvanceDefinition||
|AGE||Age||
|AREA||Area||
|ARTIST||Artist||
|ATTACKER||Country||
|AVATAR||Avatar||
|AccessActiveDLC|unknown|DlcEntry||
|AccessActiveMod|unknown|ModsPlaysetEntry||
|AccessGameRules||JominiGameRules||
|AccessLobbyCountryList||CountryListOverview||
|AccessLogViewer||LogViewer|Access Central Log Viewer|
|AccessMessageLog||MessageLog||
|AccessModsGui||ModsGui|Access Mods GUI|
|AccessOutliner||Outliner||
|AccessPauseMenu||PauseMenu||
|AccessTutorial||Tutorial||
|Application||Application||
|AuxVars||Context||
|BATTLE_RESULT||BattleResult||
|BATTLE_SIDE||BattleSide||
|BUILDING||Building||
|BUILDING_CATEGORY||BuildingCategory||
|BUILDING_TYPE||BuildingType||
|BuildModeGetBuildingType||BuildingType||
|BuildModeGetConstructScoreRanking||ConstructScoreRanking||
|CABINET||Cabinet||
|CABINET_ACTION||CabinetAction||
|CARDINAL||Cardinal||
|CASUS_BELLI||CasusBelli||
|CHARACTER||Character||
|CHARACTER_INTERACTION||CharacterInteraction||
|CHILD_EDUCATION||ChildEducation||
|CLIMATE||Climate||
|COLONIAL_CHARTER||ColonialCharter||
|COMBAT||Combat||
|COMBAT_SIDE||CombatSide||
|CONSTRUCTION||Construction||
|CONTINENT||Continent||
|COUNTRY||Country||
|COUNTRY_INTERACTION||CountryInteraction||
|COUNTRY_RANK||CountryRank||
|CULTURE||Culture||
|CULTURE_GROUP||CultureGroup||
|DATE||Date|Jomini Date|
|DATE_MAX||Date|Jomini Date - Max|
|DATE_MIN||Date|Jomini Date - Min|
|DEFENDER||Country||
|DIALECT||Dialect||
|DISASTER||Disaster||
|DISASTER_TYPE||DisasterType||
|DISEASE||Disease||
|DISEASE_OUTBREAK||DiseaseOutbreak||
|DYNASTY||Dynasty||
|EMPLOYMENT_SYSTEM||EmploymentSystem||
|ESTATE||Estate||
|ESTATE_PRIVILEGE||EstatePrivilege||
|ESTATE_TYPE||EstateType||
|ETHNICITY||Ethnicity||
|EXPLORATION||Exploration||
|EmptyScope||TopScope||
|ExpandModeGetConstructScoreRanking||ConstructScoreRanking||
|FORMABLE_COUNTRY||FormableCountry||
|GC|unknown|GameConceptTooltip||
|GENERIC_ACTION||GenericAction||
|GOD||God||
|GOODS||Goods||
|GOODS_DEMAND||GoodsDemand||
|GOODS_DEMAND_ENTRY||GoodsDemandEntry||
|GOVERNMENT_REFORM||GovernmentReform||
|GOVERNMENT_TYPE||GovernmentType||
|GetActiveMapMode||MapMode||
|GetAutoModifier|unknown|StaticAutoModifier||
|GetAutomatedSystemItem|unknown|AutomatedSystemsItem||
|GetAutomatedSystemItem2|unknown unknown|AutomatedMultiSystemItem||
|GetAutomatedSystemItem3|unknown unknown unknown|AutomatedMultiSystemItem||
|GetAutomatedSystemItem4|unknown unknown unknown unknown|AutomatedMultiSystemItem||
|GetAutomatedSystemItem5|unknown unknown unknown unknown unknown|AutomatedMultiSystemItem||
|GetAutomatedSystemItem6|unknown unknown unknown unknown unknown unknown|AutomatedMultiSystemItem||
|GetCharacter|unknown|Character||
|GetCharacterAction|unknown|CharacterInteraction||
|GetCharacterQuickActions|unknown|QuickCharacterActions||
|GetCountry|unknown|Country||
|GetCountryCoatOfArms|unknown|CoatOfArmsWrapper||
|GetCountryFlagCoatOfArms|unknown|CoatOfArmsWrapper||
|GetCountryNeeds|unknown|CountryNeeds||
|GetCultureByKey|unknown|Culture||
|GetCultureGroupByKey|unknown|CultureGroup||
|GetCurrentAge||Age||
|GetDefaultMapMode||MapMode||
|GetDisasterTypeByKey|unknown|DisasterType||
|GetDisease|unknown|Disease||
|GetDynasty|unknown|Dynasty||
|GetDynastyCoatOfArms|unknown|CoatOfArmsWrapper||
|GetDynastyFlagCoatOfArms|unknown|CoatOfArmsWrapper||
|GetEconomyView||EconomyView||
|GetFirstUnitSelected||Unit||
|GetFormableCountry|unknown|FormableCountry||
|GetFormableCountryCoatOfArms|unknown|CoatOfArmsWrapper||
|GetGameRules||JominiGameRules||
|GetGenericAction|unknown|GenericAction||
|GetGlobalVariable|unknown|Scope||
|GetHint|unknown|ScriptableHintDefinition||
|GetHistoricalScoreCoatOfArms|unknown|CoatOfArmsWrapper||
|GetInstitutionByKey|unknown|Institution||
|GetInternationalOrganization|unknown|InternationalOrganization||
|GetInternationalOrganizationPayment|unknown|Payment||
|GetInternationalOrganizationType|unknown|InternationalOrganizationType||
|GetLanguageFlagCoatOfArms|unknown|CoatOfArmsWrapper||
|GetLastSelectInteractionTargetGlue||SelectInteractionTargetGlue||
|GetLaw|unknown|Law||
|GetMapColorLedgerByName|unknown|MapColorLedger||
|GetMapColorLedgerSearchBar||SearchBar||
|GetMapMode|unknown|MapMode||
|GetMapModeSearchBar||SearchBar||
|GetMarketCountryNeeds|unknown unknown|MarketCountryNeeds||
|GetMessageLog||MessageLog||
|GetModifier|unknown|StaticModifier||
|GetMultiplayerChat||MultiplayerChat||
|GetPlayStyleItem|unknown|PlayStyleItem||
|GetPlayer||Country||
|GetPlayerInternationalOrganization|unknown|InternationalOrganization||
|GetPlayerTargettedActionParamsPtr||TargettedActionParameters||
|GetPopTypeByName|unknown|PopType||
|GetProficiency|unknown|PlayerProficiency||
|GetProvince|unknown|Location||
|GetQuickCabinetCardModifier|unknown unknown|QuickCabinetCardModifier||
|GetQuickMarketTrades|unknown unknown|QuickMarketTrades||
|GetQuickMissionList||QuickMissionList||
|GetQuickTemporaryCountryRelations|unknown|QuickTemporaryCountryRelations||
|GetQuickVisibleCountries|unknown|QuickVisibleCountries||
|GetQuickVisibleMarkets|unknown|QuickVisibleMarkets||
|GetReligionByKey|unknown|Religion||
|GetRequirementLineAux|unknown unknown unknown|RequirementLineAux||
|GetResolution|unknown|Resolution||
|GetScenario|unknown|Scenario||
|GetScriptedGui|unknown|ScriptedGui|Jomini Scripted GUI - Get scripted GUI by name|
|GetScriptedRelationType|unknown|ScriptedRelationType||
|GetSelectedCountryOrByLocation||Country||
|GetServerInfo||ServerInformation|Multiplayer - Server Info of current session|
|GetSituationByKey|unknown|Situation||
|GetSubUnitCategory|unknown|SubUnitCategory||
|GetTutorial||Tutorial||
|GetUniqueInternationalOrganization|unknown|InternationalOrganization||
|GetVariableSystem||VariableSystem|Access the global variable system|
|GetWar|unknown unknown|War||
|GetWillJoinCountryList|unknown unknown|WillJoinCountryList||
|GuiScope||TopScope|Jomini Scripted GUI - Get GUI top jomini scope|
|HEGEMONY||Hegemony||
|HEIR_SELECTION||HeirSelection||
|HOLY_SITE||HolySite||
|HOLY_SITE_DEFINITION||HolySiteDefinition||
|HOLY_SITE_TYPE||HolySiteType||
|INSTITUTION||Institution||
|INTERNATIONAL_ORGANIZATION||InternationalOrganization||
|INTERNATIONAL_ORGANIZATION_TYPE||InternationalOrganizationType||
|JominiPlayer||Playable|Jomini Script Systen - Get generic current playable object|
|LAND_OWNERSHIP_RULE||LandOwnershipRule||
|LANGUAGE||Language||
|LANGUAGE_FAMILY||LanguageFamily||
|LAW||Law||
|LEVY_SETUP||LevySetup||
|LOAN||Loan||
|LOCATION||Location||
|LOCATION_RANK||LocationRank||
|LeftView||LateralView||
|MARKET||Market||
|MERCENARY||Mercenary||
|MERCHANT||Merchant||
|MIGRATION||Migration||
|MISSION||MissionDefinition||
|MISSION_TASK||MissionTaskDefinition||
|MapModeSelectorVars||UIVariables||
|PARLIAMENT_AGENDA||ParliamentAgenda||
|PARLIAMENT_ISSUE||ParliamentIssue||
|PARLIAMENT_TYPE||ParliamentType||
|PAYMENT||Payment||
|PEACE_TREATY||ScriptedPeaceTreatyType||
|POLICY||Policy||
|POP||Pop||
|POP_TYPE||PopType||
|PREV||Scope|Script Scope|
|PRICE||Price||
|PRIVATEER||Privateer||
|PRODUCTION_METHOD||ProductionMethod||
|PROVINCE||Province||
|PROVINCE_DEFINITION||ProvinceDefinition||
|PdxAccount||PdxAccount||
|Pin|unknown|PinCollection||
|PinManager||PinningManager||
|Player||Country||
|PlayerScope||TopScope||
|REBEL||Rebel||
|RECRUITMENT_METHOD||RecruitmentMethod||
|REGENCY||RegencyType||
|REGENCY_TYPE||RegencyType||
|REGION||Region||
|RELATION_TYPE||ScriptedRelationType||
|RELIGION||Religion||
|RELIGION_GROUP||ReligionGroup||
|RELIGIOUS_ASPECT||ReligiousAspect||
|RELIGIOUS_FACTION||ReligiousFaction||
|RELIGIOUS_FIGURE||ReligiousFigure||
|RELIGIOUS_FOCUS||ReligiousFocus||
|RELIGIOUS_SCHOOL||ReligiousSchool||
|RESOLUTION||Resolution||
|ROAD_TYPE||RoadType||
|ROOT||Scope|Script Scope|
|RecruitModeGetRecruitItem|unknown|LocationToRecruitItem||
|RecruitModeGetRecruitScoreRanking||RecruitScoreRanking||
|RecruitModeGetView||RecruitInLocationLateralView||
|RevolutionaryTarget||Country||
|RightView||LateralView||
|SCOPE||TopScope|Script Scope|
|SCRIPTABLE_HINT_DEFINITION||ScriptableHintDefinition||
|SIEGE||Siege||
|SITUATION||Situation||
|SOCIETAL_VALUE||SocietalValue||
|SPECIAL_STATUS||SpecialStatus||
|SUBJECT_MILITARY_STANCE||SubjectMilitaryStance||
|SUBJECT_TYPE||SubjectType||
|SUBUNIT||SubUnit||
|SUBUNITCATEGORY||SubUnitCategory||
|SUBUNITDEFINITION||SubUnitType||
|SUB_CONTINENT||SubContinent||
|SUPPLY_DEPOT||SupplyDepot||
|SelectCountryDiplomacy_GetDiplomaticActionItem|unknown|DiplomaticActionItem||
|StringToBlockList|unknown|BlockList||
|StringToBlockListAndTrim|unknown|BlockList||
|StringToBlockListWithTitle|unknown|BlockList||
|StringToConditionList|unknown|ConditionList||
|StringToConditionListForceFail|unknown|ConditionList||
|StringToConditionListOnlyFail|unknown|ConditionList||
|StringToConditionListOnlyFailAndNeutral|unknown|ConditionList||
|StringToConditionListOnlyFailCollapseRequirement|unknown|ConditionList||
|StringToConditionListOnlyPassed|unknown|ConditionList||
|StringToConditionListOnlyPassedAndNeutral|unknown|ConditionList||
|StringToConditionListOnlyPassedAndNeutralIfNot|unknown unknown|ConditionList||
|StringToConditionListWithTitle|unknown|ConditionList||
|StringToConditionListWithTitleForceFail|unknown|ConditionList||
|StringToConditionListWithTitleOnlyFail|unknown|ConditionList||
|StringToConditionListWithTitleOnlyFailAndNeutral|unknown|ConditionList||
|StringToConditionListWithTitleOnlyPassed|unknown|ConditionList||
|StringToConditionListWithTitleOnlyPassedAndNeutral|unknown|ConditionList||
|StringToRequirementsList|unknown|RequirementsList||
|StringToRequirementsListWithTitle|unknown|RequirementsList||
|StringToRowList|unknown|RowList||
|StringToStringPairList|unknown|StringPairList||
|StringToStringPairListWithTitle|unknown|StringPairList||
|StringToStringPairListWithTitleAndFooter|unknown|StringPairList||
|StringToTableColumnList|unknown|TableColumnList||
|StringToTitleDescTooltip|unknown|TitleDescTooltip||
|TARGET_ACTIVE_RESOLUTION||ActiveResolution||
|TARGET_ADVANCE_DEFINITION||AdvanceDefinition||
|TARGET_AGE||Age||
|TARGET_AREA||Area||
|TARGET_ARTIST||Artist||
|TARGET_AVATAR||Avatar||
|TARGET_BUILDING||Building||
|TARGET_BUILDING_TYPE||BuildingType||
|TARGET_CABINET||Cabinet||
|TARGET_CABINET_ACTION||CabinetAction||
|TARGET_CARDINAL||Cardinal||
|TARGET_CASUS_BELLI||CasusBelli||
|TARGET_CHARACTER||Character||
|TARGET_CHARACTER_INTERACTION||CharacterInteraction||
|TARGET_CHILD_EDUCATION||ChildEducation||
|TARGET_CLIMATE||Climate||
|TARGET_COLONIAL_CHARTER||ColonialCharter||
|TARGET_COMBAT||Combat||
|TARGET_COMBAT_SIDE||CombatSide||
|TARGET_CONTINENT||Continent||
|TARGET_COUNTRY||Country||
|TARGET_COUNTRY_INTERACTION||CountryInteraction||
|TARGET_COUNTRY_RANK||CountryRank||
|TARGET_CULTURE||Culture||
|TARGET_CULTURE_GROUP||CultureGroup||
|TARGET_DIALECT||Dialect||
|TARGET_DISASTER||Disaster||
|TARGET_DISASTER_TYPE||DisasterType||
|TARGET_DISEASE||Disease||
|TARGET_DISEASE_OUTBREAK||DiseaseOutbreak||
|TARGET_DYNASTY||Dynasty||
|TARGET_EMPLOYMENT_SYSTEM||EmploymentSystem||
|TARGET_ESTATE||Estate||
|TARGET_ESTATE_PRIVILEGE||EstatePrivilege||
|TARGET_ESTATE_TYPE||EstateType||
|TARGET_ETHNICITY||Ethnicity||
|TARGET_EXPLORATION||Exploration||
|TARGET_FORMABLE_COUNTRY||FormableCountry||
|TARGET_GENERIC_ACTION||GenericAction||
|TARGET_GOD||God||
|TARGET_GOODS||Goods||
|TARGET_GOODS_DEMAND||GoodsDemand||
|TARGET_GOODS_DEMAND_ENTRY||GoodsDemandEntry||
|TARGET_GOVERNMENT_REFORM||GovernmentReform||
|TARGET_GOVERNMENT_TYPE||GovernmentType||
|TARGET_HEGEMONY||Hegemony||
|TARGET_HEIR_SELECTION||HeirSelection||
|TARGET_HOLY_SITE||HolySite||
|TARGET_HOLY_SITE_DEFINITION||HolySiteDefinition||
|TARGET_HOLY_SITE_TYPE||HolySiteType||
|TARGET_INSTITUTION||Institution||
|TARGET_INTERNATIONAL_ORGANIZATION||InternationalOrganization||
|TARGET_INTERNATIONAL_ORGANIZATION_TYPE||InternationalOrganizationType||
|TARGET_LAND_OWNERSHIP_RULE||LandOwnershipRule||
|TARGET_LANGUAGE||Language||
|TARGET_LANGUAGE_FAMILY||LanguageFamily||
|TARGET_LAW||Law||
|TARGET_LEVY_SETUP||LevySetup||
|TARGET_LOAN||Loan||
|TARGET_LOCATION||Location||
|TARGET_LOCATION_RANK||LocationRank||
|TARGET_MARKET||Market||
|TARGET_MERCENARY||Mercenary||
|TARGET_MIGRATION||Migration||
|TARGET_MISSION||MissionDefinition||
|TARGET_MISSION_TASK||MissionTaskDefinition||
|TARGET_PARLIAMENT_AGENDA||ParliamentAgenda||
|TARGET_PARLIAMENT_ISSUE||ParliamentIssue||
|TARGET_PARLIAMENT_TYPE||ParliamentType||
|TARGET_PAYMENT||Payment||
|TARGET_PEACE_TREATY||ScriptedPeaceTreatyType||
|TARGET_POLICY||Policy||
|TARGET_POP||Pop||
|TARGET_POP_TYPE||PopType||
|TARGET_PRICE||Price||
|TARGET_PRIVATEER||Privateer||
|TARGET_PRODUCTION_METHOD||ProductionMethod||
|TARGET_PROVINCE||Province||
|TARGET_PROVINCE_DEFINITION||ProvinceDefinition||
|TARGET_REBEL||Rebel||
|TARGET_RECRUITMENT_METHOD||RecruitmentMethod||
|TARGET_REGENCY_TYPE||RegencyType||
|TARGET_REGION||Region||
|TARGET_RELATION_TYPE||ScriptedRelationType||
|TARGET_RELIGION||Religion||
|TARGET_RELIGION_GROUP||ReligionGroup||
|TARGET_RELIGIOUS_ASPECT||ReligiousAspect||
|TARGET_RELIGIOUS_FACTION||ReligiousFaction||
|TARGET_RELIGIOUS_FIGURE||ReligiousFigure||
|TARGET_RELIGIOUS_FOCUS||ReligiousFocus||
|TARGET_RELIGIOUS_SCHOOL||ReligiousSchool||
|TARGET_RESOLUTION||Resolution||
|TARGET_ROAD_TYPE||RoadType||
|TARGET_SCRIPTABLE_HINT_DEFINITION||ScriptableHintDefinition||
|TARGET_SIEGE||Siege||
|TARGET_SITUATION||Situation||
|TARGET_SOCIETAL_VALUE||SocietalValue||
|TARGET_SPECIAL_STATUS||SpecialStatus||
|TARGET_SUBJECT_MILITARY_STANCE||SubjectMilitaryStance||
|TARGET_SUBJECT_TYPE||SubjectType||
|TARGET_SUBUNIT||SubUnit||
|TARGET_SUBUNITCATEGORY||SubUnitCategory||
|TARGET_SUBUNITDEFINITION||SubUnitType||
|TARGET_SUB_CONTINENT||SubContinent||
|TARGET_TOPOGRAPHY||Topography||
|TARGET_TRADE||Trade||
|TARGET_TRAIT||Trait||
|TARGET_UNIT||Unit||
|TARGET_UNIT_ABILITY||UnitAbility||
|TARGET_UNIT_TYPE||SubUnitType||
|TARGET_VEGETATION||Vegetation||
|TARGET_WAR||War||
|TARGET_WEATHER_SYSTEM||WeatherSystem||
|TARGET_WORK_OF_ART||WorkOfArt||
|TARGET_WORK_OF_ART_TYPE||WorkOfArtType||
|TEMPORARY_DEMAND||TemporaryDemand||
|THIS||Scope|Script Scope|
|TOPOGRAPHY||Topography||
|TRADE||Trade||
|TRAIT||Trait||
|UNIT||Unit||
|UNIT_ABILITY||UnitAbility||
|UNIT_TYPE||SubUnitType||
|VEGETATION||Vegetation||
|WAR||War||
|WEATHER_SYSTEM||WeatherSystem||
|WORK_OF_ART||WorkOfArt||
|WORK_OF_ART_TYPE||WorkOfArtType||

### List of all GUI promotes

|Type|Promote|Arguments|Output|Description|
|---|---|---|---|---|
|ActiveClip|OnEnterEventsKeyframe||ActiveClipEventsKeyframe||
|ActiveClip|OnExitEventsKeyframe||ActiveClipEventsKeyframe||
|ActiveHegemon|GetCurrent||Country||
|ActiveHegemon|GetHegemony||Hegemony||
|ActiveHegemonItem|GetHegemon||ActiveHegemon||
|ActiveInstitution|GetBirthPlace||Location||
|ActiveInstitution|GetInstitution||Institution||
|ActiveParliamentAgenda|GetAgenda||ParliamentAgenda||
|ActiveParliamentAgenda|GetSpecialStatus||SpecialStatus||
|ActiveParliamentAgendaWrap|GetEstateType||EstateType||
|ActiveParliamentAgendaWrap|GetSpecialStatus||SpecialStatus||
|ActiveProductionMethod|GetMethod||ProductionMethod||
|ActiveResolution|GetParams||TargettedActionParameters||
|ActiveResolution|GetProposer||Country||
|ActiveResolution|GetResolution||Resolution||
|ActiveResolution|GetTarget|unknown|InteractionTarget||
|ActiveResolution|MakeScope||Scope||
|ActiveResolutionContainer|GetActiveResolution|unknown|ActiveResolution||
|ActiveResolutionContainer|GetActiveResolutionFromKey|unknown|ActiveResolution||
|ActiveSituation|GetActiveResolution|unknown|ActiveResolution||
|ActiveSituation|GetActiveResolutionFromKey|unknown|ActiveResolution||
|ActiveSituation|GetSituation||Situation||
|Advance|GetAge||Age||
|Advance|GetDefinition||AdvanceDefinition||
|AdvanceDefinition|GetAge||Age||
|AdvanceDefinition|GetModifier||DatabaseModifier||
|AdvanceDefinition|MakeScope||Scope||
|AdvanceItem|GetAdvance||Advance||
|AdvanceNode|GetItem||AdvanceItem||
|AdvancesLateralView|GetAdvancesSortSearch||FilteredSortedList||
|AdvancesLateralView|GetPlayer||Country||
|AdvancesLateralView|Manager||LateralView||
|AdvancesLateralView|Vars||Context||
|Age|MakeScope||Scope||
|AgeAdvancesWrap|GetAge||Age||
|AgendaView|AccessUIVars||UIVariables||
|AiCurrencyClassGlue|GetCurrentAiCurrency||AiCurrencyGlue||
|AiCurrencyViewer|GetCurrentAiCurrencyClass||AiCurrencyClassGlue||
|AiTransportTarget|GetTargetLocation||Location||
|AlertCanJoinTargettedIO|GetTargettedIO||InternationalOrganization||
|AlertFormableCountry|GetFormableCountry||FormableCountry||
|AlertManager|GetPlayer||Country||
|AlertMemberLeavingUnion|GetUnion||InternationalOrganization||
|AnimationClipsEditor|AccessUndoer||UndoStack||
|AnimationEditor|AccessAnimationStateSearch||NodeEditorSearch||
|AnimationEditor|AccessUndoer||UndoStack||
|AnimationEditor|AccessVariablesPanel||AnimationEditorVariablesPanel||
|AnimationEditorConnectionTab|AccessLhsSearchList|unknown unknown|ToolPropertySearchList||
|AnimationEditorConnectionTab|AccessOperatorSearchList|unknown unknown|ToolPropertySearchList||
|AnimationEditorStateTab|ClipReferenceComplexGuis|unknown|AnimationComplexClipReferenceGui||
|AnimationEditorStateTab|ClipReferenceRandomGuis|unknown|AnimationRandomClipReferenceGui||
|AnimationEditorStateTab|ClipReferenceSimpleGuis|unknown|AnimationSimpleClipReferenceGui||
|AnimationEditorViewer|GetSingleActiveClip||ActiveClip|Returns first entry from the [AnimationEditorViewer.ActiveClips] only if there is exactly one entry.|
|AnnexationMarker|GetCountry||Country||
|AnnexationMarker|GetLocation||Location||
|AntagonismBombSpecWrap|GetAntagoniser||Country||
|AntagonismTwoCountriesWrap|GetThem||Country||
|AntagonismTwoCountriesWrap|GetThemRef||Country||
|AntagonismTwoCountriesWrap|GetUs||Country||
|AntagonismTwoCountriesWrap|GetUsRef||Country||
|AntagonismWrapper|GetCountry||Country||
|Area|FindFirstNonIntegrated|unknown|Location||
|Area|GetCapital||Location||
|Area|GetRegion||Region||
|Area|MakeScope||Scope||
|ArmyBuilderLateralView|GetArmyTypesSortSearch||FilteredSortedList||
|ArmyBuilderLateralView|GetLocation||Location||
|ArmyBuilderLateralView|GetMercenariesSortSearch||FilteredSortedList||
|ArmyBuilderLateralView|GetPlayer||Country||
|ArmyBuilderLateralView|GetPreferredMethod||RecruitmentMethod||
|ArmyBuilderLateralView|Manager||LateralView||
|ArmyBuilderLateralView|Vars||Context||
|ArmyConstructionMarker|GetConstruction||Construction||
|Artist|MakeScope||Scope||
|ArtsItem|GetArt||WorkOfArt||
|ArtsView|GetArtsItemsSortSearch||FilteredSortedList||
|ArtsView|GetPlayer||Country||
|ArtsView|Manager||LateralView||
|ArtsView|Vars||Context||
|AskRepayLoanMessagePopup|GetFirstCountry||Country||
|AskRepayLoanMessagePopup|GetSecondCountry||Country||
|AutocompleteEntry|GetFilter||SearchFilter||
|AutomationLateralView|GetPlayStyle|unknown|PlayerPlayStyleItem||
|AutomationLateralView|GetPlayer||Country||
|AutomationLateralView|Manager||LateralView||
|AutomationLateralView|Vars||Context||
|AvailableMercenaryTypes|GetCategory||SubUnitCategory||
|Avatar|MakeScope||Scope||
|BattleParticipant|GetCountry||Country||
|BattleResult|GetAttacker||BattleSide||
|BattleResult|GetDefender||BattleSide||
|BattleResult|GetLoser||BattleSide||
|BattleResult|GetWinner||BattleSide||
|BattleResultMessage|GetAttacker||BattleResultMessageSide||
|BattleResultMessage|GetBattleResult||BattleResult||
|BattleResultMessage|GetDefender||BattleResultMessageSide||
|BattleResultMessageParticipant|GetSide||BattleResultMessageSide||
|BattleResultMessageParticipant|GetStats||BattleParticipant||
|BattleResultMessageSide|GetActiveParticipant||BattleResultMessageParticipant||
|BattleResultMessageSide|GetBattleSide||BattleSide||
|BattleResultMessageSide|GetMessagePopup||BattleResultMessage||
|BattleSide|GetCommander||Character||
|BattleSide|GetMainParticipant||Country||
|BattleUnitStats|GetCategory||SubUnitCategory||
|BattleView|GetCombat||Combat||
|BattleView|GetPlayer||Country||
|BattleView|Manager||LateralView||
|BattleView|Vars||Context||
|BlockedVisionMarker|GetLocation||Location||
|BrushSettings|Amount||BrushFloat||
|BrushSettings|Hardness||BrushFloat||
|BrushSettings|PixelSnap||BrushBool||
|BrushSettings|Radius||BrushFloat||
|BrushSettingsDropdown|Settings||BrushSettings||
|BuildInLocationLateralView|GetBestBuildLocationItem||LocationToBuildItem||
|BuildInLocationLateralView|GetBuildRankingItems||ConstructScoreRanking||
|BuildInLocationLateralView|GetBuildingType||BuildingType||
|BuildInLocationLateralView|GetEstate||Estate||
|BuildInLocationLateralView|GetItemsSortSearch||FilteredSortedList||
|BuildInLocationLateralView|GetLastBuildLocationItem||LocationToBuildItem||
|BuildInLocationLateralView|GetPlayer||Country||
|BuildInLocationLateralView|GetSelectedLocation||Location||
|BuildInLocationLateralView|GetSelectedMarket||Market||
|BuildInLocationLateralView|Manager||LateralView||
|BuildInLocationLateralView|Vars||Context||
|BuildLocationSelectMarket|Parent||BuildInLocationLateralView||
|Building|GetLocation||Location||
|Building|GetOwner||Country||
|Building|GetType||BuildingType||
|Building|GetUnderConstructionForPlayer||Construction||
|Building|MakeScope||Scope||
|BuildingCandidate|GetBuilding||Building||
|BuildingCandidate|GetBuildingCandidateUIAction||UIActionProvider||
|BuildingConstructionMarker|GetConstruction||Construction||
|BuildingItem|GetBuilding||Building||
|BuildingItem|GetBuildingItemUIAction||UIActionProvider||
|BuildingItem|GetBuildingType||BuildingType||
|BuildingItem|GetCardBuildingItemUIAction||UIActionProvider||
|BuildingItem|GetEstate||Estate||
|BuildingItem|GetFirstBuilding||Building||
|BuildingItem|GetNoCandidateUIAction||UIActionProvider||
|BuildingPromoteTimeWrapper|GetLocation||Location||
|BuildingSpyNetworkMarker|GetCountry||Country||
|BuildingSpyNetworkMarker|GetLocation||Location||
|BuildingType|GetAge||Age||
|BuildingType|GetCategory||BuildingCategory||
|BuildingType|GetConstructionDemand||GoodsDemand||
|BuildingType|GetEligibleEstate||EstateType||
|BuildingType|GetNextReplaced|unknown|BuildingType||
|BuildingType|GetObsoleteBuildingInLocation|unknown unknown|Building||
|BuildingType|GetPopType||PopType||
|BuildingType|MakeScope||Scope||
|BuildingView|GetBuildAllUIAction||UIActionProvider||
|BuildingView|GetBuildUIAction||UIActionProvider||
|BuildingView|GetBuilding||Building||
|BuildingView|GetGoods||Goods||
|BuildingView|GetPlayer||Country||
|BuildingView|Manager||LateralView||
|BuildingView|Vars||Context||
|CDPopEditor|GetCulturesSortSearch||FilteredSortedList||
|CDPopEditor|GetReligionsSortSearch||FilteredSortedList||
|CDPopEditor|GetSelectedPops||PopulationConfiguration||
|CDPopEditor|GetTemplate||PopulationConfiguration||
|CEconomy|GetCountry||Country||
|CEnumValueAnimation|AccessEnum||CPdxEnumValue||
|Cabinet|GetAction||CabinetAction||
|Cabinet|GetCharacter||Character||
|Cabinet|GetSocietalValue||SocietalValue||
|Cabinet|MakeScope||Scope||
|CabinetActionMarker|GetCabinet||Cabinet||
|CabinetActionMarker|GetProvince||Province||
|CabinetItem|GetAdvisorUIAction||UIActionProvider||
|CabinetItem|GetCabinet||Cabinet||
|CabinetItem|GetNoAdvisorUIAction||UIActionProvider||
|CallAllyAlert|GetCountry||Country||
|CallAllyAlert|GetUIAction||UIActionProvider||
|Cardinal|GetLocation||Location||
|Cardinal|GetOwner||Country||
|Cardinal|GetReligion||Religion||
|Cardinal|MakeScope||Scope||
|CasusBelli|GetWarGoalType||WarGoalType||
|CasusBelli|MakeScope||Scope||
|CategoryBuildingTypesItem|GetCategory||BuildingCategory||
|CharMessage|GetCharacter||Character||
|Character|GetArtInProgress||WorkOfArtType||
|Character|GetArtistType||Artist||
|Character|GetBirthLocation||Location||
|Character|GetCourtCountry||Country||
|Character|GetCulture||Culture||
|Character|GetDynasty||Dynasty||
|Character|GetEducation||ChildEducation||
|Character|GetEstateType||EstateType||
|Character|GetExploration||Exploration||
|Character|GetFather||Character||
|Character|GetLocation||Location||
|Character|GetMother||Character||
|Character|GetRebel||Rebel||
|Character|GetReligion||Religion||
|Character|GetReligiousFigureType||ReligiousFigure||
|Character|GetReligiousSchool||ReligiousSchool||
|Character|GetRoleMask||CharacterRoleMask||
|Character|GetSpouse||Character||
|Character|GetTimedModifierOwner||TimedModifierOwner||
|Character|GetUnitPointer||Unit||
|Character|MakeScope||Scope||
|CharacterActionItem|GetUIAction||UIActionProvider||
|CharacterInteraction|MakeScope||Scope||
|CharacterInteractionItem|GetInteraction||CharacterInteraction||
|CharacterItem|GetCharacter||Character||
|CharacterLateralview|GetCharacter||Character||
|CharacterLateralview|GetPlayer||Country||
|CharacterLateralview|Manager||LateralView||
|CharacterLateralview|Vars||Context||
|CharacterRulerData|GetRuler|unknown|Character||
|Chat|GetReceiver||Friend||
|ChatNotificationMessage|ChatMessage||ChatMessage||
|ChatTab|GetChat||Chat||
|ChildEducation|MakeScope||Scope||
|ChildEducationCandidate|GetChildEducation||ChildEducation||
|CityGraphicsWrap|GetSelectedBuilding||Building||
|CityGraphicsWrap|GetSelectedGood||Goods||
|CityGraphicsWrap|GetSelectedHolySite||HolySite||
|CityGraphicsWrap|GetSelectedLocation||Location||
|CityGraphicsWrap|GetSelectedPop||PopType||
|CityGraphicsWrap|GetSelectedWorkOfArt||WorkOfArt||
|CityMarker|GetLocation||Location||
|Climate|MakeScope||Scope||
|ColonialCharter|GetDestination||Location||
|ColonialCharter|GetOrigin||Location||
|ColonialCharter|GetOwner||Country||
|ColonialCharter|GetProvinceDefinition||ProvinceDefinition||
|ColonialCharter|MakeScope||Scope||
|ColonialCharterItem|GetColonialCharter||ColonialCharter||
|ColonialCharterItem|GetProvinceDefinition||ProvinceDefinition||
|ColonyCharterMarker|GetLocation||Location||
|Combat|GetAttacker||CombatSide||
|Combat|GetDefender||CombatSide||
|Combat|GetLocation||Location||
|Combat|GetWar||War||
|Combat|MakeScope||Scope||
|CombatImminentMarker|GetLocation||Location||
|CombatMarker|GetCombat||Combat||
|CombatMarker|GetLocation||Location||
|CombatSide|GetBattleSide||BattleSide||
|CombatSide|GetCaptured||CombatSubUnitArray||
|CombatSide|GetCenter||CombatSubUnitArray||
|CombatSide|GetCombat||Combat||
|CombatSide|GetCommander||Character||
|CombatSide|GetCountry||Country||
|CombatSide|GetLeadingUnit||Unit||
|CombatSide|GetLeft||CombatSubUnitArray||
|CombatSide|GetReserves||CombatSubUnitArray||
|CombatSide|GetRetreated||CombatSubUnitArray||
|CombatSide|GetRight||CombatSubUnitArray||
|CombatSide|MakeScope||Scope||
|CombatSideWrap|GetCombatSide||CombatSide||
|CombatSubUnitArray|GetCombatSide||CombatSide||
|CondottieriItem|GetUIHeaderAction||UIActionProvider||
|CondottieriItem|GetUnit||Unit||
|ConquistadorConstructionMarker|GetConstruction||Construction||
|ConstructScoreItem|GetLocation||Location||
|ConstructScoreRanking|GetBuildingType||BuildingType||
|ConstructScoreRanking|GetConstructScoreFirstItem||ConstructScoreItem||
|ConstructScoreRanking|GetGoods||Goods||
|ConstructScoreRanking|GetInvalidFirstItem||ConstructScoreItem||
|ConstructScoreRanking|GetLastConstruction||Construction||
|ConstructScoreRanking|GetLastConstructionLocation||Location||
|Construction|GetBuilding||Building||
|Construction|GetCountry||Country||
|Construction|GetEstateType||EstateType||
|Construction|GetExplorationArea||Area||
|Construction|GetGoodsDemand||GoodsDemand||
|Construction|GetLocation||Location||
|Construction|GetLocationRank||LocationRank||
|Construction|GetProvince||Province||
|Construction|GetSubUnitDefinition||SubUnitType||
|ConstructionItem|GetConstruction||Construction||
|Context|AccessUIVars||UIVariables||
|Continent|MakeScope||Scope||
|ControlGroupsView|AccessGroup|unknown|GroupItem||
|CountriesListView|GetCountriesSortSearch||FilteredSortedList||
|CountriesListView|GetPlayer||Country||
|CountriesListView|Manager||LateralView||
|CountriesListView|Vars||Context||
|CountriesListViewItem|GetCountry||Country||
|Country|GetBiasConfig|unknown|BiasType||
|Country|GetCapital||Location||
|Country|GetCapitalOrParliament||Location||
|Country|GetCapitalRegion||Region||
|Country|GetCommonDialect||Dialect||
|Country|GetCommonLanguage||Language||
|Country|GetCourtDialect||Dialect||
|Country|GetCourtLanguage||Language||
|Country|GetCulture||Culture||
|Country|GetCurrentCivilWar||Country||
|Country|GetCurrentReligiousFocus||CurrentReligiousFocus||
|Country|GetCurrentResearch||CurrentResearch||
|Country|GetDiplomacy||Diplomacy||
|Country|GetDominantLanguage||Language||
|Country|GetDynamicQuickDiplomaticActions||QuickDiplomaticActions||
|Country|GetEconomy||CEconomy||
|Country|GetEmploymentSystem||EmploymentSystem||
|Country|GetGovernment||Government||
|Country|GetHighestProgressRebel||Rebel||
|Country|GetLiturgicalDialect||Dialect||
|Country|GetLiturgicalLanguage||Language||
|Country|GetMilitaryStance||SubjectMilitaryStance||
|Country|GetMissionProgress||MissionProgress||
|Country|GetModifierTooltipContext|unknown|CountryModifierWrap||
|Country|GetPlayerQuickDiplomaticActions||QuickDiplomaticActions||
|Country|GetPopulationChart||CountryPopulationChart||
|Country|GetQuickDiplomaticActions||QuickDiplomaticActions||
|Country|GetRank||CountryRank||
|Country|GetReligion||Religion||
|Country|GetReligiousSchool||ReligiousSchool||
|Country|GetScore||Score||
|Country|GetStaticModifier|unknown|StaticModifier||
|Country|GetTimedModifierOwner||TimedModifierOwner||
|Country|GetWarLosses||WarLosses||
|Country|MakeScope||Scope||
|CountryCultureLateralView|GetCountry||Country||
|CountryCultureLateralView|GetCulture||Culture||
|CountryCultureLateralView|GetCultureSortSearch||FilteredSortedList||
|CountryCultureLateralView|GetPlayer||Country||
|CountryCultureLateralView|GetPopsPiechartWidget||PopsPiechartWidget||
|CountryCultureLateralView|GetWorkOfArtSortSearch||FilteredSortedList||
|CountryCultureLateralView|Manager||LateralView||
|CountryCultureLateralView|Vars||Context||
|CountryCultureLateralViewWorkOfArtItem|GetWorkOfArt||WorkOfArt||
|CountryDiplomaticItem|GetCountry||Country||
|CountryInteraction|MakeScope||Scope||
|CountryListOverview|GetCountriesSortSearch||FilteredSortedList||
|CountryMessage|GetFirstCountry||Country||
|CountryMessage|GetSecondCountry||Country||
|CountryPeopleLateralView|GetCharactersSortSearch||FilteredSortedList||
|CountryPeopleLateralView|GetDynastiesSortSearch||FilteredSortedList||
|CountryPeopleLateralView|GetPlayer||Country||
|CountryPeopleLateralView|GetPopsPiechartWidget||PopsPiechartWidget||
|CountryPeopleLateralView|GetPopsSortSearch||FilteredSortedList||
|CountryPeopleLateralView|GetRebelsSortSearch||FilteredSortedList||
|CountryPeopleLateralView|Manager||LateralView||
|CountryPeopleLateralView|Vars||Context||
|CountryPopulationChart|GetCountry||Country||
|CountryPopulationChart|GetPopsPiechartWidget||PopsPiechartWidget||
|CountryRank|MakeScope||Scope||
|CountryRankCandidate|GetCountryRank||CountryRank||
|CountryReligionLateralView|GetCanonizeAction||UIActionProvider||
|CountryReligionLateralView|GetCountry||Country||
|CountryReligionLateralView|GetCurrentReligiousFocus||ReligiousFocusGlue||
|CountryReligionLateralView|GetHolySitesSortSearch||FilteredSortedList||
|CountryReligionLateralView|GetPatriarchate||InternationalOrganization||
|CountryReligionLateralView|GetPlayer||Country||
|CountryReligionLateralView|GetReligion||Religion||
|CountryReligionLateralView|GetReligionSortSearch||FilteredSortedList||
|CountryReligionLateralView|Manager||LateralView||
|CountryReligionLateralView|Vars||Context||
|CreateCasusBelliMarker|GetCountry||Country||
|CreateCasusBelliMarker|GetLocation||Location||
|CreateSubjectsLateralView|GetPlayer||Country||
|CreateSubjectsLateralView|Manager||LateralView||
|CreateSubjectsLateralView|Vars||Context||
|Culture|GetCountriesList||QuickCultureCountryList||
|Culture|GetDialect||Dialect||
|Culture|GetDominantCountry||Country||
|Culture|GetLanguage||Language||
|Culture|MakeScope||Scope||
|CultureGroup|MakeScope||Scope||
|CultureItem|GetCulture||Culture||
|CulturesLedger|GetCultureItemsSortSearch||FilteredSortedList||
|CulturesLedger|GetPlayer||Country||
|CulturesLedger|Manager||LateralView||
|CulturesLedger|Vars||Context||
|CurrencyPriceWrap|GetCurrencyGameConceptType||GameConceptTooltip||
|CurrencyPriceWrap|GetPrice||PriceTooltipWrap||
|CurrentNeedsItem|GetGoods||Goods||
|CurrentNeedsItem|GetMarket||Market||
|CurrentReligiousFocus|GetReligiousFocus||ReligiousFocus||
|CurrentResearch|GetAdvance||Advance||
|CurryingFavorsMarker|GetCountry||Country||
|CurryingFavorsMarker|GetLocation||Location||
|DecalsEditorDecalInstancesList|AccessFilter||DecalsEditorSearchFilter||
|DecalsEditorDecalSetsList|AccessFilter||DecalsEditorSearchFilter||
|DeclareWarAlly|GetCountry||Country||
|DeclareWarLateralView|GetDeclareWarAction||UIActionProvider||
|DeclareWarLateralView|GetEnemyCountry||Country||
|DeclareWarLateralView|GetPlayer||Country||
|DeclareWarLateralView|GetPriceImpactFromWar||WarImpactWrap||
|DeclareWarLateralView|GetRecipient||Country||
|DeclareWarLateralView|GetSelectedWarGoal||WarGoal||
|DeclareWarLateralView|Manager||LateralView||
|DeclareWarLateralView|Vars||Context||
|DemandCategoryWrap|GetGoods||Goods||
|DemandsOnMarketWrap|GetGoods||Goods||
|DemandsOnMarketWrap|GetMarket||Market||
|DesertConnectionMarker|GetLocation||Location||
|Dialect|GetLanguage||Language||
|DiploAlert|GetCountry||Country||
|Diplomacy|GetCountry||Country||
|Diplomacy|GetHighestPrioritySpecialStatus|unknown|SpecialStatus||
|Diplomacy|GetMarriageUnion||InternationalOrganization||
|Diplomacy|GetOverlord||Country||
|Diplomacy|GetRelation|unknown|DiplomacyStatus||
|Diplomacy|GetSubjectType||SubjectType||
|Diplomacy|GetTopOverlord||Country||
|Diplomacy|GetTopOverlordOrThis||Country||
|Diplomacy|GetUnion||InternationalOrganization||
|DiplomacyDialog|GetCountry||Country||
|DiplomacyLateralView|GetCountriesSortSearch||FilteredSortedList||
|DiplomacyLateralView|GetDiplomaticRelationsSortSearch||FilteredSortedList||
|DiplomacyLateralView|GetOrgsSortSearch||FilteredSortedList||
|DiplomacyLateralView|GetPlayer||Country||
|DiplomacyLateralView|Manager||LateralView||
|DiplomacyLateralView|Vars||Context||
|DiplomacyMacrobuilderLateralView|GetDefaultCategory||DiplomaticActionCategory||
|DiplomacyMacrobuilderLateralView|GetDiploCategoriesSortSearch||FilteredSortedList||
|DiplomacyMacrobuilderLateralView|GetPlayer||Country||
|DiplomacyMacrobuilderLateralView|GetSelectedCountry||Country||
|DiplomacyMacrobuilderLateralView|Manager||LateralView||
|DiplomacyMacrobuilderLateralView|Vars||Context||
|DiplomacyMacrobuilderSelectCountry|Parent||DiplomacyMacrobuilderLateralView||
|DiplomacyStatus|GetWar||War||
|DiplomaticActionItem|GetRecipient||Country||
|Disaster|GetOwner||Country||
|Disaster|GetType||DisasterType||
|DisasterType|MakeScope||Scope||
|DisasterView|GetDisaster||Disaster||
|DisasterView|GetPlayer||Country||
|DisasterView|Manager||LateralView||
|DisasterView|Vars||Context||
|Disease|GetOrigin||Location||
|Disease|MakeScope||Scope||
|DiseaseOutbreak|GetDisease||Disease||
|DiseaseOutbreak|GetOrigin||Location||
|DiseaseOutbreak|MakeScope||Scope||
|DiseasesLateralView|GetPlayer||Country||
|DiseasesLateralView|GetPossibleDiseasesSortSearch||FilteredSortedList||
|DiseasesLateralView|Manager||LateralView||
|DiseasesLateralView|Vars||Context||
|DockableLayoutManager|AccessActiveLayout||DockableLayout||
|DockableLayoutManager|AccessLayoutSearchList||ToolPropertySearchList||
|DockableLayoutManager|AccessSelectedLayout||DockableLayout||
|DynastiesLedger|GetDynastyItemsSortSearch||FilteredSortedList||
|DynastiesLedger|GetPlayer||Country||
|DynastiesLedger|Manager||LateralView||
|DynastiesLedger|Vars||Context||
|Dynasty|GetDynastyFounder||Character||
|Dynasty|GetDynastyHead||Character||
|Dynasty|GetHome||Location||
|Dynasty|MakeScope||Scope||
|DynastyItem|GetDynasty||Dynasty||
|DynastyMarker|GetDynasty||Dynasty||
|DynastyMarker|GetLocation||Location||
|DynastyNodeItem|GetCharacter||Character||
|DynastyTreeView|GetAutocompleteFromKey|unknown|Character||
|DynastyTreeView|GetDynasty||Dynasty||
|DynastyTreeView|GetPlayer||Country||
|DynastyTreeView|GetSearchBar||SearchBar||
|DynastyTreeView|Manager||LateralView||
|DynastyTreeView|Vars||Context||
|EconomyItem|GetMaintenanceSetting||MaintenanceSetting||
|EconomyItem|GetTaxRateSetting||TaxRateSetting||
|EconomyView|GetMaintenanceSetting|unknown|MaintenanceSetting||
|EconomyView|GetPlayer||Country||
|EconomyView|Manager||LateralView||
|EconomyView|Vars||Context||
|EditorSettingsWindow|AccessActivePage||EditorSettingsPage||
|EmploymentSystem|MakeScope||Scope||
|Encyclopedia|AccessCurrentPage||EncyclopediaPage||
|Encyclopedia|GetAllPage||EncyclopediaPage||
|Encyclopedia|GetCurrentPage||EncyclopediaPage||
|EncyclopediaEntryView|Get||EncyclopediaEntry||
|EncyclopediaLateralView|GetPlayer||Country||
|EncyclopediaLateralView|Manager||LateralView||
|EncyclopediaLateralView|Vars||Context||
|EntityDesigner|AccessUndoer||UndoStack||
|EntityEditor|Entity||ViewerEntity||
|Estate|GetCountry||Country||
|Estate|GetRebel||Rebel||
|Estate|GetType||EstateType||
|Estate|MakeScope||Scope||
|EstateOpinionWrap|GetCountry||Country||
|EstateOpinionWrap|GetEstate||Estate||
|EstateOpinionWrap|GetEstateType||EstateType||
|EstateOpinionWrap|GetTarget||Country||
|EstatePrivilege|GetType||EstateType||
|EstateType|MakeScope||Scope||
|EstatesItem|GetEstate||Estate||
|Ethnicity|MakeScope||Scope||
|EventTargetSetupContext|AccessVariableLists||VariableListStore||
|EventTargetSetupContext|AccessVariables||VariableStore||
|EventWindow|AccessOptionItemWithKey|unknown|EventOption||
|EventWindow|GetFirstCharacter||Character||
|EventWindow|GetLockableInfo||LockableInfo||
|EventWindow|GetSecondCharacter||Character||
|ExpandRawGoodsLateralView|GetBestExpandingLocationItem||RawGoodLocationItem||
|ExpandRawGoodsLateralView|GetExpandRankingItems||ConstructScoreRanking||
|ExpandRawGoodsLateralView|GetLastExpandingLocationItem||RawGoodLocationItem||
|ExpandRawGoodsLateralView|GetPlayer||Country||
|ExpandRawGoodsLateralView|GetRawGoodLocationsSortSearch||FilteredSortedList||
|ExpandRawGoodsLateralView|GetSelectedLocation||Location||
|ExpandRawGoodsLateralView|GetSelectedMarket||Market||
|ExpandRawGoodsLateralView|Manager||LateralView||
|ExpandRawGoodsLateralView|Vars||Context||
|ExpandRawGoodsSelectMarket|Parent||ExpandRawGoodsLateralView||
|ExpansionLateralView|GetColonialChartersSortSearch||FilteredSortedList||
|ExpansionLateralView|GetExplorationsSortSearch||FilteredSortedList||
|ExpansionLateralView|GetPlayer||Country||
|ExpansionLateralView|GetProvincesSortSearch||FilteredSortedList||
|ExpansionLateralView|Manager||LateralView||
|ExpansionLateralView|Vars||Context||
|Exploration|GetArea||Area||
|Exploration|GetCharacter||Character||
|Exploration|GetLocation||Location||
|Exploration|GetOwner||Country||
|Exploration|MakeScope||Scope||
|ExtraTooltipInfo|GetSectionIndex|unknown|SectionIndex||
|ExtraTooltipInfo|GetTooltiped||PdxGuiWidget||
|ExtraTooltipInfo|GetUIAction||UIAction||
|FilteredSortedList|GetSearchBar||SearchBar||
|FilteredSortedList|GetSortKeyButton|unknown|SortKey||
|FilteredSortedList|WithFilterTags|unknown|FilteredSortedList||
|FoodLocationItem|GetBuildingsUIAction||UIActionProvider||
|FoodLocationItem|GetGoods||Goods||
|FoodLocationItem|GetLocation||Location||
|FoodLocationItem|GetUpgradeRGOConstructionDemand||GoodsDemand||
|FoodProductionLateralView|GetFoodProductionListSortSearch||FilteredSortedList||
|FoodProductionLateralView|GetPlayer||Country||
|FoodProductionLateralView|GetSelectedMarket||Market||
|FoodProductionLateralView|GetSelectedProvince||Province||
|FoodProductionLateralView|Manager||LateralView||
|FoodProductionLateralView|Vars||Context||
|FoodProductionListItem|AccessLocationItem||FoodLocationItem||
|FoodProductionListItem|AccessProvinceItem||FoodProvinceItem||
|FoodProductionSelectMarket|Parent||FoodProductionLateralView||
|FoodProvinceItem|GetProvince||Province||
|ForeignBuildingLocationItem|GetLocation||Location||
|ForeignCountrySelectCountry|Parent||ForeignCountryView||
|ForeignCountryView|GetCharactersSortSearch||FilteredSortedList||
|ForeignCountryView|GetCountry||Country||
|ForeignCountryView|GetCountryPointer||Country||
|ForeignCountryView|GetDefaultCategory||DiplomaticActionCategory||
|ForeignCountryView|GetDiploCategoriesSortSearch||FilteredSortedList||
|ForeignCountryView|GetDiplomaticAction|unknown|DiplomaticActionItem||
|ForeignCountryView|GetDiplomaticRelationsSortSearch||FilteredSortedList||
|ForeignCountryView|GetHeirSelection||HeirSelectionCandidate||
|ForeignCountryView|GetPlayer||Country||
|ForeignCountryView|GetRelativePowerTooltipGlue||RelativePowerTooltipGlue||
|ForeignCountryView|GetRulerTermEntriesSortSearch||FilteredSortedList||
|ForeignCountryView|GetWarUIAction||UIActionProvider||
|ForeignCountryView|Manager||LateralView||
|ForeignCountryView|Vars||Context||
|FormNewCountry|GetCandidatesSortSearch||FilteredSortedList||
|FormNewCountry|GetNextRankCandidate||CountryRankCandidate||
|FormableCountry|GetOrCreateCoatOfArms|unknown|CoatOfArmsWrapper||
|FormableCountry|MakeScope||Scope||
|FormattedTooltipWrap|GetEstate||Estate||
|FortFlipRestoreMarker|GetLocation||Location||
|FortMarker|GetLocation||Location||
|FortMarker|GetSiege||Siege||
|FrontEndMainView|AccessMarketingContainer||MarketingContainer||
|FrontEndMainView|GetLatestPlaythrough||PlaythroughItem||
|FrontEndSinglePlayerView|GetSelectedProficiency||PlayerProficiency||
|FrontEndSinglePlayerView|GetSelectedScenario||Scenario||
|FrontEndView|AccessMarketingContainer||MarketingContainer||
|GUIAchievement|GetAchievement||Achievement||
|GameLobby|GetDiplomaticRelationsSortSearch||FilteredSortedList||
|GameLobby|GetSelectedCountry||Country||
|GameLobby|GetUniqueContentCategoriesSortSearch||FilteredSortedList||
|GameLobby|GetUniqueContentDescription||UniqueContentDescription||
|GameLobby|Vars||Context||
|GenericAction|MakeScope||Scope||
|GeographyGlue|GetGeography||InteractionTarget||
|God|MakeScope||Scope||
|GodWithReligionWrap|GetGod||God||
|GodWithReligionWrap|GetReligion||Religion||
|GoodItem|GetGoods||Goods||
|Goods|MakeScope||Scope||
|GoodsDemand|GetCategory||DemandCategory||
|GoodsDemand|MakeScope||Scope||
|GoodsDemandEntry|GetGoods||Goods||
|GoodsDetailsLateralView|GetGoods||Goods||
|GoodsDetailsLateralView|GetGoodsInMarketsSortSearch||FilteredSortedList||
|GoodsDetailsLateralView|GetPlayer||Country||
|GoodsDetailsLateralView|GetSourcesSortSearch||FilteredSortedList||
|GoodsDetailsLateralView|Manager||LateralView||
|GoodsDetailsLateralView|Vars||Context||
|GoodsInMarket|GetGoods||Goods||
|GoodsInMarket|GetGoodsMarketEntry||GoodsMarketEntry||
|GoodsInMarket|GetMarket||Market||
|GoodsItem|GetBiggestMarket||Market||
|GoodsItem|GetGoods||Goods||
|GoodsMarketEntry|GetGoods||Goods||
|GoodsMarketEntry|GetMarket||Market||
|GoodsMessage|GetGoods||Goods||
|GoodsOnMarketWrap|GetMarket||Market||
|GoodsPriceOnMarketWrap|GetGoods||Goods||
|GoodsPriceOnMarketWrap|GetGoodsMarketEntry||GoodsMarketEntry||
|GoodsPriceOnMarketWrap|GetMarket||Market||
|GoodsProductionLateralView|GetPlayer||Country||
|GoodsProductionLateralView|GetRawGoodsSortSearch||FilteredSortedList||
|GoodsProductionLateralView|GetSelectedMarket||Market||
|GoodsProductionLateralView|Manager||LateralView||
|GoodsProductionLateralView|Vars||Context||
|GoodsProductionSelectMarket|Parent||GoodsProductionLateralView||
|GoodsSellPriceWrap|GetGoods||Goods||
|GoodsSourceItem|GetGoods||Goods||
|GoodsSourceItem|GetLocation||Location||
|GoodsView|GetGoodsItemsSortSearch||FilteredSortedList||
|GoodsView|GetPlayer||Country||
|GoodsView|Manager||LateralView||
|GoodsView|Vars||Context||
|GovReformOutlinerEntry|GetReformItem||ReformItem||
|Government|CalcBestRepresentativeForPlaystyle|unknown|Character||
|Government|GetActiveRegent||Character||
|Government|GetBestHeirCandidateFor|unknown|Character||
|Government|GetConsort||Character||
|Government|GetEstate|unknown|Estate||
|Government|GetEstateFromKey|EstateKey|Estate||
|Government|GetGovernmentType||GovernmentType||
|Government|GetHeir||Character||
|Government|GetHeirSelection||HeirSelection||
|Government|GetImplementedPolicyForLaw|unknown|ImplementedPolicy||
|Government|GetParliament||Parliament||
|Government|GetPolicyForLaw|unknown|Policy||
|Government|GetPreviousRuler||Character||
|Government|GetRegencyType||RegencyType||
|Government|GetRuler||Character||
|Government|GetRulerOrHeirIfRegent||Character||
|Government|GetRulerOrRegent||Character||
|GovernmentReform|GetAge||Age||
|GovernmentReform|GetGovernmentType||GovernmentType||
|GovernmentReformItem|GetReform||GovernmentReform||
|GovernmentReformItem|GetUIAction||UIActionProvider||
|GovernmentReformsLateralView|GetPlayer||Country||
|GovernmentReformsLateralView|GetReformsSortSearch||FilteredSortedList||
|GovernmentReformsLateralView|Manager||LateralView||
|GovernmentReformsLateralView|Vars||Context||
|GovernmentType|MakeScope||Scope||
|GovernmentView|GetCountry||Country||
|GovernmentView|GetHeirSelection||HeirSelectionCandidate||
|GovernmentView|GetLawCategoriesSortSearch||FilteredSortedList||
|GovernmentView|GetModifiersSortSearch||FilteredSortedList||
|GovernmentView|GetPlayer||Country||
|GovernmentView|Manager||LateralView||
|GovernmentView|Vars||Context||
|GraphPanel|AccessAnimationEditorSearch||NodeEditorSearch||
|GraphPanel|AccessMetadataWindow||MetadataWindow||
|GraphPanel|GetMetadataWindow||MetadataWindow||
|GreatPowerItem|GetCountry||Country||
|GroupItem|GetButtonAction||UIActionProvider||
|GroupItem|GetCharacter||Character||
|GroupItem|GetCountry||Country||
|GroupItem|GetInternationalOrganization||InternationalOrganization||
|GuiGameRule|GetRule||GameRule||
|GuiGameRule|GetSetting||GameRuleSetting||
|GuiGameRulePreset|GetSettingForRule|unknown|GameRuleSetting||
|Hegemony|MakeScope||Scope||
|HeirSelection|MakeScope||Scope||
|HeirSelectionCandidate|GetBestHeirCandidate||HeirSelectionValue||
|HeirSelectionCandidate|GetHeirSelection||HeirSelection||
|HeirSelectionCandidate|GetSelectAction||UIActionProvider||
|HeirSelectionValue|GetHeir||Character||
|HintsLateralView|GetHintsSortSearch||FilteredSortedList||
|HintsLateralView|GetPlayer||Country||
|HintsLateralView|Manager||LateralView||
|HintsLateralView|Vars||Context||
|HistoricalScoreItem|GetHistoricalScore||HistoricalScore||
|HolySite|GetLocation||Location||
|HolySite|GetType||HolySiteType||
|HolySite|MakeScope||Scope||
|HolySiteDefinition|MakeScope||Scope||
|HolySiteGlue|GetHolySite||HolySite||
|HolySiteType|MakeScope||Scope||
|ImplementedCabinetAction|GetAction||CabinetAction||
|ImplementedEstatePrivilege|GetEstatePrivilege||EstatePrivilege||
|ImplementedGovernmentReform|GetReform||GovernmentReform||
|ImplementedPolicy|GetPolicy||Policy||
|ImportExportLateralView|GetBestDealMarket||Market||
|ImportExportLateralView|GetGoods||Goods||
|ImportExportLateralView|GetItemsSortSearch||FilteredSortedList||
|ImportExportLateralView|GetMarket||Market||
|ImportExportLateralView|GetPlayer||Country||
|ImportExportLateralView|Manager||LateralView||
|ImportExportLateralView|Vars||Context||
|ImportExportMarker|GetLocation||Location||
|ImportExportMarker|GetPossibleItem||PossibleItem||
|ImportantCultureItem|GetCulture||Culture||
|ImportantReligionItem|GetReligion||Religion||
|ImproveOpinionMarker|GetCountry||Country||
|ImproveOpinionMarker|GetLocation||Location||
|InGameMissionTaskItem|GetTask||MissionTaskDefinition||
|InGameTopbar|AccessAlertManager||AlertManager||
|InGameTopbar|AccessControlGroups||ControlGroupsView||
|InGameTopbar|GetCurrentAdvanceUIAction||UIActionProvider||
|InGameTopbar|GetPlayer||Country||
|Institution|GetAge||Age||
|Institution|GetOrigin||Location||
|Institution|MakeScope||Scope||
|InstitutionItem|GetInstitution||Institution||
|InstitutionItem|GetUIAction||UIActionProvider||
|InstitutionMessage|GetInstitution||Institution||
|InteractionTarget|AccessUnit||Unit||
|InteractionTarget|GetActiveResolution||ActiveResolution||
|InteractionTarget|GetAdvanceType||AdvanceDefinition||
|InteractionTarget|GetAge||Age||
|InteractionTarget|GetArea||Area||
|InteractionTarget|GetArtist||Artist||
|InteractionTarget|GetAvatar||Avatar||
|InteractionTarget|GetBuilding||Building||
|InteractionTarget|GetBuildingType||BuildingType||
|InteractionTarget|GetCabinet||Cabinet||
|InteractionTarget|GetCabinetAction||CabinetAction||
|InteractionTarget|GetCardinal||Cardinal||
|InteractionTarget|GetCasusBelli||CasusBelli||
|InteractionTarget|GetCharacter||Character||
|InteractionTarget|GetCharacterInteraction||CharacterInteraction||
|InteractionTarget|GetChildEducation||ChildEducation||
|InteractionTarget|GetClimate||Climate||
|InteractionTarget|GetColonialCharter||ColonialCharter||
|InteractionTarget|GetCombat||Combat||
|InteractionTarget|GetCombatSide||CombatSide||
|InteractionTarget|GetContinent||Continent||
|InteractionTarget|GetCountry||Country||
|InteractionTarget|GetCountryInteraction||CountryInteraction||
|InteractionTarget|GetCountryRank||CountryRank||
|InteractionTarget|GetCulture||Culture||
|InteractionTarget|GetCultureGroup||CultureGroup||
|InteractionTarget|GetDialect||Dialect||
|InteractionTarget|GetDisaster||Disaster||
|InteractionTarget|GetDisasterType||DisasterType||
|InteractionTarget|GetDisease||Disease||
|InteractionTarget|GetDiseaseOutbreak||DiseaseOutbreak||
|InteractionTarget|GetDynasty||Dynasty||
|InteractionTarget|GetEmploymentSystem||EmploymentSystem||
|InteractionTarget|GetEstate||Estate||
|InteractionTarget|GetEstatePrivilege||EstatePrivilege||
|InteractionTarget|GetEstateType||EstateType||
|InteractionTarget|GetEthnicity||Ethnicity||
|InteractionTarget|GetExploration||Exploration||
|InteractionTarget|GetFormableCountry||FormableCountry||
|InteractionTarget|GetGenericAction||GenericAction||
|InteractionTarget|GetGod||God||
|InteractionTarget|GetGoods||Goods||
|InteractionTarget|GetGoodsDemand||GoodsDemand||
|InteractionTarget|GetGovernmentReform||GovernmentReform||
|InteractionTarget|GetGovernmentType||GovernmentType||
|InteractionTarget|GetGraphicalCultureType||GraphicalCultureType||
|InteractionTarget|GetHegemony||Hegemony||
|InteractionTarget|GetHeirSelection||HeirSelection||
|InteractionTarget|GetHolySite||HolySite||
|InteractionTarget|GetHolySiteDefinition||HolySiteDefinition||
|InteractionTarget|GetHolySiteType||HolySiteType||
|InteractionTarget|GetInstitution||Institution||
|InteractionTarget|GetInternationalOrganization||InternationalOrganization||
|InteractionTarget|GetInternationalOrganizationType||InternationalOrganizationType||
|InteractionTarget|GetLandOwnershipRule||LandOwnershipRule||
|InteractionTarget|GetLanguage||Language||
|InteractionTarget|GetLaw||Law||
|InteractionTarget|GetLevySetup||LevySetup||
|InteractionTarget|GetLoan||Loan||
|InteractionTarget|GetLocation||Location||
|InteractionTarget|GetLocationRank||LocationRank||
|InteractionTarget|GetMarket||Market||
|InteractionTarget|GetMercenary||Mercenary||
|InteractionTarget|GetMissionDefinition||MissionDefinition||
|InteractionTarget|GetMissionTaskDefinition||MissionTaskDefinition||
|InteractionTarget|GetParliamentAgenda||ParliamentAgenda||
|InteractionTarget|GetParliamentIssue||ParliamentIssue||
|InteractionTarget|GetParliamentType||ParliamentType||
|InteractionTarget|GetPayment||Payment||
|InteractionTarget|GetPolicy||Policy||
|InteractionTarget|GetPop||Pop||
|InteractionTarget|GetPopType||PopType||
|InteractionTarget|GetPrice||Price||
|InteractionTarget|GetPrivateer||Privateer||
|InteractionTarget|GetProductionMethod||ProductionMethod||
|InteractionTarget|GetProvince||Province||
|InteractionTarget|GetProvinceDefinition||ProvinceDefinition||
|InteractionTarget|GetRebel||Rebel||
|InteractionTarget|GetRecruitmentMethod||RecruitmentMethod||
|InteractionTarget|GetRegencyType||RegencyType||
|InteractionTarget|GetRegion||Region||
|InteractionTarget|GetRelationType||ScriptedRelationType||
|InteractionTarget|GetReligion||Religion||
|InteractionTarget|GetReligionGroup||ReligionGroup||
|InteractionTarget|GetReligiousAspect||ReligiousAspect||
|InteractionTarget|GetReligiousFaction||ReligiousFaction||
|InteractionTarget|GetReligiousFigure||ReligiousFigure||
|InteractionTarget|GetReligiousFocus||ReligiousFocus||
|InteractionTarget|GetReligiousSchool||ReligiousSchool||
|InteractionTarget|GetResolution||Resolution||
|InteractionTarget|GetRoadType||RoadType||
|InteractionTarget|GetScopeObjectReference||Scope||
|InteractionTarget|GetScriptableHintDefinition||ScriptableHintDefinition||
|InteractionTarget|GetScriptedPeaceTreatyType||ScriptedPeaceTreatyType||
|InteractionTarget|GetSiege||Siege||
|InteractionTarget|GetSituation||Situation||
|InteractionTarget|GetSocietalValue||SocietalValue||
|InteractionTarget|GetSpecialStatus||SpecialStatus||
|InteractionTarget|GetSubContinent||SubContinent||
|InteractionTarget|GetSubUnit||SubUnit||
|InteractionTarget|GetSubUnitCategory||SubUnitCategory||
|InteractionTarget|GetSubjectMilitaryStance||SubjectMilitaryStance||
|InteractionTarget|GetSubjectType||SubjectType||
|InteractionTarget|GetTopography||Topography||
|InteractionTarget|GetTrade||Trade||
|InteractionTarget|GetTrait||Trait||
|InteractionTarget|GetUnit||Unit||
|InteractionTarget|GetUnitAbility||UnitAbility||
|InteractionTarget|GetUnitType||SubUnitType||
|InteractionTarget|GetVegetation||Vegetation||
|InteractionTarget|GetWar||War||
|InteractionTarget|GetWeatherSystem||WeatherSystem||
|InteractionTarget|GetWorkOfArt||WorkOfArt||
|InteractionTarget|GetWorkOfArtType||WorkOfArtType||
|InternationalOrganization|GetActiveResolution|unknown|ActiveResolution||
|InternationalOrganization|GetActiveResolutionFromKey|unknown|ActiveResolution||
|InternationalOrganization|GetCountryOrderedByGreatPowerScore|unknown|Country||
|InternationalOrganization|GetCountryWithHighestGreatPower||Country||
|InternationalOrganization|GetCountryWithHighestGreatPowerScoreWithSpecialStatus|unknown|Country||
|InternationalOrganization|GetImplementedPolicyForLaw|unknown|ImplementedPolicy||
|InternationalOrganization|GetLeaderCountry||Country||
|InternationalOrganization|GetLeaderScopeObjectAtIndex|unknown|Scope||
|InternationalOrganization|GetLeadershipElectionResolution||Resolution||
|InternationalOrganization|GetParliament||Parliament||
|InternationalOrganization|GetPolicyForLaw|unknown|Policy||
|InternationalOrganization|GetReligion||Religion||
|InternationalOrganization|GetSeat||Location||
|InternationalOrganization|GetSpecialStatus|unknown|SpecialStatus||
|InternationalOrganization|GetTarget||Country||
|InternationalOrganization|GetTimedModifierOwner||TimedModifierOwner||
|InternationalOrganization|GetType||InternationalOrganizationType||
|InternationalOrganization|GetVariableSpec|unknown|InternationalOrganizationTypeVariable||
|InternationalOrganization|MakeScope||Scope||
|InternationalOrganizationMessagePopup|GetCountry||Country||
|InternationalOrganizationMessagePopup|GetInternationalOrganization||InternationalOrganization||
|InternationalOrganizationType|GetLandOwnershipRule||LandOwnershipRule||
|InternationalOrganizationType|MakeScope||Scope||
|InternationalOrganizationTypeView|GetInternationalOrganizationType||InternationalOrganizationType||
|InternationalOrganizationTypeView|GetPlayer||Country||
|InternationalOrganizationTypeView|Manager||LateralView||
|InternationalOrganizationTypeView|Vars||Context||
|InternationalOrganizationsView|GetFavoriteForVoter|unknown|Country||
|InternationalOrganizationsView|GetHolySitesSortSearch||FilteredSortedList||
|InternationalOrganizationsView|GetInternationalOrganization||InternationalOrganization||
|InternationalOrganizationsView|GetLawCategoriesSortSearch||FilteredSortedList||
|InternationalOrganizationsView|GetMembersSortSearch||FilteredSortedList||
|InternationalOrganizationsView|GetPlayer||Country||
|InternationalOrganizationsView|GetSaintsSortSearch||FilteredSortedList||
|InternationalOrganizationsView|GetSpecialMembersSortSearch||FilteredSortedList||
|InternationalOrganizationsView|GetSpecialStatusCountry|unknown|Country||
|InternationalOrganizationsView|Manager||LateralView||
|InternationalOrganizationsView|Vars||Context||
|JominiGameRules|AccessNamedGameRule|unknown|GuiGameRule||
|JominiGameRules|GetSelectedPreset||GuiGameRulePreset||
|JominiLoadWindow|AccessLatestPlaythrough||PlaythroughItem||
|JominiNotification|GetDate||Date||
|JominiNotification|SetupDataContexts|unknown|NotificationDummyContext||
|JominiSettingsWindow|AccessActivePage||SettingsPage||
|LackingGoodsForRepairEntry|GetMarket||Market||
|LandOwnershipRule|MakeScope||Scope||
|Language|GetFamily||LanguageFamily||
|Language|MakeScope||Scope||
|LanguageFamily|MakeScope||Scope||
|LateralView|Vars||Context||
|Law|MakeScope||Scope||
|LawWithContextWrap|GetInternationalOrganization||InternationalOrganization||
|LawWithContextWrap|GetLaw||Law||
|LayerTreeItem|GetEntry||Type||
|LeaderCandidate|GetCandidate||Country||
|LevySetup|GetUnit||SubUnitType||
|LevySetup|MakeScope||Scope||
|Loan|GetBorrower||Country||
|Loan|GetLender||Country||
|Loan|MakeScope||Scope||
|LoanEntry|GetLoan||Loan||
|LoanEntry|GetRepayLoanUIAction||UIActionProvider||
|LobbyPlayer|GetLobbyView||LobbyView||
|LobbyPlayer|GetPlayable||Playable||
|LobbyView|AccessLocalPlayer||LobbyPlayer||
|LobbyView|AccessSelectedPlayable||Playable||
|LobbyView|GetSelectedPlayable||Playable||
|LobbyView|GetServerInfo||ServerInformation||
|Location|GetArea||Area||
|Location|GetBestFortBuilding||Building||
|Location|GetClimate||Climate||
|Location|GetClosestPort||Location||
|Location|GetCombat||Combat||
|Location|GetContinent||Continent||
|Location|GetController||Country||
|Location|GetDiseaseOutbreak|unknown|DiseaseOutbreak||
|Location|GetDominantCulture||Culture||
|Location|GetDominantDialect||Dialect||
|Location|GetDominantLanguage||Language||
|Location|GetDominantReligion||Religion||
|Location|GetListOfCountries||CountryListFromLocation||
|Location|GetLocation||Location||
|Location|GetMaritime||Maritime||
|Location|GetMarket||Market||
|Location|GetOwner||Country||
|Location|GetOwnerForMap||Country||
|Location|GetPopulation||Population||
|Location|GetPopulationChart||LocationPopulationChart||
|Location|GetPortSeaZone||Location||
|Location|GetProvince||Province||
|Location|GetProvinceDefinition||ProvinceDefinition||
|Location|GetQuickRebelLocationList||QuickRebelLocationList||
|Location|GetRank||LocationRank||
|Location|GetRawMaterial||Goods||
|Location|GetRegion||Region||
|Location|GetSiege||Siege||
|Location|GetSoundTollController||Location||
|Location|GetSpecificBaseModifier||StaticModifier||
|Location|GetSubContinent||SubContinent||
|Location|GetSupplyDepot||SupplyDepot||
|Location|GetTimedModifierOwner||TimedModifierOwner||
|Location|GetTopography||Topography||
|Location|GetUpgradeRGOConstructionDemand||GoodsDemand||
|Location|GetVegetation||Vegetation||
|Location|MakeScope||Scope||
|LocationBuildingItem|GetBuilding||Building||
|LocationBuildingItem|GetConstruction||Construction||
|LocationBuildingItem|GetRoadType||RoadType||
|LocationItem|GetLocation||Location||
|LocationPopItem|GetLocation||Location||
|LocationPopItem|GetType||PopType||
|LocationPopPieChartTooltipWidget|GetLocation||Location||
|LocationPopulationChart|GetPopsPiechartWidget||PopsPiechartWidget||
|LocationRank|MakeScope||Scope||
|LocationReference|GetLocation||Location||
|LocationToBuildItem|GetBuilding||Building||
|LocationToBuildItem|GetBuildingType||BuildingType||
|LocationToBuildItem|GetDequeueUIAction||UIActionProvider||
|LocationToBuildItem|GetLocation||Location||
|LocationToRecruitItem|GetConstruction||Construction||
|LocationToRecruitItem|GetLocation||Location||
|LocationToRecruitItem|GetMercenary||Mercenary||
|LocationToRecruitItem|GetUnitType||SubUnitType||
|LocationView|GetColonialCharter||ColonialCharterItem||
|LocationView|GetForeignCountry||Country||
|LocationView|GetHigherPresenceDisease||Disease||
|LocationView|GetLocation||Location||
|LocationView|GetPlayer||Country||
|LocationView|GetPopTypeItem|unknown|LocationPopItem||
|LocationView|GetRaisingArmyLevies||Construction||
|LocationView|GetRaisingNavyLevies||Construction||
|LocationView|GetRankUIAction||UIActionProvider||
|LocationView|GetRenameUIClickAction||UIClickAction||
|LocationView|GetUpgradeRGOConstructionDemand||GoodsDemand||
|LocationView|Manager||LateralView||
|LocationView|Vars||Context||
|LocationViewSelectProvince|Parent||LocationView||
|LocationsListView|GetLocationsListSortSearch||FilteredSortedList||
|LocationsListView|GetPlayer||Country||
|LocationsListView|Manager||LateralView||
|LocationsListView|Vars||Context||
|LocationsListViewItem|GetLocation||Location||
|LogViewer|GetLastLogEntry||LogViewerEntry||
|LogViewer|GetSelectedLogEntry||LogViewerEntry||
|MaintenanceSetting|GetSettingOwner||Country||
|ManageSubjectsLateralView|GetPlayer||Country||
|ManageSubjectsLateralView|GetSubjectRelationsSortSearch||FilteredSortedList||
|ManageSubjectsLateralView|Manager||LateralView||
|ManageSubjectsLateralView|Vars||Context||
|MapContentEditorViewport|GetTooltip||GuiEditorTooltip||
|MapEditor|AccessUndoHistoryViewerClient||UndoHistoryViewerClient||
|MapEditor|GetUndoHistoryViewerClient||UndoHistoryViewerClient||
|MapEditorGui|AccessLogViewer||LogViewer|Access Central Log Viewer|
|MapObjectPainterOptions|AccessBlurThresholdCtx||BlurThreshold||
|MapObjectTool|GetTooltip||GuiEditorTooltip||
|MapObjectTool|MoveTool||MoveTool||
|MapObjectTool|SelectTool||SelectTool||
|Maritime|GetLocation||Location||
|MaritimeInLocationWrap|GetCountry||Country||
|MaritimeInLocationWrap|GetLocation||Location||
|MaritimeInLocationWrap|GetPresence||MaritimePresence||
|MaritimeItem|GetPresence||MaritimePresence||
|MaritimeItem|GetSeaZone||Location||
|MaritimeLateralView|GetPlayer||Country||
|MaritimeLateralView|GetPrivateersSortSearch||FilteredSortedList||
|MaritimeLateralView|GetSeazonesSortSearch||FilteredSortedList||
|MaritimeLateralView|Manager||LateralView||
|MaritimeLateralView|Vars||Context||
|MaritimePresence|GetCountry||Country||
|MaritimePresence|GetOwner||Maritime||
|Market|GetCenterLocation||Location||
|Market|GetGoodsWithHighestSupplyAndValue||Goods||
|Market|GetLanguage||Language||
|Market|GetMarketEntry|unknown|GoodsMarketEntry||
|Market|GetOwner||Country||
|Market|MakeScope||Scope||
|MarketAccessWrap|GetLocation||Location||
|MarketAccessWrap|GetMarket||Market||
|MarketCountryNeeds|AccessMarket||Market||
|MarketCountryNeeds|GetMarket||Market||
|MarketMarker|GetLocation||Location||
|MarketViewSelectMarket|Parent||SelectedMarketLateralView||
|MarketingContainer|AccessSlotByName|unknown|MarketingSlot||
|MarketingContainer|GetSlotByName|unknown|MarketingSlot||
|MarketsView|GetMarketsItemsSortSearch||FilteredSortedList||
|MarketsView|GetPlayer||Country||
|MarketsView|Manager||LateralView||
|MarketsView|Vars||Context||
|MaskPainterViewport|GetTooltip||GuiEditorTooltip||
|MemberTypeItem|GetSpecialStatus||SpecialStatus||
|Mercenary|GetCustomer||Country||
|Mercenary|GetHomeLocation||Location||
|Mercenary|GetLeader||Character||
|Mercenary|GetOwner||Country||
|Mercenary|GetTimedModifierOwner||TimedModifierOwner||
|Mercenary|MakeScope||Scope||
|MercenaryItem|GetMercenary||Mercenary||
|MercenaryTypeItem|GetMercenary||Mercenary||
|MercenaryTypeItem|GetUIAction||UIActionProvider||
|Merchant|GetCountry||Country||
|Merchant|GetMarket||Market||
|MerchantCapacityInMarketWrap|GetCountry||Country||
|MerchantCapacityInMarketWrap|GetMarket||Market||
|MerchantPowerInMarketWrap|GetCountry||Country||
|MerchantPowerInMarketWrap|GetMarket||Market||
|MeshImporter|AccessMaterialImportSettings||MeshImporterMaterials||
|MeshImporter|AccessUndoer||UndoStack||
|MessagePopup|GetLockableInfo||LockableInfo||
|Migration|GetCulture||Culture||
|Migration|GetFrom||ProvinceDefinition||
|Migration|GetFromLocation||Location||
|Migration|GetPopType||PopType||
|Migration|GetReligion||Religion||
|Migration|GetTo||ProvinceDefinition||
|Migration|GetToLocation||Location||
|MilitaryObjectiveGroupView|AccessObjective||MilitaryObjective||
|MilitaryObjectiveGroupView|GetArmySortSearch||FilteredSortedList||
|MilitaryObjectiveGroupView|GetCommitAction||UIActionProvider||
|MilitaryObjectiveGroupView|GetGeographySortSearch||FilteredSortedList||
|MilitaryObjectiveGroupView|GetMilitaryObjectiveGroup||TacticalMilitaryObjectiveGroup||
|MilitaryObjectiveGroupView|GetNavySortSearch||FilteredSortedList||
|MilitaryObjectiveGroupView|GetObjective||MilitaryObjective||
|MilitaryObjectiveGroupView|GetSpecialOptionsSortSearch||FilteredSortedList||
|MilitaryObjectiveGroupsView|GetDefendHomeTerritoryUIAction||UIActionProvider||
|MilitaryObjectiveGroupsView|GetObjectiveTypesSortSearch||FilteredSortedList||
|MilitaryObjectiveGroupsView|GetPlayer||Country||
|MilitaryObjectiveGroupsView|GetRepatriateTroopsUIAction||UIActionProvider||
|MilitaryObjectiveGroupsView|Manager||LateralView||
|MilitaryObjectiveGroupsView|Vars||Context||
|MissionAlert|GetTask||MissionTaskDefinition||
|MissionDefinition|MakeScope||Scope||
|MissionItem|GetMission||MissionDefinition||
|MissionLateralView|GetActiveMission||MissionItem||
|MissionLateralView|GetPlayer||Country||
|MissionLateralView|Manager||LateralView||
|MissionLateralView|Vars||Context||
|MissionMessage|GetMission||MissionDefinition||
|MissionProgress|GetActiveMission||MissionDefinition||
|MissionProgress|GetCurrentMissionTask||MissionTaskDefinition||
|MissionTaskDefinition|GetMission||MissionDefinition||
|MissionTaskDefinition|MakeScope||Scope||
|MissionTaskItem|GetTask||MissionTaskDefinition||
|MissionTaskMessage|GetMissionTask||MissionTaskDefinition||
|MissionTasksLateralView|GetMissionItem||MissionItem||
|MissionTasksLateralView|GetPlayer||Country||
|MissionTasksLateralView|Manager||LateralView||
|MissionTasksLateralView|Vars||Context||
|ModifierDebugInspectorPlugin|GetScopeData||ModifierDebugData||
|ModifierSourceWrap|GetModifierType||ModifierType||
|ModsGui|ActivePlayset||ModsPlayset||
|ModsGui|GetPlayset|unknown|ModsPlayset||
|ModsPlaysetEntry|Playset||ModsPlayset||
|MultiUnitSelectUnit|Parent||MultiUnitWindow||
|MultiUnitWindow|GetFirstUnit||Unit||
|MultiUnitWindow|GetPlayer||Country||
|MultiUnitWindow|GetUnitsSortSearch||FilteredSortedList||
|MultiUnitWindow|Manager||LateralView||
|MultiUnitWindow|Vars||Context||
|MultiplayerSetupWindow|AccessMPConfig||MPConfig||
|MultiplayerSetupWindow|GetMPConfig||MPConfig||
|NavyConstructionMarker|GetConstruction||Construction||
|NewBornMessage|GetCharacter||Character||
|NewCountryCandidate|GetFormableCountry||FormableCountry||
|OngoingRelationCountry|GetCountry||Country||
|OosData|GetPlayable||Playable||
|OrgItem|GetOrg||InternationalOrganization||
|OutbreakItem|GetDiseaseOutbreak||DiseaseOutbreak||
|OutlinerCabinetEntry|GetActionProgressScope||TopScope||
|OutlinerDiplomacyEntry|GetTargetCountry||Country||
|OutlinerDiplomacyEntry|GetTemporaryRelationCountry||OngoingRelationCountry||
|OutlinerPlayerEntry|GetCountry||Country||
|OutlinerSettings|GetOutliner||Outliner||
|Parliament|GetCountryParliamentAgenda|unknown|ActiveParliamentAgenda||
|Parliament|GetCurrentDebate||ParliamentIssue||
|Parliament|GetOrganizationParliamentAgenda|unknown|ActiveParliamentAgenda||
|Parliament|GetParliamentLocation||Location||
|Parliament|GetParliamentType||ParliamentType||
|ParliamentAgenda|MakeScope||Scope||
|ParliamentAgendaGlue|GetParliamentAgenda||ActiveParliamentAgenda||
|ParliamentAgendaGlue|GetUIAction||UIActionProvider||
|ParliamentAgendaItem|GetAgenda||ActiveParliamentAgenda||
|ParliamentAgendaItem|GetType||EstateType||
|ParliamentAgendaItem|GetUIAction||UIActionProvider||
|ParliamentInSession|GetParliament||Parliament||
|ParliamentIssue|GetEstateType||EstateType||
|ParliamentIssue|GetSpecialStatus||SpecialStatus||
|ParliamentIssue|MakeScope||Scope||
|ParliamentIssueWithContextWrap|GetParliamentIssue||ParliamentIssue||
|ParliamentMarker|GetGovernment||Government||
|ParliamentType|MakeScope||Scope||
|Payment|GetPrice||Price||
|Payment|MakeScope||Scope||
|PaymentWithContextWrap|GetInternationalOrganization||InternationalOrganization||
|PaymentWithContextWrap|GetPayment||Payment||
|PdxAccount|GetInventory||AccountInventory||
|PdxGuiWidget|AccessChild|unknown|PdxGuiWidget||
|PdxGuiWidget|AccessParent||PdxGuiWidget||
|PdxGuiWidget|FindChild|unknown|PdxGuiWidget||
|PdxGuiWidget|FindParent|unknown|PdxGuiWidget||
|PdxGuiWidget|GfxVideoControl||PdxGuiGfxVideoControl||
|PdxSetting|GetSettingPromoted||PdxCoreSetting||
|PeaceOfferLateralView|GetAnnexTreaty||PeaceTreaty||
|PeaceOfferLateralView|GetCategoriesSortSearch||FilteredSortedList||
|PeaceOfferLateralView|GetGoldTreaty||PeaceOfferWarScoreTreatyGlue||
|PeaceOfferLateralView|GetPlayer||Country||
|PeaceOfferLateralView|GetSacrificeTreaty||PeaceOfferWarScoreTreatyGlue||
|PeaceOfferLateralView|GetSelectedParticipant||Country||
|PeaceOfferLateralView|GetWar||War||
|PeaceOfferLateralView|Manager||LateralView||
|PeaceOfferLateralView|Vars||Context||
|PeaceOfferLateralViewParticipant|GetCountry||Country||
|PeaceTreaty|GetInnerCategory||PeaceOfferCategory||
|PeaceTreaty|GetLocation||Location||
|PeaceTreaty|GetRelevantCountryToShowForUI||Country||
|PeopleDynastyItem|GetDynasty||Dynasty||
|PeoplePopItem|GetPop||Pop||
|PeopleRebelItem|GetRebel||Rebel||
|Periphora|GetCountry||Country||
|Periphora|GetDestination||Location||
|Periphora|GetIcon||WorkOfArt||
|Periphora|GetOrigin||Location||
|PinningManager|Collection|unknown|PinCollection||
|Playable|GetCountry||Country||
|Playable|GetJominiPlayableCountryRef||Country||
|PlayerEntryForChat|GetCountry||Country||
|PlayerModifiersLateralView|GetModifiersSortSearch||FilteredSortedList||
|PlayerModifiersLateralView|GetPlayer||Country||
|PlayerModifiersLateralView|Manager||LateralView||
|PlayerModifiersLateralView|Vars||Context||
|Policy|GetLaw||Law||
|Policy|MakeScope||Scope||
|PolicyWithContextWrap|GetInternationalOrganization||InternationalOrganization||
|PolicyWithContextWrap|GetPolicy||Policy||
|Pop|GetCulture||Culture||
|Pop|GetEstate||Estate||
|Pop|GetEstateType||EstateType||
|Pop|GetLocation||Location||
|Pop|GetOwner||Country||
|Pop|GetOwnerOrLocationOwner||Country||
|Pop|GetRebel||Rebel||
|Pop|GetReligion||Religion||
|Pop|GetType||PopType||
|Pop|MakeScope||Scope||
|PopCultureItem|GetCulture||Culture||
|PopEntry|GetCulture||Culture||
|PopEntry|GetReligion||Religion||
|PopPoliticsItem|GetLocation||Location||
|PopReligionItem|GetReligion||Religion||
|PopTaxItem|GetLocation||Location||
|PopType|MakeScope||Scope||
|PopTypeEntry|GetPopType||PopType||
|PopsCountryItem|GetCountry||Country||
|PopsLocationItem|GetLocation||Location||
|PopsOverview|GetPlayer||Country||
|PopsOverview|GetPopsSortSearch||FilteredSortedList||
|PopsOverview|Manager||LateralView||
|PopsOverview|Vars||Context||
|PopsProvinceItem|GetProvince||Province||
|PortMarker|GetLocation||Location||
|PortraitEditorWindow|GetChildGenerator||ChildGenerator||
|PortraitEditorWindow|GetPortraitDataContext||PortraitDataContext||
|PortraitEditorWindow|GetSelectedEthnicityItem||EthnicityItem||
|PortraitEditorWindow|GetSelectedGeneItem||GeneItem||
|PossibleDisease|GetDisease||Disease||
|PossibleExplorationItem|GetArea||Area||
|PossibleExplorationItem|GetCharacter||Character||
|PossibleExplorationItem|GetExploration||Exploration||
|PossibleExplorationItem|GetExplorationConstruction||Construction||
|PossibleItem|GetExistingTrade||Trade||
|PossibleItem|GetFromMarket||Market||
|PossibleItem|GetGoods||Goods||
|PossibleItem|GetMarket||Market||
|PossibleItem|GetToMarket||Market||
|PossibleLeaderItem|GetCharacter||Character||
|PossiblePrivateerItem|GetArea||Area||
|PossibleSubUnitDefinition|GetSubUnitDefinition||SubUnitType||
|PossibleTrade|GetExistingTrade||Trade||
|PossibleTrade|GetFromMarket||Market||
|PossibleTrade|GetGoods||Goods||
|PossibleTrade|GetMerchantMarket||Market||
|PossibleTrade|GetToMarket||Market||
|PossibleTrade|GetUIActions||UIActionProvider||
|PossibleTradesSelectMarket|Parent||TradeOverview||
|Price|MakeScope||Scope||
|Privateer|GetArea||Area||
|Privateer|GetOwner||Country||
|Privateer|MakeScope||Scope||
|PrivilegeItem|GetPrivilege||EstatePrivilege||
|PrivilegeItem|GetUIAction||UIActionProvider||
|ProducedOnMarketWrap|GetGoods||Goods||
|ProducedOnMarketWrap|GetMarket||Market||
|ProductionMethod|GetGoodsDemand||GoodsDemand||
|ProductionMethod|GetProduced||Goods||
|ProductionMethod|MakeScope||Scope||
|ProductionMethodItem|GetProductionMethod||ProductionMethod||
|ProductionSelectMarket|Parent||ProductionView||
|ProductionView|GetBestBuildLocation||Location||
|ProductionView|GetBuildRankingItems||ConstructScoreRanking||
|ProductionView|GetBuildingsSortSearch||FilteredSortedList||
|ProductionView|GetEstateBuildingsSortSearch||FilteredSortedList||
|ProductionView|GetForeignBuildingsSortSearch||FilteredSortedList||
|ProductionView|GetPlayer||Country||
|ProductionView|GetSelectedLocation||Location||
|ProductionView|GetSelectedMarket||Market||
|ProductionView|Manager||LateralView||
|ProductionView|Vars||Context||
|Province|FindFirstNonIntegrated||Location||
|Province|GetArea||Area||
|Province|GetCapital||Location||
|Province|GetContinent||Continent||
|Province|GetCountry||Country||
|Province|GetDefinition||ProvinceDefinition||
|Province|GetProvince||Province||
|Province|GetRegion||Region||
|Province|GetTimedModifierOwner||TimedModifierOwner||
|Province|MakeScope||Scope||
|ProvinceDefinition|GetArea||Area||
|ProvinceDefinition|MakeScope||Scope||
|QuickCabinetCardModifier|GetCabinetCardModifier||CabinetCardModifier||
|QuickDiplomaticActions|GetSpecificAction|unknown|DiplomaticActionItem||
|QuickTemporaryCountryRelations|GetTemporaryRelation|unknown|OngoingRelationCountry||
|QuickUnitActions|GetBalanceAction||UnitActionItem||
|RawGoodLocationItem|GetLocation||Location||
|RawGoodsMarker|GetLocation||Location||
|Rebel|GetMostPowerfulSupporter||Country||
|Rebel|GetOwner||Country||
|Rebel|GetPretender||Character||
|Rebel|MakeScope||Scope||
|RebelDetailsLateralView|GetLocationsSortSearch||FilteredSortedList||
|RebelDetailsLateralView|GetPlayer||Country||
|RebelDetailsLateralView|GetPopsSortSearch||FilteredSortedList||
|RebelDetailsLateralView|GetRebel||Rebel||
|RebelDetailsLateralView|Manager||LateralView||
|RebelDetailsLateralView|Vars||Context||
|RecruitInLocationLateralView|GetItem|unknown|LocationToRecruitItem||
|RecruitInLocationLateralView|GetMercenary||Mercenary||
|RecruitInLocationLateralView|GetPlayer||Country||
|RecruitInLocationLateralView|GetPreferredMethod||RecruitmentMethod||
|RecruitInLocationLateralView|GetRecruitSortSearch||FilteredSortedList||
|RecruitInLocationLateralView|GetUnitType||SubUnitType||
|RecruitInLocationLateralView|Manager||LateralView||
|RecruitInLocationLateralView|Vars||Context||
|RecruitScoreRanking|GetLastRecruitmentLocation||Location||
|RecruitScoreRanking|GetUnitType||SubUnitType||
|RecruitmentMethod|MakeScope||Scope||
|ReformItem|GetReform||GovernmentReform||
|ReformItem|GetUIAction||UIActionProvider||
|RegencyType|MakeScope||Scope||
|Region|GetSubContinent||SubContinent||
|Region|MakeScope||Scope||
|RelationDescItem|GetCountry||Country||
|RelationDescItem|GetRelationDescItemUIAction||UIActionProvider||
|RelationTypeItem|GetCountry||Country||
|RelationTypeItem|GetInternationalOrganization||InternationalOrganization||
|RelativePowerTooltipGlue|GetCountry||Country||
|RelativePowerTooltipGlue|GetPlayer||Country||
|Religion|GetCountriesList||QuickReligionCountryList||
|Religion|GetGroup||ReligionGroup||
|Religion|GetImportantCountry||Country||
|Religion|GetLanguage||Dialect||
|Religion|GetTimedModifierOwner||TimedModifierOwner||
|Religion|MakeScope||Scope||
|ReligionGroup|MakeScope||Scope||
|ReligionItem|GetReligion||Religion||
|ReligionMessage|GetReligion||Religion||
|ReligionsLedger|GetPlayer||Country||
|ReligionsLedger|GetReligionsSortSearch||FilteredSortedList||
|ReligionsLedger|Manager||LateralView||
|ReligionsLedger|Vars||Context||
|ReligiousAspect|MakeScope||Scope||
|ReligiousAspectGlue|GetReligiousAspect||ReligiousAspect||
|ReligiousFaction|MakeScope||Scope||
|ReligiousFactionActionGlue|GetUIAction||UIActionProvider||
|ReligiousFactionGlue|GetFaction||ReligiousFaction||
|ReligiousFigure|MakeScope||Scope||
|ReligiousFigureGlue|GetCharacter||Character||
|ReligiousFigureGlue|GetUIAction||UIActionProvider||
|ReligiousFocus|MakeScope||Scope||
|ReligiousFocusGlue|GetReligiousFocus||ReligiousFocus||
|ReligiousFocusGlue|GetUIAction||UIActionProvider||
|ReligiousSchool|MakeScope||Scope||
|RenameDialog|GetCountry||Country||
|ReorgWindow|GetLeft||Unit||
|ReorgWindow|GetRight||Unit||
|ReportIssueWindow|GetItemSortSearch||FilteredSortedList||
|ResearchMessage|GetAdvancePointer||Advance||
|Resolution|MakeScope||Scope||
|ResolutionGlue|GetEnactNoVoteTarget||InteractionTarget||
|ResolutionGlue|GetEnactResolution||Resolution||
|ResolutionGlue|GetEnactYesVoteTarget||InteractionTarget||
|ResolutionGlue|GetHighestVote||VoteGlue||
|ResolutionGlue|GetOwner||InternationalOrganization||
|ResolutionGlue|GetProposer||Country||
|ResolutionGlue|GetRepealResolution||Resolution||
|ResolutionGlue|GetSpecificParams||TargettedActionParameters||
|ResolutionGlue|GetTarget|unknown|InteractionTarget||
|ResolutionGlue|GetTargetCountry||Country||
|ResolutionGlue|GetVoteToEnactAction||UIActionProvider||
|ResolutionGlue|GetVoteToRepealAction||UIActionProvider||
|RoadBuilder|GetLocation||Location||
|RoadBuilder|GetPlayer||Country||
|RoadBuilder|GetRoadDestinationsSearch||FilteredSortedList||
|RoadBuilder|Manager||LateralView||
|RoadBuilder|Vars||Context||
|RoadDestinationItem|GetLocation||Location||
|RoadDestinationItem|GetRoadType||RoadType||
|RoadType|MakeScope||Scope||
|RoadTypeItem|GetRoadType||RoadType||
|RulerTerm|GetCharacterRulerData||CharacterRulerData||
|RulerTerm|GetCountryRulerData||CountryRulerData||
|RulerTerm|GetRuledCountry||Country||
|RulerTerm|GetRuledInternationalOrganization||InternationalOrganization||
|RulerTermEntry|GetRulerTerm||RulerTerm||
|RulerTraitEntry|GetCharacter||Character||
|RulerTraitEntry|GetTrait||Trait||
|RulingHistoryView|GetPlayer||Country||
|RulingHistoryView|GetRulerTermEntriesSortSearch||FilteredSortedList||
|RulingHistoryView|Manager||LateralView||
|RulingHistoryView|Vars||Context||
|SaintGlue|GetSaint||Character||
|SaveGameAnalysisView|GetSaveGame||SaveGame||
|ScaledStaticModifierWrap|GetModifier||StaticModifier||
|Scenario|GetProficiency||PlayerProficiency||
|SceneEditor|AccessUndoer||UndoStack||
|Scope|ActiveResolution||ActiveResolution|Jomini Script System|
|Scope|AdvanceType||AdvanceDefinition|Jomini Script System|
|Scope|Age||Age|Jomini Script System|
|Scope|Area||Area|Jomini Script System|
|Scope|Artist||Artist|Jomini Script System|
|Scope|Avatar||Avatar|Jomini Script System|
|Scope|Building||Building|Jomini Script System|
|Scope|BuildingType||BuildingType|Jomini Script System|
|Scope|Cabinet||Cabinet|Jomini Script System|
|Scope|Cardinal||Cardinal|Jomini Script System|
|Scope|CasusBelli||CasusBelli|Jomini Script System|
|Scope|Character||Character|Jomini Script System|
|Scope|CharacterInteraction||CharacterInteraction|Jomini Script System|
|Scope|ChildEducation||ChildEducation|Jomini Script System|
|Scope|Climate||Climate|Jomini Script System|
|Scope|ColonialCharter||ColonialCharter|Jomini Script System|
|Scope|Combat||Combat|Jomini Script System|
|Scope|CombatSide||CombatSide|Jomini Script System|
|Scope|Continent||Continent|Jomini Script System|
|Scope|Country||Country|Jomini Script System|
|Scope|CountryInteraction||CountryInteraction|Jomini Script System|
|Scope|CountryRank||CountryRank|Jomini Script System|
|Scope|Culture||Culture|Jomini Script System|
|Scope|CultureGroup||CultureGroup|Jomini Script System|
|Scope|DisasterType||DisasterType|Jomini Script System|
|Scope|Disease||Disease|Jomini Script System|
|Scope|DiseaseOutbreak||DiseaseOutbreak|Jomini Script System|
|Scope|Dynasty||Dynasty|Jomini Script System|
|Scope|EmploymentSystem||EmploymentSystem|Jomini Script System|
|Scope|Estate||Estate|Jomini Script System|
|Scope|EstateType||EstateType|Jomini Script System|
|Scope|Ethnicity||Ethnicity|Jomini Script System|
|Scope|Exploration||Exploration|Jomini Script System|
|Scope|Faction||ReligiousFaction|Jomini Script System|
|Scope|FormableCountry||FormableCountry|Jomini Script System|
|Scope|GenericAction||GenericAction|Jomini Script System|
|Scope|GetActiveResolution||ActiveResolution||
|Scope|GetAdvanceType||AdvanceDefinition||
|Scope|GetAge||Age||
|Scope|GetArea||Area||
|Scope|GetArtist||Artist||
|Scope|GetAvatar||Avatar||
|Scope|GetBuilding||Building||
|Scope|GetBuildingType||BuildingType||
|Scope|GetCabinet||Cabinet||
|Scope|GetCabinetAction||CabinetAction||
|Scope|GetCardinal||Cardinal||
|Scope|GetCasusBelli||CasusBelli||
|Scope|GetCharacter||Character||
|Scope|GetCharacterInteraction||CharacterInteraction||
|Scope|GetChildEducation||ChildEducation||
|Scope|GetClimate||Climate||
|Scope|GetColonialCharter||ColonialCharter||
|Scope|GetCombat||Combat||
|Scope|GetCombatSide||CombatSide||
|Scope|GetContinent||Continent||
|Scope|GetCountry||Country||
|Scope|GetCountryInteraction||CountryInteraction||
|Scope|GetCountryRank||CountryRank||
|Scope|GetCulture||Culture||
|Scope|GetCultureGroup||CultureGroup||
|Scope|GetDialect||Dialect||
|Scope|GetDisaster||Disaster||
|Scope|GetDisasterType||DisasterType||
|Scope|GetDisease||Disease||
|Scope|GetDiseaseOutbreak||DiseaseOutbreak||
|Scope|GetDynasty||Dynasty||
|Scope|GetEmploymentSystem||EmploymentSystem||
|Scope|GetEstate||Estate||
|Scope|GetEstatePrivilege||EstatePrivilege||
|Scope|GetEstateType||EstateType||
|Scope|GetEthnicity||Ethnicity||
|Scope|GetExploration||Exploration||
|Scope|GetFormableCountry||FormableCountry||
|Scope|GetGenericAction||GenericAction||
|Scope|GetGod||God||
|Scope|GetGoods||Goods||
|Scope|GetGoodsDemand||Goods||
|Scope|GetGovernmentReform||GovernmentReform||
|Scope|GetGovernmentType||GovernmentType||
|Scope|GetHegemony||Hegemony||
|Scope|GetHeirSelection||HeirSelection||
|Scope|GetHolySite||HolySite||
|Scope|GetHolySiteDefinition||HolySiteDefinition||
|Scope|GetHolySiteType||HolySiteType||
|Scope|GetInternationalOrganization||InternationalOrganization||
|Scope|GetInternationalOrganizationType||InternationalOrganizationType||
|Scope|GetLandOwnershipRule||LandOwnershipRule||
|Scope|GetLanguage||Language||
|Scope|GetLaw||Law||
|Scope|GetLevySetup||LevySetup||
|Scope|GetLoan||Loan||
|Scope|GetLocation||Location||
|Scope|GetLocationRank||LocationRank||
|Scope|GetMarket||Market||
|Scope|GetMercenary||Mercenary||
|Scope|GetMissionDefinition||MissionDefinition||
|Scope|GetMissionTaskDefinition||MissionTaskDefinition||
|Scope|GetParliamentAgenda||ParliamentAgenda||
|Scope|GetParliamentIssue||ParliamentIssue||
|Scope|GetParliamentType||ParliamentType||
|Scope|GetPayment||Payment||
|Scope|GetPolicy||Policy||
|Scope|GetPop||Pop||
|Scope|GetPopType||PopType||
|Scope|GetPrice||Price||
|Scope|GetPrivateer||Privateer||
|Scope|GetProductionMethod||ProductionMethod||
|Scope|GetProvince||Province||
|Scope|GetProvinceDefinition||ProvinceDefinition||
|Scope|GetRebel||Rebel||
|Scope|GetRecruitmentMethod||RecruitmentMethod||
|Scope|GetRegencyType||RegencyType||
|Scope|GetRegion||Region||
|Scope|GetRelationType||ScriptedRelationType||
|Scope|GetReligion||Religion||
|Scope|GetReligionGroup||ReligionGroup||
|Scope|GetReligiousAspect||ReligiousAspect||
|Scope|GetReligiousFaction||ReligiousFaction||
|Scope|GetReligiousFigure||ReligiousFigure||
|Scope|GetReligiousFocus||ReligiousFocus||
|Scope|GetReligiousSchool||ReligiousSchool||
|Scope|GetResolution||Resolution||
|Scope|GetRoadType||RoadType||
|Scope|GetScriptableHintDefinition||ScriptableHintDefinition||
|Scope|GetScriptedPeaceTreatyType||ScriptedPeaceTreatyType||
|Scope|GetSiege||Siege||
|Scope|GetSituation||Situation||
|Scope|GetSocietalValue||SocietalValue||
|Scope|GetSpecialStatus||SpecialStatus||
|Scope|GetSubContinent||SubContinent||
|Scope|GetSubUnit||SubUnit||
|Scope|GetSubUnitCategory||SubUnitCategory||
|Scope|GetSubjectMilitaryStance||SubjectMilitaryStance||
|Scope|GetSubjectType||SubjectType||
|Scope|GetTopography||Topography||
|Scope|GetTrade||Trade||
|Scope|GetTrait||Trait||
|Scope|GetUnit||Unit||
|Scope|GetUnitAbility||UnitAbility||
|Scope|GetUnitType||SubUnitType||
|Scope|GetVariable|unknown|Scope||
|Scope|GetVegetation||Vegetation||
|Scope|GetWar||War||
|Scope|GetWeatherSystem||WeatherSystem||
|Scope|GetWorkOfArt||WorkOfArt||
|Scope|GetWorkOfArtType||WorkOfArtType||
|Scope|God||God|Jomini Script System|
|Scope|Goods||Goods|Jomini Script System|
|Scope|GoodsDemand||GoodsDemand|Jomini Script System|
|Scope|GovernmentType||GovernmentType|Jomini Script System|
|Scope|Hegemony||Hegemony|Jomini Script System|
|Scope|HeirSelection||HeirSelection|Jomini Script System|
|Scope|HolySite||HolySite|Jomini Script System|
|Scope|HolySiteDefinition||HolySiteDefinition|Jomini Script System|
|Scope|HolySiteType||HolySiteType|Jomini Script System|
|Scope|Institution||Institution|Jomini Script System|
|Scope|InternationalOrganization||InternationalOrganization|Jomini Script System|
|Scope|InternationalOrganizationType||InternationalOrganizationType|Jomini Script System|
|Scope|LandOwnershipRule||LandOwnershipRule|Jomini Script System|
|Scope|Language||Language|Jomini Script System|
|Scope|LanguageFamily||LanguageFamily|Jomini Script System|
|Scope|Law||Law|Jomini Script System|
|Scope|LevySetup||LevySetup|Jomini Script System|
|Scope|Loan||Loan|Jomini Script System|
|Scope|Location||Location|Jomini Script System|
|Scope|LocationRank||LocationRank|Jomini Script System|
|Scope|Market||Market|Jomini Script System|
|Scope|Mercenary||Mercenary|Jomini Script System|
|Scope|MissionDefinition||MissionDefinition|Jomini Script System|
|Scope|MissionTaskDefinition||MissionTaskDefinition|Jomini Script System|
|Scope|ParliamenType||ParliamentType|Jomini Script System|
|Scope|ParliamentAgenda||ParliamentAgenda|Jomini Script System|
|Scope|ParliamentIssue||ParliamentIssue|Jomini Script System|
|Scope|Payment||Payment|Jomini Script System|
|Scope|Policy||Policy|Jomini Script System|
|Scope|Pop||Pop|Jomini Script System|
|Scope|PopType||PopType|Jomini Script System|
|Scope|Price||Price|Jomini Script System|
|Scope|Privateer||Privateer|Jomini Script System|
|Scope|ProductionMethod||ProductionMethod|Jomini Script System|
|Scope|Province||Province|Jomini Script System|
|Scope|ProvinceDefinition||ProvinceDefinition|Jomini Script System|
|Scope|Rebel||Rebel|Jomini Script System|
|Scope|RecruitmentMethod||RecruitmentMethod|Jomini Script System|
|Scope|RegencyType||RegencyType|Jomini Script System|
|Scope|Region||Region|Jomini Script System|
|Scope|RelationType||ScriptedRelationType|Jomini Script System|
|Scope|Religion||Religion|Jomini Script System|
|Scope|ReligionGroup||ReligionGroup|Jomini Script System|
|Scope|ReligiousAspect||ReligiousAspect|Jomini Script System|
|Scope|ReligiousFigure||ReligiousFigure|Jomini Script System|
|Scope|ReligiousFocus||ReligiousFocus|Jomini Script System|
|Scope|ReligiousSchool||ReligiousSchool|Jomini Script System|
|Scope|Resolution||Resolution|Jomini Script System|
|Scope|RoadType||RoadType|Jomini Script System|
|Scope|ScriptableHintDefinition||ScriptableHintDefinition|Jomini Script System|
|Scope|ScriptedPeaceTreatyType||ScriptedPeaceTreatyType|Jomini Script System|
|Scope|Siege||Siege|Jomini Script System|
|Scope|Situation||Situation|Jomini Script System|
|Scope|SocietalValue||SocietalValue|Jomini Script System|
|Scope|SpecialStatus||SpecialStatus|Jomini Script System|
|Scope|SubContinent||SubContinent|Jomini Script System|
|Scope|SubUnit||SubUnit|Jomini Script System|
|Scope|SubUnitCategory||SubUnitCategory|Jomini Script System|
|Scope|SubjectMilitaryStance||SubjectMilitaryStance|Jomini Script System|
|Scope|SubjectType||SubjectType|Jomini Script System|
|Scope|Topography||Topography|Jomini Script System|
|Scope|Trade||Trade|Jomini Script System|
|Scope|Trait||Trait|Jomini Script System|
|Scope|Unit||Unit|Jomini Script System|
|Scope|UnitAbility||UnitAbility|Jomini Script System|
|Scope|UnitType||SubUnitType|Jomini Script System|
|Scope|Var|unknown|Scope||
|Scope|Vegetation||Vegetation|Jomini Script System|
|Scope|War||War|Jomini Script System|
|Scope|WeatherSystem||WeatherSystem|Jomini Script System|
|Scope|WorkOfArt||WorkOfArt|Jomini Script System|
|Scope|WorkOfArtType||WorkOfArtType|Jomini Script System|
|ScopeDebugInspectorPlugin|GetScopeData||ScopeDebugData||
|ScopedEditorSettingsCategory|AccessCategory||EditorSettingCategory||
|ScopedEditorSettingsCategory|GetCategory||EditorSettingCategory||
|ScoreView|GetPlayer||Country||
|ScoreView|GetScoreSortSearch||FilteredSortedList||
|ScoreView|Manager||LateralView||
|ScoreView|Vars||Context||
|ScoreViewItem|GetCountry||Country||
|ScriptProfilerGui|GetCurrentEntry||ScriptProfilerEntry||
|ScriptProfilerGui|GetFileSearchList||ToolPropertySearchList||
|ScriptProfilerGui|GetModeSearchList||ToolPropertySearchList||
|ScriptRunnerInspector|AccessEffectResult||ScriptRunnerResult||
|ScriptRunnerInspector|AccessEventTargets||EventTargetSetupContext||
|ScriptRunnerInspector|AccessTriggerResult||ScriptRunnerResult||
|ScriptableHintDefinition|GetPlaystyleHint|unknown|PlaystyleHint||
|ScriptableHintDefinition|MakeScope||Scope||
|ScriptedHintItem|GetHint||ScriptableHintDefinition||
|ScriptedPeaceTreatyType|MakeScope||Scope||
|ScriptedRelationType|MakeScope||Scope||
|ScriptedRelationTypeWithContextWrap|GetFirstCountry||Country||
|ScriptedRelationTypeWithContextWrap|GetScriptedRelationType||ScriptedRelationType||
|ScriptedRelationTypeWithContextWrap|GetSecondCountry||Country||
|SeaZoneView|GetLocation||Location||
|SeaZoneView|GetPlayer||Country||
|SeaZoneView|Manager||LateralView||
|SeaZoneView|Vars||Context||
|SearchBar|Manager||LateralView||
|SearchFilter|GetRange||SearchFilterRange||
|SearchFilterCategory|AccessRangeValues|unknown|SearchFilterRangeValues||
|SelectCasusBelli|GetCasusBelli||CasusBelli||
|SelectCasusBelli|GetPriceImpactFromWar||WarImpactWrap||
|SelectCasusBelli|GetWarGoal||WarGoal||
|SelectCharacterInteraction|GetCharacter||Character||
|SelectChildEducation|GetPlayer||Country||
|SelectChildEducation|Manager||LateralView||
|SelectChildEducation|Vars||Context||
|SelectCountryDiplomacyLateralView|GetCountriesSortSearch||FilteredSortedList||
|SelectCountryDiplomacyLateralView|GetPlayer||Country||
|SelectCountryDiplomacyLateralView|Manager||LateralView||
|SelectCountryDiplomacyLateralView|Vars||Context||
|SelectCreateCasusBelliWindow|GetExistingCBSortSearch||FilteredSortedList||
|SelectCreateCasusBelliWindow|GetPlayer||Country||
|SelectCreateCasusBelliWindow|GetPossibleCBSortSearch||FilteredSortedList||
|SelectCreateCasusBelliWindow|Manager||LateralView||
|SelectCreateCasusBelliWindow|Vars||Context||
|SelectHeirSelection|GetCurrentCandidate||HeirSelectionCandidate||
|SelectInteractionTargetGlue|GetObject||InteractionTarget||
|SelectInteractionTargetGlue|GetParent||SelectInteractionTargetView||
|SelectInteractionTargetView|GetCurrentParams||TargettedActionParameters||
|SelectInteractionTargetView|GetCurrentValueUIAction||UIActionProvider||
|SelectInteractionTargetView|GetPlayer||Country||
|SelectInteractionTargetView|GetTargetObjectSortSearch||FilteredSortedList||
|SelectInteractionTargetView|GetValueGlue|unknown|SelectInteractionTargetGlue||
|SelectInteractionTargetView|Manager||LateralView||
|SelectInteractionTargetView|Vars||Context||
|SelectLoanLateralView|GetDeclareBankruptcyUIAction||UIActionProvider||
|SelectLoanLateralView|GetLoansGivenSortSearch||FilteredSortedList||
|SelectLoanLateralView|GetLoansTakenSortSearch||FilteredSortedList||
|SelectLoanLateralView|GetPlayer||Country||
|SelectLoanLateralView|GetRepayAllLoansUIAction||UIActionProvider||
|SelectLoanLateralView|GetRepayAllPossibleLoansUIAction||UIActionProvider||
|SelectLoanLateralView|Manager||LateralView||
|SelectLoanLateralView|Vars||Context||
|SelectMissionLateralView|GetActiveMission||MissionItem||
|SelectMissionLateralView|GetAvailableMissionsSortSearch||FilteredSortedList||
|SelectMissionLateralView|GetPlayer||Country||
|SelectMissionLateralView|Manager||LateralView||
|SelectMissionLateralView|Vars||Context||
|SelectParticipant|Parent||PeaceOfferLateralView||
|SelectSearchFilter|AccessSearchBar||SearchBar||
|SelectSocietalValue|GetCabinet||Cabinet||
|SelectSubjectTypeLateralView|GetPlayer||Country||
|SelectSubjectTypeLateralView|GetSubjectTypesSortSearch||FilteredSortedList||
|SelectSubjectTypeLateralView|Manager||LateralView||
|SelectSubjectTypeLateralView|Vars||Context||
|SelectedMarketLateralView|GetFoodSourcesSortSearch||FilteredSortedList||
|SelectedMarketLateralView|GetGoodsMarketEntriesSortSearch||FilteredSortedList||
|SelectedMarketLateralView|GetMarket||Market||
|SelectedMarketLateralView|GetMerchantsSortSearch||FilteredSortedList||
|SelectedMarketLateralView|GetPlayer||Country||
|SelectedMarketLateralView|GetTradeMarketEntriesSortSearch||FilteredSortedList||
|SelectedMarketLateralView|Manager||LateralView||
|SelectedMarketLateralView|Vars||Context||
|SetupCondottieriView|GetCondottieriItemsSortSearch||FilteredSortedList||
|SetupCondottieriView|GetPlayer||Country||
|SetupCondottieriView|Manager||LateralView||
|SetupCondottieriView|Vars||Context||
|SetupEditor|GetSearch||SearchBar||
|SetupMercenaryRequirementsView|GetPossibleLeadersSortSearch||FilteredSortedList||
|SetupMercenaryRequirementsView|GetSelectedLeader||PossibleLeaderItem||
|Siege|GetBesieger||Country||
|Siege|GetCommander||Character||
|Siege|GetLocation||Location||
|Siege|GetSiegeDefender||Country||
|Siege|GetWar||War||
|Siege|MakeScope||Scope||
|SingleUnitSelectUnit|Parent||SingleUnitWindow||
|SingleUnitWindow|AccessSelectedUnit||Unit||
|SingleUnitWindow|GetBalanceAction||UnitActionItem||
|SingleUnitWindow|GetCreateUnitAction||UnitActionItem||
|SingleUnitWindow|GetDetachAction|unknown|UnitActionItem||
|SingleUnitWindow|GetEmbarkAction||UIActionProvider||
|SingleUnitWindow|GetMercenariesAction||UIActionProvider||
|SingleUnitWindow|GetObjectiveAction||UIActionProvider||
|SingleUnitWindow|GetPlayer||Country||
|SingleUnitWindow|GetSelectedUnit||Unit||
|SingleUnitWindow|GetSubUnitsSortSearch||FilteredSortedList||
|SingleUnitWindow|GetUIAction||UIActionProvider||
|SingleUnitWindow|Manager||LateralView||
|SingleUnitWindow|Vars||Context||
|Situation|MakeScope||Scope||
|SituationMessagePopup|GetCountry||Country||
|SituationMessagePopup|GetSituation||Situation||
|SituationView|GetAbstentionTarget||VoteTargetGlue||
|SituationView|GetActiveResolution||ActiveResolution||
|SituationView|GetActiveSituation||ActiveSituation||
|SituationView|GetInternationalOrganization||InternationalOrganization||
|SituationView|GetInternationalOrganizationForLaws||InternationalOrganization||
|SituationView|GetLawCategoriesSortSearch||FilteredSortedList||
|SituationView|GetPlayer||Country||
|SituationView|GetVoteTargetLeft||VoteTargetGlue||
|SituationView|GetVoteTargetRight||VoteTargetGlue||
|SituationView|Manager||LateralView||
|SituationView|Vars||Context||
|SocietalValue|MakeScope||Scope||
|SocietalValueCandidate|GetSocietalValue||SocietalValue||
|SocietalValueItem|GetCountry||Country||
|SocietalValueItem|GetLeftUIAction||UIActionProvider||
|SocietalValueItem|GetRightUIAction||UIActionProvider||
|SocietalValueItem|GetType||SocietalValue||
|SocietalValueRequirement|GetSocietalValue||SocietalValue||
|SocietalValuesLateralView|GetPlayer||Country||
|SocietalValuesLateralView|Manager||LateralView||
|SocietalValuesLateralView|Vars||Context||
|SpecialStatus|MakeScope||Scope||
|SpecificGoodsOnMarketWrap|GetGoods||Goods||
|SpecificGoodsOnMarketWrap|GetMarket||Market||
|StaticModifier|GetModifier||DatabaseModifier||
|StrategicMilitaryObjectiveGlue|GetGroup||StrategicMilitaryObjectiveGroup||
|StrategicMilitaryObjectiveGlue|GetObjective||StrategicMilitaryObjective||
|StrategicMilitaryObjectiveGroup|GetCountry||Country||
|StrategicMilitaryObjectiveGroup|GetObjective||StrategicMilitaryObjective||
|StrategicObjectiveGroupGlue|GetObjectiveGroup||StrategicMilitaryObjectiveGroup||
|SubContinent|GetContinent||Continent||
|SubContinent|MakeScope||Scope||
|SubUnit|GetController||Country||
|SubUnit|GetDefinition||SubUnitType||
|SubUnit|GetHome||Location||
|SubUnit|GetMercenary||Mercenary||
|SubUnit|GetOwner||Country||
|SubUnit|GetUnit||Unit||
|SubUnit|GetUnitBox||SubUnitArray||
|SubUnit|MakeScope||Scope||
|SubUnitArray|GetUnit||Unit||
|SubUnitCategory|GetConstructionDemand||GoodsDemand||
|SubUnitCategory|GetMaintenanceDemand||GoodsDemand||
|SubUnitCategory|MakeScope||Scope||
|SubUnitCombatCounts|GetCategory||SubUnitCategory||
|SubUnitCount|GetSubUnitDefinition||SubUnitType||
|SubUnitCounts|GetCategory||SubUnitCategory||
|SubUnitType|GetAge||Age||
|SubUnitType|GetCategory||SubUnitCategory||
|SubUnitType|GetConstructionDemand||GoodsDemand||
|SubUnitType|GetMaintenanceDemand||GoodsDemand||
|SubUnitType|MakeScope||Scope||
|SubjectItem|GetCountry||Country||
|SubjectItem|GetProvince||Province||
|SubjectItem|GetRegion||Region||
|SubjectMilitaryStance|MakeScope||Scope||
|SubjectType|GetSubjectPays||Price||
|SubjectType|MakeScope||Scope||
|SubjectTypeItem|GetSubjectType||SubjectType||
|SupplyDepot|GetFood||FoodOwner||
|SupplyDepot|GetLocation||Location||
|SupplyDepot|GetOwner||Country||
|SupplyDepotMarker|GetLocation||Location||
|SupplyOnMarketWrap|GetGoods||Goods||
|SupplyOnMarketWrap|GetMarket||Market||
|SupportRebelLateralView|GetPlayer||Country||
|SupportRebelLateralView|Manager||LateralView||
|SupportRebelLateralView|Vars||Context||
|TacticalMilitaryObjectiveGroup|GetCountry||Country||
|TacticalMilitaryObjectiveGroup|GetObjective||MilitaryObjective||
|TacticalObjectiveGroupGlue|GetArmyRecruitmentDesired||ArmyStrength||
|TacticalObjectiveGroupGlue|GetArmyRecruitmentNeeded||ArmyStrength||
|TacticalObjectiveGroupGlue|GetNavyRecruitmentDesired||NavyStrength||
|TacticalObjectiveGroupGlue|GetNavyRecruitmentNeeded||NavyStrength||
|TacticalObjectiveGroupGlue|GetObjectiveGroup||TacticalMilitaryObjectiveGroup||
|TacticalObjectiveGroupGlue|GetTotalUnitsArmyStrength||ArmyStrength||
|TacticalObjectiveGroupGlue|GetTotalUnitsNavyStrength||NavyStrength||
|TargettedActionParameters|GetActor||Country||
|TargettedActionParameters|GetFirstObjectOfType|unknown|InteractionTarget||
|TargettedActionParameters|GetProposer||Country||
|TargettedActionParameters|GetRecipient||InteractionTarget||
|TargettedActionParameters|GetTargetObjectFromFlag|unknown|InteractionTarget||
|TaxRateSetting|GetEstate||Estate||
|TechnologyLateralView|GetAutocompleteFromKey|unknown|Advance||
|TechnologyLateralView|GetPlayer||Country||
|TechnologyLateralView|GetSearchBar||SearchBar||
|TechnologyLateralView|GetSelectedAgeTechTree||TechTreeOneAge||
|TechnologyLateralView|Manager||LateralView||
|TechnologyLateralView|Vars||Context||
|TemporaryDemand|GetDemand||GoodsDemand||
|TextSearchFilter|GetFilter||SearchFilter||
|ThreatenTarget|GetLocation||Location||
|TickTaskDetailsView|GetTickTask||TickTaskData||
|TickTaskGraphItem|AccessTickTask||TickTaskData||
|TickTaskGraphItem|GetTickTask||TickTaskData||
|TimedModifier|GetModifier||DatabaseModifier||
|TollMarker|GetLocation||Location||
|TopScope|AddList|unknown unknown|TopScope||
|TopScope|AddScope|unknown unknown|TopScope||
|TopScope|GetLocalVariable|unknown|Scope||
|TopScope|GetRootScope||Scope||
|TopScope|SetRoot|unknown|TopScope||
|TopScope|sActiveResolution|unknown|ActiveResolution||
|TopScope|sAdvanceType|unknown|AdvanceDefinition||
|TopScope|sAge|unknown|Age||
|TopScope|sArea|unknown|Area||
|TopScope|sArtist|unknown|Artist||
|TopScope|sAudioCulture|unknown|AudioCultureType||
|TopScope|sAvatar|unknown|Avatar||
|TopScope|sBuildingType|unknown|BuildingType||
|TopScope|sCabinet|unknown|Cabinet||
|TopScope|sCabinetAction|unknown|CabinetAction||
|TopScope|sCardinal|unknown|Cardinal||
|TopScope|sCasusBelli|unknown|CasusBelli||
|TopScope|sCharacter|unknown|Character||
|TopScope|sCharacterInteraction|unknown|CharacterInteraction||
|TopScope|sChildEducation|unknown|ChildEducation||
|TopScope|sClimate|unknown|Climate||
|TopScope|sColonialCharter|unknown|ColonialCharter||
|TopScope|sCombat|unknown|Combat||
|TopScope|sCombatSide|unknown|CombatSide||
|TopScope|sContinent|unknown|Continent||
|TopScope|sCountry|unknown|Country||
|TopScope|sCountryInteraction|unknown|CountryInteraction||
|TopScope|sCountryRank|unknown|CountryRank||
|TopScope|sCulture|unknown|Culture||
|TopScope|sDialect|unknown|Dialect||
|TopScope|sDisaster|unknown|Disaster||
|TopScope|sDisasterType|unknown|DisasterType||
|TopScope|sDisease|unknown|Disease||
|TopScope|sDiseaseOutbreak|unknown|DiseaseOutbreak||
|TopScope|sDynasty|unknown|Dynasty||
|TopScope|sEmploymentSystem|unknown|EmploymentSystem||
|TopScope|sEstate|unknown|Estate||
|TopScope|sEstatePrivilege|unknown|EstatePrivilege||
|TopScope|sEstateType|unknown|EstateType||
|TopScope|sEthnicity|unknown|Ethnicity||
|TopScope|sExploration|unknown|Exploration||
|TopScope|sFormableCountry|unknown|FormableCountry||
|TopScope|sGenericAction|unknown|GenericAction||
|TopScope|sGod|unknown|God||
|TopScope|sGoods|unknown|Goods||
|TopScope|sGoodsDemand|unknown|GoodsDemand||
|TopScope|sGovernmentReform|unknown|GovernmentReform||
|TopScope|sGovernmentType|unknown|GovernmentType||
|TopScope|sGraphicalCulture|unknown|GraphicalCultureType||
|TopScope|sHegemony|unknown|Hegemony||
|TopScope|sHeirSelection|unknown|HeirSelection||
|TopScope|sHolySite|unknown|HolySite||
|TopScope|sHolySiteDefinition|unknown|HolySiteDefinition||
|TopScope|sHolySiteType|unknown|HolySiteType||
|TopScope|sInstitution|unknown|Institution||
|TopScope|sInternationalOrganization|unknown|InternationalOrganization||
|TopScope|sInternationalOrganizationType|unknown|InternationalOrganizationType||
|TopScope|sLandOwnershipRule|unknown|LandOwnershipRule||
|TopScope|sLanguage|unknown|Language||
|TopScope|sLanguageFamily|unknown|LanguageFamily||
|TopScope|sLaw|unknown|Law||
|TopScope|sLevySetup|unknown|LevySetup||
|TopScope|sLoan|unknown|Loan||
|TopScope|sLocation|unknown|Location||
|TopScope|sLocationRank|unknown|LocationRank||
|TopScope|sMarket|unknown|Market||
|TopScope|sMercenary|unknown|Mercenary||
|TopScope|sMissionDefinition|unknown|MissionDefinition||
|TopScope|sMissionTaskDefinition|unknown|MissionTaskDefinition||
|TopScope|sParliamentAgenda|unknown|ParliamentAgenda||
|TopScope|sParliamentIssue|unknown|ParliamentIssue||
|TopScope|sParliamentType|unknown|ParliamentType||
|TopScope|sPayment|unknown|Payment||
|TopScope|sPolicy|unknown|Policy||
|TopScope|sPop|unknown|Pop||
|TopScope|sPopType|unknown|PopType||
|TopScope|sPrice|unknown|Price||
|TopScope|sPrivateer|unknown|Privateer||
|TopScope|sProductionMethod|unknown|ProductionMethod||
|TopScope|sProvince|unknown|Province||
|TopScope|sProvinceDefinition|unknown|ProvinceDefinition||
|TopScope|sRebel|unknown|Rebel||
|TopScope|sRecruitmentMethod|unknown|RecruitmentMethod||
|TopScope|sRegencyType|unknown|RegencyType||
|TopScope|sRegion|unknown|Region||
|TopScope|sRelationType|unknown|ScriptedRelationType||
|TopScope|sReligion|unknown|Religion||
|TopScope|sReligionGroup|unknown|ReligionGroup||
|TopScope|sReligiousAspect|unknown|ReligiousAspect||
|TopScope|sReligiousFaction|unknown|ReligiousFaction||
|TopScope|sReligiousFigure|unknown|ReligiousFigure||
|TopScope|sReligiousFocus|unknown|ReligiousFocus||
|TopScope|sReligiousSchool|unknown|ReligiousSchool||
|TopScope|sResolution|unknown|Resolution||
|TopScope|sRoadType|unknown|RoadType||
|TopScope|sScriptableHintDefinition|unknown|ScriptableHintDefinition||
|TopScope|sScriptedPeaceTreatyType|unknown|ScriptedPeaceTreatyType||
|TopScope|sSiege|unknown|Siege||
|TopScope|sSituation|unknown|Situation||
|TopScope|sSocietalValue|unknown|SocietalValue||
|TopScope|sSpecialStatus|unknown|SpecialStatus||
|TopScope|sSubContinent|unknown|SubContinent||
|TopScope|sSubUnit|unknown|SubUnit||
|TopScope|sSubUnitCategory|unknown|SubUnitCategory||
|TopScope|sSubjectMilitaryStance|unknown|SubjectMilitaryStance||
|TopScope|sSubjectType|unknown|SubjectType||
|TopScope|sTopography|unknown|Topography||
|TopScope|sTrade|unknown|Trade||
|TopScope|sTrait|unknown|Trait||
|TopScope|sUnit|unknown|Unit||
|TopScope|sUnitAbility|unknown|UnitAbility||
|TopScope|sUnitType|unknown|SubUnitType||
|TopScope|sVegetation|unknown|Vegetation||
|TopScope|sWar|unknown|War||
|TopScope|sWeatherSystem|unknown|WeatherSystem||
|TopScope|sWorkOfArt|unknown|WorkOfArt||
|TopScope|sWorkOfArtType|unknown|WorkOfArtType||
|Topography|MakeScope||Scope||
|Trade|GetCapacityMarket||Market||
|Trade|GetFromMarket||Market||
|Trade|GetFromPort||Location||
|Trade|GetGoods||Goods||
|Trade|GetOwner||Country||
|Trade|GetSoundToll||Location||
|Trade|GetToMarket||Market||
|Trade|GetToPort||Location||
|Trade|MakeScope||Scope||
|TradeDetailsLateralView|GetPlayer||Country||
|TradeDetailsLateralView|GetTrade||Trade||
|TradeDetailsLateralView|GetUIAction||UIActionProvider||
|TradeDetailsLateralView|Manager||LateralView||
|TradeDetailsLateralView|Vars||Context||
|TradeOverview|GetCurrentNeedsSortSearch||FilteredSortedList||
|TradeOverview|GetMarketsSortSearch||FilteredSortedList||
|TradeOverview|GetPlayer||Country||
|TradeOverview|GetSelectedMarket||Market||
|TradeOverview|GetTradeCategoriesSortSearch||FilteredSortedList||
|TradeOverview|Manager||LateralView||
|TradeOverview|Vars||Context||
|TradePathItem|GetLocation||Location||
|TradesWrap|GetSelectedTrade||Trade||
|Trait|GetFlavor||TraitCategory||
|Trait|MakeScope||Scope||
|TransactionProportion|GetEntity||InteractionTarget||
|TransferUnit|GetSubUnit||SubUnit||
|TransferUnit|GetTarget||Unit||
|TransferUnitType|GetCountsCache||SubUnitCounts||
|TransferUnitType|GetTarget||Unit||
|UIMessage|GetBattleResult||BattleResult||
|UIMessage|GetCharacter||Character||
|UIMessage|GetCombat||Combat||
|UIMessage|GetFirstTag||Country||
|UIMessage|GetGoods||Goods||
|UIMessage|GetInstitution||Institution||
|UIMessage|GetInternationalOrganization||InternationalOrganization||
|UIMessage|GetMissionDefinition||MissionDefinition||
|UIMessage|GetMissionTaskDefinition||MissionTaskDefinition||
|UIMessage|GetReligion||Religion||
|UIMessage|GetSecondaryTag||Country||
|UIMessage|GetSiege||Siege||
|UIMessage|GetSituation||Situation||
|UIMessage|GetUnit||Unit||
|UniqueContentItem|GetAdvanceDefinition||AdvanceDefinition||
|UniqueContentItem|GetAge||Age||
|UniqueContentItem|GetBuildingType||BuildingType||
|UniqueContentItem|GetCabinetAction||CabinetAction||
|UniqueContentItem|GetCountryInteraction||CountryInteraction||
|UniqueContentItem|GetEstatePrivilege||EstatePrivilege||
|UniqueContentItem|GetGovernmentReform||GovernmentReform||
|UniqueContentItem|GetLaw||Law||
|UniqueContentItem|GetLevySetup||LevySetup||
|UniqueContentItem|GetSubUnitDef||SubUnitType||
|Unit|GetActivity||UnitActivity||
|Unit|GetCombat||Combat||
|Unit|GetCommander||Character||
|Unit|GetCountry||Country||
|Unit|GetFirstUnitOnBoard||Unit||
|Unit|GetLoadedOn||Unit||
|Unit|GetLocation||Location||
|Unit|GetObjectiveGroup||TacticalMilitaryObjectiveGroup||
|Unit|GetQuickUnitActions||QuickUnitActions||
|Unit|GetSiege||Siege||
|Unit|GetSupplySource||Location||
|Unit|GetTimedModifierOwner||TimedModifierOwner||
|Unit|GetUnitBox|unknown|SubUnitArray||
|Unit|GetVisualSubunit||SubUnit||
|Unit|MakeScope||Scope||
|UnitAbility|MakeScope||Scope||
|UnitActionItem|GetAbility||UnitAbility||
|UnitDetailsView|GetUnit||Unit||
|UnitGlue|AccessUnit||Unit||
|UnitGlue|GetSelectAction||UIActionProvider||
|UnitGlue|GetUnit||Unit||
|UnitItem|AccessUnit||Unit||
|UnitItem|GetUICommanderAction||UIActionProvider||
|UnitItem|GetUIHeaderAction||UIActionProvider||
|UnitItem|GetUnit||Unit||
|UnitMarker|GetLeadingUnit||Unit||
|UnitMarker|GetSiege||Siege||
|UnitMarkerItem|GetCountry||Country||
|UnitMarkerItem|GetMilitaryObjectiveGroup||TacticalMilitaryObjectiveGroup||
|UnitMarkerItem|GetQuickUnitActions||QuickUnitActions||
|UnitMarkerItem|GetUnit||Unit||
|UnitOverview|GetArmyUnitsSortSearch||FilteredSortedList||
|UnitOverview|GetNavyUnitsSortSearch||FilteredSortedList||
|UnitOverview|GetPlayer||Country||
|UnitOverview|GetRecruitArmyUIAction||UIActionProvider||
|UnitOverview|GetRecruitNavyUIAction||UIActionProvider||
|UnitOverview|GetSelectObjectiveArmyAction||UnitActionItem||
|UnitOverview|GetSelectObjectiveNavyAction||UnitActionItem||
|UnitOverview|Manager||LateralView||
|UnitOverview|Vars||Context||
|UnitSuppliesWrap|GetSelectedUnit||Unit||
|UnitTransportStateBag|GetArmyDisembarkLocation||Location||
|UnitTransportStateBag|GetArmyEmbarkLocation||Location||
|UnitTransportStateBag|GetShipDisembarkLocation||Location||
|UnitTransportStateBag|GetShipEmbarkLocation||Location||
|UnitTypeItem|GetUnitType||SubUnitType||
|UnitTypeLateralView|GetPlayer||Country||
|UnitTypeLateralView|GetUnitType||SubUnitType||
|UnitTypeLateralView|Manager||LateralView||
|UnitTypeLateralView|Vars||Context||
|UnitsWrap|GetSelectedUnit||Unit||
|UnprofitableBuildingsEntry|GetMarket||Market||
|VariableEntry|AccessScopeEditor||ScopeObjectEditor||
|VariableInspectorEntry|AccessVariable||VariableInspectorVariable||
|VariableInspectorPlugin|AccessSetupVariable||VariableInspectorVariable||
|VariableInspectorVariable|AccessScopeEditor||ScopeObjectEditor||
|VariableListEntry|AccessScopeEditor||ScopeObjectEditor||
|VariableListInspectorPlugin|AccessListStore||VariableListStore||
|VariableListStore|AccessNewEntryEditor||ScopeObjectEditor||
|VariableStore|AccessNewEntryEditor||ScopeObjectEditor||
|Vegetation|MakeScope||Scope||
|VfsMountPathBrowser|GetFirstSelectedNode||VfsMountPathBrowserEntryNode||
|ViewerEntity|State||ViewerEntityState||
|VoteGlue|GetVoteObject||InteractionTarget||
|VoteTargetGlue|GetVoteTarget||InteractionTarget||
|VoterGlue|GetVoter||Country||
|War|GetAttackerLosses||WarLosses||
|War|GetAttackerWarLeader||Country||
|War|GetDefenderLosses||WarLosses||
|War|GetDefenderWarLeader||Country||
|War|GetLossesFor|unknown|WarLosses||
|War|GetOriginalAttacker||Country||
|War|GetWarGoal||WarGoal||
|War|GetWarGoalController||Country||
|War|MakeScope||Scope||
|WarGlue|GetAttackers||WarSideGlue||
|WarGlue|GetDefenders||WarSideGlue||
|WarGoal|GetCasusBelli||CasusBelli||
|WarGoal|GetWar||War||
|WarGoal|GetWarGoalType||WarGoalType||
|WarImpactWrap|GetAntagonism||AntagonismBombsSpec||
|WarItem|GetWar||War||
|WarLateralView|GetEnemyLeader||Country||
|WarLateralView|GetEnemyParticipantsSortSearch||FilteredSortedList||
|WarLateralView|GetEnforceAttackerPeace||DiplomaticActionItem||
|WarLateralView|GetEnforceDefenderPeace||DiplomaticActionItem||
|WarLateralView|GetFriendlyLeader||Country||
|WarLateralView|GetFriendlyParticipantsSortSearch||FilteredSortedList||
|WarLateralView|GetInterveneInAttackerWar||DiplomaticActionItem||
|WarLateralView|GetInterveneInDefenderWar||DiplomaticActionItem||
|WarLateralView|GetPlayer||Country||
|WarLateralView|GetWar||War||
|WarLateralView|Manager||LateralView||
|WarLateralView|Vars||Context||
|WarLateralViewBattle|GetBattleResult||BattleResult||
|WarLateralViewBattle|GetCombat||Combat||
|WarLateralViewParticipant|AccessWarLateralView||WarLateralView||
|WarLateralViewParticipant|GetCountry||Country||
|WarLateralViewParticipant|GetWarLateralView||WarLateralView||
|WarMessage|GetFirstCountry||Country||
|WarMessage|GetSecondCountry||Country||
|WarParticipant|GetCountry||Country||
|WarParticipantGlue|GetCountry||Country||
|WarParticipantGlue|GetWar||War||
|WarSideGlue|GetSelectedParticipant||WarParticipantGlue||
|WarSideGlue|GetWar||War||
|WarViewer|GetCurrentWar||WarGlue||
|WarsLedger|GetPlayer||Country||
|WarsLedger|GetWarsSortSearch||FilteredSortedList||
|WarsLedger|Manager||LateralView||
|WarsLedger|Vars||Context||
|WarsOverviewWar|GetMainEnemy||Country||
|WarsOverviewWar|GetWar||War||
|WeatherSystem|MakeScope||Scope||
|WorkOfArt|GetCreator||Character||
|WorkOfArt|GetDefinition||WorkOfArtType||
|WorkOfArt|GetLocation||Location||
|WorkOfArt|GetOrigin||Location||
|WorkOfArt|GetOwner||Country||
|WorkOfArt|MakeScope||Scope||
|WorkOfArtType|MakeScope||Scope||

## References

- ↑ More precisely, "UpperCamelCase" or "PascalCase"
- To update the tables, see Module:GUI script/Functions/Updates and Module:GUI script/Promotes/Updates

