#!/usr/bin/env python3
"""
wiki_scraper.py — Download EU5 modding wiki pages and generate organized offline docs.

Usage:
  python tools/wiki_scraper.py                  # scrape all pages
  python tools/wiki_scraper.py --pages Effect Trigger   # specific pages
  python tools/wiki_scraper.py --dry-run        # list pages without downloading
  python tools/wiki_scraper.py --consolidate    # consolidate iterators after scrape

Output: docs/offline-wiki/  (core/, concepts/, interface/, entities/, systems/)

Requires: beautifulsoup4, requests (pip install beautifulsoup4 requests)
"""

import argparse
import os
import re
import sys
import time

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(ROOT_DIR)
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs", "offline-wiki")
WIKI_BASE = "https://eu5.paradoxwikis.com"

# ---------------------------------------------------------------------------
# Page catalog: (wiki-title, output-dir, output-file, category-label)
# ---------------------------------------------------------------------------
PAGES = [
    # Core scripting reference
    ("Effect", "core", "effect.md", "Core scripting"),
    ("Trigger", "core", "trigger.md", "Core scripting"),
    ("Scope", "core", "scope.md", "Core scripting"),
    ("Scope_link", "core", "scope_link.md", "Core scripting"),

    # Concepts
    ("Defines", "concepts", "defines.md", "Concepts"),
    ("Modifier_types", "concepts", "modifier_types.md", "Concepts"),
    ("Variable", "concepts", "variable.md", "Concepts"),
    ("Macro", "concepts", "macro.md", "Concepts"),
    ("Script_value", "concepts", "script_value.md", "Concepts"),
    ("Mean_time_to_happen", "concepts", "mtth.md", "Concepts"),
    ("On_actions", "concepts", "on_actions.md", "Concepts"),
    ("Color", "concepts", "color.md", "Concepts"),

    # Interface
    ("Interface_modding_guide", "interface", "interface_modding.md", "Interface"),
    ("GUI_script", "interface", "gui_script.md", "Interface"),
    ("Scripted_gui", "interface", "scripted_gui.md", "Interface"),
    ("Localization", "interface", "localization.md", "Interface"),

    # Entity modding guides
    ("Advance_modding", "entities", "advance_modding.md", "Entities"),
    ("Building_modding", "entities", "building_modding.md", "Entities"),
    ("Character_modding", "entities", "character_modding.md", "Entities"),
    ("Culture_modding", "entities", "culture_modding.md", "Entities"),
    ("Disaster_modding", "entities", "disaster_modding.md", "Entities"),
    ("Disease_modding", "entities", "disease_modding.md", "Entities"),
    ("Estate_modding", "entities", "estate_modding.md", "Entities"),
    ("Event_modding", "entities", "event_modding.md", "Entities"),
    ("Goods_modding", "entities", "goods_modding.md", "Entities"),
    ("Institution_modding", "entities", "institution_modding.md", "Entities"),
    ("International_organization_modding", "entities", "international_organization.md", "Entities"),
    ("Law_modding", "entities", "law_modding.md", "Entities"),
    ("Mission_modding", "entities", "mission_modding.md", "Entities"),
    ("Modifier_modding", "entities", "modifier_modding.md", "Entities"),
    ("Pop_modding", "entities", "pop_modding.md", "Entities"),
    ("Religion_modding", "entities", "religion_modding.md", "Entities"),
    ("Situation_modding", "entities", "situation_modding.md", "Entities"),
    ("Subject_type_modding", "entities", "subject_type_modding.md", "Entities"),
    ("Trait_modding", "entities", "trait_modding.md", "Entities"),
    ("Unit_modding", "entities", "unit_modding.md", "Entities"),
    ("War_modding", "entities", "war_modding.md", "Entities"),

    # Systems
    ("Action_modding", "systems", "action_modding.md", "Systems"),
    ("Concept_modding", "systems", "concept_modding.md", "Systems"),
    ("Setup_modding", "systems", "setup_modding.md", "Systems"),
]


# ---------------------------------------------------------------------------
# HTML fetching
# ---------------------------------------------------------------------------
def fetch_page(title):
    """Fetch a wiki page and return the HTML content."""
    url = f"{WIKI_BASE}/{title}"
    try:
        import requests
        resp = requests.get(url, timeout=30,
                            headers={"User-Agent": "EU5ModDocScraper/1.0"})
        resp.raise_for_status()
        return resp.text
    except ImportError:
        from urllib.request import urlopen, Request
        from urllib.error import HTTPError
        req = Request(url, headers={"User-Agent": "EU5ModScraper/1.0"})
        try:
            with urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except HTTPError as e:
            print(f"  ERROR: {url} -> HTTP {e.code}")
            return None


