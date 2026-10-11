---
title: Puzzle/Problem Corner
authors:
- Alan Sykes
volume: '6'
issue: '3'
page: '20'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, pages 22–25 (printed 20–23; within The Education VECTOR, after unindexed/v6n3-p19-letter-to-the-editor.md); Claude, 2026-10-11'
review: draft
tags:
- competitions and puzzles
- education
- programming techniques
queries:
- "Unsigned column within The Education VECTOR, edited by Alan Sykes, to whom it is attributed (“since the last time I put pen to Education Vector paper”). It starts below R Weber’s letter on p.20 and ends at the foot of p.23; Sykes’s “From Coin-tossing to the Weather” (art10009580) follows on p.24."
- "The 10⊥ in John Sullivan’s bound expression and in his three-digit search is printed with a glyph like ⍳ with a short stem; read as ⊥ (decode), which gives the stated 17 for N=5."
- "The CARDS example (`(⍳3)∘.=X` and the scans that follow) was run in Dyalog APL as a check on the transcription, and agrees with the print except that the second row of the first result is printed `0 1 0 1 0 1` (Dyalog: `0 1 0 1 0 0`, as the last 1 of X is card 1); kept as printed. The second reduction is printed as ∨⌿ (slash with a bar)."
- "Kept as printed: “2 BASE 16 gives 255 6 ¯99” (that is the result of 3 BASE 16; 2 BASE 16 gives 15 ¯9); “Claude Henrion from Monteiller, Saviese” (Henriod, in Savièse, as he signs his letter on p.96); “Mr McLean” here, “Bill McClean” elsewhere."
---

*by Alan Sykes*
{ .byline }

Since the last time I put pen to Education Vector paper, I have had a number of letters which gratifyingly inform me that Education Vector is read, by a wide variety of people, spread through many countries. This issue’s puzzle/problem corner therefore concentrates on reporting back to you on the many contributions that I have received. Thank you to all those who took the trouble to write to me.

## Marks to Grades (Education Vector January 1989)

My first puzzle corner referred to the problem of converting marks into grades and I have already referred to some of the contributions I received on that problem. However, I was delighted to receive one letter that came just too late for me to include then: it comes from Mr McLean in Dunoon, Scotland. Mr McLean, at the time of writing, had had a copy of I-APL for only a few weeks and although his answer to the problem is not as slick as those sent to me by the professionals, it was just as effective and shows what can be done with APL in a relatively short period of time. The solution presented went like this.

```apl
MARKS←?50 8⍴100
A←MARKS≥70
B←(MARKS<70)∧MARKS≥60
C←(MARKS<60)∧MARKS≥50
D←(MARKS<50)∧MARKS≥40
E←(MARKS<40)∧MARKS≥35
F←MARKS<35
SUM←A+(2×B)+(3×C)+(4×D)+(5×E)+(6×F)
GRADES←'ABCDEF'[SUM]
```

I do hope that readers such as Mr McLean will continue to send in their ideas, reports on their experiences with APL, and I apologise that I am often not too good at replying quickly!

## The Card Collecting Problem (Education Vector April 1989)

This was a problem on simulation, to determine the average number of cards that need to be collected in order to get one of each of the set, if the cards received are randomly chosen from the set (I took six in the set). Claude Henrion from Monteiller, Saviese, supplied a solution. The problem with such a simulation is that APL is best at dealing with fixed size arrays, rather than using algorithms of the form ‘do something until some criterion is satisfied’. With the card collecting problem, we don’t know in advance how many cards are going to be needed, and any algorithm which generates a card at a time, checks to see whether the full set has been achieved, and carries on if not, will be very slow when written in APL.

Claude’s solution is to be almost certainly sure of having sufficient cards by taking 66 (11 times the number of cards) at a go. The solution is quite heavy going for newcomers to APL, so I present his one-liner and then show how it works.

```apl
      ∇ R←N CARDS C
[1]     R←+/∨\⌽∨⌿<\(⍳C)∘.=?(N,11×C)⍴C
      ∇
```

The expression `5 CARDS 6` then yields five simulations of collecting all six cards. How does this work?

Suppose for example we had only three cards to collect and that one simulation of 6 cards gave the numbers *X* equal to `1 2 1 2 3 1` - now let’s pick up the function to the left of the `?` using *X* as a substitute for `?(N,11×C)⍴C`

```apl
      (⍳3)∘.=X←1 2 1 2 3 1
1 0 1 0 0 1
0 1 0 1 0 1
0 0 0 0 1 0


      <\(⍳3)∘.=X        (performs the operation 'less than'
1 0 0 0 0 0              accumulatively replacing all
0 1 0 0 0 0              after the first 1 by 0)
0 0 0 0 1 0


      ∨⌿<\(⍳3)∘.=X      (performs the logical 'or' down the cols)
1 1 0 0 1 0
```

At this stage, what we need to do is to find out the index position of last 1 to occur, assuming that this last 1 represents the last card required to complete the set.

```apl
      ⌽∨⌿<\(⍳3)∘.=X
0 1 0 0 1 1         (reverses the row)

      ∨\⌽∨⌿<\(⍳3)∘.=X
0 1 1 1 1 1         (sets all numbers after the first 1 to 1)
```

Hence finally summing this gives the value `5` which is where the last card to complete the set of 3 in `1 2 1 2 3 1` occurred.

Thank you, Claude, for your solution. It shows just what can be done with the useful array manipulative tools that APL provides. However, from a pure computing point of view, it has to be said that ordinary languages which are more geared to recursive steps are more suited to such calculations! Unless of course you, the reader, can do better!

## Numbers and Bases (Education Vector July 1989)

In my article on numbers and bases, I looked at whether the digits of a number could be reversed when that same number was represented using a different base. John Sullivan, who is Treasurer of the British APL Association, supplied some nice examples of his exploration of the same field which he had done in response to an article in Computer Weekly. The answer to the question - what bases from 10 to 100 give a reversal for 2 digit numbers using digits 1 to 9 only - is the bases 10 13 16 19 22 25 28, and wait for it, 37 46 55 64 73 82.

John points out in his letter that an upper bound for the bases that need to be tested when exploring a possible reversal of N digits is given by

```apl
⌊(10⊥10-1+⍳N)*÷N-1
```

which for N equal to 5 gives the answer 17. John also gives a neat function *BASE* to calculate the coefficients of the linear equation used:

```apl
      ∇ R←N BASE B;⎕IO
[1]     ⎕IO←0
[2]     R←(B*⌽⍳N)-10*⍳N
      ∇
```

... so that, for example, `2 BASE 16` gives `255 6 ¯99`. Using *BASE*, John investigates three digit numbers by using:

```apl
Y←CP 9 9 9
10⊥Y[;(0=(3 BASE B)+.×Y)/⍳9*3]
```

...with the following results:

base reversible numbers:

```
 9  544
13  477
14  438
16  173
19  144  288
21  155  219
28  169
```

John’s energy for APL being inexhaustible, he goes on to look at the 4 digit case which reveals the bases 7 (6112) 16 (1415) and 19 (1277 and 1749). Thank you John!

Since this puzzle section is somewhat longer than usual - my puzzle for this edition is simple - please submit your puzzles for inclusion in the next Education Vector!
