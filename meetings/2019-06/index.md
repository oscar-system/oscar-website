---
layout: meeting
title: Meeting 06/2019
meeting: true
meeting_nr: 201906
is_meeting_index: true
redirect_from:
  - /meetings/Meeting-06-2019/
---

# OSCAR developer meeting

## June 11 - June 14 ,<br> TU Kaiserslautern

![alt text](IMG_7429.JPG "Participants")

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
* [William Hart](mailto:wbhart@mathematik.uni-kl.de)

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic Tools in Mathematics and their Application.

## Other meetings

Please visit [the meetings page]({{ site.baseurl }}/meetings) for an overview of the OSCAR meetings.
