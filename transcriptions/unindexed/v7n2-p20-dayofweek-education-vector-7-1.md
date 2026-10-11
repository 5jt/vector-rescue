---
title: '‘DAYOFWEEK’: Education Vector 7.1'
authors:
- C.E. Williams
volume: '7'
issue: '2'
page: '20'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1990.pdf (misnamed: Vol.7 No.2), pages 22–23 (printed 20–21; within The Education VECTOR, after Puzzle Corner: Chess Board Pattern); Claude, 2026-10-11'
review: draft
tags:
- education
- programming techniques
queries:
- "The first letter under the heading “Communications” in The Education VECTOR, “From: C.E.Williams, Sept 1990”. It is followed on p.21 by J.C. Hines’s “Reading ASCII files into I-APL” (unindexed/v7n2-p21-reading-ascii-files-into-i-apl.md)."
- "The writer’s postal address, printed after the signature, is left out here."
- "Gauss’s formula and the worked example are printed in a typewriter face, not as mathematics; transcribed as printed in a code block."
- "Kept as printed: “to shed light to those”; “assigned to q” then “assigned to Q”; “29th February 1952 fell on a FRIDAY (3)” (Friday is day 5 in the scheme given; 29 February 1952 was a Friday)."
---

*From: C.E.Williams, Sept 1990*
{ .byline }

I hope the following may help to shed light to those who are unaware of the method used in the function *‘DAYOFWEEK’*

Turner’s function is simply the APL coding of the method due to Gauss, devised to determine the day of the week on which a given date will occur. Since in a leap year an additional day is added at the end of February, it is easier to assume that the year starts in March. Then March, April and May will be the first, second and third months of the year N, January and February will become the eleventh and twelfth months of the year N-1. The days of the week begin on Sunday by 0,1,2…6. Then f, the number of the day of the week corresponding to the kth day of the mth month of the year N, is determined as follows:

```
f=( k+(2.6m - 0.2) + D + (1/4 D) + (1/4 C) - 2C ) Modulo 7
```

Thus the example in Vector: August 1st 1990

```
k=1, m=6, D=90,C=19. C=number of the century
D= last two digits of year N Then

f=(1+15+90+22+4-38) Modulo 7

= 94 Modulo 7

= 3 i.e. Wednesday.
```

With this in mind:

Line 1 of *DAYOFWEEK* sets up *M*

Line 2 decodes *M* to 23888 using `0 12 ⊥ M[3 1];`

this is then encoded to 1990 5, having subtracted 3, with the code `0 12⊤¯3+0 12⊥M[3 1];`

1990 5 is rotated and one added to become 6 1990; this is assigned to *M*, which now is 6 1 1990;

finally on line 2, *Q* becomes 90 using `100|M[2]`.

Line 3 collects terms as per Gauss, and ends with MODULO 7 giving the day number 3.

(N.B., Turner has combined the last two terms +(1/4C) -2C into one: -1.75C.)

If I may be allowed to criticise (*sure! - Ed*) line two seems too complicated. Why not test the value of the month, if 3 to 12, subtract 2, and the year will be MODULO 100 assigned to q. If month is 1 or 2, add 10 to month and the year will be MODULO 100 -1 , again assigned to Q. It would be much easier to follow and no doubt speedier.

Bearing in mind k is the day of the month, substitution of a day into M, the second term allows the day of the week for any date, if `M←2 29 1952` then 29th February 1952 fell on a FRIDAY (3).

Thanks a lot for Education Vector; please keep up the good work!

Yours sincerely

C.E.Williams
