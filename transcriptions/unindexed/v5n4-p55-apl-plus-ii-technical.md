---
title: 'APL*PLUS II: STSC’s Second Generation APL System for 80386 Machines'
authors:
- Peter Cyriax
volume: '5'
issue: '4'
page: '55'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, pages 57–62 (printed 55–60); Claude, 2026-10-12'
review: draft
tags:
- implementations
- reviews
queries:
- "Contents line “APL*Plus II (technical)”; the printed heading is “APL*PLUS II / STSC's Second Generation APL System for 80386 Machines”, byline “reviewed by Peter Cyriax”. The review ends a third of the way down printed 60; the rest of that page is a MicroAPL advertisement (“MicroAPL for ... APL on the widest range of micros”), not transcribed."
- "The printed subheadings (APL*PLUS II System, APL Interpreter, APL File System, APL PC Environment, Summary) are set in plain type; transcribed as ## headings."
- "Kept as printed: “Workspace” and other capitalised nouns; “preceeded”; “the edit sessions survives )LOAD”; “what you picture looks like”; “recently reared their heads”; “mainframe APL XEDIT”. A stray mark after “panels” (“panels̃ or”) and a stray apostrophe-like mark before “Overall” are dropped."
---

*reviewed by Peter Cyriax*
{ .byline }

Early last Autumn STSC released APL\*PLUS II, a new generation of APL running on ‘386’ type IBM PCs. It offers mainframe power on your desk for a total of four or five thousand pounds; so whether you need to grade up from older PCs, or want to decentralise mainframe based systems, this is something you should know about.

In a nutshell, APL\*PLUS II combines the environment of the APL\*PLUS/PC with the APL language from the APL\*PLUS/1000 mainframe systems. If you have never used either product, that leaves you none the wiser, but at least you have a treat in store.

There are several other versions of APL that will run on 386 machines - Dyalog, Sax and APL2, which I have heard good things about; but this is not a comparative review, it's an attempt to tell you about APL\*PLUS II, and relate it to the products it was developed from.

First, what does it run on, and what do you get?

APL\*PLUS II runs on an IBM PC or compatible under DOS 3.3 or later; and requires a 386 CPU with at least 2MB of memory. That gives you an APL that seems to run 4 or 5 times faster than APL\*PLUS/PC on the same hardware, with a Workspace size of around 800K. For the moment, at least, it's a single user system, though it will run on a network.

If you want a bigger workspace you buy more memory (up to 16MB). There are many flavours of 386 PC - but a good 20Mhz machine with 3 or 4MB of memory is now commonplace, and costs a few thousand pounds. That makes an interesting comparison with a typical mainframe - it will put an APL system on your desk with a 2 to 3MB Workspace, and processing speed somewhat better than the old IBM 3031. The wire from the screen to the CPU is rather shorter on the PC, of course, so the PC is much more responsive - a couple of seconds faster than the mainframe running under light load.

However, most PCs don't have a floating point processor, so engineering, statistics, CAD-CAM or graphics applications can be very slow. If you have a lot of heavy calculations to get through, then a floating point processor should speed them up by as much as ten times, and the WIETEK chip is several times faster again - a real transformation, but still a couple of times slower than a mainframe with otherwise similar performance. You certainly can offload these sorts of applications from the mainframe to a 386 PC, but you have to think about it.

Floating point is not an issue for most people, so what it all comes down to is this:

> A modern, single-user APL with mainframe size workspaces running at about one tenth the speed of the fastest CPU that IBM sell.

## APL\*PLUS II System

The main components of APL\*PLUS II are:

1. APL Nested Array Interpreter
2. APL Component Shared File System
3. The Editor, and Access to the rest of the Environment which I will discuss in turn.

As it happens, I still have a Beta test version of APL\*PLUS II, not the production version, but so far as I know there isn't a great deal of difference. I have been using the system for development, not trying to crash it; and the main reason I haven't upgraded yet is that I haven't found any bugs. APL\*PLUS II seems reliable.

## APL Interpreter

