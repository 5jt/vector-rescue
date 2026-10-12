---
title: Zark Newsletter Extracts
authors:
- Jon Sandles
volume: '16'
issue: '2'
page: '33'
unindexed: true
transcribed: 'from page images of VOL.16-NO.2-OCTOBER-1999.pdf, pages 35–39 (printed 33–37); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
queries:
- "Printed byline “Introduced by Jon Sandles”; the Contents line gives “edited by Jon Sandles”. The extract comprises Jon Sandles’s introduction with Anne D Wilson’s looping solution to FNTREE (TEST and DOING), and the Limbering Up column “Identifiers Within Functions”. The lower half of printed 37 is a BAA house notice, “Vector Back Numbers” (from the British APL Association, c/o Gill Smith, with prices), not transcribed; the crossword on printed 38 has its own Contents line."
- "TEST and DOING were run in Dyalog APL as a check on the transcription (with the label θ10 renamed, as Dyalog does not accept θ in a label); they run without error and draw a box tree of the test relations. The printed function shows no output, so only the absence of errors was checked."
- "In DOING the header is printed over two lines, and the comment “⍝ Must slot in the correct order” stands unnumbered between lines [18] and [19]; both kept as printed. The line above the header reads “∇DOING∇”, as printed."
- "Kept as printed: “infromation” (DOING[4]); “In last issues’s”; “a utility function name FNTREE”; “the subfunctions call by”; “couldn’t possibly by the name”; “The write the ANALYSE function”; “Each of the six global variables are”."
---

*Introduced by Jon Sandles*
{ .byline }

A few Vectors back we asked you to write FNTREE which displays a tree diagram of function calls. Following Anne Wilson’s letter concerning the recommended solution to the FNTREE problem, and in particular the use of recursive calls, I asked her to send through a looping solution:

