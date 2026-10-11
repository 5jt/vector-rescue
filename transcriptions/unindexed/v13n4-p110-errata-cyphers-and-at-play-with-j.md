---
title: 'Errata: Cyphers and At Play with J'
authors: []
volume: '13'
issue: '4'
page: '110'
unindexed: true
transcribed: 'from page image of VOL.13-NO.4-APRIL-1997.pdf, page 112 (printed 110; after Norman Thomson’s “Errata” on the same page, before art10001920); Claude, 2026-10-11'
review: draft
tags:
- programming techniques
queries:
- "Untitled in print, title ours: unsigned editorial corrections printed below a rule after Norman Thomson’s “Errata” (unindexed/v13n4-p110-errata.md). No author is printed; the entry has no authors."
- "The functions are printed in italic APL type, without ∇ or line numbers; the indentation follows the print approximately. They need `public` and `private` keys and were not run."
- "The J phrase is printed `w =. ~. ^ #/. ~` followed by a full stop, which is taken as the sentence’s own."
---

In Ray Cannon’s article on cyphers (Vector 13.3 page 88) we unfortunately ran the three functions into one paragraph. Here they are again, done correctly:

```apl
   r←enc text;⎕IO
 ⍝Converts <text> string as encyphered numeric vector
  ⎕IO←0
  r←public modpower(,⍉16 16⊤⎕AV⍳text)
```

```apl
   r←dec num;⎕IO
 ⍝Converts numeric vector to deciphered text
  ⎕IO←0
  r←(⎕AV)[16⊥⍉(((⍴num)÷2),2)⍴private modpower num]
```

```apl
   r←k modpower c;s
 ⍝Returns mod|c*k
 ⍝without domain errors if k is large
  s←'mod|',(⍕c),'×'
  r←⍎(((⍴s)×k-1)⍴s),⍕c
```

Line-numbers may be unfashionable, but they do give the production team some clues where things begin and end! Authors are encouraged to use `⎕VR` format where possible.

*Stefano Lanzavecchia* pointed out a crucial missing tilde in Gene McDonnell’s "At Play with J" on page 131 where we should have: `w =. ~. ^ #/. ~`.
