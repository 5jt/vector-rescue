---
title: News from Sustaining Members
authors:
- Alison Chatterton
volume: '6'
issue: '3'
page: '12'
unindexed: true
transcribed: 'from page images of VOL.6-NO.3-JANUARY-1990.pdf, pages 14–18 (printed 12–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Alison Chatterton”. The piece ends on printed 16, whose lower part is blank."
- "HMW Computing: Val Lusmore’s home telephone number, printed for out-of-hours calls, is omitted; the office number is kept."
- "APL People: the evening and weekend number (0225 333618) is printed as the agency’s contact and is kept; it may be a home number."
- "Kept as printed: “One such tools is the User Command Processor”; “APL*PLUS PC System” (without the slash)."
---

*Compiled by Alison Chatterton*
{ .byline }

## Intelligent Programs Limited

The newest sustaining member of the British APL Association has been operating for over 10 years in continental Europe and for 6 years in the UK. Our first news as a sustaining member is a brief summary of our company history.

IPL was set up in its current structure in 1989, following the reorganisation of a group of associated companies in several European countries. The company was founded in Sweden in 1979. Since then, we have undertaken projects and installed systems throughout the world, in 9 countries and 4 continents.

We have always specialised in developing systems for the insurance and financial markets, and the majority of our business is in this field. Our systems are hybrids written in APL, Assembler and C. Use of these languages enables us to develop applications with the flexibility of APL and the efficiency of more conventional languages. The systems are designed to offer end-users a modern, user-friendly interface. IPL's other activities include consultancy work.

The company is rapidly expanding. Several new staff have joined in the past 6 months, and we expect to be announcing shortly a major new systems contract. We are pleased to support the British APL Association as a sustaining member, and we believe our systems demonstrate to wider audiences the power and flexibility of APL.

For further information about IPL, please contact Alastair Charatan, Marketing Director on 01-481-4813.

## HMW Computing Limited

HMW Computing Limited continue to develop and market "4XTRA"; our front-end Foreign Exchange Dealing and Position Keeping system. The "Computers in the City" exhibition at the London Barbican Centre generated increased interest in the product. We have a number of exhibitions early next year, and welcome Vector readers. Please call us for an invitation. On the hard work and coding front, 4XTRA was installed in a major client's site on the 11th of December: well done the HMW development team!

Our employment agency for the APL community continues to attract permanent positions with a variety of clients throughout the UK. Currently we have many vacancies for APL technicians from Juniors through to Consultants, with attractive salaries and interesting work content.

To find out what we can offer, please call Val Lusmore on 01-353 4212. If you would prefer to phone out of office hours, Val's home number is [omitted]

## APL People Limited

As THE PREMIER APL EMPLOYMENT AGENCY in the UK (if not the world!), APL People placed a record number of people in jobs in 1989. We plan to exceed that in 1990!

We invariably get to know about EVERY APL vacancy in the UK, so we always have a good selection of interesting positions available for people with APL skills. These include vacancies for junior programmers, technical experts, consultants, team leaders and even project managers. Our reputation for getting results is fast spreading abroad as well as here.

We also intend to expand our tailor-made training service for companies, offering courses conducted on the company's site and structured to suit the needs and abilities of the trainees.

Delia Marlow has joined Jill Moss in the Bath office, where she will be helping Jill with the ever expanding agency business.

So, whether you're looking for staff, or looking for a new job, call Jill or Delia on 0225 462602 (0225 333618 eves and weekends)!

## Dyadic Systems Ltd

Dyadic is now shipping Release 2 of the DOS/386 implementation of Dyalog APL. Release 2 contains a major enhancement to the Tracer, and some significant performance improvements.

In Release 1 the Tracer allowed you to single step through the function or defined operator, with the State Indicator represented by a stack of overlapping windows displaying your APL code. In Release 2 there is an additional 'naked trace' facility.

Now, if an error occurs while you aren't tracing, you can just press &lt;TRACE&gt; and the system will recreate the trace stack. You can then use all of the facilities of the Tracer to debug your application around the point where it has failed. Typing `→⎕LC` resumes execution and stops the Tracer, so you can continue once you have fixed the code. Dyadic is also developing facilities to display, trace and edit variables in pop-up windows on the screen. Watch this space for further news!

