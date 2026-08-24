#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Localization sanity check: syntax, coverage and markup parity.

Run against the main mod or a submod. Catches four things the game only tells you about
obliquely, or not at all:

  1. SYNTAX. A value containing a real newline instead of the two-character escape breaks the
     engine's reader, which reports "Missing colon (:) separator" pointing at the CONTINUATION
     line rather than at the key that caused it.

  2. COVERAGE. A key present in English and absent from a target language. Note the failure
     that motivated this script: a malformed English key is invisible to a naive line-based
     parser, so it goes missing from every translation AND from any audit that shares the same
     blind spot, and the two cancel out into a clean bill of health. This parser tracks
     unterminated values explicitly rather than skipping lines it cannot match.

  3. UNESCAPED QUOTES. A raw double quote inside a value terminates it early, since the engine
     delimits on the first and last quote on the line. Vanilla escapes them (490 instances).
     Attributed quotations in flavour text produce these constantly.

  4. MARKUP PARITY. A translation that drops a [scope.Function], $VAR$, @icon! or #colour
     token, or invents one the source lacks. Invented tokens are the dangerous case: a model
     will turn "they" into [minister.GetSheHe] in a key where that scope does not exist, which
     errors in game.

     COMPARED AS SETS, NOT COUNTS, and that distinction matters. German and Spanish routinely
     need a pronoun token more times than English does: "Bring [minister.GetHerHim] in and task
     them with..." becomes "Holen Sie [minister.GetHerHim] hinzu und betrauen Sie
     [minister.GetHerHim] mit...", because the second clause cannot elide the object. Counting
     occurrences flags every one of those as an invented token. What actually breaks the game
     is a token whose SCOPE does not exist in that key, and a repeat of a token the source
     already uses proves the scope is there.

Usage:
    python tools/check_loc.py                        # main mod
    python tools/check_loc.py submods/rhomania       # a submod
    python tools/check_loc.py submods/rhomania --fix # repair problem 1 in place, then report

--fix exists because problem 1 is produced by scripted edits, and anything that writes loc
programmatically has to emit backslash-n as two characters. That is easy to get wrong and the
game's error message points at the wrong line, so detection without repair just means doing the
same tedious edit by hand every time. --fix rejoins the value and inserts the escape.

