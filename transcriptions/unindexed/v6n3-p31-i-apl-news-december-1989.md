---
title: I-APL News - December 1989
authors:
- Anthony Camacho
volume: '6'
issue: '3'
page: '31'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, page 33 (printed 31; within The Education VECTOR, after art10009580); Claude, 2026-10-11'
review: draft
tags:
- implementations
- APL community
- education
queries:
- "Within The Education VECTOR, after Alan Sykes’s “From Coin-tossing to the Weather” (art10009580). The next page (p.32) is the I-APL Ltd order form, dated February 1989 (part, price and addresses), a house notice not transcribed here; “APL90: Accepted Papers” follows on p.33."
---

*by Anthony Camacho*
{ .byline }

## News of the Apple Port

I hear from Rolf Levenbach that he was able to load and save a workspace on the Apple for the first time on 12 December 1989! He also has a cursor (which I had not even realised was a problem). Now we have to produce documentation and do Beta testing. While that is going on we may be able to produce some workspaces to give access to the Apple machine facilities. Won’t it be marvellous to be able to release another port.

## A Traditional APL Keyboard for I-APL

F. D. H. van Batenburg of the Dutch Group has been working to produce the traditional keyboard - as for the golfball typewriter, and has done everything except the ALT key combinations. Paul is finding out where in the code the ALT key is captured and then we will be able to offer a patch which will enable professional APLers to demonstrate I-APL without getting lost looking for backslash-bar.

## Large Workspaces

We have been asked to provide access to more memory on machines such as the Archimedes and PC clones which usually have half a megabyte or more. There doesn’t seem much sense in doing this without removing limitations which were also part of the drive to save space in 8-bit machines such as BBC and Apple. For example we want transcendentals accurate to more than seven places and better floating point precision.

Paul Chapman and Dave Ziemann are therefore looking into the question to decide which is the best way to enhance I-APL to provide a 32-bit version. What enhancements do you think we should include? The candidates so far are: LEV and DEX, lower case names, the RANK operator, long direct definition lines, increased accuracy/precision (either longer BCD or IEEE), keyboard enhancements, FSCREEN access to attributes and several technical improvements which should result in shorter or faster code.
