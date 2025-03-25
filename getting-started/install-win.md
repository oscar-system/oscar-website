---
layout: page
---

<div class="platform-tabs">
  <input type="radio" id="mac" name="platform">
  <label for="mac" onclick="window.location.href='{{site.baseurl}}/getting-started/install-mac/'">Mac</label>

  <input type="radio" id="windows" name="platform" checked>
  <label for="windows" onclick="window.location.href='{{site.baseurl}}/getting-started/install-win/'">Windows</label>

  <input type="radio" id="linux" name="platform">
  <label for="linux" onclick="window.location.href='{{site.baseurl}}/getting-started/install-linux/'">Linux</label>

  <input type="radio" id="other" name="platform">
  <label for="other" onclick="window.location.href='{{site.baseurl}}/getting-started/install-generic/'">Other</label>
</div>


# Installing OSCAR {{ site.data.release.version }} on Windows

You are about to install **OSCAR v{{ site.data.release.version }}**, the latest stable release. Follow the instructions below to set up OSCAR on your system.

<div class="message">
  <strong>WARNING:</strong>
  The installation process of OSCAR, particularly the precompilation step, requires 
  <strong>at least 6GB of free memory</strong>. For optimal performance with OSCAR, we recommend having <strong>at least 16GB of RAM</strong>.
</div>

The following instructions assume that you are at least somewhat familiar with using a terminal interface.

Having trouble? Visit our [Contact & Support]({{site.baseurl}}/contact-and-support/) page to get in touch.


## Step 1: Install Windows Subsystem for Linux (WSL)

1. Follow the official instructions to install [Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install) as your [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).
2. Ensure your WSL subsystem has **at least 6GB of free memory** for the installation process, and ideally **16GB for optimal performance**. The memory available to WSL is **less than the total memory on your system**. To adjust the memory allocation, follow the [official WSL configuration instructions](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#main-wsl-settings). You can view a sample `.wslconfig` file [here](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#example-wslconfig-file).
3. After installing WSL, you should see the *Ubuntu* app in your start menu.


## Step 2: Install Julia

<div class="message">
   <strong>WARNING:</strong> 
   Do <strong>not</strong> install the Windows version of Julia. Instead, install the Linux version of Julia inside <a href="https://learn.microsoft.com/en-us/windows/wsl">WSL</a>, following the steps below.
</div>

1. Open the *Ubuntu* app from your start menu (installed in Step 1).
2. *OSCAR* requires [Julia](https://julialang.org) 1.6.0 or higher. We recommend using the latest stable release of Julia as follows:
```sh
curl -fsSL https://install.julialang.org | sh
```


## Step 3: Install OSCAR

1. Open the Julia REPL in your terminal.
   ```bash
   julia
   ```
2. Install OSCAR by running the following commands. This may take a while to complete, as it will download and install OSCAR and its dependencies.
   ```julia
   using Pkg
   Pkg.add("Oscar")
   ```


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
2. To run tutorial Jupyter notebooks locally, you will need a browser installed in WSL. Ubuntu installs browsers via Snap, but Snap is disabled in WSL. To install a browser (e.g., Firefox), follow these [instructions](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04).
3. Download the tutorial of your interested from the [list of available OSCAR tutorials]({{site.baseurl }}/getting-started/tutorials).
4. Start Jupyter by running the following in your Julia REPL:
```julia
using IJulia; notebook()
```
5. Your web browser should open with the Jupyter interface, where "Jupyter" is displayed in the upper-left corner, and a file explorer appears below. Locate and open the tutorial notebook of your interest. <br>You might see a pop-up with the message "Kernel not found" or "Kernel error". You can resolve this by selecting a different Julia kernel from the notebook's kernel menu.
