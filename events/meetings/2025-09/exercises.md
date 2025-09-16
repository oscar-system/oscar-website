---
layout: meeting
title: Exercises
meeting: true
meeting_nr: 202509
---

<p class="message">
This is a live document and will be updated during the week.
</p>

## Helpful links
- [julia syntax overview](https://learnxinyminutes.com/julia/)
- [julia documentation](https://docs.julialang.org/en/v1/)
- [OSCAR documentation](https://docs.oscar-system.org/stable/)


## Session-specific exercises

### First steps with OSCAR


### Exploring more of OSCAR’s functionality (structure/subsystems)

#### Representations and G-Modules

Create the (relative) Brauer group over $\mathbb{Q}$ and build a central
simple algebra with given Schur-indices/ local invariants.

Find groups and characters with Schur index 3, 4, 5 and 6.

Explore the connection between `gmodule`s and `matrix_group`s.
Start easy, say with some dihedral group.

#### Number Theory

Find a normal extension $K$ of degree 4 over $\mathbb{Q}$. For some primes (including
ramified and (if possible) inert ones define the completions at
those primes.

For a local field, study the structure of the multiplicative group, in 
particular at varying precision. Compare this to the theoretical structure.

Verify that the $H^1(K_p^*)$ is indeed trivial and the $H^2$ is cyclic.

Let $f = x^3 + x^2 - 2x - 1$. For which primes $p$ does
   $f$ have 3 roots mod $p$? Can you spot the pattern? Can you
   explain the pattern?

#### Linear algebra/ abelian groups

For `R = Z/8Z` and the matrix `m = matrix(R, 2, 2, [4, 2, 0, 0])`
explain the difference between `hnf(m)` and `howel_form(m)`.

Find all automorphisms of the unit group of `Z/12Z` and `Z/120Z`. What is
the structure?

Find all endomorphisms of `Z/12Z` and `Z/120Z`

Let `A = matrix(ZZ, rand(-10:10, 1000, 1000))` and 
`b = matrix(ZZ, rand(-10:10, 1, 1000))`. What is the best method in Oscar
to solve `xA = b` for rational `x`? (Maybe start with smaller matrices)

How many ways are there to compute determinants of matrices of univariate 
polynomials?

Find all integer solutions to `Ax = b` and `Cx >= 0`

Solve `Ax = b` for `A`, `b` and `x` integral.

Find all integral solutions of `2x+3y = 7`

#### Cohomology

Create some (natural) G-modules:
 - natural G-module for a matrix group
 - permutation modules
 - natural modules
 - trivial modules
 - tensor products
and see if you can compute `H^i` for i=0,1,2

How many constructors for G-modules are there?

#### General

Compare
 - `@time prod(i for i=1:10000)` (and note the result here)
 - `@time prod(ZZ(i) for i=1:10000);`
 - `@time prod(BigInt(i) for i=1:10000);`
 - `@time prod([ZZ(i) for i=1:10000]);`
 - `@time prod([ZZ(i) for i=1:100000]);`
 - `@time prod([BigInt(i) for i=1:100000]);`
and explain the differences. Can you improve it further?

Everyone(?) knows that in `Z[\sqrt -5]` we have non-unique factorisation
   (of 6 e.g.). Find more examples?

For a given integer `n` there is a function that find the largest
   exponent $e$ s.th. `n = a^e`. Write s.th. similar for polynomials.

#### Calling into GAP

You can call any GAP function from OSCAR and vice versa. Have a look
at the README and manual of [GAP.jl](https://github.com/oscar-system/GAP.jl).

- Locate an interesting package on <https://www.gap-system.org/packages/>
  (e.g. `fr` if you are Leon)
  and try loading it in Julia (via GAP.jl's `GAP.Packages.load` command).
- Look at its manual and try to replicate some of the examples there in Julia
- Pick some kind of object defined by the package or GAP which is not yet
  covered in OSCAR, and create a little Julia wrapper struct encapsulating
  these objects and providing a Julia-ish / OSCAR-ish interface to them.

### Introduction to version control with Git and GitHub


### Development workflows with Julia


### First steps to writing your own OSCAR functions


### Advanced development skills


## General exercises (easy)


#### Determinants
How many different algorithms for determinants are implemented?
What rings do they cover?
Where are they defined?

Hint: (in AbstractAlgebra: `AbstractAlgebra.det_clow`,  `AbstractAlgebra.det_df`, ...;
    Nemo: `Nemo.det_given_divisor`, ...;
    Hecke: ...;
    Oscar: ...)

Can you find references/ explanations for the algorithms implemented?
How many can you call?


#### Galois Theory
Let $K$ be $\mathbb{Q}[t]/f$ for f = $t^4-2$. This field is not normal.
 - Find the normal closure
 - Find the Galois group
 - Compare the Galois group to the automorphism group
 - Demonstrate the Galois-Correspondence (for the normal closure):
   For each subgroup of the Galois group find the corresponding subfield
   (This can be done "by hand" using automorphisms and automatically
   using the Galois machine)


#### Group Extensions
Construct all group extensions of $C_2$ by $C_2$.

What are the possible Galois groups for a field $K/\mathbb{Q}$ of degree 4
that has a subfield of degree 2 as well? Can you match this to the
group extensions?


#### Schur indices
Find a character and a group s.th. the Schur index is 2


#### Discriminants of number fields
Find a cubic cyclic field where the discriminant has 10 digits.


#### Ramification
Let $K$ be a normal number field and $P$ be a prime ideal in $K$
lying above the prime number $p$.
The ramification theory says that there is a field $K/D$ s.th.
$P\cap D/p$ is totally split, a field $K/U/D$ s.th. $P \cap U/P\cap D$
is inert and s.th. $P/P \cap U$ is totally ramified.

Find an explicit example and verify the properties above.

If this is too boring: for non-normal fields, there is a correspondence
between prime ideals and double cosets of the Galois group...


#### Group basics
Let $G$ be dihedral of order $20$. Create $G$ as
 - a permutation group
 - a PC group
 - a FP group

Find all irreducible representations of $G$.

Harder: Create $G$ as a group of 2x2 matrices over a suitable number field (or over the algebraic closure of $\mathbb{Q}$).
<details><summary>Hint</summary>Find transformation of the real plane that are automorphisms of a regular decagon.</details>


#### Subgroups
Let $G = M_{11}$.
 - How many subgroup does $G$ have?
 - Can you do this without finding all?
 - Find permutation representations of $G$ of degree $11$, $12$ and $22$
 - How many characters are rational?


#### Subgroup lattices
Let $G = S_4$. Find the
 - subgroup lattice
 - the sub-lattice of transitive subgroups
Assign names to as many of them as you can.

Hint/comment: draw the lattice on paper and label the groups by some id


#### Curves
Let $C = k[x, y]/ y^2-x^3+3x+2$ be a curve. For different fields $k\in\{\mathbb{Q}, F_2, F_3, F_7\}$
 - Find its genus.
 - Is it smooth?
 - Is it irreducible?

(via Geometry or Number Theory)


#### Riemann-Roch spaces
Find a plane curve over $k = F_7$ s.th. the Riemann-Roch space of the
trivial divsor (zero divisor) has $k$ dimension $> 1$ and s.th. the genus
is $>0$.

(via Geometry or Number Theory)


#### Intersection of number fields
Let $K$ and $L$ be two number fields. Find the intersection.
Figure out when this makes sense, is well defined, unique, ...


#### Linearly disjoint number fields
Decide if 2 number fields are linearly disjoint, ie. the splitting fields are
disjoint.


#### Intersection of affine lines (1)
Compute the intersection of 2 (non-parallel) lines in the affine plane
 - create the two lines separately
  (either as varieties or by describing them by ideals)
 - create the intersection
 - find the coordinates of the intersection point


#### Intersection of affine lines (2)
Compute the intersection of 2 pairs of parallel lines in the affine plane $\mathbb{Q}^2$
 - create each pair of parallel lines (either as algebraic set or using an ideal)
  Q: Why not as variety?
 - create the intersection
 - find an example where all intersection points are only defined over an extension field


#### Intersection of circles
Compute the intersection of 2 circles in $\mathbb{Q}^2$
 - create ideals describing the circles
 - create the ideal for the intersection
 - create the algebraic sets
 - find a field s.th. the intersection has points


#### Intersection of a circle and an ellipse
Compute the intersection of a circle and an ellipse in $\mathbb{Q}^2$.
Find an example, where you see all points (Bézout theorem) already as points in $\mathbb{Q}^2$


#### Matrix groups over finite fields

Let $G = \mathrm{SL}_5(\mathbb{F}_3)$.
1. Compute a random element $m\in G$.
   <details><summary>Hint</summary><em>Use <code>rand_pseudo</code> to get
   random elements without enumerating the group.</em></details>

2. Compute its minimal polynomial $f$
   <details><summary>Hint</summary><em>Use <code>matrix</code> to turn a group element into a matrix.</em></details>

3. Determine the set $\{f_1,\dots,f_k\}$ of irreducible factors of $f$.
   <details><summary>Hint</summary><em>You can iterate over the results of <code>factor</code> to
   get the irreducible factors.</em></details>

4. Evaluate each $f_i$ at the matrix, and compute the eigenvalues and eigenspaces of
   the resulting matrices over $\mathbb{F}_3$.


## General exercises (harder)


#### Surfaces
Write functions that given some mystery surface $V(....)$ do the following:
- Find the following numerical invariants: dimension, degree.
- Find its singular locus.
- Blow up at the singular locus.

Test your functions on $V(x^3+y^3+z^3+xyz,v^4+w^4+xvzw)$ in $\mathbb{P}^4$.


#### Schemes
Write function that given some mystery scheme $X=V(...)$ do the following:
- Find the singular locus.
- Which components of the singular locus arise from intersections of components of $X$?
- Which components of the singular locus arise from singularities of components of $X$?

Test your functions on $X = V((x^2-y^2z)((x-1)^2+y^2+z^2))$.


#### Syzygies and free resolutions
Write functions that given some ideal $I$ in a multivariate polynomial ring do the following:
- Find the first syzygy module of the given generating set of $I$.
- Find a minimal free resolution of $I$.
- Find the Castelnuovo-Mumford regularity of $I$.

Test your functions on $(xy,xz,xw,yz,yw,zw)$.


#### Number theory
Find an approximation for, and the minimal polynomial, $m$, of
$\alpha = root(2,2) + root(3,3) + ... + root(9,9)$
[Hint: use the algebraic closure of $\mathbb{Q}$]
1. What is the degree of $m$?
2. Find an odd prime number, $p$, such that $m$ splits into linear factors $mod p$
    [Hint: there is no such prime below 3000000, three million]
3. Assuming all roots are positive, explain how to compute an
approximation to $\alpha$ within $\epsilon = 10^{(-k)}$;
actually compute the approximations for $k=10$ and $k=100$.


#### Sums of square-roots
A well-known computational complexity problem is that of determining
which of two sums of square-roots of integers is the greater.
For brevity we write $\{n_1, n_2, ..., n_k\}$ to mean the sum of their square-roots.
1. Which is bigger $\{100, 778, 929, 1366\}$  or  $\{99, 627, 661, 1992\}$?
2. Which is bigger $\{22, 44, 65, 291, 1384\}$  or  $\{43, 76, 201, 252, 802\}$?
   [Hint: if it takes more than 100s, stop the computer and think]
3. Which is bigger $\{7,14,39,70,72,76,85\}$  or  $\{13,16,46,55,67,73,79\}$?
4. Is the problem easier if the two sums are not close?


#### Graph colouring via Groebner bases
Let $G = (V,E)$ be a (finite, simple) graph with vertices $V$ and edges $E$;
each edge is specified by a subset of 2 vertices (there are no loops).
Let $C$ be a colour palette: a set of colours.  A $C$-vertex-colouring of $G$
is a map $col: V \to C$ such that if $\{v_1, v_2\}$ is an edge then $col(v_1)$ is
different from $col(v_2)$, i.e. any two vertices joined by an edge have
different colours.  The main questions are: does $G$ have a $C$-colouring,
and if so, produce (at least) one such colouring.

Recall the "weak" Nullstellensatz: a polynomial system $S = \{f_1,...,f_r\}$
has no solution (in the algebraic closure) iff the ideal generated by
$\{f_1,...,f_r\}$ contains 1.

The problem can be converted into a question about solving a polynomial system.
Let $P = k[v_1, ..., v_n]$ be a polynomial ring where $n$ is the number of vertices in $G$.
Let $C$ be a subset of $k$, and define $COL(x) = \prod( x-c  \text{ for } c \in C )$,
so each $COL(v_k)$ is a polynomial in $P$.
Note that $COL(v_k)$ is square-free for every $v_k$.
Observe that $EDGE(x,y) := (COL(x)-COL(y))/(x-y)$ is a polynomial in $P$
whenever $x$ and $y$ are in $P$.
Let $c_1,c_2$ be in $C$; observe also that $EDGE(c_1,c_2)$ is zero if $c_1$ and $c_2$ are different, and non-zero if $c_1 = c_2$.
Let $S$ be the polynomial system generated by $COL(v_k)$ for $k=1,2,...,n$
and by $EDGE(v_i,v_j)$ for every $\{v_i,v_j\} \in E$.
Then any solution to $S$ is a $C$-colouring of $G$; indeed each solutions to $S$
gives a distinct colouring of $G$.  By the Nullstellensatz there is no
$C$-colouring of $G$ iff the ideal generated by these polynomials contains 1.

Write an OSCAR function which takes as input a `Vector{Tuple{Int,Int}}`
denoting the edges, and an `Int` denoting the cardinality of $C$, and which
determines whether there is a $C$-colouring, and if so produces one.


#### Sudoku
Develop an OSCAR function which solves Sudoku puzzles.
The input is an OSCAR matrix of integers ranging from 0 to 9, where 0
denotes an empty square, and the other values represent the given
starting configuration.


#### Polynomials whose square has few terms
Find a (univariate) polynomial whose square contains no more terms than
the polynomial itself -- we exclude trivial examples such as $c * x^k.$
The basic idea is to search degree by degree; in each degree, $d$, we start with
a "generic" polynomial of degree $d$: $f = \sum( a_k*x^k \mid k=0,1,...,d )$
To simplify matters we assume that all the $a_k$ are non-zero.
The coefficients of $f^2$ are polynomials in the $a_k$.  If $f^2$ has at most as
many (non-zero) terms as $f$ then at least $d$ of the coefficients in $f^2$ must be zero.  We don't know which subset of coefficients are zero, but there
are only finitely many, so we can try them all.  For each candidate subset
we seek solutions to the polynomial system defined by the vanishing of
the polynomials belonging to our "putative" subset of zero coefficients
in the square.  Recall that the polynomial system has no solutions iff
the ideal generated by the polynomials contains 1 (think of the "Weak Nullstellensatz").
You now have enough information to start searching!

<details><summary>Hint</summary>the condition "$X$ must be non-zero" can be expressed by the polynomial
equation $X*dummy-1 = 0$ where "dummy" is a new "dummy" variable;
if both $X_1$ and $X_2$ must be non-zero use $X_1*dummy_1-1$ and $X_2*dummy_2-1$ or
the single polynomial $X_1*X_2*dummy-1$.</details>


---

<p class="message">
You can also have a look at
the <a href="{{site.baseurl}}/events/meetings/2021-09/exercises">exercises from our last summer school</a>.
</p>
