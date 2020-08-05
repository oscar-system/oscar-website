---
layout: post
title: AbstractAlgebra.jl 0.10.0 released
author: Tommy Hofmann
---
We are pleased to announce the release of AbstractAlgebra.jl 0.10.0, a major update to the
[AbstractAlgebra.jl](https://github.com/nemocas/AbstractAlgebra.jl) package.

Here is an overview of the changes in this release:

- Implementation of Laurent polynomials.
- Proper handling of operator precedence when printing complex expressions. To this end,
  a new interface function `expressify` was introduced in a backwards compatible way.
  (See <https://github.com/Nemocas/AbstractAlgebra.jl/pull/611>] or the documentation).
- Rename `set_prec!` to `set_precision!` and `set_val!` to `set_valuation!`.
- Square root for field elements (falling back to factorization)
- Various small bugfixes.

For more details, please consult the
[AbstractAlgebra.jl 0.10.0 release page](https://github.com/nemocas/AbstractAlgebra.jl/releases/tag/v0.10.0)
which lists all commits that went into this release.


On behalf of the AbstractAlgebra developers,

Tommy
