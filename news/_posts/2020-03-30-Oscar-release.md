---
layout: post
title: Oscar 0.2.0 released; now an official Julia package
author: Claus Fieker
---

Oscar is now registered as an official Julia package! This means that
starting with version 0.2.0, the `Oscar.jl` Julia package can be
installed as conveniently as any other Julia package.

It requires Julia 1.3.1 and a recent enough C++ compiler (for details,
please [refer to the install instructions]({{ site.baseurl }}/install/)).
Now start Julia and enter
{% highlight julia %}
using Pkg ; Pkg.add("Oscar")
{% endhighlight %}

From this point on, you can load Oscar from any Julia session
by entering `using Oscar`:

```
julia> using Oscar
 -----    -----    -----      -      -----   
|     |  |     |  |     |    | |    |     |  
|     |  |        |         |   |   |     |  
|     |   -----   |        |     |  |-----   
|     |        |  |        |-----|  |   |    
|     |  |     |  |     |  |     |  |    |   
 -----    -----    -----   -     -  -     -  

...combining (and extending) GAP, Hecke, Nemo, Polymake and Singular
Version 0.2.0-dev ... 
 ... which comes with absolutely no warranty whatsoever
Type: '?Oscar' for more information
(c) 2019-2020 by The Oscar Development Team
```
