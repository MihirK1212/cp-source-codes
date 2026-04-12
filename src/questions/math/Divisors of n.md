# Divisors of N (Efficiently finding divisors)

## Problem Description

Given a positive integer `n` and an upper limit `m`, the task is to find all positive divisors of `n` that are less than or equal to `m`. This is a common operation in number theory problems, especially when factorization or divisibility checks are required.

## C++ Solution

This C++ solution efficiently finds all divisors of a given number `n` up to a certain limit `m`. It leverages the property that divisors of a number `n` always appear in pairs `(i, n/i)`, where one of the divisors `i` is less than or equal to `sqrt(n)`, and the other `n/i` is greater than or equal to `sqrt(n)`.

**`divisors(ll n, ll m)` function:**

*   **Parameters:**
    *   `n`: The number for which divisors are to be found.
    *   `m`: The upper limit for the divisors to be included in the result.
*   **Return Value:** A `vll` (vector of long longs) containing all divisors of `n` that are less than or equal to `m`.
*   **Logic:**
    1.  Initialize an empty `vll res` to store the resulting divisors.
    2.  Iterate `i` from `1` up to `sqrt(n)`:
        *   **Check for Divisibility:** If `n % i == 0`, then `i` is a divisor of `n`.
        *   **Add `i`:** If `i <= m`, add `i` to `res`.
        *   **Add `n/i` (the pair divisor):**
            *   The other divisor in the pair is `n/i`.
            *   If `(n/i)` is not equal to `i` (to avoid adding the same divisor twice when `n` is a perfect square) AND `(n/i) <= m`, then add `n/i` to `res`.
*   Return `res`.

```cpp
#include <vector>    // Required for std::vector
#include <cmath>     // Required for std::sqrt
#include <algorithm> // Required for std::sort (if sorted output is desired)

typedef long long ll;
typedef std::vector<long long> vll;

// Function to find all positive divisors of 'n' that are less than or equal to 'm'.
vll divisors(ll n, ll m)
{
    vll res; // Vector to store the divisors

    // Iterate from 1 up to the square root of n
    for (ll i = 1; i * i <= n; i++) // Using i*i <= n instead of i <= sqrt(n) to avoid floating point issues
    {
        if (n % i == 0) // If i divides n, then i is a divisor
        {
            // Check and add i
            if(i <= m){
                res.push_back(i);
            }
            
            // Check and add n/i (the pair divisor)
            // Ensure n/i is not the same as i (for perfect squares) and is within the limit m
            if((n / i) != i && (n / i) <= m){
                res.push_back(n / i);
            }
        }
    }
    
    // If a sorted list of divisors is desired, uncomment the following line:
    // std::sort(res.begin(), res.end());

    return res; // Return the vector of divisors
}

// Example usage in main (not part of the Solution class, but for demonstration)
#include <iostream>

int main() {
    ll n_val = 36;
    ll m_limit = 10;
    vll result_divisors = divisors(n_val, m_limit);

    std::cout << "Divisors of " << n_val << " less than or equal to " << m_limit << ":\n";
    for (ll d : result_divisors) {
        std::cout << d << " ";
    }
    std::cout << "\n";

    n_val = 100;
    m_limit = 20;
    result_divisors = divisors(n_val, m_limit);
    std::cout << "Divisors of " << n_val << " less than or equal to " << m_limit << ":\n";
    for (ll d : result_divisors) {
        std::cout << d << " ";
    }
    std::cout << "\n";

    n_val = 7;
    m_limit = 10;
    result_divisors = divisors(n_val, m_limit);
    std::cout << "Divisors of " << n_val << " less than or equal to " << m_limit << ":\n";
    for (ll d : result_divisors) {
        std::cout << d << " ";
    }
    std::cout << "\n";

    return 0;
}
```