---
title: 'Workshop: Secondary School Mathematics using APL'
authors:
- Adrian Smith
volume: '4'
issue: '4'
page: '61'
unindexed: true
transcribed: 'from page images of VOL.4-NO.4-APRIL-1988.pdf, pages 63–68 (printed 61–66); Claude, 2026-10-06'
review: draft
tags:
- conference reports
- education
queries:
- "Adrian Smith’s notes on the APL 88 Education Day talks."
- "The dates of symbols are printed “(+ - around 1489, = in 1557, |A| in 1841, and ∧ in 1933)”; the last glyph is small, read as ∧."
- "Slips transcribed as printed: “synchopated”, “Makato Kikkawa” (Makoto in Camacho’s report), “distributers”."
- "Photographs are described, not reproduced; the Education VECTOR article on APL in a Japanese high school (p.21) is in the front section, not transcribed here."
---

*notes by Adrian Smith*
{ .byline }

## The Development of Notation<br>*Neville Holmes*

This was a really effective introduction to the day. Neville was at pains to place APL in the context of the long history of notational development, from Babylonian times to the present day. He made it clear that these things take time, and that APL is just another step forward in a continuing process.

He started with the classic example of the invention of a symbolic notation (writing) around 3000BC. In ancient Babylon from 8000BC onwards, you can find scattered clay tokens. These were the ‘despatch notes’ of the time; if you sent off a consignment of goods with a courier, you needed some reliable way of ensuring that there was no ‘shrinkage’ along the way. What you did was to make an equivalent set of clay tokens (one per item) and roll the whole lot into a clay ball. This was then shipped with the goods; the receiver broke the ball and could check the tokens against the physical goods delivered.

Spot the flaw! A clever courier could just break the ball, remove the appropriate tokens, and reassemble it to match the reduced cargo. To deter this, they took to pressing matching tokens into the outside of the ball, so that the intermediary could not easily rebuild it. Some 1000’s of years later – the breakthrough!! They ceased to put the tokens in at all, and then some bright spark had the idea of just scratching the marks with a pointy stick. So was born the notion of writing.

Counting has gone through much the same pattern. The Romans used a complex set of hand signals to represent the numbers from 1 up to 100. These were transcribed into the familiar Roman Numerals, and were used, together with simple tally sticks, for hundreds of years. In fact decimal notation only drove out the tally-stick from official treasury records as late as 1826.

In both these examples, we see an evolution through:

- Rhetorical. Things have names, or individual symbols. The clay tokens were images of their real counterparts; the Roman hand signals gave the names of the numbers.
- Syncopated. The symbols are made easier to record; pictograms turn into stylized groups of lines.
- Symbolic. The whole thing is clarified into symbols which follow consistent rules and hence can be reliably manipulated. So it is with an alphabet (rather than simplified pictures of sheep), and with the decimal notation (rather than with simplified pictures of Roman hand-signals).

APL is to current algebra what the decimal system was to Roman counting, or a rational alphabet was to Hieroglyphs. It takes the notation forward from its current synchopated form to something which is genuinely symbolic. In the past, symbols have crept gradually into the system (+ - around 1489, = in 1557, |A| in 1841, and ∧ in 1933); APL is the first attempt to give consistency and coherence to a whole mish-mash of arbitrary rules.

Neville closed by just re-emphasising those dates! If we get APL accepted in less than 300 years, we have done pretty well!

## Reforming Maths Notation<br>*Howard Peelle*

Some 300+ colleges and universities are using APL. Only a dozen or so high-schools are, and few (if any) elementary schools. Yet in APL you only need to write the mathematics; other languages force you to carry so much excess baggage. Why is APL taking so long to become accepted where it is potentially most useful?

Some of the issues are:

- does APL provide you with too much? 60-odd primitives; are they too powerful? In fact does APL do the maths for you?
- is it too symbolic? There are enough ‘math-phobics’ in the world already.
- there are quite a few common ‘bugs’ in learning APL. Sometimes one symbol (such as iota) is used in two very different ways; does this cause problems?
- we all talk about ‘APL thinking’. We still don’t know what this means, or really how APL changes the way you think.
- does APL interact badly with the established world of Basic, Pascal etc?

These are things which must be tackled not only by the APL professionals, but by teachers as well if we are to see a real spread of APL into elementary education.

## Hands on

This was the fun part of the day! 20+ teachers were grouped around 8 IBM PC’s, and let loose on I-APL. At the end of the session, the copy of I-APL (complete with full documentation) was theirs to keep.

*[Photograph: a group around a PC.]* Peter Petocz explaining a point

They were helped and supported by 8 willing volunteers, who just about managed to keep their collective hands off the keyboards for the duration of the session! It was (as usual) quite hard to credit just how fast the teachers took to the systems, and indeed how little of a barrier the keyboard was. In fact by the end of the morning I was just about convinced that I-APL have got it right in going for their unique visual mapping, rather than adopting some variant of the ‘standard’ VS APL layout.

*[Photograph: teachers at a PC, two helpers standing behind.]* Education Workshop Helpers: Ian Shannon and Rob Hodgkinson standing

We broke for lunch (dragging away reluctant pupils and masters alike) and resumed with Makato Kikkawa’s splendid account of APL in a Japanese high school. As this is documented in the Education VECTOR (page 21), I shall say no more here, except to record the warm enthusiasm with which it was received. A further hour’s practice passed quickly, before we returned to the lecture theatre for Ken Iverson’s talk.

## APL in Canadian Schools<br>*Ken Iverson*

Ken has been using APL in teaching since his days as a junior faculty member (in Computer Science) in 1955. He had found traditional notation very helpful, but not adequate; hence the evolution of APL which he used for over 8 years before it was ever implemented on a computer.

In particular, the formal description of the IBM/360 (in APL) was a marvellous tool for teaching, and was indeed used for debugging the real thing! Finally in 1981 Ken was able to set up ‘a glorious week’ with 15 APL terminals and 30 maths professors. He was already moving away from computer science towards mathematics, and when he retired in 1987 he chose to devote all his time to the use of APL in maths and related subjects.

*[Photograph: Ken Iverson in conversation.]* Ken Iverson with a Visitor to the Education Workshop

In the Province of Ontario, APL was apparently given a head-start when ‘somebody sneaked it in’ to the standard offering of 5 languages on the schools micro. Are any schools using it? “Not as far as I could find out”. Clearly, easy availability of an APL system is necessary, but is by no means a sufficient condition for success. I-APL be warned!! The distributers of computer equipment are primarily in contact with the people teaching computers, not the people teaching mathematics.

For maths teachers, APL provides a coherent approach to teaching maths – not a concoction of games and puzzles as typically used to teach programming! It prevents the students escaping from high school thinking that algebra is all about letters, when it is really all about names. It is easy to learn – as is any language when you have a native speaker to help you try it out! In APL’s case the native speaker is sitting on your desk.

APL also gives you new insights, for example it makes it clear why “0 to the power 0” should be defined as 1; or why 1 is not a prime. Ken concluded with some clear advice, in part as a reaction to the obvious enthusiasm of most of the 20 teachers present: “Don’t go back and start teaching APL. Learn it first. Then teach it!”
