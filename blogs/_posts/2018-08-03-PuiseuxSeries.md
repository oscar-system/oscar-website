---
layout: post
title: "Puiseux Series: a challenging computation"
author: William Bruce Hart
---

Recently we encountered an interesting computational problem that seems to be difficult
for existing computer algebra systems, but which we have been able to complete with
components of the Oscar computer algebra system we are implementing.

The problem came up in some research Daniel Schultz and I have been doing, to do with
computing a new kind of modular equation. The theoretical details are not so important
for the purposes of this blog, so I'll only give a quick overview of where the problem
came from.

The Dedekind eta function is given by the following infinite q-series product
$$\eta(q) = q^{1/24}\prod_{n=1}^\infty (1 - q^n),$$
in the "nome" $q^{1/24}$. Naturally, we can only work with a finite precision
approximation out to $O(q^N)$ for some precision $N$, on a computer.

Here, $q = exp(2\pi i\tau)$ for $\tau$ in the complex upper half plane $\mathbb{H}$. This
makes $\eta$ a function of $\tau$ in the upper half plane. In fact, $\eta(\tau)$ is a
modular form of weight $1/2$, if you know about such things.

We have been investigating identities for certain functions that are defined in terms of
the Dedekind eta function, that hold for all $\tau \in \mathbb{H}$.

We start with a generalisation of the Weber modular function
$$\mathfrak{f}_2(\tau) = \sqrt{2}\frac{\eta(2\tau)}{\eta(\tau)}.$$

In particular, we start with
$$\mathfrak{m}_{n, \infty} = \sqrt{n}\frac{\eta(n\tau)}{\eta(\tau)},$$
where $n = 2$ is obviously the classical Weber case.
For any $m \in \mathbb{N}$ we define
$$x_{n, m}(\tau) = \frac{\mathfrak{m}_{n,\infty}(mn\tau)}{\mathfrak{m}_{n,\infty}(\tau)}, \;\; y_{n,m}(\tau) = \frac{\mathfrak{m}_{n,\infty}(n\tau)}{\mathfrak{m}_{n,\infty}(m\tau)}.$$

We have been computing the minimum polynomial relation
$P_{n,m}(x_{n,m}(\tau), y_{n,m}(\tau)) = 0$
that holds as an identity for all $\tau \in \mathbb{H}$. The bivariate polynomial
$P_{n,m}$ has coefficients in $\mathbb{Z}$.

We call such a relation $P_{n,m}(x, y) = 0$ a modular equation of degree $m$ for level
$n$ functions, though terminology varies wildly here, and these certainly don't relate
directly to the modular equations of Schlaefli, Weber, Jacobi, Russel, etc.

As an example, the minimum relation for $n = 2$ (corresponding to the original Weber
modular function) and $m = 3$ is given by
$$P_{2, 3}(x, y) = x^5y + xy^5 - 1 = 0,$$
for all $\tau \in \mathbb{H}$.

## Computing the modular equations

There are various numerical ways to compute such equations, e.g. numerically compute
the value of the eta function at various random values of $\tau$ in the upper half
plane and try to find the relation between values of our functions using LLL.

This is not an efficient approach, and it also requires a lot of work to decide on a
provable bound on numerical precision.

There are various algebraic approaches, one of which forms the basis of the paper we are
working on. In particular, we can give what we believe to be sharp bounds on the degrees
of $x$ and $y$ in our relations $P_{n, m}(x, y) = 0$.

We can currently only prove our bounds are sharp in some cases, but experimentally they
seem to always be sharp.

For any given values of $m$ and $n$, we can do a computation to check they are sharp.
This computation boils down to finding the nullspace of a certain matrix over
$\mathbb{Q}$ and checking that its nullity is 1. If it is, the bounds are sharp.

If the nullity is $1$, then we can prove that the generator of the nullspace gives
the coefficients of the minimal polynomial $P_{n, m}(x, y) \in \mathbb{Z}[x, y]$ that
appears in our modular equation.

## The interesting computational challenge

The interesting challenge is not in computing the rank of the matrix (this can be done
modulo a random prime, which allows us to bound the nullity above). The real challenge
is in computing the entries of the matrix itself.

As an example of this challenge, we explicitly describe this matrix for the case $n = 11$
and $m = 4$. The resulting matrix is 9001x4500 over $\mathbb{Q}$.

First we define the functions
$$s(q) = x(q)/y(q),\;\; t(q) = x(q)^{12}.$$

We then compute these out to $O(q^{9001})$. Although the q-series of $s(q)$ and $t(q)$
are in the nome $q$, they are defined in terms of functions in the nome $q^{1/24}$. This
means that naively the Puiseux series will be using an internal precision of
$24\times 9001 = 216024$. In fact, all of the systems we discuss in this blog work to
this precision initially.

Once we have computed $s(q)$ and $t(q)$ to this precision, we compute the q-series of
$s^it^j$ for $i \in [0, 300]$ and $j \in [0, 15]$.

