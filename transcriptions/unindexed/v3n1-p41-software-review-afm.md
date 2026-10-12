---
title: 'Software Review: AFM'
authors:
- Adrian Smith
volume: '3'
issue: '1'
page: '41'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 43–45 (printed 41–43); Claude, 2026-10-12'
review: draft
tags:
- reviews
- data and files
queries:
- "Contents line “Software Review (AFM)”; the printed heading is “Software Review : AFM”."
- "Kept as printed: “a fair amount of work from out technical support group”; “otherwise its DOMAIN ERROR time!”."
---

*by Adrian Smith*
{ .byline }

## Introduction

AFM is a file management package which runs as an Auxiliary Processor with either VS APL or APL2. It provides IBM’s APL with component files along the lines of the APL\*PLUS shared file system; simple cover functions double for `⎕FTIE`, `⎕FREAD` and so on.

AFM files can be accessed concurrently by online APL systems and from conventional batch programs (typically written in PL/1 or COBOL). File and record-level locking is provided, with security handled through access matrices in the normal way.

A wide range of ‘housekeeping’ and ‘administrator’ functions are provided, some via an ‘OPFNS’ workspace and some as batch utilities.

The cost of AFM is around $15,000 depending on the particular options chosen. It is marketed by Interprocess Systems Inc in the USA, Cocking and Drury being the UK agents.

## Background to Use at RM

AFM was brought in to Rowntrees about a year ago. The motivation for doing this was threefold:

1. We needed to redesign an antique VSPC (ex CMS) system which made heavy use of direct files. We could have set it all up with keyed VSAM files, but AFM promised a much quicker solution at a very reasonable cost.
2. We had already anticipated a VSPC to TSO conversion. A pre-emptive move to AFM looked like smoothing the path very considerably.
3. Experience from RM Canada (under VM/CMS) suggested that we could expect significant CPU savings over our standard file routines.

In addition it was becoming clear that we would soon be faced with implementing APL systems on a variety of PCs, all of which had some variant of the APL\*PLUS/PC file system. The idea of a compatible set of file utilities across all environments was obviously very attractive.

At RM the vast majority of APL filing is handled through two utilities called (with startling originality) DUMP and GET. DUMP simply takes a list of APL objects (a delimited vector or in `⎕NL` format) and bungs them all on a file. Typically there will be 50 – 80 objects, say 100K of data in all. GET reverses the process; either everything on the file, or selected variables, reappear in your workspace.

Under VSPC by far the best way of doing this turned out to be to format and ravel everything, and then to write it out (via the EBCDIC processor) in 4K chunks. The potential economies from cutting out all those ‘executes’ and ‘reshapes’ are obvious!

## Installation and Housekeeping

Getting AFM up and running was simply a matter of following the instructions! However getting it running fast required a fair amount of work from out technical support group; mainly a matter of getting the VSAM files defined right, getting catalogs in the right place and so on. The documentation was felt to be adequate, but could have been indexed better!

The utilities for file dump and restore, and the general overnight housekeeping jobs were well documented, and have caused us no problems. The OPFNS workspace is quite adequate, but can be improved out of all recognition by a bit of attention to the user-interface. Fortunately all the code is unlocked and commented, so simple patches like accepting lower-case responses (our administrator doesn’t have an APL keyboard!) are very easy to do.

There are some minor beartraps, for instance if you mistype the TSO id which you want associated with a particular AFM user, you can run a batch import for that user, but can never again get at the files! You have to wipe them from the system and try again; not serious but avoidable I would have thought.

## Using AFM from an APL Application

The first thing I must say is that the User Guide is absolutely first class. It is well organised and is readable as a tutorial as well as being a very adequate reference manual. Experienced APLers have been able to pick up the basics, and to write quite sophisticated systems, with no guidance other than a copy of the manual. I suppose all this proves is that component files are a natural extension of APL, and that it is absurd that they have never been made a native part of the IBM offerings.

My only gripes concern the very peculiar way the AFM cover functions attempt to reproduce APL\*PLUS error handling. Functions such as FTIE are result-less, and leave various obscurely named globals lying around for inspection (if you’ve previously set up an equally obscure global to define the range of errors you want to detect . . . otherwise its DOMAIN ERROR time!). I’m afraid I rewrote most of them to return explicit results, again an easy task as the source code is very straightforward. Of course you have problems with things like FREAD; this sends back an empty vector if it fails, and you then have to go looking for that pesky global again. I could almost see a case for nested arrays!

## Performance

It proved easy enough to get our DUMP and GET routines to work with AFM, but quite a task to make them as fast as they were before. The simple-minded approach of writing one object per component is hopelessly slow (in elapsed terms) when you have lots of little variables. It also leaves you wondering what to do with the odd whopper; you have to set your maximum record size somewhere, and wherever you set it (16K, 32K, 64K, . . .) sooner or later someone will bust it.

We eventually settled on a compromise of partitioning the file into character, integer and real and ravelling variables of each class together before guillotining at 16K. This still leaves us with the reshape, but does away with the execute on numerics. AFM now gives us about 30% better CPU cost (including time spent by the AP outside APL) and marginally slower elapsed times than we had before. We feel this is acceptable, if not quite up to our initial expectations.

I am more worried about that archaic ex-CMS system I mentioned at the start. Here the files have between 5,000 and 10,000 components, mostly quite small. Typically the application will tie half a dozen of these on signon, reading the odd record off each; this takes a minimum of 6 seconds elapsed, which is barely acceptable. We are too far down the road to start compromising on the design, but with hindsight I wonder if the decision to treat AFM as if it were ‘native’ might have been a mistake.

## Summary

AFM gives plain old VS APL what it should have had all along; a usable file system. It is well supported with housekeeping utilities and in general the documentation is good. We have yet to find any bugs, and we had good ‘hotline’ support from the States when we confused ourselves during the TSO conversion. Performance is very adequate as long as you minimize interaction with the AP; feed it lots of trivial requests and response times are much less satisfactory. You can design round this, but you shouldn’t really need to! On balance a good product and cheap at the price.
