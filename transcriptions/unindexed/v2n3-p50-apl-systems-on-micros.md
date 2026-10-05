---
title: Introductory Notes; APL Systems on Micros, October 18th 1985 (meeting notes)
authors:
- Adrian Smith
- Eileen Dyson
volume: '2'
issue: '3'
page: '50'
unindexed: true
transcribed: 'from page images of VOL.2-NO.3-JANUARY-1986.pdf, pages 52–61 (printed 50–59: Adrian Smith’s introductory notes, then Eileen Dyson’s notes on the talks by Staffurth, Dakin, Shaw, Birch and Thornton; an APL People advert fills the foot of p.58; the APL in Practice meeting follows on p.60); Claude, 2026-10-05'
review: draft
queries:
- "Each talk is printed under its own heading with “by <speaker>”, though these are notes on the talks (the contents list gives Eileen Dyson for the meeting). Transcribed as H2 sections with the speaker in italics."
- "p.59 (Thornton) has no running head. Its list of MicroAPL customers is printed as two columns separated by dashes; transcribed as a definition list."
- "PEFAC’s five modules are printed with hollow triangle bullets, and the two uses with solid ones; transcribed as plain lists."
- "“10⁶ and 10⁸ separate logical paths” is printed with superscripts."
- "Slips transcribed as printed: “the The Royal Over-Seas League”, “to add further in due course”, “practises”, “diagramatic”, “Don Jones” (Dow Jones?)."
---

## Introductory Notes

*by Adrian Smith*

In this issue I have included notes on two very successful meetings, both at the now well-established venue of the The Royal Over-Seas League. The first was a series of (mostly) short papers on applications on micros; the second a much more lightly programmed set of papers on commercial APL systems. Readers are referred to the Case Study for a fuller version of Christine Brewster’s talk on Sales Analysis.

Besides our coverage of British APL Association meetings, we also have a report on the APL Statistics User Group and a review of some of the sessions from the Operational Research Society conference held in Durham.

## APL Systems on Micros, October 18th 1985

### Introduction

I would like to thank Eileen Dyson for taking such thorough notes on this very heavily scheduled meeting. The overall impression was of a set of well constructed and relevant talks; towards the end this was unfortunately thrown by one speaker who went way over his allocated time, and hopelessly cramped those who followed him.

Maybe to have five talks in a single afternoon was pushing things a bit anyway? It may be a super way of filling up VECTOR, but I can’t believe that all the speakers were really given the attention they deserved.

## Developments in PEFAC

*by Chris Staffurth*

This paper gives an update of the talk on PEFAC that Herbert Walton gave to the APL Users Group in 1981, and how PEFAC – Production Engineering Fast Accurate and Consistent – has been transferred from the I P Sharp time-sharing environment to the IBM PC.

PEFAC is an estimating package that does all the arithmetic for the industrial engineer when he has to estimate the time that would be taken to machine a given component. It is particularly useful for:

- the company that does sub-contract machine shop work and has to provide a quotation from the drawing of the part to be machined. That is, it needs to be Fast and Accurate.
- the company that pays its machine shop operatives on a bonus scheme. That is, it needs to be Accurate and Consistent.

PEFAC consists of 5 modules, for:

- Turning
- Milling
- Grinding
- Drilling
- Boring

It can also cope with Ancillary modules that can be written to meet customer’s particular methods and environment. For example, Sheet Metal work is done in a variety of methods, and it is not really possible to program the general case.

PEFAC is now sold on an IBM PC/XT with 10mb. hard disc, a minimum of 384k bytes memory, mono or colour VDU and preferably an Epson FX printer. It uses the APL\*PLUS interpreter.

There is a PEFAC workspace which contains the basic functions for input, output and other housekeeping tasks. Functions relating to individual modules are called into memory when required (and the functions relating to the previous module if different are expunged). A special pair of functions containing Assembler segments has been written. One function packs objects, either functions or variables into a single object, and the other unpacks them. This is reckoned to be 5 – 10 times faster than storing functions in quad-CR form and then using quad-FX to fix them.

