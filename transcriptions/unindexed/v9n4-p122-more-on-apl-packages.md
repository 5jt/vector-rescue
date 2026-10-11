---
title: More on APL Packages
authors:
- A.J. Brown
volume: '9'
issue: '4'
page: '122'
unindexed: true
transcribed: 'from page images of VOL.9-NO.4-APRIL-1993.pdf, page 124 (printed 122; in Technical Correspondence, before art10002790); Claude, 2026-10-11'
review: draft
tags:
- development practice
- programming techniques
queries:
- "A letter in Technical Correspondence, under the section heading on the same page, replying to Nicholas Small’s letter in Vector 9.3 (unindexed/v9n3-p100-apl2-packages.md). The signature block’s postal address is omitted; the firm, Cygnus Enterprises Limited, is kept."
- "The function is for APL*PLUS II. Comment lines [5] and the long string in [4] are printed wrapped onto a second line; kept so. Kept as printed: the stray “h” among the names in [4]; the underscored deltas in “⍙p⍙”."
---

*From: A.J. Brown, 1 February 1993*
{ .byline }

I read with interest the article from Nicholas Small in Vector 9.3 (page 100).

The same problem had occurred to me some time ago, using APL\*PLUS II. My solution was to write the attached utility. The reasons for the name are now lost in the mists of time, but this function is now an integral part of all my workspaces.

```apl
    ∇ ∆ex;∆∆∆A;Z
[1]   ⍝ 921124
[2]    ⎕WINDOW← 0 0 25 80 ⋄ ⎕TCFF
[3]   ⍝ Delete any programs not needed
[4]    ⎕EX '⍙p⍙ ∆unpost ∆find h PROG DISPLAY PACKVR UNPACKVR ORDLOC
        RELABEL STORAGE'
[5]   ⍝ ∆∆ex - matrix containing list of variables NOT to be deleted
        (must contain ∆∆ex)
[6]    Z←⎕EX(~+/∆∆∆A∧.=⍉∆∆ex)⌿∆∆∆A←((1↑⍴∆∆∆A),¯1↑⍴∆∆ex)↑∆∆∆A←⎕NL 2
[7]    ⎕FUNTIE ⎕FNUMS
[8]    0 ⎕INBUF ')SIC'
[9]    ¯1 ⎕INBUF 13
[10]   ¯1 ⎕INBUF ')SAVE'
[11]   ¯1 ⎕INBUF 13
[12]   ¯1 ⎕INBUF 'START'
    ∇
```

*A.J. Brown, Cygnus Enterprises Limited*
