---
title: 'MetaAPL: an APL Preprocessor'
authors:
- Glen Tickner
- Norval R Oswald
volume: '4'
issue: '2'
page: '72'
unindexed: true
transcribed: 'from page images of VOL.4-NO.2-OCTOBER-1987.pdf, pages 74–84 (printed 72–82); Claude, 2026-10-06'
review: draft
queries:
- "Not in the index. An 11-page article in the General Articles section, typewritten (camera-ready from the authors); apparently a conference paper (“at or shortly after the time of this conference”)."
- "The heading is printed “MetaAPL”; the text writes “META\\APL” throughout; transcribed as printed."
- "Figure 1: in the source column the separator printed as a small cap-like glyph is read as ⍝ (lamp), and the block brackets as ⊂ … ⊃. In the QUIT object code the glyph after (condition) is read as ↓. Transcribed as two columns in one block, as printed."
- "Figures 2 and 3: the comment-region markers print as “⍝TT⊥⊥”; read as ⍝⊤⊤⊥⊥ (a box-drawing convention). Figure 3 skips line [13] as printed."
- "Section “2. A Pre-Compiler” is printed “A·Pre-Compiler” (a stray mark); transcribed without it."
- "Slips transcribed as printed: “The development of APL compilers are likely”, “APL’s unique character make it”."
---

by Glen Tickner and Norval R Oswald
{ .byline }

Studies conducted by IBM in the 1960’s showed that APL, when compared with traditional languages, reduced the time required by programmers to develop systems. However, the use of APL has for the large part been restricted to small applications and applications for which the development time is necessarily short. In particular, APL has remained a language poorly suited to large applications which must be maintained over an appreciable length of time.

## The Performance Problem

The major factor prohibiting the use of APL in the development of large systems is its inefficiency when compared with compiled languages. For smaller applications performance was not a pressing problem, since the APL interpreter can efficiently handle most operations where repetitive execution is not required [3].

The APL world has made a serious commitment toward solving the problem of efficiency; first, with the addition of efficient substring search and table lookup functions, either built into the language or provided as add-on functional interfaces to external programs. An example of the former would be STSC APL’s substring search function, quad SS, while the search functions available through INTERPROCESS’s CALL/AP or AFM systems provide examples of the latter. Secondly, with the advent of APL2, a new family of efficient (albeit external) subroutines has become possible, leading to a variety of new offerings from APL vendors.

The third area of progress in improving the efficiency of APL may prove the most significant. Thanks to STSC, an APL Compiler has at last become practical and commercially available. At least two additional (or more properly, “translators”) have recently been developed.[2,3] These events may at last remove efficiency as a barrier to the use of APL in large applications.

## Maintainability as a Barrier to the Use of APL

Before it can achieve acceptance as a development tool for large systems APL must improve its reputation for maintainability. Most of those familiar with APL have heard the story of the APL programmer whose code must be discarded when he leaves the company. With maintenance costs typically running at 50% of costs over the software development life cycle,[1] APL will not broaden its acceptance as a language for developing large applications if what it gives in programmer productivity is later taken back in maintenance costs.

Part of the reason APL code is difficult to modify and errors are difficult to diagnose lies in the powerful and condensed primitives. The primitives, alone or in combination, can form constructs whose meaning is extremely difficult to decipher. Because this problem is so intrinsic to the structure of the language, it may not have a solution other than the development of staff fluent in the use and interpretation of APL primitives.

Other factors affecting APL’s maintainability are more tractable. These factors can be classified under one of two headings:

1. features of the language which make APL less transparent
2. the absence of structured conditions

“Transparency” refers to the absence of hidden effects and the ease with which accurate function or program cross-reference information can be generated. Some of the opaque features of APL:

1. The APL convention (entirely backwards from our point of view) that variables are assumed to be global unless they are explicitly designated as local in the function header. The typical consequence of the latter, unless the programmer is vigilant, are unintended globals, or “leaky” variables. Leaky variables may lead to side-effects and excessive space utilization. These pathologies are most likely in large systems developed by more than one programmer, where they are most difficult to correct.
2. The capability of making multiple assignments on one line, encouraging “statement-gluing”, long lines of virtually unreadable APL code. The most severe offenders in this area may be the experienced programmers who have developed the most familiarity with APL primitives.
3. APL contains primitives for the conversion of character strings into variables, variables into functions, and vice versa. These hidden assignments make cross-referencing a difficult accomplishment for both the programmer and automated tools.

