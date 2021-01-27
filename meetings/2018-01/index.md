---
layout: meeting
title: Meeting 01/2018
meeting: true
meeting_nr: 201801
is_meeting_index: true
redirect_from:
  - /meetings/Meeting-1-2018/
---

# OSCAR developer meeting

## January 2018,<br> RWTH Aachen University

## Information

For more information, see
{% assign pages_list = site.pages | sort:"name" %}
<ul>
{% for node_inner in pages_list %}
    {% if node_inner.meeting_nr == page.meeting_nr and node_inner.is_meeting_index != true %}
        <li>
            <a href="{{ node_inner.url | relative_url }}">{{node_inner.title}}</a>
        </li>
    {% endif %}
{% endfor %}
</ul>

## Contact

If you have questions or suggestions, please contact the organizers:

* [Sebastian Gutsche](mailto:gutsche@mathematik.uni-siegen.de)
* [Frank Lübeck](mailto:frank.luebeck@math.rwth-aachen.de)

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic Tools in Mathematics and their Application.

## Other meetings

Please visit [the meetings page]({{ site.baseurl }}/meetings) for an overview of the OSCAR meetings.

