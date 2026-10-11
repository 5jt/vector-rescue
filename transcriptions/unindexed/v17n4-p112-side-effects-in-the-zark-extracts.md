---
title: Side effects in the Zark extracts
authors:
- Jonathan Barman
volume: '17'
issue: '4'
page: '112'
unindexed: true
transcribed: 'from page image of VOL.17-NO.4.pdf, page 114 (printed 112; within Technical Correspondence, the first letter); Claude, 2026-10-11'
review: draft
tags:
- development practice
- programming techniques
queries:
- "The first letter under the Technical Correspondence heading, untitled in print; the title is ours. It refers to `COMMA∆MAT` in the Zark extract of 17:3 (unindexed/v17n3-p28-utility-corner-comma-delimited-data.md). It is followed by a second letter from Barman of the same date (unindexed/v17n4-p112-distributed-rounding-of-a-trial-balance.md)."
---

*From: Jonathan Barman, 22 March 2001*
{ .byline }

One aspect of the style of coding in the Zark extracts that I find difficult is the way functions are defined which return a result and also update one or more global variables. In Vol. 17 No 3 there was a typical example where the function `COMMA∆MAT` both returns a result and assigns a global variable `fieldwidths`. Of course, with a nested array APL one just returns the two items wrapped up as a two element vector and the function becomes ‘pure’ without any side effects. I think my displeasure is due to the fact that I have used nested arrays for such a long time that seeing a function with side effects is instantly categorised as being poorly coded. I find it quite difficult to remember how I attempted to solve the dilemma of multiple results with a non-nested APL, but I think I tried to make a clear separation between functions returning results and those which did not return a result. Only the non result returning functions were allowed to update or assign global variables. I have thrown away all my old code now, so I can’t tell if my memory is correct!
