---
layout: meeting
title: Meeting 11/2018
meeting: true
meeting_nr: 201811
is_meeting_index: true
redirect_from:
  - /meetings/Meeting-11-2018/
---

# OSCAR developer meeting

## November 2018,<br> TU Berlin

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

* [Michael Joswig](mailto:joswig@math.tu-berlin.de)

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic Tools in Mathematics and their Application.

## Other meetings

Please visit [the meetings page]({{ site.baseurl }}/meetings) for an overview of the OSCAR meetings.
