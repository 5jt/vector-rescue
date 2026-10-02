"""Command line: vecrescue {inventory,convert,site,report,all} [--src DIR] [--out DIR]."""

import argparse
from pathlib import Path

from . import pipeline
from .report import run_report

STEPS = ("inventory", "convert", "site", "report")


def main(argv=None):
    p = argparse.ArgumentParser(prog="vecrescue")
    p.add_argument("step", choices=STEPS + ("all",))
    p.add_argument("--src", type=Path, default=Path("sources/sjt/Vector"))
    p.add_argument("--out", type=Path, default=Path("build"))
    p.add_argument("--config", type=Path, default=Path("site/zensical.toml"))
    a = p.parse_args(argv)
    for step in STEPS if a.step == "all" else (a.step,):
        if step == "inventory":
            print("inventory:", pipeline.run_inventory(a.src, a.out))
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
