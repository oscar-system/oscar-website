---
layout: meeting
title: Participants
meeting: true
meeting_nr: 201906
---

<ol>
{% for p in site.data.participants_meeting_2019-06 %}
  <li>
    <strong>{{ p.name }}</strong>
    {% if p.affiliation != null %} ({{ p.affiliation }}){% endif %}
    {% if p.links != null %}
        {% for item in p.links %}
            <a href="{{ item[1] }}">({{ item[0] }})</a>
        {% endfor %}
    {% endif %}
    <br/>
      {% if p.talk != null %} Talk: {{ p.talk }}{% endif %}
  </li>
{% endfor %}
</ol>
