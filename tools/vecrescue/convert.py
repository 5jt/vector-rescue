"""Convert one hand-coded XHTML article to Markdown.

Each element is handled by a rule (blocks.py, markdown.py, code.py). An
element without a rule is passed through unchanged as raw HTML, so nothing
is lost while rules are still being written; the notes list what passed
through.
"""

import lxml.html
import yaml

from . import __version__
from . import code  # noqa: F401  registers inline <code> and <tt>
from .blocks import render_blocks
from .head import extract_head
from .images import localise_images
from .links import localise_links
from .inventory import xhtml_source
from .markdown import collecting


def body_blocks(body, notes):
    with collecting(notes):
        return render_blocks(body, {"notes": notes, "raw": False})


def front_matter(fm):
    text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{text}---\n"


def convert(root, record, links=None):
    """Return (markdown, notes, assets) for RECORD's XHTML source.

    ASSETS maps paths relative to the page to the source files to copy.
    LINKS, a LinkIndex, enables rewriting links to the old site.
    """
    source = xhtml_source(record)
    doc = lxml.html.fromstring((root / source).read_bytes())
    notes = []
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
