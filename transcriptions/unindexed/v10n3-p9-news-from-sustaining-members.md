---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '10'
issue: '3'
page: '9'
unindexed: true
transcribed: 'from page images of VOL.10-NO.3-JANUARY-1994.pdf, pages 11–18 (printed 9–16); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”. The Dutch APL Users Group report (printed 15–16) is signed “Leiden, 4 November 1993 / Eke van Batenburg”; the signature is kept at its end."
- "Kept as printed: “to get at corporate data form the development tools” (Insight Systems); “smaller, simpler, and fast.” (Manugistics); “a free migrate to the Windows product”; “to deliver all of functionality”; “several months delay”; “the inter-client communications is based on”; “APL 2 late”; “where to fit in APL”; “elaborated about”; “each others’ strengths”; “by AP119”; “the comprehensive way of doing the same in APL”; “working at a Windows version for Statgraphics”; the quote mark after ‘TCPIP’ is printed as a stray mark; “Micro-APL” and “brain-slice entomogram” in the Dutch report."
---

*Compiled by Gill Smith*
{ .byline }

## Insight Systems

As a new Sustaining Member, we would like to start off by expressing our thanks to the BAA for providing us with this excellent platform from which to express our continued commitment to APL.

Insight Systems was formed in 1990 from the remains of I.P.Sharp Copenhagen. We suddenly found ourselves with no mainframe to logon to, and spent the first couple of years searching for good development tools on workstations with sufficient algorithmic punch for the type of applications we were used to. Needless to say, we did not find anything until the APL vendors finally got their act together.

The next search was for connectivity tools which would enable us to get at corporate data form the development tools of our choice, whether they be Excel, C++, Smalltalk or APL. To our delight, we discovered that the product which we liked best — SequeLink Client/Server MiddleWare™ — did not have a Danish distributor.

Besides marketing SequeLink to the general Data Processing Public in Denmark, we have created a product called SQAPL. The "SQAPL Client" gives APL applications access to all SequeLink-supported services (which includes practically all major SQL databases) via just about any network protocol. Our "SQAPL Server" product allows APL systems to function as SequeLink Servers. With the SQAPL Server, you can use a Unix APL Server to provide improved performance and security to Windows or OS/2 applications. Client and Server systems need not use the same APL interpreter — you can write a front-end in APL/W or APL\*PLUS II under Windows and call APL2/6000 applications if you wish.

To non-APL SequeLink Clients such as Visual Basic, C++ or Excel, the SQAPL Server looks like any other server — with a "non-standard" dialect of SQL. Data is input to APL in the form of "bind variables", and returned in tabular form.

Since we announced SQAPL at APL93, we have distributed SQAPL products to customers using Dyalog APL and APL\*PLUS II under Windows, OS/2 and Unix, to connect to Dyalog APL, Ingres, Oracle (6 and 7), RDB, OS/2 DBN, DB2/2 and DB2/370 over TCP/IP, SPX, DecNET, and NetBIOS. SQAPL is also available for APL2/2 and APL2/6000, as soon as these products become generally available.

The development of SQAPL has resulted in some tools for the delivery of APL tools on multiple platforms. We can now generate C-coded tools or utilities capable of handling APL arrays from (or converting between internal forms of) Dyalog APL, APL\*PLUS II or APL2 (and we plan to add APL/68000 and Sharp APL), packaged for any of these systems under Windows, OS/2 or Unix. Please give us a call if you have an idea which needs this type of technology.

## Manugistics Inc

The phones at Manugistics have been ringing all day long since we announced plans for the new APL\*PLUS III for Windows, due for release in Spring 1994. We're very encouraged to hear from so many clients who have expressed excitement and approval of the design plans we announced for APL\*PLUS III. Many of you may have had the opportunity to preview the product during James Wheeler's "seven cities in 10 days road show" in Europe this past December where feedback from seminar attendees was overwhelmingly positive.

Here are some highlights of the upcoming release:

- APL\*PLUS III will be built using the Win32 API, Microsoft's official facility for supporting 32-bit applications under Windows. This ensures that the applications you build will also run on Windows NT and the future "Chicago" version of Windows. Win32s will be packaged with the product.
- APL\*PLUS III features a pure Windows-based session manager and full-screen editor that follows Windows style conventions. This consistent graphical user interface means that in addition to having a standard Windows look-and-feel, Windows users will be able to very quickly become productive, probably without even opening the manuals.
- *Free run-time!*
- The APL-based APLGUI workspace in the current version of APL\*PLUS II is being replaced with facilities that are written in C and built into the interpreter for APL\*PLUS III. This means that the toolkit itself will be smaller, simpler, and fast. Applications written using the APLGUI toolkit in APL\*PLUS II will be upwardly compatible with APL\*PLUS III/Windows.

