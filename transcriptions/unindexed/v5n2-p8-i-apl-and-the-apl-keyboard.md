---
title: I-APL and the APL Keyboard
authors:
- Anthony Camacho
volume: '5'
issue: '2'
page: '8'
unindexed: true
transcribed: 'from page images of VOL.5-NO.2-NOVEMBER-1988.pdf, pages 10–15 (printed 8–13; within General Correspondence, after Craig Lomas’s “APL Conference on CIX”); Claude, 2026-10-11'
review: draft
tags:
- user interfaces
- implementations
- education
queries:
- "A letter in General Correspondence, From: Anthony Camacho (a reply to F H D van Batenburg VECTOR 5.1 p14), July 1988. It answers unindexed/v5n1-p14-public-letter-to-p-chapman.md, and follows Craig Lomas’s letter (unindexed/v5n2-p7-apl-conference-on-cix.md)."
- "The lists of key allocations are set in plain code blocks to keep the printed bracketed side-notes aligned."
- "The high-minus key is printed as a straight quote mark beside “(grave accent)”; transcribed as a grave accent."
- "The writer’s home address in St Albans is omitted."
- "Kept as printed: “( to be less than or equal to” (presumably “{”, which would match “}” and the note “The points are on the same sides”); “I-APLs needs”; “Llewellyn Jones’ APL-pip”; the stray comma in “all machines that use I-APL, compatible”; “rather than manage with the PC clones, shared one machine”."
---

*From: Anthony Camacho (a reply to F H D van Batenburg VECTOR 5.1 p14), July 1988*
{ .byline }

The default I-APL keyboard is very different from any other APL keyboard. How could the project have been so stupid and arrogant as to confuse an already poor situation by introducing yet another non-standard keyboard? Here is an explanation of how the decision came about and permission to anyone who cares enough and has the skill to implement an I-APL with any keyboard they like. After the introduction, the three parts deal with the aim to please the new APL user, some technical considerations and the advantage of having a standard default keyboard.

## Introduction: Microcomputer Keyboards

There is no such thing as a standard keyboard. A program designed to run on many types of microcomputer will not be able to hold every character in the same place on every keyboard. Most microcomputers have a way to enter the 7-bit ASCII set of codes; this contains 32 control codes, space, 94 printable characters and the delete character. Many of these can display the ANSI characters, but in other countries there are often accented and special characters which occupy the positions of some of the less used characters in the ANSI set.

## The Wasted Scholarship

In 1986 the project listed all the known allocations of keys and codes to APL characters. There are quite a few, even if those using EBCDIC are ignored. Most computer manufacturers have implemented APL and sought a way to allow it to be used from their common ASCII terminals. I-APL collected the lists of keywords, abbreviations or transliterations for VAX, Prime, Data General, Burroughs and ICL as well as variations in the quad-AV between most of the well known microcomputer APLs - APL/PC, Sharp APL, APL\*PLUS/PC, PortaAPL, MicroAPL, VIZ::APL, TisAPL, APL90.

All these painstaking lists were ignored when we realised that the nub of the matter was whether we wished to please people who already use APL or those who haven’t yet tried it. Those manufacturers were trying to make it possible for people with a requirement for APL to buy and use their machinery, not to encourage the use of a notation which can be executed on a computer. I-APL is not trying to sell computers. More relevant to I-APLs needs was Llewellyn Jones’ APL-pip; an ASCII transliteration of APL to allow it to be transmitted and published through ASCII channels while preserving enough of the look of traditional APL to allow an APLer to read and understand it.

## I-APL Aims to Attract New People to APL

New users of APL who know a keyboard will prefer to have as many keys as possible in their familiar places. Established APLers may prefer something similar to the golfball typewriter on which APL was first printed or to their current implementation.

Unless a compromise can be found which suits both old and new users I-APL would prefer to please the new users. After all, most established APLers will have no need to use I-APL; they are already equipped with an APL. Not one of them is going to give up APL as a result of I-APL’s choice.

## The Idea of a Union Keyboard

