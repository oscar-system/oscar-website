# Website for the OSCAR project

- [How to contribute](#how-to-contribute)
- [How to contribute a News post](#how-to-contribute-a-news-post)
- [How to contribute a tutorial notebook](#how-to-contribute-a-tutorial-notebook)
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

If your talk happens to be in a year that previously was not listed on the
website, then please add the new year in the line
```
{% assign years = "2022,2021,2020,2019,2018,2017" | split: "," %}
```
of `talks.html`. Otherwise your talk will not show up on the website.

## How to contribute a tutorial notebook

To contribute a new tutorial notebook, please follow these steps

1. Create a binder-ready repository on GitHub, containing the notebook file.
   Assume the repository is `https://github.com/myusername/mybinderrepo`
   and the notebook file is `mynotebook.ipynb` inside this repository.
   (For instance, cf. [OSCARBinder](https://github.com/oscar-system/OSCARBinder).)

2. Create a thumbnail for the notebook, say `mythumbnail.png` and store it in `/public/thumbnails`.

3. Create a new entry in the `_data/examples.yml` file, consisting of the following lines:
```
- title: "My new notebook"
  repository: myusername/mybinderrepo
  filename: mynotebook
  author: My Name
  thumbnail: mythumbnail.png
  language: julia
  date: Date at which the notebook was last modified

```
Please adjust all entries accordingly.

## How to use syntax highlighting in Markdown files

You can use Jekylls highlighter to get syntax highlighting.
For Julia code, do the following
````
```julia
function foo(x)
  return x
end
```
````

For code samples involving the Julia REPL mode, use this:
````
```console?lang=julia
julia> print(2)
2
```
````

Note however that the triple-backtick syntax does not work when nested inside
HTML elements. In that case, you can also use the following Jekyll syntax:
```
{% highlight julia %}
function foo(x)
  return x
end
{% endhighlight %}
```

A full list of supported languages can be found [here](https://github.com/rouge-ruby/rouge/blob/master/docs/Languages.md).
