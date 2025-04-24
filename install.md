---
layout: page
title: Installation Instructions
---

<script>
    const nowurl = window.location.href
    const target = nowurl.slice(nowurl.indexOf('#'))
    if (navigator.userAgent.includes("Linux")){
        window.location.replace("{{site.baseurl}}/install-linux"+target);
    }
    else if (navigator.userAgent.includes("Win")){
        window.location.replace("{{site.baseurl}}/install-win"+target);
    }
    else if (navigator.userAgent.includes("Macintosh")){
        window.location.replace("{{site.baseurl}}/install-mac"+target);
    }
    else {
        window.location.replace("{{site.baseurl}}/install-generic"+target);
    }
</script>
