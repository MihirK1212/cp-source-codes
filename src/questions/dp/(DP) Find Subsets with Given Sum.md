# Find Subsets with Given Sum (DP)

## Problem Description

Given an array of integers `arr` and a `target_sum`, this problem asks to find if there exists a subset of `arr` whose elements sum up to `target_sum`. If such a subset exists, the problem also aims to print all such subsets. This is a classic dynamic programming problem, often referred to as the **Subset Sum Problem**.

## C++ Solution

The solution involves two main parts:

1.  **Dynamic Programming (DP) for Reachability:** A 2D boolean `dp` table is used to determine if a particular sum is achievable using a subset of the first `i` elements of the array. `dp[i][s]` is `true` if a sum `s` can be formed using elements from `arr[0...i-1]`, and `false` otherwise.
2.  **Recursive Backtracking for Reconstruction:** If `dp[n][target_sum]` is `true`, a recursive function `find_subsets` is used to backtrack through the `dp` table and reconstruct all possible subsets that sum up to `target_sum`.

**DP Table (`dp[i][s]`):**

*   `i`: Represents considering the first `i` elements of the `arr`.
*   `s`: Represents the target sum.
*   **Initialization:**
    *   `dp[0][0] = true`: An empty set can achieve a sum of 0.
    *   `dp[0][s] = false` for `s > 0`: No elements can achieve a non-zero sum.
*   **Recurrence Relation (for `i > 0` and `s >= 0`):**
    *   `dp[i][s] = dp[i-1][s]` (Case: Do not include `arr[i-1]`) 
        *OR*
    *   `dp[i-1][s - arr[i-1]]` (Case: Include `arr[i-1]`, if `s >= arr[i-1]`)

**`find_subsets(int* arr, int i, int s, std::vector<int>& ss)` Function (Backtracking):**

*   **Parameters:**
    *   `arr`: The input array.
    *   `i`: The current index in the array (representing `arr[i-1]` as the current element being considered from the end).
    *   `s`: The remaining sum to achieve.
    *   `ss`: The current subset being built.
*   **Base Case:**
    *   If `i == 0` and `s == 0`, a valid subset `ss` has been found. Print it.
*   **Recursive Steps:**
    1.  **Option 1 (Exclude `arr[i-1]`):** If `i >= 1` and `dp[i-1][s]` is `true` (meaning `s` can be formed without `arr[i-1]`),
        *   Recursively call `find_subsets(arr, i-1, s, ss)`. A temporary copy `tmp` of `ss` is made to ensure separate paths in the recursion tree.
    2.  **Option 2 (Include `arr[i-1]`):** If `i >= 1`, `s >= arr[i-1]`, and `dp[i-1][s - arr[i-1]]` is `true` (meaning `s - arr[i-1]` can be formed without `arr[i-1]`),
        *   Add `arr[i-1]` to `ss`.
        *   Recursively call `find_subsets(arr, i-1, s - arr[i-1], ss)`.

