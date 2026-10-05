---
title: 'Case Study: DBASE-II at Bedford School'
authors:
- Adrian Smith
volume: '2'
issue: '1'
page: '84'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 86–91 (printed 84–89; an APL◊385 advert fills the foot of p.89; the technical section begins on p.91); Claude, 2026-10-05'
review: draft
queries:
- "Two headings: “CASE STUDY by Adrian Smith” (acknowledgements and author’s note, p.84, with a photograph of the school) and “DBASE-II at Bedford School by Adrian Smith” (p.85 on). Transcribed as one piece under the second title."
- "The photograph of Bedford School on p.84 is described, not reproduced."
- "dBASE-II listing, p.87: the not-equal operator (dBASE #) is printed £, and the three comparisons with 11 are printed with a glyph like ≹ (probably <, as printed by the same UK print wheel). Both transcribed as printed."
- "“the ″500 programming course” (p.86): the currency sign is printed as ″; presumably £500. Transcribed as printed."
- "“(VECTOR 1.4)” refers to Michael Carmichael’s paper in Vol.1 No.4."
- "Slips transcribed as printed: “I would like thank”, “to cope with”, “that that dreaded”."
---

by Adrian Smith
{ .byline }

## Acknowledgements

I would like thank Pat Wood and John Marchant for taking up so much of their valuable time to show me round, and also for being so willing to explain the history and background of the developments described.

## Author’s Note

Nowhere in this article will you find so much as a mention of APL. I have deliberately and firmly suppressed any personal tendency to think of the APL alternatives to the system described. I hope that when you first read the study you will try to do the same. Then maybe you could take a more critical perspective, and start thinking along the lines ‘I could have done that in half the time with APL\*PLUS and a couple of PCs’, or alternatively ‘I’m glad I wasn’t asked to do that in APL!’.

Looking back, it seems to me that the ‘package’ approach was dead right for the standard data entry and reporting, although you could argue that the package could perfectly well be written in APL! However poor DBASE-II was put through some dreadful hoops to produce things like age pyramids; in fact it was made to tackle all sorts of extremely APL-ish problems, and it made very heavy weather of them.

Surely the conclusion is obvious. By all means let us use DBASE-II (or Datamaster or Delta or whatever) for the things they do best. What we need for APL is a standard set of well-documented reliable ‘windows’ into all the arcane and incomprehensible file formats used by the ‘top-10’ packages. Michael Carmichael’s paper (VECTOR 1.4) is a good start; if anyone else is beavering away along the same path maybe they would like to add to the collection. There are plenty more VECTORS to come!!

*[Photograph: Bedford School, a large Victorian Gothic building with a spire, behind a lawn and a tree.]*

## Introduction

These notes are an attempt to give an overall impression of the way DBASE-II has been used at Bedford School to build up an impressive array of indexing and reporting systems around the basic school records. The detailed operation of the programs is obviously not of particular interest; rather the way the system has grown up, and the mistakes made and experience gained along the way.

## Background

Bedford School is one of the top public schools in the country; it has about 1100 boys in total (800 in the upper school, of whom 40% board). It is part of a larger grouping of public schools in Bedford, all administered under the umbrella of the Harpur Trust. Over the course of a year around 300 registrations are taken, and there are clearly some quite complex clerical systems to cope with the ‘school list’ and to estimate the number of potential entrants in any given year.

In common with most ‘big’ schools Bedford School’s maths department acquired a number of BBC micros to teach computing. These soon developed into a ‘computer club’ under the leadership of an extremely enthusiastic and able master; as you might expect it wasn’t long before this began to produce a whole range of ad hoc programs in BBC Basic to tackle the knottier bits of the existing clerical systems.

So useful did the programs become that one of the BBCs soon migrated down to the school office, and started to become an integral part of the whole administration system. Fortunately, enough of the danger signals were spotted in time, and rather than simply letting the ad hoc system grow out of control, the staff decided to step back and ask for expert advice.

## Why use a Database?

Lacking ‘experts’ of their own, the school sensibly looked elsewhere and retained a consultant to advise on the ‘best’ way of building a really professional system. The brief covered both hardware and software, and the immediate recommendations were:

- use Apricots
- use a database

This obviously implied a complete re-write of all those extremely useful Basic programs, and the return of that BBC to its rightful place in the maths department! Why throw away a perfectly workable system in favour of something unknown and untried? It might be interesting to compare the reasons given at the time with subsequent experience:

