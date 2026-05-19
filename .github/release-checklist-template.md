---
title: OSCAR v{{ env.VERSION }} release requires follow-up
labels: release-process
---

# OSCAR v{{ env.VERSION }} release requires follow-up


A new OSCAR release **v{{ env.VERSION }}** was published on **{{ env.PUBLISHED }}**.

Verify that all tutorials work with the latest OSCAR release and update them if needed. Tutorials are tested daily by the automated tutorial tester.

Verify that the OSCAR book website displays and allows to select code in this latest version as well as all earlier versions of OSCAR.

Please send an email to the OSCAR mailing list (<devel@oscar-system.org>) to inform about this update. You can use the following template.

Major releases (1.x.0) should also be announced to the SFB mailing lists (like <trr195-members@mathematik.uni-kl.de> and <trr195-grad@mathematik.uni-kl.de>).

> Subject: New OSCAR release v{{ env.VERSION }}
> 
> Dear all,
> 
> We are happy to announce that OSCAR version v{{ env.VERSION }} has been released on {{ env.PUBLISHED }}.
> 
> Highlights of this release:
> - (Add 2-3 bullet points summarizing major changes or improvements)
> 
> The new version is available from GitHub and via the usual installation methods
> (cf. https://www.oscar-system.org/install/ and https://www.oscar-system.org/upgrade/).
> 
> The release notes can be found at https://github.com/oscar-system/Oscar.jl/releases/tag/v{{ env.VERSION }}
>
> Best regards,
> The OSCAR Team


CC: @HereAround, @aaruni96

_Opened automatically by a scheduled workflow._
