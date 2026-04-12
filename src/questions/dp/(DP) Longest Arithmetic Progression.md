# Longest Arithmetic Progression (Dynamic Programming)

## Problem Description

Given a sequence of numbers, find the length of the longest arithmetic progression (LAP) in it. An arithmetic progression is a sequence of numbers such that the difference between the consecutive terms is constant.

## C++ Solution

This solution uses dynamic programming to find the longest arithmetic progression. The `dp[i][j]` state represents the length of the longest arithmetic progression with `A[i]` and `A[j]` as the first two terms (where `A[i]` comes before `A[j]` in the progression, `i < j`).

**Algorithm:**

1.  **Initialization:**
    *   `dp` table of size `n x n`, initialized with `2`. This is because any two elements `A[i]` and `A[j]` can form an arithmetic progression of length 2.
    *   `minInd`: A `std::map<int, int>` to quickly find the index of a number. It stores `value -> index`. This map is populated from right to left to ensure `k` is to the right of `j`.
    *   `ans`: Stores the maximum length found so far, initialized to 2.
2.  **Iteration (Backward):**
    *   The outer loop iterates `j` from `n-2` down to `1`.
    *   The inner loop iterates `i` from `j-1` down to `0`.
    *   For each pair `(A[i], A[j])`, we want to find a third term `A[k]` such that `A[i], A[j], A[k]` form an arithmetic progression.
        *   The common difference would be `diff = A[j] - A[i]`.
        *   The next term `A[k]` would be `A[j] + diff = 2 * A[j] - A[i]`.
        *   Look up `(2 * A[j] - A[i])` in `minInd` to find its index `k`. This ensures `k > j`.
        *   If `k` is found: `dp[i][j] = max(dp[i][j], dp[j][k] + 1)`. This means the AP ending with `(A[j], A[k])` can be extended by `A[i]`.
    *   Update `ans = max(ans, dp[i][j])`.
    *   After iterating through all `i` for a fixed `j`, add `A[j]` and its index `j` to `minInd`. This ensures that when processing `i < j`, `minInd` contains indices of elements to the right of `j`.

```cpp
#include <vector>
#include <map>
#include <algorithm> // For std::max

// Function to find the length of the longest arithmetic progression.
// A: The input vector of integers.
int Solution::solve(const vector<int> &A) 
{
    int n = A.size();

    // Base cases: If n is 1 or 2, the LAP length is n itself.
    if(n == 1 || n == 2){
        return n;
    }

    // dp[i][j] stores the length of the longest arithmetic progression
    // with A[i] as the first term and A[j] as the second term.
    // Initialize with 2, as any two elements form an AP of length 2.
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 2));
    
    // minInd maps a value to its minimum index.
    // This map is used to efficiently find a third term 'A[k]' for the AP.
    std::map<int, int> minInd;

    // Initialize ans with 2 (minimum possible LAP length for n>=2).
    int ans = 2;

    int i, j, k; // Loop iterators and index for the third term

    // Iterate 'j' from right to left (second to last element down to second element)
    for(j = n - 2; j >= 1; j--) 
    {   
        // For each 'j', iterate 'i' from 'j-1' down to '0' (elements to the left of j)
        for(i = j - 1; i >= 0; i--) 
        {
            // Calculate the expected third term 'A[k]'
            // A[j] is the middle term, A[i] is the first.
            // A[j] - A[i] = diff
            // A[k] = A[j] + diff = A[j] + (A[j] - A[i]) = 2*A[j] - A[i]
            int required_k_value = 2 * A[j] - A[i];

            // Check if the required third term exists in the map (meaning it's to the right of j)
            if(minInd.find(required_k_value) != minInd.end())
            {
                k = minInd[required_k_value]; // Get the index of the third term
                // Update dp[i][j]: The AP (A[i], A[j], A[k]...) has length dp[j][k] + 1.
                // We take the maximum of existing dp[i][j] and this new length.
                dp[i][j] = std::max(dp[i][j], dp[j][k] + 1);
            }
            
            // Update the overall maximum answer found
            ans = std::max(ans, dp[i][j]);
        }

        // After processing all (i,j) pairs for current j, add A[j] to the map
        // This makes A[j] available as a 'k' for future (i,j_new) pairs where j_new < j.
        minInd[A[j]] = j;
    }

    return ans;
}
```