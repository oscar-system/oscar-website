---
layout: page
title: Installation Instructions
---

<script>
    {% comment %}Preserve an optional section anchor through the redirect.{% endcomment %}
    const target = window.location.hash;
    {% comment %}Check mobile devices first because Android user agents also identify as Linux.{% endcomment %}
    if (/Android|iPhone|iPad/.test(navigator.userAgent)) {
        window.location.replace("{{site.baseurl}}/install/generic"+target);
    }
    else if (navigator.userAgent.includes("Linux")){
        window.location.replace("{{site.baseurl}}/install/linux"+target);
    }
    else if (navigator.userAgent.includes("Win")){
        window.location.replace("{{site.baseurl}}/install/win"+target);
    }
    else if (navigator.userAgent.includes("Macintosh")){
        window.location.replace("{{site.baseurl}}/install/mac"+target);
    }
    else {
        window.location.replace("{{site.baseurl}}/install/generic"+target);
    }
</script>

{% comment %}Provide manual choices when the automatic JavaScript redirect cannot run.{% endcomment %}
<noscript>
Choose the installation instructions for
[Linux]({{site.baseurl}}/install/linux/), [Windows]({{site.baseurl}}/install/win/),
[macOS]({{site.baseurl}}/install/mac/), or [another operating system]({{site.baseurl}}/install/generic/).
</noscript>
