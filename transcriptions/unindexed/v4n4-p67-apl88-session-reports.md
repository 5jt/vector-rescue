---
title: 'APL 88: session reports, plenaries, panel and exhibition'
volume: '4'
issue: '4'
page: '67'
unindexed: true
transcribed: 'from page images of VOL.4-NO.4-APRIL-1988.pdf, pages 69–90 (printed 67–88); Claude, 2026-10-06'
review: draft
queries:
- "Reports on individual APL 88 sessions by the Vector reporters (Camacho, Adrian Smith; see the section introduction, v4n4-p55). The bylines name the speakers (“by Warren Julian”), not the writers of the reports. Grouped into one file in print order."
- "Photographs of speakers are described, not reproduced."
- "Crystallography: +\\8⍴1 is 1…8 (balls per row), +\\+\\8⍴1 the triangular numbers (per plane), +\\+\\+\\8⍴1 the tetrahedral numbers, as described."
- "Iverson’s closing paper is said to be printed in full in Vector; the Vector reporter promises a fuller account of MacIntyre’s talk in 5.2."
- "Slips transcribed as printed: “There conclusion”, “keenness do specify”, “a lot off effort negotiating about about”, “crytallography”, “represention”, “STSC on the the hand”, “a lots of mainframe APL2 sites”, “possible as a serious”, “remarkable fast”, “extroadinary”, “different subjects attract subjects of differing ability” (for students)."
---

## APL 88 Opening Plenary Session: Computing at the University of Sydney

*by Warren Julian*
{ .byline }

Dr Julian generously made the University of Sydney School of Architecture available as the venue for most of the sessions of APL88. The School of Architecture has one of several impressive computing laboratories which we saw around the campus and Dr Julian set himself to describe how computing in the University had changed over the 30 years from the early 1950s mainframe called SILIAC to today’s banks of PCs and Macintoshes.

Dr Julian recounted how, in the High and Far Off Fifties, the then Professor of Physics raised the $50,000 (estimated) and the $75,000 (actual) needed to buy the new-fangled machine from Illinois. The authors believe that it is his name that is now carved in stone under the eaves of the Physics School in the august company of Newton, Einstein and other luminaries.

*[Photograph.]* Warren Julian

In 1964 those original, precious 1024 words were replaced with the help of some Texan money by a KDF9 and 4096 words and ALGOL. In due course IBM got a foot in the door and by 1967 there was a 7040 and FORTRAN on cards. In the School of Architecture APL was introduced to economise on programmers but in the Computer Science Department it is still, as so often, a novelty with which few students are involved.

Gradually the emphasis within the School of Architecture is shifting towards knowledge engineering, some of it based on bought-in packages but including APL on Macintoshes. A great deal of the work done arises out of the modern bureaucratic nightmare of codes and regulations which constrain all those who would build in a crowded city.

It is interesting that the University is experiencing the same dilemma as faces many other computer users who have until recently been content with a time-sharing service based on a central mainframe. Now that every Department has a bank of microcomputers what role is left for the once mighty machine? We gather that in Sydney, as elsewhere, this debate is still active.

## Iterative Scaling of Marks

*Peter Petocz*
{ .byline }

This talk described a consulting job, where APL’s matrix features had been used to advantage to get quick and accurate results. The basic problem is how to compare scores on different tests when the candidature varies. For example students take exams in 5 out of 20 topics offered; different subjects attract subjects of differing ability, so you cannot just standardize the scores to the same mean and S.Devn. and add! How do you give a fair score to the minority who take the harder subjects?

The solution is a form of inter-subject scaling, using the standard of candidature in each subject. Each subject is adjusted based on how the students did in all the other subjects ( …. ) until the whole set of marks converges. Typically 40,000 pupils take the N.S.W. tertiary selection – so it matters to get it right!

For the code and the details of the algorithm (it fits neatly on one page) see the APL88 Proceedings Page 263. Typically 3 or 4 iterations settles it (rounding to the nearest integer helps!) and a ‘pressure test’ such as adding 10% to all marks in a particular subject has no effect on the final outcome.

Peter’s final comment was that (in a topic which has aroused vehement public debate) it is nice to see the entire process expressed in a couple of simple APL functions, rather than in pages of incomprehensible text in the Educational Supplements!

