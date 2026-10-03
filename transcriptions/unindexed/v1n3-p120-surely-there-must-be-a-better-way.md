---
title: Surely There Must Be a Better Way
authors:
- Dave Ziemann
volume: '1'
issue: '3'
page: '120'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 122–124 (printed 120–122; follows the unindexed Technical Correspondence); Claude, 2026-10-03'
review: draft
queries:
- "Underscored letters are written with a combining low line (A̲)."
- "Checks: all three replacements for CURRDEF reproduce the input/output table (⎕IO←1 for the first): `5 6 1 2 5 6[2⊥C]`, `C[2]+4×C[1]≠1`, and `1↓C+⌽4×C≠1` (read at 900 dpi as `1↓`, which gives C[2]+4×C[1]≠1 as a one-element vector)."
- "The usage example calls `UNDERSCORE`, not UNDERSCORE2 or UNDERSCORE3; printed so. UNDERSCORE2’s comments refer to <A> for the argument W; printed so."
---

by Dave Ziemann
{ .byline }

We hope that this section of VECTOR will become an APL noticeboard for those small but tricky problems that one suspects have elegant solutions in APL. The trouble is that it’s not always easy to find these solutions — so if you have a problem like this, send it in to us for publication: maybe someone else can solve it for you! Alternatively, if you see a familiar problem in these pages, let’s see your solution to it — you never know, it might be the best one. In this way we hope to provide a source of APL idioms and algorithms for the APL community. If you do send us some code, please remember to abide by the VECTOR publication standards and try to use that funny little lamp symbol, especially in the first few lines of the functions.

For a first attempt, we will take a rather light-hearted look at what we believe to be two extreme cases of “Surely There Must be a Better Way”. These actual examples were extracted from live applications systems, and indicate possible ways in which APL can get a bad name among the programming languages.

The first is the following uncommented function which was taken from a financial workspace:

```
    ∇ R←CURRDEF;X
[1]    X←CURRENCY
[2]    →(X[1]=0)/COMB
[3]    →(X[1]=1)/STER
[4]    →(X[1]=2)/DOL
[5]   COMB:→(X[2]=1)/CSTER
[6]    →(X[2]=2)/CDOL
[7]   CSTER:R←5
[8]    →0
[9]   CDOL:R←6
[10]   →0
[11]  STER:→(X[2]=1)/SSTER
[12]   →(X[2]=2)/SDOL
[13]  SSTER:R←1
[14]   →0
[15]  SDOL:R←2
[16]   →0
[17]  DOL:→(X[2]=1)/DSTER
[18]   →(X[2]=2)/DDOL
[19]  DSTER:R←5
[20]   →0
[21]  DDOL:R←6
[22]   →0
    ∇
```

By constructing a table of all the possible input/output combinations

```
   | 1  2
---|------
 0 | 5  6
 1 | 1  2
 2 | 5  6
```

it doesn’t take too long to come up with this original solution, for an input VECTOR C:

```
R← 5 6 1 2 5 6 [2⊥C]
```

For those who prefer a more arithmetic approach,

```
R←C[2]+4×C[1]≠1
```

will do the trick. If you like an origin-independent solution, then the following is for you:

```
R←1↓C+⌽4×C≠1
```

In generating these alternatives, we should not forget the value of using APL comment lines to explain WHAT it is we are trying to do. For lines of code that are non-obvious, a further comment explaining how this is being achieved is also a good idea.

Our second example is this remarkable function for replacing non-underscored alphabetics by their equivalent underscored characters:

