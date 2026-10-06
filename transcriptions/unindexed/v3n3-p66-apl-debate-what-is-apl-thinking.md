---
title: 'APL Debate: What is APL Thinking?'
authors:
- David Preedy
volume: '3'
issue: '3'
page: '66'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 68–77 (printed 66–75; an advert follows on p.76; Alan Graham’s talk follows on p.77); Claude, 2026-10-05'
review: draft
tags:
- conference reports
- APL in perspective
queries:
- "Byline printed “Reported by David Preedy”. A report of the APL86 panel debate; the quotations are printed indented, transcribed as blockquotes."
- "Names and slips as printed: “Micheal Berry”, “Adin Falcoff” (Falkoff), “mole-bearer”, “currrently”, “they they”, “the the”, “know know”, “collleague”, “prefered”, “langauges”, “ecstacy”, “an example of is how”, “a subset of ordinary APL” (thinking?), “the supporting function is to manipulate”."
---

Reported by David Preedy
{ .byline }

Howard Peelle, who acted as chairman for the session, introduced the debate by outlining why he felt that the topic of APL Thinking was an important issue to discuss at the conference:

> “It’s a term that we seem to bandy about quite freely here in the APL community and if indeed we are serious about the dissemination of APL, especially for those people who are learning APL for the first time, it seems to us that it is important to understand APL thinking ourselves.”

He then said a few words on his own perspective on the subject by way of warm-up, describing some of the work done by himself and his colleagues at the University of Massachusetts, addressing the objective stated by Robert Hooker:

> “The time is right for the psychology of programming and of APL in particular to come of age . . . we have a need to study the unique mechanisms used by APL programmers in structuring their thoughts”.

Their approach to their initial studies into APL thinking has been to study the literature and extract relevant comments; to analyse some common mistakes that beginners make when learning APL; and to think about the kinds of errors that APL instructors make while teaching APL. With this background they’ve begun a series of interviews and published a survey in Quote-quad inviting people to say what they think APL thinking means to them.

They have initiated a course daringly entitled “APL thinking” – a computer science course attracting also some people from education and from mathematics. As a result they have identified quite a number of challenges or related issues surrounding the topic; they concern questions such as the extent to which individual style affects APL thinking or, as he phrased it:

> “Do you believe that APL thinking style or APL programming style can or should be taught?”.

Despite its inherent difficulties, they are using a methodology involving asking people to talk out loud while they’re thinking about a problem and while they’re using APL to solve it.

Peelle finished off his introduction by showing a few quotes that they have extracted either from the literature or from the individuals directly about what people think constitutes APL thinking.

> “Clear, simple rules; compact notation; unambiguous interpretation; executability of mathematical statements”
>
> “APL thinking is recognising patterns, decomposing a problem and seeing where to apply APL idioms”
>
> “I know I can do it iteratively but the question is how can I do it with arrays, be it elegant or not”.
>
> “The best way to gain fluency in APL is by thinking in APL”
>
> “It is not evident that the average programmer thinks in arrays”.

Several quotes explored the ideas of visualising geometric objects and dealing with mathematical expressions.

> “Problem-solving using APL can frequently be facilitated through the use of visual imagineering”
>
> “I learned APL simply by considering how a mathematician would think”.
>
> “APL is the essence of mathematical thinking”

or, by the same speaker when pressed on the point:

> “Mathematical thinking is the essence of APL thinking”.
>
> “APL is a good short-hand mathematics”
>
> “APL thinking means ecstacy”
>
> “It’s the ability to say the same thing in several ways”

Some quotes explored the importance of modelling – structuring data rather than program flow; thinking about the problem rather than thinking about the program one’s writing or certainly rather than thinking about the machine upon which it’s going to run.

> “It involves being the black sheep in the D.P. department”
>
> “One could memorise all the APL primitives and other aspects of the language and still not be able to solve problems”

(APL thinking is what would be missing in that case.)

> “There’s a large distance between how I think of a problem and how I must write it in APL”.

APL thinking is not APL itself; it’s not what APL does; or even what APL makes easy to do. It’s what we do beyond what APL offers. It may include what we have to do to make APL fit the problem or even make the problem fit APL. Therefore APL thinking is really the complement to APL. The last quote was:

> “APL thinking – I don’t know what that is”.

---

The first panellist on the debate was Micheal Berry:

Having been involved with teams working on designing parallel computers, Berry presented the view from one who has recently moved outside the APL world to a place where people are spending a lot of time doing exactly the opposite of what those in APL think people usually ought to do, namely thinking about the details of a particular computer architecture and how to write programs that will match the way the machine works. The machine in question is a massively parallel machine called the Connection Machine which involves somewhat over 65000 processors all of which are fairly small but have their own memory and each of which has the sole option of whether or not to execute the the instruction that is sent to it from a host computer.

