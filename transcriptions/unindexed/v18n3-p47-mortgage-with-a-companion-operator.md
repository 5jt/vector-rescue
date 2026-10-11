---
title: MORTGAGE with a companion operator
authors:
- Gianluigi Quario
volume: '18'
issue: '3'
page: '47'
unindexed: true
transcribed: 'from page images of VOL.18-NO.3-JANUARY-2002.pdf, pages 49–50 (printed 47–48; within The Education Vector, the second letter under the Letters heading); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- language design
queries:
- "The second letter under the Letters heading, untitled in print; the title is ours. It answers the Limbering Up task “Polyadic Functions” in 18:1 (unindexed/v18n1-p37-limbering-up-polyadic-functions.md), after Claude Henriod’s letter (unindexed/v18n3-p46-polyadic-mortgage-as-an-apl2-operator.md)."
- "`MORTGAGE`, `ofAmount` and `myMORTGAGE` were run in Dyalog APL as a check on the transcription; `myMORTGAGE` gives the three printed shapes. In `accordingly` [23] the first glyph is faint and could be read as a minus; it is read as `~`, which the guard needs. The underbarred epsilon in [23] is read as `⍷` (find)."
- "In `myMORTGAGE` lines [4] to [9] are elided in print by “...”; kept so."
- "Kept as printed: “I’m not sure having understood your trial”; interest rates written as `0.9` and `0.85`; the unused local `xFN` in `ofAmount`."
---

*From: Gianluigi Quario*
{ .byline }

I’m not sure having understood your trial. Anyway I prepared 2 functions.

1) `MORTGAGE` is a dyadic function; the operator `ofAmount` allows a kind of third argument

```apl
0.9 MORTGAGE 30
0.9 (MORTGAGE ofAmount 900000 1000000) 30
```

2) `myMORTGAGE` is a dyadic function with 3 arguments (the right one is a nested array). May I consider it like a polyadic function? Please note:

```apl
  3 2   ↔ ⍴90000 100000 200000        myMORTGAGE (0.9 0.85 0.8) (20 30)
4 2 3   ↔ ⍴90000 100000 200000 500000 myMORTGAGE (0.9 0.85)     (20 25 30)
4 2 2 3 ↔ ⍴90000 100000 200000 500000 myMORTGAGE (2 2⍴0.9 0.85) (20 25 30)
```

```apl
     ∇ Z←LO(FN ofAmount arg)RO;xFN;PRIN
[1]   ⍝  companion operator of dyadic function MORTGAGE
[2]    PRIN←arg
[3]    Z←LO FN RO
[4]   ⍝ Gianluigi Quario 2001 10 18
     ∇

     ∇ PMT←INT MORTGAGE TERM;V
[1]   ⍝ mortgage for 1 unit of amount borrowed
[2]   ⍝ if global variable PRIN found, PRIN is amount borrowed
[3]   ⍝ INT ↔nom. annual interest rate   TERM↔number of years of loan
[4]   ⍝ PMT ↔monthly payment
[5]   ⍝ PRIN↔principal(amount borrowed) can be GLOBAL
[6]
[7]   ⍝ try: 0.9 MORTGAGE 30
[8]   ⍝      0.9 (MORTGAGE ofAmount 900000 1000000) 30
[9]   ⍝Polyadic Functions
[10]
[11]   :If 2≠⎕NC'PRIN' ⋄ ⎕SHADOW'PRIN' ⋄ PRIN←1 ⋄ :End
[12]
[13]   V←÷1+INT÷12                              ⍝Monthly discount rate
[14]   PMT←PRIN÷(V-V*1+12×TERM)÷1-V
[15]  ⍝ Gianluigi Quario 2001 10 18
     ∇

     ∇ PMT←X myMORTGAGE Y;V;INT;TERM;PRIN;Xminus;Xdivide;Xpower;accordingly
[1]   ⍝ triadic function: one left arg (PRIN) + two right args (INT TERM)
[2]   ⍝ PRIN ↔principal   INT↔nom. annual interest rate   TERM↔years
[3]   ⍝ the args can have different ranks and dimensions
...
[10]   PRIN←X
[11]   INT TERM←2↑Y                             ⍝ function is triadic
[12]
[13]   accordingly←{
[14]      ⍝ operator for dyadic scalar functions :
[15]      ⍝   try to preserve "scalar behaviour" by "stretching"
[16]      ⍝   the minor rank operand;
[17]      ⍝   if not possible, outer product of operands is performed)
[18]      ⍝ if args have same rank and dimensions,  normal scalar behaviour
[19]      ⍝ elseif args have a common dim, arg with minor rank is stretched
[20]      ⍝ else,                                   outer product.
[21]
[22]       ((,1)≡⍴,⍺)∨((,1)≡⍴,⍵)∨(⍴⍺)≡⍴⍵:⍺ ⍺⍺ ⍵      ⍝normal scalar behaviour
[23]       ~∨/(a←(⍴⍺)⍷⍴⍵),b←(⍴⍵)⍷⍴⍺:⍺∘.⍺⍺ ⍵        ⍝outer product
[24]       AxesWithCommonDimension←((-⎕IO)+(((∨/a)/a),(∨/b)/b)⍳1)+⍳(⍴a)⌊⍴b
[25]       ⍺ ⍺⍺[AxesWithCommonDimension]⍵         ⍝minor rank arg is stretched
[26]   }
[27]   Xminus←-accordingly
[28]   Xdivide←÷accordingly
[29]   Xpower←*accordingly
[30]
[31]   V←÷1+INT÷12                              ⍝Monthly discount rate
[32]   PMT←PRIN Xdivide(V Xminus V Xpower 1+12×TERM)Xdivide 1-V
[33]  ⍝ Gianluigi Quario 2001 10 18
     ∇
```
