---
title: Competition Result – Watch Your Step
authors:
- David Ziemann
volume: '3'
issue: '3'
page: '107'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 109–112 (printed 107–110; the result of the competition set in v2n4-p109; Surely there must be a better way follows on p.111); Claude, 2026-10-05'
review: draft
tags:
- competitions and puzzles
queries:
- "Checked: STEP∆MK and STEP∆RC, simulated as printed, give the printed results for M1, M2 and M1÷2, give 1 for 0 STEP 1 3⍴1, and for 99 STEP 1 3⍴0 STEP∆MK returns an empty matrix where STEP∆RC returns 0, as the text describes."
- "Listings in a dot-matrix face; ⍎ is printed as a glyph like ±, read as ⍎. STEP∆NM [4] is printed `IOTA←-⎕IO-⍳⌈/,0,LENGTHS←1+⌊|GAP÷INC`; [6] `R←,R+⍉(⌽RHO)⍴ 0 ¯2 ↑MX`; STEP∆RC [10] `X←1⌈(1⌈⍴X)↑X←1+⌊|(-/M[; 1 2])÷M[;3]`. SAPLSTEP [5] uses Sharp APL’s > (disclose), ¨ with rank (⍤ printed as ¨>), and | (?) — transcribed as printed; doubtful readings."
- "Slips transcribed as printed: “producincg”, “their function were complete”, “bahaviour”, “mess avout”."
---

by David Ziemann
{ .byline }

This time the challenge was to write a function STEP that produces a matrix of ‘step’ vectors from its argument, a three-column matrix of start, stop, and step values. For example:

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

The left argument is a pad value for use in cases where a step vector contains zero, as in:

```apl
      ⎕←M2←3 3⍴8 ¯3 1,¯6 6 2,¯2 2 1
 8 ¯3 1
¯6  6 2
¯2  2 1
      99 STEP M2
 8  7  6 5 4  3  2  1  0 ¯1 ¯2 ¯3
¯6 ¯4 ¯2 0 2  4  6 99 99 99 99 99
¯2 ¯1  0 1 2 99 99 99 99 99 99 99
```

The competition attracted fourteen entries from Australia, Belgium, Denmark, West Germany and of course the UK. (What happened to our US and Canadian readers?). The entrants used eight different APLs to code their solutions, most of them on PCs and micros; VS APL, APL2, Sharp APL, APL\*PLUS PC, IBM PC APL, APL.68000, MIPS APL and Siemens APL.

Boiling the entries down proved fairly difficult, mainly because they all worked. At least, they all appeared to work for the above arguments. Closer inspection revealed that one entry did not return an explicit result, and that another went into an infinite loop if the first element of the right argument was a one!

As usual, dependence on the external index origin was tested for, and three entries were set aside because they failed when a global origin of zero was used. The next test tried each entry with a fractional right argument, as in:

```apl
      M1÷2
 5    13.5  2.5
40    50   10
56.5  50    1.5
¯4    ¯1.5  1
¯0.5  ¯1.5  0.5
      0 STEP M1÷2
 5     7.5 10    12.5  0
40    50    0     0    0
56.5  55   53.5  52   50.5
¯4    ¯3   ¯2     0    0
¯0.5  ¯1   ¯1.5   0    0
```

All the functions bar one behaved appropriately, producincg the result shown above. A floating point left argument produced the expected result in all cases, and so the search for more exacting tests was on.

What would happen if the entries were tried with a vector left argument, rather than a scalar? All entries performed as expected with a one-element pad value, but they split into three camps when a longer vector was used. The first group reported an APL error, the second group ignored the extra elements, using only the first element in the left argument as the pad value, and the third group used up the pad vector elements in a cyclic fashion. It is hard to see meaning in the cyclic use of a vector of pad numbers, and no such function documented this behaviour, and so these entries were rejected. Strictly speaking, the entries that ignore all but the first element are also not quite right – it is actually misleading and potentially dangerous for a function to accept argument values that it does not use. For example, an extended version of STEP that uses the second element of the left argument for a new purpose might now blow up when used as a replacement for the original function. The functions that caused a LENGTH or RANK error report therefore displayed the correct behaviour, and passed this test.

The next test checked to see if each function gave the correct result when a one row matrix of ones was passed in. The right answer is of course:

```apl
      0 STEP 1 3⍴1
1
```

Surprisingly perhaps, four more entries bit the dust on this one, producing two columns rather than one in the result matrix.

The next test examined the result when the right argument is an empty matrix, with zero rows and three columns. Before reading on, what do you think the shape of the result should be? This one produced no less than four different shapes of empty result and also a few errors. The error-producing functions were eliminated because an empty result is certainly to be expected in this case. Furthermore, we should expect the result to have as many rows as the argument matrix and this criterion eliminated the entry that gave an empty vector as its result.

Of the remaining empty matrices, some had zero columns, some one column and one even had two columns in the result! A zero by zero empty matrix was deemed correct because this result is consistent with the idea that the number of columns in the result should be equal to the length of the longest step vector in the result:

```apl
      ⍴0 STEP 0 3⍴0
0 0
```

This left us with only two entries. Here is Neil Mitchison’s function which has the twin merits of meaningful local variable names and clear APL code. Notice that the argument matrix MX is never indexed in Neil’s solution, and that origin-independent code is produced by just one reference to ⎕IO.

