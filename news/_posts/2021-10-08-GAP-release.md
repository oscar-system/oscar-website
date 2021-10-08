---
layout: post
title: GAP.jl 0.7.0 released
author: Max Horn
---
We are pleased to announce the release of GAP.jl 0.7.0, a major update to the
[GAP.jl](https://github.com/oscar-system/GAP.jl) package which provides full
bidirectional access to the [GAP computer algebra system](https://www.gap-system.org)
from the Julia language and vice-versa.

It contains the following breaking changes compared to the 0.6.x release:

- Require Julia 1.6 or later.
- Remove `LoadPackageAndExposeGlobals`. If you are using this, see <https://github.com/oscar-system/GAP.jl/pull/696> for alternatives.
- Remove all `convert` methods. If you were using `convert(GapObj, val)`, you can use `GapObj(val)` or `julia_to_gap(val)` instead. If you were using `convert(T,gapobj)`, use `T(gapobj)` or `julia_to_gap(gapobj)` instead.
- Remove `GAP.gap_exe()`. Instead please use `GAP.create_gap_sh(path)`.
- Remove GAP function `IsArgumentForJuliaFunction`. No replacement should be necessary.
- Remove GAP function `ImportJuliaModuleIntoGAP`. As a replacement, use `JuliaEvalString("import MODULENAME")`.
- Restrict `GapObj` constructor by adding a return type annotation that ensures only values of type `GapObj` are returned. If you relied on this also returning `Int`, `Bool` or `FFE`, please use the `GAP.Obj` constructor instead. If you relied on also Julia objects being returned, you should probably revise your code; but if you determine that you still really *really* have to do this, you can by using `julia_to_gap`.

Other changes:

- Add `GapInt` type union
- Patch the GAP package manager to perform downloads via Julia's `Downloads.download` to avoid certain failure scenarios
- Add `@wrap` macro as an alternative to `@gapwrap` for certain use cases.
- Don't show the GAP banner if Julia is started with the `--quiet` flag
- Call the GAP AtExit handler when exiting Julia, so that e.g. the command line history is saved (if the user enabled this in their preferences) or temporary directories are removed.
- Many internal changes and refactoring


For more details, please consult the
[GAP.jl 0.7.0 release page](https://github.com/oscar-system/GAP.jl/releases/tag/v0.7.0).