Linda Alvord noted that this would be a wonderful one to let the kids loose on … it is something they really care about! You would certainly get some thoughtful reactions to its fairness.

## APL Applied in Music Theory

*by Michael Kassler*
{ .byline }

The regularities of Western music have not yet been made completely clear. This presentation described the work in progress by Michael Kassler to convert theories of tonality proposed by Kollman (1756-1829) and Schenker (1868-1935) into APL. To do this it is necessary to make the vague parts of the theories precise.

The representation of polyphonic music naturally suits a matrix where the rows are the parts and the columns the passage of time: all notes in a column sound simultaneously.

It was fascinating to see how the theories add decorations to a simple phrase. The examples were shown in beautiful laser-printed music notation: a pity none of them was played or sung to us.

Would it be possible to establish the APL representation of music as a computer standard? Are there any rivals to it?

## Life: Nasty Brutish and Short

*by E E McDonnell*
{ .byline }

The man whose life is discussed is John Horton Conway. ‘Life’ is the game with cellular automata. In APL it is possible to write functions to calculate the successive generations very concisely.

Donald McIntyre’s version manages to be both concise and easy to understand. Some are impenetrable. Only those with some interesting lesson for us were shown.

*[Photograph.]* Eugene McDonnell

Defining globals as ‘nasty’ and exhaustive testing of all possibilities as ‘brutish’, the author worked his way through a series of shorter and shorter LIFE programs ending with one only nine tokens long, which is certainly short (only twelve characters plus the function name and colon). The global is a vector of nested arrays each three by three. The point of the exercise was to show the importance of the new operators in APL. The nine-token solution uses both ‘cut’ and ‘rank’.

The whole was presented with a dry wit: the audience was far from solitary and nothing about the occasion was poor.

## Symmetries of the Firing Squad Synchronisation Problem Revealed in a Nested Array.

*by J Philip Benkard*
{ .byline }

The problem is to get a line of automata or soldiers all to fire synchronously after the order to fire is given to a soldier at one end of the line.

Each soldier can only communicate with his immediate neighbours. Plainly if all are to fire at once the message must be passed at least to the other end of the line and back again.

For example the message one way could be the count of the position of each soldier/automaton in the line, which could be stored by each of them and then used on receipt of the return message to begin a count down, one count per message time, to the firing time. This solution calls for many message types and rather complex automata – they must be able to count up to the length of the line among other things.

*[Photograph.]* J Philip Benkard

Phil Benkard presented a solution which works on unlimited length lines with twelve-state automata and a single message type described as a shoulder-tap. There are many interesting symmetries involved, not least that of the matrix used to determine the next state of each automaton from its current state and incoming messages. When the matrix is expressed as a nested array there is a large saving in space.

## Interactive Simulation Modelling using APL

*Tatsuo Aonuma*
{ .byline }

Prof. Aonuma described the use of APL in teaching management skills, especially in the use of simulation. He uses APL in 2 ways: first he gives all students 10hrs APL teaching so that they can do the basic statistical analysis; then he uses his simulation generator to let them play with complex dynamic models without the need for a high level of APL programming skill.

Typically a multi-period planning model can be devised, tested and run with only enough APL skill to define the relationships between the variables in the system. The simulation generator takes care of all the hard bits (rather like a spreadsheet, only much more flexible) such as detecting circularity, and getting the equations in the right order. There are lots of handy built-in functions to define lagged relationships, exponential growth and so on.

## Networking APLs

*Gary Sullivan (on Zeidner panel)*
{ .byline }

Gary described the process of making IBM chips as ‘a bit like etching a truck from a solid block of steel’. Typically there are some 300 stages in the process, and the same chip is often competing with itself for the same tool set at different stages. The challenge was to cut costs and improve quality; they needed an ‘expert systems’ approach as there was no well-understood model of the plant.

The system was described as a ‘proactive embedded’ expert system; it takes the transaction stream from the plant (some 240,000 transactions per day) and enhances this to yield a state array of the plant. This can be compared with the plan to locate trouble spots. The system uses both MVS and VM hosts, and PC’s to handle the interaction with the shop floor. It has improved tool throughput by between 20% and 80%.

