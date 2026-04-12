# Matrix Chain Multiplication (Dynamic Programming)

## Problem Description

Given a sequence of matrices, we need to find the most efficient way to multiply these matrices. The problem is not about actual matrix multiplication, but about determining the order in which to perform the multiplications. Matrix multiplication is associative, meaning the order in which matrices are multiplied does not affect the final product, but it does affect the number of scalar multiplications required.

For a chain of `N` matrices `A_1, A_2, ..., A_N`, where matrix `A_i` has dimensions `p_{i-1} x p_i`, the problem is to find a parenthesization that minimizes the total number of scalar multiplications.

## C++ Solution

This C++ solution uses dynamic programming with memoization to solve the Matrix Chain Multiplication problem.

**Input Array `arr`:**

The input `arr` contains the dimensions of the matrices. If there are `N` matrices `A_1, ..., A_N`, then `arr` will have `N+1` elements. `arr[i-1]` and `arr[i]` represent the dimensions of matrix `A_i` as `arr[i-1] x arr[i]`.

**`dp[105][105]` table:**

*   A 2D array `dp` is used for memoization. `dp[i][j]` stores the minimum number of scalar multiplications needed to multiply the matrix chain from `arr[i-1]` to `arr[j]` (i.e., matrices `A_i` through `A_j`).
*   Initialized with `-1` (or any value indicating not computed) using `memset`.

**`solve(int *arr, int i, int j)` function (Recursive with Memoization):**

*   **Parameters:**
    *   `arr`: The array of matrix dimensions.
    *   `i`: Starting index of the matrices in the chain (1-based index for `A_i`).
    *   `j`: Ending index of the matrices in the chain (1-based index for `A_j`).
*   **Base Case:**
    *   If `i >= j`, it means there is only one matrix or no matrices, so no multiplication is needed. Return `0`.
*   **Memoization Check:**
    *   If `dp[i][j]` is already computed (`>= 0`), return its stored value.
*   **Recursive Step:**
    1.  Initialize `ans = INT_MAX` (to find the minimum).
    2.  Iterate `k` from `i` to `j-1`. `k` represents the split point where the matrix chain `(A_i ... A_j)` is divided into two sub-chains `(A_i ... A_k)` and `(A_{k+1} ... A_j)`.
    3.  For each `k`, calculate the cost:
        *   `cost = solve(arr, i, k)`: Cost to multiply `(A_i ... A_k)`.
        *   `cost += solve(arr, k+1, j)`: Cost to multiply `(A_{k+1} ... A_j)`.
        *   `cost += arr[i-1] * arr[k] * arr[j]`: Cost to multiply the two resulting matrices (one with dimensions `arr[i-1] x arr[k]`, and the other with `arr[k] x arr[j]`).
    4.  Update `ans = min(ans, cost)`.
*   Store the computed `ans` in `dp[i][j]` and return it.

**`matrixMultiplication(int N, int arr[])` function:**

*   **Parameters:**
    *   `N`: The number of matrices (or `N+1` is the size of the `arr` array, where `arr` contains dimensions). The problem states `N` is the number of matrices, so `arr` has `N+1` elements for `N` matrices.
    *   `arr[]`: The array of dimensions.
*   **Logic:**
    1.  Initialize the `dp` table with `-1` using `memset`.
    2.  Call `solve(arr, 1, N-1)` to find the minimum multiplications for the chain of `N` matrices (from `A_1` to `A_N`). Note the indices are adjusted for 1-based matrix indexing if `arr` is 0-indexed for dimensions.

```cpp
#include <bits/stdc++.h> // Includes most standard libraries
#include <vector>        // For std::vector (though raw arrays are used in example)
#include <algorithm>     // For std::min
#include <cstring>       // For memset
#include <limits>        // For INT_MAX

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution{
public:
    // DP table for memoization. dp[i][j] stores the minimum scalar multiplications for matrices A_i to A_j.
    int dp[105][105];

    // Recursive function with memoization to find the minimum scalar multiplications.
    // arr: array of matrix dimensions (e.g., arr[0]xarr[1] for A1, arr[1]xarr[2] for A2, etc.)
    // i: starting index of the matrices in the chain (1-based index, corresponding to arr[i-1])
    // j: ending index of the matrices in the chain (1-based index, corresponding to arr[j])
    int solve(int *arr, int i, int j)
    {
        // Base case: If i >= j, there is only one matrix or no matrices, so no multiplication is needed.
        if(i >= j){return 0;}
        
        // Memoization check: If the result for dp[i][j] is already computed, return it.
        if(dp[i][j] != -1){ // Using -1 as an uncomputed marker
            return dp[i][j];
        }
        
        int min_cost = std::numeric_limits<int>::max(); // Initialize with maximum possible integer value
        
        // Iterate through all possible split points k
        // The chain (A_i ... A_j) is split into (A_i ... A_k) and (A_{k+1} ... A_j)
        for(int k = i; k <= (j - 1); k++)
        {
            // Calculate cost for current split point:
            // 1. Cost to multiply (A_i ... A_k)
            // 2. Cost to multiply (A_{k+1} ... A_j)
            // 3. Cost to multiply the two resulting matrices (dimensions: arr[i-1]xarr[k] and arr[k]xarr[j])
            int current_cost = solve(arr, i, k) +               // Cost for left sub-chain
                               solve(arr, k + 1, j) +            // Cost for right sub-chain
                               (arr[i-1] * arr[k] * arr[j]);    // Cost to multiply the two resulting matrices
            
            min_cost = std::min(min_cost, current_cost); // Update overall minimum cost
        }
        
        dp[i][j] = min_cost; // Store the computed minimum cost in the DP table
        
        return min_cost; // Return the minimum cost
    }
    
    // Main function to calculate the minimum scalar multiplications for matrix chain.
    // N: Number of matrices (so arr has N+1 elements)
    // arr[]: array of dimensions where arr[k] is the k-th dimension.
    int matrixMultiplication(int N, int arr[])
    {
        // Initialize DP table with -1 to indicate uncomputed states
        std::memset(dp, -1, sizeof(dp));
        // Call solve for the entire chain of N matrices (from 1st matrix to Nth matrix).
        // The dimensions for matrix A_x are arr[x-1] x arr[x].
        // For N matrices, the chain is A_1...A_N, with dimensions arr[0]...arr[N].
        // So, we need to consider matrices from index 1 to N-1 (representing A_1 to A_{N-1} products).
        return solve(arr, 1, N - 1);
    }
};

// Driver Code (provided by the problem platform)
int main(){
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t; // Number of test cases
    while(t--){
        int N;
        std::cin >> N; // Number of matrices
        int arr[N];    // Dimensions array (size N+1 is expected for N matrices)
        for(int i = 0; i < N; i++)
            std::cin >> arr[i];
        
        Solution ob;
        std::cout << ob.matrixMultiplication(N, arr) << std::endl; // Output the result
    }
    return 0;
}
```