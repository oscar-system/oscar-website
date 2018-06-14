---
layout: page
title: Documentation
---

The OSCAR project initially encompasses a number of different software projects.
As the OSCAR system is still under development, there is no single source for user
documentation. 

Below are links to documentation for projects that are already fairly extensively
documented. Other projects are in development now, and will be announced soon.

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
