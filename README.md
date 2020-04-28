# Website for the Oscar project

- [How to contribute](#how-to-contribute)
- [How to contribute a News post](#how-to-contribute-a-news-post)
- [How to contribute an example notebook](#how-to-contribute-an-example-notebook)
- [How to add a new documentation URL](#how-to-add-a-new-documentation-url)
- [How to add a new contributor](#how-to-add-a-new-contributor)
- [How to add a new software dependency](#how-to-add-a-new-software-dependency)
- [How to add a new meeting subpage](#how-to-add-a-new-meeting-subpage)
- [How to use syntax highlighting in Markdown files](#how-to-use-syntax-highlighting-in-markdown-files)

## How to contribute

Fork this repository on GitHub, and provide a Pull Request to it.
To test your changes locally, run
```
jekyll serve
```
in the main directory.

## How to contribute a News post

To contribute a new News post, please follow these steps

1. Create a new `.md` file in the folder `news/_posts`. The filename
   must be of the format `YYYY-MM-DD-title-of-post.md`.

2. At the beginning of your `.md` file, put
```
---
layout: post
title: Title of your post
author: Your name
---
```
3. Afterwards, you can write your post in markdown syntax. Please note that the title
   is put in automatically, so you do not have to put it in the post separately.


## How to contribute a talk

Please add a new entry to the file `_data/talks.yml`, following this template
```
- title: First things
  author: Sebastian Gutsche
  location: Aachen, Germany
  date: "1988-05-28"
  conference: My conference
  conference_url: https://my.conference.de
```

To add a link to the PDF to your talk, you can either provide full
URL to the pdf, via
```
  pdf_url: http://my.url.de/my.pdf
```
or you can copy the pdf, say `my.pdf` to the `public` subfolder of the website and add
```
  pdf: my.pdf
```
to the entry in the `talks.yml` file.

## How to contribute an example notebook

To contribute a new example notebook, please follow these steps

1. Create a binder-ready repository on GitHub, containing the notebook file.
   Assume the repository is `https://github.com/myusername/mybinderrepo`
   and the notebook file is `mynotebook.ipynb` inside this repository.

   For an example repository, see [OSCARBinder](https://github.com/oscar-system/OSCARBinder).

2. Create a thumbnail for the notebook, say `mythumbnail.png` and store it in `/public/thumbnails`.

3. Create a new `.md` file in the folder `examples/_posts`. The filename
   must be of the format `YYYY-MM-DD-title-of-notebook.md`.

4. At the beginning of your `.md` file, add the following lines:
```
---
layout: post
title: My new notebook
repository: myusername/mybinderrepo
filename: mynotebook
author: My Name
thumbnail: mythumbnail.png
---
```
Please adjust all entries accordingly. All further content of the file is ignored.

## How to add a new documentation URL

Please add a new entry to the `_data/documentation_pages.yml` file, of the following form:
```
- name: Singular.jl
  documentation_url: https://www.singular.uni-kl.de
  description: The interface to Singular
               from Julia
```

## How to add a new contributor

Please add a new entry to the `_data/contributors.yml` file, of the following form:
```
- name: Sebastian Gutsche
  affiliation: University of Siegen
  email: gutsche@mathematik.uni-siegen.de
  website: https://sebasguts.github.io
```
All three entries, `affiliation`, `email`, and `website` are optional. If you provide an `email` and a `website`, the name will link to the website.

## How to add a new software dependency

Please add a new entry to the `_data/used_software.yml` file, of the following form:
```
- name: GAP
  website: https://www.gap-system.org
```

## How to add a new meeting subpage

Send an email to [Max Horn](mailto:horn@mathematik.uni-kl.de) and ask for help.

## How to use syntax highlighting in Markdown files

You can use Jekylls highlighter to get syntax highlighting.
For Julia, do the following
```
{% highlight julia %}
julia> print(2)
2
{% endhighlight %}
```
A full list of supported languages can be found [here](https://haisum.github.io/2014/11/07/jekyll-pygments-supported-highlighters/).
