---
title: 'Knowledge, Age and Experience are no Substitute for Good Fortune or How, in the end, Bill wins — you lose'
authors:
- Peter Donnelly
volume: '16'
issue: '1'
page: '111'
unindexed: true
transcribed: 'from page images of VOL.16-NO.1-JULY-1999.pdf, pages 113–114 (printed 111–112; within Technical Correspondence, after Joseph De Kerf’s letter on Fibonacci numbers for negative n); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- humour
queries:
- "A letter in Technical Correspondence, From: Peter Donnelly, May 24 1999; the last letter in the section, followed by “At Play With J: New Big Deal”. The two-part title is printed in quotation marks: “Knowledge, Age and Experience are no Substitute for Good Fortune” or “How, in the end, Bill wins — you lose”."
---

*From: Peter Donnelly, May 24 1999*
{ .byline }

**“Knowledge, Age and Experience are no Substitute for Good Fortune”**

or

**“How, in the end, Bill wins — you lose”**

I now know the cause of my embarrassing failure last Friday [at the AGM].

Given time, I had intended to close my talk with a demonstration that showed how a Dyalog APL ActiveX control (and DYALOG.DLL, if necessary) gets downloaded and installed by Internet Explorer if it is not already present on the user’s PC. When this occurs, the packaged ActiveX control file (DUAL.CAB) is downloaded and decompressed, then DUAL.OCX is copied into the Windows\System directory and registered.

On Friday morning, having tested both mechanisms for installing DUAL.OCX (saving from Dyalog APL and downloading from the Internet), I de-installed the DUAL.OCX in Windows\System (using the standard Microsoft tool REGSVR32.EXE) and erased DUAL.OCX from the Windows\System directory. I then re-saved and re-registered DUAL.OCX (in d:\dyalog82) from Dyalog APL. Being knowledgeable, elderly and experienced, and knowing Bill’s propensity for fun at my expense, I verified that everything was registered correctly using OLEVIEW.EXE and I checked that DUAL worked in Visual Basic. Happy as a sandboy, I then packed up my laptop and left for the gig.

As we know, during my talk that afternoon to the BAA, my proudly presented DUAL.OCX failed to load in IE4, leaving egg on my face and undisguised mirth at the back of the room.

The explanation is *simple* ...

When IE4 downloads and installs an ActiveX control from the Internet, it records information keyed by its ClassID in (wait for it ...)

> `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Code Store Database\Distribution Units\`

It is *this* information that IE4 subsequently uses when it sees an ActiveX control in a web page, conveniently ignoring the official ActiveX registration data.

I had installed DUAL.OCX from the Internet that very morning (as a test) then completely removed/de-installed it before re-installing directly from APL. An ActiveX control is responsible for creating/removing the entries that are officially required for ActiveX registration, and Dyalog APL fully conforms in this respect. However, it is a little unreasonable to expect APL to remove undocumented entries created by recalcitrant Microsoft products. As usual, Bill seems to be ignoring his own rules.

My DUAL.OCX demo failed because IE4 was looking for DUAL.OCX in C:\WINDOWS\SYSTEM, using the registry entries that IE4 had itself previously recorded in the Code Store Database section. In these circumstances, it seems that IE4 blithely ignores the official documented registry entries that are required by the ActiveX protocol, which in this case correctly pointed to C:\DYALOG82\DUAL.OCX.
