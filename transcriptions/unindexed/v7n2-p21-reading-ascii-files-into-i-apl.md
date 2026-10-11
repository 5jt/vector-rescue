---
title: Reading ASCII files into I-APL
authors:
- J.C. Hines
volume: '7'
issue: '2'
page: '21'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1990.pdf (misnamed: Vol.7 No.2), pages 23–25 (printed 21–23; within The Education VECTOR, after ‘DAYOFWEEK’: Education Vector 7.1); Claude, 2026-10-11'
review: draft
tags:
- data and files
- programming techniques
- education
queries:
- "A letter, “From: J.C.Hines, Sept 1990”, in the Communications of The Education VECTOR, with an editor’s comment at the end."
- "The writer’s postal address, printed after the signature, is left out here."
- "Kept as printed: the function is named Getfile in its listing and GetFile in the call; its third line reads `Z←DREAD DFIZE` (the I-APL DFILE functions are DFREAD and DFSIZE, as in the next letter); “objects could be chosen from m” (m and m, both bold); “not-reached”; the last line of ALLCOMS has three closing parentheses for two opening ones; ALLCOMS localises N but does not set it."
---

*From: J.C.Hines, Sept 1990*
{ .byline }

In the April 1990 issue of ‘The Education Vector’, you appeal for any information on reading ASCII files into IAPL. I have been away for some time and have not been able to write to you. I realise that you may be flooded with responses (*Ed’s comment = No!*), but, in case not, here are a few points.

I can read ASCII files in without trouble and have written a little function called Getfile, which reads

```apl
Z←Getfile filename
DFOPEN filename
Z←DREAD DFIZE
DFCLOSE
```

There are a few things to take care of when using this function, all quite simple, but it is often the simple things we overlook, especially when working alone and without someone to act as a cardboard Indian.

One thing is to remember that the filename is a string, so that the call must have the argument in quotes, i.e. be on the lines of

```apl
TextVar ← GetFile 'a:thislet.doc'
```

Another depends on the way the ASCII file was produced in the first place. I-APL reads the file as a vector, unless the shape is specifically changed in the reading function. This means that line ends may not be marked as specific characters, because the input may have been created in a word processor which has re-formatted the document on the screen but without inserting actual carriage returns at the end of each line. Many of the line ends will have only virtual carriage returns. There are several approaches to this. One is to look at the file as received for carriage returns, possibly on the lines of

```apl
(TextVar=⎕AV[12])/⍳⍴TextVar
```

to find out where the real carriage returns are. If they are not tidy, reformatting can be done by finding the length of the longest line and then padding the shorter ones with blanks to create a matrix. I found it easy to ensure that the text in my wordprocessor had real carriage returns at the end of each line.

I hope these thoughts are sufficient to help Mr Sargeant to trace the source of his problem.

While writing to you, I am taking the opportunity to include another little function. This was written because of an article in ‘Program Now’ on ways of listing all the ways in which **m** objects could be chosen from **m**, allowing duplicates, but without using recursion. The discussion assumed non-APL languages, without recognising that this was a self-imposed limitation. The problem was therefore now to write something on the lines of:

```
for i=1 to num
   for j=1 to num
      for k=1 to num
         .
         .
         .
         write i,j,k ......
```

… but without knowing the depth of the nesting at compile time.

Various solutions were produced, using pointers, stacks or just choosing an arbitrary maximum depth of nesting and then providing a drop-out if this was not-reached.

It has amused me to write a version in APL which shows how much more powerful it is for problems of this kind. My code is:

```apl
Z←ALLCOMS;N;⎕IO
⎕IO←0
R←(N⍴N)⊤⍳N*N
Z←(⎕AV[(49+⍳9),65+⍳26])[⍳N])[⍉R]
```

The problem can be rephrased as one of counting up to `N*N` in base `N`. Line 1 calculates the number of terms and uses encode to get the answer but written in decimal arithmetic. Line 2 then creates a symbol list, consisting of as many characters as required from the list 1..9,A..Z, rotates the answer from line 1 so that the display is a neat list, and then indexes on these symbols. This does have a limit when N reaches 35, but 35\*35 is big enough that most of us will not want to wait around for this number of cases to be calculated. I think this is a nice demonstration of the value of APL. I hope you do too.

J.C.Hines

*Editor’s comment: Yes, I agree it’s a nice approach: unfortunately its use is somewhat limited by the size of the array that is created in line 2. This is an `N*N` integer array, and each integer requires four bytes of storage. Hence for this program to work up to `N=35` would require a computer with approximately `10*51` Kbytes of random access memory! On a computer with 640K RAM, ALLCOMS is bound to fail for `N>6`.*
