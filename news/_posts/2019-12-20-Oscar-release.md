---
layout: post
title: Oscar.jl release 0.1.0
author: Bill Hart
---

Today, as mandated by our various funding sources, I tagged Singular.jl
v0.1.0 and registered it as an official Julia package and tagged the
Oscar.jl v0.1.0 release.

There is a mandatory waiting period of 3 days for new Julia packages, so I
expect everything to be usable before Christmas.

To install Oscar.jl:

using Pkg
Pkg.add(PackageSpec(url="https://github.com/oscar-system/Oscar.jl
<https://github.com/oscar-system/Oscar.jl/releases/tag/v0.1.0>"))

We have begun the user documentation project:

https://oscar-system.github.io/Oscar.jl/latest/index.html

Note that although a majority of Oscar is installed using binaries, there
are still some unavoidable dependencies to install Oscar:

* C++ compiler
* cmake
* gnu make
* Julia 1.0, 1.1 or 1.2

There are also additional dependencies that must be installed for some of
the individual packages that make up Oscar. Perhaps the authors of those
packages would be so kind as to list those dependencies below.

Congratulations everyone on this significant technical milestone.

Let us just remind ourselves of what we've achieved in this technical
release:

* Integration of Gap with the Julia garbage collector
* A continuous integration server for all parts of Oscar
* All four Oscar cornerstones (Singular, Gap, Hecke/Nemo, Polymake)
starting up in the same Julia package
* A great deal of new mathematical functionality across all our Julia
packages
* Interfaces from Julia to Gap, the Singular kernel and interpreter,
Polymake, Flint, Antic and Arb
* High level integration of Hecke/Nemo with most Singular kernel objects
* Demonstration of the documentation technology
* A first technical release of Oscar.jl itself
* Extensive test code
* A total of 11332 commits across our Julia packages, not including
contributions we've made to the non-julia cornerstone systems or Julia
packages still in preparation or to Julia itself
* Well over 30 major contributors
* 170 GitHub stars across our packages
* 126 forks of our packages on GitHub

Thanks everyone for a year of hard work, and I look forward to us building
on this first technical release with ever more improvements to usability,
reductions in startup time, mathematical features and examples,
documentation, test code, low and high level integration, parallelism, etc.

We intend to make new Oscar releases, starting in the new year, about every
week to month, depending on various technical challenges and manpower.

Seasons Greetings,

The Oscar Development Team.
