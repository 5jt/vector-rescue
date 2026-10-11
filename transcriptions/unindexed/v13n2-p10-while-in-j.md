---
title: While in J...
authors:
- Nick Cox
volume: '13'
issue: '2'
page: '10'
unindexed: true
transcribed: 'from page images of VOL.13-NO.2-OCTOBER-1996.pdf, pages 12–13 (printed 10–11; within Correspondence, after Eddie Clough’s letter on Vector 12.3, before Howard Peelle’s “Sylvester’s Algorithm (Again)”, art10006590); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- performance
queries:
- "Printed heading “While in J ...”. The byline prints the author’s e-mail address after his name; omitted here."
- "The formula line is faintly printed; read as `api[i] = precip[i-1] + k * api[i-1], 0 < k < 1`."
- "Kept as printed: “any one who wanted”; `api1` adds `(i { p)`, not the previous day’s precipitation as in the formula."
---

*From: Nick Cox, 8 June 1996*
{ .byline }

The so-called ‘antecedent precipitation index’ is a measure of the wetness of a catchment. Precipitation (rainfall, snow, etc.) makes a place wetter but such water is lost from a site over time by evaporation and drainage.

```
api[i] = precip[i-1] + k * api[i-1], 0 < k < 1
```

is one way of trying to capture this balance fairly simply.

The idea is pretty crude engineering hydrology and the API is naturally inferior to any number based on real measurements at a site. In practice, however, daily precipitation measurements for somewhere similar are far more readily available than are comparable soil moisture measurements, especially over long historical periods. I don’t know much folklore on estimating *k*, but one rough physical guide is that at most places wetness fluctuates about an average, especially on time scales of the order of a year. This allows you to bracket plausible values of *k*.

That is just context. Like the typical reader of Vector, when reading such simple formulae, I often write down the corresponding simple programs. To me, with a brain warped by too many years of Fortran and Basic, and improved slightly by exposure to various C-like languages, what springs to mind first is something like `api1`. To any J or APL enthusiast, `api1` looks incredibly long-winded for such a mathematically trivial problem. And indeed in the best and worst traditions of APL a program can certainly be produced in one line, as for example `api2`.

Yet experiments clearly show that `api2` is much slower and more demanding of space, as examination of the programs suggests. Can a quicker yet concise J script be produced?

As yet more context, any one who wanted to do this could easily have 1000 daily rainfalls, and in fact I will want to do something similar for more like 40,000 values. (I’ll probably do it with totally different software, but largely for reasons irrelevant to this journal.)

```j
api1 =. 3 : 0
NB. antecedent precipitation index NJC 15 April 1996
NB. k api p
:
k =. x.
p =. y.
api =. 0
i =. 0
while. i < #y. do.
api =. api , (i { p) + k * {: api
i =. i + 1
end.
}. api
)

api2 =. 3 : 0
NB. antecedent precipitation index NJC 15 April 1996
NB. k api p
:
+/"1(* x.&^@i.@-@#)\ y.
)
```
