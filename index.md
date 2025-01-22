---
layout: default
title: Home
---

<div class="github-ribbon">
  <a target="_blank" href="https://github.com/oscar-system/Oscar.jl/">Go to the code repository</a>
</div>


# {{ site.title }}


## Upcoming events

{% assign sorted_conferences = site.data.conferences | group-by: "start-date" | sort: "end-date" %}
{% assign today = "now" | date: "%Y-%m-%d" %}
{% assign has_upcoming_events = false %}

{% for event in sorted_conferences %}
  {% if event.end-date >= today %}
    {% assign has_upcoming_events = true %}
* [{{ event.title }} ({{ event.location }}, {{ event.start-date | date: "%d %b %Y" }} to {{ event.end-date | date: "%d %b %Y" }})]({{ event.website }})
  {% endif %}
{% endfor %}

{% unless has_upcoming_events %}
Currently no upcoming events.
{% endunless %}


## What is OSCAR?

The OSCAR project develops a comprehensive **O**pen **S**ource **C**omputer **A**lgebra **R**esearch
system for computations in algebra, geometry, and number theory, written in [Julia](https://julialang.org). In particular,
the emphasis is on supporting complex computations which require a high level
of integration of tools from different mathematical areas. 

The development of OSCAR is supported by the Deutsche Forschungsgemeinschaft DFG within the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/).

See the [About]({{site.baseurl }}/about) page for more information.

## Getting started

For tutorials, see the [Tutorials page]({{site.baseurl }}/tutorials), where pre-rendered notebooks showcase
selected things the software developed in the OSCAR project can already do.

Please also see the [Installation page]({{site.baseurl }}/install) for
instructions on how to install OSCAR. Check out our [community page]({{site.baseurl }}/community)
to learn how to get in touch with other OSCAR users and developers -- they may be able to help you
get started and answer your questions.

See the [News page]({{site.baseurl }}/news) for announcements about OSCAR development.

## The Book

The book _The Computer Algebra System OSCAR_ presents version 1.0 of OSCAR. It is an invitation
to use OSCAR. With discussions of theoretical and algorithmic aspects included, it offers a
multitude of explicit code snippets. These are valuable for interested researchers from graduate
students through established experts.

Code snippets and list of errata are available on the companion website at
[https://book.oscar-system.org/](https://book.oscar-system.org/)

## Get in touch

A great place to ask questions about OSCAR and discuss all aspects of it is
via [Slack -- click here to join it]({{site.baseurl }}/slack).
Please check out the [community page]({{site.baseurl }}/community) for further
ways to get in touch with us.

## Citing OSCAR

If you have used OSCAR in the preparation of a paper please cite it as described below:

```md
[OSCAR]
    OSCAR -- Open Source Computer Algebra Research system, Version 1.0.0,
    The OSCAR Team, 2024. (https://www.oscar-system.org)
[OSCAR-book]
    Wolfram Decker, Christian Eder, Claus Fieker, Max Horn, Michael Joswig, eds.
    The Computer Algebra System OSCAR: Algorithms and Examples,
    Algorithms and Computation in Mathematics, Springer, 2025. (https://link.springer.com/book/9783031621260)
```

If you are using BibTeX, you can use the following BibTeX entries:

```bibtex
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
  year = {2025},
  publisher = {Springer},
  series = {Algorithms and {C}omputation in {M}athematics},
  volume = {32},
  edition = {1},
  url = {https://link.springer.com/book/9783031621260},
  issn = {1431-1550},
}
```
