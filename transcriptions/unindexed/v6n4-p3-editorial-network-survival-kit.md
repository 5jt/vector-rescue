---
title: 'Editorial: A Network Survival Kit'
authors:
- Adrian Smith
volume: '6'
issue: '4'
page: '3'
unindexed: true
transcribed: 'from page images of VOL.6-NO.4-APRIL-1990.pdf, pages 5–6 (printed 3–4); Claude, 2026-10-12'
review: draft
tags:
- development practice
- APL community
queries:
- "Kept as printed: “A:;B:;C:;D:”; “a Vax in computer room”."
---

*by Adrian Smith*
{ .byline }

Did you ever think how comfy your mainframe is? At the Association's March meeting, we had an excellent outline of Sharp's LOGOS environment, where you can develop code in a co-ordinated way, and have it automatically copied into all the affected applications at the press of a key. LOGOS protects you by retaining old versions of everything you change, and it encourages a professional attitude to documentation, change-journals and so on.

I don't pretend that I have anything approaching this at Rowntrees, but at least when I change a mainframe utility function, it gets automatically copied into any workspace which uses it. We also put all our users through a common startup workspace, so we can easily )DROP old CONTINUE workspaces, check on frequency of usage, warn people about storage limits, and so on. At Christmas, everyone gets the trotting Reindeer ... yes, you can do animations even in GDDM!!

Now contrast this with a bunch of APLers developing applications on PCs. Obviously, the PC comes equipped with similar utility workspaces, but what happens when I need to fix a bug, or ship an enhancement? Do I trot round with a floppy disk, wait till the PC is free, and simply copy the .AWS or .ASF files over? Fine for development aids (as long as I remember to do it), but what about all the runtime workspaces out there? I know who I gave them to, but PC applications have a habit of spreading themselves!

In summary: once you give a PC user a disk, you relinquish all control over the contents. You no longer have any jurisdiction over the application code, or any restraints on where it could go next. It may well end up outside the company altogether; people often take work home with them ... I doubt if they are too careful about returning it when they leave!

In principle, the solution is fairly obvious: you need a network! If no-one ever needs to have your application physically present on their local disk, most of the management problems go away. Of course people can still take work home, but the vast bulk of systems remain where you can get at them. Of course, there are all sorts of design issues to be sorted out before you should even contemplate supporting live applications in this kind of environment. Well, we are going live at 6 factories across the UK at the moment, and I haven't really started to think about it yet!

The most obvious constraint is speed. On my PS/2 I have the usual complement of A:;B:;C:;D: ... however (depending on the health of a rather ad hoc length of Ethernet cable) I can also boast of G: (actually a Vax in computer room); H: (another Vax somewhere in the factory); and I: (50 miles away at Castleford). G: and H: are about as fast as my PS/2 model-70 hard disk; I: is at the end of a 9600 baud phone connection! To )LOAD a workspace over this sort of link can take over 5 minutes.

Another problem concerns the behaviour of 'runtime' APL code. On the mainframe, we still get occasional crashes from ancient systems written in the days when no-one considered the possibility of there being more than 12 PFkeys. Typically these have statements like `→(Next,Help,End,....)[1+PF]` ... which is a pretty good guarantee of an `INDEX  ERROR` when someone accidentally catches PF24. Most users have got into the habit of `PF←0  ⋄ →⎕LC`, and don't even bother to ring up! Under APL\*PLUS II (runtime) a trivial error like this will simply dump them in DOS, losing half a morning's work.

Some of the questions you need to think about:

- can you really afford to ship 'runtime' code? We are not talking *packages* here, we are talking fast moving applications which need to change as the business need changes. I suspect the answer is *no*, and that (at the very least) you should give the user emergency access to `⍎⍞` somewhere in the system. In doing so, you violate your APL\*PLUS runtime licence ... oh bother!

- how are you going to distribute utility code? I suspect that what is needed is something a bit like LOGOS which will build and maintain 'patch' files; and a corresponding component in each application which will detect these and 'upgrade' itself. To make such a 'Trojan Horse' approach work, you need to make sure that you get the bare minimum of 'listening code' into *every* application **now**. You can design the horse later ... but if no-one is there to wheel it into the city, it will avail you nothing.

- what about multiple developers working on the same application? On the mainframe, we have a system of project libraries, and can use access controls to ensure no-one does anything silly. On the PC, it is dreadfully easy to trample all over each other's code!

In short, sooner or later, you may well get bundled unceremoniously off your mainframe, and if you are in a position to start sorting out some of these issues now, then you should. In my experience, it is always better to panic sooner rather than later, and a sound line of retreat never did any general any harm at all.
