---
title: 'Book Review: Learning and Applying APL, by B. Legrand'
authors:
- Anthony Comacho
volume: '1'
issue: '3'
page: '39'
unindexed: true
transcribed: 'from page images of VOL.1-NO.3-JANUARY-1985.pdf, pages 41–43 (printed 39–41); Claude, 2026-10-12'
review: draft
tags:
- reviews
- education
queries:
- "The Contents line reads “Book Review (Legrand)”; the review is headed “Learning and Applying APL by B. Legrand Published by John Wiley and Sons (1984) Reviewed by Anthony Comacho”, under the section heading “BOOK REVIEWS Compiled by Robert Bittlestone”. The section heading and its one-paragraph introduction, on the same page, are kept here. The review ends on printed 41; the next review there, of Chris Naylor’s “Build your own Expert Systems”, begins the Contents line “Book Reviews - General” (unindexed/v1n3-p41-book-reviews-general.md)."
- "The reviewer’s name is printed “Comacho” here and on the Contents page; Anthony Camacho is the usual spelling of the name elsewhere in Vector. Kept as printed."
- "Kept as printed: “to the address on the inside back cover” printed “on the address”; “such as 2 for iota”; “recognise.In”; “Section 1.6 says “You can now start reading this book.....””; the quotation from Chapter 13 and the closing quotation set as plain text without quotation marks."
---

## BOOK REVIEWS

*Compiled by Robert Bittlestone*
{ .byline }

Books are welcomed for review on any topic likely to be of interest to the APL user, and should be sent to the editor on the address on the inside back cover.

## Learning and Applying APL

**by B. Legrand<br>
Published by John Wiley and Sons (1984)**

*Reviewed by Anthony Comacho*
{ .byline }

This book is a disappointment, not because of the technical content or the way APL is explained but because of the bad translation and the poor job of book production.

First I will deal with these disadvantages and then for anyone who is interested, describe M. Legrand’s approach to teaching APL - a review of the book the author wanted!

### Translation

The translator was Julian Glyn Matthews of Linguatech. In spite of his English-sounding name he is not a native speaker of English. It is very rare to get an idiomatic translation from anyone not native in the target language and the translator should also be familiar with the usage of the subject’s technical terms in the target language. You may judge how far Mr. Matthews falls short: instead of ‘To pick out the value 8520 from the array TYRES’ he writes “In order to designate the value 8520 to the array TYRES” (section 2.13). In another place he writes “If it is not followed by a value the branch arrow (`→`) causes the output of a function and all the functions which call it, which the instruction (`→0`) does not allow” (section 4.36). Perhaps you would agree with me that you can only disentangle this if you already know what he is trying to say.

These examples are striking but they are not alone. Mistranslations are common: I seem to have found a dozen or so in each chapter. To discern the author’s meaning I often had to call on my rusty French and my APL experience. The translation from French is so literal that one can often guess at the original and get at the meaning through a retranslation. Take the rule on page 17 for example:

> When a vector is indexed by an array, an array of the same dimensions as the index is obtained, in which each value would have been replaced by the element of the vector which it designates.

The phrase “would have been” may be right in French; in English “is” or “has been” is more natural. As it is, the rule gives the feeling that the value wasn’t replaced because “would have” leads one to expect an “if” followed by the condition under which the replacement “would have” been made.

The translator clearly does not have experience of using APL in English: he writes that a function *restores* its result (instead of ‘returns’), he calls the pi-times symbol *orange* and the del symbol *carrot*, he refers to the *line* operator (instead of ‘axis’) and to the quad symbol as ‘window’. Where the French may be precise, this translation is not as it loses the case and gender association between noun and pronoun — “when binary values are available there are logical functions which enable them to be composed from them.”

It may be amusing at first to find “the computer *passes* a blank line between each sub-array” (instead of ‘prints’ or ‘outputs’); it may seem fun to calculate *mobile* averages, print subtotals at *ruptures*, preserve your workspace by *safeguarding* it and observe the *processings* of your functions: it soon palls. The French for ‘byte’ is apparently ‘octet’. The translator has left it as octet throughout.

### Book Production

The book is produced in typescript from a daisywheel typewriter. It uses the typewheel Courier for the text, Orator for headings and Light Italic for page headers and APL, except for a few places where a different printer seems to have been used.

