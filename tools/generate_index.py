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
# Post-processing helpers
# ---------------------------------------------------------------------------

def extract_headings(html: str) -> list[tuple[int, str, str]]:
    """Return (level, id, display_text) for h2/h3 — tolerates extra attributes."""
    results = []
    for m in re.finditer(r'<h([23])\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h[23]>', html, re.S):
        level = int(m.group(1))
        slug = m.group(2)
        text = re.sub(r"<[^>]+>", "", m.group(3))
        results.append((level, slug, text.strip()))
    return results


def annotate_sections(html: str) -> str:
    """Add data-sec=N to each h2 (for CSS section-color assignment)."""
    idx = 0
    result, last = [], 0
    for m in re.finditer(r'<h2 id="([^"]+)">', html):
        result.append(html[last:m.start()])
        result.append(f'<h2 id="{m.group(1)}" data-sec="{idx}">')
        idx += 1
        last = m.end()
    result.append(html[last:])
    return "".join(result)


def polish_html(html: str) -> str:
    """Small cosmetic post-processing passes."""
    html = re.sub(r"<strong>NEW:</strong>",
                  '<span class="new-badge">NEW</span>', html)
    return html


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Flavorium Universalis — EU5 Mod</title>
<style>
:root{
  --bg:#16181f;--panel-bg:#1e2029;--card-bg:#252830;--card-border:#32363f;
  --hover-bg:#2d3040;
  --adm:#5baee8;--dip:#5abf7a;--mil:#e07b54;--gold:#d4a843;--purple:#a07bdf;
  --text:#cdd2de;--text-dim:#6a7085;--text-mid:#9099b0;
  --radius:7px;--sidebar-w:230px;
}
/* ----- reset ----- */
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);font-size:15px;line-height:1.65}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--card-border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:#4a4f5e}

/* ----- sticky header ----- */
.site-header{position:sticky;top:0;z-index:100;background:var(--panel-bg);border-bottom:1px solid var(--card-border)}
.header-inner{display:flex;align-items:center;gap:10px;padding:0 18px;height:50px}
.menu-btn{background:none;border:none;color:var(--text-mid);font-size:18px;line-height:1;padding:6px 8px;cursor:pointer;border-radius:4px;display:none;flex-shrink:0}
.menu-btn:hover{color:var(--text);background:var(--hover-bg)}
.mod-title{font-size:15px;font-weight:700;color:var(--gold);white-space:nowrap;letter-spacing:.01em}
.ver-badge{font-size:10px;font-weight:700;background:rgba(212,168,67,.12);color:var(--gold);border:1px solid rgba(212,168,67,.3);border-radius:3px;padding:2px 7px;white-space:nowrap}
.hdr-spacer{flex:1}
.planner-link{font-size:11px;color:var(--text-mid);text-decoration:none;padding:5px 12px;border:1px solid var(--card-border);border-radius:4px;white-space:nowrap;transition:color .12s,border-color .12s,background .12s}
.planner-link:hover{color:var(--adm);border-color:var(--adm);background:rgba(91,174,232,.08)}

/* ----- layout: sidebar + main ----- */
.layout{display:flex;min-height:calc(100vh - 50px)}

