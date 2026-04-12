# Sieve of Eratosthenes (Optimized to Root N)

## Problem Description

The **Sieve of Eratosthenes** is an ancient algorithm for finding all prime numbers up to a specified integer `n`. It is one of the most efficient ways to find all primes up to a moderately large limit.

**Algorithm Idea:**

The basic idea is to iteratively mark (sieve) the multiples of each prime number as composite. The numbers that remain unmarked at the end are prime.

**Optimization (Up to Root N):**

The standard Sieve of Eratosthenes can be optimized by iterating the outer loop (`for i = 2; i*i <= n; i++`). This is because if a number `j` is composite, it must have at least one prime factor less than or equal to `sqrt(j)`. When `i*i` is used as the starting point for marking multiples (`for j = i*i; j <= n; j += i`), we avoid re-marking multiples that have already been marked by smaller prime factors (e.g., multiples of 4 are already marked by 2).

## C++ Solution

The C++ solution implements the optimized Sieve of Eratosthenes:

1.  **Initialization:**
    *   Read the upper limit `n`.
    *   Create a boolean vector `is_prime` of size `n+1`, initialized to `true` (assuming all numbers are prime initially).
    *   Mark `is_prime[0]` and `is_prime[1]` as `false`, since 0 and 1 are not prime numbers.
2.  **Sieving Process:**
    *   Iterate `i` from `2` up to `sqrt(n)` (i.e., `i*i <= n`).
    *   If `is_prime[i]` is `true` (meaning `i` is a prime number):
        *   Iterate `j` from `i*i` up to `n`, incrementing by `i` (`j += i`).
        *   For each such `j`, set `is_prime[j] = false` (mark it as composite, as it's a multiple of `i`).
3.  **Print Primes:** Iterate from `i = 1` to `n`. If `is_prime[i]` is `true`, print `i`.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // For std::vector
#include <cmath>     // For std::sqrt (though i*i <= n avoids explicit sqrt)

// using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

int main()
{
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);

    long long n; // Upper limit to find primes up to
    std::cin >> n;

    // Create a boolean vector, where is_prime[i] is true if i is prime, false otherwise.
    // Initialize all to true, then mark composites.
    std::vector<bool> is_prime(n + 1, true);

    // 0 and 1 are not prime numbers.
    if (n >= 0) is_prime[0] = false;
    if (n >= 1) is_prime[1] = false;

    // Sieve process: iterate from 2 up to sqrt(n)
    for(long long i = 2; i * i <= n; i++)
    {
        // If i is prime (not marked as composite yet)
        if(is_prime[i])
        {
            // Mark all multiples of i as composite, starting from i*i.
            // Multiples less than i*i (e.g., 2*i, 3*i) would have already been marked
            // by smaller prime factors (e.g., 2, 3).
            for(long long j = i * i; j <= n; j += i)
            {
                is_prime[j] = false;
            }
        }
    }
    
    // Print all prime numbers found up to n.
    std::cout << "Prime numbers up to " << n << ":\n";
    for(long long i = 2; i <= n; i++) // Start from 2, as 0 and 1 are handled
    {
        if(is_prime[i]){ std::cout << i << " "; }
    }
    
    std::cout << "\n";
    return 0;
}
```