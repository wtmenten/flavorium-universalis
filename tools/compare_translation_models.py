#!/usr/bin/env python3
"""Run a sample of localization strings through another local model and compare the result
with the translations already in the repo.

The candidate model is driven through translate.py's own local pipeline (same prompt, batching,
markup validation and per-string retry), with only the model name swapped. So a difference in
the report is a difference between models, not between two ways of calling them. Nothing in the
mod is written.

    python tools/compare_translation_models.py                          # qwen3.5-9b-h-Q8, 30 strings
    python tools/compare_translation_models.py --sample 60 --seed 7
    python tools/compare_translation_models.py --model some-other-model -l french
    python tools/compare_translation_models.py --files cc_byz_venice    # only files matching

The sample is stratified so it is not all one-word labels: roughly a third short strings
(under 60 characters), a third medium, a third long (over 250), and at least a quarter of it
carrying markup ([scope.Function], $VAR$, #colour#!, @icon!), which is where models fail.

Writes tools/translation_compare/<model>_<timestamp>.md and .json (the folder is gitignored by
the line added to .gitignore; delete reports freely). Per language the report gives:

  translated     how many came back with faithful markup (the rest fell back to English)
  markup fails   strings the model could not translate without dropping or inventing a token
  similarity     difflib ratio against the current translation, 0..1. High means the two
                 models agree; it is NOT a quality score, since the current one can be wrong
  length ratio   candidate length / current length; far from 1 is worth reading
  seconds        wall time for the language

then every string side by side: key, English, current, candidate, similarity.
"""

from __future__ import annotations

import argparse
import difflib
import glob
import json
import os
import random
import re
import sys
import time
import urllib.request
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import translate as T  # noqa: E402  (translate.py, imported for its local pipeline)

DEFAULT_MODEL = 'qwen3.5-9b-h-Q8'
DEFAULT_LANGS = ['french', 'german', 'spanish']
OUT_DIR = TOOLS / 'translation_compare'
NO_TRANSLATE_RE = re.compile(r'#\s*NO-TRANSLATE\b')


###############################################################################
# Sampling
###############################################################################

def english_files(filter_text: str | None) -> list[Path]:
    roots = [REPO] + [p for p in (REPO / 'submods').iterdir() if p.is_dir()]
    files = []
    for root in roots:
        for content in T.LOC_CONTENT_ROOTS:
            files += [Path(p) for p in glob.glob(str(root / content / 'localization' / 'english' / '**' / '*_l_english.yml'), recursive=True)]
    if filter_text:
        files = [f for f in files if filter_text in f.name]
    return sorted(set(files))


def target_path(english: Path, lang: str) -> Path:
    parts = list(english.parts)
    i = len(parts) - 1 - parts[::-1].index('english')
    parts[i] = lang
    return Path(*parts[:-1]) / english.name.replace('_l_english.yml', f'_l_{lang}.yml')


def read_entries(path: Path) -> dict[str, tuple[str, bool]]:
    """key -> (raw value, excluded). Excluded covers NO-TRANSLATE lines and blocks."""
    out: dict[str, tuple[str, bool]] = {}
    if not path.exists():
        return out
    block = False
    for line in path.read_text(encoding='utf-8-sig').split('\n'):
        if '# NO-TRANSLATE BELOW' in line:
            block = True
            continue
        if '# NO-TRANSLATE END' in line:
            block = False
            continue
        if T.HEADER_RE.match(line):
            continue
        m = T.KEY_VALUE_RE.match(line)
        if not m:
            continue
        key = m.group(2).strip()
        key = re.sub(r':\d+$', '', key)
        out[key] = (m.group(3), block or bool(NO_TRANSLATE_RE.search(m.group(4))))
    return out


