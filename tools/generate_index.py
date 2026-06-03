#!/usr/bin/env python3
"""
Generate docs/index.html from WORKSHOP_DESCRIPTION_upload.bbcode.

Usage:
    python tools/generate_index.py
    python tools/generate_index.py --input path/to/file.bbcode
    python tools/generate_index.py --input path/to/file.md
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import bbcode
except ImportError:
    sys.exit("pip install bbcode")

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "WORKSHOP_DESCRIPTION_upload.bbcode"
OUTPUT = ROOT / "docs" / "index.html"


# ---------------------------------------------------------------------------
# BBCode → HTML
# ---------------------------------------------------------------------------

def _slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)         # strip inner tags
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text


def _heading(tag_name, value, options, parent, context):
    level = tag_name[1]
    slug = _slugify(value)
    return f'<h{level} id="{slug}">{value}</h{level}>'


def _wrap(html_tag):
    def renderer(tag_name, value, options, parent, context):
        return f"<{html_tag}>{value}</{html_tag}>"
    return renderer


def _hr_tag(tag_name, value, options, parent, context):
    return "<hr>"


def bbcode_to_html(text: str) -> str:
    p = bbcode.Parser(newline="<br>\n", install_defaults=True)
    p.add_formatter("h1", _heading, render_embedded=True)
    p.add_formatter("h2", _heading, render_embedded=True)
    p.add_formatter("h3", _heading, render_embedded=True)
    p.add_formatter("table", _wrap("table"), render_embedded=True)
    p.add_formatter("tr", _wrap("tr"), render_embedded=True)
    p.add_formatter("th", _wrap("th"), render_embedded=True)
    p.add_formatter("td", _wrap("td"), render_embedded=True)
    p.add_formatter("hr", _hr_tag, standalone=True)
    return p.format(text)


def md_to_html(text: str) -> str:
    """Minimal Markdown → HTML (enough for our workshop description)."""
    try:
        import markdown
        return markdown.markdown(text, extensions=["tables", "fenced_code"])
    except ImportError:
        sys.exit("For .md input, pip install markdown")


# ---------------------------------------------------------------------------
# Extract headings for sidebar nav
# ---------------------------------------------------------------------------

def extract_headings(html: str) -> list[tuple[int, str, str]]:
    """Return list of (level, id, display_text) for h2/h3 elements."""
    results = []
    for m in re.finditer(r'<h([23]) id="([^"]+)">(.*?)</h[23]>', html, re.S):
        level = int(m.group(1))
        slug = m.group(2)
        text = re.sub(r"<[^>]+>", "", m.group(3))
        results.append((level, slug, text.strip()))
    return results


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Flavorium Universalis</title>
<style>
:root{
  --bg:#16181f;--panel-bg:#1e2029;--card-bg:#252830;--card-border:#32363f;
  --hover-bg:#2d3040;--adm:#5baee8;--dip:#5abf7a;--mil:#e07b54;
  --gold:#d4a843;--text:#cdd2de;--text-dim:#6a7085;--text-mid:#9099b0;
  --radius:7px;--sidebar-w:230px;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);font-size:14px;line-height:1.6}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--card-border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:#4a4f5e}

/* layout */
.app{display:grid;grid-template-rows:48px 1fr;height:100vh}
.header{display:flex;align-items:center;gap:14px;padding:0 18px;background:var(--panel-bg);border-bottom:1px solid var(--card-border);z-index:20}
.header h1{font-size:15px;font-weight:700;white-space:nowrap;color:var(--gold)}
.header .sub{font-size:11px;color:var(--text-dim)}
.header .spacer{flex:1}
.header a.tool-link{font-size:11px;color:var(--text-mid);text-decoration:none;padding:4px 10px;border:1px solid var(--card-border);border-radius:4px;white-space:nowrap;transition:color .12s,border-color .12s}
.header a.tool-link:hover{color:var(--text);border-color:var(--adm)}
.body{display:grid;grid-template-columns:var(--sidebar-w) 1fr;overflow:hidden}

/* sidebar */
.sidebar{background:var(--panel-bg);border-right:1px solid var(--card-border);overflow-y:auto;padding:12px 0}
.sidebar-section{padding:6px 14px 4px;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--text-dim);margin-top:6px}
.sidebar a{display:block;padding:4px 14px 4px 18px;font-size:12px;color:var(--text-mid);text-decoration:none;border-left:2px solid transparent;transition:color .1s,background .1s,border-color .1s}
.sidebar a:hover{color:var(--text);background:var(--hover-bg)}
.sidebar a.lvl2{padding-left:18px;font-weight:600;color:var(--text-mid)}
.sidebar a.lvl3{padding-left:30px;font-size:11px;border-left:2px solid transparent}
.sidebar a.lvl3:hover{border-left-color:var(--adm)}
.sidebar a.active{color:var(--text);border-left-color:var(--adm)}

/* content */
.content{overflow-y:auto;padding:28px 44px;max-width:820px}
.content h1{font-size:26px;font-weight:700;color:var(--gold);margin-bottom:8px;margin-top:32px}
.content h1:first-child{margin-top:0}
.content h2{font-size:18px;font-weight:700;color:var(--text);margin-top:40px;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid var(--card-border)}
.content h3{font-size:14px;font-weight:700;color:var(--adm);margin-top:26px;margin-bottom:8px}
.content p{margin-bottom:10px;color:var(--text)}
.content ul,.content ol{margin:6px 0 10px 22px}
.content li{margin-bottom:3px}
.content ul ul,.content ol ul{margin-top:4px}
.content strong{color:var(--text);font-weight:600}
.content em{color:var(--text-mid)}
.content blockquote{margin:12px 0;padding:10px 16px;background:var(--card-bg);border-left:3px solid var(--gold);border-radius:0 var(--radius) var(--radius) 0;color:var(--text-mid);font-style:italic;font-size:13px}
.content blockquote p{color:var(--text-mid)}
.content hr{border:none;border-top:1px solid var(--card-border);margin:18px 0}
.content a{color:var(--adm);text-decoration:none}
.content a:hover{text-decoration:underline}
.content table{border-collapse:collapse;margin:12px 0;width:100%}
.content th{background:var(--hover-bg);color:var(--text);font-size:12px;padding:7px 12px;text-align:left;border:1px solid var(--card-border)}
.content td{padding:6px 12px;font-size:13px;border:1px solid var(--card-border);vertical-align:top}
.content tr:nth-child(even) td{background:rgba(255,255,255,.02)}
/* strip bare <br> after block elements from bbcode newline injection */
h1+br,h2+br,h3+br,hr+br,blockquote+br,table+br,ul+br,ol+br,li>br:last-child{display:none}
</style>
</head>
<body>
<div class="app">
  <header class="header">
    <h1>Flavorium Universalis</h1>
    <span class="sub">EU5 Mod</span>
    <div class="spacer"></div>
    <a class="tool-link" href="planner.html">Advance Planner &rarr;</a>
  </header>
  <div class="body">
    <nav class="sidebar">
      <div class="sidebar-section">Navigation</div>
      {NAV}
    </nav>
    <article class="content" id="content">
      {CONTENT}
    </article>
  </div>
</div>
<script>
// highlight active nav link on scroll
(function(){
  const links = document.querySelectorAll('.sidebar a[href^="#"]');
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        links.forEach(l => l.classList.remove('active'));
        const a = document.querySelector('.sidebar a[href="#' + e.target.id + '"]');
        if (a) a.classList.add('active');
      }
    });
  }, {rootMargin:'-10% 0px -80% 0px'});
  document.querySelectorAll('.content h2[id], .content h3[id]').forEach(h => obs.observe(h));
})();
</script>
</body>
</html>
"""


def build_nav(headings: list[tuple[int, str, str]]) -> str:
    lines = []
    for level, slug, text in headings:
        cls = f"lvl{level}"
        lines.append(f'      <a class="{cls}" href="#{slug}">{text}</a>')
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Generate docs/index.html from workshop description")
    ap.add_argument("--input", default=str(DEFAULT_INPUT),
                    help="BBCode or Markdown source (default: WORKSHOP_DESCRIPTION_upload.bbcode)")
    ap.add_argument("--output", default=str(OUTPUT),
                    help="Output HTML path (default: docs/index.html)")
    args = ap.parse_args()

    src = Path(args.input)
    if not src.exists():
        sys.exit(f"Input not found: {src}")

    text = src.read_text(encoding="utf-8-sig")

    if src.suffix.lower() == ".md":
        html_body = md_to_html(text)
    else:
        html_body = bbcode_to_html(text)

    headings = extract_headings(html_body)
    nav_html = build_nav(headings)

    page = TEMPLATE.replace("{NAV}", nav_html).replace("{CONTENT}", html_body)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"Written {out} ({len(page):,} bytes, {len(headings)} nav items)")


if __name__ == "__main__":
    main()
