---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '13'
issue: '4'
page: '17'
unindexed: true
transcribed: 'from page images of VOL.13-NO.4-APRIL-1997.pdf, pages 19–22 (printed 17–20); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”."
- "Kept as printed: “MicroAPL Ltd. South Bank Technopark, 90 London Road, London, London SE1 6LN, UK” (“London” twice); “fürerbunker”; “Also scheduled for release after the summer are a Web Server, which will allow …”; “several hours work”."
---

*Compiled by Gill Smith*
{ .byline }

## MicroAPL

MicroAPL has released a major upgrade to APL.68000/X for the IBM RS/6000 and compatible systems under AIX 4.1. The new interpreter has been re-engineered to take full advantage of the PowerPC architecture of the latest RS/6000 systems, and users have reported some spectacular speed improvements across the whole range of APL operations. Versions are available for Motif as well as for traditional 'dumb terminal' operation.

Meanwhile, and contrary to what you might expect from the series of gloomy press reports about Apple Computer, our APL products for MacOS continue to sell well. We are considering what opportunities for APL might arise out of the new Rhapsody operating system which Apple have announced, and we shall be visiting California in May to find out more.

Finally, following an internal re-organization and the merging of some of our non-APL activities with another company, some familiar faces are now less often seen in the MicroAPL offices. In particular, David Eastwood, who co-founded MicroAPL in 1979 and who has made a sustained and varied contribution to MicroAPL's activities over more than fifteen years, is no longer involved on a day-to-day basis in the company. Happily, he remains a non-executive director and so we still have the benefit of his input.

> MicroAPL Ltd. South Bank Technopark, 90 London Road, London, London SE1 6LN, UK
>
> WWW: http://www.microapl.co.uk PHONE: +44 171 922 8866<br>
> E-Mail: MicroAPL@microapl.demon.co.uk FAX: +44 171 928 1006

## Insight Systems / Adaytum Software

### New Offices

After six years at Nordre Strandvej 119A, there was no further room for expansion. On March 1st, Insight Systems moved into a building of our own. Instead of being spread out down a long hall in separate units in an "office hotel", we can now all see each other (and the view of Øresund) through glass walls. Only Gitte has a proper "fürerbunker" where she and Helene can hide from the rest of us. We did not move far, we are in the same complex, our address is now number 119C. Fortunately, we did not have to change telephone numbers yet again — we are still at +45 49 76 20 20 (FAX +45 49 76 20 30).

### Adaytum Planning Product News

We have rolled out the 32-bit version of Adaytum planning (using Dyalog APL version 8.0.11 and Borland C version 5), and can report that the 32-bit environment is an improvement in every way. The system is faster, more reliable, and handles larger models than before. This is such a novel experience of a conversion to new base software that it deserves mention!

The focus of our product development efforts is now providing support for new front ends to Adaytum Planning, in particular Microsoft Excel and other environments which support OLE Automation. We are producing an OLE Automation Server for Adaytum Planning, which will make it possible for virtually any Windows developer to drive Adaytum Planning from within other applications.

Also scheduled for release after the summer are a Web Server, which will allow access to Adaytum Planning over the Inter/Intranet from web browsers and other web-enabled applications.

If you would like to know more about Adaytum Planning, visit our web site www.adaytum.com, and come to our annual European User Meeting, which will be held in Birmingham (UK) on April 23rd & 24th. The web site contains registration instructions.

### Products: APL Technology Group

The focus of technology development this quarter is our OLE Automation Server, which makes it possible to make function calls to APL interpreters. This product is much less sophisticated than the OLE Server support provided by Dyadic, but has some important advantages. Our OLE Server acts as a client of our APL Pipes product, which means that it can act as a front end for all the APL systems which are supported by APL Pipes: Dyalog APL, APL\*PLUS, SHARP APL and APL2 under any of Windows 3.1, Windows 95, Windows NT or Unix. We believe that it will still be some time before network OLE will support Unix in a way which will satisfy our typical customer organisations. We expect to have the OLE Automation Server available for beta testing in May. Write to info@insight.dk for more information.

