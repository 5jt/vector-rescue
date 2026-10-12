---
title: The Education Vector
authors:
- Alan Mayer
volume: '8'
issue: '3'
page: '17'
unindexed: true
transcribed: 'from page images of VOL.8-NO.3-JANUARY-1992.pdf, pages 23–24 (printed 17–18); Claude, 2026-10-12'
review: draft
tags:
- education
- programming techniques
queries:
- "The Contents line gives the author as Alan Sykes; the section’s title page prints “Editor Alan Mayer” and its contents list credits the Editorial to Alan Mayer, so Alan Mayer is given here. The Editorial is unsigned in print; its byline is taken from that contents list."
- "The section’s own text only: its title page (printed 17, with its own contents list) and the Editorial (printed 18). The pieces it lists are transcribed separately: unindexed/v8n3-p19-simpsons-rule.md (the Letters, from Neil Sheldon), art10004160, art10000330 and art10001510."
- "Kept as printed: “Curve-fitting in APL” and “How to produce APL print on some Star printers with I-APL” in the section’s contents list."
- "Following the project rule for individuals’ contact details, the street address and telephone number of Anthony Camacho, printed as the British APL Association’s contact, are omitted; Alan Mayer’s university address, telephone, fax and JANET address are kept."
---

## The Education Vector

**January 1992**

***Editor Alan Mayer***

This Education Vector has been reprinted from VECTOR Vol.8 No.3. VECTOR is the Quarterly Journal of the British APL Association. For more information about the British APL Association, please contact: Anthony Camacho, [address and telephone number omitted].

### Contents

| | | |
|---|---|--:|
| Editorial | Alan Mayer | 18 |
| Letters | | 19 |
| An Instruction Sheet for Introducing APL to Lay Audiences (Teachers) | Zdenek V. Jizba | 19 |
| Curve-fitting in APL | David Appleton | 23 |
| How to produce APL print on some Star printers with I-APL | Camacho & Goodman | 29 |

> Dr Alan Mayer<br>
> European Business Management School<br>
> University College of Swansea<br>
> Singleton Park<br>
> Swansea SA2 8PP Wales, UK
>
> Ysgol Rheolaeth Busnes Ewropeaidd<br>
> Parc Singleton,<br>
> Abertawe SA2 8PP
>
> Tel. 0792 205678 Ext.4274 Fax: 0792 295626 JANET: MAYER@UK.AC.SWAN.MS

## Editorial

*by Alan Mayer*
{ .byline }

Welcome to Education Vector, and Happy New Year! 1992 has long been heralded as the year when we will discover the advantages of being European. As I write, discussions are going on in Maastricht which may bring great changes to the structure of government in all the countries of Western Europe. Even more profound changes are taking place further afield. Like many APLers I believe that APL has a significant role to play in bringing people of different languages and cultures together. It is a language that crosses all barriers and frontiers. If 1991 is anything to judge by, the pace of change will be bewildering. When we made tentative plans to hold APL92 in Leningrad, USSR, we did not expect to find the venue renamed St Petersburg - and recent reports suggest that the USSR itself will no longer exist by the time the conference takes place. Be that as it may, bringing together the world-wide APL community is an important aim, and our own efforts to "spread the word" in Education Vector should be designed to contribute to that aim.

While many readers do not yet have access to second generation interpreters, I feel that one of our functions should be to explore the possibilities of the very powerful extensions to the language that are now available. I am pleased to include an article by David Appleton in which he makes elegant use of multiple assignments in the field of curve-fitting. I for one would like to see more contributions telling us how best to make use of all these new toys!

Most of us have little functions sitting in odd workspaces, written to meet a particular need and then forgotten. I have several designed to introduce children to computers, and perhaps to help them learn other things as well. If you are nodding your head in agreement now, dig some of yours out and send them to me. My little contribution, to start the ball rolling, is a little program to help with the problem of multiplication (I carefully avoid the word "tables" - are they mandatory or illegal at the moment?)

```apl
[0]    MULTIPLY;ANS;I;RV;T;TARGET
[1]    RV←? 10 2 ⍴12
[2]    ANS←⍳0
[3]    I←1
[4]    T← 0 60 60 ⊥¯1↓¯4↑⎕TS
[5]    TARGET←×/RV
[6]   loop:'What is ',(⍕RV[I;1]),'×',(⍕RV[I;2]),'?'
[7]    ANS←ANS,1↑⎕
[8]    →(10≥I←I+1)/loop
[9]    'You scored ',(⍕+/ANS=TARGET),' out of 10'
[10]   'in ',(⍕(0 60 60 ⊥¯1↓¯4↑⎕TS)-T),' seconds'
```

Just type `MULTIPLY` and answer the questions as quickly as you can! I have tried to use "universal" APL - if you have to modify it to make it work, please write to me about it.
