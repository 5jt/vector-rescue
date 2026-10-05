---
title: 'Prize Competition: Wrap Up (with Competition Rules)'
authors:
- David Ziemann
volume: '2'
issue: '1'
page: '105'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 107 and 109 (printed 105 and 107; p.106 is a MetaTechnics advert; art10009930 follows on p.108); Claude, 2026-10-05'
review: draft
queries:
- "Checked: both printed WRAP examples are consistent with the stated rules (10 0 WRAP inserts three carriage returns; 11 2 WRAP gives an 11-character first segment, then 9-character segments indented 2)."
- "In the session, cr stands for the carriage-return character, as printed. The comma before the assignment (`,S←…`) displays the result, as printed."
- "Slip transcribed as printed: “acceptable, Diskettes will be returned”."
---

by David Ziemann
{ .byline }

Very often APL programmers will represent rows in a notional text matrix as the concatenation of vectors delimited by carriage return characters. This representation usually takes up less workspace because trailing blanks are not included.

For example, many APLs use a system function quadVR to return the visual representation of a user-defined function. This is a character vector containing imbedded carriage returns that displays as a neat function listing. Unfortunately, such displays often exceed some arbitrary width, because lines between the carriage returns are too long. In such cases it is desirable to wrap the offending lines by inserting appropriate extra carriage return characters. Example output could be:

```apl
      ,S←'IN PARADISE',cr,'HERONS',cr,'APPROACH FROM THE LEFT.'
IN PARADISE
HERONS
APPROACH FROM THE LEFT.

      10 0 WRAP cr,S
IN PARADIS
E
HERONS
APPROACH F
ROM THE LE
FT.
```

In this example the result is similar to the argument except that three extra carriage returns have been inserted; one after the ‘S’ of ‘PARADISE’, one after the ‘F’ of ‘FROM’ and one after the ‘E’ of ‘LEFT’. Notice that the function \<WRAP\> is quite general, with the first element of its right argument providing the delimiter character to be used. The left argument specifies the maximum allowable length substring between delimiters in the result, followed by the amount of indentation required. The indentation amount determines the number of leading blanks in each wrapped segment. For example:

```apl
      11 2 WRAP cr,S
IN PARADISE
HERONS
APPROACH FR
  OM THE LE
  FT.
```

The problem is to write such a function \<WRAP\>. As usual, the winning programs must be ISO APL standard conforming (use no extensions like replicate, nested arrays or special quad functions, etc.). Each entrant must submit only one competition entry, but may include alternatives for comparison and possible publication. These alternatives may be written in ANY APL, so let’s see some APL2 (etc) solutions too!

Entries will be judged on robustness, resource requirements, generality and intelligibility. A first prize of £30 and two others of £10 each will be sent to the winners.

The closing date for entries is 25th October 1985.

## Competition Rules

- Entries must be in legible English or APL as appropriate and should preferably be machine produced.
- Entrants must declare the type of computer and the version and release level of the APL interpreter on which their functions were written.
- The date and your full name and address should appear on each sheet of your entry.
- Entries should be physically separate from other contributions such as letters, and should be clearly marked ‘Competition Entry’
- All submissions should be sent to the editor.
- Those on the committee, activities group or journal group of the British APL Association are ineligible.
- DOS format diskettes containing APL\*PLUS, IBM or Sharp APL workspaces are acceptable, Diskettes will be returned.
- Unless otherwise stated, you should submit only one entry. We encourage submission of alternative approaches, but you must indicate clearly which answer is the competition entry.
