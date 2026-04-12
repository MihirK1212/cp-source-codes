# Solution of Linear Diophantine Equation

## Problem Description

Given a linear Diophantine equation of the form `ax + by = c`, where `a`, `b`, and `c` are integers, the task is to find one integer solution `(x, y)`. If no integer solution exists, the function should indicate that. This problem is fundamentally solved using the **Extended Euclidean Algorithm**.

**Existence of Solutions:**

A linear Diophantine equation `ax + by = c` has integer solutions `(x, y)` if and only if `c` is divisible by `gcd(a, b)` (the greatest common divisor of `a` and `b`).

## Approach

1.  **Extended Euclidean Algorithm:** Use the Extended Euclidean Algorithm to find integers `x_gcd` and `y_gcd` such that `a * x_gcd + b * y_gcd = gcd(a, b)`. Let `g = gcd(a, b)`.
2.  **Check for Solvability:** If `c` is not divisible by `g` (i.e., `c % g != 0`), then no integer solution exists for `ax + by = c`.
3.  **Find Particular Solution:** If `c` is divisible by `g`, a particular solution `(x0, y0)` can be found:
    *   `x0 = x_gcd * (c / g)`
    *   `y0 = y_gcd * (c / g)`

## C++ Solution

The C++ solution provides two functions:

1.  **`gcd_extend(int a, int b, int& x, int& y)`:** This is the implementation of the Extended Euclidean Algorithm. It recursively calculates `gcd(a, b)` and simultaneously finds `x` and `y` such that `ax + by = gcd(a, b)`.
    *   **Base Case:** If `b == 0`, then `gcd(a, 0) = a`. In this case, `x = 1` and `y = 0` satisfy `a*1 + 0*0 = a`.
    *   **Recursive Step:** It recursively calls `gcd_extend` with `(b, a % b)`. The `x` and `y` values returned from the recursive call (let's call them `x1` and `y1`) satisfy `b*x1 + (a % b)*y1 = gcd(b, a % b)`. Using the identity `a % b = a - (a/b)*b`, we can substitute and derive the new `x` and `y` for `a` and `b`.

2.  **`find_solution(int a, int b, int c)`:** This function uses `gcd_extend` to determine if a solution exists and, if so, prints one particular solution.
    *   **Edge Case (`a=0, b=0`):**
        *   If `c == 0`, there are infinite solutions (any `x, y` satisfy `0x + 0y = 0`).
        *   If `c != 0`, there is no solution.
    *   **General Case:** It calls `gcd_extend` to get `gcd` and initial `x, y` (`x_gcd, y_gcd`).
    *   Checks if `c` is divisible by `gcd`. If not, prints "No Solution exists".
    *   If divisible, calculates and prints the particular solution `x0 = x_gcd * (c / gcd)` and `y0 = y_gcd * (c / gcd)`.

```cpp
#include <iostream> // For std::cout, std::endl

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Extended Euclidean Algorithm: calculates gcd(a, b) and finds x, y such that ax + by = gcd(a, b).
// Parameters x and y are passed by reference to store the computed coefficients.
int gcd_extend(int a, int b, int& x, int& y)
{
    // Base case: if b is 0, gcd(a, 0) is a. The coefficients are x=1, y=0 (a*1 + 0*0 = a).
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    // Recursive step:
    // Call gcd_extend for (b, a % b).
    // Let x1, y1 be the coefficients for b*x1 + (a % b)*y1 = gcd(b, a % b).
    int x1, y1; // Temporary variables for recursive call results
    int g = gcd_extend(b, a % b, x1, y1); // g will be gcd(a,b)

    // Derive x and y for (a,b) from x1, y1 for (b, a%b):
    // We know: b*x1 + (a % b)*y1 = g
    // Substitute (a % b) = a - floor(a/b)*b:
    // b*x1 + (a - floor(a/b)*b)*y1 = g
    // b*x1 + a*y1 - floor(a/b)*b*y1 = g
    // a*y1 + b*(x1 - floor(a/b)*y1) = g
    // So, x = y1 and y = x1 - floor(a/b)*y1
    x = y1;
    y = x1 - (a / b) * y1; // (a / b) performs integer division (floor)

    return g; // Return the gcd
}

// Function to find and print one integer solution for the linear Diophantine equation ax + by = c.
void find_solution(int a, int b, int c)
{
    int x, y; // To store coefficients for gcd(a,b)

    // Handle edge case where both a and b are 0
    if (a == 0 && b == 0) {
        if (c == 0) {
            std::cout << "Infinite Solutions Exist" << std::endl;
        }
        else {
            std::cout << "No Solution exists" << std::endl;
        }
        return;
    }

    // Calculate gcd(a, b) and get coefficients x, y for a*x + b*y = gcd(a,b)
    int common_divisor = gcd_extend(a, b, x, y);

    // Check if c is divisible by gcd(a, b). If not, no integer solution exists.
    if (c % common_divisor != 0) {
        std::cout << "No Solution exists" << std::endl;
    }
    else {
        // Calculate the particular solution (x0, y0)
        // x0 = x * (c / gcd)
        // y0 = y * (c / gcd)
        std::cout << "x = " << x * (c / common_divisor)
                  << ", y = " << y * (c / common_divisor)
                  << std::endl;
    }
}

// Driver program
int main(void)
{
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);

    int a, b, c;

    // Example 1: a=4, b=18, c=10 (gcd(4,18)=2, 10%2==0, so solution exists)
    a = 4;
    b = 18;
    c = 10;
    std::cout << "For equation " << a << "x + " << b << "y = " << c << ":\n";
    find_solution(a, b, c);

    // Example 2: a=6, b=9, c=7 (gcd(6,9)=3, 7%3!=0, so no solution)
    a = 6;
    b = 9;
    c = 7;
    std::cout << "\nFor equation " << a << "x + " << b << "y = " << c << ":\n";
    find_solution(a, b, c);
    
    // Example 3: a=0, b=0, c=0
    a = 0;
    b = 0;
    c = 0;
    std::cout << "\nFor equation " << a << "x + " << b << "y = " << c << ":\n";
    find_solution(a, b, c);

    // Example 4: a=0, b=0, c=5
    a = 0;
    b = 0;
    c = 5;
    std::cout << "\nFor equation " << a << "x + " << b << "y = " << c << ":\n";
    find_solution(a, b, c);

    return 0;
}
```