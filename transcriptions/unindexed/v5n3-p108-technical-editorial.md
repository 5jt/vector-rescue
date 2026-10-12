---
title: 'Technical Editorial: Second Generation APL on Personal Computers'
authors:
- Jonathan Barman
- Dave Ziemann
volume: '5'
issue: '3'
page: '108'
unindexed: true
transcribed: 'from page images of VOL.5-NO.3-JANUARY-1989.pdf, pages 110–111 (printed 108–109); Claude, 2026-10-12'
review: draft
tags:
- implementations
- language design
queries:
- "Contents line “Technical Editorial:”, Jonathan Barman; the title is the fuller printed heading, and the printed byline is “by Jonathan Barman and Dave Ziemann”."
- "Kept as printed: “with the an automatic overlay technique”; “IBMs APL2/PC”; “as well the full range of operators”."
---

*by Jonathan Barman and Dave Ziemann*
{ .byline }

There is some excitement in the APL community about the second generation APL interpreters that are now available on the 386 based machines, and other high-performance personal computers. The main reasons for this interest are the additional power of the new APLs, the availability of the whole machine memory, and the increase in processing speed. Also, all three major second generation APLs are now available, so that it is possible to use the system of your choice. The next issue of VECTOR will contain detailed reviews of IBM's APL2/PC, STSC's APL\*PLUS II for the 80386, and Sharp APL/UX, or SAX, as it is more commonly called.

Second generation APLs are more powerful than vanilla flavoured APL, so much more so that the increase has been compared with the difference between Fortran and APL. The restrictive universe of ISO standard arrays can place constraints on the way of thinking. All kinds of subtle algorithms have been invented to get around these limitations, which make newcomers to APL gasp and stretch their eyes. Rather than increasing complexity, nested or enclosed arrays are a more natural way of thinking about, and structuring data. With generalised operators, these tools often provide simpler solutions to problems which can otherwise encourage the programmer to search for an elusive and perhaps unreadable 'parallel' solution.

Of course, there are the usual problems with added power. Huge arrays can be created with a few keystrokes, and as it looks so simple the perpetrator fails to realise quite how much data has been created or how much redundant computation is performed. The condensed notation can take a little while to get used to, and can appear complex, in just the same way as ordinary APL does at first.

At long last it is possible to use all the memory in a machine. Memory is now quite cheap, and most modern PCs already have more than the 640K limit of the old processors. Getting around the 640K barrier was always difficult. APL\*PLUS PC release 7 removed some of the pain with the an automatic overlay technique, but this could only be regarded as a stop gap measure pending a proper solution. Additional programming is often necessary where large amounts of data are involved, but the extra memory should relieve the programmer from having to overlay code as well.

The performance of the new offerings is surprisingly good, perhaps up to mainframe standards. It is now possible to develop production systems that compete with similar mainframe applications, but with all the benefits of the immediate response of a dedicated PC.

Perhaps the most significant benefit is that many mainframe APL solutions can be transferred to run on personal computers with little change. All the major APL vendors now offer mainframe-equivalent APL systems in the PC environment. The mainframe workspace size can be matched and usually far exceeded by buying sufficient memory. Most mainframe applications are well within the 16 Megabyte limit, and the vast majority have workspaces of less than 2 Megabytes. If data has to be shared, then networking PCs can provide equivalent solutions, though with large data volumes it could be difficult to match the performance of the big teleprocessing systems.

The three systems mentioned above all show a high degree of compatibility with their mainframe counterparts, although there are significant differences between them. IBMs APL2/PC comes in 16bit and 32bit versions, only the latter providing large workspaces and 4byte integers. The implementation is close to mainframe APL2, with nested and mixed arrays, generalised and defined operators. The IBM approach is to use shared-variables wherever possible, and Auxiliary Processors and the necessary support code are supplied with the product. The key features here are probably mainframe compatibility and connectivity.

STSC's method of integrating the system with its environment is to use specialised quad-functions; the same ones appear throughout the APL\*PLUS family of interpreters on all machine sizes. The system provides the same functions, nested and mixed arrays, and generalised operators as APL\*PLUS mainframe. The APL\*PLUS II key benefits are high performance, environmental integration, and cross-range compatibility. The under-exposed Sharp APL/UX interpreter is a Unix based extension of the Sharp APL/370 language. In fact this system closely approaches the ideal APL language as described by Ken Iverson in his Dictionary of APL. It supports enclosed arrays, mixed arrays and generalised operators, as well the full range of operators available on the mainframe system. Key features here might well be perceived to be language purity and completeness, leading to a highly productive application development environment.

All in all, interesting and exciting prospects. Get your own machine and run your application without having to put up with unpredictable response times.

The theme for the next issue of VECTOR will be second-generation APLs on personal computers. Our reviewers will be taking you through the options and you can make up your own mind which of these APLs must be yours. Following on from our technical reviews, we would like to publish the experiences of users of these systems. VECTOR will be pleased to receive letters, articles and case-studies on the use (or abuse) of second-generation APL products on PCs; perhaps you have found them too resource hungry, or the perfect vehicle for delivering high-performance solutions. Extended APLs may relieve the programming burden considerably, or on the other hand you may feel that they encourage unreadable and unmaintainable code. Either way, please let us know. Print-files on DOS-format disks are perfectly acceptable, and for longer articles we encourage you to also provide high-quality diagrams where possible.

At the other end of the scale, a forthcoming issue of VECTOR will be featuring I-APL version 1.1, STSC's Pocket APL, and Sharp APL/PC.
