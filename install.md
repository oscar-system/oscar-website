---
layout: page
title: Download and Installation
---

The OSCAR project initially encompasses a number of different software projects. 
Below are instructions to install the current parts of the OSCAR project.
Please be aware that there is no single OSCAR system, nor a single OSCAR binary
to use yet. For simplicity, we will nevertheless refer to OSCAR during the following
instructions.

OSCAR is currently under heavy development, so all parts
change continuously.

## Windows

Unfortunately, OSCAR cannot run natively in Windows, however there
is no problem running it in the Windows Subsystem for Linux.

### Installing the Windows Subsystem for Linux (Windows 10)

  * Search for "Turn Windows features on or off"
  * On the left panel, select "Turn Windows features on or off"
  * Select "Windows subsystem for Linux" and press "Ok"
  * Click "Restart the PC"
  * Click the Windows store icon (shopping bag)
  * Search for "Ubuntu" in the store - it's free!
  * Select "Ubuntu" and "Get" the app
  * Click "Launch" and follow the prompts

You can now follow the instructions for *Linux* below.

To start bash in a later session, just search for "bash".

## Installation in Linux
If you have a (moderately) recent linux, e.g.

 - Ubuntui/ Debia 18.04
 - Feodra 28

(*Moderately recent* is more technically defined as having a c++-17 capable 
compiler and a matching ```cmake```)

Just go to the [julia download](http://julialang.org/Download)
and follow those instructions. ***Note*** you need version 1.3.1.

To then install OSCAR, just start julia and run
{% highlight julia %}
  using Pkg
  Pkg.add("Oscar")
{% endhighlight %}

This will run a few minutes. From then on, do
{% highlight julia %}
  using Oscar
{% endhighlight %}
to use it.

Please have a look at 

  - [introductory examples](https://oscar.computeralgebra.de/example/)
  - [polymake examples](https://github.com/micjoswig/oscar-notebooks)
  - [Hecke examples](https://github.com/thofma/HeckeTutorials.jl)

at some examples (as Jupyter notebooks)

## Installation for Ubuntu 16.04

First set up a sane build environment. This manual is for `bash`. If you are not sure, start a bash by typing

{% highlight bash %}
bash
{% endhighlight %}

Next we need to install the necessary system packages, such as a C compiler,
and some other tools (this list of package should become considerably shorter
in the future).

{% highlight bash %}
sudo apt-get update
sudo apt-get install autoconf build-essential bzip2 cmake curl git libcurl4-gnutls-dev libczmq-dev libgmp-dev libreadline6-dev libtool m4 make wget zlib1g-dev
{% endhighlight %}

Now install Julia by downloading it from the Julia homepage:

{% highlight bash %}
wget https://julialang-s3.julialang.org/bin/linux/x64/1.3/julia-1.3.1-linux-x86_64.tar.gz
tar xf julia-1.3.1-linux-x86_64.tar.gz
{% endhighlight %}

Now start Julia

{% highlight bash %}
julia-1.3.1/bin/julia
{% endhighlight %}

Now install Oscar:

{% highlight julia %}
using Pkg
Pkg.add("Oscar")
{% endhighlight %}

The whole process will take some time. But if everything went well, you are
good to go.

{% highlight julia %}
using Oscar
{% endhighlight %}

### Starting GAP with JuliaInterface

If you have the Julia module `GAP.jl` installed above, you can also use the packages in the OSCAR ecosystem from GAP.

You can start a GAP, linked to your downloaded Julia, via

{% highlight bash %}
~/.julia/gap.sh
{% endhighlight %}

In GAP, you can load the Julia interface via

{% highlight GAP %}
LoadPackage( "JuliaInterface" );
{% endhighlight %}

