---
layout: meeting
title: Program and results
meeting: true
meeting_nr: 201805
redirect_from:
  - /meetings/Meeting-5-2018/program/
---


## Program
* Start: Monday, May 14, at noon
* Finish: Friday, May 18, at noon

- Monday:
  - 12:00: Lunch
  - 13:30: Coding sprint

- Tuesday:
  - 09:00: Begin
  - 10:00: Sebastian Gutsche: Current state of JuliaInterface and PolymakeInterface
  - 10:30: Thomas Breuer: Current state of JuliaExperimental
  - 11:00: Reimer Behrends: Current state of GAP and Julia GC integration
  - 11:30: Bill Hart: Current state of Singular.jl and Nemo.jl
  - 12:00: Lars Kastner: Current state of MPTopCom
  - 14:00: PI-Meeting

- Wednesday to Friday: Coding Sprint
  - 09:00: Begin

## Results and projects of the week

### Packaging and distribution

- Discussions about how to package OSCAR:
  - Docker
  - Conda

### Changes to packages

- GAP Julia Integration
  - Necessary changes in JuliaInterface/LibGAP.jl to work with the integrated GAP Julia GC
  - Bugfixes in the integrated GAP Julia GC
  - New features in JuliaInterface, JuliaExperimental, and LibGAP.jl
  - Full support of all GAP types in the Julia GC

- Singular Julia integration
  - Partial rewrite of the module code in Singular.jl

- Polymake Julia integration
  - Additional functionality in Polymake, using flint, arb, etc.

- Application of integration
  - Integration of Nemo matrices in LinearAlgebraForCAP via JuliaInterface
  - Using GAP and Hecke in second cohomology computations

- Julia 
  - Exploration of further possibilities of linking Julia and C++
