---
layout: page
---

<div class="platform-tabs">
  <input type="radio" id="mac" name="platform">
  <label for="mac" onclick="window.location.href='{{site.baseurl}}/install-mac/'">Mac</label>

  <input type="radio" id="windows" name="platform" checked>
  <label for="windows" onclick="window.location.href='{{site.baseurl}}/install-win/'">Windows</label>

  <input type="radio" id="linux" name="platform">
  <label for="linux" onclick="window.location.href='{{site.baseurl}}/install-linux/'">Linux</label>

  <input type="radio" id="other" name="platform">
  <label for="other" onclick="window.location.href='{{site.baseurl}}/install-generic/'">Other</label>
</div>


# Installing OSCAR {{ site.data.release.version }} on Windows

> 🛠️ **Already have OSCAR installed?** [Upgrade to the latest version here.]({{ site.baseurl }}/upgrade/)

To install **OSCAR v{{ site.data.release.version }}**, the latest stable release, follow the steps below.

<div class="message">
  <strong>WARNING:</strong>
  The installation process of OSCAR, particularly the precompilation step, requires 
  <strong>at least 6GB of free memory</strong>. For optimal performance with OSCAR, we recommend having <strong>at least 16GB of RAM</strong>.
</div>

The following instructions assume that you are at least somewhat familiar with using a terminal interface.

Having trouble? You can visit our [Contact & Support]({{site.baseurl}}/contact-and-support/) page to get in touch — or check out the [Frequently Asked Questions](https://docs.oscar-system.org/stable/General/faq/) for quick tips and troubleshooting guidance.


## Step 1: Install Windows Subsystem for Linux (WSL)

1. Follow the official instructions to install [Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install) as your [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).
2. Ensure your WSL subsystem has **at least 6GB of free memory** for the installation process, and ideally **16GB for optimal performance**. The memory available to WSL is **less than the total memory on your system**.

   You can adjust the memory allocation using the [official WSL configuration instructions](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#main-wsl-settings), typically via a `.wslconfig` file (see an [example](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#example-wslconfig-file)).

   > 💡 **Tip:** As suggested by [Miķelis Emīls Miķelsons](https://github.com/emikelsons), instead of editing a `.wslconfig` file manually, you can use the **"WSL Settings"** app on Windows. This GUI tool allows you to set the amount of RAM, number of processors, and other resources for WSL more easily.
3. After installing WSL, you should see the *Ubuntu* app in your start menu.


## Step 2: Install Julia

<div class="message">
   <strong>WARNING:</strong> 
   Do <strong>not</strong> install the Windows version of Julia. Instead, install the Linux version of Julia inside <a href="https://learn.microsoft.com/en-us/windows/wsl">WSL</a>, following the steps below.
</div>

1. Open your WSL environment -- installed in Step 1 -- by clicking the *Ubuntu* app from your start menu.
2. *OSCAR* requires [Julia](https://julialang.org) 1.6.0 or higher. We recommend installing the latest stable release of Julia as follows:
```sh
curl -fsSL https://install.julialang.org | sh
```


## Step 3: Install OSCAR

1. In your WSL environment, open the Julia REPL in your terminal by typing the following:
   ```bash
   julia
   ```
2. Install OSCAR by running the following commands. This may take a while, as it will download and install OSCAR and its dependencies.
   ```julia
   using Pkg
   Pkg.add("Oscar")
   ```


## Step 4: Start OSCAR

After the installation is complete, you can start using OSCAR by running `using Oscar` in the Julia REPL:
```console?lang=julia
julia> using Oscar
  ___   ___   ___    _    ____
 / _ \ / __\ / __\  / \  |  _ \  | Combining and extending ANTIC, GAP,
| |_| |\__ \| |__  / ^ \ |  ´ /  | Polymake and Singular
 \___/ \___/ \___//_/ \_\|_|\_\  | Type "?Oscar" for more information
o--------o-----o-----o--------o  | Documentation: https://docs.oscar-system.org
  S Y M B O L I C   T O O L S    | Version 1.4.0
```


## Step 5: Running Tutorials Locally with IJulia

1. Install *IJulia* (and Jupyter) by running the following command inside your Julia REPL (within your [WSL](https://learn.microsoft.com/en-us/windows/wsl) environment):
```julia
using Pkg; Pkg.add("IJulia")
```
For more details, refer to the [installation guide](https://julialang.github.io/IJulia.jl/stable/manual/installation/). If you encounter issues, you may need to explicitly build IJulia. Troubleshooting info can be found on the [IJulia troubleshooting page](https://julialang.github.io/IJulia.jl/stable/manual/troubleshooting/).
2. To run tutorial Jupyter notebooks locally, you will need a web browser available inside your [WSL](https://learn.microsoft.com/en-us/windows/wsl) environment, which runs Linux Ubuntu.

   By default, Ubuntu installs browsers using Snap, but Snap is disabled in [WSL](https://learn.microsoft.com/en-us/windows/wsl). Therefore, you may need to install a browser manually (e.g., Firefox). You can follow these [instructions](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04) to install Firefox using the `.deb` package method.

   > **Note:** As reported by [Oliver Clarke](https://github.com/ollieclarke8787), on **Windows 11 with WSL version 2**, this installation step may no longer be necessary. If you have a browser (e.g., Chrome) set as your default on Windows, Jupyter may automatically launch in that browser.

3. Download the tutorial of your interest from the [list of available OSCAR tutorials]({{site.baseurl }}/tutorials).
4. Start Jupyter by running the following in your Julia REPL (within your [WSL](https://learn.microsoft.com/en-us/windows/wsl) environment):
```julia
using IJulia; notebook()
```
5. Your web browser should open with the Jupyter interface, where "Jupyter" is displayed in the upper-left corner, and a file explorer appears below. Locate and open the tutorial notebook of your interest. You might see a pop-up with the message "Kernel not found" or "Kernel error". You can resolve this by selecting a different Julia kernel from the notebook's kernel menu.
