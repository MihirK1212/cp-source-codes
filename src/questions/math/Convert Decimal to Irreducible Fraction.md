# Convert Decimal to Irreducible Fraction

## Problem Description

Given a decimal number (which might have a fractional part), convert it into an irreducible (simplified) fraction of the form `N/D`, where `N` is the numerator and `D` is the denominator. An irreducible fraction is one where the numerator and denominator have no common factors other than 1.

**Example:**

*   `number = 0.5` -> `1/2`
*   `number = 0.25` -> `1/4`
*   `number = 1.75` -> `7/4`

## C++ Solution

The solution involves separating the integral and fractional parts of the decimal number, converting the fractional part into an approximate fraction, and then simplifying the resulting fraction using the Greatest Common Divisor (GCD).

**`gcd(long long a, long long b)` function:**

*   This is a standard implementation of the Euclidean algorithm to find the greatest common divisor of two non-negative integers `a` and `b`.

**`decimalToFraction(double number)` function:**

1.  **Separate Integral and Fractional Parts:**
    *   `intVal = floor(number)`: Extracts the integral part of the `number`.
    *   `fVal = number - intVal`: Extracts the fractional part.
2.  **Convert Fractional Part to Integer:**
    *   `const long pVal = 1000000000;`: A precision value (e.g., 10^9) is chosen to convert the fractional part into a large integer. This assumes the fractional part has at most 9 decimal places of precision that we want to consider.
    *   `round(fVal * pVal)`: Multiplies the fractional part by `pVal` and rounds it to the nearest integer. This effectively shifts the decimal point and converts the fractional part into an integer equivalent.
3.  **Calculate GCD:**
    *   `gcdVal = gcd(round(fVal * pVal), pVal);`: Calculates the GCD of the integer equivalent of the fractional part and the `pVal`. This GCD will be used to simplify the fraction.
4.  **Calculate Numerator and Denominator of Fractional Part:**
    *   `num = round(fVal * pVal) / gcdVal;`: The numerator of the fractional part after simplification.
    *   `deno = pVal / gcdVal;`: The denominator of the fractional part after simplification.
5.  **Combine with Integral Part:**
    *   The final numerator is `(intVal * deno) + num`. This combines the integral part with the simplified fractional part.
    *   The final denominator is `deno`.
6.  **Print Result:** Prints the irreducible fraction in `N/D` format.

```cpp
#include <iostream> // For std::cout
#include <cmath>    // For std::floor, std::round
#include <numeric>  // For std::gcd in C++17, but a custom gcd is provided here

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Function to calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
long long gcd(long long a, long long b)
{
    // Base cases
    if (a == 0) return b;
    if (b == 0) return a;
    
    // Ensure a is always greater than or equal to b for consistent modulo operation,
    // or simply use the property gcd(a, b) = gcd(b, a % b) directly.
    // The original code has an explicit if-else for a < b which simplifies to the standard form.
    if (a < b)
        return gcd(a, b % a); // gcd(a, b) = gcd(a, b % a) if a < b
    else
        return gcd(b, a % b); // gcd(a, b) = gcd(b, a % b) if a >= b
}

// Function to convert a decimal number to an irreducible fraction.
void decimalToFraction(double number)
{
    // Fetch the integral part of the decimal number.
    double intVal = std::floor(number);
    
    // Fetch the fractional part of the decimal number.
    double fVal = number - intVal;
    
    // Define a precision value to convert the fractional part to an integral equivalent.
    // For example, 10^9 means we consider up to 9 decimal places.
    const long long pVal = 1000000000; 
    
    // Calculate the GCD of the integer equivalent of the fractional part and the precision value.
    // We round fVal * pVal to handle potential floating point inaccuracies before GCD.
    long long gcdVal = gcd(static_cast<long long>(std::round(fVal * pVal)), pVal);
    
    // Calculate the simplified numerator and denominator for the fractional part.
    long long num_fractional = static_cast<long long>(std::round(fVal * pVal)) / gcdVal;
    long long deno = pVal / gcdVal;
    
    // Calculate the final numerator by combining the integral part with the simplified fractional part.
    // (integral_part * denominator_of_fractional_part) + numerator_of_fractional_part
    long long final_num = (static_cast<long long>(intVal) * deno) + num_fractional;
    
    // Print the irreducible fraction.
    std::cout << final_num << "/" << deno << std::endl;
}

// Driver code for testing
int main() {
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);

    std::cout << "0.5 as fraction: ";
    decimalToFraction(0.5); // Expected: 1/2

    std::cout << "0.25 as fraction: ";
    decimalToFraction(0.25); // Expected: 1/4

    std::cout << "1.75 as fraction: ";
    decimalToFraction(1.75); // Expected: 7/4

    std::cout << "0.333 as fraction: ";
    decimalToFraction(0.333); // Expected: 333/1000 (approximation)

    std::cout << "0.125 as fraction: ";
    decimalToFraction(0.125); // Expected: 1/8

    std::cout << "3.14 as fraction: ";
    decimalToFraction(3.14); // Expected: 157/50
    
    return 0;
}
```