```cpp
#include <iostream>   // For std::cin, std::cout
#include <vector>     // For std::vector
#include <numeric>    // For std::accumulate (optional, for total sum)
#include <algorithm>  // For std::sort, std::reverse
#include <limits>     // For std::numeric_limits
#include <cstring>    // For memset (though not used in final code, for general DP initialization)

// Commonly used in competitive programming for brevity, but explicit std:: is more robust
// using namespace std;

// DP table to store if a sum 's' is possible using first 'i' elements.
// Max array size and max sum can be up to 1000, so a 1001x1001 table.
bool dp[1001][1001]; 

// Helper function to print a subset
void display(std::vector<int>& ss)
{
    for(int i = 0; i < ss.size(); i++){
        std::cout << ss[i] << " ";
    }
    std::cout << "\n";
    return;
}

// Function to reconstruct and print all subsets that sum to 's'
// arr: The input array (passed as a pointer for C-style arrays)
// i: Current number of elements considered (from 1 to n). Represents arr[i-1].
// s: Remaining target sum
// ss: Current subset being built (passed by reference to modify)
void find_subsets(int* arr, int i, int s, std::vector<int>& ss)
{
    // Base case: If we have considered all elements (i=0) and the remaining sum is 0, 
    // it means a valid subset 'ss' has been found.
    if(i == 0 && s == 0)
    {
        display(ss);
        return;
    }
    
    // Option 1: Do not include arr[i-1] (the current element from the original array).
    // We check if the sum 's' was achievable using elements arr[0...i-2].
    if(i >= 1 && dp[i-1][s]) 
    {
        // Create a temporary copy of the current subset 'ss' to explore this path.
        // This is crucial to prevent modifications to 'ss' affecting other recursive branches.
        std::vector<int> tmp = ss;
        find_subsets(arr, i - 1, s, tmp);
    }
    
    // Option 2: Include arr[i-1] (the current element from the original array).
    // We check if the sum 's - arr[i-1]' was achievable using elements arr[0...i-2].
    // This is only possible if s is greater than or equal to arr[i-1].
    if(i >= 1 && s >= arr[i-1] && dp[i-1][s - arr[i-1]]) 
    {
        // Add arr[i-1] to the current subset 'ss'.
        ss.push_back(arr[i-1]);
        // Recursively call with the updated sum and previous index.
        find_subsets(arr, i - 1, s - arr[i-1], ss);
    }
}

int main()
{
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);
    
    int n, i, target_sum_input; // Using target_sum_input to avoid conflict with 's' in DP loop
    int total_sum = 0;

    std::cin >> n; // Number of elements in the array
    
    // Declare a C-style array for simplicity as used in original code.
    // For production code, std::vector is generally preferred.
    int arr[n]; 
    
    // Read array elements and calculate their total sum (useful for DP table sizing if max sum is not fixed)
    for(i = 0; i < n; i++){
        std::cin >> arr[i]; 
        total_sum += arr[i];
    }
    
    std::cin >> target_sum_input; // The target sum to find subsets for
    
    // DP table filling: `dp[i][s]` is true if sum `s` is possible using first `i` elements.
    // `i` goes from 0 to n, `s` goes from 0 to target_sum_input.

    // Initialize `dp[0][0]` to true (empty set sum is 0).
    dp[0][0] = true;
    // All other `dp[0][s]` for s > 0 are false by default (or explicitly set if using memset).
    for(s = 1; s <= target_sum_input; s++) {
        dp[0][s] = false;
    }

    for(i = 1; i <= n; i++) // Iterate through each element (from arr[0] to arr[n-1])
    {
        for(s = 0; s <= target_sum_input; s++) // Iterate through each possible sum
        {
            bool case_include_curr = false;
            // Case 1: Include arr[i-1] (current element).
            // This is possible if current sum 's' is at least arr[i-1]
            // and (s - arr[i-1]) was achievable using previous (i-1) elements.
            if(s >= arr[i-1]){
                case_include_curr = dp[i-1][s - arr[i-1]];
            }
            
            // Case 2: Exclude arr[i-1] (current element).
            // This is possible if sum 's' was already achievable using previous (i-1) elements.
            bool case_exclude_curr = dp[i-1][s]; 
            
            // Update dp[i][s]: Sum 's' is achievable if either case 1 OR case 2 is true.
            dp[i][s] = case_include_curr || case_exclude_curr;
        }
    }
    
    // Check if the target_sum is achievable using all 'n' elements.
    if(!dp[n][target_sum_input]){
        std::cout << "Not Possible\n";
    }
    else
    {
        std::vector<int> current_subset; // Vector to build subsets
        std::cout << "Subsets with sum " << target_sum_input << ":\n";
        // Call the backtracking function to find and print all subsets
        find_subsets(arr, n, target_sum_input, current_subset);
    }
    
    return 0;
}
```