---
title: Polyadic MORTGAGE as an APL2 operator
authors:
- Claude Henriod
volume: '18'
issue: '3'
page: '46'
unindexed: true
transcribed: 'from page images of VOL.18-NO.3-JANUARY-2002.pdf, pages 48–49 (printed 46–47; within The Education Vector, the first letter under the Letters heading); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- language design
queries:
- "The first letter under the Letters heading, untitled in print; the title is ours. It answers the Limbering Up task “Polyadic Functions” in 18:1 (unindexed/v18n1-p37-limbering-up-polyadic-functions.md). It is followed by Gianluigi Quario’s letter (unindexed/v18n3-p47-mortgage-with-a-companion-operator.md)."
- "`MORTGAGE` was run in Dyalog APL as a check on the transcription; it gives the five printed results, except that Dyalog shows 912.8399257 where the print has 912.8399258 (twice). Kept as printed."
- "The letter ends with the address of the author’s firm, “CHI - Claude Henriod Informatique”, in Savièse, Switzerland, and an e-mail address; the postal and e-mail addresses are omitted as private data."
- "Kept as printed: “74 years old, but not so atrophied, it seems ?”, “it is 2 possibilities”."
---

*From: Claude Henriod*
{ .byline }

My idea to resolve the Monthly Discount Rate proposed in Vector Vol.18.1 page 37-38. 74 years old, but not so atrophied, it seems ?

Each `IDEAn` variable is to be executed (`⍎`)

`Mortgage` is an IBM-APL2 operator

Syntax is : `LA (LO MORTGAGE) RA`<br>
Syntax is : `INT (PRIN MORTGAGE) TERM`

If `⍴INT ≡ ⍴TERM`, it is 2 possibilities :

`(.08 .09)(90000 MORTGAGE) 20 25` give a `2×2` Matrix<br>
`(.08 .09)(90000 MORTGAGE)¨20 25` give a Vector of `2` terms

```apl
      ∇MORTGAGE[⎕]∇
[0]   PMT←INT(PRIN MORTGAGE)TERM;V;W
[1]   ⍝ POLYADIC FUNCTION. VECTOR VOL.18.1
[2]   ⍝ PMT←PRIN÷(V-V*1+12×TERM)÷1-V←÷1+INT÷12 ⍝ PROPOSAL
[3]    V←÷1+INT÷12
[4]    W←V∘.*1+12×TERM
[5]    V←⍉(⌽⍴W)⍴V
[6]    PMT←PRIN÷(V-W)÷1-V
[7]   ⍝ W←(V←÷1+INT÷12)∘.*1+12×TERM ⍝ TWO-
[8]   ⍝ PMT←PRIN÷(V-W)÷1-V←⍉(⌽⍴W)⍴V ⍝ STMT
[9]   ⍝ CHI, SWISS. AN IBM-APL2 OPERATOR.
    ∇ 2001-10-09 21.03.27

      IDEA1
(9÷100)(90000 MORTGAGE)30
      ⍎IDEA1
724.1603553
      IDEA2
(9÷100)(90000 MORTGAGE)15 20 25 30
      ⍎IDEA2
912.8399258 809.7533603 755.2767273 724.1603553
      IDEA3
(8 9 10÷100)(90000 MORTGAGE)15 20 25 30
      ⍎IDEA3
860.0868759 752.7960621 694.6345974 660.3881165
912.8399258 809.7533603 755.2767273 724.1603553
967.1446059 868.5194806 817.830671  789.8144131
      IDEA4
(8 9 10÷100)(90000 MORTGAGE)20 25 30
      ⍎IDEA4
752.7960621 694.6345974 660.3881165
809.7533603 755.2767273 724.1603553
868.5194806 817.830671  789.8144131
      IDEA5
(8 9 10÷100)(90000 MORTGAGE)¨20 25 30
      ⍎IDEA5
752.7960621 755.2767273 789.8144131

      2 3⍴⎕TS
2001 10 9
  21 38 9
```

CHI - Claude Henriod Informatique