All of the above three problems can be overcome with proper programmer vigilance. For example, the programmer can adopt the convention of making explicit references to all global objects in the comments section at the top of each function. However, the programmer *need* not do so, and this fact has particular importance when multiple programmers contribute to the same application.

## Formal Structures

Similarly, it is quite possible to write structured code in APL (or with any language that depends upon branching to resolve conditions). In practice, APL conditions rarely correspond to Dijkstra’s eight allowable structures (for several examples, see Martin [7]).

The language’s lack of structure has long been a source of embarrassment to supporters who feel that APL’s unique character make it superior to more traditional languages. In the early 1970’s, following Dijkstra’s criticisms of APL, several attempts were made to add control structures to the language. Three separate approaches have been taken:

### 1. The Functional Approach

The simplest approach has been to define APL control functions such as “IF” and “DOWHILE” (see Lim and Lewis [6] and Mason [8]). This solution is also the least satisfactory, for two reasons. First, the procedure is inefficient, since it adds unnecessary function calls. Secondly, nothing would prevent or discourage a programmer from using a raw branch, since the GOTO remains an integral part of his programming environment.

### 2. A Pre-Compiler

A significant improvement over the functional approach is to provide a structured control language which can be later compiled into APL code. The best-known example of an APL pre-compiler is APLGOL, written to take advantage of both APL’s powerful operators and ALGOL’s control structure.[5]

Pre-compiled APL code carries no penalty in terms of either performance or space, since the functions which establish the control structures normally would not reside in the workspace at run-time. Furthermore, the source code can be indented to highlight the structure of code blocks. With some imagination, checks can be added to the compiler to bring to APL some of the code verification attributes of languages such as PASCAL.

Mandatory features of any APL pre-compiler would be utilities for the printing of source code and the recompilation of object code. These features would help ameliorate the problem that the interpreted functions would not be the same as the functions as they were originally developed.[4]

### 3. Integration with the Interpreter

There has been one documented case of integration of high-level control structures into an APL interpreter.[4] The modifications took little programming effort, code written with control structures such as *IF* and *DO WHILE* could run in conjunction with code using the raw APL branch, and the implementation actually improved performance.

Clearly, the best option from a technical viewpoint is integration with an APL interpreter. However, for reasons of portability and compatibility with other APLs and releases of APL, an interpreter with improved control structures is not likely to become available, except through one of the major vendors. And, as the last fifteen years have demonstrated, the major vendors are unlikely to risk such fundamental modifications to the language syntax. The best alternative at this time would appear to be some form of pre-processor.

The advantages of structured languages have been well documented. Structured code is easier to read and therefore easier to maintain and modify. Because structured code has fewer possible paths it is less likely to contain undetected errors.

Why have more formal control structures not become an accepted part of APL? In part, because the APL operators are so well structured. Conditional logic has always been recognized by APL programmers as something to be avoided, particularly as it often exacts a heavy cost in machine resources.

The development of APL compilers are likely to change the APL world’s resistance to structured controls. As larger APL systems become feasible the requirement for conditional execution will become of increasing significance. At the same time, the advent of compilers may change APL programming style, since they remove the penalty associated with APL branching.

## META\APL

Code maintainability and reliability are both central concerns of ACT Computer Services of Edmonton, Alberta. ACT began using VS/APL in 1983 and now has an APL programming team of from 5 to 8 programmers. The company’s APL programming group develops and maintains several large database and management information systems.

ACT’s APL programming is responsible for the following databases and supporting software:

1. Two time series databases:
    1. CANSIM, the Government of Canada’s public database. ACT’s CANSIM holdings include approximately 63 megabytes of data.
    2. ASIST, the Government of Alberta’s public database. 42 megabytes.
    { type="a" }
2. Two “multi-dimensional” databases stored in ALASS (A Large Array Storage System), which uses keyed and component files to simulate multi-dimensional APL arrays:
    1. MDASIST, the Government of Alberta’s public database for multi-dimensional data. 64 megabytes.
    2. EXPORTS, the Government of Alberta’s holdings of exports data for Canada and Alberta, 34 megabytes.
    { type="a" }
3. One relational database system storing records of doctor and hospital visits, practitioner and patient addresses, and billing and diagnostic code descriptions (approximately 200 megabytes).

The APL software which provides the user interface to these databases includes between 60 and 70,000 lines of decommented code.

ACT decided on the need for tools to improve the quality and maintainability of its systems written in APL. To this purpose, ACT developed META\APL, a pre-processor with the following features:

1. A structured programming language.
2. A decompiler.
3. Automatic documentation during compilation. Documentation includes the programmer name, time of the compile, a box region listing global references, and a classification of the META\APL type.
4. Function diagnostics.

The current version of META\APL is written in APL and occupies about 40K of memory.

META\APL is invoked as a function editor, so that the programmer would enter the command

```apl
MEDIT 'fnname'
```

where *'fnname'* is the name of the function to be edited. The syntax is the same whether *'fnname'* is a new function or an existing function that is being decompiled.

If an existing function is to be edited, META\APL creates a canonical representation and enters edit mode using the available editor (in this case, the full-screen VS/APL XEDITOR). META\APL converts the functional representation into a character variable in order to permit indentation of code blocks. META\APL indents the blocks automatically when a function is decompiled.

The version of META\APL currently in use at ACT is an elementary prototype. Despite its simplicity and some rather strict limitations imposed by the current version, all APL programmers have been required for the last two years to do all their development work in META\APL.

## META\APL Structured Conditions

META\APL’s syntax consists of two blocked conditions and two line conditions, as shown in figure 1 below.

```text
META\APL
SOURCE CODE                          OBJECT CODE

⊂WHEN ⍝ condition1                   ∆WB:
   function1                         →(condition1)⍴∆WE
   function2                         function1
 WHEN ⍝ condition2                   function2
   function3 ⊃                       →(condition2)⍴∆WE
                                     function3
                                     →∆WB
                                     ∆WE:

 CASES                               → caseselect
  ⊂CASES ⍝  caseselect               →∆C
     case1:                          case1:
       statement1                    statement1
     case2:                          →∆C
       statement2                    case2:
     case3:                          statement2
       statement3 ⊃                  →∆C
                                     case3:
                                     statement3
                                     ∆C:

IF ⍝ condition ⍝ s1 ⍝ s2              →(condition)⌽∆2,∆1
                                     ∆1:s1
                                      →∆3
                                     ∆2:s2
                                     ∆3:

QUIT ⍝ condition ⍝ endroutine         →(condition)↓∆Q1
 statement1                           endroutine
 statement2                           →∆Q
                                     ∆Q1:
                                      statement1
                                      statement2
                                     ∆Q:
```

*Figure 1. Source and Object Code for META\APL Conditions*
{ .caption }

The following example shows how global, local, and semi-global objects would be entered into a new META\APL function:

```apl
      ∇ RESULT←FUNCTION ARG;SEMI1;SEMI2::GLOBAL1;GLOBAL2
   [1]  ⍝⊤⊤⊥⊥
   [2]  ⍝ Unformatted comment region.
   [3]  ⍝⊤⊤⊥⊥
   [4]   LOCAL1←FN1 ARG[1]
   [5]   LOCAL2←FN2 ARG[2]
   [6]   GLOBAL1←FN3 SEMI1
   [7]   GLOBAL2←FN4 SEMI2
   [8]   RESULT←GLOBAL1 FN5 GLOBAL2
      ∇
```

*Figure 2. Newly-entered META\APL source code.*
{ .caption }

The semi-global variables, *semi1* and *semi2*, are assigned as globals in the subfunctions *fn1*, *fn2*, or *fn3*. Local variables (*local1* and *local2*) will be localized in the function header. The compiled function will appear as shown below:

```apl
     ∇ RESULT←FUNCTION ARG;LOCAL1;LOCAL2;SEMI1;SEMI2
[1]    ⍝M←APL[1]SEMI1;SEMI2::GLOBAL1;GLOBAL2
[2]    ⍝1987 3 16 0 49 24
[3]    ⍝⊤⊤⊥⊥ ( Name ) 87/MAR/16(MON)  0:49 AM ------------------------
[4]    ⍝-------------------------------------------------------------
[5]    ⍝ Automatic Copyright Region
[6]    ⍝-------------------------------------------------------------
[7]    ⍝
[8]    ⍝ Formatted comment region (words are left and right justified).
[9]    ⍝
[10]   ⍝⊤⊤⊥⊥---------------------------------------------------------
[11]   ⍝   FN1        FN3        FN5        GLOBAL2
[12]   ⍝   FN2        FN4        GLOBAL1
[14]   ⍝⊤⊤⊥⊥---------------------------------------------------------
[15]    LOCAL1←FN1 ARG[1]
[16]    LOCAL2←FN2 ARG[2]
[17]    GLOBAL1←FN3 SEMI1
[18]    GLOBAL2←FN4 SEMI2
[19]    RESULT←GLOBAL1 FN5 GLOBAL2
     ∇
```