## Plenary Session: The Past of APL

Ken Iverson gave the opening address, explaining that he would not repeat the credits already given to so many of those who had contributed technically to the development of APL but would try to cover those in other categories such as administrators, secretaries, organisers, teachers and do-it-yourselfers. The Vector reporter apologises for any names he missed.

Ken reminded us that when he began working with Adin Falkoff some years before implementation, APL was seen as a tool for developing and expressing thoughts.

*[Photograph: three men seated.]* Ken Iverson, Curtis Jones and Eugene McDonnell

Among the executives and administrators he mentioned A K Watson, who found resources for the work, John McPherson, who was a vice-president of IBM, and John Lawrence, the editor of the IBM Systems Journal through whose articles Larry Breed, R H Lathwell and Roger Moore were attracted to the project. Among secretaries and operators Colleen Conway was mentioned. The first conference organiser was Garth
Foster and the first course organiser was Al Rose who led on to teachers such as Linda Alvord. In Europe Reyner Cokeham and Yves Le Borgne, who attended the first course outside IBM which was at NASA, Per Gjerlov, Gustav Tollet and Timo Seppala were mentioned. Ken ended by quoting Fred Brooks, his co-author of “Automatic Data Processing”, who after spending some time in Australia said that the book “A Programming Language” was better known here than in the USA.

Neville Holmes then spoke about APL in Australia. He had learned APL in the early 60s from a Frenchman who had brought it back from the SRI. Then the Australian Bureau of Statistics adopted it for specifications. The Sydney APL Users Group was founded in 1977 and has had as many as 100 members; there’s also a Melbourne group. Neville hoped that APL 88, the Education Workshop and I-APL would make it possible to get APL into use in schools.

Dick Bowman, for the British APL Association, said that the Association had been set up by Romilly Cocking. It holds six meetings a year and publishes VECTOR – 128 pages – four times a year. The BAA ran “APL Business Technology 83” at Loughborough, APL 86 at Manchester and will run “APL-Ication” at Canterbury in Autumn 88.

Kyosuke Saigusa said that in Japan there were two groups. One is the APL Association, founded in 1977, which publishes an APL Journal, has 120 members and Ken Iverson as Hon. Chairman; it is rather academic.

*[Photograph.]* Kyosuke Saigusa

The other is the APL Club sponsored by IBM as part of its marketing program and with 200 companies, mainly users of IBM machines, as its members. It too has a magazine, called APL-Club. As IBM seems to be losing interest in APL, now would be a good time for the groups to amalgamate and consolidate their resources.

Marilyn Pritchard explained how the rules of the ACM had to be changed, with Alan Perlis’ help to allow the formation of Sigplan Technical Committee on APL or STAPL. She asked us to attend the SigAPL plenary later that afternoon if we wanted to know more about its current state; at present it is losing members at the rate of 100 a year and is spending more than its income. It has 1600 members and $30,000 in the bank so eclipse isn’t imminent. Linda Alvord has taken on the job of recruitment and re-recruitment.

*[Photographs.]* Marilyn Pritchard; Gitte Christensen

Gitte Christensen began APL in 1968 at a summer school taught by Iverson. By 1973, Denmark had five APL groups and the highest density of APL use in the world. In 1978 the APL subgroup of the Danish Data Processing Association was formed and it holds meetings and conferences and will host APL 90 in Copenhagen. The Danish APLers are working hard to get APL into schools and hope, with I-APL, to succeed. They are greatly increasing their emphasis on “ground level” APL and on helping people to use APL better.

Curtis A. Jones said the Bay Area User Group was formed by the people who ran APL 81 in San Francisco. It has meetings at the Sharp offices in Palo Alto. Membership statistics are untrustworthy but the group may be growing; it is certainly adding officers as now there is a proper committee, whereas last year there was only Curtis Jones himself.

Eugene McDonnell spoke about the past of the standardisation effort. The original impetus arose on one of Garth Foster’s courses when Clark Wiedmann asked “What is the result of this expression on your system?” In practice, first APL/SV and then VS/APL were the definition of APL, but it was unacceptable to have a notation defined by the results from an implementation of it. In 1975 at Pisa an attempt was made to define APL in Backus normal form. IBM tried to produce an internal standard published at APL 79.

