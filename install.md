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
You can now follow the instructions for <em><a href="#install-ubuntu1804">Ubuntu 18.04 or newer</a></em> above.
</p>
<p>
To start bash in a later session, just search for <q>bash</q>.
</p>
</details>

<details id="install-ubuntu1804">
<summary>
Ubuntu 18.04 "Bionic" or newer; Debian 10 "Buster" or newer
</summary>
Enter the following commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer).
{% highlight bash %}
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential
{% endhighlight %}
</details>

<details>
<summary id="install-ubuntu1604">
Ubuntu 16.04 "Xenial"
</summary>
<p>
The LTS release Ubuntu 16.04 has reached end of life in April 2019, but still receives
security updates until April 2021. In general we recommend that you upgrade to a more
recent Ubuntu version.
</p>
<p>
If you wish to proceed with it anyway, you can install a newer compiler as follows.
Enter the following commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer).
{% highlight bash %}
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt update
sudo apt-get upgrade
sudo apt install g++-7 -y
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 --slave /usr/bin/g++ g++ /usr/bin/g++-7
{% endhighlight %}
</p>
</details>

<details>
<summary>
Fedora 28 or newer
</summary>
Enter the following commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer).
{% highlight bash %}
sudo dnf install gcc-c++ make
{% endhighlight %}
</details>

<details>
<summary>
macOS 10.12 or newer
</summary>
On macOS, you need to install the Xcode command line tools, as explained in the following instructions.
<ol>
<li>Install Xcode <a href="https://apps.apple.com/de/app/xcode/id497799835">via the App Store</a>.</li>
<li>Launch a Terminal and enter the command <code>xcode-select —install</code>, then press enter.</li>
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

<details>
<summary>
macOS 10.11 or older
</summary>
Unfortunately the Xcode versions available for older macOS versions do not
support C++17. We recommend updating to macOS 10.12 or later, and Xcode 9.2 or
later. If this is not an option and you are an experienced user, you might be
able to get things working by installing a newer C/C++ compiler through some
other means, e.g. via Homebrew. However, we cannot provide support for this.
</details>

<details>
<summary>
Other Linux / BSD / Unix variants supported by Julia
</summary>
You will need to install at least GNU make, and a fairly recent C++ compiler supporting the C++17 standard.
Suitable compilers include
<ul>
<li>GNU C/C++ compiler (gcc) version 7 or newer,</li>
<li>Clang C/C++ compiler version 5 or newer,</li>
<li>Intel C/C++ Compiler (icc) version 19.0 or newer.</li>
</ul>
</details>

</div>

## Step 2: Install Julia

OSCAR requires at least Julia 1.3.1, but we recommend running it with the latest stable Julia release,
which is 1.6.2 at the time this is written.


There are several ways to install Julia:

1. [By downloading it from the Julia homepage](https://julialang.org/downloads/),
and following their [platform specific instructions](https://julialang.org/downloads/platform/).

<p class="message">
   <strong>WARNING:</strong> Windows users should <em>not</em> install the Julia version for Windows.
   Instead, please install the Linux version inside Windows Subsystem for Linux (WSL).
</p>

2. On macOS, you can also install it via [Homebrew](https://brew.sh): `brew install julia` 

3. The [JILL](https://github.com/johnnychen94/jill.py) project is a
   python package which allows installing and updating Julia -- this is
   in particular handy for experienced users who may want to install
   multiple Julia versions in parallel; but also for beginners it can be
   convenient as it allows updating the installed Julia version quite
   easily.

4. For Linux users, it may also be tempting to install Julia via your
   distro package manager (e.g., `apt`, `pac`, `dnf`, ...). We advise
   against this, as at least in the past these often provided outdated
   or broken Julia versions.


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
Version 0.6.0 ...
 ... which comes with absolutely no warranty whatsoever
Type: '?Oscar' for more information
(c) 2019-2021 by The Oscar Development Team

julia>
```

Please have a look at

  - [introductory examples](https://oscar.computeralgebra.de/example/)
  - [polymake examples](https://github.com/micjoswig/oscar-notebooks)
  - [Hecke examples](https://github.com/thofma/HeckeTutorials.jl)

for some examples (as [Jupyter](https://jupyter.org/) notebooks).

<!-- TODO: disabled until https://github.com/oscar-system/GAP.jl/issues/335 is resolved

### Starting GAP with JuliaInterface

If you have the Julia module `GAP.jl` installed above, you can also use the packages in the OSCAR ecosystem from GAP.

You can start a GAP, linked to your downloaded Julia, via

{% highlight bash %}
~/.julia/gap.sh
{% endhighlight %}

On the resulting GAP prompt, you can then load the Julia interface via

{% highlight GAP %}
LoadPackage( "JuliaInterface" );
{% endhighlight %}
-->

## Using IJulia for notebooks

IJulia can be installed by following its
[installation page](https://julialang.github.io/IJulia.jl/stable/manual/installation/).
Note that in some cases, IJulia must be "built" explicitly, see
the [trouble shooting page](https://julialang.github.io/IJulia.jl/stable/manual/troubleshooting/).
If you try to open an existing notebook (stored in a ".ipynb" file), it might refer to an
older Julia version, resulting in a "Kernel error"; the solution is then to select
a different kernel from the menu.
