---
layout: page
title: Software used in the OSCAR project

used_software:
    - name: GAP
      website: https://www.gap-system.org

    - name: Nemo
      website: https://github.com/Nemocas/Nemo.jl/

    - name: Hecke
      website: https://github.com/thofma/Hecke.jl/

    - name: Polymake
      website: https://www.polymake.org/

    - name: Singular
      website: https://www.singular.uni-kl.de/

    - name: GMP
      website: https://gmplib.org/

    - name: MPFR
      website: https://www.mpfr.org/

    - name: Arb
      website: http://arblib.org/

    - name: NTL
      website: https://www.shoup.net/ntl

    - name: Flint
      website: http://www.flintlib.org

    - name: Antic
      website: https://github.com/wbhart/antic

    - name: gfanlib
      website: https://users-math.au.dk/~jensen/software/gfan/gfan.html

    - name: Factory
      website: https://www.singular.uni-kl.de/ftp/pub/Math/Singular/Factory/README

    - name: cdd
      website: https://www.inf.ethz.ch/personal/fukudak/cdd_home/

    - name: AbstractAlgebra
      website: https://github.com/Nemocas/AbstractAlgebra.jl

    - name: msolve
      website: https://msolve.lip6.fr/

    - name: cohomCalg
      website: https://github.com/BenjaminJurke/cohomCalg

    - name: CxxWrap.jl
      website: https://github.com/JuliaInterop/CxxWrap.jl

    - name: Julia
      website: https://www.julialang.org
---

OSCAR relies on many software packages. For a complete and up-to-date list of dependencies, please see the [Project.toml file](https://github.com/oscar-system/Oscar.jl/blob/master/Project.toml) in the OSCAR GitHub repository. The following are some of them:

{% assign entries = page.used_software | sort_natural:"name" %}
<ul class="software_credits_list">
{% for p in entries %}
  <li>
    <a href="{{ p.website }}">
    <strong>{{ p.name }}</strong>
    </a>
  </li>
{% endfor %}
</ul>

### MaRDI

The [Mathematical Research Data Initiative](https://www.mardi4nfdi.de/about/mission) (MaRDI), is a German consortium dedicated to setting guidelines and developing software for findability, accessibility, interoperability, and reuse of mathematical research data. OSCAR's serialization employs the **mrdi** file format, the specifications of which can be found on [zenodo](https://zenodo.org/records/12723387). More details are available in [this article](https://link.springer.com/chapter/10.1007/978-3-031-64529-7_25) and the [OSCAR documentation](https://docs.oscar-system.org/stable/General/serialization/).

### LEAN meets OSCAR

The [LEAN proof assistant](https://lean-lang.org/) is a formal system for writing and verifying mathematical proofs using a computer. While OSCAR is designed to perform concrete symbolic computations in areas such as algebra and geometry, LEAN is tailored for the formalization and verification of abstract mathematical reasoning.

An initial connection between these two systems has been explored in the meeting [LEAN meets MaRDI and OSCAR (Berlin, December 2024)](https://polymake.org/doku.php/workshops/lean_workshop1224) and most notably in the [Lean-Oscar](https://github.com/todbeibrot/Lean-Oscar) repository, originally created by [Cedric Holle](https://github.com/todbeibrot). This proof-of-principle demonstrates how OSCAR can support formal proofs in LEAN. Such an interaction opens up promising avenues for collaboration and research, allowing mathematicians to bridge the gap between rigorous computation and rigorous proof.
