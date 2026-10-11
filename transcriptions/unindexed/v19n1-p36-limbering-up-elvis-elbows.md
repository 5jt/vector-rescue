---
title: 'Limbering Up: Elvis Elbows'
authors:
- Gary A. Bergquist
volume: '19'
issue: '1'
page: '36'
unindexed: true
transcribed: 'from page images of VOL.19-NO.1-JULY-2002.pdf, pages 38–39 (printed 36–37; follows art10014370); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
- data and files
queries:
- "Within the Zark Newsletter Extracts, introduced by Jon Sandles. The column is unsigned; it is attributed to Gary Bergquist as the index attributes the Utility Corner columns of the series. It sets the Soundex task. The reprint note at the foot of p.37, which closes the extract, is included here."
- "The Soundex codes in the test table were worked by hand from the printed rules as a check on the transcription; all five agree."
- "The e-mail address printed with Vector Production’s postal address is the organisation’s, and is kept. Kept as printed: “DD and T are the same”."
---

(The purpose of this column is to work some flab off your APL midsection. Like muscles, your APL skills can atrophy if not exercised with adequate frequency and variety. This column presents a task for you to perform. Set aside a few minutes from your busy schedule and work the task. Mail in your solution and stay tuned for the results.)

Suppose you have a database of 9000 names, and you need to locate "Schneider, K." Or is it "Schnyder, K."? Or maybe "Snyder, K."? Heck, you’re not sure exactly what the name is. But you do know approximately what it sounds like. What do you do?

Perhaps the U.S. government can come to the rescue. During the make-work mindset of the 1930s, as part of the massive WPA (Works Progress Administration) program, the government decided to put people to work re-indexing past censuses. In particular, they set out to re-index the U.S. federal Censuses of 1880, 1900, and 1910 by the way names *sounded*, rather than the way they were spelled.

In this way, if names were mis-spelled slightly by the census takers, a name could still be located if you knew approximately how to pronounce the name. It turns out that this phonetic indexing has been invaluable to folks doing genealogical searches.

But how did they do it? The scheme devised by the government was to treat all letters sounding approximately the same as if they are the same. For example, DD and T are the same; B and P are the same; M and N are the same; and so on. The term "Soundex" was coined to refer to this scheme. (The term "Miracode" is sometimes used too.)

Your task is to implement Soundex. In particular, write either or both of the functions `SOUNDEXV` and `SOUNDEXM`. The first takes a single character vector name as its argument and returns the Soundex code for the name. The second takes a character matrix of names, one per row, as its argument and returns a vector of Soundex codes, one per name. The functions should be as *fast* as possible.

Here are the rules for converting a name to its Soundex code:

1. Delete all blanks and nonletters from the name (Van Owen → VanOwen).
2. Convert lowercase to uppercase (VanOwen → VANOWEN).
3. Set aside the first letter (V).
4. Translate all letters, including the first, to digits between 0 and 6 via:

    ```apl
    0: A,E,H,I,O,U,W,Y
    1: B,F,P,V
    2: C,G,J,K,Q,S,X,Z
    3: D,T
    4: L
    5: M,N
    6: R
    ```

    ```apl
    VANOWEN → 1 0 5 0 0 0 5
    ```

5. Eliminate contiguous duplicates (`1 0 5 0 0 0 5 → 1 0 5 0 5`).
6. Eliminate the first letter/digit (`1 0 5 0 5 → 0 5 0 5`).
7. Squeeze out all 0s (`0 5 0 5 → 5 5`).
8. Grab the first three digits, padding with 0s, and stick the first letter, from step 3, on the front (`V550`). To get a convenient, integer result, we’ll deviate from strict Soundex conventions and convert the first letter to a number, its index into the alphabet (`V550 → 22550`).

Test your functions on the following:

| *Name* | *Soundex Code* |
|---|--:|
| `Eberhard` | 5166 |
| `Elvis` | 5412 |
| `Kelly` | 11400 |
| `Schaefer` | 19160 |
| `Van Owen` | 22550 |

Send your solutions to:

> Vector Production<br>
> Brook House, Gilling East, York YO62 4JJ<br>
> UK email apl385@compuserve.com

The notable functions and their authors’ names will be printed in the next issue of *Vector*. Good luck and happy limbering.

---

*Reprinted with kind permission from Zark APL Tutor News, a quarterly publication of Zark Incorporated, 23 Ketchbrook Lane, Ellington, CT06029, USA.*
