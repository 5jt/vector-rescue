"""Issue #8: links to the old site.

localise_links runs on the whole source document before conversion, like
localise_images, so links inside raw HTML are rewritten too. Links to
other articles become page-relative directory URLs (../art<ID>/), which
work at any base path and inside raw HTML; the run report checks that
every one resolves. Linked files are copied beside the page.
"""

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlsplit

OLD_SITE = re.compile(
    r"^https?:/{1,2}(?:(?:(?:www|archive|linux)\.)?vector\.org\.uk"
    r"|vector\.johnbutlerassociates\.co\.uk)(?=/|$|\?)", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
OTHER = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|#)", re.I)  # another scheme, or in-page


@dataclass
class LinkIndex:
    pages: set = field(default_factory=set)      # IDs converted in this run
    ids: set = field(default_factory=set)        # every ID in the index
    by_source: dict = field(default_factory=dict)  # vec:source path → ID
    articles: list = field(default_factory=list)   # (ID, volume, issue, file stem)

    @classmethod
    def from_inventory(cls, inventory, pages):
        by_source = {s["path"]: r["id"] for r in inventory if r["id"]
                     for s in r["sources"] if s["path"]}
        articles = [(r["id"], r["volume"], r["issue"], Path(s["path"]).stem)
                    for r in inventory if r["id"] for s in r["sources"]
                    if s["path"] and not s["path"].startswith("http")]
        return cls(set(pages), {r["id"] for r in inventory if r["id"]}, by_source, articles)

    def guess(self, vol, no, art):
        """The one article in VOL, issue NO (or NO-1, for a combined issue),
        whose file name starts with ART; None if none or several."""
        def ids(issue):
            return {i for i, v, n, stem in self.articles
                    if v == vol and n == issue and stem.startswith(art)}
        found = ids(no)
        if not found and no.isdigit():
            found = ids(str(int(no) - 1))
        return found.pop() if len(found) == 1 else None


def _article(vid, fragment, index, notes):
    if vid not in index.ids:
        return None
    if vid not in index.pages:
        notes.append({"kind": "link-to-unconverted", "id": vid})
    return f"../art{vid}/" + (f"#{fragment}" if fragment else "")


def _site_path(href, path, query, fragment, root, index, notes, assets):
    """Resolve a path on the old site; return the new href or None."""
    m = re.fullmatch(r"/?art(\d+)/?", path)
    if m:
        return _article(m.group(1), fragment, index, notes)
    q = parse_qs(query)
    if path in ("", "/", "/index.php") and {"vol", "no", "art"} <= q.keys():
        stem = f"trad/v{q['vol'][0]}{q['no'][0]}/{q['art'][0]}"
        for ext in (".htm", ".pdf"):  # as redirector.php did
            if stem + ext in index.by_source:
                return _article(index.by_source[stem + ext], fragment, index, notes)
        for ext in (".htm", ".pdf"):
            if (root / (stem + ext)).is_file():
                assets[stem + ext] = root / (stem + ext)
                return stem + ext
        vid = index.guess(q["vol"][0], q["no"][0], q["art"][0])
        if vid:  # printed in the newer content/ scheme, or in a combined issue
            new = _article(vid, fragment, index, notes)
            notes.append({"kind": "link-repaired", "href": href, "to": new})
            return new
        return None
    if path in ("", "/", "/index.php", "/index.htm") and not query or re.fullmatch(r"/\d+/?", path):
        notes.append({"kind": "link-repaired", "href": href, "to": "../"})
        return "../"  # the old home page, or a volume: the new home page lists both
    m = re.fullmatch(r"/?(archive/)?(v\d{3}\w*/.+)", path)
    if m:
        tree = "trad/" + m.group(2)  # the old site's archive/ is the recovered trad/
        if tree in index.by_source:
            new = _article(index.by_source[tree], fragment, index, notes)
            if not m.group(1):  # /vNNN/… without archive/: an inference
                notes.append({"kind": "link-repaired", "href": href, "to": new})
            return new
        if (root / tree).is_file():
            assets[tree] = root / tree
            return tree
        return None
    m = re.fullmatch(r"/?(\d+)/(\d+)/?", path)
    if m:
        notes.append({"kind": "link-to-issue", "volume": m.group(1), "issue": m.group(2)})
        return f"../{m.group(1)}/{m.group(2)}/"
    return None


def resolve(href, root, source, index, notes, assets):
    """The new href for HREF, or None if it is left as it is."""
    if EMAIL.fullmatch(href):  # an address without mailto:
        notes.append({"kind": "link-repaired", "href": href, "to": "mailto:" + href})
        return "mailto:" + href
    if OLD_SITE.match(href):
        u = urlsplit(OLD_SITE.sub("http://old", href))
        return _site_path(href, u.path, u.query, u.fragment, root, index, notes, assets)
    if OTHER.match(href):
        return href
    u = urlsplit(href)
    if u.path:  # a file beside the article, or elsewhere in the tree
        base = Path(source).parent
        tail = f"#{u.fragment}" if u.fragment else ""
        full = Path(os.path.normpath(base / unquote(u.path)))
        if (root / full).is_file():
            rel = os.path.relpath(full, base)
            rel = str(full) if rel.startswith("..") else rel
            assets[rel] = root / full
            return quote(rel) + tail
        # Not where the link says: the old folders were reorganised. Try the
        # article's own folder, then the path from the root of the tree.
        for found, rel in ((base / Path(u.path).name, Path(u.path).name),
                           (Path(re.sub(r"^(?:\.\.?/)+", "", u.path)),
                            re.sub(r"^(?:\.\.?/)+", "", u.path))):
            if (root / found).is_file() and "." in Path(rel).name:
                assets[rel] = root / found
                notes.append({"kind": "link-repaired", "href": href, "to": rel + tail})
                return rel + tail
    return _site_path(href, "/" + u.path.lstrip("/"), u.query, u.fragment, root, index, notes, assets)


def localise_links(doc, root, source, index, notes):
    """Rewrite <a href> in DOC; return {path: source file} to copy beside the page."""
    root = Path(root)
    assets = {}
    for a in doc.iter("a"):
        href = (a.get("href") or "").strip()
        if not href:
            continue
        new = resolve(href, root, source, index, notes, assets)
        if new is None:
            notes.append({"kind": "link-unresolved", "href": href})
        elif new != href:
            a.set("href", new)
    return assets
