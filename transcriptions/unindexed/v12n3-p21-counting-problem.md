---
title: Counting Problem
authors:
- Tony Goddard
volume: '12'
issue: '3'
page: '21'
unindexed: true
transcribed: 'from page images of VOL.12-NO.3-JANUARY-1996.pdf, pages 23–24 (printed 21–22; within The Education Vector, after Ian Clark’s introduction); Claude, 2026-10-11'
review: draft
tags:
- competitions and puzzles
- mathematics and statistics
- programming techniques
queries:
- "The byline prints the author’s e-mail address after his name; omitted here."
- "The functions assume index origin 0 (`⎕IO←0`), which the print does not state; run so, they reproduce the printed table (1 6 21 55 120 231) and the `D8 2` rows."
- "In the cycle-index formula the print shows the power sign in the typewriter font as `∧`; set here as `^`."
- "Kept as printed: “colouring of 2 x 2 tiles”; “vith” in the comment lines; “P[1] + P[2] ... + P[m]”; “Ok” (for O*k*); “G.Polya”."
---

*by Tony Goddard*
{ .byline }

Count different possible colouring of 2 x 2 tiles with n colours, given that rotated or flipped tiles are equivalent. The counts can be computed using two APL functions.

Firstly, define a function `D8` to generate all the rotations and flips of a tile, then define another function `C4T` to look at all of the n\*n\*n\*n tiles, and count only those which are distinct after all rotations and flips are taken into account.

```apl
   Z ← D8 N;P;Q
 ⍝ Eight rotations
  N ←(N,N)⍴⍳N × N
  Q ← ⌽P ← ⍉N ⋄ Q ←,Q ⋄ P ←,P
  Z ← N ← ⍳⍴P
  Z ← Z,N ← Q[N]
  Z ← Z,N ← Q[N]
  Z ← Z,N ← Q[N]
  Z ← Z,P
  Z ← Z,P ← Q[P]
  Z ← Z,P ← Q[P]
  Z ← Z,P ← Q[P]
  Z ←(8,⍴P)⍴Z
```

```apl
  Z ← C4T N;C;D;E;I4;J;K;N4;U
 ⍝ Colour 2x2 tile vith N colours
  I4 ← ⍳N4 ← N × N × N × N
  D ← D8 2
  U ← N4⍴0
  C ← 0
 AA:J ← U⍳0
  →(J ≥ N4)/XX
  C ← C+1
  E ←(4⍴N) ⊤ J
  K ← (4⍴N) ⊥ ⍉E[D]
  U[K]← C                    ⍝ all colourings equivalent to J
  → AA
 XX:Z ← C
```

```
  n  c(n)
  1    1          c(n) = t(t(n)) where t(n) is n th triangular number.
  2    6
  3   21          This looks plausible, but is it true ?
  4   55
  5  120          t(n)= n(n+1)/2
  6  231          t(t(n)) = (1/8) (nn+n)(nn+n+2)
  7  406                  = (1/8) (nn+n)(nn+n)+2nn+2n
  8  666                  = (1/8)  nnnn+2nnn+3nn+2n
  9 1035
 10 1540        & this is a polynomial in n, writing nn for n*n etc.
```

This problem was investigated by Polya. He found a formula, involving the cycle index of a group of permutations. Here the group is known as the dihedral group. It is the group of transformations of the square. The Cycle index is a sum over the elements of the group G:

```
S = (P[1] + P[2] ... + P[m]) / m
```

where m = |G| is the number of elements in G and each P[i] is a monomial in symbols X[1] X[2] ... X[n]. If an element g in G splits into disjoint orbits O1, O2, .. Ok, then it contributes a monomial which is a product from the set X[1], X[2], .. X[n] where an orbit of length k contributes a term X[k]. For example, the identity permutation contributes a term X[1] \* X[1] ... \* X[1] taken m times.

```
  D8 2     cycles
 0 1 2 3   (0)(1)(2)(3)    X1*X1*X1*X1
 2 0 3 1   (0231)          X4
 3 2 1 0   (03)(12)        X2*X2
 1 3 0 2   (0132)          X4
 0 2 1 3   (0)(12)(3)      X1*X1*X2
 2 3 0 1   (02)(13)        X2*X2
 3 1 2 0   (03)(1)(2)      X1*X1*X2
 1 0 3 2   (01)(23)        X2*X2
```

the cycle index sum is

```
P[G](X1,X2,X3,X4) = (1/8) X1^4 + 2 * X1^2 *X2 + 3*X2^2 + 2 * X4
```

A preliminary result of Polya’s theorem is that the number of distinct colourings of the configuration, given n colours is given by

```
|C| = P[G](n, n, ... n).
```

In this particular case, the count is:

```
|C| = (1/8) nnnn + 2nnn + 3nn + 2n
```

## References

1. Fred S. Roberts. *Applied Combinatorics.* Prentice Hall, 1984.
2. G.Polya. *Kombinatorische Anzahlbestimmungen für Gruppen, Graphen und Chemische Verbindungen.* Acta Math. 68 (1937) 145-254
