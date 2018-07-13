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
                    <a href="{{ node.url  | absolute_url }}">{{ node.title }}</a>
                    <ul>
                    {% for node_inner in pages_list %}
                        {% if node_inner.meeting_nr == node.meeting_nr and node_inner.is_meeting_index != true %}
                            <li>
                                <a href="{{ node_inner.url | absolute_url }}">{{node_inner.title}}</a>
                            </li>
                        {% endif %}
                    {% endfor %}
                    </ul>
                </li>
            {% endif %}
        {% endif %}
    {% endfor %}
</ol>
