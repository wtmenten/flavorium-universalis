#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Resolve every add/remove/has_country_modifier reference against STATIC MODIFIERS only.

WHY THIS EXISTS. Two load errors of the same shape have now shipped:

    PostValidate of effect 'add_country_modifier' returned false

Both were a name that existed, in the wrong namespace or not at all, and both survived an
ad-hoc grep audit that could not tell the difference:

  cc_byz_perm_pontifex          referenced by a mission task, never defined anywhere. Its
                                LOCALISATION was written, so a missing-loc-key check found
                                nothing: the key existed and the thing it named did not.

  <name>_impact_modifier        registered as a MODIFIER TYPE for all 34 bureaucracies, and
                                granted with add_country_modifier as though it were a static
                                modifier. Modifier types are the keys you write inside a
                                modifier block; static modifiers are named bundles of them.
                                A grep for the name finds it in modifier_type_definitions and
                                looks resolved.

The distinction this script enforces is exactly that: add_country_modifier reads static
modifiers and nothing else. Biases (add_opinion), character modifiers and modifier types are
separate namespaces and are reported separately rather than silently accepted.

Usage:
    python tools/check_modifiers.py                  # main mod
    python tools/check_modifiers.py submods/rhomania # a submod
"""
import glob
import io
import os
import re
import sys

VANILLA = 'f:/SteamLibrary/steamapps/common/Europa Universalis V/game/'
ENTRY = re.compile(
    r'^(?:REPLACE:|REPLACE_OR_CREATE:|INJECT:|TRY_REPLACE:|TRY_INJECT:)?([a-z0-9_]+)\s*=\s*\{', re.M)


def collect(patterns):
    out = set()
    for pat in patterns:
        for f in glob.glob(pat, recursive=True):
            try:
                s = io.open(f, encoding='utf-8-sig', errors='replace').read()
            except Exception:
                continue
            out |= set(ENTRY.findall(s))
    return out


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    # Static modifiers are the ONLY namespace add_country_modifier reads.
    statics = collect([
        os.path.join(root, 'main_menu/common/static_modifiers/**/*.txt'),
        'main_menu/common/static_modifiers/**/*.txt',
        VANILLA + 'main_menu/common/static_modifiers/**/*.txt',
    ])
    types = collect([
        os.path.join(root, 'main_menu/common/modifier_type_definitions/**/*.txt'),
        'main_menu/common/modifier_type_definitions/**/*.txt',
        VANILLA + 'main_menu/common/modifier_type_definitions/**/*.txt',
    ])
    biases = collect([
        os.path.join(root, 'in_game/common/biases/**/*.txt'),
        'in_game/common/biases/**/*.txt',
        VANILLA + 'in_game/common/biases/**/*.txt',
    ])

    bad = []
    for f in glob.glob(os.path.join(root, 'in_game/**/*.txt'), recursive=True):
        s = io.open(f, encoding='utf-8-sig', errors='replace').read()
        for n, line in enumerate(s.split('\n'), 1):
            c = re.sub(r'#.*', '', line)
            for m in re.finditer(
                    r'\b(?:add|remove|has)_(?:country|character|location|province)_modifier'
                    r'\s*=\s*\{?\s*(?:modifier\s*=\s*)?([a-z][a-z0-9_]*)', c):
                k = m.group(1)
                if k in ('modifier', 'yes', 'no') or k in statics:
                    continue
                why = ('MODIFIER TYPE, not a static modifier' if k in types else
                       'BIAS, not a static modifier' if k in biases else
                       'not defined anywhere')
                bad.append((os.path.relpath(f, root), n, k, why))

    for f, n, k, why in bad:
        print('  %s:%d  %s  <- %s' % (f, n, k, why))
    print('== %s ==' % ('OK, all modifier grants resolve to static modifiers'
                        if not bad else '%d UNRESOLVED' % len(bad)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
