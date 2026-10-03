---
title: 'Prize Competition: Matrix Numeric Validation'
authors:
- David Ziemann
volume: '1'
issue: '2'
page: '107'
unindexed: true
transcribed: 'from page images of VOL.1-NO.2-OCTOBER-1984.pdf, pages 109–110 (printed 107–108; art10005120 follows on p.109); Claude, 2026-10-03'
review: draft
queries:
- "In the VALIDNUMSV example the third number is printed `-1.1` in the argument but `¯1.1` in the result; probably the APL high minus in both, lost in typesetting. Transcribed as printed. The six results match the six blank-separated groups."
- "Slip transcribed as printed: “Our competition this issue to to write”."
- "The reference “VECTOR Vol.1 No.1 p.33” is printed so; the VI and FI functions it presumably means are in art10000550, printed pp.130–132."
---

by David Ziemann
{ .byline }

For the poor underprivileged souls who are forced to use APL interpreters that do not boast system functions such as ‘quad-VI’ and ‘quad-FI’ the problem of numeric validation is an important one. It is also relevant to those who wish to write standard-conforming code — the ISO APL standard will not include such niceties as these two system functions.

Typically, the problem is to verify a character vector which purports to contain valid numbers, where each potential number is separated by one or more blanks. The function VALIDNUMSV validates such a vector by returning a 2 column numeric matrix, as follows:

```
      VALIDNUMSV '3 1..1 -1.1   1A3 0 1E2 '
1    3
0    0
1   ¯1.1
0    0
1    0
1  100
```

Column one contains a 1 when the corresponding number has been validated successfully, and a 0 otherwise. (See VECTOR Vol.1 No.1 p.33 for clues on how to write such a function.)

However, with the increase in demand for full-screen applications the more natural approach is towards the validation of character matrices rather than character vectors. This is because the user is often required to enter numeric data into multi-row screen fields. It is normal to restrict the user to entering only a single number into each of the field rows.

Our competition this issue to to write an APL program that will perform numeric validation on a character matrix. The minimum requirements for the program are as follows:

1. It must correctly validate a character matrix, each row of which contains the representation of a single number.
2. It must provide the correctly converted numbers as well as an indication of which numbers were acceptable.
3. It must be possible to specify a validation code that restricts the set of acceptable numbers. For example:
    - 1 — 0 or 1 accepted only
    - 2 — whole number input only
    - 3 — whole or decimal numbers only
    - 4 — whole, decimal and E format numbers accepted
4. The program must conform to the first draft proposal for an ISO APL standard (don’t worry too much — if you assume VS APL and you’re not too indiscreet, the result should be acceptable).

Respondents should not feel dissuaded however, from exceeding these minimum requirements in any way.

The judges will consider the following criteria in making their decisions: usefulness, robustness, ease of use, generality, efficiency and elegance. The standard of the supplied descriptions of the facilities provided will also be taken into consideration.

A first prize of £30 (or equivalent) will be awarded to the author who, in the judges’ opinions, submits the best entry. Two commendation prizes of £10 each will additionally be awarded. The closing date for entries is 31st December 1984.

## Competition Rules

- Entries must be in legible English or APL as appropriate and should preferably be machine produced.
- The date and your full name and address should appear on each sheet of your entry.
- Entries should be physically separate from other contributions such as letters, and should be clearly marked ‘Competition Entry’.
- All submissions should be sent to the editor.
- Those on the committee, activities group or journal group of the British APL Association are ineligible.

## Prize Competition: This is your Life

Due to late distribution of the last issue, the winners of Prize Competition 1 will be announced in the next issue.
