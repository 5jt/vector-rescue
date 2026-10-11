---
title: I-APL Constraints
authors:
- Walter G Spunde
volume: '7'
issue: '2'
page: '25'
unindexed: true
transcribed: 'from page images of VOL.9-NO.2-OCTOBER-1990.pdf (misnamed: Vol.7 No.2), pages 27–28 (printed 25–26; within The Education VECTOR, after Dbase and Lotus files into I-APL); Claude, 2026-10-11'
review: draft
tags:
- education
- implementations
queries:
- "A letter, “From: Walter G Spunde, July 1990”, signed from the University College of Southern Queensland, School of Information Technology, in the Communications of The Education VECTOR, with an editor’s comment. It answers the editor’s comment on his “Function Sampling with I-APL” in Vector 7.1 (art10009260)."
- "The final character of the machine code call, after ZZ:, is printed as a Greek alpha; transcribed ⍺."
- "Kept as printed: “screenfull”; “site license”."
---

*From: Walter G Spunde, July 1990*
{ .byline }

Thank you for running my article FUNCTION SAMPLING WITH I-APL in the July issue of Vector.

I appreciate your comment on ways of clearing the screen without the need to create a screenfull of blanks (`25 1⍴' '`), although a stubborn streak in me is tempted to argue that closing down a screen from the top is more gentle on the user than shooting it out through the top like a sheet ripped from a typewriter. There is also the machine code call:

```apl
CL: ap11519 ⎕MC 1 2 1⍴'AB' ZZ A←203 0 0 25 80 ZZ B←ZZ ⎕FX 'ZZ:⍺'
```

… which achieves the result I prefer, and which one could not expect the average maths teacher to know. All this, however, is beside the point I was driving at in my article, which is, that teachers WILL want to focus attention on key areas without the distraction of their having to create certain essential tools for this study; that 32K workspaces are really too small for even simple tasks like graph-plotting and that the lack of such elementary facilities as built-in screen handling in I-APL does consequently push one’s patience to the limit.

Teachers who have to use I-APL, because of cost constraints, are not in the market for a site license for a commercial APL at this point in time. At the same time their students are often accustomed to playing with sophisticated games software. I do believe that the constraints imposed on I-APL are too severe to allow teachers to come to a happy balance between their needs and student expectations or even to exploit the full potential, especially in the graphics area, of I-APL.

How many teachers will feel that it is worthwhile developing a software library (of minuscule pieces) for I-APL? The result may well be that teachers conclude that APL would be wonderful if you could afford a commercial version, but otherwise you may as well forget about it, i.e. the same situation as before the I-APL project was initiated.

I hope I have not bored you with these comments and that you may pass them on to those more closely associated with the I-APL project, whose efforts I do most certainly appreciate and commend despite my criticisms.

Walter G Spunde

University College of Southern Queensland<br>
School of Information Technology

*Editor’s comment: I appreciate the argument, but your article showed just how much can be done in the way of producing excellent teaching material using I-APL despite the real problems discussed above.*
