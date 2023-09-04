---
layout: page
title: Download and Installation
---

OSCAR is currently under heavy development, so all parts
change continuously. If you encounter any trouble while following
the steps outlined below, feel free to contact us via
[GitHub discussion](https://github.com/oscar-system/Oscar.jl/discussions),
[our issue tracker](https://github.com/oscar-system/Oscar.jl/issues),
or by sending an email to <mailto:oscar@mathematik.uni-kl.de>.


## Step 1: Install prerequisites

The following instructions assume that you are at least somewhat familiar with using a
terminal interface.

<div class="clickdesc">

<details>
<summary>
Windows
</summary>
Please install Windows Subsystem for Linux (WSL) following the <a href="https://learn.microsoft.com/en-us/windows/wsl/install">official instructions</a>. You should now have an App "Ubuntu" in your start menu (run "explorer.exe ." in the Ubuntu terminal to open the current folder in the Windows File Explorer). You can now follow the instructions for <em><a href="#install-ubuntu">Ubuntu</a></em>. 
</details>

<details>
<summary>
macOS
</summary>
If you are using macOS 10.12 or newer, you need to install the Xcode command
line tools, as explained in the following instructions.
<ol>
<li>Launch a Terminal and copy and paste the command <code>xcode-select --install</code>, then press enter.</li>
<li>A window will appear asking you: <q>The xcode-select command requires
the command line developer tools. Would you like to install the tools
now?</q>. Confirm this by clicking <q>Install</q>.</li>
<li>Wait for this to complete; it needs to download about 130 MB of data.</li>
<li>You can verify that everything worked verifying the
<code>/Library/Developer/CommandLineTools/usr/bin/</code> exists and
contains executables such as <code>clang</code> and <code>clang++</code>,
the C and C++ compiler.</li>
</ol>
</details>

<details id="install-ubuntu">
<summary>
Ubuntu or Debian
</summary>
If you are using Ubuntu 18.04 "Bionic" or newer, or Debian 10 "Buster" or newer, proceed as follows:
Enter these commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer).
{% highlight bash %}
sudo apt-get update
sudo apt-get install build-essential
{% endhighlight %}
</details>

<details>
<summary>
Fedora
</summary>
If you are using Fedora 28 or newer,
enter the following commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer).
{% highlight bash %}
sudo dnf install gcc-c++ make
{% endhighlight %}
</details>

<details>
<summary>
Other or older operating systems supported by Julia
</summary>
We do not provided official support for other such systems at this time. But
if you wish to try anyway, you will need to install at least GNU make, and a
fairly recent C++ compiler supporting the C++17 standard.
Suitable compilers include
<ul>
<li>GNU C/C++ compiler (gcc) version 7 or newer,</li>
<li>Clang C/C++ compiler version 5 or newer,</li>
<li>Intel C/C++ Compiler (icc) version 19.0 or newer.</li>
</ul>
</details>

</div>

## Step 2: Install Julia

