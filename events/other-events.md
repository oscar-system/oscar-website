---
layout: page
title: OSCAR Related Events
meeting: true
---

---

These events are not organized by OSCAR, but include talks or sessions relevant to the OSCAR user and developer community.

Some of them are organized within the [SFB-TRR 195](https://www.computeralgebra.de/sfb/events/) collaborative research project.  
For a full list of SFB-TRR 195 meetings and activities, see their [event calendar](https://www.computeralgebra.de/sfb/events/).

---

{% assign events = site.data.events | where: "other", "Yes" | group-by: "start-date" | sort: "end-date" | reverse %}

<ul>
  {% for event in events %}
    <li>
      <strong>{{ event.title }}</strong><br>
      <em>{{ event.start-date | date: site.full_date_format }} – {{ event.end-date | date: site.full_date_format }}</em><br>
      Location: {{ event.location }}<br>
      {% if event.supplementary %}
        <a href="{{ event.supplementary }}" target="_blank" rel="noopener noreferrer">Supplementary Material</a><br>
      {% endif %}
      {% if event.website %}
        {% comment %}Related events use external websites, which open in an isolated new tab.{% endcomment %}
        <a href="{{ event.website }}" target="_blank" rel="noopener noreferrer">More information</a>
      {% endif %}
    </li>
    <br>
  {% endfor %}
</ul>
