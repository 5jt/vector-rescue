---
title: Too Much Diversity in APL?
authors:
- Joseph De Kerf
volume: '12'
issue: '1'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.12-NO.1-JULY-1995.pdf, pages 9–10 (printed 7–8; within Correspondence, the first letter); Claude, 2026-10-11'
review: draft
tags:
- implementations
- standards
- APL in perspective
queries:
- "The writer’s postal address, printed after his name at the end of the letter, is omitted."
- "Kept as printed: “Kimmo Kekäläinen”; “I am feeling myself very comfortable”; “confidence on behalf of the potential newcomer”."
---

*From: Joseph De Kerf, 10 April 1995*
{ .byline }

Maybe the two most important events on the APL front in 1994 were the implementation of control structures in Manugistics’ APL\*PLUS and the implementation of namespaces in Dyadic’s Dyalog APL. Personally I wasn’t waiting for control structures: I am feeling myself very comfortable with the goto of APL — the unconditional and conditional branch (→). On the other hand, their implementation neutralizes the objection of some opponents of APL who claim they reject APL because it doesn’t support such control structures. A very important innovation, however, is the introduction of namespaces. Eric Lescasse for instance described it as the first step to Object Oriented APL. As such, it was a very good idea of *Vector* to devote a special feature section on the concept, containing three papers respectively by Peter Donnelly, Eric Lescasse, and Kimmo Kekäläinen (*Vector* Vol 11 No 3, pp 65-95). With increasing astonishment however, we read the guest editorial on the concept by Duncan Pearson in the same number of *Vector* (p 3). He states: “Whatever Manugistics produce I hope that it is different from the Dyalog implementation.” And he goes on to say: “So let us have as many different, independently conceived, approaches to this problem as there are interpreters.” Maybe this is true for experimental implementations, but definitely not for official commercial releases: we are killing APL in that way.

Indeed, APL is a living language, but a strong handicap for its future is the diversity of its implementations. When in 1973 shared variables were introduced, only a few implementations took it over. Other implementations for instance added the possibility to treat component and native files by implementing an appropriate set of system variables and system functions. In 1991, based on a study of about eighty commercial implementations, I published two inventories, containing a list of about eight hundred system variables/functions in use at that time. A lot of them are synonyms, although more or less different in their implementation details, and a lot of them are homonyms providing totally different facilities. And the proliferation still continues. In the meantime, generalized arrays or arrays of arrays were introduced, in some implementations based on the grounded array concept, in most implementations based on the floating array concept. But even those who used the floating array concept did it in different ways. There are about ten implementations which support the so-called Extended APL for the moment, but when a software engineer wants to design portable software, he can only use the defined facilities of the APL Standard ISO 8485. He can’t even use arrays of arrays. All this not only confuses the declared user of APL, but also doesn’t inspire confidence on behalf of the potential newcomer, and is one of the most serious obstacles for the future of APL. So, let us try to ameliorate the situation rather than making things worse. But I am afraid we are preaching in the desert.

Joseph De Kerf
