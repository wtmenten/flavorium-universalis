"""Check that every scripted effect / trigger call passes exactly the parameters the
definition uses.

The engine rejects a call that passes an argument the body never reads as $NAME$:

    [jomini_script_argument.cpp:180]: Compiling source for X failed for unknown arguments: ...
    [jomini_effect.cpp:141]: PostValidate of effect 'X' returned false at ...

and a call that omits one leaves a literal $NAME$ in the expanded script. This walks a mod
tree and compares, for each call:

  - direct calls        name = { A = .. B = .. }   or   name = yes
  - computed names      cc_pty_outcome_$KEY$ = yes   (checked against every definition
                        the pattern can expand to)
  - dispatched calls    dispatcher = { .. EFFECT = target }, where the dispatcher's body
                        calls $EFFECT$ = { A = .. }: the forwarded keys must match target

    python tools/check_script_args.py                    # main mod
    python tools/check_script_args.py submods/factions   # one submod

Exits 1 if anything mismatches. Only calls to definitions inside the scanned tree are
checked; vanilla scripted effects are not.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEF_DIRS = ("in_game/common/scripted_effects", "in_game/common/scripted_triggers")
PARAM = re.compile(r"\$([A-Z_][A-Z_0-9]*)\$")
KEYS = re.compile(r"\b([A-Z_][A-Z_0-9]*)\s*=")


def strip_comments(text: str) -> str:
    return re.sub(r"#[^\n]*", "", text)


def top_level_blocks(text: str):
    """Yield (name, body, line) for each top-level `name = { ... }`."""
    for m in re.finditer(r"^([A-Za-z_0-9]+)\s*=\s*\{", text, re.M):
        start, depth, j = m.end(), 1, m.end()
        while depth and j < len(text):
            depth += (text[j] == "{") - (text[j] == "}")
            j += 1
        yield m.group(1), text[start:j - 1], text.count("\n", 0, m.start()) + 1


def main() -> int:
    tree = ROOT / (sys.argv[1] if len(sys.argv) > 1 else ".")
    texts = {}
    for f in tree.rglob("*.txt"):
        if "docs" in f.parts or ".git" in f.parts:
            continue
        try:
            texts[f] = strip_comments(f.read_text(encoding="utf-8-sig"))
        except UnicodeDecodeError:
            continue

    defs: dict[str, set[str]] = {}
    forwards: dict[str, set[str]] = {}
    for f, text in texts.items():
        rel = f.relative_to(tree).as_posix()
        if not any(rel.startswith(d) or f"/{d}/" in f"/{rel}" for d in DEF_DIRS):
            continue
        for name, body, _ in top_level_blocks(text):
            defs[name] = set(PARAM.findall(body))
            calls = re.findall(r"\$EFFECT\$\s*=\s*\{([^{}]*)\}", body)
            if calls:
                forwards[name] = set(KEYS.findall(calls[0]))

    problems = []
    # Indented or inline only: a name at column 0 is a definition (scripted effect, price,
    # ...), never a call. A price shares its key with the action that charges it.
    call = re.compile(r"(?<=[ \t{])([a-z_][A-Za-z_0-9$]*)\s*=\s*(\{([^{}]*)\}|yes\b)")
    for f, text in texts.items():
        for m in call.finditer(text):
            name, whole, body = m.group(1), m.group(2), m.group(3) or ""
            line = text.count("\n", 0, m.start()) + 1
            if "$" in name:
                pat = re.compile("^" + PARAM.sub("[a-z_0-9]+", name) + "$")
                targets = [d for d in defs if pat.match(d)]
            else:
                targets = [name] if name in defs else []
            for t in targets:
                passed = set() if whole == "yes" else set(KEYS.findall(body))
                if whole != "yes" and not passed and not defs[t]:
                    continue  # a block call to a parameterless trigger used as a scope-less trigger
                expected = defs[t]
                if passed != expected:
                    problems.append(f"{f.relative_to(ROOT)}:{line}  {name} -> {t}: passes {sorted(passed) or 'yes'}, uses {sorted(expected) or 'nothing'}")
                if t in forwards:
                    e = re.search(r"\bEFFECT\s*=\s*([a-z_0-9]+)", body)
                    if e and e.group(1) in defs and forwards[t] != defs[e.group(1)]:
                        problems.append(f"{f.relative_to(ROOT)}:{line}  {t} forwards {sorted(forwards[t])} to {e.group(1)}, which uses {sorted(defs[e.group(1)])}")

    for p in problems:
        print(p)
    print(f"{len(defs)} definitions, {len(forwards)} dispatchers, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
