---
layout: post
title: GAP.jl 0.4.0 released
author: Max Horn
---
We are pleased to announce the release of GAP.jl 0.460, a major update to the
[GAP.jl](https://github.com/oscar-system/GAP.jl) package which provides full
bidirectional access to the [GAP computer algebra system](https://www.gap-system.org)
from the Julia language and vice-versa.

Here is an overview of the changes in this release:

- Update from GAP 4.11.0 to a prerelease of 4.12, which brings many improvements
- Add support for macOS on Apple M1
- Add support for Julia 1.7
- Add macros @gapattribute and @gapwrap
- Revise handling of GAP errors, fixing many bugs related to that
- Add support for using Julia's random sources in GAP, and vice versa
- Many other small changes

For more details, please consult the
[GAP.jl 0.6.0 release page](https://github.com/oscar-system/GAP.jl/releases/tag/v0.6.0).
