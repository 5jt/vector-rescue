---
title: Surely There Must Be A Better Way; Hacker’s Corner (1)
authors:
- Dave Ziemann
- Adrian Smith
volume: '3'
issue: '1'
page: '101'
unindexed: true
transcribed: 'from page image of VOL.3-NO.1-JULY-1986.pdf, page 103 (printed 101; Hacker’s Corner (2), art10008190, follows on p.102); Claude, 2026-10-05'
review: draft
queries:
- "The contents list gives “Surely There Must Be a Better Way, Ziemann and Smith” for pp.101 on; Hacker’s Corner (2) (pp.102–103) is indexed separately as art10008190."
- "TSOID is printed in a dot-matrix italic APL face. [13] `XX←,⍉(4⍴256)⊤DATHS` (⍉ read from a ○\\-like glyph); [14]–[15] the character table uses ∆ (printed as a solid triangle) as filler for codes with no letter, an EBCDIC-order alphabet; [16] `R←ZC[(⍴ZC)⌊¯192+(¯1↑XX)↑XX]`. Doubtful glyph readings; transcribed as read."
- "[5] is printed `C← 1 0 1 0 ⎕SVC 2 5 ⍴'CTLMSDATMS'` and [4] `C←102 ⎕SVO 2 5 ⍴'CTLMSDATMS'`, though the variables are CTLMS and DATHS: the M/H shapes are hard to tell apart in this face. Transcribed as printed."
---

by Dave Ziemann
{ .byline }

This issue of VECTOR includes an article by Robert Pullman on apportioning data in APL. You’ll find it later on in the technical section. Can anyone find an alternative solution to Robert’s \<CROSS\> function?

## Hacker’s Corner (1)

*by Adrian Smith*

Following up on my attempt on the integrity of the TSO/APL Session Manager, I thought it might be time to explore the hacking potential of the workspace access processor (AP102 – authorized personnel only). Here is an alternative route to your TSO Logon Id, for which many thanks to Andy Chadwick of our Technical Support Group:

```apl
     R←TSOID;C;CTLMS;DATHS;BASE;OFF;XX;ZC
     ------------------------------------
[1]   ⍝DIG OUT YOUR USER ID, HAVING CHAINED DOWN
[2]   ⍝THREE LOTS OF CONTROL BLOCKS TO FIND IT.
[3]   ⍝
[4]    C←102 ⎕SVO 2 5 ⍴'CTLMSDATMS'
[5]    C← 1 0 1 0 ⎕SVC 2 5 ⍴'CTLMSDATMS'
[6]    CTLMS←1,540,4
[7]    BASE←DATHS
[8]    CTLMS←1,(BASE+180),4
[9]    OFF←DATHS
[10]   CTLMS←1,(OFF+264),4
[11]   OFF←DATHS
[12]   CTLMS←1,OFF,8
[13]   XX←,⍉(4⍴256)⊤DATHS
[14]   ZC←'ABCDEFGHI∆∆∆∆∆∆∆JKLMNOPQR∆∆∆∆∆∆∆STUVWXYZ'
[15]   ZC←ZC,'∆∆∆∆∆∆0123456789?'
[16]   R←ZC[(⍴ZC)⌊¯192+(¯1↑XX)↑XX]
     ∇
```

Unfortunately, this operates only in ⎕PEEK mode; real hackerdom begins with ⎕POKE, as illustrated.
