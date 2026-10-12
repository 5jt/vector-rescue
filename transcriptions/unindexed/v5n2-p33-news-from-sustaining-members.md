---
title: News from Sustaining Members
authors:
- Cathy Dargue
volume: '5'
issue: '2'
page: '33'
unindexed: true
transcribed: 'from page images of VOL.5-NO.2-NOVEMBER-1988.pdf, pages 35–37 (printed 33–35); Claude, 2026-10-12'
review: draft
tags:
- APL community
- implementations
queries:
- "Printed byline “Compiled by Cathy Dargue”. The lower half of printed 35 is blank; the APL Product Guide begins on printed 36."
- "HMW Computing: the company’s office number is kept; the directors’ out-of-hours home telephone numbers are omitted."
- "Kept as printed: “as well improving”; “Unx”; “The advanced features, efficiency and compatibility … is encouraging”."
---

*Compiled by Cathy Dargue*
{ .byline }

## APL People Ltd

The agency business continues to flourish, with an increase in both consultancy work and placements. Things are certainly looking very healthy at the moment for those seeking a job move, with new vacancies coming up all the time and not enough people to fill them! The range varies tremendously, from openings for junior staff to prestigious new opportunities in the city for highly experienced APLers (offering city rates too!).

The new office premises are working out very well and we have had to take on another member of staff to cope with the ever-increasing workload.

In addition, we have set up a new division called 'IN-FOCUS', to handle consultancy work in the fourth generation language, FOCUS, and already have a number of FOCUS contract programmers available.

With 1992 fast approaching, our next aim is to concentrate on Europe and the States. We have of course, already done a certain amount of business abroad, both finding people jobs overseas and now with our first contract outside the UK, and we intend to build on this over the forthcoming year or so.

## Dyadic

Dyadic is pleased to announce a new screen manager for Dyalog APL. The new screen manager is designed to allow developers of APL applications to provide a state-of-the-art interface for their users. It provides facilities for pop-up/pull-down menus, context-sensitive help, spreadsheets, validation, scrolling and even animation.

The screen manager is implemented using a new system variable `⎕SM` (Screen Map) and a system function `⎕SR` (Screen Read). `⎕SM` is a nested matrix which defines a form: each row in `⎕SM` represents a field; each column an attribute such as field contents, position, window size, colour and so on. Field contents can be character or numeric arrays (or even another form) which scroll vertically and horizontally in the window defined for them. When the contents of a field are scrolled all other fields in the same vertical and/or horizontal scrolling group are scrolled in parallel.

Whenever you assign a value to `⎕SM`, the change is immediately reflected on the screen. Thus you can dynamically change contents, position, colour and appearance of fields to produce animated effects. The system function `⎕SR` allows the user to interact with the screen, and edit the contents of the fields. Changes in the data are directly reflected in `⎕SM`.

Pop-up menus and help screens can be implemented simply by localising `⎕SM` in a suitable function. The local definition of `⎕SM` is overlaid on top of whatever is on the screen at the time, and automatically disappears when the function exits.

Dyadic believes that the use of a system variable to represent the screen is a powerful and natural extension to APL. The new screen manager is currently on Beta Test and is expected to be on general release in January 1989.

## HMW Computing Ltd

HMW Computing Limited have been working on "4XTRA" our front end Foreign Exchange Dealing and Position Keeping System adding facilities to enable overall management analysis across dealing positions as well improving our graphical displays of trading data.

HMW Computing Limited have also launched a new employment service for the APL community 'HMW EMPLOYMENT LTD.' This complements the services we currently offer.

The directors of the new company, Valerie Lusmore and Stan Wilkinson have both been involved with APL since the early 70's and can offer an unequalled service to people looking for APL personnel as well as APL technicians looking for a career change or even contract work.

In line with HMW's philosophy we will also be using the employment business to offer a service for other areas in computing such as Oracle, Focus, JSP Cobol etc.

To find out what we can offer, please call Stan or Val on 01-353-4212 or write to us at the address on the back cover. If you would prefer to phone out of office hours Stan's home number is [omitted] and Val's is [omitted].

## Cocking and Drury Ltd

Several new consultants have joined us in recent months, bringing with them more experience of APL systems in practical business situations. Rossy Norman, Peter Merritt and Christian Jensen have joined as Consultants, and Clive Hibberd as a Senior Consultant.

Interest in the APL\*PLUS Mainframe interpreter and Compiler software continues. The advanced features, efficiency and compatibility with the PC, Unx and Dec VAX counterparts is encouraging its use as the strategic mainframe APL for the future.

The User Command Processor feature of release 6 is proving popular with customers. It allows libraries of programs to be accessed as if they were always part of the workspace, giving productivity and efficiency benefits when utilities are standardised and centralised.

Performance trials of the new APL\*PLUS II system for 80386 machines (pronounced 'two-system') are proving very successful; APL\*PLUS PC features show speedups of between 1.5 and 30 times, with intensive mainframe applications being matched and even outperformed by the II system.

The II system imposes no artificial limits on array or workspace sizes, so you can go as high as the installed memory; 15 Megabyte workspaces are now a reality. The second-generation productivity features such as nested arrays, generalised operators and the multi-object ring-editor all proved very popular at the recent APL-ication conference.

Only Cocking and Drury include one year's free upgrades and support in the APL\*PLUS II system purchase price.

Demand for training courses has increased recently, with in-house APL2 and System Design courses being especially popular.
