---
layout: page
permalink: /install/generic/
---

<div class="platform-tabs">
  <input type="radio" id="mac" name="platform">
  <label for="mac" onclick="window.location.href='{{site.baseurl}}/install/mac/'">Mac</label>

  <input type="radio" id="windows" name="platform">
  <label for="windows" onclick="window.location.href='{{site.baseurl}}/install/win/'">Windows</label>

  <input type="radio" id="linux" name="platform">
  <label for="linux" onclick="window.location.href='{{site.baseurl}}/install/linux/'">Linux</label>

  <input type="radio" id="other" name="platform" checked>
  <label for="other" onclick="window.location.href='{{site.baseurl}}/install/generic/'">Other</label>
</div>


# Installing OSCAR {{ site.data.release.version }}

---

The latest stable release, **OSCAR v{{ site.data.release.version }}**, is officially supported on [**Windows**]({{site.baseurl}}/install/win/), [**macOS**]({{site.baseurl}}/install/mac/), and [**Linux (Debian, Ubuntu, Fedora)**]({{site.baseurl}}/install/linux/). If you are using a **different operating system**, we **do not provide support** and **cannot guarantee compatibility**. However, if you still wish to try installing OSCAR, you will need:
- **[GNU Make](https://www.gnu.org/software/make/)**
- A C++ compiler that supports C++17, such as:
  - [GNU C/C++ Compiler (GCC) **v7 or newer**](https://gcc.gnu.org/)
  - [Clang C/C++ Compiler **v5 or newer**](https://clang.llvm.org/)
  - [Intel C/C++ Compiler (ICC) **v19.0 or newer**](https://www.intel.com/content/www/us/en/developer/tools/oneapi/dpc-compiler.html)

<div class="message">
  <strong>WARNING:</strong>
  The installation process of OSCAR, particularly the precompilation step, requires 
  <strong>at least 6GB of free memory</strong>. For optimal performance, we recommend having <strong>at least 16GB of RAM</strong>.
</div>

---

## Advanced Installation Instructions

It is possible to install OSCAR and its cornerstones only once on your system,
and to let several people use this installation. For that, the following `bash` scripts can be used.

<div class="clickdesc">

<details>
<summary>
Install OSCAR system-wide,
or update the system-wide installation of OSCAR when a new version is available.
</summary>
Enter the following commands into a file (for example <code>oscar_systemwide_install</code>),
adjust the paths for the variables <code>julia_for_oscar</code> and <code>central_depot</code>,
and then run the script in a terminal (with administrator rights).
{% highlight bash %}
#!/bin/bash

set -e

# Specify the intended version of Julia.
julia_for_oscar=/usr/local/bin/julia

# Specify the intended location of the central OSCAR installation.
central_depot=/opt/oscar/depot

# Set the Julia variables that control the location of packages.
# (Do not admit the current user's own depot path.)
export JULIA_DEPOT_PATH=${central_depot}:

# Clean the environment, such that the already centrally installed packages
# get replaced by newer versions if necessary.
# (This is safer than calling `Pkg.update()` in Julia.)
# Then let Julia install and precompile the packages.
# You can customize the list below to install additional Julia packages for all users.

${julia_for_oscar} \
    --project=@v#.#-oscar \
    --startup-file=no \
    -e 'using Pkg;
        rm("'${central_depot}'/environments/v$(VERSION.major).$(VERSION.minor)/Manifest.toml", force=true)
        Pkg.update()
        Pkg.add("Oscar")
        Pkg.add("Hecke")
        Pkg.add("GAP")
        Pkg.add("Singular")
        Pkg.add("Polymake")
        Pkg.add("Nemo")
        Pkg.add("AbstractAlgebra")
        Pkg.instantiate()
        exit()
        '

{% endhighlight %}
</details>

<details>
<summary>
Call Julia such that the system-wide installation of OSCAR gets loaded
when the user enters <code>oscar</code> in their terminal.
</summary>
Enter the following commands into a file (for example <code>oscar</code>),
adjust the paths for the variables <code>julia_for_oscar</code> and <code>central_depot</code>,
and then put that file into a directory on your `PATH`. Make sure it is
executable (invoke `chmod` as needed)
{% highlight bash %}
#!/bin/sh

set -e

# Specify the intended version of Julia.
julia_for_oscar=/usr/local/bin/julia

# Specify the intended location of the central OSCAR installation.
central_depot=/opt/oscar/depot

# Admit the path with the central installation.
export JULIA_DEPOT_PATH=:${central_depot}
export JULIA_LOAD_PATH=":@v#.#-oscar"

#
echo "+------------------------------------------------+"
echo "| To complete loading OSCAR, enter 'using Oscar' |"
echo "| into the following julia> prompt.              |"
echo "|                                                |"
echo "| You can also only load GAP, Nemo, Hecke, etc.  |"
echo "+------------------------------------------------+"

# Call Julia.
exec ${julia_for_oscar} "$@"

{% endhighlight %}
</details>

</div>

<div class="message">
  <strong>WARNING:</strong>
  Users of such a system-wide installation may run into Julia errors if they have already installed some dependencies of OSCAR in their <code>~/.julia/packages</code>, or if they <C>add</C> them later on.
</div>
