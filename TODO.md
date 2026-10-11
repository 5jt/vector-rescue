# TODO

Expected next steps (updated 2026-10-11).

## PDF-only articles (`plans/pdf-conversion.md`)

- [x] Phase 2, Volumes 1–15: done (status page "after Volume 15").
- [x] Phase 2, Volumes 16–20: done (status page "after Volume 20").
- [x] Phase 2, Volume 21: done (status page "after Volume 21"). 21:4 was transcribed from the text layer of `sources/sjt/Vector/issues/v214.pdf`, as the wayback scan is damaged.
- [ ] In the 16:1 branch, add a query to Sullivan (10009460): the index titles it “…Fibonacci Series”, the printed heading “Sequence”.
- [ ] Add unindexed pieces found along the way to `transcriptions/unindexed/` and to #44.
- [ ] Phase 3: review checklists (`plans/pdf-review-checklist*.md`), ordered by interest; little-code articles need only their queries checked.
- [ ] Report: list OCR words missing from each transcription (planned, not yet built).

## Tags

- [x] Every article with text tagged (#261, #263): transcriptions carry their own tags; the converted pages' tags are in `transcriptions/article-tags.yaml`, applied by the build.
- [x] Converted pages that showed the wrong text (#265): duplicates redirect to their twins; shared sources split; placeholders held; 10012820 refiled to 10:4; two bylines corrected.

## PDF-only articles, Volumes 22–23

- [x] Transcribed the 25 indexed articles of Volumes 22–23 never online (#267: 22:1 #270, 22:2 #272, 22:4 #274, 23:3 #276, 23:4 #279, 23:4.1 #281). 23:4's Contents and PDF now follow the printed issue (issues/v234.pdf is pre-press).
- [ ] Transcribe the placeholders 10009100 (20:4 K day) and 10004730 (12:1 Langlet, A Quite Different New Primitive) (#267).
- [x] PDFs with more than one page offset (#268): 8:1 (two unnumbered order-form pages after p.20), 16:3 (four after p.112), 22:2 (pp.47–50 missing); links now follow each run of pages.

## Index corrections

- [ ] Correct `index.xml` records from the scanned Contents pages (authoritative; decided by Stephen Taylor 2026-10-10: correct without review, log every correction). Discrepancies are noted on the Contents lines in `transcriptions/contents/`.

## Manual transcription

- [ ] 12:1 Adrian Smith, *Native File Functions for Dyalog APL* (10008630, printed pp.137–142): an output content filter blocked automated transcription twice; left as a PDF-linked stub for transcription by hand (#183).
- [ ] 21:2 Paul Cockshott, *Efficient Compilation of Array Expressions* (10002580, printed pp.91–100): blocked by the output content filter twice; left as a stub (#255).

## Awaiting decisions

- [ ] #44: editorial review of the unindexed pieces.
- [ ] Earlier open items: proposed corrections; #34, #35.

## Housekeeping

- [ ] Start sessions from a fresh terminal (or with `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE=1`) so transcripts are saved.
- [ ] Delete `origin/42-folded-ocr` (fully merged).
- [ ] Fix the in-page anchor `#_Toc117273387` in art10013690 (build warning).
