"""Issue #10: the run report.

After each full run, compare every converted article with its built page
and summarise the notes, so that each revision of a rule can be measured
against the last run.
"""

import copy
import difflib
import json
import re
from collections import Counter
from pathlib import Path

import lxml.html

from .head import extract_head
from .convert import load_source
from .inventory import article_source

TAB_WIDTH = 8
LEAD_KINDS = ("subtitle", "byline", "abstract")
SAMPLES = 5
BREAKS = ("br", "td", "th", "dt", "dd", "p", "li", "div", "blockquote", "pre", "hr",
          "h1", "h2", "h3", "h4", "h5", "h6", "table", "tr", "address")


def _words(el):
    el = copy.deepcopy(el)
    for a in el.xpath('.//a[@class="headerlink"]'):
        a.drop_tree()
    for k in el.iter(*BREAKS):  # line, cell and block boundaries separate words
        k.tail = " " + (k.tail or "")
    return el.text_content().replace(" ", " ").split()


def _source_body(source_doc, record):
    """The source body as the converter sees it, and the head lead elements."""
    doc = copy.deepcopy(source_doc)
    removed = []
    extract_head(doc, record, [], removed)
    lead = [el for kind in LEAD_KINDS for k, el in removed if k == kind]
    return doc.find("body"), lead


def _article(rendered_doc):
    found = rendered_doc.xpath("//article")
    return found[0] if found else rendered_doc


