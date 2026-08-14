---
layout: meeting
title: Program and results
meeting: true
meeting_nr: 201811
redirect_from:
  - /meetings/Meeting-11-2018/program/
---

## Program
* Start: Monday, November 26, at noon
* Finish: Friday, November 30, at noon

For details, see below

## Thoughts and Results

### Data type for mutivariate ideals in Oscar.jl

* A data type `MPolyIdl <: AbstractIdeal` is to be created.
* For now, this will be just be another abstraction layer for `sideal` from Singular.jl.
* In contrast to `sideal`, `MPolyIdl` should model ideals as mathematical objects, not as lists of generators
  as in Singular.

### Developer Guidelines for Julia code

The following lines are a brief overview
of gathered conventions from the existing code

#### Naming functions and variables

Variables: `CamelCase`

Functions: `small_letters`, words separated by ‘_’

#### Keyword arguments

Handling of keyword arguments
in Julia is not as efficient as
"normal" arguments

Use keyword arguments if there are
* many optional arguments
* optional arguments that might change in the future

#### Documenting Code

- [See the Julia manual about documentation](https://docs.julialang.org/en/v1/manual/documentation/index.html)
- All user functions need to be documented in Julia’s [markdown format](https://docs.julialang.org/en/latest/stdlib/Markdown/). Example:
```
@doc Markdown.doc"""
    parent(a::AbstractAlgebra.PolyElem)
> Return the parent of the given polynomial.
"""
parent(a::PolynomialElem) = a.parent
```
- Documentation of a function can also include:
  * Example of usage
  * Explanation of algorithms (including reference to literature)

- To build documentation automatically on GitHub, see:
  [https://github.com/JuliaDocs/Documenter.jl](https://github.com/JuliaDocs/Documenter.jl)
  [https://pages.github.com/](https://pages.github.com/)

  Example
  [https://github.com/Nemocas/Nemo.jl/blob/master/.travis.yml](https://github.com/Nemocas/Nemo.jl/blob/master/.travis.yml)
  [https://github.com/Nemocas/Nemo.jl/blob/master/docs/make.jl](https://github.com/Nemocas/Nemo.jl/blob/master/docs/make.jl)

* Advantages of GAPDoc vs. Julia docs
  1. Cross referencing between modules
  2. Possibility of documenting description, algorithms and interface of the function in different places.

### Continuous integration (CI)

Various formats of tests
  * Unit tests & Regression tests:
    Short tests, can be run for every commit/PR
  * Integration tests:
    Longer tests, for stability and compatibility of the whole ecosystem
  * Monitoring of performance: Monitor test times

When should tests be run?
* Short tests should be run on Travis
* Integration tests should be run in fixed intervals, if anything has changed
  * Make Jenkins check for changes every hour
  * Only rebuild changed software
  * If something has changed, run tests
  * While tests run, do not check for updates

Which versions of software should be used?
* Fixed versions of Julia? Master?
* New/fixed versions of Cornerstones

Where/How should test failures reported?
  * Travis -> Github
  * Jenkins: Emails? Webpage board? GitHub post?
    * Idea: Post daily status to a mailing list
    * Notify all people from new commits per mail (only if test fails two times)
    * Add badge to Readme's

How to filter test output to make the error message readable?
* Try to get the error as precise as possible


### Handling large fans
For tropical varieties, GIT fans, Groebner fans and secondary fans we are currently dealing with very large datasets, e.g. the secondary fan of the hypersimplex(2,7) contains >30'000'000 triangulations and to save it takes at least 1GB of memory (compressed). We have several datasets that are orders of magnitude larger. We do not want to recompute them, since this often takes several weeks/months, so the question is how we can provide them to everyone who needs them in a practical manner.
- Save fans as collection of cones in [polyDB](https://polymake.org/doku.php/data)
- Use property RAY_LABELS to identify combinatorial structure of fan
- For [mptopcom](https://polymake.org/doku.php/mptopcom) it is necessary to output the rays of the secondary fan, which is currently not done

### Communication
#### What we have
##### [Link to mailing lists on the wiki](https://github.com/oscar-system/OSCAR-private/wiki/Mailing-Lists)

[website](https://www.oscar-system.org/), [blog](https://oscar.computeralgebra.de/blog/)
[github](https://github.com/oscar-system)
email
slack

#### Future options for enhancing communication

* Email: discussions with individuals/very private discussions
* Private: oscar-private (TRR organisation only, not public, no archive)
* Announcements: oscar (public subscription, archive)
* Public: Options
  - Discourse (\$15 per month with academic discount, open source, maintained)
  - phpBB(free/open source, we maintain(possible security nightmare))

* GitHub: issue tracking, wiki
* Website: starting points, blog
* Slack: informal discussion with whoever is online
* trr195-members: announcements to trr participants

* Other forum options: Flarum, MyBB, vBulletin, NodeBB, YaBB

* Other examples:
  * sage-devel (Google Group)
  * ODK GitHub issues (even for discussions)
  * Pelles C (PhPBB)
  * Julia Discourse/GitHub

### Progress reports

Please add intermediate results and reports of task forces to [this pad](https://hackmd.io/_uIlbM8FSE6CjttGMoGm7w#).

### Monday

#### 14:00 - 16:00: Food for thought & Discussion (MA 313)

* **Michael Joswig:** Shaping OSCAR
* **Bill Hart:** Object model in Julia

#### 16:00 - 18:00: Task forces (MA 313, MA 621)

#### 18:00: Dinner at [Cafe Hardenberg](http://cafe-hardenberg.com/)

### Tuesday

#### 10:00 - 12:00: Status report (MA 313)

* **Christian Eder:** GB.jl
* **Claus Fieker:** Hecke.jl
* **Sebastian Gutsche:** GAP-Julia integration
* **Sascha Timme:** Polymake.jl

#### 14:00 - 18:00 Task forces (MA 212, MA 621)

### Wednesday

#### 10:00 - 12:00: Task forces (MA 212, MA 621)

#### 14:00 - 16:00: Task forces (MA 212, MA 621) & Discussion (MA 212)

#### 16:00 - 18:00: Task forces (MA 621)

### Thursday

#### 10:00 - 12:00: Task forces (MA 621)

#### 14:00 - 16:00: Task forces (MA 621)

#### 16:00 - 18:00: Task forces (MA 621)

### Friday

#### 10:00 - 12:00 Discussion (MA 621)

### Explanations

* Two initial talks (of 30 minutes each) serve as *food for thought*, with suggestions for our long-term goals. Focus on usability and user perspective.
* A *task force* is a small group formed to work on one particular issue.
  + About three or four task forces work in parallel.
  + Each task force decides how they want to work (discussing, coding, ...).
  + At the end of each block a task force produces a (very short) informal protocol to describe the progress (or the lack of it).
  + Task forces can regroup at the beginning of each block.
  + It is intended that all corner stone systems are represented in each task force.
* The *status reports* are 15--20 minutes each.  Focus on mathematics and the user perspective. Leave out technical details here; instead form task force if necessary.
* The schedule for Thursday and Friday will be set during the general discussion on Wednesday.
