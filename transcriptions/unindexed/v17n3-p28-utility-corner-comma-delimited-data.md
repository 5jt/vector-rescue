---
title: 'Utility Corner: Comma-Delimited Data'
authors:
- Gary A. Bergquist
volume: '17'
issue: '3'
page: '28'
unindexed: true
transcribed: 'from page images of VOL.17-NO.3-JANUARY-2001.pdf, pages 30–34 (printed 28–32; within Zark Newsletter Extracts, after “Corrections and Clarifications”); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- data and files
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles; the solutions to the Limbering Up task set in 17:2 (unindexed/v17n2-p31-limbering-up-comma-delimited-data.md). The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. The reprint note on p.32 closes the Zark column; the “Vector Update” that follows it is transcribed separately (unindexed/v17n3-p32-vector-update.md)."
- "`COMMA∆MAT1`, `COMMA∆MAT2` and `COMMA∆MAT3` were run in Dyalog APL (with `⎕TC[2]` for the newline and `⎕ML←3`) as a check on the transcription; each gives the printed matrix and `fieldwidths` of `3 6 4`."
- "The bracketed widths over the vectors in the illustration on p.29 are printed as rules with the numbers set in them; they are drawn here with box-drawing characters."
- "Kept as printed: “whose value are aligned by field”, “Each of these records contain”, “We then time”; `<fieldwidths>` in angle brackets, and `Fieldwidths` capitalised in the display on p.28; in `COMMA∆MAT2` the comment “APL≠PLUS”, and “User biggest”; in `COMMA∆MAT3` the comment “fieldswidtghs”."
---

## Utility Corner: Comma-Delimited Data

(The purpose of this column is to make you more productive by introducing you to utility functions. Think of utility functions as APL functions that have names instead of symbols. By expanding your function vocabulary, you’ll be able to write APL code that’s more concise, more efficient, and more readable.)

In last issue’s LIMBERING UP column, we asked you to write a function named `COMMA∆MAT`. The function converts a character vector whose records are delimited by trailing newline characters (carriage returns), and whose fields within the records are delimited by commas, into a simple character matrix whose value are aligned by field.

Here’s a sample:

```text
26,154.25,Fred@
722,14.95,Jane@
17,0,Bob@
```

(We’ve used the `@` symbol to represent the newline character, so you can “see” it. The `@` symbol wasn’t included last issue, and we received a few solutions that assumed the initial array was a matrix. Not so. It’s a vector with embedded newline characters.)

Each of these records contain three values or “fields” of information. For this vector, here’s the desired result:

```text
26 154.25Fred
72214.95 Jane
17 0     Bob
```

The `COMMA∆MAT` function should also return a global vector named `<fieldwidths>`, whose elements are the respective widths of the fields in the matrix. In this case,

```apl
      Fieldwidths
3 6 4
```

This vector allows you to readily extract a field from the matrix result. For example, if the matrix is named `CM`, you can get the `I`th field via:

```apl
CM[;(0,+\fieldwidths)[I]+⍳fieldwidths[I]]
```

When writing `COMMA∆MAT`, you need a way to squeeze out the unwanted commas and newlines, and to insert some well-placed blanks for proper re-alignment.

