---
title: Towers of Hanoi from 15 Years Ago
authors:
- Adrian Smith
volume: '12'
issue: '4'
page: '32'
unindexed: true
transcribed: 'from page images of VOL.12-NO.4-APRIL-1996.pdf, page 34 (printed 32; follows the references of art10010130, within The Education Vector); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- competitions and puzzles
queries:
- "The function is printed in an italic APL face; line [5] reads `<⍀⊖~~`. Checked in Dyalog APL: HANOI 3 gives the discs 1 2 1 3 1 2 1 and the pegs 2 3 3 2 1 2 2, a valid solution."
---

*by Adrian Smith*
{ .byline }

For historical amusement, here is a rerun of the Hanoi Tower solution from *Crab APL*, Issue 10, page 11, March 1981. This recognises the binary pattern in the moves, and builds a boolean array, which it then adjusts and indexes to get the sequences of moves. Note that in modern APLs, the use of the `~~` sequence should not be necessary, as they do this sort of thing for you.

```apl
    ∇ R←HANOI N;DISC;PEG;INT
[1]   ⍝ NON-RECURSIVE SOLUTION TO THE HANOI TOWER PUZZLE
[2]   ⍝
[3]   ⍝ FIRST SET UP THE MOVE NUMBERS IN BINARY FORM; ONLY THE
[4]   ⍝ TOPMOST <ONE> BEING LEFT ON. (THE ~~ SPEEDS THINGS UP A BIT!)
[5]    INT←<⍀⊖~~(N⍴2)⊤¯1↓⍳2*N
[6]   ⍝ THE DISC TO BE MOVED IS GIVEN BY THE POSITION OF THE ONES
[7]    DISC←(⍳N)⌈.×INT
[8]   ⍝ MAKE ALTERNATE ROWS +/- TO FORCE DISKS TO
[9]   ⍝ CYCLE WITH OPPOSITE HANDEDNESS
[10]   INT←INT×⍉((1↓⍴INT),N)⍴N⍴ 1 ¯1
[11]  ⍝ THE POSITION OF EACH DISK AT ANY TIME IS THE CUMULATIVE
[12]  ⍝ VALUE OF THIS, BUT EXPRESSED IN MODULO-3.
[13]  ⍝
[14]  ⍝ TO GET THE NEW PEG AT EACH MOVE, WE INDEX BY DISK NO. FOR
[15]  ⍝ THE ROWS; MOVE NO. FOR THE COLUMNS. THIS EFFECT CAN
[16]  ⍝ BE ACHIEVED EITHER WITH A SCATTERED-PT SELECTION FUNCTION
[17]  ⍝ OR (AS HERE) WITH A 1 1⍉ TO GET THE DIAGONAL OF AN
[18]  ⍝ INTERMEDIATE OBJECT.
[19]   PEG← 1 1 ⍉(1+3|+\INT)[DISC;]
[20]   R←DISC,[0.5]PEG
    ∇
```
