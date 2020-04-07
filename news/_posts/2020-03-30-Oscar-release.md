---
layout: post
title: Oscar 0.2.0 and official Julia package
author: Claus Fieker
---

Oscar is now registered as an official Julia package!

Today marks both
 - the release of Oscar 0.2.0
 - and the official Julia registration

To install Oscar, you simply need to start Julia (version 1.3.1 preferably) and then

{% highlight julia %}
julia> using Pkg
julia> Pkg.add("Oscar")
{% endhighlight %}

To then (and later) use it:

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
