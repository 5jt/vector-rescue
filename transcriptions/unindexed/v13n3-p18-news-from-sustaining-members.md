---
title: News from Sustaining Members
authors:
- Gill Smith
volume: '13'
issue: '3'
page: '18'
unindexed: true
transcribed: 'from page images of VOL.13-NO.3-JANUARY-1997.pdf, pages 20–22 (printed 18–20); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Gill Smith”. The news ends on printed 20 (its lower part blank); the Education Vector begins on printed 21."
- "Insight Systems / Adaytum Software: the companies’ web sites and their info@ and support@ e-mail addresses are kept; Jacob Brickman’s own e-mail address, given in the “People” paragraph, is omitted as a personal e-mail address."
- "Kept as printed: “benefitted”; “prog-ramming” is hyphenated across a line break and given as “programming”."
---

*Compiled by Gill Smith*
{ .byline }

## Dyadic Systems Limited

The Beta Test release of Dyalog APL/W Version 8.1 was shipped on December 23rd, with the production release scheduled for February.

Version 8.1 provides extensive support for OLE Automation, allowing APL to act both as a client and as a server. See Vector Vol.13 No.2 for details.

Dyalog APL with OLE technology offers a new range of opportunities for APL developers. Not only can you deliver complete packaged GUI applications in APL, but you can now market stand-alone software components that can be incorporated into other products which are constructed with other languages.

Version 8.1 also includes support for TCP/IP. This is implemented by a new `TCPSocket` object that is controlled using the standard Dyalog APL object management functions (`⎕WC`, `⎕WS` and so forth). Like any other Dyalog object, a TCPSocket is of course a namespace in its own right.

The TCPSocket object allows you to communicate with other TCP/IP applications running on any computer in your network, including the World Wide Web. It supports both Stream and UDP connections and, like the underlying WinSock API, is predominantly event driven. The TCPSocket object supports character, raw, and internal APL data formats and also provides the mechanism for client/server operation between two Dyalog APL workspaces.

Finally, Version 8.1 includes *dynamic functions*. A Dynamic Function (operator) is an alternative function definition style suitable for defining small to medium sized functions. Dynamic functions support automatic localisation, nested functions, and a simple but powerful control structure called a *Guard*. See Vector Vol.13 No.2 for details.

In addition to these major new features, Version 8.1 includes other useful enhancements; and there is a parallel release 7.3 for Windows 3.1. For further information, consult the Dyalog APL web site at www.dyadic.com or contact your Dyalog APL distributor.

## Insight Systems / Adaytum Software

Insight Systems and Adaytum Software are now properly "wired"; our internal Microsoft Mail system is linked to the Internet. Or so we think — the technical glitches had not all been ironed out as this is written, but we are assured that all will be OK when this appears in print. To be sure, please check our Web sites before sending E-Mail. Addresses to note are:

**Web sites:**

| | |
|---|---|
| www.adaytum.dk<br>www.insight.dk | Adaytum Denmark and Insight Systems<br>(these two addresses are aliases for the same domain) |
| www.adaytum.com | Our US-Midwest office in Minneapolis/St.Paul |

**E-Mail addresses:**

| | |
|---|---|
| info@insight.dk | For queries regarding Insight's products and services |
| support@insight.dk | To report problems or request assistance if you are a user of our products |

Once the pilot projects in Denmark and the USA are completed, our Bristol office will become **adaytum.uk** and our new Paris office will be **adaytum.fr**.

### People

One of the people you will be able to reach (as [e-mail address omitted]) is Jacob Brickman, who joined the Adaytum Planning team on November 1st as a senior developer.

### Products: Adaytum Planning

The 32-bit version of Adaytum Planning, based on Dyalog APL version 8.0, for Windows 95 and Windows NT, is scheduled for release at the end of January 1997. A new version of our Windows Reporter product, based upon Causeway's Rain and NewLeaf printing technologies, will be available in both 16- and 32-bit versions in April.

### Products: SQAPL

There are no new product announcements this quarter; we are busy programming but not ready to announce release dates for our OLE frontend for APL (for Visual Basic, Delphi etc.) or the new SQAPL ODBC Server for Windows NT.

## Causeway Graphical Systems Ltd

This has been a quarter of steady progress on two fronts. It has been good to clear the backlog of requests for *RainPro* and *NewLeaf*, both of which have benefitted from beta feedback, and which will remain stable in their November versions for the next few months for both Dyalog and APL+Win. The few minor bugs remaining are being noted on the Causeway Web site as users flush them out, so that you can avoid them or fix them in place as you prefer. The only major last-minute change was to add `∆spoolpath` as a global in the `leaf` namespace, as otherwise NewLeaf simply used the current working directory as its work area; this can be a dangerous habit on a networked installation where the user may not have write access to the working directory!

Work in progress for the next NewLeaf version includes tables which fold across as well as down, and specific optimisation for the LaserJet II printer. The next release of RainPro will support a wide range of 'chart events' and methods so that graphs may be modified in-place by the users, and pop-up dialogues can be programmed easily to allow modification of headings, labels, colours, fonts and so on.

On the application-development side, Duncan Pearson and Jon Sandles have been working steadily towards the next SAP release date. The mixed C++ and J environment continues to perform well, and is becoming much easier to work with as all the complexity of the linkage is now well-buried in our own increasing collection of OCXs. This brings the technology back within the grasp of the average APLer (which the black art of OCX development certainly is not), as it is now accessible from Visual Basic as well as from C++. As soon as we have time to pause and take stock, we will review and complete our OCX library and consider how to make it available to the J community.

Having survived in one (quite small) office unit for nearly two years, we finally spread ourselves out just before Christmas into much more comfortable surroundings. The address, phone and fax numbers and emails remain as they were, except that Compuserve have finally implemented personal addresses, so if you feel more comfortable sending mail to causeway@compuserve.com, this now works. Of course the old number remains fine too.
