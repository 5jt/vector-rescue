---
title: 'APL2 Packages: a Cautionary Tale'
authors:
- Nicholas Small
volume: '9'
issue: '3'
page: '100'
unindexed: true
transcribed: 'from page images of VOL.9-NO.3-JANUARY-1993.pdf, page 102 (printed 100; in Technical Correspondence, before art10000880); Claude, 2026-10-11'
review: draft
tags:
- development practice
queries:
- "A letter in Technical Correspondence, under the section heading on the same page. The signature block’s postal address is omitted."
---

*From: Nicholas Small, 12 Dec 1992*
{ .byline }

The following cautionary tale, relating to the use of packaged workspaces in APL2, may cause readers some amusement.

On 3rd November I made some modifications to a workspace and saved it. A few days later one of my users came to me to complain that the date appearing on the printout produced by the program was incorrect, although the data were up to date. The date being printed was 3rd November.

A quick examination revealed that the date was put in the output from an object named `TODAY` — but this object was not a variable set by the program, rather, it was a function, and a packaged function at that. Examination of the listing for this function revealed all: function `TODAY` looks to see if a variable `Today` exists and if it does then the value of `Today` is returned; otherwise `Today` is set to the current date and that is the value returned. (I guess that it was written like that to facilitate the production of a report with a given date.) When I saved the modified workspace, the value of `Today` was saved with it. What I should have done next (see my article in Vector 7.2) was to `)CLEAR`, `)COPY` the workspace, reset the latent expression, name the workspace, then `)SAVE` again. Simple enough, I suppose, but easy to forget when one’s attention is distracted.

*Nicholas Small*
