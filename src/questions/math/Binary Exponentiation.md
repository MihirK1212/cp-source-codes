# Binary Exponentiation (Power Function)

## Problem Description

This code implements **binary exponentiation**, also known as **exponentiation by squaring**, to efficiently calculate `a` raised to the power of `n` (`a^n`). This algorithm significantly reduces the number of multiplications required compared to a naive approach, achieving a time complexity of `O(log n)`.

## C++ Solution

This C++ solution implements the binary exponentiation algorithm recursively.

**`power(long long a, long long n)` function:**

*   **Parameters:**
    *   `a`: The base number.
    *   `n`: The exponent (non-negative integer).
*   **Return Value:** `a^n`.
*   **Base Case:**
    *   If `n == 0`, then `a^0` is `1`. Return `1`.
*   **Recursive Step:**
    1.  Recursively calculate `half = power(a, n / 2)`. This computes `a^(n/2)`.
    2.  **If `n` is even:**
        *   `a^n = a^(n/2) * a^(n/2) = half * half`.
        *   Return `half * half`.
    3.  **If `n` is odd:**
        *   `a^n = a^(n/2) * a^(n/2) * a = half * half * a`.
        *   Return `half * half * a`.

**`main()` function:**

*   Reads the base `a` and exponent `n` from input.
*   Calls the `power` function and prints the result.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Not explicitly used but good for standard practices
#include <algorithm> // Not explicitly used but good for standard practices

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Function to calculate a^n using binary exponentiation (recursive approach)
long long power(long long a, long long n)
{
    // Base case: a^0 = 1
    if(n == 0){
        return 1;
    }
    
    // Calculate a^(n/2) recursively
    long long half_power = power(a, n / 2);

    // If n is even, a^n = (a^(n/2)) * (a^(n/2))
    if(n % 2 == 0){
        return half_power * half_power;
    }
    else // If n is odd, a^n = (a^(n/2)) * (a^(n/2)) * a
    {
        return half_power * half_power * a;
    }
}

int main()
{
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    long long base, exponent; 
    std::cin >> base >> exponent; // Read base 'a' and exponent 'n'

    std::cout << power(base, exponent) << "\n"; // Output a^n
    
    return 0;
}
```