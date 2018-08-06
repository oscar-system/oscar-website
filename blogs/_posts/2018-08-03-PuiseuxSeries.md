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
in the "nome" $q$. Naturally, we can only work with a finite precision
approximation out to $O(q^N)$ for some precision $N$, on a computer.

Here, $q = exp(2\pi i\tau)$ for $\tau$ in the complex upper half plane $\mathbb{H}$. This
makes $\eta$ a function of $\tau$ in the upper half plane. In fact, $\eta(\tau)$ is a
modular form of weight $1/2$, if you know about such things.

We have been investigating identities for certain functions that are defined in terms of
the Dedekind eta function, that hold for all $\tau \in \mathbb{H}$.

One of the classical Weber modular functions is
$$\mathfrak{f}_2(\tau) = \sqrt{2}\frac{\eta(2\tau)}{\eta(\tau)}.$$

In this blog we work with a generalisation of this, defined by
$$\mathfrak{m}_{n, \infty}(\tau) = \sqrt{n}\frac{\eta(n\tau)}{\eta(\tau)}.$$
Obviously $n = 2$ is the classical Weber function $\mathfrak{f}_2(\tau)$.

For any $m \in \mathbb{N}$ we define
$$x_{n, m}(\tau) = \frac{\mathfrak{m}_{n,\infty}(mn\tau)}{\mathfrak{m}_{n,\infty}(\tau)}, \;\; y_{n,m}(\tau) = \frac{\mathfrak{m}_{n,\infty}(n\tau)}{\mathfrak{m}_{n,\infty}(m\tau)}.$$

We have been computing the minimum polynomial relation
$P_{n,m}(x_{n,m}(\tau), y_{n,m}(\tau)) = 0$
that holds as an identity for all $\tau \in \mathbb{H}$. The bivariate polynomial
$P_{n,m}(X, Y)$ has coefficients in $\mathbb{Z}$.

We call such a relation $P_{n,m}(x, y) = 0$ a modular equation of degree $m$ for level
$n$ functions, though terminology varies wildly here, and these certainly don't relate
directly to the modular equations of Schlaefli, Weber, Jacobi, Russel, Ramanujan, etc.

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
the coefficients of the minimal polynomial $P_{n, m}(X, Y) \in \mathbb{Z}[X, Y]$ that
appears in our modular equation.

## The interesting computational challenge

The interesting challenge is not in computing the rank of the matrix (this can be done
modulo a random prime, which allows us to bound the nullity above). The real challenge
is in computing the entries of the matrix itself.

As an example of this challenge, we explicitly describe this matrix for the case $n = 11$
and $m = 4$. The resulting matrix is 9001x4816 over $\mathbb{Q}$.

First we define the functions
$$s(q) = x(q)/y(q),\;\; t(q) = x(q)^{12}.$$

We then compute these out to $O(q^{9001})$. Although the q-series of $s(q)$ and $t(q)$
are in the nome $q$, they are defined in terms of functions in $q^{1/24}$. This
means that naively the Puiseux series will be using an internal precision of
$24\times 9001 = 216024$. In fact, all of the systems that we discuss in this blog, with
true Puiseux series implementations, have to work to this precision initially.

Once we have computed $s(q)$ and $t(q)$ to this precision, we compute the q-series of
$s^it^j$ for $i \in [0, 300]$ and $j \in [0, 15]$.

The entries in each column of our matrix are the q-series coefficients of one of the
$s^it^j$.

Thus, there are $301\times 16 = 4816$ columns and $9001$ rows in the matrix, since the
q-series must be computed out to $O(q^{9001})$.

This gives us the matrix for $n = 11$ and $m = 4$ which conjecturally has nullity 1.

## Computation of the q-series in Oscar

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

## Computation of the q-series in Mathematica

The systems we decided to use for this blog are SageMath, Mathematica, Magma and Oscar.

Although we expected this to be a simple task, we encountered issues straight away.

We had some existing Mathematica code that we had been using in webMathematica, so it
was only necessary to alter the code.

Unfortunately, due to a recent update in webMathematica, there is a parser error that
causes newlines to be interpreted as products in some cases, meaning our code no longer
works. Therefore it is not possible to use webMathematica until they fix this issue.

However, we do know that once bignums are encountered in power series, Mathematica
switches to a generic representation, and things get really slow. We found that the
computation was not really practical in Mathematica when the code was working.

In the end, we were able to write something that worked in desktop Mathematica.

