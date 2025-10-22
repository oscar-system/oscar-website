---
layout: page
title: Contributing to OSCAR
---

We welcome contributions of many kinds to the OSCAR project — from improving the source code, to writing tutorials, to suggesting new entries for our curated publication list. No matter your background or level of technical experience, your contribution helps build a vibrant, open, and collaborative ecosystem around OSCAR.

Before starting, we recommend [getting in touch with us]({{site.baseurl}}/contact-and-support) to avoid duplicate efforts and discuss ideas. We are happy to help you find the best way to contribute.

Currently, most developments and additions are coordinated via [GitHub](https://github.com/oscar-system). If you plan to contribute regularly, becoming familiar with GitHub will make collaboration smoother and faster. If you are new to GitHub, do not worry — you can always [contact us directly]({{site.baseurl}}/contact-and-support), and we will guide you through the process.

---

## Ways to Contribute

- [Report problems on GitHub]({{site.baseurl}}/contact-and-support#reporting-issues).
- [Cite OSCAR]({{site.baseurl}}/credits/Citing-OSCAR) if you used it in your research.
- [Improve tutorials]({{site.baseurl}}/contributing#contributing-tutorials) to help others learn to use OSCAR.
- [Suggest new publications]({{site.baseurl}}/contributing#contributing-publications) for our [Bibliography]({{site.baseurl}}/credits/bibliography).
- [Develop software projects]({{site.baseurl}}/contributing#contributing-software-projects--friends-of-oscar) that complement OSCAR — see [Friends of OSCAR](https://github.com/oscar-system/FriendsOfOscar).
- [Contribute directly to the OSCAR codebase and documentation]({{site.baseurl}}/contributing#contributing-source-code) via Pull Requests on GitHub.

---

## Contributing Publications

We maintain a curated list of notable OSCAR-related publications on the [Bibliography page]({{site.baseurl}}/credits/bibliography). To suggest an addition, edit [`_data/OSCAR-credits.yml`](https://github.com/oscar-system/oscar-website/blob/gh-pages/_data/OSCAR-credits.yml) and submit a Pull Request. Alternatively, [get in touch via our Contact and Support page]({{site.baseurl}}/contact-and-support/) with the publication details.

---

## Contributing Tutorials

We provide a list of tutorials that help others learn and use OSCAR effectively on the [Tutorials page]({{site.baseurl}}/tutorials).

Tutorial authors are responsible for keeping their tutorials compatible with the latest stable OSCAR release. Tutorials that are no longer compatible will be marked as outdated.

To suggest a new tutorial:
1. Create a [Jupyter notebook](https://jupyter.org/) with the desired content.
2. Place this notebook in a GitHub repository of your choice.
3. [Get in touch via our Contact and Support page]({{site.baseurl}}/contact-and-support/) and share the link to your Jupyter notebook with us.

If you need help, [please get in touch with us]({{site.baseurl}}/contact-and-support).

---

## Contributing Software Projects – Friends of OSCAR

The *Friends of OSCAR* initiative celebrates and connects software projects that complement, extend, or interoperate with OSCAR.

These *Friends* are independent projects that share our goals: advancing open-source computational mathematics, promoting interoperability, and supporting the research community.

Examples include experimental packages, research prototypes, and companion libraries developed by individual researchers or groups.

By joining *Friends of OSCAR*, your project will:
- Be listed and promoted on the [Friends of OSCAR GitHub page](https://github.com/oscar-system/FriendsOfOscar).  
- Gain visibility within the wider OSCAR ecosystem.  
- Facilitate collaboration and knowledge exchange with other developers and researchers.

**How to become a Friend of OSCAR:**
1. Visit [Friends of OSCAR on GitHub](https://github.com/oscar-system/FriendsOfOscar).  
2. Add your project following the contribution guidelines described there. A key part of this process is providing a small example showing how your project uses OSCAR.
3. Open a Pull Request to suggest your inclusion.  
4. Optionally, [contact us]({{site.baseurl}}/contact-and-support/) to discuss how your project integrates with OSCAR.

Whether you are a student exploring new ideas or a team maintaining a large research codebase, we warmly invite you to become a *Friend of OSCAR*. Your project can inspire others, expand OSCAR’s reach, and help build a stronger open-source mathematics community.

---

## Contributing Source Code

Contributing directly to OSCAR’s codebase is a great way to strengthen the system itself.

You can fork the relevant GitHub repository from the list below and submit a Pull Request with your changes:

* [Oscar.jl](https://github.com/oscar-system/Oscar.jl) – The main OSCAR repository
* [AbstractAlgebra.jl](https://github.com/Nemocas/AbstractAlgebra.jl) – Generic abstract algebra and abstract type definitions
* [AlgebraicSolving.jl](https://github.com/algebraic-solving/AlgebraicSolving.jl) – Algebraically solving multivariate polynomial systems
* [GAP.jl](https://github.com/oscar-system/GAP.jl/) – GAP 4 to Julia bidirectional interface
* [Hecke.jl](https://github.com/thofma/Hecke.jl) – Algebraic number theory
* [Nemo.jl](https://github.com/Nemocas/Nemo.jl) – Wrappers of Flint/Arb/Antic C libraries
* [Polymake.jl](https://github.com/oscar-system/Polymake.jl) – Polymake interface
* [Singular.jl](https://github.com/oscar-system/Singular.jl) – Singular interface

If you are unsure where your contribution fits best, please [contact us]({{site.baseurl}}/contact-and-support/) — we are happy to help you find the right entry point.