This may have been what sparked off Raymond Tisserand to try to get ISO to take over the IBM standard. That attempt roused the other US manufacturers to make great efforts to have the standard set via ANSI. There have been 29 meetings of the committee called X3; the first 24 or 25 produced the standard which is soon to be the ISO and for which Raymond Tisserand, Alex Morrow and Clark Wiedmann were given the outstanding
achievement award at APL 86. Since then meetings have been doing preliminary work on a standard for extended APL. The chairman is currently Lee Dickey. Gene is now Recording Secretary of the ANSI group.

## SigAPL Plenary Session

Marilyn Pritchard opened the session. SigAPL’s officers are:

<p style="margin-left: 2em">Chairman Marilyn Pritchard<br>Secretary Garry Helzer<br>Treasurer Andrew K Dickey</p>

The budget is $45,000 p.a. and last year it was over-spent. The fund balance peaked at $65,000. Membership is now declining.

Linda Alvord spoke about halting the decline and asked for help in bringing back old members who had allowed their subscriptions to lapse.

Lee Dickey spoke about Quote-quad. Each year it produces three issues and the proceedings of the conference as a fourth. Recent editorial initiatives have produced some “monolithic” issues such as Iverson’s Dictionary of APL. Quote-quad needs more letters – the ‘year’ contest produced the record response so far. It also needs a new products editor – any volunteers? So far 189 algorithms have been published and when the total reaches 200 Lee hopes to publish “200 Algorithms from Quote-quad”. He ended by asking for contributions which are acceptable on floppy disk, via bitnet, usenet, csnet, edunet or you-name-it net or even on paper.

Lynne Shaw spoke about conferences. The next will be a workshop at Syracuse 15-20 August 1988. APL 89 will be in New York in July. IFIP 89 will be in August/September. APL 90 will be in Copenhagen. Conferences for ’91, ’92 and ’93 are not finally fixed but ’91 may be in Baltimore and ’93 may be in Los Angeles.

## Function Rank

*Bob Bernecky*
{ .byline }

This was for me (ACDS) one of the most enjoyable, and most frustrating, talks at the whole conference. The ideas Bob described are by no means new, but this was a superbly coherent exposition of just how you can use the Rank operator to simplify and improve your code. The examples he gave were all things I felt I could immediately take home and use.

The frustration arose from the fact that I have no chance at all to use the Sharp APL system in my day to day work! OK, I can play with their excellent public domain PC/APL, but I want this Rank thing, and I want it now!! Why did it make such an impact? I shall try to summarize as briefly as I can.

*[Photograph.]* Bob Bernecky

The first major insight was to see that the principle of scalar extension could quite easily be applied to functions of higher natural rank. For example Domino applies naturally to rank-2 arrays; if it is given a rank-3 array it should simply apply itself to each rank-2 subarray, and re-assemble (laminate) the results into a set of planes. For some functions, such as ravel, there is no natural rank, as it applies equally well to any array.

What the Rank operator does is to restrict it to the rank that you want. For example “ravel at rank-2” on a 2 by 3 by 4 array will yield a 2 by 12 result. It has ravelled the rank-2 arrays and re-assembled the result!

Of course you can do the same with defined functions. Say you have a simple routine WCOUNT to count the words in a text vector; to count the words in each row of a text matrix you just do “WCOUNT at rank-1” to the array. It does each rank-1 object, and assembles the resulting scalars into a vector of results, with one element per line of the original matrix.

The thing I really liked about all this is that it works without any magic tricks using enclosed arrays. In other words you can use it to cut out loops, and generally to simplify your existing code, operating on your existing data-structures. See the APL88 proceedings on page 39 for a lot more examples.

## Data Base Management with APL2

*Stockbridge and Eisner*
{ .byline }

This talk discussed the transition from a home-grown database to the use of DB2 via AP127. It was interesting in the way the authors had ‘rediscovered the past’ in finding that simple arrays (one variable per column of data) offered a far lower storage overhead and a dramatic performance improvement, in the access to DB2 data.

They had expended a deal of effort getting round the SQL restriction that tables are updated one row at a time. Compared with the power of the SQL ‘Select’ command, the authors had found it really frustrating to resort to a sequential serial process in the APL workspace (rather than having AP127 take care of the looping internally).

