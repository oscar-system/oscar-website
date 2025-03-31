---
layout: meeting
title: OSCAR Coding Sprint 03/2025
meeting: true
meeting_nr: 202503
is_meeting_index: true
weight: 1
---

# OSCAR Coding Sprint

* When: March 31 - April 04, 2025.
* Where: [RPTU Kaiserslautern](https://math.rptu.de/en/home), Gottlieb-Daimler-Straße 48, 67663
Kaiserslautern, rooms 48-436 and 48-419 (as well as 48-438 in the mornings)
* What: A general coding sprint for OSCAR and OSCAR adjacent projects (GAP, Singular, ...)
* Who: OSCAR developers

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
[Max Horn](mailto:max.horn@rptu.de).

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic
Tools in Mathematics and their Application.
