---
title: Report on APL87
authors:
- John Sullivan
volume: '4'
issue: '1'
page: '17'
unindexed: true
transcribed: 'from page images of VOL.4-NO.1-JULY-1987.pdf, pages 19–20 (printed 17–18); Claude, 2026-10-12'
review: draft
tags:
- conference reports
queries:
- "Contents line “APL 87 Report”; the printed heading is “Report on APL87”, with the byline “by J Sullivan”."
- "Kept as printed: “associated processor 11”; “their parent Reuter’s”; “[Sephen Jaffe]”; the question mark closing the sentence “particularly concerning ‘where do you draw the line?’ when it comes to compiling code that can only be interpreted at run-time?”."
---

*by J Sullivan*
{ .byline }

This is not going to be a blow-by-blow account of what happened at every session of APL87, but rather a personal view of what I found most interesting at the conference. This is not to suggest that anything I have left out was boring or uninteresting, so don’t assume that because I haven’t mentioned your favourite topic or session that I thought it so.

The tutorials on Sunday were a mixture of the serious and the not-so-serious. On the serious side the talks on Data Driven Control Methodology and APL techniques for Building Expert Systems in the PC Environment were most interesting and informative: the techniques used are not restricted to the fields mentioned by the authors, for example it is always better to have the data drive a program rather than to have the program drive the data.

Two humorous presentations were given by Gitte Christensen (How to manage APLers – conclusion: you can’t) and Phil Smith who demonstrated some of the research he is currently carrying out. Phil Smith’s talk was expanded later on in the week in another plenary session which gave much light relief amidst all the serious work that usually goes on in an APL conference.

Dr Jim Brown gave a paper on the design principles of APL2 which described some of the extensions in APL2 and discussed the reasons why they were adopted. In the paper he also explained why the result of enclosing a scalar in APL2 is identical to the original scalar. On a similar theme there were papers by Phil Benkard (Replicate Each, anyone? and Implications of APL2 Grammar) which discussed the replicate operator and APL syntax in a highly technical and exhaustive manner.

As a user of APL2 I was most interested to hear what the people from IBM had to say. The most important session from this point of view was the IBM Product Forum on the 3090 Vector Facility. As everybody is aware, APL is the ideal language for processing array operations ‘in parallel’, and the Vector Facility is the bit of hardware bolted on to the computer that performs operations in parallel. (Although I say ‘in parallel’ here, IBM will tell you that it’s not true parallel but pipelined; that’s near enough parallel for me.) The implications of this are that a whole new set of Assembler instructions has had to be written and programmers will have to amend their programs to take advantage of them. A new Fortran compiler has had to be produced and the users will have to amend their programs to take advantage of it and a new version of APL2 is being developed and programmers will have to do nothing in order to take advantage of the Vector Facility. We had the chance to test the Vector Facility on the IBM stand, where they had two terminals linked to a local computer centre for our use.

Workers at IBM Yorktown Heights are developing an APL translator which is designed to translate APL2 code into another high-level language for compiling and link-editing and calling from within your APL workspace via associated processor 11 using the `⎕NA` facility introduced with Release 2 of APL2. Currently FORTRAN has been chosen as the high-level language, because it can be called through `⎕NA` and because it lends itself to Vectorization. There were a number of problems to be sorted out in developing the translator, particularly concerning ‘where do you draw the line?’ when it comes to compiling code that can only be interpreted at run-time? The answer is you don’t compile everything, and you certainly don’t compile bad code (does anybody actually write bad APL code these days?). For those of you who want to read more about the Yorktown translator there is a very informative article in the November 1986 copy of the IBM Journal of Research and Development.

I was also interested in the ‘other’ APL that is being developed along parallel lines to IBM APL2, i.e. Sharp APL. Sharp APL is being developed towards Ken Iverson’s ‘Dictionary of APL’, which was the basis for Dr Iverson’s talk at the opening plenary session in which he traced the history of APL notation. Sharp APL was also discussed in I.P.Sharp’s product forum. In this the history of I.P.Sharp and their parent Reuter’s was outlined, and then some figures were given on the number of Sharp APL sites throughout the world. Sharp has two significant new development efforts under way: Sharp APL/VM, and Sharp APL/UX (also known as SAX), which was on display on their stand in the exhibition. I don’t intend to go into any details except to say that it is very close to ‘Dictionary APL’. Further details may be had from I.P.Sharp themselves.

On the social side, there was a reception at the Dallas Museum of Art on the Monday evening. This was very enjoyable as in addition to the food and drink we were able to wander around and enjoy the exhibits. The museum has a large collection of modern art from all over the world (I’ve never seen so many original Picassos in one place before) together with examples of early American colonial furniture and South American native artifacts.

To sum up the conference in a few words is impossible. Between 8.30 a.m. and 5.30 p.m. it was all very hard work, and between 5.30 p.m. and bedtime it was very hard play. All in all though it was exceedingly enjoyable.

Overheard at APL 87:

> “What *is* Southfork?”
>
> “The first 80% of the code takes the first 80% of the development time; the remaining 20% of the code takes the remaining 80% of the development time”. [Leslie Goldsmith]
>
> – While waiting for the output from a function: “Here’s an example of an empty array”. [Alan Graham]
>
> “That’s why they invented cars – to get around Dallas.” [Sephen Jaffe]
>
> “What do you call code that hasn’t been optimised? Pessimised.” [Graham Driscoll]
>
> “Plan to do a prototype – you will anyway.” [Alan Graham]
>
> “This machine is not infinitely fast; it is only infinite over 2.” [Jim Brown]

See you all at Sydney?
