---
title: I-APL Newsletter No 7, October 1988
authors:
- Anthony Camacho
volume: '5'
issue: '2'
page: '23'
unindexed: true
transcribed: 'from page images of VOL.5-NO.2-NOVEMBER-1988.pdf, pages 25–28 (printed 23–26); Claude, 2026-10-12'
review: draft
tags:
- education
- implementations
- APL community
queries:
- "Contents line “The Latest on I-APL” (the Education Vector’s own contents list: “The Latest I-APL News”); the printed heading is “I-APL NEWSLETTER No 7 / October 1988”, with the byline “by Anthony Camacho, Old World Chairman of the I-APL project”."
- "The Contents page gives page 26; the newsletter begins on printed 23 (supplement page 7) and ends on printed 26. The Contents line’s page is corrected to 23."
- "Following the project rule for individuals’ contact details, the street addresses of Anthony Camacho (the writer, listed as a sole consultant in the Product Guide) and of Alison Chatterton (given for the BAA Software Library, c/o her) are omitted; I-APL’s order address is kept."
- "Kept as printed: “We are very grateful to Vector to Alan Sykes”; “Zdenek V Jizbas” (later “Zdenek V. Jizba”); “Tama Traberman”; “microbee”; “APL◇385” (printed with a diamond)."
---

## I-APL NEWSLETTER No 7<br>October 1988

*by Anthony Camacho, Old World Chairman of the I-APL project*
{ .byline }

### Thank you Vector and the APL Association

The Education Vector including this newsletter is being mailed to everyone on the I-APL mailing list as well as being included in Vector. We are very grateful to Vector to Alan Sykes and to the British APL Association for doing this, as it enables I-APL to keep people informed.

The I-APL mailing list is over 1400 names and addresses and about 500 of these live outside the UK. The cost of mailing to all these people is too high to do it regularly whether there are new products or not, just to keep everyone informed. There are new things coming. We don't have them yet but we hope they will be in stock by the end of November. If you send an order it will be acknowledged at once but the goods may take until Christmas. We are hoping that the APL Association will include I-APL news regularly in Vector so that instead of starting an I-APL users magazine we can encourage all APLers to take an interest in the other uses of APL. If this can be agreed then I-APL will cease to issue newsletters and ask everyone to join the APL Association to keep in touch.

### Delays!

We were hoping to be able to issue the BBC B version of I-APL in May and then we revised this to September. We still haven't issued it and now we are hoping for November 88. The problem has been (is) that we feel it would be very foolish to give people who haven't yet met APL, an I-APL product which does not give them access to the colour, graphics and sound which are such attractive features of the BBC machine. Any reviewer would find such a product unattractive. We want APL to be as attractive as it can be to those meeting it for the first time.

Those of you who have seen the Beta test version will know that the access given through the operating system to colour graphics is very slow to use because it makes one or more operating system calls per pixel. Alan Mayer is now writing a program which takes a complete array as the right argument and does a PLOT with each row of it. I am glad to give Beta test versions of I-APL/BBC to anyone with a BBC who feels able to do some machine code work and produce a workspace giving access to any BBC facility (even the joysticks!).

### Version 1.1 of IAPL.DEB and I-APL/PC

Paul Chapman has finished version 1.1 of I-APL. Paul has also done a new version of the PC port. This has some extra facilities and a new workspace of machine code functions called FSCREEN. This workspace gives full screen control.

Another facility is to use the operating system to write the screen (invoke I-APL with I-APL/D). Doing this makes displays slower but allows near-compatibles or software-only compatibles to run I-APL without locking up, losing or permuting the display. Version 1.1 maintains a character buffer of the current screen and so WGET and WPUT (get or put characters into a window) are really very quick. People had written to us about many problems with their CGAs and EGAs and this option allows even the Nimbus PC to run I-APL. The new version also drives an EGA properly.

### All Known Bugs Cured

Porters are encouraged to ask me for the IAPL.DEB file for version 1.1; it cures all the known bugs in version 1.0. There were only a few, including these: the result from a scalar left argument to encode was reversed; there was a fault with )PCOPY; the results from tangents of over ninety degrees sometimes had the wrong sign; and the result from domino of negative one was negated.

### Availability

Version 1.1 of I-APL/PC will be available (disk only) in December from the BAA software library. You cannot get the books from them. The software library doesn't handle any paper. The address to write to is:

> The BAA Software Library,<br>
> c/o Alison Chatterton,<br>
> [address omitted]

Ask for I-APL version 1.1 (and while you are about it why not order Morten Kromberg's GRAF, the FinnAPL statistics and Zdenek V Jizbas tutorial disks at the same time). The price is £2 a disk for APL Association members and £3 for non-members plus £1 for post and packing. I-APL Ltd will continue to sell the books on their own, and disks when a manual is ordered at the same time.

We have sold out of manuals at present and anyone who ordered recently should have had an apology and a promise to send the goods as soon as a reprint is ready. If by any chance you haven't it is probably my fault. Please forgive me and bully me as gently as you can manage.

The address for orders is:

> I-APL,<br>
> 56 The Crescent, Milton,<br>
> Weston-Super-Mare,<br>
> Avon BS22 8DU.

My address is: [address omitted]. The reprint of the manual will also cover Tony Cheal's BBC version (even if we cannot yet issue it).

### Ports to Other Machines

Many porters are getting on with the work. We are promised news of the version for the Sinclair Spectrum (48K and up) by Christmas. Monsieur Emmanuel Roche is doing a port to the Amstrad word processor CP/M machines. The lack of progress on the Apple II and Commodore 64 ports is worrying. Paul says it would take a competent programmer, who knows both the operating system and machine code thoroughly, between a week and a fortnight to do a good port.

### Porting Help is Badly Needed

Such abilities are like gold dust (at least if they are combined with the time and the sort of altruism needed to work on this project) and if anyone knows where they are to be found we would be delighted to hear. A port started now and done by (or over) Christmas for the Apple II or Commodore 64 or Atari ST or Macintosh or any other common machine could bring the author kudos, a warm feeling and the thanks of thousands. We will pay out of pocket expenses. If you know of a potential porter and think you could keep them encouraged to a successful conclusion - ring me up. I have a stack of ready prepared porter's kits.

### Workspaces

Apart from the workspaces on the original issue disk and Paul's FSCREEN mentioned above, we now have utilities from FinnAPL, and on the same disk is a nice collection of statistics workspaces which Tauno Ylinen tells me were contributed by Professor Smillie of the University of Alberta. There are also workspaces for graph drawing from Morten Kromberg and a tutorial from Zdenek V. Jizba. These are available in the BAA software library.

We would like other workspaces, especially if they are of value to teachers in their teaching or their administrative work; we are promised one from APL◇385 which does schoolmaster's ranking and many other pretty things with registers of marks. It is on Beta test in a Yorkshire school at the moment.

### Books

Sales so far have been excellent. Norman Thomson and Linda Alvord's "Tutorial" has led the way with sales of not far from a thousand so far. The manual has sold out - the print run was 600. The Encyclopedia of APL has sold between six and seven hundred. The I-APL board decided that we would pay royalties on any material we publish from now on. We have been offered several things already. "APL for the social sciences" by Tama Traberman. Linda Alvord's next book. Something perhaps from Howard Peelle (I believe Ed Cherlin has a draft).

The second edition of the Tutorial is in camera copy form waiting for the first edition to run out - it will not be long now, because the Tutorial has been a great success and ordered world-wide. Garry Helzer is working on the second edition of "An APL encyclopedia".

We think there is a demand for pamphlets making APL attractive to workers in particular disciplines - about the size of "APL for Teachers" or "APL for Scientists and Engineers" by K. E. Iverson. Could you write such a pamphlet? Do please let us know.

### International Efforts

There are groups supporting the I-APL initiative all over the world. Scandinavia holds the most successful groups. The Danish group produced and issued Kim Andreasen's port for the Piccoline - the first for a school machine - and now we have Morten Kromberg's GRAF workspace. The Swedish and Finnish groups have also done great work.

The Germans and German-speaking Swiss are collaborating with Dr Andreas Geyer-Schulz on translation of the material into German. They are disappointed by the delays to the Commodore 64 version which is the commonest school machine there. In Holland Herman van Loon and his group have distributed many copies.

The Australians have Ian Shannon's port to the microbee and Prof Douglas has sent a disk of statistical functions which is being prepared for issue by Jake Ansell. Both Alain Delmotte and Gerard Langlet have translated the Tutorial into French. I knew about Alain's work but was surprised by receiving the Langlet version which may be published by the Belgian APL Association (BACUS). We have educational distributors in Kenya (John Stevens) and South Africa - the republic - (John Corrie).
