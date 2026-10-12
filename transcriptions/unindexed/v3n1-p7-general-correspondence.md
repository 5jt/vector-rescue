---
title: General Correspondence
volume: '3'
issue: '1'
page: '7'
unindexed: true
transcribed: 'from page images of VOL.3-NO.1-JULY-1986.pdf, pages 9–14 (printed 7–12); Claude, 2026-10-12'
review: draft
tags:
- APL community
- APL in perspective
queries:
- "Four letters: L J Devaney, “APL – USP or RIP”; Andre Faure, “APL for newcomers”; David Livingstone, “APL research studentship”; and A.G. Bright of I.P. Sharp Associates, printed without a heading. The editor’s replies are in italics, as printed."
- "Following the project rule for individuals’ contact details, the street address of L J Devaney (London), the street address of Andre H Faure (Jyväskylä, Finland), and David Livingstone’s vacation address and telephone number, are omitted. Livingstone’s address and telephone number at Newcastle-upon-Tyne Polytechnic, and A. G. Bright’s at I. P. Sharp Associates, are kept."
- "The lower half of printed 12 is an APL-385 advertisement (“Free Digital Cuckoo Clock”), not transcribed."
- "Kept as printed: “it is to published in full” (introduction); “a Burrough’s installation” (Devaney); “Jyvaskyla” without diacritics (Faure); “get the prospective student to.” (Livingstone); “avialable” (Bright); the editor’s reply to Bright opens with “(Ed:” where the others have “(Editor:”."
---

*The VECTOR working group welcomes correspondence on any topic affecting the APL community. All such letters should be addressed to the Editor and should indicate whether they are intended for the general or the technical section. Letters containing APL code will normally appear in the Technical Section of VECTOR, and authors are asked to observe the requirements on the inclusion of APL code stated on the inside cover. The Editor reserves the right to edit any letter unless the writer states that it is to published in full or not at all.*

## APL – USP or RIP

*From: L J Devaney, 15th April 1986*
{ .byline }

Sir,

In my opinion the APL milieu has a most unsatisfactory scabrous patter (MUSP). APL’s inability to penetrate the mass market place is surely conditioned by:

a) the complete lack of management control;  
b) the unintelligible texts that APL functions contain, whether keyword or symbolic;  
c) lack of portability;  
d) the inability to implement closed, secure systems.

Management control is important because of the need to conserve a firm’s investment in software and to establish a firm control over program libraries. Change controls are necessary procedures in business and the cycle of “design, implement, test, change, re-test” is an important one. APL is unable to support properly established libraries, segregated responsibilities and incremental implementation in the way that COBOL, FORTRAN and other languages can.

The readability of code has in the past been promoted at the expense of function, but APL promotes function at the expense of readability. Mr Last’s examples on page 98 of VECTOR, Vol.2, No.3, would not be improved by using keywords! Part of the problem is the use of one line of text to do so much work. Although COBOL, FORTRAN, etc. use more statements and would need intermediate variables to hold partial results, overall their texts would be more intelligible because of the stepwise presentation. Of course, APL could be so written, but the power of the language bodes ill for such considerations to be of more than a fleeting interest to APL “professionals”.

Portability is important to some user-communities. When I worked abroad some years ago, we received a large FORTRAN program from a Burrough’s installation. Although we were operating an IBM installation, all that was needed was to follow the few rules documented as comments at the beginning of the program and then compile link-edit, etc. in the usual way. No problems ensued. The text was received on magnetic tape. The only portability for APL that I know of is typing it all in again!

BASIC and APL have a common problem – the user can meddle with the programs if they know how to. Today it is not possible to have one’s system developed in APL and secured against intrusion. This extends also to operator authorization/permissions and operational safety. “Runtime only” versions may help, but a more thorough solution is required for the long term.

Yours,

L J Devaney,  
[address omitted]  
London, W3 0NP.

*(Editor: Thanks for your comments – no doubt they will stimulate a response from our readers!)*

## APL for newcomers