Here are the basic definitions.

```
\[Eta][q_] := q^(1/24)*QPochhammer[q,q];
f[q_] := \[Eta][q^11]/\[Eta][q];
x[q_] := f[q^44]/f[q];
y[q_] := f[q^11]/f[q^4];
s[q_] := x[q]/y[q];
t[q_] := x[q]^12;
```

Computing s and t to precision O(q^9001) takes about 4 minutes. The `PowerExpand` is
necessary to enforce the rule `(q^a)^(1/24) = q^(a/24)`, which is true in this case.
This results in power series data types using only integral exponents.

```
Timing[
    sq=Series[PowerExpand[s[q]],{q,0,9000}];
    tq=Series[PowerExpand[t[q]],{q,0,9000}];
][[1]]

243
```

The timing here is in seconds.

We next need to fill in powers of s and t, which the following code does in 3.5 hours.

```
Timing[
    sp[0] = 1 + O[q]^9001;
    Do[sp[i] = sp[i-1]*sq, {i,1,300}];
    tp[0] = 1 + O[q]^9001;
    Do[tp[i] = tp[i-1]*tq, {i,1,15}];
][[1]]

12306
```
The following code should then take at least 16 times as long as the code above, which
puts a conservative estimate on the total time to fill in the matrix to be more than
two days.

```
Timing[Do[sp[i]*tp[j],{i,0,300},{j,0,15}]][[1]]
```

## Computation of the q-series in SageMath

The first issue we encountered in SageMath is that we were unable to figure out how to
do Puiseux series. SageMath has power series and Laurent series, but raising to
fractional powers doesn't seem to be available.

In this specific case, just because we are using eta quotients, it is possible to work
out how to write the series in terms of Laurent series instead. This isn't always
convenient, but it works in our case after some minutes with a pen and paper (at least,
the third time we checked our arithmetic, it worked).

But then we encounter our next issue. The `qexp_eta` function in SageMath does not seem
to work with Laurent series. It seems to require a power series ring. Of course, we can
also work with power series, and if not, Sage can coerce to Laurent series, so this is
just a minor annoyance.

The next issue is that the `qexp_eta` function does not take a "nome" as input, but
rather a ring in which you want to compute the expansion of the eta product, minus the
leading $q^{1/24}$.

This is fine if you actually want to compute $\eta(q)$, but not if you want to compute
$\eta(q^n)$ for example, as we do.

Trying to solve this leads to another problem that is subtle and that I was only able to
detect because I have implemented numerous power series modules myself.

Naively, what seems logical is that we ought to substitute $q^n$ for $q$ in the output of
`qexp_eta` to get $\eta(q^n)$. One can perform such substitutions in SageMath using
either the `subs` function, or by functional evaluation of the $q$-series at $q^n$, i.e.
by typing $f(q^n)$, where $f$ is the power series in question.

However, SageMath has a notion of exact power series, i.e. power series given to infinite
precision. The expression $q^n$ is such an exact power series in Sage. Therefore,
substituting it into the expression from `eta_qexp` results in an expression with about
$n$ times the precision. Because of the dense representation in Sage, this would kill
performance.

Of course we can replace $q$ with $q + O(q^{9002})$ to emulate not working with infinite
precision power series. However, this still isn't sufficient.

Both Magma and Oscar do not interpret eta$(q^n)$ as substituting $(q + O(q^{9002}))^n$
into the $q$-series for eta. They interpret it to mean that we want the $q$-series
expansion of eta in a ring with relative precision $9001$. This is subtly different,
though it takes a little thought to see why.

The precision that the user supplies when creating a power series ring in Sage is not
applied as a precision cap (after all, one can have infinite precision power series in
such a ring). It's only used as a default precision for things that cannot be computed
to infinite precision, and where no precision is implied by the computation, such as
$1/(1 + q)$.

Because of this completely different model of power series, it's going to be hard to get
an apples for apples comparison with Sage.

As a first approximation, we can simply replace $q$ with $q + O(q^{9002})$ in the Sage
computations. But this will result in Sage working to higher precision than the other
systems.

We can truncate the power series to $q^{9001}$. This is technically equivalent to using
an absolute cap, whereas we really want a relative precision cap, so this advantages
Sage somewhat.

We question whether we are just implementing a power series module on top of Sage, at
this point.

First we implement the functions we require.

