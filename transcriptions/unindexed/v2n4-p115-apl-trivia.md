---
title: 'APL Trivia: Life, the Universe and Everything?; Remarks on “Towards a Better APL”'
authors:
- David Ziemann
- Claude Henriod
volume: '2'
issue: '4'
page: '115'
unindexed: true
transcribed: 'from page images of VOL.2-NO.4-APRIL-1986.pdf, pages 117–121 (printed 115–119; an IBM advert follows on p.120); Claude, 2026-10-05'
review: draft
warning: Henriod’s APL listings (printed pp.117–119) are a rough dot-matrix print in which several glyphs are doubtful; check them against the page before relying on the code. The prose is reliable.
queries:
- "Compiled by David Ziemann; the second part is by Claude Henriod (translated by Helen Piper), the technical annex to his letter in v2n4-p103-technical-correspondence.md, answering Ivor Kenson’s “Steps toward a better APL” in Vol.2 No.2, which we have no scan of (#62)."
- "Checked: BIGANSWER2, evaluated right to left, gives 1.269640335E73 as printed (! of ⌈*|⌊-○ of ¯1 = 168). BIGANSWER1 formats 0.050941… with ⍕ and reverses the characters before executing them, so more printed digits give a bigger number: with ⎕PP 10 it gives 18360149050, printed 1.836014905E10 (match); with ⎕PP 17 Python gives 8.32239608360149E17, printed 6.53239608360149E17: the last digits of the formatted value differ, presumably from a different floating-point format. Transcribed as printed."
- "In Henriod’s listings names are written with deltas round an underscored letter (∆E∆ with E underscored, and so on), APL.68000’s underscored alphabet; transcribed with the underscored letter in lower case (∆e∆), as for underscored names elsewhere in this project. Ordinary capitals are kept."
- "Doubtful glyph readings: FOR [5] is printed `⍎∆e∆, ←1↑∆i∆'` with an unmatched quote; INPUT [6] begins with a glyph like ⍳ or ⌷ before `≠0\\0⍴∆e∆` (read as `(0≠0\\0⍴∆e∆)`, as in PRINT [1] and READ [6]); SUB∆EXTRACT’s result name is printed like ∆Ʒ∆ (read as ∆r∆, the variable it assigns). The 12 ⍎ symbols, ⍕ and ⌽ are clear."
- "ON [1] is printed `→(=/I)0,⍴L←,L)/⍴R←⍳0` with unbalanced parentheses (perhaps `→((=/I)0,…` or `→(=/I>0,…`); NEXT [1] `NEXT←(89≥I←I+1)/16` (line numbers 89 and 16 of FOR’s fixed function?); SUB∆EXTRACT [2] `(⎕R ⎕BOX ⎕SI)`, where ⎕R is doubtful. Transcribed as read."
- "“Nomadic functions” (niladic) and “SERIE”, “PROGRAMM” are printed so."
---

compiled by David Ziemann
{ .byline }

## Life, the Universe and Everything?

In VECTOR Vol 2, No.2, we looked at a function that applied all the monadic primitives to 0 to produce the answer to the ultimate question, as “Hitch-hiker” fans will recall. A challenge was set to find the largest possible number obtained by scrambling the order of the primitives. Claude Henriod from Switzerland produced this interesting piece of code:

```apl
    ∇ R←BIGANSWER1
[1]   R←⍎⌽⍕-⍟!|+⌹○÷*⌈⌊×⍉⊖~⍴⍒⍋,?⍳0
    ∇

      BIGANSWER1
1.836014905E10
      ⎕PP←17
      BIGANSWER1
6.53239608360149E17
      ⎕PP←10
```

Can you see why the result gets larger as the value of the system variable ⎕PP is increased? Mark Bassett supplied the following code to produce the biggest answer he could find:

```apl
    ∇ R←BIGANSWER2
[1]   R←!⌈*|⌊-○⌽⍉⊖⌹÷~+×⍎⍕⍴?⍒⍋⍟,⍳0
    ∇

      BIGANSWER2
1.269640335E73
```

Can anyone improve on this, or perhaps prove that it can or cannot be bettered?

It seems that “Ivor Kenson’s” article “Steps Toward a Better APL” caused a bit of confusion, and was taken seriously by at least two people! (Now doesn’t that name seem somehow familiar?). Claude Henriod was so incensed that he has not only produced a criticism of the original article, but also sent us with his own version of what a simulation of BASIC in APL should look like. Let’s have a look at what Claude has to say, with thanks to Helen Piper for providing the translation, but after this, please – no more BASIC emulators!

## Remarks on “Towards a Better APL”

*by Claude Henriod*

In general one has the impression that the author of these APL functions is a FORTRAN programmer.

The APL listings which accompany these notes have been developed and tested with APL-68000 V5.0 on an Ampere computer.

### 1. Some simple improvements:

