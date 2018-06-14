---
layout: page
title: Credits
---

## Software used in the OSCAR project

### Mathematical software

The following mathematical Open Source mathematical software is used in the OSCAR project:

{% assign entries = site.data.used_software | sort_natural:"name" %}
<ul>
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

## Contributors

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
