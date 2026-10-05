---
title: 'Prize Competition: Watch your step'
authors:
- David Ziemann
volume: '2'
issue: '4'
page: '109'
unindexed: true
transcribed: 'from page images of VOL.2-NO.4-APRIL-1986.pdf, pages 111–112 (printed 109–110, with the Competition Rules; Surely there must be a better way follows on p.111); Claude, 2026-10-05'
review: draft
queries:
- "Checked: the three STEP examples (0 STEP M1, 0 STEP M2, 99 STEP M2) follow from the stated rules."
- "The Competition Rules extend those printed in v2n1-p105 with two new rules (non-members, late entries). Slips transcribed as printed: “APL *PLUS”."
---

by David Ziemann
{ .byline }

It’s a common requirement when writing APL to want to generate a set of indices from 1 up to some integer N. We can do this simply by using monadic iota, the index generator function, in origin-1:

```apl
      ⍳10
1 2 3 4 5 6 7 8 9 10
```

Sometimes we need to start counting from a number other than 1 however, or even to count backwards from a high number to a lower one. In such cases the function \<TO\> can be used:

```apl
      3 TO 10
3 4 5 6 7 8 9 10
      8 TO 2
8 7 6 5 4 3 2
      ¯3 TO 5
¯3 ¯2 ¯1 0 1 2 3 4 5
```

By the way, \<TO\> can also be used to generate multiple range vectors, for example:

```apl
       3 TO 5  4 TO ¯1  5 TO 2
 3 4 5 4 3 2 1 0 ¯1 5 4 3 2
```

Now the function \<TO\> is very useful in APL systems, but occasionally a little more is needed. In particular, what we want is a function which will produce a matrix of range vectors from an input matrix of ranges. To make things even more exciting we want to be able to specify the step in each case. Here’s an example of a function called \<STEP\> which demonstrates the required behaviour:

```apl
      ⎕←M1←5 3⍴10 27 5,80 100 20,113 100 3,¯8 ¯3 2,¯1 ¯3 1
 10  27   5
 80 100  20
113 100   3
 ¯8  ¯3   2
 ¯1  ¯3   1
      0 STEP M1
 10  15  20  25   0
 80 100   0   0   0
113 110 107 104 101
 ¯8  ¯6  ¯4   0   0
 ¯1  ¯2  ¯3   0   0
```

Each row in the right argument specifies a start-point number, an end-point number and a step. The start and end-points may be positive or negative, but the step must be positive.

The shorter range vectors in the rows of the result matrix are padded with trailing zeros. This leads to the possibility of confusion of course, if a range vector should itself contain a zero:

```apl
      ⎕←M2←3 3⍴8 ¯3 1,¯6 6 2,¯2 2 1
 8 ¯3 1
¯6  6 2
¯2  2 1
      0 STEP M2
 8  7  6 5 4 3 2 1 0 ¯1 ¯2 ¯3
¯6 ¯4 ¯2 0 2 4 6 0 0  0  0  0
¯2 ¯1  0 1 2 0 0 0 0  0  0  0
```

That’s where the left argument comes in – it’s used as the trailing pad number so that you can choose a pad number you know cannot occur in your particular set of ranges. So, changing the left argument:

```apl
      99 STEP M2
 8  7  6 5 4  3  2  1  0 ¯1 ¯2 ¯3
¯6 ¯4 ¯2 0 2  4  6 99 99 99 99 99
¯2 ¯1  0 1 2 99 99 99 99 99 99 99
```

The competition this issue requires you to write the function \<STEP\> as shown and described above. As usual FIFTY POUNDS in prize money will be shared among the winners – those who produce the best answers, in the opinion of the judges. The closing date for entries is 30th July 1986.

## Competition Rules

- Entries must be in legible English or APL as appropriate and should preferably be machine produced.
- Entrants must declare the type of computer and the version and release level of the APL interpreter on which their functions were written.
- The date and your full name and address should appear on each sheet of your entry.
- Entries should be physically separate from other contributions such as letters, and should be clearly marked ‘Competition Entry’.
- All submissions should be sent to the editor.
- Those on the committee, activities group or journal group of the British APL Association are ineligible.
- DOS format diskettes containing APL \*PLUS, IBM or Sharp APL workspaces are acceptable; diskettes will be returned.
- Unless otherwise stated, entrants should submit only one entry. We encourage submission of alternative approaches, but the entrant must indicate clearly which one of his answers is his entry in the competition.
- Non-members are encouraged to enter the competition, with the proviso that, should they win, part of their prize will comprise free B.A.A. membership for the current year.
- Late competition entries may be accepted if the competition has not yet been judged.