Those of you who program in other languages besides APL will be glad to know APL\*PLUS III will include control structures similar to those in C for easier code readability and maintenance. Even some hard-core APL purists who have seen how we're implementing control structures admit they will be of value.

Other features in APL\*PLUS III include on-line Help, improved DDE and DLL interfaces, and the APL\*PLUS Debugger, repackaged with a Windows user interface.

Anyone purchasing APL\*PLUS II between now and the time APL\*PLUS III is available will receive a coupon for a free migrate to the Windows product when it is released. Beta systems of APL\*PLUS III are available through European dealers.

For those of you running DOS applications only, we've also announced that an unbundled version of APL\*PLUS II for DOS is now available. This version runs under both DOS and Windows, but will not include the Windows interface and APLGUI toolkit. This represents an opportunity for those of you who do not need a true Windows APL to get the full power of APL\*PLUS II at a much lower price (check with your local dealer for pricing).

## MicroAPL Limited

MicroAPL is announcing APL Level II for the Apple Macintosh with PowerPC at MacWorld in San Francisco on January 5 1994. I am sure by now that most of you will have read about the new generation of Macintosh computers based on the PowerPC RISC processor which are scheduled for release in the first half of 1994. These computers will, for the first time, bring the power of high-end RISC workstations to the personal computer market.

The new interpreter has been translated to run native on the PowerPC using PortAsm, MicroAPL's 680x0 to RISC assembly-language translation tool. APL Level II is based on and 100% compatible with APL.68000 Level II, which was originally written in 68000 assembler to ensure maximum performance. PortAsm allows us to efficiently translate this code onto the PowerPC architecture while still maintaining a single set of APL interpreter source code. Indeed the compatibility between our Apple Macintosh version and the PowerPC version is so great that even auxiliary processors written in 68000 assembler will work without translation! This is achieved by automatically triggering the 68000 emulator which Apple have designed into the Macintosh for the PowerPC.

As with all our second-generation APLs, APL Level II is designed for maximum compatibility with IBM's mainframe APL2 product. APL Level II workspaces and APL files share the same binary format as those of our APL.68000 products.

Features of APL Level II include:

| | |
|---|---|
| Close conformance to IBM's APL2 | Full Mac user interface |
| Nested and mixed arrays | Easy access to Mac toolbox |
| Selective specification | APL GUI event handling |
| User-defined operators | Multi-tasking |
| N-wise reduction | Sophisticated session manager |
| Axis on scalar functions | Multiple independent edit windows |
| Overlays (packages) | Direct import from other APLs |
| Powerful file system | Free runtime licences available |

APL for PowerPC will be available simultaneously with the commercial launch of the first PowerPC Macintoshes in early 1994. It comes complete with a collection of support workspaces and complete documentation.

MicroAPL's development staff have also been at work on the RISC System/6000 and the result is the completion of our APL68000/X to C—ISAM interface. Based around the Informix implementation of C—ISAM, this product allows the APL programmer to create multi-key files where the keys themselves may be made up of several sub-parts. Access to files can be by exact key match, generic key match, first record and read forward, or last record and read backwards. It is supplied with a support workspace and full documentation.

As part of our continuing commitment to quality we have been enhancing our in-house APL testing suite. We can now perform over 200,000 automatic tests on new interpreters (or new releases of existing interpreters) to ensure that they are performing correctly. This is achieved by comparing known results with the results from the new interpreter. APL statements and their results are transferred onto the testing environment then the APL statements are executed by the new interpreter and the new results are compared with the originals.

## Dyadic Systems Ltd

During the last quarter of '93, details of the "X/Open Common Desktop Environment" (CDE), which was announced earlier in the year, began to emerge. As a result, Dyadic postponed its plans for a December release of Dyalog APL for Motif and a parallel upgrade to Dyalog APL/W for Windows.

CDE is part of a major new initiative which is backed by all the leading Unix vendors to provide a common application programming interface and a standard desktop environment for Unix workstations. CDE is based on OSF/Motif with additional software and tools contributed by members of the consortium. For example, the desktop is developed from Hewlett Packard's VUE and the inter-client communications is based on Sun's ToolTalk. CDE is intended not only to provide standardisation for developers and users alike, but also to deliver all of functionality and ease-of-use features of Microsoft Windows. Indeed, one way of looking at CDE is that it is the Unix answer to Windows.