*Figure 3. Compiled META\APL function, showing comment region.*
{ .caption }

Note the automatic generation of date and programmer identifier information (programmer identification is stored in a global variable, as is the copyright notice).

Since local objects are automatically entered into the function header the programmer does not need to waste time entering insignificant local objects, such as loop counters, into the function header. However, META\APL requires the programmer to be vigilant in keeping track of global objects by forcing him to list them in the function header. This is as it should be, since it is far more important that the programmer remain conscious of global function outputs. Note the globals list automatically generated below the copyright region.

## Function Diagnostics

An APL pre-compiler provides an excellent vehicle for the integration of function diagnostics. META\APL performs the following checks during compilation:

1. META\APL syntax check

    The pre-compiler verifies that the source program has been written in correct META\APL syntax (closed blocks, no branches, etc.).

2. APL syntax check

    Checks against unbalanced brackets, parentheses, or quotes or non-unique function headers.

3. Multiple assignment check

    To ensure that META\APL code is fully restartable and to eliminate “statement-gluing”, a check is run against multiple assignments. This check can be bypassed so as to permit such necessary constructs as

    ```apl
    'var←fn cond2' ⎕EA 'var←fn cond1'
    ```

Several additional diagnostics can be performed after compilation:

1. *prefix* LEAKYNAMES *nl*

    Prints out the names of all global objects called by functions in the name list, *nl*, not prefixed with the characters provided in *prefix*.

    For LEAKYNAMES to be effective, consistent naming conventions must be adopted for all global objects (a good idea in any case) so that the function will not output long lists of objects intended to be global.

2. *prefix* UNUSEDNAMES *nl*

    Prints out all objects called by functions in the name list, *nl*, that have been localized or input as arguments but never used.

    *prefix* can be used to exclude semi-globals from the unused name search.

3. *prefix* UNASSIGNEDLOCALS *nl*

    Prints out all objects called by functions in the name list, *nl*, that have been localized but never assigned. Like LEAKYNAMES, this function can be used to trap typographical errors in the naming of variables.

## META\APL Enhancements

In response to requests from the APL programming group at ACT Computer Services, META\APL is currently undergoing modification. The new version will be written in C to allow for the addition of new features without a penalty in performance. The new version is being developed for a variety of micro and mainframe APLs. A version for STSC APL\*Plus running on a Macintosh personal computer will be available at or shortly after the time of this conference.

The following enhancements will be incorporated into the new release:

1. The restriction of one condition block per function will be removed. Block structures can be nested or entered sequentially.
2. IF and QUIT forms will be expanded to a block structure so that multiple-line DO blocks are permissible.
3. Global and semi-global variable lists will be entered in a block region. The declaration block will have the same format as condition blocks.
4. META\APL error messages will be improved to give better information regarding errors in the source code.

The current version of META\APL is available on a beta-test basis from ACT Computer Services of Edmonton, Alberta.

## References

1. Boehm, “The High Cost of Software”, *Practical Strategies for Developing Large Software Systems.* Addison-Wesley, 1975.
2. Ching, Wai-Mee, “Program analysis and code generation in an APL/370 compiler”, *IBM Journal of Research and Development.* November 1986: Vol. 30, no. 6, p. 594.
3. Driscoll, Graham C. Jr. and Donald L. Orth, “Compiling APL: The Yorktown APL Translator”, *IBM Journal of Research and Development.* November 1986: Vol. 30, no. 6, pp 583-593.
4. Harris, Larry R., “A Logical Control Structure for APL”, *APL Congress 73,* P. Gjerlov, H.J. Helms and Johs Nielsen, eds. North-Holland, 1973.
5. Kelley, R.A., “APLGOL, an Experimental Structured Programming Language”, *IBM Journal of Research and Development.* January 1973: Vol. 17, no. 1, p. 69.
6. Lim, A.L. and G.R. Lewis, “Toward Structured Programs in APL”, *The Computer Journal.* August 1974: Vol. 18, no. 2, p. 140.
7. Martin, B.R. “Concepts of Structure in APL”, *APL80; International Conference on APL,* Gijsbert Van Der Linden, ed. North-Holland, 1980.
8. Mason, J.A., “Some User-Defined Control Functions for More Readable APL Programs”, *ACM SIGPLAN Notices.* 1975: Vol. 10, no. 8, p. 11.
