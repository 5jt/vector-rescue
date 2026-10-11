---
title: Communications
authors:
- Alan Sykes
volume: '6'
issue: '4'
page: '19'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 21–23 (printed 19–21; within The Education VECTOR, after Alan Sykes’s Education Vector Editorial on p.18); Claude, 2026-10-11'
review: draft
tags:
- education
- programming techniques
queries:
- "Unsigned letters column in The Education VECTOR, by its editor Alan Sykes (credited in the Contents to Alan Sykes); it reports Dietrich Trenkler’s teaching functions and a letter from C.E. Williams, and introduces Norman Thomson’s “The Card Collecting Problem” (unindexed/v6n4-p22-card-collecting-problem.md), the letter that follows it."
- "The telephone number Alan Sykes gives for readers to call is omitted."
- "The line `[3]` of REDUCTION and line `[4]` of SCAN run on to a second printed line; kept as printed."
- "Kept as printed: “Osnabruck”; “Dr Trenker” (for Trenkler); “Mr William’s”; in the SCAN example the first result line omits 1.875, and the line for 0.312 has one closing parenthesis too few."
---

## Communications

Thanks to Dr Dietrich Trenkler from the University of Osnabruck in West Germany. Dr Trenkler teaches courses in APL and has written the following functions to aid the understanding of just how the APL interpreter performs calculations such as ENCODE, DECODE, REDUCTION and SCAN. He supplies the following examples and the necessary code.

```apl
      '÷' REDUCTION ⍳8
÷/1 2 3 4 5 6 7 8 ↔0.2734375
1÷(2÷(3÷(4÷(5÷(6÷(7÷8))))))


      '÷' SCAN ⍳8
÷\1 2 3 4 5 6 7 8 ↔ 1 0.5 1.5 0.375 0.3125 2.1875 0.2734375
1      ↔ 1
0.5    ↔ 1 ÷2
1.5    ↔ 1÷(2 ÷3)
0.375 ↔ 1÷(2÷(3 ÷4))
1.875 ↔ 1÷(2÷(3÷(4 ÷5)))
0.312 ↔ 1÷(2÷(3÷(4÷5÷ 6))))
2.187 ↔ 1÷(2÷(3÷(4÷(5÷(6÷ 7)))))
0.273 ↔ 1÷(2÷(3÷(4÷(5÷(6÷(7÷8))))))


      16 16 16 ENCODE 500
16 16 16 ⊤ 500 ↔ 1 15 4
(1×16×16)+(15×16)+4


      0 16 ENCODE 500
0 16 ⊤ 500 ↔ 31 4
(31×16)+4


      0 24 60 60 ENCODE 94863
0 24 60 60 ⊤ 94863 ↔ 1 2 21 3
(1×24×60×60)+(2×60×60)+(21×60)+3


      0 24 60 60 DECODE 1 2 21 3
0 24 60 60 ⊥ 1 2 21 3 ↔ 94863
 0  1  2   21     3
24  1 24    0     0
60  0 26 1560     0
60  0  0 1581 94860
 0  0  0    0 94863
```

This is just Horner’s rule describing how the result is computed. The first row (column) excluding the first 0 are the arguments of `⊥`. Read row entries as ‘multiplied by’ and column entries as ‘added to’. Note that most zeros in this scheme serve only as a means to build up a matrix.

The functions are necessarily complicated and I am very grateful to Dr Trenker for supplying them.

```apl
     ∇ F REDUCTION V;R;A
[1]   R,' ↔ ',⍕⍎R←F,'/',⍕V
[2]   A←(¯2+R←⍴V)⍴')'
[3]   R←(,(' ',[1](((¯2+R),2)⍴F,'('),[1] 1 2 ⍴' ',F),
      0 1 ↓⍕(R,1)⍴V),A
[4]   (' '≠R)/R
     ∇


     ∇ F SCAN V;I;T;R
[1]   F,'\',(⍕V),' ↔ ',⍕⍎F,'\',⍕V ⋄ ' '
[2]   (5↑⍕T),' ↔ ',⍕T←V[¯1+I←2]
[3]  M1:R←(¯2+T←⍴I↑V)⍴')'
[4]   T←(,(' ',[1](((¯2+T),2)⍴F,'('),[1] 1 2 ⍴' ',F),
      0 1 ↓⍕(T,1)⍴V),R
[5]   (5↑⍕⍎T),' ↔ ',2↓T
[6]   →M1×⍳(⍴V)≥I←I+1
     ∇


     ∇ A ENCODE B;T;I;C;N;R
[1]   (⍕A),' ⊤ ',(⍕B),' ↔ ',⍕N←A⊤B
[2]   I←⍴N ⋄ R←'' ⋄ A←1↓A
[3]  LOOP:→FINISH×⍳0=I←I-1
[4]   R←R,'(',(¯1↓,(⍕N[1],[1](I,1)⍴A),'×'),')+'
[5]   N←1↓N ⋄ A←1↓A
[6]   →LOOP
[7]  FINISH:(' '≠R)/R←R,⍕N
     ∇


     ∇ R←A DECODE B;T;I;C
[1]   (⍕A),' ⊥ ',(⍕B),' ↔ ',⍕A⊥B
[2]   A←1⌽(⍴B)⍴A ⋄ T←0 ⋄ R←(0,⍴B)⍴I←1
[3]  M1:C←((I-1)⍴0),T←T+B[I] ⋄ R←R,[1]C,(T←T×A[I]),((⍴B)-I+1)⍴0
[4]   →M1×⍳(⍴B)>I←I+1
[5]   R←(0,A),B,[1]R,[1](-⍴B)↑T+¯1↑B
     ∇
```

Mr C.E.Williams from Loweswater wrote to Anthony Camacho concerning some problems he has had with I-APL. First Mr Williams makes an appeal for help with understanding APL, pointing out that it takes a long time for a letter to permeate through Education Vector back to the author, making rapid progress difficult. The point is well taken and if any reader wishes faster relief from the inevitable niggling problems, then I for one would be more than happy to receive a telephone call - which I would do my best to answer on the spot. So here is the telephone number - [telephone number omitted]. Any other offers?

Mr William’s particular problem concerned using DECODE to evaluate the values of a polynomial. I have checked the stated problem and I was able to replicate it with my version of I-APL - namely that DECODE will not accept a matrix left argument - for example `(2 1⍴4 3)⊥2 10` should yield the vector `18 16`, corresponding to the separate calculations `4⊥2 10` and `3⊥2 10`. This is rather unfortunate, and I hope it has not discouraged Mr Williams from using APL, particularly for use with electrical circuit theory - I wonder have you read Bob Spence’s book on Electrical Circuit Theory using APL? (Bob Spence is Professor of Electrical Engineering at Imperial College and his book is a superb example of how APL can be used as an educational tool to aid understanding.)

Mr Williams also makes comments about the conflicting messages within the pages of VECTOR concerning styles of programming. (Should we or should we not use parentheses and the diamond separator?) I would agree that it is confusing to the beginner to have such contradictory advice. Nevertheless it is probably impossible to avoid it! The only golden rule is to pursue such practices as make it easier for you to produce correct code that is readable to others and to yourself at a later date.

My final letter, from Norman Thomson, (my predecessor as Education Officer) shows only too clearly that submitted code will always be open to criticism by others. And that is how it should be. Please, please do not stop sending me your contributions in whatever style of programming you think appropriate!
