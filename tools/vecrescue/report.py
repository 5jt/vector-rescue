"""Issue #10: the run report.

After each full run, compare every converted article with its built page
and summarise the notes, so that each revision of a rule can be measured
against the last run.
"""

import copy
import difflib
import json
from collections import Counter
from pathlib import Path

import lxml.html

from .head import extract_head
from .inventory import xhtml_source

TAB_WIDTH = 8
LEAD_KINDS = ("subtitle", "byline", "abstract")
SAMPLES = 5


def _words(el):
    el = copy.deepcopy(el)
    for a in el.xpath('.//a[@class="headerlink"]'):
        a.drop_tree()
    for k in el.iter("br", "td", "th", "dt", "dd"):  # line, cell, term breaks separate words
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
    b = _words(art)
    ops = _diff(a, b)
    return {
        "source_words": len(a),
        "rendered_words": len(b),
        "differing": sum(max(i2 - i1, j2 - j1) for _, i1, i2, j1, j2 in ops),
        "samples": [{"source": " ".join(a[i1:i2]), "rendered": " ".join(b[j1:j2])}
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


def _summarise(notes):
    return {
        "raw_html": dict(Counter(n["tag"] for n in notes if n["kind"] == "raw-html")),
        "table_raw": dict(Counter(n["reason"] for n in notes if n["kind"] == "table-raw")),
        "notes": dict(Counter(n["kind"] for n in notes
                              if n["kind"] not in ("raw-html", "table-raw"))),
    }


def _add(total, part):
    for k, v in part.items():
        total[k] = total.get(k, 0) + v


def run_report(src, out):
    src, out = Path(src), Path(out)
    inventory = json.loads((out / "inventory.json").read_text(encoding="utf-8"))
    notes = json.loads((out / "notes.json").read_text(encoding="utf-8"))
    articles = {}
    totals = {"articles": 0, "raw_html": {}, "table_raw": {}, "notes": {},
              "text_differing_words": 0, "code_mismatched": 0}
    for record in inventory:
        page = out / "site" / f"art{record['id']}" / "index.html"
        source = xhtml_source(record) if record.get("id") else None
        if not (source and page.exists()):
            continue
        sdoc = lxml.html.fromstring((src / source).read_bytes())
        rdoc = lxml.html.fromstring(page.read_bytes())
        art = {"title": record["title"], "source": source,
               **_summarise(notes.get(record["id"], [])),
               "text": text_check(sdoc, rdoc, record),
               "code": code_check(sdoc, rdoc)}
        articles[record["id"]] = art
        totals["articles"] += 1
        for k in ("raw_html", "table_raw", "notes"):
            _add(totals[k], art[k])
        totals["text_differing_words"] += art["text"]["differing"]
        totals["code_mismatched"] += art["code"]["mismatched"]

    path, prev_path = out / "report.json", out / "report.prev.json"
    previous = None
    if path.exists():
        previous = json.loads(path.read_text(encoding="utf-8"))["totals"]
        path.replace(prev_path)
    report = {"totals": totals, "previous": previous, "articles": articles}
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
             ""]
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
    bad = [(vid, a) for vid, a in arts.items() if a["code"]["mismatched"]]
    if bad:
        lines += ["## Code block mismatches", ""]
        for vid, a in bad:
            lines.append(f"- art{vid}: {a['title']} ({a['code']['mismatched']})")
        lines.append("")
    return "\n".join(lines)
