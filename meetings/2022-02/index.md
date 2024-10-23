---
layout: meeting
title: Meeting 02/2022
meeting: true
meeting_nr: 202202
is_meeting_index: true
weight: 1
---

# OSCAR developer meeting - Tropical Geometry

## February 28 - March 4,<br> TU Kaiserslautern / Virtual

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

If you have questions or suggestions, please contact the organizers:
* [Yue Ren](mailto:yue.ren2@durham.ac.uk)
* [Hans Schoenemann](mailto:hannes@mathematik.uni-kl.de)

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic Tools in Mathematics and their Application.

## Other meetings

Please visit [the meetings page]({{ site.baseurl }}/meetings) for an overview of the OSCAR meetings.
