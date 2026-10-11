---
title: Yet More on that Ambivalent Operator ...
authors:
- Norman Thomson
volume: '6'
issue: '3'
page: '97'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, pages 99–102 (printed 97–100; within Technical Correspondence, after unindexed/v6n3-p94-concern-a-possible-feedback.md); Claude, 2026-10-11'
review: draft
tags:
- language design
- programming techniques
queries:
- "A letter in Technical Correspondence, From: Norman Thomson, 15th December 1989, on the letters of David Piper and Phil Last in Vector 6:2. It ends at the top of p.100 and is followed there by his “VCAT: A Response” (unindexed/v6n3-p100-vcat-a-response.md)."
- "Kept as printed: the header `X←L IF R` with the result assigned to Z in line [1]; AVX[1] `Z←(L+/R÷↑L,⍴R` (unbalanced parenthesis), though the error displays show `Z←(L+/R)÷↑L,⍴R`; “VALUE ERROR+”; “the language There” (no full stop); “ambi-valent”. The position of the carets under the error displays is approximate."
---

*From: Norman Thomson, 15th December 1989*
{ .byline }

My heart leapt up when I beheld the headline "Ambivalent Operators" in the Technical Correspondence section of Vector Vol.6 No.2, but sadly the promise of what I deem an ambivalent operator, that is one which can accommodate either one or two operands, was not fulfilled!

I feel that the use of lengthy descriptive names serves in the case of this correspondence to obscure rather than elucidate the underlying discussion which is nevertheless worth while following. Accordingly I shall attempt to clarify what I believe to be the salient points arising from David Piper’s and Phil Last’s contributions.

It all starts from the problem of providing an ambi-valent function which returns for a right argument *R* the moving average of period *L* if the left argument *L* is present, and the simple average if it is not, and also avoids the use of either branching on `2=⎕NC'L'` or conditional `⍎`.

David’s proposal is the following (I have amended his operator *MON* slightly so that the operand *Q* is a general condition - this seems to me to make it more useful than having a test for `Q=2`):

```apl
[0]    Z←L(P MON Q) R
[1]    →L1 IF Q
[2]    →0 Z←1(L P R)
[3]   L1:Z←0


[0]    X←L IF R
[1]    Z←R/L


[0]    Z←L AVP R;T
[1]    →0 IF↑(T Z)←(⍴R)(AVP MON(2=⎕NC 'L'))R
[2]    Z←(L+/R)÷L


      3 AVP ⍳5
2 3 4
      AVP ⍳5
3
```

The essence of the method is that the derived function `P MON` returns a flag which is 1 for dyadic, 0 for monadic, followed by the value in the former case. In the latter case it re-executes `P MON` with in the present example `(⍴R)` as left argument.

As Phil points out it is somewhat unsatisfactory always to re-execute in the monadic case. Moreover a function applied as an operand to *MON* must be constructed in the rather special way that *AVP* is, with a default left argument supplied as in line 2. This goes against the general principle that operators should have as wide a range of applicability as possible.

Phil argues that there is no case for an operator and uses a function *AM* as shown below. In the event of *L* being absent a "do-nothing" function *L* is constructed. This means of course that the technique is only useful for functions like the present one where the monadic meaning is the same as the dyadic meaning with the left argument scored out. I suspect that the number of functions of any practical use where this applies is very limited.

```apl
[0]    AM R
[1]    R←⎕FX 'Z←L R' 'Z←R'


[0]    Z←L AVL R
[1]    AM 'L'
[2]    Z←(L+/R)÷↑L,⍴R


      3 AVL ⍳5
2 3 4
      AVL ⍳5
3
```

Phil’s version of *AM* uses the same name for function and right argument - a permissible if potentially confusing use of the language There may be some hidden advantage in using this here, but if so it escapes me. Another disadvantage of this technique is that the function call to *AM* must be explicitly built into all functions which use it in this way.

One way to combine David’s and Phil’s ideas might be to define an *AMBI* operator...

```apl
[0]    Z←L(P AMBI)R
[1]    ⎕TS←⎕FX 'Z←L R' 'Z←R'
[2]    Z←P R


[0]    Z←AVX R
[1]    Z←(L+/R÷↑L,⍴R


      3 AVX AMBI ⍳5
2 3 4
      AVX AMBI ⍳5
3
```

which works, but the trouble now as the observant reader will have noticed is that *L* does <u>not</u> appear in the function header for *AVX*, and so the construction of *AVX* presupposes its use as an operand of *AMBI*. If *L* is localised in *AVX*

```apl
[0] Z←L AVX R
```

it cannot pick up the value from the encompassing operator and so trouble ensues....

```apl
      3 AVX AMBI ⍳5
VALUE ERROR+
AVX[1] Z←(L+/R)÷↑L,⍴R
            ∧∧
```

The same sort of consideration applies to the simple-minded operator approach based on `2=⎕NC'L'` branching:

```apl
[0]    Z←L(P AMB)R
[1]    →L1 IF 2=⎕NC 'L'
[2]    →0 Z←P R
[3]   L1:Z←L P R


      3 AVX AMB ⍳5
2 3 4
      AVX AMB ⍳5
VALUE ERROR+
AVX[1] Z←(L+/R)÷↑L,⍴R
            ∧∧
```

Returning to the original problem, perhaps the conditional `⍎` solution is the best after all:

```apl
[0]    Z←L AVG R
[1]    Z←⍎'(',Z,'+/R)÷↑',(Z←'L' IF 2=⎕NC 'L'),'⍴R'

      AVG ⍳5
3
      3 AVG ⍳5
2 3 4
```

Meanwhile the quest for the holy grail, alias the wholly ambivalent operator, goes on!