# ---------------------------------------------------------------------------
# HTML → markdown conversion
# ---------------------------------------------------------------------------
def extract_content(html):
    """Extract article content from wiki HTML and convert to markdown."""
    try:
        from bs4 import BeautifulSoup, Comment
        soup = BeautifulSoup(html, "html.parser")

        # Find the article content container
        content_text = soup.find("div", id="mw-content-text")
        if not content_text:
            return None

        parser_output = content_text.find("div", {"class": "mw-parser-output"})
        if not parser_output:
            return None

        # Remove noise elements
        for el in parser_output.find_all(["div", "nav", "script"]):
            try:
                cls = el.get("class", []) or []
                el_id = el.get("id", "") or ""
            except AttributeError:
                continue
            if el_id in ("toc",):
                el.decompose()
            elif any(c in cls for c in ("toc", "eu4box", "metadata", "navbox",
                                         "portal", "printfooter", "catlinks")):
                el.decompose()

        # Remove comments
        for comment in parser_output.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()

        return convert_to_markdown(parser_output)

    except ImportError:
        print("ERROR: beautifulsoup4 required. Install with: pip install beautifulsoup4")
        return None


def get_clean_text(el):
    """Get text from element, handling links and formatting."""
    parts = []
    for child in el.children:
        try:
            tag = child.name
        except AttributeError:
            text = str(child).strip()
            if text:
                parts.append(text)
            continue

        if tag == "a":
            text = child.get_text().strip()
            href = child.get("href", "")
            if href and not href.startswith("#"):
                # Keep wiki links as text (we don't need clickable links in offline docs)
                parts.append(text)
            else:
                parts.append(text)
        elif tag in ("b", "strong"):
            parts.append(f"**{child.get_text().strip()}**")
        elif tag in ("i", "em"):
            parts.append(f"*{child.get_text().strip()}*")
        elif tag == "code":
            parts.append(f"`{child.get_text().strip()}`")
        elif tag == "br":
            parts.append("\n")
        elif tag in ("span", "sup", "sub"):
            parts.append(child.get_text())
        else:
            parts.append(child.get_text())

    return "".join(parts)


