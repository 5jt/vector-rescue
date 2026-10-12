---
title: APL*PLUS II for 80386 PCs
authors:
- Ajay Askoolum
volume: '5'
issue: '4'
page: '61'
unindexed: true
transcribed: 'from page images of VOL.5-NO.4-APRIL-1989.pdf, pages 63–68 (printed 61–66); Claude, 2026-10-12'
review: draft
tags:
- reviews
- implementations
queries:
- "Contents line “APL*Plus II (applications)”; the printed heading is “APL*PLUS II for 80386 PCs”, with the byline “reviewed by Ajay Askoolum (Legal & General Assurance Society Ltd)”. The piece fills printed 61–66, the lower half of 66 blank; “SAX” follows on printed 67."
- "System names (⎕WIN, ⎕TRACE, ⎕HNAMES etc.) are printed in a small sans face; set here as code."
- "Kept as printed: “APL*PLUS PC” (without the slash) in several places beside “APL*PLUS/PC”; “workspace sizes between 1-15MB”; “far too prohibitive”; “The packaging, style and feel of this new product shares”; “Its obvious advantage being”; “between £7,000 to £12,000”; “the few incompatible ⎕POKEs”."
---

*reviewed by Ajay Askoolum (Legal & General Assurance Society Ltd)*
{ .byline }

## The Product

APL\*PLUS II is a second generation APL interpreter for 80386 based PCs (including ATs with an Intel INBOARD/AT), with or without 80387 coprocessor, running DOS 3.3 or later, with RAM size of 2MB or more. The version reviewed is 1.00.07 dated 16th August 1988.

This interpreter, unlike the APL\*PLUS/PC interpreters, is protected. Whilst a single copy of the software may be installed on as many PCs as desirable, only one such installation may be used at any time. The interpreter polls a 'dongle' - between the parallel printer port and cable - at random intervals throughout any active session. It cannot be invoked in the absence of this device and if removed during a session, the user is prompted to re-insert it and press ENTER. If ENTER is pressed without the device in place, the session is terminated with the ensuing loss of the workspace.

The software costs £2,000 plus VAT per copy and the run-time system costs £250 plus VAT per copy. An annual maintenance charge equal to 25% of the original purchase price is payable after the first twelve months. The maintenance charge includes all upgrades and (telephone) support provided by the appointed distributors Cocking & Drury (Software) Ltd. Discounts are negotiable on purchases of multiple copies at the same time.

The same package is available from MicroAPL for £1,395 plus VAT - presumably without any maintenance or upgrades.

An APL character generator ROM will be required if the display adapter in use is not EGA or VGA and will be supplied free of charge on request. This ROM is identical to the one which provides APL character generation with the APL\*PLUS/PC interpreter. Most 80386 based PCs provide a soft character set facility and will not require this ROM.

APL\*PLUS II is a new product from STSC - not intended as a replacement for APL\*PLUS/PC - which is closely modelled on IBM's APL2. However, most of the file and `⎕G`-style graphics functions in APL\*PLUS/PC are available in an enhanced form together with generic information to install and use Graphics Software Systems Computer Graphics Interface (GSS\*CGI); this is a device-independent interface to graphics devices for which cover functions are provided in the VDI (Virtual Device Interface) workspace provided as part of the package. The editor, reminiscent of )XEDIT, is a new feature: it allows multiple objects - one of which is automatically the active workspace and which may include native files - to be edited simultaneously. Another new feature is the session manager which is invoked by CTRL / and allows session bound features and parameters to be set via pull-down menus - this is an easier means than keyboard input of the relevant commands to achieve the customisation sought.

APL\*PLUS/PC workspaces and files can be migrated into the APL\*PLUS II environment and may not require code changes to run - workspaces cannot be loaded directly nor can files be tied as component files. The migration facility is not provided within the interpreter - as in the guise of )MCOPY in APL2. Instead, a number of base functions are supplied with adequate documentation on the syntax and procedure involved in the migration process. The reverse process is not documented - however, there would be little need for this when the APL\*PLUS II specific features are used. Instead of the familiar AWS and ASF extensions, WS and SF are used to differentiate workspaces and files. The APL\*PLUS/PC subset of this new interpreter is not totally compatible with APL\*PLUS/PC - just functionally so, with the aid of the utilities provided.

The packaging, style and feel of this new product shares the same hallmarks as the existing APL\*PLUS/PC product: the manuals (three volumes plus a quick reference guide) are precise and the usual range of complementary utility/tutorial workspaces - including printer support, assembler and APL character generation functions - are included on the three 1.2MB diskettes supplied (some GSS device drivers are not included because of lack of space, but are available upon request). Only 5.25 inch diskettes are supplied; however, the software may be supplied upon request and free of charge on 3.5 inch diskettes in lieu.

