---
title: Technical Editorial (with publication standards and introduction to contributed articles)
authors:
- Jonathan Barman
- David Ziemann
volume: '2'
issue: '1'
page: '92'
unindexed: true
transcribed: 'from page images of VOL.2-NO.1-JULY-1985.pdf, pages 94–96 (printed 92–94: the editorial, the VECTOR Publication Standards for APL Code, and the Introduction to Contributed Articles, which introduces art10009930, art10007700 and art10003940); Claude, 2026-10-05'
review: draft
tags:
- APL community
queries:
- "p.93, the publication standards, carries the running head “Vol. 1. No. 4”: the page from the previous issue reused. Its text is identical to that in v1n4-p105-technical-editorial.md, checked against this page."
- "“Glenford J Myers … ‘Reliable Software Through Composite Design’”, “afficionados” and “seen?.” are printed so."
---

by Jonathan Barman and David Ziemann
{ .byline }

What is it about programming style that rouses such strong emotions in people? APL symbols can cause apoplexy amongst those who are not used to them, and APL afficionados get very excited about code that is, to them, poorly written. This emotion is understandable if you take the view that hard to read code is by definition poorly written. “I’m great at writing code, but I can’t make head or tail of this load of junk” is the first reaction, rather than “This looks clever, let’s see if I can understand it”. For instance, long functions with many globals usually, and we think rightly, elicit the first response. Short functions with no globals should warrant closer inspection before being classed as good, bad or indifferent. Of course, code which is very easy to understand may not necessarily be good APL; for example a function that loops on every row of a matrix rather than using the power of APL to process the whole matrix at once.

We recently heard of an APL programmer who was having some trouble making modifications to a system where there were two notable functions with over six and seven HUNDRED lines. We once had to maintain a workspace where the key functions had been named after the entire Arsenal football team! Actually it is often the apparently more sensibly named functions that cause problems. For example, ’BOX’ has been used both for a function that converts a vector to a matrix, and for one that puts lines around a matrix for display. If the wrong function were copied into the workspace (from a utility library) it would cause a problem, in this case a small one; the functions are so different that the error would soon be detected. What happens though if the difference is small, and the error is not revealed during testing? A good example is the definition of a function often called ’ON’ - how many similar, but different definitions have you seen?.

The concept of “programming style” can be thought of as applying to at least three levels of an APL system; the line level, function level and the workspace level. The line level refers to the style at the level of individual function lines, or fragments thereof, the function level to the contents of user defined functions and the workspace level to the interaction of all the components of the workspace.

Some examples may clarify this idea. At the line level multiple assignments are normally to be avoided because of the difficulty of debugging the code and because the line may not be restartable if an error occurs in the middle of the line. At the function level a good programmer will generally produce well named short functions that do not generate side effects. At the workspace level programming style is concerned with the relationships between functions. There’s enough in this last topic for a whole book, and in fact Glenford J Myers has written one - although not with APL in mind. “Reliable Software Through Composite Design” is extremely useful in the design of APL programs, and formalises many of the ideas which we often just have a ’gut feel’ about.

A further level where programming style could be said to operate is in the area of file design and access, again a large and involved subject, worthy of several books, let alone articles in VECTOR.

We would like VECTOR to become a forum for you to air your views on good and bad coding style. Let us know what you think, and if it generates some emotion, then that should make VECTOR more exciting reading!

## VECTOR Publication Standards for APL Code

In order to make the production of VECTOR easier, the following rules should be adopted when preparing letters, articles and other contributions for publication.

Please do not include APL symbols within the text. If an APL symbol needs to be referred to, use its name; most APL textbooks have a list of symbols and their standard names.

Where variable or function names are referred to within the text they will be set in ordinary capitals. This means that sentences have to be carefully worded so that a function or variable name can be easily distinguished from any other words that need to appear in capitals.

APL statements and function listings will be reproduced from the submitted document whenever possible, and will be pasted onto a separate line between the text. This means that the listings should be of high quality; a ‘daisy-wheel’ printer with a carbon ribbon should be used. If you do not have a quality printer, we are prepared to re-set the APL ourselves if it is not too long, but we would much rather not do this as it is all too easy to make mistakes. Ideally we need two documents; the “readable” copy which shows what the final appearance is likely to be, and the “printer’s” copy which we actually send to the printers. The “printer’s” copy needs to have all the APL completely separated from the text. The easiest method is to leave three blank lines in the text where the APL is to appear, and to have a separate sheet containing all the APL; each section also separated by three lines. A simple numbering scheme can then be used to show where the APL block is to appear in the text. These APL characters will be photo-reduced and inserted into the text body.

Drawings, figures and black and white photographs are welcome, as they help to break up the text and make articles more visually interesting. Please prepare each figure on a separate sheet of paper, and give it a number and caption. The caption will be typeset and will appear at the top of each figure, which will be presented in a box as near as possible to the reference in the text. Do not worry about the size of the drawing, as the printers will photo-reduce it to fit the size of the page or the space available. Your text should refer to the drawings strictly by sequential figure numbers.

Footnotes and references will be grouped together at the end of the article, so please avoid writing text that requires a footnote to be on a particular page.

## Introduction to Contributed Articles

As APL2 inevitably becomes more popular the need for us to stop procrastinating and get to grips with it increases. To help us do this Norman Thomson of IBM Hursley Park has written our first contributed article in this issue. “A Guide to APL2 Nested Arrays” is a tutorial which takes us to quite a sophisticated level of expertise via a number of “five-finger exercises” — the APL2 equivalent of piano practice.

Following the nested arrays theme, John Scholes from Dyadic Systems presents a short excursion into some of the second generation features of their APL. “Operators and Nested Arrays in Dyalog APL” nicely demonstrates the power of these extensions.

Per Hultin and John Hagger address the issue of choosing the right horses for courses and explain why they have taken the approach of developing assembler routines to improve APL performance by speeding up many of those important utilities.