The problem with how to program such a machine therefore is how to design programs (and how to design a programming language in which to design those programs) in which it’s easy to make statements so that each of the little processors working independently of the others will usefully progress towards solving the problem.

> “One of the first weeks I was there, people were sitting around discussing the problem especially with the IF statement for the new language. The problem being that . . . you imagine arrays as being stored with one element in each processor and, if you had 2 arrays that you were going to add, the corresponding elements of each array would be in different memory locations but on the same set of processors and you would send the instruction ADD presumably with some pointers to the 2 areas in memory and each little processor would do its one addition, and so the thousands of ADDs would be done.
>
> “Well, they knew they needed to design an IF statement and the obvious way for it to work would be that you evaluate what they call the predicate, this being a LISP environment, basically a Boolean expression, and for all the processors in which it’s true they stay turned on and do the next thing and then they turn themselves off, and the other set of processors turns itself on and does the ELSE thing.
>
> “People were worried about the fact that unfortunately this decision-making has to happen in the front-end computer, something like a VAX or a Symbolics 3600, and a lot of time is wasted while thinking about doing the IF while the Connection Machine itself is sitting there not doing anything. I brought up an idea which seemed weird to people: ‘Why don’t you try and write the programs so there aren’t any IFs, because you would think of an instruction to say, which would do the right thing to all of the data. The instruction would be more complicated but each processor would do it and have done the right thing.’ ”
>
> “The reason I thought of that and everyone else was thinking about how to do the IF was because I had just come from years and years of thinking in APL and it seemed natural to me to try and think of a solution where even if it’s more complicated to express what you’re doing you can still do it all at once.”

They now regard suitable problems for the Connection Machine, as those exhibiting a high degree of “data-level parallelism”, meaning that you can do it all at once, such as image-processing, where each pixel can be instructed to ask its neighbours how bright they are and average with them or something like that.

Berry saw this as one angle on what is APL thinking; it’s thinking about how to find that data-level parallelism, because data is what we can structure very well in APL. He illustrated this concept with some examples.

The first was taken from a *Scientific American* article some time ago which compared computer languages by asking a skilled writer in each language to write what they think would be the normal way in their language to express the problem “Add up all the odd integers in this integer vector”. The APL solution differed radically from all the other solutions in incorporating data-level parallelism; all the other solutions involved looking at each element and asking if it were odd and if so incrementing the counter variable that’s collecting the sum, and if not going on to the next one and asking it. So in fact Scientific American had found a good example of APL thinking.

Another familiar example is the problem of rotating the lines of a text matrix to remove leading blanks. In APL, you work out how many leading blanks there are in each line and rotate by that amount; you don’t loop through the lines. Whilst each line does have to move by a different amount, you only need one expression by which to figure out how much they have to move.

Sometimes it’s hard to see the data-level parallelism because at the level that you’re looking at it the data doesn’t look quite parallel or looks ragged and here Berry showed how nested arrays have helped in letting parallelism or rectangularity be imposed at whatever level is most convenient.

Berry finished by exploring the trade-off between elegance and performance. One of the things that restricts us from really practising our APL thinking is that people look at you and say “That’s cute, but come on let’s be reasonable it’s not an efficient way to do things”. At Analogic, Berry had great fun implementing the paragraphing system using domino and realising that, while still perhaps slower than some other ways, it worked fast enough for him to use it, and he did use it in his text editor just for fun. If Berry does achieve his goal of getting a “thinking machine”, and if he succeeds as a mole-bearer and we ever have APL on the Connection machine, he remains confident it will be better to use the approaches currrently discarded on grounds of performance. He looks forward to the day when his APL thinking will not only be clear to himself and hopefully to readers, but will also be the best way to make the hardware do what it’s supposed to do.

In answer to a question, Berry explained how he felt that the Connection machine has been affected by APL. The proposed specification for the language for the Connection Machine borrows exclusively and fairly heavily from APL where the most noticeable things are operators reduction and scan. Although not called operators they they apply to a function and give you a new function that works just like APL ones. Another thing, that would also be an operator by our APL definitions for scalar extension, applies to a function and makes a function that is executed in every processor (in Connection Machine terms); in APL we would say it applies to each element of the array, so it’s either a scalar extension operator or an “each” operator of some kind. These were quite conscious borrowings and Berry found that in joining the Connection Machine team his knowledge of APL was recognised as a plus.

---

