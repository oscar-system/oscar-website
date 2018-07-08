---
layout: default
title: Home
---

# {{ site.title }}

The OSCAR project developes a comprehensive open source computer algebra
system for computations in algebra, geometry, and number theory. In particular,
the emphasisis is on supporting complex computations which require a high level
of integration of tools from different mathematical areas. 

The project builds on and extends the four corner stone systems

  * [GAP](https://www.gap-system.org/) - computational discrete algebra
  * [Singular](https://www.singular.uni-kl.de/) - commutative and non-commutative algebra, algebraic geometry
  * [Polymake](https://polymake.org/doku.php) - polyhedral geometry
  * Antic ([Hecke](https://github.com/thofma/Hecke.jl/), [Nemo](http://nemocas.org)) - number theory

as well as further libraries and packages. Its development, which is still at a very early stage, is supported
by the Deutsche Forschungsgemeinschaft DFG within the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/).

See the [About]({{site.baseurl}}/about) page for more information.

## Getting started

For examples, see the [Examples page]({{site.baseurl}}/example), where pre-rendered notebooks showcase
selected things the software developed in the OSCAR project can already do.

To try OSCAR live from your browser, click on the [binder](https://mybinder.org) links on the Examples page.
At present, these will take a few minutes to load, as we 
currently still build some dependencies from source behind the scenes.

If you wish to contribute to the OSCAR development, see the [Installation page]({{site.baseurl}}/install) for
instructions on how to build everything on a growing number of supported platforms.

Note that OSCAR has not reached a first public release yet, and its parts should be treated as
a technology preview. See the [News page]({{site.baseurl}}/news) for announcements about OSCAR development.

## Stay informed

If you want to get notifications about news, new blog posts, or new examples, you can subscribe to
the [OSCAR blog atom feed]({{ site.baseurl }}/feed-blog.xml), the [OSCAR news atom feed]({{ site.baseurl }}/feed-news.xml),
or the [OSCAR examples atom feed]({{ site.baseurl }}/feed-examples.xml).