There are some omissions: there is no SYSHELP.SF file and therefore no help facility on the interpreter itself is available by default. The help facility provided is sparse and barely adequate. The system does not automatically use coprocessor support if available: the invocation must specify whether the version supporting the 80387 chip or the version with software emulation of the chip is used. The WEITEK coprocessor is not supported.

Moreover, the customisation of any APL session comes from the configuration stated in a native file which is CONFIG.APL by default, unlike the APL\*PLUS PC method where the desired configuration is achieved by supplying the relevant parameters when invoking the interpreter and an initial workspace to load and an APLLIBS.ASF file.

## Upgrading to APL\*PLUS II

The interpreter is very powerful and provides a very much more versatile environment than APL\*PLUS/PC - the obvious one being the facility for workspace sizes between 1-15MB with APL2 features.

This makes it a rival contender to the mainframe environment for the type of applications developed on the mainframe. However, while there is a definite cost advantage in favour of APL\*PLUS II, there will be some loss of flexibility.

APL\*PLUS II cannot be seen as a substitute for the APL\*PLUS/PC applications currently in use: the cost of the equipment and the interpreter itself is far too prohibitive and does not necessarily offer any obvious critical advantages.

There are alternatives to APL\*PLUS II which should also complicate the decision. There is DYALOG APL running under UNIX, with the facility to run up to four terminals and the flexibility to transfer workspaces to and from the mainframe APL2 environment, and with access security which is important in the maintenance of the application run. Also, IBM have announced an APL2 PC interpreter in the same league, at around 20% of the cost of APL\*PLUS II with the possibility of free run time systems.

The APL\*PLUS II package would be an ideal means for the development of personal productivity applications. These are the development of prototype solutions for use by a small team, probably within the same department - the styling and management of applications are irrelevant but the accuracy and speed of development are vital. In such a situation, the development is undertaken by the people who fully understand the processes involved without recourse to any systems analysis. In other words, APL is simply a well understood personal productivity tool rather than an art form accessible only via third parties.

The effectiveness of APL\*PLUS II within this context is limited by at least two factors:

1. There is no support for full screen applications other than in the standard functions (`⎕WIN`, `⎕WGET`, `⎕WPUT` etc.). The available functions are extremely powerful and probably much better than the GDDM equivalent on the mainframe, but are not easy to use effectively. There is no reason why the Society could not write and document standard cover functions so as to simplify the task of developing full screen applications.

2. There is no provision of help facilities on the system features of APL\*PLUS II which are unique to STSC. A system level help facility similar to the one provided with APL\*PLUS PC would have been sufficient. Although the same help facility could be invoked from the APL\*PLUS II interpreter, this would be deficient in those things which are characteristic of second generation interpreters and may be misleading not only because the two interpreters are not fully compatible but also because certain features are exclusive. Thus training courses would be necessary for those new to the PC environment.

Also, not enough information and utilities are available to assess the effectiveness of APL\*PLUS II in a networked environment. The intention would be to share files and workspaces among users - possibly on an alternate basis so that the dongle could be used by say two people - and with the mainframe APL2 environment.

On the other hand, the APL\*PLUS II offers an APL2 style interpreter with enhanced file and graphics facilities which are very well documented in the manuals supplied.

I evaluated the package on a COMPAQ 386/20 with 5MB RAM, 80387 coprocessor, BROTHER HL 8 laser printer and colour VGA monitor. The cost of this type of configuration provides a good estimate of the cost of making a transition to APL\*PLUS II on a PC from the current APL2 on the mainframe. Also, an assessment of the training needs and the level of support should be made.

The complexity of the task to migrate mainframe applications to APL\*PLUS II must not be underestimated. GDDM or auxiliary processor 126 is not available in the APL\*PLUS II environment, and file handling is very different on the PC - thus major changes will be required to the mainframe workspaces using GDDM and file facilities before they would run. Even those applications which are workspace based and do not use files may need scrutiny as APL2 and APL\*PLUS II are not 100% compatible.

## A Personal Assessment of APL\*PLUS II

I am familiar with VSAPL under VSPC, VSAPL under TSO, APL2 under TSO and APL\*PLUS/PC.

With a good knowledge of APL, APL\*PLUS II is a familiar environment from the outset for me, particularly as it retains most of the characteristics of APL\*PLUS/PC. A notable difference is the session manager and the new editor. The session manager is very unlike the session manager for APL2 in that it can be relegated to a dormant state. Its obvious advantage being the facility to set session bound parameters within a workspace via a series of pull down menus rather than by keystrokes.

