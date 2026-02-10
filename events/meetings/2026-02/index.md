---
layout: meeting
title: OSCAR Coding Sprint 02/2026
meeting: true
meeting_nr: 202602
is_meeting_index: true
weight: 1
---

# OSCAR Coding Sprint

* When: February 23 - February 27, 2026.
* Where: TU Berlin, [E-N Building (Einsteinufer 17)](https://maps.app.goo.gl/najYFhEHoJfoQWB1A)
* What: A general coding sprint for OSCAR and OSCAR adjacent projects (polymake, Singular, ...)
* Who: OSCAR developers and enthusiasts

If you wish to particpate, **please register** by sending an email to both [Kevin Kühn](mailto:kuehn@math.tu-berlin.de) and
[Igor Makhlin](mailto:iymakhlin@gmail.com).

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

Hotel suggestions:
 - [B&B HOTEL Berlin-Tiergarten](https://www.hotel-bb.com/en/hotel/berlin-tiergarten?arrival_date=02%2F23%2F2026&departure_date=02%2F27%2F2026&destination=Berlin-Tiergarten)
 - [Holiday Inn - the niu, Flash Berlin Charlottenburg](https://www.ihg.com/hotels/us/en/find-hotels/select-roomrate?qDest=Franklinstraße%2025,%20Berlin,%20DE&qPt=CASH&qCiD=23&qCoD=27&qCiMy=012026&qCoMy=012026&qAdlt=1&qChld=0&qRms=1&qIta=99618783&qRtP=6CBARC&qSlH=BERFB)
 - [Garner Hotel Berlin - Charlottenburg](https://www.ihg.com/hotels/us/en/find-hotels/select-roomrate?qDest=Franklinstra%C3%9Fe%2022,%20Berlin,%20DE&qPt=CASH&qCiD=23&qCoD=27&qCiMy=012026&qCoMy=012026&qAdlt=1&qChld=0&qRms=1&qIta=99618783&qRtP=6CBARC&qSlH=BERSY&qRmFltr=)

## Contact

If you have questions or suggestions, please contact the organizers,
[Kevin Kühn](mailto:kuehn@math.tu-berlin.de) and
[Igor Makhlin](mailto:iymakhlin@gmail.com).

## Sponsors

This workshop is supported by [SFB-TRR 195](https://www.computeralgebra.de/sfb/) -- Symbolic
Tools in Mathematics and their Application.
