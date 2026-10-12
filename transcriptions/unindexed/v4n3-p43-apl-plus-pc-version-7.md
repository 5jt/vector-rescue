---
title: APL*PLUS/PC Version 7.0
authors:
- Adrian Smith
volume: '4'
issue: '3'
page: '43'
unindexed: true
transcribed: 'from page images of VOL.4-NO.3-JANUARY-1988.pdf, pages 45–48 (printed 43–46); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
- performance
queries:
- "Contents line “APL*PLUS Version 7.0”; the printed heading is “APL\\*PLUS/PC Version 7.0”, “reviewed by Adrian Smith”."
- "The benchmark table is set in a typewriter APL font; it is given as an APL code block, glyph for glyph, with its rules of hyphens and equals signs. The Vn. 5 timings repeat the V20(5) column of the table in “The NEC V20 Processor” (unindexed/v4n2-p51-the-nec-v20-processor.md); there the character search is printed with ⍷ (“'FAT'⍷S”), here with ∊ (“'FAT'∊S”), kept as printed."
- "“see 'Hackers Corner'” refers to Hacker’s Corner (1) in this issue (art10008220)."
- "Kept as printed: “where it might pay you to upgrade”; “If you use you APL”; “allow you arrays”; “use it a an ersatz mainframe”; “execeution times”; “flakey”; “⍝” run against “T” in “DO ⎕TS-T⍝” in three lines of the table."
---

*reviewed by Adrian Smith*
{ .byline }

### Background

APL\*PLUS/PC is now firmly established as the world standard in APL interpreters for the IBM PC and compatibles. Clearly a new release is of great importance to the APL community, as it immediately supersedes all previous versions and thus moves a substantial part of world APL development into a new environment.

The purpose of this review is to help you to decide where it might pay you to upgrade from previous versions, where you should stay put, and possibly where you might be better off staying with a previous release. As you will see, APL\*PLUS/PC 7.0 has many useful new features, but there are also some drawbacks which you may like to consider before upgrading.

### Features and Benefits

Some of the new things you can do in version 7.0 are:

- networking. If you are into LANs (as I regret to say I am not yet) you can use `⎕FSTIE`, `⎕FSTAC`, `⎕FRDAC`, and `⎕FHOLD` to do the expected things to preserve file integrity across the network.
- set up a disk file to let APL swop objects automatically in and out of memory. A fair amount of detailed control is possible over the rules by which objects are swopped. This lets you move 'big' applications straight down from 2Mbyte mainframe systems and run them without modification.
- monitoring execution time with `⎕MF`. To some extent the fact that you have a dedicated processor in the PC makes this an unnecessary luxury, but I agree that it is very convenient to be able to use your mainframe functions (assuming you are running APL\*PLUS mainframe) to run monitoring checks on the PC.
- direct graphics output to a wide variety of devices which support the CGI standard. If you use you APL with one of these 'virtual device interfaces' you can run a smaller version of the interpreter without all the old `⎕G`-style graphics functions.
- use the PS/2 to its full capability with 'mode-8' graphics and a downloaded APL font. The VGA graphics in particular I have found fast and impressive; the resolution is now the same as the old Hercules mono standard, but of course you have colour as well.
- VT100 emulation is an option in terminal mode. Your PC can thus be used as a simple monochrome terminal into a VAX system, or into a mainframe with an asynch protocol converter.

In addition there are some new assembler functions, more printers are supported, and there are some speedups to the primitives and to the workspace housekeeping.

### Drawbacks and Reservations

So much for the good points. Essentially these echo the STSC press release, and you can find out more details from any of the vendors. Some of the things they don't tell you are:

- it is a lot bigger (160K against 124K for release 5). You therefore lose some 40K of workspace, and it takes rather longer to load up (16sec from floppy). Even the 'space-saving' version only gets you 10K or so back. What's more you still can't (legally) get rid of the copyright banner. I'm afraid I still tend to implement on 4.2 for this reason alone. (see 'Hackers Corner' for the right places to prod it if you do want your own sign-on banner).
- it is about 20% slower across the board than release-5. There is no measurable difference between 6 and 7, other than in the published speed-ups. As soon as you allow you arrays to stray over the 32K limit, all the timings roughly double. See the table of 'Smith Benchmarks' for full details.
- earlier releases run quite happily on the VGA adaptor using the EGA characters and graphics modes. Personally I strongly dislike the APL font supplied for the VGA, and have replaced it with one of the APL fonts I did for my Hercules card. I shall get a copy of this onto the software exchange as soon as I can. Of course you can use VGACHAR.COM from your Release 7 disks with any earlier release of APL\*PLUS/PC if that is what you want.
- the VT100 emulation looks extremely flakey! I have failed to find any decent documentation (other than the location to `⎕POKE`!) on its use; it also has all sorts of peculiar side-effects (undocumented as far as I can tell) such as resetting `⎕WINDOW` and the default background colour. When running as a VAX terminal it was fine in simple terminal mode, but rapidly became totally confused in a form-based application (e.g. SQL\*CALC); when running as a mainframe terminal through a protocol converter it just made a total dog's breakfast of the screen. I think this one should go back to the drawing board; it is a good idea which deserves proper implementation!

