---
title: 'Utility Corner: Matrix Searching'
authors:
- Gary A. Bergquist
volume: '17'
issue: '2'
page: '25'
unindexed: true
transcribed: 'from page images of VOL.17-NO.2-OCTOBER-2000.pdf, pages 27–33 (printed 25–31; within Zark Newsletter Extracts, after Stephen Jaffe’s letter); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. It is followed on p.31 by “Limbering Up: Comma-Delimited Data”, transcribed separately as unindexed/v17n2-p31-limbering-up-comma-delimited-data.md. The timings the last paragraph mentions were put on the Vector web site (art10014130, “Timings for CMIOTA”)."
- "`CMIOTA7` to `CMIOTA12` were run in Dyalog APL as a check on the transcription; all return `2 5 1` for a small sample. `CMIOTA1` to `CMIOTA3` use APL\\*PLUS `⎕DR` conversions and were not run; nor were the looping `CMIOTA4` and `CMIOTA5`."
- "Kept as printed: “The first three function are”, “loops of the rows of the left argument”, “provide and “assembled” function”, “with as many elements are the PRODUCT”, “Do you own timings”, “Second. The result”, “Each row become”; in `CMIOTA12` the comment “Uses AP2 nests”; in `CMIOTA10` the comments “Gread-up”, “distict” and “one greate than length”."
---

## Utility Corner: Matrix Searching

In last issue’s LIMBERING UP column, we asked for algorithms to search through character matrices. In particular, given two character matrices `A` and `B`, having the same number of columns, write a function whose syntax is

```apl
R←A CMIOTA B
```

Which returns a vector of row indices that give the locations in `A` where the rows of `B` first occur. You can consider the `CMIOTA` (Character Matrix IOTA) function an extension of the primitive APL function dyadic `⍳` on vectors `A` and `B`:

```apl
R←A⍳B
```

Both functions search through `A` for the values in `B`. The result is a vector of indices whose length is determined by the shape of `B` and whose values are limited by the shape of `A`.

Frankly, we were surprised by the variety of algorithms received. There was nothing new, really, but we hadn’t stopped to count the different approaches used to solve this age-old problem. More surprising were the results of our timings. Each algorithm was a winner. We timed the algorithms in three different APL environments, APL\*PLUS PC, APL\*PLUS II, and mainframe APL2 (the three environments under which Zark APL Tutor currently operates, naturally), and for a wide variety of argument sizes.

Some were better for skinny arguments, others for fat arguments. Some preferred small left arguments and lengthy right arguments, and some preferred the opposite. Some were good in one implementation of APL and lousy in another. Very interesting.

The results strengthened our conviction that the implementers of APL should consider a logical extension of dyadic `⍳` to handle character matrix arguments. Let THEM decide which algorithm to use for different argument sizes. Besides, most vendors already provide and “assembled” function (named `LOOKUP`, `ROWFIND`, `IOTA` or some such) that performs this task. These assembled functions were not included in our timings. We suspect they would blow away the other APL algorithms.

Our recommendation: Use an assembled function if available to you. If not, pick the best algorithm from the ones below, given the sizes of your arguments.

The first three function are specific to APL\*PLUS. They use the system function `⎕DR` (data representation) and exploit the fact that a two-, four-, or eight-column character matrix can be interpreted as a numeric vector. Once you view the array as a numeric vector, dyadic `⍳` can be applied directly.

```apl
     ∇ R←A CMIOTA1 B
[1]   ⍝ For APL*PLUS PC, two-column args
[2]   ⍝ only (two-byte integers).
[3]    R←(163 ⎕DR,A)⍳163 ⎕DR,B
     ∇

     ∇ R←A CMIOTA2 B;⎕CT
[1]   ⍝ For APL*PLUS PC/II, eight-column
[2]   ⍝ args only (eight byte numbers).
[3]    ⎕CT←0 ⋄ R←(645 ⎕DR,A)⍳645 ⎕DR,B
     ∇

     ∇ R←A CMIOTA3 B
[1]   ⍝ For APL*PLUS II, four-column args
[2]   ⍝ only (four-byte integers).
[3]    R←(323 ⎕DR,A)⍳323 ⎕DR,B
     ∇
```

Notice `CMIOTA1` works for APL\*PLUS PC but not APL\*PLUS II, and `CMIOTA3` does the opposite, because APL\*PLUS PC supports two-byte integers, whereas APL\*PLUS II supports four-byte integers. Both APL\*PLUS interpreters support eight-byte floating point numbers (`CMIOTA2`), but `⎕CT` (comparison tolerance) must be set to `0` so all 64 bits of significance are considered when dyadic `⍳` makes its comparisons.

