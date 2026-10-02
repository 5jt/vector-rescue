"""Issue #24: fetching captures from the Wayback Machine (no network)."""

import gzip
import json

import pytest

from vecrescue.wayback import Fetcher, latest_captures, target_path

ROWS = [
    ["timestamp", "original", "mimetype", "statuscode"],
    ["20160214064447", "http://archive.vector.org.uk/art10501610", "text/html", "200"],
    ["20180101000000", "http://archive.vector.org.uk/art10501610", "text/html", "200"],
    ["20190101000000", "http://archive.vector.org.uk/art10501610", "text/html", "404"],
    ["20170826042458", "http://archive.vector.org.uk:80/art10501740", "text/html", "200"],
    ["20181106151058", "http://archive.vector.org.uk/content/printed/264/ike/fig01.png", "warc/revisit", "-"],
    ["20250819081328", "http://archive.vector.org.uk/content/x/https:/oeis.org/A1", "text/html", "404"],
]


def test_latest_successful_capture_per_url():
    got = latest_captures(ROWS)
    assert got == {
        "http://archive.vector.org.uk/art10501610": "20180101000000",
        "http://archive.vector.org.uk/art10501740": "20170826042458",
        "http://archive.vector.org.uk/content/printed/264/ike/fig01.png": "20181106151058",
    }


@pytest.mark.parametrize("url, path", [
    ("http://archive.vector.org.uk/art10501740", "archive.vector.org.uk/art10501740.html"),
    ("http://archive.vector.org.uk:80/index.xml", "archive.vector.org.uk/index.xml"),
    ("https://vector.org.uk/wp-content/uploads/2022/07/VOL.1-NO.1-MAY-1984.pdf",
     "vector.org.uk/wp-content/uploads/2022/07/VOL.1-NO.1-MAY-1984.pdf"),
    ("http://www.vector.org.uk/", "vector.org.uk/index.html"),
    ("http://archive.vector.org.uk/?vol=24&no=1", "archive.vector.org.uk/index.html%3Fvol%3D24%26no%3D1"),
])
def test_target_path(url, path):
    assert target_path(url) == path


class FakeNet:
    def __init__(self, responses):
        self.responses, self.calls = responses, []

    def __call__(self, url):
        self.calls.append(url)
        return self.responses[url]


def test_fetch_writes_files_and_manifest_and_skips_on_rerun(tmp_path):
    page = b"<html>article</html>"
    net = FakeNet({
        "https://web.archive.org/web/20180101000000id_/http://archive.vector.org.uk/art10501610": page,
        "https://web.archive.org/web/20210830085903id_/http://archive.vector.org.uk/index.xml":
            gzip.compress(b"<rdf/>"),
    })
    f = Fetcher(tmp_path, get=net, pause=0)
    jobs = {"http://archive.vector.org.uk/art10501610": "20180101000000",
            "http://archive.vector.org.uk/index.xml": "20210830085903"}
    assert f.fetch_all(jobs) == 2
    assert (tmp_path / "archive.vector.org.uk/art10501610.html").read_bytes() == page
    assert (tmp_path / "archive.vector.org.uk/index.xml").read_bytes() == b"<rdf/>"
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    entry = manifest["archive.vector.org.uk/art10501610.html"]
    assert entry["url"] == "http://archive.vector.org.uk/art10501610"
    assert entry["timestamp"] == "20180101000000"
    assert entry["size"] == len(page) and len(entry["sha256"]) == 64
    assert Fetcher(tmp_path, get=net, pause=0).fetch_all(jobs) == 0
    assert len(net.calls) == 2


def test_failed_fetch_is_recorded_not_fatal(tmp_path):
    def get(url):
        raise OSError("timed out")
    f = Fetcher(tmp_path, get=get, pause=0, retries=1)
    assert f.fetch_all({"http://archive.vector.org.uk/art1": "2017"}) == 0
    assert f.failed == {"http://archive.vector.org.uk/art1": "timed out"}


def test_plan_chooses_the_sets():
    from vecrescue.wayback import plan
    H = ["timestamp", "original", "mimetype", "statuscode"]
    answers = {
        "archive.vector.org.uk/index.xml": [H, ["20210830085903", "http://archive.vector.org.uk/index.xml", "application/xml", "200"]],
        "archive.vector.org.uk/art*": [H,
            ["2017", "http://archive.vector.org.uk/art10501740", "text/html", "200"],    # new
            ["2017", "http://archive.vector.org.uk/art100072301", "text/html", "200"],   # artefact
            ["2016", "http://archive.vector.org.uk/art10000010", "text/html", "200"],    # converted
            ["2016", "http://archive.vector.org.uk/art10000020", "text/html", "200"],    # cp1252
            ["2016", "http://archive.vector.org.uk/art10000030", "text/html", "200"]],   # PDF only
        "archive.vector.org.uk/content/printed/264/*": [H,
            ["2018", "http://archive.vector.org.uk/content/printed/264/ike/fig01.png", "image/png", "200"],
            ["2018", "http://archive.vector.org.uk/content/printed/264/ike/x.htm", "text/html", "200"]],
        "archive.vector.org.uk/content/printed/271/*": [H],
        "vector.org.uk/wp-content/uploads/*": [H,
            ["2025", "https://vector.org.uk/wp-content/uploads/2022/07/VOL.1-NO.1-MAY-1984.pdf", "application/pdf", "200"],
            ["2025", "https://vector.org.uk/wp-content/uploads/2022/07/logo.png", "image/png", "200"]],
    }
    def cdx(query):
        return answers[query["url"]]
    src = lambda fmt, utf8: [{"fmt": fmt, "path": "x", "exists": True, "utf8": utf8}]
    inventory = [{"id": "10000010", "sources": src("XHTML", True)},
                 {"id": "10000020", "sources": src("HTML", False)},
                 {"id": "10000030", "sources": src("PDF", False)}]
    sets = plan(inventory, cdx)
    assert sets["index"] == {"http://archive.vector.org.uk/index.xml": "20210830085903"}
    assert set(sets["new-articles"]) == {"http://archive.vector.org.uk/art10501740",
                                         "http://archive.vector.org.uk/content/printed/264/ike/fig01.png"}
    assert set(sets["issue-pdfs"]) == {"https://vector.org.uk/wp-content/uploads/2022/07/VOL.1-NO.1-MAY-1984.pdf"}
    assert set(sets["crosscheck"]) == {"http://archive.vector.org.uk/art10000020",
                                       "http://archive.vector.org.uk/art10000030"}
