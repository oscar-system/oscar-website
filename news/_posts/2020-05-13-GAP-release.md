---
layout: post
title: GAP.jl 0.4.0 released
author: Max Horn
---
We are pleased to announce the release of GAP.jl 0.4.0, a major update to the
[GAP.jl](https://github.com/oscar-system/GAP.jl) package which provides full
bidirectional access to the [GAP computer algebra system](https://www.gap-system.org)
from the Julia language and vice-versa.

Here is an overview of the changes in this release:

- Add GAP.prompt() function which gives a GAP prompt inside Julia
- Add support for Julia keyword arguments on the GAP side
- Overload the Julia 'in' operator for GAP objects
- Add conversion constructors for various Julia types, to allow for more
  idiomatic Julia code accessing GAP objects
- Improve GAP <-> Julia conversion
- Show the GAP banner again by default, unless we are being loaded from Oscar.jl
- Switch to Julia "artifact" system for downloading the GAP sources,
  which can save time and disk space when rebuilding or reinstalling GAP.jl
- Complete overhaul of the build process for GAP, making it more robust
- Ensure that we link against the same GMP and readline as other components of
  OSCAR do
- Remove the implicit dependency on LinearAlgebra.jl
- Fix a bunch of minor bugs
- Various janitorial changes

For more details, please consult the
[GAP.jl 0.4.0 release page](https://github.com/oscar-system/GAP.jl/releases/tag/v0.4.0)
which lists all commits that went into this release.
