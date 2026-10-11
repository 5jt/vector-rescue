---
title: From Stephen Jaffe (ExxonMobil Research)
authors:
- Stephen Jaffe
volume: '17'
issue: '2'
page: '25'
unindexed: true
transcribed: 'from page image of VOL.17-NO.2-OCTOBER-2000.pdf, page 27 (printed 25; within Zark Newsletter Extracts, the first item after Jon Sandles’s introduction); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
queries:
- "The first item in the Zark Newsletter Extracts, a solution to the character-matrix search (CMIOTA) set in the previous issue’s Limbering Up column. Jon Sandles’s introduction to the extract, which has no record of its own, is included at the head. It is followed by “Utility Corner: Matrix Searching”, transcribed separately as unindexed/v17n2-p25-utility-corner-matrix-searching.md."
- "The next issue’s “Corrections and Clarifications” (unindexed/v17n3-p27-corrections-and-clarifications.md) says that the code printed here was Carlo Spinicci’s (APL Italiana), hence its APLIT timestamp, and prints Jaffe’s own `CMIOTA`. Title and author are kept as printed."
- "`CMIOTA` was run in Dyalog APL as a check on the transcription: with `-~⎕IO` in [10] and `+\\B` in [11] it returns `2 5 1` for a sample like the Zark one. As printed, [10] reads `--⎕IO` and [11] `(+B)`; the `~` and `\\` were evidently lost in printing. Kept as printed."
- "Kept as printed: the comment “Sort (and grades) the together”; the wrapped comments of [11] and [12]."
---

*Zark Newsletter Extracts, introduced by Jon Sandles*
{ .byline }

Here is another Zark extract. Happily I can report that we have seen some interest in some of the challenges set in this regular feature and we have received excellent entries from Carlo Alberto and Stephen Jaffe. I have not had a chance to investigate how these compare to the Zark entries, but they look pretty good to me. If anyone fancies doing a more formal analysis, then please send it in.

## From Stephen Jaffe (ExxonMobil Research)

In use at Mobil since 1974, modified several times as we migrated from APLSV to APLSF on DEC then to VMSAPL on VAX to APL\*PLUS and finally to Dyalog.

```apl
     ∇ Z←X CMIOTA Y;I;B;C;M;N;L
[1]   ⍝ ⍳ For char matrices  (⎕IO is an implicit argument)
[2]    M←(¯2↑1 1,⍴X)⍴X ⋄ N←(¯2↑1 1,⍴Y)⍴Y   ⍝ Let arguments to be matrices
[3]    C←¯1↑(⍴M)⌈⍴N
[4]    N←(⌽C,1↑⍴N)↑N ⋄ M←(⌽C,1↑⍴M)↑M       ⍝ ... with the same no of cols
[5]    M←M⍪' '                             ⍝ Add row for "not found" case
[6]    Z←⍋I←⍋N⍪M                           ⍝ Sort (and grades) the together
[7]   ⍝ Z←⍋I←⎕AV⍋N⍪M      ⍝ Use this if APL version requires a collating seq.
[8]   ⍝ Z←⍋I←⍋⎕AV⍳N⍪M     ⍝ ... or this if it doesn't allow char grade (VSAPL)
[9]    B←I>1↑⍴N                            ⍝ Select the items ∊ M
[10]   L←(1↑⍴M)--⎕IO                       ⍝ Result if not found
[11]   Z←((B/I-1↑⍴N),L)[⎕IO+(+B)[(1↑⍴N)↑Z]]   ⍝ See each item of N after
                                             which item of M was gone
[12]   Z←L⌊Z+L×∨/M[Z;]≠N                   ⍝ If they are equal this is
                                           the result, if not give L
[13]  ⍝∘ (c)APLIT A FUB spi 13/09/1996 18:12             10363 D95
     ∇
```