(The system variable `⎕CT` is consulted by the APL interpreter only when floating point comparisons are made. The value of `⎕CT` determines how fussy [some say “fuzzy”] APL will be when deciding whether two very close values are equal. For example, the expression `2.99999999999999=3.00000000000001` will return `1` normally, but will return `0` if `⎕CT` is set to `0`, its fussiest [least fuzzy] setting.)

The next two `CMIOTA` functions take a brute-force approach. `CMIOTA4` loops on the rows of the right argument, while `CMIOTA5` loops of the rows of the left argument. The heart of each algorithm is the use of the inner product `∧.=` between a vector and the rows of a matrix. The result is a Boolean vector with as many bits as the matrix has rows. The `1` bits flag rows that match the vector.

```apl
     ∇ R←A CMIOTA4 B;I;L;N
[1]   ⍝ Loop on rows of right arg.
[2]    R←(N←1↑⍴B)⍴0
[3]    L←(N⍴LOOP),0
[4]    →L[I←⎕IO]
[5]   LOOP:R[I]←(A∧.=B[I;])⍳1
[6]    →L[I←I+1]
     ∇

     ∇ R←A CMIOTA5 B;I;L;M;N
[1]   ⍝ Loop on rows of left arg;
[2]   ⍝ decrement to return 1st, not last.
[3]    R←(N←1↑⍴B)⍴I←⎕IO+M←(⍴A)[⎕IO]
[4]    L←0,M⍴LOOP
[5]    →L[I]
[6]   LOOP:I←I-1
[7]    R[(B∧.=A[I;])/⍳N]←I
[8]    →L[I]
     ∇
```

The next two functions are similar to the functions `CMIOTA1`, `CMIOTA2`, and `CMIOTA3`, in that they convert the character matrices into numeric vectors so they can then apply dyadic `⍳`. However, the process for converting to numbers is less direct. First, each distinct character is mapped to a distinct number. For example, all As are mapped to 1s, Bs to 2s, Cs to 3s, and so on. Then the numbers from each row are packed into a single number. Here’s an illustration of the process on one row of a four-column matrix:

```apl
'FROG'  →  6 18 15 7  →  6181507
```

In this case, the numbers are packed by multiplying them by respective powers of 100 and adding:

```apl
(6×1000000)+(18×10000)+(15×100)+(7×1)
```

The functions `CMIOTA6` and `CMIOTA7` are generalized implementations of this concept. In `CMIOTA6`, the characters are converted to number by determining their index into `⎕AV`, each character is translated into a number between 0 and 255 (its origin 0 index into `⎕AV`). The resulting numbers are packed by multiplying by powers of 256.

```apl
     ∇ R←A CMIOTA6 B;⎕CT
[1]   ⍝ Pack chars into numbers using
[2]   ⍝ ⎕AV (max 6-7 cols)
[3]    ⎕CT←0
[4]    R←(256⊥(⎕AV⍳⍉A)-⎕IO)⍳256⊥(⎕AV⍳⍉B)-⎕IO
     ∇
```

There is a limitation to this approach. Since APL maintains a maximum of 16 or 17 significant digits for any number (that’s all you can hold in eight-byte floating point representation), you’ll start getting unreliable results when the number of digits exceeds 16 or 17. Since `256⍟1E17` is `7.06`, you shouldn’t rely on this method for matrices with more than seven columns. Even then, make sure you set `⎕CT` to 0 to utilise the full significance.

But, hey! If we use a smaller packing factor than 256, we can pack more columns into the 16 or 17 digits of significance. It’s not unreasonable to expect the character matrix arguments to contain only 20 to 30 different characters, not 256. Since `30⍟1E17` is `11.51`, a packing factor of 30 will allow you to use this packing method on matrices with as many as 11 columns. In `CMIOTA7`, the two arguments are initially analysed to determine the list of distinct characters they use. The arguments are then translated to origin 0 indices into the distinct list, and the length of the list is used as the packing factor.