The PEFAC system is menu driven and the user is unaware that the functions have been written in APL. Even the keyboard is set to run in the ASCII mode. This provides an interesting situation for the maintenance programmer who has to alternate between the two modes: the overstruck characters are in different positions on the keyboard. Maintenance work on site in the absence of a chip for an APL character generator is even more interesting. Characters like Spades, Hearts, Diamonds and Clubs and others appear on the screen.

Being menu driven, the user has usually to answer Yes or No or 1, 2 or 3 to questions. But where there is a list of things to look up, for example, a list of materials or a list of available machines, then use of a function key will display the whole list on to the screen in inverse video.

If the user is uncertain of what input is expected, there is a set of Help screens that are invoked with a function key, and these explain the requirements in detail.

PEFAC generates a report showing the basic machining time of each element of an operation. Each operation report is stored in a temporary file. This temporary file is a security measure, in case for any reason the estimate for a complete job is interrupted part way through. Then only the part-completed operation is lost. It also serves as a What If report, and allows the user to try out more than one method of machining the part. When the user is satisfied with the report, it can be kept permanently, and PEFAC transfers it to a separate Drawings directory.

Engineering Change Orders are a frequent occurrence in a machine shop, in which maybe only one dimension is altered. A revised estimate can be easily calculated by retrieving the drawing from the Drawings directory and by re-processing the element which calls for the particular dimension. If a material specification only is changed, the report of the drawing can be similarly retrieved and after the material has been changed PEFAC will silently reprocess the whole estimate, without the user having to re-input the answers to all the questions. This means that besides packing away the text of the report for each operation , numerous parameters relating to operations and elements have also to be stored. In fact, PEFAC has to work very hard behind the scenes, but it saves the estimator a lot of time and trouble.

As a security measure against corruption of the hard disc, the reports may be backed up on to diskettes, and there is a comprehensive index to keep track of the whereabouts of all the drawings in the system. When there are more than 50 drawings in the Drawings directory, PEFAC starts to erase them from the hard disc, but only if they have been backed up on a diskette.

Although every user has the standard functions for each module, there is usually a different set of machines and materials. Therefore different data is required for each customer. Another workspace exists to allow the user to input or edit any of the data relating to his machine shop. Full screen editing is obtained from a set of functions that has been written. The screens are arranged hierarchically. The user is asked successively for the module, machine group within the module, the actual machine within the group, and then the table within the actual machine. Functions are required to edit character and numeric arrays, and to interpret the action of some 20 non-alphanumeric keys. It is possible to insert or delete new tables or even data relating to a new machine.

At the bottom of the screen are simple prompts for going forward, going backwards, saving and quitting. There is an Edit Help screen which explains the editing in detail, and also an Engineering Help screen which explains the engineering terms used.

Although the PC might be called a micro computer, workspace size or WS FULL messages are not a problem. By overlaying the module functions and storing the report after each operation, there is sufficient space for all intermediate calculations. As a final measure, a check is kept on quad-WA, and then when it gets rather low, the user is prompted to end that operation and to start another.

The response time is generally 2-3 seconds and never more than 5 seconds. This is adequate since the estimator has to think of the job in engineering terms as well as inputting dimensions etc. The reading of the module functions takes about 30 seconds, but since it does not occur very often, it is no great hardship.

Software errors do present a problem. It is estimated that there is somewhere between 10⁶ and 10⁸ separate logical paths through PEFAC, and therefore impracticable to test it for every eventuality. In the time-sharing environment it was fairly simple to log on to the user’s CONTINUE workspace and sort out his problems. But that is not possible on the PC.

On the PC there is a general error trapping function which does two things on encountering an APL error. It sends to the printer the APL error message and the offending line in the function that caused it, together with the contents of the SI stack, plus some parameters relating to the element in hand. This is posted to us and is used as a guide in reproducing the error condition. A corrected file is copied on to a diskette which is then posted back to the user. The error trapping also escapes from the current operation, or if the error is severe, re-loads the complete PEFAC workspace. In either event, the user is not left entirely hanging in mid-air. At least he can continue with his work.

