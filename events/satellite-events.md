---
layout: page
title: Satellite Events
meeting: true
---

SFB-TRR 195 events are listed [here](https://www.computeralgebra.de/sfb/events/). In addition, the following events are relevant to the OSCAR community.

{% assign events = site.data.events | where: "satellite", "Yes" | group-by: "start-date" | sort: "end-date" | reverse %}

<ul>
  {% for event in events %}
    <li>
      <strong>{{ event.title }}</strong><br>
      <em>{{ event.start-date }} – {{ event.end-date }}</em><br>
      Location: {{ event.location }}<br>
      <a href="{{ event.website | replace: "https://www.oscar-system.org", site.baseurl }}" target="_blank">More information</a>
    </li>
    <br>
  {% endfor %}
</ul>
