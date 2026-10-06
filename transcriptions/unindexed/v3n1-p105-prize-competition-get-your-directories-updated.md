---
title: 'Prize Competition: Get your directories updated'
authors:
- Jonathan Barman
volume: '3'
issue: '1'
page: '105'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 107–108 (printed 105–106; the Introduction to Contributed Articles follows on p.107); Claude, 2026-10-05'
review: draft
tags:
- competitions and puzzles
queries:
- "The contents list gives David Ziemann; the byline is Jonathan Barman."
- "Checked: the example is consistent with the rules: record 13 (276 of 511 used) takes all 218 rows of item 100; item 200’s 731 rows go 86 into record 10 (425 used), then 511 into new record 3 and 134 into new record 4; item 300’s 134 rows go into new record 5, record 12 being full."
---

by Jonathan Barman
{ .byline }

Filing systems use directories to keep track of where the data actually resides, and APL is no different – only it is supposed to be easier to manage.

The file system in question has a fixed record size which will accommodate APL objects below a certain size limit. The programmer has decided on a very simple file structure. The first record of the file contains the directory, all other records contain data. In this case the data consists of matrices with fixed width but a varying number of rows. Being a tidy minded sort of soul, the programmer has decided to use as much of the space in each record as possible, so that when new data is added to the file as many records as possible are filled up before new records are added.

The directory has 3 columns: column 1 is the file record number, column 2 positive integers which identify the data matrix and column 3 contains the number of rows in the APL matrix currently held in the record. The first row of the directory refers to itself and therefore has a special meaning. It has a 1 in the first column indicating record 1 and a 0 in the second column because the directory is not a data item. The third column gives the maximum number of data matrix rows that can be held in a record rather than the number of rows in the directory. For example:

```apl
      DIR
 1   0 511
13 100 276
 8 100 422
 7 100 511
10 200 425
 2 200 511
12 300 511
```

The data deletion program has left things in a bit of a mess. Records that are available for use have been removed entirely from the directory (e.g. records 3 to 6), and some records which were full now have space (e.g. records 8,10,13).

When new data is added the programmer wants to fill up records where the data identifiers match, and use the lowest numbered records possible for the new records. He has produced a matrix giving the number of data rows that have to be added; column 1 is the data identifier and column 2 is the total number of rows:

```apl
      RECS
100 218
200 731
300 134
```

The programmer wants a new directory which has an extra column showing how many rows have to be added to each record:

```apl
      DIR NEWDIRECTORY RECS
 1   0 511   0
 7 100 511   0
13 100 276 218
 8 100 422   0
 2 200 511   0
10 200 425  86
 3 200   0 511
 4 200   0 134
12 300 511   0
 5 300   0 134
```

He can then update every record that does not have a zero in column 4, and at the end of the process add columns 3 and 4 together and put the new directory back into the first record.

Can you write the NEWDIRECTORY function?

Answers received before 31 July 1986 will be eligible for a share of the £50 prize.
