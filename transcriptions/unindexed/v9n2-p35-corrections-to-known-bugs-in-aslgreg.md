---
title: Corrections to Known Bugs in ASLGREG (September 1992)
authors:
- Alan Sykes
volume: '9'
issue: '2'
page: '35'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1992.pdf, pages 37–38 (printed 35–36; follows art10007490 and unindexed/v9n2-p34-comments-on-aslgreg-review.md, within The Random Vector); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "Separately headed corrections to ASLGREG by Alan Sykes, following his “Comments on the ASLGREG Review”, within The Random Vector; Jake Ansell’s “Reliability Data Analysis” (p.37) follows."
- "In ΔCHECK [30] the glyph before NAMESΔ is read as ⌿ (a slash with a bar). In MODEL [8] two spaces are printed after “Link Function”."
---

*by Alan Sykes*
{ .byline }

Since its release, five software defects have been discovered in ASLGREG. These may be easily rectified by following the instructions below. (Not necessarily all the defects will be pertinent to your copy, and copies dated September 1992 will incorporate all the changes.)

1\. `YVAR`

The function `YVAR` contained a local variable `'S'`. All references to it (including the header) should be replaced by the variable name `'ΔS'` so that a statement such as

```apl
YVAR 'S'
```

will work as required.

2\. `ORTHOG`

The function `ORTHOG` in its original form is a complete mystery to me! Somehow it got corrupted: fortunately it is short so here is the correct version.

```apl
      ∇A←ORTHOG A;M;K;T;TT
[1]    M←(⍴A)[2]
[2]    K←1
[3]   lp:A[;K]←T←T÷(T+.×T←A[;K])*.5
[4]    A[;K↓⍳M]←TT-T∘.×T+.×TT←A[;K↓⍳M]
[5]    →(M≥K←K+1)/lp
      ∇
```

3\. `MODEL`

In line 8 of `MODEL`, the links variable was originally indexed on `id` and not `il`, amend the line to read as below.

```apl
      ∇R←MODEL
[8]    ⍎(0≠⎕NC 'il')/'R←R,''Link Function  '',links[il;],'' ⋄'''
```

4\. `MUHAT`

The function `MUHAT` did not refer to the offset variable. Amend it as below noting the crucial space within the quotes before the word `'offset'`

```apl
      ∇ΔR←MUHAT
[1]    ⍎(0=⎕NC 'dis')/'START'
[2]    ⍎(inhib)/'ΔR←emess[15;]⋄→0'
[3]    ΔR←⍎'ΔMU',(⍕il),' offset+desmat+.×parest'
      ∇
```

5\. The `CHECK` function

The `CHECK` function contains a superfluous line in the section pertaining to checking whether a variable is a vector or matrix of positive integers. In APL\*PLUS, APL\*PLUS II, Dyalog APL, and APL.68000 this consists of deleting line 29 of `ΔCHECK`, whereas in APL2 it consists of deleting line 62 of `ΔCHECKΔ`. The amended section, with the line deleted is shown below:

```apl
[26] ⍝CHECK VARIABLES ARE POSITIVE INTEGER VARIABLES
[27] four:TΔ←⍎¯1↓,((DΔ,6)⍴'(0=∧/,'),NAMESΔ,((DΔ,2)⍴'=⌊'),NAMESΔ,(DΔ,2)⍴'),'
[28]  TΔ←TΔ∨⍎¯1↓,((DΔ,7)⍴'(1=∨/0≥'),NAMESΔ,(DΔ,2)⍴'),'
[29]  →(1≠IΔ←∨/TΔ)/lp1
[30]  RΔ←RΔ,IΔ/linefd,emess[5;],,TΔ⌿NAMESΔ,' '
[31]  →lp1
```
