#!/usr/bin/env python3
"""Aggregate total gold cost to build / maintain each ship from our balance files.

For every *_construction and *_maintenance goods_demand def we override, this sums:
    base gold (per category, from our prices file) + sum(goods_qty * default_market_price)

Goods prices come from vanilla goods/ defs. Base gold comes from our prices override
(falling back to vanilla 02_units.txt for keys we don't override, e.g. maintenance).

Just prints a table to console. Run from anywhere:
    python tools/ship_costs.py
"""

import os
import re
import glob

# ---------------------------------------------------------------------------
MOD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME_DIR = r"F:\SteamLibrary\steamapps\common\Europa Universalis V\game"

NAVY_DEMANDS = os.path.join(
    MOD_ROOT, "submods", "balance", "in_game", "common", "goods_demand", "99_cc_navy_demands.txt"
)
UNIT_PRICES = os.path.join(
    MOD_ROOT, "submods", "balance", "in_game", "common", "prices", "99_cc_unit_prices.txt"
)
VANILLA_PRICES = os.path.join(GAME_DIR, "in_game", "common", "prices", "02_units.txt")
GOODS_GLOB = os.path.join(GAME_DIR, "in_game", "common", "goods", "*.txt")

# non-goods keys that can appear inside a *_construction / *_maintenance block
NON_GOODS = {"category"}


def read(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()


def top_level_blocks(text):
    """Yield (name, body) for every top-level NAME = { ... } block.

    Handles a leading REPLACE_OR_CREATE: prefix and nested braces.
    """
    i, n = 0, len(text)
    name_re = re.compile(r"([A-Za-z0-9_:]+)\s*=\s*\{")
    while i < n:
        m = name_re.search(text, i)
        if not m:
            break
        name = m.group(1).split(":")[-1]  # strip REPLACE_OR_CREATE:
        depth, j = 1, m.end()
        while j < n and depth:
            c = text[j]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        yield name, text[m.end():j - 1]
        i = j


def parse_kv(body):
    """Return {key: float} for simple `key = number` lines (ignores nested blocks)."""
    out = {}
    for k, v in re.findall(r"([A-Za-z0-9_]+)\s*=\s*(-?\d+(?:\.\d+)?)", body):
        out[k] = float(v)
    return out


def load_goods_prices():
    prices = {}
    for path in glob.glob(GOODS_GLOB):
        for name, body in top_level_blocks(read(path)):
            m = re.search(r"default_market_price\s*=\s*(-?\d+(?:\.\d+)?)", body)
            if m:
                prices[name] = float(m.group(1))
    return prices


def load_unit_gold():
    """Map price-id -> base gold, our override winning over vanilla."""
    gold = {}
    for path in (VANILLA_PRICES, UNIT_PRICES):  # our file last => overrides
        if not os.path.exists(path):
            continue
        for name, body in top_level_blocks(read(path)):
            kv = parse_kv(body)
            if "gold" in kv:
                gold[name] = kv["gold"]
    return gold


# construction/maintenance def name -> price category stem
def category_of(def_name):
    if def_name.startswith("light_ship"):
        return "navy_light_ship"
    if def_name.startswith("heavy_ship") or def_name == "ship_of_the_line":
        return "navy_heavy_ship"
    if def_name.startswith("transport") or def_name == "fishing_boat":
        return "navy_transport"
    if def_name.startswith("galley") or def_name in ("canoe", "cakradonya"):
        return "navy_galley"
    return None


def aggregate(goods_prices, unit_gold, kind):
    """kind = 'construction' or 'maintenance'. Returns list of rows."""
    suffix = "_" + kind
    price_suffix = "_build" if kind == "construction" else "_maintenance"
    rows = []
    for name, body in top_level_blocks(read(NAVY_DEMANDS)):
        if not name.endswith(suffix):
            continue
        stem = name[: -len(suffix)]
        cat = category_of(stem)
        base_gold = unit_gold.get(cat + price_suffix, 0.0) if cat else 0.0

        kv = parse_kv(body)
        goods_gold = 0.0
        missing = []
        for good, qty in kv.items():
            if good in NON_GOODS:
                continue
            if good in goods_prices:
                goods_gold += qty * goods_prices[good]
            else:
                missing.append(good)
        rows.append((name, base_gold, goods_gold, base_gold + goods_gold, missing))
    return rows


def print_table(title, rows):
    print(f"\n=== {title} ===")
    print(f"{'def':<32}{'base_gold':>10}{'goods_gold':>12}{'total':>10}")
    print("-" * 64)
    for name, base, goods, total, missing in rows:
        print(f"{name:<32}{base:>10.2f}{goods:>12.2f}{total:>10.2f}")
        if missing:
            print(f"{'':<32}  (no price for: {', '.join(missing)})")


def main():
    goods_prices = load_goods_prices()
    unit_gold = load_unit_gold()
    print_table("BUILD COST (one-time)", aggregate(goods_prices, unit_gold, "construction"))
    print_table("MAINTENANCE COST (per month)", aggregate(goods_prices, unit_gold, "maintenance"))


if __name__ == "__main__":
    main()
