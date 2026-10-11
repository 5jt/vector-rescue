---
title: Bordering in the Dyalog 8.2 review
authors:
- Eugene McDonnell
volume: '15'
issue: '3'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.15-NO.3-JANUARY-1999.pdf, page 9 (printed 7; within Correspondence, the only letter in the section); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
queries:
- "An untitled letter in Correspondence, From: Eugene McDonnell, Dec 1998; the only letter in the section, followed by a house notice for Vector back numbers. The title is ours. It comments on the Life-game bordering example on p.26 of the review of Dyalog APL/W 8.2 in Vector 15.2."
---

*From: Eugene McDonnell, Dec 1998*
{ .byline }

Your article on Dyalog APL/W 8.2 had an example on p.26 of Vector 15.2. It occurred to me that the bordering could be done in two steps, possibly with a slight saving in time. I wrote them in J and my hunch was right:

```j
f=: 13 : '(3+/\3+/\"1(0,.(0,y.,0),.0))-y.'
g=: 13 : '(3+/\"1(0,.(3+/\0,y.,0),.0))-y.'
```

Functions `f` and `g` give identical results on boolean matrices. The function `f` is the same as your APL expression, where a complete border of zeros surrounds the matrix before any reductions occur. The function `g` puts rows of zeros on top and bottom only, inserts + between the rows, then puts columns of zeros on the left and right of this temporary result, and inserts + between the columns. Timings give `g` a 20% edge over `f` on small matrices such as one encounters in Life games.

A very small point probably not worth worrying about, but when one has learned to program in the 1950s, like me, the habit of looking for any small edge is hard to forsake.
