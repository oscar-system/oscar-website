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

<style>
ul.newsletters {
  list-style: none;
  padding-left: 0;
}

ul.newsletters li {
  margin: 0 0 1rem 0;
  padding: .6rem .75rem;
  border: 1px solid #dbd2d2;
  border-radius: .5rem;
}

.newsletter-meta {
  color: #555;
  margin-top: .15rem;
  font-size: .95em;
}
</style>

{% assign newsletters = site.data.newsletters | sort: "date" | reverse %}

<ul class="newsletters">
  {% for n in newsletters %}
  <li>
    <a href="{{ n.url }}">
      {{ n.date | date: "%B %Y" }} Newsletter
    </a>
    <span class="newsletter-meta">
      — released on {{ n.date | date: "%Y-%m-%d" }}
    </span>
  </li>
  {% endfor %}
</ul>

