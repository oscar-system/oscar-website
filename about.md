---
layout: page
title: About the OSCAR project
---

The OSCAR project will integrate the four computer algebra systems
[GAP](http://www.gap-system.org), [polymake](http://polymake.org),
[Singular](http://www.singular.uni-kl.de),
and [ANTIC](http://www.nemocas.org) developed within the TRR 195 into a
visionary next generation open source computer algebra system
surpassing the combined mathematical capabilities of the underlying
systems.

OSCAR will allow users to construct new mathematical objects efficiently
by combining existing building blocks from any of the cornerstones and
will equip these objects with mathematical capabilities exceeding
those of the individual systems in a transparent way.

## The four cornerstones

This project builds on four leading computer algebra systems which
are, with the exception of the new system ANTIC, widely used
internationally. While the envisaged computer algebra system will be
created by tightly integrating the four cornerstones, the individual
systems will continue to be developed further. This includes working
together with the developers of the individual cornerstones
to develop the cornerstones in a way the best integration can be achieved.

ANTIC is an evolving number theoretic software project focusing on
computations in and with number fields and generic finitely presented
rings. ANTIC is written in a mixture of C and Julia, building on top
of the very successful Flint project of William Hart. In order to
reach the mathematical goals of the OSCAR project, the functionality
of ANTIC will be considerably extended.

GAP is a system for computational discrete algebra, with particular
emphasis on group and representation theory. One of the distinguishing
features of GAP is that it provides a general purpose high level
interpreted programming language especially suited to algebraic
applications. It is easy to extend GAP’s functionality; currently over
120 GAP packages contributed by third party authors are distributed
with each release.

The system polymake is a standard tool for dealing with convex
polytopes, polyhedral fans, tropical hypersurfaces,
and related objects from combinatorics and
geometry. It is designed as a hybrid written in C++ and Perl. A
proprietary rule based mechanism decides which low-level C++
functions are to be called to satisfy user demands.

Singular is a well-established computer algebra system for polynomial
computations, with particular emphasis on applications in algebraic
geometry, commutative algebra, and singularity theory, and with two
subsystems for non-commutative algebra, Plural and
Letterplace. Singular has a kernel written in C++ and provides its own
interpreted user language. The Singular language will be enhanced with
regard to efficiency and expressiveness by rewriting its interpreter
in the modern language [Julia](http://www.julialang.org), which will also be used to integrate the
four cornerstone systems.

## The role of Julia

[Julia](http://www.julialang.org) is a an actively developed
interactive and expressive programing
languange. Julia offers

* data types that can depend on other types, for example modeling
matrices over polynomial rings over number fields;
* Just-in-time compilation (JIT) to compile code at runtime to retain
efficient performance;
* capabilities of accessing low-level C/C++ data structures in the
kernels of the cornerstones efficiently;
* easy access to standard third-party libraries, (e.g., for string
manipulation, visualisation, networking).

Julia will serve as an integration layer allowing the four
cornerstones to communicate in a more profound way than through
unidirectional interfaces. Furthermore it will serve as high-level
language for implementing efficient algorithms utilizing all
cornerstones.
