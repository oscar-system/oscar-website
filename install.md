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

If you only intend to use OSCAR we recommend you install Docker on your machine and
install the OSCAR Docker image, as this is intended to work everywhere.

If you are a developer, you will probably want to know how to install OSCAR yourself.
For that purpose we give install instructions for various platforms below.

## Windows

If you only wish to use `AbstractAlgebra.jl`, `Hecke.jl` and `Nemo.jl`, you can install a
Julia binary from the [Julia website](https://julialang.org) and follow the instructions
for adding the relevant packages, below.

However, if you want to make use of `Singular.jl` or `Polymake.jl`, OSCAR cannot run as a
native binary. If you have Windows 10, you can use the Windows Subsystem for Linux
instead.

### Installing the Windows Subsystem for Linux (Windows 10)

  * Search for "Turn Windows features on or off"
  * On the left panel, select "Turn Windows features on or off"
  * Select "Windows subsystem for Linux" and press "Ok"
  * Click "Restart the PC"
  * Click the Windows store icon (shopping bag)
  * Search for "Ubuntu" in the store - it's free!
  * Select "Ubuntu" and "Get" the app
  * Click "Launch" and follow the prompts

You can now follow the instructions for Ubuntu 16.04 below.

To start bash in a later session, just search for "bash".

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
Pkg.add("https://github.com/oscar-system/Oscar.jl")
{% endhighlight %}

If you have your own copy of GAP installed, and compiled it against your Julia,
you can tell the `GAP.jl` installation to use this GAP by setting the `GAPROOT`
environment variable to the GAP directory.

If you have your own recent polymake installed, you can tell `Polymake.jl` to use it by setting the
`POLYMAKE_CONFIG` environment variable to your `polymake-config` executable. If you do not
have a recent polymake, do not worry. `Polymake.jl` will download it for you.

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

