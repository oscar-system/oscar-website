---
layout: page
title: Publications citing OSCAR
---

Below is an incomplete list of publications citing OSCAR. A more complete list is avaiable [here](https://zbmath.org/?q=si:36845).

<ul>
  {% for p in site.data.OSCAR-credits %}
  <li>
    {% if p.url %}
      <a href="{{ p.url }}">
    {% endif %}
    <strong>{{ p.name }}</strong>
    {% if p.url %}</a>{% endif %}

    {% if p.authors %}{{ p.authors }} - {% endif %}
    {% if p.journal %}{{ p.journal }}, {% else %}Preprint, {% endif %}
    {% if p.volume %}{{ p.volume }} {% endif %}
    {% if p.month %}{{ p.month }} {% endif %}
    {% if p.year %}{{ p.year }}, {% endif %}
    {% if p.doi %}{{ p.doi }}{% endif %}
  </li>
  {% endfor %}
</ul>
