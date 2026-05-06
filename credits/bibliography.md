---
layout: page
title: Bibliography
---

---

> Below is a curated selection of OSCAR-related publications. For a more comprehensive list, you may also visit [zbMATH](https://zbmath.org/?q=si%3A36845).
>
> If you are aware of an important work that should be included, please refer to the [Contributing Publications]({{site.baseurl}}/contributing/#contributing-publications) section for details.

<style>
  ul.pubs { list-style: none; padding-left: 0; }
  ul.pubs li { margin: 0 0 1.1rem 0; padding: .6rem .75rem; border: 1px solid #eee; border-radius: .5rem; }
  .pub-title { font-weight: 700; }
  .meta { color: #555; margin-top: .15rem; font-size: .95em; }
  .badges { margin-top: .35rem; display: flex; gap: .4rem; flex-wrap: wrap; }
  .badge { display: inline-block; padding: .15rem .45rem; border-radius: .45rem; font-size: .85em; text-decoration: none; border: 1px solid transparent; }
  .badge-journal { background: #eef8ff; border-color: #cce6ff; }
  .badge-preprint { background: #eefaf0; border-color: #cdeed6; }
  .badge-doi { background: #f8f5ff; border-color: #e6dcff; }
  .sep { margin: 0 .25rem; color: #bbb; }
</style>

<ul class="pubs">

{% assign months = "Dec,Nov,Oct,Sep,Aug,Jul,Jun,May,Apr,Mar,Feb,Jan" | split: "," %}
{% assign  P = site.data.OSCAR-credits | group_by: "year" %}
{% for smallp in P %}
  {% assign monthItems = '' | split: '' %}
  {% assign nonMonthItems = '' | split: '' %}
    {% for smallq in smallp.items %}
    {% if smallq.month%}
      {% assign monthItems = monthItems | push: smallq %}
    {% else %}
      {% assign nonMonthItems = nonMonthItems | push: smallq | sort: "name" %}
    {% endif %}
    {% endfor %}
{% for p in nonMonthItems %}
  <li>
      <div class="pub-title">
        {% if title_href %}
          <a href="{{ title_href }}">{{ p.name }}</a>
        {% else %}
          {{ p.name }}
        {% endif %}
      </div>

      <div class="meta">
        {% if p.authors %}{{ p.authors }}{% endif %}
        {% if p.authors and p.journal or p.authors and p.year or p.authors and p.month or p.authors and p.volume %}
          <span class="sep">•</span>
        {% endif %}
        {% if p.journal %}{{ p.journal }}{% else %}Preprint{% endif %}
        {% if p.volume %}, Vol. {{ p.volume }}{% endif %} | 
        {% if p.month %}
          {{ p.month | append: ' ' | append: p.year | date: site.month_date_format }}
        {% elsif p.year %}
          {{ p.year }}
        {% endif %}
      </div>

      <div class="badges">
        {% if p.journal_url %}
          <a class="badge badge-journal" href="{{ p.journal_url }}">Journal</a>
        {% endif %}
        {% if p.preprint_url %}
          <a class="badge badge-preprint" href="{{ p.preprint_url }}">Preprint</a>
        {% endif %}
      </div>
    </li>
{% endfor %}
{% for month in months %}
  {% for p in monthItems %}
  {% if p.month == month %}
    <li>
      <div class="pub-title">
        {% if title_href %}
          <a href="{{ title_href }}">{{ p.name }}</a>
        {% else %}
          {{ p.name }}
        {% endif %}
      </div>

      <div class="meta">
        {% if p.authors %}{{ p.authors }}{% endif %}
        {% if p.authors and p.journal or p.authors and p.year or p.authors and p.month or p.authors and p.volume %}
          <span class="sep">•</span>
        {% endif %}
        {% if p.journal %}{{ p.journal }}{% else %}Preprint{% endif %}
        {% if p.volume %}, Vol. {{ p.volume }}{% endif %} | 
        {% if p.month %}
          {{ p.month | append: ' ' | append: p.year | date: site.month_date_format }}
        {% elsif p.year %}
          {{ p.year }}
        {% endif %}
      </div>

      <div class="badges">
        {% if p.journal_url %}
          <a class="badge badge-journal" href="{{ p.journal_url }}">Journal</a>
        {% endif %}
        {% if p.preprint_url %}
          <a class="badge badge-preprint" href="{{ p.preprint_url }}">Preprint</a>
        {% endif %}
      </div>
    </li>
  {% endif %}
  {% endfor %}
{% endfor %}
{% endfor %}


</ul>