```
    ∇ R←UNDERSCORE1 VECTOR
[1]   VECTOR[POSITION VECTOR='A']←'A̲'
[2]   VECTOR[POSITION VECTOR='B']←'B̲'
[3]   VECTOR[POSITION VECTOR='C']←'C̲'
[4]   VECTOR[POSITION VECTOR='D']←'D̲'
[5]   VECTOR[POSITION VECTOR='E']←'E̲'
[6]   VECTOR[POSITION VECTOR='F']←'F̲'
[7]   VECTOR[POSITION VECTOR='G']←'G̲'
[8]   VECTOR[POSITION VECTOR='H']←'H̲'
[9]   VECTOR[POSITION VECTOR='I']←'I̲'
[10]  VECTOR[POSITION VECTOR='J']←'J̲'
[11]  VECTOR[POSITION VECTOR='K']←'K̲'
[12]  VECTOR[POSITION VECTOR='L']←'L̲'
[13]  VECTOR[POSITION VECTOR='M']←'M̲'
[14]  VECTOR[POSITION VECTOR='N']←'N̲'
[15]  VECTOR[POSITION VECTOR='O']←'O̲'
[16]  VECTOR[POSITION VECTOR='P']←'P̲'
[17]  VECTOR[POSITION VECTOR='Q']←'Q̲'
[18]  VECTOR[POSITION VECTOR='R']←'R̲'
[19]  VECTOR[POSITION VECTOR='S']←'S̲'
[20]  VECTOR[POSITION VECTOR='T']←'T̲'
[21]  VECTOR[POSITION VECTOR='U']←'U̲'
[22]  VECTOR[POSITION VECTOR='V']←'V̲'
[23]  VECTOR[POSITION VECTOR='W']←'W̲'
[24]  VECTOR[POSITION VECTOR='X']←'X̲'
[25]  VECTOR[POSITION VECTOR='Y']←'Y̲'
[26]  VECTOR[POSITION VECTOR='Z']←'Z̲'
[27]  R←VECTOR
    ∇

    ∇ R←POSITION B
[1]    R←B/⍳⍴B
    ∇
```

Of course, the same effect could be achieved by looping through each letter of the alphabet, but the absence of a loop in this function may be an indication that the author once heard that looping in APL was inefficient! Because the function only works on vectors, function fragments of the following kind are found elsewhere in the workspace:

```
       .
       .
[24]   LARGEMAT[1;]←UNDERSCORE1,LARGEMAT[1;]
[25]   LARGEMAT[3;]←UNDERSCORE1,LARGEMAT[3;]
[26]   LARGEMAT[6;]←UNDERSCORE1,LARGEMAT[6;]
[27]   LARGEMAT[11;]←UNDERSCORE1,LARGEMAT[11;]
[28]   LARGEMAT[14;]←UNDERSCORE1,LARGEMAT[14;]
[29]   LARGEMAT[15;]←UNDERSCORE1,LARGEMAT[15;]
       .
       .
```

For those of you new to APL a non-looping rank-independent solution can be formulated as follows:

```
    ∇ R←UNDERSCORE2 W;S;I;J
[1]   ⍝ <R> IS CHARACTER ARRAY <A> WITH ALPHABETICS REPLACED BY UNDERSCORES.
[2]   ⍝ METHOD: LOOK UP ALL CHARACTERS AND THEN ONLY REPLACE ALPHABETICS.
[3]    S←⍴W
[4]    R←,W
[5]    I←'ABCDEFGHIJKLMNOPQRSTUVWXYZ'⍳R
[6]    J←(I≠26+⎕IO)/⍳⍴I
[7]    R[J]←'A̲B̲C̲D̲E̲F̲G̲H̲I̲J̲K̲L̲M̲N̲O̲P̲Q̲R̲S̲T̲U̲V̲W̲X̲Y̲Z̲'[I[J]]
[8]    R←S⍴R
    ∇
```

The function can be applied to any rank array, and so can be used on sets of VECTORS in the following way:

```
   .
   .
I←1 3 6 11 14 15
LARGEMAT[I;]←UNDERSCORE LARGEMAT[I;]
   .
   .
```

An alternative function which first restricts the set of characters to the alphabetics, and then maps them to underscored letters can also be written:

```
    ∇ R←UNDERSCORE3 W;S;I;J;A
[1]   ⍝ <R> IS CHARACTER ARRAY <A> WITH ALPHABETICS REPLACED BY UNDERSCORES.
[2]   ⍝ METHOD: RESTRICT SET TO ALPHABETICS, THEN REPLACE BY UNDERSCORES.
[3]    S←⍴W
[4]    R←,W
[5]    I←(R∊A←'ABCDEFGHIJKLMNOPQRSTUVWXYZ')/⍳⍴R
[6]    J←A⍳R[I]
[7]    R[I]←'A̲B̲C̲D̲E̲F̲G̲H̲I̲J̲K̲L̲M̲N̲O̲P̲Q̲R̲S̲T̲U̲V̲W̲X̲Y̲Z̲'[J]
[8]    R←S⍴R
    ∇
```

In many cases this function will run faster than the one above, depending on the interpreter you are using.

These functions were not included as objects of ridicule, but as a reminder for all of us to be very careful when writing APL — given a powerful tool we must demonstrate our control over it, not by abuse, but by careful application and, occasionally, restraint. Hopefully these examples will inspire us all to improve the quality of our APL code.
