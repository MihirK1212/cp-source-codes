# Divide Array into K Subsets of Equal Sum (DP with Bitmask)

## Problem Description

Given an integer array `A` and an integer `k`, determine if it's possible to divide the array into `k` non-empty subsets such that the sum of elements in each subset is equal.

## C++ Solution

This problem can be solved using dynamic programming with bitmasking. The state `dp[mask]` stores whether the elements represented by the `mask` can be partitioned into `(number of set bits in mask) / (subset_size)` subsets of equal sum. However, a more direct approach is to check if we can form `k` subsets, each summing to `total_sum / k`.

The `find` function recursively attempts to form these subsets:

*   **`find(A, k, subset, currSum, reqSum, dp)`:**
    *   `A`: The input array of integers.
    *   `k`: The number of subsets still needed to form.
    *   `subset`: A bitmask representing the elements *remaining* to be distributed.
    *   `currSum`: The current sum of the subset being built.
    *   `reqSum`: The target sum for each subset (`total_sum / k`).
    *   `dp`: A memoization table to store results for `dp[subset]`.

**Logic:**

1.  **Base Cases:**
    *   If `k <= 1`: All `k-1` subsets have been successfully formed, so return `true`.
    *   If `subset == 0`: No elements left to distribute, but `k > 1`, so return `false`.
    *   If `dp[subset]` is already computed, return the memoized value.
2.  **Recursive Step:**
    *   Iterate through the elements of `A` using the `j` index.
    *   If element `A[j]` is *not* included in the current `subset` (i.e., `!(subset & (1 << j))`), skip it.
    *   If `currSum + A[j]` exceeds `reqSum`, break (since the array `A` is sorted, further elements will also exceed the sum).
    *   **If `currSum + A[j] == reqSum`:**
        *   This means we've successfully formed one subset.
        *   Remove `A[j]` from `subset` (`subset ^ (1 << j)`).
        *   Recursively call `find` to form `k-1` more subsets, starting a new subset (`currSum = 0`).
        *   If the recursive call returns `true`, then `ans = true`.
        *   Backtrack: re-add `A[j]` to `subset`.
    *   **If `currSum + A[j] < reqSum`:**
        *   Add `A[j]` to the current subset being built.
        *   Remove `A[j]` from `subset`.
        *   Recursively call `find` to continue building the current subset (same `k`, updated `currSum`).
        *   If the recursive call returns `true`, then `ans = true`.
        *   Backtrack: re-add `A[j]` to `subset`.
3.  **Memoization:** Store `ans` in `dp[subset]` before returning.

The `canPartitionKSubsets` function first calculates the total sum of the array. If the total sum is not divisible by `k`, it's impossible to form `k` subsets of equal sum. Otherwise, it sorts the array (which helps in pruning search space) and initializes the DP table, then calls the `find` function.

```cpp
class Solution {
public:
    // dp[mask] will store if the elements represented by 'mask' can be partitioned
    // into subsets with sum 'reqSum' until 'k' subsets are formed.
    // However, the 'dp' here is more about whether the *remaining* elements can be partitioned.
    bool find(vector<int>&A,int k,int subset,int currSum,int reqSum,vector<int>&dp)
    {
        // Base case: If we need to form 1 or fewer subsets, it means we have successfully partitioned.
        if(k<=1){return true;} 
        
        // Base case: If there are no elements left in 'subset' but we still need more subsets, it's impossible.
        if(subset==0){return false;} 
        
        // Memoization: If result for this 'subset' mask is already computed, return it.
        // dp stores -1 for uncomputed, 0 for false, 1 for true.
        if(dp[subset]!=-1){return dp[subset]==1;} 
        
        int n = A.size();
        
        bool ans = false;
        
        // Iterate through elements of A
        for(int j=0;j<n && !ans;j++) // Optimization: '&& !ans' to short-circuit if a solution is found
        {
            // If the j-th element is not part of the current 'subset' (already used), skip it.
            if(!(subset&(1<<j))){continue;}
            
            // Optimization: If adding A[j] exceeds the required subset sum,
            // and array is sorted, then further elements will also exceed.
            if((currSum+A[j])>reqSum){break;} 
            
            if((currSum+A[j])==reqSum) // Found a complete subset
            {
                // Temporarily remove A[j] from 'subset'
                subset^=(1<<j); 
                // Recursively try to form k-1 more subsets, starting a new subset (currSum=0)
                ans = find(A,k-1,subset,0,reqSum,dp);
                // Backtrack: add A[j] back to 'subset' for other possibilities
                subset^=(1<<j); 
            }
            else // Continue building the current subset
            {
                // Temporarily remove A[j] from 'subset'
                subset^=(1<<j); 
                // Recursively try to complete the current subset
                ans = find(A,k,subset,currSum+A[j],reqSum,dp);
                // Backtrack: add A[j] back to 'subset'
                subset^=(1<<j); 
            }
        }
        
        // Store and return the result for this 'subset' mask
        dp[subset] = ans ? 1 : 0; 
        return ans;
    }

    bool canPartitionKSubsets(vector<int>& A, int k) 
    {
        int n = A.size();
        
        // Sort the array. This is crucial for the pruning optimization (break condition in for loop).
        sort(A.begin(),A.end()); 
        
        int total_sum = 0;
        for(auto x : A){total_sum+=x;}
        
        // If total sum is not divisible by k, it's impossible.
        if(total_sum % k != 0){return false;} 
        
        int reqSum = total_sum / k; // The target sum for each subset
        
        // `subset` is the initial mask with all bits set, representing all elements available.
        int initial_mask = (1 << n) - 1; 
        
        // Initialize DP table with -1 (uncomputed state).
        // Size of DP table is 2^n.
        vector<int> dp(initial_mask + 1,-1); 
        
        // Start the recursive process: try to form 'k' subsets from all elements.
        return find(A,k,initial_mask,0,reqSum,dp);
    }
};
```
