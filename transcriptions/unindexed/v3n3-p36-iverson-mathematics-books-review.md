---
title: Applied Mathematics for Programmers and Mathematics and Programming – Ken Iverson
authors:
- Simon Garland
volume: '3'
issue: '3'
page: '36'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 38–40 (printed 36–38; Romilly Cocking’s review of Peelle follows on p.38); Claude, 2026-10-12'
review: draft
tags:
- reviews
- mathematics and statistics
- education
queries:
- "Printed under the page heading “Book reviews”: “Applied Mathematics for Programmers (157 p) / Mathematics and Programming (132 p) / by Kenneth E. Iverson / Published by I P Sharp Associates, 1986. / Reviewed by Simon Garland”."
- "Code transcribed glyph by glyph as printed. In the brute-force example, line [11] has an unmatched closing parenthesis, “(rvρ1020))”, and the final line reads “(n∘.=v)+.×F n”; both kept as printed. The ⍝ lines of LEV and DEX print the symbols ⊢ and ⊣ as comments."
- "Kept as printed: “undertanding”; “(exercise -1)” with a hyphen; “C.A.Hoare”."
---

*Reviewed by Simon Garland*
{ .byline }

**Applied Mathematics for Programmers** (157 p)  
**Mathematics and Programming** (132 p)  
*by Kenneth E. Iverson*  
*Published by I P Sharp Associates, 1986.*

Both of these new self study courses from Dr. Iverson use an executable notation, that is (as he explains in the introduction to *Mathematics and Programming*) . . a notation whose rules are so strict and simple that a reader, or computer, can interpret any expression unambiguously.

The executable notation used is APL, as defined in *A Concise Dictionary of APL* (also available from I.P.Sharp). No prior knowledge of the notation is assumed, it is introduced clearly and simply as required – in refreshing contrast to the usual half apologetic jokes about strange symbols and unreadable one-liners.

In order to be able to use the course texts easily the reader should have access to a union keyboard version of APL and a copy of a direct definition workspace that uses the

FunctionName : ElseExpression : IfCondition : ThenExpression

form of definition.

As far as I could tell all examples could be executed without problem (apart from the response time..) with the current version of Sharp APL/PC. APL\*PLUS/PC users will not be able to use any of the expressions using Sharp enhancements like the rank operator, or enclosed arrays, but they can still execute most of the expressions without much problem by simply replacing the lev and dex symbols by the functions:

```apl
    ∇ Result←Result LEV Junk
[1]  ⍝ ⊢
    ∇

    ∇ Result←Junk DEX Result
[1]  ⍝ ⊣
    ∇
```

Better still make the direct definition compiler do it (exercise -1).

The aim of *Applied Mathematics for Programmers* is to make the mathematics involved in many of the basic tools of programming more accessible to programmers – to enable them to grasp the concepts behind the tools they use.

Anyone who has had to sit through a lecture on how quicksort works, complete with helpful diagrams, examples, handwaving, and the exhortation that it’s all very simple will appreciate the power of a concise executable notation that allows the student to experiment with the simple functions:

```apl
Sort: (B/⍵),Sort(~B←⍵=⌊/⍵)/⍵ : 0=⍴⍵ : ''

QS: (QS(⍵<F)/⍵) , ((⍵=F)/⍵) , (QS(⍵>F)/⍵)⊣F←1↑⍵ : 0=⍴⍵ : ''
```

*Mathematics and Programming* is more a review of high school mathematics using an executable notation, which exposes and clarifies relations among topics previously studied in isolation; it also goes into more detail about the notation and its ‘grammar’.

Both courses go over similar ground, but with different emphasis. They cover classifications and sets, the behaviour of elementary functions (utility functions are supplied for drawing graphs and barcharts to assist with the exploration of the behaviour of the functions), directed graphs and trees, identities and proofs, and modelling (including writing your own computer). Exercises to check and extend undertanding of the points under discussion are provided at the end of the book, with indicators within the text when an exercise is available.

*Applied Mathematics for Programmers* has a special section on manual translation with examples of translation to Pascal, C, Fortran, and Conventional Mathematical Notation, closing with a discussion on general translation techniques. This chapter is an example of the attitude that permeates the whole course – no messianic preaching APL to the masses, just a demonstration of how useful it is to be able to translate ideas into a concise clear notation to help with the understanding and communication of concepts – if a program works in Fortran then fine, don’t touch it, but perhaps it would be easier to document the essential algorithm in something less cumbersome.

*Mathematics and Programming* has a special section on co-ordinate geometry – I didn’t find this as interesting, but I’ve probably been scarred for life by not having courses like this one. . .

Although these books are meant as course texts I think most APL users could profit from a careful study of the examples. Consider for example one of the identities discussed under Efficiency in the chapter on Identities and Proofs in *Applied Mathematics for Programmers*; the problem is the common one of applying an expensive function F to a vector of non-distinct values v. The brute force solution (any mistakes in the normal APL examples are my fault) is something like:

```apl
...
[10]      r←(rv←⍴v)⍴0
[11]     →lc←(rv⍴1020)),1022⊣i←1
[12]1020: r[i]←F v[i]
[13]1021:→lc[i←i+1]
...
```

Of course we could ‘optimise’ this considerably to:

```apl
...
[42]      r←(rm←1⍴⍴msk←(uv←Nub v)∘.=v)⍴0
[43]      cols←⍳0⊥⍴msk
[44]     →lc←(rm⍴1030),1032⊣i←1
[45]1030: r[msk[i;]/cols]←F uv[i]
[46]1031:→lc[i←i+1]

    (Nub: ((⍳⍴⍵)=⍵⍳⍵)/⍵)
...
```

but with a little more thought we could have written it much more clearly from the beginning (if it’s not clear then try it out!):

```apl
...
[1] r←(n∘.=v)+.×F n←Nub v
    ∇
```

Most of all I would hope that those responsible for teaching programming (not just those responsible for teaching APL..) or mathematics would take the time to look carefully at these texts with a terminal nearby – I’m certain that students would approach such courses with much more enthusiasm than a standard lecture oriented course.

Finally a quote from C.A.Hoare, reported in the August 1986 edition of BYTE magazine:

> “Many programmers of the present day have been educated in ignorance and fear of mathematics. Of course, many programmers are mathematical graduates who have acquired a good grasp of topology, calculus and group theory. But it never seems to occur to them to take advantage of their mathematical skills to define a programming problem and search for its solution.
>
> “Our present failure to recognize and use mathematics as the basis for a programming discipline has a number of notorious consequences. They are the same as you would get from a similar neglect of mathematics in drawing maps, marine navigation, bridge building, air-traffic control, and exploring space.”
