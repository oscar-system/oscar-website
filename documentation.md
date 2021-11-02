---
layout: page
title: Documentation
---

Besides the
<a href="https://oscar-system.github.io/Oscar.jl/dev/">documentation for the OSCAR system itself</a>,
the following links to documentation for software projects encompassed by OSCAR
are useful.
Other projects are in development now, and will be announced soon.

Note that an aim of OSCAR is to combine and extend the capabilities of
Antic (<a href="https://github.com/thofma/Hecke.jl/">Hecke</a>,
<a href="http://nemocas.org">Nemo</a>),
<a href="https://www.gap-system.org/">GAP</a>,
<a href="https://polymake.org/doku.php">Polymake</a>, and
<a href="https://www.singular.uni-kl.de/">Singular</a>.

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
