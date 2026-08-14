---
layout: page
title: Citing OSCAR
---

---

If you have used **OSCAR v{{ site.data.release.version }}** in your research, please cite it using the following format, preferably including both citations:

```md
[OSCAR]
    OSCAR -- Open Source Computer Algebra Research system, Version {{ site.data.release.version }},
    The OSCAR Team, {{ site.data.release.year }}. (https://www.oscar-system.org)

[OSCAR-book]
    Wolfram Decker, Christian Eder, Claus Fieker, Max Horn, Michael Joswig, eds.
    The Computer Algebra System OSCAR: Algorithms and Examples,
    Algorithms and Computation in Mathematics, Springer, 2025. (https://link.springer.com/book/9783031621260)
```

If you are using **BibTeX**, you can use the following BibTeX entries:

```bibtex
@misc{OSCAR,
  key          = {OSCAR},
  organization = {The OSCAR Team},
  title        = {O{SCAR} -- {O}pen {S}ource {C}omputer {A}lgebra {R}esearch system, {V}ersion {{ site.data.release.version }}},
  year         = { {{- site.data.release.year }}},
  url          = {https://www.oscar-system.org},
  doi          = {10.5281/zenodo.12077975}
}

@book{OSCAR-book,
  editor = {Decker, Wolfram and Eder, Christian and Fieker, Claus and Horn, Max and Joswig, Michael},
  title = {The {C}omputer {A}lgebra {S}ystem {OSCAR}: {A}lgorithms and {E}xamples},
  year = {2025},
  publisher = {Springer},
  series = {Algorithms and {C}omputation in {M}athematics},
  volume = {32},
  edition = {1},
  url = {https://link.springer.com/book/9783031621260},
  issn = {1431-1550},
  doi = {10.1007/978-3-031-62127-7},
}
```
