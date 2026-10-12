---
title: 'Editorial: Reliability of APL Systems'
authors:
- Jonathan Barman
volume: '7'
issue: '1'
page: '3'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 5–6 (printed 3–4); Claude, 2026-10-12'
review: draft
tags:
- development practice
- APL in perspective
queries:
- "Kept as printed: “a hackers language”; “crystalising user's ideas”; “the APL prototype system becomes to be viewed as the final system”."
---

*by Jonathan Barman*
{ .byline }

Are APL systems less reliable than systems written in other languages? There was some dismay at the last Vector working group meeting when I indicated that this was the topic of my first editorial, because it looked as if I would be knocking APL. Whilst I think that many APL systems are unreliable, I do not think that this is necessarily caused by APL. A programmer's ability to produce reliable code seems to be much more important than the programming language being used.

APL is a superb language for quick, off the cuff, solutions which are to be used by the writer and no one else. This is the major factor which contributes to the impression that APL systems can be unreliable. However, the impression can be equally true of any language that is superb for quick, off the cuff, solutions - but which language falls into that category? Do you expect quality systems from Lotus 1-2-3? You can get both brilliant and rotten systems written in any language you care to name.

APL is also excellent for writing large quality systems. However, moving from a small quick solution to a quality system is much more time consuming than many people realise. Unless one has had the bitter experience of bugs coming back to haunt one, it is quite difficult to appreciate the care, time and trouble that goes into getting a system right. Time means money, and a quality system is going to be expensive.

Big companies producing major systems keep statistics of the number of errors encountered at the various stages of a product's life cycle: during development, during formal testing, and when the product is in the field. These statistics are compared with some measure of the size and complexity of the code, so that trends and performance can be assessed. I am not aware of any such statistics having been published in the APL world, so I have no hard facts to compare APL with other languages. Perhaps someone will write and tell us what is available?

In the absence of hard facts one is left with perceptions; it is easy to see how APL can get a bad name. For example, supposing there is a key business problem which requires a quick solution: someone creates a solution in APL, and it turns out to be really useful. The system is gradually extended until it is quite large - the users of the system are in the same department as the author, and when something goes wrong it can be fixed immediately. Eventually the author leaves the department and the users are left in the lurch when the system crashes, the DP department is then expected to get them out of the fix.

Exactly the same scenario happens with Lotus, Basic etc., however the problems are not normally quite as bad. The sheer power of APL allows really significant systems to be developed which would be quite difficult to achieve in other languages.

Another charge made against APL is that it is a hackers language. To some extent this is true, but I am not sure that it does or should matter. APL makes it easy to try out ideas. For some reason the trial and error approach is seen as a bad thing, unless you call it prototyping. There are many aspects to this problem; producing code without proper thought leads to stupid errors, time spent at the design stage is usually very worth while but can be overdone. How does one achieve a balance?

Searching for a solution to a problem is a very personal and idiosyncratic thing. Some like to mull over the problem in the bath, others like to bash away at the keyboard to try and generate ideas. Nobody can say which is best! APL allows, and even encourages, the latter approach; the risk is that it is possible to find an APL solution which works with the examples given, but which fails in the general case. Hackers find an apparent solution and barge in and change the system without a second thought. Suffice to say that they tend to produce poor quality systems, but hackers often produce the beginnings of useful systems which would never see the light of day in the traditional DP environment.

Prototyping is very helpful in crystalising user's ideas. It is quite extraordinarily difficult for a user to specify a large system in the complete detail needed by the programmer. Knocking up a sample system which can actually be used is where APL scores. However, there is usually an extreme reluctance to go back and rewrite any code that is working, so a prototype very often ends up as the final system, with only relatively minor changes. Sometimes the APL prototype system becomes to be viewed as the final system and when it creaks at the seams APL gets a bad name. In some ways the special prototyping languages score over APL in that they force a rewrite. At that stage all the proper things can be done, like writing the user manual first, and getting the initial design right.

In conclusion, I think that the reliability of APL systems is no worse than those written in other programming languages, but that sometimes APL gives the impression of being worse because of its power, speed and flexibility.
