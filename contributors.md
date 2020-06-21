---
layout: page
title: Contributors
---

## Active PIs

<ul>
{% for p in site.data.contributors %}
{% if p.is_active_PI == true %}
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

## Contributors

Currently, the following people contributed very significantly to the software in the
OSCAR project.
Additionally, people who are financed by the [SFB-TRR 195](https://www.computeralgebra.de/sfb/) mainly work on software
for the OSCAR project.

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
    {% if p.affiliation != null or p.paid_by_dfg == true %}
        (
        {% if p.affiliation != null %}
            {{ p.affiliation }}
        {% endif %}
        {% if p.paid_by_dfg == true %}
            {% if p.affiliation != null %}
            ,
            {% endif %}
            financed by the <a href="https://www.computeralgebra.de/sfb/">SFB-TRR 195</a>
        {% endif %}
        )
    {% endif %}

</li>
    {% endfor %}
</ul>
