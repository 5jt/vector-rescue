---
title: Year 2000 — why the Consternation?
authors:
- Bob Brown
volume: '14'
issue: '1'
page: '8'
unindexed: true
transcribed: 'from page images of VOL.14-NO.1-JULY-1997.pdf, pages 10–11 (printed 8–9; within Correspondence, after Joseph De Kerf’s “The Enclose of an Empty Array”); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- development practice
queries:
- "A letter in Correspondence, From: Bob Brown, 23 March 1997; the last letter in the section, followed by a house notice for Vector back numbers."
---

*From: Bob Brown, 23 March 1997*
{ .byline }

There have been several articles in the press about major problems with computers dealing with the year “00”. I haven’t paid much attention because the way I have designed my applications during the past 40 years means that I know that “00” means 2000, not 1900 (or even 1800) and “01” means 2001.

Apparently more fuel has been added to the fire by ISO9000 “century compliant” standards. So I spent something under an hour modifying a couple of standard utilities that are prevalent in my application.

## Internal representation

`CALJUL` takes any date and returns an internal representation based on the days since 31 December 1900. `CALJUL 32597 32599 32501` yields `35149 35879 36609`. The internal representation is not something that a person can read and make any sense of, but it does make it very easy to figure out how many days are between any pair of calendar dates.

With a bit of modification `CALJUL 3251997 3251999 3252001` gives the same internal representation. Incidentally this function is in the application because back in the mid 60s (1960s that is) I was about to leave to make a presentation in England and suddenly realized that I wanted to be able to read and write dates as dd/mm/yy as well as mm/dd/yy. The user can set a switch to determine which way makes dates more familiar in his environment.

## External representation

The other function `DTFMT` takes any internal representation and generates a formatted date, with two- or four-digit years.

`DTFMT 35149 35879 36609` generates  
`3/25/1997 3/25/1999 3/25/2001`.

The user can flip a switch so that the result comes out `25/3/1997 25/3/1999 25/3/2001`. It obviously doesn’t matter to the output how the internal representation was generated. Since it took so little time to modify two very simple utility functions that always deal with all dates throughout the application, why are consultants making so much money addressing this consternation?
