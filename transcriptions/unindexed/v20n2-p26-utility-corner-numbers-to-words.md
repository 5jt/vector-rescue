---
title: 'Utility Corner: Numbers to Words'
authors:
- Gary A. Bergquist
volume: '20'
issue: '2'
page: '26'
unindexed: true
transcribed: 'from page images of VOL.20-NO.2.pdf, pages 28–35 (printed 26–33; within Zark Newsletter Extracts, the first item after Jon Sandles’s introduction); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- development practice
queries:
- "Printed as “Utility Corner: Numbers to Words”, but the column is about comparing two versions of a function (`CRCOMPARE` and `VRCOMPARE`): the solutions to the Limbering Up task “Comparing Functions” set in 20:1 (art10014300). The heading evidently repeats the previous issue’s; the printed title is kept."
- "Within the Zark Newsletter Extracts. Jon Sandles’s introduction, which has no record of its own, is included at the head. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. It is followed on p.33 by the Limbering Up column, transcribed separately (unindexed/v20n2-p33-limbering-up-comparing-functions.md)."
- "`CRCOMPARE` and `VRCOMPARE` were run in Dyalog APL on the two `CALC` functions as a check on the transcription; with `A←B+C` in the first line of each, both give the comparison printed, except that they number the deleted lines [5] and [6]. For the run, `CRCOMPARE` [39] was read `N1-I1`; it is printed `N1[I1`, kept as printed."
- "The example is printed inconsistently, kept as printed: the first `CALC` has `A+B+C` in [1] and the second `Z×D÷100` in [7]; the comparison shows `A+B+C`, `0 0 ρ0` with a space, `[6]` and `[7]` for lines [5] and [6], and `Z←0.0×D`."
- "Kept as printed: “Move your hands … more your left hand down”, “to the fight”, “the furst remaining line”, “The try moving it”; in `CRCOMPARE` the comments “1st rows sof”, “Flag comment of label lines”, “Brance by class”; in `VRCOMPARE` “Lenghts”, “...and line indices” in [86], and “Delete (C=1)” where there is no `C`. The header of `VRCOMPARE` is broken in print within the name `PLUSIOTA`."
---

*Zark Newsletter Extracts, introduced by Jon Sandles*
{ .byline }

Here is another Zark newsletter extract. As always, don’t hesitate to send in any solutions you may have that you may be inspired to investigate. There may be new more elegant ways of solving an old problem, which may also turn out to be faster. Please don’t be afraid to try and shed “new” light on the “old” problems. Once again, thanks to Jonathan Barman for helping typeset this column. We haven’t had much feedback of late - I hope you are still finding these enjoyable!

## Utility Corner: Numbers to Words

(The purpose of this column is to make you more productive by introducing you to utility functions. Think of utility functions as APL functions that have names instead of symbols. By expanding your function vocabulary, you’ll be able to write APL code that’s more concise, more efficient, and more readable.)

In last issue’s *Limbering Up* column, you were asked to define a utility function that compares two similar functions.

When maintaining a large APL application, you will occasionally find yourself face-to-face with two copies of the same function. Yet the copies are not the same. Perhaps two different programmers enhanced the same function in different ways. You would like to know how the functions are different.

The first objective is to bring the two functions together so they can be compared. Yet, if you copy both functions into the workspace, only one will survive (since they have the same name!) To compare the functions you must convert them to character array representations via `⎕CR` (canonical representation) or `⎕VR` (visual representation). For example:

```apl
      )COPY WS1 MODEL
SAVED...
      CR1←⎕CR 'MODEL'
      )COPY WS2 MODEL
SAVED...
      CR2←⎕CR 'MODEL'
```

Now you have two character matrices that “look like” the function. The task was to write a function `CRCOMPARE` (or `VRCOMPARE` if you are using `⎕VR`) that returns/displays the differences between the functions. For example, given these two functions,

```apl
      ∇ CALC
[1]     A+B+C
[2]     D←3
[3]     E←D-A+B+C
[4]     F←D+E
[5]     A←0 0⍴0
[6]     B←0 0⍴0
[7]     G←F*0.5
[8]     'DONE'
[9]     Z←0.01×D
      ∇

      ∇ CALC
[1]     A+B+C ⋄ D←3
[2]     E←D-A+B+C
[3]     F←D+E
[4]     G←F*0.5
[5]     A←B←0 0⍴0
[6]     'DONE'
[7]     Z×D÷100
      ∇
```

