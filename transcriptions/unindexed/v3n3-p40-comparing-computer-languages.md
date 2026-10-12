---
title: Comparing Computer Languages
authors:
- Peter Branson
volume: '3'
issue: '3'
page: '40'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 42–46 (printed 40–44); Claude, 2026-10-12'
review: draft
tags:
- reviews
- APL in perspective
queries:
- "Printed heading: “Handbook and Guide for Comparing Computer Languages / Produced and published by / Research and Education Association, New York (1985) / Reviewed by Peter Branson”. Printed 45–46, before the next Contents line (p.47), are STSC and Interprocess Systems advertisements, not transcribed."
- "The 18 sub-headings of “APL details” are printed as indented run-in labels, with varying punctuation (colon, full stop or none); they are given here in bold with their printed punctuation."
- "Kept as printed: “New Yorb” (New York); “langauges”; “Kernigan and Ritchie”; “alright”."
---

*Reviewed by Peter Branson*
{ .byline }

**Handbook and Guide for Comparing Computer Languages**  
*Produced and published by*  
*Research and Education Association, New Yorb (1985)*

After all the discussions on how little publicity APL gets, the thing that hit me when I stumbled across this book in my local library was the front cover. There, in very bold print, are the eight languages covered:

| | |
|---|---|
| BASIC | PL/1 |
| FORTRAN | APL |
| PASCAL | ALGOL 60 |
| COBOL | C |

It is worth quoting part of the preface:

> “Although most languages can be used for one application or another, a great deal of confusion exists as to which language is appropriate for a given application. From among the various languages that have been developed, eight remain as the most practical and advantageous to use. These are . . .”

and the above are listed again. Although we might not all agree with the chosen eight, at least APL is in there!

After a random dip, followed by a quick serial scan, I realised I was looking at the book in two differing ways: firstly, to see how good were the APL parts; secondly, to help myself with non-APL langauges. (I have a working familiarity with some of these eight, but want to know something about C – of which I am pretty ignorant.) My first impression was that the book was excellent, but this was rapidly modified as I went through the APL sections. In this review I will look at the general parts at the start of the book, and then concentrate on the detailed APL sections, before trying to give an overall summary.

### Layout and Introduction

The book starts with a general section on factors for language choice, followed by an overview of each one. The languages are then compared side-by-side under 18 headings, and the book concludes with two sample programs, some appendices and a glossary. The paper, typeface and general layout are very good, and plenty of white space is allowed to get optimum comparison when entries differ in length. The initial section entitled *“Factors for Choice of Language”* is one page covering clarity, simplicity, unity of language and structure, naturalness of application, ease of extension, external support, portability and different measures of efficiency. Although short, this is quite good.

There follows about one page for each language entitled *“Introduction and Brief Overview”*. Within my knowledge of the various languages, the balance seems quite reasonable. The overview of APL is really quite good in what it does cover (which isn’t nearly enough – see later), although I do have minor objections to such phrases as “... restriction to homogeneous array structures (creates difficulty in) business data processing”, or “subprograms are restricted to at most two arguments (with) a single result”, both of which have a stronger negative connotation than is really justified.

### APL details

This part of the review concentrates on the APL entries, using the same 18 sub-headings as the book itself.

**Program structure:**

Good, except there is perhaps insufficient emphasis on the fact that APL is fundamentally different from the other seven.

**Statement layout:**

Reasonable, although it is not made really clear that a statement separator is only needed when there is more than one statement per line.

**Elementary data types:**

I don’t like this much, although others might think it fair:

> “APL is quite restricted in its data-structuring facilities. Numbers and characters are elementary data types.”

**Identifiers:**

This is alright.

**Declarations:**

Good, although more emphasis could have been given to the fact that declarations are simply unnecessary in APL.

**Elementary structured type array:**

This is reasonable, but gives a slightly negative impression. Only basic APL is discussed.

**Array declarations:**

Fine.

**Operators:**

After quite a reasonable beginning, the bad news now starts. Firstly, someone has clearly decided to call APL primitive functions “operators” (which others have done in the past), presumably to try and get uniformity across the eight languages. However the section then covers only right-to-left execution, parentheses, negation, minus, plus, power, logical comparison, access by name, assignment and indexing. What is done is quite reasonable but woefully inadequate. There is a reference to a “Table of APL Operators”, but no such table appears in the book.

Some simple examples are given of the kind:

```apl
2+3=5
```

but the author does not seem to realise that all the examples will give logical 1 as the result, and the parentheses are missing.

**Expressions:**

This section is reasonable, except for the use of “infix” for dyadic and “polish prefix” (yes, with a small “p”) for monadic.

**Assignment:**

Quite good, except that only scalar and vector assignments are mentioned, which might cause some confusion since higher-order arrays have previously been introduced (albeit briefly).

**Conditional and unconditional branching:**

This section is a candidate for the nuthouse. It is frankly appalling and appears to have been written by someone in their first few days with APL. Much of the section is devoted to a laborious exposition of how “times iota” works; this is the only form used anywhere in the book, and often the iota is missing! After all this heavy going, multi-way branches are omitted altogether. With one exception, all branching is to line numbers. There is a reference to the fact that branch to label is “sometimes” useful because of dynamic line number re-allocation, but the example given is poor.

