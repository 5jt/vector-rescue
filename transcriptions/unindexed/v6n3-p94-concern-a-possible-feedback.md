---
title: 'Concern: a possible feedback'
authors:
- Claude Henriod
volume: '6'
issue: '3'
page: '94'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, pages 96–98 (printed 94–96; within Technical Correspondence, after unindexed/v6n3-p93-more-on-ambivalent-operators.md); Claude, 2026-10-11'
review: draft
tags:
- language design
- programming techniques
- performance
queries:
- "A letter in Technical Correspondence, From: Claude Henriod, 21 July 1989, to David Piper, who forwarded it with his reply (unindexed/v6n3-p93-more-on-ambivalent-operators.md). “Concern: a possible feedback.” is the letter’s subject line, used as its title. It is followed by Norman Thomson’s “Yet More on that Ambivalent Operator ...” (p.97)."
- "The session listings are printed in an italic APL face. In ISUB the reduction after `ICAN-` is printed as a slash with a bar, read as ⌿. The APL comment symbol prints like a small A; read as ⍝."
- "The postal address after the signature (Monteiller, Savièse, Switzerland) is omitted."
- "Kept as printed: “more closely to an idiom of APL”; “MULTI-PRECESION”; the long comment line and AVERAG1[2] broken across two lines as printed; “AVERG0 VEC” for AVERAG0."
---

*From: Claude Henriod, 21 July 1989*
{ .byline }

Concern: a possible feedback.

Dear David,

I have just received Vector Vol 5 no 4 with your technical information about an "Ambivalent Operator". I found them very attractive for the comprehension and usage of a programmed operator. On my own usage I prefer the Execute form which is more closely to an idiom of APL. Next, the monadic *AVERAGE* produces a recursive loop taking more time. The line `AVERAGE[2]` is not very easy to understand and more complicated than the Execute or a 3 line processing. With I-APL using "Direct Definition" (stmt of maximum one line with 3 expressions) the recursive principle is of great interest.

> FUNC: L-Exp. (alpha, omega) : logical-Exp : default FUNC omega

```apl
      )WSID
MPCALC
      ⍝ MULTI-PRECESION CALCULATOR IS A WS OUT OF THE OFFERED
DISK
      ⍝ TO I-APL BY C.H.I. Swiss

      ⍝ ISUB IS A SAMPLE OF A RECURSIVE FUNCTION IF MONADIC CALL
      ⍝ THIS FORM IS VERY ATTRACTIVE FOR DIRECT DEFINITION

      ISUB:
ISUB: ICAN-⌿α ISYN ω : 2≠⎕NC 'α' : 0 0 ISUB ω

      0 1 2 ISUB 0 5
0 9997
      ISUB 0 5
0 ¯5


      )CLEAR
CLEAR WS
      )IN 10 PIPER
SAVED 1989-07-21 08.16.52 10 PIPER
      )FNS
AVERAG0 AVERAG1 AVERAG2 AVERAG3 XTIME
      )VARS
MINITESTDY MINITESTMO MINIVEC TESTDY TESTMO VEC
      )OPS
∆MONADIC
      (⍴VEC) (⍴MINIVEC)
20  5
```

