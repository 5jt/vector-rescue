---
title: I-APL for the IBM PC
authors:
- Dave Weatherby
volume: '4'
issue: '3'
page: '37'
unindexed: true
transcribed: 'from page images of VOL.4-NO.3-JANUARY-1988.pdf, pages 39–44 (printed 37–42); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
- education
queries:
- "Contents line “I-APL for the IBM PC”; the printed heading is “AN INITIAL LOOK AT I-APL”."
- "The benchmark table is printed in a typewriter APL font, ruled with lines of ‘=’; it is given here as a table, with the expressions as code, and the notes as code blocks. The absolute-value expression is printed with a glyph like ‘!’ (z←!vr); it is read as | (z←|vr), the stile being bolder than usual in this font."
- "Kept as printed: in Note 2, fib sets r←1 1 but then appends to z (and its label is “1:”); the Tutorial is credited to “Linda Alvord and Norman Thompson” (Thomson); “the the familiar del function”; “encylopaedia”; system functions “such as Lnc” (presumably ⎕NC, the quad lost in print); “Name lists”."
- "Availability: the street address of I-APL Ltd (2 Blenheim Rd., St Albans, Anthony Camacho’s home address, omitted from his letter in this issue) is omitted for consistency; for review."
---

## An Initial Look at I-APL

*by Dave Weatherby*
{ .byline }

### Introduction

This Christmas I got the opportunity to try out a pre-production version of I-APL, the shareware APL that was born at APL86 in Manchester. I-APL's objective is to enable anyone, especially schools, to try out a good quality implementation of APL on the machines that they already possess. I-APL is designed to be run on almost any micro with a minimum of 64K memory, and versions should soon be available to run on the BBC and RML micros which are the most popular in British schools.

In my view the long term future of APL will depend on its acceptance in schools and so I jumped at the chance of a preview of I-APL. However a family Christmas and reviewing APL do not fit very comfortably together and therefore this article should be seen as an initial look at I-APL rather than an in depth review. In any case I have only been able to use I-APL on the AMSTRAD PC512, an IBM PC clone, whereas a full review needs to test out its performance on a number of different machines, especially the BBC micro. In addition the supplied workspaces that I was given were not the final versions.

### What You Get

The complete package costs £11 plus postage and packing and consists of the following:

> Floppy Disc with APL interpreter and Workspaces<br>
> An Instruction Manual (52pp)<br>
> Tutorial (48pp)<br>
> Language Encyclopaedia (296pp)

The floppy disc may be copied and distributed freely, although the manuals are subject to normal copyright. So if you already know APL or prefer to use it in conjunction with other APL books then I-APL can be yours for the price of a floppy. The I-APL committee have decided not to distribute the floppy on its own but they will supply the manuals individually. I imagine that the various Shareware distribution groups will be happy to provide copies of the floppy at their normal rates.

### Getting Started

The supplied floppy disc had a READ.ME file that explained the parameters I needed to specify to get APL characters on my CGA screen. Hercules and EGA are also supported and for those without any graphics an option is provided which uses ASCII symbols instead. I-APL loaded within 10 seconds - a real relief from the 40 seconds or so that I am used to with STSC APL. Typing `⎕AV` displayed upper and lower case, normal and underlined characters as well as all the standard APL characters plus a few extras such as match, epsilon-underlined and the British pound sign. Resolution on my CGA screen was reasonable, although the overprinted characters are not easy to read.

### Keyboard Support

APL's special character set is a big advantage in communicating easily with the computer, but poses problems for APL implementers and popularisers. The I-APL ASCII option mentioned above does not provide a keyword APL as pioneered by MicroAPL; it merely gives a one-to-one arbitrary mapping between APL and ASCII symbols. The authors of I-APL clearly expect users to have access to APL characters. All the documentation uses APL symbols exclusively and would therefore require those with no APL symbols to perform a continuous translation. Despite the attempt to make the ASCII symbols relate to their APL equivalents I believe that very few people are likely to get through this process.

I-APL allows upper case characters to be entered from the keyboard using the shift key and the APL characters are entered in normal lower case. Upper and lower case ASCII characters can be entered by toggling the INSERT key. I-APL follows IPSA and STSC in providing a keyboard mapping of APL characters that is a union with ASCII. For example the minus and plus signs are in the same position as for the standard ASCII keyboard, rather than in that of the traditional APL keyboard mapping. The STSC and IPSA union keyboards are slightly different and I-APL has a totally different mapping again, so that there are now at least 3 different union keyboards. It might be better named the disunion keyboard!

