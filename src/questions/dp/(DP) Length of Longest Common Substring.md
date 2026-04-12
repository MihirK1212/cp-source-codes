# Length of Longest Common Substring (Dynamic Programming)

## Problem Description

Given two strings `S1` and `S2` with lengths `n` and `m` respectively, find the length of the longest common substring.

**Distinction from Longest Common Subsequence:**

It's important to differentiate between a **substring** and a **subsequence**. A subsequence does not require contiguous characters from the original string, whereas a substring must be contiguous. For example, for "ABCDEF":
*   "ACE" is a subsequence.
*   "BCD" is a substring.

## C++ Solution

This C++ solution uses dynamic programming to find the length of the longest common substring. The core idea is to build a 2D DP table where `dp[i][j]` stores the length of the longest common suffix of `S1[0...i-1]` and `S2[0...j-1]` that ends at `S1[i-1]` and `S2[j-1]`.

**DP Table Definition:**

*   `dp[i][j]` = Length of the longest common suffix of `S1[0...i-1]` and `S2[0...j-1]`.

**Base Cases:**

*   `dp[0][j] = 0` for all `j` (If `S1` is empty, no common substring).
*   `dp[i][0] = 0` for all `i` (If `S2` is empty, no common substring).

**Recurrence Relation:**

*   If `S1[i-1] == S2[j-1]` (characters match):
    *   `dp[i][j] = dp[i-1][j-1] + 1`
    *   This means the common suffix extends by one character.
*   If `S1[i-1] != S2[j-1]` (characters do not match):
    *   `dp[i][j] = 0`
    *   A common substring cannot continue, so the length resets to 0 at this point.

**Finding the Answer:**

*   The length of the longest common substring is the maximum value encountered anywhere in the `dp` table.

```cpp
#include <string> // Required for std::string
#include <vector> // Required for std::vector (if using dynamic DP table)
#include <cstring> // Required for memset
#include <algorithm> // Required for std::max

class Solution{
public:
    
    // Function to find the length of the longest common substring
    int longestCommonSubstr (std::string s1, std::string s2, int n, int m)
    {
        // Create a 2D DP table. dp[i][j] will store the length of the longest common suffix
        // of s1[0...i-1] and s2[0...j-1].
        int dp[n+1][m+1];
        std::memset(dp, 0, sizeof(dp)); // Initialize all values to 0
        
        int max_len = 0; // Stores the maximum length found so far (the answer)
        
        // Fill the DP table
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                // If characters match, extend the common substring
                if(s1[i-1] == s2[j-1])
                {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    max_len = std::max(max_len, dp[i][j]); // Update overall maximum
                }
                else
                {
                    // If characters don't match, common substring is broken
                    dp[i][j] = 0;
                }
            }
        }
        
        return max_len;           
    }
};
```

## Driver Code (C++)

```cpp
#include <iostream> // For std::cin, std::cout, std::endl
#include <string>   // For std::string
#include <vector>   // For std::vector
#include <cstring>  // For memset
#include <algorithm> // For std::max

// Assuming Solution class is defined in the same file or a preceding header.
// class Solution { ... };

int main()
{
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t; 
    std::cin >> t; // Number of test cases
    while (t--)
    {
        int n, m; 
        std::cin >> n >> m; // Lengths of strings
        std::string s1, s2;
        std::cin >> s1 >> s2; // Input strings
        Solution ob;

        std::cout << ob.longestCommonSubstr (s1, s2, n, m) << std::endl;
    }
    return 0;
}
```