---
title: 'IBM Systems Journal: APL 25th Anniversary Edition'
authors:
- Adrian Smith
volume: '8'
issue: '4'
page: '72'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, pages 74–77 (printed 72–75); Claude, 2026-10-12'
review: draft
tags:
- reviews
- APL in perspective
queries:
- "Contents line “IBM Systems Journal (APL Edition)”; the printed heading is “IBM Systems Journal: APL 25th Anniversary Edition”. Printed byline “reviewed by Adrian Smith”."
- "Kept as printed: “by K.E Iverson”; “the ruthless elimination of the [I;J] notation on favour of an indexing function”; “by A. Aharon et al”."
---

*reviewed by Adrian Smith*
{ .byline }

## General Comments

This is clearly the most important collection of APL material for at least the past 10 years. It ranks alongside "A Source Book of APL" as an important milestone in the evolving history of the language, and I feel that anyone with a library of APL books should take steps to add this one to his or her collection.

Because of the importance of this work (and the relative difficulty and expense for non-IBM employees in getting hold of it), the British APL Association is hoping to agree a bulk shipment arrangement with the publisher, so that copies will be available to members at significantly less than the nominal $20 subscription rate. Details will be advised to members as soon as possible.

The presentation is excellent, with good typesetting of both APL and J, and diagrams up to *Scientific American* standard. There are remarkably few typos (I have just failed to re-find the only one I noticed on first reading), and the balance of material is about right. I was particularly pleased to see that the text is not totally limited to APL2 (NARS, Sharp APL and J all get coverage), and that several of the APL2 papers refer to implementations on small machines. A brief precis of each paper follows.

## The Preface

How gratifying to see an explicit reference to the British APL Association, and specifically the ASL project, in the introduction to Norman Thomson's paper. If this helps to get the ASL concept known outside the APL world, it can only do us good.

## The IBM family of APL systems

*by A.D. Falkoff*

A nice easy read, with a lovely diagram illustrating the genealogy of IBM's APL interpreters. Plenty of surprises, and some fascinating new insights on the influence APL has had on the designers of small machines. *Recommended for all readers.*

## APL2: Getting started

*by J.A. Brown & H.P. Crowder*

A gentle introduction to second-generation APL, with some nice examples from graph-plotting to the manipulation of sparse arrays. *Recommended for all except APL2 buffs!*

## Extending the domain of APL

*by M.T. Wheatley*

This is more or less a formalized version of Mike's talk to the British APL Association at Canterbury in 1988. As I said in Vector 5.2 (Nov 88) "A lot of really good hard 'inside information' on the early development of APL, and the way it fitted into its environment. The rationale behind `⎕NA` and the shared variable processors." *Recommended for mainly `⎕SVO` and `⎕NA` freaks.*

## Storage management in IBM APL systems

*by R. Trimble*

This is quite a tough technical paper, but the excellent diagrams help a lot! It could have a major influence on interpreter design in the approaching world of multi-gigabyte workspaces. *Recommended for interpreter writers, and those of the rest of us who like to know how these things really work.*

## Putting a new face on APL2

*by J.R. Jensen & K.A. Beaty*

More or less a rerun of their APL91 paper, but again the high quality diagrams and colour images help to make the point. *Definitely a skim-read for most of us; recommended for X-windows hacks.*

## The APL IL Interpreter Generator

*by M. Alfonseca, D. Selby & R. Wilks*

I first came across this one at Copenhagen (at a G.U.I.D.E. meeting) in 1979! (see 'Design Handbook' Chapter 13 for my thoughts on using APL to run your central heating system.) It is quite hard going, but worth the effort for anyone who wants to know where IBM APL2/PC and APL2/6000 are coming from. *Recommended for all techies and most of the rest of us.*

## Parallel expression in the APL2 language

*by R.G. Willhoft*

If APL is to exploit the parallel architectures of the future, it must build on the high degree of parallelism already implicit in the language. This paper explores the boundaries of present APL2 implementations, and makes a number of important recommendations for future language design. I suspect it may generate quite a vigorous debate! *A skim-read for most of us ... recommended for language designers and anyone interested in the far future of APL.*

## The foundations of suitability of APL2 for music

*by Stanley Jordan & Erik S. Friis*

This is a much easier read than the preceding papers! It shows how APL2 nested arrays can be used at a high level to model underlying musical structures (not just the actual notes). *Recommended (not just for musicians).*

## Verification of the IBM RISC System/6000 by a dynamic biased pseudo-random test program generator

*by A. Aharon et al*

This paper provides the general reader with an excellent introduction to the basic methodology of automated system testing, and then shows how (and why) VS APL and APL2 were used to build the test suite for the RS/6000 architecture. I felt it was most valuable as a primer in automatic verification techniques, rather than for its APL content. *Recommended for anyone interested in systems methodologies.*

## APL2 as a specification language for statistics

*by N.D. Thomson*

Norman briefly introduces the ASL project, and goes on to show how APL2 can be used to specify a collection of basic statistical algorithms. *Recommended.*

## Advanced applications of APL: logic programming, neural networks, and hypertext

*by M. Alfonseca*

The title says it all! The sections on Neural Nets and a Hypertext on-line dictionary are probably those of most general interest. *Recommended for appropriate specialists.*

## Language as an intellectual tool: from hieroglyphics to APL

*by D.B. McIntyre*

If you ever wanted to know how the ancient Egyptians managed to do division (with Hieroglyphs), you should read this paper! It is a fascinating ramble through the long and confused history of mathematical notation, and I would say it has something for everyone. The APL examples are shown in the classic `∇` form, in direct definition and also in J; I found it most refreshing that an IBM publication was able to include so much material from non-IBM versions of APL!

There are over two pages of closely-spaced references which should form a superb starting point for any reader who wants to take the subject further. *Highly recommended, but don't try to take it all in at one sitting.*

## A personal view of APL

*by K.E Iverson*

This paper needs to be read in conjunction with several earlier works (e.g. "The Design of APL" and "The Evolution of APL") to which it refers. It is actually a thinly disguised polemic on where APL went wrong, and why J is better! It discusses in detail such issues as the banning of niladic functions from J, and the ruthless elimination of the `[I;J]` notation on favour of an indexing function. APLers should be prepared to take several deep breaths, and count to 100 slowly. *Recommended for J freaks and APLers of an equable temperament.*

## Summary

Whether or not you agree with everything in it, if you are serious about your APL you should find a way of obtaining this collection of important and influential papers.
