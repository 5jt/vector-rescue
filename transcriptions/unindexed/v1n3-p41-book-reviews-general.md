---
title: Book Reviews - General
authors:
- Robert Bittlestone
volume: '1'
issue: '3'
page: '41'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 43–46 (printed 41–44); Claude, 2026-10-12'
review: draft
tags:
- reviews
- expert systems and AI
queries:
- "Five books in four reviews, all by Robert Bittlestone: Chris Naylor’s “Build your own Expert Systems” (beginning in the lower half of printed 41, after the end of the Legrand review, unindexed/v1n3-p39-book-review-legrand.md), Alty and Coombs’s “Expert Systems: Concepts and Examples”, O’Shea and Eisenstadt’s “Artificial Intelligence: Tools, Techniques and Applications”, and three books on the IBM PC. The section heading “BOOK REVIEWS Compiled by Robert Bittlestone” and its introduction, on printed 39, are kept with the Legrand review. The lower half of printed 44 is blank."
- "The R1/XCON rules are set as indented text in print; kept as indented blocks."
- "Kept as printed: “at at least the conceptual level”; “How to get a Ph.D in AI”; “Osborne(McGraw Hill)”; the AI anthology’s byline “by Robert Bittlestone” where the others read “Reviewed by”."
---

## Build your own Expert Systems

**by Chris Naylor<br>
Sigma Technical Press (1983)**

*Reviewed by Robert Bittlestone*
{ .byline }

The volume of literature on expert systems is mushrooming at present, but most of the publications tend to have titles like “Fuzzy dynamic programming under conditions of non-trivial heteroscedasticity; a critical reappraisal” with authors such as Baas & Kwakernaak. It is consequently a matter for some encouragement that with this book we are faced with the high probability of being able to pronounce not only the title but also the author’s name correctly.

Naylor is a well-known populist in the computer world and a frequent contributor to the technical press. The book is subtitled “Artificial intelligence for the aspiring microcomputer - with listings for Apple II and Sinclair Spectrum”, so we know where we are before opening the cover. The contents themselves consist mainly of a comprehensively worked example of an expert system written in BASIC, which delves into necessarily labyrinthine complexity in its attempts to handle topics such as recursion and local variables, thereby unwittingly becoming perhaps the best indirect advertisement for APL one has ever seen.

Naylor does most things very well indeed; in particular his descriptions of MYCIN, PUFF, DENDRAL, and PROSPECTOR in Chapter 9 are obviously researched from the original material rather than hastily regurgitated from someone else’s article. His examples all seem to work, at at least the conceptual level. If you share a background in APL the task of entering all this code in BASIC is however superhuman, particularly if your only recollection of APPLE BASIC is knowledge of the vital “3 DOG” operating system restore kluge, which was to the best of my belief first discovered by David Eastwood in 1979.

Inevitably this leaves one or two things done badly. The first problem for many readers is going to be Naylor’s chummy style of prose. I am mindful of exhibiting most of his own worst habits in this very review, but in my defence I would argue that a book review is brief and it is the reviewer’s task to keep his audience awake. Naylor seems to feel it necessary to present himself as a cross between an agony column and a computerised weather forecast. Perhaps, however, this is psychologically desirable if you program in BASIC over any length of time. The second problem is that all this mateyness dispels the possibility of a sense of awe at some of the more impressive accomplishments in this field. This, I think, is a pity, particularly bearing in mind the average age of the target population. But it’s easy to criticise and harder to contribute; all in all a rattling good yarn and highly recommended to the younger reader.

## Expert Systems: Concepts and Examples

**by Alty and Coombs<br>
NCC Publications (1984)**

*Reviewed by Robert Bittlestone*
{ .byline }

Don’t buy this book unless you are seriously interested in finding out about expert systems, and fairly seriously interested in creating one for yourself. However, such aspirations are a sufficient as well as necessary reason for purchase; here in one modest title is really everything you need to launch yourself into this popular new activity. Part I is a fast brush-up on concepts and techniques. This time we manage to avoid BASIC in favour of LISP, ((although whether) (this is) (an unqualified advantage) (remains to be seen) (.))

Part II is a really thorough tour through MYCIN, PROSPECTOR, INTERNIST, DENDRAL, R1 and MOLGEN. If some of these names are starting to sound familiar, it’s because there are in fact only about a dozen expert systems of sufficient grandeur that everyone wants to write about anyway, so the same old names keep coming up. This makes it correspondingly easy for the neophyte to namedrop. The one I like best is R1, which DEC now call XCON. This is an expert system which allows salespersons and others of vanishingly low intelligence to order DEC VAX computers. For example:

```
      IF:  The most current active context is assigning a power supply
           And an SBI module of any type has been put in a cabinet
           And the position it occupies in the cabinet (its Nexus) is known
           And there is space available for a power supply for that Nexus
           And there is an available power supply
    THEN:  Put the power supply in the cabinet in the available space
```

One feels an overwhelming compulsion to add to the knowledge base the rule:

```
    ELSE:  The bloody thing won't work.
```

Rather more relevant, surely, is the metarule:

```
      IF:  The VAX machine is this complicated
           And your salesmen are too dumb to order it properly
           And you have a whole lot of spare research cash for some reason
    THEN:  Spend the cash simplifying the machine or hiring new salesmen.
```

However, none of this is the fault of Alty or Coombs and the book remains a bargain for the aficionado.

## Artificial Intelligence: Tools, Techniques and Applications

**ARTIFICIAL INTELLIGENCE: Tools, Techniques and Applications; O’Shea & Eisenstadt, Harper & Row 1984.<br>
Available from Harper & Row, Tavistock Street, London WC2.**

*by Robert Bittlestone*
{ .byline }

This is a collection of fifteen papers by well known innovators in the AI field. When reviewing an anthology one may criticise either the authors for infelicities in their papers, or the editors for lack of balance in their selection, or indeed both. Equally one may instead praise all concerned, my own approach in these particular circumstances. This is an invaluable source of otherwise hard to locate contributions.

Under “Tools” we get the by now mandatory introduction to LISP and PROLOG, with an interesting variant on POPLOG from the Sussex University team. If this shows that a new language can be presented as acceptable for expert systems, what about APL? In the Techniques section the emphasis is on robotics, with an amusing addition called “How to get a Ph.D in AI”. Finally, the Applications heading includes various case studies, some of them unpublished elsewhere as far as I know, ending with the inevitable walk through MYCIN.

## Three books about the IBM PC

**IBM PC Expansion & Software Guide; QUE Corporation.<br>
IBM PC & XT Assembly Language: A Guide for Programmers; Scanlon, Prentice-Hall 1983.<br>
Graphics Primer for the IBM PC; Waite & Morgan, Osborne(McGraw Hill).**

*Reviewed by Robert Bittlestone*
{ .byline }

Here are three books about the IBM Personal Computer, all available from Computer Bookshops Ltd., Lincoln Road, Olton, B27 6PA, who kindly offered them for review.

The Expansion and Software Guide is perhaps the most invaluable and complete work of its kind. The publishers are to be congratulated for compiling a detailed encyclopaedia of who makes what hardware and software for the IBM PC. Evidently — perhaps somewhat shamefully — almost all of the entries concern US companies, and it would be useful to have a UK appendix in which the details of local distributors were listed. However, there’s no minimum charge for international direct dial to America and if you can cope with the 8-hour time lag (most of the suppliers are in California) a brief call secures such information. Recommended for any serious user of the IBM PC.

Many books have now appeared about IBM PC assembler programming and I am certainly not qualified to make a comparative review. For me, assembler is just like a car engine. The theory always sounds very simple, but when you open the bonnet it takes half an hour to distinguish the starter from the generator. After an hour of reading about registers I usually feel sufficiently daring to consider transferring the contents of register A to register B, but inverting a matrix sounds a bit harder. However, Scanlon’s book is probably as sympathetic as it is possible to be for a dolt of my lack of calibre and I recommend it to all like-befuddled would-be machine codists.

The book on graphics I enjoyed, partly because graphics are easier to picture than indirectly addressed overhead camshaft hex offsets, and partly because the examples assume programming in BASIC, which even I can understand. IBM’s own manuals on their Colour Graphics Adaptor are hardly a masterpiece of clarity and this volume is much more sympathetic. If you read through it you will certainly understand the bewildering number of different modes in which the colour card works. However, despite the clever things that can be done with the hardware, I suspect you’ll also end up agreeing how imaginative IBM have been in restricting the user to 320 by 200 pixels for normal colour display. This imposes a limit on resolution which is unacceptable for most serious business purposes. However, this is hardly the fault of the book, which copes manfully with the constraints of its subject.
