---
title: Letters on String Manipulations in APL
authors:
- Alan Sykes
volume: '7'
issue: '3'
page: '19'
unindexed: true
transcribed: 'from page images of VOL.7-NO.3-JANUARY-1991.pdf, pages 25–29 (printed 19–23; within The Education Vector, after its introduction on p.17, before An APL SCRIPT Function); Claude, 2026-10-11'
review: draft
tags:
- education
- programming techniques
queries:
- "No byline is printed; Alan Sykes, editor of The Education Vector, writes in the first person, introducing readers’ letters from Bill McLean (Dunoon), Bill Smith, L Llewellyn-Jones and Gerard Langlet."
- "The listings are printed in an italic APL font. The quote-quad is transcribed ⍞, the execute glyph ⍎ and the format glyph ⍕."
- "DOW [1] is printed `M←12⍴ 7 31 30` (read at 800 dpi); a month-length vector would need `12⍴7⍴31 30`. Kept as printed. In DOW [2] the residue is followed by a second stile, `||R`."
- "In REPLACEIN [4] the second `¯1` (in `T[,L∘.+¯1++\\I⍴1]`) is printed with a mark like a dieresis over the high minus; transcribed ¯."
- "The REPLACEIN example is printed with the result THE HORSE SAT ON THE MAT AND I JUMPED ON THIS HORSE, although the left argument also asks MAT→GRASS and THE→MY; the functions as transcribed give MY HORSE SAT ON MY GRASS … in Dyalog. Kept as printed."
- "Kept as printed: “ADD al ine to the End of the pad” (in the menu and in MENU [8]); WRITE TO ALISON. ROBERT. ALASTAIR in PAD but with commas in SHOW; SEND QA and REOPRT in the INSERT example; SENS WS in the REWRITE example; the menu shown first lacks the MOVE line that MENU [6] has."
---

My recent series of articles on string manipulation has resulted in a number of letters from readers of Education Vector, and I am grateful for all who took the trouble to write to me. Here are some thoughts from home and abroad.

## 1. A Jotter-Notepad

Bill McLean from Dunoon sent me a set of APL functions that allow you to create and edit a set of notes, being a matrix called PAD. Here is his description of its use and the function listings.

```apl
      MENU

Use the following command words to run the JOTTER program

SHOW.... to see the up-to-date JOTTER pad
CREATE.. to create a NEW jotter pad
DELETE.. to remove a line from the pad
ADDB.... ADD a line to the Beginning of the pad
ADDE.... ADD al ine to the End of the pad
INSERT.. insert a line after a given line
REWRITE. rewrite a line
MENU.... to get this menu

      PAD
SEND WS TO DR SYKES
WRITE TO ALISON. ROBERT. ALASTAIR
SCOTVEC MODULES
REPORT LINES FOR COMPUTER
S3 TESTS

      SHOW
1SEND WS TO DR SYKES
2WRITE TO ALISON, ROBERT, ALASTAIR
3SCOTVEC MODULES
4REPORT LINES FOR COMPUTER
5S3 TESTS

      DELETE
Delete which line?
⎕:
      2
1SEND WS TO DR SYKES
2SCOTVEC MODULES
3REPORT LINES FOR COMPUTER
4S3 TESTS

      ADDE
Type the jotting
WRITE TO FAMILY
1SEND WS TO DR SYKES
2SCOTVEC MODULES
3REPORT LINES FOR COMPUTER
4S3 TESTS
5WRITE TO FAMILY

      INSERT
AFTER WHICH LINE WILL WE INSERT
⎕:
      1
Type in the jotting
PHONE BROTHER ROBERT, JOHN
1SEND QA TO DR SYKES
2PHONE BROTHER ROBERT, JOHN
3SCOTVEC MODULES
4REOPRT LINES FOR COMPUTER
5S3 TESTS
6WRITE TO FAMILY

      REWRITE
Which line is to be rewritten?
⎕:
      4
Type the new jotting
ATTITUDE AND HOMEWORK :TWO LINES FOR S3 REPORTS
1SENS WS TO DR SYKES
2PHONE BROTHER ROBERT, JOHN
3SCOTVEC MODULES
4S3 TESTS
5WRITE TO FAMILY
```

