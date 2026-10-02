# Master plan: Vector Rescue

Goal: recover the entire *Vector* archive and republish it, with every old `art` URL (e.g. `/art10500650`) resolving.

Revised 2026-10-02 after the filetree surveys (`filetree-survey-claude.md`, `filetree-survey-codex.md`) and decisions by Stephen Taylor.

## Principles

- Old URLs are the top priority; every design choice is judged against them.
- Never modify originals. `sources/` is read-only; all work is on derived copies.
- Record provenance for every article: which source it came from, and any conversion applied.
- Overlaps between sources are decided by examining diffs, possibly article by article.
- Do not publish private data: the request logs (`events*.log`, `icons/events.log`), `members/`, editorial `edit/`, `held/`, `rejected/` material, `info.php`, sandbox and tools.
- Start with what is cheap and safe, then widen: UTF-8 content first, other encodings later.

## What we know (from the surveys)

- The PHP tree has 1,485 index records (1,484 IDs). 616 have HTML/XHTML text on disk; 838 are metadata only. The tree's text is complete for volumes 24–26 and thin before volume 15.
- It ends with Vol. 26 Nos. 2&3 (printed, 2014) and an online article of 22 Jan 2016. The WordPress export has to supply the later years up to 2022.
- 443 of the 606 indexed text files are valid UTF-8; 163 are not. APL in older articles is often font-mapped (APL2741, APL385), which byte conversion alone cannot fix.
- The rule that mapped `/artNNN` to `index.php?id=NNN` is not in the tree. It is inferable, and in a static site we don't need it.
- Articles carry rich metadata in `index.xml` (title, authors, volume, issue, page, received and online dates, blurb).

## Blocking issues

| # | Blocker | Blocks | Owner / action |
|---|---|---|---|
| B1 | **A copy of the WordPress database export** | All articles after the PHP site's end (2014–2022), and the old-versus-WP duplicate comparison | Await Paul Grosvenor's reply; ask Jake Jacob as a second route. |
| B2 | **Use of the `archive.vector.org.uk` URL** (DNS control; today it points at WordPress) | Publishing under the original hostname | BAA (Paul). Not needed for the first publication; see Phase 5. |

Neither blocks Phases 0–4 on the existing PHP-era content.

## Phase 0: Retrieve sources: done for the PHP tree; WordPress export outstanding

- PHP filetree: recovered into `sources/sjt/Vector` (338 MB, excluded from git until a safe public home exists; see below).
- Still wanted (B1): WP database export. Also useful: Wayback Machine captures of `archive.vector.org.uk` and `vector.org.uk`, to recover the lost rewrite rule and check how pages looked.
- Decide soon where `sources/sjt` is archived safely and publicly (Dyalog Gitea, a GitHub release or a data repo). **Before publishing it, exclude the logs and `members/`.**

## Phase 1: Survey: done for the filetree

Deliverables so far: the two filetree surveys. Remaining survey work is folded into Phases 2 and 3.

## Phase 2: Early technical groundwork

2a. **Canonical inventory.** Extract `index.xml` into a table (CSV or JSON): ID, title, authors, volume, issue, page, dates, source paths and formats, whether the file exists, whether it is valid UTF-8. Add the 1,484 IDs as the *required* `art` URL list. Handle the empty-ID record (`content/printed/244/peelle.htm`), the alias paths and the combined issues. See `plans/xhtml-target-survey.md` for the detailed first task below.

2b. **Survey the hand-coded XHTML to define the Markdown target** (an early, critical step; see `plans/xhtml-target-survey.md`). Standard Markdown and GitHub-flavoured Markdown cannot be assumed to represent it. Find out which structures occur, how often, and how each should be represented.

2c. **Choose the renderer.** Evaluate Zensical against the target from 2b. Zensical is from the Material for MkDocs team, is the tool Dyalog uses, is configured by `zensical.toml`, and uses Python Markdown with Material-style extensions **(from its documentation; to be confirmed by trial)**. Questions to settle by experiment:
   - Can it emit a page at exactly `/art10500650` (a directory with `index.html`, or a flat file)? Can the URL scheme be controlled per page?
   - Can it handle ~1,500 pages quickly, and carry per-article metadata (authors, volume, issue)?
   - Does it allow raw HTML or Markdown-in-HTML for the structures Markdown can't express?
   - How does it handle APL (fonts, `<code>`) and mathematics (MathML or KaTeX; some articles contain mathematical XHTML fragments)?
   - Alternative candidates if Zensical falls short: MkDocs Material (the same lineage, mature), Eleventy, Hugo, a small custom Python generator.

