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
$$\mathfrak{f}(\tau) = \sqrt{2}\frac{\eta(2\tau)}{\eta(\tau)}.$$

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

If the nullity is $1$, then it is a theorem that the generator of the nullspace gives
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

This gives us the matrix for $n = 11$ and $m = 4$ which is conjecturally nullity 1.

## Timings for various computer algebra systems

Although we are not able to compute the given matrix using other systems, we decided to
do some timings to give an estimate on how long it would actually take.

This means working out the asymptotics of the q-series arithmetic in those systems,
timing some q-series operations and extrapolating, and then multiplying by the total
number of multiplications to the given precision, that would need to be computed
(namely ~4500).

The following table gives our estimates for the various systems we tried this with along
with an actual timing for Oscar (which makes use of Nemo.jl).

n = 11, m = 4 | SageMath | Mathematica | Magma | Oscar
--------------|----------|-------------|-------|-------
Puiseux       | ??       |             |       | 630s 
Laurent       |          |             |       | 630s

Initially we intended to give timings only for Puiseux series. However, it's not clear
if Sage supports Puiseux series directly like the other systems.

With some additional work, as we are working with eta quotients in this case, one may
work directly with Laurent series in $q$ instead of Puiseux series in $q^{1/24}$. This
is not always convenient, but it does work for this example. (Note that simply replacing
$q^{1/24}$ with $q$ throughout will also work, at the expense of possibly radically
increasing the sparsity and of course a corresponding increase in precision.)

To keep things fair between the systems, we also give timings for the other systems in
terms of Laurent series as well. However, the main timings I'm interested in for this
blog are the Puiseux series timings, which are not available for Sage.



