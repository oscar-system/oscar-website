---
layout: default
title: Home
---

<div class="github-ribbon">
  <a target="_blank" href="https://github.com/oscar-system/Oscar.jl/">Go to the code repository</a>
</div>


# {{ site.title }}

The OSCAR project develops a comprehensive **O**pen **S**ource **C**omputer **A**lgebra **R**esearch
system for computations in algebra, geometry, and number theory. In particular,
the emphasis is on supporting complex computations which require a high level
of integration of tools from different mathematical areas. 

The project builds on and extends the four cornerstone systems

  * [GAP](https://www.gap-system.org/) - computational discrete algebra (via [GAP.jl](https://github.com/oscar-system/GAP.jl))
  * [Singular](https://www.singular.uni-kl.de/) - commutative and non-commutative algebra, algebraic geometry (via [Singular.jl](https://github.com/oscar-system/Singular.jl))
  * [Polymake](https://polymake.org/doku.php) - polyhedral geometry (via [Polymake.jl](https://github.com/oscar-system/Polymake.jl))
  * Antic ([Hecke](https://github.com/thofma/Hecke.jl/), [Nemo](http://nemocas.org)) - number theory

as well as further libraries and packages, which are combined together into the
[Oscar.jl](https://github.com/oscar-system/Oscar.jl) Julia packages

The development of OSCAR is supported by the Deutsche Forschungsgemeinschaft DFG within the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/).

See the [About]({{site.baseurl }}/about) page for more information.

## Getting started

For examples, see the [Examples page]({{site.baseurl }}/example), where pre-rendered notebooks showcase
selected things the software developed in the OSCAR project can already do.

<!--
To try OSCAR live from your browser, click on the [binder](https://mybinder.org) links on the Examples page.
At present, these will take a few minutes to load, as we 
currently still build some dependencies from source behind the scenes.
-->

If you wish to contribute to the OSCAR development, see the [Installation page]({{site.baseurl }}/install) for
instructions on how to install it, and also check out our [community page]({{site.baseurl }}/community).

Note that OSCAR has not reached a first public release yet, and its parts should be treated as
a technology preview. See the [News page]({{site.baseurl }}/news) for announcements about OSCAR development.

## Stay informed

If you want to get notifications about news items, you can subscribe to
the [OSCAR news atom feed]({{ site.baseurl }}/feed-news.xml).

You can also subscribe to the [OSCAR](https://mail.mathematik.uni-kl.de/mailman/listinfo/oscar) or the [OSCAR-dev](https://mail.mathematik.uni-kl.de/mailman/listinfo/oscar-dev) email lists. You can also view the archives for [OSCAR](https://mail.mathematik.uni-kl.de/pipermail/oscar/) and [OSCAR-dev](https://mail.mathematik.uni-kl.de/pipermail/oscar-dev/).
