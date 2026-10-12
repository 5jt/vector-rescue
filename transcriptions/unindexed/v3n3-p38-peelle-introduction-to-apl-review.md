---
title: Introduction to APL – Howard Peelle
authors:
- Romilly Cocking
volume: '3'
issue: '3'
page: '38'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 40–41 (printed 38–39; it follows the end of Simon Garland’s review on p.38); Claude, 2026-10-12'
review: draft
tags:
- reviews
- education
queries:
- "Printed heading: “An Introduction to APL / by Howard A Peelle / Published by Holt, Rinehart and Winston, 1986. / Reviewed by Romilly Cocking”. The text calls the book “APL – an introduction”."
- "Kept as printed: “Both volumes are informal” and “the books are generally excellent” (the book and its instructor notes)."
---

*Reviewed by Romilly Cocking*
{ .byline }

**An Introduction to APL**  
*by Howard A Peelle*  
*Published by Holt, Rinehart and Winston, 1986.*

In the early Seventies, there were not many ways of learning APL. This did not matter much, as very few people wanted to learn it. Most students of the language were unwilling. They were victims of zealots who had just become APLers, and who were determined to share the good news.

Today, the situation is much healthier. A growing number of companies are making a healthy profit from selling APL products and services; more important, a large and growing number of organisations now depend on the use of APL to help them achieve their goals.

APL is in demand, and more people want to learn it than ever before. A wide variety of methods are available – public courses, CAI programs, and self-study books. For some years, the standard text for introductory courses has been Gilman and Rose (3rd edition, Wiley 1984). Originally published in 1974, ’the red book’ has gone through three editions, changed its colour, and sold well over a quarter of a million copies.

No book is ideal, and APL trainers are always on the lookout for new texts. I have just been reading *APL – an introduction*, by Howard Peelle. The text is intended for two uses; it can be read as a self-study guide, for individual students who are learning APL on their own; alternatively, it can be used as part of a taught course. The text has an associated volume of instructor notes, which contain details of the author’s educational philosophy, as well as teaching tips, and solutions to programming problems.

Both volumes are informal, but very well structured. The main text consists of a short preface, followed by two main sections, seven appendices, references, an index and a table of APL symbols.

The preface explains what APL is; why you should learn it; its strengths and weaknesses; some learning tips; and how to get started. The section on strengths and weaknesses is a model piece of persuasive writing, and should on no account be skipped over.

The first part of the book contains an introduction, followed by nine chapters. This part introduces the APL language; each chapter contains a list of contents, a set of objectives, examples, exercises, a review, and a set of programming projects. The pacing of each chapter has been carefully planned; early sessions go at a comfortable pace, but chapters eight and nine see the introduction of outer and inner product, and matrix divide.

The second part of the book consists of a further five chapters on APL tools. Each chapter describes (and gives the code for) APL programs that are useful in particular disciplines – business, statistics, mathematics, education and computer science. These are working programs that you can use on their own, or incorporate in your own software. The programs are written for clarity rather than efficiency, but they introduce the student to the idea of utility functions – a crucial point, omitted from many courses. Alas, the author does not place equal emphasis on the need to explore the utilities available on the student’s own computer system. Utilities can give valuable short cuts in software development, and they can also teach a lot. (If you write optimised but unreadable code, it may be kinder to lock the public versions, for just this reason!) No doubt the emphasis reflects the author’s preference for learning by experience rather than example.

At an introductory level, the book compares well with Gilman and Rose. It is even less formal, and much less daunting. It covers less material – if you learn everything in Gilman and Rose, you will know a lot more APL. How many actually do so?

*APL – an introduction* also adopts some unconventional terms – list rather than vector, input rather than argument. The vexed issue of terminology is discussed in the instructor’s notes, along with other contentious topics. I disagree with a number of choices made in this book, but one must welcome any text that emphasises that they are just choices. There are only two such choices with which I feel I must take issue.

The first is on the topic of commenting. In my view, this must be introduced very early on – in immediate execution mode, so students can pick up the habit of first-line comments as soon as they learn how to define a function. Once learnt, the habit sticks for life, but it is much harder to acquire later on!

The second is on the topic of branching methods. Peelle opts for the introduction of branching using the idiom

```apl
→label×⍳condition
```

This is later superseded by the more normal

```apl
→condition/label
```

The insuperable objection to the first method is that it goes completely wrong in origin 0. Anyone who learns it will one day waste a great deal of time finding this out the hard way.

These are minor criticisms, however, and the books are generally excellent. APL is easy, fun, and of great practical use. Peelle’s new book will help a new generation of students to find this out for themselves.