The next speaker was Ray Polivka. He started by exploring some of the premises underlying the debate. The first was that the individual concerned actually is prepared to think, and wants to think. It was an illusion to forget that many people simply do not want to think about the process they are learning.

His next statement was:

> “I don’t think there is APL thinking.
>
> “Let me say it a little differently – I believe APL fosters thinking and the type of thought patterns that it fosters are structure driven, or data driven. It allows us, if we so choose to do it, to think more like the patterns that we would like to think in. Now I’m comparing that with the patterns that are forced upon us in regular computing.”

Based on his experience in teaching APL to a whole spectrum of people from engineers, secretaries, managers and computer science trained people, Polivka had found that the problems lie with the computer science folk, because APL allows you to think more naturally.

> “What is the natural way that the computer scientist has been trained in? IF THEN ELSE I GETS INCREMENT etc DO WHILE FOR. That’s why what has happened in many cases is that the person who has come from a PASCAL trained background comes into APL and proceeds to write glorious Pascal with APL terminology.”

One of the other problems is that programmers tend to drop down too quickly to the details. If you’re going to build a piece of furniture, you don’t immediately go down to a hardware store and pick out the nails you’re going to use. You design the thing first – what shape and size you want – negotiate with your wife or husband and things of this sort. You don’t go down to the details.

And yet in fact in programming in a sequential language you are forced to go down to those details much earlier than you want to. APL promotes thinking which is:

> Algorithmic,
>
> Idiomatic – although Polivka preferred a term from psychology “chunks of APL” because you can read the statement item by item or function by function or you can see it as a chunk of APL
>
> Inquisitive – the fact that APL is executable on a machine is a great bonus and if you’re not sure what happens, you just try it out.
>
> “Multi-perspective” – meaning that there’s no one way to the solution. One of the real joys of working with APL is to come to a collleague and say “Look at the solution I have got to this problem” and he can say “Look at mine” and you find that you’ve been looking at it from two different ways.

Polivka closed by saying that APL is a notation that we need, will continue to need in the growth of our scientific and engineering development as a society and culture. APL fosters thinking.

---

The next speaker was Roy Sykes, who started by pointing out the inadequacy of the normal adjectives used to describe APL thinking – words like “modular”, “array-driven”, “whizz-bang”, “intuitive”, “parallel” and so forth. He thought those terms are inadequate. He prefered a metaphor – the metaphor of the combined architect and builder of a house, somewhat like Polivka’s furniture builder. The client, often oneself, is interviewed; the needs are assessed; the blueprints are drawn and approved; the required materials are acquired; the proper tools are brought to bear; the house is constructed; and finally some walls are shifted around, a few changes are made to better suit the client. Sykes saw APL thinking covering this broad context. It is not limited to what one does with the symbols of APL. It’s the mental process that threads throughout the entire process of defining and solving the problem.

Sykes illustrated this by going through the typical process that he typically undergoes in defining a program, a function of a modest size, not a throw-away one but one that is part of a larger system.

> “The first thing I do is think; think about what the problem is, try and understand what I’m doing. Part of that process is understanding exactly what my inputs are. This is nothing new; one decides whether one is taking character or numeric data, is it going to come in as arguments or global variables from the user at a keyboard, from files, whatever. But in any case I define that very carefully. At this point I open definition on the function, and I have the formal header, perhaps not the local variables, and perhaps 3 or 4 lines of comments describing precisely what my inputs are.”

Next he does the same with the outputs – decide what the outputs are, precisely how they are structured and ordered. He has now documented a substantial part of the function without writing any code – presuming that the header is not code.

Then he thinks about the transformations required; whether they’re structural or mathematical primarily; is it inherently a parallel or an iterative solution? Of course that is overlaid with what we can currently do in APL with the primitives available to us. This involves deciding whether to adopt a nested or a simple solution. Essentially he breaks the problem into sentence-sized chunks.

The next thing is what some other people would consider APL thinking and coding – Sykes overlays the sentence-sized chunks onto the tools and mechanisms he knows. Working in order, he starts with the APL primitives; for a structural problem he may think in terms of taking transpose, drop and laminate; for a mathematical problem he may consider the scalar primitives, ⎕divide, base-value and so on. Then he introduces the so-called idioms or chunks that are available that we all know. Thirdly he brings in the existing commonly used subroutines he has already used to solve problems. And fourth he thinks in terms of new subroutines that he might write and how they could be generalised for future applications.

The penultimate step is to lash all these chunks together trying to smooth the transition between the sentences, putting in the appropriate commas, semi-colons, periods, paragraphing, and so on – the nails of Ray Polivka’s furniture.