/* ----- sidebar ----- */
.sidebar{width:var(--sidebar-w);flex-shrink:0;position:sticky;top:50px;height:calc(100vh - 50px);overflow-y:auto;background:var(--panel-bg);border-right:1px solid var(--card-border);padding:16px 0 40px}
.sidebar-label{padding:10px 18px 4px;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--text-dim)}
.nav-sec{margin-bottom:2px}
.nav-h2{display:flex;align-items:center;gap:7px;padding:6px 14px 6px 18px;font-size:12px;font-weight:600;color:var(--text-mid);text-decoration:none;border-left:3px solid transparent;transition:color .1s,background .1s,border-color .1s;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.nav-h2:hover{color:var(--text);background:var(--hover-bg)}
.nav-h2.active{color:var(--text);border-left-color:var(--nav-color,var(--adm))}
.nav-h2-dot{width:7px;height:7px;border-radius:50%;background:var(--nav-color,var(--adm));flex-shrink:0;opacity:.7}
.nav-h2.active .nav-h2-dot{opacity:1}
.nav-sub{display:flex;flex-direction:column}
.nav-h3{padding:4px 14px 4px 38px;font-size:11px;color:var(--text-dim);text-decoration:none;border-left:3px solid transparent;transition:color .1s,background .1s,border-color .1s;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.nav-h3:hover{color:var(--text-mid);background:var(--hover-bg)}
.nav-h3.active{color:var(--text-mid);border-left-color:var(--text-dim)}
/* section accent colors for nav dots */
.nav-sec[data-sec="0"]  .nav-h2{--nav-color:var(--gold)}
.nav-sec[data-sec="1"]  .nav-h2{--nav-color:var(--adm)}
.nav-sec[data-sec="2"]  .nav-h2{--nav-color:var(--gold)}
.nav-sec[data-sec="3"]  .nav-h2{--nav-color:var(--adm)}
.nav-sec[data-sec="4"]  .nav-h2{--nav-color:var(--dip)}
.nav-sec[data-sec="5"]  .nav-h2{--nav-color:var(--mil)}
.nav-sec[data-sec="6"]  .nav-h2{--nav-color:var(--purple)}
.nav-sec[data-sec="7"]  .nav-h2{--nav-color:var(--text-mid)}
.nav-sec[data-sec="8"]  .nav-h2{--nav-color:var(--gold)}
.nav-sec[data-sec="9"]  .nav-h2{--nav-color:var(--adm)}
.nav-sec[data-sec="10"] .nav-h2{--nav-color:var(--text-mid)}
.nav-sec[data-sec="11"] .nav-h2{--nav-color:var(--mil)}

/* ----- main content area ----- */
.main{flex:1;min-width:0}
.content{max-width:1080px;margin:0 auto;padding:36px 36px 100px}

/* ----- hero h1 ----- */
.content h1{font-size:32px;font-weight:800;color:var(--gold);line-height:1.15;margin-bottom:8px;letter-spacing:-.02em}
.content h1::after{content:'';display:block;width:52px;height:3px;background:linear-gradient(90deg,var(--gold),transparent);border-radius:2px;margin-top:12px}

/* ----- section h2 — colored panel bar ----- */
.content h2{font-size:19px;font-weight:700;margin-top:52px;margin-bottom:20px;padding:12px 18px;background:var(--panel-bg);border-radius:var(--radius);border-left:4px solid var(--s-color,var(--text-mid));color:var(--text)}
.content h2[data-sec="0"] {--s-color:var(--gold)}
.content h2[data-sec="1"] {--s-color:var(--adm)}
.content h2[data-sec="2"] {--s-color:var(--gold)}
.content h2[data-sec="3"] {--s-color:var(--adm)}
.content h2[data-sec="4"] {--s-color:var(--dip)}
.content h2[data-sec="5"] {--s-color:var(--mil)}
.content h2[data-sec="6"] {--s-color:var(--purple)}
.content h2[data-sec="7"] {--s-color:var(--text-mid)}
.content h2[data-sec="8"] {--s-color:var(--gold)}
.content h2[data-sec="9"] {--s-color:var(--adm)}
.content h2[data-sec="10"]{--s-color:var(--text-mid)}
.content h2[data-sec="11"]{--s-color:var(--mil)}

/* ----- h3 sections — editorial border-left style ----- */
.h3-group{padding-left:18px;border-left:3px solid var(--g-color,var(--adm));margin:24px 0 28px}
.h3-group h3{font-size:14px;font-weight:700;color:var(--g-color,var(--adm));margin-bottom:10px;margin-top:0}

/* ----- Features section: 2-col grid tiles ----- */
.feat-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin:16px 0;align-items:start}
.feat-grid .h3-group{border-left:none;padding-left:0;margin:0;background:var(--card-bg);border:1px solid var(--card-border);border-top:3px solid var(--g-color,var(--adm));border-radius:var(--radius);padding:16px 18px}
.feat-grid .h3-group h3{font-size:11px;text-transform:uppercase;letter-spacing:.07em}
/* suppress bbcode <br> newline artifacts inside grid tiles */
.feat-grid .h3-group br{display:none}

/* ----- prose ----- */
.content p{margin-bottom:10px}
.content strong{color:var(--text);font-weight:600}
.content em{color:var(--text-mid)}
.content a{color:var(--adm);text-decoration:none}
.content a:hover{text-decoration:underline}

/* ----- lists ----- */
.content ul,.content ol{margin:6px 0 10px 20px}
.content li{margin-bottom:4px}
.content ul ul,.content ol ul{margin-top:4px}

/* ----- blockquote ----- */
.content blockquote{margin:14px 0;padding:12px 18px;background:rgba(212,168,67,.05);border-left:3px solid rgba(212,168,67,.45);border-radius:0 var(--radius) var(--radius) 0;font-size:14px;line-height:1.6}
.content blockquote,.content blockquote p{color:var(--text-mid)}
.content blockquote p:last-child{margin-bottom:0}

/* ----- hr ----- */
.content hr{border:none;height:1px;background:var(--card-border);margin:22px 0}

/* ----- table ----- */
.content table{width:100%;border-collapse:collapse;margin:12px 0;font-size:13px}
.content th{background:var(--hover-bg);color:var(--text);font-weight:600;font-size:12px;padding:8px 12px;text-align:left;border:1px solid var(--card-border)}
.content td{padding:7px 12px;border:1px solid var(--card-border);vertical-align:top}
.content tr:nth-child(even) td{background:rgba(255,255,255,.02)}

/* ----- NEW badge ----- */
.new-badge{display:inline-block;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;padding:1px 5px 2px;border-radius:3px;background:rgba(90,191,122,.12);color:var(--dip);border:1px solid rgba(90,191,122,.28);margin-right:3px;vertical-align:middle;line-height:1.4}

/* ----- anchor scroll offset: clear the sticky 50px header ----- */
.content h1[id],.content h2[id],.content h3[id]{scroll-margin-top:66px}

/* ----- suppress stray <br> after block tags (bbcode newline artifact) ----- */
h1+br,h2+br,h3+br,hr+br,blockquote+br,table+br,ul+br,ol+br{display:none}

/* ----- overlay (mobile sidebar) ----- */
.sidebar-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:98}
body.nav-open .sidebar-overlay{display:block}

