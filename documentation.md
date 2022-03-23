---
layout: page
title: Documentation
---

<p class="message">
You can find the OSCAR manual here:
 - [for the latest development version of Oscar.jl](https://oscar-system.github.io/Oscar.jl/dev)
<!-- - [for the latest stable release of Oscar.jl](https://oscar-system.github.io/Oscar.jl/latest) -->
</p>

Note that an aim of OSCAR is to combine and extend the capabilities of
Antic (<a href="https://github.com/thofma/Hecke.jl/">Hecke</a>,
<a href="http://nemocas.org">Nemo</a>),
<a href="https://www.gap-system.org/">GAP</a>,
<a href="https://polymake.org/doku.php">Polymake</a>, and
<a href="https://www.singular.uni-kl.de/">Singular</a>.

Below are links to documentation for Julia software projects
encompassed by OSCAR.
Other projects are in development now, and will be announced soon.

{% assign entries = site.data.documentation_pages | sort_natural:"name" %}
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
