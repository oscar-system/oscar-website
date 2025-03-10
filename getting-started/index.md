---
layout: page
title: Getting Started with OSCAR
---

The latest stable release of OSCAR is **v{{ site.data.release.version }}**. Follow the links below to install it, explore tutorials, and access documentation.

<div style="text-align: center;">
  <svg class="responsive-svg" viewBox="0 0 360 270" preserveAspectRatio="xMidYMid meet">
    <!-- Installation Box -->
    <a xlink:href="{{site.baseurl }}/getting-started/install/">
      <rect x="110" y="0" width="140" height="60" rx="15" ry="15" fill="#4472C4"/>
      <text x="180" y="35" font-size="20" text-anchor="middle" fill="white" font-weight="bold">Installation</text>
    </a>

    <!-- Tutorials Button -->
    <a xlink:href="{{site.baseurl }}/getting-started/tutorials/">
      <rect x="0" y="200" width="140" height="60" rx="15" ry="15" fill="#ED7D31"/>
      <text x="70" y="235" font-size="20" text-anchor="middle" fill="white" font-weight="bold">Tutorials</text>
    </a>

    <!-- Documentation Button -->
    <a xlink:href="{{site.baseurl }}/getting-started/documentation/">
      <rect x="220" y="200" width="140" height="60" rx="15" ry="15" fill="#70AD47"/>
      <text x="290" y="235" font-size="20" text-anchor="middle" fill="white" font-weight="bold">Documentation</text>
    </a>

    <!-- Arrows indicating direction -->
    <line x1="180" y1="65" x2="70" y2="195" stroke="#aaa" stroke-width="3" marker-end="url(#arrow)"/>
    <line x1="180" y1="65" x2="290" y2="195" stroke="#aaa" stroke-width="3" marker-end="url(#arrow)"/>
    
    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="10" refY="5" orient="auto">
        <path d="M0,0 L10,5 L0,10 Z" fill="#aaa"/>
      </marker>
    </defs>
  </svg>
</div>

<style>
  .responsive-svg {
    width: 100%;
    max-width: 360px;
    height: auto;
  }
</style>

Looking for more? The [OSCAR Book](https://www.oscar-book.org/) offers deeper insights into *OSCAR* beyond the standard documentation.
