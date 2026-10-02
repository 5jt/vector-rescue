"""Convert one hand-coded XHTML article to Markdown.

Each element is handled by a rule (blocks.py, markdown.py, code.py). An
element without a rule is passed through unchanged as raw HTML, so nothing
is lost while rules are still being written; the notes list what passed
through.
"""

import lxml.html
import yaml

from . import __version__
from . import code  # registers inline <code> and <tt>
from .blocks import render_blocks
from .head import extract_head
from .images import localise_images
from .links import localise_links
from .inventory import article_source
from .legacy import fix_comments, normalise
from .markdown import collecting


def body_blocks(body, notes):
    with collecting(notes):
        return render_blocks(body, {"notes": notes, "raw": False})


def front_matter(fm):
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{text}---\n"


def expand_pre_tabs(doc):
    """Expand tabs in every <pre>, wherever it ends up (raw HTML included)."""
    for pre in doc.iter("pre"):
        code.expand_tabs_in_place(pre)
    return doc


def load_source(root, fmt, path, notes):
    """Parse a source as the converter sees it: legacy HTML has its comment
    markup fixed and is normalised; a fragment is given a body."""
    data = (root / path).read_bytes()
    if fmt == "HTML":
        doc = lxml.html.fromstring(fix_comments(data.decode("utf-8")))
    else:
        doc = lxml.html.fromstring(data)
    if doc.find("body") is None:
        page = lxml.html.fromstring("<html><head></head><body></body></html>")
        page.find("body").append(doc)
        doc = page
    if fmt == "HTML":
        normalise(doc, notes)
    return expand_pre_tabs(doc)


def convert(root, record, links=None):
    """Return (markdown, notes, assets) for RECORD's XHTML source.

    ASSETS maps paths relative to the page to the source files to copy.
    LINKS, a LinkIndex, enables rewriting links to the old site.
    """
    fmt, source = article_source(record)
    notes = []
    doc = load_source(root, fmt, source, notes)
    fm, lead = extract_head(doc, record, notes)
    assets = localise_images(doc, root, source, notes)
    if links is not None:
        assets.update(localise_links(doc, root, source, links, notes))
    fm["source"] = source
    fm["converter"] = f"vecrescue {__version__}"
    blocks = lead + body_blocks(doc.find("body"), notes)
    return front_matter(fm) + "\n" + "\n\n".join(blocks) + "\n", notes, assets


def convert_article(root, record):
    return convert(root, record)[0]
