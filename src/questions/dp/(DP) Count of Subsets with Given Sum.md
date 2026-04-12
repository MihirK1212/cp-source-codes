# Count of Subsets with Given Sum (Dynamic Programming)

## Problem Description

Given a set of `n` non-negative integers `arr` and a target `sum`, the task is to find the number of subsets of the given set whose elements sum up to the target `sum`.

This is a classic dynamic programming problem, a variation of the Subset Sum problem.

## C++ Solution

This C++ solution uses a 2D dynamic programming table to count the number of subsets with a given sum. The `dp[i][s]` entry in the table stores the number of subsets from the first `i` elements that sum up to `s`.

**DP Table Definition:**

*   `dp[i][s]` = Number of subsets using the first `i` elements (`arr[0...i-1]`) that sum up to `s`.

**Dimensions:**

*   The DP table will have `(n+1)` rows and `(sum+1)` columns, where `n` is the number of elements in the input array `arr` and `sum` is the target sum.

**Initialization (Base Cases):**

*   `dp[0][0] = 1`: There is one way to achieve a sum of 0 using 0 elements (by choosing an empty set).
*   `dp[0][s] = 0` for `s > 0`: It is not possible to achieve any positive sum with 0 elements.

**Recurrence Relation:**

For `dp[i][s]`, there are two possibilities for the `i`-th element (which is `arr[i-1]` in 0-indexed array):

1.  **Exclude the `i`-th element (`arr[i-1]`):** If we don't include `arr[i-1]`, the number of ways to achieve sum `s` is `dp[i-1][s]`. (`v2 = dp[i-1][s]`).
2.  **Include the `i`-th element (`arr[i-1]`):** If we include `arr[i-1]`, then we need to achieve the remaining sum `(s - arr[i-1])` using the first `i-1` elements. This is possible if `s >= arr[i-1]`, and the number of ways is `dp[i-1][s - arr[i-1]]`. (`v1 = dp[i-1][s - arr[i-1]]`).

Therefore, `dp[i][s] = v1 + v2` (summing the ways from both possibilities).

**Final Answer:**

The final answer is `dp[n][sum]`, which represents the total number of subsets from all `n` elements that sum up to the target `sum`.

```cpp
#include <vector>    // Required for std::vector
#include <cstring>   // Required for memset
#include <algorithm> // Not explicitly used but generally useful

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution{
public:
    // Function to count the number of subsets with a given sum.
    // arr: The input array of non-negative integers.
    // n: The number of elements in the array.
    // sum: The target sum.
    int perfectSum(int arr[], int n, int sum)
    {
        // dp[i][s] = number of subsets with sum 's' using first 'i' elements.
        // Dimensions: (n+1) rows, (sum+1) columns.
        int dp[n+1][sum+1];
        int i, s;
        
        // Initialize dp table with 0s.
        std::memset(dp, 0, sizeof(dp));
        
        // Fill the DP table
        for(i = 0; i <= n; i++)
        {
            for(s = 0; s <= sum; s++)
            {
                if(i == 0) // Base case: 0 elements considered
                {
                    if(s == 0){dp[i][s] = 1;} // One way to get sum 0 (empty set)
                    else{dp[i][s] = 0;}   // No way to get positive sum with 0 elements
                }
                else // For i > 0 elements
                {
                    int ways_with_current_element = 0;
                    // Option 1: Include the current element (arr[i-1])
                    // If current sum 's' is greater than or equal to arr[i-1],
                    // add ways from dp[i-1][s - arr[i-1]].
                    if(s >= arr[i-1]){
                        ways_with_current_element = dp[i-1][s - arr[i-1]];
                    }
                    
                    // Option 2: Exclude the current element (arr[i-1])
                    // Add ways from dp[i-1][s].
                    int ways_without_current_element = dp[i-1][s];
                
                    // Total ways for dp[i][s] is the sum of ways from both options.
                    dp[i][s] = ways_with_current_element + ways_without_current_element;
                }
            }
        }
        
        return (dp[n][sum]); // The result is the number of subsets using all 'n' elements that sum to 'sum'.
    }
};
```