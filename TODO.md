# TODO

Expected next steps (updated 2026-11-27).

## PDF-only articles (`plans/pdf-conversion.md`)

- [x] Phase 2, Volumes 1–15: done (status page "after Volume 15").
- [x] Phase 2, Volumes 16–20: done (status page "after Volume 20").
- [x] Phase 2, Volume 21: done (status page "after Volume 21"). 21:4 was transcribed from the text layer of `sources/sjt/Vector/issues/v214.pdf`, as the wayback scan is damaged.
- [x] Sullivan (10009460): query on Series/Sequence in place.
- [x] Unindexed pieces found along the way: superseded by the Second Pass (below); #44 closed.
- [ ] Phase 3: review checklists (`plans/pdf-review-checklist*.md`), ordered by interest; little-code articles need only their queries checked.
- [x] Report: OCR words missing from each transcription (build/report.md, last section); 63 flagged.
- [x] Triaged the 63 flagged (2026-10-11): no omitted passages; misses come from neighbouring articles on shared pages, figures and listings kept as images, and deliberate omissions under queries. Fixed: two wrong page ranges (10004320, 10010900), one missing byline (10006380). XPL (10001020) is the abandoned transcription.
## Second Pass (decided 2026-10-11, #44: unindexed pieces are worth indexing and republishing)

