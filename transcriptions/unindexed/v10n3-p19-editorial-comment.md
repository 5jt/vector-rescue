---
title: Editorial Comment
authors:
- Alan Mayer
volume: '10'
issue: '3'
page: '19'
unindexed: true
transcribed: 'from page images of VOL.10-NO.3-JANUARY-1994.pdf, pages 21–22 (printed 19–20; within The Education Vector, after Kenneth E. Iverson’s letter, before art10004420); Claude, 2026-10-11'
review: draft
tags:
- education
- language design
queries:
- "Printed under the subheading “Note on J for beginners by the Editor”, after Kenneth E. Iverson’s letter (unindexed/v10n3-p19-iverson-letter.md) under the heading “Letter and Editorial Comment”. The Editor of the Education Vector is Alan Mayer."
- "The four boxed displays are set here with box-drawing characters."
---

*by the Editor*
{ .byline }

## Note on J for beginners by the Editor

Norman Thomson made a mistake in J-ottings 1. It is only too easy to do and as Editor I have to admit that it was my responsibility to spot the error and correct it. I failed and will probably fail again. I find J very difficult.

Unlike Kenneth E Iverson, I feel that what we offer as a correct expression should be correct. Ken is unworried about an error, saying “If it doesn’t work then the reader will have to find out why and the effort will be good for him.” I wonder whether the complete absence of complaints on my desk about the error is because nobody spotted it or because everyone is too kind. The helpful suggestion Ken made in his letter, reproduced here, was that we should commission an article to explain composition.

We have done so. We hope to be able to publish it in April. Experienced APLers too easily think they have the right mindset to understand J. J is a dialect of APL or at least they have a common aim — to enable algorithms to be expressed briefly and without ambiguity but almost everyone has difficulties when they begin to learn J. Even Donald McIntyre admitted to coming close to despair before he could write J expressions which did what he wanted.

There is no single text which we can advocate as the best way to learn J and even the articles in Vector are imperfect as the early ones were written in early versions of J which have been superseded. Some expressions have changed meaning. Even the Dictionary of J has occasional omissions as Gene McDonnell remarks (see *At Play with J* in this issue of Vector).

A valuable aid to a learner who wants to see how an expression will be evaluated is to enter the expression without arguments. For example when you enter `>:@]-[` the system displays its interpretation of this: `>:@]-[`

```j
┌────────┬─┬─┐
│┌──┬─┬─┐│-│[│
││>:│@│]││ │ │
│└──┴─┴─┘│ │ │
└────────┴─┴─┘
```

This shows that the effect is `( >: @ ] ) -[` as Norman Thomson says. Another of Norman Thomson’s expressions is: `+/%#`

```j
┌─────┬─┬─┐
│┌─┬─┐│%│#│
││+│/││ │ │
│└─┴─┘│ │ │
└─────┴─┴─┘
```

But when you give it an argument its interpretation changes, unless you have inserted parentheses round the expression shown.

Of course if you supply an argument the result is no longer the interpretation of the expression but the result of the expression applied to the argument so you have to use a little cunning to see the effect: you supply an argument in the form of a verb which has a suitable argument as a result `+/%#9:`:

```j
┌─────┬────────┐
│┌─┬─┐│┌─┬─┬──┐│
││+│/│││%│#│9:││
│└─┴─┘│└─┴─┴──┘│
└─────┴────────┘
```

[Note: the verbs `0:` to `9:` were added to J in version 6.]

The way to get the result you want is to enter parentheses: `(+/%#)9:`

```j
┌───────────┬──┐
│┌─────┬─┬─┐│9:│
││┌─┬─┐│%│#││  │
│││+│/││ │ ││  │
││└─┴─┘│ │ ││  │
│└─────┴─┴─┘│  │
└───────────┴──┘
```
