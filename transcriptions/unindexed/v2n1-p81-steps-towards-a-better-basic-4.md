---
title: Steps Towards a Better Basic — Part 4 (reprint from Datalink)
authors:
- Anthony Camacho
volume: '2'
issue: '1'
page: '81'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 83–85 (printed 81–83; follows the Mercia advert on p.80; the Bedford School case study follows on p.84); Claude, 2026-10-05'
review: draft
queries:
- "Earlier parts are in v1n1-p77, v1n2-p73 and v1n4-p95 (all unindexed)."
- "The session listings wrap at the printer’s line width; wrapped code lines and comments are rejoined here. In Fig. 1 and Fig. 5 [1] the third string is printed broken as 'AKQJ / 098765432' and 'AKQ / J098765432'; rejoined as 'AKQJ098765432'. The second string is 13 characters with the 1 in fifth place, as the output shows."
- "Fig. 2, second line, is printed A←A[⍳13;],A[13+⍳13;],A[26+⍳13;],[39+⍳13;]: the last A is missing. Transcribed as printed."
- "Fig. 3: the last line is printed `⎕AVI 64+26?26`, and the comment ends “AS ⎕AVI”; read as printed. In this italic face the I may be a left bracket, giving `⎕AV[64+26?26` with the closing bracket lost; the OCR reads the same. Its output is a fresh shuffle (all 26 letters once each), not the 26?26 shown above it."
- "Checked: the 4 13⍴52?52 deal in Fig. 4 holds each of 1–52 once, and both printed tables of hands (Fig. 4 and Fig. 5) hold each of the 52 cards once."
- "The BASIC dice line prints INT(6*RND), not 1+INT(6*RND) as the text before it recommends. Transcribed as printed."
- "The APL in the figures is printed in italic capitals with Roman digits; transcribed in plain text."
---

by Anthony Camacho
{ .byline }

This issue we include a further extract from the series in Datalink in which Anthony Camacho attempts to explain some APL concepts in terms familiar to BASIC programmers. Here he shows how random numbers can be put to use.

*The article is reproduced by kind permission of Datalink magazine.*

## The die is cast: the cards are dealt

APL has the edge on RND in BASIC

Fig. 1 shows a way of describing a pack of cards in a table of characters using only the ‘RESHAPE’ and ‘CATENATE’ functions. In APL reshape is the Greek ‘R’ which looks like a small p and catenate is the comma. The table shown has 52 spaces in the first row, more spaces but with the 1 of the 10 for each of the ten-spot cards in the second row, four sets of card names (zero for each of the 10s) in the third row and thirteen of each of the suit letters in the fourth row. The commas act like BASIC + to join the strings together to make a single string (or vector as it is called in APL) 208 characters long, and the 4 and the 52 reshape it into four rows of 52.

```apl
FIG 1
      A←4 52⍴(52⍴' '),(52⍴'    1        '),(52⍴'AKQJ098765432'),(13⍴'S'),(13⍴'H'),(13⍴'D'),(13⍴'C')
      A

    1            1            1            1
AKQJ098765432AKQJ098765432AKQJ098765432AKQJ098765432
SSSSSSSSSSSSSHHHHHHHHHHHHHDDDDDDDDDDDDDCCCCCCCCCCCCC
```

Perhaps the table will be easier to read if turned through ninety degrees and put into four columns; but we must have the 1 before the 0 in each 10 so the table has to be reflected as well as turned. The APL symbol which is the circle (called pi times) overstruck with a backslash reflects a table about the diagonal from top left to bottom right. The first line in fig. 2 makes a table of 52 lines of 4 characters. There are as many indices in the square brackets as there are dimensions; they are separated by semicolons. Iota 13 gives the integers from one to 13 so adding constants, lets us pick each of the four suits & make a table of them.

```apl
FIG 2
      A←⍉A
      A←A[⍳13;],A[13+⍳13;],A[26+⍳13;],[39+⍳13;]
      A
 AS  AH  AD  AC
 KS  KH  KD  KC
 QS  QH  QD  QC
 JS  JH  JD  JC
10S 10H 10D 10C
 9S  9H  9D  9C
 8S  8H  8D  8C
 7S  7H  7D  7C
 6S  6H  6D  6C
 5S  5H  5D  5C
 4S  4H  4D  4C
 3S  3H  3D  3C
 2S  2H  2D  2C
```

