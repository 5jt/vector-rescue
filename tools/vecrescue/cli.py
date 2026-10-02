"""Command line: vecrescue {inventory,convert,site,report,all} [--src DIR] [--out DIR]."""

import argparse
from pathlib import Path

from . import pipeline
from .report import run_report

STEPS = ("inventory", "convert", "site", "report")


def fetch_wayback(argv):
    """vecrescue fetch-wayback [--sets …] [--dest DIR]: fetch captures (issue #24)."""
    import json
    import time
    from . import wayback
    p = argparse.ArgumentParser(prog="vecrescue fetch-wayback")
    p.add_argument("--sets", nargs="*",
                   default=["index", "new-articles", "issue-pdfs", "crosscheck"])
    p.add_argument("--dest", type=Path, default=Path("sources/wayback"))
    p.add_argument("--out", type=Path, default=Path("build"))
    a = p.parse_args(argv)
    inventory = json.loads((a.out / "inventory.json").read_text(encoding="utf-8"))
    fetcher = wayback.Fetcher(a.dest)

    def cdx(query):
        time.sleep(fetcher.pause)
        return wayback.cdx_rows(query, get=fetcher._get)

    sets = wayback.plan(inventory, cdx)
    for name in a.sets:
        jobs = sets[name]
        pages = {u: t for u, t in jobs.items() if wayback.re.search(r"/art\d+$", u)}
        n = fetcher.fetch_all(pages, accept=wayback.is_article_page)
        n += fetcher.fetch_all({u: t for u, t in jobs.items() if u not in pages})
        print(f"{name}: {len(jobs)} URLs, {n} fetched now")
    for url, err in fetcher.failed.items():
        print(f"failed: {url}: {err}")


def main(argv=None):
    import sys
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["fetch-wayback"]:
        return fetch_wayback(argv[1:])
    p = argparse.ArgumentParser(prog="vecrescue")
    p.add_argument("step", choices=STEPS + ("all",))
    p.add_argument("--src", type=Path, default=Path("sources/sjt/Vector"))
    p.add_argument("--out", type=Path, default=Path("build"))
    p.add_argument("--config", type=Path, default=Path("site/zensical.toml"))
    p.add_argument("--wayback", type=Path, default=Path("sources/wayback"))
    a = p.parse_args(argv)
    for step in STEPS if a.step == "all" else (a.step,):
        if step == "inventory":
            print("inventory:", pipeline.run_inventory(
                a.src, a.out, a.wayback if a.wayback.is_dir() else None))
        elif step == "convert":
            print("convert:", len(pipeline.run_convert(a.src, a.out)), "articles")
        elif step == "site":
            print("site:", pipeline.run_site(a.src, a.out, a.config))
        elif step == "report":
            t = run_report(a.src, a.out)["totals"]
            print(f"report: {a.out / 'report.md'}: {t['articles']} articles, "
                  f"{t['text_differing_words']} differing words, "
                  f"{t['code_mismatched']} code blocks mismatched, "
                  f"{sum(t['raw_html'].values())} raw-HTML blocks")


if __name__ == "__main__":
    main()