*From: Andre Faure, 30th December 1985*
{ .byline }

Sir,

May I compliment you on your publication. I feel that VECTOR as now produced is an excellent journal. Overseas members do not probably have much use for the club news which takes up quite a bit of the publication space, but, after all, the journal must also serve the British Association. However, given the high calibre of writers involved in its production, it could perhaps reach a wider readership if it also tried to educate users and newcomers to APL. No publication to my knowledge does that at the present time.

There are two types of person interested in APL: those making a living with it and those looking for a tool to solve their computing problems. The former may not need much help with APL and usually have access to other experts. The latter need first of all convincing that APL is “it”, and then help in getting started. Moreover they are usually isolated, especially if they intend to use APL in a personal computer environment. This is where VECTOR could do a lot of good.

It must be recognized that APL presents a higher starting threshold than most languages. For instance, simply listing a function on a printer with the STSC APL\*PLUS/PC requires a function to be written with `⎕POKE`s and `⎕ARBIN`s. I doubt whether any newcomer to APL can handle that with only the aid of the manuals. It took me two days and quite a few phone calls. In BASIC, you type LIST and are content with that – any kid can do it!

You could (and should) fill two or three years of VECTOR with tutorials for newcomers (and dare I say old-timers as well?) on how to manipulate inputs and outputs in APL. How do you build an entry screen which will support a normal keyboard and a “fill the blanks” data entry principle? How do you write reports? How do you take care of headers, footers, page numbers, etc.? This is not easy, or the text-books would not so blissfully ignore the subject.

My experience is that computing with APL does not present many problems. In fact, it is fun! Adding inputs and outputs to build a system that anyone can use on any machine is another story, and that story needs telling.

A theme which keeps recurring within APL concerns those curious little characters used in APL in addition to the normal alphabet. Your editorial policy appears to be that these symbols deter potential users and should be replaced with keywords. I disagree. Using the APL character set is fun and fast. What is not so funny is returning to a function a few days later and trying to figure out what that line of symbols actually performs. What I miss is a translator, which goes beyond mechanically replacing each symbol with a keyword: the translator should look at the context in which each symbol is being applied (the APL interpreter does that, to my understanding), and replace each symbol, or set of symbols, with a suitable plain language equivalent. The plain language equivalent need not be executable code, only documentation.

Since the translator would first parse a line of code into a set of unique operations (as does the interpreter) and then replace these operations with plain language equivalents (a table look-up operation), it becomes immediately obvious that the translation could be carried out in any language. Thus APL could offer the best of both worlds: a universally understandable and transportable set of symbols, that can also be translated into the user’s own language. The compactness of the language actually makes translating easier, since phrases can then be used instead of single words.

Yours truly,

Andre H Faure,  
[address omitted]  
Jyvaskyla,  
Finland.

*(Editor: Thank you for your comments on VECTOR to which I would like to add my own thanks to all those who have contributed to it. We do try to remember the needs of APL beginners, but a regular feature sounds like a good idea.*

*The VECTOR editorial team as such does not take a policy position on such issues as symbols versus keywords; individual papers – and for that matter editorials – merely reflect the views of the author concerned. Certainly the independence of the symbols from a user’s national language is a new and interesting aspect of the discussion.*

*On a personal note, I am extremely attracted to any idea that would effectively reduce the need for me to document my code! I would however disagree with the comment that the starting threshold for APL is higher than other languages; when my son was four I sat him in front of a micro for the first time and without prompting he correctly entered a valid line of APL. Unfortunately, he didn’t know about the Return key!)*

## APL research studentship

*From: David Livingstone, 11th April 1986*
{ .byline }

Sir,

I wonder if any of your readers know of a student who may wish to do research in APL, leading to an M.Phil/Ph.D?

Such a project will be starting in the Autumn of this year at Newcastle-upon-Tyne Polytechnic’s School of Computing and Informatics. It will have External Supervisors from IBM and Dyadic Systems Ltd.

