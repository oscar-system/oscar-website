---
layout: meeting
title: Program and results
meeting: true
meeting_nr: 201811
---


## Program
* Start: Monday, November 26, at noon
* Finish: Friday, November 30, at noon

### Progress reports

Please add intermediate results and reports of task forces to [this pad](https://hackmd.io/_uIlbM8FSE6CjttGMoGm7w#).

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

#### 14:00 - 16:00: Taks forces (MA 212, MA 621) & Discussion (MA 212)

#### 16:00 - 18:00: Talk: TBA (MA 621)

### Thursday

#### TBA (MA 313)

### Friday

#### TBA (MA 212)


## Results

### Data type for mutivariate ideals in Oscar.jl

* A data type `MPolyIdl <: AbstractIdeal` is to be created.
* For now, this will be just be another abstraction layer for `sideal` from Singular.jl.
* In contrast to `sideal`, `MPolyIdl` should model ideals as mathematical objects, not as lists of generators
  as in Singular.
