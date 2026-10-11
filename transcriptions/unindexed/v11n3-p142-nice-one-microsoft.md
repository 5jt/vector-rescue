---
title: Nice One, Microsoft!
authors:
- Adrian Smith
- Gérard Langlet
volume: '11'
issue: '3'
page: '142'
unindexed: true
transcribed: 'from page images of VOL.11-NO.3-JANUARY-1995.pdf, page 144 (printed 142; within the Technical section, after art10006210, “J Inscription 0 :”); Claude, 2026-10-11'
review: draft
tags:
- user interfaces
- humour
queries:
- "The byline reads “from Gérard Langlet via Adrian Smith (Vector Production)”; the text is Adrian Smith’s, reporting Gérard Langlet’s complaint, so both are listed as authors."
- "In the third paragraph the quotation marks and bullet are themselves the subject; they are set as printed: “ and ” each followed by a straight \", and ‘ followed by a backtick-like grave mark (set here as \\`)."
---

*from Gérard Langlet via Adrian Smith (Vector Production)*
{ .byline }

Following the note on fonts in the last Vector, I received a splendid *cri de cœur* from Gérard, not un-naturally upset about the lack of the *oe* diphthong from APL2741. He also mentioned a problem in using the Windows clipboard to transfer APL code from Winword back into APL (either Dyalog or PLUS III) for final testing before publication.

Suspecting (as one does) the APL interpreter in one’s life, I set out to investigate. Sure enough, function listings from Winword arrived in Dyalog looking very strange indeed — then I spotted that the execute had come through as a hyphen. If you look carefully at page 106 of Vector 11.2 you will see that execute is opposite en-dash — a vital clue! What the morons of Redmond have (allegedly — they might read this) done is to substitute what they thought you might have meant for what you actually put!

So — for “ you get " and for ” you get ", and yet (oh joy) for ‘ you get \`. For • you get o (that’s right, they just knew you meant little letter o when you typed bullet) and so on. Try this from Winword to Write (or Notepad or Works) and you will see what I mean.

The work-around is to save your document in Write format and clipboard from there, or just use a sensible word-processor like MS Works which does not exhibit this ‘helpful’ behaviour. At least we can rule out Winword as a candidate for *Vector OnLine*.
