---
title: What’s New for 1985? (organiser’s report and selected highlights)
authors:
- Dick Bowman
- Adrian Smith
volume: '1'
issue: '3'
page: '62'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 64–68 (printed 62–66: two pages of captioned photographs, Dick Bowman’s report on p.63 and Adrian Smith’s highlights on pp.65–66); Claude, 2026-10-03'
review: draft
tags:
- implementations
- APL community
queries:
- "Two pieces printed under one event, set as H2 sections. The photographs (half-tones of the exhibition) are described, not reproduced."
- "The caption ends “1 0 1\\APL[2 1]”, an APL joke: `1 0 1\\'PA'` gives `P A`, two of the three letters; printed so."
- "Slips transcribed as printed: “Somes APL people”, “Panos Anagnostopolus”."
---

## Photographs

*[Photograph: Richard Nabavi at the MicroAPL stand.]* Richard Nabavi minding his QLs.

*[Photograph: three men at the APL People stand.]* Somes APL people (two out of three anyway). Tim Perry and David Alis on station. 1 0 1\APL[2 1]

*[Four photographs: the I.P. Sharp stand, delegates over coffee in the foyer, a bookstall, and the E&S Associates stand.]* As the afternoon wears on, delegates take their chance to buttonhole the exhibitors, to visit the bookstall, and to enjoy a quiet cup of coffee in the foyer.

## What’s New for 1985?

*Organiser’s Report by Dick Bowman*

Awakened from my reverie on Thursday 6 December by the delicate plop of mail in the intray and pleased to find therein an invitation by someone who’d prefer to remain nameless (they’d offered to teach me APL a few weeks earlier) to come along to the “What’s New for 1985” show on Monday 10th. I’d rather thought I might go anyway, but it’s always nice to find someone cares.

What we’d set out to do with this show was part of the Association’s quite deliberate policy of moving APL away from the introspective ghetto of talking only to ourselves and creating an image which meant that only APL converts would want to be there. So goodbye to the basement room of Imperial College (home of past incarnations) and to the shanty town of corrugated cardboard stands which we’d become accustomed to. The rather plusher surroundings of the Regent Crest Hotel beckoned, we bit the bullet of substantially increased costs of running the show (or, more accurately we bit our lips while our bold exhibitors decided to pay the substantially increased costs).

At the end of the day we had a very fine-looking exhibition (and if I single out I.P.Sharp Associates and Dyadic Systems as particular contributors to the visual excellence it is only in recognition of the degree of extra work which their ‘permanent stands’ represent); we also had a programme for the day in which Product Forums ran throughout and a fair smattering of new products (the accompanying photographs and reports will tell you more).

Attendance was very respectable at around the 100 mark (plus stand staff, representing the diehard core of the Association); we signed up 17 new members and had the opportunity of reminding a few more about all the money they still owed us. As always, we’d have liked to see more and can reflect on the qualitative difference between 100 people all sat down in one room at once and the same number of people strolling in and out throughout the day. Personally (with a degree of bias) I felt that there was ample opportunity actually to talk to the exhibitors and that the whole day was one in which everything was relevant - unlike certain other cattle markets of the computing exhibition industry.

In the longer term, we intend to continue providing the mixture of the more usual technical meetings and this sort of more overt commercial occasion. With APL86 coming closer we can look back on this event and the Loughborough exhibition as giving grounding in the important matter of putting together an attractive and professional show. No doubt there will be some commercial event organised by the BAA between now and 1986; quite what format this will take we haven’t yet decided.

Finally, I feel that it is important to recognise that putting on events like this is more than a one-person effort and in addition to the efforts of the exhibitors I would like you all to recognise the sterling services of David Allen and David Preedy (Product Forum chairmen and vendor chasing), Roy Tallis and Panos Anagnostopolus (for their ability to extract money from ex-nonmembers), Phil Goacher and Neil Truby of the BCS for their advice, experience and guidance. If I appear to have omitted Stan Wilkinson and Dominic Murphy of the Activities subgroup this is only because we jointly felt that their non-involvement would be a clear indicator of there being no possibility of any conflict of interests (Stan’s degree of participation in kicking off the Product Forums overshadows all of us, of course).

