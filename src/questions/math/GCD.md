# Greatest Common Divisor (GCD)

## Problem Description

This is an implementation of the Greatest Common Divisor (GCD) algorithm, also known as the Euclidean algorithm. The GCD of two or more integers (not all zero) is the largest positive integer that divides each of the integers without a remainder.

## C++ Solution

This C++ solution implements the Euclidean algorithm recursively to find the GCD of two non-negative integers `x` and `y`.

**Algorithm:**

*   **Base Case:** If `y` is 0, then `x` is the GCD.
*   **Recursive Step:** Otherwise, the GCD of `x` and `y` is the same as the GCD of `y` and the remainder of `x` divided by `y` (`x % y`). This step is repeated until the second number becomes 0.

```cpp
// Function to calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
// It is assumed that x and y are non-negative.
long long gcd(long long x, long long y)
{
    // Base case: If y is 0, then x is the GCD.
    if(y == 0){
        return x;
    }
    
    // Recursive step: GCD(x, y) = GCD(y, x % y)
    return gcd(y, x % y);
}
```