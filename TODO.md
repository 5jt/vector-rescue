# TODO

Expected next steps (updated 2026-10-10).

## PDF-only articles (`plans/pdf-conversion.md`)

- [x] Phase 2, Volumes 1–15: done (status page "after Volume 15").
- [x] Phase 2, Volumes 16–20: done (status page "after Volume 20").
- [ ] Phase 2, Volume 21: transcribe the indexed articles not published online, one issue, branch and PR per issue, starting with 21:1. Helpers in `tools/scratch/` (`todo.py v16n1` lists the stubs). Update the status page at the end of each volume.
- [ ] In the 16:1 branch, add a query to Sullivan (10009460): the index titles it “…Fibonacci Series”, the printed heading “Sequence”.
- [ ] Add unindexed pieces found along the way to `transcriptions/unindexed/` and to #44.
- [ ] Phase 3: review checklists (`plans/pdf-review-checklist*.md`), ordered by interest; little-code articles need only their queries checked.
- [ ] Report: list OCR words missing from each transcription (planned, not yet built).

## Index corrections

- [ ] Correct `index.xml` records from the scanned Contents pages (authoritative; decided by Stephen Taylor 2026-10-10: correct without review, log every correction). Discrepancies are noted on the Contents lines in `transcriptions/contents/`.

## Manual transcription

- [ ] 12:1 Adrian Smith, *Native File Functions for Dyalog APL* (10008630, printed pp.137–142): an output content filter blocked automated transcription twice; left as a PDF-linked stub for transcription by hand (#183).

## Awaiting decisions

- [ ] #44: editorial review of the unindexed pieces.
- [ ] Earlier open items: proposed corrections; #34, #35.

## Housekeeping

- [ ] Start sessions from a fresh terminal (or with `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE=1`) so transcripts are saved.
- [ ] Delete `origin/42-folded-ocr` (fully merged).
- [ ] Fix the in-page anchor `#_Toc117273387` in art10013690 (build warning).
