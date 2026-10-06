---
title: Report on the Plenary Panel Session at APL 86
authors:
- Anthony Camacho
volume: '3'
issue: '2'
page: '81'
unindexed: true
transcribed: 'from page images of VOL.3-NO.2-OCTOBER-1986.pdf, pages 83–87 (printed 81–85; APL86 Quotes follows on p.86); Claude, 2026-10-05'
review: draft
tags:
- conference reports
- language design
queries:
- "The contents list calls this “Implementations of Enhanced APLs”, Anthony Camacho."
- "Names as printed: “Luan Thompson” (Thomson in the photo captions)."
- "p.83: the take example is printed “So if EH > 2 3 4 5ρ of something then the shape of a 6 ^ EH is 6 3 4 5”, the relation and the take glyph garbled by the typesetter (perhaps “EH ← 2 3 4 5ρ” and “6↑EH”); transcribed with ↑ for the caret. Bob Bernecky’s wish is printed “⎕FX < ⎕ prime < ⎕CR <function name>”, < being Sharp APL’s enclose."
- "Slips transcribed as printed: “occasinally”, “caentate laminate”, “so that the work bring benefit”."
---

by Anthony Camacho
{ .byline }

“The Differences Between Implementations of Enhanced APLs”

Jim Brown was given the largest round of applause of the whole conference when he said “I want to go on record today as saying that I’m also convinced that Ken [Iverson] is correct in his direction for extending APL”. When the applause died down he continued by asking us not to jump to conclusions: there is more than one correct way to extend APL “and all it means is that different reasonable people that have different objectives in mind can come to different correct conclusions . . .”.

The full transcript of the session took seventeen pages: I will therefore summarise drastically to leave room in Vector for other things. Please forgive me if I leave your question out or misrepresent what you said: I’m sure the editor will be glad to publish your comments.

Jim Brown offered to talk about nested arrays (and the reason why an enclosed scalar was still a scalar), vector notation (and to maintain that there is no function left out between the elements of it), and to explain brackets (which people complain are neither function nor array nor operator).

The fundamental change that APL2 makes is to extend greatly the extent to which the shape of the data can control the work that functions and derived functions will do. There is no need to learn all the rules. Nearly always the simple view of the way things will work is correct; for the occasions when it isn’t it’s probably simpler to insert brackets than to go into the theory of the syntax which explains why. But there is a unified theory, thanks to Phil Benkard, and it is correct. If the brackets are occasinally redundant, who cares?

John Scholes said that Dyadic’s objective was to enhance APL to make it more useful for writing commercial systems by adding error trapping, component files, commercial format, and a wide variety of system functions. Unix was chosen as the operating system because they foresaw its growth in popularity. Dyalog APL has floating arrays like APL2 and is written in C for portability. It has an excellent UNIX interface so programs written in C can be taken into an APL workspace and called just as if they were locked functions. All the features of UNIX are available from within APL. The design of Dyalog APL closely follows STSC’s NARS and John gave credit to Bob Smith “Most of the ideas in there are Bob’s”.

James Wheeler said that the correct origin of NARS is Nested Arrays Research System. From 1979 it was used as a test bed for new language design ideas. In 1982 STSC had chosen the enhancements that had proved most effective in the eyes of the APL community and these are now part of the APL\*PLUS/1000 product. STSC also realised that APL needed to be enhanced in other ways to make it easy to use; it needed better editors a user interface with screen control and it needed ways to overcome speed limitations. These are the aims which have guided the people producing implementations on micros and the APL compiler.

James felt that the great debate about axiom systems is over and that the positions taken by the major vendors are now fixed. The set of all possible arrays in APL\*PLUS/1000, Dyalog and APL2 is now the same. STSC do not yet have defined operators, selective specification and a few of the less frequently used new primitives. The great range of system functions has made shared variables unnecessary and there are some features that STSC have which APL2 lacks. One he recommended for Jim Brown’s attention is the partitioned enclose which has proved very popular with the users. There are some differences in the way bracket indexing works that ultimately he would need to settle with Jim. In short there are some differences still but STSC is converging with APL2.

