# Minimum Unfairness (DP with Bitmask) - Fair Distribution of Cookies

## Problem Description

This problem is equivalent to [Fair Distribution of Cookies on LeetCode](https://leetcode.com/problems/fair-distribution-of-cookies/).

You are given an integer array `cookies` of length `n`, where `cookies[i]` denotes the number of cookies in the `i`-th bag. You are also given an integer `k` which denotes the number of children.

You want to distribute all the `n` cookie bags among the `k` children such that each child receives at least one bag (though this is often not a strict constraint in similar problems, the primary goal is fair distribution). The **unfairness** of a distribution is defined as the maximum total cookies received by any child.

Your task is to return the minimum unfairness of all distributions.

## C++ Solution

This problem can be solved using dynamic programming with bitmasking. The state `dp[mask][k]` represents the minimum possible maximum sum of cookies among `k` children, given that the cookies represented by the `mask` have been distributed.

*   `mask`: A bitmask where the `i`-th bit is set if the `i`-th cookie bag has been distributed.
*   `k`: The number of children remaining to distribute cookies to.

**`maskSum` Array:**
Before starting the DP, `maskSum[mask]` is precomputed. It stores the total sum of cookies for all cookie bags represented by the `mask`.

**`find(mask, dp, maskSum, k)` Function:**
*   **Base Cases:**
    *   If `k=1`, it means there's only one child left. This child must take all remaining cookies in `mask`. So, `dp[mask][1] = maskSum[mask]`.
*   **Recursive Step:**
    *   Iterate through all `submask`s of the current `mask`. `submask` represents the cookies given to the current child.
    *   For each `submask`, the current child receives `maskSum[submask]` cookies.
    *   The remaining `k-1` children need to distribute the remaining cookies (`mask ^ submask`). The minimum unfairness for this subproblem is found by `find(mask ^ submask, dp, maskSum, k-1)`.
    *   The unfairness for this particular distribution (current child gets `submask`, others get `mask ^ submask`) is `max(maskSum[submask], find(mask ^ submask, dp, maskSum, k-1))`.
    *   `dp[mask][k]` is updated with the minimum of these unfairness values found by trying all possible `submask`s.

```cpp
#include <vector>
#include <numeric>
#include <algorithm>
#include <climits> // For INT_MAX

class Solution {
public:
    // dp[mask][k] stores the minimum possible maximum sum (unfairness)
    // when cookies represented by 'mask' are distributed among 'k' children.
    std::vector<std::vector<int>> memo_dp; // Renamed dp to memo_dp to avoid conflict with function parameter
    std::vector<int> maskSum;

    int find(int mask, int k)
    {
        // Base case: If no cookies left to distribute or no children left
        // (though in problem constraints, mask will typically be > 0 if k > 0)
        if (mask == 0) return 0; // If no cookies, unfairness is 0
        
        // Base case: If only one child is left, this child takes all remaining cookies in 'mask'
        if (k == 1)
        {
            return maskSum[mask];
        }

        // If this state has been computed before, return the memoized result
        if(memo_dp[mask][k] != INT_MAX)
        {
            return memo_dp[mask][k];
        }

        int min_unfairness = INT_MAX;

        // Iterate through all possible submasks of the current mask.
        // Each submask represents the set of cookies given to one child.
        for(int submask = mask; submask > 0; submask = (submask - 1) & mask)
        {
            // Calculate the unfairness if the current child gets 'submask' cookies
            // and the remaining k-1 children distribute 'mask ^ submask' cookies.
            min_unfairness = std::min(
                min_unfairness, 
                std::max(
                    maskSum[submask], // Cookies for the current child
                    find(mask ^ submask, k - 1) // Min unfairness for remaining children
                )
            );
        }

        return memo_dp[mask][k] = min_unfairness;
    }

    int distributeCookies(std::vector<int>& cookies, int k) 
    {
        int n = cookies.size();
        int total_masks = (1 << n); // Total number of possible masks (2^n)

        maskSum.resize(total_masks); // Resize maskSum array
        // Precompute sum of cookies for each mask
        for(int mask = 0; mask < total_masks; mask++){
            int total = 0;
            for(int i = 0; i < n; i++){
                if(mask & (1 << i)){
                    total += cookies[i];
                }
            }
            maskSum[mask] = total;
        }

        // Initialize DP table with INT_MAX. memo_dp[mask][k]
        // The dimensions for dp should be total_masks by k+1
        memo_dp.assign(total_masks, std::vector<int>(k + 1, INT_MAX));

        // The problem asks for distributing all cookies, so the initial mask is (1<<n) - 1
        // which means all cookies are included.
        return find((1 << n) - 1, k);
    }
};
```
