---
title: 'Limbering Up: Generalised Searching'
authors:
- Gary A. Bergquist
volume: '18'
issue: '4'
page: '35'
unindexed: true
transcribed: 'from page images of VOL.18-NO.4-APRIL-2002.pdf, pages 37–39 (printed 35–37; follows art10014390); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- data and files
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. It is headed “Generalised Searching”, repeating the previous column’s title, though it sets the CROSSTAB (cross-tabulation) task; the solutions are reprinted in 19:1 (art10014370) under “Cross Tabulations”. The reprint note at the foot of p.37, which closes the extract, is included here."
- "The e-mail address printed with Vector Production’s postal address is the organisation’s, and is kept. The column headings of the table of records are underlined in print."
- "Kept as printed: “a bonus amout”; `R[3;;2]` (three indices for a rank-4 array); `I=1;` in CROSSTAB[13] (the other lines have `:`); “1-to1”; “(or millions) or records”; no full stop after “may be helpful”."
---

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

Suppose you have a "database" of employee information. For each of the 2000 employees, you have four items of information: age, state of residence, type of employee, and a bonus amout received last year.

Here are a few records:

```text
AGE  STATE  TYPE  BONUS
26    FL     E     200
39    MI     S     550
31    NY     O     720
52    NY     S     375
```

The information is stored in your APL workspace in four simple variables: `AGE`, `STATE`, `TYPE`, and `BONUS`. `AGE` and `BONUS` are 2000-element numeric vectors; `STATE` is a 2000-row, 2-column character matrix; and `TYPE` is a 2000-element character vector.

Your job is to summarise this mass of information by grouping the employees by age, state, and type. Complete the following function:

```apl
     ∇ R←CROSSTAB
[1]   ⍝ Summarises employee information
[2]   ⍝ stored in workspace globals AGE,
[3]   ⍝ STATE, TYPE, and BONUS.  AGE and
[4]   ⍝ BONUS are numeric vectors, STATE
[5]   ⍝ is a two-column character matrix,
[6]   ⍝ and TYPE is a character vector.
[7]   ⍝ Their elements/rows are in 1-to1
[8]   ⍝ correspondence.  R is a four-
[9]   ⍝ dimensional array whose shape is
[10]  ⍝ (5 10 3 2):
[11]  ⍝
[12]  ⍝  R[I;;;]  The Ith age range:
[13]  ⍝      I=1;   0≤AGE≤29
[14]  ⍝      I=2:  30≤AGE≤39
[15]  ⍝      I=3:  40≤AGE≤49
[16]  ⍝      I=4:  50≤AGE≤64
[17]  ⍝      I=5:  65≤AGE
[18]  ⍝ R[;J;;]  The Jth state.  The glo-
[19]  ⍝      bal ALLSTATES is a 10-row,
[20]  ⍝      2-column character matrix of
[21]  ⍝      the codes for all ten states
[22]  ⍝      in which the employees reside.
[23]  ⍝ R[;;K;]  The type 'EOS'[K]
[24]  ⍝ R[;;;1]  The employee count.
[25]  ⍝ R[;;;2]  The total bonus amount.
```

Here’s how this function can be used:

```apl
      R←CROSSTAB  ⍝ Summarise the data
```

The number of employees age 0 to 29, living in state `ALLSTATES[7;]`, with type `S`:

```apl
      R[1;7;3;1]
276
```

Their total bonus amount:

```apl
      R[1;7;3;2]
120474
```

Their average bonus amount:

```apl
      ÷/R[1;7;3;2 1]
436.5
```

The number of employees by type:

```apl
      +/[1]+/[2]R[;;;1]
802 460 738
```

The total bonus paid to ages 40 to 49:

```apl
      +/[1]+/[2]R[3;;2]
325120
```

The idea behind a function like `CROSSTAB` is to process the database once, summarising its information into a single multi-dimensional array. All subsequent analysis can then be easily and efficiently performed on the array, rather than reprocessing the thousands (or millions) or records.

Try to make the function as efficient as possible. Hint: the functions presented in the Utility Corner of this newsletter may be helpful

Send your solutions to:

> Vector Production<br>
> Brook House<br>
> Gilling East<br>
> York YO62 4JJ<br>
> UK email apl385@compuserve.com

The notable functions and their authors’ names will be printed in the next issue of *Vector*. Good luck and happy limbering.

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA.*
