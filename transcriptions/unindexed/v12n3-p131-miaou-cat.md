---
title: Miaou = Cat!
authors:
- Claude Henriod
volume: '12'
issue: '3'
page: '131'
unindexed: true
transcribed: from page images of VOL.12-NO.3-JANUARY-1996.pdf, pages 133–134 (printed 131–132; follows art10010120); Claude, 2026-10-03
review: draft
---

From: Claude Henriod, December 1995
{ .byline }

Teachers have known for years that from earliest youth one must learn the right word. One calls a cat, a cat.

It ought to be the same with languages in information technology, but it isn’t always so. I want to give a simple example drawn from *Vector* Vol 12 No 1 page 88.

The vector `Q` is formed of three numbers:

```
Q←⎕AI[2] ⋄ <SOME CODE> ⋄ Q←Q,⎕AI[2] ⋄ <SOME CODE> ⋄ Q←Q,⎕AI[2]
```

In the setting of my example I’m not debating the choice of assignation but what follows:

```
Q[2]-Q[1] ⋄ Q[3] - Q[2]
```

This is the difference between two scalars. Basic, Fortran, C and other languages are capable of doing this sum.

On the other hand APL can do better: the difference between two items from the same vector:

```
-/ Q[2 1]
```

or, to be complete,

```
-/ Q[2 2 ⍴ 2 1 3]
```

APL2 from IBM (and other APLs) can do these two sums with a simple operator:

```
¯2 -/Q
```

THINK. It takes hardly any effort to think of `Q` as a set of values as distinct from some scalars in a variable. Even in as simple an example as presented here, the latter will never be programmed well in APL.

*I deplore the logic of APL\*PLUS III which introduced structure, because it makes it easy to program treating variables as scalars, as in Fortran.*

P.S. I leave you the surprise of comparing execution times on your machine with your interpreter. (On my 66MHz PS2 with IBM’s APL2 the vector version takes a quarter of the time.)