- reliability. There is no doubt that the BBC programs were ’breakable’. One could reasonably expect a proprietary package to be much more robust.
- compatibility. All the Harpur Trust schools would eventually need some form of computerization; if they were to share the same database management system they would find it much easier to share information.
- speed of development. Typically you would expect a range of useful macros for screen-editing and report generation. These are the sort of thing which take ages to program if you have to do them yourself.
- maintainability. Databases tend to come with a high level ‘structured’ language which should generate far more comprehensible code than even the best available Basic.
- wide range of ‘standard’ reports. Using Basic even the simplest ad hoc report needed a fair amount of programming.
- speed. One would expect a professionally developed software tool to run a good bit faster than a mish-mash of schoolboy code!

There was one clear drawback to the database road; the secretaries had already got well used to the BBC programs which had been carefully hand-crafted to match the existing manual systems. No-one really believed that any database, however flexible, would exactly reproduce the programs on the BBC. There was obviously going to be a compromise between the economics of programming and ‘acceptability’ to the user. Exactly where this compromise should lie turned out to be a critical factor in the final choice of database system.

## Which Database?

From a short-list of five, the choice narrowed down to two main contenders:

- FMS-80. Friendly, easy to use, helpful. This would do the ‘simple’ things quickly and easily, and had the great benefit that untrained staff could generate their own reports through the built-in menus.
- DBASE-II. The industry standard. Much more the professional programmer’s tool; flexible and powerful, but definitely command-orientated with only the bare minimum of on-line help.

The winner was FMS-80; in the consultant’s view the school system was so close to the classic ‘personnel records’ application that the ’so simple even the cat could use it’ approach was adequate. If you did need to go off into special-purpose programming, there was always the ’extended language’ facility (sort of Pascal-like) and the ″500 programming course to learn it. It was felt at the time that it would not be necessary to use this ‘extended language’ at all.

DBASE-II lost out on the grounds of being insufficiently ‘state of the art’ in terms of ease of use; in particular it was not thought to be sufficiently simple for untrained staff to use as a report-generator. This requirement had been heavily stressed in the consultant’s brief; in the light of subsequent developments it is interesting to note how this one over-riding factor had influenced the choice, as it happened in the wrong direction!

## Developing the Database System — Take 1

The School now had rather a stroke of luck; an ex-master had for some years run his own small computer outfit (accounting systems on PETs — that sort of thing). He had recently been ‘bought out’ by a larger firm, and was on the look-out for a change of job. After some heart-searching he agreed to act as systems analyst/programmer for the project. Of course he was less than convinced about the idea of database — he had after all been writing this sort of thing in machine code for the last 10 years.

As he started putting together the first file and screen layouts he quickly began to realise just how easy FMS-80 was making life; it really did make light work of things like simple screen editors and default reports! However as fast as he discovered the joys of database, he began to fall over the drawbacks! An alarming number of apparently straightforward jobs (those that the consultant had blithely assumed were ’standard’) turned out to have just enough quirky bits that that dreaded ‘extended language’ was needed after all! Unfortunately the resulting programs were significantly harder to write (and follow) than they would have been in Basic!

At this same time it became clear that there were really very few genuinely ‘ad hoc’ reports at all; half a dozen ‘selectable’ lists were quite adequate to cover virtually everyone’s requirements. The consultant’s choice of FMS-80 began to look less and less viable, and the School was faced with a hard decision. Should they persist with a choice which seemed in retrospect to be wrong; should they throw away a considerable investment in software and training and begin again from scratch with DBASE-II; or should they scrap the idea of database altogether and revert to Basic?

## Developing the Database System - Take 2

Of course this didn’t by any means go back to square 1. The hard bits (the file design, the report specifications) had already been done, and they carried over unchanged from the previous development. As will be clear from the examples, it is by no means straightforward to program even the simplest of screen-based editors in DBASE-II; on the other hand it is quite possible to add ‘one-off’ calculations, for example to cross-check ‘expected year of entry’ and ‘date of birth’.

