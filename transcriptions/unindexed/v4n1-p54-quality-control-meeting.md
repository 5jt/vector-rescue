---
title: 'Quality Control in Application Development, 20th February 1987 at the Royal Over-Seas League'
authors:
- Adrian Smith
- Anthony Camacho
volume: '4'
issue: '1'
page: '54'
unindexed: true
transcribed: 'from page images of VOL.4-NO.1-JULY-1987.pdf, pages 56–61 (printed 54–59, to the Announcement; the Graphics meeting follows on p.59); Claude, 2026-10-06'
review: draft
queries:
- "Campen’s talk is “Summarised by Anthony Camacho”; the rest are Adrian Smith’s notes (see his Introductory Notes, v4n1-p50). The Introductory Notes credit Camacho with the notes on the panel discussion; the page does not say so."
- "The panel discussion is set as a two-column list of speakers’ initials and remarks; transcribed as a definition-style list with the initials in bold."
- "Slips transcribed as printed: “the absolute right to refuse to any system”, “throught the development cycle”, “there role has broadened”, “everyone is there own inspector”, “Myers book”, “2 day’s work”."
---

by Adrian Smith
{ .byline }

### Introduction

This was one of the most interesting and valuable meetings I can remember for a long time. The idea of getting a ‘view from the outside’ was a brave one, and (in my view at least) came off very well indeed.

Chris Campen gave us his view, from the position of Information Systems Policy Manager at the British Airports Authority. Linda Kindred followed up with the perspective of someone whose job it is to maintain (rather than create) systems in a wide range of languages.

### A Formal Approach to Implementation

*Chris Campen (British Airports Authority)*

*Summarised by Anthony Camacho*

Chris defined the quality of an information system as fitness for its purpose. To design a fit system large jobs are divided into many small tasks. Quality control includes standards and reviews of work in stages. Each small task must have well defined objectives and targets. There should be regular monitoring. Work must be checked by people controlled by different managers. The users should check that specifications are met when each milestone is passed. Anyone affected by the work or with an interest in it should be allowed to participate.

The planning is thus the key and includes everything; the membership of the teams, the allocation of other resources, the standards, the frequency of various checks and reviews, the fallback and safety procedures to protect the business.

Quality control cannot be imposed because to succeed the whole team has to believe in it. When imposed everyone goes through the motions and the quality control work adds to the load without giving a commensurate benefit.

The big problem is how to change the attitudes of the staff so that they welcome such things as walkthroughs by independent assessors. The right attitude will work with inferior standards whereas no standards can save a project when the staff have the wrong attitude.

### QC in the Systems Development Cycle

*Linda Kindred (OR/Appl Support at Wellcome Foundation)*

The strategy at Wellcome has been to separate ‘maintenance and firefighting’ out from systems development, and to keep a body of expert programmers and analysts in the ‘applications support’ department. Around 18 people are responsible for some 80 systems, comprising 2,500 programs. Of these 300-400 are APL based.

Linda has the absolute right to refuse to any system which fails her standards of quality control; in the past this has meant bouncing systems at the implementation stage, but the emphasis is now on imposing strict standards of quality throught the development cycle.

Just what is the development cycle? In the beginning there is the Budget. This used to be based on last year’s usage; it is now based on agreed business requirements for the coming year. Priorities are thrashed out with the users as necessary. From then on . . .

- all work is project based. The project manager is the user. Project management techniques (networking etc) are provided by MS where required.
- one or two levels of working party are set up, again chaired by the users. MS and Internal Audit would normally sit on these, and they would meet monthly to review the network. Each ‘activity’ would always have an ‘owner’.
- there would be ‘terms of reference’ to outline the scope, risks and limitations of the project.
- costs are approved stage by stage. There is no attempt to quantify total project costs at the beginning; the staged approval gives you the chance of killing projects after (say) an outline design phase.
- no fixed implementation date is set. Instead everyone must sign off the system (including Production Support who could force a re-write on the grounds of resource usage).
- the Post-implementation review (say 6 months later). What went wrong (and why)? What went well (and why)?

Applications support were traditionally only involved at the final stages. However in recent years there role has broadened (especially on major projects):

- they are represented on the working parties, with the particular role of checking the interfaces.
- they provide an inspection service to the analysts, programmers and project leader.
- they are the ‘custodian’ of the standards. These are all held on line on PROFS, and are used to log the benefits of past experience as well as being a rule-book for development.
- they have the QA responsibility. Clearly they are committed to this, because it is very much in the interests of the maintenance programmers. Call-outs used to average 2 per week; now 1 per month is typical.
- if you have quality from the beginning it is free. Systems are no longer bounced at implementation.

So what are their standards, and where do the benefits come from?

- Applications Support won’t take on any system which ‘ABENDS’ 3 to 5 times per month, or takes a day’s maintenance per month.
- the split between development and maintenance (at the budgeting stage) makes it quite clear to management just where the costs are coming from. It makes it much easier for the development phase to hit budget!
- changes and fixes are kept in a system log. In the long term this is used as evidence for re-writes.

The basic long-term aim is to ensure stability in the supported systems, and to free resource for urgent changes rather than basic maintenance.

Questions from the floor . . . .

What is an Abend in an APL system? When the workspace goes down and it takes you half a day to re-create the problem!

What about systems on PCs? This has hidden itself under the carpet, but managers are beginning to realise what they have got themselves into.

Who would be a typical ‘user’ on the working party? Definitely the senior guy, often a divisional manager.

