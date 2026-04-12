# Longest Repeating Subsequence (Dynamic Programming)

## Problem Description

Given a string `str`, find the length of the longest repeating subsequence such that the two subsequences do not have the same character at the same position. In other words, if `A` is the longest repeating subsequence, then for any `i`, `A[i]` should not be equal to `str[i]`.

This problem is a variation of the Longest Common Subsequence (LCS) problem. The key difference is the constraint that the characters at the same position in the original string and its repeating subsequence must be different.

## C++ Solution

This C++ solution uses dynamic programming to find the length of the longest repeating subsequence. It leverages a 2D DP table, similar to the standard LCS approach, but with an added condition to handle the non-overlapping indices constraint.

**Algorithm:**

1.  **Initialize DP Table:** Create a 2D array `dp[n+1][n+1]`, where `n` is the length of the input string `A`. Initialize all values to `0`.
    *   `dp[i][j]` will store the length of the longest repeating subsequence considering the first `i` characters of `A` and the first `j` characters of `A`.
2.  **Populate DP Table:** Iterate `i` from `1` to `n` and `j` from `1` to `n`:
    *   **Case 1: Characters Match and Indices Differ:** If `A[i-1] == A[j-1]` (characters match) AND `i != j` (indices are different, satisfying the non-overlapping condition):
        *   `dp[i][j] = dp[i-1][j-1] + 1;` (Take the diagonal value and add 1).
    *   **Case 2: Characters Don't Match or Indices are Same:** If `A[i-1] != A[j-1]` or `i == j`:
        *   `dp[i][j] = max(dp[i-1][j], dp[i][j-1]);` (Take the maximum of the value from above or from the left).
3.  **Result:** The final result `dp[n][n]` will contain the length of the longest repeating subsequence.
    *   The problem specifically asks if such a subsequence of length 2 or more exists, so return `dp[n][n] >= 2;`.

```cpp
#include <string>
#include <vector>
#include <algorithm> // For std::max
#include <cstring>   // For memset

class Solution {
public:
    // Function to find if a longest repeating subsequence of length at least 2 exists.
    // Returns 1 if it exists, 0 otherwise.
    int anytwo(std::string A) 
    {
        int n = A.size();

        // dp[i][j] will store the length of the longest repeating subsequence
        // considering prefixes of length i and j of the string A.
        // Note: The problem uses a fixed size array (105x105) for competitive programming,
        // for general C++ it's better to use std::vector<std::vector<int>>.
        // Assuming a max size of 100 for N, a 101x101 dp table is safe.
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(n + 1, 0));
        // memset(dp,0,sizeof(dp)); // Not needed with std::vector initialization above.

        // Fill the DP table
        for(int i = 1; i <= n; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                // If characters match AND their original indices are different (non-overlapping property)
                if(A[i-1] == A[j-1] && i != j){
                    dp[i][j] = dp[i-1][j-1] + 1; // Include this character in the subsequence
                }
                else{
                    // If characters don't match or indices are the same, take the maximum from previous states
                    dp[i][j] = std::max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        // If the length of the longest repeating subsequence is 2 or more, return 1 (true),
        // otherwise return 0 (false).
        return dp[n][n] >= 2; 
    }
};
```