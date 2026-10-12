---
title: The Education Vector
authors:
- Anthony Camacho
volume: '6'
issue: '2'
page: '17'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, pages 19–21 (printed 17–19); Claude, 2026-10-12'
review: draft
tags:
- education
- programming techniques
queries:
- "The section’s own text only: its title page (printed 17, with its own contents list) and the guest editorial (printed 18–19, headed “The Education Vector / Guest Editorial”). The pieces it lists are transcribed separately: the review of “APL Programs for the Mathematics Classroom” (art10005910), APL “RISC Programming Style” (art10004630/art10012110), unindexed/v6n2-p25-start-building-your-own-utilities.md and unindexed/v6n2-p29-i-apl-board-meeting-new-york.md. The I-APL Order Form (printed 32) is not transcribed."
- "The Contents line credits Alan Sykes, who remains the section’s editor (named on the title page); this issue is edited and its editorial written by Anthony Camacho as Guest Editor, so he is given here as author."
- "The editor’s and BAA Secretary’s departmental addresses are kept, as institutional addresses. The workspace name INSANITY, in the APL font, is set as code."
- "Kept as printed: the section’s contents list gives “Start Building Your Utilities” and “Minutes of I-APL Board Meeting”; “Gerard Langlet” without accent; “APL press”."
---

## The Education Vector

**October 1989**

**Guest Editor Anthony Camacho**

This Education Vector has been distributed free to everyone on the I-APL mailing list.

It is reprinted from VECTOR Vol.6 No.2. VECTOR is the Quarterly Journal of the British APL Association; for more information about the British APL Association, contact the Secretary: Graham Parkhouse, Dept. of Mech. Eng., University of Surrey, GUILDFORD.

### Contents

| | | |
|---|---|--:|
| Editorial - Programming Style | Anthony Camacho | 18 |
| "APL Programs for the Mathematics Classroom" by Norman Thomson | Reviewed by W. W. McLean | 20 |
| APL "RISC Programming Style" | G. A. Langlet | 23 |
| Start Building Your Utilities | Peter Branson | 25 |
| Minutes of I-APL Board Meeting | Sylvia Camacho | 29 |
| I-APL Order Form | I-APL Ltd. | 32 |

> Editor<br>
> Dr Alan Sykes,<br>
> Dept of Management Science and Statistics,<br>
> University College of Swansea,<br>
> Singleton Park, SWANSEA SA2 8PP

## Guest Editorial

*by Anthony Camacho*
{ .byline }

The gap between APL 89 and the British APL Association's conference on the APL Statistics Library is too short. Dr Sykes is overloaded and rather than let the set of Education Vectors become a sparse matrix I offered to have a go at filling the gap. I am asked to make it clear that this is not to be allowed to become a habit. Alan will be back in his editorial chair before you read this. I am starting work on 11 September - after the final copy date - so what you get is what comes to hand.

I-APL Ltd held an open board meeting at APL 89. The minutes are reproduced here. One of the main decisions taken was that, to survive, I-APL must become more commercial. This means that we will begin to pay directors, porters and staff for their services and that we will act as distributors for material which was not produced by I-APL. For example we have begun to distribute Norman Thomson's book "APL Programs for the Mathematics Classroom", published by Springer Verlag. This Education Vector begins with a review of it by William McLean, a physics teacher of Dunoon, who has just begun to try out I-APL. Education Vector ends with a new I-APL order form, simplified by including post and packing charges in the price of each item; there is no price increase.

One of the perennial APL arguments is about style in coding and if there is a theme to this Education Vector it is that. If you read the account of APL 89 you may notice that Adin Falkoff (the man who gave APL its name) is keen on brackets and semicolons and Gerard Langlet would like to persuade everyone to write APL using vectors rather than matrices wherever possible. There is a note from Gerard on the same theme here. Before you reject it out of hand, try it. The effort of trying to adapt to a new style will give you a new insight into APL. In another style we have some advice for beginners from Peter Branson.

Many APLers have strong views about style and there are disagreements that go right back to the roots of the language. If either of these contributions makes your blood boil, please write a rebuttal or a rejoinder. Remember that in the Education Vector we are primarily interested in teaching with APL and the urge for speed which so distorts the style of some commercial programs is less appropriate.

If someone objects that a discussion of style is out of place in Education Vector, saying that new APLers have enough to learn without bothering about it, I answer that the way you say something is indivisibly a part of the thing said, that APL is first a notation and the form of expressions is the essence of notation, and that the decision about what style you adopt should not be left until you have formed habits by default, some of which may be bad.

APL does have the equivalent of spaghetti in BASIC. It is 'semi-globals'. Nobody has a good word to say for them. Globals are bad enough, from the press they get. Just as G. A. Langlet would like to program without parentheses, Eugene McDonnell would like to program without variables. He has produced a beautiful example published by APL press as "The four cubes problem" and the functions are in the I-APL workspace `INSANITY`. The amount of work this program does is not trivial - it occupies a standard PC for about 28 minutes!

We have received two useful letters in response to my comment in Education Vector 5.4 about transfer of workspaces between BBC, PC clones and Archimedes. They are from John Dallman, who suggests using Kermit and from Malcolm Rigg who uses Beebdos software. Thanks to both.

Kermit is a serial transfer protocol and has been implemented on almost every computer ever heard of that has a serial interface. A simple cable (only three connections, I believe) joins the two machines and you set one machine to listen and the other to shout and the file is transferred rapidly and reliably. Kermit is in the public domain and is distributed by: Kermit Distribution, Department of Computing, Computer Centre, Lancaster University, Lancaster LA1 4YW. Cables may be obtained made up for the machines of your choice from: Fraser Electronics, 42 Elm Grove, Southsea, Portsmouth, Hants or RSD Connections, PO Box 1, Church St, Ware, Herts SG12 9EN

Beebdos is a program which runs on a PC clone and reads or writes disks which can be read by a BBC - DFS or ADFS. Malcolm says the software is widely advertised.
