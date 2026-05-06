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

Enter your email address [here](https://lists.uni-kl.de/oscar/subscribe/news), click **Submit** and follow the on-screen instructions.

Alternatively, send a message from the email address that should receive the newsletter to [sympa@oscar-system.org](mailto:sympa@oscar-system.org?subject=subscribe%20news%20Firstname%20Lastname). In the subject line, write `subscribe news Firstname Lastname` (use your own first and last name). Leave the email body blank.

---

### Past Issues

{% assign newsletters = site.data.newsletters | sort: "date" | reverse %}

<ul>
  {% for n in newsletters %}
  <li>
    <a href="{{ site.baseurl }}{{ n.url }}">
      Newsletter #{{ forloop.rindex }} — {{ n.date | date: site.full_date_format }}
    </a>
  </li>
  {% endfor %}
</ul>