Development of PEFAC continues, and there are plans to add further in due course.

Acknowledgements were given to Herbert Walton for starting PEFAC and making it into a commercial proposition, and to Ian Kemmish who masterminded the installation on the PC.

## Corporate Planning at Laura Ashley

*by Adam Dakin*

The speaker worked for Deloittes, a London based computer company which had been involved in developing a corporate planning system for Laura Ashley. The system was developed in eight months by a team of four; it was written in APL and ran on an IBM PC/AT.

### History of the Project

To quote the speaker:

> “LA is a fast growing company, receptive to new technology. It is an exciting place to work”

LA make corporate plans every five years. In 1980, the plan was worked out by hand; it was a long hard slog with a lot of number-crunching. Top management then vowed that a computer model would be developed for next time, both to do the number crunching and to allow ‘What if’ questions to be evaluated more easily. The model was therefore specified in 1981 but development did not begin until 1984.

LA produce a wide range of products which they sell worldwide. They have manufacturing sites in the UK, Holland and USA and sell a diversified product range through a range of outlets. The company also buy in from third parties if they feel they can sell goods which they cannot produce internally.

### Important Factors

1. Structural – The structure of the company may well change over the next 5 years. For example LA are currently moving into Japan.
2. Sales Targets – LA is a sales led company and again sales patterns may well change in the next 5 years.
3. Manufacturing and Retailing Operation – Manufacturing practises and technology could well change in 5 years as could the balance of stock.
4. External – typically exchange rates

Factors 1-3 are all within LA control and can therefore be predicted whilst LA has little control over factor 4.

The first stage in developing the model was to decide the level of detail to be used. Similar outlets and products were grouped together to make the data more manageable, but at the same time a tradeoff was needed to avoid the data becoming meaningless. It was decided to group the outlets nationally and to group products into six categories. The products and locations were then linked in a diagram; even at this early stage simply seeing a diagramatic representation of the company was useful.

### LAPLAN - Modules

The system was divided into 8 modules. Modules 1-4 could be used to simulate the company whilst 5-8 provide a means of investigating the financial implications of these simulations.

1. Calculate sales revenue & stocking
2. Routing (Demand from factory A to location B)
3. Manufacturing Costs – Unit cost of production
4. Transfer costs between groups
5. Trading account by country
6. Manufacturing account
7. Company results
8. Group results

### Implementation

Data required for the module was in several dimensions and it was therefore felt that APL was the most appropriate language to use being more flexible than WIZARD or other modelling languages available on micros or mainframes. It was decided to use APL for modules 1-4 and SYMPHONY for 5-8.

The first three months of development were spent getting the algorithms working correctly by means of a prototype.

### Benefits of a prototype

1. Proves model algorithms
2. Gives user familiarity and confidence
3. Highlights data requirements
4. Promotes discussion of possible use
5. Offers smaller version of the model earlier at a lower cost

### Current System

The system is a ‘Black Box’ menu driven system which is easy for the user and makes APL invisible to him. It now requires some 17Mb and therefore had to be switched from RAM to filing. Also in an attempt to conserve space the four-dimensional data is stored as several three dimensional arrays with pointers to them in the workspace. One of the more tricky parts of the development involved setting up print files to link to SYMPHONY.

In summary, the model is a success. It shows the value of prototyping and also that micro-based APL is powerful. It also opposes the theory that APL is an unfriendly language to use; the speaker had no previous experience of APL, yet he managed well with it and would quite happily use it in the future.

## An Integrated Manufacturing System on a Local Area Network

*by Ed Shaw Junior (Bristol Myers)*

Bristol Myers is a large American-based company producing a variety of products including pharmaceuticals and medical equipment. The Corporate Systems department employs about thirty people, all writing APL. This makes them the second largest APL users in New York.

The system which the speaker described was currently being installed in one of the Dutch factories which manufactured milk-based products.

It was complex and was copiously described to us by means of a very colourful but totally incomprehensible overhead slide. The idea was that the system had to be designed for all areas of the company to use. At the purchasing end it was used for purchase orders and goods inwards. The information was then used for inventory and production control, and also to specify the formulae for the products and for daily production scheduling. Quality control also got their hands on the data, and eventually it was used for sales information, packing lists and invoices.

