---
layout: meeting
title: Program and results
meeting: true
meeting_nr: 202003
redirect_from:
  - /meetings/Meeting-03-2020/program/
---

## Program
* Start: Monday, March 2, at noon
* Finish: Friday, March 6, at noon

<!--
We will start with talks about data structures on Tuesday. Wednesday to Friday are reserved for
coding and short discussions when necessary.
-->

The program below is just a scaffold; more concrete plans
may be added later or during the workshop. If you have suggestions or wishes,
please [contact Max](mailto:max.horn@uni-siegen.de).

In general, we want to work on making OSCAR more usable, integrating
the corner stones with each other and into OSCAR.jl, and preparing
for the software demonstration during the SFB presentation in the Summer.

For this, coding and possibly design decisions should be a focus. Talks,
if any, should be focused on this goal.


### Monday

- 12:15 Lunch
- 13:00 Begin of official program

### Tuesday

- 09:30 Morning standup
- 10:00 Coding sprint
- 12:30 Lunch
- 13:30 Coding sprint
- 17:30 Status reports
- 19:00 Dinner

### Wednesday

- 09:30 Morning standup
- 10:00 Coding sprint
- 12:30 Lunch
- 13:30 Coding sprint
- 17:30 Status reports
- 19:00 Dinner

### Thursday

- 09:30 Morning standup
- 10:00 Coding sprint
- 12:30 Lunch
- 13:30 Coding sprint
- 17:30 Status reports
- 19:00 Dinner

### Friday

* 09:30 Coding sprint
* 11:00 Final status reports
* 12:00 Departure
* Note: participants are welcome to stay and work until 5pm if they wish

## Results

### GapGroups.jl
 - intended to become `Oscar/src/Groups` eventually
 - implements groups for Oscar based on Gap
 - focus was initially on permutation groups (Carlo, Giovanni),
   in the end, work proceeded towards arbitrary group types
 - basic functionality is available, core difference to Gap is the introduction
   of proper (Magma-style) parents that are absent from Gap.

### Oscar.jl
 - graded sub-quotient modules (free modules, direct sums, hom spaces
   quotients, sub modules, homomorphisms)
 - Polymake applications in number theory (factorisations into irreducibles in 
   number fields)
 - support for arbitrary orderings in polynomial rings

### Gap.jl
 - much reduced installation time, about 90' on a test system (25% faster
   than Polymake on this machiene) aiming for 30'
 - integration of the Gap-package manager
 - documentation has been added
 - better handling of Gap-errors in Julia
 - fixed and extended conversions between Gap and Julia

