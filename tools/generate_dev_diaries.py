#!/usr/bin/env python3
"""
Generate docs/dev-diaries.html from the Markdown files in docs/dev_diaries/.

Self-contained Markdown -> HTML (no external `markdown` dependency): handles the
subset used by our dev diaries — headings, paragraphs, bullet lists, blockquotes,
horizontal rules, inline bold/italic/links, and raw HTML blocks (figures) which are
passed through verbatim. Shares the page chrome (CSS / nav / scripts) with
generate_index.py so the two pages stay visually consistent.

Usage:
    python tools/generate_dev_diaries.py
"""
import re
import sys
from pathlib import Path

import generate_index as gi  # reuse CSS, scripts, nav + heading helpers

ROOT = Path(__file__).resolve().parent.parent
DIARY_DIR = ROOT / "docs" / "dev_diaries"
OUTPUT = ROOT / "docs" / "dev-diaries.html"


# ---------------------------------------------------------------------------
# Minimal Markdown -> HTML
# ---------------------------------------------------------------------------

def _inline(text: str) -> str:
    """Inline formatting: links, bold, italic. (Prose only — raw HTML is handled separately.)"""
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def md_to_html(text: str) -> str:
    lines = text.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i, n = 0, len(lines)

    para: list[str] = []
    list_items: list[str] = []

    def flush_para():
        if para:
            out.append(f"<p>{_inline(' '.join(para))}</p>")
            para.clear()

    def flush_list():
        if list_items:
            out.append("<ul>" + "".join(f"<li>{_inline(it)}</li>" for it in list_items) + "</ul>")
            list_items.clear()

    while i < n:
        raw = lines[i]
        stripped = raw.strip()

        # Raw HTML block (figures, divs): emit verbatim until the block balances.
        if stripped.startswith("<"):
            flush_para(); flush_list()
            out.append(raw)
            i += 1
            continue

        if not stripped:
            flush_para(); flush_list()
            i += 1
            continue

        if stripped == "---":
            flush_para(); flush_list()
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"(#{1,3})\s+(.*)$", stripped)
        if m:
            flush_para(); flush_list()
            level = len(m.group(1))
            txt = m.group(2).strip()
            slug = gi._slugify(txt)
            out.append(f'<h{level} id="{slug}">{_inline(txt)}</h{level}>')
            i += 1
            continue

        if stripped.startswith("- "):
            flush_para()
            list_items.append(stripped[2:].strip())
            i += 1
            continue

        if stripped.startswith("> "):
            flush_para(); flush_list()
            quote = [stripped[2:].strip()]
            i += 1
            while i < n and lines[i].strip().startswith("> "):
                quote.append(lines[i].strip()[2:].strip())
                i += 1
            out.append(f"<blockquote><p>{_inline(' '.join(quote))}</p></blockquote>")
            continue

        # Plain prose line.
        flush_list()
        para.append(stripped)
        i += 1

    flush_para(); flush_list()
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------

EXTRA_CSS = """
/* ----- dev diary figures ----- */
.content figure{margin:18px 0;background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);overflow:hidden}
.content figure a{display:block}
.content figure img{display:block;width:100%;height:auto}
.content figcaption{padding:8px 14px;font-size:12.5px;color:var(--text-mid);border-top:1px solid var(--card-border)}
.fig-row{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:18px 0}
.fig-row figure{margin:0}
@media(max-width:680px){.fig-row{grid-template-columns:1fr}}
"""

HEADER = """\
<header class="site-header">
  <div class="header-inner">
    <button class="menu-btn" id="menuBtn" title="Navigation">&#9776;</button>
    <span class="mod-title">Flavorium Universalis</span>
    <span class="ver-badge">Dev Diaries</span>
    <div class="hdr-spacer"></div>
    <a class="planner-link" href="index.html">&larr; Home</a>
    <a class="planner-link" href="planner.html">Advance Planner &rarr;</a>
  </div>
</header>"""


def _extract(pattern: str) -> str:
    m = re.search(pattern, gi.TEMPLATE, re.S)
    if not m:
        sys.exit(f"Could not extract chrome from generate_index.TEMPLATE: {pattern}")
    return m.group(1)


def build_page(body_html: str, nav_html: str) -> str:
    css = _extract(r"<style>(.*?)</style>")
    script = _extract(r"<script>(.*?)</script>")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dev Diaries — Flavorium Universalis</title>
<style>{css}{EXTRA_CSS}</style>
</head>
<body>

{HEADER}

<div class="layout">
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-label">Dev Diaries</div>
{nav_html}
  </nav>
  <div class="sidebar-overlay" id="sidebarOverlay"></div>
  <div class="main">
    <article class="content" id="content">
{body_html}
    </article>
  </div>
</div>

<script>{script}</script>

</body>
</html>
"""


def main():
    diaries = sorted(DIARY_DIR.glob("*.md"))
    if not diaries:
        sys.exit(f"No dev diaries found in {DIARY_DIR}")

    parts = []
    for md in diaries:
        html = md_to_html(md.read_text(encoding="utf-8-sig"))
        parts.append(html)
    body = "\n<hr>\n".join(parts)

    # Page is served from docs/, so rewrite the diary-relative ../assets paths.
    body = body.replace("../assets/", "assets/")

    body = gi.annotate_sections(body)
    headings = gi.extract_headings(body)
    nav = gi.build_nav(headings)

    OUTPUT.write_text(build_page(body, nav), encoding="utf-8")
    print(f"Written {OUTPUT} ({OUTPUT.stat().st_size:,} bytes, {len(diaries)} diaries, {len(headings)} nav items)")


if __name__ == "__main__":
    main()