```
R.<q> = PowerSeriesRing(ZZ, default_prec=9001)

def m(q):
    return qexp_eta(R, 9001)((q + O(q^9002))^11)/qexp_eta(R, 9001)(q + O(q^9002))

def x(q):
    return m((q + O(q^9002))^44)/m(q + O(q^9002))

def y(q):
    return m((q + O(q^9002))^11)/m((q + O(q^9002))^4)

def s(q):
    return (q + O(q^9002))^15*x(q+O(q^9002))/y(q+O(q^9002))

def t(q):
    return (q + O(q^9002))^215*x(q+O(q^9002))^12
```

As usual, this takes no time as nothing is actually computed.

Next we compute the arrays of powers of $s$ and $t$. To ensure Sage is not disadvantaged,
we truncate $s(q)$ and $t(q)$ to the same precision as it is computed in Oscar.

```
sq = s(q) + O(q^9016);
tq = t(q) + O(q^9216);

S = [sq^0]
T = [tq^0]

for i in range(1, 301):
    S.append(S[i - 1]*sq)

for i in range(1, 16):
    T.append(T[i - 1]*tq)
```

This takes around 190s.

Finally, we compute the products of the powers.

```
for i in range(0, 301):
    for j in range(0, 16):
        p = S[i]*T[j]
```

This takes around 1650s.

## Computation of the q-series in Magma

Magma supports Puiseux series. As with Oscar, it requires one to specify the internal
Laurent series precision, depending on the fractional power of q you are using. For
example, to compute to $O(q^n)$ with Puiseux series in $q^{1/24}$ requires a Magma
`PuiseuxSeriesRing` precision of at least $24n$.

The `DedekindEta` function computes the Puiseux expansion of the Dedekind eta function in
Magma. But it immediately complains that the rationals are not contained in the
coefficient ring of the argument. So we must work with Puiseux series over the rationals.

After this, it's easy to define the functions we require in Magma.

```
R<q> := PuiseuxSeriesRing(Rationals(), 9001*24);

function m(q)
   return DedekindEta(q^11)/DedekindEta(q);
end function;

function x(q)
   return m(q^44)/m(q);
end function;

function y(q)
   return m(q^11)/m(q^4);
end function;

function s(q)
   return x(q)/y(q);
end function;

function t(q)
   return x(q)^12;
end function;
```

As in Oscar, this takes negligible time, as nothing is actually computed.

At the next step we try to compute arrays of powers of $s(q)$ and $t(q)$. In order to
ensure Magma is not at a disadvantage we truncate $s(q)$ and $t(q)$ to the same
precision as it is computed in Oscar, though this makes little difference.

```
sq := s(q) + O(q^9016);
tq := t(q) + O(q^9216);

S := [sq^0];

for i := 1 to 300 do
   S := Append(S, S[i]*sq);

end for;

T := [tq^0];
for i := 1 to 15 do
   T := Append(T, T[i]*tq);
end for;
```

This takes approximately 104s.

One has to be very careful to precompute $s(q)$ and $t(q)$. Otherwise this takes 10s
each time each of these are computed. Without being careful about this, Magma could take
over an hour to compute all the powers. In comparison, the total Oscar time does not
change radically if we don't precompute these q-series.

Finally we compute the products of the powers of $s$ and $t$.

```
for i := 1 to 301 do
   for j := 1 to 16 do
      p := S[i]*T[j];
   end for;
end for;
```

This takes about 2488s.

## Summary

Here is a table summarising the results. We give the times to compute the arrays of
powers of $s(q)$ and $t(q)$ separately, since these show a different aspect of the
performance comparison than the total times for the whole benchmark

n = 11, m = 4 | SageMath | Mathematica | Magma | Oscar
--------------|----------|-------------|-------|-------
Setup         | 190s     | ~ 3.5 hours | 104s  | 38s
Total         | 1840s    | ~ 2 days    | 2592s | 643s 

I'm not sure what we learn from this, other than that benchmarking complex calculations
can be somewhat of a deep hole at times. Artificially truncating series and doing
additional precomputation to keep times in check doesn't seem like it reflects what a
user would do.

We should point out that we have heard that Magma has very fast nullspace code (very
likely much faster than our own). So perhaps that would make a more reasonable benchmark 
for a future blog.

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
our bounds on the degrees are tight, for this benchmark.

To finish this blog, we give an example of an actual modular equation that we have
computed using our methods.

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

Verifying this as a q-series identity to high precision in Oscar takes 13s whereas it
takes around 75s to the same precision in Magma (assuming we precompute the q-series
expansions of x and y).


