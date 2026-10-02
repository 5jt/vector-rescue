"""Command line: vecrescue {inventory,convert,site,all} [--src DIR] [--out DIR]."""

import argparse
from pathlib import Path

from . import pipeline

STEPS = ("inventory", "convert", "site")


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
            print("site:", pipeline.run_site(a.out, a.config))


if __name__ == "__main__":
    main()
