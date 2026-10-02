"""Pipeline steps. Each reads from SRC (read-only) and writes under OUT."""

import json
import shutil
from pathlib import Path

from .convert import convert
from .inventory import read_index, xhtml_source
from .links import LinkIndex


def run_inventory(src, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    path = out / "inventory.json"
    path.write_text(json.dumps(read_index(src), indent=1, ensure_ascii=False),
                    encoding="utf-8")
    return path


def load_inventory(out):
    return json.loads((Path(out) / "inventory.json").read_text(encoding="utf-8"))


def run_convert(src, out):
    src, out = Path(src), Path(out)
    docs = out / "docs"
    shutil.rmtree(docs, ignore_errors=True)  # every run starts clean
    docs.mkdir(parents=True)
    written, notes = [], {}
    inventory = load_inventory(out)
    todo = [r for r in inventory if r["id"] and xhtml_source(r)]
    links = LinkIndex.from_inventory(inventory, {r["id"] for r in todo})
    for record in todo:
        folder = docs / f"art{record['id']}"
        folder.mkdir(exist_ok=True)
        markdown, notes[record["id"]], assets = convert(src, record, links)
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


def _issue_key(r):
    def num(s):
        try:
            return float(s)
        except (TypeError, ValueError):
            return float("inf")
    return (num(r.get("volume")), num(r.get("issue")))


def write_home_page(inventory, docs):
    """A plain list of converted articles, by issue. Issue #9 replaces it."""
    docs = Path(docs)
    have = [r for r in inventory if r.get("id") and (docs / f"art{r['id']}" / "index.md").exists()]
    lines = ["# Vector archive (development)", ""]
    current = object()
    for r in sorted(have, key=_issue_key):
        key = (r.get("volume"), r.get("issue"))
        if key != current:
            current = key
            label = f"{key[0]}:{key[1]}" if key[0] else "Online only"
            lines += ["", f"## {label}", ""]
        lines.append(f"- [{r['title']}](art{r['id']}/)")
    path = docs / "index.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run_site(out, config):
    """Copy CONFIG into OUT and build OUT/docs into OUT/site with Zensical."""
    import shutil
    import subprocess
    import sys
    out = Path(out)
    write_home_page(load_inventory(out), out / "docs")
    shutil.copy(config, out / "zensical.toml")
    zensical = Path(sys.executable).with_name("zensical")
    subprocess.run([str(zensical), "build"], cwd=out, check=True)
    return out / "site"