def sample_entries(files: list[Path], langs: list[str], n: int, seed: int) -> list[dict]:
    pool = []
    for f in files:
        targets = {lang: read_entries(target_path(f, lang)) for lang in langs}
        for key, (value, excluded) in read_entries(f).items():
            if excluded or not value.strip() or value.startswith('$') and value.endswith('$'):
                continue
            current = {lang: targets[lang].get(key, (None, False))[0] for lang in langs}
            if any(c is None for c in current.values()):
                continue  # need a current translation in every language to compare against
            pool.append({'file': str(f.relative_to(REPO)), 'key': key, 'english': value, 'current': current})
    rng = random.Random(seed)
    rng.shuffle(pool)

    markup = [e for e in pool if T.markup_tokens(e['english'])]
    short = [e for e in pool if len(e['english']) < 60]
    long_ = [e for e in pool if len(e['english']) > 250]
    medium = [e for e in pool if 60 <= len(e['english']) <= 250]

    picked: list[dict] = []
    seen = set()

    def take(group, count):
        for e in group:
            if count <= 0:
                break
            ident = (e['file'], e['key'])
            if ident in seen:
                continue
            seen.add(ident)
            picked.append(e)
            count -= 1

    take(markup, max(1, n // 4))
    rest = n - len(picked)
    take(short, rest // 3)
    take(long_, rest // 3)
    take(medium, n - len(picked))
    take(pool, n - len(picked))
    return picked


###############################################################################
# Running
###############################################################################

def model_available(model: str) -> bool:
    url = T.LOCAL_SETTINGS['api_base'].rstrip('/') + '/models'
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f'Error: could not reach the local server at {url}: {e}')
        return False
    ids = [m.get('id') for m in data.get('data', [])]
    if model not in ids:
        print(f'Error: model {model!r} is not offered by the server. Available: {", ".join(ids)}')
        return False
    return True


def similarity(a: str | None, b: str | None) -> float:
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def run(args) -> int:
    cfg = T.load_config(T.CONFIG_PATH)
    if cfg[0] is None:
        return 1
    system_prompt, additional_context = cfg[5], cfg[10]
    T.LOCAL_SETTINGS['model'] = args.model
    if args.batch_size:
        T.LOCAL_SETTINGS['batch_size'] = args.batch_size
    if not model_available(args.model):
        return 1

    files = english_files(args.files)
    entries = sample_entries(files, args.langs, args.sample, args.seed)
    if not entries:
        print('No strings matched.')
        return 1
    print(f'Sampled {len(entries)} strings from {len(files)} files. Model: {args.model}')

    values = sorted({e['english'] for e in entries})
    summary = {}
    for lang in args.langs:
        started = time.time()
        results = T.translate_values_local(values, lang, system_prompt, additional_context, log_prefix='  ')
        elapsed = time.time() - started
        sims, ratios = [], []
        for e in entries:
            cand = results.get(e['english'])
            e.setdefault('candidate', {})[lang] = cand
            if cand:
                sims.append(similarity(cand, e['current'][lang]))
                if e['current'][lang]:
                    ratios.append(len(cand) / max(1, len(e['current'][lang])))
        translated = sum(1 for v in values if results.get(v))
        summary[lang] = {
            'translated': translated,
            'total': len(values),
            'markup_fails': len(values) - translated,
            'similarity': sum(sims) / len(sims) if sims else 0.0,
            'length_ratio': sum(ratios) / len(ratios) if ratios else 0.0,
            'seconds': elapsed,
            'strings_per_second': len(values) / elapsed if elapsed else 0.0,
        }
    write_report(args, entries, summary)
    return 0


###############################################################################
# Report
###############################################################################

def cell(text: str | None, width: int = 400) -> str:
    if text is None:
        return '*(fell back to English)*'
    text = text.replace('|', '\\|')
    return text if len(text) <= width else text[:width] + '…'


def write_report(args, entries, summary):
    OUT_DIR.mkdir(exist_ok=True)
    stamp = time.strftime('%Y%m%d_%H%M%S')
    # Not Path.with_suffix: a model id like qwen3.5-9b would lose everything after its first dot.
    stem = f'{args.model.replace("/", "_")}_{stamp}'
    md_path, json_path = OUT_DIR / (stem + '.md'), OUT_DIR / (stem + '.json')

    md = [f'# Translation comparison: {args.model}',
          '',
          f'{len(entries)} strings, seed {args.seed}. Compared against the translations currently in the repo '
          f'(made with the model in tools/config.toml). Similarity is agreement with the current text, not quality.',
          '',
          '| Language | Translated | Markup fails | Similarity | Length ratio | Seconds | Strings/s |',
          '|---|---|---|---|---|---|---|']
    for lang, s in summary.items():
        md.append(f"| {lang} | {s['translated']}/{s['total']} | {s['markup_fails']} | {s['similarity']:.2f} | "
                  f"{s['length_ratio']:.2f} | {s['seconds']:.0f} | {s['strings_per_second']:.2f} |")
    for lang in summary:
        md += ['', f'## {lang}', '',
               '| Key | English | Current | Candidate | Sim |',
               '|---|---|---|---|---|']
        for e in sorted(entries, key=lambda x: similarity(x['candidate'].get(lang), x['current'][lang])):
            cand = e['candidate'].get(lang)
            md.append(f"| `{e['key']}` | {cell(e['english'])} | {cell(e['current'][lang])} | {cell(cand)} | "
                      f"{similarity(cand, e['current'][lang]):.2f} |")
    md_path.write_text('\n'.join(md) + '\n', encoding='utf-8')
    json_path.write_text(json.dumps({'model': args.model, 'seed': args.seed, 'summary': summary,
                                                     'entries': entries}, ensure_ascii=False, indent=1),
                                         encoding='utf-8')
    print()
    for lang, s in summary.items():
        print(f"  {lang:8} translated {s['translated']}/{s['total']}  markup fails {s['markup_fails']}  "
              f"similarity {s['similarity']:.2f}  length {s['length_ratio']:.2f}  {s['seconds']:.0f}s")
    print(f'\nReport: {md_path}')


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--model', default=DEFAULT_MODEL, help=f'candidate model id (default {DEFAULT_MODEL})')
    ap.add_argument('-l', '--langs', default=','.join(DEFAULT_LANGS), help='comma-separated target languages')
    ap.add_argument('--sample', type=int, default=30, help='number of strings (default 30)')
    ap.add_argument('--seed', type=int, default=1, help='sampling seed, so runs are repeatable')
    ap.add_argument('--files', help='only English files whose name contains this text')
    ap.add_argument('--batch-size', type=int, help='override local_batch_size for this run')
    args = ap.parse_args()
    args.langs = [l.strip() for l in args.langs.split(',') if l.strip()]
    return run(args)


if __name__ == '__main__':
    sys.exit(main())
