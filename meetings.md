---
layout: page
title: OSCAR Meetings
meeting: true
---

<ol reversed>
    {% assign pages_list = site.pages | sort: "meeting_nr" %}
    {% for node in pages_list reversed %}
        {% if node.title != null %}
            {% if node.is_meeting_index %}
                <li>
                    <a href="{{ node.url  | relative_url }}">{{ node.title }}</a>
                    <ul>
                    {% for node_inner in pages_list %}
                        {% if node_inner.meeting_nr == node.meeting_nr and node_inner.is_meeting_index != true %}
                            <li>
                                <a href="{{ node_inner.url | relative_url }}">{{node_inner.title}}</a>
                            </li>
                        {% endif %}
                    {% endfor %}
                    </ul>
                </li>
            {% endif %}
        {% endif %}
    {% endfor %}
</ol>
