---
title: 'Introductory Notes; Successful Expert Systems, Royal Station Hotel, York, February 17th 1987'
authors:
- Adrian Smith
volume: '4'
issue: '1'
page: '50'
unindexed: true
transcribed: 'from page images of VOL.4-NO.1-JULY-1987.pdf, pages 52–56 (printed 50–54, to the head of the Quality Control report); Claude, 2026-10-06'
review: draft
queries:
- "The Introductory Notes introduce all three meetings of the section; the Quality Control and Graphics reports are transcribed separately (v4n1-p54, and the indexed talks from p.59)."
- "Slips transcribed as printed: “the industrialists was singing”, “APLer’s”, “a small and well bounded domains”, “reponsibility”, “have lead to failure”, “the impact on the organisation were built in”."
---

by Adrian Smith
{ .byline }

## Introductory Notes

Three meetings are covered in this section of VECTOR. The first is really nothing to do with APL, but seeing as I was there I thought that I might as well write it up! It was the Yorkshire and Humberside OR Group’s special national event on successful applications of Expert Systems.

The second is a bona-fide BAA meeting, on the subject of Quality Control in APL applications. The talks were by Chris Campen, of the other BAA (the British Airports Authority), and by Linda Kindred of Wellcome. A summary of Chris’s paper is followed by my own notes on Linda’s talk, and Anthony Camacho’s on the panel discussion which followed.

Finally we have some notes on the March meeting on Graphics, together with Dave Preedy’s paper on ‘Graphics in the Boardroom’ (See General Papers). This covered a lot of fascinating ground (Bach Canons in APL on Amigas!) with enough technical hitches to keep all the speakers on their toes!!

## Successful Expert Systems<br>Royal Station Hotel, York<br>February 17th 1987

### Introduction

This was a most stimulating and enjoyable day, in spite of the fact that APL wasn’t mentioned once! As you will see, it gives us APLer’s a good deal of hope, in spite of that sad omission. In particular it was a notable feature of the day that the industrialists was singing the praises of ‘shells’ and ‘environments’ whereas the academics were pouring cold water, and sounding some very cogent warnings.

My overall impression was that it is fine to go out and buy Crystal, XI-Plus, or whatever as a way of getting started. Before long you will either hit the limits of what the shell designer thought of, or will end up with 90% of your rules essentially fudging round the constraints imposed. In the long term, what you really need is a plug-in ‘inference engine’ which will fit naturally into your existing software, be it database, spreadsheet, or APL model.

Enough of personal prejudice . . . here is what the speakers actually said!

### Expert Systems in British Gas

*Tony Haws*

Tony began by summarizing the current position in British Gas. He felt that the key areas to watch were: strategy for implementation; effective knowledge acquisition; interfaces to existing systems; the choice of delivery vehicle. On the first point, he noted that all but one of his 6 examples were drawn from a single enthusiastic expert (3 of these had since joined the ES group). They were now technically and financially successful, but had yet to achieve ‘commercial’ success in the sense of influencing the core of the company operations.

He now described six successful systems in detail:

- ENRICH. In the entire NW region, there were but 2 experts on noisy central heating systems!! Sometimes it took 6 months for a customer to get attention, and the experts were usually reluctant to be called out to such ’trivial’ matters. The system started off on ICL Advisor at local depots. At least this cut it down to 2-3 visits by the fitter. Now Nth Thames are re-doing it on Crystal on hand-held micros for on-site use.
- Herbicide Advisor. This time only one expert, who got pregnant! Now a national system for dealing with nasties in the ponds round gasometers.
- The Stretford Process (coal gasification). All these are sold abroad . . . they often go wrong and the phone calls cost the users lots of money! Now sold with the expert diagnosis as part of the package. (ESP Advisor on IBM compatibles.)
- CORPS. Corrosion prediction in drill wells and pipes. Does a day’s work in half an hour (See VECTOR 1.3 for a paper on PATTIE . . . . Ed)
- QUAD. ICL have a 4GL called Querymaster; casual users find it hard to frame queries, so Quad helps them.
- Physical Risk Analysis. Developed as part of contingency planning to identify the risks to computers (and subsequently to more general installations) from fire, flood, terrorist attack etc. None of the dozen or so experts could co-ordinate or structure their expertise; the ES approach got them together.

In all about 20 similar systems are under way, all of the same general type. Two classes in particular look hopeful:

- ‘Real’ ES, involving high levels of skill in a small and well bounded domains. ENRICH is the archetype.
- Simple, but more general, such as the risk analysis system. The savings multiply up rapidly when you apply the same system in many places.

In both types, the design is evolutionary, and will help the expert himself to generate more knowledge.

How to deliver? Software is the key!! Shells are really for beginners, the experts graduate to ‘environments’; typically purpose built Lisp machines costing $15,000 upwards. Of course you can develop on one machine (compilation really hammers the system) and implement on another.

Knowledge acquisition . . . in many of the examples, the expert wrote the system himself (often in his spare time). This is not a long-term option, and apart from very basic Market Research techniques there is little experience here. Some pitfalls to watch for: rare events which the expert forgets; things which ‘everyone knows’; missing links in the logic.

Selling the ideas in the organisation . . . and convincing others to spend the money. Next week they are holding a seminar for 80-odd senior managers with demos of many of the above. With luck it should give an entry into the commercial heart of the business where the real money is.

### Experience of Expert Systems in ICI

*Brian Hobson*

