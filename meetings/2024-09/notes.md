---
layout: meeting
title: Tuning Julia code
meeting: true
meeting_nr: 202409
weight: 3
---

## Preparation

- Install Julia (ideally 1.10 or newer)
- [Install OSCAR](/install/)
- Install more Julia packages:
  ```julia
  ]add Revise BenchmarkTools SnoopCompile SnoopCompileCore JET Cthulhu PProf ProfileView AllocCheck DispatchDoctor
  ```
- I heartily recommend  <https://modernjuliaworkflows.org/>
- In fact let's start out tour from there!


### Allocations

- Some of our tests take particular long or use a lot of memory
- Memory consumption is often a good proxy for performance
    - many temporary allocations -> lots of cleanup -> wasted effort
- GOAL: reduce allocations
- Example: creating a polynomial ring

```julia
julia> n=2; R=QQ; @btime S, _ = polynomial_ring(R, "y" => 1:n, "t" => 1:n);
  3.271 μs (83 allocations: 3.50 KiB)

julia> n=2; R=QQ; @btime S, _ = polynomial_ring(R, :y => 1:n, :t => 1:n);
  2.319 μs (51 allocations: 2.27 KiB)
```

- Be careful about using `gens` repeatedly

```julia
julia> S, (y,t) = polynomial_ring(R, :y => 1:n, :t => 1:n);

julia> @btime gens(S)[1:n];
  431.950 ns (15 allocations: 688 bytes)

julia> @btime y;
  1.500 ns (0 allocations: 0 bytes)
```

- there is a reason `ngens` exists

```julia
julia> @btime length(gens(S));
  407.797 ns (13 allocations: 592 bytes)

julia> @btime ngens(S);
  46.638 ns (0 allocations: 0 bytes)
```

- some rings allow `gens(S; copy=false)`


#### Some OSCAR case studies


```
@ experimental/FTheoryTools/test/literature_models.jl:1 @
# runs 400 seconds, allocates 80 GB

@ experimental/FTheoryTools/test/tate_models.jl:1 @
# runs 215 seconds, allocates 65 GB

@ test/AlgebraicGeometry/Schemes/elliptic_surface.jl:1 @
# runs 480 seconds, allocates 122 GB
```

- `literature_models.jl` has 800 lines, where are the memory hogs?
    - look at recent CI logs to get an idea
    - e.g. [this log](https://github.com/oscar-system/Oscar.jl/actions/runs/10888342184/job/30212606216)
      then search for e.g. "defining data for literature" (name of a `@testset`)
    - leads us to `Test weierstrass form of models in F-theory on all toric hypersurfaces, defined over concrete base `


## Some Relevant packages


### Measuring
- [https://github.com/JuliaCI/BenchmarkTools.jl](https://github.com/JuliaCI/BenchmarkTools.jl)
- [https://github.com/LilithHafner/Chairmarks.jl](https://github.com/LilithHafner/Chairmarks.jl)

### Profiling
- built-in profiling code ([Docs](https://docs.julialang.org/en/v1/stdlib/Profile/)) 
- [https://github.com/JuliaPerf/PProf.jl](https://github.com/JuliaPerf/PProf.jl)
- [ProfileView](https://github.com/timholy/ProfileView.jl)
- [ProfileCanvas](https://github.com/pfitzseb/ProfileCanvas.jl)
- [ProfileSVG](https://github.com/kimikage/ProfileSVG.jl)

### Type stability
- [https://github.com/aviatesk/JET.jl](https://github.com/aviatesk/JET.jl) ([Docs](https://aviatesk.github.io/JET.jl/dev/))
- [https://github.com/JuliaDebug/Cthulhu.jl](https://github.com/JuliaDebug/Cthulhu.jl)

### Other
- [https://github.com/JuliaLang/AllocCheck.jl](https://github.com/JuliaLang/AllocCheck.jl) ([Docs](https://julialang.github.io/AllocCheck.jl/dev/))
- [https://github.com/timholy/SnoopCompile.jl](https://github.com/timholy/SnoopCompile.jl) ([Docs](https://timholy.github.io/SnoopCompile.jl/dev/), the docs contain multiple nice tutorials)
- [https://github.com/MilesCranmer/DispatchDoctor.jl](https://github.com/MilesCranmer/DispatchDoctor.jl)





<!--
TODO for max
## TODO: prepare test cases

e.g. our slowest tests:
```
@ experimental/FTheoryTools/test/literature_models.jl:1 @
# runs 400 seconds, allocates 80 GB

@ experimental/FTheoryTools/test/tate_models.jl:1 @
# runs 215 seconds, allocates 65 GB

@ test/AlgebraicGeometry/Schemes/elliptic_surface.jl:1 @
# runs 480 seconds, allocates 122 GB
```


### Misc notes for myself

- TODO: put  Jupyter notebook on GitHub

```
ENV["JULIA_EDITOR"] = "/usr/local/bin/code"
```
-->