```
IF global = 'S'
  STORE T TO notnext
  DO WHILE notnext
   @ 16,2 SAY ron+' Please make up to 3 entries for mode of selection, ';
     +'from the list above. '
   @ 17,2 SAY ' If you select fields 7,8 or 9 you may enter an inclusive ';
     +'range.        '+rof
   @ 18,2 SAY 'Please select your (up to) 3 fields now ' GET fld1 PICTURE '99'
   @ 18,50 GET fld2 PICTURE '99'
   @ 18,60 GET fld3 PICTURE '99'
   READ
   CLEAR GETS
   @ 16,1
   @ 17,1
   @ 18,1
   STORE VAL(fld1) TO v1
   STORE VAL(fld2) TO v2
   STORE VAL(fld3) TO v3
   IF v1≹11 .AND. v2 ≹11 .AND. v3≹11
     STORE F TO notnext
   ENDIF
  ENDDO notnext
  IF fld1 £ ' '
     STORE TRIM($(txts,(v1*9)-8,9)) TO tx1
     STORE TRIM($(flds,(v1*9)-8,9)) TO fn1
  ENDIF
  IF fld2 £ ' '
     STORE TRIM($(txts,(v2*9)-8,9)) TO tx2
     STORE TRIM($(flds,(v2*9)-8,9)) TO fn2
  ENDIF
  IF fld3 £ ' '
     STORE TRIM($(txts,(v3*9)-8,9)) TO tx3
     STORE TRIM($(flds,(v3*9)-8,9)) TO fn3
  ENDIF
  IF fld1 = ' ' .AND. fld2 = ' ' .AND. fld3 = ' '
     STORE 'G' TO global
  ENDIF
ENDIF global
```

Much the same applies to the reports, although a surprising number of ‘internal’ lists could be generated directly by DBASE-II. In fact as the system ‘bedded in’ the users began to realise that

```
FOR ENTRY=85
LIST REGNO,NAME,BIRTHDATE,FORM
```

…wasn’t so hard after all, and was a good deal quicker than getting the same thing through the menus! So much for user-friendliness!!

As the development approached completion, it became increasingly obvious that DBASE-II really was giving considerable benefits over a ’do it yourself’ approach. Oddly enough, the one unfulfilled expectation was for increased speed; many of the more complex tasks ran faster on the dear old BBC! This apart, the new systems measured up very well against that initial list of requirements:

- reliability. Surprisingly enough, even an old established package like DBASE-II has the odd bug! The indexing has the occasional inexplicable happening, and the supplied program editor (in practice you would probably use Wordstar anyway) sometimes crashes. However it is certainly beyond doubt that it would not be humanly possible to write such a sophisticated file system in Basic, and get it anything like as clean, within a year.
- speed of development. Most of the complex reports (e.g. an ’age pyramid’ for the entire School) were effectively hand-crafted. The DBASE-II language proved itself very capable of the task, but saved little or no time over the same thing done in Basic. On the other hand the ’update and validate’ routines and the simpler reports could take full advantage of the available macros, and probably took less than a tenth the time of a Basic equivalent.
- maintainability. This is an area where the real benefits have yet to appear. Of course there have already been several significant changes to the file structures, and the ability to re-load an existing database into a new structure (with fields extended or truncated as required) has been a major boon. Also, everyone agrees that the DBASE-II code is far easier to follow than any Basic equivalent.
- standard reports. As it turns out, many of these are simple ’subset’ lists sorted in particular ways. DBASE-II can do this kind of thing with its eyes closed, and very quickly too. The non-standard ones are so non-standard that they virtually have to be programmed ’from the ground up’ anyway; at least DBASE-II doesn’t get in the way!
- speed. Once everything is set up correctly (of course you learn the wheezes as you go along) record selection and updating is extremely fast. There is a price to pay; a complete re-index of all 800 boys takes around half an hour to run. Fortunately this is a very rare occurrence! For the hand-crafted programs the situation is very different; because DBASE-II is an interpreter, and requires significantly more code than Basic to achieve the same job, it runs rather slower. Typically the old BBC programs beat the Apricot for speed on most of these ’special cases’.

In general there is no doubt that the ‘Take 2’ development has been extremely successful. In fact many fewer compromises have been made than were expected! It is interesting to note that many of the most important ‘plus’ points of DBASE-II:

- the powerful ‘general-purpose’ programming language
- the almost complete freedom from bugs
- the huge ‘user-base’, and hence the ready source of advice, literature, hints and tips, etc.

…were hardly considered in the original report. By contrast the main ‘plus’ points of FMS-80:

- the helpful front-end
- the ‘menu-generated’ reports

…were the basis of the original ‘brief’ on which it was chosen, and turned out pretty well irrelevant when the final system emerged!

## Summary

Yes, database really does pay dividends; yes it really does pay to get the right database. No, you can’t expect to get it right first time. Even if you take the sensible precaution of retaining an independent expert, he will probably ask all the wrong questions!

The Bedford School experience is particularly valuable, in that they got it wrong; recognised the fact; and had the courage to go back and start again. As a result they have developed a remarkably professional system extremely quickly. DBASE-II has been around a long time; for cheap and cheerful systems which need a modicum of hand-crafting it still looks head and shoulders above the competition.
