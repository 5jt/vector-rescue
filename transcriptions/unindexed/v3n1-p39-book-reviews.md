---
title: Book reviews
authors:
- Paul Chapman
volume: '3'
issue: '1'
page: '39'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 41–42 (printed 39–40); Claude, 2026-10-12'
review: draft
tags:
- reviews
- programming techniques
queries:
- "Printed byline “reviewed by Paul Chapman”. Two reviews: “The APL Toolkit, published by CIPS APL SIG, First Edition” and “FinnAPL Utility Library, published by FinnAPL, First Edition”."
---

*reviewed by Paul Chapman*
{ .byline }

## The APL Toolkit, published by CIPS APL SIG, First Edition

In the preface, the editor Richard Levine describes the book as the result of efforts by the Canadian Information Processing Society’s APL Special Interest Group (CIPS APL SIG) from 1983 to 1985. It must also be said that he admits that the book is not yet finished, but a second edition will be forthcoming with the last two sections completed, based on feedback from the APL community.

The book is organised in six chapters. The first two provide a general introduction and a guide for the use of the book. A directory of functions grouped under categories follows, and then the functions themselves. Finally come the incomplete chapters, documenting the categories and the functions respectively.

The functions presented range from development tools (name list, function documenting, timing, etc.) through general programming utility functions (looping, timestamp formatting, the ubiquitous BOX, etc.) all the way to application functions (e.g. mortgage amortisation).

The function listings themselves reveal a healthy smattering of comments, and a refreshing avoidance of “one-liners”. All functions are claimed to be standard-conforming and independent of global system variable settings, except, in the latter case, where dependence is natural (e.g. where the global setting of the index origin is used to produce a result containing indexes). Each function should, according to the introduction, contain a standard set of comment lines at the beginning, listing the function category, author, timestamp, version and example. Some of the lines are unfortunately missing from many of the functions, and where they are present the advertised format is not always adhered to.

The functions themselves are listed alphabetically. This seems to be a hangover from the way functions are listed in the active workspace. I cannot see why this is a better way than listing them in different sections according to category, especially in this case where each function belongs to just one category. An alphabetical index is very easy to produce, and presenting functions by category allows the reader to compare the different approaches available to solve his own problem. Much of the detail seems to have been machine-produced, and the on-line version of the utilities workspaces said to contain functions which directly support the idea of categories; so it would seem to have been easy to print the book in sections like this.

My major criticism of the book is the incompleteness of the last section, where the individual functions are documented. Of the 115 functions listed in the book, only 16 appear in this last chapter. Were the functions presented in a machine-readable form, my objection would be less, since one of the oldest (and still one of the strongest) APL maxims around would apply: if in doubt, try it out. However, most of the more interesting functions are more than 50 lines in length, and typing one of these in only to find that it doesn’t quite do what you wanted could be a frustrating exercise.

The one thing that caught my eye in this otherwise straightforward book is a method for defining local functions inside functions, using comment lines whose second character is a single digit defining which local function the line belongs to. Where it is necessary to write monolithic utility functions which can be easily copied from workspace to workspace, this is the clearest way I have seen so far of presenting local functions.

The book is not easy to use, but some of the functions in it may well make it worth obtaining. Many of the functions have been introduced as similar system functions on some APL implementations, but where portability is a concern the book could be very useful.

## FinnAPL Utility Library, published by FinnAPL, First Edition

No individual credits are given in this book of APL utility functions. The brief introduction explains that the book comprises the 101 most important functions in the “Special” workspace of the Finnish APL Association, FinnAPL.

The introduction also refers to the “widely accepted standard” of underscoring the last letter of each function name. I don’t know of this standard, but I assume its purpose is to avoid name conflicts between utility functions and application functions. However, if it were to become “widely accepted”, it would defeat its own purpose, since all publishers of utility functions would conform to it, and thereby introduce name conflicts between different sets of utility functions from different publishers. A better approach would be to start each function with the letters “FINN”, or some such, to identify the origin of the function.

Apart from the one page introduction and four pages of contents, the book consists simply of one function per page or two. The functions are grouped alphabetically within categories. The categories themselves appear by name in the contents pages, but are not mentioned thereafter. No full alphabetic function index is provided, which would be a simple and useful addition.

The documentation for each function is consistent and well laid out. Its name and purpose are given, followed by its calling syntax. Then there is a detailed description of each of the arguments and the result, with some additional informal comments. One or two clear examples follow, and finally the function itself is listed. Where a function needs to call other functions listed in the book, their names are listed explicitly.

Many of the functions will be familiar to readers of FinnAPL’s excellent idiom book. Some of the function lines tend towards the obscurity of those one-liners, particularly in their length and their use of embedded assignment. This is quite unnecessary within a function: an extra line or two spent in clarifying the inner workings would be well spent.

No independence from the global environment is claimed, but I suspect from looking at the listings that this is achieved in every case.

This is a most attractive and useful book. Its layout is excellent, and the functions themselves form a consistent set of utilities. Apart from adding an index, all I can suggest by way of improvement is: more please!
