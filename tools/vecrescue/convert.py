"""Convert one hand-coded XHTML article to Markdown.

Each element is handled by a rule. An element without a rule is passed
through unchanged as raw HTML, so nothing is lost while rules are still
being written; the notes list what passed through.
"""

import lxml.html
import yaml

from . import __version__
from .head import extract_head
from .inventory import xhtml_source
from .markdown import INLINE_RULES, inline, raw_html


def para(el):
    return inline(el)


def stray_h1(el, notes):
    """An H1 left after the head block; the page title is the only H1."""
    text = inline(el)
    notes.append({"kind": "h1-demoted", "text": " ".join(el.text_content().split())})
    return f"## {text}"


BLOCK_RULES = {"p": para, "h1": stray_h1}
NEEDS_NOTES = {stray_h1}
INLINE_RULES.update({})


def body_blocks(body, notes):
    blocks = []
    for el in body:
        if not isinstance(el.tag, str):  # comments, processing instructions
            continue
        rule = BLOCK_RULES.get(el.tag)
        if rule is None:
            notes.append({"kind": "raw-html", "tag": el.tag})
        if rule is None:
            block = raw_html(el)
        elif rule in NEEDS_NOTES:
            block = rule(el, notes)
        else:
            block = rule(el)
        if block:
            blocks.append(block)
    return blocks


def front_matter(fm):
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{text}---\n"


def convert(root, record):
    """Return (markdown, notes) for RECORD's XHTML source."""
    source = xhtml_source(record)
    doc = lxml.html.fromstring((root / source).read_bytes())
    notes = []
    fm, lead = extract_head(doc, record, notes)
    fm["source"] = source
    fm["converter"] = f"vecrescue {__version__}"
    blocks = lead + body_blocks(doc.find("body"), notes)
    return front_matter(fm) + "\n" + "\n\n".join(blocks) + "\n", notes


def convert_article(root, record):
    return convert(root, record)[0]