A key should cause the display of the character marked on it wherever that is possible. There does not seem to be any adequate reason for moving the characters which are the same in ASCII and APL from one place on the keyboard to another. To do so would merely make APL harder to use without any benefit to the learner. This is one of the principles of the union keyboard - that similar symbols should stay on the familiar keys - and I-APL has adopted it. There are minor differences: the APL star has five points, the ASCII one sometimes has six, the stile is unbroken, whereas the ASCII vertical bar has a short gap in it, and the symbol for AND has longer legs than the circumflex but these will not cause anyone difficulties in finding the corresponding keys. So the 22 ANSI symbols correspond to their APL look-alikes. This policy will also reduce the number of keys which need extra markings such as key stickers.

## Fitting the APL Symbols into the ASCII/ANSI Set

I-APL hopes to have the interpreter running on over a dozen machines. The interpreter is designed to allow all APL characters to be used on machines which can handle extended character sets. Some machines, such as CP/M machines with dumb terminals may have to manage with the ASCII/ANSI set. There are not enough codes in that set for all the APL characters even when the lower case alphabet is reallocated to be used for APL. Of the 94 displayable characters 58 are allocated so far:

```
10 the decimal digits
26 the alphabet
22 the symbols common to ANSI and APL
--
58 total allocated so far
```

There are 36 ANSI characters and 41 or more APL characters left.

## The Chosen 36 APL Characters

The symbols not yet allocated to keys are these:

> left arrow, right arrow, up arrow, down arrow, multiply, divide, high minus, rho, epsilon, iota, up stile, down stile, logarithm, circle, representation, base value, format, execute, jot, transpose, rotate, OR, del, quad, quote-quad, quad divide, lamp, alpha, omega, not equal to, greater than or equal to, less than or equal to, slash bar, backslash bar, comma bar, circle bar, delta, NOR and NAND.

The list begins with the most needed symbols and ends with those which could at a pinch be foregone on ASCII-only keyboards and displays. As the I-APL quad-AV contains all the APL characters, anything can be constructed using quad-AV indexes. On machines with extended keyboards it may be possible for the porter to provide access to all 256 codes. On ASCII-only keyboards there is not room for the last five in the above list. The symbols to leave out were chosen because they are used little and can easily be provided as combinations of other functions and operators. The delta was left out because it is only required in one place - to delete lines during editing with the del editor - and the tilde can easily be used instead. Although alpha and omega are not used in most commercial APL work and might have been omitted, I-APL took the view that direct definition will be of great value in education. We considered using A and W instead of alpha and omega and concluded there were too many disadvantages - we chose to include them rather than NOR and NAND.

## Allocation of Selected Symbols to Keys

Where a key has to be used for a character different from the mark on it some kind of mnemonic is called for. This list of allocations begins with the best justified and ends with the arbitrary.

Similar shapes …

