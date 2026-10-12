---
title: 'Zark Newsletter Extracts: Limbering Up: Combinations'
authors:
- Jon Sandles
volume: '17'
issue: '4'
page: '26'
unindexed: true
transcribed: 'from page images of VOL.17-NO.4.pdf, pages 28–29 (printed 26–27); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
- competitions and puzzles
queries:
- "Printed heading “ZARK Newsletter Extracts”, byline “introduced by Jon Sandles” (the Contents line has “edited by Jon Sandles”); the extract has no introduction of its own and consists of one column, “Limbering Up: Combinations”, which is unsigned, reprinted from Zark APL Tutor News (compare unindexed/v17n2-p31-limbering-up-comma-delimited-data.md, attributed there to Gary Bergquist). The reprint note at the foot of printed 27, which closes the extract, is included. The crossword follows on printed 28."
- "Kept as printed: “(And it even works o other objects!)”; “MIN rows”, evidently for `M!N`; “CT06029”."
---

*introduced by Jon Sandles*
{ .byline }

## Limbering Up: Combinations

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

The combination function `!` is one you probably don't use often. It tells you the number of different ways you can select M coloured jelly beans from a set of N jelly beans. (And it even works o other objects!) Each jelly bean has a different colour.

For example, suppose you have 5 beans, coloured Black, Green, Purple, Red, and Yellow. How many different combinations can you make?

```apl
      3!5
10
```

Ten combinations. Here they are:

```text
BGP   BPR   GPR   PRY
BGR   BPY   GPY
BGY   BRY   GRY

  B=Black   R=Red
  G=Green   Y=Yellow
  P=Purple
```

Your task is to write a function that allows you to construct a set of different combinations. Call it `COMBIN`, and give it the same syntax as the `!` function. Given the left argument `M` and the right argument `N`, it returns a matrix of indices with `MIN` rows and `M` columns.

```apl
      3 COMBIN 5
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
```

To get the answer to the jelly bean problem, use the expression,

```apl
      'BGPRY'[3 COMBIN 5]
BGP
BGR
BGY
BPR
BPY
BRY
GPR
GPY
GRY
PRY
```

Seem simple enough? Try your hand at writing this function. Naturally, efficiency is important. However, elegance (whatever that is) and originality will also be acknowledged.

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA*
