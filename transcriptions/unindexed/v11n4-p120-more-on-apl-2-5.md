---
title: More on APL 2.5
authors:
- I Phelphritt (nee Leigh)
volume: '11'
issue: '4'
page: '120'
unindexed: true
transcribed: 'from page images of VOL.11-NO.4-APRIL-1995.pdf, page 122 (printed 120; within Technical Correspondence, after “Namespaces and ⎕SE”, before art10001850); Claude, 2026-10-11'
review: draft
tags:
- humour
- language design
queries:
- "An April Fool: dated 1st April 1995, from “I Phelphritt (nee Leigh)”, on a fictitious IBM APL2.5 reviewed in a nonexistent “April’s Vector 6-4”. The author’s name is kept as printed; the real writer is not identified."
- "The operator body is printed in small italics as “ωβ”; the second glyph looks like a Greek beta, but it is very small and the reading is uncertain."
- "Kept as printed: the last example shows the result 2 above the input line ⎕DL INV 2, and the input is indented less than the others."
---

*From: I Phelphritt (nee Leigh), 1st April 1995*
{ .byline }

I was thrilled to see your review of IBM’s APL2.5 in April’s Vector 6-4, and felt moved to send you a further couple of examples. One consequence of the direct definition of operators which may not be immediately obvious, is the ease with which you can define the inverse operator for monadic functions:

```apl
INV: ωβ
```

`INV` produces a derived function which reverses the effect of its operand:

```apl
A←→F INV F A
```

for any array *A* and any monadic function *F*. The following examples show the power of this operator.

```apl
          ÷4
0.25
          ÷INV 0.25
4
          +\INV 1 3 6
1 2 3
```

In the case where the inverse is not simple, the system provides a ‘least squares’ solution:

```apl
          +/INV 6
6
          ?INV 4
7
```

and of course, `INV` may take a system function as its operand, so:

```apl
          ⎕EX INV 1
FOO
```

… re-instates a previously expunged function, and:

```apl
2
     ⎕DL INV 2
```

… produces the same effect as `⎕DL ¯2` in Dyalog APL.

We are only now beginning to appreciate the power of this new implementation, but I’m sure that such examples will soon swell our idiom libraries.
