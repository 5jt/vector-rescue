---
title: News from Sustaining Members
volume: '21'
issue: '4'
page: '10'
unindexed: true
transcribed: 'from page images of v214.pdf, pages 10–12 (printed 10–12); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed under the heading “News from Sustaining Members”, unsigned: items from MicroAPL Ltd and Kx Systems, and “APLNEWS for Japanese Audience”, headed “from Kyosuke Saigusa”. The Vector Product Guide follows on printed 13."
- "Kept as printed: “the APL interpreter provide access”; “a real-time database that process a million events”; “CSV,ATF”; “prior to APL processing..”; “licensed” and “non-licenced” in one sentence."
---

## MicroAPL Ltd

The launch by AMD of a 64-bit version of the x86 architecture, a couple of years ago, has opened the way for low-cost, 64-bit systems in the mass market. Today, you can buy a desktop machine – or even a laptop – with a 64-bit processor, for just a few hundred pounds. Intel have now followed AMD with a binary-compatible equivalent, and, over the next few months, we can expect 64-bit x86 systems to become commonplace. 64-bit versions of Windows and Linux are available to run on this architecture. In addition, Apple has sold 64-bit Macintoshes, based on the PowerPC architecture, for some time. 64-bit Servers are, of course, well established.

Such machines can address extraordinary amounts of memory. 32-bit systems are limited to at most 4Gb of memory address space, and usually this is not all available to user processes (Windows, for example, normally has a limit of 2Gb). Today, XP Professional x64 Edition supports up to 128Gb of RAM and 16 Terabytes of virtual memory. In the future, even more memory will be usable. And the cost of RAM has fallen to such an extent that it is already possible to configure desktop machines with tens of gigabytes of memory for a couple of thousand pounds.

Of course, it is not just the size of workspace which matters; it is also the maximum size of arrays. 32-bit APL systems use 32-bit slots to hold array sizes and dimensions. Thus, even if the processor can address more than 32-bits and the APL interpreter provide access to a workspace size greater than 4Gb, it does not follow that the APL interpreter will necessarily handle arrays which will take full advantage of this memory.

For this reason, MicroAPL is introducing a fully 64-bit version of APLX, which will overcome all limitations in workspace and array size for the foreseeable future. APLX64 is this new product. It is initially being made available for Linux and Windows, with a MacOS version following. In APLX64, all array dimensions are 64-bit, so there are effectively no limits other than available memory on the number of elements in any array, or the maximum length along any dimension. Integers are also 64-bit (otherwise you would have to use floating-point numbers to index arrays!). Booleans remain as one bit per element, making it possible to handle huge Boolean arrays without excessive memory requirements. Huge native files and component files are of course fully supported.

We believe this product extends the reach of APL upwards to applications which previously were beyond its reach. These include modelling and simulation using huge data sets, and OLAP applications for analysis and aggregation of large volumes of transactional data. In this new world, you do not need to compromise: you can just load the entire database into your APL workspace (the APLX `⎕SQL` system function will be handy here!). In some ways, this is taking APL back to the kinds of application where it used to be strong, but where it lost ground because the amount of data became too big to fit in the workspace. The benefit is direct manipulation, in the APL workspace, of data which other languages have to process piecemeal.

APLX64 is currently in beta, and will be available in the first quarter of 2006.

## Kx Systems

Kx Systems has announced new speed gains for its kdb+tick application, achieved by eliminating the latency between data capture and data analysis. Kx, leader in high-performance databases and financial applications, offers kdb+tick worldwide on Linux, Solaris and Windows x64 operating systems.

> “Today’s onslaught of tick data streams in 24x7 from multiple exchanges worldwide. The trading firm that acts on this data faster stands to make enterprising trades microseconds ahead of the competition,” said Simon Garland, Kx CTO. “Zero latency kdb+tick makes streaming data usable in applications immediately.”

Because kdb+tick v. 2.2 removes the traditional delay between the capture of streaming data and its availability for applications, it enables traders to receive every single tick instantly. Applications written using kdb+tick can, for example, update a spreadsheet in real time with every tick that streams in.

By removing the latency between tick data capture and analysis, kdb+tick endows extreme speed applications, such as auto trading and program trading, with more time to execute advanced strategies. It becomes feasible, for example, to perform full depth-of-book program trading on billions of ticks in a single trading day.

Matthew Rock, Director IT at Dresdner Kleinwort Wasserstein, commented “We rely on the capture speed and fast, flawless time-series analysis in kdb+tick to develop unprecedented trading models, to back test trading strategies, and to position DrKW for superior program trading.”

Kdb+tick gives traders more time to respond decisively and intelligently to market conditions in real time, and its database heritage takes kdb+tick beyond ordinary streaming data solutions. Without losing a microsecond of red-hot speed for streaming data processing, kdb+tick also maintains a real-time database that process a million events per second and saves a historical database for business-critical functions such as regulatory audit trails. For more information visit *www.kx.com*.

## APLNEWS for Japanese Audience

*from Kyosuke Saigusa*
{ .byline }

We started to distribute APL related news to Japanese audience strictly in Japanese language via our APL programmed Web site (*http://aplcons.com/apl*) in recent months. I would like to introduce some reported items to you, wondering if they are of some interest outside Japan.

An interesting demo program has been completed based on the APL COM interface, which became available with IBM APL2 Windows version released in May this year (Workstation APL2 V2.6).

This program (about 250 lines of APL2 code with only one utility subroutine) will start Excel and allow computation of the data on Excel sheets (regarded as pages of 2 dimension arrays in front of you) interactively from an APL window by simple APL statements handling 2-dimension arrays.

This will take XLS, CSV,ATF files for input and allow parallel processing between APL and Excel because any changes made on Excel side will be reflected in APL processing because the latest data are always read-in prior to APL processing..

The program will run in full licensed interpreter as well as non-licenced APL2 runtime. Any APL interpreter functions in respective environments are usable without restrictions. We intend to use this program to broaden the base of APL users amongst the Excel users.

There are other topics, such as a common utility APL function library based on namespaces which allow even GRAPHPAK as external functions with a lot of merits for APL group users and Windows dialog design scheme for application developers for higher productivity than standard approach.

But APL2-COM demo-program reminds us of the importance of the use of a very small elementary part of APL2 language for general public for practical results. It will be distributed basically free of charge to individuals outside enterprises. Any inquiries are most welcome.
