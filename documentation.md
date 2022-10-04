---
layout: page
title: Documentation
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
