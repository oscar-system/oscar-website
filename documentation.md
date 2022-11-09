---
layout: page
title: Documentation
documentation_pages:
    - name: AbstractAlgebra.jl
      documentation_url: https://nemocas.github.io/AbstractAlgebra.jl/dev/
      description: Pure Julia package implementing generic algorithms for basic arithmetic
                   and algebraic structures. It also defines standard interfaces for
                   generics, that can be implemented by other packages.

    - name: Nemo.jl
      documentation_url: http://nemocas.github.io/Nemo.jl/dev/
      description: The interface to the Flint, Arb and Antic C libraries from Julia.

    - name: GroebnerBasis.jl
      documentation_url: https://ederc.github.io/GroebnerBasis.jl/
      description: The interface to the gb C library from Julia.

    - name: Singular.jl
      documentation_url: https://oscar-system.github.io/Singular.jl/dev/
      description: The interface to Singular from Julia.

    - name: Hecke.jl
      documentation_url: https://thofma.github.io/Hecke.jl/dev/
      description: Algebraic number theory in Julia.

    - name: HomalgProject.jl
      documentation_url: https://homalg-project.github.io/HomalgProject.jl/dev/
      description: The homalg project compatibility package for Julia.

    - name: GAP.jl
      documentation_url: https://oscar-system.github.io/GAP.jl/dev/
      description: The interface to GAP from Julia.

    - name: Polymake.jl
      documentation_url: https://oscar-system.github.io/Polymake.jl/dev/
      description: The interface to Polymake from Julia.

---

<div class="message">
You can find the OSCAR manual here:
<ul>
<li><strong><a href="https://oscar-system.github.io/Oscar.jl/stable">Manual for the latest stable release</a></strong></li>
<li><strong><a href="https://oscar-system.github.io/Oscar.jl/dev">Manual for the latest development version</a></strong></li>
</ul>
</div>

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

{% assign entries = page.documentation_pages | sort_natural:"name" %}
<ul>
{% for p in entries %}
  <li>
    <a href="{{ p.documentation_url }}">
    <strong>{{ p.name }}</strong>
    </a>
    <br/>
    {{ p.description }}
  </li>
{% endfor %}
</ul>