```apl
      ∇ADDB[⎕]∇
      ∇SCREEN←ADDB;LINE;X;ORDER
[1]'Type the jotting'
[2] LINE←1 40⍴X←40↑⍞
[3] ORDER←((1+1↑⍴PAD),1)⍴⍳1+1↑⍴PAD
[4] PAD←LINE,[1]PAD
[5] SCREEN←(⍕ORDER),PAD
      ∇

      ∇ADDE[⎕]∇
      ∇SCREEN←ADDE;LINE;X;ORDER
[1] 'Type the jotting'
[2] LINE←1 40⍴X←40↑⍞
[3] ORDER←((1+1↑⍴PAD),1)⍴⍳1+1↑⍴PAD
[4] PAD←PAD,[1] LINE
[5] SCREEN←(⍕ORDER),PAD
      ∇

      ∇CREATE[⎕]∇
      ∇CREATE
[1] 'Input each line, up to 40 characters'
[2] 'End with a <RET> for each line'
[3] 'End with TWO <RET> at the end of the notes'
[4] PAD←MAT 40
      ∇

      ∇DELETE[⎕]∇
      ∇SCREEN←DELETE;ORDER;X;Y;Z;LINE
[1] 'Delete which line?'
[2] X←⎕
[3] Z←X≠⍳1↑⍴PAD
[4] PAD←Z/[1]PAD
[5] ORDER←((1↑⍴PAD),1)⍴⍳1↑⍴PAD
[6] SCREEN←(⍕ORDER),[2]PAD
      ∇

      ∇INSERT[⎕]∇
      ∇SCREEN←INSERT;LINE;Z;X;ORDER
[1]'AFTER WHICH LINE WILL WE INSERT?'
[2]X←⎕
[3]'Type in the jotting'
[4]LINE←1 40⍴Y←40↑⍞
[5]Z←(X=⍳(1↑⍴PAD))+(1↑⍴PAD)⍴1
[6]PAD←Z/[1]PAD
[7]PAD[X+1;]←LINE
[8]ORDER←((1↑⍴PAD),1)⍴⍳1↑⍴PAD
[9]SCREEN←(⍕ORDER),[2]PAD
      ∇

      MAT:
MAT:(⍵↑V),[1] MAT ⍵:0=⍴V←⍞:(0,⍵)⍴''

      ∇MENU[⎕]∇
      ∇MENU
[1]'Use the following command words to run the JOTTER program'
[2]''
[3]'SHOW.... to see the up-to-date JOTTER pad'
[4]'CREATE.. to create a NEW jotter pad'
[5]'DELETE.. to remove a line from the pad'
[6]'MOVE.... moves a line from one row to another'
[7]'ADDB.... ADD a line to the Beginning of the pad'
[8]'ADDE.... ADD al ine to the End of the pad'
[9]'INSERT.. insert a line after a given line'
[10]'REWRITE. rewrite a line'
[11]'MENU.... to get this menu'

      ∇MOVE[⎕]∇
      ∇SCREEN←MOVE;LINE;X;Y;Z;ORDER
[1]'Move which line?'
[2]X←⎕
[3]LINE←1 40⍴PAD[X;]
[4]Z←X≠⍳1↑⍴PAD
[5]PAD←Z/[1]PAD
[6]ORDER←((1↑⍴PAD),1)⍴⍳1↑⍴PAD
[7]⎕←SCREEN←(⍕ORDER),[2]PAD
[8]'To put AFTER which line?'
[9]Y←⎕
[10]Z←(Y=⍳1↑⍴PAD)+(1↑⍴PAD)⍴1
[11]PAD←Z/[1]PAD
[12]PAD[Y+1;]←LINE
[13]ORDER←((1↑⍴PAD),1)⍴⍳1↑⍴PAD
[14]SCREEN←(⍕ORDER),[2]PAD
      ∇

      ∇REWRITE[⎕]∇
      ∇SCREEN←REWRITE;LINE;X;Y;ORDER
[1]'Which line is to be rewritten'
[2]X←⎕
[3]'Type the new jotting'
[4]LINE←1 40⍴Y←40↑⍞
[5]PAD[X;]←LINE
[6]ORDER←((1↑⍴PAD),1)⍴⍳1↑⍴PAD
[7]SCREEN←(⍕ORDER),PAD
      ∇

      ∇SHOW[⎕]∇
      ∇SCREEN←SHOW;ORDER
[1]ORDER←((1↑⍴PAD),1)⍴⍳1↑⍴PAD
[2]SCREEN←(⍕ORDER),[2]PAD
      ∇
```

