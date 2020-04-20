---
layout: post
title: Polymake release 4.0
author: Benjamin Lorenz
---

This is to announce the release of polymake 4.0. As indicated by the major version bump, this brings several (breaking) changes, especially for authors of polymake extensions and users of the polymake callable library:

* Data file format changed from XML to JSON.
  - XML files can still be read and will be upgraded automatically.
  - XML files can no longer be written.
* C++ data type for sizes and indexes changed to `pm::Int := long int`.
  - In many cases a `s/\<int\>/Int/g` might suffice.
* Renamed C++ `Object` class to `BigObject`.

Major new features are:

* PolyDB:
  - New object oriented user interface.
  - Improved collection layout.
  - JSON based data, metadata and schema storage.
* Improved hyperplane arrangement object type.

There are also many smaller fixes and improvements, see the [release
notes](https://polymake.org/doku.php/news/release_4_0) for more details.
