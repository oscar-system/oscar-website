---
layout: default
title: Home
---

<div class="github-ribbon">
  <a target="_blank" href="https://github.com/oscar-system/Oscar.jl/">Go to the code repository</a>
</div>

# {{ site.title }}

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
* [{{ event.title }} ({{ event.location }}, {{ event.start-date | date: "%d %b %Y" }} to {{ event.end-date | date: "%d %b %Y" }})]({{ event.website }})
  {% endif %}
{% endfor %}

{% unless has_upcoming_events %}
Currently no upcoming events.
{% endunless %}

---

## 🚀 Get OSCAR Now!

Getting started with OSCAR is easy. [**Start your journey now!**]({{site.baseurl}}/getting-started/)

---
## 📙 The OSCAR Book

The [OSCAR Book](https://book.oscar-system.org/) – A detailed guide to version 1.0, featuring code snippets and in-depth explanations.

---

## 📚 Documentation & Tutorials

- Comprehensive [Documentation]({{site.baseurl }}/getting-started/documentation/).
- Hands-on [Tutorials]({{site.baseurl }}/getting-started/tutorials/).

---

## 🤖 Contribute to OSCAR

Are you a coder eager to help shape OSCAR? We are always happy to welcome new contributors! Learn how you can get involved on our [Contributing]({{site.baseurl}}/contributing/) page.

---

## 🤝 Contact & Support

Need help or want to connect? Visit our [Contact & Support]({{site.baseurl}}/contact-and-support/) page.

---

## 📝 Cite OSCAR

If you use OSCAR in your work, please cite us! Details can be found on the [Citing OSCAR]({{site.baseurl}}/credits/Citing-OSCAR/) page.

---

## 💡 Funding

The development of OSCAR is supported by the German Research Foundation (DFG) through the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/).
