---
title: Submitting Articles for Vector
authors:
- Jonathan Barman
- Anthony Camacho
volume: '4'
issue: '1'
page: '123'
unindexed: true
transcribed: 'from page images of VOL.4-NO.1-JULY-1987.pdf, pages 125–128 (printed 123–126); Claude, 2026-10-06'
review: draft
queries:
- "The contents page lists “Submitting articles to Vector”, Johnathan Barman, p.123; the article is by Jonathan Barman and Anthony Camacho."
- "“see separate article” (Hercules Plus): Adrian Smith’s review in the front section of the same issue (p.34), not transcribed here."
- "The control-code samples (“Large Centered Bold Heading.”, “Centred italics.”, “Centred text.”) are printed in the styles they name; reproduced with HTML. The codes are printed with a small raised caret, e.g. “ˆD”, presumably Ctrl-D; transcribed as ˆD."
---

*by Jonathan Barman and Anthony Camacho*
{ .byline }

The editors of Vector are all volunteers and carry out their work in their spare time. Everyone is busy, and getting Vector out on time can be a struggle when there is lots of ‘real’ work to be done. Any help in reducing the load on the editors would be very welcome, and will make the difference between getting an article into the current issue, or having to delay it.

When you send an article to Vector in typescript there may be a great deal to do to it before it is printed. It may be edited first and then it will have to be entered on a keyboard. If there is APL in it that too may have to be entered and tested before being printed out in camera ready form. We try to avoid any manual operations on code: what is printed should be a direct printout of what has just been working.

Then the text has to be sent to be typeset and the APL photographed and stripped into the text in the appropriate positions.

This article is intended to make it possible for authors who have access to a PC or clone to send us material which needs as little attention as possible.

The first thing you can do is to send us both the typescript and the text on a PC disk. This makes the greatest saving in our effort. As there are hundreds of different disk formats we have standardised on the IBM PC format (as has the Public Domain Software Library).

The general availability of the IBM PC and clones, with APL\*PLUS PC, makes it easy for text to be swapped and manipulated in a standard way. If everyone submitted articles in a suitable format, then typesetting can be carried out quite simply and at a substantially lower cost.

Our current typesetters have a PC clone which they can link into their typesetting machine, and it is the demands of the typesetting machine which forces the format of the files. Typesetting is quite different from normal typing:

- there are many different fonts of varying sizes.
- each letter is variable in width and the space between letters is varied to justify a line. The left and right margins have to be specified, so that indented text can be produced, as in this paragraph.
- there are many additional characters. Alas, not yet all the APL characters, but our typesetters are adding a desktop publishing front end to their system, using a Hercules Plus card (see separate article) and the APL set should soon be achievable.

The font and size have to be specified in detail to the typesetting machine, but we have simplified the process by specifying three fonts, a standard and two specials for headings. The standard font is assumed unless a control character appears at the beginning of a paragraph; the specified font is then in force for the whole of that paragraph.

Most word processing programs carry out line justification by assuming every letter has the same width, and adding additional spaces between words to get an even right margin. Typists usually add an extra space or two after a full stop in order to improve the visual appearance of a letter and achieve indented text by padding out with spaces. Typesetting machines treat each paragraph (i.e. up to the next carriage return/line feed) as soft putty, squeezing it into the line width that has been previously specified, and stripping out all spaces except one between each word. It is not hard to imagine the lethal effect on a file full of indents, tabs and nicely spaced out and justified text. The ability of the machine to indent is in fact infinitely fine, but to simplify things we have specified a code that will produce a standard indent.

It can also produce fixed space text, with an ‘OCR B’ font, so text needing this treatment, such as listings, should be preceded by [OCR] and an [ocr] at the end to show where the normal font resumes.

One significant problem with typesetting is the quote marks. Printed text has a different open quote to a closing quote, both for singles and doubles, and it is important that the correct ones are specified otherwise the result looks quite horrid. The way in which this has been solved is to use an ASCII single quote for a right quote, so this looks OK for the possessive case (Vector’s quotes), and the ASCII back quote (grave accent) is used for a printed left quote. The ASCII double quote goes through as an open double quote, so a different code is needed for ‘close doubles’ and for this we use two singles (”). Most typescripts so far have had a typed single quote throughout, which can be converted by assuming that all single quotes preceded by a space, or carriage return, or open bracket, are open quotes, and the remainder are right quotes.

APL text at present is a nuisance. The only way in which it can be catered for is by using some ancient terminal which produces beautiful APL characters, enlarging or reducing the printout photographically to the right size and getting the typesetters to glue the photographic print onto the page (where, of course, the right sized gap has to be left in the text). Authors should supply APL copy on white paper ready for photographing. But, as we say, we are working on it.

