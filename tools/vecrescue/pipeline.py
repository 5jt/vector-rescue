"""Pipeline steps. Each reads from SRC (read-only) and writes under OUT."""

import json
from pathlib import Path

from .convert import convert_article
from .inventory import read_index, xhtml_source


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
    docs.mkdir(parents=True, exist_ok=True)
    written = []
    for record in load_inventory(out):
        if record["id"] and xhtml_source(record):
            path = docs / f"art{record['id']}.md"
            path.write_text(convert_article(src, record), encoding="utf-8")
            written.append(path)
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
    have = [r for r in inventory if r.get("id") and (docs / f"art{r['id']}.md").exists()]
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
