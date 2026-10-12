---
title: J Questionnaire
authors:
- Jonathan Barman
volume: '8'
issue: '3'
page: '90'
unindexed: true
transcribed: 'from page images of VOL.8-NO.3-JANUARY-1992.pdf, pages 96–99 (printed 90–93); Claude, 2026-10-12'
review: draft
tags:
- language design
- APL in perspective
queries:
- "The questions are printed in italic, indented, each followed by an indented summary of the replies; they are given here as italic paragraphs followed by the replies."
- "J spellings are as printed: “: to :: and [ to }:” (the change between versions 2.9 and 3.0), `)off`, `0!:55`, `off =. 0!:55`. The bracket in “[ to }:” is small in the scan."
---

*by Jonathan Barman*
{ .byline }

In mid November I sent out a questionnaire to everyone who had had a copy of J to find out what their reactions were to the language. Articles for Vector have to be ready by 30 November, so this left very little time for replies. It was gratifying that 15 people were able to respond by that date.

Several of the respondents have got J but have no knowledge of APL, and their views are particularly interesting as their thinking has not been coloured by APL.

*Q: Was J easy to install?*

The majority found J so easy to install that they must have wondered why I asked the question. Chas Yates was the only one to have problems. He found that the tutorial files were written for J version 3.0 whereas he had been sent version 2.9. The 'spelling' is different between the two versions, so he had to fiddle about changing such things as `:` to `::` and `[` to `}:`. He also had to replace the line ending characters. I think Chas was unlucky in this respect, as my version 2.9 of J for the IBM PC had the correct tutorial files. Chas also had to change the J.PRG file to J.TOS to stop the Desktop (Presentation Manager) fouling up the system.

*Q: When you first fired up J did you find any difficulty with the editor? Was it obvious how to exit from J?*

The majority had no difficulty with the editor or in exiting from J. Donald McIntyre pointed out that the session manager has changed greatly and that the present version in 3.5x4 is great. The APL users found no difficulty with `)off` to exit. Now that exit has changed to `0!:55` in version 3.5 it is suggested in `STATUS.DOC` that you assign `off =. 0!:55` in your `PROFILE.JS`.

The Atari users did not get an editor at all. Characters can be typed on the command line and there is a destructive backspace, but nothing else. Not surprisingly, the Atari users were pretty rude about the 'editor'. Chas Yates hoped that the Atari was not going to be fobbed off as merely a games machine. It provides a cheap solution for those who cannot afford a PC or a Mac.

*Q: Is J easy to learn? Does a knowledge of APL help the learning process?*

Most found J difficult to learn, and felt that knowledge of APL was essential given the current state of the documentation. Simon Barker summed it up with the comment that learning J without the aid of a wide range of material means playing with the interpreter and relying on APL skills to aid experimentation. Donald McIntyre said that J is not easy to learn from the Dictionary, and, like APL, is best learned from a teacher.

Those who had little knowledge of APL had a slightly different view. Chas Yates felt that J was no harder than Forth, and Mark Whippey said that it was easy enough to get started. R Gillan said J was enjoyable to learn and useful in some areas of mathematics, especially induction and recursion formulae.

*Q: Do you like the Dictionary of J as a definition of the language?*

The Dictionary was generally liked. Simon Barker felt that it was a succinct and clear description of the language and useful as a basic reference text.

*Q: Could you learn J from the Dictionary of J? Was the tutorial in Appendix B useful?*

Donald McIntyre pointed out that it is not intended that you should learn J from the Dictionary. Since the Dictionary was all that Konrad Hinsen had, it had to be sufficient. Another commented that he felt that he was worrying away like a dog with a rag when someone could explain it better. Others felt it would be possible to learn J from the Dictionary, but it would take a lot of effort.

Several respondents with early versions of J did not have Appendix B of the Dictionary, but those who did have it found it useful.

*Q: Which features of J are difficult to understand?*

All of them, says Donald McIntyre, if you do not have the information! Simon Barker had difficulty using conjunctions and adverbs to derive verbs because they require a very clear understanding of how these constructions work in J. He also felt that J 'spelling' is more difficult than APL because of the use of modifiers to produce related symbols. Chris Brunsdon and Malcolm Rigg found function definition difficult, and the Suite variable an awkward method of program control.

*Q: Would you have found it easier to learn J if there were more extensive examples and exercises?*

A resounding YES to this one.

*Q: Did you enjoy learning J?*

Another resounding YES.

*Q: Which features of J are not very useful and could be dropped from the language?*

Most dared not comment, mainly because they had limited experience with J. Chris Brunsdon suggested that either APL-like programs with line numbers should be introduced, or insist entirely on tacit definition and operators for everything.

*Q: What additional features should be included in the language?*

Dave Ziemann suggested a better front end. Donald McIntyre and Chris Brunsdon would love graphics support. The remainder felt that they did not know enough about J to comment.

*Q: Does J give you new insights into programming techniques? Can you see improvements that should be carried over into APL?*

Most felt that they had benefited from studying J. Simon Barker likes the way that scan has been redefined to apply a verb monadically to increasing subsets of data. Chris Brunsdon likes the ability to assign verbs, adverbs and conjunctions to names, and could see this feature being incorporated in a new version of APL. Donald McIntyre says J is APL!

*Q: What should J be used for?*

The majority felt that J was best for teaching, education, intellectual stimulation, mathematicians and APL-type problems. Donald McIntyre uses it for everything now. Chris Brunsdon finds it useful for geographical data since he can handle arrays of complex numbers, but finds the inability to link J to graphics functions frustrating.

The only contrary note was from E Sargeant who thinks J will quickly become shelfware.

*Q: What sort of problems would be easier to solve in J than any other language?*

Dave Ziemann summed it up by saying that J is best for data transformations and array processing.

*Q: Would you be able to use J commercially?*

The majority of replies were a definite NO. Chris Brunsdon thought that there might be a possibility if the 640K barrier was broken, and Konrad Hinsen felt that an up-to-date user interface would be essential.

*Q: Why did you get a copy of J?*

The main reason seemed to be due to an interest in new languages, particularly one developed by Ken Iverson. Chas Yates and Konrad Hinsen wanted the power of APL without the hassle of special characters.

*Q: Do you like J?*

Everyone said YES. Chris Brunsdon thinks that J is an excellent idea, both as a 'tool of thought' and for rapid solutions of certain problems in practice. His complaints are just minor irritations.

One question that I did not ask was about the character set, and it was interesting to note that two users specifically got J because of APL character set problems. Simon Barker had ambivalent feelings about the subject. He likes being able to write and print J scripts in ASCII, but feels that J has lost something valuable without APL's symbology. APL was primarily a powerful notation that was then implemented as a programming language, but J is primarily a programming language that can be used as a (reasonable) notation. Because of this he finds J much harder to read than APL, J text is littered with the period and colon modifiers necessary to provide its rich symbol set and subsequently sacrifices some of the clarity and conciseness of APL.

Many thanks to the users who took the time and trouble to reply to the questionnaire. It is marvellous to be able to share their experiences in the language at this early stage of its development.
