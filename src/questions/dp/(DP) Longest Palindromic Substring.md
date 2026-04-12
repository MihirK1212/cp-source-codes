# Longest Palindromic Substring (DP)

## Problem Description

Given a string `S`, find the longest substring of `S` that is a palindrome. A substring is a contiguous sequence of characters within a string. A palindrome is a string that reads the same forwards and backwards.

**Example:**

For `S = "babad"`:

*   Palindromic substrings: "b", "a", "d", "bab", "aba"
*   Longest palindromic substrings: "bab", "aba"

## C++ Solution (Longest Common Substring Approach)

This solution uses a clever approach by reducing the problem to finding the **Longest Common Substring (LCS) between the original string and its reverse**. However, a simple LCS is not enough, as the matching substring must also have the *same starting/ending indices* when mapped back to the original and reversed strings. This extra check ensures that the common substring is indeed a palindrome in the original string.

**Algorithm:**

1.  **Reverse String:** Create a reversed version of the input string `A`, let's call it `B`.
2.  **Dynamic Programming Table `dp[i][j]`:**
    *   `dp[i][j]` stores the length of the longest common suffix between `A[0...i-1]` and `B[0...j-1]`.
    *   **Initialization:** All `dp` values are initialized to `0`.
    *   **Recurrence Relation:**
        *   If `A[i-1] == B[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1` (characters match, extend common suffix).
        *   Else: `dp[i][j] = 0` (characters don't match, common suffix breaks).
3.  **`valid(int i, int j, int len, int n)` Function:**
    *   This is the crucial function that distinguishes a simple LCS from a palindromic LCS.
    *   It checks if a common substring of `len` ending at `A[i-1]` and `B[j-1]` corresponds to a valid palindrome in the original string.
    *   In the original string `A`, the substring would be `A[i-len ... i-1]`.
    *   In the reversed string `B`, the substring would be `B[j-len ... j-1]`.
    *   For this to be a palindrome, the start index in `A` (`i-len`) must map to the end index in `B` when considering the original string, and vice versa. Specifically, `A[start]` must be `B[n-1-start]`. 
    *   The condition `end_B==(n-start_A-1) && start_B==(n-end_A-1)` checks if the substring `A[start_A...end_A]` matches `B[start_B...end_B]` and if these indices correctly imply a palindrome. More directly, for a substring `A[k...p]` to be a palindrome, `k` must match `n-1-p` in the reversed string sense.

4.  **Find `max_comm_suff_len`:** While filling the `dp` table, keep track of the maximum `dp[i][j]` value that also satisfies the `valid` condition.
5.  **Reconstruct Longest Palindromic Substring:** After filling the `dp` table, iterate through it again. When `dp[i][j]` equals `max_comm_suff_len` and is `valid`, extract the corresponding substring from `A` (`A[i-max_comm_suff_len ... i-1]`).

```cpp
#include <string>    // For std::string
#include <vector>    // For std::vector
#include <algorithm> // For std::reverse, std::max

// Helper function to validate if a common substring found between string S and its reverse
// actually forms a palindrome in the original string.
// i: current index in original string A (1-based for dp table)
// j: current index in reversed string B (1-based for dp table)
// len: length of the common suffix
// n: original length of string A (and B)
bool valid_palindrome_indices(int i, int j, int len, int n)
{
    // Substring in original string A: A[i-len ... i-1]
    // start_A = i - len; end_A = i - 1;

    // Substring in reversed string B: B[j-len ... j-1]
    // start_B = j - len; end_B = j - 1;

    // For a substring from A to be a palindrome, its start index in A must match
    // the corresponding end index in B (reversed A) when mapped back to original string indices.
    // Original string indices are 0 to n-1.
    // If a substring of A starts at `start_idx_A` and ends at `end_idx_A`,
    // its reversed counterpart in B should start at `n - 1 - end_idx_A` and end at `n - 1 - start_idx_A`.

    // Let `sub_start_A = i - len`; this is the 0-based start index in A.
    // Let `sub_end_A = i - 1`; this is the 0-based end index in A.

    // The common substring we found in B ends at `j-1` and has length `len`.
    // So it starts at `(j-1) - len + 1 = j - len`.
    // Its 0-based start index in B is `sub_start_B = j - len`.
    // Its 0-based end index in B is `sub_end_B = j - 1`.
    
    // For A[sub_start_A ... sub_end_A] to be a palindrome, it must be equal to 
    // reverse(A[sub_start_A ... sub_end_A]).
    // The reversed string B is essentially reverse(A).
    // So, we need to check if B[sub_start_B ... sub_end_B] matches A[sub_start_A ... sub_end_A].
    // The condition checks if the index mapping is consistent for a palindrome:
    // The character at A[p] should be equal to the character at A[q] if they are symmetric for palindrome. 
    // In terms of A and B, A[p] should be B[n-1-p].
    // The condition (i-1) == (n - 1 - (j-1)) + len -1 is essentially checking if the start of common
    // suffix from A is same as start of common suffix from reversed B mapped back.
    
    // The condition `end_B==(n-start_A-1) && start_B==(n-end_A-1)` in the original code is concise 
    // but a bit hard to follow. Let's use a more direct approach:
    // A common substring of length `len` ending at `A[i-1]` (0-indexed `i-1`) and `B[j-1]` (0-indexed `j-1`)
    // means: A[i-len...i-1] is equal to B[j-len...j-1].
    // For this to be a palindrome in A, A[k] must equal A[i-1-(k-(i-len))] for all k in the substring.
    // This is equivalent to checking if `n - (j-1)` (start index of current match in original string A) 
    // is equal to `i-len` (actual start index of the substring in A).
    // Or, more simply: The start index of the matched substring in A must be `n - (j-len) - 1`.
    // So `(i - len) == (n - (j-1) - 1)` is the condition.
    // Simplified: `i - len = n - j`
    return (i - len) == (n - j); 
}

// Function to find the longest palindromic substring in string A.
std::string longestPalindrome(std::string A) 
{
    std::string B = A; // Create a copy of A
    std::reverse(B.begin(), B.end()); // Reverse B
    
    int m = A.length();
    int n = B.length(); // n is same as m
    
    // dp[i][j] stores the length of the longest common suffix of A[0...i-1] and B[0...j-1].
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
    
    int max_pal_len = 0; // Stores the maximum length of a valid palindromic substring
    std::string result_pal = ""; // Stores the longest palindromic substring itself
    
    for(int i = 1; i <= m; i++)
    {
        for(int j = 1; j <= n; j++)
        {
            if(A[i-1] == B[j-1]) // If characters match
            {
                dp[i][j] = dp[i-1][j-1] + 1; // Extend common suffix
            }
            else
            {
                dp[i][j] = 0; // Common suffix breaks
            }
            
            // If current common suffix is longer than previous max and forms a valid palindrome
            // The condition (i-dp[i][j]) == (n-j) ensures the substring in A starts at the same relative position 
            // as its reverse in B (when mapped back to A).
            if(dp[i][j] > max_pal_len && (i - dp[i][j]) == (n - j))
            {
                max_pal_len = dp[i][j];
                // Extract the substring: A.substr(start_index, length)
                result_pal = A.substr(i - max_pal_len, max_pal_len);
            }
        }
    }
    
    return result_pal;
}

// The original code was structured inside a Solution class and had a wrapper for findLongestCommonSubstr.
// Re-integrating for clarity with the common problem definition.
// class Solution {
// public:
//     string longestPalindrome(string A) 
//     {
//         string B = A;
//         reverse(B.begin(),B.end());
        
//         return findLongestCommonSubstr(A,B);
//     }
// };

// main function for testing if needed
// int main() {
//     std::string s1 = "babad";
//     std::cout << "Longest Palindromic Substring for " << s1 << ": " << longestPalindrome(s1) << std::endl; // Output: bab or aba
//     
//     std::string s2 = "cbbd";
//     std::cout << "Longest Palindromic Substring for " << s2 << ": " << longestPalindrome(s2) << std::endl; // Output: bb
//     
//     std::string s3 = "a";
//     std::cout << "Longest Palindromic Substring for " << s3 << ": " << longestPalindrome(s3) << std::endl; // Output: a
//     
//     std::string s4 = "ac";
//     std::cout << "Longest Palindromic Substring for " << s4 << ": " << longestPalindrome(s4) << std::endl; // Output: a or c
//     
//     return 0;
// }
```