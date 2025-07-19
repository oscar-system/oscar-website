---
layout: default
title: Home
---

<h1 class="frontpage-headline">{{ site.title }}</h1>

Welcome to **OSCAR**, an innovative **Open Source Computer Algebra Research** system that powers cutting-edge computations in algebra, geometry, and number theory. Written in [Julia](https://julialang.org), OSCAR brings together powerful tools from diverse mathematical areas to tackle even the most complex computations.

Discover more about our project and vision on our [About]({{site.baseurl}}/about) page.

---

## 📅 Upcoming Events

{% assign sorted_conferences = site.data.events | group-by: "start-date" | sort: "end-date" %}
{% assign today = "now" | date: "%Y-%m-%d" %}
{% assign has_upcoming_events = false %}

{% for event in sorted_conferences %}
  {% if event.end-date >= today %}
    {% assign has_upcoming_events = true %}
* [{{ event.title }} ({{ event.location }}, {{ event.start-date | date: "%d %b %Y" }} to {{ event.end-date | date: "%d %b %Y" }})]({{ event.website | replace: "https://www.oscar-system.org", site.baseurl }})
  {% endif %}
{% endfor %}

{% unless has_upcoming_events %}
Currently no upcoming events.
{% endunless %}

---

## 🚀 Get OSCAR {{ site.data.release.version }}

_Released on {{ site.data.release.date | date_to_string }}_ -- [View release notes.](https://github.com/oscar-system/Oscar.jl/releases/tag/v{{ site.data.release.version }})

- Getting started is easy - [follow our installation guide here!]({{site.baseurl }}/install/)
- Already using OSCAR? [Click here to upgrade to the latest version.]({{ site.baseurl }}/upgrade/)

---

## 📚 Tutorials & Documentation

- [Hands-on Tutorials]({{site.baseurl }}/tutorials/).
- [Comprehensive Documentation]({{site.baseurl }}/documentation/).
- [Frequently Asked Questions (FAQ)](https://docs.oscar-system.org/stable/General/faq/).

---

## 📙 The OSCAR Book

The [OSCAR Book](https://book.oscar-system.org/) - A detailed guide to version 1.0, featuring code snippets and in-depth explanations.


---

## 🤝 Contact & Support

Need help or want to connect? Visit our [Contact & Support]({{site.baseurl}}/contact-and-support/) page.

---

## 🤖 Contribute to OSCAR

Are you a coder eager to help shape OSCAR? We are always happy to welcome new contributors! Learn how you can get involved on our [Contributing]({{site.baseurl}}/contributing/) page.

---

## 📝 Cite OSCAR

If you use OSCAR in your work, please cite us! Details can be found on the [Citing OSCAR]({{site.baseurl}}/credits/Citing-OSCAR/) page.

---

## 🏛️ Funding

The development of OSCAR is supported by the [German Research Foundation (DFG)](https://www.dfg.de/en) through the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/).
