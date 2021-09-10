---
layout: meeting
title: Program
meeting: true
meeting_nr: 202109
---

* Start: Monday, September 6
* Finish: Friday, September 10


## Schedule

The schedule will be adjusted as we go along, so please watch out for changes.

The talks will be in Zoom. Everything else will take place in our gather.town workspace.

### Monday, September 6
  - 09:00 Time to install stuff, try Gather.town, socialize, ...
  - 12:00 Lunch break
  - 13:00 Welcome session on Gather.town
  - 13:10 Talk “Introduction to Julia” (Tommy Hofmann) ([notebook](https://github.com/thofma/summerschool2021/blob/master/notebooks/Introduction%20to%20Julia.ipynb))
  - 14:10 Talk “An overview of Oscar” (Claus Fieker)
  - 14:40 Talk [“Git crash course”](https://www.math.rwth-aachen.de/~Thomas.Breuer/git_intro.pdf) (Thomas Breuer)
  - 15:40 Exercises
  - 16:30 Evening standup

### Tuesday, September 7
  - 09:00 Morning standup
  - 09:30 Exercises
  - 10:30 Talk [“Algorithms for polycyclic groups: abelian quotients, polycyclic presentations, collection”](https://www.math.rwth-aachen.de/~Thomas.Breuer/obrien_lecture1.pdf) (Eamonn O'Brien)
  - 11:30 Exercises
  - 12:30 Lunch break
  - 13:30 Talk “Advanced Julia: How to not write slow code” (Tommy Hofmann) ([notebook](https://github.com/thofma/summerschool2021/blob/master/notebooks/How%20to%20not%20write%20slow%20Julia%20code.ipynb))
  - 14:30 Exercises
  - 16:30 Evening standup

### Wednesday, September 8
  - 09:00 Morning standup
  - 09:30 Exercises
  - 10:30 Talk [“Algorithms for polycyclic groups: p-quotient algorithm”](https://www.math.rwth-aachen.de/~Thomas.Breuer/obrien_lectures1_2.pdf) (Eamonn O'Brien)
  - 11:30 Exercises
  - 12:30 Lunch break
  - 13:30 Talk [“Advanced Git & GitHub”](../slides/advanced-git-github) (Max Horn)
  - 14:30 Exercises
  - 16:30 Evening standup
  - 19:00 Social gathering in Gather.Town

### Thursday, September 9
  - 09:00 Morning standup
  - 09:30 Talk [“Computational exact linear algebra: from theory to practice”](../slides/oscar_linalg.pdf) (Clément Pernet)
    [abstract](#computational-exact-linear-algebra-from-theory-to-practice-clément-pernet)

  - 10:30 Talk [“Algorithms for polycyclic groups: p-group generation algorithm, SmallGroups project”](https://www.math.rwth-aachen.de/~Thomas.Breuer/obrien_lectures1_2_3.pdf) (Eamonn O'Brien)
  - 11:30 Exercises
  - 12:30 Lunch break
  - 13:30 Exercises
  - 16:30 Evening standup

### Friday, September 10
  - 09:00 Morning standup
  - 09:30 Exercises
  - 12:00 Final standup, summary, feedback round
  - 13:00 End of the summer school


## Abstracts


### “Computational exact linear algebra: from theory to practice” (Clément Pernet)

Exact linear algebra is a core component of many symbolic and algebraic computations, as it often
delivers competitive theoretical complexities and also better harnesses the efficiency of modern
computing infrastructures. We will present an overview on the recent advances in exact linear
algebra algorithmic and implementation techniques, and highlight the few key ideas that have proven
successful in their design. After considering the choice of the low level computer arithmetic, we
will illustrate how algorithmic reductions designed for theoretical complexity improvements become
also relevant for efficiency in practice. Lastly, we will give a special care to the design and
implementation of parallel exact linear algebra routines, trying to emphasize the similarities and
distinctness with parallel numerical linear algebra. We aim to provide the working computer
algebraist with a set of best practices for the use or the design of exact linear algebra software.
