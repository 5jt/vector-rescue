---
title: 'More on ‘A’ by Arthur Whitney'
authors:
- Ed Shaw
volume: '6'
issue: '4'
page: '62'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 64–65 (printed 62–63); Claude, 2026-10-12'
review: draft
tags:
- implementations
- language design
- performance
queries:
- "Contents line “Arthur Whitney on A”, Ed Shaw; the printed heading is “More on 'A' by Arthur Whitney”, “notes by Ed Shaw, via Anthony Camacho's Mailbox”."
- "The name of the language, A, is printed in italic throughout; kept so here."
- "Kept as printed: “what he has said at APL89”; “Rockerfeller Center”; “2\\*52” (2 to the 52nd power); “The digits 3716 … 3.7 gigabytes” (2 to the 32nd is 4,294,967,296)."
---

*notes by Ed Shaw, via Anthony Camacho's Mailbox*
{ .byline }

Way back in January, 1990, Arthur Whitney presented an update on his work on the *A* language to NY/SIGAPL. The meeting was hosted by Morgan Stanley in one of their corner offices high up in a Rockerfeller Center office building in the heart of Manhattan, overlooking a shimmering Avenue of the Americas after an early evening rain. It was a metaphorical venue for an APL that makes you feel on top of the world.

For the most part, Arthur reiterated what he has said at APL89, which was fully reported in the October 1989 issue of Vector. By January *A* had gone through one more revision and was operating on a machine with even more addressable memory. He also demonstrated *A* before our very eyes, including a quick pass through a 700 megabyte file containing all prices every five minutes for the last five years of a select group of stocks.

I remember trying to describe what I had seen to my associates in the office the next day. The digits 3716 stuck in my mind but I could not focus on what order of magnitude it was. Finally I calculated 2 to the 32nd power on my trusty super-calculator and realized that it was a workspace of 3.7 gigabytes. The remaining digits didn't matter! For someone who had just recently grabbed 130K of memory above 640K on a PC, it took the breath away, made the heart skip a beat, and caused the hands to develop a slight tremor. Just for the fun of it, Arthur pushed the workspace to the maximum - 4,097,835,008 bytes while I was talking to him recently on the phone. So is Morgan Stanley happy? No. They are anxiously awaiting the arrival of an IBM RISC System/6000 which will have an address space of 2\*52. I leave that computation to the reader.

It is wonderful talking with Arthur. He is excited about both APL and what he has been able to do with the interpreter. He is extremely pleased with the reception *A* has been getting at Morgan Stanley. Usage is spreading beyond the Analytical Proprietary Trading Group of which he is a part into other areas of the company. It may well be that *A* will save APL at Morgan. APL's performance has been increasingly challenged of late.

When asked what contributed to the increase in speed of *A* over other commercial APL interpreters, Arthur suggested the following factors:

- Many of the primitive functions execute 2 to 5 times faster because they use faster algorithms written in C.

- *A* allows the user to select a faster APL algorithm to solve the same problem because it has functions/operators not available in (some) other APL's, e.g. the rank operator.

- *A* uses **tight** code. It is more efficient simply because it was written by one person rather than by many over a period of years.

- *A* pre-parses to a greater extent than other implementations.

- Some meaningful efficiency derives from the absence of garbage collection (reorganizing memory so that free space is contiguous), perhaps as much as 20%.

How does *A* manage to avoid garbage collection? The answer lies in the large addressable memory space. When a request for memory is made, available memory is broken down into blocks which are some power of two in size. The new object is allocated a contiguous segment of these blocks. This process continues as more memory is requested. If real memory is no longer available, then unused objects are swapped out and the available pages are swapped in. There you do have object movement, but only what is necessary. In garbage collection as many objects are moved as are needed to clean up the fragmentation. As memory is freed in *A*, no movement takes place. Those pages are merely flagged as free.

Whether that space is usable depends on whether it is large enough to contain a new request. So there is no free lunch. In effect a trade off is made. Give *A* a large address space and under normal circumstances (who would call Morgan Stanley's circumstances normal?) there will always be space available. But fragmentation does occur and it is not directly removed. Theoretically, half the space might be fragmented enough so that only small objects can fit, so it is still possible to get a `WS FULL`.

Arthur and his colleagues have successfully processed objects of 400 megabytes in size, requiring intermediate storage of 800 megabytes. It took approximately a half hour to process on the Solbourne (A computer using SUN's SPARC chip. A side note: SUN was founded by people who were involved in the Stanford University Network project in the 1970's.)

One of the implications of *A*'s innovative memory management technique is that it ought to be transferable to other APLs running under an operating system that provides access to the paging mechanism. One wonders if it might indeed be implementable in some form using only a virtual workspace file as in STSC's APL\*PLUS/PC.

What is next? The current project for *A* is to add an interesting user interface using X-windows. And after that? ... Stay tuned. Since the source code is only 30K and the object code is only 100K maybe some way can be found to make *A* available to the rest of us mortals. One can hope.
