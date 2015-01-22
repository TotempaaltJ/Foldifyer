Foldifyer
=========

A program to visualize how it would look if you'd fold a strip of paper over
and over again (to infinity).  Licensed under the BSD license - see LICENSE.txt.

All you need is Python 2.x which should have Tkinter preinstalled.

Folding paper?
--------------

Imagine you have strip of paper, just your plain strip of paper. Looks a bit
like so:

    ┌─────────────────────────────────────────────────────────────────┐
    │                                 ¦                               │
    │                                 ¦                               │
    │                                 ¦                               │
    └─────────────────────────────────────────────────────────────────┘

Now fold it along the center (lets say folding it right means making the right
side fold towards yourself), drawn in the above strip with the dashed line, now
the strip would look something more like this:

    ┌─────────────────────────────────┐
    │                                 ¦
    │                                 ¦
    │                                 ¦
    └─────────────────────────────────┘

If you would now lay it out with all corners (the one) at ninety degrees, you'd
get a pattern somewhat like this:

    ───┐
       │
       │

Now fold the flat strip to the left and lay it out again:

       ┌───┐
       │   │
    ───┘   │

Now you get the purpose of Foldifyer. It folds a sheet of paper (of infinite
length) for a different amount of times by taking right or left instructions,
identified by an r or an l respectively. It then shows you what it'd look like
if you laid out your folded piece of paper.

Foldifyer is written specifically so it can take an infinite amount of
instructions.  Be weary though it'll take very long to draw long sets of
instructions. Seeing this should not surprise you:

![Foldifyer screenshot](http://i.imgur.com/TNymC.png)
