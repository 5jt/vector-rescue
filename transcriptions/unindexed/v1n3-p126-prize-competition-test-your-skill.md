---
title: 'Prize Competition: Test your skill'
authors:
- Dave Ziemann
volume: '1'
issue: '3'
page: '126'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 128–129 (printed 126–127; art10007060 follows on p.128); Claude, 2026-10-03'
review: draft
tags:
- competitions and puzzles
queries:
- "Check: the example result recomputes from JOBS and CONS (a consultant matches a job if every non-zero skill of the job is among theirs), and the skills matrix agrees with the prose descriptions of John, Anne, Bill and Mary."
---

by Dave Ziemann
{ .byline }

A company specialising in APL consultancy has a number of staff, each of whom has talents in a small number of different areas. For example, John has experience in system design, the TSO and CMS operating systems, and in APL\*plus/PC. Anne on the other hand, is skilled in all of these and also in APL2 and SHARP APL. Bill has APL\*plus/PC and APL2 whereas Mary has system design, SHARP APL, mathematical techniques, CMS and APL2.

This situation is represented by a consultants’ skills matrix as follows:

```
      +CONS←4 6⍴1 2 3 7 0 0, 1 3 7 9 2 6, 7 9 0 0 0 0, 1 6 5 3 9 0
1 2 3 7 0 0
1 3 7 9 2 6
7 9 0 0 0 0
1 6 5 3 9 0
```

where each row represents one consultant’s skills, and each non-zero entry is an index into a table of skill descriptions. Notice that skill 3 (CMS) belongs to John, Anne and Mary, and that in this representation zeros are used to pad the shorter skills vectors.

Now, when some work comes up, the skills of each consultant are matched against the skills required by the customer. Naturally the consultant must have all those talents needed for the job. Because business is good many jobs come in at once, and this is expressed as a jobs skills matrix each row of which contains the skill numbers required for the job; for example:

```
      +JOBS←5 3⍴1 2 3, 7 9 0, 1 4 0, 1 3 0, 1 6 3
1 2 3
7 9 0
1 4 0
1 3 0
1 6 3
```

In the attempt to allocate consultants to jobs, the company wants to generate a boolean matrix which will indicate the jobs that can be tackled by each consultant.

The competition is to write a dyadic function called &lt;SKILLSMATCH&gt; which will produce the boolean matrix as output. The left argument must be the jobs matrix and the right argument the consultants matrix. The result must then be a boolean matrix with one row per job and one column per consultant, where a 1 indicates that the consultant has sufficient skills to do the job. For example:

```
      JOBS SKILLSMATCH CONS
1 1 0 0
0 1 1 0
0 0 0 0
1 1 0 1
0 1 0 1
```

The company in question has a large number of customers and employees, whereas the number of unique skills is low. Entrants will therefore not be penalised for offering solutions that assume no more than 10 skills, but the demands on workspace, speed of execution, robustness and degree of intelligibility will be the major factors in deciding the winners.

To enter the competition you must write ISO standard-conforming code (i.e. no special features like nested arrays or new quad-functions), but we are always interested to see (and publish) alternative solutions written in other APLs.

The closing date for entries is 30th June 1985.

## Competition Rules

- Entries must be in legible English or APL as appropriate and should preferably be machine produced.
- Entrants must declare the type of computer and the version and release level of the APL interpreter on which their functions were written.
- The date and your full name and address should appear on each sheet of your entry.
- Entries should be physically separate from other contributions such as letters, and should be clearly marked ‘Competition Entry’.
- All submissions should be sent to the editor.
- Those on the committee, activities group or journal group of the British APL Association are ineligible.
