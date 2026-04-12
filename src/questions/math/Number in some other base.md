# Number in Other Bases (Conversion and Checks)

## Problem Description

This document explores various methods for handling number conversions and checks in different bases, with a particular focus on scenarios like Excel column titles where a base-26 system (A-Z) behaves uniquely (e.g., after Z comes AA, not BA).

## Methods

### Method 1: Excel Column Title Conversion (Adjusted Base-26 Logic)

This method addresses the specific behavior of Excel column titles where, after 'Z' (which is 26), the next sequence is 'AA', not 'BA' (which would be analogous to 26 in a standard base-26 system with digits 0-25). This implies that 'Z' is treated as 26 and then the number for the next digit resets with a borrow. The key adjustment is `n--` after `n/=base;` when a digit is extracted.

```cpp
// Given n and base, extract digits in reverse order
// This method is for specific base-X systems like Excel columns.
// Example: For base 26 and n = 26 (Z), dig = 0 (Z is 26th letter), n becomes 0, n-- makes it -1, loop terminates.
// Example: For base 26 and n = 27 (AA), dig = 1 (A), n becomes 1, n-- makes it 0, loop terminates.
// Then for n=0, next dig=0 (A), n becomes 0, n-- makes it -1, loop terminates.
while(n > 0) { // Changed n >= 0 to n > 0 for correct loop termination and handling of 0.
    int dig = n % base;
    n /= base;
    // Crucial adjustment for Excel-like base conversion:
    // If dig is 0, it means the current digit is 'Z'. In this system, Z corresponds to 26, not 0.
    // So, we treat it as 26 and effectively borrow from the next place value by decrementing n.
    if (dig == 0) {
        dig = base; // Represents 'Z'
        n--;        // Adjust for the borrow
    }
    // At this point, 'dig' holds the value for the current character (1 for A, ..., 26 for Z)
    // The character is 'A' + (dig - 1)
    // (Further processing needed to convert dig to char and build string)
}
```

### Method 2: Excel Column Title (InterviewBit Approach)

This method is another way to convert a given integer `n` into its corresponding Excel column title (e.g., 1 -> A, 26 -> Z, 27 -> AA). It handles the base-26 system by explicitly treating `n % 26 == 0` as the letter 'Z' (value 26) and then adjusting `n` accordingly.

```cpp
// Refer to https://www.interviewbit.com/problems/excel-column-title/
std::vector<int> find_vect(int n)
{
    std::vector<int> num; // Stores digits in reverse order initially
    while(n != 0)
    {
        if((n % 26) == 0) { // If the remainder is 0, it means 'Z'
            num.push_back(26); // Represents 'Z'
            n -= 26;           // Effectively, treat 'Z' as 26 and carry over to higher place value
        }
        else { // For non-zero remainders, directly add the digit
            num.push_back(n % 26);
        }
        n /= 26; // Move to the next place value
    }
    std::reverse(num.begin(), num.end()); // Reverse to get correct order
    return num; // Returns a vector of integer representations of characters (1 for A, ..., 26 for Z)
}
```

### Method 3: Check if a Number is Representable in a Base with Unique Non-Zero Digits (Custom Check)

This method provides a boolean function `checkBase` to determine if a number `n` can be represented in a given base `b` such that each digit position (from right to left, starting at 0) uses a unique non-zero digit.

```cpp
#include <vector> // For std::vector

// n: the number to check
// b: the base
// taken: a boolean vector to track if a digit position has been used
// This function checks if all *non-zero* digits in the base representation occupy unique positions.
bool checkBase(long long n, long long b, std::vector<bool>& taken)
{
    long long i = 0; // Represents the digit position (0 for units place, 1 for base place, etc.)
    
    while(n != 0)
    {
        long long current_digit_val = n % b; // Get the current digit's value

        // If the current digit is non-zero
        if(current_digit_val != 0) {
            // If this digit position 'i' has not been taken yet by a non-zero digit, mark it as taken.
            if(!taken[i]){
                taken[i] = true;
            }
            else { // If this digit position 'i' is already taken by a non-zero digit, it's not valid
                return false; // Found a duplicate non-zero digit position
            }
        }
        
        n /= b; // Move to the next digit position (divide by base)
        i++;    // Increment digit position counter
    }
    return true;
}
```