Performance improvements have been made in dyadic iota and grade, and in the arithmetic primitives `+`, `-`, `×`, `⌊`, and `⌈`. All applications will benefit, but those that perform a lot of arithmetic on large arrays will gain most. Some fairly typical actuarial applications run about 30% faster under Release 2 than under Release 1.

Dyadic is providing the upgrade to Release 2 free of charge to all registered users.

Dyalog APL Release 5.2 has been ported to the Sequent, a large multi-processor system that is also marketed by Prime and Unisys.

Dyadic has started work on an implementation of Dyalog APL for IBM's AIX PS/2. This is a powerful but reasonably priced multi-user Operating System which runs on any 386-based PS/2 such as a model 70 or 80. Dyadic considers this to be an ideal platform for a small multi-user APL application.

## Cocking and Drury Ltd

Last December saw the first run of our "APL in the 90s" seminar, a detailed look at the future of APL. The half-day seminar was directed at selected clients, but is now available in-house. Topics covered include the use of APL in the UK, how strategic is APL, vendor attitudes to APL, APL development strategy, APL and SAA, APL and OS/2, and CASE tools and 4GLs.

The seminar expresses our confidence in APL and demonstrates how the language is being used more than ever, particularly by organisations which require solutions to complex business problems. The principal speaker is Romilly Cocking. Please contact Beverley Satterley for further details.

We are planning a new workshop entitled "Choosing the right tools for implementing Decision Support Systems". This two-day practical event is aimed at middle managers, with a slant on using existing tools to implement applications. Again, for further details please contact Beverley Satterley.

A number of our clients have expressed interest in Cocking & Drury offering a comprehensive "APL Facilities Management" service. This service would encompass the support, maintenance and enhancement of all the customer's APL applications, and would also include the migration of such systems to other environments, if necessary. Contact Romilly Cocking for more information.

On a more general note, the company has recently been looking at Object Oriented Programming languages, and Smalltalk in particular. We would be interested in exchanging information with anyone who has gained application experience using this technology.

Release 9 of the famous APL\*PLUS PC System contains a number of facilities which may be new to many users. One such tools is the User Command Processor, which effectively allows you to write your own APL system commands. These commands start with a right-bracket - `]` rather than a right-parenthesis - `)`. The commands are written in APL, and can be invoked from any APL workspace. No workspace resident code is required in order to use the command. This means that the code of commonly used tools and operations can be centralised, and yet is available to all workspaces and users.

Release 9 comes with a large number of pre-written User Commands, including tools to help you list function globals, locals, unreferenced locals and labels, produce workspace listings, search the workspace for specified strings, package a function and all its sub-functions, and much more. This high-productivity tool has been available on APL\*PLUS Mainframe for some time, and we are pleased to see it in the PC environment.

Other Release 9 features include a fast full-screen numeric editor, an automatic symbol table clean-up option, and a new print spooling option which lets you continue work while `⎕ARBIN` is sending a report to the printer.

Release 9 also comes with a complete replacement set of documentation, with a much improved easier to read typeface.

## MicroAPL Ltd

MicroAPL Ltd. started trading in January 1980 and to celebrate our 10th birthday we are planning a series of events for 1990. We hope to start off with a bumper edition of MicroAPL News, although avid readers of Vector will know how difficult it is to produce these things quickly! Without pre-empting our own newsletter, I think it is fair to say that in our first 10 years we have done more than most to spread the knowledge of APL to a wider audience, and also to reduce the costs of using APL. A large number of our many thousands of users of APL.68000 for machines such as the Sinclair QL, Apple Macintosh, Commodore Amiga and Atari ST are first time APL users. Our policy of issuing free runtime licences for APL.68000 has also made it feasible to distribute APL-based packages at a reasonable cost.

Version 7.30 of APL.68000 for the Commodore Amiga is now on general release. Clients should have received details already, but if not please contact MicroAPL for upgrade order forms. The upgrade pack includes reprints of both the Amiga-specific booklet and the full APL.68000 manual.

In the Unix environment, version 7.30 of APL.68000 is now available on 68000-based Sun computers, the HP9000 series and 68000-based Bull computers.

We are currently starting work on the upgrade to the Atari ST version of APL.68000 and encouraging users to write in with upgrade requests. We hope to announce a release date for the upgrade in the near future.

MicroAPL's consultancy section finished 1989 with record levels of business and we intend to do better in 1990. Our training activities now include courses in APL\*PLUS II and we will be shortly introducing APL2/PC training courses. If you would like an up to date training timetable, please contact us.
