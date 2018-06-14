---
layout: page
title: Credits
---

## Software used in the OSCAR project

The following Open Source mathematical software is used in the OSCAR project:

<ul>
{% for p in site.data.used_software %}
  <li>
    <a href="{{ p.website }}">
    <strong>{{ p.name }}</strong>
    </a>
  </li>
{% endfor %}
</ul>


## Contributors

Currently, the following people contributed very significantly to the software in the
OSCAR project:

<ul>
{% for p in site.data.contributors %}
  <li>
    {% if p.website != null %}
        <a href="{{ p.website }}">
        {% assign link_open = true %}
    {% elsif p.email != null %}
        <a href="mailto:{{ p.email }}">
        {% assign link_open = true %}
    {% endif %}
    <strong>{{ p.name }}</strong>{% if link_open %}</a>{% assign link_open = false %}{% endif %}
    {% if p.affiliation != null %} ({{ p.affiliation }}){% endif %}
  </li>
{% endfor %}
</ul>
