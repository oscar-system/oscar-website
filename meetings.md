---
layout: page
title: OSCAR Meetings
meeting: true
---

<ol>
    {% assign pages_list = site.pages | sort:"name" %}
    {% for node in pages_list %}
        {% if node.title != null %}
            {% if node.is_meeting_index %}
                <li>
                    <a href="{{ site.baseurl }}{{ node.url }}">{{ node.title }}</a>
                </li>
            {% endif %}
        {% endif %}
    {% endfor %}
</ol>