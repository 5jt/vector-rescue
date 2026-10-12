---
title: 'APL at the Leading Edge: Nov 18th at the Royal Over-Seas League'
authors:
- Adrian Smith
volume: '5'
issue: '3'
page: '56'
unindexed: true
transcribed: 'from page image of VOL.5-NO.3-JANUARY-1989.pdf, page 58 (printed 56; introduces art10007050 and art10005130); Claude, 2026-10-12'
review: draft
tags:
- APL community
- performance
queries:
- "Contents line “Nov 18th: APL at the Leading Edge”, with no author; the title is the printed heading, and the printed byline is “introductory notes by Adrian Smith”. The Recent Meetings section’s own contents list (printed 55) gives “Summary of Meeting” to Adrian Smith and “Parallel Processing” to John Adams, both on page 56; the page credits the parallel-processing talk to Tom Lake of Intercept Systems."
- "Kept as printed: the full stop after the closing quotation mark of “why don’t they get on with it!”."
---

*introductory notes by Adrian Smith*
{ .byline }

**Allan Prys Williams** contrasted the way APL works with the way a rule-based system is built, and ended by showing how you could combine the approaches to provide existing software with an intelligent front-end. His notes follow this introduction.

**Brian Lochran** showed how United Glass had moved a substantial APL planning system from a mainframe (ADRS II) environment to a network of IBM 6150 machines using Dyalog APL and SQL. His notes are on page 75.

**John Adams** reviewed his experiences at the recent APL/AI conference in New York. His notes appear in VECTOR 5.2.

Finally, **Tom Lake** of Intercept Systems gave us an overview of parallel systems. This was one of those useful talks which came from a non-APL perspective. Tom defined 'parallel' as "several computers under the control of a single program". He described the evolving 'culture of the parallel' in applications such as:

- the simulation of physical systems. Fluid flow, weather forecasting, aerodynamics and so on. Also analysis of stress in engines and structures.
- animated graphics. This could be anything from Walt Disney to studies of molecular folding in drug design.
- image processing, particularly of radar and sonar images.

There are two approaches to building a parallel system:

- by repetition. The pipeline approach: instructions follow each other in short order through custom-designed chips. 20 Mflops are achievable if you keep them fed.
- by replication, e.g. DAP which has 4096 little simple processors all doing the same thing. Programmed in a sort of FORTRAN using vector and array types in a vaguely APL-ish sort of way.

Tom closed by noting that parallel people are willing to put a lot of work into the program to make life as easy as possible for the compiler. APL is something of a paradox, being a language where someone put a lot of work into the interpreter to make life as easy as possible for the programmer, and yet it seems eminently suitable for parallel processing. As was said of Chi Chi and An An "why don't they get on with it!".
