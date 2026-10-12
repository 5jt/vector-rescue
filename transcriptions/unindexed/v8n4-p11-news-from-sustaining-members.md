---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '8'
issue: '4'
page: '11'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, pages 13–17 (printed 11–15); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
- user interfaces
queries:
- "Printed byline “Compiled by Gill Smith”. Printed 16 is a MicroAPL advertisement (“Some things are worth the wait”, APL.68000 for the IBM RISC System/6000), not transcribed."
- "The separator in the DDE expression (Dyalog Systems) is printed as a broken bar, transcribed ¦."
- "APL People: the telephone number 0225 462602, given for job enquiries, is kept as a business number."
- "Kept as printed: “an interface to the Borland Paradox Database Manager, s Screen Interface Toolkit”; “the system commands )SIC is implemented” (no closing full stop); no full stop after “(CGA, MCGA, EGA, VGA)”."
---

*Compiled by Gill Smith*
{ .byline }

## Cocking & Drury Ltd and Cocking & Drury (Software) Ltd

By the time you receive Vector we shall have shipped Version 4 of the APL\*PLUS II System for the 386/486. This is the only APL product which allows you to build both Windows and DOS applications from one package.

The programmer interface to the Microsoft Windows libraries enables the building of true GUI interfaces for APL applications that run in Windows. You can:

- use standard Windows components to build interfaces
- set up APL applications so users access them through icons
- develop applications that create multiple Windows
- use the Dynamic Data Exchange (DDE) facility to share data between APL and other applications
- call third-party software through the use of a Dynamic Link Library (DLL)

In addition to this powerful new feature the new release of APL\*PLUS II also includes the first evolutionary step towards compatibility with APL2; an interface to the Borland Paradox Database Manager, s Screen Interface Toolkit to aid the building of text-based application interfaces, enhancements to `⎕NA` which mean other programs can now call APL functions, effectively as sub-routines, and many new utilities and tools.

The price of APL\*PLUS II remains unchanged. All customers on maintenance will have received their free upgrades — others can upgrade for £310 (from Version 3) or £395 (from Version 1 or 2). We are also now shipping STATGRAPHICS Plus from STSC — this uses APL\*PLUS II as its calculating engine to give significant performance improvements over regular STATGRAPHICS and, because it uses all installed RAM, virtually eliminates restrictions on data-set sizes.

Our 8-page magazine 'UPGRADE' was sent out to 7,500 people early in February with news of developments with APL\*PLUS and STATGRAPHICS — and Smalltalk/V. If you didn't get a copy give us a call — it's free.

We're going to be busy attending trade shows this year. The Windows Show which happened in February will be followed by Software Development '92; The Euro Object-Oriented Show and Business Computing (and if we have any energy left maybe Computers in the City too!). Most of the activity on our stand at these shows focuses on Smalltalk/V (monthly sales of which increased twelve-fold in 1991!) but we shall be showing the new APL\*PLUS II as well.

On the consulting front 1992 began with a bang! Three significant new APL jobs began in the first five weeks and two more are in the offing. All of a sudden our resources are thinly stretched — and the imminent beginning of two Smalltalk jobs makes recruitment look very likely for the near future; though we are looking more for Smalltalk people than APL'ers.

The European PANAPL group of STSC dealers continues to be active — a three-day meeting in Paris at the end of February is set to look at further development of the APL\*PLUS II system for GUIs and the development of more programmers' tools.

## MicroAPL Ltd

We start again with news of IBM's APL software range. At the time of writing, APL2/PC Version 1.02 is being prepared for release in the UK on April 14th, and is already shipping in the USA. This new version of APL2/PC contains a number of important features which relate both to the language specification of the product and also to the development aids supplied with the product. TryAPL2, the free packaged version of APL2/PC, has been updated to use APL2/PC Version 1.02 and is available from MicroAPL on request. Both the 16 and 32 bit interpreters will run under OS/2 and Windows3 and 32-bit workspaces may be packaged to produce run-time modules (and hence free runtime licences).

At the language level new features include N-wise reduction; partition and partition with axis; index (`⌷`) and index-with-axis; axis on scalar functions; selective specification (with minor exceptions); complex arithmetic in the 32-bit interpreter (with minor restrictions); the diamond (`⋄`) statement separator; system commands may be entered in combinations of upper and lower case letters; the system commands `)SIC` is implemented

The environment has been enhanced by the addition of new features and APs. The Session Manager (AP120) has been enhanced with new features including a pop-up help panel and a disc-based session log. Editor 3 has been added offering function, operator and text matrix editing; DOS file editing; sorting of local name lists; flagging of errors in header, and mismatched quotes, brackets and parentheses; flagging of duplicate labels; on-line help; hot key between editor and session manager. In addition Editor 3 offers a range of debug facilities such as automatic display of a failing line; break point setting; single step facility; stepping over called functions and operators.

AP124 has been enhanced to allow pop-up windows and other new features. Network support (AP172) has been extended to allow communication between PCs running APL2/PC with AP172. In addition facilities allow exchange of data between APL2/PC and other common programming languages. The new Universal Graphics AP (AP207) gives a simple but powerful interface to all standard IBM graphics adaptors (CGA, MCGA, EGA, VGA)

A range of new workspaces has been added to increase APL2/370 compatibility. In addition a workspace is added to read or write .WKS or .WK1 files. Printer support is extended to a wider range of IBM printers and the HP LaserJet. Facilities are supplied to provide an APL2/PC version of APE Version 2.

