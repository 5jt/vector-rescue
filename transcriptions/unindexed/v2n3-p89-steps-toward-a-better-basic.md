---
title: Steps toward a better BASIC — A High Grade SORT of Language (reprint from Datalink)
authors:
- Anthony Camacho
volume: '2'
issue: '3'
page: '89'
unindexed: true
transcribed: 'from page images of VOL.2-NO.3-JANUARY-1986.pdf, pages 91–92 (printed 89–90; ends the General Articles section; the technical section begins on p.91); Claude, 2026-10-05'
review: draft
queries:
- "Earlier parts: v1n1-p77, v1n2-p73, v1n4-p95 and v2n1-p81 (all unindexed)."
- "Checked: ⍋A for A←5 7 1 2 9 8 6 3 4 is 3 4 8 9 1 7 2 6 5, and ⍒A 5 6 2 7 1 9 8 4 3, as printed; ⍋⎕AVI B for the shuffled alphabet B gives exactly the printed 26 indices, and B holds each letter once."
- "The session printouts are in an italic APL face; the comment lamp ⍝ is printed as a small ∩-like glyph, read as ⍝. The comment ‘A CONTAINS THE NORMAL COLLATING SEQUENCE’ wraps onto a second line; rejoined. The index of the 26 letters wraps after 14 numbers; kept as printed."
- "⎕AVI (character to 8-bit code) is a system function of Camacho’s APL."
- "Slip transcribed as printed: “last months sales”."
---

by Anthony Camacho
{ .byline }

*In this further extract from Anthony Camacho’s series of articles aimed at introducing the delights of APL to BASIC users, the facilities for sorting in the two languages are compared.*

*This article is reproduced with the kind permission of DATALINK magazine.*

## A High Grade SORT of Language

### Sorting in APL and BASIC

In Sinclair BASIC T$(3) is the third character in the string T$. In APL A[3] is the third item in the one dimensional array A, which could hold a string of letters or a row of numbers. APL can deal with as many dimensions as you like so A[1;3] is the third item in the first row of a table. If the index is omitted the symbols refer to the whole of the unspecified dimension. So A[;3] is the third value in every row and A[1;] is the whole of the first row.

Indexing parts of arrays like this is a powerful way of sorting them. If A contains: 5 7 1 2 9 8 6 3 4 then A[3] is the smallest item, A[4] is next, A[8] next and so on. APL allows a row of items in an index so A[3 4 8 9 1 7 2 6 5] will give a sorted version of A.

APL has a function called ‘grade’ which creates just such an index. The symbol looks like a triangle with a vertical line through it; if the point of the triangle is up it is called ‘upgrade’ and produces an index in ascending order; if the point of the triangle is down it is called ‘downgrade’ and the index is in descending order.

```apl
      A←5 7 1 2 9 8 6 3 4
      A
5 7 1 2 9 8 6 3 4
      ⍝ ⍋ IS UPGRADE ⍒ IS DOWNGRADE
      ⍋A
3 4 8 9 1 7 2 6 5
      ⍒A
5 6 2 7 1 9 8 4 3
      A[⍋A]
1 2 3 4 5 6 7 8 9
      A[⍒A]
9 8 7 6 5 4 3 2 1
```

So much for the standard BASIC exercise ‘Write a program to sort ten numbers into numerical order’ – five symbols on one line! This approach to sorting is not only brief but fast too. On a run of the mill Z80 micro it took eleven seconds to sort a thousand random integers into order. My APL can hold numbers in IBM 64-bit double precision form; a thousand of these took 22 seconds to sort. The indexing method of sorting works equally well on letters, but to prepare the index the letters have to be converted to numerical form. The ⎕AVI function used below converts a character into the decimal value of its 8-bit code. This shows the unshuffling of an alphabet.

```apl
      B
TICKPUEMDVSQRAGFXZNLOBHYJW
      ⍋⎕AVI B
14 22 3 9 7 16 15 23 2 25 4 20 8 19
 21 5 12 13 11 1 6 10 26 17 24
 18
      B[⍋⎕AVI B]
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

But of course usually it is not so much letters that need sorting as words. Some versions of APL have versions of upgrade and downgrade which will do this. They create an index to the rows in a two dimensional array of characters. They also allow you to specify the order in which the characters are to be sorted. On the left of the grade symbol is a character variable (the collating sequence) and on the right of it the table of characters to be indexed by rows.

The following is an elementary example. Note the ‘;]’ to pick up the whole of each row. Five rows is all there is room for here but the advantage really shows with large word lists. An array of four hundred five-letter words picked at random took 8 seconds!

```apl
      ⍝ A CONTAINS THE NORMAL COLLATING SEQUENCE
      ⍝ B CONTAINS FIVE WORDS
      B
CHAIR
TABLE
SHELF
STOOL
BCASE
      B[A⍋B;]
BCASE
CHAIR
SHELF
STOOL
TABLE
```

One of the nice things about this is that you aren’t restricted to putting the field you took the index from into order. You can sort the sales figures into product number order or the product numbers into order based on last months sales. If your file has large records and you can’t hold them all in memory you only need space for the keys in memory and then you can extract a record at a time in graded order from the disk.
