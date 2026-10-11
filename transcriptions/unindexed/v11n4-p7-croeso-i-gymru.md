---
title: Croeso i Gymru
authors:
- John Sullivan
volume: '11'
issue: '4'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.11-NO.4-APRIL-1995.pdf, page 9 (printed 7; within Correspondence, the only letter, before APL 95 Panels and Workshops); Claude, 2026-10-11'
review: draft
tags:
- humour
- APL community
queries:
- "Untitled in print, under the section heading Correspondence; the title is ours, taken from the letter’s last line."
- "Kept as printed: the misspelt heading “Croesoe a Cymru” in the code (it is the letter’s subject)."
- "The telephone number in the P.S. is the Welsh Office’s, an organisation’s, so it is kept."
---

*From: John Sullivan, 8 March 1995*
{ .byline }

I really must complain about the heading on the top of page 50 of Vol.11 No.2.

```apl
      Croesoe a Cymru
SYNTAX ERROR
      Croesoe a Cymru
              ^
```

APL is very pernickety about its syntax. So should APLers be when dealing with other languages. Welsh has some peculiarities which I shall not go into here, but suffice it to say that you cannot have a C on the start of a word following the word *a*, no matter which version of the word *a* you are using (it will begin with G or Ch). Assuming that we can mangle our syntax (or make a user-defined function called *a*) we now get the following:

```apl
      Croesoe a Cymru
VALUE ERROR
      Croesoe a Cymru
      ^
```

because Welsh does not have a symbol called `Croesoe` in its symbol table (vocabulary).

Enough of this idiocy: you can see what I’m getting at. Let’s just say that I wish to complain that everybody tries to get their English (of whatever variant) correct, they try to get their APL (of whatever variant) correct, they even try to get their Russian correct. But nobody cares about getting their Welsh correct! This kind of thing is typical of the non-Welsh contempt of all things Welsh, and for a journal with delusions of academic excellence it just isn’t good enough.

The correct heading should, of course, be

Croeso i Gymru.

P.S. Maybe Vector ought to contact the Welsh Office in Cardiff and ask about the availability of their Welsh language spell-checker. It won’t find all of your errors, but it should find the ones I am complaining about here. Tel: 01222-488745.
