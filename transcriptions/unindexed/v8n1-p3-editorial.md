---
title: 'Editorial: Windows and APL'
authors:
- Jonathan Barman
volume: '8'
issue: '1'
page: '3'
unindexed: true
transcribed: 'from page images of VOL.8-NO.1-JULY-1991.pdf, pages 5–6 (printed 3–4); Claude, 2026-10-12'
review: draft
tags:
- user interfaces
- implementations
---

*by Jonathan Barman*
{ .byline }

Windows are wonderful! Most of you must be getting pretty fed up with those sentiments which seem to be getting ever more strident since Windows 3 has sold by the million.

Actually I think that windows are pretty hot stuff. My conversion came about after using OS/2 for about a year. As far as I am concerned the two key ingredients are the consistency of the user interface, and the ability to have several tasks running simultaneously.

The stated advantages of multiple tasks always seemed to me to be rather thin. Constantly switching from one task to another appeared to be a very disorganised way of working. However, having used multiple windows and multiple tasks I have now changed my tune. My basic ‘window set’ is APL in one window, the favourite text editor in another, a mainframe session in a third, and an appointments reminder running in the background. Hopping about between windows in order to use the best facilities in each seems to speed things up substantially. APL can be used as a super calculator and the results can then be pasted across into the word processor. Of course, if substantial quantities of data need to be transferred then you need functions and files, which comes down to much the same thing as running separate sessions.

The thing that really switches me on is the consistency of the user interface. Window hopping demands consistency. Constantly switching between mainframe and PC applications, where the user interfaces are so very different, is quite difficult to learn and is a bore. Most of the OS/2 applications that I have seen so far are very good, but unfortunately I have come across some which don’t stick to the rules.

Applications written in APL need to stick to the rules, as does the APL interpreter itself. Getting the APL interpreter to work with windows is a one time job, and one can only buy a version that has this feature. However, writing an APL application that is properly integrated with windows means that the APL programmer must be able to access all the windowing facilities. There should be no differences in the user interface just because the application has been written in APL. All the little features should be present, the dialogue boxes, standard editing of text, changing fonts, menu bars, buttons, etc. etc.

An APL application simply running in a window is not the same as one which is fully integrated into the environment. If I change the printer driver will the APL application know about it? The APL programmer may have taken great care to create buttons which look and feel like the real thing, but what happens if I change the button colour?

APL interpreters are now able to interface with windows. MicroAPL have had APL integrated into the Macintosh environment for some years. IBM, STSC and Dyalog have all recently announced interfaces with X Windows. We should expect a Windows 3 interface to be announced ‘real soon now’. In this issue there are several articles explaining how the interfaces work and how you can use them.

Windows programs seem amazingly complex, with several hundred function calls and as many global variables to set or access. A very low level interface is obviously desirable so that you can poke and tweak exactly what is needed, but APL’s interpretive overhead may make it too slow for some of the very low level activities - leave that for C programmers. APL needs a high level interface as well as a low level one.

I have a nasty feeling that every APL supplier will produce radically different high level interfaces. The big problem is that this is a chicken and egg situation. Until a high level interface is available it will be quite difficult to create serious, window-integrated, applications. It will be quite easy to provide APL cover functions to hide the awful window complexities, but I suspect that they may be too slow for live applications. There may be a small band of dedicated enthusiasts, but there probably won’t be a large enough group of people with strong views to influence the suppliers before something is actually produced. The APL ‘hacker’ will not be interested unless there is an interface available which is really easy to use.

This is the first issue of Vector with substantial articles about windows. Hopefully we will be able to have a constant supply of articles to keep you informed about progress on this important topic.
