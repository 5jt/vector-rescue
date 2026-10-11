---
title: Counting in APL - Part Two
authors:
- Alan Sykes
volume: '5'
issue: '3'
page: '26'
unindexed: true
transcribed: 'from page images of VOL.5-NO.3-JANUARY-1989.pdf, pages 28–34 (printed 26–32; within The Education VECTOR, after I-APL News); Claude, 2026-10-11'
review: draft
tags:
- education
- programming techniques
- mathematics and statistics
queries:
- "The last piece in the Education Vector, after unindexed/v5n3-p22-i-apl-news.md (and the I-APL order form on printed 25); British APL Association News follows on printed 33. Part One is “Counting in APL” in Vector 5:2 (printed 27 there), whose functions FREQTAB and BAR are used here but not listed."
- "The birth data are transcribed line for line as printed. As printed they hold 646 symbols, of which 283 are B, 265 G and 98 |, against the text’s “length 648” and the result `283 267 98`. The boy-birth bar chart agrees with the data as printed; the daily table and the girl-birth chart imply one more G on the second day (BBGBBGGG) and on the day split across the last two lines (GGGB|GBGBBG), which are printed without it. Kept as printed."
- "The expressions on the small examples, COUNT and COUNTALL were run in Dyalog APL (⎕IO←1) as a check on the transcription; the printed results agree. COUNTALL [1] assigns R where the result is TAB; kept as printed."
- "Kept as printed: “preceeded”, “4 2’s,2 3’s”."
- "The bar charts use the quad-like box of the BAR function, transcribed ⎕; the bars were counted from the image and agree with the printed frequency table."
---

*by Alan Sykes*
{ .byline }

Oh no, not more counting! Nothing like counting to send the reader to sleep. Let’s arouse your interest by considering the following set of data consisting of a long list of the symbols B,G and |.

```
|BGBB|BBGBBGGG|GBBB|GB|GBBGGGBG|GGGBGGB|GBBGG|GBBBGB|BB|GBBGGGG|B
BGG|BBG|GBGBBBBBB|BG|BGG|BGBG|BBGBBB|BGBGG|BBBBG|BGGGBGGGG|GBGG|GG
BGBBB|GGBBGB|GGBBGBGG|BBGGB|GBGGGBB|GGGBBGB|BGGGG|GB|GGGBBGG|BG|GB
GB|GGBGGBBBG|BBGB|BGBGB|BGGB|GBB|BGBBBB|BGBGBG|BBGBBGB|BBBBBGB|GGG
GGBBB|BBGB|GBGBB|BGGG|GGGBBBGGG|B|BBGBBGBB|GBBGGBGBG|BGBGGBGGGB|BB
BBGGBBBG|BGGBBGB|GGBBBGG|BBGG|BBBGB|BBBBBBGG|GBBGG|GGBBBB|GBGGBBGG
GGG|GBBGB|GGGG|GBGG|BBBGGGG|GGBB|BBB|BGGBGGGG|BGGBGBBGB|BGGB|GBG|B
BGBB|GBG|BBBB|BBG|GGGBBGGGGGG|GGGBBBGBB|BGBBBB||GGGBB|BBBGBGBBB|GG
BBGGB|BGB|GGBBBBBB|GGGGGG|GGGGG|BGBB|BGBG|GBBBG|BBGGBB|BBGBGG|GGGB
GBGBBG|GB|BBGBB|GBGG|BBBBGGBGBG|BGBB|BGBBBBG|BGBGGGG|
```

This (genuine) data represents a sequence of successive births in a maternity hospital over a number of days. You will have guessed that B stands for a boy and G for a girl; not so obvious is that | denotes the division between days. To work with data such as this we need it as an APL character vector. The easiest way to enter the data from the keyboard is by way of the simple function `CHARINPUT`.

```apl
     ∇ R←CHARINPUT;X
[1]    R←''
[2]   MORE:X←⍞ ⋄ →(0=⍴,X)/0 ⋄ R←R,X ⋄ →MORE
     ∇
```

This allows small chunks of the list to be entered (say a day at a time):

```apl
      SEXORDER←CHARINPUT
|BGBB|
BBGBBGGG|
 .
 .
BGBGGGG|
```

Each new chunk is appended to the characters previously entered, and entry stops when a blank line is entered (i.e. RETURN is pressed with no prior characters).

Try entering some (not necessarily all) of the data. If all the data is entered as one long character vector of length 648, then the results of my previous article on counting in APL applied to `SEXORDER` produce some interesting preliminary results. For example

```apl
      +/'BG|'∘.=SEXORDER
283 267 98
```

