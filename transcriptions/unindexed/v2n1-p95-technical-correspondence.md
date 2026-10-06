---
title: Technical Correspondence (Smith, Wiggins, Bassett)
authors:
- Adrian Smith
- Andrew Wiggins
- Mark Bassett
volume: '2'
issue: '1'
page: '95'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 97–98 (printed 95–96; Surely There Must Be a Better Way follows on p.97); Claude, 2026-10-05'
review: draft
tags:
- programming techniques
queries:
- "Letters with the editors’ italic replies, transcribed as italic paragraphs. Smith’s letter answers the first example in v1n3-p120-surely-there-must-be-a-better-way.md."
- "CHECK: lines [4] and [6] both read `5 6 [¯1↑X]`, as printed; IF is a user-defined (‘multi-way IF’) function, not shown. The editor’s one-liner is printed `R←5 6 1 2 5 6[2⊥C]`."
- "“Lewis Carrol” is printed so."
---

## From Adrian Smith, 15 May 1985

Sir: I am not entirely convinced by your first example in ‘Surely there must be a better way’ from Vector 1.3. I agree that the original function is rather awful, but in some ways your suggested numeric versions obscure the structure of the problem. They could also make ‘trivial’ changes unnecessarily hard, as the whole algorithm would need re-thinking. Maybe something like:

```apl
    ∇ R←CHECK X
[1]   ⍝ RETURN APPROPRIATE FLAG DEPENDING ON VALUES IN X[1 2]
[2]    R←0
[3]    →(Comb,Ster,Doll,0)IF 0 1 2 =1↑X
[4]   Comb:R← 5 6 [¯1↑X] ⋄ →0
[5]   Ster:R← 1 2 [¯1↑X] ⋄ →0
[6]   Doll:R← 5 6 [¯1↑X] ⋄ →0
    ∇
```

… note the multi-way IF, which I find an absolutely invaluable extension when faced with this sort of problem.

Yours sincerely,

Adrian Smith  
Operational Research,  
Rowntree Mackintosh,  
YORK YO1 1XY.

*Editor: Absolutely — I’m surprised that no-one else complained! It could be that I over-reacted in boiling down the original 22-line function to:*

```apl
R←5 6 1 2 5 6[2⊥C]
```

*The point is that the author had failed to spot a pattern underlying the problem and as a result produced uncommented and verbose code. Of course, the most important thing is that the APL should not be obscure, but understandable by another programmer (who might have to maintain it). This can be achieved both by writing clear code and by using comments as well, which your function does. By the way, I agree that the multi-way IF function is a very useful tool — and an underused one.*

## From Andrew Wiggins, 17 April 1985

Sir: I enclose a problem that I have had around for many months. It can easily be solved using a loop, but I have yet to find a way without the use of looping. I would therefore like to hand it over to the other readers of VECTOR, so that they may attempt it.

Yours faithfully,

Andrew Wiggins  
Lombard North Central PLC,  
Lombard House,  
London W1A 1EU.

*Editor: Andrew’s problem is presented in this issue’s “Surely there must be a better way” column.*

## From Mark Bassett, 13 May 1985

Sir: Here is a suggestion for a competition that you might like to include in a future issue of VECTOR. The problem had its origin in the need to display lists of names, grouped under various headings, in a way that was a little less dazzling to the eye than a simple columnar layout.

This led to the invention of a function, WORDWRAP, that would reshape text into a matrix of specified width with each row left-justified and no word being ‘broken’ at the right-hand margin unless it was too long to fit on one line.

The attached printout shows two examples of its use, taken from Lewis Carrol, with a suggested implementation below (the best I could find). The idea used was to build up the result row by row: take characters from the input text N at a time, remove any trailing non-blanks and catenate onto the output, unless this makes the next character a blank in which case we’ve reached the end of a word and should catenate without removing anything.

It is the need to worry about the beginning of the next line while constructing the current one that results in the function scanning the input in blocks of size N + 1.

No amount of search sufficed to discover a non-looping method so this is one obvious improvement entrants could make; if looping really is intrinsic to the problem then perhaps less work could be done inside the loop.

Yours faithfully,

M.S. Bassett  
20 Coval Lane,  
Chelmsford,  
Essex,  
CM1 1TD.

*Editor: It seemed more appropriate to include Mark’s problem in the “Surely there must be a better way” column, and so that’s where it is, along with some examples and Mark’s solution.*