Their solution to reducing the overhead was to define a separate update table, put the changes on this, then delete the affected rows from the base table and insert the new versions at the end. They had defined a detailed 13-step procedure, involving flags to ensure integrity at all stages, to control this. See APL88, page 314 for all the details. There conclusion was that it worked, and had saved a lot of CPU cost, but they would much rather not have had to do it!

## Application-SQL Interaction

*Stephen Deerhake*
{ .byline }

This paper was concerned with a way for the inexperienced SQL programmer to access DB2 effectively, and hence to isolate SQL from the APL application code. Typically it allowed APL to get data easily from 5 or 6 tables, fiddle about in the workspace, and reflect the changes back into the database.

The SQL knowledge needed was limited to ‘Select …’, and the APL2 knowledge to arrays of vectors. As with the above paper, the interface handles the update problems for you, and the same comments apply “Insert and delete are easy …. update is a real pig!”.

Again some limitations in SQL were apparent; there is no way to get a random selection of rows without first retrieving all the keys and then picking the randomly chosen rows with a second ‘Select’; there is also no way to get the first (or last) 10 matching entries.

The final comment (in answer to a question) was that in a single user system, this all worked very nicely, but “if you get into a multi-user system things get real interesting – fast”

## Plenary Session: The Present of APL

The purpose of this session was to bring out the differences in the various interpreters, and (more importantly) why they had been designed that way in the first place. In general I felt that the speakers achieved this aim rather well, and that this was one of the more successful joint sessions of the conference.

*[Photograph.]* James Wheeler

### James Wheeler (STSC and APL\*PLUS)

STSC’s objectives for APL are:

1. To provide a compatible APL system across most popular computing environments. IBM mainframe (TSO/VM); DEC Vax (VMS/Ultrix); IBM PC; Mac.
2. To build what the users want. They use ‘focus groups’ and market research to drive frequent updates of the system.
3. To supply a computing environment, not just the APL language. This means decent editors, file systems and good interfaces to the host machine. These are provided with quad functions, rather than APs, for speed, reliability, ease of coding and more readable programs.

They have moved to ‘2nd generation’ features, but these will not be available under MS DOS or on the Mac. It is no longer the obsolete NARS experiment, but is now based on the same axiom system as Dyalog and APL2. They provide similar functions and operators, as well as the ‘strand’ notation. There are some differences in the detailed syntax of this, but the long-term plan is for convergence with APL2.

### Jim Brown (IBM and APL2)

Some of IBM’s objectives for APL2 were:

- all functions are equal. They can all be applied with operators, even FORTRAN ones.
- you can assign whatever you can select.
- connectivity. You can use APL2 alongside all the other things on the system. SPF, DB2, FORTRAN and so on. Lets let all the people who like these things find out about APL!
- portability. SAA does not include APL, however there are experimental PC and RT versions of APL. No sign as yet of any interest from system 36/38 users

Jim suggested that the attitude of IBM to APL is continually changing; just at the moment they have found that APL sells machines. “That is why I’m taking a year in marketing!”

*[Photographs.]* Jim Brown; Paul Chapman

### Paul Chapman (Himself and I-APL)

I-APL is portable and small; it will run on the sorts of machines you find all over the world. The extensions to the ISO standard are minimal, except for direct definition which is built in to the product. Interfacing to the environment is kept to a minimum so that I-APL will run the same way on all machines.

## Panel session on “APL Extensions in Perspective”.

*Panel: James Wheeler, Bob Bernecky, Paul Chapman, Phil Benkard, Martin Gfeller, Eugene McDonnell*
{ .byline }

David Ziemann was in the chair and asked each member of the panel to make a preliminary statement about his objectives for his interpreter and his criteria for selection of extensions.

*[Photograph.]* David Ziemann and James Wheeler

James Wheeler said that the ISO standard was OK for portable algorithms but not for portable applications. In order to be able to offer customers portable applications STSC had written their own internal standard. The extensions STSC had added were mainly to improve the power and ease of use for commercial programmers and the main route that they had chosen to take for non-structural enhancements was the quad function. The nested array enhancements were largely compatible with APL2. STSC were moving towards full compatibility with APL2.