I have used a daisywheel printer with a word processor to produce a book and it is an excellent method. The company that prints the book can’t add mistakes if it is given camera-ready copy. To be clear APL lines need consistent alignment so that the six space prompt is easy to recognise.In this book the alignment is not quite consistent and someone has used rub-on shading to distinguish keyboard entries. The shading is not skilfully applied and makes many pages look a mess.

There are many corrections to this text that are misaligned as if the correction was made with paint-out liquid and then clumsily overtyped. It would have been much better to use a word processor and reprint the corrected pages. There are still many typing errors. There are *principle* arguments, one thing has *lead* to another and *preceeded* a third - the latter so often that I suspect the translator. Other errors are surely misprints, such as 2 for iota, stile or even slash for backslash, capital I for I-beam, capital V for del and a monadic header as an example of a dyadic function. A newcomer to APL would find examples with such errors inexplicable. I estimate that there is on average one error per page. There are misprints even in the page headers. Attempts have been made to retouch some pages manually - erasures and alterations in ink. Where tables had to be ruled they are sometimes not even ruled straight (see section 4.22).

There are other inconsistencies too. In chapter 4, for example, the text repeatedly refers to a function `INCREASE` whereas the examples given are called `BIGRISE`. Similarly there is a function `CONSULT` sometimes called `CONSULTATION` in the text (it is even listed as that in what purports to be the computer response to ‘`)FNS` ’). In section 2.6 an array is defined generally so that a scalar is an example and then restrictively so as to exclude scalars. Section 1.6 says “You can now start reading this book.....” In section 5.4 we are told that a bar chart is often incorrectly called a histogram: the function given as an example, which draws bar charts, is called `HISTO`!

### Approach to APL

The book begins at chapter 2 and after two pages introduces a rank 3 array called `TYRES`. This daring is repeated elsewhere. There are surprises and tricks that kept me awake and interested. Every chapter ends with a collection of exercises, and these are one of the best features of the book. If you teach APL and want examples there is a seam here to be mined.

The attempt to be comprehensive is worthy but sometimes inadequate, particularly at the end of the book. I suspect the author cannot speak with authority of all the APL implementations. Here is a complete paragraph:

> Some systems enable special characters to be created by overstriking two letters. For example ‘E’ which is L and F overstruck, gives the character Line Feed. The reading of functions is complicated by this.

My appetite was whetted. I wanted to know which systems do this and to understand the problem and whether there are other such oddities: M. Legrand leaves me unsatisfied.

Chapter 3 explains some of the primitive functions to give material for the exercises and examples of defined functions in chapter 4. I liked the way M. Legrand introduces ravel, take and drop by setting them as exercises to be written as defined functions using only previously explained primitive functions.

Chapter 5 introduces operators thus:

> Operator is the name given to a function when one at least of the arguments is a function or another operator. Hence the notation `+/A` indicates that the operator `/` applies to the function `+`. The whole `+/` comprises the RESULTANT FUNCTION, the operand of which is `A`.

Some people may find this insufficiently rigorous, but I doubt whether anyone would be really confused by it. I could have complained that he defines an operator as a function, but I think in this case it would be unfair. There are two places where similar ways of explaining things are used, which cause no confusion in the classroom but which need more careful wording to exclude misunderstandings in a book.

Chapter six deals with operations on arrays, chapters seven, eight and nine with the remaining primitive functions, ending with a comparison between a brief introduction to quad-FMT and ‘format’. Chapter 10 is called INTERFACES WITH THE COMPUTER, SHARED VARIABLES and is the first place where workspaces, the index origin, the random link, the comparison tolerance and the latent expression are dealt with. Chapter 11 is about files (mostly STSC component files). Chapter 12 is about function development (mostly the del editor and the stop and trace facilities). Both these chapters are rather sketchy; neither of them covers the range of filing or editing features now available.

Chapter 13 is entitled STYLES, METHODS AND ADVICE. I agree with most of the advice given but dislike the didactic tone and the absence or weakness of the reasons for it. I feel the lack of a frame of reference within which conflicting requirements such as brevity and comprehensibility could be balanced. Readers will also be puzzled to know what action they should take to follow advice such as:

Care should be taken that the performances obtained cannot be brought into question by a change of equipment.

This last chapter also suffers badly from the inadequacy of the translation.

M. Legrand clearly is an optimist about the chances of APL becoming the language of the 90s:

In 1990, programs written in FORTRAN, COBOL, and PL/1, will still be used, but new developments will occur essentially with the aid of APL , or totally in APL.

I hope he is right but have my doubts.
