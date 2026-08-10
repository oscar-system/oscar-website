---
layout: page
title: OSCAR Meetings
meeting: true
---

---

{% assign events = site.data.events | where: "other", "No" | group-by: "start-date" | sort: "end-date" | reverse %}

<ul>
  {% for event in events %}
    <li>
      <strong>{{ event.title }}</strong><br>
      <em>{{ event.start-date | date: site.full_date_format }} – {{ event.end-date | date: site.full_date_format }}</em><br>
      Location: {{ event.location }}<br>
      {% if event.website %}
        {% comment %}Use baseurl for OSCAR-hosted pages so links also work in local and GitHub Pages builds; open only external sites in a new tab.{% endcomment %}
        {% assign event_url = event.website | replace: "https://www.oscar-system.org", site.baseurl %}
        <a href="{{ event_url }}"{% unless event.website contains "https://www.oscar-system.org" %} target="_blank" rel="noopener noreferrer"{% endunless %}>More information</a>
      {% endif %}
    </li>
    <br>
  {% endfor %}
</ul>