```apl
     ∇ R←A CMIOTA7 B;C;N;⎕CT
[1]   ⍝ Pack chars into nums using distinct
[2]   ⍝ chars (max 6-15 or so columns)
[3]    ⎕CT←0
[4]    N←⍴C←⎕AV~(⎕AV~A)~B ⍝ Chars used
[5]   ⍝ N←⍴C←((⎕AV∊A)∨⎕AV∊B)/⎕AV ⍝ Ditto
[6]    R←(N⊥(C⍳⍉A)-⎕IO)⍳N⊥(C⍳⍉B)-⎕IO
     ∇
```

The next two functions offer the maximum in elegance. Like `CMIOTA4` and `CMIOTA5`, they use inner product to compare the rows of their arguments. Unlike `CMIOTA4` and `CMIOTA5`, they do so without looping. All rows are compared at once. The “mismatch” inner product (`∨.≠`) is used instead of “match” (`∧.=`) for convenience, and the “leading” scan (`∧\`) and the “how many” reduction (`+/`) are used on the resulting Boolean matrix to count the number of mismatched rows before the first matching row.

```apl
     ∇ R←A CMIOTA8 B
[1]   ⍝ Inner product; transpose right arg.
[2]    R←⎕IO++⌿∧⍀A∨.≠⍉B
     ∇

     ∇ R←A CMIOTA9 B
[1]   ⍝ Inner product; transpose left arg.
[2]    R←⎕IO++/∧\B∨.≠⍉A
     ∇
```

The differences between these two functions are the choice of argument to be transposed, and the choice of axis across which to scan and reduce.

Though elegant in their concise expressiveness, these two algorithms suffer from two weaknesses. First, all the rows of the left argument are compared to all the rows of the right argument. The algorithms aren’t smart enough to stop when they find the appropriate match. Second. The result of the inner product is a Boolean matrix with as many elements are the PRODUCT of the number of rows in the two arguments. The matrix can get pretty big, sometimes big enough to generate a `WS FULL` error message.

The next function, `CMIOTA10`, is the most obscure. It relies on grade-up (`⍋`) to perform the comparisons between the two arguments. By catenating the arguments row-wise, grading the catenated matrix, and analysing the resulting grade vector, the desired `CMIOTA` result is constructed. Since grade-up is generally quite efficient compared to other searching algorithms, `CMIOTA10` promises to give the other functions a run for their money. Its only real disadvantage is its greater number of steps. For small arguments, the greater amount of interpretation is likely to eat up the savings from its more efficient algorithm.

```apl
     ∇ R←A CMIOTA10 B;I;G;N;S
[1]   ⍝ Gread-up char mats, using ⎕AV.
[2]    G←⎕AV⍋S←A,[⎕IO]B
[3]    S←S[G;]
[4]   ⍝ Flag 1st of distict rows by shift
[5]   ⍝ and compare:
[6]    S←∨/S≠¯1⊖S
[7]   ⍝ Ensure 1st elt is 1 (in case all
[8]   ⍝ rows the same):
[9]    S[⎕IO]←1
[10]  ⍝ Indices of 1st distinct rows:
[11]   I←S/G
[12]  ⍝ Replicate for each like row:
[13]   S[⎕IO]←⎕IO
[14]   I←R←I[+\S]
[15]  ⍝ Unsort inds (to catenated order):
[16]   R[G]←I
[17]  ⍝ Keep those corresp to right arg
[18]  ⍝ and set 'not found' inds to
[19]  ⍝ 'one greate than length':
[20]   N←(⍴A)[⎕IO]
[21]   R←(N↓R)⌊N+⎕IO
     ∇
```

The final two functions use nested array approaches. Therefore, they require implementations of APL that support nested arrays. `CMIOTA11` works in any version of APL\*PLUS that supports nested arrays, the notable exception being APL\*PLUS PC. `CMIOTA12` works in APL2. The approach of both functions is the same: convert the matrix arguments into nested vectors of character vectors. Each row become one item in the resulting nested array. Then, use dyadic `⍳` on the two vector arguments. Since dyadic `⍳` has been extended to compare items of nested arrays, you get the desired result directly.

```apl
     ∇ R←A CMIOTA11 B
[1]   ⍝ Uses APL*PLUS nests
[2]    R←(↓A)⍳↓B
     ∇

     ∇ R←A CMIOTA12 B
[1]   ⍝ Uses AP2 nests
[2]    R←(⊂[1+⎕IO]A)⍳⊂[1+⎕IO]B
     ∇
```

The comparative timings are tabulated in detail on the Vector web page. The point of these timings is to illustrate the KIND of effects you can expect to see as you vary the size of the arguments and as you move from one implementation of APL to another. Do you own timings if important.
