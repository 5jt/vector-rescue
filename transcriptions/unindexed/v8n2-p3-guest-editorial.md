---
title: 'Guest Editorial: Wanted: Programmer Support'
authors:
- Gregg W Taylor
volume: '8'
issue: '2'
page: '3'
unindexed: true
transcribed: 'from page images of VOL.8-NO.2-OCTOBER-1991.pdf, pages 7–8 (printed 3–4); Claude, 2026-10-12'
review: draft
tags:
- language design
- APL in perspective
queries:
- "Printed heading “Wanted: Programmer Support”, byline “Guest Editorial by Gregg W Taylor”; the Contents page gives “Gregg Taylor”."
---

*Guest Editorial by Gregg W Taylor*
{ .byline }

Extended APLs are no longer new products. By now, there should be evidence of a fair amount of proficiency in the use of nested arrays, user-defined operators, and the various new functions that manipulate nested arrays. Yet, I am compelled to say that the level of proficiency in these areas is disappointingly low.

I have not collected hard evidence in the form of surveys or extended research; this conclusion is based on observations I have made at several corporations, several user groups, and chats with other APLers. As a disclaimer, I will say that there is a good amount of code that is being written using extended features - by a few good programmers. But the majority (!) of people that use APL to program are still using a small subset of the capabilities available to them. WHY?

I think there are four basic reasons:

- the cost and effort of conversion
- the prices of the newer systems tend to be higher
- extended systems seem more complicated
- a lack of good examples

I will briefly cover these in the order listed.

Moving out of flat APL into the broader realm of ragged arrays and the each operator is really not that difficult. Migration tools are provided, and by and large, flat APL is a proper subset of nested systems. But on a practical basis, there are those nagging differences. IBM no longer supports the 124 processor; strand notation and ambivalent functions allow code that once failed to now successfully execute; and if you have never tested for complex numbers, you may be inclined to start. In short, it is a simple application that migrates trivially; the more sophisticated, the more considerations.

And I know of large corporations that are intimidated by the prospect of migrating hundreds, or even thousands, of workspaces out of a system that is working fine. This situation is worsened by purists (like myself) who have to improve the systems in the process by rewriting existing methodologies. All of this is for the better, mind you; but it is all at a cost.

The newer systems, mainly on the PC, tend to carry higher price tags. IBM has reduced the price of their mainframe product to approximately the VSAPL price, and their APL2PC product is still $500, but compare STSC's two PC offerings. I am not suggesting that there should not be a price differential between flat APL and an extended system, but I do think the pricing should be accessible to the fellow who can afford an 80386 machine. When you can buy C compilers and assemblers for under $200 (and even under $100 in some cases), it's no wonder that even $500 seems high. Is APL priced more for corporations than individuals?

But I can't blame the vendors for the programmer inertia which prevents (flatland) APLers from learning to use the extended systems. I remember my own misgivings about learning a new way to do APL - all the timings that had to be done, all the new idioms to be discovered, the pitfalls to be avoided. It is easier to just keep on doing things the same old way. For me, this is the most frustrating thing to witness - complacent programmers, no longer interested in growing in their professions.

Some have said that the new flavours of APL are simply too complicated. I even remember listening to one APLer saying that, since a printer could only print pages, why work in dimensions higher than two? More sophisticated data structures are intended to more closely model more complicated physical realities. Flat APL provided a method of organising data dimensionally; extended APLs provide a broader range of data structures, hence a close match with real data in more situations. Once the data structure is decided upon, the other new features are needed to manipulate that data.

The process of abstraction and generalisation leads to richer structure and function. To paraphrase Einstein: keep things as simple as possible, but no simpler. Some solutions are not adequate when over-simplified. Extended APLs provide more capabilities when dealing with non-trivial problems.

If the new APLs are more complicated, I think this is a result of the lack of understanding about them. Once you get acquainted with and use the new features, it becomes a lot more difficult to solve a problem using flat APL. Overcoming the reluctance to learn new tricks and the fear of not catching on quickly are the two real problems facing APL programmers, not the language itself.

But the learning process could be made a lot simpler if there were more samples of good coding techniques in the extended APLs. Not all of us will do the timings, discover the nifty algorithms, and warn of the nasty pitfalls. Yet publications like this one are much too rare, and there are only a few books on techniques in extended APLs. The New York APL users' group has undertaken, with the support of the SIGAPL, the compilation of a book of APL phrases that deal only with extensions in the various dialects. This promises to be quite good - hopefully combining good coding style with interesting idioms, all the while illuminating the differences in the several flavours of APL available today.

Really getting the newer APLs into proper use is not that difficult a task. But it will require the efforts of corporations, vendors, programmers, and (a few) writers. It's hard, and often expensive, to keep up with new technology. Hardware has typically outstripped software in these areas, but I dare say that extended APLs are in the software vanguard, waiting for more of us to catch up.
