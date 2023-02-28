---
layout: meeting
title: Exercises
meeting: true
meeting_nr: 202109
---

<!--
<p class="message">
This is a live document and will be updated during the week.
</p>
-->

* This will become a table of contents (this text will be scrapped).
{:toc}


## Bring your own problem

### 1. Questions and problems

If you have any questions about or problems with anything related to the workshop,
talk to us! Via gather.town, Slack, email, telephone, carrier pigeon, ...

Do you need help with the Git/Github setup for your project? Would you like do discuss when to use another branch? When do you commit? After every line you changed?

For some problem areas, participants volunteered to help out, so you can also ask them.
(Feel free to add your name here).

  - git: Jens Brandt, ...
  - Julia: Tommy Hofmann, Daniel Schultz, ...
  - Oscar: Tommy Hofmann, Daniel Schultz, ...

### 2. Work on your own Julia/Oscar code

If you are already working on Julia code, possibly even are using Oscar, e.g. for your thesis project, feel free to continue working on that, and just asking us for general help.

Although, if you are already that good at it, surely finishing a few exercises quickly won't be a problem for you, so why not try? You might still learn something here or there.


## Git and GitHub exercises

### 1. Exercise solutions in git

  1. Fork the repository <https://github.com/oscar-system/Summerschool21Exercises.jl> and clone this to your computer.

  2. In the `solutions` directory in your local clone, create a subdirectory whose name is your GitHub username, and add solutions to some of the exercises to this directory, commit them, and push them to your fork.

  3. Optionally, if you want, create a pull request to merge the additions into the original repository.

  (Note: Forks of public repositories are automatically public.  With some effort, you can create a corresponding private repository, or one with restricted access if you want.)

