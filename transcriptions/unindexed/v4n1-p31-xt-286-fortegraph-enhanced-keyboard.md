---
title: 'Hardware Review: The XT-286, ForteGraph, and the IBM Enhanced Keyboard'
authors:
- Adrian Smith
volume: '4'
issue: '1'
page: '31'
unindexed: true
transcribed: 'from page images of VOL.4-NO.1-JULY-1987.pdf, pages 33–35 (printed 31–33); Claude, 2026-10-12'
review: draft
tags:
- reviews
- user interfaces
queries:
- "Contents line “XT-286, ForteGraph, IBM Enhanced Kbd”; the printed heading is “Hardware Review: The XT-286, ForteGraph, and the IBM Enhanced Keyboard”."
- "Kept as printed: “I havn’t tested”; “INI0” (the last character may be a zero or a letter O); “I flirted briefly with ‘()’ on shift ‘90’”."
---

*by Adrian Smith*
{ .byline }

### Background

Some time ago, I hatched a dream of a ‘one-per-desk’ APL workstation; something which would allow me to do mainframe APL (with full 32 line graphics) as well as APL\*PLUS/PC (in colour at a decent resolution). The right hardware for the job has gradually become available, in the Enhanced colour display, and the FORTEGRAPH (alias DCA) piggyback for IRMA. A brief trial of this in our dear old twin floppy PC convinced me, so off went the equipment request, and some days ago a heap of junk duly appeared on my desk.

### XT-286: First Impressions

The first thing to note is that this machine isn’t terribly PC compatible. It won’t run Borland’s Superkey, and things like the Turbo Pascal installation lock up (both these are fine on the AT and a wide variety of other kit, such as the TI-3100). It does however, run APL with no problems!

The second thing is that it is rather fast. OK the hard disk is from the XT, not the AT, but we floppy hacks find anything impressive so no quibbles there. Anyway, APL doesn’t use the disks a great deal once you have loaded up. Basically it benchmarks a shade faster than a standard AT.

### The Enhanced Keyboard

I really don’t think I am going to like this. In fact I am on the lookout for some muggins with an old-style AT keyboard who would like an ‘upgrade’! It has a dedicated cursor pad, and 12 function keys along the top of the keyboard. &lt;Control&gt; has moved down by the spacebar, and the backslash key is back down between &lt;Z&gt; and &lt;shift&gt; (or is it??). The &lt;\*&gt; has sloped off to the extreme right, and there is one extra key (top left) with the back-quote on it. Sounds acceptable enough, and for a touch-typing secretary it probably is . . . however:

1. Most current software assumes it is easy to get at &lt;shift-FN&gt; and at &lt;Ctrl-xxx&gt;. These become two handed ‘hunt and peck’.
2. MS Word treats the backslash as a dead key. This makes it impossible to access files on sub-directories!
3. In APL the mappings are pretty well all over the place. Again the backslash is dead, but at least you can redefine things to get it back on that new key top left. However there is worse . . . by default the numeric pad moves the cursor (fair enough) but the ‘dedicated’ cursor keys produce numbers!! At one point I managed to poke Num Lock to get everything giving numbers . . . it varies depending on APL/Text/Union. I’m afraid I havn’t tested all the possible permutations.

In short, from an APL development point of view, this keyboard is a lemon. You should definitely avoid it until a reasonable base of software (APL included) explicitly supports it. In other words vote with your feet in favour of something which runs the current software base acceptably, and don’t accept the word of your hardware people when they tell you that the new layout is the best thing since grip-top socks.

### ForteGraph

You will probably have to look for this under the DCA ‘IrmaGraph’ label; mine says IRMA in the documentation and Forte on the board! It is quite expensive, and does require the enhanced display, but it really does do the job. What you get is an IBM 3179-G look-alike (32-line graphics done locally) with 3279-like keyboard mapping. As a mainframe terminal it is very fast (actually rather faster than the 3179-G) and the resolution is acceptable (although not quite as good as the real thing).

I have been using it as my day-to-day mainframe workstation for a couple of weeks now, and can report only the following list of minor problems:

- it has the occasional lapse when attached to 3174 control units. I don’t pretend to understand the details, but every so often it locked up when you left your finger on &lt;delete&gt;. The problem has since gone away.
- the supplied keyboard mapping is from the US 3279 to the US PC. This causes endless hours of fun, as the APL symbols follow their non-APL associates (e.g. ‘GoTo’ stays with the curly bracket and ends up to the left of the ‘1’ on the top row!!)
- one or two characters occasionally acquire random embellishments, such as extra tails or overbars. A power-off reboot usually puts things right.
- APL gets to the keyboard before IRMA, so you can’t use &lt;Shift-shift&gt; to toggle from PC APL to VS APL and back. I have given up running IRMA resident for this reason.

The keyboard mapping is only a minor nuisance, as you can use a supplied utility to put pretty well any key anywhere. The only limitation is that you are stuck with the APL-to-nonAPL associations; for example I duplicated &lt;shift-K&gt; on the lower-case PC quote. This is very nice when you have APL on, but rather a pain when it is off! This apart, some of the nice things you can do are:

- Pf-1 up to Pf-10 can be put on F1 to F10. Unfortunately you can’t do Pf-11 and 12, as Forte refuses to hear of F11 and F12 on the enhanced keyboard! I put them on &lt;shift-F1/F2&gt;.
- You can set PgUp and PgDn to double Pf-7/8, and End to double Pf-3. TSO hacks will see the point!
- My AP-126 editor uses Pf-9 for ‘End and save’; I doubled this on &lt;Ctrl-E&gt; so I can use my APL\*PLUS/PC reflexes on the mainframe.

I have also moved the square brackets to the PC keys where they are, leaving the shifted curly ones for the left and right arrows. I flirted briefly with ‘()’ on shift ‘90’, but my reflexes got the better of me, and they are back where they were!

Of course once you are in APL\*PLUS/PC you can put anything anywhere, so whatever you settle on for your mainframe layout you can quickly match on the PC. If you want to save yourself the trouble of getting the basics right, send me a formatted floppy, and you can have copies of the ‘GRAPH.DAT’ for Forte and INI0 for APL\*PLUS/PC.

### Summary

The XT-286 is a bit of a wolf in sheep’s clothing; once having disposed of the enhanced keyboard I quite got to like it. ForteGraph has done all I expected of it, and apart from some very minor niggles it provides a fully functional APL workstation for mainframe or PC use. The all-up cost (including software) was a shade under £5,000.
