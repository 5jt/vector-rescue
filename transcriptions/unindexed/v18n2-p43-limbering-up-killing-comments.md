---
title: 'Limbering Up: Killing Comments'
authors:
- Gary A. Bergquist
volume: '18'
issue: '2'
page: '43'
unindexed: true
transcribed: 'from page images of VOL.18-NO.2-OCTOBER-2001.pdf, pages 45–46 (printed 43–44; follows art10014430); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- development practice
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. The solutions are reprinted in 18:3 (art10014410)."
- "The e-mail address printed with Vector Production’s postal address is the organisation’s, and is kept."
---

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

Ill-disciplined APL programmers rationalise their failure to include comments with statements like, "Comments make my functions too big. I hate to waste valuable workspace on useless comments."

You can argue that comments are never useless, or that comments don’t consume much workspace, but your arguments are likely to fall on deaf ears.

Your better bet is to provide the lazy sceptic with a utility function that eliminates the comments from any specified user-defined function. They say, "Include plenty of comments in your functions and save them in a ‘development workspace.’ Use this utility function to eliminate all comments from the functions and save them in a ‘production workspace.’ You’ll have one workspace that is big and readable and easy to maintain, and another that is small and unreadable and streamlined for running."

Your task is to design and write a function named `UNCOMMENT` that eliminates the comments and all-blank lines from a specified function. Use `⎕CR` to convert the function to its character matrix representation; manipulate the character matrix to eliminate its comments and all-blank rows; and use `⎕FX` to convert the character matrix back to a function. See the `PRIMITIVE POINTERS` section for some hints.

The function should be efficient, but extreme efficiency is not needed since the function will be used during the development process, not during production. And, by the way, your function should contain lots of comments.

Send your solutions to:

> Vector Production<br>
> Brook House<br>
> Gilling East<br>
> York YO62 4JJ<br>
> UK email: apl385@compuserve.com

The notable functions and their authors’ names will be printed in the next issue of *Vector*. Good luck and happy limbering.
