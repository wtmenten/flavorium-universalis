# Goods modding

**Source:** https://eu5.paradoxwikis.com/Goods_modding

---

**Goods modding** involves the creation of new good types, adding raw materials to game start, and defining demands of pops.

## Good type modding

Good type modding involves the creation of new good types.

### Example

```
copper = {
	method = mining
	category = raw_material
	color = goods_copper
	default_market_price = 3
	transport_cost = 2
}
```

### Creating raw materials

Goods can be marked as raw materials using `category = raw_material`. If the created good is not meant to be a raw material, it should be explicitly marked as such using `category = produced`.

Raw materials need to have a gathering type specified using `method`. There are 5 gathering types available and `farming` is the default one:

- `mining`
- `farming`
- `hunting`
- `gathering`
- `forestry`

### Basic attributes

`color` is an attribute to associate a good with a color for mapmode purposes - the RHS uses color notation.

`food` is a number of food units that this good produces for the province.

`default_market_price` is the default price of the good when supply and demand are equal to each other.

`transport_cost`, default 1, is the measure of how pricy this good is to transport when importing and exporting. Goods that are harder to transport will yield less in trade income.

### Slaves good

There needs to be one and only one good marked with `is_slaves = yes`.

### Base production

Some goods can be made to be produced in every location with `base_production`. Every location in a market will then supply the market with this value times scaled by development (0 for 0 development, 1 for 100 development). The right side is a number but not a script value.

### Tags

Goods can be given tags by using `custom_tags`, which accept a list of strings:

```
custom_tags = {
	lategame_manufactory
	guild
}
```

Those can then be checked using has_tag trigger.

### Pop type demands

Basic values for pop demands are handled via pop_demand goods category. Goods, in addition, have two fields to impact goods demand on pop type basis that accept pop type (and a few other wildcards) - value pairs. Those fields are `demand_add` and `demand_multiply`.

Example:

```
demand_add = {
	all = 0.001
}
demand_multiply = {
	upper = 2
	slaves = 0
	tribesmen = 0
}
```

Demand add will add the right-side amount of demand per pop type and multiply will multiply the value added by add.

Regarding wildcards:

- `all` is a wildcard that stands for all pop types
- `upper` is a wildcard that stands for pop types that are "upper class", i.e. pop types that have `upper = yes` attribute.
`wealth_impact_threshold` attribute works similarly to make pops only demand the good if their estates' wealth meets the declared threshold. It uses the same syntax.

### Other parameters

- `block_rgo_upgrade = yes` can be used to block rgo expansion of this good.
- `inflation = yes` marks this good as one that may cause inflation when produced. The inflation is calculated as this goods' share of total good production multiplied by INFLATION_RGO_INCOME_FACTOR define (Vanilla value: `2`)
- `development_threshold` is the development value a location needs to reach before pops in it will starting demanding this good.

### Ai importance

There are two ways to impact the AI when it comes to goods - `ai_rgo_size_importance` and `ai_rgo_expansion_priority` - both accept numbers but not script values.

`ai_rgo_size_importance`, default value 1, is used to increase the value of rgo size modifiers in the location. This value is multiplied with the market price of the good and AI_RGO_SIZE_PRICE_UTIL define (Vanilla value: `0.02`)

`ai_rgo_expansion_priority` is used to determine AIs priority for expanding this good when it is in shortage of it - used for RGOs that are important for the economy to function.

### Hardcoded goods

There is one good that the game needs access to internally: `tools`.

### Modifier types

Every good should also have modifier types associated with it:

- `ban_exports_of_<key>` - used for embargos
- `ban_imports_of_<key>` - used for embargos
- `local_<key>_output_modifier` - used for increasing local goods production
- `global_<key>_output_modifier` - used for increasing country-wide goods production
- `can_extract_<key>` - determined if a country can benefit from RGO of this good

### Localisation

Every good should have its name and desc localized with:

- `<key>`
- `<key>_desc`
As well as any modifier types it would use.

### Icons and illustrations

While trade goods follow the familiar icon folder logic like other objects - it must also be specified that trade goods also have illustrations placed in path defined by TRADE_GOODS_ILLUSTRATION_PATH define (Vanilla value: `"gfx/interface/icons/trade_goods/illustrations"`).

Moreover, entries for both illustrations and icons need a prefix defined by GOODS_ICON_PREFIX define (Vanilla value: `"icon_goods_"`).

## Good demands modding

Good demands are good-value pairs that represent the good needs of certain in game objects. While technically the right side accepts script values, those script values only work in the case of pop demands - a special case of good demands.

### Example

```
road_maintenance = {
	lumber = 0.02
	masonry = 0.02
	sand = 0.01
	category = building_maintenance
}
```

### Syntax

Besides the good-value pairs, good demands also accept the following three attributes:

- `copy_from` accepts a key of a previously defined goods demand. When a good demand is copied over, its values are added onto existing entries, or added if there is no such good demand already existing.
- `hidden = yes` will hide the tooltip for the demand.
- `category` is used to assign a category of a goods demand.

### Hardcoded demands

These are demands that the game requires to function:

- `grant_privilege`
- `revoke_privilege`
- `set_cabinet_action`
- `set_cabinet_member`
- `remove_government_reform`
- `embrace_institution`
- `market_create_demand`
- `market_destroy_demand`
- `default_construct_building`
- `capital_movement_demand`
- `create_supply_depot`
- `pop_demand`
- `minting_maintenance`
- `colonial_charter_maintenance`
- `slave_rgo_demands`
- `create_sea_exploration`
- `create_land_exploration`
- `create_conquistador`
- `upgrade_rgo_demand_farming`
- `upgrade_rgo_demand_mining`
- `upgrade_rgo_demand_gathering`
- `upgrade_rgo_demand_hunting`
- `upgrade_rgo_demand_forestry`

### Pop demands

Pop demands are a special case of goods demand - they fully accept the use of script values. Such pop demands are done in the `pop_demand` good demand.

```
pop_demand = {
	wine = {      # Demand for wine
		value = 1 # base value
		if = {
			limit = {
				#Andeans favor "Chicha" that is a beer
				culture = { has_culture_group = culture_group:andean_group }
			}
			multiply = {
				desc = "POP_DEMAND_CULTURAL_PREFERENCES"
				value = 0.5
			}
		}
		if = {
			limit = {
				#Japanese favor "Sake" that is a liquor
				culture = { has_culture_group = culture_group:japanese_group }
			}
			multiply = {
				desc = "POP_DEMAND_CULTURAL_PREFERENCES"
				value = 0.5
			}
		}
		...
	}
	...
}
```

### Good demand categories

Good demand categories are defined in a separate file - this is mostly used to define a way they are displayed in.

#### Example

```
government_activities = {
	display = integer
}
```

The only available attribute is `display`, which accepts one of the following three values:

- `pop`
- `integer`
- `default` (the default)
The display attribute is not known to do anything in particular.

#### Localisation

Good demand keys need to be localized with their key:

- `<key>`

## Starting good setup

In basegame, starting raw materials are defined in `in_game\map_data\location_templates.txt`, inside each location using `raw_material`:

```
stockholm = { ... raw_material = clay }
```

Due to the file's non-additive nature, it may be recommended to insert any good changes using on actions, which can be made additive:

```
on_game_start = {
	on_actions = {
		mod_goods_change
	}
}

mod_goods_change = {
	effect = {
		location:stockholm = {
			change_raw_material = goods:fish
		}
	}
}
```

## References


