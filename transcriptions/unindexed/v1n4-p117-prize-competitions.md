---
title: 'Prize Competition: Reshaping Rows of a Matrix; Result: Numeric Matrix Validation'
authors:
- Jonathan Barman
- David Ziemann
volume: '1'
issue: '4'
page: '117'
unindexed: true
transcribed: 'from page images of VOL.1-NO.4-APRIL-1985.pdf, pages 119–122 (printed 117–120; the QL/APL review follows on p.121); Claude, 2026-10-04'
review: draft
tags:
- competitions and puzzles
queries:
- "Two pieces: Barman’s new competition and Ziemann’s result of the matrix-validation competition (v1n2-p107), which received no entries; set as H2 sections."
- "The ROWRESHAPE example checks: each row, without trailing blanks, is reshaped to 20 characters (e.g. `20⍴'CODES'`), as printed."
- "VALIDNUMSMAT read at 600 dpi. Labels a, b, c, w are printed in lower case (underscored letters). [6] is a comment `⍝ ⍴R←→(1↑⍴W1),2`. [10] `L←+/∧\\⌽' '=W1←(⍴W1)⍴V`. [24] `E←+/∨\\W1='E'`. [28] `EI←(∧/0≠C[;,2],E)/⍳⍴E`. [29]–[30] use `⍟`. The header lists V twice; printed so."
- "The TEST results are printed as a 14-row display (TEST, result column 1, result column 2) whose last-but-five row is blank; transcribed as printed, spacing approximate. The test input `1.23E-307` uses a hyphen, which line [9] maps to high minus."
- "Slip transcribed as printed: “implemeted”."
---

## Prize Competition: Reshaping Rows of a Matrix

by Jonathan Barman
{ .byline }

This problem arose from a user requirement that initially seemed irksome, but turned out to have an easily stated solution. It involved the creation of a set of tree structured codes from a list of basic codes. The solution came down to taking a matrix of codes of varying lengths and reshaping each to fill a specified width. The function &lt;ROWRESHAPE&gt; does the trick; notice that trailing blanks are not reshaped.

If the variable &lt;A&gt; contains the codes to be reshaped, then:

```
      A
CODES
TO BE
RESHAPED
ON EACH LINE
      ⍴A
4 12
      20 ROWRESHAPE A
CODESCODESCODESCODES
TO BETO BETO BETO BE
RESHAPEDRESHAPEDRESH
ON EACH LINEON EACH
```

The problem is to write the function &lt;ROWRESHAPE&gt;. As usual the program must conform to the draft ISO APL standard (assume VS APL). A first prize of £30 and two others of £10 each will be awarded to the winners. The closing date for entries is 31st July 1985.

## Prize Competition Result: Numeric Matrix Validation

by David Ziemann
{ .byline }

When I discovered that we hadn’t received a single entry for this prize competition my immediate reaction was intense disappointment - especially considering the importance and relevance of the subject. However, this emotion was soon converted to relief when I imagined one of the possible alternative outcomes - that of receiving ONE very bad entry!

Anyway, having learned my lesson, I shall endeavour to ensure that future competitions don’t actually involve too much hard programming.

One possible solution to the problem is now described.

