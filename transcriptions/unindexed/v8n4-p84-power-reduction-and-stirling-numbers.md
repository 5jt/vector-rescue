---
title: Comments on Power Reduction and Stirling Numbers
authors:
- Ken Iverson
volume: '8'
issue: '4'
page: '84'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, pages 86–88 (printed 84–86; within Featuring j, after Comments on J Questionnaire); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "A letter, From: Ken Iverson, January 12, 1992, on two papers in the October Vector (Parkhouse on power reduction; Appleton on Stirling numbers). It is signed “Roger Hui & Ken Iverson”; their postal address under the signature is omitted. It ends with an editor’s note."
- "The J is the 1992 dialect (version 4.1x2), kept as printed. Where the print sets two displays side by side (a and b; x vm c and the sums), they are set one after the other here."
- "In “Appleton’s result is given by }.}.\"S1” the brace glyphs are hard to read in the print; read as }. (behead)."
---

*From: Ken Iverson, January 12, 1992*
{ .byline }

I would like to comment on two papers in the October issue of Vector.

I believe that the point of the limits observed by Parkhouse might be clarified by the observation that if repeated application of a function `g` converges to a limit `y`, then `y` is the solution of the equation `y = g y`. In J, experimentation with this can be expressed using the *power conjunction* (dyadic operator) `^:`, and the corresponding *adverb* (monadic operator) `lim=. ^:_` for the limiting case of infinite power.

Thus:

```j
   cos=. 2&o.
   i=. 0 1 2 3 4 5
   cos^: i 1
1 0.540302 0.857553 0.65429 0.79348 0.701369
   lim=. ^:_
   ]y=. cos lim 1
0.739085
   y=cos y
1
   g=. 1.3&^
   g^:i 1
1 1.3 1.40646 1.44629 1.46149 1.46733
   g lim 1
1.47099
   g lim 1 0 _1 0j1
1.47099 1.47099 1.47099 1.47099
```

In his *Numerical Methods for Scientists and Engineers* (McGraw-Hill, 1962), R. W. Hamming introduces Stirling numbers in order to relate the coefficients `c` of a polynomial (expressed in J as `+/c*x ^ i.#c`) and the coefficients `cf` of a *factorial* polynomial.

If `k` is zero, the product over `x` plus `k` times iota `n` is equivalent to `x` to the power `n`; if `k` is negative *one*, it is Hamming’s factorial function. Moreover, if `c` is the vector of coefficients of an ordinary polynomial and `cf` the coefficients of an equivalent factorial polynomial, then `cf` is given by the matrix product of `S2` and `c`, where `S2` is the matrix of Stirling numbers of the second kind. In J, the *fit* conjunction `!.` produces a “variant” function; in particular, the function `^!._1` is Hamming’s factorial.

Although Hamming says “There is no simple formula for the Stirling numbers ...”, the relations outlined above lead to an expression of the form `b` times the inverse of `a`, where `a` is a Vandermonde matrix, and `b` is the corresponding “Vandermonde matrix” for the factorial polynomial. In J, the matter may be expressed as follows:

```j
    vm=. ^!. 0/ i.@#
   fvm=. ^!._1/ i.@#
   x=. 2 3 4 [ c=. 1 5 10 10 5 1

   x vm c
1 2  4  8  16   32
1 3  9 27  81  243
1 4 16 64 256 1024

   (x vm c) +/ . * c
243 1024 3125
   (x+1)^5
243 1024 3125
```

```j
   i=. i. 6
   a=. i vm i
   b=. i fvm i
   a
1 0  0   0   0    0
1 1  1   1   1    1
1 2  4   8  16   32
1 3  9  27  81  243
1 4 16  64 256 1024
1 5 25 125 625 3125

   b
1 0  0  0   0   0
1 1  0  0   0   0
1 2  2  0   0   0
1 3  6  6   0   0
1 4 12 24  24   0
1 5 20 60 120 120

   S1=. b %. a
   clean=. ".@(0&":)
   clean S1
1 0  0  0  0   0
0 1 _1  2 _6  24
0 0  1 _3 11 _50
0 0  0  1 _6  35
0 0  0  0  1 _10
0 0  0  0  0   1

   S2=. %. S1
   cf=. S2 +/ . * c
   cf
1 31 90 65 15 1
   (x fvm cf) +/ . * cf
243 1024 3125
```

The matrices `S1` and `S2` are Stirling numbers of the first and second kinds. Since Abramowitz and Stegun (and consequently Appleton) do not include the leading row and column, Appleton’s result is given by `}.}."S1`. This formulation does not provide transformation of the constant term which, of course, remains the same in the two types of polynomial. Finally, functions to generate the Stirling numbers (as function of the order) are defined by:

```j
ST2=. %.@ST1=. %./@(0 1&|:@(^!._1 0/~@i.))
```

Roger Hui & Ken Iverson

*Ed: The J is version 4.1x2, dated 11 January 1992.*
