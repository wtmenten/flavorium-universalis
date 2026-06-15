#!/usr/bin/env python3
"""
Generate the dev-diaries section of the website from the Markdown files in
docs/dev_diaries/.

Produces:
  - docs/dev-diaries.html            -- a landing page: a card index of all diaries
  - docs/dev-diaries/<slug>.html     -- one standalone page per diary

Each diary's title is its first `# ` heading; its date comes from an optional
`*Published: YYYY-MM-DD*` line (or `<!-- date: ... -->` comment) near the top, falling
back to the file's modified time. Diaries are listed newest-first. The card blurb is the
diary's first italic subtitle / paragraph.

Self-contained Markdown -> HTML (no external `markdown` dependency): handles the subset
used by our dev diaries — headings, paragraphs, bullet lists, blockquotes, horizontal
rules, inline bold/italic/links, and raw HTML blocks (figures) passed through verbatim.
Shares the page chrome (CSS / nav / scripts) with generate_index.py so the pages stay
visually consistent.

Usage:
    python tools/generate_dev_diaries.py
"""
import re
import sys
from datetime import date
from pathlib import Path

import generate_index as gi  # reuse CSS, scripts, nav + heading helpers

ROOT = Path(__file__).resolve().parent.parent
DIARY_DIR = ROOT / "docs" / "dev_diaries"
PAGES_DIR = ROOT / "docs" / "dev-diaries"          # per-diary standalone pages
INDEX_OUT = ROOT / "docs" / "dev-diaries.html"     # card landing page


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
# Diary metadata extraction
# ---------------------------------------------------------------------------

_PUBLISHED_RE = re.compile(r"Published:\s*([^\n*<]+)", re.I)
_DATE_COMMENT_RE = re.compile(r"<!--\s*date:\s*([^\n]+?)\s*-->", re.I)
_ISO_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def _fmt(d: date) -> str:
    return d.strftime("%B %d, %Y").replace(" 0", " ")


def parse_meta(text: str, path: Path) -> dict:
    """Return {title, date (date obj, for sort), date_display, blurb, slug}."""
    title_m = re.search(r"^#\s+(.+)$", text, re.M)
    title = title_m.group(1).strip() if title_m else path.stem.replace("-", " ").title()

    # Date: explicit marker (ISO preferred) else file mtime.
    mtime = date.fromtimestamp(path.stat().st_mtime)
    marker = _PUBLISHED_RE.search(text) or _DATE_COMMENT_RE.search(text)
    if marker:
        raw = marker.group(1).strip()
        iso = _ISO_RE.search(raw)
        if iso:
            d = date.fromisoformat(iso.group(0))
            date_obj, date_display = d, _fmt(d)
        else:
            date_obj, date_display = mtime, raw
    else:
        date_obj, date_display = mtime, _fmt(mtime)

    # Blurb: first italic subtitle / paragraph after the title (skip markers & raw HTML).
    blurb = ""
    body = text.split("\n", 1)[1] if title_m else text
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "<")):
            continue
        if _PUBLISHED_RE.search(s) or _DATE_COMMENT_RE.search(s):
            continue
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)   # links -> text
        s = re.sub(r"\*\*?([^*]+)\*\*?", r"\1", s)         # bold/italic -> text
        blurb = s.strip()
        break

    return {
        "title": title,
        "date": date_obj,
        "date_display": date_display,
        "blurb": blurb,
        "slug": path.stem,
    }


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
/* ----- diary entry byline (per-diary pages) ----- */
.diary-byline{color:var(--text-dim);font-size:12px;text-transform:uppercase;letter-spacing:.08em;margin:-2px 0 18px}
/* ----- dev diary index cards (landing page) ----- */
.diary-index{display:flex;flex-direction:column;gap:14px;margin-top:10px}
.diary-card{display:block;background:var(--card-bg);border:1px solid var(--card-border);border-left:3px solid var(--gold);border-radius:var(--radius);padding:16px 20px;text-decoration:none;color:inherit;transition:background .12s,border-color .12s,transform .12s}
.diary-card:hover{background:var(--hover-bg);border-left-color:var(--adm);transform:translateX(2px)}
.diary-card .dc-date{color:var(--text-dim);font-size:11px;text-transform:uppercase;letter-spacing:.08em}
.diary-card .dc-title{color:var(--gold);font-size:18px;font-weight:700;margin:3px 0 6px}
.diary-card:hover .dc-title{color:var(--adm)}
.diary-card .dc-blurb{color:var(--text-mid);font-size:14px;line-height:1.55}
.diary-card .dc-more{display:inline-block;margin-top:9px;font-size:12px;color:var(--adm);font-weight:600}
"""


def _header(prefix: str, ver_badge: str) -> str:
    """Site header. `prefix` is the relative path back to docs/ ('' or '../')."""
    return f"""\
