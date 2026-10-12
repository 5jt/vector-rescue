---
title: Counting in APL
authors:
- Alan Sykes
volume: '5'
issue: '2'
page: '27'
unindexed: true
transcribed: 'from page images of VOL.5-NO.2-NOVEMBER-1988.pdf, pages 29–34 (printed 27–32); Claude, 2026-10-12'
review: draft
tags:
- education
- programming techniques
- mathematics and statistics
queries:
- "The last piece of the Education Vector (supplement page 11). In the typewriter font of the examples the digit 1 sometimes prints like a capital I and the left arrow like +; transcribed 1 and ←. The quad character in the bar charts prints as a small box; transcribed ⎕."
- "Two results are printed on the same line as the expression that gives them (“+/(⍳6)∘.=NOS 2 3 1 2 1 1” and “+/(⍳⌈/T)∘.=T←⌈(NOS-0)÷2 6 3 2”); kept so."
- "Kept as printed: “1 3 5 , [1.5] 6 3 2” with spaces around the comma; “emphasized”."
---

*by Alan Sykes*
{ .byline }

## Introduction

Since APL is an array-oriented language, not surprisingly it is very good at counting. I don't mean by that producing the natural numbers 1 2 3 and so on, though of course the expression (for example) `⍳6` produces a list of the numbers 1 to 6. No, I mean counting incidences of occurrence of numbers or names in a list. In this first article of the new form of Education Vector, I shall try to introduce newcomers to APL to some of the techniques of counting that are really useful when it comes to applications. At the same time, I hope to include one or two 'goodies' namely useful functions whose coding may be a little complicated to the APL beginner, but nevertheless are easy to use effectively.

Throughout what follows, lines indented by five spaces correspond to APL statements that can be executed at the keyboard, with the following line(s) denoting the response.

## Simple Counting Techniques

Two lists (vectors) will be useful in this and following sections.

```apl
      NOS←2 1 2 3 2 4 1 5 6 4
      STR←'ACDBCDEABBA'
```

First we review the idea of comparisons and Boolean values (0 or 1). In APL the statement `2=3` has a numerical value of 0, and the statement `3=3` has a numerical value of 1, corresponding to the first statement being false , and the second true. Similarly the statement `X=2` is not an assignment statement as it would be in BASIC or FORTRAN, but results in one or more values of 1 or 0 depending on whether the individual numbers in X are equal to 2 or not. For example, try `NOS=2` or equivalently

```apl
      2=NOS
1 0 1 0 1 0 0 0 0 0
      'A'=STR
1 0 0 0 0 0 0 1 0 0 1
```

Hence if we want to know how many 2's there are in NOS we simply have to add up the elements of the result of `2=NOS`, which we do using the expression `+/` ...

```apl
      +/2=NOS
3
      +/'A'=STR
3
```

Now, being ambitious, we wish to count not only the number of 2's in NOS, but also the number of 1's, 3's and so on. Obviously this is possible simply by using five similar statements, with 2 replaced by 1 3 4 5 and 6. But, as you might suspect, there is an easier solution. The so-called 'jot-dot' construction using the two symbols '`∘`' and '`.`' together allows the arithmetic operation that follows to be applied to all possible pairs of numbers, one from the left argument and one from the right:

```apl
      1 2∘.=1 2 1
1 0 1
0 1 0
```

(Notice how the resulting array has as many rows as the left argument and as many columns as the right.) Hence ...

```apl
      1 2 3 4 5 6∘.=NOS
0 1 0 0 0 0 1 0 0 0
1 0 1 0 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 1
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 1 0
```

This is rather a large matrix (by 'pencil and paper' standards) but its row sums give the desired counts or frequencies. Recalling that 1 2 3 4 5 6 can be generated using `⍳6` and remembering the right to left rule, the complete set of frequencies is given by the expression:

```apl
+/(⍳6)∘.=NOS 2 3 1 2 1 1
```

## Producing a General Purpose Frequency Table

In Statistics, we often want to count not individual values but all values within a certain interval. For example, with NOS we may require to know how many values there are between 0 and including 2, between 2 and including 4 and so on. We can convert NOS into appropriate numbers by first subtracting 0, dividing by 2 and then rounding up to the nearest integer, converting ...

```apl
   2 1 2 3 2 4 1 5 6 4
TO 1 1 1 2 1 2 1 3 3 2
```

This is achieved easily using `⌈(NOS-0)÷2`. Now the ordinary counting techniques of section 2 can be applied:

```apl
+/(⍳⌈/T)∘.=T←⌈(NOS-0)÷2 6 3 2
```

Two points are worth noting about this. The right-most occurrence of `⌈` is executed first and rounds values of its argument up to the nearest integer. The next use of `⌈` is in the expression `⌈/T` which calculates the maximum value of the values in the list T. Also we have used a temporary variable T, assigned to it and then operated with T later (to the left!). This is a frequent nicety that experienced programmers in APL slip into, but there is nothing wrong in first assigning to T, and then executing the rest of the line up to the second occurrence of T. Indeed as a general rule always approach a new APL statement by taking each meaningful bit of it, working from right to left, and seeing what the result is - only then is it sometimes possible to understand what's really going on.

Back to our frequency table. It would be nice to output the frequencies 6 3 2 together with the mid-interval values associated with those frequencies. These values are calculated using:

```apl
(0-2÷2)+2×⍳⌈/T 1 3 5
```

These two results can be formed into a column matrix with the first column equal to the mid-interval values, and the second equal to the frequencies using:

```apl
      1 3 5 , [1.5] 6 3 2
1 6
3 3
5 2
```

