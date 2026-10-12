---
title: Dyalog APL for 386 DOS PC's
authors:
- Jonathan Martin
volume: '6'
issue: '1'
page: '61'
unindexed: true
transcribed: 'from page images of VOL.6-NO.1-JULY-1989.pdf, pages 63–64 (printed 61–62); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
queries:
- "Contents line “Impressions: Dyalog APL for MS DOS”; the printed heading is “Dyalog APL for 386 DOS PC's”, “reviewed by Jonathan Martin”."
- "Printed 63 carries only the GENERAL ARTICLES section introduction, not transcribed here."
- "Kept as printed: “on an PC-AT”; “lets just say”; “It now becomes much more viable at this speed” (no full stop)."
---

*reviewed by Jonathan Martin*
{ .byline }

## The Reviewer

Let me put my cards on the table first. I've been an APLer for over 6 years, most of which was spent using APL\*Plus under VM/CMS. However, for the last two years, I have been using Dyalog APL, both on an PC-AT with a go-faster Unix board in it and, for the last twelve months, on an IBM RT-6150 (all to myself!). Consequently, I was a little unsure of "going back" to good old DOS and its single-tasking environment.

My testing was done on a Compaq Deskpro 386 with 4Meg of memory, running at 16MHz. I had hoped to fully test it on an IBM PS/2 model 80, running at 25MHz as well but time caught up with me.

## The Product

As I'm sure many of you are aware, Dyalog APL has been around for a number of years now but, until the release of this version, it was available solely for the Unix/Xenix world. I'm not sure exactly how many Unix machines it is available on - lets just say Dyadic are experienced at porting it... It is a true second generation APL with all the features you would expect - nested arrays, defined operators, error trapping, file system etc... but a lot more to distinguish it from the other APLs around.

## The Review

The hardest part about doing this review is that I am used to using Dyalog - I spend most of my day working with it. Constantly, during this review, my feelings were that I was just using Dyalog APL. Now that may sound stupid. Yes, of course I was using Dyalog, there wouldn't have been much point in the review otherwise. What I mean is that it is just like the other versions of Dyalog I have used.

It was quick - that was something that you notice immediately. Starting up APL and loading a workspace takes three to four seconds. As far as benchmarks go, we have one at British Airways that is a solution to the Eight Queens problem. It is very typical of the work we do - lots of boolean matrices being thrown around, data being expanded to a common form and then compressed down to get the results out - Queens on Dyalog under DOS ran only about 15% slower than it does on my (old) 6150.

A major enhancement to Dyalog that, while not brand new (it has just appeared in the current release of the 6150 version), is certainly worth talking about. It is `⎕SM`, the new screen manager. Under this version, they have introduced something called Screen Memory Mapping which, while I do not claim to understand how it does what it does, transforms `⎕SM` from being just a superb method of managing and updating the screen to a superb and extremely fast facility. If you have only ever used an AP124/6 type interface and have longed for those flashy PC-style front-ends, then want no more. `⎕SM` gives you all that and more and in such an intuitively APL-like way.

Useful things like pop-up windows become trivial and selection bars and "buttons" need only a few minutes coding. You can also do a hundred and one other things with it. Try your hand at Othello, again written using `⎕SM`. Simple animation was one thing that was just about possible using the 6150 version. It now becomes much more viable at this speed

Two tests that I wanted to do on this version were to port two very different workspaces down. I must say porting is a bit slow at the moment but given that it is a job that is done once and once only, I can live with it. The first workspace was something I had knocked up quite quickly - a simple database with update/delete/edit facilities. It isn't particularly well written - the sort of thing that everyone writes for themselves and assumes that no-one will ever see. I had two minor problems with it under DOS. Firstly I had written it for 12 PFkeys - this particular set-up only had 10 of the twelve accessible. Moving 'quit' from PF12 to PF10 resolved that. Secondly, the line-drawing characters had been stripped out of the BOXTM function that decorates the help message. Again, only a minor irritation. Apart from that, no problems.

The second workspace was much larger (about 300 functions) and is one that had been moved from APL\*Plus under VM to Dyalog about 18 months ago. It is a text editor with facilities for moving text around, inserting and deleting lines, formatting text and drawing graphics characters. The two problems mentioned above obviously occurred here but nothing else. I had effectively moved an application from a Unix machine to a DOS machine with only minor problems. Very impressive indeed.

There were certainly one or two bugs in it - this version is a couple of months away from being released yet - but nothing that appears dramatically difficult to solve. In fact, one of the bugs (excessive use of the cursor keys causing the APL to hang) generally manifests itself whilst playing the version of Othello that they have written for `⎕SM` (I was just about to win as well, honest).

## Conclusion

This new version looks and feels just like the other versions of Dyalog I have used. I'm sorry to go on about it, but that is the over-riding impression that comes out. Personally, I like the multi-tasking features of running under Unix and the ability to be doing more than one thing at a time. However, there are many people and many companies who do not like Unix for one reason or another or who are bound by company loyalties and budgets to stay with DOS. This version could well be the answer to those people.

If you want to know what is happening to APL, get hold of a copy of this.