```apl
      ∇ RC←TEST
[1]     RELATIONS←12 2⍴1 7 1 1 10 1 1 2 2 2 2 1 2 3 2 4 2 5 5 6 7 3 8 4 8 5
[2]     RELATIONS←RELATIONS,[1]9 2⍴8 5 7 4 7 6 7 8 7 5 7 9 9 10 1 11 11 4
[3]     RELATIONS←RELATIONS,[1]4 2⍴11 12 1 13 2 4 2 5
[4]     NAMES←8 6⍴'EMPLS SELECTCINPUTIF    MSG   UNLESSADDEMPNINPUT'
[5]     NAMES←NAMES,[1]5 6⍴'CATEMPRCAT  DELEMOSQZEMPLSTEMP'
[6]     RC←RELATIONS DOING NAMES
      ∇
∇DOING∇
      ∇ RC←RLTNS DOING NAMES;BOX;FIRST;I;J;L;LEV;NGI;PC;RCX;S;SH;SUB;T;TERM;
       USED;V0;V1;XPND
[1]     ⍝ Anne D Wilson   June 1999
[2]     ⍝
[3]     ⍝  First order nodes into correct printing order
[4]     ⍝  Use their LEVEL to convey infromation
[5]     RC←0
[6]     USED←(1↑⍴RLTNS)⍴0    ⍝ To keep track of nodes already processed
[7]     LEV←1⍴1    ⍝ Start with root node's data already there
[8]     PC←1⍴1     ⍝ or wherever the node's parent is in the name list
[9]     L←1        ⍝ Find nodes at level L+1
[10]  θ10:
[11]    NGI←RLTNS[;1]∊(LEV=L)/PC          ⍝ NGI - indices of Next Generation
[12]    NGI←NGI∧~USED
[13]    USED←USED∨NGI                     ⍝ Only expand subtrees once
[14]    NGI←NGI/⍳⍴NGI
[15]    NGI←NGI[⍋PC⍳RLTNS[NGI;1]]
[16]    I←(⍳⍴PC),PC⍳RLTNS[NGI;1] ⋄ I←I[⍋I] ⋄ XPND←I≠¯1↓0,I
[17]    LEV←XPND\LEV ⋄ LEV←LEV+(~XPND)×L+1 ⍝ Set up level numbers
[18]    PC←XPND\PC ⋄ PC←PC+(~XPND)\RLTNS[NGI;2]
      ⍝ Must slot in the correct order
[19]    L←L+1
[20]    →((⍴PC)<1+1↑⍴RLTNS)/θ10          ⍝ Loop until all input processed
[21]    ⍝
[22]    TERM←LEV≥1↓LEV,0         ⍝ Terminal nodes
[23]    FIRST←(PC⍳PC)=⍳⍴PC       ⍝ First occurrence of nodes
[24]    ⍝
[25]    ⍝ Picture   - Boxes + lines
[26]    BOX←4 14
[27]    RC←4⌽(((⍴PC),BOX[2]-¯1↑⍴NAMES)⍴' |   -| '),[2]NAMES[PC;]
[28]    RCX←((⍴PC),BOX[2])⍴BOX[2]↑'  |--------|'
[29]    I←(TERM∧~FIRST)/⍳⍴TERM ⋄ RC[I;BOX[2]+¯1 0]←((⍴I),2)⍴'-+'
[30]    I←(FIRST∧~TERM)/⍳⍴TERM ⋄ RC[I;BOX[2]+¯1 0]←((⍴I),2)⍴'--'
[31]    RC←((BOX[1]×⍴PC),BOX[2])⍴RCX,RC,RCX,((⍴PC),BOX[2])⍴' '
[32]    I←⍴RC←(-BOX[2]×BOX[1]/LEV-1)⌽((BOX[2]×⌈/LEV)↑BOX[2]⍴1)\[2]RC
[33]    ⍝ Vertical lines
[34]    SH←⍴S←(((⌈/LEV),(⍴LEV))⍴LEV) ⋄ S←,(S-⍉(⌽SH)⍴⍳⌈/LEV)
[35]    J←,⌽SH⍴(1=S)×(SUB←+\0=S)       ⍝ J has positions of children ie lev+1
[36]    V1←J⍳⍳⌈/J ⍝ Youngest
[37]    V1←SH⊤(V1≤⍴J)/V1 ⍝ of many
[38]    V1[2;]←(SH[2]+1)-V1[2;]
[39]    V1←SH⊥V1
[40]    V0←SH⊤SH[2]+SUB⍳SUB[V1]
[41]    V1←1+(SH⊤V1-1)[2;]
[42]    S←(1+BOX[1]×V0[2;]-1)+(1↑⍴RC)×¯1+BOX[2]×V0[1;]
[43]    T←1+4×V1-V0[2;]
[44]    S←T/S-¯1↓0,+\T ⋄ S←S+⍳⍴S
[45]    RC←,⍉RC ⋄ RC[S]←'|' ⋄ RC←0 2↓⍉(⌽I)⍴RC
      ∇
```

In this following extract we build on FNTREE to produce a genuinely useful utility.

## LIMBERING UP: Identifiers Within Functions

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

In last issues’s LIMBERING UP column, we introduced a utility function name `FNTREE` that displays a tree diagram of the subfunctions (and their subfunctions) called by a specified function in the workspace. The right argument of `FNTREE` is the name of the function to be diagrammed:

```apl
      FNTREE 'EMPLS'
```

The result is a character matrix of the tree diagram. (See the UTILITY CORNER column in this issue for an illustration.) Last issue, you were assigned the task of writing the logic to construct the tree diagram. This issue, you’ll be given the task of analysing a function to spot the names of the subfunctions called by that function. Next issue, we’ll ask you to put it all together and finally write the `FNTREE` function.

The problem of determining the subfunctions call by a specified function is not as simple as it might first appear.

Consider this function:

