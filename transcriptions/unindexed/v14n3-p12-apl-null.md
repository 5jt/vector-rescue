---
title: APL Null
authors:
- Ajay Askoolum
volume: '14'
issue: '3'
page: '12'
unindexed: true
transcribed: 'from page images of VOL.14-NO.3-JANUARY-1998.pdf, page 14 (printed 12; within Correspondence, after George MacLeod’s “Finding an Elephant”); Claude, 2026-10-11'
review: draft
tags:
- language design
queries:
- "A letter in Correspondence, From: Ajay Askoolum, January 1998; the last letter in the section, followed by News from Sustaining Members. R.G. Selfridge replies in Vector 14.4 (“Re APL Null Vector Vol 14 No 3”)."
- "The underlined epsilon of the third and fourth examples is printed as `∊` with an underbar, the APL*PLUS find function; set as `⍷`."
---

*From: Ajay Askoolum, January 1998*
{ .byline }

APL character null `''` (or `0/'anystring'`) and numeric null `⍬` (or `0/any numeric vector`) surprised me. I have checked this with APL\*PLUS III, APL\*Win, Sharp APL and Dyalog/APL: all these interpreters behave identically. Therefore, tempted as I am, I cannot call this a bug. However, I would like to be able to express what is happening in words.

```apl
''∊'ABCD'          ⍝ Returns null
'ABCD'∊''          ⍝ Returns 0 0 0 0
''⍷'ABCD'          ⍝ Returns 1 1 1 1
'ABCD'⍷''          ⍝ Returns null
```

The results are consistent when `1 2 3 4`, say, is substituted for `'ABCD'`.

```apl
'A'∧.=0/'ABCD' ⍝ Returns a surprise 1
```

as does

```apl
(0/'ABCD')∧.='A'
```

What is APL doing? The surprise result which prompted me to look into this was

```apl
2∧.=0/1 1
```

or more generally, `2∧.=condition/value` which caused my function to branch to a routine I had not expected. I would have expected the result to be null or zero.

Can you express what APL is doing in words?
