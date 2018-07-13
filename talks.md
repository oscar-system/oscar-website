---
layout: page
title: Talks and conferences
---

A collection of talks about the OSCAR project, given on various conferences:

{% assign entries = site.data.talks %}
<ul>
{% for p in entries %}
{% assign has_link = false %}
  <li>
    {{ p.author }}:<br/>
    {% if p.pdf_url != null %}
        {% assign has_link = true %}
        <a href="{{ p.pdf_url }}">
    {% elsif p.pdf != null %}
        {% assign has_link = true %}
        <a href="{{ site.baseurl }}public/{{ p.pdf }}">
    {% endif %}
    <emph>{{ p.title }}</emph>
    {% if has_link == true %}
        </a>
    {% endif %}
    <br/>
    {{ p.location }}, {{ p.date }}
  </li>
{% endfor %}
</ul>