2d. **Fix the encoding strategy.** Start with the 443 valid-UTF-8 files. Study the 163 others separately in Phase 6.

## Phase 3: First slice: valid UTF-8 content already in the PHP tree

Scope: indexed articles whose source is valid UTF-8 (XHTML first, then UTF-8 `trad/` HTML).

- Convert each to the target Markdown, with front-matter metadata and provenance. Keep the original `vec:source` path and the conversion applied.
- Check output against the originals (text equality, links, images, counts of structures), with sampled visual comparison.
- Copy images and assets across; list the missing ones.
- Pilot first on a few issues (suggest 25:1, which contains `art10500650`), then widen to volumes 24–26, then the other UTF-8 files.

## Phase 4: Generate the site and publish on GitHub Pages

- Build with the renderer chosen in 2c.
- **Publish rescued content on GitHub Pages first**, under the Pages hostname. Defer the `archive.vector.org.uk` question (B2) until we have use of the URL.
- URL design: see "Old URLs on GitHub Pages" below.
- Add issue and volume indexes, author pages if cheap, search, and an explicit statement of what is missing.

### Old URLs on GitHub Pages

Static hosting has two limits to plan around:

1. **Extensionless paths.** `/art10500650` can be served from `art10500650/index.html`, but GitHub Pages will redirect it to `/art10500650/`. Alternatively a flat file named `art10500650` (no extension) could be served, but the content type is then uncertain. Test both. If a trailing slash is the best we can do, that must be accepted or the hosting reconsidered.
2. **Query-string URLs** (`?vol=&no=&art=`, the old `redirector.php` scheme) cannot be handled by Pages. A small client-side script on the home page could map them to `/art<ID>` using a generated lookup table.

Also needed: stub redirects for any IDs that map to external (HTTP-only) sources, and a page for each metadata-only record explaining that the article is not online.

On a project site the base path is `/vec-rescue/…`, not `/`; true root-relative URLs require a custom domain or a user/organisation site. This is another reason B2 matters later.

## Phase 5: Hosting and domain, after B2

When the `archive.vector.org.uk` URL becomes available, re-examine hosting:

- GitHub Pages with a custom domain (DNS CNAME), if the trailing-slash behaviour is acceptable.
- Dyalog's Gitea, if it can serve static output.
- HTTPD on dyalog.com, which gives full control of rewrites and redirects and is the fallback if Pages cannot honour the `art` URLs exactly.
- Also cover `vector.org.uk/art…` and `vector.johnbutlerassociates.co.uk/art…`, which need redirects at those hosts.

## Phase 6: Widen the content

- **WordPress content (needs B1):** import 2014–2022 articles; compare old-versus-WP duplicates by diff and rule on each, article by article.
- **Other encodings:** the 163 non-UTF-8 files. First Windows-1252, which `lib/present.php` assumed; then APL font-mapped text (APL2741, APL385, `tools/codingprobs.txt` has notes) with human review of the mapping.
- **Word documents:** the five `.doc` files (one is really HTML) and any further Word issues supplied by Paul or Jake; Ian Clark's converted versions if they can be found.
- **Unindexed and metadata-only material:** review the unindexed candidate files; find PDFs or other sources for the 838 metadata-only records, especially volumes 1–9 (no online text) and the issues that exist only in print.
- **Assets:** convert `.wmz` images, repair or replace images with wrong formats, fix case-mismatched image directories.

## Phase 7: Verify and hand over

- Test every required `art` URL, plus the URLs seen in `events.log` and in the README.
- Document how to rebuild the site and how to add future material.
- Agree long-term ownership with the BAA, and where the source archive lives.

## Open questions

- Which hosting option in the end? (Phase 5, after B2.)
- Who controls the vector.org.uk DNS and the WordPress site?
- Licensing and author permissions for republication.
- Where should `sources/sjt` live safely, and what should be stripped before it goes public?
- Can Zensical give us `/art<ID>` URLs with at most a trailing slash? (Phase 2c.)