the comparison looks like:

```apl
      CR1 CRCOMPARE CR2

[1]  A+B+C
[2]  D←3
---- replaced by ----
[1]  A+B+C ⋄ D←3

[6]  A←0 0 ⍴0
[7]  B←0 0 ⍴0
---- deleted ----

[5]  A←B←0 0 ⍴0
---- added ----

[9]  Z←0.0×D
---- replaced by ----
[7]  Z←D÷100
```

A straightforward approach to this problem is to place the representation of the old function on the left side of your desk, and the new one on the right. Move your hands down both functions until you come to lines that don’t match. Keeping your left hand on the first mismatching line, move your right hand down until you find a matching line. If you don’t, more your left hand down to the second line and again scan through the remaining lines of the function to the fight until you find a match. Keep this up until you find a match or run out of lines. If you run out of lines, report all remaining lines in the left function as “replaced” by the remaining lines in the right function.

If there *is* a match, and if your left hand is still pointing at the furst remaining line, report the lines of the right function up to the matching line as “added” lines. If your right hand is pointing at the first remaining line, report the lines of the left function up to the matching line as “deleted” lines. Otherwise, report the lines of the left function up to the matching line as “replaced” by the lines of the right function up to the matching line. Then repeat this process, starting at the matching lines.

The trickiest part of the `CRCOMPARE` function is formatting the lines so they have line numbers and so the comment and label lines are exdented (lines `[86]` to `[106]`):

