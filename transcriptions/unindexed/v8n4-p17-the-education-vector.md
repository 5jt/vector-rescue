---
title: The Education Vector
authors:
- Alan Mayer
volume: '8'
issue: '4'
page: '17'
unindexed: true
transcribed: 'from page images of VOL.8-NO.4-APRIL-1992.pdf, pages 19–21 (printed 17–19); Claude, 2026-10-12'
review: draft
tags:
- education
- programming techniques
queries:
- "The section’s own text only: its title page (printed 17, with its own contents list), the Editorial (printed 18), and “Email Contact” and “More on MULTIPLY” (printed 19, unsigned, in the editor’s voice). The pieces it lists are transcribed separately: art10009680, unindexed/v8n4-p23-review-of-i-apl-for-the-macintosh.md, art10005260 and art10005270."
- "Following the project rule for individuals’ contact details, the street addresses and telephone numbers of Anthony Camacho (the British APL Association’s contact) and Rowena Small (membership enquiries) are omitted; Alan Mayer’s university address is kept."
---

## The Education Vector

**April 1992**

***Editor Alan Mayer***

This Education Vector has been reprinted from VECTOR Vol.8 No.4. VECTOR is the Quarterly Journal of the British APL Association. For more information about the British APL Association, please contact: Anthony Camacho, [address and telephone number omitted].

### Contents

| | | |
|---|---|--:|
| Editorial | Alan Mayer | 18 |
| APL and the Birthday Problem | Alan Sykes | 20 |
| Review of I-APL for the Macintosh | Bill McLean | 23 |
| How Much Water Under the Bridge? | Alan Mayer | 25 |
| Pass Me Another Diagonal Slice, Please! | Alan Mayer | 26 |

> Dr. Alan Mayer<br>
> European Business Management School<br>
> University College of Swansea<br>
> Singleton Park<br>
> Swansea SA2 8PP Wales, UK

> Ysgol Rheolaeth Busnes Ewropeaidd<br>
> Parc Singleton,<br>
> Abertawe SA2 8PP

Tel. 0792-205678 Ext.4274 Fax: 0792 295626 JANET: MAYER@UK.AC.SWAN.MS

## Editorial

It seems that another three months have passed since I wrote the last editorial for Education Vector. Looking back, I note my comment about the possible demise of the USSR - by the time anyone read it, of course, the event itself was ancient history (does anyone apart from the editor read editorials?). Perhaps I should confine my comments to things less transient than mere empires - such as the continued growth of the world-wide APL community.

On the subject of the last edition, I must apologise to Neil Sheldon for two typographical errors in our reproduction of his letter about Simpson's Rule. The quantities h3 and h4 should have referred to the third and fourth powers of h respectively.

I am keen to keep in close touch with developments at schools where APL is being used, and in this context I particularly welcome the contribution to this edition by Bill McLean of Dunoon Grammar School. If you are a teacher or pupil at a school using APL, or for that matter if you are considering using APL in future, please write and tell me about it. Our readers will also, I know, be pleased to see a contribution from Alan Sykes, my predecessor as editor.

Readers of Education Vector may not all be aware that it is reprinted from Vector, the official journal of the British APL Association. The sixteen-page reprint is delivered free of charge to anyone who is interested in APL. So if you are reading someone else's copy, or know of someone who would like to receive a copy, just drop me a line/phone/fax/email - I will be glad to add names to our distribution list.

The full journal, Vector, is distributed to members of the Association. If you are interested in joining, please write to Rowena Small, [address omitted]. Currently the UK private subscription is £12 per annum, for which you get four copies of Vector (144 pages per edition) and notice of meetings etc. Members and non-members are welcome to attend the meetings, most of which take place in the IEE Building (next to the Savoy Hotel) in London. Our programme for the coming months includes: (i) "A Tutorial in J" by Donald McIntyre on 27th March, (ii) a talk on the ISO APL language standards and talks by Adrian Smith and Maurice Jordan on 1st May, (iii) the Annual General Meeting, with news from SigAPL and their idiom collection (by Dick Bowman) and a video of the APL91 panel discussion "25 Years of APL" on 12th June.

### Email Contact

We have received several email messages from readers in recent months, and it has been suggested that this could be a useful medium to encourage communication between APLers. We are compiling a list of email addresses, with a view to distributing news items, suggestions and APL tips to those who are interested.

If you have an email address, contact me (MAYER@UK.AC.SWAN.MS) and tell me what you think we should be doing for you.

### More on `MULTIPLY`

My program `MULTIPLY` in the last edition seems to have interested a few people, but as yet I have received no contributions in that line. In response to the suggestion that I could generalise the program to test things other than multiplication, I offer the following:

```apl
[0]    FUN TEST VALS;RV;ANS;I;TARGET;T
[1]    RV←¯1+VALS[2]+?(2×VALS[1])⍴1+-/VALS[3 2]
[2]    ANS←⍳0
[3]    I←1
[4]    T←0 60 60⊥¯1↓¯4↑⎕TS
[5]   LOOP:TARGET←(VALS[1],2)⍴RV
[6]    ⍎'TARGET←TARGET[;1]',FUN,'TARGET[;2]'
[7]    'What is ',(⍕RV[I]),FUN,(⍕RV[I+1]),'?'
[8]    ANS←ANS,1↑⎕
[9]    →((2×VALS[1])≥I←I+2)/LOOP
[10]   'You scored ',(⍕+/ANS=TARGET),' out of ',⍕VALS[1]
[11]   'in ',(⍕(0 60 60⊥¯1↓¯4↑⎕TS)-T),' seconds'
```

The left argument of `TEST` is a function, such as +, -, ÷, ×, etc. and the right argument is a 3-component vector: the number of questions, followed by the minimum and maximum values to be used. For example:

```apl
'+' TEST 10 5 15
```

will give you 10 sums (additions) of numbers chosen from the range 5-15. This is all pretty unsophisticated stuff - if you've got something better, please share it with us!
