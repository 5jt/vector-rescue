# TODO

Expected next steps (updated 2026-10-10).

## PDF-only articles (`plans/pdf-conversion.md`)

- [x] Phase 2, Volumes 1–15: done (status page "after Volume 15").
- [ ] Phase 2, Volumes 16–21: transcribe the indexed articles not published online, one issue, branch and PR per issue, starting with 16:1. Helpers in `tools/scratch/` (`todo.py v16n1` lists the stubs). 16:4 survives only in a damaged copy. Update the status page at the end of each volume.
- [ ] In the 16:1 branch, add a query to Sullivan (10009460): the index titles it “…Fibonacci Series”, the printed heading “Sequence”.
- [ ] Add unindexed pieces found along the way to `transcriptions/unindexed/` and to #44.
- [ ] Phase 3: review checklists (`plans/pdf-review-checklist*.md`), ordered by interest; little-code articles need only their queries checked.
- [ ] Report: list OCR words missing from each transcription (planned, not yet built).

## Manual transcription

- [ ] 12:1 Adrian Smith, *Native File Functions for Dyalog APL* (10008630, printed pp.137–142): an output content filter blocked automated transcription twice; left as a PDF-linked stub for transcription by hand (#183).

## Awaiting decisions

- [ ] #44: editorial review of the unindexed pieces.
- [ ] Index errors found in the pilot: page ranges, 10008370 (two pieces, garbled authors), 10010060 (wrong page). Correct via `corrections.yaml`?
- [ ] Earlier open items: proposed corrections; the 26:4 month; #34, #35.

## Housekeeping

- [ ] Start sessions from a fresh terminal (or with `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE=1`) so transcripts are saved; once session 8e36916b is no longer needed, its 4.2 GB transcript in `~/.claude/projects/` can be deleted (archived copy verified).

- [ ] Delete `origin/42-folded-ocr` (fully merged).
- [ ] Fix the in-page anchor `#_Toc117273387` in art10013690 (build warning).