- [x] Pieces left out by the First Pass and noted in its queries: 26 transcribed into `transcriptions/unindexed/` and put on their issues' Contents files; three earlier pieces linked (#297).
- [x] Swept Volumes 5–21 for further unindexed pieces (#299): 226 added to the Contents files, linked to the scan, not yet transcribed. 74 finds left out (section editorials, which are their Contents line's own text; pieces already inside a held transcription; house notices, captions, parts of reports): listed in #299. Not swept: 7:4, 16:4 and 21:4 (damaged scans; 21:4 was transcribed from another copy).
- [x] Transcribed the sweep's pieces (#301): 210 files in `transcriptions/unindexed/`. 16 Contents lines removed, as their text is already published inside an indexed transcription (13:4, 14:1, 14:4, 15:2, 19:2, 7:2, 8:2).
- [ ] 12:2 p.113, “Microsoft Announces APL for the 8088 – almost 20 years late!” (Adrian Smith): blocked by the output content filter (long quotations from the book *Gates*); left linked to the scan, for transcription by hand.
- [x] The remaining Contents lines (#305; plan, conventions and brief in `plans/second-pass.md`): 650 pieces in seven waves (#306–#311 and wave 7), Volumes 1–25, and 11:1 APL94 Abstracts (missed by the First Pass). Contact details of individuals omitted throughout (rules of 2026-10-12). Status page updated.
- [x] The printed pieces with no Contents line noticed during #305 (#314): 47 transcribed, mostly section introductions; flyers, a form and an advertisement left out (`plans/second-pass.md`).

## Complete scans of 3:4, 7:4 and 16:4 (#321)

- [x] Found on vector.org.uk (#316); in `sources/wordpress/`; the build prefers them to the truncated captures. Their 31 indexed articles link to the scan, with its OCR.
- [x] Checked the three Contents files against the complete scans (2026-11-22): missing page numbers added; 3:4 regains two authors' rightful items (APL88 is Neville Holmes's, the society news David Preedy's) and its APL 86 heading; 7:4's title *Thoughts on J←f g h* restored. Found in passing: 7:4's Random Vector has its own contents (p.33), including David Appleton's *Sterling's Function* (p.47), not in the index: for the Second Pass sweep.
- [ ] First Pass: transcribe the 31 indexed articles.
- [ ] Second Pass: the unindexed pieces of the three issues (never swept).

## WordPress content (Phase 8, #316)

- [x] Catalogue: `surveys/wordpress-survey.md`. IDs from 10501780 by post date. BAA 2016 talks page drafted (`transcriptions/art10501780.md`).
- [x] The build adds a record for each transcription marked `added:` (#323); the talks page is published.
- [x] Converted the 11 new articles (`transcriptions/art10501790.md`–`art10501890.md`), images from vector.org.uk; published.
- [ ] Awaiting Jake's reply (asked 2026-11-20): `wp-content/uploads` for the lost Langlet figure 1 (10501810, `2019/04/figure1.png`; Stephen may also track it down); the source of Dan Baronet's *Finding text in files* (10501800) for the lost `]find` markers (not in the 1984–2016 material nor Dyalog's 12.1/13.0 User Commands guides; an old Dyalog running the examples would show them); scans of 2:2 and 7:2 (#62). Apply what he sends.
- [x] Bodon's pivot-with-totals figure (10501860) restored from KDnuggets, the article's first publication (#343). *Fun Q* reviewer confirmed as Daniel Krizian (Stephen, 2026-11-26).
- [x] *The Derivative Revisited* (WordPress draft 2075): excluded, as another author's work published elsewhere, not in *Vector* (Stephen, 2026-11-27). No message to Richard Park needed.
- [x] The WordPress scripts are kept in `tools/scratch/wordpress/` (#326, PR #327; sequence in `tools/scratch/README.md`).
- [x] Compared the 12 low-scoring duplicate posts (#328): no revisions, the held texts stand; the low scores were a fault in the scoring. 10501740–10501760 need no better source.
- [x] Volume 27 on the home page (#331): 27:1, never printed, with its 15 pieces (WordPress's 27:1 category plus the PHP site's `printed/271/`) in order of publication online; the 2016 talks page refiled as published online.
- [x] Lead images for the never-printed pieces and bylines for the WordPress articles (#333).
- [x] Authors' email addresses in 101 bylines of pages converted from the old site: retained as published (Stephen Taylor, 2026-11-22).
- [x] Pushed `main` to `official` (VecEd/VectorArchive), 2026-11-22; keep it in step after each merge.
- [x] Volume 27 tab shows online dates (#339); the header logo is the BAA logogram as SVG (#338); site title “Vector archive”. Favicon stays the blue V (Stephen, 2026-11-22).
- [ ] Look into the missing author of *Dyalog '16 – an insider's view* (10501750).

## CI/CD to GitHub Pages (begun 2026-11-22)

Agreed scope: CI runs only the Zensical build (plus `lift_bylines`) from the Markdown tree the pipeline writes locally (`build/docs`, `zensical.toml`, `overrides/`), and deploys to GitHub Pages. `sources/` stay off GitHub.

Measured 2026-11-22: input 749 MB (PDFs and images are most of it), built site 857 MB (881 MB as a tar; PDFs 510 MB, search.json 29 MB, duplicate files only 18 MB). Zensical build 34 s, 850 MB RAM. Pages limits: site ≤ 1 GB, deploy ≤ 10 min. So CI can handle it, with ~140 MB headroom.

- [x] Where: `official` (VecEd/VectorArchive) gets the Markdown tree and the scan PDFs, with an Actions workflow to Pages; later it becomes the single source of truth and vec-rescue is archived (Stephen, 2026-11-26). Until the handover `official` is generated output: never edit by hand.
- [x] Deploy limits: the existing gh-pages deploy of the full 857 MB site (GitHub's own Pages workflow) takes about 90 s, of which deploy 31 s (run 45059054714). No trial needed.
- [x] `official`'s `main` replaced by the Markdown tree, the PDFs, the workflow and a README (2026-11-26, #341, PR #342; commit 70c038c). From now on: `make all`, then `make official`.
- [x] Live at https://britapl.github.io/VectorArchive/ (2026-11-27): BritAPL/VectorArchive public, Pages from GitHub Actions, Publish runs on every push (PR #348; first run 45982930806: build 1m40s, deploy 30s). Publish with `make all`, then `make official`.
- [ ] Jake to delete or archive VecEd/VectorArchive.
- [ ] Decide whether to keep the 5jt.github.io preview (`make publish`); point the site's #62 links (5jt/vector-rescue) somewhere lasting before vector-rescue is archived.
- [ ] Once live: decide whether `make publish` (5jt.github.io preview) is still wanted; issue links in the site still point to 5jt/vector-rescue (#62).
- [ ] Before the handover: a README for `official` on what it is and how to edit and publish it, including the pages that become hand-kept (volume tabs, full index, tags, home, nav).
- [x] `lift_bylines` runs on its own (`tools/vecrescue/bylines.py`, copied to official as `scripts/lift_bylines.py`); `make official` writes, commits and pushes the tree.

## Metadata

- [ ] Publish a machine-readable full index, `vector-index.json`, written by the build (#303). It also settles the index-corrections item below, as `index.xml` cannot be corrected in place.
- [ ] When the site goes public: Highwire `citation_*` tags on article pages, for Google Scholar and Zotero (#302). No Dublin Core on pages.

## Tags

- [x] Every article with text tagged (#261, #263): transcriptions carry their own tags; the converted pages' tags are in `transcriptions/article-tags.yaml`, applied by the build.
- [x] Converted pages that showed the wrong text (#265): duplicates redirect to their twins; shared sources split; placeholders held; 10012820 refiled to 10:4; two bylines corrected.

## PDF-only articles, Volumes 22–23

- [x] Transcribed the 25 indexed articles of Volumes 22–23 never online (#267: 22:1 #270, 22:2 #272, 22:4 #274, 23:3 #276, 23:4 #279, 23:4.1 #281). 23:4's Contents and PDF now follow the printed issue (issues/v234.pdf is pre-press).
- [x] Transcribed the placeholders 10009100 (20:4 K day) and 10004730 (12:1 Langlet, A Quite Different New Primitive) (#292).
- [x] PDFs with more than one page offset (#268): 8:1 (two unnumbered order-form pages after p.20), 16:3 (four after p.112), 22:2 (pp.47–50 missing); links now follow each run of pages.

## Index corrections

- [ ] Correct `index.xml` records from the scanned Contents pages (authoritative; decided by Stephen Taylor 2026-10-10: correct without review, log every correction). Discrepancies are noted on the Contents lines in `transcriptions/contents/`.

## Manual transcription

- [ ] 12:1 Adrian Smith, *Native File Functions for Dyalog APL* (10008630, printed pp.137–142): an output content filter blocked automated transcription twice; left as a PDF-linked stub for transcription by hand (#183).
- [ ] 21:2 Paul Cockshott, *Efficient Compilation of Array Expressions* (10002580, printed pp.91–100): blocked by the output content filter twice; left as a stub (#255).

## Awaiting decisions

- [x] #44: closed 2026-10-12 (the Second Pass republished the unindexed pieces).
- [ ] Earlier open items: proposed corrections; #34, #35.

## Housekeeping

- [ ] Start sessions from a fresh terminal (or with `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE=1`) so transcripts are saved.
- [x] Deleted `origin/42-folded-ocr` (fully merged).
- [x] Fixed the in-page anchor `#_Toc117273387` in art10013690; the build has no warnings. Two corrections that a duplicated key had silently disabled (10014110, 10003430) now apply; a test forbids duplicate keys.
