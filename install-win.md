---
layout: page
permalink: /install/win/
---

<div class="platform-tabs">
  <input type="radio" id="mac" name="platform">
  <label for="mac" onclick="window.location.href='{{site.baseurl}}/install/mac/'">Mac</label>

  <input type="radio" id="windows" name="platform" checked>
  <label for="windows" onclick="window.location.href='{{site.baseurl}}/install/win/'">Windows</label>

  <input type="radio" id="linux" name="platform">
  <label for="linux" onclick="window.location.href='{{site.baseurl}}/install/linux/'">Linux</label>

  <input type="radio" id="other" name="platform">
  <label for="other" onclick="window.location.href='{{site.baseurl}}/install/generic/'">Other</label>
</div>


# Installing OSCAR {{ site.data.release.version }} on Windows

---

> 🛠️ **Already have OSCAR?** [Upgrade to the latest version here.]({{ site.baseurl }}/upgrade/)

---

Follow the steps below to install OSCAR v{{ site.data.release.version }}. Basic familiarity with using a terminal is assumed.

Having trouble? Visit our [Contact & Support]({{site.baseurl}}/contact-and-support/) page for help.

---

<div class="message">
  <strong>WARNING:</strong>
  The installation process of OSCAR, particularly the precompilation step, requires 
  <strong>at least 6GB of free memory</strong>. For optimal performance, we recommend having <strong>at least 16GB of RAM</strong>.
</div>

---

## Step 1: Install Windows Subsystem for Linux (WSL)

Follow the official instructions to install [Ubuntu](https://learn.microsoft.com/en-us/windows/wsl/install) as your [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install). After the installation, you should see the *Ubuntu* app in your Start menu.

Ensure your WSL subsystem has **at least 6GB of free memory** for the installation process, and ideally **16GB for optimal performance**. The memory available to WSL is **less than the total memory on your system**. You can adjust the memory allocation using the [official WSL configuration instructions](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#main-wsl-settings), typically via a `.wslconfig` file (see an [example](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#example-wslconfig-file)).

> 💡 **Tip:** As suggested by [Miķelis Emīls Miķelsons](https://github.com/emikelsons), instead of editing a `.wslconfig` file manually, you can use the "WSL Settings" app on Windows. This GUI tool allows you to set RAM, number of processors, and other resources for WSL easily.



---

## Step 2: Install Julia

<div class="message">
   <strong>WARNING:</strong> 
   Do <strong>not</strong> install the Windows version of Julia. Instead, install the Linux version of Julia inside <a href="https://learn.microsoft.com/en-us/windows/wsl">WSL</a>, by following the steps below.
</div>

1. Open your WSL environment by clicking the *Ubuntu* app from your start menu.
2. *OSCAR* requires [Julia](https://julialang.org) {{ site.data.release.julia-min }} or higher. We recommend installing the latest stable release of Julia by entering the following in a terminal and heeding the instructions it shows:
```sh
curl -fsSL https://install.julialang.org | sh
```

---

## Step 3: Install OSCAR

1. In your WSL environment, open the Julia REPL in your terminal by typing the following:
   ```bash
   julia
   ```
2. Install OSCAR by running the following commands. This may take a while, as OSCAR and its dependencies will be downloaded and installed.
   ```julia
   using Pkg
   Pkg.add("Oscar")
   ```

---

## Step 4: Start OSCAR

Run `using Oscar` in the Julia REPL:
```console?lang=julia
julia> using Oscar
  ___   ___   ___    _    ____
 / _ \ / __\ / __\  / \  |  _ \  | Combining and extending ANTIC, GAP,
| |_| |\__ \| |__  / ^ \ |  ´ /  | Polymake and Singular
 \___/ \___/ \___//_/ \_\|_|\_\  | Type "?Oscar" for more information
o--------o-----o-----o--------o  | Documentation: https://docs.oscar-system.org
  S Y M B O L I C   T O O L S    | Version {{ site.data.release.version }}
```

---

## Optional: Running Tutorials Locally with IJulia

If you would like to run the [OSCAR tutorials]({{site.baseurl}}/tutorials/) locally, you can do so using
[IJulia](https://github.com/JuliaLang/IJulia.jl).

1. Install *IJulia* (and Jupyter) by running the following command inside your Julia REPL (within your [WSL](https://learn.microsoft.com/en-us/windows/wsl) environment):
```julia
using Pkg; Pkg.add("IJulia")
```
For more details, see the [IJulia installation guide](https://julialang.github.io/IJulia.jl/stable/manual/installation/). If you encounter issues, you may need to explicitly build IJulia. Troubleshooting information is available on the [IJulia troubleshooting page](https://julialang.github.io/IJulia.jl/stable/manual/troubleshooting/).
2. To run the OSCAR tutorials locally, you need a web browser accessible from your [WSL](https://learn.microsoft.com/en-us/windows/wsl) environment (which runs Ubuntu).

   Ubuntu normally installs browsers via Snap, but Snap is disabled in [WSL](https://learn.microsoft.com/en-us/windows/wsl).
   You may therefore need to install a browser manually (for example, Firefox).
   You can follow these
   [instructions](https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04)
   to install Firefox using the `.deb` package method.

   > **Note:** As reported by [Oliver Clarke](https://github.com/ollieclarke8787),
   on **Windows 11 with WSL version 2** this step may no longer be necessary.
   If a browser (e.g. Chrome) is set as your default browser on Windows,
   Jupyter may open automatically in that browser.
3. Download one of the [OSCAR tutorials]({{site.baseurl }}/tutorials).
4. Start Jupyter by running the following in your Julia REPL (within your [WSL](https://learn.microsoft.com/en-us/windows/wsl) environment):
```julia
using IJulia; notebook()
```
5. Your web browser should open the Jupyter interface. In the upper-left corner you should see "Jupyter"; the file explorer appears below it. Locate and open the tutorial notebook you downloaded. If you see a message such as `Kernel not found` or `Kernel error`, select a different Julia kernel in the top-right corner of the notebook.
