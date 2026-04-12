# Longest Common Subsequence (Recursive with Memoization)

## Problem Description

Given two sequences (strings) `S1` and `S2`, find the length of their longest common subsequence (LCS). A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. The longest common subsequence problem is a classic example that can be solved using dynamic programming.

## C++ Solution

This C++ solution implements a recursive approach with memoization (top-down dynamic programming) to find the length of the Longest Common Subsequence.

**`dp[1005][1005]` table:**

*   A 2D vector `dp` is used for memoization. `dp[i][j]` stores the length of the LCS of `S1[0...i-1]` and `S2[0...j-1]`.
*   Initialized with `-1` (or any value indicating not computed) to distinguish from actual LCS lengths (which are non-negative).

**`solve(string &s1, string &s2, ll end1, ll end2, vector<vll>& dp)` function (Recursive with Memoization):**

*   **Parameters:**
    *   `s1`, `s2`: The input strings.
    *   `end1`: The current ending index of `s1` (0-based) to consider.
    *   `end2`: The current ending index of `s2` (0-based) to consider.
    *   `dp`: The memoization table.
*   **Base Cases:**
    *   If `end1 < 0` or `end2 < 0`, it means one of the strings is exhausted (or empty subsequence considered). The LCS length is `0`. Store `0` in `dp[end1+1][end2+1]` and return `0`.
*   **Memoization Check:**
    *   If `dp[end1+1][end2+1]` is not `-1`, it means the result for this subproblem is already computed. Return its stored value.
*   **Recurrence Relation:**
    1.  **Characters Match:** If `s1[end1] == s2[end2]`:
        *   The current characters are part of the LCS. The length of LCS increases by 1 plus the LCS of the remaining prefixes `s1[0...end1-1]` and `s2[0...end2-1]`.
        *   `dp[end1+1][end2+1] = solve(s1, s2, end1-1, end2-1, dp) + 1;`
    2.  **Characters Don't Match:** If `s1[end1] != s2[end2]`:
        *   The current characters cannot both be part of the LCS simultaneously. We must either exclude `s1[end1]` or `s2[end2]`.
        *   `v1 = solve(s1, s2, end1, end2-1, dp)`: LCS without `s2[end2]`.
        *   `v2 = solve(s1, s2, end1-1, end2, dp)`: LCS without `s1[end1]`.
        *   `dp[end1+1][end2+1] = max(v1, v2);`
*   Store the computed result in `dp[end1+1][end2+1]` and return it.

**`main()` function:**

*   Reads two input strings `s1` and `s2`.
*   Initializes the `dp` table. `dp[i][j]` is set to `0` if `i=0` or `j=0` (base cases for empty strings), otherwise `-1` (uncomputed).
*   Calls `solve(s1, s2, n-1, m-1, dp)` to get the LCS length for the entire strings.
*   Prints the result.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <string>    // Required for std::string
#include <algorithm> // Required for std::max
#include <limits>    // For std::numeric_limits

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define ll long long 
#define ld long double 
#define vll std::vector<long long>
#define vi std::vector<int>
// #define f first // Avoiding conflicts with member access
// #define s second // Avoiding conflicts with member access
#define pb push_back
#define printoneline(arr) for(long long x_val : arr){std::cout<<x_val<<" ";} std::cout<<"\n";
// #define sort(a) std::sort(a.begin(),a.end()); // Avoid macro conflict
// #define rsort(a) std::sort(a.rbegin(),a.rend()); // Avoid macro conflict
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid macro conflict
#define input(arr) for(long long i_idx=0;i_idx<arr.size();i_idx++){std::cin>>arr[i_idx];}\

// Define a large value for infinity or an uncomputed state, if needed. -1 is used here for uncomputed.
// ll inf=std::numeric_limits<long long>::max();

// Recursive function with memoization to find the Longest Common Subsequence length.
// s1, s2: input strings
// end1, end2: current ending indices (0-based) of prefixes of s1 and s2 to consider
// dp: memoization table
ll solve(std::string &s1, std::string &s2, ll end1, ll end2, std::vector<vll>&dp)
{
    // Base case: If either string prefix is empty, LCS length is 0.
    // Indices in dp table are 1-based, so map end1 -> end1+1, end2 -> end2+1.
    if(end1 < 0 || end2 < 0){
        return 0;
    }
    
    // Memoization check: If result for this subproblem is already computed, return it.
    if(dp[end1+1][end2+1] != -1){
        return dp[end1+1][end2+1];
    }
    
    // If characters at current ends match
    if(s1[end1] == s2[end2])
    {
        // Include current characters in LCS and recurse for remaining prefixes.
        dp[end1+1][end2+1] = solve(s1, s2, end1-1, end2-1, dp) + 1;
    }
    else // If characters at current ends do not match
    {
        // Exclude s2[end2] and find LCS of s1[0...end1] and s2[0...end2-1]
        ll val1 = solve(s1, s2, end1, end2-1, dp);
        
        // Exclude s1[end1] and find LCS of s1[0...end1-1] and s2[0...end2]
        ll val2 = solve(s1, s2, end1-1, end2, dp);
        
        // Take the maximum of these two possibilities
        dp[end1+1][end2+1] = std::max(val1, val2);
    }
    
    return dp[end1+1][end2+1]; // Return the computed and stored result
}

int main()
{
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);
    
    std::string s1, s2;
    std::cin >> s1;
    std::cin >> s2;
    
    ll n = s1.length();
    ll m = s2.length();
    
    // dp table. dp[i][j] stores LCS of s1[0...i-1] and s2[0...j-1].
    // Initialize with -1 to mark uncomputed states.
    std::vector<vll> dp(n + 1, vll(m + 1, -1));
    
    // Base cases for DP: LCS with an empty string is 0.
    for(ll i = 0; i <= n; i++){dp[i][0] = 0;}
    for(ll j = 0; j <= m; j++){dp[0][j] = 0;}
    
    // Call the recursive solve function starting with the full strings (0-indexed n-1, m-1).
    // The result is stored at dp[n][m].
    ll ans = solve(s1, s2, n - 1, m - 1, dp);
    
    std::cout << ans << "\n";
    
    return 0;
}
```