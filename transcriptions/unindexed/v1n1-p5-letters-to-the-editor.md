---
title: Letters to the Editor
authors:
- Richard Bowman
- Alan Hawkes
- Anthony Camacho
volume: '1'
issue: '1'
page: '5'
unindexed: true
transcribed: 'from page images of VOL.1-NO.1-MAY-1984.pdf, pages 7–9 (printed 5–7); Claude, 2026-10-12'
review: draft
tags:
- language design
- programming techniques
- APL community
queries:
- "The Contents line gives the authors as “Bowman, Camacho & Hawke”; the letters are from Richard (Dick) Bowman, Professor A. G. (Alan) Hawkes and Anthony Camacho, in that order."
- "Following the project rule for individuals’ contact details, the letter-writers’ postal addresses are omitted: Bowman’s street address at the CEGB (85 Park Street, London SE1), Hawkes’s at University College of Swansea (Singleton Park, Swansea SA2 8PP) and Camacho’s home address in St. Albans. The employer’s and department’s names are kept."
- "The glyphs in Bowman’s second paragraph are read as ⌽, ⎕, ⎕← and ←⎕, ⍋ and ⍒."
- "Kept as printed: “Professor Hawke’s views” (Editor’s note); “Alan. G. Hawkes”; “the improved FinnAPL idiom number 49” (Camacho means the original idiom, which his first listing reproduces); neither function assigns its result `R` in its last line, though both headers declare one."
- "The code was checked in Dyalog APL: both functions give the printed results."
- "The lower half of printed 7 is a Delphi Consultation advertisement (“Need help with APL? Then consult the oracle”), not transcribed."
---

Letters should be written with non-APL as well as APL readers in mind wherever possible. The Editor reserves the right to edit letters unless a writer states that a letter is to be published in full or not at all.

*From: Mr. Richard Bowman, 27th February 1984*
{ .byline }

Sir: A certain amount of discussion has been going on recently regarding the desirability of an ASCII-character representation for APL. Perhaps I might be allowed to make something of a pre-emptive strike in favour of the present graphic notation.

Many of the present symbols carry something of a visual sense of what they do; for example, `⌽` is concerned with spinning objects around on axes, `⎕` looks somewhat reminiscent of a terminal screen (I don't have to think too deeply about `⎕←` sending characters to terminals and `←⎕` taking them from the keyboard), `⍋` is obviously going in the opposite direction to `⍒`.

Leading on from this, APL as presently represented is rather more cross-cultural than the essentially text-represented languages like BASIC (paraphrasing Allen Rose, do French programmers have to write text such as "LAISSEZ A=2 S'IL VOUS PLAIT"?). In its current form I would expect APL to have an advantage in transcending national and cultural barriers.

In any case, while history has imposed a penalty of several hundred pounds as the luxury cost of putting an APL keyboard onto a terminal, we are now in a situation where the STSC (Scientific Time Sharing Corporation) chip for the IBM Personal Computer is being made available for $25. To my naïve mind, this indicates that economics could cease to be the issue.

I suspect that given a historical perspective the advent of APL as a notational style will be seen in the same light as the move from Roman to Arabic numerals, or the evolution of calculus notation. We must not allow ourselves to be tyrannised by the temporary inability or unwillingness of hardware manufacturers to supply us with what we need at an economic price. Some of the introductory remarks in Kenneth Iverson's "Notation as a Tool of Thought" (Communications of the ACM August 1980 Vol. 23 No. 8) are well worth re-reading.

Yours sincerely,

Dick Bowman,<br>
CEGB,<br>
[address omitted]

(Editor. The various current arguments in favour of promoting a conventional representation for APL do not imply that the existing notation is wholly without any merits, only that its advantages are in some cases outweighed by problems. Dick's argument may well be the right one, but some people feel it is twenty years too late! Most computer users by now already own or have access to non-APL screens; although these could be converted, in practice they won't be. Another issue is the awkwardness of including APL character set output in typeset copy without specialist aids, which most publishers are reluctant to employ. This makes the inclusion of APL algorithms in most computer journals difficult or impossible, limiting in turn the spread of the language. We share this problem; the VECTOR editorial team would dearly like to hear from any organisation that can offer them a solution.)

*From: Professor A. G. Hawkes, 19th March 1984*
{ .byline }

Sir: I don't know when you expect to bring out the new Journal (to be called "VECTOR") but no doubt you will need a collection of papers to put in it. Enclosed is a paper which I hope you will feel is suitable.

A proper journal should make good sales from libraries. I hope it will cater for a broad spectrum of interests. I think the use of APL for scientific purposes has been sadly neglected in this country, and feel that a proportion of scientific papers in the journal, as well as the more commercial stuff, will help to remedy this.

Yours sincerely,

Alan. G. Hawkes,<br>
Dept. of Management Science & Statistics,<br>
University College of Swansea,<br>
[address omitted]

(Editor: We agree with Professor Hawke's views and are grateful to him for contributing a scientific paper, which is included in the Technical Section of this issue).

*From: Mr. Anthony Camacho, 24th February 1984*
{ .byline }

Sir: I found an error in an algorithm published in the "FinnAPL Idiom List". I think this is rare enough to be worth notice. Idiom 49 does not work if the largest value in "X" is an exact power of 16.

```apl
     ∇ R←FDTOH X
[1]   ⍝ FINNAPL IDIOM 49
[2]   ⍝ RESULT TOO SHORT IF ⌈/X IS 16*N
[3]    ⍉'0123456789ABCDEF'[⎕IO+((⌈⌈/16⍟,X)⍴16)⊤X]
     ∇
       FDTOH 16
0
       FDTOH 256
00
       FDTOH 4096
000
       FDTOH 15
F
```

It can easily be corrected by taking the logarithm to the base 16 of "1 + ,X", but if "X" contains many values this process may be time-consuming. It is much faster to find the maximum and to take the logarithm of that value only.

```apl
     ∇ R←DTOH N
[1]   ⍝ IMPROVED DECIMAL TO HEX CONVERTER
[2]    ⍉'0123456789ABCDEF'[1+((⌊1+16⍟⌈/,N)⍴16)⊤N]
     ∇
       DTOH 15 16
0F
10
       DTOH 4096
1000
       DTOH 4095
FFF
```

This takes less than three seconds to convert the first 256 integers on my microcomputer, compared with about 33 seconds for the improved FinnAPL idiom number 49!

Yours sincerely,

Anthony Camacho,<br>
[address omitted]

(Editor: Our Technical Editors confirm Mr. Camacho's observations)
