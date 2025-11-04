---
layout: meeting
title: OSCAR Coding Sprint 03/2025
meeting: true
meeting_nr: 202503
is_meeting_index: true
weight: 1
---

# OSCAR Coding Sprint

* When: February 23 - February 27, 2026.
* Where: TU Berlin, E-N Building (Einsteinufer 17)
* What: A general coding sprint for OSCAR and OSCAR adjacent projects (polymake, Singular, ...)
* Who: OSCAR developers and enthusiasts

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
[Kevin Kühn](mailto:kuehn@math.tu-berlin.de) and
[Igor Makhlin](mailto:iymakhlin@gmail.com).

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic
Tools in Mathematics and their Application.