Re-run translation after a --fix: a key the parser could not read was never handed to
translate.py either, so it is missing from every target language.
"""
import collections  # noqa: F401  (kept for future count-based checks)
import glob
import io
import os
import re
import sys

KEY = re.compile(r'^(\s*)([A-Za-z0-9_.]+):\s*(.*)$')
HEADER = re.compile(r'^\s*l_\w+:\s*$')
TOKEN = re.compile(r'(\[[^\]]+\]|\$[A-Za-z0-9_|%\-\.]+\$|@\w+!|#\w+|#!)')

LANGS = ('french', 'german', 'spanish')


def parse(path):
    """Return (keys dict, list of syntax problems)."""
    keys, problems = {}, []
    for n, raw in enumerate(io.open(path, encoding='utf-8-sig').read().split('\n'), 1):
        line = raw.rstrip('\r')
        if not line.strip() or line.lstrip().startswith('#') or HEADER.match(line):
            continue
        m = KEY.match(line)
        if not m:
            problems.append((n, 'no colon separator', line.strip()[:60]))
            continue
        val = m.group(3).strip()
        if val.startswith('"') and not (val.endswith('"') and len(val) > 1):
            problems.append((n, 'unterminated value (real newline in string?)', m.group(2)))
            continue
        body = val[1:-1] if val.startswith('"') and val.endswith('"') else val
        # A raw double quote inside the value terminates it early: the engine delimits on the
        # first and last quote on the line. Vanilla escapes them as backslash-quote in 490
        # places. Caught here because attributed quotations in flavour text produce them
        # constantly and nothing else in the pipeline notices.
        if re.search(r'(?<!\\)"', body):
            problems.append((n, 'unescaped double quote inside value', m.group(2)))
        keys[m.group(2)] = body
    return keys, problems


ESCAPED_BREAK = '\\' + 'n' + '\\' + 'n'   # two-char escape, twice: a paragraph break


def repair(path):
    """Rejoin values broken across lines. Returns the number of keys repaired."""
    lines = io.open(path, encoding='utf-8-sig').read().split('\n')
    out, i, n = [], 0, 0
    while i < len(lines):
        s = lines[i]
        m = KEY.match(s)
        opened = m and m.group(3).strip().startswith('"') and not (
            m.group(3).strip().endswith('"') and len(m.group(3).strip()) > 1)
        if opened:
            buf = [m.group(3).rstrip()]
            j = i + 1
            while j < len(lines):
                buf.append(lines[j].strip())
                if lines[j].rstrip().endswith('"'):
                    break
                j += 1
            out.append('%s%s: %s' % (m.group(1), m.group(2),
                                     ESCAPED_BREAK.join(x for x in buf if x)))
            n += 1
            i = j + 1
            continue
        out.append(s)
        i += 1
    if n:
        io.open(path, 'w', encoding='utf-8-sig', newline='\n').write('\n'.join(out))
    return n


def main():
    argv = [a for a in sys.argv[1:] if a != '--fix']
    do_fix = '--fix' in sys.argv
    root = argv[0] if argv else '.'
    eng = sorted(glob.glob(os.path.join(root, '**', 'localization', 'english', '*.yml'),
                           recursive=True))
    if do_fix:
        allfiles = sorted(glob.glob(os.path.join(root, '**', 'localization', '*', '*.yml'),
                                    recursive=True))
        total = sum(repair(f) for f in allfiles)
        print('== fix ==\n  repaired %d key(s) across %d file(s)\n' % (total, len(allfiles)))
    if not eng:
        print('no english localization found under %s' % root)
        return 1

    syntax_errors = 0
    missing_total = 0
    token_total = 0
    english = {}

    print('== syntax ==')
    for f in eng:
        keys, problems = parse(f)
        english[f] = keys
        for n, what, ctx in problems:
            print('  %s:%d  %s  %s' % (f, n, what, ctx))
            syntax_errors += 1
    print('  %d file(s), %d key(s), %d problem(s)'
          % (len(eng), sum(len(k) for k in english.values()), syntax_errors))

    print('== coverage and markup ==')
    for lang in LANGS:
        miss, tok, nfiles = [], [], 0
        for f, ekeys in english.items():
            tf = f.replace(os.sep + 'english' + os.sep, os.sep + lang + os.sep)
            tf = tf.replace('_l_english.yml', '_l_%s.yml' % lang)
            if not os.path.exists(tf):
                miss.append('ENTIRE FILE %s' % os.path.basename(tf))
                continue
            nfiles += 1
            tkeys, problems = parse(tf)
            for n, what, ctx in problems:
                print('  %s:%d  %s  %s' % (tf, n, what, ctx))
                syntax_errors += 1
            for k, v in ekeys.items():
                if k not in tkeys:
                    miss.append('%s:%s' % (os.path.basename(f), k))
                    continue
                a = set(TOKEN.findall(v))
                b = set(TOKEN.findall(tkeys[k]))
                if a != b:
                    tok.append('%s  dropped=%s invented=%s'
                               % (k, sorted(a - b), sorted(b - a)))
        print('  %-8s %2d files | missing %3d | markup mismatch %3d'
              % (lang, nfiles, len(miss), len(tok)))
        for m in miss[:10]:
            print('      MISSING %s' % m)
        for m in tok[:10]:
            print('      TOKEN   %s' % m)
        missing_total += len(miss)
        token_total += len(tok)

    bad = syntax_errors + missing_total + token_total
    print('== %s ==' % ('OK' if not bad else '%d PROBLEM(S)' % bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