```apl
      ∇ R←CR1 CRCOMPARE CR2;A;C;D;F;I;I1;I2;L;M;N1;N2;NL;S;T;U;Z;⎕IO
[1]   ⍝ Compares the canonical representa-
[2]   ⍝ tions (⎕CR) of two similar fns CR1
[3]   ⍝ and CR2 and returns a character
[4]   ⍝ vector (with embedded newlines) of
[5]   ⍝ the differences between the two.
[6]   ⍝
[7]    ⎕IO←0 ⍝ Origin 0 simplifies logic
[8]    R←'' ⍝ Initialise the result
[9]    →(CR1≡CR2)/0 ⍝ Exit if the same
[10]   NL←⎕TC[1] ⍝ Newline (⎕RCNL)
[11]  ⍝ Pad both to the same no. of cols:
[12]   C←0,(1↓⍴CR1)⌈1↓⍴CR2
[13]   N1←1↑⍴CR1←(C⌈⍴CR1)↑CR1
[14]   N2←1↑⍴CR2←(C⌈⍴CR2)↑CR2
[15]   I1←0 ⍝ Row index into CR1
[16]   I2←0 ⍝ Row index into CR2
[17]  ⍝
[18]  ⍝ Grab as many of each as possible:
[19]  LOOP1:I←(N1-I1)⌊N2-I2
[20]  ⍝ Where is next mismatch line?
[21]   I←(∨/CR1[I1+⍳I;]≠CR2[I2+⍳I;])⍳1
[22]   I1←I1+I
[23]   I2←I2+I
[24]  ⍝ Branch if more in CR1:
[25]   →(I1<N1)/L1
[26]  ⍝ Exit if none left in either:
[27]   →(I2=N2)/0
[28]  ⍝ Else remainder in CR2 added:
[29]   L←I2+⍳N2-I2 ⍝ Line numbers
[30]   T←CR2[L;] ⍝ Text of lines
[31]   C←0 ⍝ Class of format (0=add)
[32]   Z←0 ⍝ Return label (exit)
[33]   →FMT ⍝ Branch to format lines
[34]  ⍝
[35]  ⍝ More left in CR1; branch if more
[36]  ⍝ left in CR2:
[37]  L1:→(I2≠N2)/L2
[38]  ⍝ Else remainder in CR1 deleted:
[39]   L←I1+⍳N1[I1 ⍝ Line numbers
[40]   T←CR1[L;] ⍝ Text of lines
[41]   C←1 ⍝ Class of format (1=delete)
[42]   Z←0 ⍝ Return label (exit)
[43]   →FMT ⍝ Branch to format lines
[44]  ⍝
[45]  ⍝ More left in both; 1st rows sof
[46]  ⍝ each are different; search CR2 for
[47]  ⍝ the next line of CR1:
[48]  L2:S←I1 ⍝ This is the starting point
[49]   Z←LOOP1 ⍝ Return label
[50]  LOOP2:I←(((I2,0)↓CR2)∧.=CR1[I1;])⍳1
[51]  ⍝ Branch if found
[52]   →(N2>I2+I)/L3
[53]  ⍝ Iterate if some rows left in CR1:
[54]   →(N1>I1←I1+1)/LOOP2
[55]  ⍝
[56]  ⍝ Branch unless 1st CR1 row matches:
[57]  L3:→(S≠I1)⍴L4
[58]  ⍝ CR2 lines have been added:
[59]   L←I2+⍳I ⍝ Line numbers
[60]   T←CR2[L;] ⍝ Text of lines
[61]   C←0 ⍝ Class of format (0=add)
[62]  ⍝ Increment counters for return:
[63]   I1←I1+1
[64]   I2←I2+I+1
[65]   →FMT ⍝ Branch to format lines
[66]  ⍝
[67]  ⍝ CR1 lines have been deleted:
[68]  L4:L←S+⍳I1-S ⍝ Line numbers
[69]   T←CR1[L;] ⍝ Text of lines
[70]  ⍝ Branch unless 1st CR2 row matches:
[71]   →(I≠0)/L5
[72]   C←1 ⍝ Class of format (1=delete)
[73]  ⍝ Increment counters for return:
[74]   I1←I1+1
[75]   I2←I2+I+1
[76]   →FMT ⍝ Branch to format lines
[77]  ⍝
[78]  ⍝ A later line in CR1 matches a
[79]  ⍝ later line in CR2 (or no match):
[80]  L5:C←2 ⍝ Class of format (2=replace)
[81]   M←I2+⍳I ⍝ Line numbers in CR2
[82]   U←CR2[M;] ⍝ Text of lines
[83]  ⍝ Increment counter for return:
[84]   I2←I2+I
[85]  ⍝
[86]  ⍝ Format here, line numbers first,
[87]  ⍝ right justified w/ right brackets:
[88]  FMT:L←(((3⌈⍴⍕⌈/L),0)⍕((⍴L),1)⍴L),']'
[89]  ⍝ Left justified, with both brackets
[90]  ⍝ and newline:
[91]   L←NL,'[',(L+.=' ')⌽L
[92]  ⍝ Characters that may begin labels:
[93]   A←'ABCDEFGHIJKLMNOPQRSTUVWXYZ∆abcdefghijklmnopqrstuvwxyz⍙'
[94]  ⍝ Other characters within labels:
[95]   D←'0123456789_'
[96]  ⍝ First character in each line:
[97]   F←T[;0]
[98]  ⍝ Flag comment of label lines:
[99]   D←(F='⍝')∨(F∊A)∧∨/(T=':')∧<\~T∊A,D
[100] ⍝ De-indent comment or label lines
[101] ⍝ and include line numbers:
[102]  T←L,D⌽' ',T
[103] ⍝ Squeeze out trailing blanks
[104]  T←(,⌽∨\' '≠⌽T)/,T
[105] ⍝ Brance by class of format:
[106]  →(L6,L7,L8,L9)[C]
[107] ⍝
[108] ⍝ Add (C=0):
[109] L6:R←R,T,NL,'---- added ----',NL
[110]  →Z
[111] ⍝ Delete (C=1):
[112] L7:R←R,T,NL,'---- deleted ----',NL
[113]  →Z
[114] ⍝ Replace (C=2):
[115] L8:R←R,T,NL,'---- replaced by ----'
[116]  L←M ⍝ Line no.s in CR2
[117]  T←U ⍝ Text of lines
[118]  C←3 ⍝ Class of format (end of repl)
[119]  →FMT
[120] ⍝ End of replace (C=3):
[121] L9:R←R,T,NL
[122]  →Z
      ∇
```

