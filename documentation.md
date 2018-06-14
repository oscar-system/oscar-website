---
layout: page
title: Documentation
---

The OSCAR project is formed of several different software projects. Currently, as
OSCAR is still under development, there is no single documentation for the project.
However, you can access the documentation for several parts here:

<ul>
{% for p in site.data.documentation_pages %}
  <li>
    <a href="{{ p.documentation_url }}">
    <strong>{{ p.name }}</strong>
    </a>
    <br/>
    {{ p.description }}
  </li>
{% endfor %}
</ul>
