"""Issue #24: fetch captures from the Wayback Machine into sources/wayback/.

The CDX API lists captures; for each URL the latest successful capture is
fetched unmodified (the `id_` form) and saved under sources/wayback/<host>/
<path>, with a manifest of URL, capture time, size and SHA-256. Requests
are made one at a time with a pause, and files already fetched are skipped,
so a run can be repeated or resumed.
"""

import gzip
import hashlib
import json
import re
import time
import urllib.request
from pathlib import Path
from urllib.parse import quote, urlencode, urlsplit

CDX = "https://web.archive.org/cdx/search/cdx"
RAW = "https://web.archive.org/web/{ts}id_/{url}"
AGENT = "vector-rescue (archive recovery; https://github.com/5jt/vector-rescue)"


def http_get(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def normalise_url(url):
    return re.sub(r"^(https?://[^/:]+):80(?=/|$)", r"\1", url)


def cdx_rows(query, get=http_get):
    """All capture rows for a CDX query, header first."""
    params = {"output": "json", "fl": "timestamp,original,mimetype,statuscode", **query}
    data = get(f"{CDX}?{urlencode(params)}")
    return json.loads(data) if data.strip() else [["timestamp", "original", "mimetype", "statuscode"]]


def latest_captures(rows):
    """{url: timestamp} of the latest successful capture of each URL.

    A 'revisit' record (status '-') is the same content as an earlier
    capture, and Wayback serves it, so it counts as successful.
    """
    out = {}
    for ts, url, mime, status in (r[:4] for r in rows[1:]):
        if status == "200" or (status == "-" and mime == "warc/revisit"):
            url = normalise_url(url)
            if ts > out.get(url, ""):
                out[url] = ts
    return out


def target_path(url):
    """Where a capture of URL is saved, relative to sources/wayback/."""
    u = urlsplit(normalise_url(url))
    host = re.sub(r"^www\.", "", u.hostname or "")
    path = u.path or "/"
    if path.endswith("/"):
        path += "index.html"
    elif "." not in path.rsplit("/", 1)[-1]:
        path += ".html"
    if u.query:
        path += quote("?" + u.query, safe="")
    return host + path


class Fetcher:
    def __init__(self, root, get=http_get, pause=1.5, retries=4):
        self.root, self.get, self.pause, self.retries = Path(root), get, pause, retries
        self.manifest_path = self.root / "manifest.json"
        self.manifest = (json.loads(self.manifest_path.read_text(encoding="utf-8"))
                         if self.manifest_path.exists() else {})
        self.failed = {}

    def _get(self, url):
        for attempt in range(self.retries):
            try:
                return self.get(url)
            except Exception as e:  # network errors, 429 and 5xx from Wayback
                error = e
                time.sleep(self.pause * 2 ** (attempt + 1))
        raise error

    def fetch_all(self, jobs):
        """Fetch {url: timestamp}; return how many files were newly saved.

        Several URLs (http and https, say) may save to the same file: their
        captures are tried newest first until one succeeds.
        """
        by_target = {}
        for url, ts in jobs.items():
            by_target.setdefault(target_path(url), []).append((ts, url))
        saved = 0
        for rel, candidates in sorted(by_target.items()):
            if rel in self.manifest and (self.root / rel).exists():
                continue
            data = None
            for ts, url in sorted(candidates, reverse=True):
                wayback = RAW.format(ts=ts, url=url)
                try:
                    data = self._get(wayback)
                    break
                except Exception as e:
                    error = e
            if data is None:
                for _, url in candidates:
                    self.failed[url] = str(error)
                continue
            if data[:2] == b"\x1f\x8b":
                data = gzip.decompress(data)
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            self.manifest[rel] = {"url": url, "timestamp": ts, "wayback": wayback,
                                  "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            self.manifest_path.write_text(json.dumps(self.manifest, indent=1, sort_keys=True),
                                          encoding="utf-8")
            saved += 1
            time.sleep(self.pause)
        return saved


def plan(inventory, cdx):
    """The sets of captures to fetch, as {set name: {url: timestamp}}.

    CDX is a function from a query dict to CDX rows (header first).
    """
    known = {r["id"] for r in inventory if r.get("id")}

    def crosscheck(r):  # sources we cannot convert directly: non-UTF-8 HTML, or PDF only
        live = [s for s in r.get("sources", []) if s.get("exists")]
        return live and not any(s["fmt"] == "XHTML" or (s["fmt"] == "HTML" and s["utf8"]) for s in live)

    wanted = {r["id"] for r in inventory if r.get("id") and crosscheck(r)}
    pages = latest_captures(cdx({"url": "archive.vector.org.uk/art*"}))
    by_id = {}  # ID → every captured URL for it (http, https), for fallback
    for url in pages:
        m = re.search(r"/art(\d{8})$", url)
        if m:
            by_id.setdefault(m.group(1), []).append(url)

    images = {}
    for folder in ("264", "271"):
        rows = cdx({"url": f"archive.vector.org.uk/content/printed/{folder}/*"})
        images.update({u: t for u, t in latest_captures(rows).items()
                       if re.search(r"\.(png|jpe?g|gif|svg)$", u, re.I)})

    pdfs = cdx({"url": "vector.org.uk/wp-content/uploads/*"})
    return {
        "index": latest_captures(cdx({"url": "archive.vector.org.uk/index.xml"})),
        "new-articles": {**{u: pages[u] for i in by_id if i not in known for u in by_id[i]}, **images},
        "issue-pdfs": {u: t for u, t in latest_captures(pdfs).items() if u.lower().endswith(".pdf")},
        "crosscheck": {u: pages[u] for i in wanted if i in by_id for u in by_id[i]},
    }
