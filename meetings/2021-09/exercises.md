---
layout: meeting
title: Exercises
meeting: true
meeting_nr: 202109
---

TODO: Exercises for the participants will appear here


# Git / GitHub exercises

1. Fork the repository XYZ

2. Create a pull request doing XYZ

3. ...


# Julia exercises

1. Hello

    1. Implement a hello world function `hello_world()`, which prints "hello world".
    2. Implement a hello function `hello(name::String)`, which prints "hello x", where x is the first argument.

2. Collatz conjecture
    
    1. Implement a function `f(n::Int)`, which returns $n/2$ if $n$ is even and $3n + 1$ if $n$ is odd.
    2. Implement a function `g(n::Int)`, which determines the smallest $k$ with $f^k(n) = 1$.
    3. Find two numbers $> 100$ for which $g$ returns the same value.

3. Pascal triangle

    Implement a function `pascal_triangle(n)` which prints the first $n$ rows of Pascal's triangle.
    For example, `pascal_triangle(5)` should return
    ```
       1
      1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
    ```
    At the start, you might consider ignoring the proper layout of the triangle.

4.  My permutation

    Consider the following type, which defines a permutation:

    ```julia
    struct Permutation
      images::Vector{Int}
    end
    ```

    Thus the permutation with field `[1, 2, 3]` is the identity on 3 letters and
    `[2, 1, 3]` is the transposition $(1, 2)$ on 3 letters.

    1.  Fill in the stub below to write a function for multiplying two permutations.
        Permutations are applied from the right, so that, $(1, 2)(2, 3) = (1, 2, 3)$.

        ```julia
        function *(x::Permutation, y::Permutation)
        end
        ```
    
        Test your function by computing `Permutation([2, 1, 3]) * Permutation([1, 3, 2])`.

    2.  Write a function `apply` that applies a `Permutation` to an `Int`. Make sure that the function has the right types.

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

    4. Write an `apply!` function that permutes the entries of a given `Vector` of the same length.

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

        Derive a method `apply(p::Permutation, x::Vector)`, which does the same as `apply!` without changing the input.

        ```julia
        p = Permutation([2, 3, 4, 5, 1])
        x = ["a", "b", "c", "d", "e"]
        println(apply(p, x) == ["b", "c", "d", "e", "a"])
        println(x == ["a", "b", "c", "d", "e"])
        ```