*[Photograph.]* Eugene McDonnell, Martin Gfeller, Philip Benkard and Paul Chapman

Bob Bernecky said that Sharp APL was ISO and ANSI compatible. Extensions to the notation were to improve its value as a tool of thought, for example the ‘cut’ operator. Sharp’s main effort was put into changes which would bring benefits to their customers. Some of these were concerned with improvement of performance and with facilities for measuring performance and making faster ways of doing things accessible. Recent additions have been the line timer and provision for hybrid machine-code/APL functions. A second area of improvement is in the size of system that can be handled – to some of their customers a system with a thousand users on line at a time is small! Eugene McDonnell interpolated that Sharp also wish to include some of the good things from APL2.

*[Photograph.]* Jim Brown and David Ziemann

So Jim Brown began by saying that he would like to include some of the good things in Dictionary APL, such as ‘rank’. He spoke about the advantages of using PC implementations as front-end systems to the mainframe; programming development could be carried on without causing delays to mainframe work (or being delayed by it). He spoke of extending the number of uses for which APL2 was seen as a suitable language. For example there was to be a conference next August on AI and APL at Syracuse, where he would like to see us all. There are plenty of places where the current picture of APL2 is not complete and he is also exploring these, for example what would a nested left argument to ‘reshape’ do? The other area of possible expansion is arrays of functions about which there have been several papers at APL conferences.

Paul Chapman said that he was the only author of an ISO conforming APL interpreter who had used the ISO draft standard as his blueprint. He believed that I-APL was the only APL which could pass all the conformance tests. I-APL had to be conforming because it was intended for use in schools who would find an international standard product much more acceptable and might be reluctant to endorse any particular vendor’s product by adopting it for educational use.

*[Photograph.]* Paul Chapman

The enhancements to the standard he had included were therefore few and only those which were common and very likely to be agreed as part of the core of the next standard such as replicate and monadic grade of character vectors.

Direct definition was a conforming enhancement: it replaced what would otherwise be error messages. It had been included for its elegance and because so much educational writing about APL used it. He had also taken one enhancement out, after it was working and tested, because it would have made programs which used it incompatible with other APLs.

Phil Benkard said …….. your reporter was so fascinated he forgot to take any notes and it is now completely forgotten. Let this be a lesson: either issue a written account of what you say or put in some dull patches in which people can make notes. (Perhaps reporters should take tape recorders).

Martin Gfeller arrived late because, as he said, the Pacific had taken his glasses and he had had to get another pair at very short notice (half an hour) from an optician in George street. In Martin’s opinion by the year 2014 we would probably not be using a version of
APL which was upwards compatible from what we have now. He thought we were a bit too satisfied with what we have.

Eugene McDonnell spoke about the past achievements and the current intentions of the standards group. He listed some of the proposals made to the group to show how much they had to consider. They had chosen to exclude anything which was not a consistent extension, not commonly available, not stable or which was machine dependent. The purpose of the group is to make programs and programming skills portable and to extend the applicability of APL. It is, as he said, too much work. The next meeting is at La Hulpe in Belgium in April 1988.

### Some comments from the audience:

Maurice Jordan, implying that APL had fallen so far out of the mainstream that it was not even used for things it would be good at, asked “Why isn’t relational database theory expressed in APL?” He didn’t get any answer.

Jim Lucas felt that Maurice was unfair to the extensions of APL. They could do the job and the reasons they were not used were not related to the language standards. He also asked Bob Bernecky whether ‘cut’ was complemented by a ‘paste’. Bob replied that it was and the function was called ‘raze’.

Ray Polivka mentioned that at Minnowbrook there had been a transfer standard to allow APL code to be passed from one machine to another and asked if it was still alive. Bob Bernecky replied that the ISO standard has the extended transfer form as an appendix. Ray then asked whether all manufacturers would have it, and although not a direct answer, Eugene was able to tell him that it was approved in the committee by a vote of eleven to zero.

Tom Pritchard spoke about simplicity and felt that this was a desirable aim which some extensions seemed to rate not highly enough.

Jim Lucas complained that this was too simplistic. English has no case endings, Rumanian has cases: but which is simpler depends on arguable criteria.

