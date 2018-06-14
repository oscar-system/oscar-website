---
layout: page
title: Community
---

Currently, the following people contributed to the software in the OSCAR project:

<ol>
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
</ol>
