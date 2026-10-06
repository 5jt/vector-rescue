---
title: Idioms and Problem Solving in APL2 (talk at APL86)
authors:
- Alan Graham
- John Sullivan
volume: '3'
issue: '3'
page: '77'
unindexed: true
transcribed: 'from page images of VOL.3-NO.3-JANUARY-1987.pdf, pages 79–93 (printed 77–83 and 86–91; pp.84–85 are adverts); Claude, 2026-10-05'
review: draft
queries:
- "Printed “Delivered by Alan Graham at APL86 / Transcribed by John Sullivan”: a transcript of a recorded talk. The APL examples are printed in a small monospace face; the dieresis of each is set as two dots, here ¨."
- "Checked: (⊂I)-0 1 with I←9 2 13 gives 9 2 13 and 8 1 12, which pick IBM and HAL from A←' ABCDEFGHIJKLMNOPQRSTUVWXYZ' in origin 0, as printed."
- "The DS (DISPLAY) results are printed with the ASCII box characters of APL2’s DISPLAY (. → - | ' ~ ↓ ∊); transcribed with those characters, the alignment approximate. Checked: X←(2⍴¨3 5 7)⍴¨⊂I,0 with I,0 = 9 2 13 0 gives the three matrices printed (3 3, 5 5 and 7 7 reshapes), and X⊃¨¨⊂⊂A spells them out in IBM and blanks."
- "DD (p.82): the local names carry an overbar suffix (Z¯, F¯, X¯, Y¯), as the talk explains; transcribed with ¯. [4] is printed `⎕ES(~F¯≡⍕F¯)/5 4`, [5] and [7] `(('⍵'=F¯)/F¯]←⊂' X¯ '` with a ] for the closing parenthesis, read as ). The VALENCE ERROR remark refers to ⎕ES codes."
---

Delivered by Alan Graham at APL86
{ .byline }

*Transcribed by John Sullivan*

*(Editor: The start of the tape is unfortunately inaudible.)*

. . . A very common one (idiom) I call ‘All Right’ takes each item on the left and pairs it with the entire array R on the right. I have some examples which will make this clear. To take the whole array on the right, if that’s what you want, you don’t want it itemwise.

```apl
L f¨ (⊂R)
```

‘All Left’ is the whole array on the left.

```apl
(⊂L) f¨ R
```

Now what’s the final combination of EACH and ENCLOSE? How about if you enclose both of them? Not interesting or important, because you have that identity.

```apl
(⊂L) f¨ (⊂R)  ←→  ⊂ L f¨ R
```

So there’s ‘All Right’, ‘All Left’, but ‘All Both’ doesn’t make sense.

One thing you find when using EACH is that the derived function with RESHAPE is a scalar function.

What that means is that like addition and subtraction items get paired and, if you have a scalar, scalar extension occurs; dealing with scalars you can think of it as the RESHAPE to the size of the non-scalar and then the function is applied pairwise. This is important because RESHAPE is not a scalar function, but RESHAPE EACH is a scalar function. FOO EACH is a scalar function – I don’t care what FOO does, it’s a scalar function. I found that hard to adapt to, once I’d adapted to it I say, as you do once you’ve learned something, “Of course It’s simple”, but you don’t say that while trying to adapt to it because it’s tough.

OK we’ll look at some examples and try and adapt to it. A two-element vector plus a two-element vector, you get a two-element vector, same thing here,

```apl
2 3⍴¨4 5
```

that’s 2 rehape 4, 3 reshape 5. Well, how about if I’d like for instance down here I’d like two 2 by 3 matrices, one filled with 4s, one filled with 5s. That’s it, I want to use the entire left argument over and over again, so I enclose it, you get scalar extension

```apl
(⊂2 3)⍴¨4 5
```

so it’s the same as writing (2 3)(2 3) both in parentheses RESHAPE EACH and then carry out

```apl
(2 3⍴4),(2 3⍴5)
```

And the final one, ‘All Right’

```apl
2 3⍴¨⊂4 5
```

