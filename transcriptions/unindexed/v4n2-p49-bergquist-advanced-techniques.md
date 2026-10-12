---
title: 'Book Review: APL - Advanced Techniques and Utilities'
authors:
- Dick Bowman
volume: '4'
issue: '2'
page: '49'
unindexed: true
transcribed: 'from page images of VOL.4-NO.2-OCTOBER-1987.pdf, pages 51–52 (printed 49–50); Claude, 2026-10-12'
review: draft
tags:
- reviews
- programming techniques
queries:
- "The Contents line reads “Bergquist - Advanced Techniques”; the printed heading is “Book Review: APL - Advanced Techniques and Utilities”, by Gary A Bergquist, reviewed by Dick Bowman."
- "The publisher’s address (Zark Incorporated) is kept."
- "⎕KITCHENSINK is printed in the APL font; set as code."
- "Kept as printed: “inculcate a instinctive urge”; “oldAPL imitate newAPL”; “IBM327x's and PC's”."
---

**by Gary A Bergquist**

*reviewed by Dick Bowman*
{ .byline }

Chapter Titles: 1 Limbering Up; 2 Branching and Looping; 3 Computer Efficiency; 4 Positioning Character Data; 5 Sorting and Searching; 6 Selecting; 7 Frequency Counts, Accumulations and Cross-tabulations; 8 Writing User-friendly Interactive Functions; 9 Manipulating Dates; 10 Writing Reports; 11 System Development Procedure; 12 Programming Standards; 13 Workspace Design and Documentation; 14 File Design and Utilities; 15 Boolean Techniques; 16 Irregular Arrays; 17 Curve Fitting; 18 Financial Utilities; 19 Exception Handling.

I really want to feel positive about this book; the world's been waiting for one with this title, but the contents make me feel uneasy. In my perception APL needs two educational texts which it doesn't yet have; the first is an introductory text which is as contemporary as those of Gilman/Rose and Pakin/Polivka were when they were published, the second is the book that takes over where the first stops and solves the problem so many newcomers express of 'now I know what all the symbols do, how do I make something useful?'.

Many have tried, and in essence I perceive the text at hand as being an attempt to supply my second need; it functions at a level closer to the code than Smith's 'Design Handbook' and is less philosophical than the Gibson/Metzger/Levine IPSA82 tome. It's not a case of choose one from three, they complement one another.

I really do like the way it starts, with a set of exercises for the reader; it conjures up a vision of the future in which we install APL terminals in all bookshops and only permit books to be purchased by those mentally equipped to read them. At least it establishes whether the reader and Mr Bergquist are on the same mental plane.

Let's be absolutely positive about this; anyone who reads this book, attempts the exercises therein, and follows the advice given about development procedures is going to produce APL solutions which are a whole league in advance of those produced by someone who doesn't. So why am I so uneasy about an unqualified recommendation?

At a general level I continually found myself thinking that the author was addressing questions which the APLer fresh from an introductory course should have formulated answers to already. That these questions should either be the stuff of an introductory course, or else that the solutions should form part of well-stocked public libraries. The question I find hard to generate an answer to myself being why it's so difficult to inculcate a instinctive urge to go and look in the public libraries on the part of the newcomer? Perhaps to be as fair as I can, a novice reader of Mr Bergquist's book would benefit from the insight being given into developing this sort of utility - maybe the book is more subtle than me (admittedly this isn't too difficult).

More specifically, two chapters make me distinctly uneasy; Chapter 8 on 'user-friendly interactive functions' and Chapter 16 on 'irregular arrays'.

The first is based exclusively around stop-start dialogues of the 2741 genre; and I don't see where this is a major technique any more. Can't we agree on an approach to dialogue amongst ourselves so that a system gets developed in two stages... a) as an open system in the classic 'functions take data from their arguments and return results' mould; which serves to get the processing running, before... b) we wrap these proven functions up in utility dialogue for current hardware like IBM327x's and PC's. Agreed that the IBM327x is one of the lousiest man-machine interfaces yet developed; in the mainframe world everybody else uses one and if we want our APL applications taken seriously we really ought to try and make them have the same sort of features as are demanded of other applications. I haven't yet seen a really good set of utilities either for the 327x or for the PC using STSC's `⎕KITCHENSINK` approach - both of these must surely be overdue.

As for the second - my personal feeling is that old-generation APL is old-hat and that making your oldAPL imitate newAPL isn't a relevant skill for 90% of APLers. Either you have generalised arrays (in which case use them), or you don't (in which case live with what you have). Given the historic progress in hardware power I would anticipate desktop nesting becoming the norm in a couple of years for all but the most underprivileged users. Agreed there are problems, but I really would like to begin seeing books about APL which treat nested arrays as something more fundamental than a trip to the leper colony. Do it right from the very first day. Again, to be fair to Mr Bergquist - his excursions into APL2/NARS/IPSA territory appear to be thorough, he favours no single participant.

So there you have it, to me this seems to be a somewhat expensive book for its contents; on the other hand I would expect most of it to find a ready market if the word 'Advanced' is sufficiently discounted. By another token - if you find a function in it that saves the time of writing that function yourself you end up ahead.

Available from:

<p style="margin-left: 2em">Zark Incorporated<br>53 Shenipsit Street<br>Vernon<br>Connecticut 06066</p>

<p style="margin-left: 2em">USA Price: 44.95 USD<br>(plus 15.00 USD for optional APL*PLUS/PC-compatible functions diskette).<br>Paperbound, 488 pages, 200+ utility functions described/listed/on disk.</p>
