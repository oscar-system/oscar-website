---
layout: page
title: Documentation
docs:
    - name: AbstractAlgebra.jl
      url: https://nemocas.github.io/AbstractAlgebra.jl/stable/
      description: Pure Julia package implementing generic algorithms for basic arithmetic
                   and algebraic structures. It also defines standard interfaces for
                   generics, that can be implemented by other packages.

    - name: AlgebraicSolving.jl
      url: https://algebraic-solving.github.io/
      description: A Julia package for algebraically solving multivariate polynomial systems.

    - name: GAP.jl
      url: https://oscar-system.github.io/GAP.jl/stable/
      description: The interface to GAP from Julia.

    - name: Hecke.jl
      url: https://thofma.github.io/Hecke.jl/stable/
      description: Algebraic number theory in Julia.

    - name: Nemo.jl
      url: http://nemocas.github.io/Nemo.jl/stable/
      description: The interface to the Flint, Arb and Antic C libraries from Julia.

    - name: Oscar.jl
      url: https://docs.oscar-system.org/stable/
      description: The main OSCAR package.

    - name: Polymake.jl
      url: https://oscar-system.github.io/Polymake.jl/stable/
      description: The interface to Polymake from Julia.

    - name: Singular.jl
      url: https://oscar-system.github.io/Singular.jl/stable/
      description: The interface to Singular from Julia.

---

<div class="message-big">
<a href="https://docs.oscar-system.org/stable/">Click here for the latest OSCAR manual.</a>
</div>
Expert users may also wish to use the [manual for the latest development version](https://docs.oscar-system.org/dev/).


### OSCAR Book

Looking for more? The [OSCAR Book](https://book.oscar-system.org/) offers deeper insights into *OSCAR* beyond the standard documentation.


### Additional Documentation

Among others, OSCAR aims to combine and extend the capabilities of
Antic (<a href="https://github.com/thofma/Hecke.jl/">Hecke</a>,
<a href="https://github.com/Nemocas/Nemo.jl">Nemo</a>),
<a href="https://www.gap-system.org/">GAP</a>,
<a href="https://polymake.org/doku.php">Polymake</a>, and
<a href="https://www.singular.uni-kl.de/">Singular</a>.
Below are links to documentation for Julia software projects encompassed by OSCAR.

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