I get enclosed vector 4 5, and enclosed vector 4 5 4. And this occurs time after time after time. I guess – er – well I’ll leave it at that.

I want to show you some other applications of this, this in action. Garth Foster called me up, well, I guess I called him, a few weeks ago; he had a question that after a little head-scratching I came out with, I knew the answer, I don’t know why it took me so long. He said you have the alphabet and you’d like to map indices into the alphabet into words, and more specifically, he wanted to get a nested array of indices representing an array of words, and he’d like to do that mapping and extract the words. So, here’s one reason why I use index-origin zero, so you can put the blank in front and A is one, and blank is zero. Here is my alphabet

```apl
A←' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

and with PICK it works easily, you can take out the I like that

```apl
      9⊃A
I
```

and during one organized conference they had the competition for what words and phrases in history mean. Before this talk, because there is the CHIPMUNK idiom, they had it after this talk everyone in this room wanted to win that prize. Why is it called the CHIPMUNK idiom?

```apl
9 2 13⊃¨⊂A
```

You see, doesn’t that look like a chipmunk to you? Eyes, and big fat cheeks there. So there’s the chipmunk idiom for you. It has to be asked, which one of the templates is it, pairwise, all left or all right; which one am I using? (Pause, then answer from the audience ‘All Right’) All right. I’m taking the entire alphabet, and picking from it the ninth, then picking from it the second, then picking from it the thirteenth and I get IBM out of it and, well, hold on, what is the F; the F is PICK EACH, that’s the scalar function that I call F. So that’s just a case of All Right.

Now, what Garth wanted to do – Oh, so you could say it was an index I’ll call I, and then you could use the chipmunk again

```apl
      I←9 2 13
      I⊃¨⊂A
IBM
```

and then you could say, well I want to add one to each number and compare that to the addition of zero,

```apl
      II←(⊂I)-0 1
      II⊃¨¨⊂⊂A
IBM HAL
```

but then of course I’d get IBM and HAL from 2001! This is what Garth wanted to do, and this is another example of All Right, because PICK EACH ENCLOSE (the chipmunk idiom) is the chipmunk function, you could call it, so I’d like to do a list on the left, that function, EACH, All Right; so I have this idiom which really would have been an obscure question. What do you think that idiom is called? You’ll never guess so I’ll tell you. That’s called ’chipmunk with glasses and a toothache’. (Laughter) You’ll have to use it a whole bit more and have great fun.

When I invite people in to see these things or give demos I tell them that this is my APL2 PC, even though it’s on the mainframe, and these are my APL2 toys, although I think they’re not as trivial as toys. Another way to do this if you want to avoid the pepper effect, you can define a sub-function called vector indexing, which is very nice.

```apl
[0]  Z←I VI V
[1]  ⍝ VECTOR INDEX
[2]  Z←I⊃¨⊂V
```

now you can say ‘jot-dot-VI’, you can say ‘VI-each’, you can say ‘VI-each-each-each-each’, and you can use the function without thinking ‘chipmunk’, which might not have much to do with vector indexing. This works fine, (inaudible), and now it becomes apparent that we’re using All Right here, because here is the function, a list of indices or a list of lists of indices, and All Right on the right.

```
      DS II
.→-----------------.
| .→-----. .→-----. |
| |9 2 13| |8 1 12| |
| '~-----' '~-----' |
'∊------------------'
      DS II VI¨⊂A
.→-----------.
| .→--. .→--. |
| |IBM| |HAL| |
| '---' '---' |
'∊------------'
```

Now lets have some fun with EACH. Take a look at that.

```
      X←(2⍴¨3 5 7)⍴¨⊂I,0
      DS X