def clean_heading(text):
    """Remove [edit | edit source] and similar artifacts from heading text."""
    text = re.sub(r'\s*\[edit.*?\]\s*', '', text)
    text = re.sub(r'\s*\|\s*edit\s*source\s*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def convert_to_markdown(element):
    """Convert a BeautifulSoup element to markdown."""
    lines = []

    for el in element.children:
        # Skip non-tag elements (text nodes, comments)
        try:
            tag = el.name
        except AttributeError:
            continue

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            raw = el.get_text().strip()
            # Skip TOC heading
            if raw == "Contents":
                continue
            title = clean_heading(raw)
            level = int(tag[1])
            if title:
                lines.append("")
                lines.append(f"{'#' * level} {title}")
                lines.append("")

        elif tag == "p":
            text = get_clean_text(el).strip()
            # Skip wiki maintenance messages
            if ("Please help with verifying" in text or
                "This article needs" in text or
                "stub" in text.lower()):
                continue
            if text:
                lines.append(text)
                lines.append("")

        elif tag == "pre":
            text = el.get_text().strip()
            if text:
                lines.append("```")
                lines.append(text)
                lines.append("```")
                lines.append("")

        elif tag == "table":
            md = table_to_markdown(el)
            if md:
                lines.append(md)
                lines.append("")

        elif tag in ("ul", "ol"):
            for li in el.find_all("li", recursive=False):
                text = get_clean_text(li).strip()
                if text:
                    lines.append(f"- {text}")

        elif tag == "div":
            # Recurse into remaining divs
            nested = convert_to_markdown(el)
            if nested.strip():
                lines.append(nested)

        elif tag == "blockquote":
            text = el.get_text().strip()
            for line in text.split("\n"):
                lines.append(f"> {line}")
            lines.append("")

    return "\n".join(lines)


def table_to_markdown(table_el):
    """Convert a HTML table to a markdown table."""
    rows = table_el.find_all("tr")
    if not rows:
        return ""

    table_rows = []
    for row in rows:
        cells = row.find_all(["th", "td"])
        if not cells:
            continue
        cell_texts = []
        for cell in cells:
            text = get_clean_text(cell).strip()
            text = text.replace("|", "\\|").replace("\n", " ")
            # Collapse whitespace
            text = re.sub(r'\s+', ' ', text)
            cell_texts.append(text)
        if cell_texts:
            table_rows.append(cell_texts)

    if not table_rows:
        return ""

    # Build markdown table
    max_cols = max(len(r) for r in table_rows)
    for row in table_rows:
        while len(row) < max_cols:
            row.append("")

    if len(table_rows) >= 2:
        header = table_rows[0]
        separator = "|" + "|".join(["---"] * len(header)) + "|"
        md_lines = ["|" + "|".join(header) + "|", separator]
        for row in table_rows[1:]:
            md_lines.append("|" + "|".join(row) + "|")
        return "\n".join(md_lines)
    elif len(table_rows) == 1:
        return "|" + "|".join(table_rows[0]) + "|"

    return ""


# ---------------------------------------------------------------------------
# Iterator consolidation
# ---------------------------------------------------------------------------
ITERATOR_RE = re.compile(r"^\|\s*(every_|ordered_|random_|any_)([a-z_]+)\s*\|(.*)$")


def consolidate_iterator_tables(markdown_text):
    """Consolidate iterator table rows by target noun."""
    lines = markdown_text.split("\n")
    output = []
    buffer = []
    in_table = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("|") and "-" in stripped and stripped.count("|") >= 2:
            # Table separator row
            output.append(line)
            continue

        if stripped.startswith("|"):
            m = ITERATOR_RE.match(stripped)
            if m:
                buffer.append((m.group(1), m.group(2), m.group(3)))
                continue

        # Flush buffer if we hit a non-iterator line
        if buffer:
            consolidated = _consolidate_rows(buffer)
            output.extend(consolidated)
            buffer = []

        output.append(line)

    # Flush remaining
    if buffer:
        consolidated = _consolidate_rows(buffer)
        output.extend(consolidated)

    return "\n".join(output)


def _consolidate_rows(rows):
    """Group iterator rows by target noun."""
    targets = {}
    for prefix, target, rest in rows:
        targets.setdefault(target, {})[prefix] = rest

    output = []
    for target in sorted(targets):
        prefixes = targets[target]
        prefix_str = "/".join(sorted(prefixes))
        sample_rest = prefixes.get("every_", list(prefixes.values())[0])
        output.append(f"| {prefix_str}_{target} | {sample_rest}")

    return output


# ---------------------------------------------------------------------------
# README generation
# ---------------------------------------------------------------------------
def generate_readme():
    """Generate the index README for the offline docs."""
    categories = {}
    for title, subdir, outfile, label in PAGES:
        categories.setdefault(label, []).append((title, subdir, outfile))

    lines = [
        "# EU5 Modding Wiki (Offline)",
        "",
        "Offline copy of the [EU5 Paradox Wiki](https://eu5.paradoxwikis.com/) modding pages,",
        "reorganized for AI agent reference. Content preserved from original; layout reorganized.",
        "",
        "## Structure",
        "",
    ]

    for label in ["Core scripting", "Concepts", "Interface", "Entities", "Systems"]:
        entries = categories.get(label, [])
        if not entries:
            continue
        dir_name = label.lower().replace(" ", "-")
        lines.append(f"### [{dir_name}/]({dir_name}/) — {label}")
        lines.append("")
        for title, subdir, outfile in entries:
            display = title.replace("_", " ")
            lines.append(f"- [{display}]({subdir}/{outfile})")
        lines.append("")

    lines.extend([
        "## Quick Search",
        "",
        "Use `python tools/wiki_search.py` for fast lookups:",
        "",
        "```",
        "python tools/wiki_search.py effect <name>       # search effects",
        "python tools/wiki_search.py trigger <name>      # search triggers",
        "python tools/wiki_search.py scope_link <name>   # search scope links",
        "python tools/wiki_search.py modifier <name>     # search modifier types",
        "python tools/wiki_search.py on_action <name>    # search on-actions",
        "```",
        "",
        "## Source",
        "",
        f"Scraped from {WIKI_BASE}/ — run `python tools/wiki_scraper.py` to refresh.",
        "",
    ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def scrape_all(pages=None, dry_run=False, consolidate=False):
    """Scrape wiki pages and write markdown files."""
    if pages:
        filtered = [(t, d, f, l) for t, d, f, l in PAGES if t in pages]
        if not filtered:
            print(f"No matching pages for: {pages}")
            return
        to_scrape = filtered
    else:
        to_scrape = PAGES

    for _, subdir, _, _ in to_scrape:
        os.makedirs(os.path.join(DOCS_DIR, subdir), exist_ok=True)

    if dry_run:
        print(f"Would scrape {len(to_scrape)} pages:")
        for title, subdir, outfile, _ in to_scrape:
            print(f"  {title} -> {subdir}/{outfile}")
        return

    success = 0
    for idx, (title, subdir, outfile, _label) in enumerate(to_scrape):
        url = f"{WIKI_BASE}/{title}"
        print(f"[{idx+1}/{len(to_scrape)}] Fetching {url} ...")

        html = fetch_page(title)
        if html is None:
            continue

        content = extract_content(html)
        if content is None:
            print(f"  WARNING: Could not extract content from {url}")
            continue

        # Clean up excessive blank lines
        content = re.sub(r"\n{3,}", "\n\n", content)

        outpath = os.path.join(DOCS_DIR, subdir, outfile)
        header = f"# {title.replace('_', ' ')}\n\n**Source:** {url}\n\n---\n\n"
        full_content = header + content

        if consolidate:
            full_content = consolidate_iterator_tables(full_content)

        with open(outpath, "w", encoding="utf-8") as f:
            f.write(full_content)

        success += 1
        time.sleep(1.5)

    # Generate README
    readme_path = os.path.join(DOCS_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme())

    print(f"\nDone: {success}/{len(to_scrape)} pages written to {DOCS_DIR}/")
    if consolidate:
        print("Iterator consolidation applied.")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pages", nargs="+", help="Scrape only these wiki page titles")
    parser.add_argument("--dry-run", action="store_true", help="List pages without downloading")
    parser.add_argument("--consolidate", action="store_true",
                        help="Consolidate iterator entries (every_/any_/ordered_/random_)")
    args = parser.parse_args()

    scrape_all(pages=args.pages, dry_run=args.dry_run, consolidate=args.consolidate)


if __name__ == "__main__":
    main()
