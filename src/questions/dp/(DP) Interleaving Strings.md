# (DP) Interleaving Strings

## Problem Description

Given three strings `A`, `B`, and `C`, determine if `C` is an interleaving of `A` and `B`. An interleaving means that `C` is formed by combining characters from `A` and `B` in a way that maintains their relative order. For example, `"axyb"` is an interleaving of `"ab"` and `"xy"`.

## C++ Solution

This C++ solution uses dynamic programming to solve the interleaving strings problem. A 2D `dp` table is used where `dp[i][j]` is `true` if the first `i` characters of string `A` and the first `j` characters of string `B` can form the first `i+j` characters of string `C`.

**Algorithm:**

1.  **Initialization:**
    *   `dp[0][0]` is set to `true` (empty `A` and empty `B` can form an empty `C`).
    *   Other `dp` entries are initially `false`.
2.  **Fill DP Table:** Iterate `i` from `0` to `A.length()` and `j` from `0` to `B.length()`:
    *   **If `i > 0` and `A[i-1] == C[i+j-1]`:** If the `i`-th character of `A` matches the `(i+j)`-th character of `C`, and `dp[i-1][j]` was true (meaning `A[0...i-2]` and `B[0...j-1]` formed `C[0...i+j-2]`), then `v1` is true.
    *   **If `j > 0` and `B[j-1] == C[i+j-1]`:** Similarly, if the `j`-th character of `B` matches the `(i+j)`-th character of `C`, and `dp[i][j-1]` was true, then `v2` is true.
    *   `dp[i][j]` is `true` if either `v1` or `v2` is true.
3.  **Result:** The final answer is `dp[A.length()][B.length()]`.

```cpp
int Solution::isInterleave(string A, string B, string C) 
{
    int a = A.length();
    int b = B.length();
    int c = C.length();
    
    // If the total length of A and B is not equal to C, C cannot be an interleaving.
    if((a+b)!=c){return 0;}
    
    vector<vector<bool>> dp(a+1,vector<bool>(b+1,false));
    
    // dp[i][j] = true if A[0...i-1] and B[0...j-1] can form C[0...i+j-1]
    
    // Base case: empty A and empty B can form empty C
    dp[0][0] = true;
    
    // Fill dp table
    for(int i=0;i<=a;i++)
    {
        for(int j=0;j<=b;j++)
        {
            if(i==0 && j==0){continue;}
                        
            bool v1 = false , v2 = false;
            
            // Case 1: C[i+j-1] comes from A[i-1]
            if(i>0 && A[i-1]==C[i+j-1]){
                v1 = dp[i-1][j];
            }
            
            // Case 2: C[i+j-1] comes from B[j-1]
            if(j>0 && B[j-1]==C[i+j-1]){
                v2 = dp[i][j-1];
            }
            
            // C[i+j-1] can be formed if either case is true
            dp[i][j] = v1 || v2;
        }
    }
    
    return dp[a][b]; // Final result is whether full A and full B interleave to form full C
}
```