# Perfect Number

## Problem Description

A **perfect number** is a positive integer that is equal to the sum of its proper positive divisors (divisors excluding the number itself). The first perfect number is 6, as its proper divisors are 1, 2, and 3, and `1 + 2 + 3 = 6`.

This problem aims to identify if a given number is perfect and, in the provided driver code, lists all perfect numbers up to a certain limit.

## C++ Solution

The `isPerfect(long long int n)` function checks if a given number `n` is a perfect number.

**Algorithm:**

1.  **Initialize `sum`:** Start `sum` with `1` because `1` is a divisor of every positive integer.
2.  **Iterate through potential divisors:** Loop from `i = 2` up to `sqrt(n)`.
    *   If `i` is a divisor of `n` (`n % i == 0`):
        *   If `i * i != n` (meaning `i` and `n/i` are distinct divisors), add both `i` and `n/i` to `sum`.
        *   If `i * i == n` (meaning `i` is the square root of `n`, so `i` and `n/i` are the same divisor), add `i` to `sum` only once.
3.  **Check for Perfect Number:** After the loop, if `sum` is equal to `n` and `n` is not `1` (as `1` has no proper divisors and is not considered perfect), then `n` is a perfect number. Return `true`.
4.  Otherwise, return `false`.

The `main` function demonstrates usage by finding and printing perfect numbers up to 10000.

```cpp
#include <iostream> // For std::cout, std::cin
#include <cmath>    // For std::sqrt

// using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Function to check if a number is a perfect number
bool isPerfect(long long int n)
{
    // To store sum of proper divisors. Start with 1 as it's a divisor of every number.
    long long int sum = 1;
    
    // Iterate from 2 up to sqrt(n) to find divisors.
    // If i divides n, then n/i also divides n.
    for (long long int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            if(i * i != n) { // If i and n/i are distinct divisors
                sum = sum + i + n / i;
            }
            else { // If i is the square root (i * i == n), add it only once
                sum = sum + i;
            }
        }
    }
    
    // A perfect number is equal to the sum of its proper divisors.
    // And 1 is not considered a perfect number.
    if (sum == n && n != 1) {
        return true;
    }
  
    return false;
}
  
// Driver program to find perfect numbers
int main()
{
    std::cout << "Below are all perfect numbers till 10000\n";
    for (int n = 2; n < 10000; n++) {
        if (isPerfect(n)) {
            std::cout << n << " is a perfect number\n";
        }
    }
  
    return 0;
}
```