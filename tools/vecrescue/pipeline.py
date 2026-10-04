"""Pipeline steps. Each reads from SRC (read-only) and writes under OUT."""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from .convert import convert
from .inventory import article_source, merge_wayback, read_index, read_issues
from .legacy import decode, mapped_apl, read_codingprobs
from .pages import (_catalogue, issue_pdfs, nav_toml, wayback_issue_pdfs, write_home_page, write_issue_pages,
                    write_volume_pages)
from . import stubs
from .links import LinkIndex


def run_inventory(src, out, wayback=None):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    records = read_index(src)
    if wayback is not None:
        records = merge_wayback(records, wayback, src)
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


def write_stub_pages(inventory, issues, pdfs, out, transcriptions=None):
    """A page for every indexed article without text (issue #38), linking to
    its first page in the issue PDF, or the article's transcription from
    TRANSCRIPTIONS/art<ID>.md where there is one (issue #40). Offsets and
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
            texts[pdf] = stubs.pdf_pages(pdf)
        return texts[pdf]

    for r in inventory:
        if not r.get("id") or r["id"] in converted:  # what convert wrote, not what is on disk
            continue
        key = alias.get((r.get("volume"), r.get("issue")), (r.get("volume"), r.get("issue")))
        pdf = pdfs.get(key)
        link, match, ocr = None, None, None
        transcription = Path(transcriptions or "") / f"art{r['id']}.md"
        transcription = transcription if transcriptions and transcription.is_file() else None
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
                link = f"{key[0]}/{key[1]}/{pdf.name}#page={n}"
                ocr_key = f"ocr:{check}"
                if not transcription and ocr_key not in entry["checks"]:  # its pages: to the next article, at most 20
                    following = [p for p in starts.get(key, ()) if p > int(r["page"])]
                    last = min(min(following) - 1 if following else 10_000, int(r["page"]) + 19)
                    pp = pages_of(pdf)
                    entry["checks"][ocr_key] = stubs.ocr_block(pp[n - 1:min(len(pp), last + entry["offset"])])
                ocr = entry["checks"].get(ocr_key)
        if transcription:
            stubs.write_transcribed(r, docs, transcription, link)
            review = stubs.read_transcription(transcription)[0].get("review")
        else:
            stubs.write_stub(r, docs, link, ocr if link else None)
            review = None
        results[r["id"]] = {"pdf": link, "match": match, "transcribed": review}
    cache_path.write_text(json.dumps(cache, indent=1, ensure_ascii=False), encoding="utf-8")
    (out / "stubs.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    return results


def run_site(src, out, config, wayback=None, corrections=None, transcriptions=None):
    """Write the home and issue pages, copy the site files from CONFIG's
    folder, and build OUT/docs into OUT/site with Zensical."""
    src, out, config = Path(src), Path(out), Path(config)
    docs = out / "docs"
    inventory, issues = load_inventory(out), read_issues(src)
    if corrections:
        issues = corrections.apply_catalogue(issues)
    more = wayback_issue_pdfs(wayback) if wayback else None
    pdfs = issue_pdfs(issues, src, more)
    write_stub_pages(inventory, issues, pdfs, out, transcriptions)
    write_issue_pages(inventory, issues, src, docs, more)
    write_volume_pages(inventory, issues, docs, pdfs, out / "covers")
    write_home_page(inventory, issues, docs)
    toml = config.read_text(encoding="utf-8")
    toml = re.sub(r"^nav = \[.*?\]$", lambda _: nav_toml(inventory, issues), toml, count=1, flags=re.M)
    (out / "zensical.toml").write_text(toml, encoding="utf-8")
    shutil.rmtree(out / "overrides", ignore_errors=True)
    shutil.copytree(config.parent / "overrides", out / "overrides")
    shutil.copytree(config.parent / "assets", docs / "assets", dirs_exist_ok=True)  # incl. fonts
    zensical = Path(sys.executable).with_name("zensical")
    subprocess.run([str(zensical), "build"], cwd=out, check=True)
    return out / "site"