In the meanwhile, it is expensive and difficult to include any APL in a paragraph of text. We have had to do substantial editing to remove embedded APL. Please keep all your APL separate. All APL examples should be in between blocks of text.

There are a large number of word processing programs around, and no particular difficulties have been encountered so far with any of them. The main problems are that in copying files from one disk format to another wordwrap line ends (‘soft’ carriage returns) become hard. That is itself no problem, as line ends are now ‘space, carriage return’, and these can be stripped out by the typesetters, unless of course you are in the habit of hitting ‘full stop, space bar, carriage return’ at your ends of paragraphs . . . .  Worst of all are the file transfers that produce carriage returns with *no* spaces at line ends, so that every line has to be unpicked. Moral: it can save a lot of grief if all wordwraps are removed before they leave you, so that in effect each paragraph is one long skinny line.

One benefit of using a word processor is getting the spelling right. It is amazing how many mistakes slip through the net. Proof reading is difficult and time consuming, and if there are many corrections to make, checking the corrections is a chore that is most unwelcome as we are usually right up against the time limit.

Text that arrives on diskette goes through at least two editing processes. First we make sure that all the control codes are in the correct places, and make sure that the text fits the style of Vector. All the articles received are then combined into a few files and sent to the typesetters, with a printed copy of the text. The typesetters then change all the control characters into the actual controls needed for their typesetting machine; most of this is automatic, but the tabs need special treatment. The proofs are sent back to us for correction, and the typesetters then edit their files for any mistakes or changes that are required.

The control characters are as follows. They can be accessed in APL\*PLUS PC by using the ⎕AV indices given (index origin 0), or by using the APL character.

<p style="text-align: center; font-size: 1.4em"><strong>Large Centered Bold Heading.</strong></p>

ˆD (AV 4 diamond) at beginning and end of text.

**Small bold heading.**

ˆB (AV 2 not-equal overstruck by underbar) at beginning and end of text.

*Italics.*

ˆS (AV 19 del-tilde) at beginning and end of text.

<p style="text-align: center"><em>Centred italics.</em></p>

ˆX (AV 24 take) at beginning and end of text.

<p style="text-align: center"><strong>Centred text.</strong></p>

[c] at end of line to be centered, immediately before the carriage return/line feed. This can be used in combination with other control codes.

**Left/right justified text (rare).**

[lr] at the point where text is to be split and [j] at the end of the line. Can be used in combination with other control codes.

**Indented paragraph.**

[i] at beginning and end of paragraph to be indented. If a paragraph number is needed, then put the [i] between the number and the start of the paragraph, but Vector articles do not normally have numbered paragraphs.

**Tabs.**

ASCII split stile (AV 124). The actual amount to tab is set by the typesetters, who adjust it to look well and suit all the text in the columns required. If you must have absolutely precise positioning, specify the OCR font (see above), making sure there are no more than 90 characters per line.

If APL\*PLUS PC is being used, then )EDIT is best for producing the text which can be in the form that looks good when printed. It is quite simple to change the resulting vector into the format needed by the typesetters, as follows:

<div style="margin-left: 2em" markdown>

Put APL diamonds around title and APL takes around the by-line.

Put APL inequivalent (not-equal overstruck by underbar) around the small bold headings.

Add [c] to the end of lines to be centered.

Put a [i] at the beginning and end of the indented paragraphs.

If a table is included, replace the spaces with an ASCII split stile.

Use the TEXTREPL function distributed in the ASMFNS workspace to replace the double carriage returns between paragraphs to a dummy character, replace all carriage returns with spaces, and replace the dummy character with carriage return.

Use the DEB function distributed in the ASMFNS workspace to remove all surplus spaces.

Use TEXTREPL to replace space-quote with space-backquote and cr-quote with cr-backquote. Do the equivalent for double quotes by replacing double quotes in double-quote-space or double-quote-punctuation-mark by two single quotes.

Use TEXTREPL to replace carriage returns with carriage return/line feed.

Visually check that the result looks ok.

Add an APL right arrow to the end of the vector, and write to file.

</div>

We have had lots of problems. The printed copy sent to the typesetters did not always match the text on file, sometimes the file was correct, sometimes the printed copy. The typesetters have been able to point out all sorts of spelling mistakes and grammatical errors, in spite of the technical nature of the articles. We have found errors in the original scripts at the proof reading stage, and worse, some blunders in the printed copy of Vector. Ideally, what you type in your article is what you get and if you really want a spelling mistake, then so be it. However, the editors are not happy producing a journal with spelling mistakes and bad grammar, so a little editing of files is inevitable. We hope this article will reduce the work to a minimum.
