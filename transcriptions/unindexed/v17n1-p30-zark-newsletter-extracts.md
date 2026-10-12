---
title: Zark Newsletter Extracts
authors:
- Jon Sandles
volume: '17'
issue: '1'
page: '30'
unindexed: true
transcribed: 'from page images of VOL.17-NO.1-JULY-2000.pdf, pages 32–33 (printed 30–31); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- performance
- competitions and puzzles
queries:
- "Printed byline “introduced by Jon Sandles”; the Contents line has “edited by Jon Sandles”. Sandles’s introduction is followed by one reprinted Zark column, “LIMBERING UP: Matrix Searching”, which is unsigned and has no Contents line or index record of its own; it is kept here under its own heading. (The Zark columns of the series are attributed by the index to Gary Bergquist.) The solutions follow in 17:2 as “Utility Corner: Matrix Searching” (unindexed/v17n2-p25-utility-corner-matrix-searching.md). The crossword the introduction mentions is the next Contents line (printed 32)."
- "The reprint note at the foot of printed 31, which closes the extract, is included here; Zark Incorporated’s address in it is a company address and is kept. The postal address for solutions is Vector Production’s, and is kept."
- "The APL names are printed in an italic APL face; they are set here as code."
---

*introduced by Jon Sandles*
{ .byline }

I hope you are all still enjoying these Zark reprints! Once again, we include a new crossword for your enjoyment and another classic APL problem. It would be interesting to see some new solutions to these problems, perhaps using Dyadic’s dynamic functions, or some J or even K. Solutions will be printed in the next issue.

## LIMBERING UP: Matrix Searching

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

Dyadic `⍳` (“index of”) is the principal searching function in APL. The value of each of the elements in its right argument is searched for in the vector left argument. The left argument *must* be a vector. The result is the same shape as the right argument and contains indices into the vector left argument where the elements of the right argument are first located.

Not all problems involve searching for values in a vector. Many searching problems involve matrices. For example, given a ten-row, eight-column character matrix of eight-character identification codes for ten products, locate each of the ten products in a master list of 1000 products (a 1000 by 8 character matrix). If dyadic `⍳` worked on matrices as well as vectors, the solution would be straightforward:

```apl
      INDICES←MASTERLIST ⍳ PRODUCTCODES
```

Where `MASTERLIST` and `PRODUCTCODES` are character matrices with shapes `1000 8` and `10 8` respectively, and `INDICES` is a ten-element vector of row indices into `MASTERLIST` where each row of `PRODUCTCODES` is first located.

Unfortunately, dyadic `⍳` requires a vector left argument. Given a matrix, it signals `RANK ERROR`. Until `⍳` is extended to work for matrices as well as vectors (we’re optimistic the day will come), alternative algorithms need to be used. Typically, these alternative algorithms hide in sub-functions that have the same syntax as dyadic `⍳` and that go by the name `IOTA`, `MIOTA`, `CMIOTA`, `LOOKUP`, `ROWFIND`, etc. Some implementations of APL even come equipped with a specially compiled or assembled function that serves this purpose.

Many different APL algorithms exist for searching character matrices. Your task is to compose the fastest ones you can muster and mail them in. The syntax should be:

```apl
      INDICES←CMATL CMIOTA CMATR
```

`CMIOTA` should work on character matrices. Searching problems that involve numeric matrices are relatively rare. If your algorithm works on numeric matrices too, that’s nice, but you get no extra credit!

The quality of the different algorithms will be measured based upon *speed* alone. However, all submitted functions will be tested on a variety of different implementations, and for different argument sizes. We’ll try them with left arguments having 2, 8, 64, 256, and 2048 rows, right arguments having 2, 8, 64, 256, and 2048 rows, and for 2, 4, 8, and 16 columns.

Please send your solutions to Vector Production at:

> Vector Production<br>
> Brook House<br>
> Gilling East<br>
> YORK YO62 4JJ<br>
> UK

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA*
