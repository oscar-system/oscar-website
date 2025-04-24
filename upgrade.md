---
layout: page
title: Upgrading to the Latest OSCAR Release
---

If you already have OSCAR installed (cf. [installation guide]({{site.baseurl }}/getting-started/install/)) and wish to upgrade to **OSCAR v{{ site.data.release.version }}**, the latest stable release, follow the instructions below. If you encounter any issues, do not hesitate to [contact us]({{ site.baseurl }}/contact-and-support/).

---

### Upgrade OSCAR

1. Open a terminal and launch Julia:
   ```bash
   julia
   ```

2. At the Julia prompt, update the OSCAR package:
   ```julia
   using Pkg
   Pkg.update("Oscar")
   ```

OSCAR depends on several actively developed packages. To ensure full compatibility - especially if you experience any issues - we recommend updating all your packages via `Pkg.update()`.

---

### Upgrade Julia

For performance and feature improvements, consider upgrading Julia. Instructions are available [here](https://julialang.org/install/).

After upgrading, you may need to [reinstall OSCAR]({{site.baseurl }}/getting-started/install/) in the new environment.