- ELSE, RETURN, STOP are unchanged.
- GOTO, IF are simplified.
- BASICDEMO and my equivalent FIBOBASIC are no comparison with the APL function FIBO.
- THEN uses 4 lines and 2 branches and is too complicated in APL.
- NEXT is so much simpler in APL.
- STEP is a BASIC keyword which must be included.
- ON is associated with GOTO, for example:  
  GOTO (L100,L200,L300) ON INDEX

### 2. Comments on Mr. Kenson’s code

- Allowing assignment to ⎕WA is a weakness in some interpreters. It is always dangerous to use the errors of a system, since a new version could correct them.
- APL-68000 does not allow assignment into ⎕WA, and also does not understand ⎕ALX or ⎕ELX, and so I think it is preferable to use local variables with a naming standard.
- FOR and INPUT contain the same sequence of code which can be extracted as a sub-function (see also READ).
    - Line 3 is simplified
    - Lines 2 and 4-6 are moved to SUBEXTRACT
- INPUT is closer to BASIC if a prompt is incorporated. It would also be necessary to initialise the variable or variables, as with READ.
- PRINT is a very inadequate copy of the BASIC command. It is very simple to simulate it in 3 lines (see the code in FIBOBASIC).

### 3. BASIC extensions

- FOR does not correspond to the BASIC version:
    - lacks the ability to use a decreasing sequence
    - cannot be nested
    - the FOR....NEXT loop is executed at least once (DO-UNTIL instead of DO-WHILE).

I have not been able to resist the pleasure of completing M. Kenson’s study:

- READ, DATA and RESTORE are new functions
- READ uses SUBEXTRACT. Constraint: The variable must be initialised with the maximum length of the data, which can likened to a DIM statement.
- DATA requires an argument of a single data type, but this is not a great handicap thanks to RESTORE.
- RESTORE n. If n=0, the first line of DATA is restored. If n is not a line of DATA, RESTORE has no effect on the sequence of data.

APL-68000 has certain differences which I have used, for example Nomadic functions, but it could be written without the use of such extensions.

⎕SI is “vectorised”, so I have used ⎕BOX. ⎕SS directly gives the index of the argument being sought.

I have not copyrighted, nor do I make any reservations on the presented code, because I am only concerned with the promotion of APL.

