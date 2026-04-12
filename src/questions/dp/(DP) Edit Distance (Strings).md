# Edit Distance (Strings) - DP

## Problem Description

Given two strings `A` and `B`, find the minimum number of operations required to convert string `A` to string `B`. The allowed operations are:
1.  Insert a character.
2.  Delete a character.
3.  Replace a character.

## C++ Solution

This problem can be solved using dynamic programming. We define `dp[i][j]` as the minimum number of operations to convert the first `i` characters of string `A` to the first `j` characters of string `B`.

**Base Cases:**
- `dp[0][j] = j`: To convert an empty string to a string of length `j`, we need `j` insertions.
- `dp[i][0] = i`: To convert a string of length `i` to an empty string, we need `i` deletions.

**Recurrence Relation:**
- If `A[i-1] == B[j-1]` (characters match), then `dp[i][j] = dp[i-1][j-1]` (no operation needed).
- If `A[i-1] != B[j-1]` (characters don't match), then `dp[i][j]` is 1 plus the minimum of:
    - `dp[i-1][j-1]` (Replace `A[i-1]` with `B[j-1]`)
    - `dp[i][j-1]` (Insert `B[j-1]` into `A`)
    - `dp[i-1][j]` (Delete `A[i-1]` from `A`)

```cpp
#include <string>
#include <vector>
#include <algorithm> // Required for std::min

class Solution {
public:
    int minDistance(std::string A, std::string B) 
    {
        int n = A.length();
        int m = B.length();

        // dp[i][j] will store the minimum operations to convert A[0...i-1] to B[0...j-1]
        int dp[n+1][m+1];

        // Initialize DP table
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=m;j++)
            {
                // Base cases
                if(i==0) // Converting an empty string A to B[0...j-1] requires j insertions
                {
                    dp[i][j] = j; 
                    continue;
                }
                if(j==0) // Converting A[0...i-1] to an empty string B requires i deletions
                {
                    dp[i][j] = i; 
                    continue;
                }

                // If characters match, no operation needed for this pair
                if(A[i-1]==B[j-1])
                {
                    dp[i][j] = dp[i-1][j-1];
                }
                else // Characters don't match, consider all three operations
                {
                    dp[i][j] = std::min({
                        dp[i-1][j-1], // Replace
                        dp[i][j-1],   // Insert
                        dp[i-1][j]    // Delete
                    }) + 1;
                }
            }
        }

        return dp[n][m]; // The result is in the bottom-right corner of the DP table
    }
};
```