In many ways, I feel that this release of APL\*PLUS/PC is a step backwards. One of the great benefits of the PC is the absolutely consistent response time; as soon as you bring in the concept of paging, you are back in the 'mainframe' environment where the same operation could take differing lengths of time depending on how you got there. To a lesser extent the extension to objects over 32K gives a similar set of problems; a trivial change to the user's data could suddenly double execution times.

From my own experience, it is generally far better to fail the application on `WS FULL` or `LIMIT ERROR` and to fix the code to use less space. A typical example was a 'summarize this by that' expression which did it the VS APL way using plus-dot-times and jot-dot-equals; on Vn5 this failed on `LIMIT ERROR`, so we moved it to Vn6. It then started to fail on `WS FULL`, so we took 10 minutes to rewrite it (extract unique elements and loop round them with plus-dot-equals). It is now back on Vn5, and runs some 30 times quicker than it did before! I have a horrible suspicion that with Vn7 we would just have given it the workspace and hence given the user a slower and less predictable system.

The same sort of thing applies to a little workspace I use to process the output from this word-processor so that I can get it up to our mainframe for laser printing. A typical document is around 20K, so Vn5 handles this quite happily. Moving to 33K forces you to Vn6, and suddenly it is like watching paint dry. I hate to contemplate the possibility of running a complete VECTOR (approx 120K) through Vn7; much better to invest the time in a rewrite which moves down the file in (say) 10K slabs.

In summary, the IBM PC is a 5 year-old architecture, based around 64K segments and a 1Mbyte address limit. Trying to make it pretend that it is a mainframe with 32bit addressing and infinite memory is like teaching a dog to walk on its hind legs; it can be done, but it makes terribly inefficient use of the resources available. Use your PC as a PC, and I think you will be most pleasantly surprised at the power and performance available; use it a an ersatz mainframe and I fear that you can only expect disappointment.

### Benchmark Results

Here again is my standard collection from VECTOR 4.1. As previously noted, the simple 1000 looper FN 1000 seems to be the best indicator of overall speed:

```apl
APL Expression                  Type          Vn. 5  Vn. 7
--------------                  ----          -----  -----
T←⎕TS ⋄ +/V+V   ⋄ DO ⎕TS-T ⍝ INT ....      350    380
T←⎕TS ⋄ +/V[I] ⋄ DO ⎕TS-T ⍝ INT ....       50     60
-----------------------------------------------------------
T←⎕TS ⋄ V+.×V   ⋄ DO ⎕TS-T ⍝ RL  ....      380    440
T←⎕TS ⋄ +/V*2   ⋄ DO ⎕TS-T ⍝ RL  ....     3680   3850
T←⎕TS ⋄ X←+/M   ⋄ DO ⎕TS-T ⍝ RL  ....      660    710
T←⎕TS ⋄ V+.×,M ⋄ DO ⎕TS-T ⍝ RL  ....     2140   2200
-----------------------------------------------------------
T←⎕TS ⋄ +/S='T' ⋄ DO ⎕TS-T⍝ CH  ....     3630   3790
T←⎕TS ⋄ 'FAT'∊S ⋄ DO ⎕TS-T⍝ CH  ....       60     60
T←⎕TS ⋄ X←S∊'FAT' ⋄DO ⎕TS-T ⍝ CH ...     2520   4730
-----------------------------------------------------------
T←⎕TS ⋄ X←B∨B∧~B ⋄ DO ⎕TS-T ⍝ BL....     4840   5550
T←⎕TS ⋄ ∧/B       ⋄ DO ⎕TS-T ⍝ BL....      110    160
T←⎕TS ⋄ X←∨\B     ⋄ DO ⎕TS-T ⍝ BL....      220    280
-----------------------------------------------------------
T←⎕TS ⋄ FN 10     ⋄ DO ⎕TS-T ⍝ FN....      330    440
T←⎕TS ⋄ FN 100    ⋄ DO ⎕TS-T ⍝ FN....     3100   4010
T←⎕TS ⋄ FN 1000   ⋄ DO ⎕TS-T ⍝ FN....    30.3s  41.7s
-----------------------------------------------------------
T←⎕TS ⋄ X←FF∧.='EJD..'    ⋄ DO ⎕TS-T  ⍝    60     60
T←⎕TS ⋄ X←FF∧.=⍉20 5⍴'EJD..'⋄DO ⎕TS-T⍝   33.6s  37.5s
===========================================================
```

All timings on IBM PC with NEC V20 processor (Approx 20% faster than standard 8088-based PC).

### Conclusion

If you need to run on a PS/2 and want to use VGA graphics, you need version 7. If you must (and I mean must) handle large objects in large workspaces, then you need release 7. If you want really detailed analysis of execeution times, or need networking support, or could use the VT100 emulation, then you need release 7.

If none of the above apply, then stick with release 5. It is smaller, faster, and probably better debugged. Personally, I shall continue to stockpile both 6 and 7 in my cupboard, and install from my release 5 disks (or even occasionally from 4.2) unless there is a proven need for the new facilities.