/* ----- mobile ----- */
@media(max-width:768px){
  .menu-btn{display:block}
  .sidebar{position:fixed;top:50px;left:0;height:calc(100vh - 50px);z-index:99;transform:translateX(-100%);transition:transform .22s ease}
  body.nav-open .sidebar{transform:translateX(0)}
  .content{padding:22px 18px 80px}
  .content h1{font-size:26px}
  .content h2{font-size:17px;padding:10px 14px;margin-top:36px}
  .feat-grid{grid-template-columns:1fr}
}
@media(max-width:480px){
  .content{padding:18px 14px 60px}
  .h3-group{padding-left:14px}
}
</style>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <button class="menu-btn" id="menuBtn" title="Navigation">&#9776;</button>
    <span class="mod-title">Flavorium Universalis</span>
    <span class="ver-badge">EU5 1.2.*</span>
    <div class="hdr-spacer"></div>
    <a class="planner-link" href="dev-diaries.html">Dev Diaries &rarr;</a>
    <a class="planner-link" href="planner.html">Advance Planner &rarr;</a>
  </div>
</header>

<div class="layout">
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-label">Contents</div>
    {NAV}
  </nav>
  <div class="sidebar-overlay" id="sidebarOverlay"></div>
  <div class="main">
    <article class="content" id="content">
      {CONTENT}
    </article>
  </div>
</div>