```apl
    ∇ R←FL STEP∆NM MX;GAP;INC;IOTA;LENGTHS;RHO
[1]   ⍝ Produces matrix of step vectors, filled with FL
[2]    GAP←-/ 0 ¯1 ↓MX
[3]    INC←, 0 2 ↓MX
[4]    IOTA←-⎕IO-⍳⌈/,0,LENGTHS←1+⌊|GAP÷INC
[5]    RHO←⍴R←(INC××-GAP)∘.×IOTA
[6]    R←,R+⍉(⌽RHO)⍴ 0 ¯2 ↑MX
[7]    R[(,LENGTHS∘.≤IOTA)/⍳⍴R]←FL
[8]    R←RHO⍴R
    ∇
```

The other successful entry was submitted by Morten Kromberg, who gave us this function:

```apl
    ∇ R←FILL STEP∆MK CTL;⎕IO;STEP;START;END;DIFF;N;MAX;MASK
[1]    ⍎(0=⎕NC 'FILL')/'FILL←0'
[2]    ⎕IO←0
[3]    START←CTL[;0]
[4]    END←CTL[;1]
[5]    STEP←CTL[;2]
[6]   ⍝
[7]    MAX←0⌈⌈/N←1+⌊(|DIFF←END-START)÷STEP
[8]    MASK←N∘.>⍳MAX
[9]   ⍝
[10]   R←(START∘.+MAX⍴0)+(STEP××DIFF)∘.×⍳MAX
[11]   R←(R×MASK)+FILL×~MASK
    ∇
```

Morten’s function has the additional feature of being able to handle the elision of the left argument when run on an APL system which supports ambi-valent functions.

It seemed clear that the winners had been found, and that their function were complete. I was ready to put the results to bed when another simple test occurred to me. The one row matrix of ones had already been tried, but what about a one row matrix of zeroes? Again, another reasonable function argument. To my horror (and depression because I thought the work was over) twelve out of the fourteen entries failed! Neil, Morten and ten others all yielded the following incorrect result:

```apl
      99 STEP∆NM 1 3⍴0
0 0
      99 STEP∆MK 1 3⍴0
0 0
```

Of the two who passed this test, one had already failed two other tests, and so this elevated R H Currie’s solution, which had produced a one-column empty matrix in response to the empty argument. R H Currie’s correct answer to the test, and the well-commented code follow:

```apl
      99 STEP∆RC 1 3⍴0
0

    ∇ R←L STEP∆RC M;X;Y;⎕IO
[1]   ⍝L is trailing pad number. M[;1 2] are start- and end-points
[2]   ⍝M[;3] are steps
[3]   ⍝Return matrix of range vectors
[4]   ⍝Assume L is numeric scalar; M numeric n×3 matrix
[5]   ⍝Don't mess avout with index origin - set it to 1
[6]    ⎕IO←1
[7]   ⍝Take absolute value of steps: replace 0 with 1
[8]    M[;3]←Y+0=Y←|M[;3]
[9]   ⍝X is no. within range in each row
[10]   X←1⌈(1⌈⍴X)↑X←1+⌊|(-/M[; 1 2])÷M[;3]
[11]  ⍝Y is a Boolean matrix of required shape: 1=within range
[12]   Y←X∘.≥⍳⌈/X
[13]  ⍝Generate R as though all ranges are same length
[14]   R←M[;(⌈/X)⍴1]+(M[;3]××-/M[; 2 1])∘.×0,⍳¯1+⌈/X
[15]  ⍝Replace out-of-range elements by L
[16]   R←(R×Y)+L×~Y
    ∇
```

So it turned out that the three best entries all failed exactly one test each – an unexpectedly tough competition indeed.

Morten also supplied the following appropriately named function which ran well over fifty per cent faster (under APL\*PLUS PC) than any of the other entries:

```apl
    ∇ R←FILL QUICKSTEP CTL;⎕IO;STEP;START;END;DIFF;N;MAX;MASK;T;INDEX
[1]    ⍎(0=⎕NC 'FILL')/'FILL←0'
[2]    ⎕IO←0 ⋄ START←CTL[;0] ⋄ END←CTL[;1] ⋄ STEP←CTL[;2]
[3]   ⍝
[4]    MAX←0⌈⌈/N←1+⌊(|DIFF←END-START)÷STEP
[5]    T←N/STEP←STEP××DIFF
[6]    T[¯1↓0,+\N]←START-¯1↓0,START+(N-1)×STEP
[7]    MASK←N∘.>⍳MAX
[8]    ⎕IO←1 ⋄ INDEX←(⍴MASK)⍴(,MASK)\⍳⍴T
[9]    ⎕IO←0 ⋄ R←(FILL,+\T)[INDEX]
    ∇
```

QUICKSTEP was by far the fastest function, but would require modification to change its current bahaviour of ignoring extra elements in the left argument. It also fails the one row matrix of zeroes test.

Competition entries must be written in standard-conforming APL, but we are always interested to see solutions in other APL dialects. Morten included this Sharp APL alternative with his entry:

```apl
    ∇ R←FILL SAPLSTEP CTL;⎕IO;STEP;START;END;DIFF;N;MAX
[1]    ⍎(0=⎕NC 'FILL')/'FILL←0'
[2]    ⎕IO←0 ⋄ START←CTL[;0] ⋄ END←CTL[;1] ⋄ STEP←CTL[;2]
[3]   ⍝
[4]    MAX←0⌈⌈/N←1+⌊(|DIFF←END-START)÷STEP
[5]    R←(START+¨>(STEP××DIFF)×¨>⍳¨>N),|>(MAX-N)⍴¨>FILL
    ∇
```

Congratulations to Neil Mitchison, Morten Kromberg and R H Currie who share the £50 prize money equally. Commendations are also due to Anthony Quas and Heinz Reutersberg.
