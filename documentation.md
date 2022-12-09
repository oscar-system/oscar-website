---
layout: page
title: Documentation
docs:
    - name: AbstractAlgebra.jl
      url: https://nemocas.github.io/AbstractAlgebra.jl/stable/
      description: Pure Julia package implementing generic algorithms for basic arithmetic
                   and algebraic structures. It also defines standard interfaces for
                   generics, that can be implemented by other packages.

    - name: GAP.jl
      url: https://oscar-system.github.io/GAP.jl/stable/
      description: The interface to GAP from Julia.

    - name: GroebnerBasis.jl
      url: https://ederc.github.io/GroebnerBasis.jl/
      description: The interface to the gb C library from Julia.

    - name: Hecke.jl
      url: https://thofma.github.io/Hecke.jl/stable/
      description: Algebraic number theory in Julia.

    - name: HomalgProject.jl
      url: https://homalg-project.github.io/HomalgProject.jl/stable/
      description: The homalg project compatibility package for Julia.

    - name: Nemo.jl
      url: http://nemocas.github.io/Nemo.jl/stable/
      description: The interface to the Flint, Arb and Antic C libraries from Julia.

    - name: Oscar.jl
      url: https://oscar-system.github.io/Oscar.jl/stable/
      description: The main OSCAR package.

    - name: Polymake.jl
      url: https://oscar-system.github.io/Polymake.jl/stable/
      description: The interface to Polymake from Julia.

    - name: Singular.jl
      url: https://oscar-system.github.io/Singular.jl/stable/
      description: The interface to Singular from Julia.

---

<div class="message message-big">
<a href="https://oscar-system.github.io/Oscar.jl/stable/">Click here for the latest OSCAR manual.</a>
</div>
Expert users may also wish to use the [manual for the latest development version](https://oscar-system.github.io/Oscar.jl/dev/).

### Additional documentation

Note that an aim of OSCAR is to combine and extend the capabilities of
Antic (<a href="https://github.com/thofma/Hecke.jl/">Hecke</a>,
<a href="https://github.com/Nemocas/Nemo.jl">Nemo</a>),
<a href="https://www.gap-system.org/">GAP</a>,
<a href="https://polymake.org/doku.php">Polymake</a>, and
<a href="https://www.singular.uni-kl.de/">Singular</a>.

Below are links to documentation for Julia software projects
encompassed by OSCAR.
Other projects are in development now, and will be announced soon.

{% assign entries = page.docs | sort_natural:"name" %}
<ul>
{% for p in entries %}
  <li>
    <a href="{{ p.url }}"><strong>{{ p.name }} manual</strong></a>
    <br/>
    {{ p.description }}
  </li>
{% endfor %}
</ul>
