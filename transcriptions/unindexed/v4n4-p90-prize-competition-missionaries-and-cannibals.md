---
title: 'Prize Competition: Rules; Missionaries and Cannibals'
authors:
- Anne Wilson
volume: '4'
issue: '4'
page: '90'
unindexed: true
transcribed: 'from page images of VOL.4-NO.4-APRIL-1988.pdf, pages 92–93 (printed 90–91); Claude, 2026-10-06'
review: draft
tags:
- competitions and puzzles
queries:
- "The rules (p.90) are unsigned; the problem (p.91) is by Anne Wilson."
- "Checked: the RAFT 2,3 example is a valid crossing: 1 missionary and 1 cannibal cross, 1 missionary returns, 2 missionaries and 1 cannibal cross; no bank or raft ever has more cannibals than missionaries (where there are missionaries), and all 2+2 end on the far bank. The rows alternate between crossings and returns."
---

## Prize Competition: Rules

Entries must be in legible English or APL as appropriate and should preferably be machine produced.

Entrants must declare the type of computer and the version and release level of the APL interpreter on which any functions were written.

The date and the entrant’s full name and address must appear on each sheet of the entry.

Entries should be physically separate from other contributions such as letters, and should be clearly marked “Competition Entry”.

All submissions should be sent to the Editor.

Members of the B.A.A. committee, activities working group or journal working group are ineligible.

DOS format diskettes containing APL\*PLUS, IBM or SHARP APL workspaces are acceptable; diskettes will be returned.

Unless otherwise stated, entrants should submit only one entry. We encourage submission of alternative approaches, but the entrants must indicate clearly which one answer is the entry in the competition.

Non-members of the B.A.A. are encouraged to enter the competition. If they should win, then part of their prize will comprise free B.A.A. membership for the current year.

Late competition entries may be accepted if the competition has not yet been judged.

## Prize Competition: Missionaries and Cannibals

*by Anne Wilson*
{ .byline }

Several years ago we entertained a visiting minister who had been a missionary in Papua New Guinea. Amongst the tales he told were ones of talking to old men who had been aware of their elders eating missionaries. The solutions to this problem are dedicated to him.

The scenario is familiar. There is a party of cannibals and missionaries travelling from one village to the next. The missionaries are safe so long as they are not outnumbered by the cannibals. Luckily there are equal numbers of cannibals and missionaries!

Between the two villages are several rivers which the party crosses by raft. These rafts are made by the cannibals, and their size depends on the trees in the surrounding jungle.

As the rafts can not usually accommodate all the people in one crossing the missionaries have to work out how many to send across on each journey of the raft. They obviously want to keep the number of journeys to a minimum because they are anxious to reach the next village quickly.

What the missionaries need is an APL program which will take as input the number of missionaries and cannibals, and the size of the raft. It will return a 2 column matrix showing the number of missionaries and of cannibals on the raft for each journey. At no place must the number of cannibals be greater than the number of missionaries, neither on the bank or on the raft.

The program will be of the form:-

```text
RAFT number-of-people, raft-size
```

where the number-of-people is the number of missionaries, and the number of cannibals (as they are the same).

```text
RAFT 2,3

        missionaries cannibals
             1           1
             1           0
             2           1
```
