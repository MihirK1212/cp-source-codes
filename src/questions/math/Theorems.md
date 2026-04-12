# Mathematical Theorems

## Overview

This document outlines some important mathematical theorems and concepts frequently encountered in competitive programming and discrete mathematics.

## 1. GCD and LCM Relationship

The Greatest Common Divisor (GCD) of two numbers multiplied by their Least Common Multiple (LCM) is equal to the product of the two numbers:

```
gcd(a, b) * lcm(a, b) = a * b
```

## 2. Property of GCD

If `gcd(a, b) = d`, then `gcd(a/d, b/d) = 1`. This means that `a/d` and `b/d` are coprime (their greatest common divisor is 1).

## 3. Bézout's Identity and Linear Diophantine Equations

Bézout's identity states that if `d = gcd(a, b)`, then there always exist integers `x` and `y` such that `ax + by = d`. This is the smallest positive integer `k` for which `ax + by = k` has an integer solution.

*   **One Solution**:
    If `c % d == 0`, one particular solution `(x0, y0)` for `ax + by = c` can be found using the extended Euclidean algorithm where `x0 = U * (c/d)` and `y0 = V * (c/d)` (from `aU + bV = d`).
*   **All Solutions**:
    All integer solutions are of the form `(x0 - k*(b/d) , y0 + k*(a/d))` for any integer `k`.

## 4. Integer Factorization - Sieve of Eratosthenes

The Sieve of Eratosthenes is a common algorithm for finding all prime numbers up to a specified integer. For integer factorization, it is often sufficient to scan primes up to `sqrt(N)` when factorizing `N`.

To factorize all numbers from 1 to N, for every integer `k`, you can maintain its smallest prime factor and its highest power. The remaining factors of `k` are then found by recursively factorizing `k / (p^a)`.

## 5. Modulo Property

For any two integers `x` and `y` where `y > 0`, the remainder of `x` divided by `y`, denoted as `x % y`, will always satisfy:

```
x % y < y
```

This property is fundamental to modular arithmetic.

## 6. Modular Multiplicative Inverse (Fermat's Little Theorem)

If `m` is a prime number, then the modular multiplicative inverse of `y` modulo `m` is `(y^(m-2)) % m`:

```
(y^(-1))modm = (y^(m-2))modm
```