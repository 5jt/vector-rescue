---
title: 'Limbering Up: Comma-Delimited Data'
authors:
- Gary A. Bergquist
volume: '17'
issue: '2'
page: '31'
unindexed: true
transcribed: 'from page image of VOL.17-NO.2-OCTOBER-2000.pdf, page 33 (printed 31; within Zark Newsletter Extracts, after “Utility Corner: Matrix Searching”); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- data and files
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles; printed as “Limbering Up: Comma-Delimited Data”. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. The reprint note at the foot of the page, which closes the extract, is included here. The solutions follow in 17:3 (unindexed/v17n3-p28-utility-corner-comma-delimited-data.md)."
- "The postal address for solutions is Vector Production’s, and is kept."
- "Kept as printed: “Each of these records contain three values of “fields””."
---

When working with data from “external” (non-APL) applications, you need the ability to accept the data in a form comprehensible to both parties (you and them). One such form is the “comma-delimited file.” The values in a comma-delimited file are separated by commas. The records are typically separated by a newline character (carriage return).

Here’s a sample:

```text
26,154.25,Fred
722,14.95,Jane
17,0,Bob
```

Each of these records contain three values of “fields” of information.

Here’s your task: Given a comma- and newline-delimited character vector (newline at the end of each record), return a character matrix with the values realigned so they may be readily extracted via column-indexing. Like so:

```text
26 154.25Fred
72214.95 Jane
17 0     Bob
```

The function (call it `COMMA∆MAT`) should also return the global integer vector `fieldwidths` to tell you how wide the realigned fields are (`3 6 4` in this case).

Write the fastest `COMMA∆MAT` you can muster and mail your solution on paper or APL\*PLUS PC or APL\*PLUS II disk to:

> Vector Production<br>
> Brook House, Gilling East<br>
> YORK YO62 4JJ UK

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA*
