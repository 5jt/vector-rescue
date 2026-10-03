---
title: A Lifestyle under VM/CMS VSAPL (meeting notes)
volume: '1'
issue: '3'
page: '60'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 62–63 (printed 60–61; follows art10010990; the introductory notes on p.48 call this the workshop ‘How to Survive in XXAPL’, October 19th); Claude, 2026-10-03'
review: draft
queries:
- "No byline; the speakers were Martin Malin, David Doherty, Mark Longstaff and Phil Last."
- "Slips transcribed as printed: “use of facilities … have allowed”."
---

The talk was given by four staff from a major VSAPL site, which currently runs VSAPL Release 3 under VM/CMS on an IBM 4341 group 2 machine (8 megabytes, 1.2 MIPS), with around 30 APL users and normally between 10 and 20 concurrent users.

The item was introduced by Martin Malin, who expressed the aim of the talk as being to demonstrate that whilst VSAPL was certainly lacking the enhancements that many other APL interpreters made available, it was still possible to develop effective and attractive tools. The strategy required was threefold, namely to make best use of what facilities were available, to make up for the missing facilities as far as possible, and to exploit those features which were unique to the environment. The following three speakers broadly covered these areas.

First David Doherty talked about making the most of the screen-support facilities provided, namely AP124. He described in outline a parameter-driven package called SCREENIO (described in the article ‘SCREENIO - An IBM Full-Screen Manager’ in VECTOR Volume 1, No. 1) which had been developed to cover all aspects of full screen usage. The basic software provided by IBM gives utilities to assist with screen design, writing to the screen and reading from the screen. What was needed was an integrated facility covering not only those aspects, but also validation and assignment of input, and identification and actioning of input key pressed. SCREENIO permits design of screen layout, definition of both fixed and dynamic text to be written to fields, definition of validation and assignment rules for input fields, and PF key definitions and actions. In the application a single call to SCREENIO retrieves all the parameters from file, runs the screen and handles user entry as specified. Amongst the advantages of such a tool are easier application maintenance through much reduced application code and use of a standard, well-proven utility, increased speed of development, and consistent appearance and behaviour to the user.

Next Mark Longstaff talked about making up for missing facilities, such as a native APL file system. He described the standard cover functions developed for AP110 to simulate a component filing system as in other interpreters, as well as giving access to fixed or variable length CMS files. Again the advantages stem from standard utilities giving speed of development and ease of maintenance. Mark then described two facilities which permit non-terminal execution of APL routines. The first allows detached running of non-interactive tasks, such as generation of lengthy reports, with status reporting to any other logon ID as execution proceeds. This frees the terminal (and the user!), but still consumes CPU at peak time. The second allows overnight execution of non-interactive tasks by punching jobs to the virtual reader of a machine which is scheduled to log on automatically each night and run through the night if required. Thus although VSAPL does not directly offer batch or non-terminal tasks, it is possible to accomplish both using AP100 and AP101.

Finally Phil Last described a full-screen workspace manager which makes extensive use of the alternate input stack (AP100) and the full-screen editor (XEDIT). It provides a wide range of facilities for selecting, editing, grouping and listing functions and/or variables. There are also string search and/or replacement options which use XEDIT and run many times faster than any comparable APL algorithm, as well as execution of system commands and various workspace housekeeping utilities. Thus use of facilities peculiar to the environment have allowed the development of an extremely powerful and comprehensive tool.

In closing Martin summarised by saying that, despite the well-known limitations of VSAPL , thoughtful and intelligent use of the available facilities had enabled a reasonable simulation or equivalent of many of the enhancements available elsewhere, and some that weren’t.

The questions which followed elicited details of the hardware configuration, which is as above, and discussed some of the more obscure peculiarities of AP124 and XEDIT.
