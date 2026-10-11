---
title: Stirling numbers by recursion
authors:
- Norman Thomson
volume: '8'
issue: '1'
page: '95'
unindexed: true
transcribed: 'from page images of VOL.8-NO.1-JULY-1991.pdf, page 99 (printed 95; within Technical Correspondence, the first letter, before Working with Windows); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- programming techniques
queries:
- "Untitled in print: a letter, “From: Norman Thomson, 20 May 1991”, the first under the Technical Correspondence heading; the title is ours. It answers David Appleton on Stirling numbers of the second kind in Vector 7.4."
- "The writer’s business address (IBM UK Laboratories Ltd, Hursley Park) is printed after the signature; the postal address is left out here."
- "The functions use a cover function IF, not shown. Kept as printed: ST1 [2] reads `(¯,N)↑`, a high minus with no number after it (probably `¯1`)."
---

*From: Norman Thomson, 20 May 1991*
{ .byline }

David Appleton in his article on generating Stirling Numbers of the second kind (Vol.7 No.4) concludes that it may be appropriate to use the recurrence relation:

\begin{equation*}
\sigma^{n}_{t} = n\,\sigma^{n}_{t-1} + \sigma^{n-1}_{t-1}
\end{equation*}

I agree, but surely the appropriate development is a recursive function, e.g. `ST0` below which generates the nth row of the table:

```apl
[0]   Z←ST0 N;T
[1]   →0 IF N=Z←1
[2]   Z←(¯1⌽T)+(⍳N)×T←(ST0 N-1),0
```

If the entire table is required, use

```apl
[0]   Z←ST1 N;T;U
[1]   →0 IF N=↑Z←1 1⍴1
[2]   Z←U,[1](¯1⌽T)+(⍳N)×T←,(¯,N)↑U←(ST1 N-1),0
```

which contains redundant zeros in its upper triangle but could trivially be transformed to David’s compressed table where Stirling rows are read as diagonals.

Norman Thomson<br>
IBM UK Laboratories Ltd