Bruce Frost sent a solution that uses compress (`/`) to do the squeezing and expand (`\`) to do the inserting:

```apl
     ∇ CM←COMMA∆MAT1 TEXT;D;E;I;L;NL;R;⎕IO
[1]    ⎕IO←1 ⍝ Origin 1 works fine
[2]    NL←⎕TCNL ⍝ APL*PLUS newline char
[3]   ⍝ NL←⎕TC[2] ⍝ APL2
[4]    R←+/TEXT∊NL ⍝ Number of records
[5]   ⍝ Bits and indices of delimiters:
[6]    I←(D←TEXT∊',',NL)/⍳⍴TEXT
[7]    TEXT←(~D)/TEXT ⍝ Squeeze them out
[8]    L←I-1,1+¯1↓I ⍝ Lengths of segments
[9]    L←(R,(⍴L)÷R)⍴L ⍝ ... as a matrix
[10]   fieldwidths←⌈⌿L ⍝ Biggest per field
[11]  ⍝ Build expansion vector:
[12]   I←⍳⌈/fieldwidths
[13]   E←(,((⍴L)⍴fieldwidths)∘.≥I)/,L∘.≥I
[14]  ⍝ Expand as needed, and reshape:
[15]   CM←(R,+/fieldwidths)⍴E\TEXT
     ∇
```

The logic is relatively straightforward up to line 13. On that line, two outer products are used to generate Boolean arrays that combine to generate the desired expansion vector. To illustrate the logic, consider the string `'Bob'` in the sample above. Note `<fieldwidths>` is `3 6 4` and the value of `L` is `3` for `'Bob'` (its length).

```apl
      ⌈/fieldwidths
6
      ⎕←I←⍳⌈/fieldwidths
1 2 3 4 5 6
      4≥I       ⍝ 4=width of last field
1 1 1 1 0 0
      3≥I       ⍝ 3=width of 'Bob'
1 1 1 0 0 0
      ─────6───── ─────6─────
      ───4───     ──3──
      1 1 1 1 0 0/1 1 1 0 0 0
1 1 1 0
```

The result, `1 1 1 0`, is the segment of the expansion vector that expands `'Bob'` into `'Bob '`.

Louis Zucchi’s solution is similar to Bruce’s but uses replicate (`/`) in place of compress and expand:

```apl
     ∇ CM←COMMA∆MAT2 TEXT;B;I;L;N;NL;R;⎕IO
[1]    ⎕IO←1 ⍝ Origin 1 works fine
[2]   ⍝ NL←⎕TCNL ⍝ APL≠PLUS newline char
[3]    NL←⎕TC[2] ⍝ APL2
[4]   ⍝ Indices of delimiters:
[5]    I←(TEXT∊',',NL)/⍳⍴TEXT
[6]    N←I⍳TEXT⍳NL ⍝ Number of fields
[7]    R←(⍴I)÷N ⍝ Number of records
[8]    L←¯1+I-¯1↓0,I ⍝ Lengths of segments
[9]    fieldwidths←⌈⌿(R,N)⍴L ⍝ User biggest
[10]   TEXT[I]←' ' ⍝ Blank out delimiters
[11]   B←(⍴TEXT)⍴1 ⍝ Replication vector
[12]  ⍝ Number of blanks needed per field:
[13]   B[I]←((R×N)⍴fieldwidths)-L
[14]  ⍝ Compress/expand, and reshape:
[15]   CM←(R,+/fieldwidths)⍴B/TEXT
     ∇
```

The key to this function is the replacement of the commas and newlines by blanks so they can be subsequently compressed (replicated 0 times) or expanded (replicated 1 or more times).

Gary Logan’s solution uses a nested APL2 approach:

```apl
     ∇ CM←COMMA∆MAT3 TEXT
[1]   ⍝ Use the newline to partition into
[2]   ⍝ a vector of char vec records:
[3]    CM←(TEXT≠↑1↓⎕TC)⊂TEXT
[4]   ⍝ Use commas to partition into a vec
[5]   ⍝ (recs) of vecs (flds) of char vecs:
[6]    CM←(CM≠',')⊂¨CM
[7]   ⍝ Disclose to a mat (recs by flds)
[8]   ⍝ of char vecs:
[9]    CM←⊃CM
[10]  ⍝ Enclose 1st dimension to get a vec
[11]  ⍝ (flds) of vecs (recs) of char vecs:
[12]   CM←⊂[⎕IO]CM
[13]  ⍝ Disclose each item to get a vec
[14]  ⍝ (flds) of mats (one row per rec):
[15]   CM←⊃¨CM
[16]  ⍝ Disclose gives each mat item the
[17]  ⍝ minimum no. of cols. How many?
[18]   fieldwidths←↑¨¯1↑¨⍴¨CM
[19]  ⍝ OR:- fieldswidtghs←(⊃⍴¨CM)[;1+⎕IO]
[20]  ⍝ Cat the mats together via reduction
[21]  ⍝ and disclose the scalar result:
[22]   CM←⊃,/CM
     ∇
```

If you’re not a daily user of nested arrays, this solution may be a bit perplexing. To help you understand the code, let’s illustrate the steps on the sample problem above.

Parentheses are included to give a better view of nesting.

```text
TEXT←     26,154.25,Fred@
          722,14.95,Jane@
          17,0,Bob@

[3]  (26,154.25,Fred) (722,14.95,Jane) (17,0,Bob)

[6]  ((26)(154.25)(Fred)) ((722)(14.95)(Jane)) ((17)(0)(Bob))

[9]   (26)    (154.25)  (Fred)
      (722)   (14.95)   (Jane)
      (17)    (0)       (Bob)

[12]  ((26)(722)(17)) ((154.25)(14.95)(0)) ((Fred)(Jane)(Bob))

[15]  (26        (154.25    (Fred
       722        14.95      Jane
       17 )       0      )   Bob )

[18]  3          6          4

[22]  26 154.25Fred
      72214.95 Jane
      17 0     Bob
```

Clearly, the approach of this function is entirely different from the approach of the first two functions. Which do you think is fastest?

We timed all three functions on an APL2 mainframe system. We used a character vector of length 63000 that defined 1000 records, each having ten fields. The fastest was `COMMA∆MAT2` (replicate), followed by `COMMA∆MAT1` (expand), which was 30% slower, and `COMMA∆MAT3` (nesting), which was 80% slower than `COMMA∆MAT2`.

We then time `COMMA∆MAT1` and `COMMA∆MAT2` on an APL\*PLUS II system. The difference there was more dramatic. `COMMA∆MAT2` (replicate) ran four times faster than `COMMA∆MAT1` (expand).

On the APL\*PLUS PC system, the character vector had to be shortened to 200 records (12600 characters) to avoid WS FULL from the outer products. At that size, `COMMA∆MAT1` (expand) ran five times slower than `COMMA∆MAT2` (replicate).

The winner: `COMMA∆MAT2`.

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA*
