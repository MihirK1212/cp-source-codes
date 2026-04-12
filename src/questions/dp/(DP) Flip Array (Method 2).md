# Flip Array (Method 2) - Minimum Elements to Flip for Half Sum

## Problem Description

Given an array `A` of `n` positive integers, you are allowed to flip the sign of any number in the array (change `x` to `-x`). The goal is to find the minimum number of elements you need to flip such that the sum of the modified array is non-negative and as small as possible.

This is a classic variation of the knapsack or subset sum problem. We want to find a subset of numbers to flip (make negative) such that:
1.  The sum of these flipped numbers (`S_flipped`) is as large as possible, but not exceeding `TotalSum / 2`, where `TotalSum` is the sum of all elements in the original array. This ensures the final array sum `(TotalSum - 2 * S_flipped)` is non-negative and minimized.
2.  Among all such subsets that maximize `S_flipped` (while `S_flipped <= TotalSum / 2`), we want the one that uses the *minimum number of elements*.

## C++ Solution

This solution uses dynamic programming to solve the problem. The core idea is to find, for each possible sum up to `TotalSum / 2`, the minimum number of elements required to achieve that sum.

**`min_required(weights, target_sum, n)` function:**
*   `weights`: The input array `A` (elements are treated as "weights" or "values" in a knapsack context).
*   `target_sum`: The maximum sum we are trying to achieve with the flipped elements, which is `TotalSum / 2`.
*   `n`: The number of elements in the `weights` array.

**`dp[w][i]` state:**
*   `dp[w][i]` stores the *minimum number of elements* from `weights[0...i-1]` that sum up to `w`.
*   Initialization:
    *   `dp[0][j] = 0` for all `j` (0 elements are needed to achieve a sum of 0).
    *   `dp[w][0] = 1e7` (a very large number, representing infinity) for `w > 0` (impossible to achieve a positive sum with 0 elements).

**Recurrence Relation:**
For each `dp[w][i]` (considering `weights[i-1]`):
1.  **Include `weights[i-1]`:** If `w >= weights[i-1]`, we can potentially include `weights[i-1]`. The number of elements used would be `dp[w - weights[i-1]][i-1] + 1`.
2.  **Exclude `weights[i-1]`:** We don't include `weights[i-1]`. The number of elements used would be `dp[w][i-1]`.
`dp[w][i] = min( (include_case), (exclude_case) )`

After filling the `dp` table:
We iterate backward from `target_sum` down to `0`. The first `w_achieved` encountered for which `dp[w_achieved][n]` is not `1e7` is the largest sum `<= target_sum` that can be formed using a subset of elements with the minimum possible count. This `dp[w_achieved][n]` value is our answer.

```cpp
int min_required(const vector<int>&weight,int W,int n)
{
    // dp[w][i] stores the minimum number of elements to achieve sum 'w' using first 'i' elements.
    int dp[W+1][n+1];

    for(int w=0;w<=W;w++)
    {
        for(int i=0;i<=n;i++)
        {
            if(w==0) // Base case: 0 elements to make sum 0
            {
                dp[w][i] = 0;
            }
            else if(i==0) // Base case: cannot make positive sum with 0 items
            {
                dp[w][i] = 1e7; // Represents infinity
            }
            else
            {
                int val_if_included = 1e7;
                // If current weight (weight[i-1]) can be included
                if(w >= weight[i-1]) {
                    // Cost is 1 (for current item) + min items for remaining capacity
                    val_if_included = dp[w - weight[i-1]][i-1] + 1;
                }
                
                // Value if current item (weight[i-1]) is excluded
                int val_if_excluded = dp[w][i-1];

                dp[w][i] = min(val_if_included, val_if_excluded);
            }
        }
    }
    
    // Find the largest sum `w_achieved` (<= W) that can be formed
    // with the minimum number of elements.
    for(int w_achieved=W; w_achieved>=0; w_achieved--)
    {
        if(dp[w_achieved][n] != 1e7){
            return dp[w_achieved][n];
        }
    }

    return 0; // Should not be reached for valid inputs.
}

int Solution::solve(const vector<int> &A) 
{
    int n = A.size();

    int total_sum = 0;
    for(auto x : A){total_sum+=x;}
    
    // The target sum for the subset of flipped elements should be `total_sum / 2`.
    // We want to find a subset that sums up to `S_flipped` such that `S_flipped <= total_sum / 2`
    // and `S_flipped` is maximized, while minimizing the count of elements in that subset.
    // The `min_required` function directly gives this minimum count for the largest achievable sum `w_achieved <= total_sum / 2`.
    
    return min_required(A,total_sum/2,n);
}
```