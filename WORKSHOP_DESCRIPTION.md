# Cabinets and Choices

**Compatible with EU5 1.2.* | Multiplayer synchronized | Save-game compatible**

---

## Overview

Cabinets and Choices enhances the vanilla EUV experience across multiple areas: 
* transform your cabinet members from interchangeable bureaucrats into memorable characters whose histories, values, and rivalries shape how your nation grows. 
    * Develop powerful traits over time through events.
    * Clash or collaborate (with you/each-other/foreigners) based on their ideological leanings.
    * Leave lasting legacies when they retire or die.
* A system of new subject types - gives you access to subject-meta like you never though possible: 
    * Small OPMs for powerful modifiers like cultural influence and naval govenor capacity.
    * Low antagonism and control subjects for exerting progressively expanding influence on foriegn states (akin to Victoria 3 protectorate->puppet progression)
    * Powerful late-game subjects for organizing large empires and defining/solidifying your sphere of influence.
* Age-specific advances give regions, cultures, religions, and the Adm/Dip/Mil age-branches more meaningful choices - catchup opportunies, balance, and playstyle specialization as you play through the ages.
    * Many unlocks are sprinkled into the existing tech tree.
    * New micro-tech trees are unlocked in the age of discovery and after. 
        * Currently these require no new institutions but many of the advances are branch and/or region locked. Some are hidden conditional associated with the adm/dip/mil branches that do not appear in the age branch selector ui

### Balance & Compatibility Disclosure

The mod is fully additive — it adds no replace_paths and does not overwrite vanilla content. It can be enabled mid-campaign without risk, however, you would not recieve the country specific starting balance modifiers, and may have missed out on early age dynamic events.

This mod adds tons of new sources of modifiers from:
* cabinet members, 
* permanent and temporary country modifiers, 
* new advances, 
* subject type bonuses, 
* government reforms 
* and likely more in the future. 

It will change game balance significantly and to that end may not play nicely with other balance mods.

Otherwise, it should be broadly compatible with mods. I've personally been playtesting it with the existing country flavor mods and many more.

see the bottom for my complete test mod list.

---

## Installation

Subscribe on the Steam Workshop, then enable the mod in the EU5 launcher before starting a new game. All game rules default to **on** and can be toggled in the game setup screen.

---

## Features

### Minister Trait System

Cabinet members accumulate traits through gameplay events. Traits reflect a minister's background, competencies, and political philosophy — and they interact with each other, creating emergent synergies and tensions.

<!-- GEN:trait-summary -->
**Core Cabinet Traits (24)**
Tier 1 simple traits, Tier 2 kiss-curse trade-offs with real downsides, Tier 3 attribute-scaled triads covering integration, antagonism, exploration, and more.

**Age Traits (35)**
Era-specific traits granted through historical period events — Renaissance humanists, Reformation theologians, Absolutist administrators, Revolutionary agitators.

**Conditional Traits (75)**
Dynamic traits that spawn based on your realm's development level, societal value axes (17 ideological pairs), regional/religious context, military specialization, parliamentary activity, and specific game actions.

**Negative Traits (9)**
Acquired through underperformance events; each has a dedicated rehabilitation chain that removes the trait when you address the underlying problem.

*Total: 143+ traits*

**Notable traits:**

- **Iron Disciplinarian** — Order, hierarchy, obedience — these are the tools of this advisor's trade.
- **Shadow Counselor** — This advisor operates in the spaces between official channels, weaving a web of informants and leverage that would make a spider envious.
- **Progressive Reformist** — This advisor burns with the conviction that the old ways must give way to the new.
- **War Hawk** — This advisor's blood runs hot at the smell of gunpowder.
- **Master Integrator** — Exceptional in every dimension, this advisor commands the full sweep of administrative, military, and diplomatic knowledge.
- **Master Statesman** — Rare is the advisor who can read a room in three languages and leave everyone feeling they have won.
- **Grand Chancellor** — There are diplomats, and there are architects of foreign policy — this advisor is the latter.
- **Tribune of the People** — A cabinet minister beloved by the commons is a rare and powerful thing.
- **Philosopher King** — To be governed by a philosopher-king is the dream of every idealist and the nightmare of every opportunist.
<!-- /GEN:trait-summary -->

---

### Synergy Events

When ministers share complementary traits, synergy events fire during the yearly pulse and grant temporary country modifiers. There are **26 standard synergies**, **10 dual-role synergies** (cabinet × religious figure on the same minister), and **12 cross-country synergy events** that fire when your ministers interact with neighboring courts.

