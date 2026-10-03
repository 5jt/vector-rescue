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
review: draft          # draft → approved (or corrected) by a named reviewer
```

The pipeline treats a transcription as the article's source in place of the PDF link, and the page shows "Transcribed from the printed issue; not yet reviewed" until `review: approved`.

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

- **Checklists** (`plans/pdf-review-checklist*.md`): one line per article with tick box, links to the transcription, the page on the development site and the PDF page. A reviewer ticks the box for an article approved as it is, and opens a PR.
- **Corrections**: a reviewer who finds errors edits `transcriptions/art<ID>.md` in the same PR (GitHub's web editor is enough).
- A merged PR sets `review: approved` (or `corrected`) and the reviewer's name in the article's front matter.
- An issue labelled `editorial review` tracks progress; questions about a particular article go in comments there.

Priority: the more interesting articles first (practical how-to and theoretical work); meeting minutes, editorials and news last.

## Decided (Stephen Taylor, 2026-10-02)

- Articles excused from review still carry a "not reviewed" note (caution).
- Reviewers use GitHub only, for now.
- Until an article is transcribed, its page shows the PDF's OCR text folded away (a closed `<details>` section labelled as unedited machine-read text), so site search can find it, imperfectly.

## Decided (Stephen Taylor, 2026-10-03)

- Printed pieces with no index entry are transcribed into `transcriptions/unindexed/` (not published) and listed for editorial review in #44.
