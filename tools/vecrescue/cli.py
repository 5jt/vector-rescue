"""Command line: vecrescue {inventory,convert,site,report,all} [--src DIR] [--out DIR];
vecrescue fetch-wayback; vecrescue fetch-php; vecrescue review."""

import argparse
from pathlib import Path

from . import pipeline
from .report import run_report

STEPS = ("inventory", "convert", "site", "report")


def fetch_php(argv):
    """vecrescue fetch-php [--renderings | --check] [--dest DIR]: fetch from the restored
    PHP site what our tree lacks (issue #104)."""
    from . import phpsite
    p = argparse.ArgumentParser(prog="vecrescue fetch-php")
    p.add_argument("--dest", type=Path, default=Path("sources/php-site"))
    p.add_argument("--src", type=Path, default=Path("sources/sjt/Vector"))
    p.add_argument("--renderings", action="store_true", help="also fetch the site's article pages")
    p.add_argument("--check", action="store_true",
                   help="only compare the fetched article pages with build/site (to build/php-check.json)")
    a = p.parse_args(argv)
    if a.check:
        import json
        stubs = json.loads(Path("build/stubs.json").read_text(encoding="utf-8"))
        out = phpsite.compare(a.dest / "rendered", Path("build/site"), stubs)
        Path("build/php-check.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
        ok = out["results"].values()
        print(f"php-check: {len(ok)} compared, {sum(v['captured_words'] for v in ok)} words, "
              f"{sum(v['differing'] for v in ok)} differing; {out['kinds']}")
        return
    fetcher = phpsite.Fetcher(a.dest)
    got = fetcher.sources(a.src)
    print(f"fetch-php: {len(got)} sources")
    if a.renderings:
        print(f"fetch-php: {len(fetcher.renderings())} article pages")
    for rel, err in fetcher.failed.items():
        print(f"  failed: {rel}: {err}")


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
        pdfs = {u: t for u, t in jobs.items() if u.lower().endswith(".pdf")}
        n = fetcher.fetch_all(pages, accept=wayback.is_article_page)
        n += fetcher.fetch_all(pdfs, accept=wayback.is_complete_pdf)
        n += fetcher.fetch_all({u: t for u, t in jobs.items() if u not in pages and u not in pdfs})
        print(f"{name}: {len(jobs)} URLs, {n} fetched now")
    for url, err in fetcher.failed.items():
        print(f"failed: {url}: {err}")


def review(argv):
    """vecrescue review [--checklist FILE] [--transcriptions DIR]: record the
    reviews ticked in the checklist in the transcriptions' front matter (#58)."""
    from . import review as rv
    p = argparse.ArgumentParser(prog="vecrescue review")
    p.add_argument("--checklist", type=Path, default=Path("plans/pdf-review-checklist.md"))
    p.add_argument("--transcriptions", type=Path, default=Path("transcriptions"))
    a = p.parse_args(argv)
    results = rv.apply(a.checklist, a.transcriptions)
    for path, outcome in results:
        if outcome != "already reviewed":
            print(f"{path}: {outcome}")
    n = sum(outcome == "reviewed" for _, outcome in results)
    print(f"review: {n} newly reviewed, {len(results)} ticked in {a.checklist}")


def main(argv=None):
    import sys
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["fetch-wayback"]:
        return fetch_wayback(argv[1:])
    if argv[:1] == ["fetch-php"]:
        return fetch_php(argv[1:])
    if argv[:1] == ["review"]:
        return review(argv[1:])
    p = argparse.ArgumentParser(prog="vecrescue")
    p.add_argument("step", choices=STEPS + ("all",))
    p.add_argument("--src", type=Path, default=Path("sources/sjt/Vector"))
    p.add_argument("--out", type=Path, default=Path("build"))
    p.add_argument("--config", type=Path, default=Path("site/zensical.toml"))
    p.add_argument("--wayback", type=Path, default=Path("sources/wayback"))
    p.add_argument("--php", type=Path, default=Path("sources/php-site"), help="the restored PHP site (#113)")
    p.add_argument("--corrections", type=Path, default=Path("corrections.yaml"))
    p.add_argument("--transcriptions", type=Path, default=Path("transcriptions"))
    a = p.parse_args(argv)
    from .corrections import Corrections
    corrections = Corrections.load(a.corrections)
    php = a.php if a.php.is_dir() else None
    for step in STEPS if a.step == "all" else (a.step,):
        if step == "inventory":
            print("inventory:", pipeline.run_inventory(
                a.src, a.out, a.wayback if a.wayback.is_dir() else None, php))
        elif step == "convert":
            print("convert:", len(pipeline.run_convert(a.src, a.out, corrections)), "articles")
        elif step == "site":
            print("site:", pipeline.run_site(a.src, a.out, a.config, a.wayback if a.wayback.is_dir() else None, corrections,
                                              a.transcriptions if a.transcriptions.is_dir() else None, php))
        elif step == "report":
            t = run_report(a.src, a.out, corrections)["totals"]
            print(f"report: {a.out / 'report.md'}: {t['articles']} articles, "
                  f"{t['text_differing_words']} differing words, "
                  f"{t['code_mismatched']} code blocks mismatched, "
                  f"{sum(t['raw_html'].values())} raw-HTML blocks")


if __name__ == "__main__":
    main()
