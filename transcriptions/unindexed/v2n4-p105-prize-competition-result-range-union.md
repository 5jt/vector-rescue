---
title: 'Prize Competition result: “Range Union”'
authors:
- Jonathan Barman
volume: '2'
issue: '4'
page: '105'
unindexed: true
transcribed: 'from page images of VOL.2-NO.4-APRIL-1986.pdf, pages 107–109 (printed 105–107; an advert follows on p.108; Watch your step follows on p.109); Claude, 2026-10-05'
review: draft
tags:
- competitions and puzzles
queries:
- "The competition was set in Vol.2 No.2, which we have no scan of (#62)."
- "The scan operator is printed ⌈ with a barred backslash (⌈⍀, scan along the first axis), as the printed results require; the bar is faint in places."
- "Checked by hand: every intermediate result on pp.105–106 follows from A as printed (sort, ⌈⍀, 0 ¯1⊖, 1,1↓1<-/R = 1 0 1 0 0, and the final 1 4 / 8 12)."
- "RANGEUNION [3] is printed `R← 0 1 ⊖(1,1<1↓-/R)⌿R`, the text above it `(1,1↓1<-/R)⌿R`; the two are equivalent."
- "Slips transcribed as printed: “makes the the comparison”, “the second column is so rotated so that”."
---

by Jonathan Barman
{ .byline }

Competitors had to provide a function that combined overlapping and duplicate ranges in a set of ranges, and returned the ‘union’ of the set. For example:

```apl
      A
 1  4
12 12
 8 11
 8 10
 2  2
      RANGEUNION A
 1  4
 8 12
```

Twelve entries were received which exhibited almost as many different methods of solving the problem. The fastest, and the most elegant, method was submitted by Paul Chapman and also Morten Kromberg, who used the ingenious method of taking the maximum scan of the sorted matrix of ranges to get the set of overall start and end ranges. It is easiest to understand the method with a worked example.

The first step is to sort the matrix so that the range starts are in sequence:

```apl
      A[⍋A[;⎕IO];]
 1  4
 2  2
 8 11
 8 10
12 12
```

and then do the maximum scan:

```apl
      ⌈⍀A[⍋A[;⎕IO];]
 1  4
 2  4
 8 11
 8 11
12 12
```

The maximum scan has the effect of forcing the end of the ranges to be the biggest so far encountered. One competitor missed out this vital step, but sorted both columns of the matrix, which only produces an erroneous result if one range is wholly included inside another range. In the example the range 2 to 2 is wholly included inside the range 1 to 4.

The ranges required are those where the start of each range is greater than the end of the previous range. Rotating one column of the matrix makes the the comparison between the starts and previous ends easy:

```apl
      0 ¯1⊖⌈⍀A[⍋A[;⎕IO];]
 1 12
 2  4
 8  4
 8 11
12 11
```

At this point both Paul and Morten noticed that a temporary variable could be formed which could be used later when generating the result, so the first line of the function is:

```apl
R←0 ¯1⊖⌈⍀A[⍋A[;⎕IO];]
```

The first row is always required, as it contains the lowest start which is correct for the first range, and the highest end which is correct for the last range. The remaining rows are needed if start is larger than the previous end:

```apl
      1,1↓1<-/R
1 0 1 0 0
```

and this is used to select the rows of the temporary result:

```apl
      (1,1↓1<-/R)⌿R
1 12
8  4
```

Finally, the second column is so rotated so that the previous range ends become the current range ends:

```apl
      0 1⊖(1,1↓1<-/R)⌿R
1  4
8 12
```

So the final function becomes:

```apl
    ∇ R←RANGEUNION A
[1]   ⍝ <R> is union of ranges in two column matrix <A>
[2]    R← 0 ¯1 ⊖⌈⍀A[⍋A[;⎕IO];]
[3]    R← 0 1 ⊖(1,1<1↓-/R)⌿R
    ∇
```

Many other methods were used, including a looping solution. Several solutions used the outer product to compare the start and end points with the full set of possible numbers; which results in WS FULL if the disparity between ranges is large. As in previous competitions, competitors did not always test their code in index origin zero or with zero row matrices.

The problem stated that the right argument could be assumed to be a 2-column integer matrix, but it was not stated that the ranges would always be given with the starts in the first column. Only two solutions included code to reverse the columns, and Mark Longstaff’s method was best:

```apl
(>/A)⌽A
```

As it was stated that no checking of the matrix was necessary, it was decided not to make this check a requirement for a successful entry.

The CPU times varied enormously, from 0.44 to 11.59 seconds (for a matrix of 100 ranges, on an IBM PC XT running APL\*PLUS APL). Morten Kromberg’s solution was the fastest. He transposed the matrix at the beginning and again at the end so that the rotates could be applied along the last axis.

Paul Chapman gave a very good analysis of how he came to save the temporary result, which is worth reproducing. In his example R is the sorted right argument:

> By comparing each max-scanned range end with the following range start, we can establish where the breaks occur:
>
> ```apl
> X←1<1↓-/ 0 ¯1 ⊖⌈⍀R
> ```
>
> This gives us a 1 between each pair of ranges which are not connected, so that there is one less 1 than rows in the desired result. Now the result range starts are:
>
> ```apl
> (1,X)/R[;⎕IO]
> ```
>
> and the result range ends are:
>
> ```apl
> (X,1)/⌈\R[;⎕IO+1]
> ```
>
> which also happens to be:
>
> ```apl
> 1⌽(1,X)/¯1⌽⌈\R[;⎕IO+1]
> ```
>
> so the two operations can be combined:
>
> ```apl
> 0 1⊖(1,X)⌿ 0 ¯1 ⊖⌈⍀R
> ```
>
> But we have already calculated
>
> ```apl
> 0 ¯1 ⊖⌈⍀R .
> ```
>
> so we can simplify:
>
> ```apl
> Z← 0 ¯1 ⊖⌈⍀R
> X←1<1↓-/Z
> R← 0 1 ⊖(1,X)⌿Z
> ```

Paul Chapman and Morten Kromberg are the joint winners. Paul included code to sort the second column of the matrix, but this is not strictly necessary as the maximum scan takes care of items being out of sequence within each set of starts. Morten did not use the minus reduction in order to compare the break points, so his code looked a little less elegant. Third prize goes to Mike Day who gave a fast solution using a slightly different method.

We were again pleased to see entries from overseas, this time they included correspondents from Italy, Sweden and Switzerland. It was also good to see a solution developed on the QL.