<header class="site-header">
  <div class="header-inner">
    <button class="menu-btn" id="menuBtn" title="Navigation">&#9776;</button>
    <span class="mod-title">Flavorium Universalis</span>
    <span class="ver-badge">{ver_badge}</span>
    <div class="hdr-spacer"></div>
    <a class="planner-link" href="{prefix}index.html">&larr; Home</a>
    <a class="planner-link" href="{prefix}dev-diaries.html">All Dev Diaries</a>
    <a class="planner-link" href="{prefix}planner.html">Advance Planner &rarr;</a>
  </div>
</header>"""


def _extract(pattern: str) -> str:
    m = re.search(pattern, gi.TEMPLATE, re.S)
    if not m:
        sys.exit(f"Could not extract chrome from generate_index.TEMPLATE: {pattern}")
    return m.group(1)


def build_page(title: str, header_html: str, sidebar_label: str, nav_html: str,
               body_html: str) -> str:
    css = _extract(r"<style>(.*?)</style>")
    script = _extract(r"<script>(.*?)</script>")
    # The shared chrome script tags the 3rd <h2> (data-sec="2") as the index page's
    # "Features" grid and lays its <h3>s out as card tiles. Dev-diary pages have no such
    # section, so neutralize that branch — keep h3 grouping, scroll-spy, and mobile toggle.
    script = script.replace(
        "inFeatures = el.getAttribute('data-sec') === '2';",
        "inFeatures = false;",
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>{css}{EXTRA_CSS}</style>
</head>
<body>

{header_html}

<div class="layout">
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-label">{sidebar_label}</div>
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


def build_index_nav(metas: list[dict]) -> str:
    """Sidebar for the landing page: each diary links to its standalone page."""
    lines = []
    for i, m in enumerate(metas):
        lines.append(f'  <div class="nav-sec" data-sec="{i}">')
        lines.append(
            f'    <a class="nav-h2" href="dev-diaries/{m["slug"]}.html">'
            f'<span class="nav-h2-dot"></span>{m["title"]}</a>'
        )
        lines.append('  </div>')
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    diaries = sorted(DIARY_DIR.glob("*.md"))
    if not diaries:
        sys.exit(f"No dev diaries found in {DIARY_DIR}")

    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    metas: list[dict] = []
    for md in diaries:
        text = md.read_text(encoding="utf-8-sig")
        meta = parse_meta(text, md)
        meta["text"] = text
        metas.append(meta)

    # Newest first.
    metas.sort(key=lambda m: m["date"], reverse=True)

    # --- per-diary standalone pages (docs/dev-diaries/<slug>.html) ---
    for m in metas:
        body = md_to_html(m["text"])
        # Inject the dated byline right after the diary's <h1>.
        byline = f'<p class="diary-byline">{m["date_display"]}</p>'
        body = re.sub(r"(</h1>)", r"\1\n" + byline, body, count=1)
        # Pages live one level deep (docs/dev-diaries/); diary ../assets paths
        # resolve correctly from here, so leave them as written.
        body = gi.annotate_sections(body)
        headings = gi.extract_headings(body)
        nav = gi.build_nav(headings)
        page = build_page(
            title=f'{m["title"]} — Flavorium Universalis',
            header_html=_header("../", "Dev Diary"),
            sidebar_label="Contents",
            nav_html=nav,
            body_html=body,
        )
        (PAGES_DIR / f'{m["slug"]}.html').write_text(page, encoding="utf-8")

    # --- landing card index (docs/dev-diaries.html) ---
    cards = ['<h1>Dev Diaries</h1>', '<div class="diary-index">']
    for m in metas:
        cards.append(
            f'<a class="diary-card" href="dev-diaries/{m["slug"]}.html">'
            f'<div class="dc-date">{m["date_display"]}</div>'
            f'<div class="dc-title">{m["title"]}</div>'
            f'<div class="dc-blurb">{m["blurb"]}</div>'
            f'<span class="dc-more">Read &rarr;</span>'
            f'</a>'
        )
    cards.append('</div>')
    index_body = "\n".join(cards)

    index_page = build_page(
        title="Dev Diaries — Flavorium Universalis",
        header_html=_header("", "Dev Diaries"),
        sidebar_label="Dev Diaries",
        nav_html=build_index_nav(metas),
        body_html=index_body,
    )
    INDEX_OUT.write_text(index_page, encoding="utf-8")

    print(f"Written {INDEX_OUT} (index of {len(metas)} diaries)")
    for m in metas:
        print(f"  - dev-diaries/{m['slug']}.html  [{m['date_display']}]  {m['title']}")


if __name__ == "__main__":
    main()
