---
layout: page
title: Credits
---

## Software used in the OSCAR project

### Mathematical software

The OSCAR project is based on the following mathematical software:

{% assign entries = site.data.used_software | sort_natural:"name" %}
<ul class="software_credits_list">
{% for p in entries %}
  <li>
    <a href="{{ p.website }}">
    <strong>{{ p.name }}</strong>
    </a>
  </li>
{% endfor %}
</ul>

### Technical software

The following software is used as technical components in the OSCAR project:

{% assign entries = site.data.used_software_technical | sort_natural:"name" %}
<ul>
{% for p in entries %}
  <li>
    <a href="{{ p.website }}">
    <strong>{{ p.name }}</strong>
    </a>
  </li>
{% endfor %}
</ul>

## Citations of Oscar and its components

### Papers

<ul>
  {% for p in site.data.citations %}
  <li>
      {% if p.url != null %}
          <a href="{{ p.url }}">
          {% assign link_open = true %}
      {% endif %}
      <strong>{{ p.name }}</strong>{% if link_open %}</a>{% assign link_open = false %}{% endif %}
      {% if p.authors != null %} ({{p.authors }}){% endif %}
  </li>
  {% endfor %}
</ul>