So now we aren't too far from piecing bits of APL together to make a really useful function. Before we do so, we have to decide on the SYNTAX of that function, i.e. its name and what its arguments are. We will call it FREQTAB. This function needs two arguments, one to specify the name of the list of numbers it operates on - the right argument, and a second one telling us where to start our intervals, and how wide they are to be. So I propose that the above result of investigating NOS should be executed using the expression

```apl
      0 2 FREQTAB NOS
1 6
3 3
5 2
```

Users of I-APL have two methods of constructing this function. The direct definition method uses right argument `⍵` and left argument `⍺` and care must be taken to construct the rather long statement:

```apl
FREQTAB:((⍺[1]-⍺[2]÷2)+⍺[2]×M),[1.5]+/(M←⍳⌈/⍵)∘.=⍵←⌈(⍵-⍺[1])÷⍺[2]
```

The alternative to this mouthful, is to use the ordinary APL function editor and type short meaningful lines, as follows:

```apl
    ∇TAB←A FREQTAB W;F;V;T;M
[1]  T←⌈(W-A[1])÷A[2]
[2]  M←⍳⌈/T
[3]  F←+/M∘.=T
[4]  V←(A[1]-A[2]÷2)+A[2]×M
[5]  TAB←V,[1.5]F
    ∇
```

(N.B., the variables F,V,T, and M are only required internally and so are made LOCAL variables to the function FREQTAB by inserting them, separated by semi-colons after the function name and right argument.)

As an example of its use, create 25 numbers at random between 0 and 1 and count how many there are in intervals of width .25. First, to construct the numbers `?25ρ10000` produces 25 numbers chosen at random from 1 to 10000, so dividing the result by 10000 should suffice.

```apl
      R←(?25ρ10000)÷10000
      ⎕←F←0 .25 FREQTAB R
0.125  5
0.375 10
0.625  4
0.875  6
```

## Displaying FREQTAB using a BAR CHART - hence HISTOGRAMS!

Producing a bar chart from a frequency table such as the above is not an easy task for a newcomer to APL, but when explained clearly, the APL solution is quite straightforward - and again the power of thinking in terms of arrays is emphasized.

To illustrate the argument, consider the frequency column of F, consisting of the numbers 5 10 4 and 6, with maximum frequency 10. The bars corresponding to these frequencies must be of length 5,10,4,6 - or they could all be of length 10 as long as the last 5,10,6 and 4 characters respectively in each bar consist of blank characters! That's the first clue. Secondly, the expression

```apl
      5 10 4 6∘.≥⍳10
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
1 1 1 1 0 0 0 0 0 0
1 1 1 1 1 1 0 0 0 0
```

yields a pattern of 1's and 0's corresponding to that required. All we have to do is to replace the 1's by a character such as '⎕',the so-called 'quad', and the 0's by a blank. Normally we work in index origin 1 (the default setting) and so we can index the two element vector '` ⎕`' using the boolean array plus 1.

```apl
      ' ⎕'[1+5 10 4 6∘.≥⍳10]
⎕⎕⎕⎕⎕
⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
⎕⎕⎕⎕
⎕⎕⎕⎕⎕⎕
```

Now all that is required is to glue to the left-hand side of this array, a separator , say '|', preceded by the first column of the frequency table as an array of characters. The resulting function is called BAR and takes as its right argument a frequency table.

```apl
BAR:(⍕⍵[;,1]),'|',' ⎕'[1+⍵[;2]∘.≥⍳⌈/⍵[;2]]
```

or equivalently

```apl
    ∇B←BAR F
[1]  B←(⍕F[;,1]),'|',' ⎕'[1+F[;2]∘.≥⍳⌈/F[;2]]
    ∇
```

Let's try the results on some simulated dice values.

```apl
      THROW1←?50ρ6
      THROW2←?50ρ6
      THROW3←?50ρ6
      AV←(THROW1+THROW2+THROW3)÷3

      .5 1 FREQTAB THROW1
1 10
2  7
3  6
4  8
5 10
6  9

      BAR .5 1 FREQTAB THROW2
1|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕⎕⎕⎕⎕

      BAR 1.5 1 FREQTAB THROW1+THROW2
 2|⎕⎕⎕⎕
 3|⎕⎕⎕⎕
 4|⎕⎕⎕⎕⎕⎕
 5|⎕⎕⎕⎕
 6|⎕⎕⎕⎕
 7|⎕⎕⎕⎕⎕⎕
 8|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 9|⎕⎕⎕
10|⎕⎕⎕⎕
11|⎕⎕
12|⎕⎕⎕

      BAR .5 1 FREQTAB AV
1|⎕
2|⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕
```

As these simple examples illustrate, FREQTAB and BAR are powerful tools for investigating data. In fact pursuing examples like the ones above are quite sufficient to convince newcomers to Statistics of the validity of one of the most important results of Statistics - the so-called Central Limit Theorem, which for example, justifies the empirical observation that the values of AV ( the average of three separate tosses) tend to be more frequent near the mean value of 3.5 than at the extremes. (This is not true of course for just one throw.)

In practice, FREQTAB and BAR are used so often together that it is worth combining them to give HIST, as follows:

```apl
HIST: BAR ⍺ FREQTAB ⍵
```

or ...

```apl
    ∇H←L HIST DATA
[1]  H←BAR L FREQTAB DATA
    ∇
```

so that statements such as `0.5 1 HIST THROW1` are now meaningful.

## Conclusion

Throughout the presentation here, I have made use of the essential counting technique of summing the rows of a boolean matrix constructed by using '`∘.=`'. This is by far the most elegant way of achieving the results required, and is particularly handy for small-scale problems. However, for larger sets of data, the method does become rather inefficient. In the next issue of Education Vector we will discuss alternative methods, and present an interesting case study where its application is most effective.
