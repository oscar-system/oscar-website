---
layout: page
title: Contributors
---

Currently, the following people contributed very significantly to the software in the
OSCAR project:

{% assign entries = site.data.contributors | sort_natural:"name" %}
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

## Contributors financed by the DFG SFB-TRR 195 (2017 - 2020)

Additionally, the following people were or are financed by the [SFB-TRR 195](https://www.computeralgebra.de/sfb/) to mainly work on software
for the OSCAR project:

<ul>
{% for p in site.data.contributors %}
{% if p.paid_by_dfg == true %}
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
{% endif %}
{% endfor %}
</ul>
