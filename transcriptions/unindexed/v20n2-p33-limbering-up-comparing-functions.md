---
title: 'Limbering Up: Comparing Functions'
authors:
- Gary A. Bergquist
volume: '20'
issue: '2'
page: '33'
unindexed: true
transcribed: 'from page image of VOL.20-NO.2.pdf, page 35 (printed 33; within Zark Newsletter Extracts, after “Utility Corner: Numbers to Words”); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
queries:
- "Printed as “Limbering Up: Comparing Functions”, but the task set is Execute Inverse (`EI`), whose solutions follow in 20:3 (“Execute Inverse”, art10014290). The heading evidently repeats the previous issue’s; the printed title is kept."
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. The reprint note at the foot of the page, which closes the extract, is included here."
- "The postal and e-mail addresses for solutions are Vector Production’s, and are kept."
- "Kept as printed: “some flab off you APL midsection”."
---

## Limbering Up: Comparing Functions

(The purpose of this column is to work some flab off you APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

The symbols for format (`⍕`) and execute (`⍎`) were chosen carefully by the implementers of APL to imply an inverse relationship. After all, `⍕` turns the numbers `3 4 5` into the character vector `'3 4 5'`. However, `⍕` and `⍎` are not perfect inverses. For example, `⍕` converts a numeric matrix into a character matrix, but `⍎` does not do the reverse.

Your task is to write a monadic function `EI` (Execute Inverse) that converts any array `A` to a character vector such that `A≡⍎EI A`. There are a number of useful applications for a function that translates an APL array into a character vector. We’ll discuss them next issue.

Send your solution to:

> Vector Production<br>
> Brook House<br>
> Gilling East<br>
> York YO62 4JJ<br>
> UK email apl385@compuserve.com

The notable functions and their authors’ names will be printed in the next issue of *Vector*. Good luck and happy limbering.

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA*
