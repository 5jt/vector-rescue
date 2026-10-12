---
title: J Locales
authors:
- Richard Oates
volume: '12'
issue: '2'
page: '141'
unindexed: true
transcribed: 'from page images of VOL.12-NO.2-OCTOBER-1995.pdf, pages 143–144 (printed 141–142); Claude, 2026-10-12'
review: draft
tags:
- language design
- programming techniques
queries:
- "Signed at the end “Richard H. Oates” with his postal address, which is omitted under the project rule for individuals’ contact details."
- "The code is J of 1995 (J 2.x): the explicit definitions use `1 : 0` and `x.`, and scripts are run with `0!:0`; the two displayed results are boxed output, given here as printed."
- "Kept as printed: “more worst case than typical”; “In the figure but not for real”."
---

*by Richard Oates*
{ .byline }

Explicit Definition isolates names with the Local Copula (`=.`). Locales isolate names with spelling, possibly expressed, usually implied. My trip may have been more worst case than typical. I wrote three verbs.

The name `table_bob_`, say, is `table` in locale `bob`, while `table_z_` is `table` in locale `z`. The names `table_bob_` and `table_z_` are *locatives*. One locale, the *base*, has no name. One locale, `z`, is special: its names are known in all locales unless overridden. Locales are usually populated by script. The application is scripted to the base. Secondary verbs script to named locales. If a file called `add` is:

```j
table=. 1 : 0
by=. ' '&;@,.@[ ,. ]
over=. ({. ; }.)@":@,
tbl=. 1 : '[by] over x./'
 x. tbl
)
```

... then `0!:0<'\add'` scripts the adverb to the base. This scripts the adverb to locale `z`:

```j
sc_z_=. 0!:0
sc_z_ <'\add'
```

I script most of my secondaries without change to locale `z`. If the first sentence of `table` is removed, and the last two as well, `by`, `over` and `tbl` become global. That is how I script my verb tracking program, and also the DOS editor I described in Vector 11.3. The former is scripted to locale `t` and the latter to locale `e`, in each case to keep names isolated by locale after Explicit (`:`) is removed.

I happened to have `cut` defined one way in the base and another way in locale `z`. Locales are populated by definition as well as script. In the next figure `5!:5@<` represents the tracking program in locale `t`. In the figure but not for real, `5!:5@<` is also defined in locale `z`. The verbs `trk` and `zing` are distinct. The first box surprised me. I expected `trk'cut'` to be `<;.1`. Then I realized locale `t` knows nothing about the base, just as the base knows nothing about `t`. After `trk_t_` is plugged into `z` it can be called `trk` but it still runs in `t`. On the other hand `zing_z_` runs in locale `z` and `zing` runs in the base.

```j
cut=. <;.1
cut_z_=. <;.2
zing_z_=. trk_t_=. 5!:5@<
trk_z_=. trk_t_       NB. plug into z
d=. 1 : '(x.''cut'');(x.''cut__'');(x.''cut_z_'')'
(trk d),(zing_z_ d),:(zing d)
┌────┬────┬────┐
│<;.2│<;.1│<;.2│
├────┼────┼────┤
│<;.2│<;.1│<;.2│
├────┼────┼────┤
│<;.1│<;.1│<;.2│
└────┴────┴────┘
```

After I saw this I added a verb to `trk` that makes a locative for any name that is not full (`cut__` from `cut`).

My DOS editor in locale `e` scripts its result to the locale determined by the extension of the file name. I substituted `locale` for `0!:0` in the definition and added two verbs. For a calendar program in locale `c`, say, the first verb makes `'sc_c_'` from `'\j\s\cal.c'`, and the second verb is almost:

```j
lo=. ('locale=. '"_ ":@, ]) ; (] ":@, '=: 0!:0'"_)
lo'sc_c_'
┌──────────────┬────────────┐
│locale=. sc_c_│sc_c_=: 0!:0│
└──────────────┴────────────┘
```

For each Format (`":`) `lo` really has Do (`".`). Do is like Execute in APL. I get a nonce error if `sc_c_` is not global (`=:`).

I made no change to applications. I wrote three verbs that construct locatives for two secondaries not in `z`. All other locatives appear in a profile script. In an application session I never key a locative or see one. Names have grown up in J. Like the best people, they have lost their innocence but kept their simplicity. Locales are a major improvement.

Richard H. Oates<br>
[address omitted]
