---
layout: post
title: AbstractAlgebra 0.13.0 and Nemo 0.20.0 released
author: Tommy Hofmann
---
We are pleased to announce the release of new versions of AbstractAlgebra (0.13.0) and Nemo (0.20.0).

Here is an overview of the changes in this release:

### AbstractAlgebra

- Plenty of small bugfixes.
- Retiring the legacy printer, including the functions `show_minus_one`,
  `needs_parentheses` and `displayd_with_minus_in_fron` used by the old
  printing routines.
- Matrices now implement the iterator interface of julia.
- Matrix spaces now implement the iterator interface (if the base ring is
  iteratable).
- Use of `one(G)` instead of `G()` to create the identity element of
  permutation groups.
- Renaming `rref` to `rref_rational` for rings.

For more details, please consult the
[AbstractAlgebra.jl 0.13.0 release page](https://github.com/Nemocas/AbstractAlgebra.jl/releases/tag/v0.13.0)
which lists all changes that went into this release.

### Nemo

- Various small bugfixes.
- Retiring the legacy printer and use the `expressify` mechanism for all types.
- Iteration for finite fields.

For more details, please consult the
[Nemo.jl 0.20.0 release page](https://github.com/Nemocas/Nemo.jl/releases/tag/v0.20.0)
which lists all changes that went into this release.

The main contributors to these releases were:
@albinahlback, @fieker, @fingolfin, @kalmarek, @rfourquet, @thofma, @tthsqe12, @wbhart

On behalf of the developers,

Tommy