def _diff(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return [op for op in sm.get_opcodes() if op[0] != "equal"]


def text_check(source_doc, rendered_doc, record):
    body, lead = _source_body(source_doc, record)
    a = [w for el in lead for w in _words(el)] + _words(body)
    art = copy.deepcopy(_article(rendered_doc))
    title = art.find(".//h1")
    if title is not None:
        title.drop_tree()
    for el in art.xpath('.//p[@class="prefix" or @class="printed"]'):  # template header
        el.drop_tree()
    b = _words(art)
    ops = _diff(a, b)
    return {
        "source_words": len(a),
        "rendered_words": len(b),
        "differing": sum(max(i2 - i1, j2 - j1) for _, i1, i2, j1, j2 in ops),
        "samples": [{"source": " ".join(a[i1:i2]), "rendered": " ".join(b[j1:j2])}
                    for _, i1, i2, j1, j2 in ops[:SAMPLES]],
    }


def capture_check(captured_doc, rendered_doc):
    """Words of the old site's own rendering (captured by the Wayback
    Machine) against ours, title excluded on both sides."""
    a = copy.deepcopy(captured_doc.xpath('//div[@id="article"]')[0])
    for el in a.xpath('.//h1[1]|.//p[@id="validation"]|.//ul[@id="publication"]|.//p[@class="legacy-warning"]'):
        el.drop_tree()
    art = copy.deepcopy(_article(rendered_doc))
    for el in art.xpath('.//h1[1]|.//p[@class="prefix" or @class="printed"]'):
        el.drop_tree()
    x, y = _words(a), _words(art)
    ops = _diff(x, y)
    return {
        "captured_words": len(x),
        "differing": sum(max(i2 - i1, j2 - j1) for _, i1, i2, j1, j2 in ops),
        "samples": [{"captured": " ".join(x[i1:i2]), "rendered": " ".join(y[j1:j2])}
                    for _, i1, i2, j1, j2 in ops[:SAMPLES]],
    }


def _code_text(pre, leading_newline):
    text = pre.text_content()
    if leading_newline and text.startswith("\n"):
        text = text[1:]
    lines = [line.expandtabs(TAB_WIDTH).rstrip() for line in text.split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.pop(0)
    return "\n".join(lines)


def code_check(source_doc, rendered_doc):
    a = [t for t in (_code_text(p, True) for p in source_doc.iter("pre")) if t]
    b = [t for t in (_code_text(p, False) for p in _article(rendered_doc).iter("pre")) if t]
    ops = _diff(a, b)
    return {
        "source_blocks": len(a),
        "rendered_blocks": len(b),
        "mismatched": sum(max(i2 - i1, j2 - j1) for _, i1, i2, j1, j2 in ops),
        "samples": [{"source": "\n".join(a[i1:i2])[:300], "rendered": "\n".join(b[j1:j2])[:300]}
                    for _, i1, i2, j1, j2 in ops[:SAMPLES]],
    }


def image_check(source_doc, rendered_doc, page_dir):
    """Count images on both sides and list rendered ones with no file."""
    srcs = [i.get("src") or "" for i in _article(rendered_doc).iter("img")]
    local = [s for s in srcs if not re.match(r"^[a-z]+:|^/", s, re.I)]
    return {
        "source_images": len(source_doc.xpath('//img[not(ancestor::p[@id="validation"])]')),
        "rendered_images": len(srcs),
        "external": len(srcs) - len(local),
        "broken": [s for s in local if not (Path(page_dir) / s).is_file()],
    }


def anchor_check(rendered_doc):
    """In-page links (#x) and those whose target is not on the page."""
    page = rendered_doc
    targets = {e.get("id") for e in page.iter() if isinstance(e.tag, str) and e.get("id")}
    targets |= {a.get("name") for a in page.iter("a") if a.get("name")}
    hrefs = [a.get("href") for a in _article(page).iter("a")
             if (a.get("href") or "").startswith("#") and len(a.get("href")) > 1
             and "headerlink" not in (a.get("class") or "")]
    return {"links": len(hrefs), "missing": [h for h in hrefs if h[1:] not in targets]}


def link_check(rendered_doc, page_dir, site_dir):
    """Local links on the page, and those that resolve to no file in the site."""
    page_dir, site_dir = Path(page_dir).resolve(), Path(site_dir).resolve()
    hrefs = [a.get("href") for a in _article(rendered_doc).iter("a")
             if a.get("href") and not re.match(r"^(?:[a-z][a-z0-9+.-]*:|#)", a.get("href"), re.I)
             and "headerlink" not in (a.get("class") or "")]
    broken = []
    for h in hrefs:
        path = h.split("#")[0].split("?")[0]
        target = (page_dir / path).resolve()
        if path.endswith("/") or target.is_dir():
            target = target / "index.html"
        if not (target.is_file() and site_dir in target.parents):
            broken.append(h)
    return {"links": len(hrefs), "broken": broken}


def _summarise(notes):
    return {
        "raw_html": dict(Counter(n["tag"] + (f' ({n["reason"]})' if n.get("reason") else "")
                                 for n in notes if n["kind"] == "raw-html")),
        "table_raw": dict(Counter(n["reason"] for n in notes if n["kind"] == "table-raw")),
        "notes": dict(Counter(n["kind"] for n in notes
                              if n["kind"] not in ("raw-html", "table-raw"))),
    }


def _add(total, part):
    for k, v in part.items():
        total[k] = total.get(k, 0) + v


def run_report(src, out, corrections=None):
    src, out = Path(src), Path(out)
    inventory = json.loads((out / "inventory.json").read_text(encoding="utf-8"))
    notes = json.loads((out / "notes.json").read_text(encoding="utf-8"))
    stubs_path = out / "stubs.json"
    stubs = json.loads(stubs_path.read_text(encoding="utf-8")) if stubs_path.exists() else {}
    articles = {}
    totals = {"articles": 0, "raw_html": {}, "table_raw": {}, "notes": {},
              "text_differing_words": 0, "code_mismatched": 0,
              "images": 0, "images_broken": 0, "images_lost": 0,
              "anchor_links_missing": 0, "links_broken": 0,
              "capture_checked": 0, "capture_differing_words": 0}
    for record in inventory:
        page = out / "site" / f"art{record['id']}" / "index.html"
        found = article_source(record) if record.get("id") else None
        if not (found and page.exists()) or record["id"] in stubs:
            continue
        fmt, source = found
        sdoc = load_source(src, fmt, source, [], record["id"], corrections)
        rdoc = lxml.html.fromstring(page.read_bytes().decode("utf-8", errors="replace"))
        art = {"title": record["title"], "source": source,
               **_summarise(notes.get(record["id"], [])),
               "text": text_check(sdoc, rdoc, record),
               "code": code_check(sdoc, rdoc),
               "images": image_check(sdoc, rdoc, page.parent),
               "anchors": anchor_check(rdoc),
               "links": link_check(rdoc, page.parent, out / "site")}
        if record.get("captured") and (src / record["captured"]).is_file():
            art["capture"] = capture_check(lxml.html.fromstring((src / record["captured"]).read_bytes().decode("utf-8", errors="replace")), rdoc)
        articles[record["id"]] = art
        totals["articles"] += 1
        for k in ("raw_html", "table_raw", "notes"):
            _add(totals[k], art[k])
        totals["text_differing_words"] += art["text"]["differing"]
        totals["code_mismatched"] += art["code"]["mismatched"]
        im = art["images"]
        totals["images"] += im["rendered_images"]
        totals["images_broken"] += len(im["broken"])
        totals["images_lost"] += max(0, im["source_images"] - im["rendered_images"])
        totals["anchor_links_missing"] += len(art["anchors"]["missing"])
        totals["links_broken"] += len(art["links"]["broken"])
        if "capture" in art:
            totals["capture_checked"] += 1
            totals["capture_differing_words"] += art["capture"]["differing"]

    skipped_path = out / "skipped.json"
    skipped = json.loads(skipped_path.read_text(encoding="utf-8")) if skipped_path.exists() else {}
    totals["skipped"] = dict(Counter(v["reason"] for v in skipped.values()))
    totals["stubs"] = {"pages": len(stubs), "with_pdf": sum(1 for v in stubs.values() if v["pdf"]),
                       "title_not_found": sum(1 for v in stubs.values() if v["match"] == "not found")}
    totals["transcribed"] = dict(Counter(v["transcribed"] for v in stubs.values() if v.get("transcribed")))

    path, prev_path = out / "report.json", out / "report.prev.json"
    previous = None
    if path.exists():
        previous = json.loads(path.read_text(encoding="utf-8"))["totals"]
        path.replace(prev_path)
    stale = {vid: [n for n in ns if n["kind"] == "correction-stale"] for vid, ns in notes.items()}
    report = {"totals": totals, "previous": previous, "articles": articles, "skipped": skipped,
              "stubs": stubs, "titles": {r["id"]: r["title"] for r in inventory if r.get("id") in stubs},
              "stale": {k: v for k, v in stale.items() if v}}
    path.write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
    (out / "report.md").write_text(render_markdown(report), encoding="utf-8")
    return report


# Markdown rendering ----------------------------------------------------------

def _change(now, before):
    if before is None:
        return ""
    d = now - before
    return "0" if d == 0 else (f"+{d}" if d > 0 else f"−{-d}")


def _counts_table(title, now, before):
    keys = sorted(set(now) | set(before or {}), key=lambda k: (-now.get(k, 0), k))
    if not keys:
        return []
    rows = [f"| {k} | {now.get(k, 0)} | {_change(now.get(k, 0), (before or {}).get(k, 0) if before is not None else None)} |"
            for k in keys]
    return [f"## {title}", "", "| | Now | Change |", "| --- | ---: | ---: |", *rows, ""]


def render_markdown(report):
    t, p = report["totals"], report["previous"]
    get = (lambda k: p.get(k)) if p else (lambda k: None)
    lines = ["# Run report", "",
             "| Measure | Now | Change |", "| --- | ---: | ---: |",
             f"| Articles | {t['articles']} | {_change(t['articles'], get('articles'))} |",
             f"| Differing words | {t['text_differing_words']} | {_change(t['text_differing_words'], get('text_differing_words'))} |",
             f"| Code blocks mismatched | {t['code_mismatched']} | {_change(t['code_mismatched'], get('code_mismatched'))} |",
             *[f"| {label} | {t.get(k, 0)} | {_change(t.get(k, 0), get(k))} |"
               for label, k in (("Images", "images"), ("Images with no file", "images_broken"),
                                ("Images lost", "images_lost"),
                                ("In-page links with no target", "anchor_links_missing"),
                                ("Site links with no page or file", "links_broken"),
                                ("Articles checked against the old site's rendering", "capture_checked"),
                                ("Words differing from the old site's rendering", "capture_differing_words"))],
             ""]
    st = t.get("stubs") or {}
    if st:
        tr = dict(t.get("transcribed") or {})
        failed = tr.pop("failed", 0)  # a transcription with no text (#58)
        states = ", ".join(f"{k} {v}" for k, v in sorted(tr.items()))
        lines += ["## Pages without text", "",
                  f"{st['pages']} indexed articles have a page but no text; {st['with_pdf']} link to their "
                  "first page in the issue PDF"
                  + (f", and {sum(tr.values())} transcribed from the printed issue ({states})" if tr else "")
                  + (f"; {failed} could not be transcribed" if failed else "")
                  + f". For {st['title_not_found']} the title was not found on or next to the computed page:", ""]
        inv_titles = report.get("titles", {})
        lines += [f"- art{vid}: {inv_titles.get(vid, '')} → `{v['pdf']}`"
                  for vid, v in sorted(report.get("stubs", {}).items()) if v["match"] == "not found"]
        lines.append("")
    lines += _counts_table("Not converted yet, by reason", t.get("skipped", {}), get("skipped"))
    lines += _counts_table("Passed through as raw HTML", t["raw_html"], get("raw_html"))
    lines += _counts_table("Tables kept as raw HTML, by reason", t["table_raw"], get("table_raw"))
    lines += _counts_table("Other notes", t["notes"], get("notes"))

    arts = report["articles"]
    worst = sorted((a for a in arts.items() if a[1]["text"]["differing"]),
                   key=lambda a: -a[1]["text"]["differing"])
    if worst:
        lines += ["## Text differences", "",
                  "Words in the source body that differ in the rendered page (title and series prefix excluded).", ""]
        for vid, a in worst[:30]:
            lines.append(f"### art{vid}: {a['title']} ({a['text']['differing']})")
            lines.append("")
            for s in a["text"]["samples"]:
                lines.append(f"- source: `{s['source'][:120]}` → rendered: `{s['rendered'][:120]}`")
            lines.append("")
    broken = [(vid, a) for vid, a in arts.items() if a.get("images", {}).get("broken")]
    if broken:
        lines += ["## Images with no file", ""]
        for vid, a in broken:
            lines.append(f"- art{vid}: {', '.join(a['images']['broken'])}")
        lines.append("")
    stale = [(vid, n["find"]) for vid, ns in report.get("stale", {}).items() for n in ns]
    if stale:
        lines += ["## Corrections no longer found in their source", ""]
        lines += [f"- art{vid}: `{find[:100]}`" for vid, find in stale]
        lines.append("")
    dangling = [(vid, a) for vid, a in arts.items() if a.get("anchors", {}).get("missing")]
    if dangling:
        lines += ["## In-page links with no target", ""]
        for vid, a in dangling:
            lines.append(f"- art{vid}: {', '.join(a['anchors']['missing'])}")
        lines.append("")
    unlinked = [(vid, a) for vid, a in arts.items() if a.get("links", {}).get("broken")]
    if unlinked:
        lines += ["## Site links with no page or file", ""]
        for vid, a in unlinked:
            lines.append(f"- art{vid}: {', '.join(a['links']['broken'])}")
        lines.append("")
    vs = sorted(((vid, a) for vid, a in arts.items() if a.get("capture", {}).get("differing")),
                key=lambda x: -x[1]["capture"]["differing"])
    if vs:
        lines += ["## Differences from the old site's rendering", "",
                  "Words in the old site's own page (captured by the Wayback Machine) that differ in ours.", ""]
        for vid, a in vs[:30]:
            lines.append(f"### art{vid}: {a['title']} ({a['capture']['differing']})")
            lines.append("")
            for s in a["capture"]["samples"]:
                lines.append(f"- old site: `{s['captured'][:120]}` → ours: `{s['rendered'][:120]}`")
            lines.append("")
    bad = [(vid, a) for vid, a in arts.items() if a["code"]["mismatched"]]
    if bad:
        lines += ["## Code block mismatches", ""]
        for vid, a in bad:
            lines.append(f"- art{vid}: {a['title']} ({a['code']['mismatched']})")
        lines.append("")
    return "\n".join(lines)
