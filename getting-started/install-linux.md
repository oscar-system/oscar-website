---
layout: page
---

<div class="platform-tabs">
  <input type="radio" id="mac" name="platform">
  <label for="mac" onclick="window.location.href='{{site.baseurl}}/getting-started/install-mac/'">Mac</label>

  <input type="radio" id="windows" name="platform">
  <label for="windows" onclick="window.location.href='{{site.baseurl}}/getting-started/install-win/'">Windows</label>

  <input type="radio" id="linux" name="platform" checked>
  <label for="linux" onclick="window.location.href='{{site.baseurl}}/getting-started/install-linux/'">Linux</label>

  <input type="radio" id="other" name="platform">
  <label for="other" onclick="window.location.href='{{site.baseurl}}/getting-started/install-generic/'">Other</label>
</div>


# Installation Instructions for Linux


<div class="message">
  <strong>WARNING:</strong>
  The installation process of OSCAR, particularly the precompilation step, requires 
  <strong>at least 6GB of free memory</strong>. For optimal performance with OSCAR, we recommend having <strong>at least 16GB of free memory</strong>.
</div>

The following instructions assume that you are at least somewhat familiar with using a terminal interface.

Having trouble? Visit our [Contact & Support]({{site.baseurl}}/contact-and-support/) page to get in touch.


## Step 1: Install prerequisites

If you are using Ubuntu 20.04 "Focal" or newer, or Debian 11 "Bullseye" or newer, proceed as follows:
Enter these commands into a terminal (this will prompt for your root password and requires that you
have permissions to administer your computer):
```sh
sudo apt update
sudo apt install build-essential
```

If you are using Fedora 40 or newer, enter the following commands into a terminal (this will prompt for your password
and requires that you have permissions to administer your computer):
```sh
sudo dnf install gcc-c++ make
```

## Step 2: Install Julia

<div class="message">
   <strong>WARNING:</strong>
   Linux users should generally <strong>not</strong> install the Julia version
   provided by their package manager (e.g., `apt`, `pac`, `dnf`, `homebrew`, ...), as in many cases,
   these Julia version are either outdated, or crippled, or both.
</div>

1. *OSCAR* requires [Julia](https://julialang.org) 1.6.0 or higher. We recommend using the latest stable release of Julia.
2. We suggest installing Julia via [juliaup](https://github.com/JuliaLang/juliaup) for easy updates and version management. *juliaup* will automatically install the latest stable release of Julia and allows you to manage multiple Julia versions if needed.
3. To install Julia via *juliaup*, run the following command in your terminal:
   ```sh
   curl -fsSL https://install.julialang.org | sh
   ```
4. Alternatively, you can [download Julia directly from the official website](https://julialang.org/downloads/) and follow the [installation instructions for Linux](https://julialang.org/downloads/platform/).


## Step 3: Install OSCAR

1. Open the Julia REPL in your terminal.
2. Install OSCAR by running the following commands:
   ```julia
   using Pkg
   Pkg.add("Oscar")
   ```
   This process will take a few minutes to complete, as it will install OSCAR and its dependencies. Internet access is required.


## Step 4: Start OSCAR

After the installation is complete, you can start using OSCAR by running `using Oscar` in the Julia REPL:
```console?lang=julia
julia> using Oscar
  ___   ____   ____    _    ____
 / _ \ / ___| / ___|  / \  |  _ \   |  Combining ANTIC, GAP, Polymake, Singular
| | | |\___ \| |     / _ \ | |_) |  |  Type "?Oscar" for more information
| |_| | ___) | |___ / ___ \|  _ <   |  Manual: https://docs.oscar-system.org
 \___/ |____/ \____/_/   \_\_| \_\  |  Version 1.0.0
```


## Step 5: Running Tutorials Locally with IJulia

1. Install *IJulia* (and jupyter) by running the following command inside your Julia REPL:
```julia
using Pkg; Pkg.add("IJulia")
```
For more details, refer to the [installation guide](https://julialang.github.io/IJulia.jl/stable/manual/installation/). If you encounter issues, you may need to explicitly build IJulia. Troubleshooting info can be found on the [IJulia troubleshooting page](https://julialang.github.io/IJulia.jl/stable/manual/troubleshooting/).
2. Download the tutorial of your interested from the [list of available OSCAR tutorials]({{site.baseurl }}/getting-started/tutorials).
3. Start Jupyter by running the following in your Julia REPL:
```julia
using IJulia; notebook()
```
4. Your web browser should open with the Jupyter interface, where "Jupyter" is displayed in the upper-left corner, and a file explorer appears below. Locate and open the tutorial notebook of your interest. <br>You might see a pop-up with the message "Kernel not found" or "Kernel error". You can resolve this by selecting a different Julia kernel from the notebook's kernel menu.
