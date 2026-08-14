---
layout: page
permalink: /install/mac/
---

<div class="platform-tabs">
  <input type="radio" id="mac" name="platform" checked>
  <label for="mac" onclick="window.location.href='{{site.baseurl}}/install/mac/'">Mac</label>

  <input type="radio" id="windows" name="platform">
  <label for="windows" onclick="window.location.href='{{site.baseurl}}/install/win/'">Windows</label>

  <input type="radio" id="linux" name="platform">
  <label for="linux" onclick="window.location.href='{{site.baseurl}}/install/linux/'">Linux</label>

  <input type="radio" id="other" name="platform">
  <label for="other" onclick="window.location.href='{{site.baseurl}}/install/generic/'">Other</label>
</div>


# Installing OSCAR {{ site.data.release.version }} on MacOS

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

## Step 1: Install prerequisites

If you are using macOS 10.12 or newer, you need to install the Xcode command line tools, as explained in the following instructions.

1. Launch a Terminal and copy and paste the command <code>xcode-select --install</code>, then press enter.
2. A window will appear asking you: <q>The xcode-select command requires the command line developer tools. Would you like to install the tools now?</q>. Confirm this by clicking <q>Install</q>.
3. Wait for this to complete; it needs to download about 130 MB of data.
4. You can verify that everything worked by verifying that the folder <code>/Library/Developer/CommandLineTools/usr/bin/</code> exists and contains executables such as <code>clang</code> and <code>clang++</code>, the C and C++ compiler.

---

## Step 2: Install Julia

*OSCAR* requires [Julia](https://julialang.org) {{ site.data.release.julia-min }} or higher. We recommend installing the latest stable release of Julia by entering the following in a terminal and heeding the instructions it shows:
```sh
curl -fsSL https://install.julialang.org | sh
```

---

## Step 3: Install OSCAR

1. Open the Julia REPL in your terminal by typing the following:
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

1. Install *IJulia* (and Jupyter) by running the following command inside your Julia REPL:
```julia
using Pkg; Pkg.add("IJulia")
```
For more details, see the [IJulia installation guide](https://julialang.github.io/IJulia.jl/stable/manual/installation/). If you encounter issues, you may need to explicitly build IJulia. Troubleshooting information is available on the [IJulia troubleshooting page](https://julialang.github.io/IJulia.jl/stable/manual/troubleshooting/).
2. Download one of the [OSCAR tutorials]({{site.baseurl }}/tutorials).
3. Start Jupyter by running the following in your Julia REPL:
```julia
using IJulia; notebook()
```
4. Your web browser should open the Jupyter interface. In the upper-left corner you should see "Jupyter"; the file explorer appears below it. Locate and open the tutorial notebook you downloaded. If you see a message such as `Kernel not found` or `Kernel error`, select a different Julia kernel in the top-right corner of the notebook.