The entries in each column of our matrix are the q-series coefficients of one of the
$s^it^j$.

Thus, there are $300\times 15 = 4500$ columns and $9001$ rows in the matrix, since the
q-series must be computed out to $O(q^{9001})$.

This gives us the matrix for $n = 11$ and $m = 4$ which conjecturally has nullity 1.

## Computing the q-series in Oscar

First we should write out how the computation can be done in Oscar (note that the $\sqrt{11}$ cancels in the functions we are using and can be omitted).

As we will be working with Puiseux series in $q^{1/24}$ we will need to work with
$9001\times 24$ terms in order to compute everything out to $O(q^{9001})$.

Here is the code required to compute the functions $s$ and $t$.

```julia
using Nemo

R, q = PuiseuxSeriesRing(ZZ, 9001*24, "q")

m(q) = divexact(eta_qexp(q^11), eta_qexp(q))

x(q) = divexact(m(q^44), m(q))
y(q) = divexact(m(q^11), m(q^4))

s(q) = divexact(x(q), y(q))
t(q) = x(q)^12
```

This does not take any appreciable time, as nothing is actually computed.

The next step is to populate an array with the q-series expressions for $s(q)^i$ for
$i \in [0, 300]$ and $t(q)^j$ for $j \in [0, 15]$ so that these powers are not recomputed
over and over again. We do this efficiently with one multiplication for each entry.

```julia
T1 = typeof(q)
S = Array{T1, 1}(301)
T = Array{T1, 1}(16)

sq = s(q);
tq = t(q);

S[1] = sq^0
T[1] = tq^0

for i = 2:301
   S[i] = S[i - 1]*sq
end

for i = 2:16
   T[i] = T[i - 1]*tq
end
```

This takes about 38s.

The final step is to compute all the $s^it^j$ for $i$ and $j$ in the required ranges
and populate the matrix. To keep things simple, we just compute all the products and
don't bother computing the matrix.

```julia
for i = 0:300
   for j = 0:15
      p = S[i + 1]*T[j + 1]
   end
end
```

This by far consumes the largest part of the total runtime in Oscar, at 605s.

## Computation in Mathematica

The systems we decided to use for this blog are SageMath, Mathematica, Magma and Oscar.

Although we expected this to be a simple task, we encountered issues straight away.

We had some existing Mathematica code that we had been using in webMathematica, so it
was only necessary to alter the code.

Unfortunately, due to a recent update in webMathematica, there is a parser error that
caused newlines to be interpreted as products in some cases, meaning our code broke.
Therefore it was not possible to use Mathematica until they fixed this issue.

However, we do know that once bignums are encountered in power series, Mathematica
switches to a generic representation, and things get really slow. We found that the
computation was not really practical in Mathematica when the code was working.

## Computation of the q-series in SageMath

The first issue we encountered in SageMath is that we were unable to figure out how to
do Puiseux series. SageMath has power series and Laurent series, but raising to
fractional powers doesn't seem to be available.

In this specific case, just because we are using eta quotients, it is possible to work
out how to write the series in terms of Laurent series instead. This isn't always
convenient, but it works in our case after some minutes with a pen and paper.

But then we encounter our next issue. The `qexp_eta` function in Sage does not seem
to work with Laurent series. It seems to require a power series ring. The solution to
this issue is obvious.

Also, the `qexp_eta` function does not take a "nome" as input, but rather a ring in
which you want to compute the expansion of the eta product, minus the leading $q^{1/24}$.

This is fine if you actually want to compute $\eta(q)$, but not if you want to compute
$\eta(q^n)$ for example, as we do.

The solution seems to be to substitute $q^n$ for $q$ in the output of `qexp_eta`.

In order to mimic what we had done in Oscar, we wrote a function $etaq(q)$ which accepts
a nome in a power series ring, and substitutes it into the q-series expansion of eta
from SageMath's `eta_qexp` function.

It might seem like we are done, since we can now write all the other functions we need
in terms of this function.

But now we encounter another issue. Trying to evaluate our functions at the nome q
results in a very slow runtime. This is probably because we are no longer working with
the correct precision, as we used subst which does not truncate things to the precision
of the power series ring we are working over.

At this point we are just writing a custom q-series module and it is hard to know how we
can get an apples for apples comparison.

If we persist long enough, we can get timings comparable with Oscar, but it just didn't
seem to be in the spirit of the task to implement things this way. Of course, a Sage
expert might be able to more easily do the computation, without losing performance.

## Computation of the q-series in Magma

Magma supports Puiseux series. As with Oscar, it requires one to specify the internal
Laurent series precision, depending on the fractional power of q you are using. For
example, to compute to $O(q^n)$ with Puiseux series in $q^{1/24}$ requires a Puiseux
series precision of at least $24n$.

The DedekindEta function computes the Puiseux expansion of the Dedekind eta function in
Magma. But it immediately complains that the rationals are not contained in the
coefficient ring of the argument. So we must work with PuiseuxSeries over the rationals.

After this, it's easy to define the functions we require in Magma.

