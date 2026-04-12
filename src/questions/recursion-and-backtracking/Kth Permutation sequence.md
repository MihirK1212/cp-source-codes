# Kth Permutation Sequence (Recursion and Backtracking)

## Problem Description

The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations. By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

1.  "123"
2.  "132"
3.  "213"
4.  "231"
5.  "312"
6.  "321"

Given `n` and `k`, return the `k`-th permutation sequence.

## C++ Solution

This C++ solution finds the `k`-th permutation using a mathematical approach rather than generating all permutations. The core idea is to determine each digit of the permutation from left to right. We use the fact that there are `(n-1)!` permutations starting with each of the `n` available digits.

**Algorithm:**

1.  **Initialization:**
    *   Create a string `ans` to store the resulting permutation.
    *   Create a `set<int> s` to store the available digits (1 to `n`). A set maintains elements in sorted order, which is crucial for selecting the `pos`-th available digit.
    *   Calculate `fact_n_minus_1 = (n-1)!`. This represents the number of permutations that start with a particular digit when there are `n-1` remaining digits.
    *   Decrement `k` by 1 (`k = k - 1`) because `k` is 1-indexed in the problem, but for 0-indexed calculations (like `k / fact_n_minus_1`), it's easier to use a 0-indexed `k`.

2.  **Iterative Selection:** Loop `i` from `1` to `n` (representing the position of the digit we are currently determining):
    *   **Determine `pos`:** Calculate `pos = k / fact_n_minus_1`. This `pos` (0-indexed) tells us which block of `fact_n_minus_1` permutations `k` falls into, and thus which available digit should be chosen for the current position.
    *   **Select Digit:** Use an iterator to find the `pos`-th element in the `set s`. Add this digit to `ans`.
    *   **Remove Digit:** Erase the chosen digit from `s` so it's not used again.
    *   **Update `k`:** Update `k = k % fact_n_minus_1` to find the relative `k` within the chosen block of permutations.
    *   **Update Factorial:** If `n - i` (number of remaining elements) is greater than 0, update `fact_n_minus_1 = fact_n_minus_1 / (n - i)` for the next iteration.

3.  **Return `ans`.

**Example for `n=3, k=3` (0-indexed `k=2`):

*   `s = {1, 2, 3}`, `fact_n_minus_1 = 2! = 2`.

*   **Iteration 1 (i=1):**
    *   `k = 2`, `fact_n_minus_1 = 2`.
    *   `pos = 2 / 2 = 1`.
    *   `s.begin()` points to 1. Advancing by 1, `*it` becomes 2. `ans = "2"`.
    *   `s` becomes `{1, 3}`.
    *   `k = 2 % 2 = 0`.
    *   `fact_n_minus_1 = 2 / (3-1) = 2 / 2 = 1`.

*   **Iteration 2 (i=2):**
    *   `k = 0`, `fact_n_minus_1 = 1`.
    *   `pos = 0 / 1 = 0`.
    *   `s.begin()` points to 1. Advancing by 0, `*it` is 1. `ans = "21"`.
    *   `s` becomes `{3}`.
    *   `k = 0 % 1 = 0`.
    *   `fact_n_minus_1 = 1 / (3-2) = 1 / 1 = 1`.

*   **Iteration 3 (i=3):**
    *   `k = 0`, `fact_n_minus_1 = 1`.
    *   `pos = 0 / 1 = 0`.
    *   `s.begin()` points to 3. Advancing by 0, `*it` is 3. `ans = "213"`.
    *   `s` becomes `{}`.
    *   `k = 0 % 1 = 0`.

Result: "213", which is the 3rd permutation.

```cpp
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <numeric> // For std::iota (not used, but good for sequences)

class Solution {
public:
    // Helper function to calculate factorial. Used for initial (n-1)!
    int factorial(int n)
    {
        int res = 1;
        for (int i = 2; i <= n; ++i) {
            res *= i;
        }
        return res;
    }

    std::string getPermutation(int n, int k)
    {
        std::string ans = "";
        std::vector<int> numbers;
        int fact = 1;

        // Prepare numbers from 1 to n and calculate (n-1)!
        // We calculate (n-1)! initially, and for subsequent steps, we divide by (remaining_elements)!
        for(int i = 1; i <= n; ++i) {
            numbers.push_back(i); // Store available digits
            if (i < n) { // Calculate (n-1)! (or (n-i)! for subsequent steps)
                fact *= i;
            }
        }
        
        // Adjust k to be 0-indexed
        k--; 

        for(int i = n; i >= 1; --i) {
            // The index of the number to be placed at the current position
            // is k / (remaining_elements - 1)!
            int index = k / fact;
            
            // Append the chosen number to the result
            ans += std::to_string(numbers[index]);
            
            // Remove the chosen number from the available numbers
            numbers.erase(numbers.begin() + index);
            
            // Update k for the next iteration
            k %= fact;
            
            // Update factorial for the next step
            if (i > 1) { // Avoid division by zero when i becomes 1 (last element)
                fact /= (i - 1);
            }
        }

        return ans;
    }
};
```