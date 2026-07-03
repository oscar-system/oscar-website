---
layout: page
title: What is OSCAR?
---

---

**OSCAR** is an **O**pen **S**ource **C**omputer **A**lgebra **R**esearch System
written in the [Julia programming language](https://julialang.org). It
provides a unified, high-performance framework for computations in
algebra, geometry, number theory, and polyhedral geometry. OSCAR builds
on the capabilities of four major systems:
  [GAP](https://www.gap-system.org),
  [Singular](https://www.singular.uni-kl.de),
  [Polymake](https://polymake.org), and
  ANTIC,
whose functionality is provided by
  [Hecke](https://github.com/thofma/Hecke.jl),
  [Nemo](https://github.com/Nemocas/Nemo.jl), and
  [AbstractAlgebra](https://github.com/Nemocas/AbstractAlgebra.jl).
By combining these specialized tools under one umbrella, OSCAR enables
workflows and mathematical functionality that go far beyond what each system
offers on its own. *We elaborate on these cornerstones below.*

Through deep integration via Julia, OSCAR allows mathematical objects from
different domains to interoperate seamlessly. This empowers researchers,
developers, and students to construct, manipulate, and compute with
sophisticated algebraic and geometric structures in a modular, extensible, and
expressive environment.

<img src="{{ site.baseurl }}/public/OSCAR-overview.png" alt="OSCAR Overview" width="70%" style="margin-left:13%;" align="center">

<!--
To update OSCAR-overview.png, run the following shell script:

    /etc/build-overview.sh

This script compiles _data/OSCAR-overview.tex, converts the resulting PDF into a web-optimized PNG,
and places the final image in the /public folder.

Dependencies:
  - pdflatex
  - ImageMagick (for the 'convert' command)

The LaTeX source is located in: _data/OSCAR-overview.tex
-->

{: .caption }
The OSCAR system connects advanced mathematical computations with the power of
multiple domain-specific tools. At the top, sample applications—ranging from
Galois cohomology to quantum groups of matroids—illustrate the breadth of
OSCAR's capabilities, symbolized by an idea of clouds surrounding "OSCAR".
Beneath this, five core disciplines—number theory, group theory, polyhedral
geometry, algebraic geometry, and non-commutative algebra—form the
mathematical focus of the system. These domains are linked via arrows to the
underlying software packages that serve as computational backbones, reflecting
OSCAR’s design as a deeply integrated and extensible research system. While
the current focus is on these five mathematical domains, OSCAR is built to
grow and evolve with the mathematical community.

---

## What Makes OSCAR Unique?

- **Deep Integration:** GAP, Singular, Polymake, and ANTIC are embedded into
OSCAR at a low level. Their functionality is exposed natively in Julia, and
mathematical objects move seamlessly between them without conversions.

- **Unified Language:** Julia serves as the single, high-level language across
all components, enabling concise, expressive, and efficient code in a modern
mathematical environment.

- **Interoperability:** OSCAR supports mixed-domain workflows—allowing, for
example, algebraic, geometric, and number-theoretic computations to be
composed naturally within the same session.

- **Research-Oriented:** OSCAR is designed for mathematical research. It
supports precise, reproducible computations and is actively developed by and
for the academic community.

- **Modular and Extensible:** OSCAR’s architecture encourages contributions.
New packages and algorithms can be added easily, benefiting from existing
infrastructure and interoperability.

---

## Why Julia?

[Julia](https://www.julialang.org) is a fast, modern, open-source language
tailored to numerical and symbolic computing. It offers:

- High-level syntax with just-in-time (JIT) compilation for speed
- Parametric types for precise mathematical modeling (e.g., matrices over
  polynomial rings over number fields)
- Direct access to C/C++ libraries used by the underlying systems
- A wide ecosystem for visualization, data handling, and scientific computing

---

## Cornerstone Systems

At the heart of OSCAR are four powerful, domain-specific computer algebra
systems. Each contributes unique strengths, and their deep integration within
Julia makes OSCAR a unified platform for advanced mathematical computation.

### ANTIC (Hecke) — Exact Arithmetic, Algebra and Number Theory

The ANTIC cornerstone is comprised of various Julia-based packages, providing
comprehensive support for exact arithmetic and linear algebra as well as
algebraic number theory.

- [**Hecke.jl**](https://github.com/thofma/Hecke.jl) implements high-level
  number theory algorithms, including computations in algebraic number fields
  and function fields.
- [**Nemo.jl**](https://github.com/Nemocas/Nemo.jl) serves as a wrapper for
  the highly optimized [FLINT](http://flintlib.org) library, which provides fast
  implementations for polynomials, matrices, and other fundamental structures.
- [**AbstractAlgebra.jl**](https://github.com/Nemocas/AbstractAlgebra.jl)
  defines the generic interface layer for rings, fields, groups, and modules in
  Julia, complementing FLINT with a flexible, abstract foundation.

Together, these packages provide the computational backbone for OSCAR’s
number-theoretic and algebraic capabilities — from basic arithmetic to
advanced structures in algebraic number theory and arithmetic geometry.

### GAP — Discrete Algebra and Group Theory

[GAP](https://www.gap-system.org) specializes in group theory and discrete
algebra. It offers a high-level language, a rich library of functions, and
over 120 contributed packages. Through
[GAP.jl](https://github.com/oscar-system/GAP.jl), GAP is seamlessly available
in Julia and thus forms the foundation for OSCAR’s algebraic capabilities.

### Polymake — Polyhedral and Combinatorial Geometry

[Polymake](https://polymake.org) is a software system for computations in
polyhedral geometry, convex polytopes, polyhedral fans, toric and tropical
geometry, and related combinatorial structures. With a hybrid architecture
(C++ and Perl) and a rule-based evaluation system, polymake is highly
extensible and efficient. Its full functionality is available in OSCAR via
[Polymake.jl](https://github.com/oscar-system/Polymake.jl), offering seamless
access from Julia.

### Singular — Polynomial Systems and Algebraic Geometry

[Singular](https://www.singular.uni-kl.de) specializes in computations with
polynomial rings, particularly in commutative algebra, algebraic geometry, and
singularity theory. It features advanced Gröbner basis algorithms and supports
non-commutative extensions through
[PLURAL](https://www.singular.uni-kl.de/Manual/4-1-2/sing_423.htm#SEC463) and
[LETTERPLACE](https://www.singular.uni-kl.de/Manual/4-1-2/sing_789.htm#SEC841).
Singular is embedded into OSCAR via
[Singular.jl](https://github.com/oscar-system/Singular.jl), exposing its
powerful capabilities within Julia.

The functionality of Singular is complemented by
[AlgebraicSolving.jl](https://github.com/algebraic-solving/AlgebraicSolving.jl),
a package that adds robust support for solving multivariate polynomial systems
using symbolic methods. Informally, it enables users to model and work with
points on algebraic varieties; more formally, it provides tools for symbolic
algebraic solving.

---

## Learn More and Get Involved

🚀 **[Installation Guide]({{site.baseurl}}/install/)** – Everything you need to install OSCAR {{ site.data.release.version }} (released on {{ site.data.release.date | date_to_string }}).

🛠️ **[Upgrade Instructions]({{ site.baseurl }}/upgrade/)** – Already using OSCAR? Learn how to upgrade to version {{ site.data.release.version }}.

🎓 **[Tutorials]({{site.baseurl}}/tutorials/)** – Interactive [Jupyter notebooks](https://jupyter.org/) to help you get started.

📚 **[Documentation]({{site.baseurl}}/documentation/)** – In-depth documentation and examples.

🎬 **[OSCAR Video Channel](https://tube.mathe.social/a/oscar/videos)** – interviews with contributors and demonstrations of OSCAR's capabilities.

📙 **[OSCAR Book](http://book.oscar-system.org)** – A detailed guide to OSCAR 1.0, featuring code snippets and in-depth explanations.

📝 **[Release Notes of OSCAR {{ site.data.release.version }}](https://github.com/oscar-system/Oscar.jl/releases/tag/v{{ site.data.release.version }})** – released on {{ site.data.release.date | date_to_string }}

🧑‍💻 **[GitHub Repository](https://github.com/oscar-system/Oscar.jl)** – Source code, issue tracking, and development discussions.

🤖 **[Contributing Guide]({{site.baseurl}}/contributing/)** – Learn how to contribute code, documentation, or ideas.

🧮 **[OSCAR Merchandise](https://oscar-system.myspreadshop.de/)** – OSCAR-branded items to support and represent the project.

🤝 **[Contact & Support]({{site.baseurl}}/contact-and-support/)** – Find ways to connect, ask questions, or get help.

📰 **[Newsletter]({{ site.baseurl }}/newsletter/)** – Occasional updates about OSCAR releases, papers, events, and community news.

🏛️ **Funding** – OSCAR is supported by the [German Research Foundation (DFG)](https://www.dfg.de/en) through the [Collaborative Research Center TRR 195](https://www.computeralgebra.de/sfb/)."