<script>
(function(){
  // --- group h3 + following siblings into .h3-group, put Features ones in a .feat-grid ---
  // Uses childNodes (not children) so that bare text nodes produced by bbcode are moved
  // along with their surrounding element siblings and not stranded as orphans.
  var PALETTE = ['--adm','--dip','--mil','--gold','--purple'];
  var content = document.getElementById('content');
  var nodes = Array.prototype.slice.call(content.childNodes); // includes text nodes
  var inFeatures = false, currentGrid = null, currentGroup = null, ci = 0;

  for (var i = 0; i < nodes.length; i++) {
    var el = nodes[i];
    // Text / comment nodes: absorb into current group if one is open
    if (el.nodeType !== 1) {
      if (currentGroup) currentGroup.appendChild(el);
      continue;
    }
    var tag = el.tagName;
    if (tag === 'H2') {
      inFeatures = el.getAttribute('data-sec') === '2';
      currentGrid = null; currentGroup = null; ci = 0;
    } else if (tag === 'H3') {
      var color = 'var(' + PALETTE[ci++ % PALETTE.length] + ')';
      currentGroup = document.createElement('div');
      currentGroup.className = 'h3-group';
      currentGroup.style.setProperty('--g-color', color);
      if (inFeatures) {
        if (!currentGrid) {
          currentGrid = document.createElement('div');
          currentGrid.className = 'feat-grid';
          el.parentNode.insertBefore(currentGrid, el);
        }
        currentGrid.appendChild(currentGroup);
      } else {
        el.parentNode.insertBefore(currentGroup, el);
      }
      currentGroup.appendChild(el);
    } else if (currentGroup) {
      currentGroup.appendChild(el);
    }
  }
})();

(function(){
  // --- scroll-spy: sidebar active links ---
  var allLinks = document.querySelectorAll('.nav-h2, .nav-h3');
  function activate(id) {
    allLinks.forEach(function(l){ l.classList.remove('active'); });
    var a = document.querySelector('[href="#' + id + '"]');
    if (a) {
      a.classList.add('active');
      // also activate parent h2 when a h3 is active
      if (a.classList.contains('nav-h3')) {
        var sec = a.closest('.nav-sec');
        if (sec) { var h2 = sec.querySelector('.nav-h2'); if (h2) h2.classList.add('active'); }
      }
      a.scrollIntoView({block:'nearest'});
    }
  }
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if (e.isIntersecting) activate(e.target.id); });
  }, {rootMargin:'-6% 0px -78% 0px'});
  document.querySelectorAll('.content h2[id], .content h3[id]').forEach(function(h){ obs.observe(h); });
})();

(function(){
  // --- mobile sidebar toggle ---
  var btn = document.getElementById('menuBtn');
  var overlay = document.getElementById('sidebarOverlay');
  function close() { document.body.classList.remove('nav-open'); }
  btn.addEventListener('click', function(){ document.body.classList.toggle('nav-open'); });
  overlay.addEventListener('click', close);
  document.querySelectorAll('.nav-h2, .nav-h3').forEach(function(a){
    a.addEventListener('click', function(){ if (window.innerWidth <= 768) close(); });
  });
})();
</script>

</body>
</html>
"""


def build_nav(headings: list[tuple[int, str, str]]) -> str:
    """Build sidebar nav tree: h2 sections with h3 sub-items grouped inside."""
    lines = []
    sec_idx = -1
    in_sec = False
    for level, slug, text in headings:
        if level == 2:
            if in_sec:
                lines.append('    </div>')   # close nav-sub
                lines.append('  </div>')     # close nav-sec
            sec_idx += 1
            lines.append(f'  <div class="nav-sec" data-sec="{sec_idx}">')
            lines.append(f'    <a class="nav-h2" href="#{slug}"><span class="nav-h2-dot"></span>{text}</a>')
            lines.append('    <div class="nav-sub">')
            in_sec = True
        elif level == 3 and in_sec:
            lines.append(f'      <a class="nav-h3" href="#{slug}">{text}</a>')
    if in_sec:
        lines.append('    </div>')
        lines.append('  </div>')
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

    html_body = annotate_sections(html_body)
    html_body = polish_html(html_body)

    headings = extract_headings(html_body)
    nav_html = build_nav(headings)

    page = TEMPLATE.replace("{NAV}", nav_html).replace("{CONTENT}", html_body)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"Written {out} ({len(page):,} bytes, {len(headings)} nav items)")


if __name__ == "__main__":
    main()