.→----------------------------------------------------.
| .→------. .→------------. .→-----------------.      |
| ↓ 9 2 13| ↓ 9  2 13 0  9| ↓ 9  2 13  0  9  2 13|    |
| | 0 9  2| | 2 13  0 9  2| | 0  9  2 13  0  9  2|    |
| |13 0  9| |13  0  9 2 13| |13  0  9  2 13  0  9|    |
| '~------' | 0  9  2 13 0| | 2 13  0  9  2 13  0|    |
|           | 9  2 13  0 9| | 9  2 13  0  9  2 13|    |
|           '~------------' | 0  9  2 13  0  9  2|    |
|                           |13  0  9  2 13  0  9|    |
|                           '~-------------------'    |
'∊----------------------------------------------------'
```

Well, let’s see. Only two EACHes. ‘Two reshape each’ you get 3 3 (pause) 5 5 (pause) 7 7. We say we want to apply each one of those to the entire thing to the right, which are the indices I followed by zero, so we want to do 3 3 reshape of that whole list, then a 5 5 reshape of that whole list, and a 7 7 reshape of that whole list, and we get this beautiful thing.

I feel that with APL1 I’ve been pedalling a very very nice bicycle, and with APL2 they gave me a motor (some chuckles from the audience). It’s very easy to get horribly carried away, and you should maybe restrain yourself; so I can use the chipmunk with glasses to solve Garth’s problem of mapping arrays of indices into characters

```
      DS X⊃¨¨⊂⊂A
.→------------------------.
| .→--. .→----. .→------. |
| ↓IBM| ↓IBM I| ↓IBM IBM| |
| | IB| |BM IB| | IBM IB| |
| |M I| |M IBM| |M IBM I| |
| '---' | IBM | |BM IBM | |
|       |IBM I| |IBM IBM| |
|       '-----' | IBM IB| |
|               |M IBM I| |
|               '-------' |
'∊------------------------'
```

A little bit different example, of how EACH helps you out, and how derived functions and operators can help you out. I just made this array that I’d like to manipulate, and you might make that array just experimenting: it’s a 3-element vector, and whatever you can do: a scalar, a vector and a matrix. If you display it it looks like this

```
      DS R←3.14 'ABRACADABRA' (2 3⍴4 3 2 1)
.→--------------------------.
|      .→----------. .→----. |
| 3.14 |ABRACADABRA| ↓4 3 2| |
|      '-----------' |1 4 3| |
|                    '~----' |
'∊---------------------------'
```

You take the shape and, sure enough, it is a three-element vector

```apl
      ⍴R
3
```

Sometimes I ask my students a trick question, “How many elements in a 3-element vector?” They get that (laughter). “How many elements in a scalar?” One, we know that, but sometimes – hmmm – zero? “What’s the shape of a scalar?” One? No, so the edge conditions are tricky; this is a normal 3-element vector, nothing up my sleeve. You also may want to say, what’s the shape of each one of those items

```apl
      ⍴¨R
  11  2 3
```

and you can clearly see the first item is empty, which is correct (It is indented, it’s hard to seewhen you get a wider display font like this), an 11-element vector and a 2 by 3. In the spacing of the original system this is pretty close to it, there’s two blanks there, and so you can only default this place, you do get the feel for the separation here if you look carefully. I find I don’t use this display too terribly often because I do like to default this place. One of the other things I tried is – Ah yes, of course, I want the rank of each one, zero one two

```apl
      ⍴⍴¨R
3
```

That doesn’t work. Why? Anybody know? I mean, three? Where did that come from? (answer from audience RHO-EACH) Rho-each is a scalar function, what’s a scalar function on a 3-element vector? A three-element vector: that’s not a trick question. So what’s the shape of a 3-element vector? Three. Even my students get that, very easily. So, of course I tried this, thinking “Ah, I’ll fix it”. (laughter)

```apl
      (⍴⍴)¨R
SYNTAX ERROR
      (⍴⍴)¨R
       ∧∧
```

and dialled up Jim Brown and said “Hey, it doesn’t work”. Well, sure, we could make this work, but I think rho-rho – I think you mean rho-rho made-up in a direct-definition form, but you could mean W-rho-rho-W or you could mean – there’s many different functions so we didn’t choose one: no, that doesn’t work. The thing is not a function, so you get SYNTAX ERROR. Well, you can do it rho-each-rho-each

```apl
      ⍴¨⍴¨R
 0  1  2