Luan Thompson explained that although he has been working in machine code on the Motorola 68000 for some years and with APL for four years, MicroAPL only took control over the 68000 interpreter six months ago and have spent the time since mainly in optimisations for speed. As the interpreter is written in machine code its natural targets among small machines are the QL, Atari, Macintosh and Amiga. On enhancements MicroAPL feel that there is already a dominant vendor in the APL market and that they are not going to try to buck the trend. There are already a few features such as dyadic grade in the interpreter and there are hidden features in it which they believe will be able to handle nested arrays, although these are not at present available to the user. Luan said he believed that the enhancements to user and system interfaces would probably be more important than enhancements to the language. APL competes in a market where BASIC, Pascal, C, and FORTRAN all have multi-window WIMPS (window, ikon, mouse and pop-up menu) interfaces and better editing and error control. MicroAPL will enable programmers to write WIMPS applications which nobody can tell use APL. The main problem is that these features are different on every machine which makes it a lot of work, but MicroAPL think it is worth while to make life easier for the programmer.

Bob Bernecky said that the Sharp philosophy is to make enhancements simple, consistent and general. The more complexity the harder it is to teach and learn and use (and complexity also affects the implementations). Bob too would like to see APL2 and Sharp APL converge and suggested that STSC and IBM might like to consider ‘link’ and ‘rank’ which would help them converge.

Link does the same as strand notation (Bob asserted that strand notation complicates syntax analysis) but because it is a function you can apply an operator to it. With the rank operator you can link say matrices or vectors from two arrays. There’s no obvious way to do that in APL2 because there’s no function for an operator to work on. [Alan Graham interjected that one of his idioms did the trick.]

The benefit of the rank operator is apparent when you look at the bracket axis notation it replaces. In APL2 bracket axis gives rise to many special cases; the definition of ravel takes several pages because of the different ways that things in brackets can affect it. When Ken Iverson and Arthur Whitney proposed the rank operator Sharp realised that brackets had been inconsistent from the beginning; caentate laminate, rotate, reduction all are affected by brackets in different ways and each has to be learned separately. The rank operator
replaces the bracket axis notation and applies identically to all functions, even user defined functions. Furthermore if the rank operator is made more efficient it will make every function that uses it more efficient, whereas the brackets would have to be improved one use with one function at a time.

Consistency brings benefits; Sharp had a minor but uninteresting enhancement to take or drop – if the argument shape was a scalar or one element vector and less than the rank of the right argument then the result has a shape of the same rank, defined by the left argument catenated onto the remaining shape of the right argument. So if EH > 2 3 4 5ρ of something then the shape of a 6 ↑ EH is 6 3 4 5. Combined with the rank operator this can be made to yield results of shape 2 6 4 5, 2 3 6 5 and 2 3 4 6 as well. So you start to see some synergy between the enhancements and the ISO APL.

Sharp is trying to put APL back into the mainstream of data processing and this won’t be done by language enhancement but by improving the environment. Sharp are providing a consistent interface which will allow any language to drive APL or an APL function to drive programs written in any language. They are also building special purpose interfaces to all manner of peripheral equipment and a network shared variable processor which enables a user to share a variable with a user in another city or with a PC and it still looks just like a variable in the program.

A lot of Sharp’s work has been to improve large applications with hundreds of users so that the work bring benefit to many people. Now they have signed a co-operation agreement with STSC and hope that this will enable them to do more in the micro field. Bob would like to see ⎕FX < ⎕prime < ⎕CR \<function name\> allowing you to edit a function using the operating system’s full screen editing and agreed that the latest things like WIMPS had to be available with microcomputer APLs.

Philip Goacher then called for questions; below is a brief summary of the main discussion.

Alan Graham endorsed the rank operator: when he first heard of it he put it into his workspace as a defined operator and nowadays even has it defined with its own symbol so that he doesn’t have to begin every new workspace with )COPY UTILITIES RANK. He has set his students the exercise of writing all the Iverson operators in APL2 and although there are one or two tricky ones he believes he has correct versions of all of them. Anthony Camacho asked whether he would circulate his code, saying “Send it to Vector and we’ll publish it” and Alan replied “I’ll do that”. He also said that he very much regretted brackets and wished that the fathers of APL had never put them in. Bob interjected that the rank operator made brackets redundant.

This exchange stimulated Adin Falkoff to come to the stage to defend brackets. While he was trying to get enough ink out of a dead pen to put his name on the overhead projector he was asked whether he originated the acronym APL. He confirmed that it was his idea. Adin maintains that there is a good use for bracket-semicolon notation and that is to pass multiple arguments explicitly. He too endorses the rank operator and doesn’t wish to defend every use of brackets. By passing arguments explicitly you avoid having to box things together which have a merely contingent association and also avoid having to unpack them inside the function before using them. You can also leave out an argument between two semicolons with the same meaning as in ambivalent functions. He seriously recommended this extension as consistent with all implementations.