A total of over 40 systems are in progress or in use, ranging through: technical sales; engineering design; diagnosis; business planning; operator guidance. They are all written using ‘ISI Savoir’ in which ICI have a 50% stake. After some early failures, they have achieved real commercial success from 1984 onwards. Some typical systems were:

- Wheat Counsellor. This dates back to 1984, and has changed little since. It uses ICI’s private viewdata network to access current data on wheat prices, local weather, soil conditions etc. The farmer is then quizzed about his ‘field’ and is informed of the disease risks and a fungicide is suggested (not always ICI’s!!) Some indication of cost-benefit is also given. It was initially successful, but has rather stagnated as farmers have moved to Amstrads. It is also limited to wheat (some 1200 rules); barley, oats and so on must be included if it is to attain ‘critical mass’.
- SYSLAG (lagging on pipes). Here the expert spent his last two years before retirement learning the shell and getting the knowledge into the system. Because there is a lot of maths involved, over 50% of the code is actually in Pascal exits, rather than Savoir itself. The inference is all done using Bayesian probabilities; in many cases the maths is dubious (e.g. where the options are highly correlated) but with suitable fudging of prior probabilities it appears to give the right answers! It is used 15 – 20 times per month, took 6 – 9 months to develop (mostly free), and runs in 150K on an IBM PC.
- Coater Plant Diagnosis. Latex coating on plastic flying by at 60mph! One expert, who fancied Saturday mornings in bed, supported by the plant management, who were aware of the drop in productivity whenever ‘Walter’ wasn’t around. Why not write a handbook? The ES is better for training, forces the operators to explore more options, and keeps a log for the next shift to see. This one took 3 man-months to do, and has definitely increased plant efficiency.
- Operator guidance. This schedules paint manufacture in a plant which needs running ‘gently’ and with some thought. 30 tons of ‘White with a hint of Black’ could be a problem! Here the knowledge acquisition was a problem, as the various experts shouted at one another across the conference table. At least the ES is consistent! It is attached to ICI’s ‘Auditor’ plant monitoring package to get its data; eventually they hope to feed back directly into the plant control systems.

In summary ‘Small is Beautiful’ in all the really successful cases. Wheat counsellor was an early breakthrough, but has stagnated as it cannot achieve wide enough coverage of a large domain. Of the 42 systems in progress, 5 have paid off, 10 are deemed to be successes, 5 are dead ducks, and the rest must wait and see.

### Criteria for Successful Expert Systems

*Bob O’Keefe (University of Kent)*

This was a talk with a difference! Bob very briefly outlined a system for screening graduate applicants in a major accountancy firm. Not surprisingly the details were confidential . . . the criteria for screening 2,000 applicants for 200 jobs are not likely to become public knowledge. Instead Bob concentrated on the reasons for success, and gave us his (deliberately controversial) list of the most common reasons for failure.

First the reasons for success:

- A willing and enthusiastic ‘knowledge Czar’ with a very definite ‘I am right’ attitude. His considerable input of time was worth more than the cost of consultancy, hardware and software put together.
- Flexible software. ESP Advisor lets you out into Prolog when the going gets tough. The system could not have been done quickly and cost-effectively if they had been ‘locked in’ to a shell. They needed ‘a programming tool, not an imposed paradigm’. Typical symptoms of the latter are systems with 3,000 rules; 2,900 of these are probably getting round the shell!
- A simple approach to uncertainty. Bayesian inference really is an absolute nightmare! They used simple ‘what’s A worth against B’ comparisons to establish a set of weights; these were then simply combined to give an overall score.
- Validation. This took more effort (60% of the total time) than knowledge acquisition and building. Random batches of 20 – 30 applicants were run through the system; when these all checked OK, they looked for the real extreme cases and pushed it to the edge of past experience.
- User interface. It takes a lot of care to get the questions in a sensible order! Users are bothered by some ‘Y/N’, some ‘Enter number (1 – 3)’ and so on; everything was set up as a menu option to avoid this inconsistency.
- The needs of the user came first. It is quicker and simpler to use the system than to do it by hand. It guides them through the task – maybe this should have been put in a handbook 20 years ago; these days it is easier to put it in an ES.
- the impact on the organisation were built in. The system gives a better and more consistent recruitment policy, and the reponsibility can be taken lower down the structure.

Some elements which have lead to failure in other systems:

- the ‘consultative mode’. The system asks all the questions, and does all the reasoning. You sit there and say ‘Y’, or ‘0.35’ and so on. Attempts to use ES in financial planning have been a disaster for this reason … here the use of ‘critique mode’ works much better. The expert has a first go at a plan and the system criticises it. Of course many shells embed ‘consult mode’ in the shell structure!
- Imposed methods of handling uncertainty. We just don’t know how to do this, and should stop pretending that Bayes and Fuzzy logic are any sort of a solution.
- Shells. If you have a hammer, you see every problem as a nail. If you have a Backward-chaining Bayesian Inference Engine . . . . . In the US they are moving back to ES environments (e.g. CitiBank have spent $10M on Lisp machines) rather than using shells.
- Poor validation. ‘It never got implemented, but it’s a useful training tool’. This translates as ‘we couldn’t check its answers’. If you haven’t got documented case studies, or an independent expert, you are in big trouble.

In general, ES are moving fast towards being ‘bottom line’ benefits, rather than just nice toys. Either someone is making better decisions, or lots more people are making good decisions. This is all well and good, but has anyone a clue as to how we should measure the results quantitatively? The DSS people have been trying for years; will the ES fraternity do any better?!