shows us that 97 days are recorded, and that in total there are 283 boy-births and 267 girl-births. The proportion of boy-births is therefore `283÷283+267` or 51.4%. (Incidentally, this could have been calculated directly using the expression `÷1+÷/+/'GB'∘.=SEXORDER`.)

Before we investigate the data in more detail, let me quickly review some more operations on vectors that we need, and to do this I shall use the vector:

```apl
      X←2 1 3 5 9 2 4
```

We know already that the elements of `X` may be summed using the APL expression `+/X`. The symbol `/` is an APL operator, that may be combined with `+` (or other functions such as `×÷-*` and the comparison functions `<≤=≥>≠` and others) to produce another function. The scan operator `\` can also be used similarly with interesting effect. For example with `+` we get cumulative sums.

```apl
      +\X
2 3 6 11 20 22 26
```

Very often it is convenient to be able to take some of the elements of a vector either by choosing elements from the beginning or the end, or by dropping elements from the beginning or end. This is achieved by using `↑` to ‘take’ elements, or `↓` to ‘drop’ elements. Thus:

```apl
      2↑X
2 1

      3↓X
5 9 2 4
```

If a negative number is used, then the operation of taking or dropping is performed on the end of the vector.

```apl
      ¯1↓X
2 1 3 5 9 2
      ¯2↑X
2 4
```

Finally, we can select elements from a vector according to a boolean vector (logical recipe) using the replicate function `/` preceeded by a boolean vector.

```apl
      (X≠5)/X
2 1 3 9 2 4
      (X=2)/⍳⍴X
1 6
```

(because `⍳⍴X` is the vector `1 2 3 4 5 6 7`).

So back to our next task in counting - to count the total number of births for each day. To illustrate the method I shall use the first three days of the data, namely `S←'|BGBB|BBGBBGGG|GBBB|'`. Applying the tools just illustrated, we can calculate the vector `N` which tells us where each `'|'` is.

```apl
      ⎕←N←(S='|')/⍳⍴S
1 6 15 20
```

(In this last expression `'⎕←'` merely outputs the results to the screen as well as assigning them to `N`.)

What is required from `N` is the successive differences (6-1), (15-6), and (20-15). The easiest way to achieve them is to difference the two vectors created by dropping one element from each of the front and the back:

```apl
      (1↓N)-¯1↓N
5 9 5
```

Since these differences include one |, the frequencies required are one less and so the frequencies for the first three days are given by:

```apl
      ¯1+(1↓N)-¯1↓N←(S='|')/⍳⍴S
4 8 4
```

Applying to the complete data `SEXORDER`, we can obtain the vector `DAILYFREQ` of daily frequencies:

```apl
      DAILYFREQ←¯1+(1↓N)-¯1↓N←(SEXORDER='|')/⍳⍴SEXORDER
```

Using the functions `FREQTAB` and `BAR` introduced last time, we may process the frequency vector as follows:

```apl
      ⎕←FT←¯.5 1 FREQTAB DAILYFREQ
 0  1
 1  1
 2  6
 3  8
 4 20
 5 15
 6 10
 7 14
 8  7
 9  9
10  3
11  3
      BAR FT
 0|⎕
 1|⎕
 2|⎕⎕⎕⎕⎕⎕
 3|⎕⎕⎕⎕⎕⎕⎕⎕
 4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 6|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 7|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 8|⎕⎕⎕⎕⎕⎕⎕
 9|⎕⎕⎕⎕⎕⎕⎕⎕⎕
10|⎕⎕⎕
11|⎕⎕⎕
```

Now we can see that the most likely number of births in a day is 4, but the average is 5.67 (calculated from `DAILYFREQ` using `(+/DAILYFREQ)÷⍴DAILYFREQ` or from `FT` using `(+/×/FT)÷+/FT[;2]`).

Slightly more demanding, is to determine the frequency of boy-births for each day. With our small sample `S` introduced earlier, the secret is to calculate cumulative sums of boy-births:

```apl
      ⎕←CB←+\S='B'
0 1 1 2 3 3 4 5 5 6 7 7 7 7 7 7 8 9 10 10
```

The vector `N←(S='|')/⍳⍴S` used before tells us where each | is. Indexing `CB` on `N` yields `M`, the cumulative number of boys for each day:

```apl
      ⎕←N←(S='|')/⍳⍴S
1 6 15 20
      ⎕←M←(+\S='B')[N]
