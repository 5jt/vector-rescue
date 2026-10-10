# Plan: converting the PDF-only articles to Markdown

Drafted 2026-10-02. Follows the issue-PDF survey (`surveys/issue-pdf-survey.md`) and the page-per-article work (#38).

## Aim

825 articles exist only in the scanned issue PDFs (vols 1–23; 7,545 pages). Each already has a page linking to its first page in the PDF. The aim is to give each a Markdown text that can be read, searched and linked, without losing faith with the printed page, and to share the reviewing with anyone interested, piecemeal, through the repository.

## What the survey and estimate found

- The PDFs are scans with an OCR text layer. Its prose is readable but about 12% of longer words are damaged, mostly by lost spaces ("takentheliberty"), some by clipped or misread letters ("ultiplying", "1 do think").
- APL does not survive the OCR (`3 20 FTAIL F` became `3°20 FYAIL F`).
- By the share of code-like lines: 290 articles with much code (2,652 pages), 292 with some (3,064), 243 with little or none (1,829). Roughly 70% of the articles, most of the pages, need editorial review because of their code; the other 30% might be excused after a good transcription, with spot checks.

## Method

**Transcribe from the page images, not the OCR text.** Claude reads each page image and writes Markdown in the conventions the converter already uses (front matter, fenced code, figures, tables, raw HTML where Markdown cannot express a structure). The OCR text is a cross-check: words present in it and missing from the transcription are flagged.

**Where transcriptions live.** `transcriptions/art<ID>.md`, committed to the repository: they are authored work, unlike `build/`. Front matter records the source (issue PDF and pages), how it was made, and its review state:

```yaml
transcribed: from page images of VOL.13-NO.2.pdf, pages 36–46 (Claude, 2026-…)
review: draft          # draft → reviewed, by make review (#58)
reviewed_by: Jane Doe  # set by make review
reviewed_on: '2026-10-06'
warning: …             # only if the transcription is doubtful or missing
```

The pipeline treats a transcription as the article's source in place of the PDF link, and the page shows "Transcribed from the printed issue; not yet reviewed" until `review: reviewed`, then "Reviewed by {name} on {date}" from `reviewed_by` and `reviewed_on`.

**Warnings.** A transcription made without confidence carries a `warning:` saying why; the page shows it at the head of the text and the issue index marks the article ⚠. An article that cannot be transcribed at all gets a transcription file with front matter and warning but no text; its page keeps the PDF link and folded OCR, headed by the warning. Both are listed under "Needs editorial attention" in `plans/pdf-review-checklist.md`; a major failure also gets its own issue (#58).

**Figures.** Cropped from the page images into the article's folder; diagrams that are mostly text (tables, boxed displays) transcribed instead.

## Phases

### 1. Pilot (about 30 articles)

Ten articles from each group (much code, some code, little or none), chosen at random within each group, plus any of the checklist's 20 that fall out. For each:

- transcribe from the page images;
- compare with a careful reading of the page (Claude, then Stephen Taylor for a sample), counting errors by kind: prose words, APL characters, code layout, structure (headings, lists, tables), figures;
- time and cost per page.

Decide from the error rates:

- which groups can be excused from review (expected: prose-only articles, if their error rate is very low);
- what reviewers must check in the others (expected: every code block against the page image).

Write up in `surveys/pdf-transcription-pilot.md`.

### 2. Convert at leisure

Transcribe the rest in batches (by volume), each batch a branch and PR, all with `review: draft`. The run report counts transcriptions by review state and lists OCR words missing from each.

### 3. Review, shared and piecemeal

Reviewing happens through GitHub, open to anyone interested:

- **Checklist** (`plans/pdf-review-checklist.md`): one line per article with tick box, links to the transcription, the page on the development site and the PDF page. A reviewer ticks the box and signs the line (`— Name`, optionally `, date`).
- **Corrections**: a reviewer who finds errors edits `transcriptions/art<ID>.md` (GitHub's web editor is enough).
- **`make review`** records each ticked, signed line in the transcription's front matter (`review: reviewed`, `reviewed_by`, `reviewed_on`) and drops its `warning:`; the next build shows the reviewer's name and date on the page (#58).
- #41 (labelled `editorial review`) tracks progress; questions about a particular article go in comments there.

Priority for review: the more interesting articles first (practical how-to and theoretical work); meeting minutes, editorials and news last. Transcription goes volume by volume regardless (decided 2026-10-03): the priority is for spending human effort.

## Decided (Stephen Taylor, 2026-10-02)

- Articles excused from review still carry a "not reviewed" note (caution).
- Reviewers use GitHub only, for now.
- Until an article is transcribed, its page shows the PDF's OCR text folded away (a closed `<details>` section labelled as unedited machine-read text), so site search can find it, imperfectly.

## Decided (Stephen Taylor, 2026-10-03)

- Printed pieces with no index entry are transcribed into `transcriptions/unindexed/` (not published) and listed for editorial review in #44.
- On the pilot's evidence (`surveys/pdf-transcription-pilot.md`): articles with little or no code are excused from review, apart from checking their `queries:`. Articles with some or much code are reviewed, with attention on code that no printed result checks. Excused articles still carry the "not reviewed" note.

## Decided (Stephen Taylor, 2026-10-05)

- So that transcription need not wait on review, Claude opens and merges its own PRs on this repo (a repo-only token). PRs are still raised for the audit trail.
- Review state is held in transcription front matter and shown by the build; `make review` applies the checklist's ticks (#58).
- Doubtful or failed transcriptions carry a warning on their page and a mark in the issue index, and are listed in the checklist. Separate issues only for major transcription failures (the first: #59, XPL).

## Decided (Stephen Taylor, 2026-10-06)

- `index.xml` was compiled by hand: it probably omits pieces then thought not worth keeping, and likely contains errors. **What the scans show has authority** over the index (titles, authors, pages, issue placement). Discrepancies go in the transcription's `queries:`.
- Vol.3 No.4: the wayback PDF is truncated at 1 MiB and cannot be rendered, but its invisible OCR text layer survives for all 140 pages. Its articles get pages showing that recovered text folded away, as for other untranscribed articles; no transcriptions from it. The build recovers it from the truncated capture itself (#81), and so also for the truncated 7:4 and 16:4: 30 articles in all. A whole copy may be in Jake's newer source tree; failing that, Dyalog holds a complete printed series and the issue can be rescanned (#62).

## Decided (Stephen Taylor, 2026-10-06, later)

- **The issue Contents pages are the authority for what an issue holds.** A full index is derived from them (one data file per issue, `transcriptions/contents/`); the volume pages and the Full index page are built from it. Each Contents line links to the best text we have: an article page (indexed or not), else the issue PDF at that page; no link only where nothing survives.
- **`index.xml` is kept as a source of IDs and old URLs**, and its discrepancies with the scans are recorded in queries.
- **First Pass.** `index.xml` reflects the editors’ judgement of what was most worth keeping, so it is used as a filter: the First Pass transcribes the articles in `index.xml`; everything else on a Contents page (front sections: editorials, news, reviews; and unindexed pieces from Volume 5 on) is listed and linked to its PDF page, not transcribed. A Second Pass, if budget allows, picks up the rest. The unindexed pieces already transcribed for Volumes 1–4 are published.
- A **Project status** page, second in the nav, summarises what is done and what remains; updated after each volume.
- **Tags.** Transcribed articles are to be tagged by subject (e.g. language design, programming techniques, system descriptions). A vocabulary is drawn from Volumes 1–4 first, then applied and extended as the First Pass continues.

## Contents pages transcribed ahead of the articles (Stephen Taylor, 2026-10-08; #116)

Every issue with a scan now has its Contents page in `transcriptions/contents/` (100 files: all issues but 2:2, which has no scan; 7:4 and 16:4 from the text recovered from truncated captures). The Full index is built from them: about 2,540 Contents lines against 1,493 dated index records. Every dated index record is linked from a Contents line, except the nine in 2:2.

What the Contents pages showed about `index.xml`:

- **Filed under the wrong issue (4):** Adams 10000010 (5:2, not 5:3); Crossley 10002690 (19:1, not 19:2); and two p.999 records for web versions of articles printed elsewhere (10013650, R.net, printed 20:2; 10013750, Enigma 1368, printed 22:3). Mandelbrot Sets (10001750) is indexed in 7:3 but was held over; it is printed in 7:4 (10001770).
- **Misnamed scan:** `VOL.9-NO.2-OCTOBER-1990.pdf` is Vol.7 No.2 throughout. 7:2 therefore has a scan after all; the pipeline maps it (`pages.MISNAMED`).
- **Pages:** about 30 index pages disagree with the Contents; where checked against the scan, the Contents was right (e.g. 23:4, where three are 3–16 pages out).
- **Duplicates:** 44 records at p.999 (mostly Vols 10–16) are a second record for an article, the one that holds the converted text; each is listed beside its twin on the Contents line.
- **Not on the Contents page:** 173 index entries are pieces within a regular feature (The Education Vector, The Random Vector, Correspondence, Zark Newsletter Extracts, News from Sustaining Members), placed under it.

Each discrepancy is noted on its Contents line (`note:`).

### Index records corrected from the Contents (Stephen Taylor, 2026-10-10; #211)

Decided: the Contents pages are authoritative; the index records are corrected from them without review, and every correction is logged. The inventory step does it, so article pages, stubs, issue tabs, volume pages and the Full index all see the corrected record; `build/report.md` lists every field changed ("Index records corrected": index value → new value, and where from).

- **Page and issue** come from the Contents automatically (`inventory.correct_from_contents`): a line with one record gives it its page and issue; on a line with several, only a p.999 duplicate whose twin is at the line's page is corrected. Lines with no printed page, "not on the Contents page" lines and pages "from the index" correct nothing.
- **Titles and authors** are not taken from the Contents: of about 650 title and 270 author differences on single-record lines, nearly all are abbreviations, short labels for the printed heading, or other forms of a name. Where the index is actually wrong, `records:` in corrections.yaml corrects it, with `why` and `decided`.

First run: 79 records (page 70, issue 5, volume 1, authors 5, title 2). Mandelbrot Sets 10001750, held over from 7:3, is refiled at 7:4 p.110, beside 10001770, the record of the same printed article (as the p.999 twins are). Left as they are: 10008370, one record for two printed pieces (its authors are corrected, but splitting it is a separate decision); the p.999 twins on "not on the Contents page" lines (10012110, 10012400, 10013120, 10013250, 10013480) and 10012490, whose page was inferred from its file name.
