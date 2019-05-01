---
layout: post
title: Polymake release 3.4 and Polymake.jl release 0.1.0
author: Michael Joswig
---

Dear friends of polymake,

this is to announce the release of polymake 3.4, which is actually available
since 15 April.  So you will find it already in some of the quicker Linux
distributions such as arch.

While this is mainly a technical release with numerous fixes and improvements
(see also the updated documentation at [polymake.org](https://www.polymake.org)), there are several new
features.  Let me highlight one:

* The interfaces to TOSimplex and SCIP were extended such that polymake can now
also solve mixed-integer linear programs (with exact rational arithmetic).

Most importantly for the OSCAR project, however, is the deepened coordination
with ongoing Julia development.  In particular, I am very, very happy to announce

* the first release of Polymake.jl.

This is a new generic interface from Julia to polymake, which provides almost
all of our functions (save visualization). As its key feature it lives entirely
in the Julia world, i.e., you can start any (recent) Julia, then 'add
Polymake.jl' and 'using Polymake.jl', and you are good to go.  Probably the
easiest way ever to get polymake running on your computer.

A big thanks to the Polymake.jl developers Sebastian Gutsche, Marek Kaluba and
Sascha Timme, who put this together with a bit of help by Benjamin Lorenz.

As far as the further development is concerned, polymake shifted to a 3 month
release cycle. So the next version 3.5 will be ready in mid-July. The plan is
to always update the Polymake.jl version one week after the new polymake
release. So they will stay in sync.

Happy polymaking!

Michael Joswig and the polymake team