Then Sykes tests his code. The testing has three phases. First he assures that the proper inputs result in the proper outputs, especially on the edge conditions. Secondly he checks that bad inputs are handled properly, giving correct responses to the users, or signalling errors to the outer environment or just letting the program blow up – that’s acceptable provided that the error performance is documented. Third is testing no undesirable outputs arise, such as unlocalised local variables and so on. We don’t after all want the neighbour’s house subsiding!

Finally, the last step is incorporating revisions. He reviews the core algorithm used and removes any redundancies. The chunks have a bit of a disadvantage in that if you simply write in chunks, you may end up with a chunky program. One wants to have a smooth program, and sometimes if you look at the broader measure you see that two or three chunks put together are rather an entirely new algorithm. Sykes removes these redundancies and revises the documentation.

> “If we define APL thinking in its very narrowest sense, that of the transformations and coding, we encourage a myopic approach to problems. I teach APL and I find that the most difficult problem is not APL thinking, it’s thinking. The results are fuzzy because the inputs and outputs are not even clarified by the students to start. He or she has a very broad idea of what they want to do; they don’t know know really what they start with, and they don’t know really what they want. Once those two things are clarified, the process is simplified by APL. If we can teach people to clarify their thoughts, the embodiment of their thoughts into APL code is simplified.”

In response to a question, Sykes explained his approach when he finds he actually gets stuck in defining the algorithm. If none of his colleagues can help he puts together the very simplest, often iterative, scalar solution to solve the problem.

> “I get something that works; it may put my machine to sleep for 30 seconds but at least it works. It represents the most basic, (pun intended), solution to the problem. It works, I know my inputs, I know my outputs, and the transformation there. That process will often clarify to me what I have to do in a more parallel sense, using the APL primitives at hand. Very often, especially these days, I find myself at first thinking in terms of nested array solutions, and then backing off into simpler solutions that are almost as terse but run considerably faster using simple arrays.”

---

The final panellist was Norman Thomson. He felt that his view of APL thinking might reflect a transatlantic difference in attitude from his three co-panellists. To him APL thinking is a kind of layer that goes on outside APL; it’s the kind of things that he says to himself in order to make APL make sense.

At an earlier session Stephen Jaffe had formalised little rules – rules that are the baby-talk of APL – the things that make it easy to get it right if you are re-structuring multi-dimensional arrays. What you do is you build up a fabric of these informal rules, informal as opposed to the formal rules of APL, and that forms the basis of Thomson’s APL thinking.

He then looked at the increasing challenge presented by APL2:

> “Now, I guess that if we had reviewed this five or six years’ ago, before APL2 came widely onto the scene, we could see that we’d to a large extent exhausted the APL1 challenge – we’d begun to understand and largely control the symbols that are present in APL1. In my bookcase at home, I’ve got a book of silly ideas. I once had the idea that it would be fun to take all the APL primitive symbols, and combine them, take all the possible pairs of symbols and work out what they did together; maybe take a few triads and find out what groups of three did; explore the possibilities and see what you got, and hopefully quite a lot of them might be interesting. In a sense when you’ve done that, and you’ve filled that book, then you would know all there was to know about APL, that’s the end of it and I could then go on and study something interesting like beetles or mushrooms or something of that sort. I hasten to say that it’s a book with a lot of empty pages, but there was a point at which APL1 looked like a closed universe.”

Thomson then gave an illustration of how his existing APL1 informal rules had been affected by the introduction of APL2. He looked at the case of outer product. Intuitively there he had an interpretation; it meant extending an argument and applying a function to any string of numbers to get blocks of results. It only becomes meaningful, to do an outer product in code, when we had the “each” operator, and so it was lovely when APL2 came along and proposed “each”, because somehow it was the jigsaw-piece that neatly filled in a gap that was somehow a void in APL1.

However the other side to this particular coin had come to mind earlier in the day when an expression involving nested arrays had been displayed and Thomson had fallen hook, line and sinker for an incorrect interpretation. He had been forced to go back to first principles and even then his interpretation was rejected in discussions with others. It seems that with APL2 we have created a structure of vastly greater complexity than we ever had with APL1. Some time ago APL1 looked like being a nicely closed, nicely rounded, self-contained unity. Now with APL2, the “clear, simple rules” and “unambiguous interpretation”, so admired by Howard Peelle’s respondents seem to have evaporated. As Thomson concluded:

> “Yes it’s unambiguous, but goodness me it takes a lot of seeing to perceive that unambiguous interpretation.”
>
> “So in short that’s my perception of APL thinking – something that has radically changed between the, what now seems relatively simple, structure of APL1 and this vast relatively unexplored territory of APL2.”

---

