---
title: The Dangers of APL RISC programming ...
authors:
- Bob Bykerk
volume: '7'
issue: '1'
page: '112'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 114–115 (printed 112–113; within Technical Correspondence, after Hackers Corner: Lots More VGA Colours); Claude, 2026-10-11'
review: draft
tags:
- development practice
- programming techniques
queries:
- "The first letter under the Technical Correspondence heading (p.112), From: Bob Bykerk, 5 Feb 1990. It replies to Gérard Langlet’s “APL ‘RISC Programming Style’” in Vector 6.2 (art10004630). It is followed on p.113 by E.E. McDonnell’s “VCAT in Sharp APL” (unindexed/v7n1-p113-vcat-in-sharp-apl.md)."
- "The writer’s postal address (c/o Sydney APLUG, a post office box in Sydney) is omitted."
- "The words set in bold in print (“being pedantic”, “trying to reduce”, “may”) are kept bold."
- "Kept as printed: “Risc”; “Gerard” without accent."
---

*From: Bob Bykerk, 5 Feb 1990*
{ .byline }

The article by Gerard Langlet on APL Risc programming (Vector 6.2) created the impression that Gerard does not program in the real world. His argument is loosely strung together and not adequately supported by example. Translated, his argument reads something like this:

> Here is a function which works on homogeneous data.  
> Here is my way of writing it without GOTOs, locals, or matrices.  
> Therefore, the use of GOTOs, locals and matrices is not good practice.  
> I have written thousands of these functions, so the above must be true.

The example is useful for homogeneous data, and would not require any data structure other than a vector anyway. It merely shows an alternative, shorter solution to the problem, and does not even demonstrate any tangible benefits, e.g. efficiency. Surely he could have used an example derived from one of his thousands of functions which would demonstrate how a problem dealing with heterogeneous data could be more easily solved by stripping out the structure and converting the data to a series of vectors?

I feel that **being pedantic** about eliminating GOTOs is a useless exercise, especially when structured code can easily be written (to flow from top to bottom, without spaghetti) using them. Sure, **trying** to **reduce** the number of GOTOs **may** reveal a more elegant and efficient solution, but the use of GOTOs for special casing, taking into account particular properties of the data, eliminating redundancies, or selecting only relevant parts of the data often reveal solutions that are many times faster than non-branching solutions. String searching as developed in the *Collected Whizzbangs* texts is a good example of this.

His idea of not using locals is fundamentally wrong. Not only does it mean that multi-line functions will almost invariably not be restartable, but they also become unreadable, and consequently a nightmare to debug. Local variables are used to store intermediate results. These are most useful for debugging, as one can see the results of all major transformations up to any point in a function, enabling one to retrace one’s steps. That way you don’t burn your bridges.

Vectors are great for data without structure, unless you want the overhead of partitioning or enclosing. Matrices or higher dimensional arrays are ideal for mimicking structure inherent in business operations, and there are many primitives in APL which naturally and optimally manipulate this type of data. These data structures mirror the way that one would view the information, e.g. sales data in 3 dimensions - salesman × month × year would be seen as pages of sales data, one page per year. A complete analysis can be done on this data without breaking it into vectors, so why entertain the idea?

To conclude, I think that the ideas Gerard presented are on the whole quite worthless until he backs them up with substantial examples. These ideas, if presented to beginners in APL could severely warp the process of learning a healthy coding style.

Bob Bykerk
