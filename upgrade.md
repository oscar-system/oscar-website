---
layout: page
title: Upgrading to the Latest OSCAR Release
---

---

If you already have OSCAR installed (cf. [installation guide]({{site.baseurl}}/install/)) and wish to upgrade to **OSCAR v{{ site.data.release.version }}**, the latest stable release, follow the instructions below. If you encounter any issues, do not hesitate to [contact us]({{site.baseurl}}/contact-and-support/).

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

3. Verify the installed version -- it should report OSCAR v{{ site.data.release.version }} -- as follows:
```julia
using Oscar
Oscar.versioninfo()
```

---

### Troubleshooting the OSCAR Upgrade

OSCAR depends on several actively developed packages. To ensure full compatibility — especially if you experience any issues — we recommend updating **all** your packages:
```julia
Pkg.update()
```
Then restart Julia and check the OSCAR version (it should be OSCAR v{{ site.data.release.version }}):
```julia
using Oscar
Oscar.versioninfo()
```
If the version is not updated or you encounter any failures during the upgrade, please [contact us]({{site.baseurl}}/contact-and-support/) for assistance.

---

### Upgrade Julia

For performance and feature improvements, we recommend upgrading Julia to the latest stable version.

If you installed Julia using **[juliaup](https://github.com/JuliaLang/juliaup)** (the recommended method), upgrading is as simple as running:
```bash
juliaup up
```

If you're not using `juliaup`, please refer to the official [Julia installation instructions](https://julialang.org/install/) for upgrade guidance.

After upgrading Julia, you will need to [reinstall OSCAR]({{site.baseurl}}/install/) in the new Julia environment. In most cases, the installation will reuse existing OSCAR files and complete relatively quickly. However, this cannot be guaranteed and may depend on your specific setup.