The editor is reminiscent of )XEDIT in VSAPL under TSO. Once within the editor, it responds to the usual ALT/key combinations in the same way as the APL\*PLUS/PC editor. The ability to edit and update native files from within a workspace simplifies the procedure a great deal - although when APL\*PLUS II writes back an existing native file, called up by the editor but not altered, the new file is larger by a matter of a few hundred bytes. The specification of a workspace name using the DOS path as part of the specification rather than a library number appeared somewhat alien to an APL environment - but the usual convention of library numbers may be selected by modifying the CONFIG.APL file appropriately.

Some irritations with the APL\*PLUS PC interpreter still exist - for instance it is still not possible to edit numeric objects in the new editor. Others do not: `⎕TRACE` and `⎕STOP` survive the editor, there is no need to wrestle with the setting up of virtual workspaces. The usual convention for ambivalent functions is retained. There are some practical enhancements such as )PSAVE which prevents accidental overwriting of a workspace on disk. The )GROUP facility does not exist - in the VSAPL environment this allowed any number of objects which had been grouped to be copied from a saved workspace by simply specifying the group name. It is possible to copy any number of objects from a saved workspace but the individual object names must be known and specified in a character array and the array specified for the )COPY operation.

Given the size of the workspaces, and the fact there is no warning that there may be multiple editor sessions pending when logging off, I would have liked to have a facility within the interpreter which saved the active workspace at random intervals providing something in the guise of the CONTINUE workspaces in APL2. Such a facility would permit most of the work during any session to be partially safeguarded automatically.

The equivalent of `⎕TF` in IBM APL2 is absent, as is )MCOPY. Both of these omissions are noted by STSC; a way round the problems created is suggested in the workspace and file migration procedures detailed and the provision of the SLT (Source Level Transfer) workspace which uses the WIC (Workspace Interchange Convention level 1). An )MCOPY facility would be valuable in that developments are very likely to be continued in the APL\*PLUS/PC environment and subsequently ported into the (expensive) APL\*PLUS II environment.

The migration procedure advocated does work, although it is quite contrived to be contemplated as a matter of routine, as long as the few incompatibilities of the APL\*PLUS/PC and APL\*PLUS II are remembered. The `⎕CT` is different, `⎕KEYW` does not exist, system functions are not absorbent, library number convention must be used within the CONFIG.APL file when an application uses library numbers, the help file is defined in the CONFIG.APL file and the few incompatible `⎕POKE`s are sorted out.

For the types of applications I have developed, the omission of the `⎕HNAMES` system function causes unnecessary problems. It means that it is not possible to change the file to hand when pressing ALT F6 from an APL session. The file accessed is specified in the CONFIG.APL file and cannot be specified in a `⎕LX` function as is my current practice. Also, the fact that system functions are no longer absorbent and cause an error condition is very irritating to me - it's a style that I am very fond of and which I use to avoid yet another entry in the Symbol Table - space is at a premium when the maximum workspace size is 440KB. However, this is a minor problem since the APL\*PLUS II workspace sizes are appreciably larger and the Symbol Table is dynamic and allows 32767 entries.

The interpreter is fast, the loading and saving of workspaces also appear appreciably faster. My personal preference would be to develop fresh applications from scratch using wherever possible the enhancements of this second generation interpreter. The first objectives would be to develop a workspace of cover functions for full screen applications and another workspace of standard library routines of the type I have developed in APL\*PLUS/PC.

## Songs of Innocence & Experience

APL\*PLUS II offers an unrivalled environment as a personal productivity tool, requiring only a good knowledge of the language for the development of any application without compromise. The power of the language is that it allows its user total control over expression - it allows all its characteristics to be interrogated, offers very good error trapping facilities as well as reporting errors in a constructive way, has operators and primitives which are capable of reducing concepts to a few symbols (think of nested arrays, for instance), offers excellent filing and graphics facilities and allows progress from concept to program code without any intermediate steps with great ease. It has no equal in the absence of automatic code generators.

Unfortunately, the APL environment is marred by its propensity for a variety of programmer abuse, and it requires a run time system - at extra cost - for the distribution of applications. The APL\*PLUS II system suffers in a number of respects: the enormity of its workspaces makes a disciplined approach to documentation and maintenance mandatory, the cost of its run time system is high and the cost of putting together an APL\*PLUS II work station is very high at between £7,000 to £12,000.

Given that APL\*PLUS II is highly unlikely to be considered for application development in a green field situation, I would have liked such utilities as workspace migration from the mainframe and the ability to read data from industry standard applications, such as LOTUS and SMART, bundled with the package. A facility to use APL\*PLUS II under Microsoft Windows/386 such that multiple APL\*PLUS II sessions were possible might have its uses too - I was unable to use APL\*PLUS II under the Windows environment.

The utility workspaces are the ones packaged with APL\*PLUS/PC Release 6.0 onwards - that is they are not optimised for the enhanced second generation environment.

Nevertheless, I would have no hesitation in recommending APL\*PLUS II as a strategic product for PC applications development.
