"""Pipeline steps. Each reads from SRC (read-only) and writes under OUT."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

from .convert import convert
from .inventory import article_source, merge_wayback, read_index, read_issues
from .legacy import decode, mapped_apl, read_codingprobs
from .pages import wayback_issue_pdfs, write_home_page, write_issue_pages
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


def run_site(src, out, config, wayback=None, corrections=None):
    """Write the home and issue pages, copy the site files from CONFIG's
    folder, and build OUT/docs into OUT/site with Zensical."""
    src, out, config = Path(src), Path(out), Path(config)
    docs = out / "docs"
    inventory, issues = load_inventory(out), read_issues(src)
    if corrections:
        issues = corrections.apply_catalogue(issues)
    write_issue_pages(inventory, issues, src, docs, wayback_issue_pdfs(wayback) if wayback else None)
    write_home_page(inventory, issues, docs)
    shutil.copy(config, out / "zensical.toml")
    shutil.rmtree(out / "overrides", ignore_errors=True)
    shutil.copytree(config.parent / "overrides", out / "overrides")
    shutil.copytree(config.parent / "assets", docs / "assets", dirs_exist_ok=True)  # incl. fonts
    zensical = Path(sys.executable).with_name("zensical")
    subprocess.run([str(zensical), "build"], cwd=out, check=True)
    return out / "site"
