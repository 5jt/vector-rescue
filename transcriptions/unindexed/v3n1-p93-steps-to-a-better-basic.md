---
title: Steps to a better BASIC — A Choice Method of Selection (reprint from Datalink)
authors:
- Anthony Camacho
volume: '3'
issue: '1'
page: '93'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 95–96 (printed 93–94; ends the General Articles section; the technical section begins on p.95); Claude, 2026-10-05'
review: draft
tags:
- APL in perspective
- humour
queries:
- "Earlier parts: v1n1-p77, v1n2-p73, v1n4-p95, v2n1-p81, v2n3-p89 (all unindexed)."
- "The two sessions are printed in an italic APL face at a narrow line width, with long lines wrapped and indented; kept as printed. The membership result is printed as 85 digits wrapped 19, 16, 16, 16, 16, 1; it has the expected number of 1s (one for each punctuation mark in TEXT), but the exact string, with its wrapped spaces, cannot be recovered to check the positions."
- "The quoted string contains ¨ (dieresis) after CAN, and the punctuation list is '.,:;?!¨'. ⎕AVI converts between characters and numbers, as in Camacho’s earlier parts. `¯32×(N>96)∧N<123` is printed with a high minus."
- "Slips transcribed as printed: “arrays of numbers of logical values”, “zeroes”."
---

by Anthony Camacho
{ .byline }

*In this issue’s extract from his series of articles introducing APL to BASIC users. Anthony Camacho shows how APL provides powerful selection processes. This article is reproduced with kind permission of Datalink magazine.*

## A Choice Method of Selection

### Conditional operations without IF

In most microcomputer versions of BASIC, the logical value ‘true’ is represented by a one and ‘false’ by zero. A few treat any non-zero value for ‘true’ and/or set true variables to -1. This allows some elegant tricks. If you want an expression which puts B into A if x=y then

```
A=A*(X<>Y)+B*(X=Y)
```

will fill the bill. Either the bracket X<>Y or the bracket X=Y will be a one so either A\*1+0 or 0+B\*1 will go into A.

If your computer renders PRINT 1=1 as -1 then the expression you need is

```
A=-A*(X<>Y)+-B*(X=Y).
```

If what you want to do is to increment a counter until it reaches, say 50, then the expression is even neater:

```
C=C+(C<50) [or -(C<50) to suit]
```

The power of this kind of selection is greatly developed in APL, partly because it uses arrays of numbers of logical values and partly because it has some extra operators. In particular among these is the ‘compression’ operator, displayed as an oblique stroke. If the variable BOOLE is an array of ones and zeroes the same shape as an array VALUES containing any kind of item, then the expression ‘BOOLE/VALUES’ yields another array with as many items as there were ones in BOOLE. The items are, of course, the items from VALUES that corresponded to the ones in BOOLE.

For example suppose you wish to remove all punctuation characters from a line (or page or chapter) of text. In APL it is easy to construct an array of ones and zeroes the same length as the text with zeroes where the punctuation marks are and ones for all the other characters. This is done by using the membership operator which gives ones and zeroes as its result. The result is the same shape as the left argument and has a one whenever the item in the left array occurs in the right argument. Then compression of the original array gives the result you want.

```apl
      TEXT←'DEMONSTRATION. HOW, MEMBERSHIP
          : (∊); AND ?COMPRESS! (/) CAN¨
           REMOVE PUNCTUATION'
      TEXT ∊ '.,:;?!¨'
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0
        1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
        0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
        0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0
        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        0
      ⍝ EXCHANGE 0 AND 1 WITH LOGICAL NOT
          (~)
      (~TEXT ∊ '.,:;?!¨')/TEXT
DEMONSTRATION HOW MEMBERSHIP (∊) AND
        COMPRESS (/) CAN REMOVE PUNCT
        UATION
```

A similar line will convert all lower case to upper case. First it converts the text to its numeric form; then creates an array with ones where there are lower case characters (they have codes from 97-122). This array is then multiplied by 32 and subtracted from the numeric form of the text. (The lower case code for each letter is 32 more than the code for the corresponding upper case letter). When the codes are converted back from numbers to letters they are all upper case.

```apl
      ⍝ PHR CONTAINS A SENTENCE IN UPPER A
          ND LOWER CASE

      PHR
Now is the time for all good men to
come to the aid of the SDP.

      ⍝ ⎕AVI CONVERTS CHARACTERS TO NUMBER
          S AND NUMBERS TO CHARACTERS
      ⎕AVI(¯32×(N>96)∧N<123)+N←⎕AVI PHR
NOW IS THE TIME FOR ALL GOOD MEN TO
        COME TO THE AID OF THE SDP.
```

You may feel this messing about with text is trivial. The examples were chosen because text arrays are naturally displayed horizontally and so the examples take less space than numbers in columns would do. But similar expressions are used daily by APL users to select, say, all the accounts whose credit limit is exceeded or all the stock items whose rate of turn is in the bottom quartile or even all the MPs who were elected with the support of less than a third of their electorate.

And of course any action the program can take could easily be made to depend upon such selections.
