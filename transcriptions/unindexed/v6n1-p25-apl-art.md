---
title: APL Art
authors:
- Alan Sykes
volume: '6'
issue: '1'
page: '25'
unindexed: true
transcribed: 'from page images of VOL.6-NO.1-JULY-1989.pdf, pages 27–28 (printed 25–26; within The Education VECTOR, after Puzzle Corner); Claude, 2026-10-11'
review: draft
tags:
- humour
- education
- competitions and puzzles
queries:
- "Headed “APL ART”, unsigned; the Education Vector’s own contents list (printed 23) gives it to Alan Sykes. The function LEAR is his wife Claire’s. It follows unindexed/v6n1-p25-puzzle-corner.md and precedes “Let a Child Loose in APL!” (unindexed/v6n1-p27-let-a-child-loose-in-apl.md)."
- "LEAR [1] holds an overstruck circle (the owl’s eyes), transcribed `⍟`; ESB’s box glyph, a square divided into four, is transcribed `⊞`. Stray marks in LEAR (a bar over ⍴ in [4] and over the T of BOAT in [6], under the 20s in [6]) are taken as blemishes. The catenation in [7] is printed as comma-bar, `⍪`."
- "LEAR and `3 ESB 11 22` were run in Dyalog APL (⎕IO←1) as a check on the transcription; their results, set here as text, agree with the printed pictures."
---

APLers are often teased concerning their use of strange symbols. Curiously enough, even mathematicians are sometimes guilty of this! Whilst teaching students who use APL in their statistics practical I have sometimes caught them playing with the symbols to see just what shapes can be created from them. All good fun though at the time they had better things to do!

Recently I noticed that my wife Claire (who is both a mathematician and an APLer) was doodling with the APL characters, and I began to wonder just how many works of aplart there are out there. So here is Claire’s contribution to start the ball rolling. The program is called `LEAR` and it defines global variables `OWL` `CAT` and `BOAT`. So there are no prizes for guessing just what `LEAR` does. As you can see the results are quite good. (I have to say that!) But of course you, the reader can do better?

```apl
     ∇ RES←LEAR;O;C;B
[1]    O←' ∧∨⍟π'
[2]    OWL← 6 5 ⍴O[1 2 1 2 1 1 4 3 4 1 ,(15⍴5), 1 5 1 5]
[3]    C←' ∧O=1/_'
[4]    CAT← 7 5 ⍴C[1 2 1 2 1 1 3 1 3 1 1 4 5 4 1 ,(15⍴6), 7 7 7 7 6]
[5]    B←'_ \ / ~'
[6]    BOAT← 3 20 ⍴(20 1 1 16 1 1 20)/B
[7]    RES←((7 ¯8 ↑CAT), 7 12 ↑ ¯7 ¯9 ↑OWL)⍪BOAT
     ∇
```

```apl
    ∧ ∧
    O O      ∧ ∧
    =1=      ⍟∨⍟
   /////    πππππ
   /////    πππππ
   /////    πππππ
   ____/     π π
____________________
 \                /
~~~~~~~~~~~~~~~~~~~~
```

My contribution to APLART looks forward to the summer and the next international conference APL ’89 to be held in Manhattan, New York. Since I have never been to the Big Apple before I am really excited at the thought of seeing the Empire State Building and other sites. So below is a function, cryptically called `ESB`, which requires a left argument equal to an integer, and a right argument requiring two positive integers. The result, for suitable choices, is something not dissimilar to part of the Manhattan skyline.

```apl
     ∇ R←A ESB N
[1]    R←'⊞ '[1+(⍳N[2])∘.≤A×|(⍳N[1])-⌈N[1]÷2]
     ∇

  3 ESB 11 22
     ⊞
     ⊞
     ⊞
    ⊞⊞⊞
    ⊞⊞⊞
    ⊞⊞⊞
   ⊞⊞⊞⊞⊞
   ⊞⊞⊞⊞⊞
   ⊞⊞⊞⊞⊞
  ⊞⊞⊞⊞⊞⊞⊞
  ⊞⊞⊞⊞⊞⊞⊞
  ⊞⊞⊞⊞⊞⊞⊞
 ⊞⊞⊞⊞⊞⊞⊞⊞⊞
 ⊞⊞⊞⊞⊞⊞⊞⊞⊞
 ⊞⊞⊞⊞⊞⊞⊞⊞⊞
⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞
⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞
⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞
⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞
⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞
⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞
⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞⊞
```

If you are a newcomer to APL, then you may be a bit bemused as to how this function works. The best way to proceed is to assign say `N←11 22` and `A←3`. Then try looking at bits of the code. (Note the use of `|` which takes the absolute value of its right argument.)

So may I exercise my privilege as editor of Education Vector and offer a prize for the most innovative `APLART` submission using a maximum of 10 lines of code? Please submit your contributions to the editor at the address at the foot of the front page.