I-APL has chosen to link the APL character keyboard position to that of the similar ASCII symbol. So epsilon is lower case E and iota is lower case I. However more controversial is the decision to link the not equals symbol to lower case Z due to similarity of shape, or grad up and grad down to lower case q and lower case d respectively. The overall effect is that the keyboard mapping is quite different from any other APL I have seen. While this may not be a problem for newcomers to APL it will cause them irritation if they graduate to other more powerful APLs.

I do not believe that the mnemonic nature of I-APL's layout is sufficient to justify a wholly new keyboard layout, especially as those mnemonics rely on lower case letters while most keyboards are labelled with upper case characters. I suggest that I-APL follows the union keyboard approach of normal ASCII for the first and shift character sets with more specialised APL characters available via the INSERT toggle key.

### The APL

The APL itself conforms to the draft ISO APL standard and even offers some facilities beyond the standard. For example grad up and grad down work on character matrices, and the replicate extension of compress as well as stop and trace are all provided. No file access or screen driver facilities are provided. However a method of calling machine code is included, which I understand will be used to create workspaces offering these and other facilities.

During my use of I-APL I did not notice any bugs and was certainly never dumped back in DOS, despite hitting keys at random while the interpreter was executing. Hitting CTL-C did confuse the screen display somewhat, however my general impression was that the APL is solid.

A good implementation of direct definition is also provided and, although its use in large scale applications may be controversial, it undoubtedly simplifies function creation as well as encouraging a modular programming style. Functions may also be defined using the the familiar del function. Direct definition functions are treated slightly differently from standard functions in that they cannot be suspended and appear in listings with a colon as the last character of their name. An example of the care which has been taken with this APL is that `⎕FX` has been extended to create direct definition type functions. A function is also provided to convert from direct definition form to del form.

I hope very much that other APL vendors follow I-APL's lead in offering direct definition as an integral part of their APLs.

Variable types include 1-bit boolean, 2-byte integers and 6-byte reals. I-APL has therefore sacrificed some accuracy to minimise memory requirements. On my Amstrad I had a useful workspace size of 31624 bytes and, since I-APL only makes use of 64k of memory, I assume that the workspace size would be very similar on other machines. The documentation states that compromises between speed and memory have always been resolved in favour of memory in order to maximise the workspace available.

### User Interface

The user interface is simple. In-line editing is provided, but there is no scrolling memory. The last line executed can be recalled for editing but not any previous lines. However the interface is intelligent enough to define the last line as the last immediate execution line and ignores system and editing commands.

I am very used to scrolling memory and would have willingly swapped workspace size for a page or two of scrolling session log. I suspect that beginners will miss it even more. It would be very attractive to have a parameter to allow multiple page session logs at the expense of workspace size.

### Speed

Given that speed has been sacrificed for space it would be surprising if I-APL was very fast. The table of benchmarks shows a comparison with STSC APL and clearly indicates, as expected, that STSC APL is probably at least 15 to 20 times faster in normal circumstances:

<p style="text-align: center">BENCH MARK FOR I-APL AND STSC APL VERS 6.3<br>
ALL TIMES IN SECONDS ON AN AMSTRAD PC512</p>

| OPERATION | | I-APL | STSC |
|---|---|--:|--:|
| Plus reduction | `z←+/vi` | 1.49 | 0.43 |
| Logical reduction | `z←∨/vl` | 0.14 | 0.005 |
| Maximum reduction | `z←⌈/[1]mi` | 0.44 | 0.023 |
| Exponentiation | `z←vi*.1` | 95.9 | 26.220 |
| Absolute value | `z←\|vr` | 0.68 | 0.38 |
| Indexing | `z←vr[vi[⍳20]]` | 0.48 | 0.017 |
| Sorting | `z←vi[⍋vi]` | 5.15 | 0.45 |
| Take | `z←¯2 1↑mr` | 0.15 | 0.022 |
| Membership | `z←vi∊vi` | 3.44 | 1.81 |
| Transposition | `z←2 1⍉mc` | 1.66 | 0.056 |
| Outer product, characters | `z←vc∘.=vc` | 2.22 | 0.072 |
| Outer product, integers | `z←(⍳50)∘.+⍳50` | 7.76 | 0.208 |
| Inner product, reals | `z←vr⌊.+vr` | 2.63 | 1.37 |
| Matrix division | `z←mr⌹10↑vr` | 7.03 | 0.36 |
| Fibonacci series (note 2) | `z←fib` | 28.78 | 2.21 |
| Multiplication | `z←vr×3.14` | 2.87 | 1.36 |
| Division | `z←vr÷3.14` | 7.95 | 1.82 |
| Logarithm | `z←⍟vr` | 39.08 | 13.98 |
| Sine | `z←1○vr×.1` | 39.47 | 17.95 |