```apl
      ∇ IND←CHOICES SELECT PROMPT;R
[1]    ⍝ Ask for choice:
[2]    ASK:R←CINPUT PROMPT
[3]    ⍝ Search choices for 1st char of response:
[4]     IND←CHOICES⍳1↑R
[5]    ⍝ Ask again if not a valid choice:
[6]     →ASK IF(IND>⍴CHOICES)MSG'INVALID CHOICE.'
      ∇
```

What are the subfunctions of `SELECT`?

The subfunctions are `CINPUT`, `IF`, and `MSG`. How do you know?

Your eyes scan the lines of the function, starting with line 1. Any name within comments is ignored (e.g. `Ask for choice`). Any name within quotes is ignored (e.g. `INVALID CHOICE`). Any label is ignored (e.g. `ASK:`). Any name that is local is ignored (e.g. `IND` or `PROMPT`). Incidentally, a name is considered local if it’s the result variable (e.g. `IND`), an argument variable (e.g. `CHOICES` or `PROMPT`), a localised variable (e.g. `R`), or a label (e.g. `ASK`).

Any name remaining after all of this ignoring *may* be a subfunction. It may also be a global variable. To find out for sure, you need to look at the names of the other functions in the workspace to see if there’s a match.

Sounds simple? Not really.

Here’s your task: Write a function named `ANALYSE` that accepts a character vector function name and analyses the identifiers within the function specified. (The term “Identifier” is the fancy word for any variable name, function name, or label name.) In particular, the `ANALYSE` function should create six global variables, named `FNS`, `RESULT`, `ARGS`, `LOCALS`, `LABELS`, and `IDS`.

No, we haven’t forgotten our resolve to avoid using global variables. The `ANALYSE` function is not a utility function we’re going to save for posterity. It’s just a temporary repository for algorithms you’ll be needing next issue. Don’t worry. Be happy.

Each of the six global variables are character matrices with one name per row. Short names are left-justified, i.e. padded to the right with blanks.

The variables contain the following names:

| | |
|---|---|
| `FNS` | the names of the functions in the workspace |
| `RESULT` | the name of the result variable (0 rows if none) |
| `ARGS` | the names of the argument variables (0, 1 or 2 rows) |
| `LOCALS` | the names of the variables localised in the header, i.e. preceded by `';'` |
| `LABELS` | the names of the labels, i.e. the names beginning a function line and followed immediately by `':'` |
| `IDS` | the names of all identifiers within the body of the function (all lines but the header), ignoring names within comments or quotes; you may include or ignore label names, at your whim. |

All six character matrices must have the same number of columns, namely as many as the longest name in `FNS`. Any longer name should be omitted, since it couldn’t possibly by the name of a subfunction. Names that begin with the `⎕` symbol, such as `⎕IO` or `⎕PW`, should be omitted. You don’t want to include system variables or system functions in the list of subfunctions.

Here’s an illustration of the `ANALYSE` function:

```apl
      )FNS
ANALYSE   SELECT
      )VARS
                              No variables
      ANALYSE SELECT
      )VARS
ARGS  FNS  IDS  LABELS  LOCALS  RESULT
      ARGS
CHOICES
PROMPT
      FNS
ANALYSE
SELECT
      IDS
ASK
R
CINPUT
PROMPT
IND
CHOICES
R
ASK
IF
IND
CHOICES
MSG
      LABELS
ASK
      LOCALS
R
      RESULT
IND
```

The write the `ANALYSE` function, you need to know about a few system functions, namely `⎕CR` and `⎕NL`. The system function `⎕CR` (Canonical Representation) takes a character vector function name as its right argument and returns a character matrix of the function’s contents, less line numbers, dels (`∇`), and cosmetic indenting:

```apl
      ⎕CR'SELECT'
 IND←CHOICES SELECT PROMPT;R
⍝ Ask for choice:
ASK:R←CINPUT PROMPT
⍝ Search choices for 1st char of response:
 IND←CHOICES⍳1↑R
⍝ Ask again if not a valid choice:
 →ASK IF(IND>⍴CHOICES)MSG'INVALID CHOICE.'
```

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA*
