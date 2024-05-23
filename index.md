---
layout: default
title: Home
---

<div class="github-ribbon">
  <a target="_blank" href="https://github.com/oscar-system/Oscar.jl/">Go to the code repository</a>
</div>


# {{ site.title }}

The OSCAR project develops a comprehensive **O**pen **S**ource **C**omputer **A**lgebra **R**esearch
system for computations in algebra, geometry, and number theory, written in [Julia](https://julialang.org). In particular,
the emphasis is on supporting complex computations which require a high level
of integration of tools from different mathematical areas. 

The development of OSCAR is supported by the Deutsche Forschungsgemeinschaft DFG within the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/).

See the [About]({{site.baseurl }}/about) page for more information.

## Getting started

For tutorials, see the [Tutorials page]({{site.baseurl }}/tutorials), where pre-rendered notebooks showcase
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

## Get in touch

A great place to ask questions about OSCAR and discuss all aspects of it is
via [Slack -- click here to join it]({{site.baseurl }}/slack).
Please check out the [community page]({{site.baseurl }}/community) for further
ways to get in touch with us.

## Citing OSCAR

If you have used OSCAR in the preparation of a paper please cite it as described below:

    [OSCAR]
        OSCAR -- Open Source Computer Algebra Research system, Version 1.0.0,
        The OSCAR Team, 2024. (https://www.oscar-system.org)
    [OSCAR-book]
        Wolfram Decker, Christian Eder, Claus Fieker, Max Horn, Michael Joswig, eds.
        The Computer Algebra System OSCAR: Algorithms and Examples,
        Algorithms and Computation in Mathematics, Springer, 2024. (https://link.springer.com/book/9783031621260)

If you are using BibTeX, you can use the following BibTeX entries:

    @misc{OSCAR,
      key          = {OSCAR},
      organization = {The OSCAR Team},
      title        = {OSCAR -- Open Source Computer Algebra Research system,
                      Version 1.0.0},
      year         = {2024},
      url          = {https://www.oscar-system.org},
      }

    @book{OSCAR-book,
      editor = {Decker, Wolfram and Eder, Christian and Fieker, Claus and Horn, Max and Joswig, Michael},
      title = {The {C}omputer {A}lgebra {S}ystem {OSCAR}: {A}lgorithms and {E}xamples},
      year = {2024},
      publisher = {Springer},
      series = {Algorithms and {C}omputation in {M}athematics},
      volume = {32},
      edition = {1},
      url = {https://link.springer.com/book/9783031621260},
      month = {8},
      issn = {1431-1550},
    }
