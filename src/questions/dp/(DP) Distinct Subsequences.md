# Distinct Subsequences (DP)

## Problem Description

This problem is from InterviewBit: [Distinct Subsequences](https://www.interviewbit.com/problems/distinct-subsequences/)

Given two sequences `A` and `B`, count the number of unique ways in sequence `A` to form a subsequence that is identical to sequence `B`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, "ACE" is a subsequence of "ABCDE", but "AEC" is not.

## C++ Solution

This problem can be solved using dynamic programming. We define `dp[i][j]` as the number of distinct subsequences of `A[0...i-1]` that are equal to `B[0...j-1]`.

**Base Cases:**
- `dp[i][0] = 1`: There is always one way to form an empty string `B` (by deleting all characters from `A`).
- `dp[0][j] = 0` for `j > 0`: An empty string `A` cannot form a non-empty string `B`.

**Recurrence Relation:**
- If `A[i-1] == B[j-1]` (current characters match):
    - `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`
    - `dp[i-1][j-1]` represents the case where we **include** `A[i-1]` to match `B[j-1]`. We then need to form `B[0...j-2]` from `A[0...i-2]`.
    - `dp[i-1][j]` represents the case where we **exclude** `A[i-1]`. We then need to form `B[0...j-1]` from `A[0...i-2]`.
- If `A[i-1] != B[j-1]` (current characters don't match):
    - `dp[i][j] = dp[i-1][j]`
    - We can only **exclude** `A[i-1]`. We then need to form `B[0...j-1]` from `A[0...i-2]`.

```cpp
#include <string>
#include <vector>
#include <algorithm> // Required for std::max (though not directly used with min/max, for general utility)

class Solution {
public:
    int numDistinct(std::string A, std::string B)
    {
        int m = A.length();
        int n = B.length();

        // Edge cases for empty strings or string B being longer than A
        // (An empty string can form an empty subsequence in one way)
        // (A string shorter than B cannot form B as a subsequence)
        if (n == 0) return 1; // B is empty, one way to form it
        if (m < n) return 0; // A is shorter than B, cannot form B

        // dp[i][j] stores the number of distinct subsequences of A[0...i-1] equal to B[0...j-1]
        // Using long long to prevent potential overflow as counts can be large
        std::vector<std::vector<long long>> dp(m + 1, std::vector<long long>(n + 1, 0));

        // Initialize DP table
        for(int i = 0; i <= m; i++)
        {
            for(int j = 0; j <= n; j++)
            {
                // Base case: To form an empty string B (j=0), there's one way (delete all chars from A)
                if(j == 0)
                {
                    dp[i][j] = 1; 
                    continue;
                }
                // Base case: To form a non-empty string B from an empty string A (i=0), there are zero ways
                if(i == 0)
                {
                    dp[i][j] = 0; 
                    continue;
                }
                
                // If current characters match (A[i-1] and B[j-1])
                if(A[i-1] == B[j-1])
                {
                    // Sum of two cases:
                    // 1. Include A[i-1] to match B[j-1]: then count distinct subsequences of A[0...i-2] for B[0...j-2]
                    // 2. Exclude A[i-1]: then count distinct subsequences of A[0...i-2] for B[0...j-1]
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                }
                else // If current characters do not match
                {
                    // Only one case: Exclude A[i-1]
                    // Count distinct subsequences of A[0...i-2] for B[0...j-1]
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        return static_cast<int>(dp[m][n]); // Cast to int as problem expects int return type
    }
};
```
