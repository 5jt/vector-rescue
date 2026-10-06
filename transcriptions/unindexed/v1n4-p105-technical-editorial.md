---
title: 'Technical Editorial: Is APL Always Appropriate?'
authors:
- Jonathan Barman
- David Ziemann
volume: '1'
issue: '4'
page: '105'
unindexed: true
transcribed: 'from page images of VOL.1-NO.4-APRIL-1985.pdf, pages 107–109 (printed 105–107, upper part of p.107: the editorial, the VECTOR Publication Standards for APL Code, and the Introduction to Contributed Articles, which introduces art10002080, art10002530 and art10009540); Claude, 2026-10-04'
review: draft
tags:
- APL in perspective
queries:
- "The publication standards repeat those printed in v1n2-p99-technical-editorial.md, with “between” for “beween”."
- "Slip transcribed as printed: “one gets ones head”, “10% of the code in an interpreter account for”, “J Ansell” (Alan Ansell in the index; the article’s own byline is checked there)."
---

by Jonathan Barman and David Ziemann
{ .byline }

When should APL be used? As this journal is read mainly by those who have been converted to APL, perhaps the question should be put another way; are there any programming tasks where another language would be more cost effective? Those of us who are very committed to APL should stand back every now and again to take stock of their reasons for using APL, and look to see if it would be worth investing the time to obtain equivalent skills in another language. The APL community is rightly accused of religious fervour in favour of APL, to the exclusion of all other languages.

APL interpreters are large, and need a reasonable amount of memory to work satisfactorily. If there are less than 32K bytes of memory available, then one must consider using another language. BASIC is small, universally available, and universally hated by APLers, but does the job when it has to. FORTH is even smaller, and is pleasant to use when one gets ones head screwed on the right way!

APL can be slow, and if speed is important, then a compiled language or assembler may be more suitable. Most APL interpreters allow machine code to be mixed in with APL, so speeding up heavily used pieces of code is reasonably easy. Although it is possible to run machine code programs from within VS APL this technique does not seem to have been widely used, and it has been largely left to APL interpreters on micros to provide this facility. APL is not however relegated to those tasks where speed is not an issue. In fact it is sometimes used effectively in time-urgent environments; Myriade APL for example has most of its operating system environment written in APL. How about writing an APL interpreter in APL? Ridiculous? Not so; parts of VSAPL and the APL2 interpreters are written in APL (you may have noticed a strange message appearing when a workspace load is interrupted, which is because quadLX is written in one of the secret APL functions). The 10%—90% rule is often said to apply in such cases, where 10% of the code in an interpreter account for 90% of the running time. In this situation, the essential 10% is written in assembler, while parts of the less critical 90% can be implemented using APL itself.

The ACM Communications has a regular feature ‘Programming Pearls’ written by Jon Bentley, and in the February issue he explores these 10%—90% ‘rules’, which apply to many other areas beside speed of execution - recommended reading if you have access to a copy.

As well as running machine code, we also want APL to talk to packages and systems written in other languages. Sometimes the interface can be made directly by APL itself, and other times a low-level interface program written in C or assembler might be used. Two contributed technical articles in this issue report on the successes using these kinds of technique.

Finally, and perhaps most importantly, there is the question of whether an application is, by its nature, more appropriately programmed in a language other than APL. This is a very difficult question to answer, as it requires extensive knowledge of at least two programming languages, which is a fairly rare skill. With nested arrays, APL is coming of age and appears difficult to beat. The major contenders for special applications seem to be Prolog and its derivatives, and Nial.

We are particularly keen to receive letters and articles on APL interfacing and also on the use of languages and systems other than APL. Please keep your contributions coming!

## VECTOR Publication Standards for APL Code

In order to make the production of VECTOR easier, the following rules should be adopted when preparing letters, articles and other contributions for publication.

Please do not include APL symbols within the text. If an APL symbol needs to be referred to, use its name; most APL textbooks have a list of symbols and their standard names.

Where variable or function names are referred to within the text they will be set in ordinary capitals. This means that sentences have to be carefully worded so that a function or variable name can be easily distinguished from any other words that need to appear in capitals.

APL statements and function listings will be reproduced from the submitted document whenever possible, and will be pasted onto a separate line between the text. This means that the listings should be of high quality; a ‘daisy-wheel’ printer with a carbon ribbon should be used. If you do not have a quality printer, we are prepared to re-set the APL ourselves if it is not too long, but we would much rather not do this as it is all too easy to make mistakes. Ideally we need two documents; the “readable” copy which shows what the final appearance is likely to be, and the “printer’s” copy which we actually send to the printers. The “printer’s” copy needs to have all the APL completely separated from the text. The easiest method is to leave three blank lines in the text where the APL is to appear, and to have a separate sheet containing all the APL; each section also separated by three lines. A simple numbering scheme can then be used to show where the APL block is to appear in the text. These APL characters will be photo-reduced and inserted into the text body.

Drawings, figures and black and white photographs are welcome, as they help to break up the text and make articles more visually interesting. Please prepare each figure on a separate sheet of paper, and give it a number and caption. The caption will be typeset and will appear at the top of each figure, which will be presented in a box as near as possible to the reference in the text. Do not worry about the size of the drawing, as the printers will photo-reduce it to fit the size of the page or the space available. Your text should refer to the drawings strictly by sequential figure numbers.

Footnotes and references will be grouped together at the end of the article, so please avoid writing text that requires a footnote to be on a particular page.

## Introduction to Contributed Articles

This issue we are presenting three contributed articles. In addition we have a review of QL/APL and also a “Pot-Pourri of Improveable Code” from Dick Bowman, employee of the CEGB and the Association’s Activities Officer. Dick’s contribution started as a letter in response to our plea for improveable code, but as postscripts were added one by one it became apparent that it was too long for the letters page. Therefore the result of Dick’s efforts can be found in the “Surely There Must be a Better Way” feature, and we welcome any responses or further input to the column.

The contributed articles follow the theme of “Is APL Always Appropriate?”. In “Moving Data from 1-2-3 to APL” Michael Carmichael of Occidental International Oil Inc. recognises that many people use Lotus 1-2-3 to ease the strain of developing data entry front-ends in APL. He describes four techniques that he has used to import 1-2-3 worksheets into APL.

A different approach is taken by Romilly Cocking, a Director of Cocking and Drury Ltd., who uses a Symphony utility in conjunction with a program written in the C language to import Symphony worksheets into APL via DIF files. His article is entitled “A DIF File Interface”.

Finally, “When Domino is not Sufficient” explains how APL code can be used to avoid the intrinsic problems caused by the application of the matrix inverse function to singular and near-singular matrices in MIPS APL. This is presented by A Sykes and J Ansell of the Department of Management Science and Statistics, University College of Swansea.