The question mark in APL is the symbol for two functions, ‘ROLL’ and ‘DEAL’. Roll is like the BASIC function RND but only produces integers, whereas RND normally will produce a random number between 0 and 1. Some versions of BASIC have a number in brackets after RND, to vary the function. BBC BASIC is unusual in allowing RND(6) to give a random throw of a die. Most BASICS need 1 + INT(6\*RND). The number on the right of the function specifies the number of possibilities; in APL the number on the left of the function (if there is one) specifies how many of those possibilities are to be chosen — or how many of the cards are to be dealt!

In BASIC, to produce a dozen throws of a die we would write:

```
FOR I=1 TO 12:PRINT INT(6*RND);:NEXT I
```

but there is no easy way to avoid picking duplicates. Here is one way to shuffle the alphabet:

```
 10 DIM B(26): B$=""
 20 FOR I=1 TO 26
 30 A=1+INT (26*RND): OK=1
 40 FOR J=0 TO I-1
 50 IF A=B(J) THEN OK=0
 60 NEXT J
 70 IF OK=0 THEN GOTO 30
 80 B(I)=A: B$=B$+CHR$(64+A)
 90 NEXT I
100 PRINT B$: END
```

Fig. 3 shows the APL equivalents.

```apl
FIG 3
      ⍝ HERE ARE 12 THROWS OF A DIE
      ?12⍴6
5 6 2 1 4 1 6 3 4 3 2 2
      ⍝ HERE ARE 26 INTEGERS SHUFFLED
      26?26
22 4 16 2 11 8 25 15 12 1 13 9 5 6 20 24 21 10 23 18
 3 17 14 7 19 26
      ⍝ TO CONVERT TO LETTERS ADD 64 TO CONVERT TO ASCII AND THEN USE THOSE NUMBERS TO INDEX ITEMS OUT OF THE CHARACTER SET WHICH APL HOLDS AS ⎕AVI
      ⎕AVI 64+26?26
KUHEXTLVIZPGAFSRQBNWMCODYJ
```

An elegant way of expressing a hand of whist or bridge is as a four by thirteen reshape of a deal of 52 out of 52 cards. Our 52 numbers can easily be translated into the names of the cards by picking them out of the table of names that we made (fig. 1). Note the blank after the semicolon in fig. 4 which takes a whole line of four characters.

```apl
FIG 4
      4 13⍴52?52
11 50 27 14 35 28 39 38 30 32 47 15 22
26 13 33 16 37 10 43  4 45 46 42 34 41
49 21 23 36  6 20 12  3  5 24 48 19 25
 8 31 29  7 17 52 18  1 40 51  2 44  9
      13 16⍴A[52?52;]
 KS 10H  JC  9H
 9D  KD  QS  7D
 2S  8H  7S  JS
 5D  2D  5H  2C
 3H  3C  4C  JD
 AH  6H  8S  6C
 QC  2H  8D  4H
 3S  8C 10D  5C
10S  AS  KH  7H
 QH  5S  6S  4D
10C  6D  9S  4S
 9C  KC  JH  7C
 3D  QD  AD  AC
```

All the APL shown so far is commands. Like BASIC it can also be used to write programs. An APL program is made of functions, rather in the way a good BASIC program is made of subroutines (or in BBC BASIC of procedures). But whereas all BASICs allow you to write instructions outside subroutines or procedures, APL does not. All APL instructions are in functions and one function must be the main program and call the others. Here in fig. 5 is an example of an APL function called HAND which produces a set of bridge or whist hands as its result. The upside down delta is the symbol which introduces and ends an APL function, and the assignment to R is the way APL specifies that the function has an explicit result. The variable after the semicolon is localised.

```apl
FIG 5
      ∇HAND[⎕]∇
    ∇ R←HAND ;A
[1]   A←⍉4 52⍴(52⍴' '),(52⍴'    1        '),(52⍴'AKQJ098765432'),(13⍴'S'),(13⍴'H'),(13⍴'D'),(13⍴'C')
[2]   ⍝ [1] PUTS THE NAMES OF THE PACK INTO A
[3]   R←13 16⍴A[52?52;]
[4]   ⍝ [3] PICKS THE NAMES ACCORDING TO THE DEAL AND PUTS THEM INTO A TABLE OF FOUR HANDS
    ∇

      HAND
10C  2S  8S  5D
 9D  5S  AC  KS
10S  6S  QH  6C
 QD  2H  5H  3C
 9S  4S  5C  7S
 6H  4D  AD  JH
 7C  3S  9H  7H
 8H  4H  4C  7D
 JS  6D  9C  8C
10D 10H  QS  3H
 KD  AH  2C  AS
 8D  JC  KH  2D
 3D  KC  JD  QC
```
