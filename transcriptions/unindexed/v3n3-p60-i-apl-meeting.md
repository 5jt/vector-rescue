---
title: British APL Association Meeting – I-APL, 17 October 1986
authors:
- Anthony Camacho
volume: '3'
issue: '3'
page: '60'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 62–66 (printed 60–62 and 63–64; the APL86 logo page, p.65, heads the APL thinking debate on p.66); Claude, 2026-10-05'
review: draft
tags:
- implementations
- education
- APL community
queries:
- "Byline printed “Reviewed by Anthony Camacho”. The contents list gives “Camacho, Ziemann, Thomson & Chapman”."
- "The charts are printed indented; Chart 1 as a two-column table. Charts 3 and 4 are omitted in print (see the editor’s note)."
---

Reviewed by Anthony Camacho
{ .byline }

I-APL had been advertised as the only topic. The plan of the afternoon was for Anthony to explain what the project was about, then for Norman Thomson to talk about what is being done to prepare for introducing it into schools and finally for David Ziemann and Paul Chapman to answer any questions about the specification and how the interpreter is to be produced and ported to the target machines.

The explanation of the project’s history and content took the form of five large charts. The main events so far, the reasons for the project, the target specification, the details of the features of the interpreter (ISO conformance) and the organisation of the project.

**Chart 1: I-APL Main events so far.**

| | |
| --- | --- |
| April 1986 | First discussed |
| APL 86, July | Committee formed; 30 enthusiasts |
| August 1986 | SigAPL votes $5000 (conditionally) |
| September 1986 | Letters to all European Groups; BAA votes £6000 (conditionally) |
| October 1986 | Specification in draft; Marketing plan to be produced; Work on interpreter begins |
| November 1986 | Fundraising begins in earnest |
| . . . . . | |
| APL 87 Dallas, May | Interpreter on demonstration |

It was made clear that the project is not under the auspices of the British APL Association or SigAPL and that it should not be assumed that what the members of the project said expressed the opinions of the BAA. The details of the conditions under which the sums voted by SigAPL and the BAA would be paid were made clear. SigAPL wishes to see and approve of the marketing plan (as it is not a commercial product some things will be harder and a few easier than the usual kind of marketing), and will pay $500 on evidence that the project is really going to start, $2500 on approval of the marketing plan and $2000 on completion of the interpreter (to assist with the costs of launching it and distribution). The BAA conditions are that its Technical Officer vets the Technical Specification and reports his acceptance to the committee and that its Publicity Officer and Education Officer are given the opportunity to see and suggest improvements to the marketing plan, and that the project accepts any amendments they require.

When asked what the state of the BAA finances was, the BAA Officers present agreed that they could not really speak for the Treasurer in his absence; however they could safely say that the BAA had more than the proposed contribution in its current bank account and that this was before the profit from APL 86 was taken into account; in short all that could be said was that it would not strain the BAA’s finances to make this contribution.

> **Chart 2: I-APL – Reasons for the Project**
>
> An interpreter which will run on small computers is needed to give more people the chance to try APL (especially at school and at home).
>
> A free interpreter is needed to overcome the price barrier which prevents many people from taking their interest further (most schools cannot afford commercial prices).

The target machines for the project are the BBC ‘B’, Spectrum 48K (and up), the Apple II (and up), all CP/M micros (e.g. Amstrad word processors) and all PC look-alikes (e.g. Amstrad 1512 series).

The major task besides producing the interpreter itself will be to provide introductory material suitable for this large potential readership: teaching material for schools, games for home use and manuals and guides which do not assume the degree of determination to absorb new ideas that a company expects from a data processing employee.

The purpose of the whole project is to promote the use of APL: not specially I-APL, which will neither be fast nor well provided with facilities, but any APL. If the project succeeds it will bring many new members to the BAA.

> *(Editor: As the I-APL specification is printed in full in the technical section of this issue of VECTOR, we have omitted charts 3 and 4 which were an abbreviated specification.)*

David Ziemann explained that although it may take some time for the formalities to be completed before the ISO Standard is issued, the draft is now fixed and we can safely assume that it will not change.

Paul Chapman explained that the interpreter will be designed to be ported easily onto any new machine and the source code will be freely available so that the project does not have to do all the ports – or even to have knowledge of all of them.

Paul Chapman explained that this outline specification is a target not an absolute commitment (some facilities may have to be dropped if there is no room for them), but that he intended to write the interpreter with all these facilities built-in and only to drop features as a last resort if he could find no other way of getting the interpreter into the space.

David Ziemann offered to provide a copy of the draft specification as it stood (not yet agreed) to anyone with a legitimate interest, provided that recipients would treat it with discretion and not allow it to be published until agreed.

> **Chart 5: I-APL: Project Organisation**
>
> The Committee is:
>
> Edward M. Cherlin (Editor: APL Market News) joint chairman  
> Anthony Camacho (Sec: BAA) joint chairman  
> Howard Peelle (Prof. of Education, Univ. of Massachusetts)  
> Norman Thomson (Educn. Officer, BAA – algorithms ed: Quote-quad)  
> David Ziemann (Technical Officer, BAA)
>
> The Committee has formed a Company called I-APL Limited and all committee members are Directors. Anthony Camacho is Company Secretary.
>
> There are at present nearly 40 enthusiasts on the mailing list, mostly collected at APL 86. Anyone interested may add their name to the list and will be circulated with news of progress.

David Ziemann explained that he hoped to improve the draft specification as a result of comments made at this meeting.

It was agreed that it is most important to make clear that all manuals and other documents issued as part of the project could be copied and translated freely (the latter point especially important to users of APL whose native tongue is not English).