## Selected Highlights

*by Adrian Smith*

### Gareth Brentnall (APL\*PLUS): Compiler Support for APL

Oddly enough the compiler is written in APL! There have been numerous attempts in the past to allow some kind of partial APL compilation. This is the latest, and sounds as if it may be close to success. The effect of compiling functions is almost invisible to the user; essentially they behave just like locked code except for a possible speed-up of between 3 and 10 times. However there are (as there had to be) a good many snags, and I cannot see it ever being a cut-and-dried decision to compile code routinely.

Firstly if you want maximum benefit from compilation you really need to DECLARE (shades of my PL/1 days) all your local variables. Secondly compilation has no effect on transactions with files or other auxiliary processors. In my experience this is where the majority of looping occurs in APL, and would have been an area where compilation could have paid very big dividends.

Thirdly the actual compilation costs you an arm and a leg, so you really do need to be hammering the CPU before it pays. Of course you also lose the instant error diagnosis, as the line numbers no longer exist. Clearly you would need to keep a parallel ‘debugging’ copy of everything just in case of disaster.

However having said all that, there are clearly people who need to solve FORTRAN-type problems (Linear Programming, Simulation etc.) in APL, and anyone who is doing this kind of thing may find that partial compilation is just the service they need.

### Richard Nabavi (MicroAPL): APL on the Sinclair QL

As far as I know this was the only talk to get a spontaneous round of applause at the end! Richard began by musing on the unpleasant question of why, if APL is so wonderful, is no-one using it?! A slight exaggeration I know, but not too far from the truth once you start looking at schools and the home computer. He felt that the three outstanding reasons were:

- Price. The hardware is all well above the top end of the home market, and the APL itself is not cheap in these terms.
- Off-putting appearance. Richard quoted one QL user …

    “Since starting to use QL/APL, I have become convinced that the conventional character set was just an elitist trick to restrict the spread of an immensely powerful language”
- Non-standard peripherals. There are all sorts of horrid snags as soon as you hook up APL to normal off the shelf devices. For example negatives turn up as ‘@’ on HP plotters. Cost is another penalty of being out of the mainstream; an APL VDU will set you back some £750, compared to £350 for a standard version of the same device.

APL/QL is an attempt to take these issues full in the face; in other words to produce a cheap APL, running on a normal keyboard, with no peculiar hardware requirements. How well MicroAPL have succeeded you must judge for yourselves; in general I found the choice of keywords quite effective, but was rather distressed by the refusal to allow ‘ = ’ for assign (if you’re going BASIC you might as well be hung for a sheep as for a lamb!) and by the ambiguous use of ‘-’. I suspect that the first time user who gets a SYNTAX ERROR with ‘3-2’ might have cause to wonder about the supposed consistency of APL.

Fast and cheap it certainly is. In a very brief encounter with a QL I found it very speedy indeed; nearly half as fast as top-line systems like the SAGE, and a lot quicker than the IBM PC. Even the microdrives may prove less of a disaster for APL than for other languages, after all we tend to )LOAD everything into memory and rarely need to venture outside the confines of our nice comfy RAM until lunch, when a quick )SAVE is all there is to it.

At £99 (VAT included) you can’t go far wrong (assuming you already have the QL!). Even with £200 on top to get a reasonable workspace, this really does look like a mass-market product for the first time in the APL world. No wonder it drew such an enthusiastic response from the biggest audience of the day.

### John Ward (APL\*PLUS): APL\*PLUS for UNIX

Again this attempts a partial compilation, this time automatically on the first pass through each function. John claimed a speed-up of around x2.3 on subsequent executions. It allows access to standard Unix drivers from within APL (for jobs like setting up the keyboard), and maps the APL system commands, such as )LIB, to the Unix directory structure.

### Neil Macmillan (APL\*PLUS): APL\*PLUS Release 4.0

This is covered in detail in ‘News from Sustaining Members’ so there would be little point in my saying more here. The talk was received with considerable interest, and the idea of using APL\*PLUS on the IBM PC/AT obviously excited many of the audience.
