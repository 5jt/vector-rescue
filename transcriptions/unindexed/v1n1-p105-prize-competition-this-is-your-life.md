---
title: 'Prize Competition: This is Your Life'
authors:
- David Ziemann
volume: '1'
issue: '1'
page: '105'
unindexed: true
transcribed: from page images of VOL.1-NO.1-MAY-1984.pdf, pages 107–108 (printed 105–106; art10003490 follows on p.107); Claude, 2026-10-03
review: draft
tags:
- competitions and puzzles
queries:
- "The 4 by 5 grid is printed as APL quads (empty) and dominoes (live); transcribed as ⎕ and ⌹. The run code 2 2 4 5 2 2 3 matches the grid and sums to 20."
- "Birth and Death rules set as a definition list."
---

by David Ziemann
{ .byline }

In the Game of Life a rectangular grid is used as a framework within which the behaviour of ‘organisms’ over successive generations is studied. Each square within the grid must be either filled or empty, representing either a live or dead/unborn cell. Rules that determine the conditions under which new cells are born and old ones die are used to produce the next generation of organisms. For example (and for interest only), the usual rules for birth and death are:

Birth
: an empty cell becomes live in the next generation if it currently has exactly 3 live neighbours.

Death
: a live cell dies in the next generation if: i) it currently has 0 or 1 live neighbours (isolation) or ii) it currently has 4 or more live neighbours (overcrowding)

In this context, each cell has 8 neighbours — the squares directly adjacent to it.

In APL, the most obvious data structure that can be used to represent the grid is a boolean matrix of known shape, with 1s indicating live cells and 0s dead ones. It is then possible to write an APL function that will take a boolean matrix right argument and return a new one that represents the next generation of cells. In fact this is quite an old problem, and it can be solved in a fairly satisfactory non-looping way. However, the time taken to calculate a successor generation is proportional to the grid size, and will be the same regardless of the contents of that grid. With large grid sizes, this cost can become prohibitive, and is particularly annoying when the grid only contains a smallish organism somewhere near the centre!

An alternative representation considers runs of 0s and 1s in the ravelled boolean matrix. For example, using this run-coding method, a 4 by 5 grid

```
⎕⎕⌹⌹⎕
⎕⎕⎕⌹⌹
⌹⌹⌹⎕⎕
⌹⌹⎕⎕⎕
```

would be represented by the integer vector: 2 2 4 5 2 2 3 where the quads represent empty cells and the dominoes live ones.

The first element of the run-code vector *always* indicates the leading number of 0s in the corresponding ravelled boolean matrix. The second element then gives the length of the next run of 1s, the third the length of the next run of 0s, and so on.

For typical Game of Life grids, this representation provides a reasonably compact data structure. Moreover, the time taken to calculate the successor grid is now proportional to the size of the contained organisms, rather than the grid size. This means that ‘boring’ generations are calculated quickly, whereas more complex ones take longer.

Because it is convenient to define and view a grid as a character matrix containing only spaces and crosses, the boolean representation is still important, and functions are required for converting between the boolean and run-coded forms. This is the subject of this issue’s competition.

The task is to write the two monadic functions BTR and RTB. BTR converts its boolean vector argument into a run-coded vector, and RTB goes back the other way. Note that the shape of the grid is not relevant because BTR has a boolean vector argument and RTB a boolean vector result.

For example:

```
      +BM←4 5⍴0 0 1 1 0,0 0 0 1 1,1 1 1 0 0,1 1 0 0 0
0 0 1 1 0
0 0 0 1 1
1 1 1 0 0
1 1 0 0 0

      BTR ,BM
2 2 4 5 2 2 3

      ⍝ THE FOLLOWING IDENTITIES MUST ALWAYS HOLD TRUE:

      (⍴,BM)=+/BTR ,BM
1

      (,BM)∧.=RTB BTR ,BM
1
```

Each respondent must submit two APL functions that conform to the first ISO draft proposal for an APL language standard. (Don’t worry — this effectively just means VS APL).

Additionally, respondents may include two further functions written for the APL implementations of their choice (please specify!). Note that no prizes will be awarded in this category.

Entries will be disqualified if they do not conform to the above descriptions, or if they rely on the external environment (ie, if a function is not a ‘black box’). The criterion for judging functions that jump these hurdles will be the minimisation of the number of characters in the solution. This character count will only include the printing characters entered at the keyboard in del-editor mode, but will NOT include characters in the function header-line or in comment lines. Composite symbols count as one character.

A first prize of £30 (or equivalent) will be awarded to the author who, in the judges’ opinions, submits the shortest correct entry. Two special commendation prizes of £10 each will additionally be awarded.

Many thanks to Paul Chapman, author of VIZ::APL, who suggested the competition topic.
