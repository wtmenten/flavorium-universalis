#!/usr/bin/env python
"""Find script keys the mod defines that have no localisation string.

Each check knows one naming convention the engine expects. A missing key of any of these
kinds does not stop the mod loading; it renders in game as the raw key or as a blank line,
which is why they accumulate unnoticed.

    python tools/audit_loc.py            # every check, missing entries only
    python tools/audit_loc.py --all      # every entry, present or not
    python tools/audit_loc.py auto_mod   # one check by name

Exits non-zero when anything is missing, so it works in a pre-commit hook.
"""
import io
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(path):
    return io.open(path, encoding='utf-8-sig').read()


def strip_comments(text):
    return re.sub(r'#.*', '', text)


def english_keys():
    """Every key defined in any english .yml the mod ships, main mod and submods."""
    keys = set()
    for f in glob.glob(os.path.join(ROOT, '**', 'localization', 'english', '*.yml'),
                       recursive=True):
        keys |= set(re.findall(r'^\s*([A-Za-z0-9_.]+):', read(f), re.M))
    return keys


def top_level_entries(pattern, skip=('readme.txt',)):
    """(key, file) for every `key = {` at column 0 in the matched files."""
    out = []
    for f in glob.glob(os.path.join(ROOT, pattern), recursive=True):
        if os.path.basename(f) in skip:
            continue
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        for m in re.finditer(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\{',
                             strip_comments(read(f)), re.M):
            out.append((m.group(1), rel))
    return out


# Each check: (name, description, entries, required-suffix list)
# The suffixes are formatted against the entry key.
CHECKS = [
    ('auto_mod',
     'auto_modifiers need AUTO_MODIFIER_NAME_<key> (DESC is optional)',
     lambda: top_level_entries('**/auto_modifiers/*.txt'),
     ['AUTO_MODIFIER_NAME_{0}']),

    ('static_mod',
     'static_modifiers need STATIC_MODIFIER_NAME_<key>',
     lambda: top_level_entries('**/static_modifiers/*.txt'),
     ['STATIC_MODIFIER_NAME_{0}']),

    ('char_action',
     'character_interactions need <key> and <key>_desc',
     lambda: top_level_entries('**/character_interactions/cc_*.txt'),
     ['{0}', '{0}_desc']),

    ('generic_action',
     'generic_actions need <key> and <key>_desc',
     lambda: top_level_entries('**/generic_actions/cc_*.txt'),
     ['{0}', '{0}_desc']),

    ('trait',
     'traits need <key> and desc_<key>',
     lambda: top_level_entries('**/common/traits/cc_*.txt'),
     ['{0}', 'desc_{0}']),
]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    show_all = '--all' in sys.argv

    keys = english_keys()
    total_missing = 0

    for name, blurb, collect, suffixes in CHECKS:
        if args and name not in args:
            continue
        entries = collect()
        missing = []
        for key, path in sorted(set(entries)):
            absent = [s.format(key) for s in suffixes if s.format(key) not in keys]
            if absent:
                missing.append((key, path, absent))
            if show_all:
                print('  %-44s %-9s %s' % (key, 'MISSING' if absent else 'ok', path))

        print('[%s] %s' % (name, blurb))
        print('    %d entries, %d missing' % (len(set(entries)), len(missing)))
        for key, path, absent in missing:
            print('    %-42s %s' % (key, ', '.join(absent)))
            print('    %-42s   (%s)' % ('', path))
        total_missing += len(missing)
        print('')

    if total_missing:
        print('%d entr%s missing localisation.' % (total_missing,
                                                   'y is' if total_missing == 1 else 'ies are'))
        return 1
    print('No missing localisation.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
