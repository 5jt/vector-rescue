---
title: How to Kill More Cats ...
authors:
- Norman Thomson
volume: '7'
issue: '1'
page: '115'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 117–118 (printed 115–116; within Technical Correspondence, after unindexed/v7n1-p113-vcat-in-sharp-apl.md); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- language design
queries:
- "A letter in Technical Correspondence, From: Norman Thomson, 25 May 1990, replying to Peter Branson’s “Yet more VCAT...” in Vector 6.4 (p.95). It ends with an italic comment signed “Ed(ex)”, kept here."
- "The writer’s postal address (a mail point at IBM UK Laboratories, Hursley Park) is omitted."
- "The functions are APL2; disclose is printed ⊃ and enclose ⊂. Checked in Dyalog APL (⎕ML←3): `CAT`, `TAC` and `MAT` give the displays printed."
- "Kept as printed: “appraoach”; “which which”; “pondor which the designer for efficiency has” (a word seems lost); “I never though”."
---

*From: Norman Thomson, 25 May 1990*
{ .byline }

Peter Branson’s reply (Vector Vol.6 No.4) to my `VCAT` suggestions rightly takes me to task for using the pompous phrase ‘a modern didactic appraoach’. In simple terms I mean that APL2 allows us to cut through much of the algorithmic obscurity of old-time APL, thereby making APL2 of great value as a specification language. I agree with both Adrian and Peter that my `VCAT` is horrendously inefficient with screenful-sized matrices, but that I submit is not the point. Consider rather that `VCAT` is only the tip of an iceberg, in the sense that if you are motivated to have `VCAT` in your toolkit, you are likely also to want `HCAT` (horizontal catenation). Then there is the further matter of justification, - do you want primary (left/top) or secondary (right/bottom)? So generalise `CAT` to take a vector of matrices as right argument `R` and 1 or 2 as left argument to denote horizontal or vertical:

```apl
[0] Z←L CAT R
[1] Z←⊃[L]⊃,/⊂[L]¨R

      A B
WEE  RATHER
ONE  LARGER
     MATRIX


      (1 CAT A B)(2 CAT A B)
WEERATHER  WEE
ONELARGER  ONE
   MATRIX  RATHER
           LARGER
           MATRIX
```

Justification is then an exercise in using rotate as a dual transformation, and can be embodied in:

```apl
[0]  Z←L TAC R
[1]  Z←⌽[L]L CAT⌽[L]¨R

      (1 TAC A B)(2 TAC A B)
   RATHER       WEE
WEELARGER       ONE
ONEMATRIX    RATHER
             LARGER
             MATRIX
```

Now degeneracy has to be considered. A vector requiring catenation may be regarded either as a row or a column vector, so there is another 1/2 option for the left argument `L` of the function `MAT` which which converts its right argument `R` into a matrix.

```apl
[0]  Z←L MAT R
[1]  Z←⊃[L]1/⊂1/R

      (1 MAT 'PIG')(2 MAT 'PIG')
P  PIG
I
G
```

`(1/R)` on the right ensures that `MAT` will also deal with a scalar, but in order to work as a null function for a non-degenerate matrix `R` it is necessary to add the first line:

```apl
[.1]  →(2=⍴⍴R)/0
```

The eight significant choices, i.e. all combinations of horizontal/vertical, primary/secondary and row/column resolution have now been dealt with in a systematic way, leaving the path open for efficiency if the goal is other than a pure teaching one. I don’t think Peter and I have any fundamental disagreements, and I certainly don’t suggest the abandonment of old practices and idioms where these are of worth at the implementation stage. I do however advocate the use of APL2 at specification and design stages, and invite readers to pondor which the designer for efficiency has by viewing the whole of this particular problem so compactly.

Norman Thomson

---

*Comment: I never though that such an innocuous little function could generate such interest; maybe we should expose some more ‘pragmatic antiques’ to competition from advanced APLs? Ed(ex).*
