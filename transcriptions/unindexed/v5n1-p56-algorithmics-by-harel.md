---
title: Algorithmics by Harel
authors:
- Anthony Camacho
volume: '5'
issue: '1'
page: '56'
unindexed: true
transcribed: 'from page images of VOL.5-NO.1-JULY-1988.pdf, pages 58–60 (printed 56–58); Claude, 2026-10-12'
review: draft
tags:
- reviews
- education
- APL in perspective
queries:
- "Printed byline “reviewed by Anthony Camacho”. The lower part of printed 58 is an APL Consulting advertisement, not transcribed; printed 59 is the Recent Meetings section introduction, not transcribed here."
- "Kept as printed: the stray text-formatter command “.pa” after “is not mentioned.”, run into the paragraph; “over- emphasises”; “Addison Welsey” (for Addison-Wesley)."
---

*reviewed by Anthony Camacho*
{ .byline }

This is a very good book. The author's style has a refreshing directness and clarity. The subheadings of the chapters are a good sample and also show you the contents.

Preliminaries

1. What it's all about
2. Getting it done
3. Getting it done by computer

Methods and analysis

4. Getting it done methodically
5. Getting it done right
6. Getting it done cheaply

Limitations and robustness

7. You can't always get it done cheaply
8. Sometimes you can't get it done at all
9. The simplest machines that get it done

Relaxing the rules

10. Getting it done by co-operating
11. Getting it done by tossing coins
12. Are they better at it than us?

More knowledgeable reviewers have written that the book is an excellent survey of computer science (which I never studied) and it is certainly an excellent introduction to the range of computing that I know about and to some unfamiliar bits. I think it could be read with profit by intelligent sixth formers. It does require the reader to think. It encourages him to pause and to try to do things for himself too. Do not expect to get through its 400-odd pages without effort.

The bibliographic notes give, in 55 pages, a first rate survey of the best and seminal books on computer science. With a guide like this there is no excuse to be at a loss for a book on any topic in computer science. Such a guide (but to APL books) is just what we should have in Vector (reprinted say, once a year). If there was such a survey of the APL books in print and a reliable source which stocked them all, yet another small obstacle to the spread of APL in education would be removed.

The sections in the book which most interested me were those on the efficiency of algorithms and the non-computability of some kinds of problems, either because no conceivable machine could be fast enough or large enough or because the problem turns out to be logically undecidable.

Vector readers will be glad to hear that APL has a two page summary in the section on programming languages which, although one could cavil at some things in it, is clearly written by someone who appreciates what APL is like. It is not surprising in a book essentially about programming that APL's strength as a notation is not mentioned. .pa Every subject has its traditions and prejudices. Those of computing are ...... I was going to say what I think they are, but my view is equally prejudiced. How would we find out? An answer is to read a good survey of the subject and look for the occasions where solutions are approved of when no reason is given. This book is full of such value judgements because it is written in a lively style: the author's aim is plainly to explain things as clearly as possible and he doesn't care a bit if this clarity is used against him. In "Algorithmic methods" many of the solutions are described as 'better'. Some authors (should I say all politicians!) try to appear wise by saying things in a way which allows them to escape responsibility for what they dare not say straight.

So here is an illustration of what I found. How do we find the maximum distance across a convex polygon? Find all the distances from vertex to vertex and take the largest? No, he says, it's better to take a vertex, find the two vertices furthest from it, record the distance to the further one and then move one vertex round the polygon and see if one of the next pair of distances is larger and if so record that, until one has tested every vertex. His example allows him to demonstrate the ingenuity called for to reduce computation (which begins to be effective when the number of sides gets large), but he assumes that the solution must be a looping one.

I have said before that I think computer training too often over- emphasises looping so that students' ability to think in parallel is atrophied. I'm sure this is a mistake of the educationists. Parallel solutions (using J. J. Sylvester's 'multiple quantity' as Donald MacIntyre would say) can be just as elegant and can give even more delight than the cleverest recursion.

I do not think it is a fault of this book that parallel thinking appears so little in it. The reason is that it reflects the real world and there is too little parallel thinking there too. As Harel writes at the end of the chapter on Parallelism and concurrency:

> "Many of the best parallel algorithms known cannot be implemented because existing parallel computers are inadequate in some way. On the other hand, we still do not know enough about designing concurrent programs and systems to take full advantage of the features those same computers offer. The work continues, however, and many people hope that the next few years will produce developments that will put algorithmic and computerized concurrency on a par with the more manageable notion of sequentiality."

I hope he's wrong about "more manageable", and that it is a computing prejudice; if he isn't yet, I hope he will be made wrong one day.

> Algorithmics by Harel<br>
> Addison Welsey 1987<br>
> Price £14.95
