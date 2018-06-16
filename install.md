---
layout: page
title: Download and Installation
---

If you only intend to use OSCAR we recommend you install Docker on your machine and
install the OSCAR Docker image, as this is intended to work everywhere.

If you are a developer, you will probably want to know how to install OSCAR yourself.
For that purpose we give install instructions for various platforms below.

## Windows

If you only wish to use AbstractAlgebra.jl, Hecke.jl and Nemo.jl, you can install a
Julia binary from the [Julia website](https://julialang.org) and follow the instructions
for adding the relevant packages, below.

However, if you want to make use of Singular.jl or Polymake.jl, OSCAR cannot run as a
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

First set up a sane build environment:

```
sudo apt-get update
sudo apt-get install build-essential m4 libtool-bin autoconf autogen cmake
sudo apt-get install libboost-all-dev libxml2-dev libperl-dev ninja-build
sudo apt-get install libxml-writer-perl libxml-perl libxml-libxslt-perl
```

Now install Julia:

```
wget https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.3-linux-x86_64.tar.gz
tar -xvf julia-0.6.3-linux-x86_64.tar.gz
mv julia-d55cadc350 julia-0.6
```

Now start Julia:

```
julia-0.6/bin/julia
```

Now install the relevant Julia packages:

```
Pkg.add("AbstractAlgebra")

Pkg.add("Nemo")

Pkg.add("Hecke")

Pkg.clone("https://github.com/wbhart/Singular.jl")
Pkg.build("Singular")

Pkg.clone("https://github.com/oscar-system/Polymake.jl")
Pkg.build("Polymake")
```

The whole process will take some time (> 1 hour). But if everything went well, you are
good to go.

Note that the various packages are independent and you do not need to install them all.

