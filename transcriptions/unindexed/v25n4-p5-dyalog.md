---
title: Dyalog
volume: '25'
issue: '4'
page: '5'
unindexed: true
transcribed: 'from the typeset issue v254.pdf, pages 5–9 (printed 5–9); Claude, 2026-10-12'
review: draft
tags:
- implementations
- APL community
queries:
- "Unsigned, under the page heading “Industry news” and the heading “Dyalog Ltd”. Kx’s news follows on printed 10."
- "The subheading “Summary of Version 13.1 enhancements” is printed in roman text, not bold; it is kept as a paragraph."
- "Kept as printed: “Pat Buteux” on printed 5 but “Pat Buteaux” on printed 8; “Dyalog’12” without a space (the apostrophe is printed full-width, given here as ’); “the regular expression operators ⎕R/⎕S”; “Apples OSX”; “http://www.reddit.com/r/programming/comments/uu2br/try_apl_is_weird_but_fun/”, broken across two lines in print; “the Dyalog File Server (DFS), will provide”."
---

## Dyalog Ltd

### Looking East and West

The Annual Dyalog Programming Contest is in its 4th year. In the first three years, we have had entries from all over the world, with winners and runners-up coming from New Zealand, the USA and Germany. This year, the best submissions were from the East (as seen from the United Kingdom): we are very pleased to announce that the winner of the Grand Prize in 2012 (USD 2,500 and an expenses-paid trip to the Dyalog’12 Conference in Denmark) is 橋本隼人 (Hayato Hashimoto), a 21 year old undergraduate student at Kyoto University in Japan – and the runner-up Татьяна Иванова (Tatiana Ivanova) from Russia.

At the same time, we are delighted to announce that Pat Buteux has joined Dyalog Ltd as VP of Sales & Marketing for the USA. Pat joins Dyalog Ltd with one of the finest pedigrees in software development and software consulting, and she is particularly experienced in working with business development, strategic branding and positioning. Pat’s career started at General Electric in the timesharing days. She helped transform STSC into an independent software vendor and was responsible for development, marketing and sales of APL\*PLUS. She also built STSC’s international network of resellers. We’re incredibly pleased to have Pat join the Dyalog team and we’re looking forward to working with her on expanding the APL market to our West.

### Dyalog APL Versions 13.1 and 13.2

We are currently about halfway between Version 13.1, which was released in April, and 13.2, which is due to be released at the end of January 2013. As the decimals suggest, these are incremental updates, with particular focus on performance or capacity enhancements, and (ahem) the odd bug fix – while we work on version 14.0 (targeting end of 2013) which is intended to add very significant new core-language features and more fundamental performance improvements and features to support parallel hardware.

That being said, versions 13.1 and 13.2 will not be without new functionality:

Summary of Version 13.1 enhancements

- New system function `⎕FHIST` – The new File History system function reports information about which user created and most recently updated the file (and when it happened). This feature has been added to support clients who have previously been running the SHAREFILE/AP system on mainframes.
- New system constant `⎕DMX` – Version 13.1 adds significant new error reporting functionality, in the form of a system variable which has been named `⎕DMX`. `⎕DMX` is designed to make error handling simpler, more complete and more accurate.

  The key benefits of `⎕DMX` are: the provision of more detailed information, including the relevant operating-system error where appropriate; that it is thread safe (`⎕DMX` is local to each APL thread – which is not the case for `⎕DM` and `⎕EN`) and that it is local to the code which is invoked to handle an error, in such a way that successfully handled (trapped) errors will leave no trace of the handled event.
- Performance Improvements: including much faster processing of lines which contain no code, speedups to most cases of dyadic iota (Index Of), a couple of new idioms `0=⊃⍴` and `0≠⊃⍴` , and finally significant speed-ups to the performance of expressions of the form `(n↑1)`.
- URL string support: URLs in the session or tracer/editor are underlined. Control- and left-click on the URL string will cause the URL string to appear in the default browser (or the default e-mail client for mailto: URLs).
- Enlist in selective assignment: Enlist (`∊`) may be used in selective assignment expressions.
- Large arrays: version 13.1 marks the final step in adding support for unlimited array sizes. All primitives and the component file system now support arrays of any size.

Release Notes for version 13.1 (and all other releases) can be viewed online at http://help.dyalog.com, and can be downloaded in PDF format from http://docs.dyalog.com.

