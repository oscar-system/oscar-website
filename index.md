---
layout: default
title: Home
---

<h1 class="frontpage-headline">{{ site.title }}</h1>

---

Welcome to **OSCAR**, an innovative **Open Source Computer Algebra Research** system that powers cutting-edge computations in algebra, geometry, and number theory. Written in [Julia](https://julialang.org), OSCAR brings together powerful tools from diverse mathematical areas to tackle even the most complex computations.

Discover more about our project and vision on our [About]({{site.baseurl}}/about) page.

Questions about OSCAR, stuck on an example, or missing features (e.g., from GAP, Polymake, or Singular)? Join our [Slack channel]({{site.baseurl}}/contact-and-support/#slack) — beginners and first-time users are very welcome.

---

## 📅 Upcoming Events

{% assign sorted_conferences = site.data.events | group-by: "start-date" | sort: "end-date" %}
{% assign today = "now" | date: "%Y-%m-%d" %}
{% assign upcoming_conferences = sorted_conferences | where_exp: "event", "event['end-date'] >= today" %}
{% assign max_events = site.number_of_displayed_events_on_index_page %}

{% if upcoming_conferences.size > 0 %}
  {% for event in upcoming_conferences limit:max_events %}
    {% if event.website %}
  * [{{ event.title }} ({{ event.location }}, {{ event.start-date | date: site.full_date_format }} to {{ event.end-date | date: site.full_date_format }})]({{ event.website | replace: "https://www.oscar-system.org", site.baseurl }})
    {% else %}
  * {{ event.title }} ({{ event.location }}, {{ event.start-date | date: site.full_date_format }} to {{ event.end-date | date: site.full_date_format }})
    {% endif %}
  {% endfor %}
  {% if upcoming_conferences.size > max_events %}
More upcoming events are available [here]({{ site.baseurl }}/events/).
  {% endif %}  
{% else %}
  Currently no upcoming events.
{% endif %}

---

## 🚀 Get OSCAR {{ site.data.release.version }}

_Released on {{ site.data.release.date | date: site.full_date_format }}_ -- [View release notes.](https://github.com/oscar-system/Oscar.jl/releases/tag/v{{ site.data.release.version }})

- Getting started is easy - [follow our installation guide here!]({{site.baseurl }}/install/)
- Already using OSCAR? [Click here to upgrade to the latest version.]({{ site.baseurl }}/upgrade/)

---

## 📚 Tutorials & Documentation

- [Hands-on Tutorials]({{site.baseurl }}/tutorials/).
- [Comprehensive Documentation]({{site.baseurl }}/documentation/).
- [Frequently Asked Questions (FAQ)](https://docs.oscar-system.org/stable/General/faq/).

---

## 🎬 Videos

The OSCAR Video Channel features interviews with contributors and demonstrations of OSCAR's capabilities.

📺 **Visit the [OSCAR Video Channel](https://tube.mathe.social/a/oscar/videos).**

---

## 📙 The OSCAR Book

The [OSCAR Book](https://book.oscar-system.org/) - A detailed guide to version 1.0, featuring code snippets and in-depth explanations.

---

## 🤝 Contact & Support

Need help or want to connect? Visit our [Contact & Support]({{site.baseurl}}/contact-and-support/) page.

---

## 📰 Newsletter

Stay up to date with OSCAR releases, papers, events, and community news via the [OSCAR Newsletter]({{ site.baseurl }}/newsletter/).

---

## 🤖 Contribute to OSCAR

There are many ways to get involved — from reporting problems and suggesting improvements to contributing directly to OSCAR’s codebase. Another option is the [**Friends of OSCAR**](https://github.com/oscar-system/FriendsOfOscar) initiative, which highlights independent software projects that build upon OSCAR.

Learn more about these and other ways to contribute on our [Contributing page]({{site.baseurl}}/contributing/).

---

## 📝 Cite OSCAR

If you use OSCAR in your work, please cite us! Details can be found on the [Citing OSCAR]({{site.baseurl}}/credits/Citing-OSCAR/) page.

----

## 🏛 Funding

The development of OSCAR is supported by the [German Research Foundation (DFG)](https://www.dfg.de/en) through the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/).
