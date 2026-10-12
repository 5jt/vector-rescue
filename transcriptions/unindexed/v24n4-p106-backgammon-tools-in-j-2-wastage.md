---
title: 'Backgammon tools in J: 2. Wastage'
authors:
- Howard A. Peelle
volume: '24'
issue: '4'
page: '106'
unindexed: true
transcribed: 'from the typeset issue v244.pdf, pages 106–109 (printed 106–109); Claude, 2026-10-12'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "The index has this article with no ID. Headed “BACKGAMMON TOOLS IN J” over the title “2. Wastage”; printed byline “by Howard A. Peelle” (the Contents line has “Howard Peelle”). Following the project rule for individuals’ contact details, the author’s personal e-mail address under the byline is omitted."
- "The table of other distributions is printed in the code font without rules; it is given here as a table, with the printed column headings."
- "Code is kept as printed, with its indentation: the input line “boards #~ wastages = <./wastages” on printed 107 is indented further than the others, and “Partitions =: ;@AllParts” on printed 108 less; the blank lines between “ELSE =: `” and “WHEN =: @.”, and after “#boards” and “boards #~ wastages = <./wastages” on printed 109, are printed. The text layer of the PDF misreads several J characters (~, -, ^); the page images were followed."
- "Kept as printed: in the Appendix, “wastages =. Wastage\"1 boards” with a local assignment, where the body has “=:”."
---

*by Howard A. Peelle*
{ .byline }

> J programs are presented as analytical tools for expert backgammon. Part 2 here develops a program to compute the number of pips expected to be wasted while bearing off pieces in one inner board (without contact).

The inner board is represented as a list of six integers. For example, 0 pieces on the 1, 2, and 3 points, 2 on the 4-point, 3 on the 5, and 4 on the 6:

```j
   board =: 0 0 0 2 3 4
```

To count pips for bearing off, sum the board times a list of the point numbers:

```j
   ,pips =:  +/ board * 1 2 3 4 5 6
47
```

Use program `N` (from [1]) to compute expected number of rolls to bear off:

```j
   ,n =: N board
6.56681
```

Expected number of pips to bear off is the expected number of rolls `n` times the average number of pips per roll (8 1/6):

```j
   n * 8+1%6
53.6289
```

Wastage is this expected number of pips minus the pipcount.

```j
   ,wastage =: (n * 8+1%6) - pips
6.62895
```

Define a program to compute wastage for any inner board:

```j
   Wastage =: (N * 8:+1:%6:) - Pips
      Pips =: +/ . * Points
         Points =: 1: + i.@6:
```

For the example above:

```j
   Wastage 0 0 0 2 3 4
6.62895
```

Wastage for all possible full distributions (with all 15 pieces) in the inner board follows:

```j
   all =: (6#16) #: i.16^6
   boards =: (15 = +/"1 all) # all
```

(See Appendix for an alternative way to generate these boards using partitions.)

Wastages for all full inner boards are:

```j
   wastages =: Wastage"1 boards
```

The minimum wastage is:

```j
   <./wastages
7.06895
```

The board with minimal wastage is:

```j
      boards #~ wastages = <./wastages
0 0 0 3 5 7
```

Other distributions can be searched similarly:

| # Pieces | #Boards | Minimum Wastage | Best board |
|---:|---:|---:|---|
| 15 | 15504 | 7.06895 | 0 0 0 3 5 7 |
| 14 | 11628 | 7.02941 | 0 0 0 3 5 6 |
| 13 | 8568 | 6.98028 | 0 0 0 3 4 6 |
| 12 | 6188 | 6.90551 | 0 0 0 2 4 6 |
| 11 | 4368 | 6.82085 | 0 0 0 2 4 5 |
| 10 | 3003 | 6.75322 | 0 0 0 2 3 5 |
| 9 | 2002 | 6.62895 | 0 0 0 2 3 4 |
| 8 | 1287 | 6.51014 | 0 0 0 1 3 4 |
| 7 | 792 | 6.36102 | 0 0 0 1 3 3 |
| 6 | 462 | 6.14734 | 0 0 0 1 2 3 |
| 5 | 252 | 5.88967 | 0 0 0 1 2 2 |
| 4 | 126 | 5.52802 | 0 0 0 1 1 2 |
| 3 | 56 | 5.30579 | 0 0 0 1 1 1 |
| 2 | 21 | 4.62037 | 1 0 1 0 0 0 |
| 1 | 6 | 4.20833 | 0 0 0 0 0 1 |

## Reference

1. Peelle, Howard A. “Backgammon Tools in J: 1. Bearoff Expected Rolls”, *Vector*, Vol.24, N°2

## Appendix

Program to compute wastage:

```j
Wastage =: (N * 8:+1:%6:) - (+/ . * 1: + i.@6:)
```

See [1] for script with definition of N to compute expected number of rolls to bear off.

Co-recursive program to compute all partitions of an integer x into y parts:

```j
   ELSE =: `

   WHEN =: @.
Partitions  =: ;@AllParts
   AllParts =: <@Parts"0 >:@i.
      Parts =: Ps ELSE (,.@[) WHEN (]=1:)
         Ps =: Add1 ELSE (#1:) WHEN =
            Add1 =: 1: + ] {."1 - Partitions - <. ]
```

For example:

```j
   8 Partitions 3
8 0 0
7 1 0
6 2 0
5 3 0
4 4 0
6 1 1
5 2 1
4 3 1
4 2 2
3 3 2
```

Program to produce a table of permutations:

```j
Perms =: i.@! A. i.
```

All full distributions of 15 pieces on 6 points in an inner board:

```j
   boards =: ~. ,/ (Perms 6) {"1/ 15 Partitions 6
```

Number of full inner boards:

```j
   #boards

15504
```

All wastages:

```j
   wastages =. Wastage"1 boards
```

Average wastage:

```j
   Average =: +/ % #
   Average wastage
15.7857
```

Minimal wastage:

```j
   <./wastages
7.06895
```

Board with minimal wastage:

```j
   boards #~ wastages = <./wastages

0 0 0 3 5 7
```

Top ten minimal boards:

```j
   10 {. boards /: wastages
0 0 0 3 5 7
0 0 1 2 5 7
0 0 1 3 5 6
0 0 0 2 5 8
0 0 1 3 4 7
0 0 0 2 6 7
0 0 0 3 6 6
0 0 0 4 5 6
0 0 0 3 4 8
0 0 1 2 6 6
```
