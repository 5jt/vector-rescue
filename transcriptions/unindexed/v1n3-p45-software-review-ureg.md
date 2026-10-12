---
title: 'Software Review: U-REG (User-friendly Regression)'
authors:
- Teresa Jones
volume: '1'
issue: '3'
page: '45'
unindexed: true
transcribed: 'from page image of VOL.1-NO.3-JANUARY-1985.pdf, page 47 (printed 45); Claude, 2026-10-12'
review: draft
tags:
- reviews
- mathematics and statistics
queries:
- "Printed heading “SOFTWARE REVIEW U-REG: (User-friendly Regression)”. Printed 46 is a MetaTechnics advertisement (“MetaPack.. EVERYTHING YOU NEED FOR APL ON THE PC”), not transcribed."
---

*by Teresa Jones*
{ .byline }

This is a regression package supplied by UFSS who are associated with the Applied Statistics Research Unit at Kent University. It is written in APL and can be run on a mainframe or a PC with an APL interpreter.

The package is easy to use - one can merely type `)LOAD UREG` and the package itself will tell you how to proceed, with extra help if required in answer to ?, HELP, or SOS. The standard prompts can be cut to a bare minimum as one becomes used to them, and answers to questions can be stacked if you know what is coming next.

Data can be input manually, from an APL matrix stored elsewhere, or from one of UREG’s own rather idiosyncratic data files. This is reasonably flexible, although if you already have a standard filing system it would be nice to use that instead.

## Helpful

From a statistical point of view the package is very helpful. You are given ideas and hints on sensible things to try, such as the suggestion that you should visually explore your data to check for unlikely values. It also reports such things as sequential ordering of data and possible qualitative observations.

The package then leads you on through different stages (which can be bypassed using NEXT) allowing you to transform your data if necessary. It then calculates a regression equation on those variables you wish to include; all the usual statistics are available. If your equation did not give a particularly good fit UREG may suggest that you transform one of the variables, for example to use the log of it, and try again. On completion all the data is automatically saved.

## Presentation

The presentation of the results is not quite as good as the content - as our VSPC system has no ‘offline’ facility we are limited to simple screen hardcopies, or a printed log of the whole terminal session. There are also some problems when many columns of data are being used; the results are not neatly formatted, but wrap round making it difficult to extract the required information.

The amount of data is restricted by the system you run on. To get results on a ‘large’ (530 observations on 37 variables) data matrix around 700K of workspace is required to avoid WS FULL problems.

## Summary

On the whole we are pleased with the package despite its idiosyncrasies, and we hope to make good use of it. It is possible that some of the functions could be tailored to suit us, and UFSS seem fairly happy for us to do this. Of course we may then encounter problems as new releases of the software arrive! The package is very usable in its own right as long as you don’t expect it to slot in too neatly with everything else at your installation.
