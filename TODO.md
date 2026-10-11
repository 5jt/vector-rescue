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
- [ ] Converted pages that show the wrong text, or none, found while tagging (tagged by title; to check against the index and sources):
    - 10005080 APL+Santa Fe preview (22:2): shows part of the Naples report.
    - 10011390 news from Kx (22:4): shows the Kx meeting report (10011270).
    - 10003550, 10007130 (22:2) and 10011230, 10011240, 10011260 (22:4): each letter shows its whole letters section.
    - 10011440–10011470 (23:1) Kx news items: one shared Sustaining Members' News text.
    - 10013600 Review of Pocket APL (19:2): shows the APL2002 Madrid report (10000300).
    - 10008880 VML (16:4): its source is the Finnish Forests report, `trad/v164/finn164.htm` (10003190).
    - 10009230 and 10013650: the same R.Net article twice.
    - 10009100 BAA Anniversary K day and 10004730 A Quite Different New Primitive: placeholders, no text.
    - 10012820 Abstracts (11:1): shows an APL94 announcement.
    - Bylines to check: 10010800 (Smith's notes on Wheeler's talk), 10007300 (Reiter's review of Peelle's book). Placement to check: 10012110 (indexed 6:2 p.999; cites 5:3).

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
