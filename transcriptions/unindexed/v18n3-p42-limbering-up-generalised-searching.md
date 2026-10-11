---
title: 'Limbering Up: Generalised Searching'
authors:
- Gary A. Bergquist
volume: '18'
issue: '3'
page: '42'
unindexed: true
transcribed: 'from page images of VOL.18-NO.3-JANUARY-2002.pdf, pages 44–47 (printed 42–45; follows art10014410); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. The solutions are reprinted in 18:4 (art10014390). The reprint note at the foot of p.45, which closes the extract, is included here."
- "`CMIOTA` was run in Dyalog APL as a check on the transcription; it returns `2 5 1` for the printed example. The same function is listed again, as `CMIOTA1`, in 19:1 (art10014370)."
- "The e-mail address printed with Vector Production’s postal address is the organisation’s, and is kept. Kept as printed: `⎕vr'CMIOTA'` (lower-case `vr`); “whether the upper of lower limits”."
---

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

In a previous issue of the Zark APL Tutor News, we developed a number of functions for searching through the rows of a character matrix for the first occurrence of each row of another matrix. Different algorithms excelled in different circumstances. However, one algorithm stood above the rest when used on large arguments.

In case you missed that issue, here’s a listing of the function:

```apl
      ⎕vr'CMIOTA'
     ∇ R←A CMIOTA B;G;J;K;N;S;T;Z
[1]   ⍝ Returns row indices of character
[2]   ⍝ matrix A where each row of B is
[3]   ⍝ found. Like dyadic ⍳, CMIOTA re-
[4]   ⍝ turns one greater than the largest
[5]   ⍝ index in A for rows of B not found.
[6]   ⍝
[7]   ⍝ Index returned if not found:
[8]    Z←⎕IO+1↑⍴A
[9]    N←1↑⍴B ⍝ No. rows in B
[10]  ⍝ Stick ¯1↑⎕AV as new row of A:
[11]   A←A,[⎕IO]⎕AV[255+⎕IO]
[12]   G←⎕AV⍋B,[⎕IO]A ⍝ Grade vec
[13]  ⍝ Which ones come from B (∧/K∊⍳N):
[14]   K←(S←G<N+⎕IO)/G
[15]  ⍝ The relative ind of the next A row:
[16]   J←⎕IO+S/+\T←~S
[17]   R←J←(T/G)[J]-N ⍝ The absolute A inds
[18]   R[K]←J ⍝ ...in the orig order of B
[19]  ⍝ Use the "not-found" value for those
[20]  ⍝ not matching:
[21]   R[(∨/B≠A[R;])/⍳N]←Z
     ∇
```

The function is named `CMIOTA` (Character Matrix IOTA) because of its similarity in syntax with the primitive dyadic APL function `⍳` (iota). For example:

```apl
      38 42 75 84 ⍳ 42 15 38
2 5 1
      (4 3⍴'REDBOYCANSIT') CMIOTA (3 3⍴'BOYWASRED')
2 5 1
```

Each function searches through the items (elements or rows) of its left argument for the first occurrence of each item (element or row) of its right argument. The result has one index per item of the right argument, telling where in the left argument the item was first located. If the item of the right argument is not found in the left argument, the corresponding number in the result is the index just beyond the last item of the left argument. In origin 1, that "not-found" index is one more than the number of items in the left argument. In origin 0, it’s the number of items.

In this issue, we’re going to suggest another way to view APL’s searching capability. Instead of saying, "`⍳` returns the index in the left argument where the items of the right argument are first *found*," let’s say, "`⍳` returns the index in the left argument where the items of the right argument are first *equal*." Stated this way, searching sounds more like an *operator* than a *function*. After all, there’s a function (`=`) involved.

Just as the reduction (`/`) operator requires a function operand (such as `+/` or `×/` or `⌈/`), perhaps the searching operator should also require an operand (such as `=⍳` or `>⍳` or `<⍳`). Unfortunately, this notation conflicts with the existing definition of monadic `⍳` (as in, `3 4 5=⍳3`). This conflict doesn’t bother us a whole lot, because we’re not really suggesting a new operator. We’re suggesting a new way to look at searching. For now, to avoid the ambiguity, we’ll slap the operator and operand in parentheses, like so:

```apl
      38 42 75 84 (=⍳) 42 15 38
2 5 1
```

This is the "where is it first equal" function. Let’s try a different relational function:

```apl
      10 20 35 50 (≤⍳) 12 57 35
2 5 3
```

This is the "where is it first less than or equal" function. The result contains 1 ( in origin 1) for each number of the right argument less than or equal 10, 2 for each number greater than 10 but less than or equal 20, 3 for each number greater than 20 but less than or equal 35, and so on. In more concise notation:

```apl
1 if    X≤10
2 if 10<X≤20
3 if 20<X≤35
4 if 35<X≤50
5 if 50<X
```

Notice the index `5` is returned for any corresponding number in the right argument that is not less than or equal any of the numbers of the left argument. Like dyadic `⍳`, the result contains indices of the left argument, or one greater than the largest index if the corresponding element of the right argument does not belong to any of the defined sets.

Let’s try (`<⍳`):

```apl
      10 20 35 50 (<⍳) 12 57 35
2 5 4
```

This is the "where is it first less than" function. It returns indices according to the following scheme:

```apl
1 if    X<10
2 if 10≤X<20
3 if 20≤X<35
4 if 35≤X<50
5 if 50≤X
```

This scheme is similar to that of (`≤⍳`). The difference lies in whether the upper of lower limits of the ranges are inclusive. In the case of (`≤⍳`), the upper limits are inclusive; for (`<⍳`), the lower limits are inclusive.

These functions, (`≤⍳`) and (`<⍳`), if available, would be quite useful in a number of applications. We’ll discuss some of these in the next issue of the Tutor News.

In the meanwhile, your task is to implement one or both of the functions `LEIOTA` and `LTIOTA` to emulate (`≤⍳`) and (`<⍳`) respectively:

```apl
      10 20 35 50 LEIOTA 12 57 35
2 5 3
      10 20 35 50 LTIOTA 12 57 35
2 5 4
```

Try to make the functions as efficient as possible, especially when the right argument is long. The function does not need to work properly for non-vector right arguments or for left arguments that contain duplicates or are not in ascending order. However, if you do handle these cases, without forsaking efficiency, you’ll win a special prize (our admiration, and that of our readers). Naturally, comments are a welcome surprise.

Send your solutions to:

> Vector Production<br>
> Brook House<br>
> Gilling East<br>
> York YO62 4JJ<br>
> UK email apl385@compuserve.com

The notable functions and their authors’ names will be printed in the next issue of *Vector*. Good luck and happy limbering.

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA.*
