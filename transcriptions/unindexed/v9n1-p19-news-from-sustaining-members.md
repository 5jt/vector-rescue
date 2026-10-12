---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '9'
issue: '1'
page: '19'
unindexed: true
transcribed: 'from page images of VOL.9-NO.1-JULY-1992.pdf, pages 21–22 (printed 19–20); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
- applications
queries:
- "Printed byline “Compiled by Gill Smith”. The piece ends on printed 20; printed 21 is a MicroAPL advertisement (“Some things are worth the wait”, APL.68000 for the IBM RISC System/6000) and printed 22 a Lingo Allegro U.S.A. advertisement, neither transcribed."
- "Kept as printed: “cacheing”; “OS-2”."
---

*Compiled by Gill Smith*
{ .byline }

## HMW Trading Systems Limited

The most advanced foreign exchange dealing system in the world - now the most affordable. With over five years of evolutionary development to its credit, 4XTRA from HMW is now being launched as the leading edge technology capable of maximising profits and maintaining a competitive edge.

Developed as a front end deal capture and management system, 4XTRA provides the functionality required to monitor real time multi-currency positions, enter deals and calculate profit opportunities. With NPV profit and loss accounting as standard, the dealer is able to cover his positions accurately whilst providing his management with a real time picture of the overall risk.

4XTRA’s comprehensive position keeping and deal entry screens enhanced to meet the demands of forward, spot and corporate trading together with facilities such as automatically generated spot cover deals, overnight tom-next switching and value added reporting give the trader the tools he needs to deal effectively.

And 4XTRA won’t burn a hole in the IT budget. Cost is based on the number of users, and because the system is PC-based, you can forget about mainframe investment and maintenance costs - a simple PC network is all that’s required. However, low cost doesn’t mean low performance. Already installed in one of the world’s busiest dealing rooms, 4XTRA easily manages over 4000 deals a day and can accommodate peak rates of over 60 deals a minute.

The next release of 4XTRA will use Dyalog APL-W, which will allow the system to run on other platforms (UNIX as well as DOS). A Windows version of Dyalog APL is being released later this year, with a full OS-2 version following on.

If you would like to hear more about how 4XTRA can help your FX business expand, please contact: Rob Thurston, Business Development Manager, HMW Trading Systems Limited, 1 Temple Avenue, London EC4Y 0HA. Tel: 071-353-4212; fax 071-353-3325.

## MicroAPL Ltd

In the last couple of issues of Vector we have concentrated on our new relationship with IBM UK, focussing on recent product announcements for APL2 both on mainframe and PC systems. David Eastwood is progressively making contact with IBM’s mainframe APL users and indeed if any readers have questions relating to IBM’s product range they should contact David at our offices.

In this issue of Vector, we shall be reviewing some of the work our developers have been doing on our own APL product range — the APL.68000 family of products.

We have recently issued a minor upgrade for our Macintosh users to support the new Quadra range of Macintoshes. These are the latest 68040-based systems and are the fastest models in the Mac range. In common with other versions of APL.68000 we have had to make minor changes to the interpreter to support the data and instruction cacheing facilities on the Quadra. This upgrade is available at no charge for owners of APL.68000 Level I Version 7 or APL.68000 Level II Version 2.

Users of APL.68000/X — our version of APL.68000 for the RISC System/6000 — might be interested to note that we have implemented our ‘MicroPLOT’ business plotting language under APL.68000/X. MicroPLOT has been available for many years both under APL\*PLUS/PC and for our multi-user versions of APL.68000. MicroPLOT is designed to simplify the production of routine business graphics and to present a device-independent syntax for APL programmers. We have versions of MicroPLOT available for HP plotters, Tektronix terminals and PostScript devices. Using MicroPLOT on the RISC System/6000 allows APL programmers to produce two dimensional business graphics without having to delve too deeply into the XLib facilities supplied on this system. The code is supplied in an unlocked form to permit customisation.

Our experiences with graphics on the RISC System/6000 coupled with numerous user enquiries have led us to recognise that there is a considerable demand for this sort of software on other windows-based platforms and we are in the midst of producing a Macintosh version of MicroPLOT.

APL.68000/X has been designed to make writing new applications which have a Graphical User Interface (windows, menu bars, dialogs, etc) as simple as possible. At the same time, because the IBM RS/6000 is so fast, APL.68000/X is being used to ‘down-size’ existing mainframe APL applications. Many of these older applications communicate with the user through AP124, an auxiliary processor performing screen layout and forms entry on IBM 3270 terminals.

MicroAPL have recently developed a windows-based AP124 for APL.68000/X. In APL-programming terms, the new processor is an exact replacement for AP124, so all the screen layout arrays and expressions like `CTL←3` to update the screen will work unmodified. However, the new AP124 is a true widget-based implementation using the Motif/X-Windows user interface.

An AP124 screen under APL.68000/X appears in its own window. It is implemented as a special case of a generalised Motif dialog, in which all the elements are either labels or text entry fields. Under Motif text entry fields will have a border, and our AP124 processor takes this into account when laying out the dialog. As well as using the normal AP124 keystrokes, the user can move around the dialog with the mouse and use it to select and edit text. Also, being a true Motif implementation, the dialog is customisable through the Motif resource mechanism, so you can change the colours and fonts used very easily. The result is that unmodified AP124-oriented programs take on a whole new lease of life and look like true windows applications.