5. Caching*

    Write a function `cached(f)`, that given a function/callable object `f`, returns a variant of `f` which caches the values.
    Test it with various functions:

    ```julia
    g = cached(+)
    println(g(1, 1)) == 1 + 1
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
      
6. Vector vs Tuple

    1.  Observe the difference in timings for the following two ways of calculating the
        millionth Fibonacci number (modulo 2^64).

        ```
        F(a::Tuple{Int, Int}) = (a[2], a[1]+a[2])
        F(a::Vector{Int})     = [a[2], a[1]+a[2]]

        function G(a, n)
          for i in 1:n
            a = F(a)
          end
          a
        end

        @time G((0,1), 10^6)
        @time G([0,1], 10^6)
        ```

    2.  Write a function `H` that accepts an input `n::Int` and returns a `Tuple{Bool, Int}`
        where the first return indicates whether `n` is a square and the second return
        is the positive square root if it exists or zero otherwise. You should have

        ```
        @assert H(0) == (true, 0)
        @assert H(1) == (true, 1)
        @assert H(2) == (false, 0)
        @assert H(3) == (false, 0)
        @assert H(4) == (true, 2)
        @assert H(-1) == (false, 0)
        ```

        Try to change `H` to return a vector and observe what happens to the type of the return.

7. `methods` and `methodswith`

    1.  What arguments does `pushfirst!` expect?
    2.  Without `using Oscar`, list all functions that accept a `Vector` argument.
    3.  After `using Oscar`, list all functions that accept an `FmpzPolyRing`.
    4.  List all functions that accept both an `fmpz_mat` and an `fmpz`.


# Oscar exercises

## Number theory and algebra

1. Vandermonde matrices
    1. Create the polynomial ring $R = \mathbf{Q}[x\_1,\dotsc,x\_5]$.
    2. Create the Vandermonde matrix $$
        V = (x_i^j)\_{1 \leq i \leq 5, 0 \leq j \leq 4} \in R^{5 \times 5}
       $$

    3. Compute and factorize the determinant $\det(V)$.
    4. Pick 10 random elements $p \in \mathbf{Q}^5$ and verify that $\det(V)(p) = \det(V(p))$.

    <small>Hint:`PolynomialRing`, `factor`, `rand`, `evaluate`, `map_entries`</small>


2. Invariants of number fields.

    1. Define the number field $K = \mathbf{Q}(\sqrt[3]{65})$.
    2. Determine the ring of integers $\mathcal{O}_K$ and its discriminant.
    3. Determine the class group $\mathrm{Cl}_K$.
    4. Determine the set $S$ of prime ideals of $\mathcal{O}_K$ lying over $2$. Are these ideals ramified?
    5. How large is the subgroup of $\mathrm{Cl}_K$ generated by the classes of $S$?

    <small>Hint: `number_field`, `ring_of_integers`, `discriminant`, `class_group`, `prime_decomposition`, `preimage`.</small>

3. Galois groups

    1. Determine the Galois group of $f = x^3 + x + 1 \in \mathbf{Z}[x]$.
    2. Find a polynomial of degree 6 with the same Galois groups as $f$.
    3. Determine the Galois groups of 10000 random irreducible polynomials in $\mathbf{Z}[x]$ of degree $3$ and coefficients bounded in absolute value by $100$. What is the distribution?
    4. For all transitive groups of order 5, find an irreducible polynomial of degree 5 of $\mathbf{Z}[x]$ with that Galois group.

    <small>Hint: `galois_group`, `number_field`, `normal_closure`, `defining_polynomial`, `rand`, `transitive_group_identification`, `number_transitive_groups`</small>

4. Abelian extensions

    1. Define the number field $K = \mathbf{Q}(\sqrt[3]{2})$.
    2. Find a normal extension $L/K$ such that $\operatorname{Gal}(L/K) \cong \operatorname{C_2} \times \operatorname{C_4}$.
    3. Find a normal extension $L/K$ as in part 2 such that $L/\mathbf{Q}$ is normal.
    4. Determine $\operatorname{Gal}(L/\mathbf{Q})$ for the field found in part 3.

    <small>Hint: `number_field`, `abelian_extensions`, `abelian_normal_extensions`, `absolute_field`, `automorphism_group`, `galois_group`</small>

5. Determinantal variety

    1. Define the polynomial ring $R = {\mathbf{F}}{\_4}[x\_{ij} \mid 1 \leq i \leq 3, 1 \leq j \leq 3]$.
    2. Define the matrix $$
        M = (x_{ij})_{1 \leq i \leq 3, 1 \leq j \leq 3} \in R^{3 \times 3}
       $$

    3. Determine the determinantal variety $V$ of size $3 \times 3$ and rank 1, which is defined as the vanishing set of the $2$-minors of $M$.
    4. Determine the dimension of $V$?
    5. Determine $\lvert V(\mathbf{F}_4) \rvert \subseteq \mathbf{F}_4^9$.

    <small>Hint: `polynomial_ring`, `FiniteField`, `matrix`, `minors`, `dim`, `Oscar.AbstractAlgebra.ProductIterator`.</small>

6. Gröbner bases

    1. Define the polynomial ring $R = \mathbf{Q}[x, y, z]$.
    2. Define the ideal $I = \langle xy + z, yz − x, zx − y \rangle$.
    3. Determine $\dim(I)$.
    4. Compute a Gröbner basis of $I$ with respect to the lexicographical ordering.
    5. Determine $V(\mathbf{Q}) \subseteq \mathbf{Q}^3$.
    6. Determine $V(\mathbf{Q}[i]) \subseteq \mathbf{Q}[i]^3$.

    <small>Hint: `polynomial_ring`, `ideal`, `groebner_basis`, `to_univariate`, `roots`.</small>

7. Integral lattices

    1. Define the $\mathbf{Z}$-lattice $L$ with Gram matrix
       $$
       \begin{pmatrix}
       2 & 1 & 1 \\
       1 & 2 & 1 \\
       1 & 1 & 68
       \end{pmatrix}
       $$
     2. Determine generators $S$ for the automorphism group of $L$ and its order.
     3. Define the matrix group $G = \langle S \rangle \subseteq \operatorname{GL}_3(\mathbf{Q})$.
     4. Determine the maximal subgroups of $G$. Can you find out which group this is?
     5. Determine the class number of $L$.
     6. Find representatives for the isometry classes in the genus of $L$.
     7. Use the mass formula to show that the result of part 6 is correct.

     <small>Hint: `Zlattlice`, `automorphism_group_generators`, `automorphism_group_order`, `maximal_subgroups`, `genus_representatives`, `mass`.</small>

8. Lattices from number fields

    1. Define $K = \mathbf{Q}(\sqrt{2})$.
    2. Determine the $\mathbf{Z}$-lattice $(\mathcal{O}_K, q)$, where $q$ is the quadratic form
    associated to the trace pairing.
    3. Determine the class number of $L$.
    4. Try to represent each isometry class in the genus of $L$ as a lattice attached to a number field.

    <small>Hint: `number_field`, `ring_of_integers`, `tr`, `Zlattice`, `genus_representatives`, `isisometric`.</small>

## Implement something your own

1. Product of rings.
   
    The goal of this exercise is two implement $R \times S$, the product of two commutative rings $R$ and $S$.

    ```julia
    mutable struct ProdRing{S, T} <: Ring
      first::S
      second::T
    end
    ```

    ```julia
    mutable struct ProdRingElem{U, V} <: RingElement
      first::S
      second::T
      parent
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

    As an example, consider the implementation of $\mathbf{Z}[i]$ [here](https://github.com/ulthiel/GaussianIntegers.jl/blob/master/src/GaussianIntegers.jl).

2.  Skew polynomial rings

    Let $S = R[X]$ be the set of all polynomials $\sum_{i} a_i X^i$ and $f$ a ring endomorphism of $R$. We define $X^n \cdot r = f(r)\cdot X^n$ for $r \in R$. With the ordinary additional of polynomials, this yields a skew-polynomial ring, which we want to implement.

    ```julia
    mutable struct SkewPolyRing{S, T} <: NCRing
      poly_ring::S
      f::T
    end

    mutable struct SkewPolyRingElem{U} <: NCRingElement
      poly::U
      parent
    ```

    The goal is to make the following work:

    ```julia
    S, x = skew_polynomial_ring(QQ, a -> 1//a, "x")
    f = QQ(2) * x
    g = f * QQ(3)
    M = matrix(S, 2, 2, [1, f, 0, 1])
    M * M
    ```

    As an example, consider the implementation of $\mathbf{Z}[i]$ [here](https://github.com/ulthiel/GaussianIntegers.jl/blob/master/src/GaussianIntegers.jl).

3.  $\mathbf{Z}[\sqrt{2}]$ as an Euclidean ring

    The aim of this exercise is to implement the ring $\Z[\sqrt{2}]$ together with its Euclidean structure, which is determined by the Euclidean function $v(a + b \sqrt 2) = \lvert a^2 - 2b^2 \rvert$.
    To satisfy the ring interface, we will use the following type for the parent.

    ```julia
    mutable struct ZZSqrt2Elem
    end
    ```

    We will represent elements of a + b \sqrt 2$ using the following type:

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

4.  Inverting integer matrices

    The aim is to invert an invertible integer matrix $M \in \mathbf{Z}^{n \times n}$ using the Chinese remainder theorem and $p$-adic lifting

    1. Implement a function
        
        ```julia
        function inverse_via_lifting(A, p)
        end
        ```
       
        which given an invertible integer matrix, determines the inverse via $p$-adic lifting and inversion of matrices over $\mathbf{F}\_p$.

        Hint: If $B$ is the inverse of $A$, write $B = B_0 + pB_1 + p^2 B_2 + \dotsb$ and reduce modulo $p$.


    2. Implement a function

        ```julia
        function inverse_via_crt(A, startp)
        end
        ```

        which given an invertible integer matrix, determines the inverse using the Chinese remainder theorem and inversion of matrices over $\mathbf{F}\_p$ for various primes $p$.

    3. Compare both functions on random matrices of different sizes.

    4. Can you do the same for matrices over $\mathbf{F}\_q[x]$ by replacing primes with irreducible polynomials?

1. TODO

2. TODO

3. ....

## Group theory

1.  Given a finite group $G$ of $n \times n$ matrices over `QQ`, find a matrix $T$ such that conjugation of $G$ with $T$ yields a group of matrices over `ZZ`.

    <small>Hint: More generally, let $R$ be a ring with quotient field $K$, and let $G$ be a matrix group over $K$.  Let $m$ be an integer such that the entries of $m M$ are in $R$, for all $M \in G$, and consider the set $U = m R^n G$; then $U$ is a subset of $R^n$ and invariant under multiplication with elements of $G$.
    If we know that any finitely generated $R$-submodule of $R^n$ has an $R$-basis then we can compute the action of $G$ on $U$ w.r.t. such a basis.</small>

    1.  Write a function that computes integral matrices from rational ones, as sketched in the hint.

    2.  Apply the function to the group generated by the matrices
        $$
           \begin{pmatrix}
             25 &  -6 &   3 \\
             -5 &  -4 &  15 \\
              7 &  42 &   5
           \end{pmatrix} / 26,
           \begin{pmatrix}
             11 &  14 &  19 \\
             37 & -64 & -33 \\
            -35 & 102 &  53
           \end{pmatrix} / 26.
        $$

    3.  Usually groups are given by generators.  Develop an algorithm that solves the problem from part 1. without running over all group elements.

    4.  Does this method work also for (finitely generated) infinite groups?


2. TODO

3. ....

## Exercises related to Eamonn O'Brien's first lecture

1.  Abelian quotients

    1.  Write a Julia function that computes the isomorphism type of the abelian quotient $G/G'$ of a given `FPGroup` $G$ via the Smith normal form of the matrix of abelianized relators.

        <small>Hint: The Oscar function `snf` for computing the Smith normal form can be used.</small>

        Test the function by comparing the results with the function available in Oscar.
        (Note the difference between the diagonal of the Smith normal form and the result of the GAP function `AbelianInvariants`.)

    2.  In order to write down a group epimorphism from $G$ to $G/G'$ that maps the generators of $G$ to the corresponding integer vectors, one needs not only the Smith normal form but also a transformation matrix.
        Write a Julia function that computes the epimorphism.

    3.  The entries in the transformation matrices that occur in the computation of the Smith normal form can get quite large.
        Make some experiments with random integer matrices whose entries have small absolute value.
        Consider also $n$ by $n$ diagonal matrices with diagonal entries $1, 2, \ldots, n$.

2.  Collection

    <small>Hint: There is a github repository with a [straightforward implementation of collection in pc groups](https://github.com/ThomasBreuer/Summerschool21Exercises.jl).  You can clone it, add the Julia module to your Julia session, and then extendand improve the code.</small>

    1.  Implement the collection process in Julia.
        That is, define data structures representing an (uncollected) word and a collector object that contains the relators of a consistent pc-presentation.

        Test the implementation for various groups:

        - Try different collection strategies, by providing suitable `findfirst_uncollected` functions.  How many steps are needed for various examples?

        - What are the steps when one applies collection for multiplying elements in abelian groups?

        - Try also some infinite groups, for example the infinite dihedral group.

        - How can the implementation be simplified for finite groups and for finite $p$-groups?

    2.  The GAP system provides several implementations of collectors (written in C) for finite polycyclic groups.
        (And the GAP package `Polycyclic` deals also with collection for infinite polycyclic groups.)
        How can some of the tricks used in that code be used in the Julia implementation?

    3.  Implement a new type of elements in polycyclic groups for which multiplication and inversion are based on collection in Julia, not on underlying group elements in GAP.

## Exercises related to Eamonn O'Brien's second lecture

1.  Consistency algorithm

    1.  Implement the consistency algorithm for $p$-groups.
        That is, write a Julia function that takes a perhaps inconsistent pc-presentation (via a collector object, see the exercises for the first lecture), and returns a consistent one.

    2.  Implement a check whether a given pc-presentation is consistent.

    3.  The consistency theorem is stated for $p$-groups only.
        How would a consistency theorem for general polycyclic presentations look like?

2.  $p$-covering group

    Write a function that takes a consistent pc-presentation of a $p$-group $G$ (via a collector object, see the exercises for the first lecture) and returns a consistent pc-presentation of the $p$-covering group of $G$.

## Exercises related to Eamonn O'Brien's third lecture

1.  Burnside groups

    We know that the Burnside group $B(2,4)$ (the largest $2$-generator group of exponent $4$) is finite and has order $2^{12}$.
    Find a proof for this statement, by constructing a presentation for $B(2,4)$, with suitable $4$-th powers as relators.

    (It is known that the minimal number of relators is $9$.)

2.  Fibonacci groups

    1.  Write a function that creates the generalized Fibonacci groups $G_n(m, k)$ as a finitely presented group.

    2.  Use the theorem mentioned in the talk to prove that $G_9(1, 2)$ and $G_9(3, 4)$ are infinite.

        <small>Hint: The GAP implementation of the p-quotient algorithm can be used.
        Consider the first steps of the $p$-central series of a suitable subgroup of $G_9(1, 2)$, for a suitable $p$.</small>


## TODO more Oscar topic ....

