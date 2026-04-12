# Permutations of Letters (With Repetition)

## Problem Description

Given a set of `n` distinct characters and an integer `k`, the task is to generate all possible permutations (strings) of length `k` where characters can be used multiple times (with repetition). For example, if the characters are `{'a', 'b'}` and `k = 2`, the permutations would be `"aa", "ab", "ba", "bb"`.

This is a classic problem solved using recursion and backtracking.

## C++ Solution

This C++ solution uses a recursive backtracking approach to generate all permutations of a specified length with repetition allowed.

**`show(vector<char> &s)` function:**

*   A simple helper function to print a `vector<char>` as a string, followed by a newline.

**`print(vector<char> &ch, long long k, vector<char> &s)` function (Recursive Backtracking):**

*   **Parameters:**
    *   `ch`: The input `vector<char>` containing the distinct characters available for permutation.
    *   `k`: The desired length of the permutations.
    *   `s`: The current permutation being built (passed by reference).
*   **Base Case:**
    *   If the current permutation's length (`s.size()`) is equal to `k`, it means a complete permutation of length `k` has been formed. Print `s` using the `show` function and return.
*   **Recursive Step:**
    1.  Iterate through each character `ch[i]` available in the input set `ch`.
    2.  **Choose:** Add `ch[i]` to the current permutation `s` (`s.push_back(ch[i])`).
    3.  **Explore:** Recursively call `print(ch, k, s)` to build the rest of the permutation.
    4.  **Unchoose (Backtrack):** Remove `ch[i]` from `s` (`s.pop_back()`) to backtrack and explore other possibilities.

**`main()` function:**

*   Reads `n` (number of distinct characters) and the characters into `ch`.
*   Reads `k` (desired length of permutations).
*   Initializes an empty `vector<char> s` to store the current permutation.
*   Calls `print(ch, k, s)` to start the permutation generation process.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <string>    // For string manipulation if needed (not directly in this code)
#include <algorithm> // For std::sort (if input chars need sorting for lexicographical order)

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Helper function to print a vector of characters as a string
void show(std::vector<char> &s)
{
    for(char c : s) // Range-based for loop for cleaner iteration
    {
        std::cout << c;
    }
    std::cout << "\n";
}

// Recursive backtracking function to generate permutations with repetition
// ch: available characters, k: desired length, s: current permutation being built
void print(std::vector<char> &ch, long long k, std::vector<char> &s)
{
    // Base case: If the current permutation 's' has reached the desired length 'k'
    if(s.size() == k)
    {
        show(s); // Print the complete permutation
        return;
    }
    
    // Recursive step: Try appending each available character to the current permutation
    for(long long i = 0; i < ch.size(); i++)
    {
        s.push_back(ch[i]);   // Choose: Add the character
        print(ch, k, s);      // Explore: Recursively call to build the rest of the permutation
        s.pop_back();         // Unchoose (Backtrack): Remove the character to try other options
    }
    
    return;
}

int main()
{
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    long long n_chars, k_length; 
    std::cin >> n_chars; // Read number of distinct characters
    std::vector<char> ch(n_chars); // Vector to store distinct characters

    // Read the distinct characters
    for(long long i = 0; i < n_chars; i++){std::cin >> ch[i];}
    
    std::cin >> k_length; // Read the desired length of permutations
    
    std::vector<char> current_permutation; // Vector to build permutations
    
    print(ch, k_length, current_permutation); // Start the permutation generation

    return 0;
}
```