APL\*PLUS II is a second generation APL supporting Generalized (Mixed and Nested) Arrays with the extra functions and operators needed to handle them. It also has the earlier developments, such as Grade on Characters and on Matrices, plus the extension of Compress to Replicate, of course.

There has been a lot of criticism of Nested Arrays - mainly that they produce incomprehensible, highly inefficient code. This criticism was also made of first generation APL - and with just as much validity. Like any powerful tool, Nested Arrays can be abused; and abused they certainly were, particularly when we were trying to learn how to use them to begin with. My own first attempts are no exception, but even so I find no real difficulty in reading code I wrote five years ago; whereas in some cases traditional APL would have needed a nightmare of globals, making it quite impossible to maintain. The single most important use for Nested Arrays is to pass multiple parameters into Functions, which helps to make them modular and clarifies their interface - hard to argue with.

Neither is efficiency an issue. This is particularly true of APL\*PLUS II, which, in common with other modern APLs, was designed from the ground up to support Nested Arrays. The Monitor (`⎕MF`) facility is quite up to the task of finding out where CPU is going, and it shows that Nested Arrays can lead to simpler and faster code when they represent well how your data is actually organised. I would not be without them.

In language compatibility terms, APL\*PLUS II is almost identical to the APL\*PLUS/1000 mainframe system, which is a (major) development of VS/APL. The only differences I have found are that Replicate Foreach (`/¨`) does not work because of the conflict between Replicate (Compress) and Reduction - `IVERSON ERROR`; and also `⎕SIZE` gives the answer you always wanted anyway i.e. how big the object actually is. Dyalog APL is also very similar - it was modeled on STSC's experimental system that preceeded APL\*PLUS/1000; and IBM's APL2, though different, shares the same basic definition of Arrays plus many of the extensions. Finally APL\*PLUS/PC is a small, non-nested version of APL\*PLUS/1000; so altogether APL\*PLUS II is generally upward compatible with, or at least similar to most other major APL systems.

The implementation of APL\*PLUS II is also impressive, with only one obvious weakness - Index and Replicate are both very slow. Index has always been a problem, because in general it is quite difficult to spot the cases that can be optimised; but Replicate is surprising, though it may have been improved by now. This is a minor quibble for such a new product: overall the Interpreter seems fast - it runs in true 386 chip 32 Bit mode; and like the mainframe product it uses 1 Bit Booleans (faster, and saves a lot of space), 32 Bit Integers (no more floating-point dates and array indices), and 64 Bit Floating-point Numbers. Also, it passes APL values around with internal pointers as much as possible, rather than copying them, so it doesn't waste CPU or use up Workspace.

## APL File System

APL\*PLUS II supports the Component Shared File System originally developed by Sharp and STSC in the early 70s, and still going strong.

APL\*PLUS/1000 and APL\*PLUS/PC also have this same Component File System, implemented using the `⎕F`… family of System Functions.

An APL Component File is essentially a sequence of Components, each of which is an APL value of whatever shape, rank, depth, type and size you can dream up (or fit into your workspace). It is simple, but it fits APL well, which is why it is so successful.

The mainframe version of the File System is a shared system, which means that different people can use it simultaneously; even updating the same file at the same time in a controlled way. At first sight this feature appears irrelevant on a single user PC system; but it is implemented on both APL\*PLUS/PC and APL\*PLUS II. This means that both products can be used to share data on a network of PCs, and in due course APL\*PLUS II should also work on a multi-user 386 system running under either CDOS or OS/2.

The performance of any File System depends predominantly on disk hardware and buffering, but the APL\*PLUS II version is noticeably faster than APL\*PLUS/PC. Also it suffers far less from the fragmentation which can occur when Components keep changing their size, particularly if they are large.

## APL PC Environment

This I love, and hate. The good news is there is nothing you cannot do, and probably with only one keystroke: the bad news is that, like me, you may find it quite impossible to remember what that keystroke is. To be fair, this problem seems to be endemic to all PC systems, not just PC APL. One of the features that makes APL attractive is the way it fits together to form a coherent whole - it seems a shame to spoil it with a myriad of un-coordinated facilities, however useful each one might be on its own. This is a very personal view, but I do feel that too much use has been made of the freedom that the PC provides. However these facilities are indeed useful, and I must admit that APL\*PLUS II is a more productive development environment than either APL\*PLUS/PC or any mainframe system.