```
    ∇ R←A VALIDNUMSMAT W;V;L;W1;B;E;M;V;C;D;EI;⎕IO
[1]   ⍝ VALIDATE EACH ROW OF CHARACTER MATRIX <W> AS ONE VALID NUMBER
[2]   ⍝ |<A> IS SCALAR VALIDATION TYPE: 1/2/3/4=BOOL/INTEGER/REAL/E FMT
[3]   ⍝ <R>[;1]=VALID/INVALID(0/1)      <R>[;2]=THE NUMBER IF VALID
[4]   ⍝ BLANK ROWS OF <M> ARE VALID ONLY IF A<0, WHEN 0 IS RETURNED
[5]   ⍝ TOO LARGE E FORMAT NUMBERS ARE INVALID AND RETURN A 1 IN <R>[;2]
[6]   ⍝ ⍴R←→(1↑⍴W1),2
[7]    ⎕IO←1
[8]    V←,W1←(¯2↑ 1 1 ,⍴W)⍴W
[9]    V[(V='-')/⍳⍴V]←'¯'
[10]   L←+/∧\⌽' '=W1←(⍴W1)⍴V
[11]   W1←(-L)⌽W1
[12]   →(a,b,b,c,0)[1 2 3 4 ⍳|A]
[13]  ⍝ BOOLEAN
[14]  a:R←2 VALIDNUMSMAT W1
[15]   R←0∨R×B,[1.5]B←R[;2]∊ 0 1
[16]   →w
[17]  ⍝ INTEGER OR REAL
[18]  b:M←'0111111111239'[' 0123456789¯.'⍳' ',W1]
[19]   V←1↓⍎'0 ',((V∊'23')∨V≠¯1↓' ',V)/V←,' ',M
[20]   R←V∊(6×2=|A)↓ 13 31 131 213 231 2131 1 21
[21]   R←R,[1.5]R\1↓⍎'0',,' ',R⌿W1
[22]   →w
[23]  ⍝ E FORMAT
[24]  c:E←+/∨\W1='E'
[25]   M←(-E)⌽(1 2 ×⍴W1)↑W1
[26]   C←3 VALIDNUMSMAT(⍴W1)↑M
[27]   D←¯2 VALIDNUMSMAT(0 1 -⍴W1)↑M
[28]   EI←(∧/0≠C[;,2],E)/⍳⍴E
[29]   V←D[EI;2]+10⍟|C[EI;2]
[30]   B←V<10⍟⌊/⍳0
[31]   C[EI;2]←(~B)+(×C[EI;2])×D[EI;1]×B\10*B/V
[32]   R←(C[;1]∧D[;1]),C[;,2]
[33]   R[EI;1]←R[EI;1]∧B
[34]  w:R[;1]←R[;1]∨(A<0)∧L=¯1↑⍴W1
    ∇

      ⍴TEST
14 9
      TEST,⍕¯4 VALIDNUMSMAT TEST
3            1        3
 ¯7.1        1     ¯7.1
3..1         0        0
2.2 3.4      0        0
 1E3         1     1000
¯1.71E27     1  ¯1.71E27
131.7E¯1     1    13.17
13E1.6       0        0
6E789        0        1
             1        0
1.23E-307    1   1.23E¯307
1.23E¯308    1        0
1E2E3        0        0
3.E2         1      300
```

The function &lt;VALIDNUMSMAT&gt; above expects as a right argument a character matrix where each row is to be validated as a single number. The scalar left argument indicates the type of validation required; boolean, whole number, decimal number or E format (scientific notation), each successive validation type being a ‘superset’ of the last. The result is a two column matrix where the first column is a 1 for a valid single number in the corresponding row of the argument, or a 0 otherwise. The second column is the actual number, if valid. Blank rows of the argument are considered invalid unless the left argument is negative, in which case 0 is returned.

The first few lines prepare the argument by ensuring it’s a matrix, mapping any minus signs into high-minus symbols and right-justifying it. Line 12 is a branch according to the required validation type. Lines 18-21 are an expression of that by now well known technique for numeric validation, as demonstrated in VECTOR Vol.1 No.1 page 133. The parenthesised part of line 20 determines whether to validate for decimal numbers as well as whole numbers.

The boolean validation segment in lines 14-15 first validate the argument as a set of integers (type 2) and then check that the results are 0 or 1 only. Note that in this case the explicit result is forced to be boolean on line 15.

A similar approach is used in lines 24-33 for E format input, but with the text to left of each ‘E’ being validated independently from that to the right. Line 24 determines which rows are potential E format numbers. Lines 25-27 validate the left portion (mantissa) as a decimal number, and the part to the right of the ‘E’ as a whole number (exponent).

The next four lines create the actual number from the two validated portions. Because an entered number may be too large for the machine (e.g. 1E791) the result cannot be formed directly. Instead the logarithm of the number is compared with the logarithm of the largest machine number to determine validity, on line 30. Line 31 then forms the actual results without fear of a DOMAIN (or LIMIT) ERROR. For numbers which are too large, line 31 causes a 1 to be returned in the second column of the result, so that the application can tell why the E format number was bounced. Taking logs may be slow, and so the technique is used only for those rows that have ‘E’s in them. The advantage of this method is that it will work regardless of the size of the implemeted number limit.

The last line permits blank rows to be accepted with a result of 0 provided that the left function argument is negative.

## Competition Rules

- Entries must be in legible English or APL as appropriate and should preferably be machine produced.
- Entrants must declare the type of computer and the version and release level of the APL interpreter on which their functions were written.
- The date and your full name and address should appear on each sheet of your entry.
- Entries should be physically separate from other contributions such as letters, and should be clearly marked ‘Competition Entry’.
- All submissions should be sent to the editor.
- Those on the committee, activities group or journal group of the British APL Association are ineligible.
- DOS format diskettes containing APL\*PLUS, IBM or Sharp APL workspaces are acceptable. Diskettes will be returned.
