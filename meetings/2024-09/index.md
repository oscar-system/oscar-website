---
layout: meeting
title: Meeting 09/2024
meeting: true
meeting_nr: 202409
is_meeting_index: true
weight: 1
---

# OSCAR workshop

## September 16 - 20, RPTU Kaiserslautern-Landau

## Information

{% assign subpages = site.pages | where: "meeting_nr", page.meeting_nr | sort: "name" %}
<ul>
{% for node_inner in subpages %}
    {% if node_inner.is_meeting_index != true %}
        <li>
            <a href="{{ node_inner.url | relative_url }}">{{node_inner.title}}</a>
        </li>
    {% endif %}
{% endfor %}
</ul>

## Contact

If you have questions or suggestions, please contact the organizers,
[Claus Fieker](mailto:claus.fieker@rptu.de) and
[Max Horn](mailto:mhorn@rptu.de).

## Sponsors

This workshop is supported by
* [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic Tools in Mathematics and their Application