Norman Thomson pointed out that as far as the bulk of the new potential users were concerned, the project will not have a product until the supporting documentation is complete and can be provided with the interpreter.

The documentation at present being prepared consists of a Tutorial on which Linda Alvord is working, an encyclopaedia of APL (giving examples of each use for the primitive functions, operators and system features in alphabetical order) which Garry Helzer is writing and a series of books or booklets to be called “APL for . . . .” where the dots are replaced by a particular application of APL.

The obvious first example was *APL Programs for Mathematics* and Norman circulated draft copies of his book with that title (90 pages of A4 text). This was tried out by looking up in it some school mathematics topics such as Pythagorean triples and going through the examples given. Norman will welcome comments from those who took copies away.

This book (and Garry Helzer’s, which is also in draft) at present has only standard APL examples: eventually there will be side by side examples both in APL and in the ASCII mnemonic transliteration. This will make the book suitable for use whether or not the computer has an APL character set available and will help to accustom people to the APL characters at the same time. Llewellyn Jones has been working on a way to do this transliteration for some two years now and is willing to give the project permission to use his work free of charge. He has functions which will translate from either form into the other under VS APL and under APL\*PLUS/PC. (APLpip for the PC and APLpup for the mainframe where EBCDIC is a bit more restrictive than ASCII.)

Norman said that the marketing effort could only begin when both interpreter and documentation were ready. He suggested several lines of attack. As these were discussed and added to during the meeting the set below includes all the main ideas that seemed acceptable to those present.

1. Prestige schools. Norman Thomson has contacts at several of these and believes that as they have better facilities and lively and open-minded staff, they should be easier to persuade to try out APL. If two or three of the best known schools can be shown to have made a success with APL then it may be easier to overcome resistance in other schools. Excellent reference sites will certainly do us no harm.
2. County Education advisers (or Inspectors as they are called in ILEA – which Neil Bibby pointed out) should certainly be made aware of what we are offering and asked to encourage their schools to try experiments with APL.
3. British APL Association members should be asked to demonstrate what we produce to anyone in education that they know and to help to give away the interpreter, sell any books we have to charge for and provide the project with feedback on what other material could be provided which would help to make the product more acceptable.
4. Plainly any school which can be persuaded to give APL a try should be; the selection will have to be haphazard – it will be the teachers members of the APL Association or the I-APL Project know rather than any selection by some criterion of suitability.
5. It was agreed that it would be particularly valuable to get I-APL exposed to the trainees and staff of teacher training colleges. A few committed advocates in such an institution could encourage the spread of APL out of all proportion to their numbers.
6. It was suggested that another good place for publicity was the user groups. There are groups interested in particular machines, microcomputer clubs for particular districts or in particular colleges and these enthusiasts are more open to new ideas than the general run of home and school microcomputer users. It might even be possible to get the interpreter put onto a public access network so that people could download it.

Norman Thomson reported that the Mathematical Association has a book giving the BASIC programs for 132 common mathematical functions or processes and that this is very popular and widely used. His book is intended to upstage this as it contains many more functions (about twice as many) and need not be more expensive. He has already been exploring ways to get it published as cheaply as possible and is weighing the relative advantages of cheapness and getting onto the lists of a recognised and respected educational publisher.

Les Hollingbery asked about style and standards of the examples in the material to be produced for the project (he liked the style of Norman’s examples). It is desirable that the examples should encourage good habits but the project ought not to try to impose ‘good’ style on potential users (at least not where there is room for a difference of opinion about what style is ‘good’). The project cannot really afford an editor to impose a house style on authors who are all doing voluntary work and may be unwilling to accept anyone else’s views of how to do it. Any suggestions which could be circulated for comment to all authors working on the project would be very welcome.

When the meeting was thrown open to general discussion (questions had been encouraged throughout) many helpful suggestions were made. The dash between the I and APL could subtly be made heart-shaped. We should write and include some games in the free software issued with the project. We should all write to computer and non-computer press about the project to give it publicity and arouse expectations; perhaps we could ask magazine readers to send in their names and addresses if they were interested in an early copy of the interpreter.

Paul Chapman was asked about the process of writing the interpreter and he explained that he intended to write code which would be interpreted in every machine. The interpreter would be a very simple version of a threaded language – something after the style of FORTH but not FORTH itself because the interpreter would be too big and complex. The APL interpreter could thus be exactly the same sequence of ones and zeros on every machine. It would use the machine code entirely through the kernel of the threaded interpreter. To port the APL to a new machine it would be necessary to write the machine language kernel for the machine and code the calls to the operating system which did such things as write a character to the screen, get a character from the keyboard and so on. As it happens only three machine language kernels will be required – to suit 6502, Z80 and the 8088 family. Paul hopes that his development environment will have commercial value. It is to be called DE (to imply it is better than C as an environment for creating portable software) – he was going to call it DEL (for development environment language) until he discovered he was unaccountably losing files!

The general atmosphere of the meeting was friendly and no-one voiced any adverse criticism of the work that had been done so far or of the plans presented. When the audience was challenged to suggest a better way to encourage the spread of APL no suggestion was offered. When people were asked explicitly whether they thought the contribution from the BAA was a good use of the funds there was no dissenting voice to say that it was not. There was general agreement that this was a very good way to try to spread the use of APL, and many present felt that so far unfruitful efforts might meet with success once they had the proposed free product to help them.

Thirteen people put themselves down on the list of people interested in having news about the project and most of them offered to help in some way.

The meeting ended at about 5.30 and discussions continued in the bar for some time.
