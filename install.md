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
We currently only support Windows 10 or newer using <a href="https://docs.microsoft.com/en-us/windows/wsl/install-win10">Windows Subsystem for Linux (WSL)</a>.
<ol>
<li>Search for "Turn Windows features on or off"</li>
<li>On the left panel, select "Turn Windows features on or off"</li>
<li>Select "Windows subsystem for Linux" and press "Ok"</li>
<li>Click "Restart the PC"</li>
<li>Click the Windows store icon (shopping bag)</li>
<li>Search for "Ubuntu" in the store - it's free!</li>
<li>Select "Ubuntu" and "Get" the app</li>
<li>Click "Launch" and follow the prompts</li>
</ol>
<p>
You can now follow the instructions for <em><a href="#install-ubuntu">Ubuntu</a></em>.
</p>
<p>
To start bash in a later session, just search for <q>bash</q>.
</p>
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

OSCAR requires at least Julia 1.6.0, but we recommend running it with the latest stable Julia release,
which is 1.7.2 at the time this is written.

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

{% highlight julia %}
using Pkg
Pkg.add("Oscar")
{% endhighlight %}

This will run for a few minutes. From then on, you can start Julia, then type `using Oscar`
and press enter to use OSCAR. The result should look something like this:

```
julia> using Oscar
 -----    -----    -----      -      -----
|     |  |     |  |     |    | |    |     |
|     |  |        |         |   |   |     |
|     |   -----   |        |     |  |-----
|     |        |  |        |-----|  |   |
|     |  |     |  |     |  |     |  |    |
 -----    -----    -----   -     -  -     -

...combining (and extending) ANTIC, GAP, Polymake and Singular
Version 0.8.2 ...
 ... which comes with absolutely no warranty whatsoever
Type: '?Oscar' for more information
(c) 2019-2022 by The Oscar Development Team

julia>
```

Please have a look at

  - [introductory examples](https://oscar.computeralgebra.de/example/)
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