### 2. git in the browser

  1. Go to the [participants list](https://www.oscar-system.org/meetings/2021-09/participants/) in your web browser

  2. Follow the "Edit this page" link in the navigation sidebar (resp. at the very end of the page, if your browser window is narrow / you are using a mobile browser)

  3. Edit your entry in the participants list by adding your GitHub username (using the syntax already in use for some of the entries)

  4. Submit your change as a pull request.


## Julia exercises

You may wish to consult the [Julia documentation](https://docs.julialang.org/en/v1/).

### 1. Hello

  1. Implement a hello world function `hello_world()` which prints "hello world".

  2. Implement a hello function `hello(name::String)` which prints "hello x", where x is the first argument.


### 2. Collatz conjecture

  1. Implement a function `f(n::Int)` which returns $n/2$ if $n$ is even and $3n + 1$ if $n$ is odd.

  2. Implement a function `g(n::Int)` which determines the smallest $k$ with $f^k(n) = 1$.

  3. Write a program which finds two numbers $> 100$ for which $g$ returns the same value.


### 3. Pascal triangle

  Implement a function `pascal_triangle(n)` which prints the first $n$ rows of Pascal's triangle.
  For example, `pascal_triangle(5)` should print
  ```
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
  ```
  At the start, you might consider ignoring the proper layout of the triangle.

### 4. My permutation

  Consider the following type, which defines a permutation:

  ```julia
  struct Permutation
    images::Vector{Int}
  end
  ```

  Thus the permutation with `images` set to `[1, 2, 3]` is the identity on 3 letters and
  `[2, 1, 3]` is the transposition $(1, 2)$ on 3 letters.

  1. Fill in the stub below to write a function for multiplying two permutations.
     Permutations are applied from the right, so that $(1, 2)(2, 3) = (1, 3, 2)$.

     ```julia
     function *(x::Permutation, y::Permutation)
     end
     ```

     Test your function by computing `Permutation([2, 1, 3]) * Permutation([1, 3, 2])`.

  2. Write a function `apply` that applies a `Permutation` to an `Int`. Make sure that the function has the right signature.

     ```julia
     function apply(p::Permutation, x::Int)
     end
     ```

     Test your function:

     ```julia
     p = Permutation([2, 3, 4, 5, 1])
     println(apply(p, 1) == 2)
     println(apply(p, 5) == 1)
     ```

  3. Write another `apply` method that entry-wise applies a permutation to a tuple.

      ```julia
      function apply(p::Permutation, x::Tuple)
      end
      ```

      Test your function
      ```julia
      p = Permutation([2, 3, 4, 5, 1])
      println(apply(p, (1, 5)) == (2, 1))
      ```

  4. Write an `apply!` function that modifies a given `Vector` of the right length by permuting its entries according to `x[i] = x[p(i)]`, and returns it.

      ```julia
      function apply!(p::Permutation, x::Vector)
      end
      ```

      Test your function:

      ```julia
      p = Permutation([2, 3, 4, 5, 1])
      x = ["a", "b", "c", "d", "e"]
      println(apply!(p, x))
      println(x == ["b", "c", "d", "e", "a"])
      ```

  5. Derive a method `apply(p::Permutation, x::Vector)` which does the same as `apply!` without changing the input.

      ```julia
      p = Permutation([2, 3, 4, 5, 1])
      x = ["a", "b", "c", "d", "e"]
      println(apply(p, x) == ["b", "c", "d", "e", "a"])
      println(x == ["a", "b", "c", "d", "e"])
      ```

### 5. `Vector` vs `Tuple`

  1. Observe the difference in timings for the following two ways of calculating the
     millionth Fibonacci number (modulo 2^64).

     ```julia
     F(a::Tuple{Int, Int}) = (a[2], a[1]+a[2])
     F(a::Vector{Int})     = [a[2], a[1]+a[2]]

     function G(a, n)
       for i in 1:n
         a = F(a)
       end
       return a
     end

     @time G((0,1), 10^6)
     @time G([0,1], 10^6)
     ```

  2. Write a function `H` that accepts an input `n::Int` and returns a `Tuple{Bool, Int}`
     where the first return indicates whether `n` is a square and the second return
     is the positive square root if it exists or zero otherwise. You should have

     ```julia
     @assert H(0) == (true, 0)
     @assert H(1) == (true, 1)
     @assert H(2) == (false, 0)
     @assert H(3) == (false, 0)
     @assert H(4) == (true, 2)
     @assert H(-1) == (false, 0)
     ```

     Try to change `H` to return a vector and observe what happens to the type of the return.

### 6. Methods and functions

  1. What arguments does `pushfirst!` expect?
     {% include hint.html content="`methods`" %}

  2. Without `using Oscar`, list all functions that accept a `Vector` argument.
     {% include hint.html content="`methodswith`" %}

  3. After `using Oscar`, list all functions that accept an `FmpzPolyRing`.

  4. List all functions that accept both an `fmpz_mat` and an `fmpz`.

  5. Find the source code for the method computing the power `fmpz(2)^10`.
     {% include hint.html content="`@which`, `@less`, `@edit`" %}


### 7. Caching

  Write a function `cached(f)` that takes a function/callable object `f` and returns a new function which returns the same values as `f` but caches the return value for any input value.
  Test it with various functions:

  ```julia
  g = cached(+)
  println(g(1, 1) == 1 + 1)
  ```

  To check the caching, try the following function:

  ```julia
  h = function(s)
    sleep(1)
    return s
  end

  g = cached(h)
  @time g(1) # this should take 1 second
  @time g(1) # this should take almost no time
  @time g(2) # this should take 1 second
  ```


## Oscar exercises: Number theory and algebra

Exercises 1-8 provide opportunities to get to know Oscar and its functionality.
On the other hand, exercises 9-12 are about implementing functionality on your
own using basic functionality provided by Oscar.

You may wish to consult the [Oscar documentation](https://docs.oscar-system.org/stable/).

### 1. Vandermonde matrices

  1. Create the polynomial ring $R = \mathbf{Q}[x\_1,\dotsc,x\_5]$.
     {% include hint.html content="`PolynomialRing`" %}

  2. Create the Vandermonde matrix
      $$
         V = (x_i^j)_{1 \leq i \leq 5, 0 \leq j \leq 4} \in R^{5 \times 5}.
      $$
     {% include hint.html content="`matrix`" %}

  3. Compute and factorize the determinant $\det(V)$.
     {% include hint.html content="`det`, `factor`" %}

  4. Pick 10 random elements $p \in \mathbf{Q}^5$ and verify that $\det(V)(p) = \det(V(p))$.
     {% include hint.html content="`rand` (e.g. `rand(QQ, -2:2)`), `evaluate`, `map_entries`." %}


### 2. Invariants of number fields

  1. Define the number field $K = \mathbf{Q}(\sqrt[3]{65})$.
     {% include hint.html content="`number_field`" %}

  2. Determine the ring of integers $\mathcal{O}_K$ and its discriminant.
     {% include hint.html content="`ring_of_integers`, `discriminant`" %}

  3. Determine the class group $\mathrm{Cl}_K$.
     {% include hint.html content="`class_group`" %}

  4. Determine the set $S$ of prime ideals of $\mathcal{O}_K$ lying over $2$. Are these ideals ramified?
     {% include hint.html content="`prime_decomposition`, `prime_ideals_over`, `isramified`" %}

  5. How large is the subgroup of $\mathrm{Cl}_K$ generated by the classes of the ideals in $S$?
     {% include hint.html content="`order`" %}

### 3. Galois groups

  1. Determine the Galois group of $f = x^3 + x + 1 \in \mathbf{Z}[x]$.
     {% include hint.html content="`galois_group`, `number_field`" %}

  2. Find a polynomial of degree $6$ with the same Galois groups as $f$.
     {% include hint.html content="`normal_closure`, `defining_polynomial`, `isisomorphic`" %}

  3. Determine the Galois groups of $1000$ random monic, irreducible polynomials in $\mathbf{Z}[x]$ of degree $3$ and coefficients bounded in absolute value by $10$.
      What is the distribution?
     {% include hint.html content="`rand`, `setcoeff!`, `isirreducible`" %}

  4. For all transitive groups of order $4$, find a monic irreducible polynomial of degree $4$ of $\mathbf{Z}[x]$ with that Galois group (random monic polynomials with coefficients in absolute value bounded by $10$ will do).
     {% include hint.html content="`transitive_group_identification`, `number_transitive_groups`, `count`" %}

### 4. Abelian extensions

  1. Define the number field $K = \mathbf{Q}(\sqrt{2})$.
     {% include hint.html content="`number_field`" %}

  2. Find a normal extension $L/K$ such that $\operatorname{Gal}(L/K)$ is non-cyclic of order $4$.
     {% include hint.html content="`automorphism_group`, `iscyclic`, `order`" %}

  3. Find all normal extension $L/K$ with $\operatorname{Gal}(L/K) \cong C_2 \times C_2$ such that $L/\mathbf{Q}$ is normal and the absolute discriminant of $L$ is bounded by $10^{10}$.
     {% include hint.html content="`abelian_normal_extensions`" %}

  4. Determine a defining polynomial for one of the fields $L$ found in part 3. What is $\operatorname{Gal}(L/\mathbf{Q})$?
     {% include hint.html content="`absolute_simple_field`, `galois_group`, `describe`" %}

### 5. Determinantal variety

  1. Define the polynomial ring $R = {\mathbf{F}}{\_4}[x\_{ij} \mid 1 \leq i \leq 3, 1 \leq j \leq 3]$.
     {% include hint.html content="`PolynomialRing`, `FiniteField`, `GF`" %}

  2. Define the matrix $M = (x\_{ij})\_{1 \leq i \leq 3, 1 \leq j \leq 3} \in R^{3 \times 3}$.
     {% include hint.html content="`matrix`" %}

  3. Determine the defining ideal of the determinantal variety $V$ of size $3 \times 3$ and rank 1, which is defined as the vanishing set of the $2$-minors of $M$.
     {% include hint.html content="`minors`, `ideal`" %}

  4. What is the dimension of $V$?
     {% include hint.html content="`dim`" %}

  5. Determine $\lvert V(\mathbf{F}_4) \rvert$, where $V(\mathbf{F}\_4) \subseteq \mathbf{F}_4^9$.
     {% include hint.html content="`AbstractAlgebra.ProductIterator`, `evaluate`, `all`" %}

### 6. Gröbner bases

  1. Define the polynomial ring $R = \mathbf{Q}[x, y, z]$.
     {% include hint.html content="`PolynomialRing`" %}

  2. Define the ideal $I = \langle xy + z, yz − x, zx − y \rangle$.
     {% include hint.html content="`ideal`" %}

  3. Determine $\dim(I)$.
     {% include hint.html content="`dim`" %}

  4. Compute a Gröbner basis of $I$ with respect to the lexicographical ordering.
     {% include hint.html content="`groebner_basis`" %}

  5. Is $I$ a prime ideal?
     {% include hint.html content="`isprime`" %}

  6. Find a prime ideal containing $I$.
     {% include hint.html content="`issubset`" %}

### 7. Integral lattices

  1. Define the $\mathbf{Z}$-lattice $L$ with Gram matrix
     $$
        \begin{pmatrix}
        2 & 1 & 1 \\
        1 & 2 & 1 \\
        1 & 1 & 68
        \end{pmatrix}.
     $$
     {% include hint.html content="`Zlattice`, `matrix`" %}

  2. Determine generators $S$ for the automorphism group of $L$ and its order.
     {% include hint.html content="`automorphism_group_generators`, `automorphism_group_order`" %}

  3. Define the matrix group $G = \langle S \rangle \subseteq \operatorname{GL}_3(\mathbf{Q})$.
     {% include hint.html content="`matrix_group`" %}

  4. Find an isomorphic matrix group $H$ over a finite field.
     {% include hint.html content="`Oscar.isomorphic_group_over_finite_field`" %}

  5. Can you find out which group this is?
     {% include hint.html content="`describe`" %}

  6. Find representatives for the isometry classes in the genus of $L$.
     {% include hint.html content="`genus_representatives`" %}

  7. Use the mass formula to show that the result of part 6 is correct ($\operatorname{mass}(L) = \sum_{L'} 1/\lvert \operatorname{Aut}(L') \rvert$, where the sum runs over a set of genus representatives of $L$).
     {% include hint.html content="`mass`" %}

### 8. Lattices from number fields

  1. Create the number field $K$ with defining polynomial $x^3 - 54x - 150 \in \mathbf{Q}[x]$.
     {% include hint.html content="`number_field`" %}

  2. Determine the $\mathbf{Z}$-lattice $L = (\mathcal{O}_K, q)$, where $q$ is the quadratic form
     associated to the trace pairing.
     {% include hint.html content="`Zlattice`, `basis`, `trace`" %}

  3. What is the signature of $L$? What is the signature of $K$?
     {% include hint.html content="`signature`" %}

  4. Consider the fields $K_1$ and $K_2$ defined by $x^3 - 36x - 78$ and $x^3 - 18x - 6$ respectively. For $K_1$ and $K_2$ construct lattices $L_1$ and $L_2$.
     Are the fields $K_i$ isomorphic to $K$? Are the lattices $L_i$ in the same genus as $L$? Are the lattices $L_i$ isometric to $L$?
     {% include hint.html content="`genus`, `isisometric`, `isisomorphic`" %}

### 9. Product of rings

  The goal of this exercise is to implement $R \times S$, the product of two commutative rings $R$ and $S$.

  ```julia
  mutable struct ProdRing{S, T} <: AbstractAlgebra.Ring
    first::S
    second::T
  end
  ```

  ```julia
  mutable struct ProdRingElem{U, V} <: AbstractAlgebra.RingElem
    first::U
    second::V
    parent
  end
  ```

  Implement enough functionality to make the following work:

  ```julia
  R = product_ring(ZZ, QQ)
  a = R(ZZ(2), QQ(1, 2))
  M = matrix(R, 2, 2, [1, a, 0, 1])
  M * M
  Rx, x = R["x"]
  f = (a * x)^2
  ```

  Assuming that both rings are Euclidean and support the `divrem` function, implement
  `divrem` also for product rings. Try to make the following work:

  ```julia
  hnf(M)
  ```

  As an example for a ring implementation, consider the implementation of $\mathbf{Z}[i]$ [here](https://github.com/ulthiel/GaussianIntegers.jl/blob/master/src/GaussianIntegers.jl).

### 10. Skew-polynomial rings

  Let $S = R[X]$ be the set of all polynomials $\sum_{i} a_i X^i$ and $f$ a ring endomorphism of $R$. We define $X \cdot r = f(r)\cdot X$ for $r \in R$. With the ordinary additional of polynomials, this yields a skew-polynomial ring, which we want to implement.

  ```julia
  mutable struct SkewPolyRing{S, T} <: NCRing
    poly_ring::S
    f::T
  end

  mutable struct SkewPolyRingElem{U} <: NCRingElement
    poly::U
    parent
  end
  ```

  The goal is to make the following work:

  ```julia
  F, a = FiniteField(3, 2, "a")
  S, x = skew_polynomial_ring(F, a -> a^3, "x")
  f = F(2) * x
  g = f * F(3)
  M = matrix(S, 2, 2, [1, f, 0, 1])
  M * M
  ```

  As an example for a ring implementation, consider the implementation of $\mathbf{Z}[i]$ [here](https://github.com/ulthiel/GaussianIntegers.jl/blob/master/src/GaussianIntegers.jl).

### 11. $\mathbf{Z}[\sqrt{2}]$ as an Euclidean ring

  The aim of this exercise is to implement the ring $\mathbf{Z}[\sqrt{2}]$ together with its Euclidean structure, which is determined by the Euclidean function $v(a + b \sqrt 2) = \lvert a^2 - 2b^2 \rvert$.
  To satisfy the ring interface, we will use the following type for the parent:

  ```julia
  mutable struct ZZSqrt2
  end
  ```

  We will represent elements $a + b \sqrt 2$ using the following type:

  ```julia
  mutable struct ZZSqrt2Elem
    a::fmpz
    b::fmpz
    parent
  end
  ```

  Implement enough functions to make the following work

  ```julia
  R = ZZSqrt2()
  x = R(2, 3)
  y = R(0, 1)
  q, r = divrem(x, y)
  M = matrix(R, 2, 2, [1, 2, x, y])
  hnf(M)
  ```

  As an example for a ring implementation, consider the implementation of $\mathbf{Z}[i]$ [here](https://github.com/ulthiel/GaussianIntegers.jl/blob/master/src/GaussianIntegers.jl).

### 12. Inverting integer matrices

  The aim is to implement two methods to invert invertible integer matrices. The first method will be based on $p$-adic lifting and the second one on the Chinese remainder theorem.

  1. Implement a function

      ```julia
      function inverse_via_lifting(A, p)
      end
      ```

      which given an invertible integer matrix, determines the inverse via $p$-adic lifting and inversion of matrices over $\mathbf{F}\_p$.

      Hint: If $B$ is the inverse of $A$, write $B = B_0 + pB_1 + p^2 B_2 + \dotsb$ and reduce modulo $p$. There is no need to work with $p$-adic integers. It is sufficient to work in $\mathbf{Z}$ and $\mathbf{F}_p$. Helpful commands: `change_base_ring`, `inv`, `lift`, `divexact`.


  2. Implement a function

      ```julia
      function inverse_via_crt(A, startp)
      end
      ```

      which given an invertible integer matrix, determines the inverse using the Chinese remainder theorem and inversion of matrices over $\mathbf{F}\_p$ for various primes $p$.

      Helpful commands: `change_base_ring`, `inv`, `lift`, `crt`.

  3. Compare both functions on random matrices of different sizes.

  4. Can you do the same for matrices over $\mathbf{F}\_q[x]$ by replacing primes with irreducible polynomials?

## Oscar exercises: Group theory

You may wish to consult the [Oscar documentation](https://docs.oscar-system.org/stable/).

### 1. Fixed point free permutations

  1. Write a function $f$ which computes for small values of $n$, the number of fixed point free permutations on $n$ points. For example, $f(1)=0$, $f(2)=1$, $f(3)=2$, $f(4)=9$ and $f(30)=97581073836835777732377428235481$.
     {% include hint.html content="`symmetric_group`,  `conjugacy_classes`, `number_moved_points`" %}

  2. Write a function which computes the proportion $x(n)$ of these permutations in the symmetric group on $n$ points, and the first decimal digits of $x(n)$ and $1/x(n)$.

  3. Do you have a conjecture what $\lim_{n \rightarrow\infty} x(n)$ is?


### 2. Shuffle groups
  Inspect the groups returned by the following function, for small positive values of `n`.
  ```julia
  function shuffle_group(n::Int)
    out_perm = zeros(Int, 2*n)
    out_perm[1:2:(2*n-1)] = 1:n
    out_perm[2:2:(2*n)] = (n+1):(2*n)

    in_perm = zeros(Int, 2*n)
    in_perm[1:2:(2*n-1)] = (n+1):(2*n)
    in_perm[2:2:(2*n)] = 1:n

    sym = symmetric_group(2*n)
    return sub(sym, [sym(out_perm), sym(in_perm)])[1]
  end
  ```

  1. Determine the group orders.

  2. How many of the groups are abelian / perfect / simple / solvable?

  3. Can you give an interpretation what these groups describe?

### 3. Matrix groups

  Given a finite group $G$ of $n \times n$ matrices over `QQ`, find a matrix $T$ such that conjugation of $G$ with $T$ yields a group of matrices over `ZZ`.

  <small>Hint: More generally, let $R$ be a ring with quotient field $K$, and let $G$ be a matrix group over $K$. Let $m$ be an integer such that the entries of $m M$ are in $R$, for all $M \in G$, and consider the set $U = m R^n G$; then $U$ is a subset of $R^n$ and invariant under multiplication with elements of $G$.
  If we know that any finitely generated $R$-submodule of $R^n$ has an $R$-basis then we can compute the action of $G$ on $U$ w.r.t. such a basis.</small>

  1. Write a function that computes integral matrices from rational ones, as sketched in the hint.

  2. Apply the function to the group generated by the matrices

     $$
        \begin{pmatrix}
          25 &  -6 &   3 \\
          -5 &  -4 &  15 \\
           7 &  42 &   5
        \end{pmatrix} / 26,
        \quad
        \begin{pmatrix}
          11 &  14 &  19 \\
          37 & -64 & -33 \\
         -35 & 102 &  53
        \end{pmatrix} / 26.
     $$

  3. Usually groups are given by generators. Develop an algorithm that solves the problem from part 1. without running over all group elements.

  4. Does this method work also for (finitely generated) infinite groups?

### 4. Finitely presented groups

  1. Determine all groups (up to isomorphism) that are generated by three elements $x, y, z$ and such that the relations $xy = z$, $yz = x$ und $zx = y$ hold.
     {% include hint.html content="`free_group`, `gens` or `gen`, `quo`, `normal_subgroups`" %}


## Exercises related to Eamonn O'Brien's lectures

### First lecture

#### 1. Abelian quotients

1. Define the group $H = \langle x, y \mid x^2 y^2 = 1,  x^{-1} y^3 x^4 y = 1 \rangle$.
   {% include hint.html content="`free_group`, `gens` or `gen`, `quo`" %}

2. Write a Julia function that computes the isomorphism type of the abelian quotient $G/G'$ of a given `FPGroup` $G$ via the Smith normal form of the matrix of abelianized relators. Apply it to the group $H$ defined above.
   {% include hint.html content="`abelianized` (defined in [the Julia module in the repository for exercises](https://github.com/oscar-system/Summerschool21Exercises.jl)), `relators`, `snf`" %}

3. Test the function by comparing the results with the GAP function available in Oscar.
   {% include hint.html content="Use `GAP.Globals.AbelianInvariants(G.X)`. Note the difference between the diagonal of the Smith normal form and the result of the GAP function `AbelianInvariants`." %}

4. In order to write down a group epimorphism from $G$ to $G/G'$ that maps the generators of $G$ to the corresponding integer vectors, one needs not only the Smith normal form but also a transformation matrix.
    Write a Julia function that computes the epimorphism.

5. The entries in the transformation matrices that occur in the computation of the Smith normal form can get quite large.
    Make some experiments with random integer matrices whose entries have small absolute value.
    Consider also $n$ by $n$ diagonal matrices with diagonal entries $1, 2, \ldots, n$.

#### 2. Collection

  <small>Hint: There is a github repository with a [straightforward implementation of collection in pc groups](https://github.com/oscar-system/Summerschool21Exercises.jl).  You can (fork and) clone it, add the Julia module to your Julia session, and then extend and improve the code.</small>

1. Implement the collection process in Julia.
    That is, define data structures representing an (uncollected) word and a collector object that contains the relators of a consistent pc-presentation.

    Test the implementation for various groups:

    - Try different collection strategies (collection to the left, from the right, from the left, as defined in the talk), by providing suitable `findfirst_uncollected` functions.
      How many steps are needed for various examples?

    - What are the steps when one applies collection for multiplying elements in abelian groups?

    - Try also some infinite groups, for example the infinite dihedral group.

    - How can the implementation be simplified for finite groups and for finite $p$-groups?

2. The GAP system provides several implementations of collectors (written in C) for finite polycyclic groups.
    (And the GAP package `Polycyclic` deals also with collection for infinite polycyclic groups.)
    How can some of the tricks used in that code be used in the Julia implementation?

3. Implement a new type of elements in polycyclic groups for which multiplication and inversion are based on collection in Julia, not on underlying group elements in GAP.

4. The GAP help for "Pc Groups" (a chapter in the GAP Reference Manual) lists more rules for a power-conjugate presentation than the definition of a polycyclic presentation in the talk. Are the additional rules necessary?

### Second lecture

#### 1. Consistency algorithm

1. Implement the consistency algorithm for $p$-groups.
    That is, write a Julia function that takes a perhaps inconsistent pc-presentation (via a collector object, see the exercises for the first lecture), and returns a consistent one.

2. Implement a check whether a given pc-presentation is consistent.

3. The consistency theorem is stated for $p$-groups only.
    How would a consistency theorem for general polycyclic presentations look like?

#### 2. $p$-covering group

Write a function that takes a consistent pc-presentation of a $p$-group $G$ (via a collector object, see the exercises for the first lecture) and returns a consistent pc-presentation of the $p$-covering group of $G$.

### Third lecture

#### 1. Burnside groups

We know that the Burnside group $B(2,4)$ (the largest $2$-generator group of exponent $4$) is finite and has order $2^{12}$.
Find a proof for this statement, by constructing a presentation for $B(2,4)$, with suitable $4$-th powers as relators.

(It is known that the minimal number of relators is $9$.)

#### 2. Fibonacci groups

1. Write a function that creates the generalized Fibonacci groups $G_n(m, k)$ as a finitely presented group.

2. Use the theorem mentioned in the talk to prove that $G_9(1, 2)$ and $G_9(3, 4)$ are infinite.
   {% include hint.html content="The GAP implementation of the p-quotient algorithm can be used. Consider the first steps of the $p$-central series of a suitable subgroup of $G_9(1, 2)$, for a suitable $p$." %}
