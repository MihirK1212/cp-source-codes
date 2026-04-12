# Target Subset Sum (Dynamic Programming)

## Problem Description

Given an integer array `nums` and an integer `target`, you want to build an expression out of `nums` by adding one of the symbols `'+'` or `'-'` before each integer in `nums` and then concatenate all the integers. Return the number of different expressions that you can build, which evaluates to `target`.

This problem can be transformed into a subset sum problem. Let `P` be the set of elements in `nums` that are assigned a `'+'` sign, and `N` be the set of elements in `nums` that are assigned a `'-'` sign. The sum of elements with a `'+'` sign is `sum(P)`, and the sum of elements with a `'-'` sign is `sum(N)`.

We have two equations:
1.  `sum(P) - sum(N) = target` (Given problem statement)
2.  `sum(P) + sum(N) = total_sum` (Where `total_sum` is the sum of all elements in `nums`)

Adding these two equations gives:
`2 * sum(P) = target + total_sum`
`sum(P) = (target + total_sum) / 2`

The problem then becomes finding the number of subsets of `nums` whose sum is equal to `sum(P)`.

**Constraints:**
*   If `(target + total_sum)` is odd, or if `(target + total_sum)` is negative, it's impossible to form the target sum, so return `0`.

## C++ Solution

This C++ solution uses dynamic programming to count the number of subsets that sum to `sum(P)`. The `dp[i][s]` state represents the number of subsets with sum `s` using the first `i` elements of the array `arr`.

**Algorithm:**

1.  **Calculate Total Sum:** Compute the `total_sum` of all elements in `arr`.
2.  **Check Feasibility:**
    *   If `(total_sum + target)` is odd, return `0`.
    *   If `(total_sum + target)` is negative, return `0`.
    *   Calculate `target_subset_sum = (total_sum + target) / 2`.
    *   If `target_subset_sum` is greater than `total_sum` (meaning `sum(P)` is too large) or negative, return `0`.
3.  **Initialize DP Table:** Create a 2D DP table `dp` of size `(n+1) x (target_subset_sum + 1)`, initialized with zeros.
    *   `dp[0][0] = 1`: There is one way to achieve a sum of 0 with 0 elements (by choosing an empty set).
4.  **Populate DP Table:** Iterate `i` from `1` to `n` (representing the number of elements considered) and `s` from `0` to `target_subset_sum` (representing the current sum):
    *   **Option 1: Exclude `arr[i-1]` (current element):** `dp[i][s] += dp[i-1][s];` (Number of ways without including the current element).
    *   **Option 2: Include `arr[i-1]` (current element):** If `s >= arr[i-1]`, then `dp[i][s] += dp[i-1][s - arr[i-1]];` (Number of ways by including the current element and reducing the target sum).
    *   `dp[i][s]` will be the sum of these two options.
5.  **Return Result:** `dp[n][target_subset_sum]` will contain the number of subsets that sum to `target_subset_sum` using all `n` elements.

```cpp
#include <vector>
#include <numeric> // For std::accumulate (if not using manual sum)
#include <cmath>   // For std::abs

class Solution {
public:
    int findTargetSumWays(std::vector<int>& arr, int target) 
    {
        int n = arr.size();
        int sum = 0;
        
        // Calculate total sum of all elements in the array
        for(int x : arr){sum += x;}
        
        // Check for edge cases where a solution is impossible:
        // 1. (sum + target) must be even, because 2*sum(P) = sum + target.
        // 2. (sum + target) must not be negative, because sum(P) cannot be negative.
        if(((sum + target) % 2) != 0 || (sum + target) < 0) {
            return 0;
        }

        // Calculate the target sum for subset P
        int target_subset_sum = (sum + target) / 2;
        
        // If target_subset_sum is greater than the total_sum, it's impossible.
        // Also, if target_subset_sum is negative (already checked above, but as a safeguard).
        if (target_subset_sum < 0 || target_subset_sum > sum) {
            return 0;
        }

        // dp[i][s] = number of subsets with sum 's' using first 'i' elements
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(target_subset_sum + 1, 0));
        
        // Base case: There is one way to get a sum of 0 with 0 elements (empty set).
        dp[0][0] = 1;
        
        // Fill the DP table
        for(int i = 1; i <= n; i++) // Iterate through elements (from 1 to n)
        {
           for(int s = 0; s <= target_subset_sum; s++) // Iterate through possible sums
           {
               // Option 1: Exclude the current element (arr[i-1])
               int count_exclude = dp[i-1][s];
               
               // Option 2: Include the current element (arr[i-1])
               int count_include = 0;
               if(s >= arr[i-1]){
                   count_include = dp[i-1][s - arr[i-1]];
               }
               
               // Total ways for dp[i][s] is the sum of ways from both options
               dp[i][s] = count_exclude + count_include;
           }
        }
        
        return dp[n][target_subset_sum];
    }
};
```