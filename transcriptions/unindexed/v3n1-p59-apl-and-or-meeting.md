---
title: Introductory Notes; APL and Operational Research, January 17th 1986 (meeting notes)
authors:
- Adrian Smith
volume: '3'
issue: '1'
page: '59'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 61–63 (printed 59–61; Tony Cooper’s paper, art10002590, follows on p.62); Claude, 2026-10-05'
review: draft
queries:
- "Adrian Smith’s introductory notes (p.59), then his notes on four talks at the January meeting (pp.60–61). Each talk is printed as a centred heading with the speaker in italics; transcribed as H3 sections."
---

## Introductory Notes

by Adrian Smith
{ .byline }

1986 got off to a cracking start with two very well supported meetings at the Royal Overseas League. On 17th Jan we had a batch of papers on APL and OR, and on 21st March a set of talks on APL system design.

Much of the detail from the talks will be available in full as VECTOR articles (Tony Cooper’s is included after these notes – many thanks) so I shall be very brief in giving little more than an outline of the papers.

Many thanks to Nic Cook for taking very thorough notes at the March meeting (and my apologies for not using more of them!).

## APL and Operational Research, January 17th 1986

### A Computing Environment for OR

*Tony Cooper (British Airways)*

Tony is a member of a small group in BA who support OR (and others) on APL\*PLUS (mainframe), DEC-10 and so on. His talk covered the themes of:

- what aspects of computing are helpful to OR.
- how well does BA measure up?

He concluded with the interesting quote:

> “All the really undisciplined people have congregated in the groups that do APL.”

I wonder why . . . see Romilly Cocking’s paper from the March meeting.

### Optimum Pallet Loading

*Eileen Dyson (Rowntree Mackintosh)*

The evolution of a pallet-loading model at Rowntree Mackintosh fell into three phases:

- 1976 (or thereabouts) saw the design of a ‘best-fit’ algorithm which was implemented in batch PL/1. The output from this was a ‘layout chart’ giving a complete packing schema for a particular pallet size.
- 1983 saw an APL front-end, which used GDDM graphics to select and display the choice of layouts for any given box size. Using this the product development department could (for example) superimpose two candidate patterns to check interlocking and hence stability.
- 1985, and the APL package moved down to APL\*PLUS/PC for distribution to several factory sites. The graphics lacks the flair of GDDM, but is entirely adequate in day to day use.

Eileen brought along a disk of the model, which attracted an interested gaggle of people when run on a nearby Compaq.

### Linear Programming and APL: Pains and Pleasures

*Phil Chastney*

APL effectively grew out of linear algebra; ergo it ought to be ideal for tasks like LP! Unfortunately LP is intrinsically procedural and highly iterative; FORTRAN programs may run for 8 hours . . . what can APL hope to offer?

It is a nice environment in which to *use* LP, and it does have all the right primitives. In fact the whole basis of LP is two inner products, a division, and an outer product. The problems lie in the implementation of the typical matrix operations when the data is very sparse (1 – 10%). This leaves a niche for APL in relatively small problems, where the answer is wanted interactively, and where the user is willing to pay for the privilege.

### Pouring Water on Troubled Oils

*Dominic Murphy (ex Texaco)*

This was a typical Dominic half-hour! Ostensibly it covered the ‘human element’ in the design and implementation of a refinery simulation. As he put it, the motivation went something like this:

> UK to USA: We need some more tanks  
> USA to UK: No you don’t  
> UK to USA: Oh yes we do  
> USA to UK: Oh no you don’t . . . we’ve done a simulation!!  
> UK to OR : We need a simulation – and make it snappy!

The whole thing ended up as a vast board game; it cost some phenomenal amount of money to run on IPSA, as everyone collected their printouts and flung them off to the States.

Unfortunately, after all this effort, all they proved was that they really didn’t need the tanks after all. Oh dear, they never spoke to OR again!
