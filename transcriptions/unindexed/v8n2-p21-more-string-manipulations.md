---
title: More String Manipulations (Education Vector, July 1990)
authors:
- Peter Branson
volume: '8'
issue: '2'
page: '21'
unindexed: true
transcribed: 'from page images of VOL.8-NO.2-OCTOBER-1991.pdf, page 25 (printed 21; within The Education Vector’s Letters, after Tony O’Hagan’s, before Science Education in California); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- education
queries:
- "A letter under Letters in The Education Vector, headed “From Peter Branson, Uxbridge, Middlesex. More String Manipulations (Education Vector, July 1990)”. It answers Alan Sykes’s article (art10009600) and its function DAYOFWEEK."
- "Kept as printed: “professes to not even trying”."
---

*From Peter Branson, Uxbridge, Middlesex.*
{ .byline }

**More String Manipulations (Education Vector, July 1990)**

In this article, Alan Sykes gives a little function named *DAYOFWEEK* which, given the month and year, finds the weekday number (starting with Monday). Alan attributes *DAYOFWEEK* to Jerry Turner and professes to not even trying to understand it. As they say: “Me too, neither!”. Instead, I give below an alternative called *WEEKDAY*, which I believe is rather easier to understand:

```apl
      ∇WD←WEEKDAY;CONST;YRMO;DAYS
[1] ⍝ Get day of the week     Peter B  Util  Apr 91
[2] CONST←0 8 25 5 1 9 5 13 21 17 25 21
[3] YRMO←(⎕TS[1]-1900)+CONST[⎕TS[2]]
[4] WD←7|⎕TS[3]+(7|YRMO)+⌊((28|YRMO)+3)÷4
[5] ⍝
[6] ⍝ To return name of day, instead of no, add next 2 lines
[7] ⍝ DAYS←7 4⍴'SUN MON TUE WED THU FRI SAT '
[8] ⍝ WD←DAYS[WD;]
      ∇
```

Note the different calling syntax since it doesn’t need any arguments at all. Also there are a suggested couple of fairly obvious extra lines which can be de-commented to give the name of the day, instead of the number, if preferred. Note also that I am a bit more conventional, so Sunday is Day 1 here.

On the same sort of theme, another sometimes-useful utility function, using a similar technique, is *JULDAY* which gives the Julian Day number:

```apl
      ∇JD←JULDAY
[1] ⍝ Get Julian day number  Peter B  Util  Nov 90
[2] JD←0 31,(28+0=4|⎕TS[1]),31 30 31 30 31 31 30 31 30
[3] JD←⎕TS[3]++/⎕TS[2]↑JD
      ∇
```
