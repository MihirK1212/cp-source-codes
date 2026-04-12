# (DP) Painting the Walls

## Problem Description

This problem is from LeetCode: [Painting the Walls](https://leetcode.com/problems/painting-the-walls/).

You are given two 0-indexed integer arrays, `cost` and `time`, of size `n`. There are `n` walls to be painted. You are also given `n` painters. Each painter `i` paints the `i`-th wall. The `i`-th painter will take `time[i]` units of time and `cost[i]` units of money to paint the `i`-th wall.

However, a paid painter can also help paint another wall for free. The free painter for the `i`-th paid painter will take `time[i]` units of time, but will paint a wall *for free*. You must paint all `n` walls.

Return the minimum cost to paint all `n` walls.

## C++ Solution

This C++ solution uses dynamic programming to find the minimum cost to paint all `n` walls. The core idea is to transform the problem into a variation of the knapsack problem. For each paid painter `i`, they paint one wall for `cost[i]` and free up `time[i]` units of time, which can be used to paint `time[i]` additional walls for free. Effectively, one paid painter `i` paints `time[i] + 1` walls for `cost[i]`.

Now, the problem becomes: from the given `n` items (where each item `i` has a "value" of `time[i] + 1` walls painted and a "weight" of `cost[i]` money), select a subset of items such that the total number of walls painted is at least `n`, and the total cost is minimized.

**`findAns(vector<int>& value, vector<int>& cost, int n, int target_sum)` function:**

*   **Purpose:** This function solves a variation of the unbounded knapsack problem. It finds the minimum cost to achieve a `target_sum` of "value" (walls painted) using `n` items.
*   **`dp[i][s]`:** Represents the minimum cost to achieve a sum of `s` walls using the first `i` painters.
*   **Initialization:**
    *   `dp[i][0] = 0` for all `i`: Cost is 0 to paint 0 walls.
    *   `dp[0][s] = inf` for `s > 0`: Impossible to paint `s > 0` walls with 0 painters.
*   **State Transition:** For each painter `i` (0-indexed `i-1` in `cost` and `value` arrays) and each possible sum `s`:
    *   `v1 = cost[i-1] + dp[i-1][max(s - value[i-1], 0)]`:
        *   This represents choosing the current painter `i-1`. The cost is `cost[i-1]` plus the minimum cost to paint the remaining `max(s - value[i-1], 0)` walls using previous painters. `max(s - value[i-1], 0)` is used because we need to paint *at least* `s` walls.
    *   `v2 = dp[i-1][s]`:
        *   This represents *not* choosing the current painter `i-1`. The cost is simply the minimum cost to paint `s` walls using previous painters.
    *   `dp[i][s] = min(v1, v2)`: The minimum of the two options.

**`paintWalls(vector<int>& cost, vector<int>& time)` function:**

*   **Preprocessing `time`:** Creates `modTime` where `modTime[i] = time[i] + 1`. This new `modTime` array represents the total number of walls a painter `i` can cover (one they paint, `time[i]` for free).
*   Calls `findAns` with `modTime` as `value`, `cost` as `cost`, `n` as the number of painters, and `n` as the `target_sum` (because we need to paint all `n` walls).

**Time Complexity:** O(N * N) where N is the number of walls (and painters), as the `dp` table is `N x N`. (More precisely, `N x (N*max_time)` but `max_time` is also bounded by `N` in total effectively, so `N*N` is a loose bound).

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    
    // Using a large integer to represent infinity for cost.
    int inf = 1e9; // A sufficiently large value for infinity
    
    // This function is a variation of the knapsack problem.
    // It calculates the minimum cost to achieve at least 'target_sum' 'value' (walls painted)
    // using 'n' items (painters), where each item has a 'value' and a 'cost'.
    int findAns(std::vector<int>&value, std::vector<int>&cost, int n, int target_sum)
    {
        // dp[i][s] = minimum cost for achieving a sum of 's' walls using the first 'i' painters.
        // The dimensions are (number of painters + 1) x (target_sum + 1).
        std::vector<std::vector<int>> dp(n+1, std::vector<int>(target_sum+1));
        
        // Initialize DP table
        for(int i=0; i<=n; i++) {
            for(int s=0; s<=target_sum; s++) {
                if(s==0) {
                    // Base case: 0 cost to paint 0 walls.
                    dp[i][s] = 0;
                    continue;
                }
                if(i==0) {
                    // Base case: If no painters are available (i=0) and we need to paint >0 walls,
                    // it's impossible, so set cost to infinity.
                    dp[i][s] = inf; 
                    continue;
                }
                
                int cost_if_taken = inf; // Cost if current painter is taken
                int cost_if_not_taken = inf; // Cost if current painter is not taken
                
                // Option 1: Take the (i-1)-th painter
                // The cost is the current painter's cost plus the minimum cost to paint
                // the remaining walls. We need AT LEAST 's' walls, so we use max(s - value[i-1], 0).
                // value[i-1] is the number of walls this painter can cover.
                cost_if_taken = cost[i-1] + dp[i-1][std::max(s-value[i-1], 0)];

                // Option 2: Do not take the (i-1)-th painter
                // The cost is simply the minimum cost to paint 's' walls using previous painters.
                cost_if_not_taken = dp[i-1][s];
                
                // The minimum cost for dp[i][s] is the minimum of the two options.
                dp[i][s] = std::min(cost_if_taken, cost_if_not_taken);
            }
        }
        
        return dp[n][target_sum]; // Return the minimum cost to paint at least 'target_sum' walls.
    }

    // Main function to calculate the minimum cost to paint all walls.
    int paintWalls(std::vector<int>& cost, std::vector<int>& time) 
    {
        int n = cost.size();
        
        // Create a modified time array where each element represents the total walls
        // a painter can cover (1 for the wall they paint + time[i] for free walls).
        std::vector<int> modTime(n);
        for(int i=0; i<n; i++) {
            modTime[i] = time[i] + 1;
        }
        
        // Call the DP helper function.
        // We are effectively finding the minimum cost to paint at least 'n' walls,
        // where each painter (item) contributes modTime[i] (value) for cost[i] (weight).
        return findAns(modTime, cost, n, n);
    }
};
```