## 2. A Correction From Bill Smith

Bill Smith wrote to tell me that I missed a sentence out of his note on ‘dBase Files and Lotus Files into I-APL’ published in the October edition of Education Vector. (My Apologies.) The corrected paragraph reads as follows.

‘dBaseIII files, output with a COPY TO &lt;filename&gt; TYPE SDF command, yield a series of fixed length records in ASCII format. Lotus spreadsheets, ‘databases’ at least, printed to file result in .PRN files with one record per row in ASCII format. These are only fixed length if the right-most field of each row is of the same size but this is easily managed even if you have to create a dummy column to achieve it. A further problem with Lotus files is that they are preceded by a number of carriage returns/line feed characters which need to be disposed of in the first stages of transfer; actually in the DREAD function.’

## 3. Day-of-Week Algorithm

I am grateful to L Llewellyn-Jones of London for sending me a copy of an article by Bhairav Joshi published in COMPUTERWORLD (January 14 1980) who explains the mathematics of calculating the day of the week from the date. The article is easy to follow and also includes an APL program. Unfortunately I am unable to include the article in this column but will supply copies to any interested reader who cares to provide a stamped-addressed envelope. However, here is the supplied function:

```apl
     ∇ R←DOW D;M;R;T
[1]    M←12⍴ 7 31 30
[2]    M[2]←28+-/0=(T← 4 100 400 4000)||R←2↓D
[3]    R←R+-/⌊(¯1+|R)÷T, 1000 2000
[4]    R←1+7|¯1+R+D[2]++/(¯1+1↑D)↑M
[5]    R←(7 9 ⍴'SATURDAY SUNDAY MONDAY TUESDAY WEDNESDAYTHURSDAY
     FRIDAY ')[R;]
     ∇
```

## 4. Replacing Strings

Gerard Langlet sent me lots of comments regarding string searching including `SS4` below which is ‘short and fast enough to help those people whose APL interpreter does not have a system function `⎕SS` for string searching’

```apl
     ∇R←S SS4 T;C;L;N
[1]    R←T=1↑S ⋄ R←R/⍳⍴R ⋄ T←T,1↑⎕AV ⋄ L←⍴S←1↓S ⋄
     C←L×⍴N←'C←T[R←R+1]=1↑S ⋄ R←C/R⋄S←1↓S⋄' ⋄ ⍎C⍴N ⋄ R←R-L
     ∇
```

He also sent me a string replacement programme which no doubt is extremely efficient, but unfortunately is not very easy to understand. Nevertheless I present it to you together with a more pedestrian version of my own which is intended for those readers who prefer to work through a program knowing something of the strategy behind its construction.

```apl
     ∇ ∆E do ∆N
[1]    ∆N←∆N×⍴∆E←∆E,'⋄' ⋄ ⍎∆N⍴∆E
     ∇

     ∇ T←S REPLACEIN T;A;B;C;D;E;I;J;K;L;M;N;U;a;b;c;d
[1]    a←'N←0<E←⍴A←B⋄M←1+L←+/∧\S≠C⋄E←E-⍴B←L↑S⋄S←M↓S'
[2]    b←'K←U[L←L+1]=1↑A⋄L←K/L⋄A←1↓A'
[3]    c←'L←T=1↑A⋄L←L/⍳⍴L⋄U←T,1↑⎕AV⋄b do D←⍴A←1↓A⋄J←⍴L←L-
D⋄K←⍴T⋄K←K⍴1⋄I←0=K[L]←0⌈1-E'
[4]    c←c,'⋄N←0⌈E⋄K[,L∘.+¯1++\N⍴1]←0⋄T←K/T⋄L←L-
E×¯1++\J⍴1⋄K←J×I←⍴B⋄T[,L∘.+¯1++\I⍴1]←K⍴B'
[5]    d←'a do 2⋄c do N'
[6]    d do ⌈0.5×S+.=B←C←'/'
     ∇

      'CAT/HORSE/MAT/GRASS/THE/MY' REPLACEIN 'THE CAT SAT ON THE
MAT AND I JUMPED ON THIS CAT'

THE HORSE SAT ON THE MAT AND I JUMPED ON THIS HORSE
```
