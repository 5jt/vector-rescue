---
title: Optimizing the Antecedent Precipitation Index
authors:
- Norman Thomson
volume: '14'
issue: '1'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.14-NO.1-JULY-1997.pdf, page 9 (printed 7; within Correspondence, the first letter under the section heading); Claude, 2026-10-12'
review: draft
tags:
- programming techniques
queries:
- "The Contents line reads “Norman Thomson *et al*” under Correspondence; this file holds the section’s first letter, From: Norman Thomson, 12 May 1997, printed under the heading “Optimizing the Antecedent Precipitation Index”, with the editor’s note that follows it. The other letters (Thomson’s “APL and the rank operator”, De Kerf’s “The Enclose of an Empty Array”, Brown’s “Year 2000 — why the Consternation?”) have their own files."
- "The section heading “Correspondence” carries no text of its own."
---

*From: Norman Thomson, 12 May 1997*
{ .byline }

Am I missing something, or is Bob Bernecky unaware of decode (see Vector Vol.13 No.4 pp.7-11)? This solves the above problem in six characters, viz: `x⊥¨,\y` and incidentally runs about four times as fast on APL2/PC as either of Bob’s `api1` or `api3`. I described the analogous J version, namely `>@(#.&.><\)` , in Vector Vol.13 No.3 p. 12.

*[Ed - see also Andrei Buzin’s note on page 140]*
