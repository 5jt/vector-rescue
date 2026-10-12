---
title: 'Industry news: Dyalog, Kx Systems, Optima, IBM'
volume: '24'
issue: '4'
page: '10'
unindexed: true
transcribed: 'from the typeset issue v244.pdf, pages 10–15 (printed 10–15); Claude, 2026-10-12'
review: draft
tags:
- implementations
- APL community
queries:
- "Printed heading “Industry News”, with unsigned news from Dyalog, Kx Systems, Optima Systems and IBM under their own headings. Printed 16 begins the APL2010 reports."
- "Kept as printed: “IEEE-745 2008” (the standard is IEEE 754-2008); “significant faster”; “Regexs”."
---

## Dyalog

Although we did not manage to get any new releases out the door during this calendar year (v12.1 was released in the last quarter of 2009 and v13.0 will be out in Q1 of 2011), we have had a very busy year!

### Version 13.0

Version 13.0 of Dyalog APL will be Beta-testing in January and should be released in March 2011. As usual, it will be available in 32- and 64-bit versions under Microsoft Windows, AIX and Linux (and for Solaris on demand). V13.0 will break significant new ground on a number of fronts:

First (because it caused us the largest headaches), we have been working on adding support for 128-bit decimal floating-point numbers, implemented according to the IEEE-745 2008 (DPD) standard – with hardware support on recent IBM POWER and ‘z’ processors and software emulation on other platforms. The current 64-bit binary floating-point representation (corresponding to roughly 16 decimal digits) is sufficient for the vast majority of applications, but financial reporting involving multiple currencies can run into problems due to the limited precision (16 digits) and the fact that many decimal numbers cannot be precisely represented, leading to multiple small errors which can become significant if financial portfolios are sufficiently large. Version 13.0 allows the optional use of 34-digit decimal numbers, which avoid all such inaccuracies at the cost of slower calculations.

If you are willing to spend about $10,000 on memory chips, and have enough coffee to get you through the time it takes to )LOAD it from disk, you can now have nearly 128Gb of workspace in memory on ordinary hardware. In version 13.0, most primitive functions are no longer subject to the limit of 2 billion elements per simple array that existed in earlier 64-bit versions. In version 13.1, we plan to remove the size limits for all primitive functions, upgrade our test machine from 32 to 128Gb, and revisit other strategies and limits in the interpreter that might come into play when workspaces grow extremely large.

For technical and educational users, we have added complex numbers, which are implemented as a pair of 64-bit binary floating-point numbers (we do not think there is much of a market for 2x128-bit decimal complex numbers). Our implementation follows the extended ISO APL standard (ISO/IEC 13751:2001), and should be identical to that found in IBM APL2, SHARP APL or J.

Although APL applications tend to have a numerical focus, APL is also a terrific language for connecting things together; massaging, cleaning and redistributing data for use by APL code or indeed applications written in other languages. An important missing link has been integrated support for regular expressions. Regexs have become a tool that most young computer scientists, software engineers or hackers pretty much take for granted and miss when they move to APL. Version 13.0 contains our first system operators, one for searching and one for replacing using regular expressions as implemented by PCRE, one of the most widely used regular expression engines available today.

Version 13.0 also adds a number of good ideas pioneered by other array language dialects. *Take* (`↑`), *drop* (`↓`) and *squad indexing* (`⌷`) allow short left arguments (you only need specify what to select on leading dimensions, as in SHARP APL). We have implemented the functions *right* `⊢` and *left* `⊣`. We have also been inspired to implement a much simpler yet more powerful application profiling tool, after seeing Richard Nabavi demonstrate `⎕PROFILE` in a recent release of APLX.

The addition of the two new numeric data types mentioned above has forced us to revisit a number of algorithms, in particular *index of* (dyadic `⍳`), *matrix inverse* (`⌹`) and the *gamma* and *beta* functions (monadic and dyadic `!`), with the result that they are not only significant faster (for all data types) but often produce more accurate results.

### Other projects

