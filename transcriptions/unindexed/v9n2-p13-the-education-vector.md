---
title: The Education Vector
authors:
- Alan Mayer
volume: '9'
issue: '2'
page: '13'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1992.pdf, pages 15–17 (printed 13–15, to the middle of printed 15); Claude, 2026-10-12'
review: draft
tags:
- education
- APL community
queries:
- "The section’s own text only: its title page (printed 13, with its own contents list), Alan Mayer’s Editorial (printed 14) and the unsigned notice “Free Subscriptions to Education Vector!” (top of printed 15). The pieces it lists are transcribed separately: unindexed/v9n2-p15-new-email-discussion-list.md, art10011140 (Exploring MAGIC) and art10005280 (Some Notes on Direct Definition)."
- "The editorial has no byline; the section’s contents list gives Alan Mayer as its author. The editorial refers to Bill McLean’s “The MAGIC Puzzle” (Vector 9.1, art10005920) and Alain Delmotte’s “Workspace Listing in I-APL” (Vector 9.1, art10002830)."
- "Following the project rule for individuals’ contact details, the street addresses and telephone number of Anthony Camacho (the Association’s contact) and Rowena Small (the membership address in the notice) are omitted; the editor’s university contact details are kept."
- "Kept as printed: the contents list gives “David Ziemann” where the editorial says “Dave Ziemann”; “Workspace Listing in IAPL” (the article is headed “I-APL”); the correction ends at line [1] of ΔΔLIST, as printed."
---

## The Education Vector

**October 1992**

***Editor Alan Mayer***

This Education Vector has been reprinted from VECTOR Vol.9 No.2. VECTOR is the Quarterly Journal of the British APL Association. For more information about the British APL Association, please contact: Anthony Camacho, [address and telephone number omitted].

### Contents

| | | |
|---|---|--:|
| Editorial | Alan Mayer | 14 |
| Exploring MAGIC | David Ziemann | 16 |
| Some Notes on Direct Definition | Alan Mayer | 27 |

> Dr. Alan Mayer<br>
> European Business Management School<br>
> University College of Swansea<br>
> Singleton Park<br>
> Swansea SA2 8PP Wales, UK
>
> Ysgol Rheolaeth Busnes Ewropeaidd<br>
> Parc Singleton,<br>
> Abertawe SA2 8PP
>
> Tel: 0792-205678 Ext.4274 Fax: 0792-295626 JANET: MAYER@UK.AC.SWAN.MS

## Editorial

Welcome to Education Vector. I note, with some surprise, that I am embarking upon my second year as Editor. My first year has been one in which much has occurred in the world at large, and many plans have been laid. I am grateful to so many readers who have contributed their work, their views and their ideas. My receipt of “email” in particular has increased considerably since I took over the editorship of this journal!

I am particularly pleased with the response to my request for material for use in education. Several people have responded with ideas and offers of help. My own inability to devote enough time to the task has tended to make progress slower than it should be, but I shall endeavour to clear the back-log and make some of the material available as soon as possible. I am still very keen to hear from any schools that would be interested in trying out APL.

In the last issue, Bill McLean contributed a game called MAGIC and issued a challenge to readers: “Any offers of an algorithm (in APL of course) to solve MAGIC problems?”. Dave Ziemann has taken up that challenge, and a good deal of this issue of Education Vector is devoted to his solution. Dave’s approach to programming by direct definition is instructive, and his article demonstrates very well how this form of APL can be used to “mimic” the thought processes involved in problem-solving. His approach is fundamentally second generation, and he uses APL\*PLUS II.

I have added a note of my own on direct definition, including a workspace to provide direct definition facilities, which I hope will help those who do not have this mode of input implemented in their APL, or who have not come across this method before.

Alain Delmotte has asked me to include a small correction to his paper on “Workspace Listing in IAPL”. On page 38 of the last issue, the functions `ΔΔHEADINGS` and `ΔΔLIST` were “glued” together. I think the line-numbering makes it clear where function `ΔΔHEADINGS` ends and `ΔΔLIST` begins. Those few lines should read:

```apl
[8]   ΔΔPRINT ''
     ∇

     ∇ ⍺ ΔΔLIST ⍵
[1]  ⍝ Successively lists the variables and functions
```

### Free Subscriptions to Education Vector!

If you are reading someone else’s copy, or know of someone who would like to receive Education Vector, please let the Editor know. Education Vector is distributed free of charge to over a thousand readers each quarter.

If you are interested in APL, you may like to join the British APL Association. Members receive four issues of the journal Vector (144 pages per issue) of which Education Vector is a part. To obtain an application form, write to Rowena Small, [address omitted]. The current subscription is £12 per annum (UK private membership). Student membership is half price.

A final thought. A subscription to the BAA makes an ideal Christmas present for an APLer!
