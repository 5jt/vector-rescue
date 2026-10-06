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
