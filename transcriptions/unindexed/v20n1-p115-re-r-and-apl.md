---
title: 'RE: R and APL'
authors:
- Mike Day
- Alexander Skomorokhov
volume: '20'
issue: '1'
page: '115'
unindexed: true
transcribed: 'from page images of VOL.20-NO.1-JULY-2003.pdf, pages 117–118 (printed 115–116; the only item under the Correspondence heading, before art10005720); Claude, 2026-10-11'
review: draft
tags:
- system interfaces
- mathematics and statistics
queries:
- "The only item under the Correspondence heading, printed as “RE: R and APL”: an exchange of e-mails between Mike Day and Alexander (“Sasha”) Skomorokhov, ending with Day’s reply. It is followed by “At Play with J: Greed” (art10005720)."
- "The four interface functions are Dyalog APL/W and need R’s COM server; they were not run."
- "Kept as printed: in `rexec` the comment “possibly returns the result” and the example “mlexec 'surf(peaks)'”; in `rput` the comments “create in MatLab” and “put var xu into R with name z” (evidently carried over from a MATLAB interface); “R download … (version 1021)”."
---

*From: Mike Day*
{ .byline }

Did Sasha explain how he’d set up R as (presumably) a server process? I’ve got R, and it has associated folders for Tcl (for example) in its installation tree, but there’s no obvious sign of

> “StatConnectorSrv.StatConnector”

Maybe this is a feature to be paid for in S+ rather than the free R!

*Reply: Alexander Skomorokhov wrote:*

I use:

R-(D)COM Interface (for Windows) contains a COM server used to connect a client application (e.g., Microsoft Excel) with R. An Add-In for Microsoft Excel is provided as well as Active X controls to be included in your applications.

The url is as follows: http://cran.r-project.org/contrib/extra/dcom/

Dyalog 9 ws with 4 small interface functions is attached here (see rapl.zip on the resources page of the Vector website).

```apl
      ⎕vr¨ 'rexec'   'rget'    'rinit'   'rput'

      ∇ a←{r}rexec exp
[1]    ⍝ Execute R expression and possibly returns the result
[2]    ⍝R: R expression ('char')
[3]    ⍝L: if 1, then return the result
[4]    ⍝e: mlexec 'surf(peaks)'
[5]    ⍎(0=⎕NC'r')/'r←0'
[6]    a←⍬
[7]    :If r
[8]      a←#.R.Evaluate(exp)
[9]    :Else
[10]     #.R.EvaluateNoReturn(exp)
[11]   :EndIf
      ∇

      ∇ r←rget name;rho;Re;Im;⎕ML
[1]    ⍝ version for ⎕SE
[2]    ⍝ Get R variable (matrix or vector) to APL
[3]    ⍝R-name of variable to import ('char')
[4]     ⎕ML←3
[5]     r←#.R.GetSymbol(name)
      ∇

      ∇ rinit
[1]    ⍝ version for ⎕SE
[2]    '#.R'⎕WC'OleClient' 'StatConnectorSrv.StatConnector'
[3]    #.R.Init('R')
      ∇

      ∇ {m}rput a;x1
[1]    ⍝ Version for ⎕SE
[2]    ⍝ Put APL array into R
[3]    ⍝R-name of variable to export from APL
[4]    ⍝L-name of variable to create in MatLab
[5]    ⍎(0=⎕NC'm')/'m←''x''' ⍝ Default
[6]    m←,⊂m
[7]    a←,⊂a
[8]    #.R.SetSymbol(m,a) ⍝ put var xu into R with name z
      ∇
```

*Mike Day replies:*

Thanks/spasibo to you both

I had looked at the cran.r-project site after mailing Adrian, and thought it MIGHT be R-(D)COM Interface that was needed; however, the associated web pages didn’t mention StatServer but did seem to suggest that one would need to set up a class for each R command or function or group thereof, so I was inclined to think I must need something else instead.

It’s not bundled into my R download, but as that (version 1021) is a couple of years old, it may be that the later/latest versions do include it.

I’ll download R-(D)COM Interface when I find some time and let you know if I have any problems, for possible addition/amendment to the Vector article.

Mike
