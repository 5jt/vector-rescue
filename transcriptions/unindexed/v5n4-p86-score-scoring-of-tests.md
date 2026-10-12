---
title: 'SCORE: An APL Program for the Scoring of Tests'
authors:
- Jerry M. Brennan
- Jennifer E. Daly
volume: '5'
issue: '4'
page: '86'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, pages 88–94 (printed 86–92); Claude, 2026-10-12'
review: draft
tags:
- applications
- mathematics and statistics
queries:
- "Contents line “Standardised Test Scores”, by Jerry Brennan; the printed heading is “SCORE: An APL Program for the Scoring of Tests”, by Jerry M. Brennan and Jennifer E. Daly. The piece ends on printed 92; printed 93 carries only the TECHNICAL SECTION introduction."
- "Function and variable names set in a smaller code face in the prose are given as code. Lower-case letters in names (sSSHAPE, sSINDEX, Ns, Nf, NXTs, NXTf, nUM, oK, rEC, Nr) are as printed; they probably stand for APL*PLUS underscored letters. The code mixes sSINDEX and SSINDEX, NF and Nf, oK (label) and OK (branch), NR (header) and Nr — all kept as printed."
- "Code glyphs: ◇ is transcribed ⋄, the boxed quote as ⍞, the execute glyph as ⍎, the format glyph as ⍕, the empty-vector glyph in RECODE [4] as ⍬. In SCORE [11] and RECODE [5] the arrows in “⍳Ns←S+1” and “⍳Nr←N+1” are read as assignment, as printed (a less-than seems intended)."
- "RECODE [1]: “Recode data D_from S” — an underscore is printed between D and from; kept."
- "Kept as printed: “'¤' delimits items and their weights” although the examples use $; “This test has three factors labeled ONE, TWO, THREE, and FOUR”; “CRTL-E”; “Item 1 is punched 1, 2 ,3”; “returns to nXT for the next subject” (the label is NXTs)."
- "The author’s university department address is kept as an institutional address."
---

*by Jerry M. Brennan and Jennifer E. Daly*
{ .byline }

## Introduction

Score is a general purpose program for the scoring of tests. The program scores data according to a key that is customised by the user, and options exist for keyed, reversed, and weighted scoring of data.

Detailed instructions for the program (a printout of these is included as an Appendix) can be accessed anytime by the user. Two methods of input are allowed:

1. Interactive input, where the user is queried for up to 512 (including blanks) elements of data.
2. Batch input, which allows for a virtually unlimited amount of data.

Output includes the scoring key(s), subject identification, input vector, total number of elements entered, and scores for all the factors (i.e. each scoring scale).

Score has three advantages:

- the program is flexible, with uncomplicated, customised keys that allow scoring of an unlimited number of items and factors.
- data can be scored in a variety of ways by changing the keys and rescoring.
- large sets of scoring keys for different tests (e.g. batteries) can be compactly stored and easily retrieved for future use.

## Score in APL

`SCORE` is a dyadic function with both arguments containing segmented character strings. The right argument `KEY` contains the scoring key. This argument requires a major segment for each scale and optional minor segments for special scoring features of each scale. The optional left argument `DATA` contains subject identification and item responses for each subject.

If `DATA` contains no elements, `SCORE` reads data interactively and the user is prompted to enter subject identification and item responses. In this mode the major segments of the `KEY` argument (i.e. each scoring key) as well as each scale in `KEY` and `DATA` (or, if interactive, each subject entry) are separated by a carriage return. Thus, for input, each subject's data and each scoring key for that data is entered on a new line. Each minor segment within the scoring key and within the data set is separated by '/'.

Two main functions are used for scoring: `SCORE` and `RECODE`. `SCORE` is the primary function that calls `RECODE` if recoding of data is done. In addition, two one-line utility functions, `sSINDEX` and `sSSHAPE`, are also used. For all functions, the variable DATA contains all subjects' data, and `SCORE` loops through `DATA` for each subject. Within `SCORE`, the variable D contains data for one subject and `F` is a counter indicating which factor is being calculated. Similarly `Nf` is the number of factors contained in `KEY`, `S` is the subject loop counter, and `Ns` contains the number of subjects stored in `DATA`.