Following the formal presentations by each of the panellists, there followed a more general discussion involving members of the audience as well. There was considerable discussion on the alternative interpretations of some APL2 idioms and whether they could be read naturally left to right, read aloud for instance so that a class can understand them.

From the floor, Anthony Camacho called on the principle of Occam’s Razor, saying that it seemed to him that the types of thinking identified as APL thinking do not appear to differ from ordinary thinking. So he was inclined to agree with Ray Polivka when he said that there isn’t APL thinking – there’s just thinking. The opposing view was given that APL thinking is in fact a subset of ordinary APL, and the debate had been concerned with identifying the specific characteristics that are typical of APL thinking in particular.

In response to Norman Thomson’s APL2 problems, it was hypothesised that he had given an example of is how APL thinking is something that he has developed. When he looked at the expression and applied APL thought to it, he didn’t get the right answer, because in APL2 APL thinking doesn’t work!

Adin Falcoff suggested that the answer to Anthony Camacho’s dilemma was that in discussing APL Thinking we are working in the context of the world of programming and so when he talks about APL thinking he is contrasting it with thinking about other programming languages.

> “I think there are some very simple and obvious differences. You tend to think in terms of transformations of arrays; you tend to think in terms of functions that have arguments and results; you tend and you learn eventually to think in terms of operators; and the consequence of this is that you learn to think of breaking your problem down in some logical way. Some of these things are present in other programming languages, but most of them are not, and certainly the others are present to a much larger extent in APL than in other langauges.”

Ken Iverson looked at the different types of approach to describing processes, or even to describe the same process from different points of view. Sometimes one wants to emphasize iteration, sometimes recursion, and there’s also the use of arrays. Then there’s the question of doing things modularly and having functions with arguments and results; on the other hand also possibly deciding things in detail. He thought that the essential thing of any good language is that it allows you to express yourself in any of these ways conveniently and cleanly and to the extent that APL is successful it is because it does that. Iverson finished with a question:

> “How much harm do you think that the people in APL have been doing and are doing by emphasising that APL thinking has one narrow notion that of arrays?”

Roy Sykes believed that we have been doing a lot of harm and asked how many times we have wasted time trying to make things faster, in particular by making them non-looping, when the first solution that comes to mind is an iterative solution. He felt that one of the biggest boons of an APL compiler is that it allows the freedom to think in ways that either are not overlaid on the primitives and operators that we have at hand, or not intuitively overlaid on them.

Norman Thomson pointed out as evidence of the distinction between APL thinking and ordinary thinking that in his own personal experience, APL had affected his life in some sense – he saw things differently once he had been shown APL. He also disagreed with Adin Falcoff’s view that the context of APL Thinking had to be programming. He felt that the one thing that characterizes APL and makes it different from other languages is that its context is a great deal broader than just programming. The revelation about APL was its relevance in the real world; that, for example, the encode function is what you do when you get change; or it’s what you do when you convert from centimetres to Imperial units.

> “It seems to me that the whole essence of APL, and the whole thing that keeps conferences like this going year after year, is the fact that APL has a spark, a bit of inspiration, a bit of something I don’t know what – the thing we’re trying to identify, I guess – that is just that much broader than pure programming.”

Adin Falcoff responded that he thought that people’s interest in it would be somewhat diminished if it were not implemented on computers – that programming should not be regarded as a dirty word. Norman Thomson’s reply was that APL was the thing that to him at least humanizes computers.

Linda Alvord explained how, as a mathematics teacher, she has a mental model allowing her to see the structure of APL as if it was the 3-dimensional world that we live in. There’s a visual aspect to the images of the data that is quite different from the way you think about it in other programming languages. There’s something about the thought process that involves image-making, and model-making, that characterizes it as different from other languages.

Ray Polivka felt that we need to encourage array-thinking. He paraphrased what Anthony Camacho had said at the Education Day:

> “Loop-thinking is not natural; more and more programmers are learning more and more on how to be baffled by parallel array thinking.”

APL isn’t the only language capable of handling collections of data – vectors, arrays, strings, etc. – but one of its other strengths is it provides the supporting function is to manipulate these things very concisely and precisely.

Roy Sykes finished the debate by highlighting APL’s interactive executability as fundamental to its nature. But primarily, he thought:

> “APL is a new vocabulary and it’s been said, by whom I don’t know, that without vocabulary, without language, thought is impossible. Language in some respects defines thought. And the language that we’re speaking of, which is APL, defines our thoughts in a much broader way, a much richer language, than any other computer language that I know of. I think the very fact that we have such a large vocabulary in APL makes our thinking process larger and richer in solving problems.”
