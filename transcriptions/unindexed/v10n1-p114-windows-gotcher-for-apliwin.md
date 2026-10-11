---
title: A Windows GOTCHER for APLIWIN
authors:
- Anthony Camacho
volume: '10'
issue: '1'
page: '114'
unindexed: true
transcribed: 'from page images of VOL.10-NO.1-JULY-1993.pdf, pages 116–117 (printed 114–115; the first letter in Technical Correspondence, before Errors in “Integrating with Insight”); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- implementations
queries:
- "A letter in Technical Correspondence, From: Anthony Camacho, 15 May 1993."
---

*From: Anthony Camacho, 15 May 1993*
{ .byline }

I have been using APLIWIN to provide a customer with a PC version of a system originally written in Sharp APL in 1977. I have been very impressed with APLIWIN even though my stupidity and the lack of a system manual for this specific implementation has caused me some head-banging (for example it took me ages before I found out how to fill a combo box with 20 lines of alternatives).

This letter is being written in WinWord. I have been using WinWord to make notes on the conversion for colleagues and have been delighted to be able to cut functions from the workspace and paste them into WinWord (or Write) and then by selecting the pasted section and changing font to ISIAPL’s TrueType font the correct APL characters are both displayed and printed. Marvellous.

The other evening I had some work to do which required a PostScript font. I set WinWord to use the PostScript printer, did the job (printing to file and using GoScript to emulate the printer) and thought no more about it. I little realised what I had done.

The next time I did a cut and paste from ISIAPL to WinWord the characters were displayed in some default font or other. The ISIAPL font was there in the font list and could be applied to selected text but it appeared not to work: the text obstinately refused to turn into APL.

So of course I tried all the obvious things; I deleted and re-installed the font; I did something which I had intended to do ever since I mistakenly allowed CorelDraw to install hundreds of rarely needed fonts - I deleted about a hundred fonts; I edited WIN.INI to remove the section which specified font substitutions; I rang the Microsoft help line (a mistake - see below); I even bought a book Windows 3.1 Insider (£24.00!) which had a large section on fonts.

The Microsoft help line was worse than useless. An authoritative man told me to do this and that and the other and, like a fool, I did what he said. When we had got as far as to ‘remove’ all fonts and then ‘add’ all fonts I realised that my adviser knew less than I did. The effort of selecting a hundred fonts to delete and waiting for the Windows longwinded deletion process was undone. Then he said he was going to delete and re-install all my drivers and I said that plainly he was unable to see what was wrong and that I might as well re-install windows from scratch as it would take less time than his diagnosis.

The GOTCHER is the shibboleth WYSIWYG [What You See Is What You Get]. Microsoft have programmed WinWord and Write so that if a printer is selected that cannot print TrueType the display will not show TrueType. They could easily have indicated that the TrueType fonts were not available or disabled by removing them from the list of fonts or by some warning or other. But they didn’t; you can select from all the fonts and the substitution is automatic and outside your control and you are not told it is being done to you.

The Insider book (and, to be fair, the Microsoft help line) told me that the printer driver determined what could be displayed. The Microsoft help line did not tell me to check what printer was selected. They didn’t realise the significance of this. They didn’t suggest I tried selecting other printers. All I had to do to recover the ability to cut and paste APL was to select the DeskJet or Epson or any printer that can do TrueType.

Try it! Put something on the screen in an out-of-the-way font. Set up a PostScript printer (you don’t need to have one) or a plotter or daisywheel and select it; the screen miraculously changes its display to the nearest default font. Select a dot matrix printer that can do TrueType and the screen changes back to show the font as you expected.

I have written to Microsoft saying that I think they have made a mistake. If my text will not print as I intend, please warn me but don’t in the name of WYSIWYG convert my intentions to something else. And don’t call it a printer driver if it is really a display and printer driver. Write the message loud and clear WHAT IS SHOWN ON THE SCREEN IS LIMITED TO WHAT YOUR PRINTER CAN PRINT.

Apart from the waste of effort it does make me feel so stupid.

Anthony Camacho