### Planned v13.2 Features

We would like to thank the participants of the 2012 BAPLA AGM & Moot, which was held at the YHA Lee Valley Youth Hostel, Cheshunt, in April (http://moot.aplwiki.com/). In 2006, version 11.0 of Dyalog APL introduced support for object-oriented programming in APL, and this included support for editing both classes and namespaces in the form of a single script. As the use of scripted APL code has slowly spread in the APL community, it has become apparent that the editor needs further enhancements (and some bug fixes). The participants of the moot were invited to discuss these issues, and we would like to acknowledge this valuable input, which will be a driver for work going into both 13.2 and future releases. Other candidates for new functionality to be delivered as part of 13.2 include:

- A number of new GUI features to provide support for gradient colouring, transparent effects, and other modern GUI features (in order to allow clients a bit more time to see which way the Microsoft.NET cookie is going to crumble).
- Speedups to scans, summations, and the regular expression operators `⎕R`/`⎕S`.
- Support for all the selective assignment syntax allowed by IBM APL2.
- Callbacks into APL from `⎕NA` calls.

The planned release date for Version 13.2 is January 31st, 2013

### The Dyalog File Server

Due to be released shortly after version 13.2, the Dyalog File Server (DFS), will provide secure, multi-user access to APL component files and native files – similar to the functionality provided by products like SHAREFILE/AP which was used with mainframe APL systems. The TCP-based client/server architecture employed by DFS avoids the need for direct network access to the underlying component files, doing away with the need for network shares.

DFS provides significantly enhanced security, compared to the use of component files in the form of shared files on a LAN. DFS supports username/password style authentication as well as Integrated Windows Authentication (IWA) on Windows platforms. Secure communications can be used between the client and server using Conga’s Transport Layer Security (TLS) support. As a fringe benefit of this project, recent versions of Conga allow you to provide single-sign-on functionality in your own application, if your organization uses Windows domains.

In many typical scenarios the DFS also performs better than the existing component file system. Multiple file services can be configured to help balance the usage loads, and a web-based console will provide logging, usage/performance monitoring, and administrative functions – including the ability to perform full and incremental backups and restore operations without taking the system down.

The DFS will be sold separately from Dyalog APL, and targets enterprise systems. It will initially only be available for Microsoft Windows, but is designed to be portable.

### TryAPL.ORG

As announced in our previous news item, we released an on-line interactive APL workbench at http://tryapl.org, early this year. We are not quite seeing Google-sized numbers but the site has seen an average of 10-20 distinct user sessions per day, and at times the numbers have been spectacular, as they were in the days following the discovery of TryAPL by “reddit”.

We had about 8,000 distinct sessions over a weekend following http://www.reddit.com/r/programming/comments/uu2br/try_apl_is_weird_but_fun/. The server crashed a few times due to a WS FULL in our log file handling code, but increasing MAXWS quickly resolved that! In June, the site was used to teach an afternoon’s APL workshop for a group of students running a variety of operating systems including Windows, Linux and Apples OSX, without requiring the installation of any software!

### APL Training Courses

Speaking of workshops: as was the case the last time we submitted a news report to Vector, Bernard Legrand has just completed another introductory APL course at our head office in Bramley. We are very pleased to be able to report a steady increase in demand for APL training, and expect to be running a minimum of two courses per year in Bramley, in addition to the in-house courses that Bernard regularly teaches at client sites. If you have an APL-related training requirement anywhere in the world, please contact Karen Shaw in Europe or Pat Buteaux in North America or reach all the relevant people at once with an e-mail to sales@dyalog.com.

Karen and Pat’s email addresses are &lt;firstname&gt;@dyalog.com as indeed is almost everyone else at Dyalog too.

### More Details

In-depth articles on many of the issues mentioned above are available in the last two issues of the Dyalog newsletter, which can be viewed at http://dyalog.com/news.htm – look for the “newsletter” links in the left column. The best place to catch up on all things Dyalog is of course to attend our annual User Conference. The next conference will be held at the Embassy Suites Hotel on Deerfield Beach, between Boca Raton and Ft. Lauderdale on Florida’s Gold Coast, October 20-24, 2013. Recordings of talks from the recent conference in Denmark will be posted to http://videos.dyalog.com and on YouTube (search for ‘Dyalog Conference’).
