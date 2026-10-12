---
title: APL Standard Update
authors:
- David Ziemann
volume: '6'
issue: '2'
page: '118'
unindexed: true
transcribed: 'from page images of VOL.6-NO.2-OCTOBER-1989.pdf, pages 120–124 (printed 118–122); Claude, 2026-10-12'
review: draft
tags:
- standards
- language design
queries:
- "Contents line “APL Standards Update”; the printed heading is “APL Standard Update”, “by Dave Ziemann (as convenor of BSI APL Standards Panel)”."
- "The addresses of ISO, the Department of Trade and Industry and BSI Standards, with the named officials, are kept as organisations’ addresses."
- "Kept as printed: “enhanced facilties”; “GCD and LCD”; “heterogenous arrays”; “droppped”; “humourous”; “nominated the \"Principal Expert\" is entitled”."
---

*by Dave Ziemann (as convenor of BSI APL Standards Panel)*
{ .byline }

This report primarily covers events that occurred at the ISO meeting held in Princeton University, New Jersey, USA from July 31-August 3rd this year, just before the APL conference in New York city.

The four day meeting of Working Group 3 (WG3) attracted fourteen delegates from Belgium, Canada, France, UK and the USA. Two BSI (British Standards Institute) representatives attended the meeting, Paul Chapman and myself. The meeting was convened by Lee Dickey. Ken Iverson, now retired from I P Sharp Associates was a notable attendee.

The main agenda item was of course the Extended APL Standard, although the status of the original APL Standard, affectionately known as IS8485, was also on the agenda.

## The First APL Standard

What news of IS8485 then? Lee Dickey had submitted the document to Sub-Committee 22 (Programming Languages) in Geneva for "International Standards processing" some time ago. Although this at first appears to be a technical term for a bureaucratic black hole, it now seems that we are in imminent danger of having an APL standard. If there are no hold-ups, we can expect publication before the end of this year, apparently.

If you want to get hold of this 275 page document, request document IS8485 from:

> Secretariat Central ISO<br>
> Case Postale 56<br>
> CH1211 Geneve 20<br>
> Suisse

The standard will be published in English and French, so you should state which you want. A price is not currently available.

Once IS8485 is published as an ISO standard, it can be "endorsed" or "adopted" by the national standards bodies, such as the BSI. "Endorsing" effectively means that the national body establishes a pointer to the international standard, and you have to send to Geneva to get a copy, whereas "adopting" means that it is accepted as a national standard and printed locally.

The original text of IS8485 is currently being transferred from Script into Tex, a project which has been funded by SIGAPL and more recently by I P Sharp Associates. This will bring the document under the control of WG3 once more, and should make work on a new document much easier.

## The Extended APL Standard

For some time the ISO group has been struggling with the problem of how to resolve some fundamental differences in the way that certain enhanced facilties should be standardised. In particular, nested arrays (where an array can contain items other than simple scalars) and the reduction operator are subjects upon which effective agreement cannot be found.

At the ISO meeting the BSI submitted a paper which summarised and enumerated the logical possibilities open to WG3, and suggested that WG3 reconsider its direction. The choices open to us are:

1. Standardise the intersection of the extended facilities in the different dialects
2. Standardise the union of facilities by a very general approach
3. Standardise a new dialect of APL which combines desirable facilities from each dialect
4. Standardise multiple facilities, allowing implementations to select the preferred approach
5. Pick one approach to standardise (essentially APL2 or Sharp APL)
6. Develop two distinct extended standards
7. Postpone work on the Extended APL standard

None of these possibilities is particularly attractive, each resulting in severe technical, political or practical difficulties.

Although possible, compromise solutions involving the combination of facilities, such as in option 3, damage the consistency and synergy of the language, and would result in a standard language which does not actually exist. It has long been the policy of the working group to standardise on the basis of what exists rather than to invent, wherever this is possible. But standardising from what exists in two distinct self-consistent dialects can produce a monster without the consistency or usability of either one.

A standard which includes both APL2's nested and Sharp's boxed arrays, for example, would be a standard for a language which no-one has used, and perhaps one which no-one would want to use. The behaviour of all the associated primitives in one school would have to be carefully defined on arrays of the other school, and vice versa. Even if it were possible, the vendors could not afford to change their systems to conform to such a standard, and the document would then serve little purpose.

## A Way Forward

Work on the standard proceeds by discussing and voting on proposals received by WG3. We decided that proposals should be as near "standard-ready" as possible, ie they should be in the same format as pages in IS8485. Before the Princeton meeting many topics had already been rejected by agreement or vote, although several contentious proposals still remained.

After discussion WG3 decided to prepare two publications, a Supplement and a Technical Report. Our main effort, a Supplement to the existing standard, will contain only those proposals upon which agreement has been reached. The Technical Report will describe those topics which have been proposed, but on which consensus has not been reached.

During the course of the meeting twenty-six topics were identified for likely inclusion in the proposed Supplement, and nineteen topics were identified for likely inclusion in the proposed Technical Report. Two topics were dropped from further consideration because proposals in the appropriate format had not been received.