The trickiest part of the `VRCOMPARE` function is, well, all of it:

```apl
      ∇ R←VR1 VRCOMPARE VR2;I;I1;I2;E;EL1;EL2;J;L;N;N1;N2;NB1;NB2;NL;NL1;NL2;PL1;PL2;PL
USIOTA;S;T;U;Z;⎕IO
[1]   ⍝ Compares the visual representa-
[2]   ⍝ tions (⎕VR) of two similar fns VR1
[3]   ⍝ and VR2 and returns a character
[4]   ⍝ vector (with embedded newlines) of
[5]   ⍝ the differences between the two.
[6]   ⍝
[7]    ⎕IO←0 ⍝ Origin 0 simplifies logic
[8]    R←'' ⍝ Initialise the result
[9]    →(VR1≡VR2)/0 ⍝ Exit if the same
[10]   NL←⎕TC[1] ⍝ Newline (⎕TCNL)
[11]  ⍝ Define local function A PLUSIOTA L
[12]  ⍝ that returns (A[1]+⍳L[1]),
[13]  ⍝ (A[2]+⍳L[2]), and so on:
[14]   T←⎕FX 3 15⍴'R←A PLUSIOTA L
                 R←L/A-¯1↓0,+\L
                 R←R+⍳⍴R        '
[15]  ⍝
[16]  ⍝ Find where lines begin and end;
[17]  ⍝ consider just the important chars
[18]  ⍝ (newlines, or nonblanks after a
[19]  ⍝ blank or right bracket):
[20]   NL1←VR1=NL
[21]   I←NL1∨(VR1∊'∇ ')<0,¯1↓VR1∊'∇ ]'
[22]   I←I/⍳⍴I ⍝ Bits to indices
[23]   NL1←NL1[I] ⍝ Which are newlines?
[24]  ⍝ Flag NLs starting nonempty lines:
[25]   N←NL1>1↓NL1,1
[26]  ⍝ ... & of NLs that end those lines
[27]  ⍝ (including the end of line [0]):
[28]   E←(NL1\¯1↓1,NL1/N)/I
[29]  ⍝ Inds(+1) of NLs that start lines:
[30]   NL1←0,1+N/I ⍝ 0 to begin line [0]
[31]  ⍝ Inds of 1st nonblanks per line:
[32]   NB1←(1,¯1↓N)/I
[33]  ⍝ Lengths of entire lines (with
[34]  ⍝ trailing newline):
[35]   EL1←1+E-NL1
[36]  ⍝ Lenghts of lines without line no.s
[37]  ⍝ (and without newlines):
[38]   PL1←E-NB1
[39]  ⍝
[40]  ⍝ Do the same for VR2:
[41]   NL2←VR2=NL
[42]   I←NL2∨(VR2∊'∇ ')<0,¯1↓VR2∊'∇ ]'
[43]   I←I/⍳⍴I
[44]   NL2←NL2[I]
[45]   N←NL2>1↓NL2,1
[46]   E←(NL2\¯1↓1,NL2/N)/I
[47]   NL2←0,1+N/I
[48]   NB2←(1,¯1↓N)/I
[49]   EL2←1+E-NL2
[50]   PL2←E-NB2
[51]  ⍝
[52]   N1←⍴NL1 ⍝ Number of lines of each
[53]   N2←⍴NL2
[54]   I1←0 ⍝ Line index into each
[55]   I2←0
[56]  ⍝
[57]  ⍝ Grab as many of each as possible:
[58]  LOOP1:N←(N1-I1)⌊N2-I2
[59]  ⍝ But only if they have same length:
[60]   →(0=N←+/∧\PL1[I1+⍳N]=PL2[I2+⍳N])/L2
[61]  ⍝ Compare next N lines:
[62]   L←PL1[I1+⍳N] ⍝ Their lengths
[63]   I←VR1[NB1[I1+⍳N]PLUSIOTA L]≠VR2[NB2[I2+⍳N]PLUSIOTA L]
[64]   →(∨/I)↓L1 ⍝ Branch if all the same
[65]  ⍝ Where is the next mismatch line?
[66]   N←((I⍳1)<+\L)⍳1
[67]  L1:I1←I1+N
[68]   I2←I2+N
[69]  ⍝ Branch if more in VR1:
[70]  L2:→(I1<N1)/L3
[71]  ⍝ Exit if none left in either:
[72]   →(I2=N2)/0
[73]  ⍝ Else remainder in VR2 added:
[74]   I←I2+⍳N2-I2 ⍝ Line indices
[75]   L←EL2[I] ⍝ ...and line lengths
[76]  ⍝ Text of lines:
[77]   T←VR2[NL2[I]PLUSIOTA L]
[78]   Z←0 ⍝ Return label (exit)
[79]   →ADD
[80]  ⍝
[81]  ⍝ More left in VR1; branch if more
[82]  ⍝ left in VR2:
[83]  L3:→(I2≠N2)/L4
[84]  ⍝ Else remainder in VR1 deleted:
[85]   I←I1+⍳N1-I1 ⍝ Line indices
[86]   L←EL1[I] ⍝ ...and line indices
[87]  ⍝ Text of lines
[88]   T←VR1[NL1[I]PLUSIOTA L]
[89]   Z←0 ⍝ Return label (exit)
[90]   →DEL
[91]  ⍝
[92]  ⍝ More left in both; 1st lines of
[93]  ⍝ each are different; search VR2 for
[94]  ⍝ the next line of VR1.
[95]  L4:S←I1 ⍝ This is the starting point
[96]   Z←LOOP1 ⍝ Return label
[97]  ⍝ Compare just lines of same length
[98]  LOOP2:L←PL1[I1]
[99]   E←L=I2↓PL2
[100]  I←(E\VR2[NB2[I2+E/⍳⍴E]∘.+⍳L]∧.=VR1[NB1[I1]+⍳L])⍳1
[101] ⍝ Branch if found
[102]  →(N2>I2+I)/L5
[103] ⍝ Iterate if some lines left in VR1:
[104]  →(N1>I1←I1+1)/LOOP2
[105] ⍝
[106] ⍝ Branch unless 1st VR1 row matches:
[107] L5:→(S≠I1)⍴L6
[108] ⍝ VR2 lines have been added:
[109]  J←I2+⍳I ⍝ Line indices
[110]  L←EL2[J] ⍝ ...and line lengths
[111] ⍝ Text of lines:
[112]  T←VR2[NL2[J]PLUSIOTA L]
[113] ⍝ Increment counters for return:
[114]  I1←I1+1
[115]  I2←I2+I+1
[116]  →ADD
[117] ⍝
[118] ⍝ VR1 lines have been deleted:
[119] L6:J←S+⍳I1-S ⍝ Line indices
[120]  L←EL1[J] ⍝ ..and line lengths
[121] ⍝ Text of lines:
[122]  T←VR1[NL1[J]PLUSIOTA L]
[123] ⍝ Branch unless 1st VR1 row matches:
[124]  →(I≠0)⍴L7
[125] ⍝ Increment counters for return
[126]  I1←I1+1
[127]  I2←I2+I+1
[128]  →DEL
[129] ⍝
[130] ⍝ A later line in VR1 matches a
[131] ⍝ later line in VR2 (or no match):
[132] L7:J←I2+⍳I ⍝ Line indices in VR2
[133]  L←EL2[J] ⍝ ...and line lengths
[134] ⍝ Text of lines:
[135]  U←VR2[NL2[J]PLUSIOTA L]
[136] ⍝ Increment counter for return:
[137]  I2←I2+1
[138] ⍝
[139]  R←R,NL,T,'---- replaced by ----'
[140]  R←R,NL,U
[141]  →Z
[142] ⍝
[143] ⍝ Add:
[144] ADD:R←R,NL,T,'---- added ----',NL
[145]  →Z
[146] ⍝ Delete (C=1):
[147] DEL:R←R,NL,T,'---- deleted ----',NL
[148]  →Z
      ∇
```

Jim Weigang pointed out several potential problems with the (relatively) straight-forward approach presented above. To illustrate one such problem, try moving a line from `[20]` to `[10]`. What do you get? The try moving it from `[10]` to `[20]`. Now what? Jim offered algorithms and code for overcoming some of these problems, but the solutions are beyond the scope of this quarter’s newsletter.
