---
title: The Education Vector
authors:
- Alan Sykes
volume: '6'
issue: '1'
page: '23'
unindexed: true
transcribed: 'from page images of VOL.6-NO.1-JULY-1989.pdf, pages 25–26 (printed 23–24); Claude, 2026-10-12'
review: draft
tags:
- education
- programming techniques
queries:
- "The section’s own text only: its title page (printed 23, with its own contents list) and Alan Sykes’s editorial (printed 24, headed “The Education Vector”). The pieces it lists are transcribed separately: unindexed/v6n1-p25-apl-art.md, unindexed/v6n1-p25-puzzle-corner.md, unindexed/v6n1-p27-let-a-child-loose-in-apl.md, unindexed/v6n1-p29-the-i-apl-news.md and art10009570 (Numbers and Bases)."
- "The editorial’s mention of the “matrix of marks into grades” question refers to Education Vector, January 1989 (Vector 5:3)."
- "Kept as printed: the section’s contents list gives “Let a child loose in APL!!” and “The Latest I-APL News”; the editorial says Richard Smith is “now aged 5”, where the issue’s Contents page credits “Richard Smith (when aged 3)”."
---

## The Education Vector

**JULY 1989**

**Edited by Alan Sykes**

Reprinted from VECTOR Vol.6 No.1. VECTOR is the Quarterly Journal of the British APL Association; for more information about the British APL Association, contact the Secretary: Graham Parkhouse, Dept. of Mech. Eng., University of Surrey, GUILDFORD.

### Contents

| | | |
|---|---|--:|
| Editorial | Alan Sykes | 24 |
| APL Art | Alan Sykes | 25 |
| Let a child loose in APL!! | Richard Smith | 27 |
| The Latest I-APL News | Anthony Camacho | 29 |
| Numbers and Bases | Alan Sykes | 31 |

> Dr Alan Sykes,<br>
> Dept of Management Science and Statistics,<br>
> University College of Swansea,<br>
> Singleton Park, SWANSEA SA2 8PP

## Editorial

*by Alan Sykes*
{ .byline }

Welcome to Education Vector, the educational supplement to the quarterly journal produced by the British APL Association which is also mailed to all members on the (British) I-APL mailing list. For this edition we also welcome to our readership all attendees at APL '89, the international APL conference in New York in August.

I am glad to report that feedback to Education Vector is increasing and I welcome all contributions, comments and indeed criticisms. I thank those readers who (rightly) criticised some of my coding in past issues and I shall make every attempt to rectify my ways in future! (My use of APL tends to be very much one of getting the job done as soon as possible, and despite definite attempts to improve code presented in these columns, clearly I still haven't achieved the standards of professional APLers.)

In Education Vector (January 1989) I presented the question of how to turn a matrix of marks into grades. The solution I had in mind was duly presented by a number of APLers. This involved indexing the vector 'FEDCBA' according to the number of elements of the vector 70 60 50 40 35 0 that a mark was greater than or equal to. Thus the expression:

```apl
'FEDCBA'[⎕IO+¯1++/MARKMATRIX∘.≥70 60 50 40 35 0]
```

provides the matrix of grades. (The `⎕IO` is included to give complete generality to the expression whatever index origin the user is using - see this edition's article by me.)

I did however receive another solution which I had not anticipated and which is really preferable. Thanks to Mike Kingston (of IBM!) who pointed out that if we construct a vector of grades for each possible mark then all we need do is index this vector using `MARKMATRIX`. The easiest way to do this is to use / to replicate the required values: the vector of 100 grades is given by:

```apl
35 5 10 10 10 30/'FEDCBA'
```

Hence the alternative solution, with virtually no computation, is:

```apl
(35 5 10 10 10 30/'FEDCBA')[⎕IO+MARKMATRIX]
```

In this issue of Education Vector, the theme is 'using APL is fun'. Richard Smith (now aged 5) shows us just how much fun he has had at the APL keyboard. In 'APL ART' I throw open the challenge to readers to use their creative talents to produce pictures using APL characters. Finally in 'Numbers and Bases' we show how APL can be used in an investigative project on numbers and bases. The great beauty of such investigations is that everybody has something to offer - please share your gems of APL fun with us all by submitting comments, notes, or articles for inclusion in future editions. I hope that you enjoy the columns of this edition as much as I have enjoyed compiling them.