```apl
      DATA SCORE KEY;INT;D;Ns;NF;F;S;T;V;VALS;⎕ELX
      --------------------------------------------

[1]   ⍝ Key is segmented string (e.g., 'ONE/1 2/1/0'). Each scale
[2]   ⍝ is separated by ⎕TCNL & "/" separates fields in a scale.
[3]   ⍝ Fields: 1=scale name 2=items 3=multiplier 4=add.
[4]   ⍝ DATA is the optional left argument of a character vector
[5]   ⍝ with Subject ID, "/", and the item values. Each on newline.
[6]   ⍝ If DATA does not exist, the program asks for Subj & data.

[7]    0 0 ⍴1 ⎕POKE 96
[8]    'Scoring key:' ⋄ NF←sSSHAPE ⎕TCNL,⎕←KEY
[9]    →LOOP×⍳INT←0=⎕NC 'DATA'
[10]    Ns←sSSHAPE DATA←⎕TCNL,DATA ⋄ S←0
[11] NXTs:→0×⍳Ns←S+1 ⋄ D←1↓DATA sSINDEX S
[12]   '----------> Subject ID: ',¯1↓(T←D⍳'/')↑D ⋄ 'Data :',D←T↓D
[13]   →nUM
[14] LOOP:⍞←'----------> Subject ID: ' ⋄ →0×⍳0=⍴⍞ ⋄ ⍞←'Data : '
[15]   →0×⍳0=⍴D←⍞
[16] nUM:→OK×⍳' '∊D ⋄ D←((2×⍴D)⍴ 1 0)\D
[17] oK:D←⍎D ⋄ (⍕⍴D),' numbers entered.' ⋄ F←0
[18] NXTf:→PAU×⍳Nf←F+1 ⋄ V←'/',(1↓(⎕TCNL,KEY)SSINDEX F),'/1/0'
[19]   VALS←D RECODE 1↓V SSINDEX 2
[20]   (1↓V SSINDEX 1),'=',⍕+/(⍎1↓V SSINDEX 3)×VALS+
      (⍎1↓V SSINDEX 4)
[21]   →NXTf
[22] PAU:→LOOP×⍳INT ⋄ →NXTs
      ∇
```

Lines 1-6 are comments that describe essential features of the program.

The `⎕POKE` on line 7 discards the character prompt utilized in the interactive mode.

Line 8 displays the scoring key(s) and determines the number of factors (i.e. the number of major segments) in `KEY`. The results of this line are then stored in `Nf`, the loop factor counter.

Line 9 skips to `LOOP` (i.e. the interactive mode) if `DATA` does not exist. The program then reads data interactively (lines 14-16).

Line 10 catenates a carriage return to `DATA`, and calls `sSSHAPE` to determine the shape (i.e. the number of subjects) in `DATA`. It stores the result in `Ns` and initialises the subject counter `S`.

`sSSHAPE`, the function used to count the number of arguments in the segmented strings, returns the number of carriage returns present in the string. A carriage return is thus added to `KEY` (and also to `DATA`) so that the first element is included in the count.

```apl
       R←sSSHAPE SS
       -----------

  [1]   ⍝Returns the shape of a segmented string
  [2]    R←+/SS=1↑SS
       ∇
```

Similarly `sSINDEX` returns selected delimited segments from a longer string, the delimiter for the segmented string is the first character (i.e. carriage return).

```apl
       R←SS sSINDEX I
       --------------

  [1]   ⍝Function for the indexing of segmented strings
  [2]    R←((+\SS=1↑SS)∊I)/SS
       ∇
```

Line 11 of `SCORE` increments the subject counter and exits when all the data has been processed. Otherwise the next subject is selected and the data stored in `D`.

Line 16 checks if there are blanks in `D`. If not, spaces are automatically inserted between the single digit integers; this facilitates entry of single digit data.

Line 18 goes to `PAU` when all of the factors have been calculated. This line also catenates the default multiplier, 1, and the default adder, 0, to the segmented string, and stores the result in `V`. These default options eliminate the need for user input of values when items are added with equal weight.

Line 19 passes the 'recode' subsegment to the `RECODE` function. If this subsegment is not empty, the data is recoded:

```apl
       R←D RECODE C;T;NR;N;V;M;I
       -------------------------

  [1]  ⍝ Recode data D_from S e.g 1:1=4 3=7$3:1=4 2=9
  [2]  ⍝ IF D→1 2 2 ¯4 then R→4 2 9 ¯4 [2nd value not recoded]

  [3]   →rEC×⍳':'∊C ⋄ R←(×T)×D[|T←⍎C] ⋄ →0
  [4]  rEC:Nr←sSSHAPE C←'$',C ⋄ N←0 ⋄ R←⍬
  [5]  L1:→0×⍳Nr←N+1 ⋄ V←1↓C sSINDEX N
  [6]   V[(V∊':=')/⍳⍴V]←' ' ⋄ I←1↑V←⍎V
  [7]   M←((0.5×¯1+⍴V),2)⍴1↓|V
  [8]   R←R,(×I)×1↑((M[;1]∊D[|I])/M[;2]),100
  [9]   →L1
       ∇
```

Line 20 of `SCORE` computes the scale score by multiplying and then adding the possibly recoded values.

Line 21 returns to score the next factor. Finally if the program is being run interactively, line 22 goes to `LOOP` to query the user for additional data. Otherwise the program returns to `nXT` for the next subject.

> Jerry M Brennan<br>
> University of Hawaii at Manoa<br>
> Department of Sociology, Porteus Hall<br>
> 2424 Maile Way, Honolulu<br>
> Hawaii 96822

## Appendix: Screen Hardcopy of Program Notes

To PRINT these NOTES, toggle CTRL-PRNTSC on or off.

