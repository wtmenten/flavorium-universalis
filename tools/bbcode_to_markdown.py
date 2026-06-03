#!/usr/bin/env python3
"""Convert a BBCode file to Markdown."""

import argparse
import sys
import bbcode
import html2text


def _heading_tag(tag_name, value, options, parent, context):
    level = tag_name[1]  # '1', '2', or '3'
    return f"<h{level}>{value}</h{level}>"


def _wrap_tag(html_tag):
    def renderer(tag_name, value, options, parent, context):
        return f"<{html_tag}>{value}</{html_tag}>"
    return renderer


def convert(bbcode_text: str) -> str:
    parser = bbcode.Parser()
    parser.add_formatter("h1", _heading_tag, render_embedded=True)
    parser.add_formatter("h2", _heading_tag, render_embedded=True)
    parser.add_formatter("h3", _heading_tag, render_embedded=True)
    parser.add_formatter("table", _wrap_tag("table"), render_embedded=True)
    parser.add_formatter("tr", _wrap_tag("tr"), render_embedded=True)
    parser.add_formatter("th", _wrap_tag("th"), render_embedded=True)
    parser.add_formatter("td", _wrap_tag("td"), render_embedded=True)
    html_content = parser.format(bbcode_text)
    handler = html2text.HTML2Text()
    handler.ignore_links = False
    handler.body_width = 0
    return handler.handle(html_content).strip()


def main():
    parser = argparse.ArgumentParser(description="Convert BBCode file to Markdown")
    parser.add_argument("input", help="Input .bbcode file")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        text = f.read()

    result = convert(text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result + "\n")
        print(f"Written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