The topics currently marked for inclusion in the Supplement are: replicate, grade extensions, without, underbar/overbar in names, ambi-valent defined functions, ambi-valent primitive functions, transfer form (`⎕TF`), defined operators, canonical representation of defined operators, locking of defined functions and operators, shared variable extensions to `⎕SVR` and `⎕SVQ`, `)NMS` and `)OPS` system commands, N-wise reduction, comma-bar, nub, left and right, GCD and LCD, commute, complex numbers, formatting complex numbers, heterogenous arrays, fill-items for heterogenous arrays, function rank operator, alpha and omega as names, event handling (`⎕EA ⎕EM ⎕ES ⎕ET`) and component file cover functions.

The topics marked for inclusion in the Technical Report are: reduction, nested arrays and fills, enclose/disclose/box/open, formatting for nested arrays, pick, partition, depth, link, enlist, strand notation, match, primitive operators applying to non-scalar functions, compose, dual, first, each, national language characters, function rank in standard metalanguage, function assignment.

The two topics droppped from further discussion were `⎕FMT` and the "find" function for string searching.

## Future Issues

It is unfortunate that the projected Supplement does not include any nested or boxed array extensions, although this is ameliorated to some extent by inclusion of the function rank operator. Many people feel that an extended standard should include nested arrays, whereas others think that the field is still undergoing evolution, and that it is too early to standardise. No doubt this subject will arise again.

Another interesting area is event-handling. Where the model in the standard signals an error, a conforming implementation may replace that error behaviour by some other behaviour - this is the "consistent extension" mechanism by which implementors may add facilities to their conforming systems. Therefore an APL program cannot strictly rely on this error being signalled, and so such a program is deemed non-conforming.

The whole purpose of including the (APL2-style) event handling system functions in the standard is to allow users to trap events and handle them, so currently we have the strange situation that a facility defined in the standard cannot be used by a conforming program! Clearly something will have to change in the next standard.

The meeting also agreed to liaise further with WG2, the ISO committee involved with the standardisation of character sets, and we will be sending them a list of APL characters for inclusion in the new multiple octet character set standard.

Another sad divergence between the APL2-school and the Sharp approach is the reduction operator, and therefore inner product. In APL2-type systems the primary definition of reduction is on vectors, the function being applied between the items of a sub-array of vectors. The Sharp philosophy is to apply the function between the items of a vector of sub-arrays.

In addition, the APL2 definition involves an implicit enclose operation, which means that the result is often nested, whereas the Sharp definition does not involve enclosure, the result being simple. The enclose allows the APL2 definition to preserve the familiar rank-reducing identity, but in the Sharp view that effect was merely due to the domain of the operator being restricted to scalar functions, and is not a general identity. Perhaps for that reason the true Sharpie prefers the name "over" to "reduction". I heard one Sharp advocate offer the opinion that Bob Smith, the inventor of STSC's Nested Arrays Research System, had been "imprisoned by the beauty of the identities he discovered".

Of course, none of these differences manifest themselves in old-fashioned APL, but only become apparent with the requirement to generalise operators to non-scalar functions.

Standards meetings evoke a mixture of feelings; they can be extremely fascinating, sometimes boring, and very often humourous. When faced with a 6-3-3 vote to include the function rank operator, the convenor was not sure that this indicated consensus. So a metavote was agreed, and we each picked a number greater than 50 and not greater than 100, the percentage which we thought fairly represented consensus. We agreed to pick the median number, and the result was 70%. A revote was then called for the function rank operator, and this time it passed 8-3-1.

## The Timeline

The next scheduled meeting will take place in August 1990, somewhere in Europe. If sufficient progress on the Supplement has been made by February 1 1990, then an additional meeting will be scheduled for April 1990 in Waterloo, Ontario.

It is hoped that the new document will reach the first Draft Proposal stage by March 1991.

## UK Involvement at Risk

Travel to International Standards Organisation meetings for BSI representatives is funded in this country by the Department of Trade and Industry. One representative, nominated the "Principal Expert" is entitled to a fixed amount based on the location of the meeting. For example, for the Princeton meeting the figure was £500, enough to cover a cheap air fare to New York. Accommodation and living expenses are not paid; the expert must rely on a very generous employer or bear the cost directly.

All BSI Technical Committees have now been informed that future claims may not be met, and those that are may have to be at a reduced rate, possibly no more than 50%. Perhaps as many as nine out of ten claims will be rejected.

It therefore looks likely that future UK involvement in ISO APL standards meetings will not be possible. If anybody has any complaints about this they can write to:

> Mr Alec Berry<br>
> Dept. of Trade and Industry<br>
> Kingsgate House<br>
> 68-74 Victoria Street<br>
> LONDON SW1 6SW

with a copy to:

> Mr Tony Valvona<br>
> Business Support Group<br>
> BSI Standards<br>
> 2 Park Street<br>
> LONDON W1A 2BS
