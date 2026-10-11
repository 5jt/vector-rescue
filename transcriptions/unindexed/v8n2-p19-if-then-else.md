---
title: IF-THEN-ELSE (Education Vector, April 1991, p.27)
authors:
- Robert L. Briechle
volume: '8'
issue: '2'
page: '19'
unindexed: true
transcribed: 'from page images of VOL.8-NO.2-OCTOBER-1991.pdf, page 23 (printed 19; within The Education Vector, the first of its Letters, before Andy Pole’s); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- user interfaces
queries:
- "A letter under the heading “Letters” in The Education Vector, headed “From: Robert L. Briechle, Cleveland, Ohio. IF-THEN-ELSE (Education Vector, April 1991, p.27)”, with an editor’s comment."
- "Kept as printed: `chrstr` in the comments."
---

## Letters

*From: Robert L. Briechle, Cleveland, Ohio.*
{ .byline }

**IF-THEN-ELSE (Education Vector, April 1991, p.27)**

A slight modification to allow the simpler construct, IF-THEN without the ELSE to operate if that was desired:

```apl
      ∇ R←A ELSE B
[1] ⍝---FL1: IF <APL chrstr> THEN <APL chrstr>
                             ELSE <APL chrstr> construct
[2]  M←(⍴A←,A)⌈⍴B←,B ⋄ R←(2,M)⍴(M↑A),M↑B
      ∇

      ∇ IF S
[1] ⍝---FL1: IF <APL chrstr> THEN <APL chrstr>
                             ELSE <APL chrstr> construct
[2] ⍎S
      ∇

      ∇R←C THEN A
[1] ⍝---FL1: IF <APL chrstr> THEN <APL chrstr>
                             ELSE <APL chrstr> construct
[2] ⍎(~¯1+⍴⍴A)/'→0,0⍴R←(⍎C)/A' ⋄ R←A[1+~⍎C;]
     ∇
```

I write APL code entirely without interaction with any humans, relying heavily on VECTOR, SIGAPL and the like for guidance. If you can recommend a good screen data input facility, I’d sure like to hear about it. I have written four or five for specialized use myself and have looked at several packages and bought one of them. I do not wish to have my workspaces prostituted with all kinds of objects about which I know little and which are named to conventions different from my own. I want a single object, perhaps written in C, which can be invoked on a setup basis (giving it a map of the screen together with a table of fields and attributes) and then called to manage screen input, allowing functions of my own to be executed (optionally) upon leaving any field. I want the data to be automatically sent from the screen to be scrollable or pageable up and down as I need that. And I want function-key-callable dialog boxes and information messages to pop up as needed. I know there are products which meet some or all of these requirements. If you know of any which you can recommend, I’d appreciate it.

*(Editor’s comment: Any suggestions will be forwarded. If they are of general interest, they will be published.)*
