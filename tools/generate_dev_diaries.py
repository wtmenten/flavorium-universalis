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

LAYOUT COMPONENTS. Raw HTML lines pass through and the Markdown between them is still
converted, so a diary can wrap ordinary prose in these (each tag on its own line):

  <div class="dd-cols">                cards side by side, collapsing on narrow screens
    <div class="dd-card">
    <div class="dd-eyebrow">Label</div>
    ...markdown...
    </div>
  </div>
  <div class="dd-split">               text beside its figure on wide screens
    <div>...markdown...</div>
    <figure>...</figure>
  </div>
  <div class="dd-tabs">                tabs built by the page script; without JS the
    <section data-tab="Label">         panels show stacked, each labelled
    ...markdown...
    </section>
  </div>
  <details class="dd-more">            optional detail, collapsed
    <summary>What can happen</summary>
    ...markdown...
  </details>

Do NOT put headings inside tabs or <details>: the sidebar is built from h2/h3 and would
link to something hidden.

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
.content figure img{display:block;width:100%;height:auto;max-height:760px;object-fit:contain;background:#0f1116}
.content figcaption{padding:8px 14px;font-size:12.5px;color:var(--text-mid);border-top:1px solid var(--card-border)}
.fig-row{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:18px 0}
.fig-row figure{margin:0}
@media(max-width:680px){.fig-row{grid-template-columns:1fr}}
/* ----- dev diary layout: wider on wide screens, prose kept to a readable measure ----- */
@media(min-width:1500px){.content{max-width:1320px}}
.content>p,.content>ul,.content>blockquote,.h3-group>p,.h3-group>ul,.dd-split>div>p,.dd-split>div>ul,.dd-tabs>section>p,.dd-tabs>section>ul,.dd-more>p,.dd-more>ul{max-width:78ch}
/* cards side by side */
.dd-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin:16px 0 18px}
.dd-card{background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:14px 16px 12px;font-size:14px;line-height:1.55}
.dd-card p:last-child,.dd-card ul:last-child{margin-bottom:0}
.dd-card:nth-child(5n+1){--c:var(--gold)}.dd-card:nth-child(5n+2){--c:var(--adm)}.dd-card:nth-child(5n+3){--c:var(--dip)}.dd-card:nth-child(5n+4){--c:var(--mil)}.dd-card:nth-child(5n){--c:var(--purple)}
.dd-eyebrow{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.11em;color:var(--c,var(--gold));padding-bottom:7px;margin-bottom:9px;position:relative}
.dd-eyebrow::after{content:'';position:absolute;left:0;bottom:0;width:28px;height:2px;border-radius:2px;background:var(--c,var(--gold))}
/* text beside a figure */
.dd-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,42%);gap:24px;align-items:start;margin:8px 0 18px}
.dd-split>figure{margin:4px 0 0;position:sticky;top:66px}
@media(max-width:1100px){.dd-split{grid-template-columns:1fr}.dd-split>figure{position:static}}
/* tabs */
.dd-tabs{margin:18px 0 20px;background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);overflow:hidden}
.dd-tabbar{display:flex;flex-wrap:wrap;gap:2px;padding:6px 8px 0;background:var(--panel-bg);border-bottom:1px solid var(--card-border)}
.dd-tab{appearance:none;background:none;border:none;color:var(--text-mid);font:inherit;font-size:12.5px;font-weight:600;padding:8px 12px 9px;cursor:pointer;position:relative}
.dd-tab:hover{color:var(--text)}
.dd-tab[aria-selected="true"]{color:var(--gold)}
.dd-tab[aria-selected="true"]::after{content:'';position:absolute;left:12px;right:12px;bottom:-1px;height:2px;border-radius:2px;background:var(--gold)}
.dd-tab:focus-visible{outline:2px solid var(--adm);outline-offset:-2px}
.dd-tabs>section{padding:14px 18px 6px}
.dd-tabs:not(.js)>section::before{content:attr(data-tab);display:block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.11em;color:var(--gold);margin-bottom:8px}
.dd-tabs:not(.js)>section+section{border-top:1px solid var(--card-border)}
/* optional detail */
.dd-more{margin:4px 0 14px}
.dd-more>summary{cursor:pointer;color:var(--adm);font-size:13px;font-weight:600;list-style:none;display:inline-block}
.dd-more>summary::-webkit-details-marker{display:none}
.dd-more>summary::before{content:'\\25B8';display:inline-block;margin-right:6px;transition:transform .12s}
.dd-more[open]>summary::before{transform:rotate(90deg)}
.dd-more[open]>summary{margin-bottom:8px}
/* ----- diary entry byline (per-diary pages) ----- */
.diary-byline{color:var(--text-dim);font-size:12px;text-transform:uppercase;letter-spacing:.08em;margin:-2px 0 18px}
/* ----- dev diary index cards (landing page) ----- */
.diary-index{display:flex;flex-direction:column;gap:14px;margin-top:10px}
.diary-card{display:block;background:var(--card-bg);border:1px solid var(--card-border);border-radius:var(--radius);padding:18px 20px 16px;text-decoration:none;color:inherit;transition:background .12s,border-color .12s,transform .12s}
.diary-card:hover{background:var(--hover-bg);border-color:#3f4452;transform:translateY(-1px)}
.diary-card .dc-date{color:var(--gold);font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.11em}
.diary-card .dc-title{color:var(--text);font-size:18px;font-weight:700;margin:5px 0 8px;padding-bottom:9px;position:relative}
.diary-card .dc-title::after{content:'';position:absolute;left:0;bottom:0;width:32px;height:2px;border-radius:2px;background:var(--gold);transition:width .12s,background .12s}
.diary-card:hover .dc-title::after{width:48px;background:var(--adm)}
.diary-card .dc-blurb{color:var(--text-mid);font-size:14px;line-height:1.55}
.diary-card .dc-more{display:inline-block;margin-top:9px;font-size:12px;color:var(--adm);font-weight:600}
"""


# Builds the tab bars for .dd-tabs. Arrow keys move between tabs. Without this script
# the panels simply show stacked with their labels (see the CSS above).
EXTRA_JS = """
(function(){
  var boxes = document.querySelectorAll('.dd-tabs');
  Array.prototype.forEach.call(boxes, function(box, bi){
    var panels = Array.prototype.filter.call(box.children, function(c){
      return c.tagName === 'SECTION' && c.hasAttribute('data-tab');
    });
    if (!panels.length) return;
    var bar = document.createElement('div');
    bar.className = 'dd-tabbar';
    bar.setAttribute('role', 'tablist');
    function select(i){
      panels.forEach(function(p, k){
        p.hidden = k !== i;
        var b = bar.children[k];
        b.setAttribute('aria-selected', k === i ? 'true' : 'false');
        b.tabIndex = k === i ? 0 : -1;
      });
    }
    panels.forEach(function(p, i){
      var id = 'ddt' + bi + '-' + i;
      p.id = id;
      p.setAttribute('role', 'tabpanel');
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'dd-tab';
      b.textContent = p.getAttribute('data-tab');
      b.setAttribute('role', 'tab');
      b.setAttribute('aria-controls', id);
      b.addEventListener('click', function(){ select(i); });
      b.addEventListener('keydown', function(e){
        var n = panels.length, j = null;
        if (e.key === 'ArrowRight') j = (i + 1) % n;
        if (e.key === 'ArrowLeft') j = (i - 1 + n) % n;
        if (j !== null) { e.preventDefault(); select(j); bar.children[j].focus(); }
      });
      bar.appendChild(b);
    });
    box.insertBefore(bar, box.firstChild);
    box.classList.add('js');
    select(0);
  });
})();
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

<script>{script}{EXTRA_JS}</script>

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
            title=f'{m["title"]} | Flavorium Universalis',
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
        title="Dev Diaries | Flavorium Universalis",
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