## HMW Trading Systems Ltd.

As we stated in the October 1996 issue of Vector, we are attempting to broaden our product range by extracting a number of modules from 4XTRA. This issue of Vector contains an article describing Change Control, the software portion of the Configuration Management environment that we have developed. We aim to have a stand-alone Dyalog APL/W version available during the second quarter of this year. This will include the Object Manager CASE tools that we use for development. We are also looking to publish an article in Vector about the modular prototyping methodology that we use with Change Control.

The next item on the agenda is to extract and package the multi-processor sequence scheduler. In simple terms, this is an APL module that is capable of running self-contained APL tasks on separate PCs that are on the same network. It takes into account the machine resources as well as any task interdependencies. Tasks are designed to fit within a standard framework that is capable of producing transaction logs containing as much or as little detail as required. An associated module allows remote monitoring of the tasks.

## Dyadic Systems Limited

Dyadic is pleased to report that the production releases of Dyalog APL/W Version 7.3 and 8.1 are now available. The product is now distributed on CD, although diskette versions may be obtained on request. Dyadic extends its thanks to all those who took part in the Beta Test program.

The new versions were a month or so later than planned as a result of a rather late decision to include *syntax colouring* for the function editor. This feature, popularised by our competitors, has been extended to allow you to set up a range of different colour schemes and be able to switch quickly between them. For example, in addition to your regular multi-purpose colour scheme, you could have a scheme designed only to highlight global references and another designed specifically to make labels stand out. Dyalog APL's enhanced syntax colouring also identifies unbalanced control structures and unbalanced braces in dynamic functions.

Another minor but useful last-minute improvement is the support for wild-card searches in the Find/Replace dialog boxes.

Having completed Version 8.1 for Windows, effort is being directed towards porting this code to UNIX platforms. The production release of Dyalog APL/M will therefore be Version 8.1 compatible.

Further details concerning Version 8.1 and other implementations of Dyalog APL are available at the new-look Dyalog APL web site www.dyadic.com.

## Causeway Graphical Systems Ltd

One of the great joys of being a software company is in seeing your work exploited and extended in ways you could never have devised yourself. *NewLeaf* has the rather (as we thought) esoteric capability of including any completed page as a scaled image into another page. Partly we put this in to be consistent with PostScript, which has a completely scale-independent language model, but mostly we put it in because recursion is fun. Jan Karman (who knows a thing or two about bookbinding) immediately spotted the possibility of saving several hours work on the photocopier by printing booklets (facing pages, double-sided) directly on his duplex laser. We fixed a couple of bugs in `leaf.Fetch` and now NewLeaf is shipped with a simple `Booklet` capability which anyone can use to save paper and time.

The "engine" of *CausewayPro* is now looking very solid, completely namespace aware and completely relocatable (you can call it whatever you like, and hide its namespace anywhere). It runs the existing class table roughly twice as fast as shareware Causeway, so you will be able to migrate existing applications along with any classes which you have written for them. New developments can be based around a completely new class library (accessible entirely through the Dyalog WS Explorer) which makes it remarkably easy to modify existing classes and add new controls of your own.

*CausewayPro* also extends the Causeway paradigm with **multiple active properties**. Currently, a Causeway object has a single 'data' property which is linked to an APL variable or expression; the property is refreshed whenever any of a list of 'watched' variables changes. Now you can have as many of these 'active properties' as you like, each with its own list of dependencies. For example a *Form* might have 'Position' and 'Size' both set by APL expressions such as `∆pos+10 10` and updated on a change to `∆pos` or `∆size`. If you make several such forms (and change the expression to give them all slightly different calculations) they will follow each other about in a very amusing way.

Useless? Well so was the ability to include a page within a page within a page ... until someone found a use for it!
