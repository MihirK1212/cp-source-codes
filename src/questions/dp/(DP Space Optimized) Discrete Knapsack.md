# Discrete Knapsack (Space-Optimized DP - 0/1 Knapsack)

## Problem Description

The **0/1 Knapsack problem** is a classic combinatorial optimization problem. Given a set of `n` items, each with a `weight[i]` and a `value[i]`, and a knapsack of maximum capacity `W`. The objective is to select a subset of these items such that their total weight does not exceed `W`, and the total value of the selected items is maximized. Each item can either be completely included in the knapsack or completely excluded (hence "0/1"), and it can be included at most once.

This solution presents a space-optimized dynamic programming approach for the 0/1 Knapsack problem. Instead of using a 2D DP table `dp[n+1][W+1]`, it uses only two 1D arrays, reducing the space complexity from O(N*W) to O(W).

## C++ Solution

The `discrete_knapsack` function implements the space-optimized DP approach.

**Parameters:**

*   `n`: Number of items.
*   `W`: Maximum capacity of the knapsack.
*   `weight`: `std::vector<ll>` of item weights.
*   `value`: `std::vector<ll>` of item values.

**Space-Optimized DP Strategy:**

The core idea behind this space optimization is that `dp[i][w]` (the maximum value for current item `i` and current capacity `w`) only depends on values from the *previous item* (`i-1`). Therefore, we can use two 1D arrays to store the results for the current and previous items, reducing the space complexity.

1.  **Initialization:**
    *   `dp_prev`: A 1D `std::vector<ll>` of size `W+1`, initialized to zeros. This stores the maximum values achievable with items considered *before* the current item.
    *   `dp_next`: A 1D `std::vector<ll>` of size `W+1`, initialized to zeros. This will store the maximum values achievable with the current item `i` being considered.

2.  **Iteration:**
    *   **Outer loop:** Iterates through each item `i` from `0` to `n-1`.
    *   **Inner loop:** Iterates through capacities `w` from `0` to `W`.
    *   For each `(i, w)` pair, `dp_next[w]` is calculated based on two choices for the `i`-th item:
        *   **Exclude item `i`:** The maximum value for capacity `w` without including the current item `i` is simply `dp_prev[w]`.
        *   **Include item `i`:** If the current capacity `w` is sufficient to hold `weight[i]` (`w >= weight[i]`), then we can potentially include item `i`. The value obtained would be `value[i]` plus the maximum value achievable for the remaining capacity `(w - weight[i])` using items *before* item `i`, which is `dp_prev[w - weight[i]]`.
        *   `dp_next[w]` is then updated to be the maximum of these two options: `std::max(dp_prev[w], dp_prev[w - weight[i]] + value[i])` (if `weight[i]` fits).
    *   **State Update:** After processing all capacities `w` for the current item `i`, `dp_prev` is updated with the values from `dp_next` to prepare for the next item (`i+1`). This ensures that `dp_prev` always holds the results from the *previous* iteration (i.e., `i-1` items).

**Result:**

After iterating through all items, `dp_prev[W]` (or `dp_next[W]` if the final `dp_prev = dp_next` assignment is considered) will contain the maximum value that can be obtained for a knapsack with capacity `W` using all `n` items.

```cpp
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::max
#include <iostream>  // For standard input/output

typedef long long ll;
typedef std::vector<ll> vll;

// Function to solve the 0/1 Knapsack problem with space optimization
// using two 1D DP arrays (dp_prev and dp_next).
ll discrete_knapsack(ll n, ll W, vll& weight, vll& value)
{
    // dp_prev stores maximum value for items considered up to (i-1) for various capacities.
    // dp_next stores maximum value for items considered up to (i) for various capacities.
    vll dp_prev(W + 1, 0);
    vll dp_next(W + 1, 0); 

    // Iterate through each item. 'i' represents the index of the current item (0 to n-1).
    for(ll i = 0; i < n; i++) 
    {
        // Iterate through each possible knapsack capacity 'w' from 0 to W.
        for(ll w = 0; w <= W; w++) 
        {
            // Option 1: Exclude the current item (item at index i).
            // The maximum value for capacity 'w' without the current item is dp_prev[w].
            dp_next[w] = dp_prev[w]; 

            // Option 2: Include the current item (item at index i).
            // This is only possible if the current capacity 'w' is sufficient for the item's weight.
            if(w >= weight[i]) 
            {
                // Compare with taking the current item:
                // (value of current item) + (max value for remaining capacity (w - weight[i])) 
                //                                 from items considered *before* the current one (dp_prev).
                dp_next[w] = std::max(dp_next[w], dp_prev[w - weight[i]] + value[i]);
            }
        }

        // After processing all capacities for item 'i',
        // the dp_next array becomes the dp_prev for the next iteration (item i+1).
        dp_prev = dp_next;
    }

    // The maximum value for capacity 'W' using all 'n' items is in dp_prev[W].
    return dp_prev[W];
}

int main() {
    // Example usage of the discrete_knapsack function
    ll n = 3; // Number of items
    ll W = 5; // Knapsack capacity
    vll weights = {1, 2, 3}; // Weights of items
    vll values = {6, 10, 12}; // Values of items

    ll max_val = discrete_knapsack(n, W, weights, values);
    std::cout << "Maximum value in knapsack: " << max_val << std::endl;

    // Another example
    n = 4;
    W = 7;
    weights = {1, 3, 4, 5};
    values = {1, 4, 5, 7};
    max_val = discrete_knapsack(n, W, weights, values);
    std::cout << "Maximum value in knapsack (second example): " << max_val << std::endl;

    return 0;
}
```