```apl
      ∇AVERAG0[⎕]∇
[0]    AVE←SIZE AVERAG0 NUMS;RUN
[1]    ⍝ FUNCTION LIKE D.B. PIPER, USING AN OPERATOR
[2]     →(↑(RUN AVE)←(⍴NUMS)(AVERAG1 ∆MONADIC ⎕NC 'SIZE')NUMS)/0
[3]     AVE←(SIZE+/NUMS)÷SIZE
      ∇

      ∇AVERAG1[⎕]∇
[0]    AVE←SIZE AVERAG1 NUMS;RUN
[1]    ⍝ FUNCTION LIKE D.B. PIPER, USING AN OPERATOR
[2]     →(↑(RUN AVE)←(⍴NUMS)(AVERAG1 ∆MONADIC (⎕NC
'SIZE'))NUMS)/0
[3]     AVE←(SIZE+/NUMS)÷SIZE
      ∇

      ∇AVERAG2[⎕]∇
[0]    AVE←SIZE AVERAG2 NUMS
[1]    ⍝ FUNCTION USING EXECUTE FOR SIMPLE VISUALISATION
[2]     ⍎(2≠⎕NC 'SIZE')/'SIZE←⍴NUMS'
[3]     AVE←SIZE+/NUMS÷SIZE
      ∇

      ∇AVERAG3[⎕]∇
[0]    AVE←SIZE AVERAG3 NUMS
[1]    ⍝ FUNCTION, WITH OR WITHOUT LEFT ARGUMENT
[2]     →(2=⎕NC 'SIZE')/⎕LC+2
[3]     →0 AVE←+/NUMS÷⍴NUMS
[4]     AVE←SIZE+/NUMS÷SIZE
      ∇
      ⍝ HERE, IN THE MONADIC CASE, THE RESULT IS A SCALAR.


      ⍝ NOTE: AVERAG0 DOESN'T WORK WITH APL2/PS2
      AVERG0 VEC
SYNTAX ERROR
∆MONADIC[2]
[2]    →(2=CLASS)/R←0
             ∧

      ⎕NC 'CLASS'
3
```

```apl
      ⍝ TIMINGS WITH APL2/PC

    ⊂XTIME¨TESTMO
AVG CPU:   0.0291 Sec for  100   times of:  R1←AVERAG1 VEC
AVG CPU:   0.0171 Sec for  100   times of:  R2←AVERAG2 VEC
AVG CPU:   0.0148 Sec for  100   times of:  R3←AVERAG3 VEC
    ⊂XTIME¨TESTDY
AVG CPU:   0.0264 Sec for  100   times of:  R1←15 AVERAG1 VEC
AVG CPU:   0.0286 Sec for  100   times of:  R2←15 AVERAG2 VEC
AVG CPU:   0.0291 Sec for  100   times of:  R3←15 AVERAG3 VEC
    ⊂XTIME¨MINITESTMO
AVG CPU:   0.0291 Sec for  100   times of:  R1←AVERAG1 MINIVEC
AVG CPU:   0.0154 Sec for  100   times of:  R2←AVERAG2 MINIVEC
AVG CPU:   0.0142 Sec for  100   times of:  R3←AVERAG3 MINIVEC
    ⊂XTIME¨MINITESTDY
AVG CPU:   0.0203 Sec for  100   times of:  R1←4 AVERAG1 MINIVEC
AVG CPU:   0.0159 Sec for  100   times of:  R2←4 AVERAG2 MINIVEC
AVG CPU:   0.0148 Sec for  100   times of:  R3←4 AVERAG3 MINIVEC


      ⍝ TIMINGS WITH APL232

    ⊂WSTIME¨TESTMO,TESTDY,MINITESTMO,MINITESTDY
AVG CPU:   0.0235 Sec for  100   times of:  R1←AVERAG1 VEC
AVG CPU:   0.0122 Sec for  100   times of:  R2←AVERAG2 VEC
AVG CPU:   0.0085 Sec for  100   times of:  R3←AVERAG3 VEC
AVG CPU:   0.0203 Sec for  100   times of:  R1←15 AVERAG1 VEC
AVG CPU:   0.0149 Sec for  100   times of:  R2←15 AVERAG2 VEC
AVG CPU:   0.0165 Sec for  100   times of:  R3←15 AVERAG3 VEC
AVG CPU:   0.0205 Sec for  100   times of:  R1←AVERAG1 MINIVEC
AVG CPU:   0.0109 Sec for  100   times of:  R2←AVERAG2 MINIVEC
AVG CPU:   0.0099 Sec for  100   times of:  R3←AVERAG3 MINIVEC
AVG CPU:   0.0154 Sec for  100   times of:  R1←4 AVERAG1 MINIVEC
AVG CPU:   0.0138 Sec for  100   times of:  R2←4 AVERAG2 MINIVEC
AVG CPU:   0.0105 Sec for  100   times of:  R3←4 AVERAG3 MINIVEC

      ⍝ WSTIME EXECUTES A ⎕WA BEFORE EACH ELEMENTARY LOOP

      ⎕WA
5166576
```

Best regards

Claude Henriod
