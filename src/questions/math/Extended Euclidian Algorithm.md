# Extended Euclidean Algorithm

## Problem Description

The **Extended Euclidean Algorithm** is an extension of the standard Euclidean algorithm. It computes not only the greatest common divisor (GCD) `g` of two integers `a` and `b`, but also finds integer coefficients `x` and `y` such that `ax + by = g`. This linear Diophantine equation is known as **Bézout's identity**.

The algorithm is crucial in various areas of number theory and cryptography, such as finding modular multiplicative inverses.

## C++ Solution

This C++ solution implements the Extended Euclidean Algorithm recursively.

**`gcdExtended(int a, int b, int *x, int *y)` function:**

*   **Parameters:**
    *   `a`, `b`: The two integers for which GCD and Bézout coefficients are to be found.
    *   `*x`, `*y`: Pointers to integers where the Bézout coefficients `x` and `y` will be stored.
*   **Return Value:** The GCD of `a` and `b`.
*   **Base Case:**
    *   If `a` is `0`:
        *   The GCD is `b`.
        *   The coefficients are `x = 0` and `y = 1`, since `0*x + b*1 = b`.
        *   Return `b`.
*   **Recursive Step:**
    1.  Make a recursive call: `gcd = gcdExtended(b % a, a, &x1, &y1)`.
        *   Here, `x1` and `y1` are the coefficients for the equation `(b % a)*x1 + a*y1 = gcd(b % a, a)`. Note that `gcd(b % a, a)` is equal to `gcd(a, b)`.
    2.  Update `x` and `y` for the current call using `x1` and `y1`:
        *   `*x = y1 - (b / a) * x1;`
        *   `*y = x1;`
    3.  Return `gcd`.

**Derivation of `x` and `y` updates:**

From the recursive call, we have `(b % a) * x1 + a * y1 = g`.
We know that `b % a` can be written as `b - (b / a) * a`.
Substituting this into the equation:
`(b - (b / a) * a) * x1 + a * y1 = g`
`b * x1 - (b / a) * a * x1 + a * y1 = g`
`a * (y1 - (b / a) * x1) + b * x1 = g`

Comparing this with `ax + by = g`:
`x = y1 - (b / a) * x1`
`y = x1`

## Driver Code (C++)

The provided driver code demonstrates how to use `gcdExtended` to find the GCD and corresponding `x` and `y` coefficients for specific numbers.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <algorithm> // Not explicitly used but good for general practices

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Function for Extended Euclidean Algorithm
// This finds the integral solution for ax + by = gcd(a,b)
// x and y are passed by pointer to be updated
int gcdExtended(int a, int b, int *x, int *y)
{
    // Base Case: If a is 0, then b is the GCD
    // In this case, 0*x + b*y = b, so x=0, y=1 is a valid solution.
    if (a == 0)
    {
        *x = 0;
        *y = 1;
        return b;
    }

    int x1, y1; // To store results of recursive call
    // Recursive call with (b % a, a)
    int gcd = gcdExtended(b % a, a, &x1, &y1);

    // Update x and y using results from the recursive call
    // The derivation is explained in the Problem Description section above.
    *x = y1 - (b / a) * x1;
    *y = x1;

    return gcd;
}

// Driver Code
int main()
{
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int x, y, a = 35, b = 15;
    int g = gcdExtended(a, b, &x, &y);
    std::cout << "GCD(" << a << ", " << b << ") = " << g << std::endl;
    std::cout << "x = " << x << ", y = " << y << std::endl;
    std::cout << "Verification: " << a << "*" << x << " + " << b << "*" << y << " = " << (a*x + b*y) << std::endl;

    // Another example
    a = 10, b = 7;
    g = gcdExtended(a, b, &x, &y);
    std::cout << "\nGCD(" << a << ", " << b << ") = " << g << std::endl;
    std::cout << "x = " << x << ", y = " << y << std::endl;
    std::cout << "Verification: " << a << "*" << x << " + " << b << "*" << y << " = " << (a*x + b*y) << std::endl;

    return 0;
}
```