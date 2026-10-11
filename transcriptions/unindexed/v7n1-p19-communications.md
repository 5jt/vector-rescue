---
title: Communications
authors:
- Alan Sykes
volume: '7'
issue: '1'
page: '19'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 21–24 (printed 19–22; within The Education VECTOR, after its Editorial); Claude, 2026-10-11'
review: draft
tags:
- education
- APL community
- programming techniques
queries:
- "Unsigned; printed under the heading “Communications” in The Education VECTOR, directly after the section’s Editorial (pp.18–19), and written in the voice of its editor, Alan Sykes. It is followed by Walter Spunde’s “Function Sampling with I-APL” (art10009260) on p.23."
- "The input glyph in `SOUND TABLE['.- '⍳⍞]` and in `MORSE` is printed as a quad with a tick inside, read as quote-quad ⍞. In `SEEK` the glyph before `((2,⍴B)⍴16)` is read as ⊖."
- "The text speaks of the inner product `M⌊.⍳X`, but the function `CARDS` that follows uses `M⌈.⍳C`; both kept as printed."
- "Kept as printed: “Makato Kikkawa”; “Howard Peelle sent has sent”; “Claude Henrion’s” (Claude Henriod); “round-the world”; the space in `W +1 0` in `CC`."
---

Looking through my file of correspondence, I realise that there are many letters and notes from people in different countries that I have not acknowledged. So here is some attempt to remedy this.

## From Nottingham, England

E.J.Sargeant replied to the questionnaire in the last issue, and commented on the problem of retrieving ASCII files into APL using IAPL. I must confess to not having time to investigate this, so may I ask readers who have used IAPL to read an ASCII file please to respond with a note to Education Vector discussing relevant details?

## From Hereford, England

Graham Bennett also wrote a reply to the questionnaire. Graham is a Maths and Computing teacher in a comprehensive school. He writes .. ‘I have been getting Education Vector for about two years but still have not bought an interpreter and am not using APL in the classroom. It may help you to know why.

In our school, and in others around, Computer Studies has recently been dropped both at A-level and GCSE because it is not perceived to be a very useful course for most students and it is felt better to devote time and resources on IT for all. This means that no one now studies programming in our school where previously we taught BASIC and Pascal. There is an emphasis on applications instead.

In Maths we are so busy struggling with the National Curriculum that no one has the time to look at how APL might be of use to us. ..... I do not know what you can do to make APL more known and used. The pressure all teachers are under makes it very hard for any but the most enthusiastic and dedicated to devote precious time to an unknown quantity like APL however good it may be.’

## From La Habra, California

Zdenek Jizba sent a letter to Anthony Camacho describing in part the way IAPL is used in the fifth grade (eleven years of age) to stimulate discovery and exploration. I would like to extend an invitation to Zdenek (and anybody else) to present a typical (or atypical!) exploration in Education Vector:- volunteers please.

## From Dunoon, Scotland

Mr Bill McLean may be just such a person to send me an account of using APL in investigative working? Bill tells me of his work in Physics, optical illusions, graphs, and playing Noughts and Crosses. I particularly liked his notes on how to produce Morse Code on a BBC 128 machine using IAPL. The first step is to produce a sound table for a dot, dash, space and longer space.

```apl
      TABLE
1 ¯12 101   1
1 ¯12 101   3
1   0   0   1
1   0   0  16
```

As a result `SOUND  TABLE[1 3 2 3 2 3;]` would produce .-- in sound.

Morse code corresponding to input from the keyboard can be achieved using `SOUND  TABLE['.- '⍳⍞]` if the user presses dot, dash or space.

To translate actual letters, the alphabet is required:

```apl
  ALPH←' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

together with a 27 by 9 character matrix called `CODE` whose first row for example contains `'. -      '`.

Then the function `MORSE` (written here in direct definition) will produce Morse Code corresponding to letters entered at the keyboard:

```apl
  MORSE: SOUND TABLE['.- '⍳CODE[ALPH⍳⍞;];]
```

## From Sendai, Japan

Makato Kikkawa wrote to Anthony Camacho to report the successful porting of IAPL to NEC machines by Mr Tohru Kawahata. Makato also reports that the translation of ‘An Encyclopedia of APL’ and ‘APL in Social Studies’ is well under way.

## From Kensington, New South Wales

Jim Douglas wrote to me concerning graph plotting using character graphics after reading an article I wrote in VECTOR on this subject. Jim is in the Department of Statistics at the University of New South Wales so we have lots of interests in common.

## From Amherst, Massachusetts

Howard Peelle sent has sent two communications to me from the University of Massachusetts at Amherst where he lectures in the School of Education. First he points out, quite correctly, that the answer to the puzzle on numbers and bases (Education Vector July 1989) given in Education Vector January 1990 was incorrect. There, I stated that the only bases from 10 to 100 that gave rise to two digit numbers being reversed when converted to base 16 were 10 13 16 19 22 25 28 37 46 55 64 73 and 82. These are in fact the bases which give rise to reversals when numbers are compared to base 10 and not base 16. So the correct answer, given by Howard is 10 11 13 16 21 26 31 46 61 76 and 91. Here is his solution:

```apl
      ∇ B←L IF C
[1]   B←C/L
      ∇


      ∇ N←SEEK B
[1]   N←B IF ∨/∧⌿((B,[.5]B)⊤N)=⊖((2,⍴B)⍴16)⊤N←⍳99
      ∇

      SEEK 9+⍳91
10 11 13 16 21 26 31 46 61 76 91
```

(N.B. this one-line solution gave me `WS  FULL` error when I tried it with `B←9+⍳91` - so you may have to use it repeatedly to get Howard’s result in toto.)

Howard also supplied a solution to the card collecting problem which he claims to be faster than Claude Henrion’s. It is:

```apl
      ∇ R←N CARDS C
[1]   R←1++/∨⌿∧\(⍳C)∘.≠?(N,11×C)⍴C
      ∇
```

Readers may also be interested in Howard’s ‘awfully inefficient’ recursive function which generates a probability tree in order to approximate the expected number of cards required:

```apl
      ∇ R←A CC W
[1]   R←W[1]
[2]   →0 IF (=/A)∨=/W
[3]   R←((÷A)× A CC W+1 0)+(1-÷/A)×(A+1 0)CC W +1 0
      ∇
```

but of course, the correct expected value for `N` cards is `N×+/÷⍳N`.

## From New York

Paul Mansour also wrote to me concerning the card-collecting problem. However, his solution makes use of the extra facilities that second-generation APL interpreters have to offer. If `X` is a vector and `M` is a matrix, then the inner product using `⌊` and `⍳`, i.e. `M⌊.⍳X` returns a vector of the first occurrence of an element of `X` in each row of `M`. Hence it is possible to simulate the card-collecting problem as follows:

```apl
      ∇ R←N CARDS C;M
[1]   M←?(N,11×C)⍴C ⋄ R←M⌈.⍳⍳C
      ∇
```

As you can see, this has been quite a round-the world trip. Please continue to send comments and correspondence particularly including code that you feel other readers might appreciate.
