---
layout: meeting
title: Summer School 09/2021
meeting: true
meeting_nr: 202109
is_meeting_index: true
---

# Summer School “Computer algebra”

## September 6 - 10,<br> Virtual Reality

<p class="message">
Attention: Due to recent developments, the summer school cannot take place in Aachen.
Instead, it will be done completely online. We will use
<a href="https://www.gather.town">gather.town</a> and other tools.
</p>

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

If you have questions or suggestions, please contact the organizers:

* [Claus Fieker](mailto:fieker@mathematik.uni-kl.de),
  [Max Horn](mailto:horn@mathematik.uni-kl.de),
  [Thomas Breuer](mailto:sam@math.rwth-aachen.de),
  [Tommy Hofmann](mailto:thofmann@mathematik.uni-kl.de)

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic Tools in Mathematics and their Application.

## Other meetings

Please visit [the meetings page]({{ site.baseurl }}/meetings) for an overview of the OSCAR meetings.