OSCAR requires at least [Julia](https://julialang.org) 1.6.0, but we recommend running it with the latest stable Julia release,
which is 1.8.5 at the time this is written.

<div class="message">
   <strong>WARNING:</strong>
   <ul>
   <li>
   <strong>Windows</strong> users should <em>not</em> install the Julia version for Windows.
   Instead, please install the Linux version inside Windows Subsystem for Linux (WSL).
   </li>
   <li>
   <strong>Linux</strong> and <strong>macOS</strong> users should generally <em>not</em> install the Julia version
   provided by their package manager (e.g., `apt`, `pac`, `dnf`, `homebrew`, ...), as in many cases,
   these Julia version are either outdated, or crippled, or both.
   </li>
   </ul>
</div>


There are several ways to install Julia:

1. [By downloading it from the Julia homepage](https://julialang.org/downloads/),
and following their [platform specific instructions](https://julialang.org/downloads/platform/).

2. The [juliaup](https://github.com/JuliaLang/juliaup) and
   [JILL](https://github.com/johnnychen94/jill.py) projects are
   external packages which allow installing and updating Julia -- this is
   in particular handy for experienced users who may want to install
   multiple Julia versions in parallel; but also for beginners it can be
   convenient as it allows updating the installed Julia version quite
   easily.

## Step 3: Install OSCAR

To then install OSCAR, just start julia and run

```julia
using Pkg
Pkg.add("Oscar")
```

This will run for a few minutes. From then on, you can start Julia, then type `using Oscar`
and press enter to use OSCAR. The result should look something like this:

```console?lang=julia
julia> using Oscar
 -----    -----    -----      -      -----
|     |  |     |  |     |    | |    |     |
|     |  |        |         |   |   |     |
|     |   -----   |        |     |  |-----
|     |        |  |        |-----|  |   |
|     |  |     |  |     |  |     |  |    |
 -----    -----    -----   -     -  -     -

...combining (and extending) ANTIC, GAP, Polymake and Singular
Version 0.11.3 ...
 ... which comes with absolutely no warranty whatsoever
Type: '?Oscar' for more information
(c) 2019-2023 by The OSCAR Development Team

julia>
```

Please have a look at

  - [introductory examples](https://www.oscar-system.org/example/)
  - [polymake examples](https://github.com/micjoswig/oscar-notebooks)
  - [Hecke examples](https://github.com/thofma/HeckeTutorials.jl)

for some examples (as [Jupyter](https://jupyter.org/) notebooks).


### Getting a GAP prompt

If you are a GAP user and have installed loaded OSCAR in a Julia session as
described above, you can at any time switch back and forth between the Julia prompt
and a GAP prompt, by using the command `GAP.prompt()`:

<pre>
<span style="color: green">julia></span> x = 1
1

<span style="color: green">julia></span> GAP.prompt()
<span style="color: blue">gap></span> Julia.x;
1
<span style="color: blue">gap></span> G := SymmetricGroup(3);
Sym( [ 1 .. 3 ] )
<span style="color: blue">gap></span> quit;   # or press Ctrl-D

<span style="color: green">julia></span> GAP.Globals.G
GAP: Sym( [ 1 .. 3 ] )

</pre>



## Using IJulia for notebooks

IJulia can be installed by following its
[installation page](https://julialang.github.io/IJulia.jl/stable/manual/installation/).
Note that in some cases, IJulia must be "built" explicitly, see
the [trouble shooting page](https://julialang.github.io/IJulia.jl/stable/manual/troubleshooting/).
If you try to open an existing notebook (stored in a ".ipynb" file), it might refer to an
older Julia version, resulting in a "Kernel error"; the solution is then to select
a different kernel from the menu.

If you are using OSCAR in the Windows Subsystem for Linux, you will require a browser 
in your subsystem. This can be a probem as the default subsystem is Ubuntu and Ubuntu 
installs browsers via snap which is disabled for subsystems. To circumvent this problem, 
please see [how to install browsers via deb](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04).


## System-wide installation of Oscar

It is possible to install Oscar and its cornerstones only once on your system,
and to let several people use this installation.
For that, the following `bash` scripts can be used.

<div class="clickdesc">

<details>
<summary>
Install Oscar system-wide,
or update the system-wide installation of Oscar when a new version is available.
</summary>
Enter the following commands into a file (for example <code>oscar_systemwide_install</code>),
adjust the paths for the variables <code>julia_for_oscar</code> and <code>central_depot</code>,
and then run the script in a terminal (with administrator rights).
{% highlight bash %}
#!/bin/bash

# Specify the intended version of Julia.
julia_for_oscar=/users/oscar/julia-1.8.5/bin/julia

# Specify the intended location of the central Oscar installation.
central_depot=/users/oscar/JULIA_DEPOT

# We will store the necessary artifacts in the
# "architecture dependent location" in Julia's default DEPOT_PATH.
# First determine this path and create the directory if necessary.
system_depot=$(${julia_for_oscar} --startup-file=no -e 'println(DEPOT_PATH[2])')
if ! test -d "${system_depot}/artifacts"; then
  mkdir -p "${system_depot}/artifacts"
fi

# Set the Julia variables that control the location of packages.
# (Do not admit the current user's own depot path.)
export JULIA_DEPOT_PATH=${central_depot}:${system_depot}
export JULIA_LOAD_PATH="@:@v#.#:@stdlib:${central_depot}/environments/globalenv"

# Clean the environment, such that the already centrally installed packages
# get replaced by newer versions if necessary.
# (This is safer than calling `Pkg.update()` in Julia.)
# Then let Julia install and precompile the packages.
${julia_for_oscar} -e 'using Pkg, Artifacts; \
rm("'${central_depot}'/environments/v" * join(split(string(VERSION), ".")[1:2], ".") * "/Project.toml", force=true)
Artifacts.with_artifacts_directory("'${system_depot}'/artifacts") do; \
Pkg.add("Oscar"); \
Pkg.add("GAP"); \
Pkg.add("Nemo"); \
Pkg.add("Hecke"); \
Pkg.add("Singular"); \
Pkg.add("Polymake"); \
Pkg.add("AbstractAlgebra"); \
Pkg.instantiate(); \
end; \
exit();'

# Write a file that will be loaded by Julia on startup.
echo 'using Pkg; Pkg.activate("'${central_depot}'/environments/v" * join(split(string(VERSION), ".")[1:2], "."))' > ${central_depot}/julia_load_initial.jl
{% endhighlight %}
</details>

<details>
<summary>
Call Julia such that the system-wide installation of Oscar gets loaded
when the user enters <code>using Oscar</code> in the Julia session.
</summary>
Enter the following commands into a file (for example <code>julia_with_oscar</code>),
adjust the paths for the variables <code>julia_for_oscar</code> and <code>central_depot</code>,
and then run the script in a terminal (not with administrator rights).
{% highlight bash %}
#!/bin/bash

# Specify the intended version of Julia.
julia_for_oscar=/users/oscar/julia-1.8.5/bin/julia

# Specify the intended location of the central Oscar installation.
central_depot=/users/oscar/JULIA_DEPOT

# Admit the user's own depot path and the path with the central installation.
export JULIA_DEPOT_PATH=$HOME/.julia:${central_depot}
export JULIA_LOAD_PATH="@:@v#.#:@stdlib:${central_depot}/environments/globalenv"

# Polymake may need a directory writable by the user.
export POLYMAKE_USER_DIR=$HOME/.julia/polymake_user

# Call Julia.
${julia_for_oscar} --load ${central_depot}/julia_load_initial.jl $*
{% endhighlight %}
</details>

</div>