```
x to be multiply
v to be OR
o to be circle
i to be iota
a to be alpha
w to be omega
e to be epsilon
z to be not equal to
% to be divide
` (grave accent) to be high minus
# to be quad
```

Distinctive characters …

```
& to be quote-quad
$ to be del (the dollar is commonly a control character)
@ to be branch
_ (underline) to be assign
```

Similar Symmetries …

```
n to be encode                          ) These four fit well
u to be decode (upside-down n)          ) together as a mnemonic
h to be format (n plus a bit)           ) set. APLers only have
y to be execute (upside-down h)         ) to remember the n.
q to be upgrade                         )
d to be downgrade                       ) One symmetry preserved.
p to be upstile                         )
b to be downstile                       )
( to be less than or equal to           ) The points are on the
} to be greater than or equal to        ) same sides.
s to be transpose - it has the same diagonal symmetry
```

Others …

```
r to be rho - r is the equivalent of the greek rho
f to be rotate - phi looks like rotate and is greek f
j to be jot                             )
m to be matrix divide                   ) Initial letters may
l to be logarithm                       ) help with these.
t to be up arrow (take)                 )
k to be down arrow (arbitrary)
" to be lamp - association of ideas
c to be slash bar (arbitrary)
g to be backslash bar (arbitrary)
```

Overstrikes do not provide extra characters.

## Some Technical Considerations

## The Porter Controls the Shell

I-APL is written in a language called DE. It stands for Development Environment. The DE code is interpreted by the program the porter writes - nowadays commonly called DEGO. The porter provides a complete shell insulating the interpreter from any machine dependent features. Every character input to the interpreter or output from it passes through the DEGO program. The porter is in complete control of this channel and so can make any translation of characters he wishes.

The bulk of DEGO is now available to prospective porters for the 6502, 8086 family, 68000 family and Z80. All that a porter needs to add is the links to the native operating system to get and display characters, to switch the printer toggle on and off, to save and load workspaces using the native filing system and to provide the quad-MC interface for machine code routines. The simplest possible port to a new machine would simply send, display and receive the ASCII equivalent characters.

## Characters are Sent and Received in Two Forms

To make it as easy as possible to deal with whatever range of characters is available, I-APL passes characters for output as a pair of bytes and receives characters input in one of a pair of bytes. One output byte is the index in quad-AV and allows use of the complete range; the other is the ASCII equivalent according to the tables above. One input byte is the index in quad-AV and the other is ASCII which will be translated according to the tables above. The porter chooses which output byte to use and which input byte to provide and the choice may vary from one byte to another so hybrids between ASCII equivalence and full quad-AV are possible. All ports so far are hybrids.

So a porter can implement keywords or mimic whatever keyboard he chooses. He can also offer alternatives of keyboard mapping much as other interpreters allow a choice of keywords, traditional APL or a union keyboard. These choices might be selected by adding a parameter to the initial call of I-APL. I-APL is happy to give porters permission to do this; all we require is that a proper job is done and that it is thoroughly tested before issue.

## Accented and Special Characters

In many countries special characters or accented characters are required and these are often allocated to positions in the ASCII set of infrequently used ANSI characters. When only the ASCII 94 characters can be used, none of these extras is available. On extended keyboards I-APL allows for them as follows:

There is a spare alphabet in the I-APL quad-AV which defaults to lower case underlined. This may be used for any special characters. As the keys marked with the special characters will return ASCII codes the porter will have to trap these and translate them.

The porter will also have to specify a method for entry of the ANSI characters normally returned with the trapped codes (commonly a combination of keys).

## Advantages of a Standard Default Keyboard

The key allocations explained above will probably be those most widely used in implementations of I-APL. The project has some influence with porters and can encourage them to follow a particular line. Which line should I-APL favour?

One of the strengths of I-APL is that if the machine-dependent functions quad-MC, quad-TS and quad-DL are not used then an I-APL workspace will run on any I-APL machine and produce the same results. It is possible to send a workspace from a PC clone to a BBC B, a Sinclair Spectrum or a VAX and run it unchanged.

It would be very good to have all machines that use I-APL, compatible in other ways such as the keyboards. This is not possible (as explained above), but it is possible for the ASCII character set to be treated similarly on all machines.

Many schools have a mixture of computers and have difficulties using them all in a single class because of the variations between machines. If the variations are only in the positions of the keys while the association between key labels and APL characters stays constant, most of the difficulties are overcome. Whereas it would cause confusion if the quad were sometimes on the key marked # and sometimes on the SHIFT-L, little trouble is caused by the varying position of the asterisk or plus sign; so long as an APL character is always on the key with the corresponding ASCII mark there is little difficulty holding a class with mixed machines.

A teacher faced with the need to equip a class with a mixture of PC clones, CBM 64s and Apples would probably prefer to have one machine per pupil or per pair of pupils, all equipped with an APL which uses the same key allocations rather than manage with the PC clones, shared one machine between several pupils. The same instructions to the pupils about how to enter a line of APL can be given to all users of I-APL. The extra speed and capacity of the commercial APLs is less important in the classroom than having fewer pupils per machine and being able to say that the quad is on the key marked with a hash or that execute is SHIFT-Y. Furthermore the commercial APLs are expensive.

I-APL is asking all porters to provide the ASCII to APL key associations shown above as the default, while encouraging anyone who has the time and effort to offer alternatives which may suit established APLers and advanced pupils better.

Anthony Camacho