Although the decision to re-target the Motif version of Dyalog APL for CDE has delayed the product considerably (CDE itself will not be available until mid '94), it will bring major benefits to APL users. In particular, CDE will enable Dyadic to deliver 100% APL/W compatibility in areas where this is impossible to achieve with Motif alone. For example, CDE provides very "Windows-like" printer support and font management facilities that are entirely absent from Motif itself. In addition, CDE's inter-application communication facilities are equivalent to Windows DDE and will permit the full implementation of shared variables in the Unix version of Dyalog APL.

Dyalog APL for CDE will be provided as a free upgrade to existing Dyalog APL/X users who have a current Support and Maintenance Agreement. To allow customers to begin to migrate existing APL/W and APL/X applications to the new product, an interim version for "raw" Motif is available on IBM RS/6000 and Sun SPARC systems. This version lacks certain features such as the PRINTER object and shared variables, and is supplied with the Dyalog APL/W manuals rather than the final CDE documentation. Nevertheless, this version is otherwise complete and will run most APL/W applications (with the restrictions noted above) unchanged. Customers wishing to take advantage of this offer should contact Dyadic or their local Dyalog APL distributor.

Although there will be several months delay before CDE is available from IBM, Sun Microsystems etc. the Dyadic development team will not be idle. Rather than producing a parallel (with Motif) end '93 release of Dyalog APL/W as originally planned, the company intends instead to develop an even richer new version of the product. In addition to the features announced at APL93, this version will include major object-oriented extensions to the APL language and many exciting enhancements to the already extensive GUI support facilities.

In response to the growing number of successful Dyalog APL/W products, Dyadic is planning to produce a third-party software catalogue ("Outer Products"). This will be distributed to existing customers and shipped with each new copy of the software. To obtain an entry in the catalogue, please contact Peter Donnelly at Dyadic.

## Soliton Associates Limited

Version 4.02 of SHARP APL for UNIX has been well received by customers, and Soliton's mainframe customer base is showing increasing interest in porting large-scale multi-user SHARP APL applications from IBM MVS mainframes to the UNIX environment. Significant cost savings can be obtained by running such applications under UNIX. Where required, Soliton's NSVP and MVSLink products provide access from UNIX to MVS data and services.

Current development plans for SHARP APL for UNIX include enhanced support for very large SHARP APL applications on SMP (symmetrical multi-processor) UNIX platforms.

An Application Programming Interface (API) for Soliton's Network Shared Variable Processor (NSVP) has recently been announced. The NSVP API supports access from non-SHARP APL software both to SHARP APL and to SHARP APL Auxiliary Processors. The NSVP accessed by the API can be either local or remote, thus the NSVP can be on the same computer as the calling software or on a network-connected computer.

The NSVP API will support the client-server architecture, typically with non-SHARP APL clients accessing SHARP APL or SHARP APL Auxiliary Processor servers. Initially, the NSVP API will be available under UNIX, with support for UNIX-MVS connectivity. This will allow, for example, access from another vendor's APL for UNIX to Soliton's DB2 Auxiliary Processor for MVS. Most of Soliton's major auxiliary processors for MVS can now be installed stand-alone (thus without SHARP APL for MVS) and accessed via NSVP from network-connected UNIX and MVS computers. Support for the NSVP API in additional environments, including Microsoft Windows, is under consideration.

## Kestrel Consulting

First of all, let me wish all Vector Members a Happy New Year! At the time of going to press it is December and far from things slowing up in preparation for the festive season, the phone lines have never been hotter! Our American contracts in particular have been coming through fast and furious and we are, as ever, on the lookout for APL or SMALLTALK professionals with a taste for the good life.

As a result of our constant dealings with America, we now have an office in Los Angeles which enables us to provide an even better service for anyone wishing to work in the USA. Kestrel takes care of the Visa application and costs, pays for a return flight to the USA and foots the bill for the initial accommodation and hire car expenses. All you need to do is provide our clients with a glowing telephone interview!

If you fancy a change of scene but not a trip across the Atlantic, don't despair! We are in contact with many APL sites in this country and are sure to be able to offer you something of interest.

## Dutch APL Users Group

The Dutch APL Users group organised an APL day in The Hague in close co-operation with Share Europe. A short summary of the speakers and their main points follows.

- Theo Zwart of OASIS chaired the day and started with a general introduction.
- Louis van Geldrop of Pecoma kicked off with an evocative statement about 'The Good, the Bad and the Ugly of APL'. It appeared that the ugly stands for the ugly APL characters, the bad was for the suppliers (insufficient standardisation, APL 2 late) and the good were (of course) the APL programmers.
- David Eastwood of Micro-APL talked about 'The Advantage of APL in Application Development'. He raised many interesting points in defining the characteristics of 4GLs in general and where to fit in APL. Unfortunately, the tight schedule did not allow for much discussion. David finished with a small APL.68000 demo on the Macintosh.
- Jim Brown of IBM talked about 'Inside the Human Brain with Parallel Processing'. He showed how you could feed another processor with APL instructions; you can not only transmit data and APL expressions (and get them executed and replied to) but even send APL functions by sending a transfer-file-function. Jim also elaborated about the possibilities of assigning several computations (for example, 128 sections of a brain-slice entomogram) to several processors, or to have a PC session manager for user-interface and a mainframe computer for computation.
- Peter Donnelly of Dyadic Systems demonstrated his event-driven paradigm for GUI and other objects (graphics in particular). Peter showed the 4 basic GUI quad functions `⎕WCreate` `⎕WSet` `⎕WGet` and `⎕WName`, how properties of objects could be set (positional as well as by keyword), deleted and copied (... well, ... next week).
- Paul Lewi from Janssen Pharmaceutical spoke about 'APL as Tool of Thought; an Instrument of Problem Formulation'. "Not solving, that is less interesting than problem formulation", he said. Paul elaborated upon the virtue of APL's symbols and of simplification. He showed several examples of APL equalities which are obvious in APL's symbols but are not obvious, or may even be impossible in a 3GL. He elaborated about the virtue of being able to simplify (thereby losing details, of course) like Mercator's projection as done in factor analysis. Paul showed several examples of the use of factor analysis. Your acceptance of this tool depends on your being a Platonist (the shadows give you all you can know about reality) or Aristotelian (what you see is all there is to see).
- Benoit Paquin of Soliton Associates talked about 'Sharp APL for the Nineties'. First he recapped the history of Soliton (I.P. Sharp, Reuters, Soliton; gigantic databases, data, APL). He stressed the strong expertise of Soliton in networking and communication between very different computers. This was also illustrated by means of Soliton's NSVP (Network Shared Variable Processor) where APL on an IBM mainframe under MVS corresponds to APL (SAX actually) on a Unix machine. Benoit invited other vendors to work together more closely and share each others' strengths (a point also raised earlier by van Geldrop).
- Jim Brown talked about 'Network Programming with Sockets: A Comparison of C and APL2'. Dressed in his socks, Jim said he was wearing a suit and a tie and wanted to talk about sockets (not socks). So he talked about protocols. Jim showed how to communicate by means of the TCP/IP protocol to other machines by AP119. He compared the elaborate way of doing that in C with the comprehensive way of doing the same in APL (mainly due to the need for extensive declarations in C). It seemed wasteful to repeat the character string 'TCPIP' in each command but Jim explained that this was 'a feature', because it would enable them to communicate via other protocols too (if necessary).
- James Wheeler of Manugistics was unable to come but sent his slides. So in his place Theo Zwart presented them. They mostly stressed that Manugistics is still working to improve the Windows version of APL\*PLUS (and they will drop DOS support to some extent). A full Windows version was finally announced, called APL\*PLUS III. APL will also have the feature that it can be called from another language, like C, by DLL. Manugistics are also still working at a Windows version for Statgraphics. A positive message was the announcement of a free run-time version in the future.
- Nancy Wheeler of IBM talked about 'APL2 for OS/2 and APL2 Connections'. Like Benoit she recapped history, but now IBM's view, in particular about the APs. Nancy reported that IBM is working towards more consistency in the use of APs so a user could port his applications between different machines without bothering about differences in AP syntax. Nancy also presented a short wish-list of top-priorities (but apparently still under discussion) including porting to other, non-IBM-machines, Windows NT, Windows? and (after some prompting from the audience) the APL compiler. Finally, she and Jim gave a demonstration of several features of the OS/2 version of APL2: easy printer support, colour font, keyboard handling and the use of name association.
- Although it had become very late, Bernard Smoor evoked a lively but short discussion about Vendor co-operation.

Leiden, 4 November 1993<br>
Eke van Batenburg
