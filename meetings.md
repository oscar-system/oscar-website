---
layout: page
title: OSCAR Meetings
meeting: true
---

<ol reversed>
    {% assign pages_list = site.pages | where: "is_meeting_index", "true" | sort: "meeting_nr" %}
    {% for node in pages_list reversed %}
        {% if node.title != null %}
            <li><a href="{{ node.url  | relative_url }}">{{ node.title }}</a></li>
        {% endif %}
    {% endfor %}
</ol>
