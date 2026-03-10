# Website for the OSCAR project

- [How to contribute](#how-to-contribute)
- [How to test the website locally](#how-to-test-the-website-locally)
- [How to contribute a tutorial notebook](#how-to-contribute-a-tutorial-notebook)
- [How to use syntax highlighting in Markdown files](#how-to-use-syntax-highlighting-in-markdown-files)


## How to contribute

Fork this repository on GitHub, and provide a Pull Request to it.


## How to test the website locally

For larger changes, it is useful to build a local version of the GAP
website first. This requires use of [Jekyll](https://jekyllrb.com). We
recommend using Ruby's `bundler`. This can be installed on Debian or
Ubuntu via `apt-get install bundler`. Then as a one-time setup, run

    bundle config set --local path 'vendor/bundle'
    bundle install

Afterwards, you can build a version of the website and open a local
webserver to test it by entering

    bundle exec jekyll serve

after which you can open <http://localhost:4000> in a web browser to see
a preview of the page. For more information on using Jekyll, please
consult the [Jekyll documentation](https://jekyllrb.com/docs/).


## How to contribute a tutorial

To contribute a new tutorial in the form of a Jupyter notebook, please follow the steps below.

### 1. Create a GitHub repository for the notebook

Create a GitHub repository that contains your Jupyter notebook (`.ipynb`). You should retain access to this repository, since updates may occasionally be required—for example when a new OSCAR release becomes available.

Maintaining these notebooks often requires mathematical expertise, so we rely on the notebook authors to make or verify necessary updates. All tutorials must run successfully with the latest stable release of OSCAR.

Let us assume your repository is `https://github.com/myusername/mybinderrepo` and the notebook file inside the repository is `mynotebook.ipynb`.

---

### 2. Provide a thumbnail image

Each tutorial category on the website is represented by a thumbnail image (a QR code) that links to the page listing tutorials for that topic. For instance
`https://www.oscar-system.org/tutorials/CommutativeAlgebra/#main-content`.

If your tutorial introduces a **new topic**, create a thumbnail image such as `mythumbnail.png` and place it in `/public/thumbnails`. However, if the topic already exists and a thumbnail is already available, you are strongly encourage to use the existing one and skip this step.

---

### 3. Add an entry to `_data/tutorials.yml`

Add an entry to `_data/tutorials.yml` describing your tutorial. The entry should follow the following structure:
```yaml
- filename: mynotebook
  repository: myusername/mybinderrepo
  branch: master
  title: "My new notebook"
  author: My Name
  thumbnail: mythumbnail.png
  topic: The topic of my tutorial
  last_modified: Date at which the notebook was last modified
  test_status: success
```


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