```

and here’s some pepper occurring. You’ll also notice the spacing here, there’s two spaces between the items, so if I’m doing rank-each, I know the rank of anything is a single number and I prefer the simplest data-structure possible so now we really get the scrambled eggs with pepper and you get zero-one-two and that’s exactly the right answer I want.

```apl
      ↑¨⍴¨⍴¨R
0 1 2
```

Hmmm, what can I do. Well, I take stock and write this rank function,

```apl
      ⎕FX 'Z←RANK X' 'Z←↑⍴⍴X'
RANK
```

and that I find the easiest way without popping into an editor, just define on the fly, and then you RANK-EACH

```apl
      RANK¨ R
0 1 2
```

I find that what I want is not to have to stop to define functions then to come back to all my problems but I never have the function RANK lying around in all my workspaces because it’s just too easy, so what do I do? (How am I doing on time? OK? What’s that? Fifteen minutes, ah, OK means different things to different people (laughter) I can only give one percent of my talk now (more laughter).) I want an operator, an operator to the rescue. My friend Phil Benkard calls this idea a ‘Nonce function’ (Nonce means ‘for the moment’) Some APL systems give out NONCE ERROR when they’re not sure what should be implemented or not. IBM says “We can’t do that” because nonce is pre-announcing something that’s going to be . . . . OK. I call these nonce functions so I can have a function for the moment so I can apply each to it, or outer product or what-have-you, and then have it evaporate.

Here, what I do is I use the simple form of direct definition what I mean is I don’t do the if-then-else case, sure you can do it, but I have another way to do if-then-else and what I do is I take a function in a character representation form, a character string. Operators always produce real live functions so anywhere in APL2 where we say you can use a function, you can use a primitive or a defined function or a derived function. So therefore what I get out of this operator taking a data operand, which I feel a little queasy about, is a derived function. I don’t feel so bad because the F represents a function as character. So let’s go through it.

```apl
[0]  Z¯←Y¯ (F¯ DD) X¯
[1]  ⍝ Direct Definition (APL2's Lambda)
[2]  ⎕ES(2≠⎕NC'F¯')/5 4          ⍝ Variable?
[3]  ⎕ES(1<⍴⍴F¯)/5 2             ⍝ Vector/Scalar?
[4]  ⎕ES(~F¯≡⍕F¯)/5 4            ⍝ String
[5]  (('⍵'=F¯)/F¯)←⊂' X¯ '       ⍝ Replace ⍵←right
[6]  F¯←∊F¯                      ⍝ Simple
[7]  (('⍺'=F¯)/F¯)←⊂' Y¯ '       ⍝ Replace ⍺←left
[8]  F¯←∊F¯                      ⍝ Simple
[9]  '⎕ES ⎕ET' ⎕EA 'Z¯←',F¯      ⍝ Do it under trap
```

What I do is I do the error checking first, as primitives must do error checking of their input before they try it out, and I’ll read it in English as fast as I can. F must be a variable coming in, not a function because this doesn’t apply. Then I say if it’s over rank 1 it’s no good, it’s got to be a string, then I say check – if it’s not a string blow up. I remember that 5 4 is a domain error, but I got it wrong – I put in 5 1 and was getting VALENCE ERROR. Well, I sit with the book next to my desk, or I could type it in quickly to see what error I get. Right here I say if there are any omega’s in this string replace them with the name of the argument – oh, I should mention, why the little marks next to each one of the names? I’m trying, in a vain attempt perhaps, to avoid name conflict, because the thing you’re executing may reference variables, global variables, or may call subfunctions – if you have a subfunction by the name of X, or worse F, this doesn’t work If I had not put the suffix of an overbar; now things won’t work if you have a subfunction F-overbar, but I’m using that convention to say “these names I really want to be strictly local” APL doesn’t give you the facility to say “make them strictly local”, so I do it by naming convention.

So finally I say take this square peg and fit it into the round hole because this is 4 characters long and I’m replacing occurrences of scalars, so I enclose it, get rid of the nesting, and enclose the other argument. Now I never do a name-class to see if this function is monadic or dyadic if it’s monadic there won’t beany alphas in there I don’t even have to check. The last statement says execute the right argument and if it fails for any reason take the error you got which is stored in ⎕ET and record it one level higher because I may have a function whose argument I pass is not in the domain, the operator has no idea of what’s right, it blindly applies functions, so this is very common in operators, to say do it now and oh by the way if you blow up don’t report it here, report it one level up. Just as you don’t get the assembler language code for outer product, if you do an outer product jot-dot-divide and you have some zeros lying around, I don’t want the code for my operators to show up in the same way. So, how can I use this? There’s my original array

```apl
      R
3.14 ABRACADABRA   4 3 2
                   1 4 3
```

I would like to say the rank of each item, conveniently, and I say it here

```apl
      '↑⍴⍴⍵' DD¨ R
0 1 2
```

I’d like to say de-duplicate each one: give me the nub of each item,

```apl
      '((⍵⍳⍵)=⍳⍴⍵)/⍵←,⍵' DD¨ R
3.14  ABRCD  4 3 2 1
```

and it works. Also, you can be the judge, sometimes I put unnecessary parentheses to enhance clarity, and, looking at it myself I don’t know whether it enhances it or not. Would you like parentheses to the left of the quote and directly to the right of the DD to say that thing in parentheses is my function? I don’t know, does it help or hurt? (mixed replies from the audience).

Let me show you some other things, what you should do when you get started. This is what Bob Bernecky said APL2 didn’t have; well maybe he’s right but with DD I can do this without having to define anything, so APL2 does have it. This is the cartesian product of two lists of things

```apl
      'APL' 'AI' ∘.('⍺ ⍵' DD) '' 1 2 86 (2 3⍴⍳6)
APL      APL 1    APL 2    APL 86    APL  0 1 2
                                          3 4 5
AI       AI 1     AI 2     AI 86     AI   0 1 2
                                          3 4 5
```

and you can see APL being paired with each item on the right in every combination using outer product, so now with APL2 outer product can be used any time you need any sort of cartesian product. Doesn’t have to be a scalar function, it can be any function, and this says make a 2-item list, take one from the left and one from the right. Now the way you do it without DD is you enclose each of the left and you enclose each of the right and you do jot-dot-comma. Why do you need to enclose it in this case? Because you get a length error trying to catenate things of wildly different shapes. If you have, say, character strings and you want to glue them together in every combination, just simple jot-dot-comma will work. So that’s a pretty easy way.

And if it will make it a little bit freer, I’ll show you that you get a 2 by 4 array, which you can deduce from the original outer-product shape rules: the shape of the result of an outer product is the shape of the left catenated to the shape of the right. I also find you can do useful work. One of the common phrases in my paper is the first of jot-dot-comma-reduce and one application I use of that is I do an outer-product reduction, I use that to form all the indices of an array using jot-dot-comma-reduce, so this does come up in day-to-day work, I’m not just making pretty slides.

Let me show you another application of DD which I do use all over the place to such an extent that I’d like to have some built-in facilities that will do this without my having to carry around DD. I’m not sure how that would work, but I’d also like to do without the quotes, I’m not sure how that would work but there are proposals. In teaching APL Ken (Iverson) suggests doing outer products to see tables.

```apl
      ¯1 0 1 2 ∘.* 0 1 2 3
1 ¯1 1 ¯1
1  0 0  0
1  1 1  1
1  2 4  8
```

Maybe somebody else asks where do those answers come from. You’d like to trace star. So you’d like to have a variant of star, which shows what’s going on as you do it. So I can use the simple recognition method and I say quote-quad DD. Well quote-quad is a sort of funny input – open the keyboard and let me type; and I say all right do the operation and put the answer there, show an assignment, put the left there and the right there and you get this beautiful traced display

```apl
      ¯1 0 1 2 ∘.(⍞ DD) 0 1 2 3
(⍺*⍵)'←'⍺'*'⍵
1 ← ¯1 * 0   ¯1 ← ¯1 * 1   1 ← ¯1 * 2   ¯1 ← ¯1 * 3
1 ←  0 * 0    0 ←  0 * 1   0 ←  0 * 2    0 ←  0 * 3
1 ←  1 * 0    1 ←  1 * 1   1 ←  1 * 2    1 ←  1 * 3
1 ←  2 * 0    2 ←  2 * 1   4 ←  2 * 2    8 ←  2 * 3
```

Never do my fingers leave my hands. Oh, now I know where they come from

Looking clockwards again – how much time – less than 10 minutes – ah, I see – I thought you were going to say less than 10 nanoseconds. I think two more topics. One of the key things I have to do, If I write a program that’s going to be inserted into the interpreter, as a new function, maybe experimentally (we call it PDF – pre-defined function or primitive defined functions) I have to be as severe as a primitive function and fully check the arguments.

```apl
0=⍴X                  ⍝ Empty
1≥≡X                  ⍝ Simple
X≡⌊X                  ⍝ Integer
X≡⍕X                  ⍝ Simple Character
0∧.=∊↑0⍴⊂X            ⍝ Numeric
' '∧.=∊↑0⍴⊂X          ⍝ Character
1=↑⎕EC'⍴⍴X⌈X'         ⍝ Non-Complex
```

So I have a set of idioms for domain checking and of course common ones like this everyone knows (empty), Simple – is the array a simple array? This is integer, assuming that you already know your array is numeric, the floor of all integers is the same array. Here’s a simple character one. Then they get massive. X there is an array of any depth rank shape or whatever entirely numeric. Now I found that I could write this over and over again without flaws but it does get a little tricky. Also all character; here’s the most tricky one of all – non-complex – meaning X is numeric of any depth rank and shape, but I don’t want any complex numbers sneaking in there. What I do is use ⎕EC, and rank is simply to say look I don’t want WS FULL on my ⎕EC, so rank gives you that single number or maybe it won’t work but, maximum is not defined on complex numbers, because which is bigger:
2J93 or negative-15J22? Well, we could have said you take the magnitude from the origin and return the larger one, instead we said we don’t know what that means. And so that blows up the maximum, but this is bad because if somebody comes along and says this means this, then this won’t work. So that’s the quick way to find out non-complex.

I don’t like doing this, because now I know what to say; I’d rather say the word EMPTY or the word SIMPLE and so forth. I don’t like to do these phrases because I can make a mistype, I can leave out this enclose, and now it works sometimes, I’d rather just say this. So, how do you do this? You can just say it. The nice thing about programming languages is that if you don’t like a facility that’s there you can abstract it by making a program. This is what I call a ‘good’ program (I say good in quotes because if you’re not making a program that you want to be just like a primitive and reject all its arguments you don’t have to be so extreme)

```
  Header
⍝ Abstract
⍝ Prolog
  Argument checks     ⍝ Comments
                      ⍝
  Body                ⍝
                      ⍝
```

You have an abstract, a one-line abstract; a prologue saying don’t do this with it or that, or maybe an example; then you do argument checks, than you have code that actually does it. So let me give you an example of why you might want to do this I’ve purposely chosen a stupid function to do. Now COUNT means in origin 1 iota-N; it’s so simple even in origin zero you don’t want a subfunction. I’m showing this to emphasize that argument checking helps. So I test it like a good programmer – COUNT 3 and I test it again, how about something bad and you get an answer

```apl
[0]  Z←COUNT N
[1]  ⍝ First N counting numbers
[2]  Z←+\N⍴1

      COUNT 3
1 2 3
      COUNT 2 3
1 2 3
1 2 3
```

Now that may not be desirable; we want to say LENGTH ERROR, or DOMAIN ERROR or some such message. So how do I do it? OK I’m a thorough person, I’ll go through and put the checks in.

```apl
[0]  Z←COUNT N
[1]  ⍝ First N counting numbers
[2]  ⎕ES(~1=×/⍴N)/5 3
[3]  ⎕ES(~1≥≡N)/5 4
[4]  ⎕ES(~0=↑0⍴N)/5 4
[5]  ⎕ES(~1≡⌊N)/5 4
[6]  ⎕ES(~N≥0)/5 4
[7]  Z←+\N⍴1

      COUNT 3
1 2 3
      COUNT 2 3
LENGTH ERROR
      COUNT 2 3
      ∧
```

Do you have any uneasy feeling at all about this function? (laughter) Yeah, even if you don’t care about it very much, I look at this and say Where’s the code that actually does it? There’s several nice things that I can say about this, the error-checking part of it is in the beginning all with ⎕ESs, so I could work out a workspace with all the checks in and then run a processing function that takes them out once the thing works. So we have in APL a strongly-typed language if we want a strongly-typed language. And you also notice that these phrases aren’t horrible error-trapping phrases, but you could make a mistake, you could do this and put 1 less-than depth and get wrong; I do try to do this as NOT, this means that if it is NOT a single then blow up with a length error. If it’s NOT simple blow up and so forth. As for efficiency, I don’t care, NOT is very very fast, especially NOT on 1-bit scalars. In fact, I was showing off APL PC 2.0, with a 30,000-element bit vector . . . how many more minutes – I won’t tell that story.

So this works just like the primitive would work with different argument. How can we do a little better? Well, look, I can actually apply IOTA, I can apply a related function that has the same domain, and if it blows up for any reason I can use the error we’re going to code. So the style is this, now it’s an admittedly bad example because COUNT is trivial, it’s using IOTA to check essentially IOTA, but I’ve used this in good cases. I proposed a new function whose argument treatment and forms is just like compression arguments and forms. So how do I test that they’re OK? I try compression on the arguments, if they blow up I say No good. They’re easy to do, actually they’re quite fast, there it is. I could make one more step, of course this was not my point, but I can do it with IOTA, and I want it to accept any single matrix or scalar or vector, so I can do it like that, and now at this point we spit back the errors, even the one – resource failure, we spit back just like a primitive that fails to work.

```apl
[0]  Z←COUNT N
[1]  ⍝ First N counting numbers
[2]  '⎕ES ⎕ET' ⎕EA '→0⍴⍳,N'
[3]  Z←+\(,N)⍴1
```

Now there is a better way, and a fast better way.

```apl
[0]  Z←COUNT N;⎕IO
[1]  ⍝ First N counting numbers
[2]  ⎕IO←1
[3]  '⎕ES ⎕ET' ⎕EA 'Z←⍳,N'

      COUNT 3
1 2 3
      COUNT 1 1 1⍴4
1 2 3 4
      COUNT 'OF MONTE CRISTO'
LENGTH ERROR
      COUNT 'OF MONTE CRISTO'
      ∧
      COUNT 2*35
WS FULL
      COUNT 2*35
      ∧
```

Finally the function COUNT is perfect

> 1. Correct output given proper input.
> 2. Rejects all improper input.
> 3. Reports resource failures.
> 4. Easy to understand. \*
> 5. Efficient. \*\*
>
> (\* Some may argue about this)  
> (\*\* Usually overemphasized)

I’ve made the two last points ‘Easy to understand’ that’s heavily subjective, I tried to make it easy to understand. Efficient? – well, probably overemphasized. Many times I find my watch doesn’t go down to nanoseconds so I’m not sure if it’s inefficient or not. There is another way to do it. I could write helper functions – I’ll show you the helper functions later. Now you do this, and you say What the heck is this PL/1 doing in my APL code.

```apl
[0]  Z←COUNT N
[1]  ⍝ First N counting numbers
[2]  DECLARE NONEG INTEGER SINGLE SIMPLE N
[3]  Z←+\(,N)⍴1

      COUNT 3
1 2 3

      COUNT 2 3
DOMAIN ERROR
COUNT[2]  DECLARE NONEG INTEGER SINGLE SIMPLE N
                        ∧       ∧

      COUNT ¯2
DOMAIN ERROR
COUNT[2]  DECLARE NONEG INTEGER SINGLE SIMPLE N
          ∧       ∧

      COUNT 1 (2 3)
DOMAIN ERROR
COUNT[2]  DECLARE NONEG INTEGER SINGLE SIMPLE N
                                ∧      ∧
```

except for the last name which is the argument name all of these are monadic functions; except for the DECLARE function, all the rest take their argument and immediately return it, but before they do that they check to make sure that it’s satisfied. If it’s not satisfied they report an error and what happens here is that this is not a single number so you notice that the right-hand caret points to the word that is offended by that argument. Now if everything is clear the N tumbles through from function to function, of course DECLARE is a monadic function that says Oh, we got there, it does nothing. So you can write a very wordlike form.

The other nice thing is that if I put the word NONCOMPLEX in and later on we change maximum so that it works with complex, then I can change NONCOMPLEX without changing this. The other nice thing is that I get everything debugged here, and I don’t want to carry around these helper functions with me, then I just go through and put a lamp here and replace that DECLARE and now there’s a nice comment in ENGLISH. I also thought this would be wonderful for the compiler people, because if you wrote your programs like this they could specifically recognize a line starting with DECLARE and now they know what the arguments are, which is one of the hard things to do for a compiler.

Let me sum up. Finally one more step in this. You notice that we showed the inside of the code. Finally after we’re sure that everything works we want to say like Peter suggested, Don’t show me that, report it like a primitive, We can finally do this with ⎕FX ⎕CR

```apl
      0 1 0 0 ⎕FX ⎕CR 'COUNT'
COUNT

      COUNT 3
1 2 3

      COUNT 2 3
LENGTH ERROR
      COUNT 2 3
      ∧

      COUNT '?'
DOMAIN ERROR
      COUNT '?'
      ∧
```

Now we’ll put up at the end after I’m done the functions that do that. I think that’s far more readable and I am an APL bigot and I prefer to say it that way than say it another way. You don’t have to make any extensions to the language, so I’ll give you these functions, they’re one-liners after the comment.

Let me leave you with a quick whizbang if I may. This is one that we noticed I think, well Roy Sykes gets the credit for this perhaps. This says Is A and B the same to 4 significant digits?

```apl
¯4 ≡ (⍕¨) A B
```

and it works like this: I can rewrite it like that

```apl
≡/¯4 ⍕¨ A B
```

which says this

```apl
≡/(¯4⍕A)(¯4⍕B)
```

and now you can see, this

```apl
⊂(¯4⍕A)≡(¯4⍕B)
```

and match always gives back a simple scalar so you don’t need the enclose

```apl
(¯4⍕A)≡(¯4⍕B)
```

and obviously this matches the arrays: are they all to 4 digits? But if I don’t want to check that, I want to say How many digits do they match to? and so now what I need is to say “for D, I want to know D.”

```apl
(-D)≡.(⍕¨) A B
```

I could do this

```apl
(-1)≡.(⍕¨) A B
```

I could do this

```apl
(-2)≡.(⍕¨) A B
```

I could do this

```apl
(-3)≡.(⍕¨) A B
```

until they finally match, but I have a list of numbers of digits, like 1, 2, 3 and so forth, so I can do it with a whizbang, I don’t call it an idiom it’s not common enough, I use the All Right, and match-dot-format-each is the function that I do All Right with and now what do I do? To find out how many digits? Just sum them up

```apl
      (-+\18⍴1)≡.(⍕¨)¨⊂A B
1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0

      +/(-+\18⍴1)≡.(⍕¨)¨⊂A B
5
```

so let me leave you with something that . . . sometimes it hurts me when I try to think . . . but here is an APL2 whizbang.

```apl
+/∧\(-+\99⍴1)≡.(⍕¨)¨⊂A B
```

I figure 99 digits: all systems would poop out before 99 digits. So now, the and-scan there is to say take the format and if you get a one after you get the first zero then don’t consider that. I showed this at New York City SIGAPL meeting and somebody said “Oh my goodness”, I felt that person was representing the computer this was run on. (laughter) I will . . . to you, this does turn on the error-conditioning. But you have to realize this, I don’t mind how much CPU time is used up, because if you don’t use the CPU time now, it’s gone for ever. (Laughter)

O.K. (Applause)
