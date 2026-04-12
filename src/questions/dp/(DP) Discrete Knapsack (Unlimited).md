# Discrete Knapsack (Unbounded / Unlimited Repetition)

## Problem Description

Given `N` types of items, each with a `weight[i]` and a `value[i]`, and a knapsack of maximum capacity `W`. The goal is to choose items such that the total weight does not exceed `W` and the total value is maximized. In the unbounded knapsack problem, each item type can be taken multiple times (i.e., there is an unlimited supply of each item type).

This is a classic dynamic programming problem.

## C++ Solution

This C++ solution uses a 1D dynamic programming array to solve the Unbounded Knapsack problem. The `max_value[w]` entry in the array stores the maximum value that can be obtained for a knapsack with a total capacity of `w`.

**DP Array Definition:**

*   `max_value[w]` = The maximum value achievable with a knapsack of capacity `w`.

**Dimensions:**

*   The `max_value` array will have `W+1` elements, indexed from 0 to `W`.

**Initialization:**

*   `max_value[0] = 0`: A knapsack with capacity 0 can hold no items, so its value is 0.
*   All other `max_value[w]` are initialized to 0, implying no value is gained if no items fit.

**Recurrence Relation:**

To calculate `max_value[w]`:

*   Iterate `w` from `1` to `W` (for each possible knapsack capacity).
*   For each capacity `w`, iterate through each item type `i`.
*   If the current capacity `w` is greater than or equal to the `weight[i]` of the `i`-th item:
    *   Consider including the `i`-th item. If we include it, the remaining capacity would be `w - weight[i]`, and the value from that remaining capacity would be `max_value[w - weight[i]]`. So, the total value would be `max_value[w - weight[i]] + value[i]`.
    *   `max_value[w]` should be the maximum of its current value (which implicitly means not including the `i`-th item, or using other combinations) and `(max_value[w - weight[i]] + value[i])`.
    *   `max_value[w] = max(max_value[w], max_value[w - weight[i]] + value[i]);`

**Key Difference from 0/1 Knapsack:**

In Unbounded Knapsack, `max_value[w - weight[i]]` is used because we can pick the same item `i` again (unlimited supply). In 0/1 Knapsack, `dp[i-1][w - weight[i]]` would be used, referring to a subproblem *without* the `i`-th item to ensure it's picked at most once.

**Final Answer:**

The final answer is `max_value[W]`, which is the maximum value that can be obtained for a knapsack with capacity `W`.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::max
#include <limits>    // For std::numeric_limits

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define ll long long 
#define ld long double 
#define vll std::vector<long long>
#define vi std::vector<int>
// #define f first // Avoiding conflicts with member access
// #define s second // Avoiding conflicts with member access
#define pb push_back
#define printoneline(arr) for(long long x_val : arr){std::cout<<x_val<<" ";} std::cout<<"\n";
// #define sort(a) std::sort(a.begin(),a.end()); // Avoid macro conflict
// #define rsort(a) std::sort(a.rbegin(),a.rend()); // Avoid macro conflict
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid macro conflict
#define input(arr) for(long long i_idx=0;i_idx<arr.size();i_idx++){std::cin>>arr[i_idx];}\

int main()
{
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);
    
    ll n_items, max_capacity_W;
    
    std::cout << "Enter number of different kinds of items\n";
    std::cin >> n_items;
    
    vll weights(n_items, 0);
    vll values(n_items, 0);

    std::cout << "Enter weights and values of the " << n_items << " kinds of items\n";
    for(ll i = 0; i < n_items; i++)
    {
        std::cin >> weights[i] >> values[i];
    }
    
    std::cout << "Enter maximum capacity of bag\n";
    std::cin >> max_capacity_W;
    
    // max_value[w] = maximum value we can obtain for total capacity of 'w'
    vll max_value(max_capacity_W + 1, 0); 

    // Iterate through all possible capacities from 1 to W
    for(ll current_capacity = 1; current_capacity <= max_capacity_W; current_capacity++)
    {
        // For each capacity, iterate through all available item types
        for(ll i = 0; i < n_items; i++)
        {
            // If the current item's weight can fit into the current_capacity
            if(current_capacity >= weights[i])
            {
                // Update max_value[current_capacity]:
                // It's the maximum of:
                // 1. Its current value (not including item i or using other combinations).
                // 2. The value obtained by including item i:
                //    (value of item i) + (max value for remaining capacity (current_capacity - weights[i]))
                max_value[current_capacity] = std::max(max_value[current_capacity], 
                                                     max_value[current_capacity - weights[i]] + values[i]);
            }
        }
    }
    
    std::cout << max_value[max_capacity_W] << "\n";
    
    return 0;
}
```