As in Oscar, this takes negligible time, as nothing is actually computed.

At the next step we try to compute arrays of powers of $s(q)$ and $t(q)$. This takes
approximately 85s.

One has to be very careful to precompute $s(q)$ and $t(q)$, however, as this takes 10s
each time each of those are computed. Without being careful about this, Magma could take
over an hour to compute all the powers. The Oscar times barely change if we don't
precompute these q-series.

Finally we compute the products of the powers of $s$ and $t$. This takes about 829s.

## Summary

Here is a table summarising the results.

n = 11, m = 4 | SageMath | Mathematica | Magma | Oscar
--------------|----------|-------------|-------|-------
Puiseux       | ??       | ??          | 914s  | 643s 

I'm not sure what we learn from this, other than that benchmarking complex calculations
can be somewhat of a deep hole at times. It's not at all clear how we could fairly
compare all the systems.

We feel that the comparison with Magma is not unfair. But it's not clear how much work
it is fair for us to do in order to include the other systems.

Quite obviously, in this case, we could simply write out q-series expressions and then
perform substitutions at each step and then truncate to a given precision. However, this
is error prone and kind of defeats the purpose of what we are trying to do.

We should point out that we believe Magma has very fast nullspace code (very likely
much faster than our own). So perhaps that would make a more reasonable benchmark for
our next blog.

## Why are Oscar q-series fast

Assuming that we accept that Oscar has relatively fast Puiseux series, we should say a
few words about why that is.

In Oscar, we store Puiseux series internally as Laurent series along with a common
denominator for the exponents.

The Puiseux series precision is automatically computed in each operation. When
combining q-series in different nomes, the two expressions are first brought to
expressions in the same nome.

Laurent series themselves are also stored with a valuation, precision and a scale factor.
Thus regularly spaced q-series such as $q + q^4 + q^7 + O(q^8)$ would be stored with a
scale factor of 3. This radically reduces the space required to store them, and
dramatically speeds up computations.

This scale factor can be used regardless of the valuation or precision, though this does
make computation quite complex internally, as for example, two Laurent series with a
scale factor of 3 may not sum to a Laurent series with a scale factor of 3, etc.

Finally, Oscar makes use of fast power series arithmetic over $\mathbb{Z}$, implemented
in Flint.

## An example modular equation

The modular equation for $n = 11$, $m = 4$ is really too huge to reproduce here (and in
fact, we have not bothered computing it). We were only interested in checking whether
our bounds on the degrees are tight, in this blog.

In terms of the functions $x_{n,m}$ and $y_{n,m}$ described above, the modular equation
for $n = 5$ and $m = 8$ is

$$\begin{multline}x^{17}y - 4x^{16}y^2 + 10x^{15}y^3 + x^{15}y - 20x^{14}y^4 + 6x^{14}y^2 +\\
        35x^{13}y^5 - 35x^{13}y^3 + 2x^{13}y - 52x^{12}y^6 + 61x^{12}y^4 +\\
        13x^{12}y^2 + 68x^{11}y^7 - 59x^{11}y^5 - 39x^{11}y^3 + 3x^{11}y -\\
        80x^{10}y^8 + 42x^{10}y^6 + 2x^{10}y^4 - 12x^{10}y^2 + 85x^9y^9 -\\
        33x^9y^7 + 67x^9y^5 + 40x^9y^3 + 5x^9y - 80x^8y^{10} +\\
        30x^8y^8 - 52x^8y^6 - 58x^8y^4 - 10x^8y^2 + 68x^7y^{11} -\\
        33x^7y^9 + 16x^7y^7 - 9x^7y^5 - 8x^7y^3 - 7x^7y - 52x^6y^{12} +\\
        42x^6y^{10} - 52x^6y^8 + 78x^6y^6 + 37x^6y^4 + 10x^6y^2 +\\
        35x^5y^{13} - 59x^5y^{11} + 67x^5y^9 - 9x^5y^7 - 49x^5y^5 +\\
        12x^5y^3 - x^5y - 20x^4y^{14} + 61x^4y^{12} + 2x^4y^{10} - 58x^4y^8 +\\
        37x^4y^6 - 36x^4y^4 - 2x^4y^2 - x^4 + 10x^3y^{15} - 35x^3y^{13} -\\
        39x^3y^{11} + 40x^3y^9 - 8x^3y^7 + 12x^3y^5 + 5x^3y^3 - x^3y -\\
        4x^2y^{16} + 6x^2y^{14} + 13x^2y^{12} - 12x^2y^{10} - 10x^2y^8 +\\
        10x^2y^6 - 2x^2y^4 + 6x^2y^2 + xy^{17} + xy^{15} + 2xy^{13} +\\
        3xy^{11} + 5xy^9 - 7xy^7 - xy^5 - xy^3 + xy - y^4 = 0\end{multline}$$

Verifying this as a q-series identity in Oscar takes 13s whereas it takes around 75s in
Magma (assuming we precompute the q-series expansions of x and y).