Jon McGrew, speaking personally and not for IBM, thought that we were now stuck with brackets, which people find convenient and easy to learn. Jim Lucas questioned the notion that the divergence in APL was a bad thing; progress is achieved by experimentation and competition and perhaps APL will get superseded by a language which will not have to carry on old mistakes as APL has to.

Neil Mitchison disagreed with Jim Lucas, and felt pessimistic about APL’s chances of wide acceptance if it continued to diverge. He asked what the panel thought should be the role of the ISO in this. Should they create a compromise standard which went over to one side for some things and to the other for others? Jim Brown said that he felt that the Standards Committee were right not to put files into the standard because there wasn’t enough agreement about their form and he would like to see the standards committee sticking to the description of agreed usage. There are wide areas of this; everyone has the same definition of dyadic upgrade and of complex numbers and of replicate. Neil was not satisfied with this and asked what should be done about features where there was no agreement and the versions were incompatible. Jim’s answer in effect was that those features should be left out of the standard.

Anthony Camacho asked about the size of the interpreters, saying that he wanted to run APL on microcomputers small enough to take into school or give to children to use at home and that the size of the interpreter determined how far down the market it could spread. James Wheeler said that the size depended on the machine. The STSC interpreter is written in C and when compiled varies from about 200,000 bytes on a Vax to about 400,000 bytes on the PC; unfortunately larger on the machine where less space can be afforded. He looked forward to cheaper machines with larger memories which would allow enhanced APLs to be run in schools. Luan Thompson said MicroAPL is about 95,000 bytes varying by plus or minus 10,000 bytes according to machine, and that there will be four megabyte memories available before you can blink. Bob Bernecky said that the Sharp PC interpreter was essentially the same as the mainframe version but even with all the bells and whistles it only took 400,000 bytes. He reckoned that each 30 months the capacity of chips was quadrupling and agreed that long term there was no problem about memory size. When prodded by Adin Falkoff he said that the naked interpreter was about 250,000 bytes. John Scholes said that Dyalog APL is also written in C and also varies. Originally (on the Z8000) it was 200,000 bytes with all the frills then available. The decision on enhancements is always to take more space to gain speed and the current version, on say a Stride 68000 based machine, is 400,000 bytes. Jim Brown asked David Selby what the size of the PC APL was and David said 70,000 plus the auxiliary processors. A quite adequate set can be put together and run in a 256K machine. David added that he didn’t agree with the ’memory will be cheap’ argument, saying that we should not expect the user to pour hardware in.

Chris Brady wanted APL to be less greedy of mainframe capacity: his employer seemed likely to cut its APL workforce because of this effect. He also asked when he could see code, variables, the stack and the state of the filing system all on the screen at once. Luan Thompson replied “As soon as I’ve finished the version for the Atari: that is exactly what I’m working on”.

Linda Alvord returned to the problem of getting APL into schools. Her main point was that education authorities and heads of school departments who might consider APL will be put off by the choice of versions since they did not have either an International Standard or any agreed consensus to guide them. If you go to a supplier and say ’I want to buy a standard APL’ nobody has one for sale. Everybody tries to sell you the special advantages of their own version and the consequence is that people decide to wait until the question is settled by another mechanism. She felt that there should be a standard APL which everyone could buy safely and that the enhancements were not of much value in secondary schools. These comments brought a big round of applause. Roy Sykes called out that the ISO Standard version should be available for forty five bucks and that was obviously accepted by general acclamation too.

Comment by reporter:

Philip Benkard called attention to the great applause for Jim Brown’s opening remarks and I would like to do so again.

It shows the strength of feeling in the APL community that regrets the differences between enhanced APLs and wishes to see all APLs converge.

APL used to have the advantage that you could write and test programs on a microcomputer, benefiting from micro editor and response time, and then download the program to a mainframe. Nowadays it would take great self discipline to stick to ISO APL and even that would not work with APL2. And it would take great dedication and unusual opportunity to get to be at home in all versions of APL.

This diversity is not in the APL user or programmers interest. It arises because each vendor wants to offer something better than the others and which, if possible, commits their customer to them.

I believe a powerful alliance of users could and should apply pressure on vendors to converge and perhaps this could be done by persuading the ISO to set a standard for enhanced APL which does exactly what Neil Mitchison suggests above.

Anthony Camacho  
2 August 1986