The aim of the research is to develop the concept of domains in APL. Currently there are just 2 domains or types of value that may appear in a variable – numbers (the set of all numbers that can be held on the computer) and characters (the set of all characters stored in the Atomic Vector).

It would be useful if the programmer could tailor domains to meet the particular needs of an application rather than be limited to these 2 primitive sets of values. By specifying a variable’s domain precisely, data can be validated automatically when it is assigned to the variable. The same approach can be used in debugging, to check a variable contains only permitted values at a particular point in a function.

The specific objective is to add to APL the optional facility to associate a user-specified domain of values with a variable. Whenever a value is assigned to that variable, a check will be made to see whether it lies in the variable’s domain of permissible values. If it does not, a DOMAIN ERROR or appropriate interrupt will be generated.

As a domain is a mathematical set, it can be specified either by enumeration or by set conditions. Ordinary APL variables or functions respectively will be used to implement the 2 kinds of set definitions. Thus the full power of APL will be available to define domains.

Please phone or write to me if you know of anyone who may be interested in doing this project; or better still, get the prospective student to.

Yours sincerely,

David Livingstone,  
School of Computing and Informatics,  
Newcastle-upon-Tyne Polytechnic,  
Northumberland Building,  
Newcastle-upon-Tyne,  
NE1 8ST.  
Tel (0632) 326002 ext 3347

Vacation address: [address and telephone number omitted]

---

*From: A.G. Bright, 1st May 1986*
{ .byline }

Sir,

I read with interest the recent article in VECTOR Vol. 2, No. 3, by Katie Williamson and Geoff Wells concerning external databases and APL applications. It was pleasing to see experienced programmers integrating I.P. Sharp databases with APL systems.

As a postscript to the article it was stated that there were inaccuracies in the share price data provided by ourselves and that the service was being withdrawn. Having had extensive contact with the authors of the article I can appreciate the accuracy of the statement from their perspective. It is however slightly misleading to the outsider and I would like to clarify the situation.

Through extensive use of our FTSTOCK database (London share price information is provided – in a raw form – to I.P. Sharp by the Financial Times), Katie and Geoff did indeed find several inaccuracies. Upon close examination of the database we realised that due to the extent of these inaccuracies we could no longer market FTSTOCK in good faith and therefore withdrew this database at the end of February 1986.

However, a suitable replacement is avialable on-line from us in the form of EXSHARE – Extel Computing’s International Stocks Database. This contains coverage not only of the London market (including the USM, Eurobonds and options) but also all major non-American markets. The database is updated daily and data goes back to January 1983. EXSHARE complements our North American databases giving I P Sharp a complete coverage of the world’s major stock markets. This is in addition to worldwide coverage of commodities, traded options, and over 100 other time-series databases . . . but then this isn’t supposed to be a commercial!

So, it is true to say that errors were found in our London share price database. We therefore changed our source and in doing so we now supply a more comprehensive coverage. I trust this has clarified the situation.

Yours faithfully,

A. G. Bright,  
Database Consultant,  
I. P. Sharp Associates Ltd.,  
10 Dean Farrar Street,  
London SW1H 0DX.

*(Ed: Thanks for clarifying the issue. Geoff and Katie encountered these problems late after submitting their article for publication, so there was only time available to append a brief postscript. I’m sure that many readers will find your letter useful.*

*Two thoughts arise as a result of this. Firstly that the responsibility of ensuring data validity is an onerous one, whether the data is provided externally, as in this case, or is only made available within one’s own organisation. Clearly I.P. Sharp’s prompt action in withdrawing the particular service involved reflects their own recognition of this responsibility.*

*Secondly, that the issues involved in this particular case, as I understand them, were not the simple ones of whether a particular set of numbers were right or wrong, but concerned the exact mechanisms used to adjust historic data, e.g. to compensate for subsequent share issues. I wonder how many other data-sources there may be whose exact specifications are either unclearly defined or rarely validated and how many Decision Support Systems provide such data as an input for decision-making.)*
