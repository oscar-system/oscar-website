---
layout: page
permalink: /try-online/
---

# Try OSCAR Online

OSCAR can be tried online without installing, on the NFDI jupyter hub. We provide a docker image
with a precompiled ahead of time version of OSCAR. This strategy side steps lenghty online 
precompiling, and allows an online "try it before you buy it" version of OSCAR.


Use the following steps:

1. Go to
[https://hub.nfdi-jupyter.de/workshops/oscar-latest](https://hub.nfdi-jupyter.de/workshops/oscar-latest)
, and login.

2. Select "Helmholtz AAI" 

3. Select your academic institution, or Google/Github/ORCID to identify yourself.

4. Start the workshop image. This may take some time, upto 5 minutes. You will be automatically
redirected to a jupyter interface when it is ready.

5. Select "Oscar 1.12" in the notebook section.

6. Try `println(4)`, to see that the Julia kernel has started and connected to the image. (This
may also take some time)

7. Use OSCAR as normal. Note that running `using Oscar` is a required step,
but will not print the OSCAR banner. Run `Oscar.versioninfo()` to verify the
version of OSCAR being used.

![OSCAR in Jupyter](/jupyter-oscar.png)