The principal facilities of the APL PC Environment are:

1. APL Character Set Support
2. Session Manager
3. The Editor
4. Access to DOS Native Files
5. Screen Control
6. Graphics
7. Communication with other Systems

Support for the APL Character Set is available for almost any screen configuration and a large selection of printers, without any hardware changes, using software defined Character Sets. The old, low resolution mono screens needed a special Character Set ROM, and that is still available, but I cannot see anybody putting a screen like that on a 386 machine. I tested APL\*PLUS II on a number of systems before buying one, and they all worked fine. Over the last few years screens and printers have become steadily more flexible, as well as better and cheaper; so Character Set problems should be a thing of the past.

The Session Manager is similar to IBM's Session Manager for VS/APL: it allows you to scroll back over your session log, and to change and re-execute statements; but it also contains other facilities e.g. string search, printer control, cut and paste, change character sets, undo changes and deletions, talk to the mainframe… obtain help on all of these facilities etc., etc.

The Editor is a development of the `)EDIT` full-screen editor available on earlier versions of APL\*PLUS/PC. It is not that different to use, but much more powerful, and has been made available in Release 8 of APL\*PLUS/PC as well. You can stack up edit sessions just as you can with mainframe APL `XEDIT`. The Session Manager itself is integrated into the Edit Stack - the system thinks you are editing the session log - which explains why some of the more ‘advanced’ features are there at all, but it all works cleanly, and it means that you can easily move code between functions or between a function and the session log, or even between workspaces as the edit sessions survives `)LOAD` - surprising, but very handy. I also like the facility to break lines and glue them back together again. This Editor is also much better suited to text data than `XEDIT` is - almost as good as a word processor. Overall I like it, though one final facility does seem to be missing - it would be most useful to split the screen and have two sessions available simultaneously, particularly during de-bugging.

Access to DOS native files is via the `⎕NF`… (Native Files) family of System Functions. I haven't used them much, but when I tried they did what I expected and ran quite quickly.

Screen Control centres around `⎕WIN` and other `⎕W`… System Functions. `⎕WIN` defines the fields on the screen using a format matrix similar to the one in GDDM's ASMFMT call. This is the same interface that APL\*PLUS/PC offers, and I find it somewhat inelegant and a bit slow; though compared with using GDDM via AP126 it is a paragon of simplicity. Unlike GDDM this interface does not provide any graphics capability - that is what the `⎕G`… family of System Functions are for. These, again, are the same as the APL\*PLUS/PC offering.

However, APL\*PLUS II also provides an interface to third-party graphics software (included in the product) that implements the Graphics Standard Interface - GSI - and supports an impressive list of devices. GSI is an ISO and ANSI device independent graphics standard, which means that you can decide what you picture looks like without having to worry what device you will use to produce it; and the definition should work on a wide range of hardware. This has to be the right approach. At the moment you cannot mix Text and Graphics on screen using either GSI or the `⎕G`… functions in conjunction with `⎕WIN`; but under OS/2 Presentation Manager all screen handling will be in graphics mode - otherwise you cannot scale panels or lay them over each other, so I am sure that STSC will fix that restriction when they produce an OS/2 version.

As far as Communications with other systems are concerned there are really three issues. If you want to drive local devices using the serial or parallel ports - touch screens, for instance, recently reared their heads - `⎕ARBIN` is well up to the task. If you want to log on to a mainframe, you need an IRMA board (or something similar) if it's an IBM bi-synch system, otherwise the built in terminal emulation or `⎕ARBIN` should do the trick. Finally if you want to call programs in other languages, possibly running in other CPUs on a network, that is a bit harder. This is what IBM's new Systems Applications Architecture - SAA - is all about; and the central APL facility here is `⎕NA`, which isn't available, yet. However, all the signs are that STSC intend to provide the necessary features in this area; and my guess is that they will be available before most people actually need them.

## Summary

I'm glad I bought a copy.
