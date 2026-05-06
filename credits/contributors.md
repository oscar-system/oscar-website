---
layout: page
title: Contributors

# The data resides in _data/contributors.yml
# In the datafile, all three entries, `affiliation`, `email`, and
# `website` are optional. If you provide an `email` and a `website`, the
# name will link to the website.

---

---

Many wonderful people have contributed to OSCAR in many ways. Our thanks
extend to all of them!

On this page we mention just a subset: those who
contributed code to one of the Julia packages listed on the
[Contributing to OSCAR]({{site.baseurl}}/contributing/#contributing-source-code)
page.

---

## Project leaders

<ul>
{% for p in site.data.contributors %}
  {% if p.status == "pi" %}
    <li>
      <a href="{{ p.website }}"><strong>{{ p.name }}</strong></a>, {{ p.affiliation }}
      {% if p.github != null %}
        — <a href="https://github.com/{{ p.github }}">{{ p.github }} on GitHub</a>
      {% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

---

## Current Code Contributors
These {{ site.data.contributors | where: "status", "active" | size }} individuals have contributed source code to the OSCAR project in the past 12 months (as of {{ 'now' | date: site.full_date_format }}).

<ul>
{% for p in site.data.contributors %}
  {% if p.status == "active" %}
  <li>
    {% if p.website != null %}
        <a href="{{ p.website }}">
        {% assign link_open = true %}
    {% elsif p.email != null %}
        <a href="mailto:{{ p.email }}">
        {% assign link_open = true %}
    {% endif %}
    <strong>{{ p.name }}</strong>{% if link_open %}</a>{% assign link_open = false %}{% endif %}
    {%- if p.affiliation != null or p.paid_by_dfg == true -%}
    <em>
        {%- if p.affiliation != null -%}
            , {{ p.affiliation }}
        {%- endif -%}
        {%- if p.paid_by_dfg == true -%}
            {%- if p.affiliation != null -%},{% endif %}
            financed by the <a href="https://www.computeralgebra.de/sfb/">SFB-TRR 195</a>
        {%- endif -%}
      </em>
    {% endif %}
    {%- if p.github != null %}
      — <a href="https://github.com/{{ p.github }}">{{ p.github }} on GitHub</a>
    {%- endif -%}
  </li>
  {% endif %}
{% endfor %}
</ul>

---

## Former Code Contributors

The following {{ site.data.contributors | where: "status", "retired" | size }} individuals contributed to the OSCAR project in the past but have not in the last 12 months (as of {{ 'now' | date: site.full_date_format }}).

<ul>
{% for p in site.data.contributors %}
  {% if p.status == "retired" %}
  <li>
    {% if p.website != null %}
        <a href="{{ p.website }}">
        {% assign link_open = true %}
    {% elsif p.email != null %}
        <a href="mailto:{{ p.email }}">
        {% assign link_open = true %}
    {% endif %}
    <strong>{{ p.name }}</strong>{% if link_open %}</a>{% assign link_open = false %}{% endif %}
    {%- if p.affiliation != null or p.paid_by_dfg == true -%}
    <em>
        {%- if p.affiliation != null -%}
            , {{ p.affiliation }}
        {%- endif -%}
        {%- if p.paid_by_dfg == true -%}
            {%- if p.affiliation != null -%},{% endif %}
            financed by the <a href="https://www.computeralgebra.de/sfb/">SFB-TRR 195</a>
        {%- endif -%}
    </em>
    {% endif %}
    {%- if p.github != null %}
      — <a href="https://github.com/{{ p.github }}">{{ p.github }} on GitHub</a>
    {%- endif -%}
  </li>
  {% endif %}
{% endfor %}
</ul>