Examples of synergy effects:
- **Court of Learning** (Scholar + Learned Courtier): +8% research, +4% literacy, +8% institution growth
- **Iron Hegemony** (Iron Disciplinarian + War Hawk): +5% discipline, -10% all army costs, +10% antagonism
- **Caliphate Network** (Caliphate Diplomat + Grand Vizier): +2 diplomatic reputation, -12% antagonism, +1 diplomatic capacity
- **Shadow Network Activated** (Shadow Counselor + Espionage Director): +20 power projection, +2 diplomatic rep, +20% spy network

---

### Minister Legacies

Senior ministers can be recognized before they retire, granting them the **Retired Legend** trait. When they eventually die — or if they hold a legendary title (Grand Vizier, Tribune, Navigator, Philosopher King) — they leave a **permanent legacy modifier** on your country. Legendary deaths grant stronger legacies than standard retirements. Consecrated legacy variants (granted at death) are more powerful than the retirement versions.

---

### Negative Traits & Rehabilitation

Ministers who underperform acquire negative traits through yearly events. Each negative trait has a dedicated **rehabilitation chain**: if you address the underlying problem (stabilize finances, reform institutions, remove the minister's estate privileges, etc.), the negative trait is removed and the minister emerges stronger.

---

### New Subject Types
There are many new subject types to diversive and enhance subject-based gameplay:
* Progressively tighten your control on loosely aligned states, although they can sometimes be more troublesome then they are worth...
* Release special opm states for specific benefits - cultural, research, prestige, naval govenor cap.
* powerful marcher and govenorate subjects during the imperial era paving the way for napoleon-era-like consolidation, rebelions, and breakaways regions etc. 

Some subject types require you to have the matching estate privilege or government reform (at least one when there are options) to use them: 
* Elite Enclave
* Scientific College
* Naval Administration
* Provincial Governorate
* Tax Farm
* Military March

<!-- GEN:subject-types -->
**Personal Union**
- **Junior Partner** *(unlocks Age 2)* — A Junior Partner retains its own ruler and conducts independent foreign policy, yet acknowledges the preeminence of its overlord.
- **Lesser Partner** *(unlocks Age 2)* — A Lesser Partner is the maturation of a Junior Partner after fifty years of shared dynasty.

**Shadow / Client**
- **Shadow State** *(unlocks Age 2)* — A Shadow State is formally independent, bound only by secret treaty and discreet arrangement.
- **Client State** *(unlocks Age 3)* — A Client State is a nation brought into the orbit of a stronger power through treaty or released provinces.
- **Puppet State** *(unlocks Age 5)* — A Puppet State is a formerly independent nation brought under full administrative supervision of its overlord.

**Elite & Cultural**
- **Elite Enclave** *(unlocks Age 2)* — An Elite Enclave is a culturally kindred domain granted self-governance in recognition of its noble heritage.
- **Palatinate** *(unlocks Age 4)* — A Palatinate is an Elite Enclave that has grown into a semi-sovereign power — the count palatine may now declare war, call levies, and join campaigns.
- **Artists' Commune** *(unlocks Age 2)* — An Artists Commune is a self-governing community of painters, sculptors, and craftsmen whose works redound to their patron's glory.
- **Scientific College** *(unlocks Age 4)* — A Scientific College is a scholarly institution of a religiously governed polity, free to pursue learning on behalf of its patron.
- **Naval Administration** *(unlocks Age 3)* — A Naval Administration is a port town granted semi-independence to manage the maritime logistics of its patron's fleet.

**Trade**
- **Associated Republic** *(unlocks Age 2)* — An Associated Republic is an independent republican state under formal patronage.
- **Chartered Company** *(unlocks Age 5)* — A Chartered Company is a royally chartered trading corporation operating in distant lands on behalf of its overlord.

**Governance**
- **Protectorate** *(unlocks Age 3)* — A Protectorate is a weaker neighboring state under the protection of a stronger power without formal subjugation.
- **Crown Dependency** *(unlocks Age 2)* — A Crown Dependency is a realm bound to its overlord by ties of shared dynasty — the same ruler family governs both courts without a formal personal union.
- **Holy Protectorate** *(unlocks Age 4)* — A Holy Protectorate is a coreligionist state taken under the spiritual patronage of a larger power.
- **Provincial Governorate** *(unlocks Age 5)* — A high-autonomy administrative region governed by a Crown-appointed magnate.
- **Tax Farm** *(unlocks Age 5)* — An exploitative extraction arrangement in which a powerful lord manages revenue collection in exchange for a portion of the proceeds.
- **Military March** *(unlocks Age 5)* — An offensive border vassal given special military charter to project power beyond our frontiers.
<!-- /GEN:subject-types -->

---

### Era Advances
New advances have been added across the ages to unlock new subject types and reforms, enhance regional flavor, add gameplay variability, and maybe a little balancing (1.2 diseases).
Some of these are age-branch (Adm/Dip/Mil) specific - others cultural, regional, or country based. 

Many are mixed into exising tech trees, but there are also new micro-trees in each age past the renaissance. 
    - The mini-trees also have age-branch based advances, some have follow-on advances which are not listed in the age picker UI. 

<!-- GEN:advances -->
**Age of Renaissance** (6 advances)
- **Royal Union Network** — Unlocks: **Junior Partner, Lesser Partner**. Personal unions need not be passive inheritances.
- **Shadow Diplomacy** — Unlocks: **Shadow State**. Not all influence announces itself.
- **Artistic Patronage** — Unlocks: **Artists' Commune**. To commission great art is to leave one's mark on time itself.
- **Noble Patronage** — Unlocks: **Elite Enclave**. A wise ruler recognizes that the high nobility, given honored autonomy, will return loyalty rather than resentment.
- **Republican Patronage** — Unlocks: **Associated Republic**. Republics possess a practical genius that monarchies would do well to cultivate.
- **Dynastic Governance** — Unlocks: **Crown Dependency**. The web of royal marriages binding European courts together need not remain ceremonial.

**Age of Discovery** (15 advances)
- **Client State Diplomacy** — Unlocks: **Client State**. By offering protection in exchange for tribute, a great power can extend its influence into neighboring territories without the expense of outright conquest.
- **Naval Charter** — Unlocks: **Naval Administration**. A great fleet requires not only ships but infrastructure: dry docks, provisioning networks, and merchant expertise.
- **Protectorate Rights** — Unlocks: **Protectorate**. The law of nations permits a stronger power to declare itself the protector of a weaker neighbor, extending a shield without requiring formal subjugation.
- **Late Renaissance Ideas** — The flowering of humanist thought and classical revival that defined the Renaissance has not ended with a new age — our scholars and administrators continue to deepen its fruits in literacy, reason, and civic order.
- **Natural Philosophy** — Renaissance thinkers turned their gaze from scripture toward nature itself, cataloguing plants, studying the human body, and laying the ground for the empirical sciences.
- **Civic Humanism** — Humanist thinkers argue that civic virtue — active participation in governance, rhetoric, and public duty — is the highest expression of human excellence.
- **Church Patronage of Learning** — The Church has long been a patron of art and scholarship.
- **Scholastic Reform** — Catholic theologians have fused Aristotelian logic with Christian doctrine, creating a rigorous intellectual culture in our monasteries and cathedral schools.
- **Islamic Observatory Tradition** — The great observatories of Samarkand, Cairo, and Istanbul represent a centuries-long Islamic tradition of precise astronomical and medical knowledge.
- **Polymath Networks** — The great cities of the Islamic world are home to polymaths who move freely between mathematics, medicine, philosophy, and engineering.
- **Renaissance Court Culture** — The princely courts of Italy have become models of refined learning and artistic patronage.
- **Civic Republican Ideals** — Renaissance republicanism drew on ancient Rome to argue that free citizens deliberating together produce wiser law than any monarch alone.
- **Classical Revival** — Neo-Confucian scholars have renewed attention to the classical texts of antiquity, re-examining the Four Books and Five Classics with fresh commentary.
- **Examination System Refinement** — Generations of scholarly refinement have made the examination system an extraordinarily precise instrument for selecting capable administrators.
- **Italian Masters** — The workshops of Florence, Venice, and Milan have produced an unbroken line of masters in painting, sculpture, and architecture.

**Age of Reformation** (14 advances)
- **Scholarly Orders** — Unlocks: **Scientific College**. The great religious orders have long been the guardians of learning.
- **Palatinate System** — Unlocks: **Palatinate**. The most elevated noble enclaves may be recognized as palatinates — sovereign-within-sovereign territories whose counts wield near-regal authority.
- **Holy Patronage** — Unlocks: **Holy Protectorate**. Faith is a bond stronger than treaty.
- **Late Discovery Ideas** — A generation of explorers has mapped the contours of a world far larger than our ancestors imagined.
- **Systematic Cartography** — Where early explorers navigated by rumor and estimation, a new generation of cartographers brings mathematical precision to the art of the map.
- **Colonial Consolidation** — The era of reckless discovery is giving way to careful consolidation.
- **Maritime Republic Trade Networks** — The mercantile republics have long understood that profit lies not in territory but in the control of exchange.
- **Maritime Tribute Networks** — Our great fleets have long projected power through tribute relationships with maritime peoples across the seas.
- **Missionary Expansion** — Faith follows the flag.
- **Colonial Ecclesiastical Orders** — The great religious orders — Dominicans, Franciscans, Jesuits — have established missions across our colonial territories, building schools and churches that anchor European civilization in the new world.
- **Iberian Colonial Doctrine** — Spain and Portugal have developed a sophisticated theory of colonial administration: encomienda grants, viceroyalties, and a transatlantic commercial system that channels the wealth of new worlds to Iberian coffers.
- **Atlantic Fleet Doctrine** — The carrack and galleon — heavily armed, deep-hulled ships capable of crossing oceans — represent an Iberian mastery of oceanic warfare.
- **Overland Trade Routes** — While European powers struggle to find sea routes around our lands, we command the ancient arteries of overland trade: the Silk Road, the incense routes, the great caravans that have connected East and West for millennia.
- **Silk Road Revival** — By securing the caravan routes, investing in caravanserais, and negotiating safe passage agreements, we restore the Silk Road to something of its former glory — channeling the wealth of Asia through our markets.

**Age of Absolutism** (21 advances)
- **Naval Administration** — The state establishes a permanent admiralty board to oversee distant naval stations, extending royal control over the seas.
- **Puppet State Administration** — Unlocks: **Puppet State**. Shadow influence must eventually give way to direct administration.
- **Chartered Trading Companies** — Unlocks: **Chartered Company**. The merchant classes have demonstrated an unparalleled capacity for organizing commerce at global scale.
- **Provincial Governance** — Unlocks: **Provincial Governorate**. A formalized system of Crown-appointed governorates allows the realm to extend administrative reach over distant regions without direct annexation.
- **Tax Farming** — Unlocks: **Tax Farm**. Contracting the collection of revenues to powerful local lords — at a price.
- **Military Marches** — Unlocks: **Military March**. Designating border territories as military marches creates offensive buffers that extend our power at the frontier.
- **Late Reformation Ideas** — A century of religious upheaval has exhausted many, but its legacy is real: confessions are clearer, institutions more self-aware, and hard-won settlements give the realm a cautious stability that prior generations could not imagine.
- **Confessional State Building** — The lesson drawn from the Wars of Religion is that a stable realm requires a unified confession — or at least a carefully managed one.
- **Protestant Church-State** — Protestant reformers insisted that the Word of God, accessible to all who can read, must be the foundation of a Christian realm.
- **Lutheran Educational Legacy** — Luther's insistence on every Christian reading Scripture for themselves drove the establishment of parish schools across Protestant Europe.
- **Catholic Confessional Legacy** — The Council of Trent revitalized Catholic institutions, clarifying doctrine, reforming the clergy, and establishing new religious orders dedicated to education and pastoral care.
- **Jesuit Reform Networks** — The Society of Jesus operates schools, universities, and missions across three continents, transmitting the methods of rigorous Tridentine Catholicism wherever European colonialism has reached.
- **Confessional Consolidation** — In an age when European powers fight over doctrine, Islamic rulers face their own choices between Sunni orthodoxy, Shia devotion, and syncretic practice.
- **Millet Administrative System** — The Ottoman millet system, which grants recognized religious communities legal autonomy under their own institutions, has proven a remarkably effective tool for governing a diverse empire.
- **Post-War Religious Settlement** — Decades of religious war have produced exhausted pragmatism: most rulers now accept that forcing universal religious conformity is too costly.
- **Westphalian Sovereignty Doctrine** — The Peace of Westphalia established a new framework for European politics: states are sovereign within their own borders, and the principle of cuius regio, eius religio gives rulers authority over their realms' confessional identity.
- **Syncretic Tolerance** — India's extraordinary religious diversity has long required its rulers to practice a degree of tolerance unknown in Europe.
- **Sulh-e-Kul** — Akbar's doctrine of sulh-e-kul — universal peace — argued that a wise ruler stands above sectarian division, drawing legitimacy from all his subjects regardless of faith.
- **Court of Universal Tolerance** — Our court has become a meeting place for scholars of every tradition: Hindu pandits, Muslim ulama, Jain monks, Sikh teachers, and European missionaries all find a welcome audience.
- **State Orthodoxy** — By aligning state ritual and institutional practice with an orthodox tradition — Confucian, Buddhist, or Shinto — our government projects continuity, legitimacy, and cultural coherence across our realm.
- **Confucian Bureaucratic Faith** — Neo-Confucian state philosophy has fused ritual, ethics, and administrative technique into a seamless whole.

**Age of Revolutions** (14 advances)
- **Late Absolutism Ideas** — The age of absolute monarchy has passed its zenith, but its achievements endure: centralized bureaucracies, permanent armies, and rationalized state finances are now the baseline from which even reformers must begin.
- **Enlightened Administration** — Enlightenment thought has reached the corridors of power.
- **Enlightened Despotism** — Frederick of Prussia, Catherine of Russia, Joseph of Austria — the great enlightened despots demonstrate that absolute power need not mean arbitrary power.
- **Reform from Above** — Faced with the threat of revolution from below, wise rulers choose reform from above.
- **Mercantilist Legacy** — Two centuries of mercantilist policy have created sophisticated trading institutions: regulated companies, customs regimes, navigation acts, and state banks.
- **Colonial Mercantile System** — Our colonial empire is now a mature economic system: plantation agriculture, monopoly trade companies, navigation acts, and silver flows all converge to channel colonial wealth into the metropole.
- **Professional Standing Army** — The military revolution has reached its culmination: every major power now maintains a permanent, paid, uniformed army rather than relying on feudal levies or mercenaries.
- **Prussian Discipline** — Prussia's army has become the envy and model of Europe: relentless drill, cadenced marching, and a culture of obedience that makes the Prussian musketeer the most precisely controllable soldier on any battlefield.
- **General Staff System** — The Prussian innovation of a permanent general staff — officers who plan campaigns, map terrain, and war-game scenarios before battles begin — transforms warfare from an art into a science.
- **New Order Military Reform** — Reformist viziers and sultans have recognized that European military methods represent a genuine challenge.
- **Qing Administrative Consolidation** — The Qing conquest has not replaced Chinese administrative culture — it has absorbed and perfected it.
- **Bureaucratic Peak** — Our administrative tradition has reached a summit of refinement.
- **Administrative Sophistication** — Indian states have developed elaborate traditions of revenue administration, provincial governance, and fiscal management.
- **Fiscal Administration** — The Maratha confederacy has demonstrated that decentralized revenue farming, when combined with effective military power and political skill, can build a formidable state from a fragmented beginning.
<!-- /GEN:advances -->

---

### New Estate Privileges & Government Reforms

<!-- GEN:privileges-reforms -->
**Estate Privileges**
- **Shadow Network** *(via: Shadow Diplomacy)*
- **Patronage of the Arts** *(via: Artistic Patronage)*
- **Noble Enclave Rights** *(via: Noble Patronage)*
- **Naval Charter** *(via: Naval Charter)*
- **Scholarly Brotherhood** *(via: Scholarly Orders)*
- **Royal Trading Charter** *(via: Chartered Trading Companies)*
- **Governorate Charter** *(via: Provincial Governance)*
- **Tax Charter** *(via: Tax Farming)*
- **March Charter** *(via: Military Marches)*

**Government Reforms**
- **Naval Administration** — The establishment of a permanent admiralty board extends royal authority over distant naval stations, enabling an additional naval governorship and reducing the cost of maintaining far-flung ports. *(via: Naval Administration)*
- **Colonial Charter System** — The crown establishes a formal legal framework for issuing royal charters to commercial enterprises operating in distant lands, granting them military and commercial authority in exchange for tribute and loyalty. *(via: Chartered Trading Companies)*
- **Governorate System** — Formalizes the system of Crown-appointed provincial governorates, improving administrative capacity across the realm. *(via: Provincial Governance)*
- **Tax Farming Contracts** — Systematizes the practice of farming out tax collection to powerful lords, reducing bureaucratic overhead in exchange for local efficiency. *(via: Tax Farming)*
- **March Charter** — Issues formal charters to border territories designating them as military marches, creating a network of offensive buffers along the realm's most contested frontiers. *(via: Military Marches)*
<!-- /GEN:privileges-reforms -->

---

### Event Categories

<!-- GEN:event-categories -->
| Namespace | Events | Description |
|-----------|:------:|-------------|
| `cc_cabinet` | 16 | Minister counsel, estate relations, diplomatic situations, provincial affairs |
| `cc_traits` | 18 | Age trait acquisition, ruler teaching, peer learning |
| `cc_cond` | 15 | Conditional trait spawning based on realm conditions and actions |
| `cc_synergy` | 26 | Trait pair synergies — temporary bonuses when ministers share trait families |
| `cc_neg` | 17 | Underperformance events and rehabilitation chains |
| `cc_wealth` | 10 | Wealth hoarding pressure and minister enrichment |
| `cc_dual` | 10 | Cabinet × religious figure dual-role synergies |
| `cc_intl` | 12 | Cross-country interactions between neighboring courts |
| `cc_feudal` | 8 | Feudal era court events |
| `cc_legacy` | 3 | Senior minister retirement and legacy transmission |
| `cc_legend` | 6 | Legendary minister quest chains |

*~141 events total*
<!-- /GEN:event-categories -->

---

### Game Rules

All rules are toggleable in the game setup screen before starting a session.

<!-- GEN:game-rules -->
**C&C: France — Lowlands Containment**
Gives France's Lowlands-culture neighbors elevated antagonism toward France at game start, decaying over 200 years.
- **Enabled** *(default)* — France begins under pressure from its Lowlands neighbors, reflecting historical anxieties about French hegemony.
- **Disabled** — France starts with no extra antagonism from its neighbors.

**C&C: Wealth Hoarding Events**
When enabled, countries that hoard gold above 100x their monthly income will periodically face events representing court demands and economic pressure.
- **Enabled** *(default)* — Wealth hoarding events fire from the biyearly pulse when the gold threshold is met.
- **Disabled** — No wealth hoarding events will fire.

**C&C: Mamluks — Foreign Rule Strain**
Gives the Mamluks starting penalties reflecting their status as a foreign military caste ruling over native Egyptians.
- **Enabled** *(default)* — The Mamluks begin with a permanent peasant levy penalty and decaying military strain, easing over 200 years.
- **Disabled** — The Mamluks start with no historical penalties.

**C&C: Ottomans — Colonization **
Prevent the Ottomans from colonizing.
- **Prevent Colonization** *(default)* — The Ottomans are permanently prevented from colonizing.
- **Allow Colonization** — The Ottomans may still colonize as normal.
<!-- /GEN:game-rules -->

---

### Country Starting Modifiers

<!-- GEN:country-starts -->
**France — Lowlands Containment** *(default: on)*
France begins under elevated antagonism from its Lowlands-culture neighbors (Burgundy, the Low Countries, and nearby realms), reflecting historical anxieties about French regional hegemony. The pressure decays over 200 years. France also starts with a permanent modifier representing its expansionist posture toward the Lowlands.

**Mamluks — Foreign Rule Strain** *(default: on)*
The Mamluks begin with a permanent peasant levy penalty (representing their status as a foreign military caste ruling over native Egyptian society) and a severe military strain modifier that decays over 200 years. Combined, these represent the fragility of Mamluk rule and ease as the regime stabilizes — or they don't.

**Ottomans — No Colonization** *(default: on)*
The Ottomans are permanently prevented from colonizing overseas. This reflects the historical Ottoman orientation as a land empire focused on Anatolia, the Balkans, and the Middle East, rather than competing in Atlantic exploration.
<!-- /GEN:country-starts -->

---

## Compatibility

- No `replace_paths` — fully additive, compatible with other mods that don't replace the same files
- Safe to enable on existing saves (new content will start appearing as events fire)
- Multiplayer synchronized
- May break balance as cabinet members and new subjects provide a lot of bonuses.
- Generally mod compatible so long as they dont modify traits heavily like i have. 
    - Not tested with other subject mods as i found them unstable.
    - Tested with:
        * Hussite, Austria, Brandenburg (the 'country pack' one), Timur, and Ottoman flavor packs. 
        * Community Flavor Pack
        * Overseas Naval Govenors
        * Logical Advances Trees
        * Improved Subject Management
        * Nobles Auto Marry
        * Auto Child Education
        * Additional Buildings
        * Bureaucracies for Everyone
        * Parliament Expanded
        * National Destinies
        * Continental Hegemonies
        * Terra Cognita
        * Forced Cultural Expulsion
        * Improved Cultural Dynamics


---

## AI Use Disclosure

Numerous AI agents were used in the creation of this project: Claude, Gemini, Qwen.
Currently there is no AI art or music in the project, but only because I havn't added any yet. 


---

## Feedback & Bugs

Report issues on the Steam Workshop discussion page or the mod's GitHub repository.
