---
title: 'Vendor Forum: 20th April 1990'
authors:
- Adrian Smith
volume: '7'
issue: '1'
page: '60'
unindexed: true
transcribed: 'from page images of VOL.7-NO.1-JULY-1990.pdf, pages 62–68 (printed 60–66); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “notes by Adrian Smith”."
- "Printed 66 ends the piece, its lower half blank; “J: An Informal Introduction” (art10003990) begins on printed 67."
- "The floating-point benchmark is printed as two domino glyphs, given as `⌹⌹`. The `)WATCH` syntax is printed “)WATCH IOTA; Z” with a space after the semicolon, given without it. The assignment arrow in `TOTAL←+/` is printed as a left arrow."
- "Adrian Smith’s sign-off address (Brook House, Gilling East, York) is kept: it is the business address of APL 385 in this issue’s APL Product Guide."
- "Kept as printed: “Jim Brown has asked him to hold back”; “Dyadic systems may have chafed”."
---

*notes by Adrian Smith*
{ .byline }

## Highlights

This was an interesting and worthwhile meeting, at least as much for what was not said, as for what was said. I.P. Sharp were conspicuous by their absence; I think we can reasonably conclude that Sharp APL is now a 'stabilised' product, and that they simply had nothing interesting to say about the future.

Slightly more surprising was the fact that neither STSC, nor MicroAPL had anything much to say either. This was in sharp contrast to previous meetings, where STSC were keen to stress the future convergence of their APL platforms (the obvious ones being APL\*PLUS/1000 and APL\*PLUS II) on a common standard. The impression I gained was that STSC are now taking a 'cash cow' approach to APL in general, and a 'dead dog' approach to their mainframe system. MicroAPL were also keen to stress stability and portability; in particular they majored on the benefits of free runtime, with some impressive examples of user-developed Mac packages.

The two outfits which did have something to say were IBM and Dyadic. Under the cover of a standard disclaimer, Dave Selby proceeded to tell us about his current research into APL2/PC; the 32-bit packager, and a totally new session manager are the key elements. Following in the wake of Pete 'n Pam (now coyly renamed as P&P, I regret to say), Dyadic have just been born again as Pete 'n John 'n Pauline (and the Royal Bank of Scotland). In short, they have just bought themselves out, and with one mighty bound have escaped from the clutches of both Lynwood and Hunting plc. Long may they prosper! John Scholes showed off a bit more of their new environment (see the review of this on page 49), with some fascinating additional (very experimental) bits for watching variables, both local and global. I think I am going to like this!!

Now to the talks proper: it was agreed that Dave Selby should bat at number-1, but following some haggling on the current value of `⎕IO`, Romilly Cocking started proceedings at number-0 ...

## Romilly Cocking, representing APL\*PLUS

Romilly saw the current APL marketplace split up between:

- the core APL users, who rely extensively on APL for critical corporate systems. Even those who may decide now to get out of APL will need 5-15 years to achieve it. These users need stability and connectivity; they are interested in performance and support costs.
- power personal computing. They want more `⎕WA` and more speed. They are beginning to get interested in connectivity and workstations.
- vertical-market developers, producing closely targeted software in APL. They need developer productivity, communication with other languages, and a stable, long-term platform.
- Info Centre diehards. They want to carry on running ADRS and ADI - that means continued support for VS APL.

Next, Romilly turned to the APL\*PLUS product family:

- mainframe APL. This is a mature market, where the revenue from maintenance agreements now exceeds the revenue from new licences. There is almost no drive for new features, except in the Sharefile arena, where enhancements to support networking and workstations are being worked on. These are likely to be 5 years away from the marketplace.
- workstation and mid-range APL. At long last the Unix market is growing from a significant installed base; in the UK it is being driven by UK subsidiaries of US companies. Many of the above 'core' users are looking hard at Unix opportunities, in particular STSC have come under unexpected pressure to port to the RS/6000 workstation ... maybe this will be at APL90?? We can look for graphics and X-windows interfaces in these APLs.
- APL\*PLUS II. A pleasant surprise, as sales have been way over plan! The next release will be around in late summer / early autumn, and will feature a 'high' session manager (about 140K more space in the DOS box), more interfaces through `⎕NA`, and better comms and network support.
- APL\*PLUS/PC. This seems not to have been hit by the APL\*PLUS II launch, so it is obviously in a different segment of the market. The main pressures are towards enhancing the development environment, with windowing-type debuggers, similar to MicroSoft Codeview. (There was a fairly broad grin on John Scholes' face at this point ... I think he agreed with the idea!) Other things to look for will be better interfacing (sooner or later `⎕NA` will turn up), and good behaviour under OS/2.

Romilly was asked about APL\*PLUS/PC pricing, and the implications of dongles on APL\*PLUS II. He thought that an APL\*PLUS/PC 'Developer's Kit' was unlikely, as STSC were milking a growing revenue stream from all those vertically integrated software products. However there was the possibility of a corporate runtime for existing APL\*PLUS/1000 mainframe sites. Romilly removed his STSC hat for long enough to admit to a thorough detestation of dongles, but was pessimistic about the future. In answer to "When will the dongle go away?" he replied " ... when the Italians get honest!". Following recent experiences with Statgraphics, I would give him all the support I can in keeping APL\*PLUS/PC undongled. Romilly also mentioned in passing the availability of 'partial' systems (basically software only with no documentation) at much reduced prices .... please can we have a product guide entry!

## David Selby, representing APL2/PC

Being an IBMer, Dave had to prefix his talk with a disclaimer, pointing out that anything he said was purely hypothetical, and in no way represented an announcement, a statement of direction, or anything else! The reader is warned.

Dave covered 'work in progress' on both the interpreters themselves, and on the various auxiliary processors that go to make up the complete system:

- the 16-bit system gets a proper implementation of `)CONTINUE`, `)SINL` and `)LIB`. The SVP storage allocation is improved, and will hopefully be Camacho-proofed (see Vector 6.1 page 58). Parameters can be passed from the DOS command line, and there is a new `TIME` utility to monitor code performance and flag 'hotspots'.
- the 32-bit system has a number of performance improvements, and is extended to handle complex numbers. There is also the option to load most of the interpreter high, leaving a mere 30K in the DOS box. APL2PACK.EXE has an improved user-interface, and will package 32-bit code, to be run (with no license implications) by APL2RUN.EXE.
- AP120 - the session manager. Dave admitted to this having been "the bane of my life" in the current product. It is rewritten from the bottom up, although the screen layout has been preserved, and it can still be used in 'page-mode'. However, it now does sane things when you type off the edge of a line (you just push the screen across to the left), it will scroll with the arrow keys, and can run split-screen, with a graph in the other half of the screen. You can journal the session to file, or printer.
- AP124 - full-screen processing. Extended to handle character arrays better, and to give 'selectable' fields for menu operations.
- AP210 - much faster reading of simple DOS files, with a user-defined translation table. (EBCDIC to ASCII is provided as the default option.)
- Other odds and ends: Hercules+ support; Mouse support; Font editing and codepage creation; on VGA graphics "it was very stupid of us not to put this in the original product".

Dave was asked about selective specification, and `⎕NA` support. He replied that the theory of selective specification was still not fully understood, and that Jim Brown has asked him to hold back; he felt that a general `⎕NA` is hard to do, and it would not be in the product in the foreseeable future.

## Anthony Camacho, representing I-APL

Anthony reported that the original objective of I-APL had been met, with the implementation of a working interpreter, and the sale of over 2,000 copies of I-APL and supporting documentation. Lots of ports were still in progress, but I-APL was now available on more than half the initial target list. He was at pains to point out that I-APL was in no way in competition with any commercial APL, and that he frequently recommended users to move towards an existing commercial APL when they outgrew the limitations (e.g. a 28K workspace on the IBM PC) of the free system.

Getting schools to use I-APL in the classroom remains a slow process, but it is beginning to get a following among both teachers and pupils, who form the bulk of the 1600+ mailing list. (Incidentally, it was good to see "APL in the Mathematics Classroom" recommended in the April Byte.)

The major work in progress is the development of a 32-bit version of I-APL to run on the Archimedes system; this has required a thorough rehash of the transcendental functions to give full IEEE precision.

## David Eastwood, representing MicroAPL

David took us on a guided tour of MicroAPL's first 10 years, from hardware breakthroughs like the first double-sided floppy disk, to the Sinclair QL. MicroAPL still service 3 of their original CP/M systems, which is an interesting comment on the longevity of some computer applications. He emphasised the importance of their free runtime policy, and low price, in generating a stream of Mac applications which were impossible to tell from any other Mac system. Over 85% of these systems are overseas, mostly in the USA and Germany. David demonstrated three systems, all built by end users with no MicroAPL support: a superb starmap (complete with planets if you can find them); a program to assist
in downloading Reuters data; and a program to help with Cladistic analysis (whatever that is!).

MicroAPL have recently been appointed Value Added Retailers for the NCR 'Tower' range, so expect some interesting announcements at APL90.

## Peter Donnelly & John Scholes, representing Dyalog APL

Peter started with the details of Dyadic's management buyout: as from the end of March the company is in the capable hands of Peter, John, Pauline (of Mexican Snacks fame ... see Vector 3.2 page 78), and the Royal Bank of Scotland. Peter was clearly delighted that they could now get on with the job of pushing forward their APL systems, without constantly having to justify this odd activity to their paymasters.

Peter was also rather chuffed to announce a complete range of RS/6000 systems, running Dyalog APL. He quoted some benchmarks for these, which I failed to copy down accurately, but which basically put this platform a good factor of 10 ahead of the fastest 386/PC on the market. The floating-point performance is phenomenal, with a `⌹⌹` benchmark coming out around 40 times faster; this is getting within a factor of 10 of a 3090 mainframe, all for around £50,000 ... no wonder Dyadic are excited about it.

> "You can do all sorts of crummy programming on these machines, and get away with it!"

John Scholes followed up with another live demo of his new toy, this time demonstrating the incredible feat of programming a recursive function:

```apl
      IOTA 12
1 2 3 4 5 6 7 8 9 10 11 12
```

The interesting bit was to watch this executing line-by-line on screen, with the 'trace' windows automatically stacking and vanishing as the recursion unwound.

Several bursts of spontaneous applause marked this show (suggesting that Dyadic must be getting something right), but the best was yet to come. John saved his work, then gingerly loaded an experimental system, and showed us `)WATCH`. This lets you 'watch' the state of any variable, the object in question being shown in a pop-up window at the top of the screen. It happily handles numeric and nested data, and allows you to tab to the window and scroll it around if the variable is too big.

John tried watching the result variable of the recursive `IOTA`, (syntax `)WATCH IOTA;Z`) which gave a stack of windows of gradually increasing width (1, 1 2, 1 2 3, etc.) which peeled off the screen as the functions vanished from the stack. The whole show took about 1/5th of a second ... this is **fast**!

John was happy to take questions about the future of this product, but was as yet unsure as to its final form; in particular he would like to see it integrated with a variable editor, similar in form to the function edit/trace capability. When asked about `SI DAMAGE` when you edited suspended things:

> "There is no SI DAMAGE in Dyalog APL; we didn't think it was a good thing to have."

## Summary

From the evidence of the day's talks, I would draw the following conclusions:

- Sharp APL is almost at the end of the road, unless someone can raise the cash and commitment to buy it back from Reuters. This makes me rather sad, as Sharp have always been in the forefront of interpreter design, and their APL is still ahead of the competition in many important areas.
- STSC have a problem. APL\*PLUS/PC has not moved significantly since release-5, and is existing increasingly on maintenance (disguised as upgrades) and run-time. APL\*PLUS II has rather a short life ahead of it, unless it can drop its price to compete more effectively with APL2/PC, and free 32-bit runtime. In the increasingly vital workstation market, Dyalog APL has a substantial lead, both in the platforms supported, and in the quality of the development environment. The APL\*PLUS/1000 mainframe product is moving rapidly from 'cash cow' to 'dead dog' status, as the mainframe becomes increasingly marginalised by distributed systems.
- IBM may just have got it right with the (hypothetical) release 1.2 of APL2/PC. Just as it took Lotus to version 1.01A to home in on an acceptable product, IBM have addressed the obvious deficiencies in the initial system, and look to me to have a winner in the making. I just hope they don't fluff it!
- MicroAPL have got themselves a really cosy niche as the only viable APL for a whole range of 68000-based machines; they deserve every credit for going for growth with cheap pricing and free runtime, not sitting around raking in easy money.
- Dyadic systems may have chafed under the yoke of a watchful paymaster, but I wonder if it did them some good by squashing some of the more exotic ideas at birth? I have always felt that they treated their APL as an interesting toy, and had a tendency to fill it with fascinating ideas (like `TOTAL←+/`) just because it was interesting to do! I hope they employ a professional devil's advocate; if so I think they have a great future, and are likely to get most of the APL trade going in the lucrative workstation market.

Of course, I confidently expect to be proved wrong about most of the above conclusions; all I can say in justification is that they are an honest reflection of my feelings at the meeting, as rationalised on the train on the way home, and written down the day after!

> Adrian Smith<br>
> Brook House, Gilling East, York<br>
> 21st April 1990.
