"""Convert one hand-coded XHTML article to Markdown.

Each element is handled by a rule (blocks.py, markdown.py, code.py). An
element without a rule is passed through unchanged as raw HTML, so nothing
is lost while rules are still being written; the notes list what passed
through.
"""

import json
import re

import lxml.html
import yaml

from . import __version__
from . import code  # registers inline <code> and <tt>
from .blocks import render_blocks
from .head import extract_head
from .images import localise_images
from .links import localise_links
from .inventory import article_source
from .aplmap import apply_mapping, load_table, repair_varch_boxes
from .legacy import decode, fix_comments, normalise
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


XSL_MANGLED = re.compile(r"^(?:content/\S*?/)?(https?):/+(.+)$")


def _captured_article(page):
    """The article in a page the old site served, captured by the Wayback
    Machine: the contents of div#article, with links that the old site's
    article.xsl mangled repaired (it prefixed the article's folder to any
    link not starting http://, so https://… became content/…/https://…)."""
    doc = lxml.html.fromstring("<html><head></head><body></body></html>")
    body = doc.find("body")
    for el in page.xpath('//div[@id="article"]')[0]:
        body.append(el)
    for a in doc.iter("a"):
        m = XSL_MANGLED.match(a.get("href") or "")
        if m:
            a.set("href", f"{m.group(1)}://{m.group(2)}")
    return doc


def load_source(root, fmt, path, notes, vid=None, corrections=None):
    """Parse a source as the converter sees it: legacy HTML is decoded (or
    read in the encoding a correction gives) with its comment markup fixed,
    and normalised; curated corrections are applied to the text; a fragment
    is given a body."""
    data = (root / path).read_bytes()
    forced = corrections.encoding(vid) if corrections else None
    apl = corrections.apl(vid) if corrections else None
    if forced:
        text, how = data.decode(forced, errors="replace"), forced
    elif fmt == "HTML":
        text, how = decode(data, keep_undefined=bool(apl))
    else:
        text, how = data.decode("utf-8", errors="replace"), "utf-8"
    if how != "utf-8":
        notes.append({"kind": "decoded", "how": how})
    if corrections:
        text = corrections.apply_text(vid, text, notes)
    if fmt == "HTML":
        text = fix_comments(text)
    doc = lxml.html.fromstring(re.sub(r"^\s*<\?xml[^>]*\?>", "", text))
    if fmt == "WAYBACK":
        doc = _captured_article(doc)
    if doc.find("body") is None:
        page = lxml.html.fromstring("<html><head></head><body></body></html>")
        page.find("body").append(doc)
        doc = page
    if fmt == "HTML":
        normalise(doc, notes)
    if apl:
        apply_mapping(doc, load_table(apl), notes, apl)
    if corrections and corrections.boxes(vid) == "varch-j":
        for pre in doc.iter("pre"):
            if pre.text and not len(pre):
                pre.text = repair_varch_boxes(pre.text)
        notes.append({"kind": "boxes-repaired", "how": "varch-j"})
    return expand_pre_tabs(doc)


def convert(root, record, links=None, corrections=None):
    """Return (markdown, notes, assets) for RECORD's XHTML source.

    ASSETS maps paths relative to the page to the source files to copy.
    LINKS, a LinkIndex, enables rewriting links to the old site.
    """
    fmt, source = article_source(record)
    notes = []
    doc = load_source(root, fmt, source, notes, record["id"], corrections)
    fm, lead = extract_head(doc, record, notes)
    assets = localise_images(doc, root, source, notes)
    if links is not None:
        assets.update(localise_links(doc, root, source, links, notes))
    fm["source"] = source
    if fmt == "WAYBACK":  # provenance: the capture it came from
        page = (root / source).resolve()
        manifest = json.loads((page.parents[1] / "manifest.json").read_text(encoding="utf-8"))
        fm["wayback"] = manifest.get(f"{page.parent.name}/{page.name}", {}).get("wayback")
    fm["converter"] = f"vecrescue {__version__}"
    blocks = lead + body_blocks(doc.find("body"), notes)
    return front_matter(fm) + "\n" + "\n\n".join(blocks) + "\n", notes, assets


def convert_article(root, record):
    return convert(root, record)[0]
