---
layout: post
title: GAP-Julia-Interface is now a julia module
author: Sebastian Gutsche
---

After a major restructuring of GAPJulia (our GAP-Julia integration part)
it is now a Julia module, named GAP.jl, which means it can be installed via

{% highlight julia %}
] add https://github.com/oscar-system/GAP.jl
{% endhighlight %}

This downloads and compiles a recent version of GAP (currently the
master branch, we can hopefully set it to a stable branch soon) together
with all GAP packages. Loading GAP into Julia is now done via

{% highlight julia %}
using GAP
{% endhighlight %}

This will make all current interface functionality available to Julia,
including the possibility to access all GAP GVars (global variables and
functions) and several conversion functions.

Furthermore, adding the package to your Julia will place a gap.sh start
script in your .Julia folder, which can be used to execute the GAP that
was installed with the package.

For those who prefer their own compiled version of GAP, if the
environment variable `GAPROOT` is set to this GAP's root dir during the
modules build process, Julia will automatically compile the module
against this GAP, and also load it when `using GAP`. Of course, this GAP
then needs to be compiled with the Julia GC.

We have also adjusted the travis tests to check against Julia 1.1 and
nightly, both with custom GAP and compiled by Julia.

If you are interested in the work that was done for it, you can find it
[here](https://github.com/oscar-system/GAP.jl/pull/207).
