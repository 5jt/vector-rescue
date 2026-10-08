"""Pipeline steps. Each reads from SRC (read-only) and writes under OUT."""

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from .convert import convert
from .inventory import article_source, merge_wayback, php_index, php_renderings, read_index, read_issues
from .legacy import decode, mapped_apl, read_codingprobs
from .pages import (_catalogue, damaged_issue_pdfs, issue_pdfs, mark_issue_tabs, nav_toml, publish_unindexed,
                    read_contents, wayback_issue_pdfs, write_home_page, write_index_page, write_tags_page,
                    write_volume_pages)
from . import stubs
from .links import LinkIndex


def run_inventory(src, out, wayback=None, php=None):
    """The canonical inventory: the restored PHP site's index where we have
    it (PHP, #113), else the PHP tree's; then what only the Wayback Machine
    holds."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    records = read_index(php, src) if php_index(php) else read_index(src)
    if wayback is not None:
        records = merge_wayback(records, wayback, src)
    if php_index(php):
        records = php_renderings(records, php, src)
    path = out / "inventory.json"
    path.write_text(json.dumps(records, indent=1, ensure_ascii=False), encoding="utf-8")
    return path


def load_inventory(out):
    return json.loads((Path(out) / "inventory.json").read_text(encoding="utf-8"))


def run_convert(src, out, corrections=None):
    src, out = Path(src), Path(out)
    docs = out / "docs"
    shutil.rmtree(docs, ignore_errors=True)  # every run starts clean
    docs.mkdir(parents=True)
    written, notes = [], {}
    inventory = load_inventory(out)
    listed = read_codingprobs(src)
    todo, skipped = [], {}
    for r in inventory:
        found = r["id"] and article_source(r)
        if not found:
            continue
        fmt, path = found
        held = corrections.held(r["id"]) if corrections else None
        if held:
            reason = f"held: {held}"
        elif fmt == "HTML" and not (corrections and corrections.released(r["id"])):
            text, how = decode((src / path).read_bytes())
            reason = mapped_apl(text, path, listed, unicode=how == "utf-8")
        else:
            reason = None
        if reason:
            skipped[r["id"]] = {"source": path, "reason": reason}
        else:
            todo.append(r)
    (out / "skipped.json").write_text(json.dumps(skipped, indent=1), encoding="utf-8")
    links = LinkIndex.from_inventory(inventory, {r["id"] for r in todo})
    for record in todo:
        folder = docs / f"art{record['id']}"
        folder.mkdir(exist_ok=True)
        markdown, notes[record["id"]], assets = convert(src, record, links, corrections)
        for rel, source in assets.items():
            target = folder / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        path = folder / "index.md"
        path.write_text(markdown, encoding="utf-8")
        written.append(path)
    (out / "notes.json").write_text(json.dumps(notes, indent=1, ensure_ascii=False),
                                    encoding="utf-8")
    return written


def article_pdf(record, src):
    """The article's own PDF in the PHP tree under SRC, if the index names one
    (#111)."""
    for source in record.get("sources") or []:
        if source.get("fmt") == "PDF" and source.get("path") and (Path(src) / source["path"]).is_file():
            return Path(src) / source["path"]
    return None


def write_stub_pages(inventory, issues, pdfs, out, transcriptions=None, damaged=None, src=None):
    """A page for every indexed article without text (issue #38), linking to
    its first page in the issue PDF, or the article's transcription from
    TRANSCRIPTIONS/art<ID>.md where there is one (issue #40). An article
    with neither (its issue has no complete scan) gets no page (#63), unless
    the issue's PDF is in DAMAGED, truncated captures from which the OCR text
    of its pages is recovered and shown (#81). The article's own PDF, where
    the index names one in SRC, is published beside its page (#111). Offsets and
    title checks are cached in OUT/pdf-cache.json; results go to
    OUT/stubs.json for the report."""
    out = Path(out)
    docs = out / "docs"
    cache_path = out / "pdf-cache.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    _, alias = _catalogue(issues)
    texts, results = {}, {}
    starts = {}  # (vol, issue) → printed start pages of every indexed article
    for r in inventory:
        if (r.get("page") or "").isdigit():
            k = alias.get((r.get("volume"), r.get("issue")), (r.get("volume"), r.get("issue")))
            starts.setdefault(k, set()).add(int(r["page"]))
    notes_path = out / "notes.json"
    converted = set(json.loads(notes_path.read_text(encoding="utf-8"))) if notes_path.exists() else set()

    def pages_of(pdf):
        if pdf not in texts:
            texts[pdf] = stubs.recovered_pages(pdf) if pdf in damaged_pdfs else stubs.pdf_pages(pdf)
        return texts[pdf]

    damaged_pdfs = set((damaged or {}).values())

    for r in inventory:
        if not r.get("id") or r["id"] in converted:  # what convert wrote, not what is on disk
            continue
        key = alias.get((r.get("volume"), r.get("issue")), (r.get("volume"), r.get("issue")))
        pdf = pdfs.get(key) or (damaged or {}).get(key)
        whole = pdf and pdf not in damaged_pdfs
        link, match, ocr = None, None, None
        transcription = Path(transcriptions or "") / f"art{r['id']}.md"
        transcription = transcription if transcriptions and transcription.is_file() else None
        warning = None
        if transcription:  # one with no text (a failure, #58) keeps the stub, with its warning
            fm, body = stubs.read_transcription(transcription)
            if not body.strip():
                transcription, warning = None, fm.get("warning") or "This article could not be transcribed."
        if pdf and (r.get("page") or "").isdigit():
            ident = f"{pdf.name}:{pdf.stat().st_size}"
            if ident not in cache:
                cache[ident] = {"offset": stubs.page_offset(pages_of(pdf)), "checks": {}}
            entry = cache[ident]
            if entry["offset"] is not None:
                n = int(r["page"]) + entry["offset"]
                check = f"{stubs.CHECK_RULE}:{r['id']}:{n}:{r['title']}"
                if check not in entry["checks"]:
                    pp = pages_of(pdf)
                    found = lambda k: 1 <= k <= len(pp) and stubs.title_on_page(r["title"], pp[k - 1])
                    entry["checks"][check] = ("page" if found(n) else
                                              "adjacent" if found(n - 1) or found(n + 1) else "not found")
                match = entry["checks"][check]
                link = f"{key[0]}/{key[1]}/{pdf.name}#page={n}" if whole else None
                ocr_key = f"ocr:{check}"
                if not transcription and ocr_key not in entry["checks"]:  # its pages: to the next article, at most 20
                    following = [p for p in starts.get(key, ()) if p > int(r["page"])]
                    last = min(min(following) - 1 if following else 10_000, int(r["page"]) + 19)
                    pp = pages_of(pdf)
                    entry["checks"][ocr_key] = stubs.ocr_block(pp[n - 1:min(len(pp), last + entry["offset"])],
                                                               stubs.OCR_SUMMARY if whole else stubs.DAMAGED_SUMMARY)
                ocr = entry["checks"].get(ocr_key)
        own = article_pdf(r, src) if src else None
        if own:
            (docs / f"art{r['id']}").mkdir(parents=True, exist_ok=True)
            shutil.copyfile(own, docs / f"art{r['id']}" / own.name)
        own = own.name if own else None
        if transcription:
            stubs.write_transcribed(r, docs, transcription, link, own=own)
            review = "doubtful" if fm.get("warning") else fm.get("review")
        elif link or warning or own or (ocr and not whole):
            stubs.write_stub(r, docs, link, ocr if link or not whole else None, warning,
                             None if whole else stubs.DAMAGED, own)
            review = "failed" if warning else None
        else:  # no scan of the issue, nothing to show: no page, and no link to one (#63)
            shutil.rmtree(docs / f"art{r['id']}", ignore_errors=True)
            review = None
        results[r["id"]] = {"pdf": link, "match": match, "transcribed": review,
                            "own_pdf": own,
                            "page": bool(transcription or link or warning or own or (ocr and not whole))}
    cache_path.write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf-8")
    (out / "stubs.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    return results


def pdf_links(pdfs, out):
    """{(vol, issue): (path of the issue PDF from the site root, offset of PDF
    page from printed page)} for each issue PDF whose offset is known, from
    OUT/pdf-cache.json (written by write_stub_pages), so a Contents line can
    link to its page (#93)."""
    path = Path(out) / "pdf-cache.json"
    cache = json.loads(path.read_text()) if path.exists() else {}
    links = {}
    for key, pdf in pdfs.items():
        entry = cache.get(f"{pdf.name}:{pdf.stat().st_size}")
        if entry and entry.get("offset") is not None:
            links[key] = (f"{key[0]}/{key[1]}/{pdf.name}", entry["offset"])
    return links


def _digest(path):
    """A short hash of PATH's contents, to version its URL so browsers fetch
    a changed stylesheet rather than reuse a cached one."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:8]


def run_site(src, out, config, wayback=None, corrections=None, transcriptions=None, php=None):
    """Write the home and issue pages, copy the site files from CONFIG's
    folder, and build OUT/docs into OUT/site with Zensical."""
    src, out, config = Path(src), Path(out), Path(config)
    docs = out / "docs"
    catalogue = php if php is not None and (Path(php) / "issues" / "index.xml").is_file() else src
    inventory, issues = load_inventory(out), read_issues(catalogue)
    if corrections:
        issues = corrections.apply_catalogue(issues)
    more = wayback_issue_pdfs(wayback) if wayback else None
    pdfs = issue_pdfs(issues, src, more)
    damaged = {k: v for k, v in damaged_issue_pdfs(wayback).items() if k not in pdfs} if wayback else None
    write_stub_pages(inventory, issues, pdfs, out, transcriptions, damaged, src)
    links = pdf_links(pdfs, out)
    publish_unindexed(transcriptions, docs, links)
    contents = read_contents(Path(transcriptions) / "contents") if transcriptions else {}
    thumbs = src / "images" / "covers" / "32x45"
    write_volume_pages(inventory, issues, src, docs, more, thumbs, contents, links)
    write_home_page(inventory, issues, docs, thumbs)
    write_index_page(inventory, issues, docs, contents, links)
    status = config.parent / "pages" / "status.md"  # the project status page (#93)
    if status.is_file():
        (docs / "status").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(status, docs / "status" / "index.md")
    mark_issue_tabs(inventory, issues, docs)
    if transcriptions:
        write_tags_page(Path(transcriptions) / "tags.yaml", docs)
    toml = config.read_text(encoding="utf-8")
    toml = re.sub(r"^nav = \[.*?\]$", lambda _: nav_toml(inventory, issues), toml, count=1, flags=re.M)
    toml = re.sub(r'"(assets/[^"?]+\.css)"', lambda m: f'"{m[1]}?v={_digest(config.parent / m[1])}"', toml)
    (out / "zensical.toml").write_text(toml, encoding="utf-8")
    shutil.rmtree(out / "overrides", ignore_errors=True)
    shutil.copytree(config.parent / "overrides", out / "overrides")
    shutil.copytree(config.parent / "assets", docs / "assets", dirs_exist_ok=True)  # incl. fonts
    zensical = Path(sys.executable).with_name("zensical")
    subprocess.run([str(zensical), "build"], cwd=out, check=True)
    return out / "site"
