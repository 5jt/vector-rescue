---
title: Steps Towards a Better Basic - Part 2
authors:
- Anthony Camacho
volume: '1'
issue: '2'
page: '73'
unindexed: true
transcribed: 'from page images of VOL.1-NO.2-OCTOBER-1984.pdf, pages 75–76 (printed 73–74; follows the XPL article, art10001020); Claude, 2026-10-03'
review: draft
tags:
- APL in perspective
- humour
queries:
- "A reprint from DATALINK; part 1 is v1n1-p77-steps-towards-a-better-basic-1.md."
- "The byline is printed “Anthony Comacho”, the editorial note says “Anthony Comacho’s series”; part 1 has Camacho. Transcribed as printed."
- "Figure 1 is typeset in a serif face. The reduction after `≠` is printed like `+`; read as `≠⌿` (not-equal reduction down the columns), which gives the printed LEAPS."
---

by Anthony Comacho
{ .byline }

*In this second extract from Anthony Comacho’s series aimed at convincing BASIC users of the delights of APL, the notion of array processing is discussed and an intriguing example is selected from the Gregorian calendar.*

*The article is reproduced with the kind permission of DATALINK magazine.*

A language which allows a single instruction or command to process all the members of an array “at once” so to speak, has the advantages that it saves the programmer thinking about unnecessary loops and it makes the programs compatible with parallel processors.

In any programming language it is necessary to have a method for referring to variables which allows the variable referred to to be changed under program control.

An easy way is to name all the fields in a record and then to step from the record to the next through a file. This approach avoids the need to vary the name of the variable that you are dealing with while at the same time achieving the object of dealing with a series of variables in the same way with the same piece of program. This is common in Cobol.

A second way — one familiar to people who have programmed in Basic — is to define an array of variables which have a name in common and a subscript to distinguish between the various members of the array, for example ARRAY (25) for 25 numbers.

The third method is to use the array name to refer to all the members of the array and to use a subscripting method when one or more of the members of the array is to be singled out for individual special treatment.

Of these three methods, only the third allows simple instructions to refer to all the members of an array.

The first advantage of this is that the programmer doesn’t have to think of so many loops. All he needs to do is to ensure that all the variables on which he wants to perform a similar operation are members of the same array. Of course, this doesn’t actually remove the loop from the program. The machine code still runs round processing each item of the array in turn until they are all done, but it is done in machine code by the interpreter program, not slowly as a FOR…NEXT, DO WHILE or REPEAT UNTIL loop and the programmer does not have to bother about start and end conditions of the loop.

The other main advantage is that this method explicitly allows for parallel processing. We will not benefit much from this until a new generation of computers is in common use. The problem with array processors or parallel processors of any kind is that they normally require programs to be specially rewritten for them. This is because an ordinary compiler cannot tell whether the sequence given is important.

A consequence of this is that most programs get no advantage from array processors and so very few array processors are in regular daily use.

The leap year function shown in Figure 1 demonstrates the great brevity of APL. Instead of explaining the use of the symbols, I will stick to the principles. It takes in YEARS — a one dimensional array (ie a row or list) of years — and outputs LEAPS — another one dimensional array of leap years. I have put in an extra pair of brackets to show the sequence of calculation. The first operation (inner bracket) is to find the remainder after dividing each year in the list by 4 and 100 and 400 and 4000.

The result of this is a table of remainders four deep and as long as the number of years in the list. Then for each year (ie column in the table) this table is processed (outer brackets). If the remainder from division by four was zero then it is a leap year unless the remainder from division by 100 was zero, in which case it is not. But even then it would be if the remainder from the division by 400 was zero and the remainder from division by 4000 was not.

The result of the processing is an array of true or false or yes or no values — ones for years that passed the test and are leap years, and zeros for years that did not pass the test. The last thing to do is to select out of the original array all those years which correspond to ones in the array of true and false values and this is done outside all the brackets by the (true and false array)/YEARS operation. Notice how the operations on each year can be done in parallel. The line works equally well with two, 20 or 200 years in the YEARS array.

*Figure 1: A Leap Year Solution in APL*

```
      YEARS
1984 1985 1986 1987 1988 1989 1990 1991 1992
      LEAPS←(≠⌿0=(4 100 400 4000∘.|YEARS))/YEARS
      LEAPS
1984 1988 1992
```
