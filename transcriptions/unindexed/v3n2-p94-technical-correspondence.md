---
title: Technical Correspondence (McDonnell)
authors:
- Eugene McDonnell
volume: '3'
issue: '2'
page: '94'
unindexed: true
transcribed: 'from page image of VOL.3-NO.2-OCTOBER-1986.pdf, page 96 (printed 94; the competition result follows on p.95); Claude, 2026-10-05'
review: draft
queries:
- "Answers Phil Last’s second letter in v2n3-p95-technical-correspondence.md. The timing table is printed in a small monospace face; the first entry under time is printed I (for 1). “DUPSOUT” is printed DUPSQUT, read as DUPSOUT."
---

## From Eugene McDonnell, May 27, 1986

Sir: The second letter from Phil Last in volume 2 number 3 of your magazine asked in its last paragraph ‘. . . why haven’t IBM (and others) done anything about this before?’ He is complaining about the fact that he can write defined functions for dyadic iota and membership that execute faster than the primitives. I’m sure he will be gratified to hear that I.P. Sharp Associates has done something about it. In fact, Bob Bernecky of IPSA reported on his speedups for these primitives at the APL73 conference in Copenhagen, so users of IPSA APL have been the beneficiaries of Bernecky’s speedups for thirteen years already. I give below some timings I’ve just made for Last’s cases on the IPSA timesharing system. The same measurements apply (roughly) to IPSA APL on the PC and on the XT/370 and AT/370, since all of these systems are code compatible.

```apl
For Q←100+?5000⍴2

expression          time(normalised)

((Q⍳Q)=⍳⍴Q)/Q              1
DUPSOUT Q                5.9

Q⍳Q                        1
Q DIOTA Q               16.7

Q∊Q                        1
Q MEMBER Q              16.5
```

The fact that these IPSA speedups (and there are many others in our APL system) are so little known has given rise to an occasional amusing incident. Several years ago we had a summer student come to work for us here in the IPSA Palo Alto office whose APL training had come on IBM APL systems. He challenged us to come up with the fastest expression that would do

```apl
((Q⍳Q)=⍳⍴Q)/Q
```

Our then branch manager Joey Tuttle submitted exactly that expression as his entry, and the summer student was sure that Joey had missed the point, whereupon Joey asked the student to time the entry. He did so and was startled to find that the primitive was far faster than the arcane code which he had been intending to dazzle us with.

Sincerely,

Eugene McDonnell  
Suite 201, 220 California Avenue  
Palo Alto, California 94306-1683  
U.S.A.
