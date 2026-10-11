---
title: Dbase and Lotus files into I-APL
authors:
- W J Smith
volume: '7'
issue: '2'
page: '24'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1990.pdf (misnamed: Vol.7 No.2), pages 26–27 (printed 24–25; within The Education VECTOR, after Reading ASCII files into I-APL); Claude, 2026-10-11'
review: draft
tags:
- data and files
- programming techniques
queries:
- "A letter, “From: W J Smith, Sept 1990”, in the Communications of The Education VECTOR."
- "The writer’s postal address, printed after the signature, is left out here."
- "Kept as printed: “WORKS WIH .PRN FILES” in line [11] of MSDFM."
---

*From: W J Smith, Sept 1990*
{ .byline }

Your appeal on behalf of E.J.Sargeant in the July Vector re retrieving ASCII files into an IAPL workspace struck a chord. Some time ago, on the grounds that it is usually possible to transfer data from one package to another, I experimented with transferring files from Lotus and dBaseIII into an IAPL workspace.

dBaseIII files, output with a COPY TO &lt;filename&gt; TYPE SDF command, yield a series of fixed length records in ASCII format. These are only fixed if the rightmost field of each row is of the same size but this is easily managed even if you have to create a dummy column to achieve it! A further problem with Lotus files is that they are preceded by a number of carriage returns/line feed characters which need to be disposed of in the first stages of transfer; actually in the *DFREAD* function.

The *DFREAD* function in the IAPL DFILE workspace reads foreign files into the workspace as a VECTOR which includes all the CR’s and LF’s of the original file.

Having acquired the vector, a count of the CR’s can be used to determine the number of records (as long as you haven’t got the leading ones from LOTUS!). Then, after stripping out the unwanted CR and LF characters, the vector can be reshaped into an appropriate character matrix.

This matrix can then be separated into character matrices corresponding to the columns/fields of the original files; effectively generating an inverted file in data processing jargon.

I enclose a couple of ‘partly-baked’ functions I wrote while experimenting with this problem; they may be of use to your enquirer.

```apl
     ∇ Z←GETSDF F
[1]    ⍝ OPENS AND READS AN ASCII FILE 'F' IN THE \APL DIRECTORY
[2]     Z←'FILE ',F,' NOT FOUND'
[3]     →(0=DFOPEN F)/0
[4]     Z←DFREAD DFSIZE
     ∇
```

```apl
     ∇ Z←MSDFM A
[1]    ⍝ CONVERTS AN SDF FILE INTO A MATRIX OF
[2]    ⍝ ITS CONSTITUENT RECORDS. B CALCULATED, IS THE NUMBER OF
[3]    ⍝ RECORDS IN THE VECTOR, A IS THE NAME OF THE RAW VECTOR
[4]    ⍝ [7] COUNTS RECORDS, [8] REMOVES THE CR'S AND THE LF'S,
[5]    ⍝ [9] CALCULATES THE RECORD LENGTH AND RESHAPES THE
[6]    ⍝      CLEANED VECTOR
[7]     B←+/A=⎕AV[14]
[8]     A←((A≠⎕AV[14])∧(A≠⎕AV[11]))/A
[9]     Z←(B,⌊((⍴A)÷B))⍴A
[10]   ⍝
[11]   ⍝ WORKS WIH .PRN FILES GIVEN THAT: (1) THE LAST LOTUS
[12]   ⍝ COLUMN HAS ALL DATA OF EQUAL LENGTH; (2) THE FILE IS
[13]   ⍝ READ WITH '9 DFREAD DFSIZE' TO SKIP BLANK HEADING ROWS
     ∇
```

W J Smith