Note 1: The variables used in the benchmarks are defined by

```apl
mi←10 10⍴vi←(500⍴0 1 0 0 1)/⍳500
vl←1 0 1 1 0 0 0 1
mr←10 10⍴vr←vi+0.1
mc←26 26⍴vc←'abcdefghijklmnopqrstuvwxyz'
```

Note 2: The function fib is defined as

```apl
∇r←fib
  r←1 1
  1:→(100>⍴z←z,+/¯2↑z)/1
∇
```

The more important point however is whether I-APL is fast enough for teaching purposes. In my view the results show that I-APL is certainly fast enough for educational purposes and may even be fast enough for real applications in some circumstances.

### Documentation

I was given a pre-release version of the documentation and cannot comment on its presentation, and so the following remarks are restricted to content only.

1. Tutorial. The Tutorial by Linda Alvord and Norman Thompson is clearly designed for those with a theoretical bent. The terms 'scalar' and 'vector' are introduced quickly and are followed up with the use of the term 'argument' with very little explanation. However I assume that the expected audience will be largely teachers of maths and science and so the presentation is probably appropriate. The topics covered emphasise probability theory, matrix inversion and the use of simple graphics to investigate functions. Again the emphasis is on the use of APL in the teaching environment. Given the assumed target audience of teachers and theoreticians the Tutorial provides a good introduction to APL. It is unlikely however to appeal to the teenage hacker or computer freak.
2. Instruction Manual. The Instruction Manual is designed to show how I-APL runs on a particular machine. I was very impressed with the level of detail provided about the way data is stored and how the APL primitives are calculated. Such information may not be used often but gives real confidence in the integrity of the system. It also emphasised the rigour of APL in comparison to languages such as LOGO. My main criticism of the Instruction Manual is that the instructions on how to load APL were relegated to an Appendix. It would be preferable to have a section labelled 'Getting Started' for those users, such as myself, who cannot wait to read all the documentation.
3. Encyclopaedia. The Encyclopaedia attempts to give information about the I-APL language in general rather than any particular implementation. I did not get enough time to really assess the quality of the information given but what I saw appeared well written and comprehensive. However I was not convinced that the format was well designed for easy reference. For example system functions such as Lnc are to be found in the list of contents under 'Name lists'. This is not helpful when trying to understand someone else's code. Moreover any item given in the list of contents is not given in the index which requires the user to look in two places. The encylopaedia needs a better index and one that attempts to index APL characters in a similar manner to that in Paul Berry's Sharp APL.

Overall the quality of the documentation was good, although it would have been useful to have had a brief introduction to what was on the floppy and what each of the manuals were for. The orientation of the documentation is geared to the theoretic or academic user of computers rather than the home or small business user wanting to get the computer to do something useful. Personally I believe this orientation is correct but it is important that the package gets exposure to the right audience.

I think it would be very helpful to include a practical application of APL, such as the workspace NATIONS as presented at the Helsinki APL conference by Paul Berry and Michael Berry. Such a workspace illustrates how simply APL can create database type applications as well as providing good examples of APL code. Although the importance of reading APL as a means of learning has been stressed by Iverson, the I-APL documentation provides little opportunity for doing so.

### Supplied Workspaces

I am unable to say much about the supplied workspaces since those that I saw were not the final versions. However I am told that workspaces will be available which provide the APL functions in Linda Alvord's book on probability, in the APL Tutorial and in the APL Encyclopaedia. In addition workspaces will be provided that give access to simple turtle colour graphics, give access to DOS files, provide functions similar to `⎕WPUT` and `⎕WGET` in STSC APL and offer simple APL tutorials. Clearly some of these workspaces are specific to the PC, but, no doubt, similar facilities could be provided on machines such as the BBC.

### Overall Assessment

I-APL for the PC is a full implementation of the APL standard with some workspaces that offer significant extensions. The orientation of the product is for teachers of analytic subjects such as maths and probability. The availability of a colour graphics workspace should enable I-APL to emulate LOGO's turtle graphics and this should help APL to be accepted by the education community. Overall this is an impressive product and deserves to be a Shareware classic.

### Availability

> I-APL (ISO APL with graphics, file access and screen handling)<br>
> I-APL Ltd., [street address omitted], St Albans

> PRICE: Software free, documentation £11
