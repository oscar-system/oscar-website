# AbstractAlgebra : A Julia package for algebra

This is the first in a series of blog posts we will be writing on aspects of the new
OSCAR Computer Algebra System we are writing.

In this blog we'll be covering a new package we have created as part of the OSCAR
project, called AbstractAlgebra.jl.

The AbstractAlgebra package is written entirely in Julia and serves two purposes. The
first is to implement generic algorithms in abstract algebra and the second is to
outline a set of interfaces that must be implemented in order to make use of these
generics.

## What are generic algorithms?

If one requires polynomials for a project, over the integers for example, then one can
make use of a specialised very fast C/C++ or even a specialised Julia implementation
for polynomials over the integers. But what happens if you then want to work with
fractions in the fraction field of that polynomial ring, or with power series, the
coefficients of which are polynomials over that fraction field.

Clearly there is a combinatorial explosion in the number of groups, rings, fields and
modules that algebraists want to consider. It is exceptionally unlikely that a dedicated
C/C++ library exists for the rather complicated algebraic objects you want to work with.

Computer algebra systems solve this problem by providing generics. For example,
AbstractAlgebra provides fraction fields and power series over any ring, so long as
a certain Ring interface is implemented.

## What generic constructions does AbstractAlgebra provide

AbstractAlgebra starts with some basic objects, such as Julia BigInts or rationals or
BigFloats, or with any type provided by a Julia package that satisfies a simple
interface and then implements the following generics over those types:

  * Fraction fields
  * Dense univariate polynomials
  * Sparse distributed multivariate polynomials
  * Power series (absolute and relative)
  * Laurent series
  * Puiseux series
  * Residue rings and fields
  * Matrices
  * Maps, cached maps and maps with inverse

Abstract Algebra also provides the following (limited to full symmetric groups), with
permutations represented internally using any specified Julia integer type:

  * Permutation groups
  * Characters
  * Young tableaux

Of course, everything is recursive, so that you can take a fraction field over a
polynomial ring over a residue ring over a polynomial ring over the integers, for
example.

## What algorithms does AbstractAlgebra implement?

AbstractAlgebra has been under development for a few years and already implements a
large number of algorithms. Some of the highlights are as follows:

For univariate polynomials we implement Ducos' algorithm for resultant, generic
interpolation over an integral domain, the pseudo-remainder GCD algorithm for
polynomials over a Euclidean domain.

Laurent and Puiseux series are implemented using a data structure that stores a
valuation, scaling factor and precision, so that a series of the form
$x^{-1} + 3x^2 + 7x^5 + O(x^6)$ would be stored with a valuation of $-1$, a scaling
factor of $3$ and a precision of $6$. This means that only $3$ coefficients are
stored, instead of the usual $7$.

Sparse distributed, multivariate polynomials implement the heap based algorithms of
Johnson, Monagan and Pearce. In this way we implement very fast generic multiplication,
division and powering of multivariate polynomials. In some cases, our generic Julia
implementation is competitive with certain specialised C implementations for basic
arithmetic of multivariate polynomials.

For dense matrices we implement reduced row echelon forms, linear system solving,
minimal and characteristic polynomial, Smith normal form, Hermite normal form over a
Euclidean domain, LU decomposition, nullspace, numerous fast determinant algorithms,
Popov form and much more.

## What if we want fast C implementations as well?

AbstractAlgebra provides generic implementations which work as generally as possible.
Apart from the distinction of working over a ring, field or Euclidean domain, more
specialised algorithms are not implemented.

However, we have also been writing a number of packages which provide very specialised
C implementations for specific rings and fields.

The most straightforward of these is Nemo.jl, which we have introduced previously. It
makes use of the Flint, Arb and Antic libraries to provide highly optimised C
implementations of finite fields, number fields, real and complex numbers, padics,
and all the usual rings and fields, such as the integers, rationals, integers mod n, and
so on.

Nemo.jl implements the interfaces set out in AbstractAlgebra.jl and so any
AbstractAlgebra generic algorithm can be used over any Nemo.jl domain. Moreover, instead
of using a generic implementation of polynomials over the integers, for example,
when Nemo.jl is loaded instead of AbstractAlgebra.jl, polynomials over the integers
will be implemented automatically using the highly optimised routines available for this
in Flint.

Over the course of the next few weeks and months, we'll be introducing other libraries
we are working on which implement AbstractAlgebra interfaces.

Of course AbstractAlgebra.jl is fully usable on its own, without Nemo.jl and other
packages with C dependencies. It is great for situations where one wants pure Julia
code, or where the C library dependencies of Nemo.jl are not wanted, e.g. when
interfacing some other project to AbstractAlgebra.jl for its generics capability.

This "pure Julia" feature of AbstractAlgebra.jl is something that has been requested by package developers in the Julia community, and we hope it will be of use to the
community and will attract volunteer Julia developers to contribute to the project and
further develop its capabilities in the area of AbstractAlgebra.

## What is planned for the future of AbstractAlgebra?

AbstractAlgebra is already quite stable, and we are using it extensively in other
components of Oscar that we are working on.

However, there are many other things we'd like to add in the future. Maybe this list
inspires someone with an itch to scratch, who would like to contribute something to the
AbstractAlgebra.jl project!

We've made a list of things we definitely want. See

[Development Roadmap](https://github.com/Nemocas/AbstractAlgebra.jl/issues/64)

One of the biggest features not yet supported by AbstractAlgebra, but planned for the
future, is non-commutative algebra. Currently, AbstractAlgebra assumes all rings are
commutative (matrices and groups are of course not).

## Documentation

Recently, we've spent a lot of time documenting all the AbstractAlgebra interfaces. This
includes not only the interfaces that need to be implemented by other packages in order
to benefit from AbstractAlgebra generics, but also all the generic algorithms that
AbstractAlgebra provides once the necessary interfaces are implemented.

The complete documentation for AbstractAlgebra.jl is available here:

[AbstractAlgebra.jl documentation](https://nemocas.github.io/AbstractAlgebra.jl/)

Of course, there are sure to be errors in the documentation. Pull requests and bug
reports are welcome on the GitHub issue tracker!

## AbstractAlgebra's role in OSCAR

The OSCAR project is a very large project with many working parts. Part of the
integration work being done in OSCAR makes use of Julia, and indeed some of the packages
we are implementing are written entirely in Julia (e.g. Nemo.jl and Hecke.jl).

AbstractAlgebra.jl is a package that most, if not all, Julia components of OSCAR will
use. It spells out the common interfaces that are required for generics to work. Then it
provides the generic algorithms back to those other systems.

## Scratch an itch

Do you have an itch you want to scratch and AbstractAlgebra might get you part of the
way there? We'd love to hear from you.

AbstractAlgebra is considered very stable at this point, and we feel that now is the
right time to be announcing it and encouraging pull requests. We believe that the code
that is already there gives a good template for future additions. It should be quite
clear how to follow the pattern.

Of course, it is better if we know what's coming, rather than to have large code dumps
that require significant work to harmonise them with other code that is there or on its
way. So we ask contributors to talk to us early and often, so we can be as helpful as
possible.

