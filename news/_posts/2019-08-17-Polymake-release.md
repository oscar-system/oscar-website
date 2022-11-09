---
layout: post
title: Polymake.jl 0.2.0 released
author: Marek Kaluba
---

This is a technical release focused on bringing more functionality to Julia.
With `Polymake-v0.2.0` we require `polymake-3.5`.

The main change is the addition of the `@pm` macro. This macro is the swiss army knife of calls to `polymake` library (it transforms julia-like syntax to low-level calls to `polymake`). Therefore nearly all functionality of `polymake` is now accessible in `Polymake.jl` in one form or another.

----

## Summary of new features

* All user functions from perl/polymake are available in the appropriate modules, e.g. homology function from topaz can be called as Topaz.homology(...) in julia. `?Topaz.homology` brings `polymake` docstring.
* Most of the user functions from `polymake` are available as `Appname.funcname(...)` in `Polymake.jl`. However, any function from polymake `C++`` library can be called via `@pm Appname.funcname(...)` macro.
* All big objects of perl/polymake can be constructed via @pm macro. For example
```julia
@pm Tropical.Polytope{Max, QuadraticExtension}(:POINTS=>[1 0 0; 1 1 0; 1 1 1])
```
* Properties of `polymake` big objects are accessible by `bigobject.property` syntax (as opposed to `$bigobject->property` in `polymake`). If there is a missing property (e.g. `Polytope.Polytope` does not have `DIM` property in `Polymake.jl`), please check if it can be accessed by `Appname.property(object)`. For example property `DIM` is exposed as `Polytope.dim(...)` function.
* Methods are available as functions in the appropriate modules, with the first argument as the object, i.e. `$bigobj->methodname(...)` can be called via Appname.methodname(bigobj, ...)
* A function in `Polymake.jl` calling `polymake` may return a big or small object, and the generic return (`PropertyValue`) is transparently converted to one of the native data types (below). If you really care about performance, this conversion can be deactivated by adding `keep_PropertyValue=true` keyword argument to function/method call.
* `polymake` data structures can be converted to appropriate julia types, but are also subtypes of the corresponding julia abstract types, e.g., a `pm_Vector` is an `AbstractVector`, and one can call methods that apply to `AbstractVectors` on `polymake` arrays. The list of available wrapped data structures includes:
 - `pm_Integer <: Integer`,
 - `pm_Rational <: Real`,
 - `pm_Vector <: AbstractVector`,
 - `pm_Matrix <: AbstractMatrix`,
 - `pm_Array <: AbstractVector` (it's a container type without arithmetic),
 - `pm_Set <: AbstractSet`.
 Some combinations thereof are available as well, e.g., Sets of Arrays of Integers.

Happy polymaking!
