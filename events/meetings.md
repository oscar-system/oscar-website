---
layout: page
title: OSCAR Meetings
meeting: true
---

{% assign events = site.data.events | where: "satellite", "No" | group-by: "start-date" | sort: "end-date" | reverse %}

<ul>
  {% for event in events %}
    <li>
      <strong>{{ event.title }}</strong><br>
      <em>{{ event.start-date }} – {{ event.end-date }}</em><br>
      Location: {{ event.location }}<br>
      <a href="{{ event.website }}" target="_blank">More information</a>
    </li>
    <br>
  {% endfor %}
</ul>
