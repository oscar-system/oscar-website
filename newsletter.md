---
layout: page
title: OSCAR Newsletter
---

---

The OSCAR Newsletter is a low-traffic mailing list. It provides occasional updates about

* new OSCAR releases, features, and important changes,
* papers and projects using OSCAR,
* upcoming events, workshops, and coding sprints,
* news from the wider OSCAR community.

---

### Subscribe

Follow the instructions at <https://lists.uni-kl.de/oscar/info/news>.

---

### Past Issues

{% assign newsletters = site.data.newsletters | sort: "date" | reverse %}

<ul>
  {% for n in newsletters %}
  <li>
    <a href="{{ site.baseurl }}{{ n.url }}">
      Newsletter #{{ forloop.rindex }} — {{ n.date | date: "%b %-d %Y" }}
    </a>
  </li>
  {% endfor %}
</ul>