```apl
    ∇ DATA ∆s∆
[1]    →(2=⎕NC'DATA∆CTRL')/⎕LC+1 ⋄ DATA∆CTRL←⍳0
[2]    ∆s∆←¯1↑2↑⎕LC ⋄ →(∆s∆∊DATA∆CTRL)/0
[3]    DATA∆CTRL←DATA∆CTRL,∆s∆
    ∇

    ∇ R←X ELSE Y
[1]    R←X,Y
    ∇

    ∇ X←FIBO N
[1]   ⍝ FIBONACCI SERIE
[2]    X←1 1
[3]    →(N>⍴X←X,+/¯2↑X)/⎕LC
    ∇

    ∇ FIBO∆BASIC
[1]   ⍝ REM SIMULATED BASIC PROGRAMM IN APL
[2]    N←0
[3]    'GIVE FIBO LIMIT'INPUT N
[4]   L100:→IF(N≤0)THEN STOP ELSE L200
[5]   L200:I←1
[6]    R←0
[7]    S←1
[8]   L300:→IF(I=N)THEN GOTO L400
[9]    →GOSUB L500
[10]   PRINT I,R
[11]   I←I+1
[12]   →GOTO L300
[13]  L400:→GOSUB L500
[14]   PRINT I,R
[15]   X←''
[16]   FOR I←1 TO R
[17]   PRINT'*;'
[18]   →NEXT I
[19]   PRINT'*'
[20]   →STOP
[21]  L500:T←S
[22]   S←R+S
[23]   R←T
[24]   →RETURN
    ∇

    ∇ FOR FOR;∆a∆;∆e∆;∆i∆;∆l∆;∆s∆
[1]    ∆a∆←⍕1+¯1↑2↑⎕LC
[2]    ∆l∆←SUB∆EXTRACT'FOR'
[3]    ∆e∆←¯1↓(∆i∆←∆l∆⍳'←')↑∆l∆
[4]    ⍎'∆i∆←',(∆i∆)↓∆l∆
[5]    ⍎∆e∆, ←1↑∆i∆'
[6]    ∆l∆←⍕¯1↑2↑∆i∆
[7]    ∆s∆←⍕¯1↑3↑∆i∆,1
[8]    FOR←'NEXT←(',∆l∆,'≥',∆e∆,'←',∆e∆,'+',∆s∆,')/',⍕∆a∆
[9]    0 0⍴⎕FX((⍴FOR)↑'NEXT←NEXT NEXT'),[⎕IO-0.5]FOR
    ∇

    ∇ R←GOSUB R;∆i∆;∆x∆
[1]    ∆i∆←⍕1+¯1↑2↑⎕LC
[2]    ∆x∆←(8⌈⍴∆x∆)↑∆x∆←'R←',∆i∆
[3]    0 0⍴⎕FX((⍴∆x∆)↑'R←RETURN'),[⎕IO-0.5]∆x∆
    ∇

    ∇ R←GOTO R
    ∇

    ∇ R←IF R
    ∇

    ∇ ∆t∆ INPUT INPUT;∆l∆;∆e∆
[1]    ∆l∆←⍴,INPUT ⋄ ∆e∆←0≠0\0⍴INPUT ⋄ INPUT←SUB∆EXTRACT'INPUT'
[2]    →(2≠⎕NC'∆t∆')/⎕LC+1 ⋄ PRINT ∆t∆
[3]    →∆e∆/⎕LC+1 ⋄ ∆e∆←⎕ ⋄ →⎕LC+2
[4]    ∆t∆←(¯1+⍴∆t∆)×';'=¯1↑∆t∆←,∆t∆ ⋄ ∆e∆←∆t∆↓⍞
[5]    ∆e∆←(∆l∆⌊⍴,∆e∆)↑∆e∆
[6]    →(0≠0\0⍴∆e∆)/⎕LC+1 ⋄ ⍎INPUT,'←',⍕∆e∆ ⋄ →0
[7]    ⍎INPUT,'←''',∆e∆,''''
    ∇

    ∇ NEXT←NEXT NEXT
[1]    NEXT←(89≥I←I+1)/16
    ∇

    ∇ R←L ON I
[1]    →(=/I)0,⍴L←,L)/⍴R←⍳0
[2]    R←L[⎕IO-1-I]
    ∇

    ∇ PRINT ∆x∆
[1]    →(0≠0\0⍴∆x∆)/⎕LC+1 ⋄ ∆x∆ ⋄ →0
[2]    →(';'=¯1↑∆x∆)/⎕LC+1 ⋄ ∆x∆ ⋄ →0
[3]    ⍞←¯1↓∆x∆
    ∇

    ∇ READ READ;∆c∆;∆e∆;∆l∆
[1]    ∆l∆←⍴,READ ⋄ READ←SUB∆EXTRACT'READ'
[2]    →(2≠⎕NC'DATA∆LIST')/⎕LC+1 ⋄ →(0=⍴DATA∆LIST)/⎕LC+1 ⋄ →∆i∆
[3]    DATA∆LIST←(1↑DATA∆CTRL)SUB∆EXTRACT'DATA' ⋄ DATA∆CTRL←1⌽DATA∆CTRL
[4]   ∆i∆:∆c∆←-⎕IO-DATA∆LIST⍳',' ⋄ ∆e∆←⍎∆c∆↑DATA∆LIST
[5]    DATA∆LIST←(1+∆c∆)↓DATA∆LIST ⋄ ∆e∆←(∆l∆⌊⍴,∆e∆)↑∆e∆
[6]    →(0≠0\0⍴∆e∆)/⎕LC+1 ⋄ ⍎READ,'←',⍕∆e∆ ⋄ →0
[7]    ⍎READ,'←''',∆e∆,''''
    ∇

    ∇ READ∆BASIC
[1]    DATA 1,3,5,7,11,13,17,19,23,29
[2]    DATA 10
[3]    DATA'BRITAIN','FRANCE','GERMANY','SWITZERLAND','ITALY'
[4]    RESTORE 3
[5]    FOR NO←1 TO 4
[6]    TXT←8⍴' '
[7]    READ TXT
[8]    PRINT NO
[9]    PRINT TXT
[10]   →NEXT NO
[11]   RESTORE 2
[12]   CNT←0
[13]   READ CNT
[14]   RESTORE 0
[15]   FOR NO←1 TO CNT STEP 2
[16]   VALUE←0
[17]   READ VALUE
[18]   PRINT VALUE
[19]   →NEXT NO
[20]   →STOP
    ∇

    ∇ RESTORE ∆x∆
[1]    →(0≠∆x∆)/⎕LC+1 ⋄ ∆x∆←⌊/DATA∆CTRL
[2]    DATA∆CTRL←(-⎕IO-DATA∆CTRL⍳∆x∆)⌽DATA∆CTRL
[3]    0 0⍴⎕EX'DATA∆LIST'
    ∇

    ∇ R←RETURN
[1]    R←13
    ∇

    ∇ R←X STEP Y
[1]    R←X,Y
    ∇

    ∇ R←STOP
[1]    R←0
    ∇

    ∇ ∆r∆←∆l∆ SUB∆EXTRACT ∆n∆;⎕IO
[1]    →(2=⎕NC'∆l∆')/⎕LC+1 ⋄ ∆l∆←¯1↑3↑⎕LC
[2]    ∆r∆←(⎕R ⎕BOX ⎕SI)[2+⎕IO←1;]
[3]    ∆r∆←⎕CR ¯1↓(∆r∆⍳'[')↑∆r∆
[4]    ∆r∆←,∆r∆[1+∆l∆;]
[5]    ∆r∆←((¯1+⍴∆n∆)+1↑⎕SS(∆r∆;∆n∆))↓∆r∆
    ∇

    ∇ R←C THEN L
[1]    R←(C,(~C)×2=⍴L)/L
    ∇

    ∇ R←X TO Y
[1]    R←X,Y
    ∇
```