0 3 7 10
```

`M` can then be differenced as before to obtain the daily number of boy births. Here is the whole calculation pieced together though it is no sin to do it in separate stages!

```apl
      (1↓M)-¯1↓M←(+\S='B')[N←(S='|')/⍳⍴S]
3 4 3
```

Using this expression with `S` replaced by `SEXORDER` and assigning the result to `BOYFREQ`, we can calculate the boy-birth daily frequencies, and hence by subtracting this from `DAILYFREQ`, the vector `GIRLFREQ` can also be calculated. Here are the bar charts, first for `BOYFREQ` and secondly for `GIRLFREQ`:

```apl
0|⎕⎕⎕⎕
1|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕
7|⎕⎕⎕

0|⎕⎕⎕⎕⎕
1|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
2|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
3|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
4|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
5|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
6|⎕⎕⎕⎕⎕⎕
7|⎕
8|⎕
9|⎕
```

So much for our interesting example. Let’s now see how these same techniques may be used to good effect to provide more efficient APL methods for counting.

Suppose `X` is the vector `X←2 1 2 2 1 3 4 3 2 4`

Then it may be ordered (increasingly) by indexing `X` on the vector `⍋X`. (`⍋` stands for ‘upgrade’, and it is the vector whose first element is the index (position in `X`) of the smallest element of `X`, whose second element is the position of the next smallest element in `X`, and so on.)

```apl
      ⍋X
2 5 1 3 4 9 6 8 7 10
      X[⍋X]
1 1 2 2 2 2 3 3 4 4
```

If we rotate this vector one place to the left as follows:

```apl
      X←X[⍋X]
      1⌽X
1 2 2 2 2 3 3 4 4 1
```

then the indicator vector `I←(1⌽X)≠X` has 1’s in the positions of the last occurrence of each of the values occurring.

```apl
      ⎕←I←(1⌽X)≠X
0 1 0 0 0 1 0 1 0 1

      ⎕←N←I/⍳⍴I
2 6 8 10
```

By differencing the vector `2 6 8 10` with `0 2 6 8`, we can deduce that there are 2 1’s, 4 2’s,2 3’s and 2 4’s.

```apl
      N-0,¯1↓N
2 4 2 2
```

One slight technical problem with this approach is that if all the elements of the counted vector are the same, then the above procedure must be modified. The technique illustrated is used in the following two functions to count elements of a numeric vector. `COUNT` returns the frequencies in the right argument of each element of the left argument:

```apl
      1 2 3 COUNT 3 1 1 2 1 5
3 1 1
```

`COUNTALL` on the other hand returns a frequency table whose first column is a list of unique values, whilst the second column gives the associated frequencies:

```apl
      COUNTALL 3 1 1 2 1 5
1 3
2 1
3 1
5 1
```

```apl
     ∇ FREQ←T COUNT X;I;N;V;F
[1]    X←X[⍋X] ⋄ V←,X[1] ⋄ F←⍴X
[2]    →(X[1]=X[⍴X])/SETFREQ
[3]    I←(1⌽X)≠X ⋄ F←N-0,¯1↓N←I/⍳⍴I
[4]    V←I/X
[5]   SETFREQ:FREQ←(F,0)[V⍳T]
     ∇

     ∇TAB←COUNTALL X;I;N
[1]    X←X[⍋X] ⋄ R← 1 2 ⍴(1↑X),⍴X
[2]    →(X[1]=X[⍴X])/0
[3]    I←(1⌽X)≠X ⋄ N←I/⍳⍴I
[4]    TAB←(I/X),[1.5]N-0,¯1↓N
     ∇
```

As you can see, the new method is somewhat more involved than that used previously. For large sets of data however, the method used here is much quicker, because it does not involve the construction and row summation of a very large matrix. In addition, the techniques described here may be adapted to deal with character arrays with only minor changes.

This is because `⍋` or upgrade will work on a character matrix as long as the required ordering of the characters is specified. For most purposes, the order of the characters as contained in the atomic vector `⎕AV` is appropriate. For example, let `M` be the 4 by 4 matrix given by:

```apl
      M←4 4⍴'FREDALGYPETEALAN'
      M
FRED
ALGY
PETE
ALAN
```

Then `⎕AV⍋M` returns the vector `4 2 1 3`, so that `M[⎕AV⍋M;]` lists the names in alphabetical order.

```apl
      M[⎕AV⍋M;]
ALAN
ALGY
FRED
PETE
```

(N.B. the semi-colon is necessary as we wish to print the rows of the matrix out in the order determined by `⎕AV⍋M`.)

Given this, the functions `COUNT` and `COUNTALL` may be suitably altered to deal with character lists. But perhaps that’s best left for another time!
