---
title: 'Typesetting J: some Comments'
authors:
- R.H. Oates
volume: '8'
issue: '4'
page: '82'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, pages 84–85 (printed 82–83); Claude, 2026-10-12'
review: draft
tags:
- language design
queries:
- "A letter under the heading “Correspondence”, From: R.H. Oates, February 26, 1992, followed by an unsigned “Typesetter’s note” (printed in italics, evidently by the editor who set the J font), kept here. The letter ends at mid-page on printed 83, where “Comments on J Questionnaire” begins (unindexed/v8n4-p83-comments-on-j-questionnaire.md)."
- "R.H. Oates’s address (a New York street address with an apartment number) looks like a private home address and is omitted."
- "The J characters in the letter and note are set in the J typeface: “f f”, “$”, “@”, “m : n” and the run “'$\"@%&”; transcribed as code."
---

## Correspondence

*From: R.H. Oates, February 26, 1992*
{ .byline }

I saw your request for comments on J typefaces in the January Vector. The quote character on page 72 is too light. I was reading Vector on the bus and thought both `f f` expressions had open quotes until I looked over at the APL side. And the bulk of `$` makes that character too dark. It almost looks bold. How is your `@`? You want to establish an even blackness throughout the font, and to do that you have to compensate for the relative bulk of the characters. You can't just make them all two pixels wide, or whatever. It's not easy.

I find Programming in J and Tangible Math easier to read than the Dictionary and Arithmetic because they use bold characters for J (at least in the 1991 editions) consistently throughout. If you go with bold, then the problem becomes generating a bold Dot and Quote, say, that will be blacker than the normal At and Dollar Sign. It gets harder. My own fonts, which I got for APL2, are not very good, even within a font and particularly in the contrast between bold and normal fonts.

The J dictionary does not use bold consistently, just at the heading of each entry, and that is a mistake. Ken is following English dictionary format too closely. When people complain about the dictionary what they usually mention is its terseness. I like the terseness and think the typography is the real problem.

There is more white space (to accommodate figures) within the entries of the J dictionary than in an English dictionary. The contrast between bold and normal in the J dictionary is less than an English dictionary. Entries in the J dictionary divide into sub-entries in small caps, while entries in an English dictionary are homogeneous. Entries in the J dictionary begin either with a single J word or with a phrase like `m : n`. J words average 1.65 characters in length and phrase words average 1.1 characters in length, while English words average maybe 5 or 6 characters.

All of these things conspire to keep the J dictionary page from breaking down into distinct entries like a page in an English dictionary does. The J page is just one big blob. It would be much improved if a blank line were left in front of each entry and if the bold typefont were used consistently throughout for J words. When I get a new J dictionary the first thing I do is rule it off in black ink. I know that sounds stupid, but I do and it makes a big difference.

Typography is an art, of course, not a science, a profession, actually. But I wish you well and look forward to experimenting with your font.

> R.H. Oates,<br>
> [address omitted]

*Typesetter's note: your comments are much appreciated, and I hope I have fixed the obvious infelicities in the design. See Roger Hui's article (page 91) for the revised* `'$"@%&` *in action! At the moment, this is implemented as a PostScript type-3 font, using stroked characters (except for simple fills like dot). I am in the process of converting my* APL2741 *face to an Adobe type-1, which demands filled characters throughout. Fortunately, the font currently exists as numbers in an APL workspace, so much of the geometry is automatic, but I am not clever enough to convert complex shapes like* `⍺` *totally mechanically!*

*The obvious advantage of a type-1 is that all Windows software will display it (at any sensible size) and will also render it on paper on most reasonable printers (like HP Deskjets) very well. All you need to do is buy Adobe Type Manager, or wait for Windows 3.1 and TrueType. I will try to have both fonts available by APL92.*