Dave Ziemann had asked the panel members to supply him with questions which they would have liked to ask if they had been in the audience. He read out the following: “When are you guys going to standardise quote-quad input and output?”; “What are you doing to reduce strife between versions of APL?”; “When you consider an enhancement what does the enhancement have to be for you to include it?”.

Both Jim Brown and Eugene McDonnell answered the last question; for Jim it had to be Dynamic and Array; for Eugene it had to be Parallel and Equipedal.

Rob Hodgkinson asked whether it was possible to use a common modelling system to allow each vendor to review other people’s extensions. Was there, for example any chance of placing the Sharp, STSC or IBM development models into a software library?

## Shadows Cast by Buildings.

*Dr Warren Julian*
{ .byline }

Professor Julian has a long-standing interest in daylight and artificial lighting. He finds APL very suitable for this work – things like multiple reflections work out cleanly. He has used APL since 1972, introduced it to students as soon as it was available and has been a member of the Sydney APL Users Group since it was established.

He was disappointed that so few people were interested in specifying their own systems. The work on shadows grew out of his keenness do specify new work and his interest in lighting. The effect of a building on the microclimate of adjacent land is complex.

*[Photograph.]* Warren Julian

In Sydney there are many new tall buildings each of which adds a new pattern of shade. The effect at different times of day and year all may be important when it comes to planning laws and appeals from neighbouring landowners. It is worth a lot off effort negotiating about about exact position, shape and size to avoid legal processes.

He reviewed how the system works. It distinguishes the shadows of interest in solid from incidentals which are hatched. He explained the way the printed functions work together. Since the system uses latitude and longitude, it is not restricted to Australian use.

The parts of the system which it was hardest to get working were those concerned with Macintosh facilities. The APL is complex but it is logical and consistent, lends itself easily to correction and gives good clues about what is wrong. Getting the Macintosh tricks to work robustly ought to have been easier but lacked these advantages.

## Crystallography

*Donald MacIntyre*
{ .byline }

Fortunately, the organisers of APL 88 had had the foresight to set a videotape running for this entire session. I hope we can successfully transcribe enough of it to make sense in a future VECTOR; otherwise we shall just have to twist Don MacIntyre’s arm until he lets us have a written copy!

In essence, this was a marvellous paper, and was superbly delivered with the aid of numerous props (mostly assembled out of ping-pong balls). His use of APL to express many of the fundamentals of crytallography was wonderful to see. Just to give you a flavour:

<p style="margin-left: 2em">if you make an 8-row triangle out of ping-pong balls<br>&nbsp;then the number in each row is <code>+\8⍴1</code>;</p>

<p style="margin-left: 2em">if this is the plane of a close-packed tetrahedron<br>&nbsp;then there are <code>+\+\8⍴1</code> balls in each successive plane;</p>

<p style="margin-left: 2em">if you make a crystal out of successive tetrahedra,<br>&nbsp;then there are <code>+\+\+\8⍴1</code> balls in each tetrahedron!</p>

The tape of this talk is available from the APL 88 committee for the cost of copying and postage; otherwise we shall do our best to give a much fuller account in VECTOR 5.2. Watch this space.

## Notes on the Exhibition

This was very much a home-grown affair. The IBM and STSC stands were the main vendor represention, while C.A. Read Associates and Lois Hill (Interactive Barchart Scheduling) were available to demonstrate their APL software packages.

From the general APL community point of view, the two most interesting stands were placed handily opposite one another: IBM running APL2/PC on a PS/2 Model-60; STSC running APL\*PLUS/386 on a PS/2 Model-80.

*[Photograph: two men at the APL2 stand.]* David Selby with Paul Chapman

The IBM offering may never see the light of day as a commercial product, so this was a fascinating chance to get in and ‘have a go’. STSC on the the hand are committed to a mid-88 launch of the 386 product, so this was really a preview, rather than a once in a lifetime opportunity.

