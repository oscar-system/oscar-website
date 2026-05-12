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
        <a href="{{ event.website | replace: "https://www.oscar-system.org", site.baseurl }}" target="_blank">More information</a>
      {% endif %}
    </li>
    <br>
  {% endfor %}
</ul>
