# Evaluate Boolean Expression to True (DP) - Boolean Parenthesization

## Problem Description

This problem is commonly known as [Boolean Parenthesization on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/boolean-parenthesization5610/1#).

Given a boolean expression `S` of length `N` with boolean symbols (`T` for True, `F` for False) and logical operators (`&` for AND, `|` for OR, `^` for XOR), find the number of ways to parenthesize the expression such that it evaluates to `true`. The result should be returned modulo `1003` (a common prime modulus in competitive programming).

For example, given the expression `T|F&T`:

*   `(T|F)&T` evaluates to `(T)&T` which is `T` (1 way)
*   `T|(F&T)` evaluates to `T|(F)` which is `T` (1 way)

Thus, the total number of ways to evaluate to true is 2.

## C++ Solution

This is a classic dynamic programming problem, similar in structure to Matrix Chain Multiplication. We need to find the number of ways a subexpression `S[i...j]` can evaluate to `True` and `False`.

**DP Table Definition:**

*   `dp[i][j][0]` stores the number of ways the subexpression `S[i...j]` evaluates to `False`.
*   `dp[i][j][1]` stores the number of ways the subexpression `S[i...j]` evaluates to `True`.
*   `mod = 1003`: The modulus for calculations.

**`solve(string& S, int i, int j, char target_char)` function (Recursive with Memoization):**

*   **Parameters:**
    *   `S`: The boolean expression string.
    *   `i`, `j`: Start and end indices (inclusive) of the current subexpression `S[i...j]`.
    *   `target_char`: The desired evaluation result (`'T'` for True, `'F'` for False).
*   **Base Cases:**
    1.  **Invalid Range:** If `i > j`, the range is invalid. Return `0` ways.
    2.  **Single Literal:** If `i == j`, it's a single boolean literal (`T` or `F`).
        *   If `S[i]` matches `target_char`, there is `1` way.
        *   Otherwise, there are `0` ways.
        *   Memoize this result in `dp[i][j][target_char == 'T']` and return.
*   **Memoization Check:**
    *   If `dp[i][j][target_char == 'T']` is already computed (`!= -1`), return its stored value.
*   **Recursive Step:**
    1.  Initialize `ans = 0` (total ways for current state).
    2.  Iterate through all possible operators to split the expression. In the input string `S`, operands are at even indices (`0, 2, 4, ...`) and operators are at odd indices (`1, 3, 5, ...`). So, `k_op_idx` iterates from `i+1` up to `j-1` with a step of 2.
    3.  For each operator `op = S[k_op_idx]`:
        *   Recursively calculate `left_true`, `left_false` for the left subexpression `S[i...k_op_idx-1]`.
        *   Recursively calculate `right_true`, `right_false` for the right subexpression `S[k_op_idx+1...j]`.
        *   Based on `op` and `target_char`, sum up the ways:
            *   **`op == '|'` (OR):**
                *   If `target_char == 'T'`: `(Left True AND Right True) + (Left True AND Right False) + (Left False AND Right True)`
                *   If `target_char == 'F'`: `(Left False AND Right False)`
            *   **`op == '&'` (AND):**
                *   If `target_char == 'T'`: `(Left True AND Right True)`
                *   If `target_char == 'F'`: `(Left True AND Right False) + (Left False AND Right True) + (Left False AND Right False)`
            *   **`op == '^'` (XOR):**
                *   If `target_char == 'T'`: `(Left True AND Right False) + (Left False AND Right True)`
                *   If `target_char == 'F'`: `(Left True AND Right True) + (Left False AND Right False)`
        *   All intermediate sums are taken modulo `mod` to prevent overflow.
    4.  Memoize and return `ans`.

**`countWays(int N, string S)` function (Main Entry Point):**

*   Initializes the `dp` table with `-1`.
*   Calls `solve(S, 0, N - 1, 'T')` to find the number of ways the entire expression evaluates to `true`.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // Not directly used but generally useful
#include <string>    // For std::string
#include <cstring>   // For memset
#include <algorithm> // For std::max, std::min

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution{
public:
    // dp[i][j][0] stores ways S[i...j] evaluates to False
    // dp[i][j][1] stores ways S[i...j] evaluates to True
    // Size 205 is chosen based on typical problem constraints (N <= 200).
    int dp[205][205][2];
    int mod = 1003; // Modulus for calculations
    
    // Recursive function with memoization to find the number of ways a subexpression
    // S[i...j] can evaluate to target_char ('T' or 'F').
    int solve(std::string& S, int i, int j, char target_char)
    {
        // Base Case 1: If the range is invalid (start index > end index)
        if(i > j){return 0;}

        // Convert target_char to a 0/1 index for the DP table (0 for False, 1 for True)
        int target_bool_idx = (target_char == 'T');

        // Memoization check: If result for this state is already computed, return it.
        if(dp[i][j][target_bool_idx] != -1){
            return dp[i][j][target_bool_idx];
        }

        // Base Case 2: If it's a single literal (operand, i.e., i == j)
        if(i == j)
        {
            // If the literal matches the target character, there's 1 way.
            // Otherwise, 0 ways.
            dp[i][j][target_bool_idx] = (S[i] == target_char); // 1 if match, 0 otherwise
            return dp[i][j][target_bool_idx];
        }
        
        long long total_ways = 0; // Use long long for intermediate sums to prevent overflow before modulo
        
        // Iterate through all possible operators to split the expression.
        // Operators are at odd indices (relative to the start of the entire expression).
        // In a subexpression S[i...j], operators are at i+1, i+3, ... k_op_idx.
        for(int k_op_idx = i + 1; k_op_idx < j; k_op_idx += 2)
        {
            char op = S[k_op_idx]; // Current operator
            
            // Recursively calculate ways for left and right subexpressions to be True/False.
            // Note: solve() will memoize these values, so no redundant calculations.
            int left_true = solve(S, i, k_op_idx - 1, 'T');
            int left_false = solve(S, i, k_op_idx - 1, 'F');
            
            int right_true = solve(S, k_op_idx + 1, j, 'T');
            int right_false = solve(S, k_op_idx + 1, j, 'F');
            
            // Apply operator logic based on the operator 'op' and the desired 'target_char'
            if(op == '|') { // OR operator
                if(target_char == 'T') {
                    // Ways to get True: (T|T) + (T|F) + (F|T)
                    total_ways = (total_ways + (1LL * left_true * right_true) % mod) % mod;
                    total_ways = (total_ways + (1LL * left_true * right_false) % mod) % mod;
                    total_ways = (total_ways + (1LL * left_false * right_true) % mod) % mod;
                }
                else { // Ways to get False: (F|F)
                    total_ways = (total_ways + (1LL * left_false * right_false) % mod) % mod;
                }
            }
            else if(op == '&') { // AND operator
                if(target_char == 'T') {
                    // Ways to get True: (T&T)
                    total_ways = (total_ways + (1LL * left_true * right_true) % mod) % mod;
                }
                else { // Ways to get False: (T&F) + (F&T) + (F&F)
                    total_ways = (total_ways + (1LL * left_true * right_false) % mod) % mod;
                    total_ways = (total_ways + (1LL * left_false * right_true) % mod) % mod;
                    total_ways = (total_ways + (1LL * left_false * right_false) % mod) % mod;
                }
            }
            else if(op == '^') { // XOR operator
                if(target_char == 'T') {
                    // Ways to get True: (T^F) + (F^T)
                    total_ways = (total_ways + (1LL * left_true * right_false) % mod) % mod;
                    total_ways = (total_ways + (1LL * left_false * right_true) % mod) % mod;
                }
                else { // Ways to get False: (T^T) + (F^F)
                    total_ways = (total_ways + (1LL * left_true * right_true) % mod) % mod;
                    total_ways = (total_ways + (1LL * left_false * right_false) % mod) % mod;
                }
            }
        }
        
        // Memoize and return the computed total ways for this state.
        return dp[i][j][target_bool_idx] = total_ways; 
    }
    
    // Main function to count ways to evaluate the expression to True.
    int countWays(int N, std::string S){
        // Initialize DP table with -1 to indicate uncomputed states.
        // Use memset for efficiency on primitive arrays.
        std::memset(dp, -1, sizeof(dp));
        // Call solve for the entire expression S[0...N-1] to evaluate to True.
        return solve(S, 0, N - 1, 'T');
    }
};

// Driver Code (provided by the problem platform)
int main(){
    // Fast I/O setup
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t; // Number of test cases
    while(t--){
        int N;
        std::cin >> N;
        std::string S;
        std::cin >> S; // The boolean expression string
        
        Solution ob;
        std::cout << ob.countWays(N, S) << "\n"; // Output the count of ways
    }
    return 0;
}
```