The thing that was amazing everyone about the IBM offering (including the author of I-APL pictured above!) was how on earth you get a complete APL2 interpreter into roughly the same space as APL\*PLUS/PC. The first thing I tried in a clear workspace was ⎕WA; sure enough back it came with 397136, so far so good! The basic interpreter speed (`FN 1000` = 13 sec) was very comparable with other APLs on similar hardware; the ⎕AV looked pretty ASCII (although I noticed that many of the line-drawing characters had been reused for APL symbols); the session manager was very mainframe-ish (no type-ahead and a tendency to say ‘INPUT’ while it was still running).

Some bits of APL2 were missing, such as stranded assignment. It was also possible to do some rather odd things like `'⎕IO←'A' 'B' 'C''`; after much persistent trying David Ziemann finally managed to crash it with a depth-4219 enclosure of ,1. I don’t think this represents a serious problem in real life! In summary, this had all the makings of a really good APL2 for small machines. If IBM choose to market it I’m sure a lots of mainframe APL2 sites will take it on as a development/training environment, and possible as a serious application delivery vehicle.

APL\*PLUS/386 is a full implementation of the STSC mainframe APL product, with all the PC enhancements included. As its name implies, it is specific to the 80386 chip and uses the full memory addressing capability available. Typically you would run in
workspaces of 2 - 4 Mbytes. Upward compatibility from APL\*PLUS/PC was promised, although most of the ⎕POKE commands were not implemented in the version on display.

There is very little I can say about this APL, except that it worked, and worked remarkable fast. `FN 10000` ran in 27 sec (note the extra zero!) and floating point appeared to approach mainframe speeds. I can think of few mainframe applications which would not transfer to this environment and show a marked increase in overall execution speed. In particular it re-inforces my view (VECTOR 4.3 page 43) that the ‘virtual workspace’ of APL\*PLUS/PC Vn7 is a temporary aberration, and that the 386 implementation is the real way forward.

## Closing Plenary: A Commentary on APL Development

*Ken Iverson*
{ .byline }

As Ken’s paper was not included in the APL 88 Proceedings, we have asked his permission to print it in full in VECTOR; I am delighted to say that he has agreed to let us do this, with the agreement of the editor of Quote-quad who clearly had first refusal on all APL 88 related material. This way, you will have a chance to see the complete text as Ken wrote it; so there would be little point in filling up this VECTOR with extensive notes on what we think he said!

The main topics covered were: the proposed ‘Yoke’ operator, which produces the conjunction of two functions, and its use in expressing the common set manipulations; function arrays; the use of the ‘box’ function as a universal scalar encoding.

## Closing Remarks: The Future of APL

*Anthony Camacho*
{ .byline }

Most children are prone to asking their parents questions like “What are you doing, Daddy?”; maybe there is some significance in the fact that in the Camacho household the question was more often phrased “Daddy, what are you <u>trying</u> to do?!”. Anyway, let’s look at some of the things the APL community might be trying to do:

- recover old members. Obviously a valid activity, but a purely short-term aim.
- recruit new members among APLers. Another valid aim, but surely we wouldn’t be happy even if we achieved 100% success.
- try to get the computing community to use more APL and less FORTRAN, PL/1 and the rest. Unfortunately we aren’t going to get the DP department to replace COBOL, which from their point of view probably does a better job anyway. (At this point there was a vigorous interjection from the audience – Joey Tuttle – along the lines of “Stop apologising for APL!”)
- increase the number of people using APL. What we need is people aged 20 who already have 10 years APL experience! There is only one way to do this; get APL widely used in education.

If you start by regarding APL primarily as a Programming language, then the fact that it also happens to be a notation gives you very little. On the other hand if you regard it first as a notation, then it is quite extroadinary. How many other notations have been used by so many people in the lifetime of their author? APL has one quite overpowering advantage – it can be executed directly on a computer!

Here then is one final thing the APL community might try to do – set about replacing conventional maths notation. When the ‘Ant and Bee’ books in the Infant schools have APL in them, we will have succeeded.

## Postscript

At the final plenary session Neville Holmes paid tribute to the great efforts of Rob Hodgkinson, John Searle and Chris Craddock who had made APL 88 such a success. The audience obviously agreed. As the applause was dying down, Dave Weintraub remarked in a loud voice that he didn’t think that Neville had been properly thanked yet.

Applause began, and went on and on as gradually the audience got to its feet to give Neville a spontaneous standing ovation. It was a good way to end.
