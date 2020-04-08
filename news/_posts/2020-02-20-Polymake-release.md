---
layout: post
title: Polymake.jl 0.3.0 released
author: Marek Kaluba
---

This is a major release streamlining and simplifying the architecture of the project.
Among the largest changes are: the usage of `polymake-4.0` and `CxxWrap-0.9.0` which rises our requirement to `c++-17` compatible compiler as well. More importantly we took the direct perspecive of integrating `Polymake.jl` into `Oscar` in this cycle.

----

## New features

`polymake` now comes with `flint` and `Singular` dependencies and it is possible to perform some polynomial algebra in `Polymake.jl`. However we provide only the very basics, the more advanced task will be delegated to Oscar level.

## Notable changes

Among many changes (see [release notes](https://github.com/oscar-system/Polymake.jl/releases/tag/v0.3.0) for a detailed list), here are the most notable ones:

 * We stopped exporting our internal (small) types in order to facilitate the use of `Polymake.jl` within the Oscar project.
 * Small types (the `c++` wrapped structures) in `Polymake.jl` were renamed dropping the unfortunate `pm_` prefix, so that:
  - `pm_Matrix <: AbstractMatrix` became `Polymake.Matrix  <: AbstractMatrix`,
  - `pm_Integer <: Base.Integer` became `Polymake.Integer <: Base.Integer`, etc.

We hope the two decisions above will make developing in Oscar a much cleaner experience and hopefully we will see other packages following suit. Moreover,

- internal modules of `Polymake.jl` have been renamed to lowercase (matching polymake application names), i.e. `Polymake.Tropical` became `Polymake.tropical`.
- those modules remain exported from `Polymake.jl`, i.e. after `using Polymake` one can immediately call `polytope.Cone(...)`.

To summarize: the only names exported from `Polymake` at the moment are: `visual` (for producing visualisation of polymake objects), application names and macros: `@pm` and `@convert_to`.

## Constructors and macros

All `BigObjects` (in `polymake` nomenclature) gained corresponding `structs` in `Polymake.jl`.
Of course none of it is written by hand, but auto-generated from `polymake` itself.

These constructors allow us to deprecate `@pm` macro in multiple cases. Just a quick reminder: the `@pm` macro can be used to issue more complicated calls to polymake from julia. If You need to pass templates to `BigObjects`, some limited support is provided in costructors.
For example one can construct `polytope.Polytope{Float64}(...)`.
However for this to work, the templates need to be valid julia types/object, hence it is not possible to construct a `Polytope<QuadraticExtension>` through such call. For this (and in general: for passing more complicated templates) one still needs the @pm macro:
```perl
$obj = new BigObject<Template,Parameters>(args)
```
becomes
```julia
obj = @pm appname.BigObject{Template, Parameters}(args)
```

`@convert_to` macro is provided to facilitate conversion between different polymake types:
```julia
julia> c = polytope.cube(3);

julia> f = c.FACETS;

julia> f[1,1] # f is an opaque pm::perl::PropertyValue to julia
ERROR: MethodError: no method matching getindex(::Polymake.PropertyValueAllocated, ::Int64, ::Int64)
Stacktrace:
  [...]

julia> m = @convert_to Matrix{Integer} f # the template must consist of C++ names
pm::Matrix<pm::Integer>
1 1 0 0
1 -1 0 0
1 0 1 0
1 0 -1 0
1 0 0 1
1 0 0 -1
```

## Known Bugs

* `Nemo.jl` MUST be loaded before `Polymake.jl`, otherwise `julia` crashes, see [Nemo.jl/issues/108](https://github.com/wbhart/Nemo.jl/issues/108).
