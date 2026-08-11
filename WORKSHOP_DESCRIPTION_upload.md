# Flavorium Universalis

  
  
**Compatible with EU5 1.3.* | Multiplayer synchronized**  
**Languages:** English, Français, Deutsch, Español  
  


* * *

  
  


## Overview

  
**A note from the author:**  


> This mod is still in an early preview and not everything has been fully tested. Several subject paths and their event chains are underexplored:  
> 
> 
>   * Large late-game subjects and palatinates and their event families have yet to be fully tested.
>   * The subject changes that culminate in the federalization system during the Age of Revolutions are still being tested and will change.
>   * not all character legacies have been verified and balanced.
>   * Cabinet situations like the war council and minister schemes still need more work. Along with adding remaining ones: the scholar's court, regency crisis, and federal/international congress.
> 
Balancing of new content is subject to change as more playtesting is done and other feedback comes in.   
>   
>  The game has been simulated in observer mode through to the 1800s a few times.   
>   
>  At this point I'm looking for community thoughts on the new subject types, cabinet gameplay, balance, mexico situation, etc.

  
Flavorium Universalis enhances the vanilla EUV experience across multiple areas:  


  * Improved AI personality system with dynamic logic AND historical changes.
    * Let the AI adjust its personality logically instead of randomly. It can react immediately to an event or to a build-up of circumstances.
    * Watch the great nations of history make historic shifts in their foreign policy.
  * Give your cabinet members distinct histories, values, and rivalries that affect how your nation develops.
    * Develop powerful traits over time through events.
    * Clash or collaborate (with you, each other, and foreign courts) based on their ideological leanings.
    * Leave lasting legacies when they retire or die.
    * **NEW:** Ministers scheme against each other. Rivalries escalate through a three-stage event chain, and ideologically aligned ministers may form cabals and pursue joint agendas.
    * **NEW:** Assign explicit duties to ministers: war council, domestic reform, diplomatic mission, colonial posting, and more. Each duty raises related events and grants an ongoing country modifier.
    * **NEW:** Cabinet composition has aggregate effects. A court dominated by militarists, merchants, or clergy activates auto-modifiers that reflect the makeup of your advisors.
    * **NEW:** Ministers grow through stepping-stone trait chains, starting as fumbling reformists or green adjutants and advancing through events into masters of their craft.
    * **NEW:** Military ministers run war council events during conflicts, which unlock post-war reform proposals when you win.
    * **NEW:** Post a minister overseas as a colonial governor to run charter company events, handle native uprisings, and unlock the decolonization crisis chain in the Age of Revolutions.
  * New subject types add more ways to use subjects:
    * Small OPMs that grant modifiers like cultural influence and naval governor capacity.
    * Low-antagonism, low-control subjects for steadily expanding influence over foreign states (similar to a Victoria 3 protectorate-to-puppet progression).
    * Late-game subjects for organizing large empires and defining a sphere of influence.
    * **NEW:** Long-term subjects remember how you treated them. A bond system tracks economic, military, political, cultural, and personal relationships across the Ages, which sets how your subjects behave in the Age of Revolutions.
  * Age-specific advances give regions, cultures, religions, and the Adm/Dip/Mil age-branches more choices: catch-up opportunities and playstyle specialization as you play through the ages.
    * Many unlocks are placed into the existing tech tree.
    * New micro-tech trees unlock from the Age of Discovery onward. They are branch- and region-locked, and some stay hidden until you meet the conditions.
  * Historical flavor for the Hundred Years War, Hussite Wars, and more.
  * **NEW:** The Invasion of Mexico, a historical situation covering the colonial conquest of Mesoamerica. A native Mesoamerican Confederation can resist the incursion, with a dedicated expedition casus belli and 28+ events across the conquest and its aftermath.
  * **NEW:** The Balance of Power, a continent-wide great-power situation where an aspiring hegemon's Preponderant Bloc is checked by a Balancing Coalition. Track the Preponderance Share, court neutrals, and play Napoleonic-era events toward hegemony, an eastern deluge, revolution, stagnation, or a lasting Concert of Europe.
  * **NEW:** Parliamentary diplomacy for the Balance of Power. The Balancing Coalition can convene a **Balancing Congress** of its own (Pitt's subsidies, the Treaty of Chaumont, a Pragmatic Army command, a joint démarche, a partition treaty). A coalition victory founds the playable **Concert of Europe** , an elected great-power directorate that votes on its own doctrine, collective-security pacts, and standing-congress mediation.
  * **NEW:** A literacy rebalance. A global baseline change to pop literacy is paired with region-specific catch-up advances and per-estate library bonuses, so Western Europe, colonial powers, and East Asia develop education at different rates.
  * **NEW:** Frontier Governance, a lesser Frontier Governor for rural, road-less interior provinces. An advance and per-estate privileges help steppe, mountain, and Mandate-of-Heaven realms hold ground they cannot yet urbanize.

  


### Balance & Compatibility Disclosure

  
  
The mod is mostly additive. It replaces some vanilla laws, advances, and reforms, but it adds no replace_paths and removes no vanilla content. I would not advise using it with an existing save, because of the balance and country starting-condition changes.  
  
This mod adds many new sources of modifiers: cabinet members, permanent and temporary country modifiers, new advances, subject type bonuses, government reforms, cabinet duty assignments, auto-modifiers from cabinet composition profiles, subject bond payoff events, and more. It will change game balance significantly and may not play nicely with other balance mods.  
  
**Balance changes that apply to every game (not toggleable by game rule):**  


  * **Literacy nerf.** Three vanilla advances are overridden. The **Written Alphabet** baseline drops from +5 to +2 global max literacy. **Printing Press** and **Innovativeness** now raise upper-class literacy (nobles, clergy, burghers) rather than generic global literacy, so the masses no longer benefit directly from these advances. Regional catch-up advances partially restore literacy for Western Europe, colonial powers, and East Asia. Libraries grant per-estate literacy bonuses instead of generic local literacy.
  * **Culture capacity nerf.** Several era advances and laws reduce **cultures_capacity** , making cultural integration of diverse realms harder and more costly than in vanilla.

  
**Balance changes gated by game rules (all default on, all toggleable):**  


  * France and England starting modifiers (Hundred Years War Flavor rule)
  * Mamluk foreign rule strain starting modifiers (Mamluks: Foreign Rule Strain rule)
  * Ottoman colonization restriction (Ottomans: Colonization rule)
  * France Lowlands antagonism at game start (France: Lowlands Containment rule)

  
Otherwise it should be broadly compatible. See the Compatibility section at the bottom for the full test mod list.  
  


* * *

  
  


## Installation

  
  
Subscribe on the Steam Workshop, then enable the mod in the EU5 launcher before starting a new game. All game rules default to **on** and can be toggled in the game setup screen (split between the gameplay and flavor tabs).  
  


* * *

  
  


## Features

  
  


### Minister Trait System

  
  
Cabinet members accumulate traits through gameplay events. Traits reflect a minister's background, competencies, and political philosophy, and they interact with each other to create synergies and tensions.  


> As of 1.2, characters can only have one cabinet trait, which limits how many country modifiers we can tie to a character's cabinet employment.

  
**Core Cabinet Traits (24)**  
Tier 1 simple traits, Tier 2 kiss-curse trade-offs with real downsides, Tier 3 attribute-scaled triads covering integration, antagonism, exploration, and more.  
  
**Age Traits (37)**  
Era-specific traits granted through historical period events: Renaissance humanists, Reformation theologians, Absolutist administrators, Revolutionary agitators.  
  
**Conditional Traits (75)**  
Dynamic traits that spawn based on your realm's development level, societal value axes (17 ideological pairs), regional/religious context, military specialization, parliamentary activity, and specific game actions.  
  
**Negative Traits (9)**  
Acquired through underperformance events; each has a dedicated rehabilitation chain that removes the trait when you address the underlying problem.  
  
_Total: 145+ traits_  
  
**Notable traits:**  


  * **Iron Disciplinarian** : This advisor governs through order, hierarchy, and obedience.
  * **Shadow Counselor** : This advisor works through informants and quiet leverage rather than official channels.
  * **Progressive Reformist** : This advisor is convinced the old ways must give way to the new.
  * **War Hawk** : This advisor is eager for war.
  * **Master Integrator** : This advisor is highly capable across administrative, military, and diplomatic affairs.
  * **Master Statesman** : This advisor is a skilled negotiator who can leave rival courts satisfied even when they have conceded.
  * **Grand Chancellor** : This advisor does not merely conduct diplomacy; they direct foreign policy.
  * **Tribune of the People** : This advisor is genuinely popular with the commons and uses that popularity to govern: smoothing legislation through parliament, suppressing unrest, and making the estates feel heard.
  * **Philosopher King** : This ruler combines real intellectual power with political authority.

  


* * *

  
  


### Synergy Events

  
  
When ministers share complementary traits, synergy events fire during the yearly pulse and grant temporary country modifiers. There are **26 standard synergies** , **10 dual-role synergies** (cabinet × religious figure on the same minister), and **12 cross-country synergy events** that fire when your ministers interact with neighboring courts.  
  
Examples of synergy effects:  


  * **Court of Learning** (Scholar + Learned Courtier): +8% research, +4% literacy, +8% institution growth
  * **Iron Hegemony** (Iron Disciplinarian + War Hawk): +5% discipline, -10% all army costs, +10% antagonism
  * **Caliphate Network** (Caliphate Diplomat + Grand Vizier): +2 diplomatic reputation, -12% antagonism, +1 diplomatic capacity
  * **Shadow Network Activated** (Shadow Counselor + Espionage Director): +20 power projection, +2 diplomatic rep, +20% spy network

  


* * *

  
  


### Minister Legacies

  
  
Senior ministers can be recognized before they retire, granting them the **Retired Legend** trait. When they die, or if they hold a legendary title (Grand Vizier, Tribune, Navigator, Philosopher King), they leave a **permanent legacy modifier** on your country. Legendary deaths grant stronger legacies than standard retirements, and consecrated legacy variants granted at death are stronger than the retirement versions. A retiring minister may also seek out a protégé to pass their wisdom to.  
  


* * *

  
  


### Negative Traits & Rehabilitation

  
  
Ministers who underperform acquire negative traits through yearly events. Each negative trait has a dedicated **rehabilitation chain** : if you address the underlying problem (stabilize finances, reform institutions, remove the minister's estate privileges, etc.), the negative trait is removed and the minister emerges stronger.  
  


* * *

  
  


### Stepping Stone Traits & Progression

  
  
Ministers can enter **progressive trait chains** , starting from a Tier 0 entry trait and advancing into specialists over a lifespan:  


  * **Chain A, The Reformer 's Path:** fumbling_reformist → … → master_reformer (driven by the Domestic Reform duty)
  * **Chain C, The Diplomat 's Ascent:** tentative_envoy → … → master_statesman
  * **Chain D, Military Hardening:** green_adjutant → … → standing_army_advocate or defensive_commander
  * **Chain F, The Fiscal Path:** clumsy_accountant → … → treasury/prosperity specialist
  * **Chain E, Colonial Pioneer:** frontier_administrator → returned_colonial_governor (driven by the Colonial Posting duty)

  
Entry traits are mild negatives. They are the starting point, not the destination. Progress is tracked per minister via event variables and advances. Assigning a minister to the matching duty doubles their progression rate.  
  


* * *

  
  


### Court Rivalry & Cabal

  
  
Ministers with opposing ideological traits build **court tension** over time. When court tension reaches its threshold, a three-stage rivalry chain fires:  


  * **The Minister 's Complaint:** the rival ministers clash and the ruler must take sides
  * **A Letter Unsealed:** whispers turn to written evidence and the feud becomes harder to contain
  * **The Faction Hardens:** the court fractures along factional lines, forcing a resolution

  
Ideologically aligned ministers can instead form **cabals** , political compacts that let them pursue joint agendas. Cabinet alliances grant temporary bonus modifiers, but they create factions the ruler may need to manage later.  
  
The **Purge Rival** character interaction lets rulers act before tensions escalate, at the cost of minister loyalty.  
  


* * *

  
  


### Cabinet Duties

  
  
Assign ministers to explicit roles to boost related event systems and gain ongoing country modifiers:  


  * **War Council:** improves discipline and morale recovery, and runs war council events during conflicts
  * **Domestic Reform:** reduces stability cost and doubles stepping-stone progression rate
  * **Diplomatic Mission:** diplomatic effect, and gates diplomatic interaction events
  * **Scholarly Inquiry:** research effect, and raises scholarly events (Age 5 to 6)
  * **Religious Oversight:** religious influence effect, and gates confessional tension events
  * **Colonial Posting:** sends a minister overseas and unlocks colonial dispatch, corruption, and crisis events
  * **Free Hands:** a 'no action' assignment. The minister attends to whatever the court requires, and all idle events fire at baseline rate

  
Multiple ministers may share Free Hands. Other duties are exclusive.  
  


* * *

  
  


### Cabinet Composition Auto-Modifiers

  
  
The cabinet has effects as a whole, not only as individual ministers. When the cabinet matches a composition profile, an **aggregate auto-modifier** activates and persists until the profile no longer holds:  


  * **Warlord Court:** two or more military specialists; the court is geared for war
  * **Merchant Republic Spirit:** two or more commercial or fiscal specialists; a court focused on revenue
  * **Enlightened Court:** two or more scholarly or empiricist ministers; research bonuses
  * **Court Paralysis:** opposing ideologues deadlock the cabinet; efficiency suffers
  * **Entrenched Court:** three or more conservative ministers; reform slows but stability holds
  * **Balanced Court:** no single trait category dominates; modest bonuses across the board
  * **Nobles / Burghers / Clergy Court Captured:** one estate holds a majority in the cabinet; estate power and influence modifiers follow

  


* * *

  
  


### War Council

  
  
Your military ministers now drive outcomes during wars:  


  * **The Council of War:** fires annually while at war; military traits decide whether you favor offensive action, defensive consolidation, or emergency resupply
  * **Financing the War:** when the treasury is strained during a conflict, ministers debate emergency measures
  * **The General 's Request:** a supreme commander or outdated general asks for authority or retirement
  * **Post-war reform proposals:** winning a war opens a short window for standing army reform, supply reform, or fortification doctrine proposals, based on which military traits are present
  * **The Outdated General:** veterans past their prime can be retired with honor during a conflict

  


* * *

  
  


### Estate Faction Capture

  
  
When a single estate dominates the cabinet, with two or more ministers bearing Noble, Burgher, or Clergy affiliation traits, the captured-court auto-modifier activates and faction events begin firing:  


  * **The Nobles Demand:** the noble faction asks for sweeping privilege; refusal risks minister loyalty
  * **The Merchant Compact:** burgher ministers advance a trade agenda; you choose compliance or friction
  * **The Prelates Move:** clergy ministers press for religious influence; you decide how much power the church gets

  
Balancing your cabinet composition is a real strategic concern.  
  


* * *

  
  


### Colonial Cabinet

  
  
Post a minister overseas as a **Colonial Posting** to unlock a dedicated colonial event chain:  


  * **The Governor 's Dispatch:** regular flavor reports from the posted minister; invest, extract, or acknowledge their work
  * **Corruption in the Colony:** risk events when the minister's character interacts with colonial wealth
  * **A Native Uprising:** the posted minister must manage colonial resistance
  * **Fever in the Colony:** the minister faces tropical disease; their traits and your choices decide the outcome

  
Charter company owners also receive dedicated events:  


  * **The Company 's Accounts:** the minister audits the company ledgers; windfall or investigation
  * **A Monopoly Dispute:** merchant-aligned ministers clash over company privileges
  * **The Colonial Petition:** a late-game decolonization pressure chain (Ages 5 to 6) that can lead to a Defection or a negotiated Compromise

  


* * *

  
  


### Invasion of Mexico

  
  
A historical situation that fires when a colonial or foreign power establishes a foothold in Mesoamerica (or the adjacent Caribbean and Central America by 1540). The situation persists until all independent native Mesoamerican powers are subjugated, or until 1600.  


  * **The Mesoamerican Confederation:** native powers can unite under a defensive confederation international organization, sharing military access and coordinating resistance against colonial incursion
  * **Expedition Casus Belli:** colonial powers gain a dedicated CB for pressing territorial claims against Mesoamerican states during the situation window
  * **Conquest events:** about 28 events covering the expeditioner's dilemmas, native reactions, confederation formation, diplomatic overtures, and the resolution of the situation
  * **Generic actions:** the confederation leader can call member states to arms; colonial powers can press terms or offer a negotiated settlement

  
Gated by the **C &C: Invasion of Mexico** game rule (default: on).  
  


* * *

  
  


### Balance of Power

  
  
A two-pole great-power situation spanning Europe and the Near East. The strongest eligible power leads the **Preponderant Bloc** as it reaches for pre-eminence, and the strongest power that fears it leads the **Balancing Coalition** formed to deny it. A **Preponderance Share** (0 to 100, where 50 is equilibrium) measures how dominant the leading bloc has become. Let it run past 65 and a hegemon may emerge.  


  * **Two international organizations:** purpose-built blocs with their own ambition and resolve gauges, and AI alignment logic driven by kinship, faith, fear, threats, and gold
  * **The balancer 's craft:** subsidise faltering partners, court neutrals, and convene a Congress to close ranks. As the hegemon, lean on weaker courts, impose a Continental System, or bind them by marriage
  * **Napoleonic-era flavor:** the Battle of the Nations, scorched earth, the Spanish ulcer, levée en masse, and a separate peace, each shifting the equilibrium and tying into cabinet duties and minister traits
  * **Player actions:** petition a bloc to join (the leader decides), proclaim armed neutrality, or play both sides as an unaligned court. As a bloc leader, spend Ambition or Resolve on coercive or balancing measures from the organisation view
  * **Satellite kingdoms:** a dominant hegemon can turn coerced courts into client or puppet states
  * **The Balancing Congress:** the coalition can convene a parliament of its own and carry collective motions by majority vote: pooled subsidies (Pitt's gold), the Treaty of Chaumont's pledge of no separate peace, a Pragmatic Army unified command, a joint démarche, and a partition treaty agreeing the war aims in advance
  * **The reckoning:** the contest resolves along three roads tracked in disjoint share-bands. Hegemony and a coalition victory each prime a decisive final war won on the real treaty, while stagnation quietly closes a contest that has gone nowhere

  
**The Concert of Europe** is more than an ending. A coalition victory under the right policy founds a **playable great-power directorate** that the victors govern:  


  * **An elected presidency:** the chief balancer becomes founding president, and the chair then rotates by election, with an on-demand Vote of No Confidence to unseat it. New powers are admitted only by a vote of the congress
  * **Three questions of state, voted in congress:** the guiding Doctrine (classic Balance of Power, the legitimist Principle of Intervention, or Liberal Internationalism), Collective Security (ad-hoc concerts or a binding Mutual Guarantee), and whether the powers sit as a Standing Congress
  * **Collective actions:** Congress Mediation of a member's wars, a Collective Intervention, management of the Eastern Question, and the admission of a rising power
  * **Not permanent:** even the best-managed concert may fray a generation later, and a new balance arise

  
Arrives once a great power adopts the Balance of Power Doctrine, or once the revolutionary era opens. Gated by the **C &C: Balance of Power** game rule (default: on).  
  


* * *

  
  


### Balance Changes - Literacy & Culture Capacity Nerfs

  
  
**Literacy Nerfs** give different regions and estates different educational trajectories. The goal is to reduce peasant literacy, and thus pop promotion, while letting Europe recoup some of it through new follow-on advances:  


  * **Global baseline adjustment:** a nerf to vanilla's universal pop literacy, which widens the gap between literate and non-literate societies
  * **Library building rework:** vanilla libraries granted generic local literacy. They now provide per-estate bonuses (nobles, clergy, burghers) rather than literacy for all pops
  * **Regional catch-up advances:** targeted advances that partially restore literacy for specific world regions:
    * **Western Europe (Age 2):** mass literacy driven by Innovativeness; soldiers, peasants, laborers
    * **Western Europe (Age 4):** Printing Press follow-on; burghers, soldiers, peasants, laborers
    * **Colonial powers (Age 4):** colonial ecclesiastical networks; burgher and soldier literacy for powers with active colonial nations
    * **East Asia (Age 4):** classical examination tradition; noble and burgher literacy for Japan and China

  
**Culture Capacity Nerfs** : several vanilla advances are overridden to halve their **cultures_capacity** bonus, making it harder and more expensive to maintain large multi-cultural realms:  


  * **Cultural Acceptance** (Age 1, universal): halved from the vanilla value to **+0.5**
  * **Vibrant Court** (Age 2, universal): halved to **+0.5**
  * **Cultural Ties** (Age 4 Adm, universal): reduced to **+1**
  * **Persian in the Court** (Age 3, Ottoman): halved to **+0.5**
  * **Millets** (Age 2, Ottoman): halved to **+0.5**
  * **Foreign Cultural Law** (law): the _Allow Foreign Rituals_ option changes from a flat **+1** culture capacity to **+20%** relative, which reduces its value for small realms
  * **Magyar Supremacy** (Nobles estate privilege, Hungary): **-33%** culture capacity modifier

  


* * *

  
  


### Overlord-Subject Bonds

  
  
Long-term subjects keep a **relationship history**. A five-part bond system tracks your relationship with each significant subject across the game:  


  * **Economic:** how you tax and invest in the subject
  * **Military:** whether you use them as cannon fodder or shield them
  * **Political:** how much autonomy you grant or revoke
  * **Cultural:** integration versus preservation of local identity
  * **Personal:** how your rulers and their court interact over generations

  
Bond scores accumulate silently through event chains specific to each subject type (colonial nations, governorates, palatinates, puppets, dependencies, marches, federal subjects). Periodic **status reveal events** show what your subjects think of you.  
  
In the **Age of Revolutions** , accumulated bond scores resolve into **one-shot payoff events**. Subjects with high bonds become steady partners, while those with poor bonds may push for independence, defect to rivals, or demand constitutional concessions.  
  
Gated by the **C &C: Overlord-Subject Bonds** game rule (default: on).  
  


* * *

  
  


### New Subject Types

  
  
There are many new subject types to diversify and enhance subject-based gameplay:  


  * Progressively tighten control over loosely aligned states, though they can be more troublesome than they are worth.
  * Release special OPM states for specific benefits: cultural, research, prestige, naval governor capacity.
  * Strong marcher and governorate subjects during the imperial era, setting up Napoleonic-era consolidation, rebellions, and breakaway regions.

  
Some subject types require a matching estate privilege or government reform (at least one when there are options):  


  * Elite Enclave
  * Scientific College
  * Naval Administration
  * Provincial Governorate
  * Tax Farm
  * Military March

  
**Personal Union**  


  * **Junior Partner** _(unlocks Age 2)_ : A Junior Partner retains its own ruler and conducts independent foreign policy, yet acknowledges the preeminence of its overlord.
  * **Lesser Partner** _(unlocks Age 2)_ : A Lesser Partner is the maturation of a Junior Partner after fifty years of shared dynasty.

  
**Shadow / Client**  


  * **Shadow State** _(unlocks Age 2)_ : A Shadow State is formally independent, bound only by secret treaty and discreet arrangement.
  * **Client State** _(unlocks Age 3)_ : A Client State is a nation brought into the orbit of a stronger power through treaty or released provinces.
  * **Puppet State** _(unlocks Age 5)_ : A Puppet State is a formerly independent nation brought under full administrative supervision of its overlord.

  
**Elite & Cultural**  


  * **Elite Enclave** _(unlocks Age 2)_ : An Elite Enclave is a culturally kindred domain granted self-governance in recognition of its noble heritage.
  * **Palatinate** _(unlocks Age 4)_ : A Palatinate is an Elite Enclave that has grown into a semi-sovereign power.
  * **Artists ' Commune** _(unlocks Age 2)_ : An Artists Commune is a self-governing community of painters, sculptors, and craftsmen whose works redound to their patron's glory.
  * **Scientific College** _(unlocks Age 4)_ : A Scientific College is a scholarly institution of a religiously governed polity, free to pursue learning on behalf of its patron.
  * **Naval Administration** _(unlocks Age 3)_ : A Naval Administration is a port town granted semi-independence to manage the maritime logistics of its patron's fleet.

  
**Trade**  


  * **Associated Republic** _(unlocks Age 2)_ : An Associated Republic is an independent republican state under formal patronage.
  * **Chartered Company** _(unlocks Age 5)_ : A Chartered Company is a royally chartered trading corporation operating in distant lands on behalf of its overlord.

  
**Governance**  


  * **Protectorate** _(unlocks Age 3)_ : A Protectorate is a weaker neighboring state under the protection of a stronger power without formal subjugation.
  * **Crown Dependency** _(unlocks Age 2)_ : A Crown Dependency is a realm bound to its overlord by ties of shared dynasty, where the same ruler family governs both courts without a formal personal union.
  * **Holy Protectorate** _(unlocks Age 4)_ : A Holy Protectorate is a coreligionist state taken under the spiritual patronage of a larger power.
  * **Provincial Governorate** _(unlocks Age 5)_ : A high-autonomy administrative region governed by a Crown-appointed magnate.
  * **Tax Farm** _(unlocks Age 5)_ : An exploitative extraction arrangement in which a powerful lord manages revenue collection in exchange for a portion of the proceeds.
  * **Military March** _(unlocks Age 5)_ : An offensive border vassal given special military charter to project power beyond our frontiers.

  


* * *

  
  


### Protectorate & Holy Protectorate Event Chains

  
  
Protectorates and holy protectorates have a full event arc covering the political life of the relationship from early maturity through its eventual resolution.  
  
**Ward Maturation (cc.220):** after 100 years as a protected state with high opinion and loyalty, the ward can become a full vassal. The available paths depend on your ministers: a grand chancellor orchestrates a diplomatic masterstroke; a consolidation minister establishes an integration framework with a permanent liberty desire bonus; cruel rulers absorb the ward by decree; zealot rulers may treat the transition as a sacred relinquishment. In Age 5+, decline becomes Honorable Release (with a skilled diplomat) or Embarrassing Release (without one). Deeply disloyal wards can demand independence outright.  
  
**Diplomatic Incident Chain (cc.221-223):** your protectorate provokes a hostile neighbor. Defuse the situation, back your ward publicly, or step back and let them face it alone. Each choice branches. Standing firm leads to war, where you can declare using a custom Protectorate Intervention CB or abandon the ward and break the subject relation. Stepping back sends the rival to war against the ward without you, with lasting loyalty damage and possible third-party stigma.  
  
**Ward Ambitions (cc.224):** a developed protectorate with flagging loyalty presses for a better arrangement. Accept their terms (client state or vassal conversion), deny them (tracked, with an independence war after two refusals), or offer a diplomat-brokered recognition deal that frames tighter bonds as partnership.  
  
**Faith Crisis (cc.225):** a disengaged overlord faces a holy protectorate that asks to be released from the arrangement. Release graciously, recommit at religious cost, or refuse. Refuse twice and the ward goes to war for independence, with the Pope potentially joining their side if they are Catholic.  
  
**Patron of the Faith (cc.226):** holding multiple holy protectorates with strong religious engagement triggers a one-time recognition event. Embrace the title for a permanent religious influence and power projection modifier, or use the reputation diplomatically.  
  
**Religion Divergence (cc.227-228):** when overlord and holy protectorate no longer share a faith, the compact has no foundation. Issue a reconversion ultimatum, release the ward graciously, or maintain the arrangement under growing tension. If the ultimatum sits unresolved and loyalty collapses, the ward demands independence, potentially backed by the Pope.  
  
**Catholic Flavor:** Papal opinion reacts throughout. The Pope disapproves when a holy protectorate is dissolved into a secular vassal, approves of gracious releases, can mediate faith crises between Catholic parties, formally recognizes an overlord as Patron of the Faith, and may join independence wars for Catholic wards abandoned by a faithless or apostate overlord.  
  


* * *

  
  


### Frontier Governance

  
  
Realms that push into terrain they cannot easily urbanize or road-connect have always struggled to hold those gains: Muscovy and Novgorod across the steppe, the Ottomans through the Anatolian and Kurdish mountains, and the holder of the Mandate of Heaven over its interior. Frontier Governance gives them a tool for it.  
  


  * **Frontier Governor:** a lesser, land-based cousin of the Local Governor. It can be raised in **rural, non-road-connected** provinces, where a true governor cannot go, provided they stay connected to the capital by land, directly or through subjects. It projects less proximity than a full governor and draws from its own small dedicated pool.
  * **Frontier Administration** advance: branch-independent, available in the Age of Renaissance. It unlocks the building and the four frontier estate privileges, and grants the first governor slot. The AI is biased toward adopting it in frontier-prone realms and historical cases (Muscovy, Novgorod, the Ottomans, and the Mandate holder).
  * **Frontier estate privileges:** each estate can specialize the lands around every frontier governor. They refresh yearly and expire if the governor or privilege is lost: **Governance** (nobles: an extra governor slot and tighter local control), **Missions** (clergy: faster conversion toward the state religion), **Markets** (burghers: market access and trade), and **Settlement** (peasants: migration attraction and pop promotion).

  


* * *

  
  


### Era Advances

  
  
New advances have been added across the ages to unlock new subject types and reforms, enhance regional flavor, add gameplay variability, and provide some balancing.  
Some are age-branch (Adm/Dip/Mil) specific; others are cultural, regional, or country based.  
  
Many are mixed into existing tech trees, but there are also new mini-trees in each age past the Renaissance. Mini-trees also have age-branch advances; some have follow-on advances which do not appear in the age picker UI.  
  
**Age of Renaissance** (8 advances)  


  * _[DIP]_ **Royal Union Network** unlocks **Junior Partner, Lesser Partner**. Personal unions need not be passive inheritances.
  * _[DIP]_ **Shadow Diplomacy** unlocks **Shadow State**. Not all influence announces itself.
  * _[ADM]_ **Artistic Patronage** unlocks **Artists ' Commune**. To commission great art is to leave one's mark on time itself.
  * _[MIL]_ **Noble Patronage** unlocks **Elite Enclave**. A wise ruler recognizes that the high nobility, given honored autonomy, will return loyalty rather than resentment.
  * _[DIP]_ **Republican Patronage** unlocks **Associated Republic**. Republics possess a practical genius that monarchies would do well to cultivate.
  * _[ADM]_ **Dynastic Governance** unlocks **Crown Dependency**. The web of royal marriages binding European courts together need not remain ceremonial.
  * _[MIL]_ **Holy Patronage** unlocks **Holy Protectorate**. Faith is a bond stronger than treaty.
  * _[All]_ **Frontier Administration** : Rather than wait for roads and cities to reach the marches, the crown plants resident noble governors directly in the unsettled interior, binding the borderlands to the capital by loyalty where it cannot yet bind them by stone.
+1 frontier governors
  
**Age of Discovery** (15 advances)  


  * _[ADM]_ **Client State Diplomacy** unlocks **Client State**. By offering protection in exchange for tribute, a great power can extend its influence into neighboring territories without the expense of outright conquest.
  * _[DIP]_ **Naval Charter** unlocks **Naval Administration**. A great fleet requires not only ships but infrastructure: dry docks, provisioning networks, and merchant expertise.
  * _[MIL]_ **Protectorate Rights** unlocks **Protectorate**. The law of nations permits a stronger power to declare itself the protector of a weaker neighbor, extending a shield without requiring formal subjugation.
  * _[All]_ **Late Renaissance Ideas** : The humanist thought and classical revival that defined the Renaissance have not ended with a new age.
+1 max literacy, +1 burgher literacy 
  * _[All]_ **Natural Philosophy** : Renaissance thinkers turned their gaze from scripture toward nature itself, cataloguing plants, studying the human body, and laying the ground for the empirical sciences.
+2 life expectancy, +5% disease resistance 
  * _[ADM]_ **Civic Humanism** : Humanist thinkers argue that civic virtue, meaning active participation in governance, rhetoric, and public duty, is the highest expression of human excellence.
+5% cabinet efficiency 
  * _[All]_ **Church Patronage of Learning** : The Church has long been a patron of art and scholarship.
+10% institution growth, +5% pop conversion _(Catholic or Orthodox or Lutheran or Calvinist or Anglican)_
  * _[All]_ **Scholastic Reform** : Catholic theologians have fused Aristotelian logic with Christian doctrine, creating a rigorous intellectual culture in our monasteries and cathedral schools.
+1 clergy literacy _(Catholic)_
  * _[All]_ **Islamic Observatory Tradition** : The great observatories of Samarkand, Cairo, and Istanbul represent a centuries-long Islamic tradition of precise astronomical and medical knowledge.
+2 life expectancy, +10% dip range _(Sunni or Shia or Ibadi, Middle East capital)_
  * _[All]_ **Polymath Networks** : The great cities of the Islamic world are home to polymaths who move freely between mathematics, medicine, philosophy, and engineering.
+5% disease resistance, +5% cultural influence _(Middle East capital)_
  * _[All]_ **Renaissance Court Culture** : The princely courts of Italy have become models of refined learning and artistic patronage.
+5% cultural influence, +3 power projection _(Monarchy)_
  * _[All]_ **Civic Republican Ideals** : Renaissance republicanism drew on ancient Rome to argue that free citizens deliberating together produce wiser law than any monarch alone.
+5% legislative efficiency _(Republic)_
  * _[All]_ **Classical Revival** : Neo-Confucian scholars have renewed attention to the classical texts of antiquity, re-examining the Four Books and Five Classics with fresh commentary.
+5 max literacy, +5% cabinet efficiency _(East Asia capital)_
  * _[All]_ **Examination System Refinement** : Generations of scholarly refinement have made the examination system an extraordinarily precise instrument for selecting capable administrators.
+10% cabinet efficiency _(East Asia capital)_
  * _[All]_ **Italian Masters** : The workshops of Florence, Venice, and Milan have produced an unbroken line of masters in painting, sculpture, and architecture.
+10% art skill, +5% cultural influence _(Italian culture)_
  
**Age of Reformation** (14 advances)  


  * _[ADM]_ **Scholarly Orders** unlocks **Scientific College**. The great religious orders have long been the guardians of learning.
  * _[DIP]_ **Palatinate System** unlocks **Palatinate**. The most elevated noble enclaves may be recognized as palatinates, sovereign-within-sovereign territories whose counts wield near-regal authority.
  * _[MIL]_ **Military Academy** unlocks **Military Academy**. The informal apprenticeship of knights and captains has given way to organized study of strategy, logistics, and the art of war.
  * _[All]_ **Late Discovery Ideas** : A generation of explorers has mapped the contours of a world far larger than our ancestors imagined.
+100 trade range, +150 colonial range 
  * _[All]_ **Systematic Cartography** : Where early explorers navigated by rumor and estimation, a new generation of cartographers brings mathematical precision to the art of the map.
+100 trade range, +10% dip range 
  * _[DIP]_ **Colonial Consolidation** : The era of reckless discovery is giving way to careful consolidation.
+3 subject loyalty, +10% integration speed 
  * _[All]_ **Maritime Republic Trade Networks** : The mercantile republics have long understood that profit lies not in territory but in the control of exchange.
+10% merchant power, +2% maritime merchant power _(Republic)_
  * _[All]_ **Maritime Tribute Networks** : Our great fleets have long projected power through tribute relationships with maritime peoples across the seas.
+150 naval range, +3 subject loyalty _(East Asia capital)_
  * _[All]_ **Missionary Expansion** : Faith follows the flag.
+10% pop conversion, +100 colonial range _(Catholic or Lutheran or Calvinist or Anglican)_
  * _[All]_ **Colonial Ecclesiastical Orders** : The great religious orders (Dominicans, Franciscans, Jesuits) have established missions across our colonial territories, building schools and churches that anchor European civilization in the new world.
+10% institution growth, +100 colonial range _(Catholic, Europe capital, has Colonial Nation subject)_
  * _[All]_ **Iberian Colonial Doctrine** : Spain and Portugal have developed a sophisticated theory of colonial administration: encomienda grants, viceroyalties, and a transatlantic commercial system that channels the wealth of new worlds to Iberian coffers.
+200 colonial range, +5% naval morale _(Iberian culture)_
  * _[All]_ **Atlantic Fleet Doctrine** : The carrack and galleon, heavily armed, deep-hulled ships capable of crossing oceans, represent an Iberian mastery of oceanic warfare.
+15% heavy ship power, +5% naval morale _(Iberian culture)_
  * _[All]_ **Overland Trade Routes** : While European powers struggle to find sea routes around our lands, we command the ancient arteries of overland trade: the Silk Road, the incense routes, the great caravans that have connected East and West for millennia.
+150 trade range, +25 logistics distance _(Sunni or Shia or Ibadi)_
  * _[All]_ **Silk Road Revival** : By securing the caravan routes, investing in caravanserais, and negotiating safe passage agreements, we restore the Silk Road to something of its former glory, channeling the wealth of Asia through our markets.
+150 trade range, +15% dip range, +10% merchant power _(Sunni or Shia or Ibadi, Middle East capital or Central Asia capital)_
  
**Age of Absolutism** (22 advances)  


  * _[DIP]_ **Naval Administration** : The state establishes a permanent admiralty board to oversee distant naval stations, extending royal control over the seas.
  * _[DIP]_ **Puppet State Administration** unlocks **Puppet State**. Shadow influence must eventually give way to direct administration.
  * _[DIP]_ **Chartered Trading Companies** unlocks **Chartered Company**. The merchant classes have demonstrated an unparalleled capacity for organizing commerce at global scale.
  * _[ADM]_ **Provincial Governance** unlocks **Provincial Governorate**. A formalized system of Crown-appointed governorates allows the realm to extend administrative reach over distant regions without direct annexation.
  * _[MIL]_ **Tax Farming** unlocks **Tax Farm**. Contracting the collection of revenues to powerful local lords, at a price.
  * _[MIL]_ **Military Marches** unlocks **Military March**. Designating border territories as military marches creates offensive buffers that extend our power at the frontier.
_(has Military Academy subject, has Elite Enclave subject or has Palatinate subject)_
  * _[All]_ **Late Reformation Ideas** : A century of religious upheaval has exhausted many, but its legacy is real: confessions are clearer, institutions more self-aware, and hard-won settlements give the realm a cautious stability that prior generations could not imagine.
+5% pop conversion 
  * _[ADM]_ **Confessional State Building** : The lesson drawn from the Wars of Religion is that a stable realm requires a unified confession, or at least a carefully managed one.
+1 reform slots 
  * _[All]_ **Protestant Church-State** : Protestant reformers insisted that the Word of God, accessible to all who can read, must be the foundation of a Christian realm.
+5 max literacy, +5% cabinet efficiency _(Lutheran or Calvinist or Anglican)_
  * _[All]_ **Lutheran Educational Legacy** : Luther's insistence on every Christian reading Scripture for themselves drove the establishment of parish schools across Protestant Europe.
+5 max literacy _(Lutheran or Calvinist or Anglican, Europe capital)_
  * _[All]_ **Catholic Confessional Legacy** : The Council of Trent revitalized Catholic institutions, clarifying doctrine, reforming the clergy, and establishing new religious orders dedicated to education and pastoral care.
+10% institution growth _(Catholic)_
  * _[All]_ **Jesuit Reform Networks** : The Society of Jesus operates schools, universities, and missions across three continents, transmitting the methods of rigorous Tridentine Catholicism wherever European colonialism has reached.
+10% institution growth, +100 colonial range _(Catholic, Europe capital, has Colonial Nation subject)_
  * _[All]_ **Confessional Consolidation** : In an age when European powers fight over doctrine, Islamic rulers face their own choices between Sunni orthodoxy, Shia devotion, and syncretic practice.
+10% pop conversion, +3 power projection _(Sunni or Shia or Ibadi)_
  * _[All]_ **Millet Administrative System** : The Ottoman millet system, which grants recognized religious communities legal autonomy under their own institutions, has proven a remarkably effective tool for governing a diverse empire.
+10% integration speed, +3 subject loyalty _(Sunni or Shia or Ibadi, Middle East capital)_
  * _[All]_ **Post-War Religious Settlement** : Decades of religious war have produced exhausted pragmatism: most rulers now accept that forcing universal religious conformity is too costly.
+1 tolerance (heretic) 
  * _[All]_ **Westphalian Sovereignty Doctrine** : The Peace of Westphalia established a new framework for European politics: states are sovereign within their own borders, and the principle of cuius regio, eius religio gives rulers authority over their realms' confessional identity.
+10% dip range, +3 subject loyalty _(Western Europe capital)_
  * _[All]_ **Syncretic Tolerance** : India's extraordinary religious diversity has long required its rulers to practice a degree of tolerance unknown in Europe.
-5% pop conversion, +5% cultural influence, -5% cultural tradition _(South Asia capital)_
  * _[All]_ **Sulh-e-Kul** : Akbar's doctrine of sulh-e-kul, or universal peace, argued that a wise ruler stands above sectarian division, drawing legitimacy from all his subjects regardless of faith.
+10% integration speed, +10% cultural influence _(South Asia capital)_
  * _[All]_ **Court of Universal Tolerance** : Our court has become a meeting place for scholars of every tradition: Hindu pandits, Muslim ulama, Jain monks, Sikh teachers, and European missionaries all find a welcome audience.
+5% cabinet efficiency _(South Asia capital)_
  * _[All]_ **State Orthodoxy** : By aligning state ritual and institutional practice with an orthodox tradition, whether Confucian, Buddhist, or Shinto, our government projects continuity, legitimacy, and cultural coherence across our realm.
+5% pop conversion, +5% cabinet efficiency _(East Asia capital)_
  * _[All]_ **Confucian Bureaucratic Faith** : Neo-Confucian state philosophy has fused ritual, ethics, and administrative technique into a seamless whole.
+10% cabinet efficiency, +1 reform slots _(East Asia capital)_
  * _[DIP]_ **Balance of Power Doctrine** : The art of statecraft matures into a science of equilibrium: alliances assembled and dissolved, subsidies and guarantees, all turned to the single end of preventing any rival from dominating the continent.

  
**Age of Revolutions** (18 advances)  


  * _[ADM]_ **Colonial Assemblies** : Establish representative assemblies in our colonial territories, giving local leadership a formal voice in imperial governance.
+5 subject loyalty, +10% integration speed _(has Colonial Nation subject or has Client State subject or has Shadow State subject or has Chartered Company subject)_
  * _[ADM]_ **Federal Constitution** unlocks **Imperial Council Member, Federal Member, Associate Member**. Draft a constitutional framework for imperial federation, granting colonial assemblies legislative standing within a broader federal parliament.
+5 subject loyalty, +10% integration speed 
  * _[DIP]_ **Imperial Trade Compact** : Formalize an empire-wide preferential trade zone, binding the colonies to the metropole through shared commercial interest.
+1 dip rep, +10% trade center power _(has Colonial Nation subject or has Client State subject or has Shadow State subject or has Chartered Company subject)_
  * _[DIP]_ **Federal Charter** unlocks **Federal Charter Holder**. Issue federal charters to existing colonial and client territories.
+1 dip rep 
  * _[All]_ **Late Absolutism Ideas** : The age of absolute monarchy has passed its zenith, but its achievements endure: centralized bureaucracies, permanent armies, and rationalized state finances are now the baseline from which even reformers must begin.
+5% cabinet efficiency 
  * _[ADM]_ **Enlightened Administration** : Enlightenment thought has reached the corridors of power.
+5% legislative efficiency 
  * _[All]_ **Enlightened Despotism** : Frederick of Prussia, Catherine of Russia, and Joseph of Austria, the great enlightened despots, show that absolute power need not mean arbitrary power.
+1 reform slots, +5% cabinet efficiency _(Monarchy)_
  * _[All]_ **Reform from Above** : Faced with the threat of revolution from below, wise rulers choose reform from above.
+5 max literacy _(Monarchy, Europe capital)_
  * _[DIP]_ **Mercantilist Legacy** : Two centuries of mercantilist policy have created sophisticated trading institutions: regulated companies, customs regimes, navigation acts, and state banks.
+25% trade range, +15% merchant power, -1% bank interest _(Republic)_
  * _[All]_ **Colonial Mercantile System** : Our colonial empire is now a mature economic system: plantation agriculture, monopoly trade companies, navigation acts, and silver flows all converge to channel colonial wealth into the metropole.
+5% sea trade efficiency, +10% merchant power, +5 subject loyalty _(Europe capital, has Colonial Nation subject)_
  * _[MIL]_ **Professional Standing Army** : The military revolution has reached its culmination: every major power now maintains a permanent, paid, uniformed army rather than relying on feudal levies or mercenaries.
+2% discipline, +25 logistics distance 
  * _[All]_ **Prussian Discipline** : Prussia's army has become the envy and model of Europe: relentless drill, cadenced marching, and a culture of obedience that makes the Prussian musketeer the most precisely controllable soldier on any battlefield.
+10% tactics, +5% land morale _(German culture)_
  * _[All]_ **General Staff System** : The Prussian innovation of a permanent general staff, officers who plan campaigns, map terrain, and war-game scenarios before battles begin, transforms warfare from an art into a science.
+2% discipline, +10% tactics _(German culture)_
  * _[All]_ **New Order Military Reform** : Reformist viziers and sultans have recognized that European military methods represent a genuine challenge.
+10% tactics, +2% discipline _(Sunni or Shia or Ibadi, Middle East capital)_
  * _[All]_ **Qing Administrative Consolidation** : The Qing conquest has not replaced Chinese administrative culture; it has absorbed and perfected it.
+10% cabinet efficiency _(East Asia capital)_
  * _[All]_ **Bureaucratic Peak** : Our administrative tradition has reached a summit of refinement.
+1 reform slots, +1 max literacy _(East Asia capital)_
  * _[All]_ **Administrative Sophistication** : Indian states have developed elaborate traditions of revenue administration, provincial governance, and fiscal management.
+5% cabinet efficiency, +20% loan capacity _(South Asia capital)_
  * _[All]_ **Fiscal Administration** : The Maratha confederacy has demonstrated that decentralized revenue farming, when combined with effective military power and political skill, can build a formidable state from a fragmented beginning.
+10% merchant power _(South Asia capital)_
  


* * *

  
  


### New Estate Privileges & Government Reforms

  
  
**Estate Privileges**  


  * **Shadow Network** _(via: Shadow Diplomacy)_
+0.33 noble power, +5 power projection, +1 dip rep _(Nobles >=35%)_
  * **Patronage of the Arts** _(via: Artistic Patronage)_
+0.25 noble power, +20 cultural tradition, +10% cultural influence 
  * **Noble Enclave Rights** _(via: Noble Patronage)_
+0.5 noble power, +0.05/mo prestige, +50 cultural influence _(Nobles >=35%)_
  * **Naval Charter** _(via: Naval Charter)_
+0.25 burgher power, +5% sailors, +5% naval morale, +1 naval governors _(Burghers >=30%)_
  * **Scholarly Brotherhood** _(via: Scholarly Orders)_
+0.25 clergy power, -10% institution embrace cost, +5% institution growth, +5% research _(Clergy >=35%)_
  * **Military Academy Charter** _(via: Military Academy)_
+0.25 noble power, +0.1/mo army tradition, +1% discipline _(Nobles >=30%)_
  * **Royal Trading Charter** _(via: Chartered Trading Companies)_
+0.25 burgher power, +5% trade center power, +1 dip capacity _(Burghers >=40%, has Colonial Charter reform)_
  * **Governorate Charter** _(via: Provincial Governance)_
+0.25 noble power, +0.002/mo dev, +5% noble agenda _(Nobles >=25%)_
  * **Tax Charter** _(via: Tax Farming)_
+0.25 burgher power, -8% bureaucracy removal cost _(Burghers >=30%)_
  * **March Charter** _(via: Military Marches)_
+0.33 noble power, -10% light cav cost, -5% heavy cav cost _(Nobles >=35%)_
  * **Noble Diplomatic Corps** _(via: Balance of Power Doctrine)_
+0.2 noble power, +1 dip capacity, +1 dip rep, +0.03/mo prestige _(Nobles >=30%)_
  * **Frontier Governance** _(via: Frontier Administration)_
+1 frontier governors, +0.1 noble power _(Nobles >=25%)_
  * **Frontier Missions** _(via: Frontier Administration)_
+0.1 clergy power _(Clergy >=12%)_
  * **Frontier Markets** _(via: Frontier Administration)_
+0.1 burgher power _(Burghers >=12%)_
  * **Frontier Settlement** _(via: Frontier Administration)_
+0.1 peasant power _(Peasants >=10%)_
  
**Government Reforms**  


  * **Naval Administration** : The establishment of a permanent admiralty board extends royal authority over distant naval stations, enabling an additional naval governorship and reducing the cost of maintaining far-flung ports. _(via: Naval Administration)_
+1 naval governors, +5% naval morale, -1 port distance cost 
  * **Colonial Charter System** : The crown establishes a formal legal framework for issuing royal charters to commercial enterprises operating in distant lands, granting them military and commercial authority in exchange for tribute and loyalty. _(via: Chartered Trading Companies)_
+1 dip capacity, +5% sailors 
  * **Governorate System** : Formalizes the system of Crown-appointed provincial governorates, improving administrative capacity across the realm. _(via: Provincial Governance)_
+2 dip capacity, +0.003/mo dev, -8% reform removal cost 
  * **Tax Farming Contracts** : Systematizes the practice of farming out tax collection to powerful lords, reducing bureaucratic overhead in exchange for local efficiency. _(via: Tax Farming)_
+1 dip capacity, -10% bureaucracy removal cost 
  * **March Charter** : Issues formal charters to border territories designating them as military marches, creating a network of offensive buffers along the realm's most contested frontiers. _(via: Military Marches)_
-8% light cav cost, -5% antagonism received, +10% noble agenda 
  * **Balancer 's Doctrine**: Our diplomacy is organised around the maintenance of equilibrium, winning us reputation and the diplomatic reach to assemble coalitions while blunting the antagonism our maneuvering provokes. _(via: Balance of Power Doctrine)_
+2 dip capacity, +1 dip rep, -10% antagonism received 
  * **Raison d 'État**: Policy is governed by the cold calculus of state interest rather than dynastic sentiment or confessional loyalty, lending our statecraft flexibility, prestige, and resilience in protracted struggles. _(via: Balance of Power Doctrine)_
+1 dip capacity, +0.03/mo prestige
  


* * *

  
  


### Event Categories

  
  
  
Namespace| Events| Description  
---|---|---  
  
cc_cabinet| 21| Minister counsel, estate relations, diplomatic situations, provincial affairs  
  
cc_traits| 20| Age trait acquisition, ruler teaching, peer learning  
  
cc_cond| 16| Conditional trait spawning based on realm conditions and actions  
  
cc_synergy| 28| Trait pair synergies: temporary bonuses when ministers share trait families  
  
cc_neg| 21| Underperformance events and rehabilitation chains  
  
cc_wealth| 10| Wealth hoarding pressure and minister enrichment  
  
cc_dual| 10| Cabinet × religious figure dual-role synergies  
  
cc_intl| 12| Cross-country interactions between neighboring courts  
  
cc_feudal| 8| Feudal era court events  
  
cc_legacy| 3| Senior minister retirement and legacy transmission  
  
cc_legend| 6| Legendary minister quest chains  
  
cc_hyw| 11| Hundred Years War flavor: FRA/ENG war outcomes, observer reactions, vassal defection pressure  
  
cc_personality| 18| Dynamic AI personality inflection events at key historical turning points  
  
cc_bonds| 110| Overlord-subject bond system: per-type chain events, monitor, status reveals, AoR payoffs  
  
cc_rival| 4| Court rivalry escalation: minister complaint → letter unsealed → faction hardens  
  
cc_cabal| 3| Cabinet alliance formation: alliance forms → joint reform proposal  
  
cc_wc| 9| War council: active-war events, post-war reform proposals, outdated general retirement  
  
cc_fac| 3| Estate faction capture events  
  
cc_prog| 14| Stepping stone trait progression chains (Paths A/C/D/F/E)  
  
cc_colonial| 6| Colonial divan: charter company events + decolonization crisis chain  
  
cc_posting| 4| Colonial posting duty: dispatch, corruption, native uprising, fever  
  
cc_hus| 1| Hussite Wars papal loan event  
  
cc| 76| Protectorate & holy protectorate chains: ward maturation, diplomatic incidents, faith crises, religion divergence, papal interactions  
  
cc_invasion_mexico| 28| Mexican Conquest situation: expedition decisions, Mesoamerican reactions, confederation events, conquest resolution  
  
cc_balance_of_power| 52| European Balance of Power situation: alignment, congresses, Napoleonic-era warfare/economy/diplomacy events, and the four endings  
  
  
  
 _~494 events total_  
  


* * *

  
  


### Hundred Years War Flavor

  
  
A system of historical events and starting modifiers for the Hundred Years War situation, activated by the **C &C: Hundred Years War Flavor** game rule (default: on).  


  * **France and England** begin with historical starting modifiers for their positions at the opening of the conflict: French levy readiness and English estate pressure.
  * **War outcome events** fire when either side wins or loses major wars, stacking levy and estate effects over time to reflect the shifting fortunes of the conflict.
  * **Observer power reactions:** Burgundy, Castile, and Aragon witness western European wars and may choose sides or demand concessions (cc_hyw.12/13).
  * **Vassal defection pressure:** French and English vassals face events when their suzerain suffers defeat, with opportunities to renegotiate terms or waver in loyalty (cc_hyw.20-23).
  * **Lowlands incursion events:** when France or England take land in the Lowlands during the HYW, their Lowlands subjects or the local population may demand the land be transferred to them, on pain of political crisis (cc_hyw.30/31).
  * **The Auld Alliance** (cc_hyw.1): France can formally guarantee Scottish independence, binding England's northern flank and setting up the FRA-SCO-ENG triangle.
  * **Replace Appanage Ruler decision:** France can replace disloyal appanage lords to consolidate control, at the cost of other vassals' opinions.

  
_~11 events spanning France, England, Scotland, Burgundy, and observer powers._  
  


* * *

  
  


### Hussite Wars Flavor

  
  
When the Hussite Wars situation fires and Bohemia fights the Papacy, the **C &C: Hussites, One Small Loan** game rule (default: on) enables a flavored papal outreach event:  


  * **The Pope Calls for Aid:** the Pope approaches the strongest Catholic power with coin, asking them to enter the crusade on Rome's side.
  * Catholic countries already in the war can accept or demand more; those on the opposing side can defect for gold; neutral powers can weigh in diplomatically.
  * This may seem silly and unbalanced, especially since it always prefers a Catholic player country and the sum is large. It is only a fraction of the Pope's treasury.

  


* * *

  
  


### Dynamic AI Personalities

  
  
AI countries evolve their strategic personality across the ages, shifting from aggressive early expansion to defensive consolidation, commercial pragmatism, or cautious decline as the game progresses. Controlled by the **C &C: Dynamic AI Personalities** game rule (default: Dynamic Historical + Drift).  
  
**27 countries** have historically-informed personality arcs covering all six ages:  
_TUR, FRA, ENG, MOS, CAS, HAB, POR, SWE, POL, LIT, DAN, BUR, VEN, PAP, GEN, BYZ, HUN, MAM, ETH, MNG, SHO, KOR, NOG/GLH, NAP, SCO, MLO, MLI/SON_  
  
**Key inflection events** fire at historical turning points and give AI-controlled countries a choice between the historical personality and an alternative:  


  * **The Conquering Sultan** (TUR, Age 3): peak Selim/Suleiman-era aggressive expansion
  * **The Long Stagnation** (TUR, Age 4): early Ottoman institutional decline begins
  * **The Sun King Rises** (FRA, Age 5): Louis XIV's absolutist ambition
  * **Britannia 's Maritime Empire** (ENG, Age 5): English commercial and naval dominance
  * **The Terrible Tsar** (MOS, Age 3): Ivan the Terrible's consolidation
  * **The New World Empire** (CAS, Age 3): Castilian colonial and imperial apex
  * **The Great Northern Reckoning** (SWE, Age 4): Swedish imperial overstretch

  
After a historical event fires, an **AI personality guard** prevents random drift from overriding the fresh assignment for about 20 years.  
  
**Game rule modes:**  


  * **Vanilla:** no changes; vanilla personality assignment only
  * **Dynamic Historical:** major powers follow age-based personality arcs and fire inflection events at key turning points
  * **Dynamic Drift Only:** context-driven drift shifts personality for all AI countries based on war outcomes, power, and wealth
  * **Dynamic Historical + Drift** _(default)_ : both historically-grounded arcs for major powers and context drift for everyone else

  
 _~18 inflection events; drift logic fires on yearly and four-yearly pulses for all AI countries._  
  


* * *

  
  


### Game Rules

  
  
All rules are toggleable in the game setup screen before starting a session.  
  
**C &C: France, Lowlands Containment**  
Gives France's Lowlands-culture neighbors elevated antagonism toward France at game start, decaying over 200 years.  


  * **Enabled** _(default)_ : France begins under pressure from its Lowlands neighbors, reflecting historical anxieties about French hegemony.
  * **Disabled** : France starts with no extra antagonism from its neighbors.

  
**C &C: Wealth Hoarding Events**  
When enabled, countries that hoard gold above 100x their monthly income will periodically face events representing court demands and economic pressure.  


  * **Enabled** _(default)_ : Wealth hoarding events fire from the biyearly pulse when the gold threshold is met.
  * **Disabled** : No wealth hoarding events will fire.

  
**C &C: Mamluks, Foreign Rule Strain**  
Gives the Mamluks starting penalties reflecting their status as a foreign military caste ruling over native Egyptians.  


  * **Enabled** _(default)_ : The Mamluks begin with a permanent peasant levy penalty and decaying military strain, easing over 200 years.
  * **Disabled** : The Mamluks start with no historical penalties.

  
**C &C: Ottomans, Colonization**  
Prevent the Ottomans from colonizing.  


  * **Prevent Colonization** _(default)_ : The Ottomans are permanently prevented from colonizing.
  * **Allow Colonization** : The Ottomans may still colonize as normal.

  
**C &C: Dynamic AI Personalities**  
Controls whether AI countries evolve their grand strategies across ages and shift in response to game events.  


  * **Vanilla** : No changes. AI personalities use vanilla historical assignments and random rules only.
  * **Dynamic Historical** : Major powers follow historically-informed personality arcs across ages. Key turning points fire choice events with a historical option and one or two alternatives.
  * **Dynamic Drift Only** : Adds context-driven personality changes for all AI countries, shifting in response to war, power, wealth, and circumstance.
  * **Dynamic Historical + Drift** _(default)_ : Adds context-driven drift events for all AI countries, shifting personalities in response to war, power, wealth, and circumstance. Major powers follow historically-informed personality arcs across ages. Key turning points fire choice events with a historical option and one or two alternatives. Historical events still guard against random drift for ~20 years after they fire.

  
**C &C: France, Hundred Years War Flavor**  
Enables historical flavor for the Hundred Years War: starting levy and estate modifiers for France and England, war outcome stacking, vassal defection pressure events, observer power reactions, and the Replace Appanage Ruler decision.  


  * **Enabled** _(default)_ : France and England start with historical modifiers; war outcomes stack levy and estate effects over time; Burgundy, Brittany, and other vassals may waver when their suzerain suffers defeat.
  * **Disabled** : No HYW-specific starting modifiers, stacking events, or vassal defection pressure will fire.

  
**C &C: Overlord-Subject Bonds**  
When enabled, tracks 5 relationship dimensions (economic, military, political, cultural, personal) across large long-term subjects. Player choices across Ages 1-4 determine how subjects behave in the Age of Revolutions. Most tracking is hidden; consequences appear decades later.  


  * **Enabled** _(default)_ : Detailed multi-dimensional run-spanning subject event-chains, sentiments, and profiles.
  * **Disabled** : Normal subject relationships, bond tracking and event chains disabled.

  
**C &C: Custom Subject Types**  
Controls whether the mod's custom subject types (personal-union partners, shadow and client states, elite enclaves, chartered companies, cultural communes, provincial governorates, tax farms, marches, federal members, and the rest) are available. The toggle gates every advance that unlocks these subjects.  


  * **Enabled** _(default)_ : The advances that unlock the mod's custom subject types appear in the tech tree for every country, alongside their estate privileges and government reforms.
  * **Player Only** : Only human-controlled countries can research these advances and create the custom subjects. AI countries are limited to vanilla subject types.
  * **Disabled** : Those advances never appear, so the custom subjects cannot be created. Only vanilla subject types remain, and the related event chains stay dormant.

  
**Cc Invasion Mexico**  


  * **Enabled** _(default)_ : The Mexican Invasion situation will fire for eligible countries.
  * **Disabled** : The Mexican Invasion situation will not fire.

  
**C &C: Colonial Consolidation**  
When enabled, mid/late-colonial (Age of Absolutism onward) event chains fire for colonial empires: border friction between adjacent colonies of incompatible cultures, consolidation of kindred colonies into viceroyalties, and the hardening of colonial labor and demographic regimes.  


  * **Enabled** _(default)_ : Colonial border friction, viceroyalty consolidation, and labor/demographic event chains will fire from the Age of Absolutism onward.
  * **Disabled** : Colonial consolidation and border friction event chains are disabled.

  
**C &C: Balance of Power**  
When enabled, a two-pole great-power situation can arise across Europe and the Near-East: an aspiring Preponderant Bloc checked by a Balancing Coalition. It begins once a great power adopts the balance-of-power doctrine (Age of Absolutism) or once the revolutionary era opens, and ends through hegemony, an eastern deluge, revolution, or a lasting Concert of Europe.  


  * **Enabled** _(default)_ : The European Balance of Power situation will fire for eligible great powers.
  * **Disabled** : The European Balance of Power situation is disabled.

  
**Cc Cc One Small Loan**  


  * **Enabled** _(default)_ : Papal one small loan events will fire depending on your stance during hussite crusades.
  * **Disabled** : No Papal one small loan events will fire.

  


* * *

  
  


### Country Starting Modifiers

  
  
**France: Hundred Years War Flavor** _(default: on)_  
France begins with historical modifiers for its position at the opening of the Hundred Years War: levy readiness, estate pressure, and elevated antagonism from its Lowlands-culture neighbors. The Lowlands antagonism decays over 200 years. France also starts with a permanent modifier for its expansionist posture toward the Lowlands.  
  
**England: Hundred Years War Flavor** _(default: on)_  
England begins with estate and levy modifiers for its precarious continental position at the start of the Hundred Years War: a kingdom stretched across the Channel with ambitious claims and restless nobles.  
  
**Mamluks: Foreign Rule Strain** _(default: on)_  
The Mamluks begin with a permanent peasant levy penalty (for their status as a foreign military caste ruling over native Egyptian society) and a severe military strain modifier that decays over 200 years. Together these represent the fragility of Mamluk rule, which eases as the regime stabilizes, if it does.  
  
**Ottomans: No Colonization** _(default: on)_  
The Ottomans are permanently prevented from colonizing overseas. This reflects the historical Ottoman orientation as a land empire focused on Anatolia, the Balkans, and the Middle East, rather than competing in Atlantic exploration.  
  


* * *

  
  


### Coming in Future Updates

  
  
Several expansion pillars are designed and planned for future releases:  


  * **The Scholar 's Court:** Age 5 to 6 empiricism events; the Royal Academy building; Scholasticism versus Empiricism cabinet tensions
  * **Succession Crisis Cabinet:** regency events, dynastic drama, and cabinet behavior during interregna and heir disputes
  * **Religious Cabinet Tensions:** the Reformation splits courts; confessional traits; inquisitorial pressure events
  * **The Congress System:** multi-country diplomatic theater; congress events where great power ministers interact directly
  * **More Historical Flavor:** Ottoman, Italian, Spanish, Mughal, and French court event chains

  


* * *

  
  


## Compatibility

  


  * No replace_paths; fully additive, compatible with other mods that don't replace the same files
  * May still be safe to enable on existing saves, but not recommended (new content will start appearing as events fire)
  * Multiplayer synchronized
  * May affect game balance, since cabinet members and new subjects provide many bonuses
  * Generally mod-compatible, as long as other mods don't modify character traits heavily
    * Not tested with other subject mods; they were unstable in testing

  
Tested with:  


  * Hussite, Austria, Brandenburg, Timur, and Ottoman flavor packs
    * Ottoman and Hussite flavor pack CBs are not well limited and cause the AI to misuse them.
  * Community Flavor Pack
  * Overseas Naval Governors
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

  


* * *

  
  


## AI Use Disclosure

  
  
Numerous AI agents were used in the creation of this project: Claude, Gemini, Qwen, Flux.  
  


* * *

  
  


## Feedback & Bugs

  
  
Report issues on the Steam Workshop discussion page or the mod's [GitHub repository](https://github.com/wtmenten/flavorium-universalis).
