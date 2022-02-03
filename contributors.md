---
layout: page
title: Contributors
contributors:
  - name: Mohamed Barakat
    affiliation: University of Siegen
    website: https://mohamed-barakat.github.io/

  - name: Reimer Behrends
    affiliation: TU Kaiserslautern
    retired: true

  - name: Alex Best
    affiliation: Boston University
    website: https://github.com/alexjbest

  - name: Martin Bies
    affiliation: University of Pennsylvania
    website: https://martinbies.github.io

  - name: Simon Brandhorst
    affiliation: Saarland University
    website: https://www.math.uni-sb.de/ag/brandhorst/index.php

  - name: Thomas Breuer
    affiliation: RWTH Aachen University
    email: thomas.breuer@math.rwth-aachen.de
    website: http://www.math.rwth-aachen.de/~Thomas.Breuer/
    paid_by_dfg: true

  - name: Taylor Brysiewicz
    email: Taylor.Brysiewicz@mis.mpg.de
    affiliation: Max Planck Institute for Mathematics in the Sciences
    website: https://sites.google.com/view/taylorbrysiewicz/home

  - name: Wolfram Decker
    affiliation: TU Kaiserslautern
    website: https://www.mathematik.uni-kl.de/en/agag/people/head/prof-dr-wolfram-decker/
    is_active_PI: true

  - name: Alexander Dinges
    affiliation: TU Kaiserslautern

  - name: Christian Eder
    affiliation: TU Kaiserslautern
    website: https://www.mathematik.uni-kl.de/~ederc/index.html

  - name: Raul Epure
    affiliation: TU Kaiserslautern
    retired: true

  - name: Claus Fieker
    affiliation: TU Kaiserslautern
    website: https://www.mathematik.uni-kl.de/en/agag/people/head/prof-dr-claus-fieker/
    is_active_PI: true

  - name: Giovanni De Franceschi
    affiliation: TU Kaiserslautern
    retired: true

  - name: Rafael Fourquet
    affiliation: TU Kaiserslautern
    retired: true

  - name: Sebastian Gutsche
    affiliation: TU Kaiserslautern
    email: gutsche@mathematik.uni-siegen.de
    website: https://sebasguts.github.io/
    retired: true

  - name: William Hart
    affiliation: TU Kaiserslautern
    #website: https://www.mathematik.uni-kl.de/agag/mitglieder/wissenschaftliche-mitarbeiter/dr-william-hart/
    paid_by_dfg: true

  - name: Florian Heiderich
    affiliation: University of Siegen
    website: https://www.heiderich.org/math/

  - name: Tommy Hofmann
    affiliation: University of Siegen
    website: https://www.thofma.com

  - name: Max Horn
    affiliation: TU Kaiserslautern
    website: https://www.quendi.de/math
    is_active_PI: true

  - name: Fredrik Johansson
    affiliation: Institut de Mathématiques de Bordeaux
    website: http://fredrikj.net/

  - name: Alexej Jordan
    affiliation: TU Berlin

  - name: Michael Joswig
    affiliation: TU Berlin
    website: https://page.math.tu-berlin.de/~joswig/
    is_active_PI: true

  - name: Marek Kaluba
    affiliation: KIT Karlsruhe
    website: https://kalmar.faculty.wmi.amu.edu.pl/

  - name: Lars Kastner
    affiliation: TU Berlin
    website: https://page.math.tu-berlin.de/~kastner/

  - name: Avi Kulkarni
    affiliation: Dartmouth College
    website: https://math.dartmouth.edu/~akulkarn/index.html

  - name: Benjamin Lorenz
    affiliation: TU Berlin
    website: https://www.math.tu-berlin.de/fachgebiete_ag_diskalg/fg_diskrete_mathematik_geometrie/v_menue/mitarbeiter/benjamin_lorenz/v_menue/home/

  - name: Frank Lübeck
    affiliation: RWTH Aachen University
    website: http://www.math.rwth-aachen.de/~Frank.Luebeck/index.html

  - name: Alexander Mattes
    website: https://github.com/alexandermattes

  - name: Sachin Mohan
    affiliation: TU Kaiserslautern
    website: https://github.com/sachinkm308

  - name: Oleksandr Motsak
    affiliation: IMAGINARY
    website: https://imaginary.org/users/oleksandr-motsak

  - name: Oguzhan Yürük
    affiliation: TU Berlin

  - name: Markus Pfeiffer
    affiliation: St Andrews
    retired: true
    website: https://github.com/markuspf

  - name: Delphine Pol
    affiliation: TU Kaiserslautern

  - name: Sebastian Posur
    affiliation: University of Siegen
    website: https://sebastianpos.github.io/

  - name: Martin Raum
    affiliation: Chalmers University
    website: https://github.com/martinra

  - name: Johannes Schmitt
    affiliation: TU Kaiserslautern
    website: https://github.com/joschmitt

  - name: Hans Schönemann
    affiliation: TU Kaiserslautern

  - name: Benjamin Schröter
    affiliation: KTH Stochkholm
    website: https://people.kth.se/~schrot

  - name: Daniel Schultz
    affiliation: TU Kaiserslautern

  - name: Carlo Sircana
    affiliation: TU Kaiserslautern

  - name: Andreas Steenpaß
    affiliation: TU Kaiserslautern
    retired: true

  - name: Jayantha Suranimalee
    affiliation: TU Kaiserslautern

  - name: Sascha Timme
    affiliation: TU Berlin
    retired: true
    website: https://github.com/saschatimme

  - name: Erec Thorn
    affiliation: TU Kaiserslautern
    website: https://github.com/erecthorn

  - name: Matthias Zach
    affiliation: TU Kaiserslautern
    paid_by_dfg: true

---

## Project leaders

<ul>
{% for p in page.contributors %}
{% if p.is_active_PI == true %}
  <li>
    {% if p.website != null %}
        <a href="{{ p.website }}">
        {% assign link_open = true %}
    {% elsif p.email != null %}
        <a href="mailto:{{ p.email }}">
        {% assign link_open = true %}
    {% endif %}
    <strong>{{ p.name }}</strong>{% if link_open %}</a>{% assign link_open = false %}{% endif %}
    {% if p.affiliation != null %} ({{ p.affiliation }}){% endif %}
  </li>
{% endif %}
{% endfor %}
</ul>

## Contributors

Currently, the following people contributed significantly to the software in the
OSCAR project.

<ul>
{% for p in page.contributors %}
{% if p.is_active_PI != true %}
  <li>
    {% if p.website != null %}
        <a href="{{ p.website }}">
        {% assign link_open = true %}
    {% elsif p.email != null %}
        <a href="mailto:{{ p.email }}">
        {% assign link_open = true %}
    {% endif %}
    <strong>{{ p.name }}</strong>{% if link_open %}</a>{% assign link_open = false %}{% endif %}
    {%- if p.affiliation != null or p.paid_by_dfg == true -%}
    <em>
        {%- if p.affiliation != null -%}
            , {{ p.affiliation }}{% if p.retired == true %} (formerly){% endif %}
        {%- endif -%}
        {%- if p.paid_by_dfg == true -%}
            {%- if p.affiliation != null -%},{% endif %}
            financed by the <a href="https://www.computeralgebra.de/sfb/">SFB-TRR 195</a>
        {%- endif -%}
    </em>
    {% endif %}
 </li>
{% endif %}
{% endfor %}
</ul>
