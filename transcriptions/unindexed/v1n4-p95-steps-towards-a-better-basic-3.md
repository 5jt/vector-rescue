---
title: Steps Towards a Better Basic — Part 3
authors:
- Anthony Camacho
volume: '1'
issue: '4'
page: '95'
unindexed: true
transcribed: 'from page images of VOL.1-NO.4-APRIL-1985.pdf, pages 97–99 (printed 95–97; follows art10006700; the Case Study notes heading art10003470 follow on p.98); Claude, 2026-10-03'
review: draft
queries:
- "A reprint from Datalink; parts 1 and 2 are v1n1-p77 and v1n2-p73."
- "The BASIC example sets T$ = “ABCEDFGHI” and prints ABCEDFGHI after the exchange; printed so (the starting string presumably meant ABCDEFGHIJ)."
- "Checks: every result in Figs 1–4 recomputed: 2 5⍴A, 7⍴A, 3 9⍴A, 2 3 4⍴A, A[1;2;3] = 7, all five Fig. 2 lines give 1 2 4 3 5 6 7 8 9 0, B+5, B×1.15, +/A = 45, +/B = 15 30, +⌿B = 7 9 12 12 5."
- "APL in the figures is in an italic APL face; the comment glyph is printed as ⍝ with an arrow in Fig.1’s first comment (“⍝ ← THIS IS THE APL SYMBOL FOR COMMENT”). Wrapped comment lines are rejoined."
---

by Anthony Camacho
{ .byline }

*This is the third extract from the series in Datalink in which Anthony Camacho attempts to explain some APL concepts in terms familiar to BASIC programmers. Here he takes BASIC string handling and re-casts it using the APL ideas of indexing and character vectors.*

*The article is reproduced by kind permission of Datalink magazine.*

When there are many items in a single variable, there has to be a way of determining how many items there are and of picking out one or several of the items for separate processing. In BASIC only string variables can contain many items, and LEN, MID$, LEFT$ and RIGHT$ are the functions used. They are fairly clumsy in use as the expression needed to exchange the third and fourth letters in a ten letter variable makes clear.

```
T$ = "ABCEDFGHI"
T$ = LEFT$(T$,2) + MID$(T$,4, 1) +
        MID$(T$,3, 1) + RIGHT$(T$,6)
PRINT T$
ABCEDFGHI
```

In Sinclair BASIC the expression is more elegant:

```
T$ = T$( TO 2) + T$(4) + T$(3) + T$(5 TO )
```

Some versions of BASIC allow:

```
MID$(T$,3,2) = MID$(T$,4,1) + MID$(T$,3,1)
```

and the Sinclair version is:

```
T$(3 TO 4) = T$(4) + T$(3)
```

— even better.

In APL a variable can hold many items of any one kind: many integers, floating point numbers or Boolean values as well as letters; these arrays can have several dimensions so that tables and sets of tables are practical. LEN in BASIC only reports size in one dimension; APL needs ‘SHAPE’ and uses the Greek letter ‘R’ (rho) for the function. ‘SHAPE’ reports the shape of a variable by giving the length of each dimension in turn, so there are as many items in the result as there are dimensions in the variable. For example the shape of a variable which has two tables each three rows of four columns would be 2 3 4. The shape of 2 3 4 is 3 because it contains three separate integers, so you can find the number of dimensions of a variable by asking for the shape of the shape of it.

You can change the shape of a variable by giving a left argument which is the required shape (making the function ‘RESHAPE’). If the number of items in the reshaped variable is not the same as in its original shape then items are lost or repeated as necessary. See Fig. 1 for some examples. APL uses the left arrow for assignment instead of the equals sign. Notice how convenient it is that APL displays any value you enter which is not explicitly assigned to a variable.

*Fig.1*

```
      A←1 2 3 4 5 6 7 8 9 0
      ⍴A
10
      ⍝ ← THIS IS THE APL SYMBOL FOR COMMENT
      ⍝ NOW SOME RESHAPING OF A
      2 5⍴A
1 2 3 4 5
6 7 8 9 0
      7⍴A
1 2 3 4 5 6 7
      3 9⍴A
1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8
9 0 1 2 3 4 5 6 7
      ⍝ NOW RESHAPE A INTO TWO TABLES OF 3 ROWS BY 4 COLUMNS
      2 3 4⍴A
1 2 3 4
5 6 7 8
9 0 1 2

3 4 5 6
7 8 9 0
1 2 3 4
      ⍝ OF COURSE A IS UNCHANGED BY ALL THIS
      A
1 2 3 4 5 6 7 8 9 0
```

The comma is used to join arrays together where BASIC joins strings with ‘ + ’. The APL equivalent of LEFT$ is the upwards pointing arrow (called ‘take’) which takes items from the left (or right if the argument is negative), and the downwards pointing arrow (called ‘drop’) similarly drops items from the left or right. APL uses square brackets to contain an index (and if there are several dimensions, separates the indices with semi-colons), so in the last example Fig. 1 A[1;2;3] would be 7. With these and other functions which can operate along the rows or down the columns of tables, APL offers very versatile ways of handling variables containing many values. Fig. 2 shows five APL equivalents of the BASIC above, incidentally showing in the fifth example that APL can assign values to part of a variable.

*Fig.2*

```
      A←(2↑A),A[4],A[3],4↓A
      A←(¯8↓A),A[4 3],¯6↑A
      A←A[1 2],A[4 3],A[5 6 7 8 9 10]
      A←A[1 2 4 3 5 6 7 8 9 10]
      A[3 4]←A[4 3]
      ⍝ THE VALUE OF A AFTER ANY OF THESE IS:
1 2 4 3 5 6 7 8 9 0
```

There are far more operations that work on numbers than there are that work on strings. The handling of numeric arrays gives great scope. See Fig.3.

*Fig.3*

```
      B←2 5⍴A
      B
1 2 4 3 5
6 7 8 9 0
      ⍝ NOW ADD 5 TO ALL ITEMS
      B+5
 6  7  9  8 10
11 12 13 14  5
      ⍝ OR ADD VAT
      B×1.15
1.15 2.3  4.6  3.45 5.75
6.9  8.05 9.2 10.35 0
```

One frequent need is to carry out the same operation repeatedly on all members of an array. The function ‘over’ (APL uses the oblique stroke) inserts the function on the left between each item of the variable to the right. See Fig.4.

*Fig.4*

```
      +/A
45
      ⍝ THE / REFERS TO THE LAST DIMENSION SO +/B ADDS THE COLUMNS
      +/B
15 30
      ⍝ BUT ⌿ REFERS TO THE FIRST DIMENSION SO +⌿B ADDS THE ROWS
      +⌿B
7 9 12 12 5
      ⍝ AND +/+/B ADDS ALL ITEMS
      +/+/B
45
```
