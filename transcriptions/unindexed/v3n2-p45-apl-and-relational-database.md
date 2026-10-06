---
title: APL and Relational Database, May 23rd 1986 (meeting notes)
authors:
- Adrian Smith
volume: '3'
issue: '2'
page: '45'
unindexed: true
transcribed: 'from page images of VOL.3-NO.2-OCTOBER-1986.pdf, pages 47–48 (printed 45–46; the AGM meeting; Iverson’s talk, art10003970, follows on p.47); Claude, 2026-10-05'
review: draft
tags:
- data and files
queries:
- "Adrian Smith’s notes (see his introductory notes, p.44) on two talks at the AGM; the third, Iverson’s, is indexed as art10003970. Each talk is printed as a bold heading with the speaker in italics; transcribed as H2 sections."
- "“RDMS” is printed so (RDBMS)."
---

## Reading Chicken Bones (Oracle, SQL and APL)

*Phil Chastney*

By way of preamble, Phil stated the assumptions that most of us knew APL, but were less familiar with the ideas of RDMS. APLs (mostly) come equipped with some kind of component file system, which is a good start, but is definitely not a database. To get at external data without lots of code (and lots of loops) you need a relational system:

- for religious reasons (!)
- because it will be rectangular
- because it will *not* be hierarchical. This is essential because you don’t know the paths in advance.

### Some Properties of Tables

They have no duplicate rows or columns. The row order doesn’t matter. They have no repeating groups (i.e. ragged edges). Tables stand alone without visible links between them. The links are made on the basis of the *data values* alone.

The sort of things you can do with tabular data include:

– Extraction. This commonly employs SQL or an equivalent language (note the word *language* . . . SQL is not a package!). The structure of SQL is APL-like in the extreme:

```
SELECT      columns
FROM        table
WHERE       some condition is true
```

. . . there is an obvious parallel with:

```apl
MASK/[1] TABLE[;COL1,COL2,COL3]
```

SQL allows expressions very much in the APL mould. As with APL, the results are further tables which can be used in subsequent expressions:

```
SELECT Ename,Job from EMP
  WHERE Job=
    (SELECT Job from EMP where Ename='JONES')
```

This will get a list of all the employees who have the same job as anyone called ‘Jones’!

– Joining Tables. Typically you might want to pick up departmental data (location in the example below) to go with selected employees:

```
SELECT Ename,Loc from EMP,DEPT
  WHERE Ename='ALLEN'
  and EMP.Deptno=DEPT.Deptno
```

. . . no physical (or permanent) join is made . . . it is all done with address calculations to give the appearance of a single table.

– Arithmetic: SELECT 12 x Salary where . . . . and so on.

### The Best of Both Worlds?

This is tremendous for data retrieval, but turns out to be an absolute pain in the neck for data manipulation! Now as we all know, APL is rather good at data manipulation . . . . can we envisage a language which will get us the best of both worlds? Unfortunately, we cannot, at least not yet. Some of the outstanding problems are:

1. The use of names. ‘Select Fred,Joe’ is a list of tokens, not names in the APL sense.
2. Treatment of nulls. APL has no way of handling ‘no data’ as a cell entry in an array.
3. Symbolic notation. SQL is headed down the ‘verbosity’ route.
4. Implicit joins. APL is a great one for creating all the intermediate objects.
5. SQL is truly *functional*. It has no assignment statement.

If we can’t unite the two, can we embed one in the other? It is very hard to see APL sitting within SQL, so the only practical option is some arrangement where APL passes a text string to SQL, which returns an array of data. An Auxiliary Processor is marketed by Oracle to do just this; it works, but has some performance problems:

- most SQL is pre-compiled within COBOL code. Of course you can’t do this in APL and you need a lot of nitty-gritty routines to keep track of storage etc.
- APL still only gets one record at a time.

In summary, APL and relational database appear in principle to be made for each other. In practice the links are not straightforward, or as efficient as they could be.

## Using APL with a Variety of Databases

*Paul Jackson (IPSA)*

The theme of this talk was the use of an I.P. Sharp package (Viewpoint) as a way of getting at lots of different databases in a consistent way. Typically an administrator would set up ‘virtual files’ on a central Id., and would manage the copying of data for users to share. There were lots of nice ideas (e.g. the ability to output a report to your Mailbox), and some problems (e.g. in representing multidimensional data).

Readers are referred to the appropriate IPSA glossies for more details.
