"""Convert one hand-coded XHTML article to Markdown.

Each element is handled by a rule in RULES. An element without a rule is
passed through unchanged as raw HTML, so nothing is lost while rules are
still being written; the run report lists what passed through.
"""

import re

import lxml.html
import yaml

from .inventory import xhtml_source

FRONT_MATTER_FIELDS = ("id", "title", "volume", "issue", "page")


def _ws(s):
    return re.sub(r"\s+", " ", s or "")


def raw_html(el):
    return lxml.html.tostring(el, encoding="unicode", with_tail=False)


def inline(el):
    """Markdown for the inline content of EL, whitespace collapsed."""
    out = [_ws(el.text)]
    for child in el:
        rule = INLINE_RULES.get(child.tag)
        out.append(rule(child) if rule else raw_html(child))
        out.append(_ws(child.tail))
    return "".join(out).strip()


def para(el):
    return inline(el)


INLINE_RULES = {}
BLOCK_RULES = {"p": para}


def body_blocks(body):
    blocks = []
    for el in body:
        if not isinstance(el.tag, str):  # comments, processing instructions
            continue
        rule = BLOCK_RULES.get(el.tag)
        block = rule(el) if rule else raw_html(el)
        if block:
            blocks.append(block)
    return blocks


def front_matter(record, source):
    fm = {"vid": record["id"]}
    for k in FRONT_MATTER_FIELDS[1:]:
        if record.get(k) is not None:
            fm[k] = record[k]
    fm["source"] = source
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{text}---\n"


def convert_article(root, record):
    source = xhtml_source(record)
    doc = lxml.html.fromstring((root / source).read_bytes())
    body = doc.find("body")
    blocks = body_blocks(body if body is not None else doc)
    return front_matter(record, source) + "\n" + "\n\n".join(blocks) + "\n"
