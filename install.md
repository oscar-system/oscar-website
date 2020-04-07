---
layout: page
title: Download and Installation
---

OSCAR is currently under heavy development, so all parts
change continuously.

## Step 1: Install prerequisites

Using OSCAR requires a working copy of [Julia 1.3.1 or newer](http://julialang.org/Download) and
a fairly recent C++ compiler. 

The following instructions all require that you are at least somewhat familiar with using a
terminal interface

<div class="clickdesc">

<details>
<summary>
Ubuntu 18.04 or newer.
</summary>
Enter the following commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer).
{% highlight bash %}
sudo apt-get update
sudo apt-get install build-essential g++ gcc
{% endhighlight %}
</details>

<details>
<summary>
Ubuntu 16.04 LTS
</summary>
Enter the following commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer).
{% highlight bash %}
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt update
sudo apt install g++-7 -y
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 --slave /usr/bin/g++ g++ /usr/bin/g++-7
{% endhighlight %}
</details>

<details>
<summary>
Other Linux distributions (e.g. Fedora 28 or newer)
</summary>
Please install C and C++ compiler for your Linux distribution (we recommend GCC 7 or newer).
</details>

<details>
<summary>
macOS
</summary>
On macOS, you need to install the Xcode command line tools; we also
expect you to be familiar with using the Terminal, either 
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
Windows 10
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
You can now follow the instructions for <em>Linux</em> below.
</p>
<p>
To start bash in a later session, just search for <q>bash</q>.
</p>
</details>

</div>

## Step 2: Install Julia 1.3.1 or newer

Install Julia 1.3.1 or newer [by downloading it from the Julia homepage](https://julialang.org/downloads/),
and following their [platform specific instructions](https://julialang.org/downloads/platform/).




## Step 3: Install OSCAR

To then install OSCAR, just start julia and run
{% highlight julia %}
  using Pkg
  Pkg.add("Oscar")
{% endhighlight %}

This will run a few minutes. From then on, you can start Julia and enter
{% highlight julia %}
  using Oscar
{% endhighlight %}
to use OSCAR.

Please have a look at 

  - [introductory examples](https://oscar.computeralgebra.de/example/)
  - [polymake examples](https://github.com/micjoswig/oscar-notebooks)
  - [Hecke examples](https://github.com/thofma/HeckeTutorials.jl)

at some examples (as Jupyter notebooks)

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

