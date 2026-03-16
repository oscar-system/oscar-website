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

You can join the OSCAR newsletter in two ways:

1. **Web subscription:**
  Enter your email address [here](https://lists.uni-kl.de/oscar/subscribe/news), click **Subscribe** and follow the on-screen instructions to confirm your subscription.

2. **Email subscription:**
  From the email address that you want to receive the newsletter at, send an email to `sympa@oscar-system.org`. In the subject line, write: `subscribe news Firstname Lastname` (use your own first and last name). Leave the email body blank.

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