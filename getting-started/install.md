---
layout: page
title: Installation Instructions
---

<script>
    const nowurl = window.location.href
    const target = nowurl.slice(nowurl.indexOf('#'))
    if (navigator.userAgent.includes("Linux")){
        window.location.replace("{{site.baseurl}}/getting-started/install-linux"+target);
    }
    else if (navigator.userAgent.includes("Win")){
        window.location.replace("{{site.baseurl}}/getting-started/install-win"+target);
    }
    else if (navigator.userAgent.includes("Macintosh")){
        window.location.replace("{{site.baseurl}}/getting-started/install-mac"+target);
    }
    else {
        window.location.replace("{{site.baseurl}}/getting-started/install-generic"+target);
    }
</script>
