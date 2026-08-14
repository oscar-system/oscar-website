---
layout: meeting
title: Meeting 10/2022
meeting: true
meeting_nr: 202210
is_meeting_index: true
---

# OSCAR workshop

## October 10 - 14, Uni Saarbrücken

## Information

For more information, see
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
[Claus Fieker](mailto:fieker@mathematik.uni-kl.de) and
[Max Horn](mailto:horn@mathematik.uni-kl.de).

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic Tools in Mathematics and their Application.