While the production of new releases of Dyalog APL still consumes most of our efforts, those of you who visited the successful APL2010 conference in Berlin in September will be aware that we have a number of other irons in the fire. The two most important ones are APL# (‘APL Sharp’) and RIDE.

APL# is the name of a new APL Interpreter which will be a native (‘managed code’) Microsoft .Net language. We published the first description of this new language at APL2010, and are inviting feedback from the entire APL community. The .Net framework implements a virtual machine which has significant benefits, such as being able to run APL# applications off a web page in the same way that Javascript applications can run without first being installed – but also significant drawbacks, like making it hard to implement the extremely simple and efficient data model that native APL interpreters provide.

APL# will not be a replacement for Dyalog APL, but a slightly different APL system that will allow APL to be used in ways which are not possible today. We hope to make the first prototypes of APL# available for experimentation (as a free download) around the middle of 2011, and keep APL# as an experimental system for at least a year after that before considering a commercial release.

The Remote Integrated Development Environment (RIDE) is the name of a new front end that we are building to provide an identical graphical development environment for APL# and Dyalog APL, on all platforms where either interpreter is available. This will allow us to unify the user experience for developers running APL or APL# locally – or on remote machines running Windows, UNIX and Linux – even when APL is running on servers which would otherwise not be accessible for debugging. Early versions of the RIDE will start to appear in the late spring or summer of 2011, but general availability is unlikely before the second half of the year.

You can watch John Daintree introduce the RIDE at APL2010 – and a number of other interesting presentations which we recorded at that conference – at http://video.dyalog.com/APL2010/.

### Manpower

We have recruited two more developers, and our good fortune in finding excellent developers has continued! Jay Foad joined the team in May and is now working on the core interpreter, and Liam Flanagan who came on board in September is working on .NET, GUI and other interfaces. 2011 will get off to a perfect start as we provide a little balance to the newcomers by welcoming an array language legend into the team: Roger Hui has been helping us with performance enhancements for some years; we are incredibly pleased and proud that Roger will be working for Dyalog in an almost full time capacity from January – with a little of his time fenced off to continue his work as the chief architect and implementer of the J programming language!

From the middle of November to February of 2011 Ronald Chan, the first winner of the Dyalog Programming Competition back in 2009, is braving the (record) English winter in order to be an intern at Dyalog during his New Zealand summer holidays. Ronald is a wonderful mathematician and C coder; in his first month at Dyalog he re-implemented matrix inverse and the beta and gamma distribution functions for all our numeric types, resulting in faster and more precise results all round! Over Christmas, Ronald has been playing with a model of an interface to the R programming language. We will be sorry to see him return to University to attack a PhD in February, and hope to see him again in the future!

In addition to new employees, we have been very happy to collaborate with a growing number of external APL consultants who have helped us develop and test code in 2010. Peter-Michael Hager has been applying his combined APL and cryptographic skills to help us design a comprehensive Cryptographic Library for APL, which will provide cross-platform access to fast algorithms for hashing, symmetric and asymmetric encryption using a variety of algorithms. We would also like to thank Kai Jaeger, Michael Hughes and Brian Becker, who presented recent work that they have done in collaboration with Dyalog on tools for Dyalog APL, at APL2010.

By the time this is in print, we hope to have hired one or two full time APL developers in order to be able to accelerate the development of tools and interfaces written in APL. Over the next few years, it is our ambition to augment the enhancements that we have been putting into the interpreter with a comprehensive set of application development tools for APL developers, and to work hard on sharing these with the APL community on our own web page, on the APL Wiki and other online forums.

Keep an eye on the Dyalog web page in 2011! If you have not already done so, subscribe to the new Dyalog forums at http://forums.dyalog.com – you do not need to be a user of Dyalog APL to do so. The Forums are getting livelier all the time and have become our primary channel for formal and informal announcements including FAQs. In 2011, we also expect to make increasing use of our Twitter and Facebook feeds as distribution channels for news.

## Kx Systems

