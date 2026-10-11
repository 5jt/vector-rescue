---
title: ASL - where have we got to and where do we go from here?
authors:
- Tony O'Hagan
volume: '8'
issue: '2'
page: '49'
unindexed: true
transcribed: 'from page images of VOL.8-NO.2-OCTOBER-1991.pdf, pages 53–57 (printed 49–53; within The Random Vector, after Gregynog 91, the last piece in The Random Vector); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- development practice
- APL community
queries:
- "A discussion paper for the third ASL Conference at Gregynog, introduced by the unsigned note “Gregynog 91” (unindexed/v8n2-p49-gregynog-91.md)."
- "Kept as printed: the heading “Not doing everything that the last minute”; “how to we get goodwill”; “than we did do”; “They are what drives us forward”."
---

*by Tony O’Hagan*
{ .byline }

As I step down from the ASL Management Team, I thought it might be useful to take stock of what has and has not been achieved so far with the project. This may help to set priorities and realistic objectives for the future.

What have we got? By the time of the third ASL conference, we should have formally released the first three volumes. Although they are late in coming, their actual release is a landmark in ASL. We must ultimately leave it to others to judge how good they are, but I believe they already form a very useful set of tools for any statistician. Volume 1 gives us a valuable collection of basic calculations. Even I sometimes want significance points of standard distributions, or want to calculate a correlation matrix, and having those functions so conveniently to hand is great.

Volume 2 gives me a really good toolkit for building graphs. They are much quicker and easier to use than the basic low-level graphics functions supplied with most commercial interpreters, but much more flexible than the high-level suites of ‘presentation graphics’ functions that are often also provided. Of course, you cannot use Volume 2 yet if it is not yet implemented for your graphics system, but that is a good reason to call loudly for an implementation or port to your system (or do it yourself!).

Volume 3 gives me a very powerful system for linear and generalised linear models. Many statisticians will need nothing more.

I think that we can be proud of what has been achieved so far, so if I now go on to dwell on what has not been done it is not meant as a criticism. The fact is, one can always do more and better. It is easy to focus on the ‘more’, which in ASL terms means starting on new volumes, but it is useful to think a little about the ‘better’ - how we can improve on what we have done.

## Programming Standards

We set out with high ideals. ASL was to set the standard for statistical work in APL. Functions would be well designed, well programmed and well documented. I think we have achieved the first of these, because in my opinion the functions are well designed. We have not achieved the other two.

I know it is difficult to say what constitutes good APL code, but I am pretty sure that very little of what we have done would satisfy the best professional programmers. I know this to be a fact for Volume 2 because I wrote most of the final version! It was my first attempt at using second generation APL features in a serious application, and I am sure that I must have used them badly in many places. Alan Sykes would not claim to write consistently good APL either. Like me, he has learnt a lot through ASL, but Volume 3 grew out of a much older workspace, and probably looks patched and messy to any professional programmer. We talked about publishing our code, as part of ‘setting the standard’: with the current versions that would be unwise! It is debatable whether we should really try for good code, or settle for code that works. What should we do with future volumes?

## Documentation

We also hoped to produce good documentation. A standard was set for internal documentation by comments. It was never written down and enforced, and I am afraid that under pressure to produce Volume 2 even this fell by the wayside. Did Volumes 1 and 3 manage to get this part right?

Documentation also means user manuals and technical manuals. This is something else that slipped through lack of time and manpower, but if ASL is to succeed it is vitally important. I believe that we must set as a high priority the production of high quality documentation of Volumes 1 to 3, in a consistent ASL-standard format, and that this must be maintained for future volumes. It is no good having good software if nobody can understand how to use it.

We also planned a book to introduce non-APLers to doing statistical analysis with ASL. This is a very big nettle that I believe must also be grasped. We know what we want to do; we even have a major publisher interested. But who will write it? And will it be done soon enough to be of any use?

## The Library

ASL was expected to grow so big that good management tools would be needed for any user to draw into the workspace precisely the functions needed for the job. A Working Party was going to develop these, but did not deliver. As it happens there was no real urgency because ASL is not yet that big, but that is not a satisfactory view. We designed the functions carefully and we should design the library and its management carefully from the outset. Otherwise we will end up with volumes that need major revision to fit whatever format is ultimately chosen.

We talked endlessly about naming conventions and even appointed a ‘custodian of names’, but he was never given any names to take custody of! Who knows whether we have made any blunders? I know that in Volume 2 there is an odd hang-over from earlier conventions in the use of ASL as a prefix to names of global variables, but not as a prefix to function names. There was simply not enough time to resolve this.

## Implementing WAGS

If Volume 2 is to be of any real value, a high priority must be its implementation on as wide a variety of systems as possible. We have a Dyalog PC version that works on screen and outputs to some printers, but is not tested on other printers because we did not have them available. We have an APL\*PLUS PC version that works on screen with the (obsolete) `⎕G` graphics but is not reliable for output on a printer. That is all. We do not need to do the development work ourselves if vendors are willing to take on implementations for their own systems. But we should take the lead in positively encouraging them to do so. Then what do we do about the ones that we know will not yield to that persuasion?

## Future Manpower

I have spent some time on saying just how Volumes 1 to 3 fail to deliver at the level of our early high hopes. In thinking about the future of ASL, we should ask why. The reason is that wonders were achieved with the available resources, but the available resources were inadequate. Each one of the three volumes was developed by one or two dedicated people in their spare time. The work they put in dwarfs the input of any other person in ASL. Again, I am not really criticising. Whereas it was clear that without their efforts there would be no software, the effort of other people was always more marginal. Our working party on Standards and Implementation did relatively little not because of a lack of goodwill, but because the software could be produced (and was produced) largely without them.

So there are two manpower issues to face. How do we get new people to develop whole new volumes (particularly if they can guess how much work the first three entailed)? And how to we get goodwill to turn into a comparable amount of time and effort from those whose involvement is more peripheral? A lot of what I have said about the shortcomings of the current offerings revolves around the failure to bring forward this second kind of manpower - and make no mistake, this is just as important as getting in people to write new volumes.

We also need to decide whether we can make better use of a specialist programmer than we did do. Perhaps we were unlucky in the ways things worked out this time, but I have my doubts whether such a programmer can ever play a big part in the original development of a volume. There may be a compensating case, however, for a specialist programmer to come along afterwards to add any internal documentation, ensure adherence to standards (when we have them) and improve coding.

## Not doing everything that the last minute

One thing is clear, software always ends up with a frantic rush to deliver by some date. No matter how many times the delivery date is postponed (which is usually somewhere near infinity) there is always a last minute rush. In fact, the more postponements it has had the more bouts of frantic effort the poor finished product will carry the scars of!

Therefore we cannot expect the refinements of good documentation, thorough testing and good coding to be put in at the end. Either they are built in all the way through or they will not be there at the first release. I have a suggestion - we should try hard to build in these refinements all the way through but, when we inevitably fail, we should plan for an early second release in which they are all there.

So, give Release 1 of Volumes 1 to 3 a few months to find the main bugs, then go full ahead to give Release 2 all the good things that I have said they lack at the present. Now is the time to recruit an experienced programmer to work on that. Now is the time to get the Standards and Documentation teams up to speed.

## Some final words

I am sorry I could not be at Gregynog this time. I hope to be involved with ASL in the future, through a continuing interest in Volume 3, as a user of ASL and perhaps as a contributor to new volumes. I would like to see ASL go from strength to strength, still trying to set ‘the standard’. Although lofty ideals must always be compromised in practice, let us not lose those ideals. They are what drives us forward.