The development team here at MicroAPL have been busy too. Whilst APL.68000/X has been under beta test at a number of RISC System/6000 sites, we have refined the shared variable interface to allow `⎕SVO` to dynamically bind auxiliary processors. This is a slight variant on our previous mechanism for auxiliary processors and brings us more into line with mainframe conventions. The first auxiliary processor to benefit from this treatment is AP124. We have developed a widget-based implementation of AP124 which will automatically run AP124 code in its own window. We were pleasantly surprised at how good some of our old AP124 systems look. Despite putting most of our efforts into the windowing version of APL.68000/X, we have not neglected dumb terminal users. Most of our Mirage and Unix dumb-terminal facilities have now been implemented on the RISC System/6000, including most of the major auxiliary processors we have developed over the years.

## Dyadic Systems Limited

At the end of January, Dyadic distributed Test copies of Dyalog APL/W for Microsoft Windows 3. This new product is a true 32-bit Windows application, and contains many exciting and powerful features.

Foremost of these is support for the Windows GUI that is implemented at the interpreter level. It is not just a set of cover functions to drive C or Assembler subroutines. By implementing this support within the interpreter, Dyadic has managed to achieve a result that is fully integrated with the Dyalog APL language and development environment. A second key feature is that the GUI support has been designed to support other systems including PM, Motif and Open Look. This means that Dyalog APL workspaces will be portable between Windows, OS/2 and Unix. You won't have to write different code to handle the different GUIs.

The system is based on three concepts: objects, properties, and events. Objects (often called "widgets") are user-interface components such as Forms, Buttons and Scrollbars. Each object has associated with it a set of properties. For example, the properties of a Form include its size, position, caption (title), border (yes or no) and so forth. Objects generate events. For example, Pushbuttons and Menuitems generate a SELECT event when the user clicks them or presses the appropriate key. To process a particular event in a particular object, you associate an APL function with it. This is termed a "callback" function, and will be invoked automatically by the interpreter whenever the event occurs. Callback functions can create new objects or change the properties of existing ones, so that a highly dynamic and responsive user-interface can be easily provided. Developing Dyalog APL applications is thus a matter of establishing a set of objects, assigning values to their properties, and attaching callback functions to various events. The need for complex control code to steer the user through an application is removed. Finally, a neat but important feature is the ability to TRACE callback functions like any others. When you TRACE your system, the callback functions pop up in windows on the screen as they are fired. You can then step through them line by line, open windows to watch your variables change, and so forth. This greatly simplifies and accelerates the task of testing and debugging a GUI application.

A second major feature of Dyalog APL/W is its interface to *Dynamic Data Exchange* (DDE). Again, this has been designed with other environments in mind and is not limited to Windows. The interface is based on Shared Variables which have been implemented in accordance with the APL standard. To share an APL variable `X` with a block of cells in an Excel spreadsheet, you simply type the expression: `'DDE:EXCEL¦SHEET1' ⎕SVO 'X R1C1:R20C30'`. `X` now contains the Excel data, and assigning new values to `X` will poke them back into the spreadsheet. The DDE interface is a general one, and allows data to be passed freely between Dyalog APL/W and any other application that supports DDE. Shared variables will also be implemented in other versions of Dyalog APL using the communications protocols that are appropriate for those environments.

## APL People Limited

At the time of writing (early February) things are still pretty quiet on the recruitment front, although I have noticed a marked increase in activity compared to the three months before Christmas. I currently have several vacancies for people with APL2 experience to work in Paris, and am also looking for someone with sound APL coding skills for a position in London. Anyone who's interested, please call me on 0225 462602.

Fortunately, sales of our engineering software have been quite buoyant, with large orders from a company called Breknell Willis, who specialise in making switching gear for light railways, and from British Nuclear Fuels, plus a lot of interest from British Steel! Let's hope it continues!

## HMW Trading Systems Limited

The most advanced foreign exchange dealing system in the world - now the most affordable. With over five years of evolutionary development to its credit, 4XTRA from HMW is now being launched as the leading edge technology capable of maximising profits and maintaining a competitive edge.

Developed as a front end deal capture and management system, 4XTRA provides the functionality required to monitor real time multi-currency positions, enter deals and calculate profit opportunities. With NPV profit and loss accounting as standard, the dealer is able to cover his positions accurately whilst providing his management with a real time picture of the overall risk.

4XTRA's comprehensive position keeping and deal entry screens enhanced to meet the demands of forward, spot and corporate trading together with facilities such as automatically generated spot cover deals, overnight tom-next switching and value added reporting give the trader the tools he needs to deal effectively.

And 4XTRA won't burn a hole in the IT budget. Cost is based on the number of users, and because the system is PC-based, you can forget about mainframe investment and maintenance costs - a simple PC network is all that's required. However, low cost doesn't mean low performance. Already installed in one of the world's busiest dealing rooms, 4XTRA easily manages over 4000 deals a day and can accommodate peak rates of over 60 deals a minute.

The next release of 4XTRA will use Dyalog APL-W, which will allow the system to run on other platforms (UNIX as well as DOS). A Windows version of Dyalog APL is being released later this year, with a full OS-2 version following on.

If you would like to hear more about how 4XTRA can help your FX business expand, please contact: Rob Thurston, Business Development Manager, HMW Trading Systems Limited, 1 Temple Avenue, London EC4Y 0HA. Tel: 071-353-4212; fax 071-353-3325.