The system had to run in real time. When the milk was delivered production needed to know what the protein and solid content of each batch was so that they could adjust their recipes accordingly.

Other than the gory details of what each function of the company used the system for, I did glean that it used an STSC tool box of APL’isms and ran on a LAN which had a four hour ‘fix it or else’ maintenance agreement with the suppliers.

## Migration from Mainframe to Micro

*by John Birch*

The speaker was from Premium Management, a company in the City concerned with managing investments for the insurance industry. He felt that to be successful a company should consider three questions:

1. Where are we now?
2. How did we get here?
3. Where do we go next?

Because of statutory restrictions his company had to concentrate on points 1 & 2 even though 3 is probably the most interesting.

The fixed investment market involves a great deal of arithmetic. Until 1983 the company ran APL on an IBM mainframe when they decided to migrate to a micro. The micro which they chose was the MicroAPL Spectrum.

### The Migration

Three points arose during the migration:

1. The IBM APL was compatible with APL.68000. However the execution of some code was accelerated by using the APL.68000 quad functions.
2. The file system was incompatible and had to be rewritten for the Spectrum. The data base also had to be redesigned to obviate problems created by the relatively slow input/output processes.
3. The Full Screen systems were compatible as the company had moved from AP124 to AP126.

It took just 15 days to migrate from the mainframe to an operational system on the Spectrum (including the Christmas break). It then took 2 people a further 5 weeks to enhance it to a satisfactory system.

Before the migration the company had 1 printer and 1 VDU on their mainframe. They now have 5 VDUs connected to the Spectrum and the system is also linked, or is planned to be linked, to various external services such as those offered by Citibank, Don Jones and the Telex network.

Investors like an easy life and therefore any systems developed for them must be simple to use with minimum effort. For this reason the company is looking at using Telecom touch screens.

### Why APL?

APL is used within the company because it is quick and easy to write. The strange hieroglyphics and intricacies of APL can be hidden from computer illiterate users. It is also easy to amend reports to please the users and can be done relatively quickly. It is however the only language the speaker has used so he may be slightly biased!

### Problems with the Spectrum?

Multi-usage is not a problem on the Spectrum. If there is a problem it lies not with APL but with the speaker’s secretary who tends to get rather carried away when using the machine as a wordprocessor!

The only real problem is that response is poor if several users are all accessing disks at once because the Spectrum reads sequentially.

## An Overview of APL Applications on Micros

*by Paul Thornton (MicroAPL Ltd)*

The speaker gave a very brief overview of the types of applications MicroAPL have been involved with in recent years. In general there is a broad spread of applications across a variety of industries. These applications are in fields such as OR, Information Services, Maths, Commerce, Science, Education and Real Time applications (primarily Process Control).

National Westminster Bank
:   Dial in data bulletin board.
:   Developing funds transfer via a dial-in system.

Bank of England
:   Small Multi-user systems.

Golden Wonder
:   Distribution Applications
:   What is the best method of transferring goods from A to B?

St Thomas’s Hospital
:   Collating data from a questionnaire on diabetes

British Telecom
:   Training staff on electronic theory

Mobil Oil
:   Calculating wastage when passing oil through pipes.
:   Route Planning
:   APL Simulation of a complex Fortran simulation program

Cornhill
:   Modelling

Heineken
:   On-line production monitoring

Before 1982 there were no full implementations of APL on micros, today there are several.

### Features of micros

1. Small desk top unit – The user therefore feels more secure.
2. Ease of access encourages people to dabble.
3. Fast data output to screens, a feature only previously available from IBM.
4. Excellent for device control – it is relatively easy to connect to Reuters etc.
5. APL is used extensively for prototyping. It is now possible to link in Assembler and use non APL packages thus increasing the range of usage.
6. More people though not a significant number are using APL.
7. IBM PC APL was the cheapest available but now APL is available on the QL for around £300.

Taking all this into account, the future looks promising.
