"""Issue #104: sources from the restored PHP site, archive.vector.org.uk.

The restored site runs a newer copy of the PHP tree than ours (it stops in
November 2016, ours in mid-2016). We fetch what our tree lacks: its two
indexes, the source files they name that we do not have, and the images
those files use; and, for comparison with our conversion, the site's own
rendering of each article page it links. Everything goes under
sources/php-site/, at the path it has on the server, with a manifest.
"""

import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import urljoin

from .wayback import http_get

BASE = "https://archive.vector.org.uk/"
INDEXES = ("index.xml", "issues/index.xml")
SOURCE = re.compile(r'<vec:source fmt="([^"]*)">([^<]*)<')
ASSET = re.compile(rb'(?:src|href)\s*=\s*"([^"#:?]+)"', re.I)
ARTICLE = re.compile(r'href="/?(art\d{8})"')


def missing_sources(index_xml, tree):
    """The source paths named in INDEX_XML (text) that TREE lacks; URLs skipped."""
    out = []
    for _, path in SOURCE.findall(index_xml):
        path = path.strip()
        if path and not path.startswith(("http:", "https:")) and not (Path(tree) / path).exists():
            out.append(path)
    return list(dict.fromkeys(out))


def assets(data, rel):
    """Relative files (images, stylesheets, downloads) that the page DATA at
    REL refers to, as server paths; links to other pages are left out."""
    base = PurePosixPath(rel).parent
    out = []
    for m in ASSET.findall(data):
        target = m.decode("utf-8", "replace")
        if target.startswith("/") or target.endswith((".htm", ".html", ".php")) or "." not in target:
            continue
        parts = []
        for p in (base / target).parts:
            if p == "..":
                parts = parts[:-1]
            elif p != ".":
                parts.append(p)
        out.append("/".join(parts))
    return list(dict.fromkeys(out))


class Fetcher:
    def __init__(self, root, get=http_get, pause=1.0):
        self.root, self.get, self.pause = Path(root), get, pause
        self.manifest_path = self.root / "manifest.json"
        self.manifest = (json.loads(self.manifest_path.read_text(encoding="utf-8"))
                         if self.manifest_path.exists() else {})
        self.failed = {}

    def fetch(self, rel, again=False, save_as=None):
        """Fetch BASE + REL to ROOT/REL (or ROOT/SAVE_AS) unless already held;
        the data, or None."""
        key = save_as or rel
        path = self.root / key
        if path.exists() and key in self.manifest and not again:
            return path.read_bytes()
        url = urljoin(BASE, rel)
        try:
            data = self.get(url)
        except Exception as e:
            self.failed[key] = str(e)
            return None
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        self.manifest[key] = {"url": url, "fetched": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                              "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        self.manifest_path.write_text(json.dumps(self.manifest, indent=1, sort_keys=True), encoding="utf-8")
        time.sleep(self.pause)
        return data

    def sources(self, tree):
        """The indexes (always fetched afresh), then the sources our TREE
        lacks and the files they use. Returns the source paths fetched."""
        index = {rel: self.fetch(rel, again=True) for rel in INDEXES}
        fetched = []
        for rel in missing_sources((index["index.xml"] or b"").decode("utf-8"), tree):
            data = self.fetch(rel)
            if data is None:
                continue
            fetched.append(rel)
            if rel.endswith((".htm", ".html", ".xhtml")):
                for asset in assets(data, rel):
                    if not (Path(tree) / asset).exists():
                        self.fetch(asset)
        return fetched

    def renderings(self):
        """The site's own page for every article its full index links, under
        rendered/art<ID>.html, for comparison with ours."""
        index_page = self.fetch("index", again=True, save_as="rendered/index.html") or b""
        ids = list(dict.fromkeys(ARTICLE.findall(index_page.decode("utf-8", "replace"))))
        for vid in ids:
            self.fetch(vid, save_as=f"rendered/{vid}.html")
        return ids


def compare(rendered, site, stubs):
    """The site's article pages in RENDERED against our build in SITE: the
    kind of each page on either side, and a word check (report.capture_check)
    where both have text."""
    import lxml.html
    from .report import capture_check
    kinds, results = {}, {}
    for f in sorted(Path(rendered).glob("art*.html")):
        vid = f.stem[3:]
        doc = lxml.html.fromstring(f.read_bytes().decode("utf-8", "replace"))
        art = doc.xpath('//div[@id="article"]')
        if not art:
            kind = "no article"
        elif "have this article online" in art[0].text_content():
            kind = "not online"
        elif art[0].xpath(".//iframe"):
            kind = "framed PDF"
        else:
            kind = "text"
        ours = Path(site) / f"art{vid}" / "index.html"
        side = "missing" if not ours.exists() else "stub" if vid in stubs else "page"
        key = f"{kind} / {side}"
        kinds[key] = kinds.get(key, 0) + 1
        if kind == "text" and side == "page":
            rdoc = lxml.html.fromstring(ours.read_bytes().decode("utf-8", "replace"))
            results[vid] = capture_check(doc, rdoc)
    return {"kinds": kinds, "results": results}
