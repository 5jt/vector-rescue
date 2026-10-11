---
title: Security? What Security?
authors:
- John Sullivan
volume: '5'
issue: '2'
page: '85'
unindexed: true
transcribed: 'from page images of VOL.5-NO.2-NOVEMBER-1988.pdf, pages 87–88 (printed 85–86; within Technical Correspondence, the first letter under the section heading); Claude, 2026-10-11'
review: draft
tags:
- development practice
- implementations
queries:
- "A letter in Technical Correspondence, From: John Sullivan, 20th July 1988. It has no signature; it is followed by his “Sharing GDDM pages between APL2 and Fortran” (unindexed/v5n2-p86-sharing-gddm-pages-between-apl2-and-fortran.md)."
---

*From: John Sullivan, 20th July 1988*
{ .byline }

I am becoming more than a little concerned about the way APL implementers seem to imply that passwords in filing systems and function locking give security to an APL system. The truth of the matter is that there is no such thing as APL security, and any impression that there is gives a dangerous false sense of security to those who decide to rely on it. The only way to ensure that your APL programs and data are safe from prying eyes is to use the security systems that you use for your other programs and data, and if you haven’t got any other security systems you ought to start looking for one.

If security is non-existent, what is the point of function locking? This question is even more relevant when there are well-known (but undocumented) ‘unofficial’ ways of unlocking locked functions which range from the exceedingly handy (APL\*PLUS/PC) to the inconvenient (mainframe APL2). Even more, if you don’t have a function unlocker, but you have the knowledge of the workings of APL that can be gained from talking to a few technically-minded people or from reading a few technical reports, you can write one in a reasonable time that will work well, even if it is not the best way of doing the job. For example I have recently written a 17-line function in MicroAPL’s APL.68000 for the Atari ST that will unlock locked functions; the research required to write this (which also involved deciphering the APL component filing system) took me about 24 hours of non-continuous work, and also gave several side-effects which may well prove profitable in further research.

So, function locking is a waste of time when it comes to security. What is function locking good for, then? Well, you don’t want your users to get confused when your functions crash because some condition has occurred that you didn’t program for (sooner or later this will happen to you!), so locking functions and allowing the error to be dealt with further up the stack seems a reasonable idea (this idea is already incorporated into IBM’s dyadic quad-FX, with a feature to allow unlocked functions to be non-suspendable). To help with this, why don’t the implementers give you a facility for easy unlocking of locked functions? I can think of two ways of doing this, those implementations that use quad-lock could also use quad-unlock, and of course, what is wrong with using del-tilde for opening function editing for a locked function?

I have heard some people say that functions are locked to protect the secrets of their algorithms. Having unlocked a few functions written by other people in my time I am not at all surprised. The only APL functions that you don’t want people to look at are the ones that you are ashamed of. If you genuinely have a super new algorithm that you don’t want people to copy, why don’t you supply the function to the users in machine code? Most APL systems have facilities for calling machine code, and machine code usually runs faster than APL, so use it.
