---
title: 'Prize Competition Result: This is your Life'
authors:
- David Ziemann
volume: '1'
issue: '3'
page: '123'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 125–127 (printed 123–125; results of the competition in v1n1-p105-prize-competition-this-is-your-life.md; an E&S Associates advert fills the lower part of p.125); Claude, 2026-10-03'
review: draft
queries:
- "Checks: every solution printed here (both BTRs, Mike Day’s looping BTR, Phil Last’s RTB, and the replicate RTB) was run, as transcribed, against all boolean vectors up to length 8, in index origins 0 and 1, and all are correct; BTR of the example grid gives 2 2 4 5 2 2 3."
- "Mike Day’s line [4] is `→3⌈B←~C/B` (ceiling), read at 900 dpi: `3⌈B` is a vector of 3s while B is non-empty, so the loop continues; empty, it exits."
- "Slip transcribed as printed: “J Jollife”."
---

by David Ziemann
{ .byline }

The first VECTOR competition attracted respondents from Austria, Holland and Switzerland, as well as from the UK. The UK entries even included one from a certain P Andrew with an address in The Mall, London!

To recap, the problem was to write two monadic functions BTR and RTB that convert between the boolean and run-coded representations of a binary grid. For example:

```
      BM
0 0 1 1 0
0 0 0 1 1
1 1 1 0 0
1 1 0 0 0

      BTR ,BM
2 2 4 5 2 2 3

      (⍴,BM)∧.=+/BTR ,BM
1

      (,BM)∧.=RTB BTR ,BM
1
```

The first element of the run-coded vector was to always give the number of leading zeros in the corresponding ravelled boolean matrix. The two functions were to be written in ISO Standard APL and were also to be independent of their environment. All else succeeding, entries were to be judged on the brevity of the solutions.

There were many interesting responses, including one recursive function and one entry with six rather than two functions!

So, what happened? Well, each entrant’s functions were automatically tested with sixteen different arguments to see how they behaved. These cases included boolean matrices of all types — leading ones, leading zeros, trailing ones, trailing zeros, singular matrices, empty matrices, matrices of different sizes, etc., etc. In each case both functions were tested with an external index origin setting of both zero and then one, to check for environment independence.

The result of all this was that some functions were disqualified for producing incorrect results. For example: three RTBs, and two BTRs when the global index origin was zero, one BTR for leading zeros in the argument and four BTRs for empty matrices. One BTR was disqualified for producing an APL error with an empty argument.

Note that an empty argument to BTR should produce a vector whose only element is a zero, in order for the above identities to hold.

About half of the BTRs achieved origin independence by explicitly setting quadIO first. A more concise answer is possible if the system variable is referenced explicitly, as in this 31 character solution by Thomas van den Heuvel:

```
    ∇ R←BTR B;X;Y
[1]   ⍝ CONVERT BOOLEAN VECTOR <B> TO RUN-CODE VECTOR <R>
[2]    R←Y-¯1↓⎕IO,Y←X/⍳⍴X←(B≠¯1↓0,B),1
    ∇
```

Further research shows that a shorter solution is possible if one remembers that the function argument is always boolean:

```
    ∇ R←BTR B
[1]   ⍝ CONVERT BOOLEAN VECTOR <B> TO RUN-CODE VECTOR <R>
[2]    R←R-⎕IO,¯1↓R←R/⍳⍴R←(0,B)≠B,2
    ∇
```

Mike Day had the gall to suggest this incredible 25 character looping solution:

```
    ∇ R←BTR B;C
[1]   ⍝ CONVERT BOOLEAN VECTOR <B> TO RUN-CODE VECTOR <R>
[2]    R←''
[3]    R←R,+/~C←∨\B
[4]    →3⌈B←~C/B
    ∇
```

The judges do not recommend the use of this particular function in a real application!

Andrew Tarr pointed out that users of DEC-10 APLSF could increase BTR’s efficiency, and further shorten it, by using monadic omega. This function directly converts a boolean vector into an index vector, as follows:

```
ωB ←→ B/⍳⍴B
```

(See the technical letters section for Andrew’s letter — Ed.)

The RTBs were generally more interesting. A number of entrants used indexing to solve the problem, whereas others used outer products of various kinds (less than, less than or equals, greater than or equals, plus) followed by reductions or compressions to produce the desired result. Those who strove for a shorter solution discovered that outer product was not necessary. At 18 characters, the shortest and most elegant RTB was submitted by Phil Last:

```
    ∇ R←RTB V
[1]   ⍝ CONVERT RUN-CODE VECTOR <V> TO BOOLEAN VECTOR <R>
[2]    R←≠\(⍳+/V)∊⎕IO++\V
    ∇
```

A surprising number of entrants used the residue function, failing to recall the following boolean identities:

```
2|+/B ←→ ≠/B
2|+\B ←→ ≠\B
```

Claude Henriod and Phil Last pointed out that RTB is trivial with an APL that supports extended compression (replicate):

```
    ∇ R←RTB V
[1]    R←V/(⍴V)⍴ 0 1
    ∇
```

No doubt some authors arrived at their solutions by working backwards from this one.

After deliberation the judges decided to award the prize money to Phil Last (£20), Mike Day (£20) and Thomas van den Heuvel (£10). Special commendations also go to Mark Bassett and J Jollife.

Two entrants wanted to know how the run-coded representation was used to calculate the next generation in the “Game of Life”. Space prohibits the full details of the algorithm, which was due to Paul Chapman, being printed here.

Briefly though, the rows of the boolean matrix are individually scanned from left to right with concurrent reference to the run-code vector. In this way subsequent columns of the next generation grid are generated. This finite-state machine approach is obviously heavily reliant on loops, but APL was only used as a prototype for the final machine code version. One of the main advantages of this algorithm is that it can deal with large amounts of empty space in one step.