What motivates the project teams to follow the QA standards? They will finish on time, within cost. You always get those who don’t; their annual review reflects it, and they don’t get the plums next time around! (Some have even been known to get ‘special projects’.)

Is there a development team for APL? Lots of it was done in OR; this has been cleaned up and taken over. Some small APL developments have been picked up recently as confidence in APL maintainability has begun to increase.

### Panel Discussion

*Dave Parker (in the chair), Les Hollingbery, Adrian Smith, Maurice Jordan, Linda Kindred*

**DP**
: In the Electricity Council they use Delta to standardize conventional program development, with an in-house front-end. This leads to a common style of code across all applications, and he has followed this with his APL methods. Basically this means standards for function, variable and label names, and a base of common utilities.

**AS**
: At the 1985 OR conference, there was an excellent talk from Nissan-UK, where it was emphasised that there are no quality control inspectors in Japan! Quality is built in, not inspected in! At Rowntrees we think we now have a APL community who have been trained from the beginning in ‘the right way’ of doing things; no-one would ever think of using shared variables, or using files other than through cover functions.

    Change control: for big systems there is a formal procedure for scheduling changes (e.g. to ensure 2 related changes go in separately). Each workspace has a text variable called RELEASE where programmers leave a log of what was changed and why.

    For mainframe APL it doesn’t matter all that much if it stops . . . usually no-one else is hurt, and you can often fix it ‘on the fly’. PCs are a different matter, and delivered systems must be much more robust.

**LH**
: Les supports Information Centres at Rank Xerox. APL systems were very much ad hoc, but have now settled down and stabilised. They are looking at LOGOS from IPSA as a way of getting control over development and change. Xerox use a ‘total quality’ approach where everyone is there own inspector. He recommended Myers book for general advice, and a ‘belt and braces’ approach for critical systems (i.e. self checking software).

**MJ**
: Quality certainly matters on things like the reservation system (a 3-hour down time could lose the MD his job!); in APL they encourage the use of tools and common utilities, but not all systems conform. They suffered from an ‘explosion’ into APL (0 – 30 APLers overnight) and the undisciplined approach this led to. MJ is personally responsible for some 2,500 functions; few of these give him trouble, and he is trying to understand what the differences are.

**Qn**
: Do you use passwords and locked functions to protect code?

**AS**
: In the old days )SAVE was our file system. This is still OK for personal systems, but now we try to separate the code (typically on project libraries) from the data (on files on the user’s own ID). We try to avoid knowing other people’s passwords for routine maintenance!

**DP**
: They do much the same; he owns the workspace and the user owns the data.

**General**
: Beware the input stack!! At least with APL2 you can turn it off; it is not a safe substitute for a file system.

**Qn**
: How do APL systems compare on reliability?

**LK/MJ**
: Historically, APL has caused more trouble

**LH**
: When an APL program goes down, I have a lot less paperwork!

**AS**
: You sometimes discover a fault years after the system was implemented (e.g. a missing quote in an error message). However the real problems are caused when the system gives wrong answers, but doesn’t crash!

**MJ**
: A big APL system went into parallel running after 6 man-years; most of the discrepancies were faults in the original system (unnoticed for years).

**Lusmore**
: A random-number generator was once left in a sales commission routine for 6 months before anyone spotted it!

**Qn**
: Does this conflict with the idea of fast development?

**MJ**
: Things that should have taken a day’s thought and 2 day’s work often took weeks when rushed into!

**AS**
: Sit on your hands for half an hour! Don’t let the user (whoever he is) rush you into designing at the keyboard! Let the computer find the SYNTAX ERRORS by all means; it is up to you to find the DESIGN ERRORS at your desk.

**LH**
: There is always the danger that APL will encourage you to tackle things which are beyond you.

**Qn**
: APL may do things fast, but what kind of documentation should you do?

**DP**
: Even if you document the functions, it is hard to document the methodology. Where possible get the user to do it for you.

**AS**
: Most of the ‘user guide’ should be on the screen. Similarly the system documentation should be in the WS; e.g. an active data-dictionary which logs the types and descriptions of variables as well as driving the editing functions.

**Camacho**
: First write the manual; second write empty (commented) functions; third fill in the code.

**MJ**
: It is surprisingly easy to read other people’s code. Good APL is really just the specification expressed in a mathematical notation.

**Cyriax**
: Often it is hard to comment adequately in English; quite often you slip into APL, particularly when describing function arguments.

**Lusmore**
: Good comments are hard to do; often they look alright until you try to use them!

**AS**
: APL doesn’t let you do good layout. Compared to Pascal or PL/1 it is a typographic disaster area! You can only comment on separate lines; you can’t indent; you can’t leave blank lines or spaces in the middle of lines. Try reading someone else’s Pascal if all these visual cues are taken out!

**MJ**
: Perhaps the most valuable documentation is a collection of sample inputs and outputs for functions.

**Camacho**
: Use meaningful names, not daft standards like ‘L1:’ for labels.

**AS**
: Often the choice of local names tells me who last changed the function.

### Announcement

Linda closed the meeting by telling us about a group called the QA Forum which meets quarterly to discuss issues related to QC in systems development.

It is an independent body, and costs £300 pa, with a fee of £85 per meeting attended. The members are able to get specific topics on to the agenda, and workshops are held to help with particular problem areas. The collected papers from each meeting are circulated to all members, who are generally people involved in day to day QA work.
