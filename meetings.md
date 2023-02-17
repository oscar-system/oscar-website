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

For more OSCAR-related meetings, please also take a look at the [meetings of the SFB - TRR 195](https://www.computeralgebra.de/sfb/events/).
