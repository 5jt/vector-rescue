---
title: Steps Towards a Better Basic - part 1
authors:
- Anthony Camacho
volume: '1'
issue: '1'
page: '77'
unindexed: true
transcribed: from page images of VOL.1-NO.1-MAY-1984.pdf, pages 79–80 (printed 77–78; follows art10001000); Claude, 2026-10-03
review: draft
tags:
- APL in perspective
- humour
queries:
- "A reprint: the footnote reads “Reprinted by kind permission of DATALINK magazine”."
- "Slips transcribed as printed: “MID$(NAMES$,3,2,)”, “little point is keeping”, “reputaton”."
- "The outer-product table and the selection `[3 4;4 5]` (12 15 / 16 20) check by hand."
---

by Anthony Camacho
{ .byline }

When you want to know the value of a variable in BASIC you have to type ?VAR or P.VAR or even PRINT VAR. Just typing VAR has no significance. If it were given the same significance as PRINT VAR nothing would be lost and a good many key depressions saved. To find out the value of an array is even worse; you have to write a loop. There could scarcely be any loss if the same were done for arrays. Millions of BASIC programmers would be grateful if they could type ARRAY and have it displayed for them. Most of the “programmers’ toolkits” miss this opportunity to be really helpful; I have one that responds to DUMP with a display of all the single variables and their values but totally ignores the arrays.

This reluctance to deal with more than a single variable is odd because BASIC already deals with some multiple variables as if they were single. The string NAME$ may be ten or a hundred characters long — a thousand in some versions of BASIC — yet it can all be displayed by PRINT NAME$. Some of the loops in BASIC could be cut out by making this method of handling multiple variables available for numbers as well as letters. In that case NOS could contain 1 2 3 4 5 (or a list of works order numbers or part numbers).

Strings are only moved about, compared and printed; arithmetic on multiple variables brings complications. If one array holds stock quantity and another holds the prices for the corresponding items, the instruction LET VALUE = QUANTITY \* PRICE would create the new array called VALUE. Thus it is obviously useful to be able to operate on each variable in one array with the corresponding element in another array of the same shape, and to produce a third array of the same shape as the result. But there are occasions when a whole array needs to be multiplied by a single factor: exchange rates, discounts and inflation rates are factors that come to mind. There is no reason why DISPRICE = PRICE \* .90 could not create the array DISPRICE which is the price after 10% discount.

Such facilities offer the opportunity to create some more functions, such as would add the rows of an array or the columns or even all the items. It could be useful to convert an array of another shape (for convenience in printing it, if nothing else). There could also be a function to take each item of one array with each item of another. It could be called EWE (for Each With Each) and be followed by the operation needed in brackets, so NOS EWE(\*) NOS would give:-

```
1   2   3   4   5
2   4   6   8  10
3   6   9  12  15
4   8  12  16  20
5  10  15  20  25
```

My excellent cheap calculator changes its display for very small and very large numbers; they are shown in scientific notation. As in this improved version of BASIC, character and numeric variables can both hold single or multiple variables, there will no longer be any need to decide in advance which type of value each variable is to hold. VAR could now hold either a string or a number, and the interpreter could follow the example of my calculator and distinguish between numbers of different types; it will adjust the way the number is held from integer to floating point and back according to its value.

Of course this implies that all arithmetic will be done to some standard accuracy, because the interpreter would no longer know from the variable name whether a variable was wanted as an integer or single or double precision number, so would have to do everything in double precision.

Very few calculations would be appreciably slowed by this and all would be speeded up to a small extent by having only one method of handling. As computers get faster and cheaper the loss of speed will be less and less noticeable. And anyway if speed is important, the program should not be run under an interpreter but should be compiled.

String handling in BASIC demonstrates that in an interactive language there is no need to DIMension multiple variables. It is quite practical to assign them dynamically, but if that were done there would be a need for a function such as LEN (which returns the length of a string) for arrays. If the arrays were to be limited to one dimension then LEN would still be adequate, but it is often convenient to have tables of numbers (or lists of words) and it would be better to introduce a new function which reported all the dimensions of an array; it could be called SHAPE. The only reason this was impossible before was that the result could have had one or several numbers in it. Now that a variable will be able to hold one or several values there is no difficulty. So, in the example above SHAPE NOS would be 5 because NOS contains five numbers. SHAPE NOS EWE(\*) NOS would be 5 5. Also a way of extracting one or a group of the numbers will be needed. For strings BASIC has MID$(NAMES$,3,2,) to extract the third and fourth letter. In Sinclair BASIC, NAMES$(3 TO 4) does the same job better so NOS[3 4] could do the equivalent for the numbers, and pick out the third and fourth items. And (NOS EWE(\*) NOS)[3 4;4 5] would pick out

```
12 15
16 20
```

(each dimension separated from the next by a semicolon, taking lines first and columns second).

One possible objection that might be raised to this is that there would be many more reserved words. Even with BASIC as it is now there are occasions when a reserved word is inadvertently used as a variable name. If more reserved words are to be added steps should be taken to avoid confusion. Variables could be kept in lower case for example. This is already common practice with the Sinclair Spectrum and the BBC. It makes programs less tiring to read too. Originally BASIC was used on teleprinters without lower case but as even cheap microcomputers have lower case now there is little point is keeping to upper case only. It might be sensible to use the capital X as a reserved word for multiplication, for those who find the asterisk annoying.

Now for the surprise: this description, in all essentials, fits a language in current use on hundreds of microcomputers and mainframes. The language has a great many more attractive features which will be explored in further articles. It has a reputaton for being difficult because of the peculiar characters it uses instead of reserved words, and it cannot become widely popular while keyboards and displays and printers have to be specially adapted to use these characters. It has most of the virtues of such languages as LISP and LOGO and FORTH and a richer collection of functions than any other language. It should be more widely known. Its name is APL.

\* *Reprinted by kind permission of DATALINK magazine*
