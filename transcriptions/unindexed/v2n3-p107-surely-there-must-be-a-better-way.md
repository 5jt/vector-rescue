---
title: Surely there must be a Better Way
authors:
- David Ziemann
volume: '2'
issue: '3'
page: '107'
unindexed: true
transcribed: 'from page images of VOL.2-NO.3-JANUARY-1986.pdf, pages 109–110 (printed 107–108; Sullivan’s and Buckland’s answers to Wiggins’s problem in v2n1-p97-surely-there-must-be-a-better-way.md; art10006740 follows on p.109); Claude, 2026-10-05'
review: draft
queries:
- "Byline printed “compiled by David Ziemann”."
- "Checked by hand: WIGGINS [16] and [19] and REDUCE [4], evaluated on the example data, give the printed results, which are Wiggins’s required solution."
- "WIGGINS [16] is printed `R←X[1;],[1](X[1;]-A),[0.1]A←A-0,¯1↓A←⌈\\+\\-⌿X←0,X`; the laminate axis is printed [0.1]. [19] `R← 0 1 ↓R,[1]+\\X[2;]-R[2;]`. “2×?” and “4×?” in the comments are printed so."
---

compiled by David Ziemann
{ .byline }

In VECTOR 2.1 Andrew Wiggins presented a depreciation problem to which he had found only a looping solution. John Sullivan has sent us the following parallel solution (If you search hard you’ll find the code):

```apl
    ∇ R←WIGGINS X;A
[1]   ⍝ <X> is a 2×? matrix, the first row is 'Income'
[2]   ⍝ the second is 'Depreciation'
[3]   ⍝ <R> is a 4×? matrix containing 'Income', 'Depreciation' as revised
[4]   ⍝ by the function, 'Profit' and 'Carried forward'
[5]   ⍝ Function written in APL2, although it does not use anything outside
[6]   ⍝ standard VS APL
[7]   ⍝ Method:
[8]   ⍝    Since the program doesn't work properly unless it starts with a
[9]   ⍝ 'profit',we add a nominal profit of 0 to the start of the input.
[10]  ⍝ Since we are taking profits whenever they occur, we calculate a
[11]  ⍝ Profit/Loss vector (+\-⌿X), and save the amount of profit taken
[12]  ⍝ so far (A←⌈\+\-⌿X). If we subtract this lagged 1 period from itself
[13]  ⍝ we obtain the profit taken in each period (A←A-0,¯1↓A). Now we can
[14]  ⍝ revise the 'Depreciation' figures (X[1;]-A) and prepare the first
[15]  ⍝ three lines of the table at the bottom of page 97.
[16]   R←X[1;],[1](X[1;]-A),[0.1]A←A-0,¯1↓A←⌈\+\-⌿X←0,X
[17]  ⍝ Last of all we calculate the 'Carried Forward' figures, and drop
[18]  ⍝ the data we added to make the program work
[19]   R← 0 1 ↓R,[1]+\X[2;]-R[2;]
    ∇
```

Here is John’s function in action:

```apl
      ID
100 110 120 130 140 150 160 170 180 190
 70 130 140 130 120  60 180 170 150 230
      WIGGINS ID
100 110 120 130 140 150 160 170 180 190
 70 110 120 130 140  80 160 170 170 190
 30   0   0   0   0  70   0   0  10   0
  0  20  40  40  20   0  20  20   0  40
```

Another John, this time John Buckland, furnished us with this:

```apl
    ∇ R←INC REDUCE DEPN;A;B
[1]   ⍝ Reduces income <INC> by depreciation <DEPN> as required.
[2]   ⍝ Returns <R> with two rows holding the amounts deducted
[3]   ⍝ and carried forward in each period
[4]    R←(2,⍴B)⍴R,B-+\R←A-0,¯1↓A←A-⌈\0⌈(A←+\INC)-B←+\DEPN
    ∇

      ID[1;] REDUCE ID[2;]
70 110 120 130 140  80 160 170 170 190
 0  20  40  40  20   0  20  20   0  40
```

Notice that this function has the advantage of being origin independent.

We trust that these solutions will satisfy Andrew, or any other interested readers, but hope that more suitable names will be chosen for the functions. A better name might be \<CARRYFORWARD\> for example, rather than \<DEPRECIATE\> say, because this name matches the generality of the function more closely. In this way the reader will be led to believe that the function has a more general usage than just in calculating depreciation.

Mark Bassett’s plea in VECTOR 2.1 for the \<WORDWRAP\> function has been answered by Zeke Hoskin. His function is printed in the competition result page. Has anyone managed to solve this problem without looping? Maybe a good application for ‘matrix-divide’?
