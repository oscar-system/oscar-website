---
layout: post
title: AbstractAlgebra.jl 0.12.0, Nemo 0.19.0 and Hecke 0.9.0 released
author: Tommy Hofmann
---
We are pleased to announce the release of new versions of AbstractAlgebra.jl
(0.12.0), Nemo (0.19.0) and Hecke (0.9.0).

Here is an overview of the changes in this release:

### AbstractAlgebra

- Overhaul of the functions for solving linear equations. We now have the
  triple `solve`, `can_solve` and `can_solve_with_solution`, which work for
  fields and rings supporting Hermite form computations. The functions also
  have a `side` keyword so that one can either solve `AX = B` or `XA = B`.
- Experimental code for factorization of multivariate polynomials, which
  reduces the problem to factorization of univariate polynomials.
- Finite fields now support iteration.
- Rename `rref` for matrices over rings to `rref_rational`.
- Various small bugfixes.

For more details, please consult the
[AbstractAlgebra.jl 0.12.0 release page](https://github.com/Nemocas/AbstractAlgebra.jl/releases/tag/v0.12.0)
which lists all changes that went into this release.

### Nemo

- Bump the flint version to 2.7.0, the arb version to 2.19.0 and the antic version to 0.2.4.
- Factorization for `fq_nmod_mpoly` and `nmod_mpoly`.
- `sqrt`, `issquare` and `issquare_with_square_root` functions for finite fields and polynomials.
- Various small bugfixes.

For more details, please consult the
[Nemo.jl 0.19.0 release page](https://github.com/Nemocas/Nemo.jl/releases/tag/v0.19.0)
which lists all changes that went into this release.

### Hecke

- Overhaul of morphisms between number fields. One can now work with morphisms
  between number fields of any type.
- Infinite places for all number fields, including relative and non-simple extensions.
- Factorization of multivariate polynomials over number fields.
- Various bug fixes and improvements.

For more details, please consult the
[Hecke.jl 0.9.0 release page](https://github.com/thofma/Hecke.jl/releases/tag/v0.9.0)
which lists all changes that went into this release.

The main contributors to these releases were:
@fieker, @hwjsnc, @rfourquet, @thofma, @tthsqe12, @wbhart, @CarloSircana.

On behalf of the developers,

Tommy
