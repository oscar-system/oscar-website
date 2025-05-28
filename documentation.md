---
layout: page
title: Documentation
docs:
    - name: AbstractAlgebra.jl
      url: https://nemocas.github.io/AbstractAlgebra.jl/stable/
      description: Implements generic algorithms for arithmetic and algebraic structures in pure Julia. Defines standard interfaces for generics used by other packages.

    - name: AlgebraicSolving.jl
      url: https://algebraic-solving.github.io/
      description: Solves multivariate polynomial systems algebraically in Julia.

    - name: GAP.jl
      url: https://oscar-system.github.io/GAP.jl/stable/
      description: Interface to GAP from Julia.

    - name: Hecke.jl
      url: https://thofma.github.io/Hecke.jl/stable/
      description: Algebraic number theory in Julia.

    - name: Nemo.jl
      url: http://nemocas.github.io/Nemo.jl/stable/
      description: Interface to Flint, Arb, and Antic C libraries from Julia.

    - name: Oscar.jl
      url: https://docs.oscar-system.org/stable/
      description: Main OSCAR package.

    - name: Polymake.jl
      url: https://oscar-system.github.io/Polymake.jl/stable/
      description: Interface to Polymake from Julia.

    - name: Singular.jl
      url: https://oscar-system.github.io/Singular.jl/stable/
      description: Interface to Singular from Julia.
---

---

### OSCAR Manual (Stable Release)

<div class="message-big">
<a href="https://docs.oscar-system.org/stable/">Read the OSCAR v{{ site.data.release.version }} manual.</a>
</div>


---

### OSCAR Manual (Development Version)

For expert users, the [manual for the latest development version](https://docs.oscar-system.org/dev/) is also available.

---

### The OSCAR Book

Looking for more? The [OSCAR Book](https://book.oscar-system.org/) offers deeper insights into *OSCAR* beyond the standard documentation.

---

### Documentation for Related Packages

OSCAR integrates and extends several powerful software projects, including:

- [**Antic**](https://github.com/thofma/Hecke.jl/) (via Hecke, Nemo)
- [**GAP**](https://www.gap-system.org/)
- [**Polymake**](https://polymake.org/doku.php)
- [**Singular**](https://www.singular.uni-kl.de/)

Below are links to documentation for Julia software projects that are part of OSCAR.

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