The APL workspace name is TESTSCOR. Load this workspace with one of the following:

```
      )LOAD TESTSCOR        [default drive (same as APL system)]
      )LOAD 0 TESTSCOR      [drive (e.g., 0=A 1=B 2=C)]
```

To SEE the KEYS & DATA in the workspace TESTSCOR, type:

```
      )VARS
```

### SCORING KEY:

1. To CREATE the scoring key for the test type )EDIT and some name - probably the name of the test.

   For example:

   ```
   )EDIT SHORTMEMORY   [Up to 77 characters with no blanks.]
   ```

2. ENTER the scoring key for each factor on one line.

   For example:

   ```
   FACTOR NAME/ITEMS ON FACTOR/MULTIPLIER/AMOUNT TO ADD
   FACTOR NAME/ITEMS/MULTIPLIER/AMOUNT TO ADD
   ...etc
   ```

```
WHEN YOU ARE FINISHED CREATING OR MODIFYING THIS KEY, LEAVE THE EDITOR WITH
Ctrl-E.

To SAVE the scoring key for use on another day, save the workspace with:
    )SAVE
```

### KEY: EXAMPLE 1: (Note that each factor begins on a new line)

```
ONE/1 2/1 3/¯2
TWO/1 3 4/1/0
THREE/4 ¯5/1/0
FOUR/2:1=10 2=20$5:1=30$¯6:1=5 2=7
```

This test has three factors labeled ONE, TWO, THREE, and FOUR.

The first factor, ONE, contains Items one and two. The multiplier for Item one is 1 and for Item two the multiplier is 3. Minus 2 is added to all Items. The second factor, TWO, contains three Items and all are multiplied by 1 and have 0 added. The third factor, THREE, contains Items four and five. Item four is added and Item five is subtracted.

Finally, factor FOUR has three Items: Two, five, and six. Items 2 and 5 are added and 6 is subtracted.

> If Item 2 has a value of 1, it is scored 10; if it has a value of 2, it is scored 20. All other values of Item two are scored 0.
>
> Similarly, if Item 5 has a value of 1, it is scored 30 otherwise, it is scored 0.
>
> If Item 6 has a value of 1, it is scored 5. A value of 2 on Item 6 is scored seven. Otherwise, this item is scored 0. Note: Since Item 6 has a minus, these values are subtracted.

NOTE: ............':' delimits item numbers from their scoring weights. In the above example, a score of 1 equals 10 for Item 2. '¤' delimits items and their weights from each other. Also, the high minus is used to subtract items. This minus is Alt-2 on the keyboard and may look like a small two on your screen. For all computations, addition is done first, then multiplication and, finally, the sign is changed.

### KEY: EXAMPLE 2:

```
FACTOR ONE/1 2
FACTOR TWO/3 4 5
```

EXAMPLE 2 has two factors: The first has two items and the second has three items. By default, nothing will be added to the items and there is no multiplier.

### KEY: EXAMPLE 3:

This last example illustrates a scoring situation in which some items are REVERSED. The scoring for one REVERSED factor might be as follows:

```
Item 1 is punched 1, 2 ,3 and is to be scored 1, 2, 3.
Item 2 is punched 1, 2, 3 BUT is to be scored 3, 2, 1.
```

This might be keyed as follows:

```
FACTOR ONE/1=3$2=2$3=1
```

### DATA ENTRY:

1. CALL the program with the following command:

   ```
   SCORE SHORTMEMORY    [The name of the program is always SCORE,
                         you insert the name of your key--in this case
                         SHORTMEMORY.]
   ```

The program will query for a "Subject ID". This identification can be any length and any characters--including blanks. After Subject ID is entered, the program queries for the items. Data consisting of all single digit numbers may be entered as a string (i.e., without blanks between each single digit). Data consisting of double (or more) digits must be entered with blanks separating each number. To QUIT data entry, strike RETURN when queried for "Subject ID".

Note: .............. Continue typing at the end of each line. The program will wrap automatically. The limit is 512 characters, including blanks.

2. Another way to ENTER DATA is to use the editor as you did for the scoring keys. However, this time a variable will be created that contains the data.

   For example:

   ```
   )EDIT SUBS      [Up to 77 characters with no blanks]
   ```

Enter the Subjects' ID followed by a "/". Next, enter the data. (See above for information about data entry). Begin each new subject on a new line. For example, the data for two subjects might look like this:

```
Sally Brown female age 42/12321
Bill Douglas male age unknown/22213
```

When data entry is complete, quit with CRTL-E and save with )SAVE.

### TEST SCORING:

1. To RUN the scoring program (using the key and data created in the last two examples):

   ```
   SUBS SCORE SHORTMEMORY
   ```

Many keys and subject data can be saved in this workspace. In fact, you can save over 500 separate variables.

2. To ERASE a key or a data file, do the following:

   ```
   )ERASE SHORTMEMORY      [Erase working copy in memory]
   )SAVE                   [save the erased copy onto the disk]
   ```
