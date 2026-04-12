# Last Digit of a^b

## Problem Description

Given two numbers, `A` (represented as a single digit or the last digit of a larger number) and `B` (represented as a string, potentially a very large number), the task is to find the last digit of `A` raised to the power of `B` (i.e., `A^B`).

**Example:**

*   `A = "3"`, `B = "10"` -> `3^10 = 59049`, last digit is `9`.
*   `A = "2"`, `B = "3"` -> `2^3 = 8`, last digit is `8`.

## C++ Solution

The solution leverages the cyclicity of the last digits of powers of a number. The last digits of powers repeat in cycles of length at most 4.

**Key Observations on Cyclicity of Last Digits:**

*   **Last digit 0, 1, 5, 6:** Always themselves (cycle length 1).
*   **Last digit 4, 9:** Cycle length 2.
    *   `4^1 = 4`, `4^2 = 16 (6)`, `4^3 = 64 (4)`, ...
    *   `9^1 = 9`, `9^2 = 81 (1)`, `9^3 = 729 (9)`, ...
*   **Last digit 2, 3, 7, 8:** Cycle length 4.
    *   `2^1 = 2`, `2^2 = 4`, `2^3 = 8`, `2^4 = 16 (6)`, `2^5 = 32 (2)`, ...

Therefore, to find the last digit of `a^b`, we only need the last digit of `A` and `B` modulo 4 (or 2 for digits 4 and 9), adjusted for `b=0` or `b` being a multiple of the cycle length.

**Algorithm:**

1.  **Extract Last Digit of `A`:** Convert the last character of string `A` to an integer `a`.
2.  **Handle `b = 0`:** If `B` represents `0`, then `A^0 = 1`. Return `1`.
3.  **Extract Last Two Digits of `B`:** To find `B % 4`, we only need the last two digits of `B`. A helper function `last_two(std::string& B)` is used for this. If `B` has only one digit, it returns that digit. Otherwise, it returns the integer formed by the last two digits.
4.  **Calculate Effective Exponent:** Let `b_mod_4 = b % 4`. 
    *   To handle cases where `b % 4 = 0` (which implies `b` is a multiple of 4, or `b` is 0), and to avoid `pow(x,0)` returning `1` when it should return `x^4`'s last digit (e.g., `2^4` last digit is 6, `2^0` is 1), we use `b_effective = b_mod_4 + 4`. This ensures the exponent is always at least 4 for non-zero `B`, correctly capturing the cycle.
5.  **Calculate Power and Last Digit:** Compute `(a ^ b_effective) % 10`. The `pow` function in `<cmath>` returns a `double`, so cast `a` and the result carefully. For `long long` integers, a custom modular exponentiation function is safer and more precise.

```cpp
#include <string>    // For std::string
#include <vector>    // Not directly used but common
#include <algorithm> // Not directly used but common
#include <cmath>     // For std::pow (use with caution for large exponents/precision)

// Helper function to extract the last two digits of a string-represented number.
// This is relevant for finding the number modulo 4 or 100, etc.
int last_two(const std::string& B)
{
    int n = B.size();
    
    if(n == 0) { return 0; } // Handle empty string case for B
    if(n == 1) { return B[0] - '0'; } // If B has only one digit
    
    // Otherwise, return the integer formed by the last two digits
    return (B[n-2] - '0') * 10 + (B[n-1] - '0');
}

// Function to find the last digit of A^B.
// A: base as a string (its last digit matters)
// B: exponent as a string (its last two digits matter for modulo 4)
class Solution {
public:
    int solve(std::string A, std::string B) 
    {
        // Edge case: B is "0"
        if (B == "0") {
            return 1; // Any number to the power of 0 is 1
        }

        // Get the last digit of A
        long long a_last_digit = (A.back() - '0');

        // Get the last two digits of B to calculate B % 4
        // This is sufficient because (X * 100 + Y) % 4 == Y % 4
        // if X is an integer and Y is the last two digits.
        long long b_last_two_digits = last_two(B);
        
        // Calculate the effective exponent for cyclicity.
        // The cycle length of last digits is at most 4. (e.g., 2,4,8,6,2...)
        // We use b_last_two_digits % 4. If result is 0, use 4 instead of 0 to get correct 4th power.
        // Adding 4 ensures the exponent is never 0 and correctly corresponds to the 4th power if b is a multiple of 4.
        long long effective_exponent = (b_last_two_digits % 4 == 0) ? 4 : (b_last_two_digits % 4);
        
        // Calculate (a_last_digit ^ effective_exponent) % 10
        // Using std::pow might introduce floating point inaccuracies for large numbers,
        // but for single digit base and small effective_exponent, it's generally fine.
        // For production, a custom integer power function is recommended.
        long long result_pow = 1;
        for (int i = 0; i < effective_exponent; ++i) {
            result_pow = (result_pow * a_last_digit) % 10;
        }
        
        return result_pow;
    }
};
```