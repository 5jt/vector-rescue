---
title: More on Finding the Location of that PSP...
authors:
- Dave Phillips
volume: '6'
issue: '2'
page: '115'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, pages 117–118 (printed 115–116; within Technical Correspondence, after unindexed/v6n2-p115-hackers-corner-dos-environment-variables.md); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- programming techniques
queries:
- "A letter, From: Dave Phillips, 15th September 1989, on the Hackers Corner “DOS Environment Variables” in Vector 5.4 (art10008260). Signed “Dave Phillips, Principal Support Consultant, Cocking & Drury Ltd.”"
- "In line [15] the underscored epsilon is read as ⍷; in line [19] the underscored delta as ⍙; in line [22] the compress is printed as ⌿. The comment in line [19] is printed “TAÏLORING” with a mark over the I, read as a blemish."
- "Kept as printed: “merci trez bien!”; “SESSION MNG”."
---

*From: Dave Phillips, 15th September 1989*
{ .byline }

I was delighted to read that most useful piece of insight regarding how to acquire DOS Environment Variables from an APL\*PLUS/PC system. (VECTOR Vol.5 No.4 - Hacker’s Corner). The ability, as you so rightly say, for one’s APL system to get runtime information from the external environment (e.g. the actual name of a data-file to use - almost like tying a DDNAME to a DSNAME in MVS/JCL, only better!) is most appealing.

I would like to point out, however, that the piece of code you supplied will only work for the Standard APL\*PLUS/PC System. This is because the location of the Program Segment Prefix address is no longer at the same offset to the function key table in the new Extended System (with Session Manager) that is available in APL\*PLUS/PC r8. All is not lost; an alternative method of locating the PSP is provided by DOS itself and is applicable to all flavours/releases of APL\*PLUS/PC.

I was recommended to closely examine the IBM DOS Technical Reference, (I have DOS 3.30), wherein is to be found a list of programmed calls that can be made via Int21. A call 62h to this interrupt yields, as a return value, the address of the PSP directly. At least it does for DOS 3.0 and above; for earlier DOS releases, use of the undocumented call 51h produces the desired effect. From there on, your code, or rather M. Philippe Denoyelle’s code, works as is. (Monsieur Denoyelle: merci trez bien!)

I am including a copy of the reworked code below. I hope this may be of some additional benefit. One further point I should make is that this approach is not applicable to the APL\*PLUS II System. However, I do have a solution for that environment, care of a private communication from STSC, should you or other VECTOR readers wish to have it.

Dave Phillips  
Principal Support Consultant  
Cocking & Drury Ltd.

```apl
      ∇ R←DOS∆ENV SEL;AV;DOS;ENV;PSP;V;X;⎕IO;⎕SEG
[1]    ⍝∇DETERMINE DOS ENVT VARIABLES WITH OPTIONAL PREFIX <SEL>
[2]    ⍝∇UNDER APL*PLUS/PC, INCLUDING SESSION MNG IN /PCR8, ET SEQ.
[3]    ⍝∇USAGE: R←DOS∆ENV '' RETURNS ALL DOS VARIABLES
[4]    ⍝∇ R←DOS∆ENV 'C' RETURNS ALL DOS VARS. STARTING 'C'
[5]     ⎕IO←0 ⋄ V←⍬
[6]    ⍝ DETERMINE DOS VERSION USING INT21H CALL 30H
[7]    ⍝ (N.B. CALCULATE 30H←→16⊥3 0 0 0 - I.E. 12288DEC)
[8]     DOS←1↑⌽ 256 256 ⊤''⍴12288 ⎕INT 33
[9]    ⍝ FIND PSP ADDR. USING INT21H CALL 62H (25088) FOR DOS 3.0+
[10]   ⍝ OR CALL 51H (20736) FOR PRE-DOS 3
[11]   ⍝ PSP SEGMENT ADDR. IS SECOND ELEMENT OF RETURN FROM CALL
[12]    PSP←((25088 20736)[DOS<3]⎕INT 33)[⎕IO+1]
[13]   ⍝ OFFSET 2CH (44) IN PSP GIVES SEGMENT ADDR. FOR ENVIRONMENT
[14]    ⎕SEG←PSP ⋄ ENV←256⊥⎕PEEK 45 44
[15]   L1:⎕SEG←ENV ⋄ V←V,⎕PEEK⍳256 ⋄ X← 0 0 ⍷V ⋄ →(∨/X)/L2
[16]    ENV←ENV+16 ⋄ →L1 ⍝ LOOP UNTIL WHOLE TABLE IS READ
[17]   ⍝ TRANSLATE RETRIEVED NUMERIC VALUES INTO TEXT
[18]   L2:AV←⎕AV
[19]   ⍝ AV[64 36 61]←'⍙∆←' ⍝ OPTIONAL TRANSLATE TAILORING
[20]    V←AV[(X⍳1)↑V] ⋄ R←SSTOMAT ⎕TCNUL,V
[21]    SEL←,SEL ⋄ →(⍴SEL)↓0 ⍝ IF <SEL> IS REQUESTED...
[22]    R←(R[;⍳⍴SEL]∧.=SEL)⌿R ⍝ ...TAKE SUBSET
      ∇
```