Kx Systems, the leader in high-performance database and time series analysis, today announced that Guosen Securities Co. Ltd, one of China’s top-tier securities firms, has signed an OEM license deal for its kdb+ database. The database platform will power the investment bank’s algorithmic trading system, which will be embedded into Guosen’s offering to its corporate clients.

kdb+ allows vast amounts of data to be accessed and processed with minimal latency. With a single format for both real-time and historical data, kdb+ provides performance and flexibility for high-volume, data-intensive analytics and applications.

Hanxi Liu, GM of Guosen Securities’ IT department commented: “Choosing kdb+ was an important strategic decision for us. The sophistication of Kx’s programming language and the addition of its calculation engine to our new algorithmic trading system provide us with a great competitive advantage and the optimal balance of speed and simplicity. Kx has made a serious commitment to the Asian market, and its industry knowledge and superior solutions have made the company a serious contender in the local arena.”

Chris Burke, Director of Asia Pacific, added: “We are seeing rising data volumes across Asia, growth in algorithmic trading and increasingly stringent, data-intensive risk management processes. At the same time, companies are looking to drive down latency at all levels. The kdb+ platform was designed from the outset with this dual challenge in mind, and its combination of speed and flexibility has proven to be very compelling. We are delighted to be expanding our Chinese client base with such a well-respected name as Guosen Securities.”

This announcement follows the opening of Kx’s Hong Kong office two years ago to support its locally-based international clients, as well as the domestic financial community. Kx’s ‘Growth via Partnership’ strategy with First Derivatives and Symagon has been extremely successful, resulting in several new relationships and the expansion of global clients into the Asian market.

## Optima Systems

Seems like a very long time since we last communicated and much has happened.

Firstly our prime customer has, after many years, made us strategic to their business. This makes a huge difference to us and places additional responsibilities at the same time. So why their change of heart? Well, put simply, using APL in the way we all love to use it and by avoiding administration, committee meetings and the usual ‘large organisation drag’ we have been able to show that systems can be delivered on time and on price and that this performance can be relied upon.

Secondly we have started to build a new software model in APL to deliver time series clinical data in new and intuitive ways. Whilst our solution is not pure APL, all of the heavy-duty analysis and grunt work certainly is. We are currently experimenting with new (to us) technologies to deliver the final user interface and hopefully provide the necessary wow factor. I hope to be able to demonstrate some of this work in future APL conferences.

We attended the Berlin APL 2010 conference and enjoyed it very much. It was very refreshing to see so many active APLers in one place and, more importantly, so many young faces. As always the conversations were fast and furious and I feel sure that the world was ‘put to rights’ many times over.

I remain unsure where 2010 has gone but very much look forward to 2011. Much is going on and much more remains to be done. Another busy year beckons.

## IBM

The IBM APL Products and Services group is pleased to announce Service Level 17 for Workstation APL2 for Multiplatforms Version 2.0. This new service level was made available on November 11, 2010 for all Workstation APL2 platforms (AIX, Linux, Sun Solaris, and Windows.)

Along with fixes for customer-reported problems, Service Level 17 contains several enhancements.

In the interpreter, the performance of the find primitive is improved for right arguments of rank 2 or higher. When running under the Calls to APL2 facility, the execution stack is now available to the calling program on error. In the DEMOJAVA workspace, the XML2APL function has been updated to support DTD addresses, and a new function, JAVA_PRINT, prints APL objects using Java print services.

On Windows, a session manager system option has been added to control the workspace size of watch windows, and the line number popup window in the object editor has new choices for ‘Trace this line’ and ‘Stop this line’. New key shortcuts include Ctrl+Double-Click to mark a token, Ctrl+Shift+Double-Click to localise or unlocalise a name, and Alt+PageDown to move the current line to the top of the window.

Further information on the new facilities will be found in the updated APL2 User’s Guide and on-line help after installing Service Level 17. A complete list of fixes included in this level will be found in the updated README (Unix systems) or Service Information (Windows systems) file.

The APL2 Service Level 17 download is available to customers with a Software Maintenance contract, through the Support link at the APL2 web site:

http://www.ibm.com/software/awdtools/apl
