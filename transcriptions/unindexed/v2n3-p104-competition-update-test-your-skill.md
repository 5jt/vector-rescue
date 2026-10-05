---
title: 'Competition Update: Test your Skill'
authors:
- David Ziemann
volume: '2'
issue: '3'
page: '104'
unindexed: true
transcribed: 'from page image of VOL.2-NO.3-JANUARY-1986.pdf, page 106 (printed 104; follows up v2n1-p99-prize-competition-result-test-your-skill.md; the Porsche competition follows on p.105); Claude, 2026-10-05'
review: draft
queries:
- "SM9 [4] prints the outer-product function as a glyph like A (∧ overstruck with ~ in this face), read as ⍲, as in the original SM9 (v2n1-p99). Here SM9 uses Z, LAB and LOOP in place of the original MAT, lab and Loop."
- "SMNAPS [1] is printed `Z←∧/↑(↓J)∘.∊↓C,0`, using APL*PLUS’s ↓ (split) and ↑ (mix)."
- "SM10 [3] is printed `Z←0=(×/P[J])∘.|×/P[C]`; the C has a stray mark above it. The primes still stop at 23, though the text says 29 must be added."
---

by David Ziemann
{ .byline }

Maurice Jordan from British Airways has kindly sent in some timings for the skillsmatch functions presented in VECTOR 2.1. Here are his results for Adrian Smith’s looping solution \<SM9\>, Maurice’s own APL\*PLUS nested arrays production system answer \<SMNAPS\> and the winning entry \<SM10\>. By the way, as Phil Last has correctly pointed out, the function \<SM10\> requires the addition of a 29 to the vector of prime numbers if 10 skills are to be correctly processed.

```apl
      JOBS
1 2 3
7 9 0
1 4 0
1 3 0
1 6 3
      CONS
1 2 3 7 0 0
1 3 7 9 2 6
7 9 0 0 0 0
1 6 5 3 9 0
      ⎕VR'SM9'
    ∇ Z←JB SM9 CN;SK;LAB;CT
[1]    SK←⌈/,JB
[2]    Z←((1↑⍴JB),1↑⍴CN)⍴1
[3]   LOOP:→LAB←1+(SK⍴LOOP),END,CT←1
[4]    Z←Z∧(JB∨.=CT)∘.⍲(CN∧.≠CT)
[5]   END:→LAB[CT←CT+1]
    ∇
      ⎕VR'SMNAPS'
    ∇ Z←J SMNAPS C
[1]    Z←∧/↑(↓J)∘.∊↓C,0
    ∇
      10 TESTTIME 'Z←JOBS SM9 CONS'
4.5
      10 TESTTIME 'Z←JOBS SMNAPS CONS'
2.3
      ⍝ But still the best
      10 TESTTIME 'Z←JOBS SM10 CONS'
0.4
      ⎕VR'SM10'
    ∇ Z←J SM10 C;P;⎕IO
[1]    ⎕IO←0
[2]    P← 1 2 3 5 7 11 13 17 19 23
[3]    Z←0=(×/P[J])∘.|×/P[C]
    ∇
```