How easy it should have been to include the standard list of “condition, reduce, label” branches, and perhaps the standard IF function as well.

**Looping & iteration**

Like many of the sections, typographical errors abound. A simple interest calculation is chosen (which doesn’t actually need a loop in any of the languages – but never mind that). My APL complaints are that “minus reduce” is used (without explanation) for a simple numeric difference; it may be clever but can only be confusing in this context. Local variables are introduced in a header line without being mentioned anywhere in the book that I have seen. A less important point is the use of a trailing decision.

In particular though, there is no attempt to show how APL can avoid many types of loop altogether; another opportunity sadly missed.

**Function (user-defined)**

By way of complete contrast, this section is quite well done; even the typographical errors are fewer here than in other sections. It was a heart-felt relief to find four quite reasonable functions, and with branching to labels, no less! The author(s) have clearly battled to try and get common terminology, as noted previously. In earlier sections APL functions are called “programs” or “subprograms”, but this section fails to point out that this is what user-defined functions are as well. On the plus side, the terms “dyadic”, “monadic” and “niladic” are used correctly, although the attempt to discuss the presence or absence of an explicit result using “unlimited” or “limited” is not so good.

A final point – there are no examples using text or character data either here or elsewhere in the book. This appears to be the case for all the languages and is a notable omission.

**Subroutines.**

This APL section is brief but good. It correctly describes functions (as “functions”!) and function calling. It also refers properly to unrestricted recursive calls.

**Intrinsic/library functions.**

In this section the book starts to fall apart again. The text talks variously about “operations”, “generator primitives”, “expressions”, “primitives”, etc., whereas what it actually covers are three APL operators – reduction, inner product and outer product. There is further reference to the mythical Table of APL Operators. There is no discussion of library functions, or quad functions for that matter.

**Input/output.**

A very poor section with no mention of “quote-quad” nor of other forms of I/O available on any reasonable system. There is a passing reference to files which are “not normally provided”, but at least “some recent APL implementations include such features”.

**Program halts.**

The entire entry is “Not applicable”. The authors have presumably never heard of “quad delay”, or of function-defined halts, etc.

**Documentation.**

The final subsection deals with comment statements within a function in a moderately acceptable way, although the example given is poor.

### Sample programs.

Two sample programs are included and the best word to describe them is “hideous”. Riddled with typographical errors, as usual, but also with such charming features as:

> numbered header lines;  
> all branches use “times iota” to line numbers;  
> two “quad” entries for data input, rather than a vector;  
> etc.

The examples under user-defined functions could not be called brilliant, except perhaps in comparison with these.

### Appendices.

| | |
|---|---|
| I. | Pascal delimiter words (1 page) |
| II. | ANSI Cobol reserved words (2 pages) |
| III. | Summary of Cobol formats (4 pages) |
| IV. | PL/1 built-in functions (1 page) |
| V. | C syntax summary (2 pages) |
| VI. | PL/1 Arithmetic built-in functions |

Without checking a reference manual, I believe that IV and VI are both PL/1, so perhaps one of these should be the missing APL table.

### Glossary.

An excellent glossary comes last, although it is far too extensive for the subject matter of the book. It includes gates, bytes, buffers, cascaded arrays, clock pulse, etc. – terms which don’t appear at all in the text. Some of the 25 pages used (out of a total of only 122) could have been put to better use.

Well that’s the end of the book as such, but I can’t leave without listing some of the more glaring omissions. Workspaces and system commands are mentioned but only in the Overview. The following are not covered at all:

> many of the important functions;  
> local and global variables;  
> quad functions and variables;  
> quote-quad and other I/O forms;  
> text or character data;  
> library workspaces and functions;  
> public domain software; draft ISO standard;  
> portability; fast prototyping;  
> modularity;  
> access to other languages and systems;  
> availability on micros;  
> nested arrays;  
> user-defined operators;  
> other features of enhanced APLs.

Before summing up, I will paraphrase some of the claims made on the back cover:

- Enables comparison of all eight languages at a glance.
- Makes for rapid selection of the most appropriate language.
- Transition between the eight languages made easy.
- Enables design of completely new languages.

Leaving aside the last, rather grandiose, claim, the very good design and style of the book, should have made the other claims possible. However the appalling errors and omissions in the APL partly nullify these claims, certainly as far as APL is concerned. I imagine a potential APL user would be totally confused.

As for my other interest – can it help me quickly to get a grasp of C? Well it appears to give me something of the flavour of the language, but naturally I am left wondering how many errors there are in the C entries. (A cursory look at the Fortran and Basic parts suggests that these are not too bad, but I still wouldn’t trust them without a critical review.) So unless someone will kindly review the C parts for me, it looks as though I am going to have to fork out for *Kernigan and Ritchie* after all, and I suggest that anyone wishing to learn APL sticks to *Gilman and Rose*.

My overall sentiment is one of intense disappointment; such a good idea was ruined in the execution. The book is well worth a look (if only to see what might have been), but I have not been able to track down a U.K. supplier; in any case I would recommend your local library, rather than spending well-earned money on this edition. A second edition, thoroughly checked for accuracy and completeness would be well worth having, and I am waiting to hear from the Association in New York whether or not one is planned.
