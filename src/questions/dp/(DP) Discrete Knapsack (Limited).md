# Discrete Knapsack Problem (Limited Items) - Dynamic Programming

## Problem Description

Given `N` items, each with a `weight` and a `value`, and a knapsack of capacity `W`, find the maximum total value that can be put into the knapsack such that the total weight does not exceed `W`. Each item can be used at most once (this is the 0/1 Knapsack variation).

## C++ Solution

This C++ solution uses dynamic programming to solve the 0/1 Knapsack problem. The `dp[w][i]` state represents the maximum value that can be obtained with a knapsack capacity of `w` using the first `i` items. Since each item can be used at most once, we consider two options for each item: either include it or exclude it.

**Algorithm:**

1.  **Initialize DP Table:** Create a 2D DP table `max_value` of size `(W+1) x (N+1)`. `max_value[w][i]` will store the maximum value for capacity `w` using the first `i` items.
    *   Initialize `max_value[w][0] = 0` for all `w`: If no items are considered, the value is 0.
    *   Initialize `max_value[0][i] = 0` for all `i`: If the knapsack capacity is 0, no items can be taken, so the value is 0.
2.  **Populate DP Table:** Iterate `i` from `1` to `N` (representing the current item being considered) and `w` from `1` to `W` (representing the current knapsack capacity):
    *   **Option 1: Exclude Current Item `i`:** `value_excluded = max_value[w][i-1];` (The maximum value obtained using the first `i-1` items with the same capacity `w`).
    *   **Option 2: Include Current Item `i`:** If `w >= weight[i]` (if the knapsack has enough capacity for the current item):
        *   `value_included = max_value[w - weight[i]][i-1] + value[i];` (The value of the current item plus the maximum value obtained from the remaining capacity `(w - weight[i])` using the first `i-1` items).
    *   **Choose Maximum:** `max_value[w][i] = max(value_included, value_excluded);` (Take the maximum of the two options).
3.  **Result:** The final answer is `max_value[W][N]`. This represents the maximum value that can be obtained with the total knapsack capacity `W` using all `N` items.

**Time Complexity:** O(N * W)
**Space Complexity:** O(N * W)

*(Note: This problem can also be solved with O(W) space complexity using a 1D DP array, but the 2D solution is more intuitive for understanding the state transitions.)*

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
#define ld long double 
#define vll vector<long long>
#define vi vector<int>
#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define sort(a) sort(a.begin(),a.end());
#define rsort(a) sort(a.rbegin(),a.rend());
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}


int main()
{
    // Input variables: N (number of items), W (knapsack capacity)
    ll N,W,i,w;
    
    cout<<"Enter number of different kinds of items\n";
    cin>>N;

    // Store weights and values of items (1-indexed for convenience with DP table)
    vll weight(N+1,0),value(N+1,0);
    cout<<"Enter weights and values of the "<<N<<" kinds of items\n";
    for(i=1;i<=N;i++)
    {
        cin>>weight[i]>>value[i];
    }
    
    cout<<"Enter maximum capacity of bag\n";
    cin>>W;
    
    // DP table: max_value[w][i] = maximum value for capacity 'w' using first 'i' items
    vector<vll> max_value(W+1,vll(N+1));
    
    // Initialization:
    // If capacity is 0, max value is 0 for any number of items.
    for(w=0;w<=W;w++){max_value[w][0]=0;}
    // If no items are considered, max value is 0 for any capacity.
    for(i=0;i<=N;i++){max_value[0][i]=0;}
    
    // Fill the DP table
    for(i=1;i<=N;i++) // Iterate through items (from 1 to N)
    {
        for(w=1;w<=W;w++) // Iterate through capacities (from 1 to W)
        {
            ll value_included=-1; // Value if current item is included
            ll value_excluded=-1; // Value if current item is excluded
            
            // Option 1: Include the current item 'i'
            // Only possible if current capacity 'w' is greater than or equal to item's weight.
            if(w>=weight[i]){
                // Value is current item's value + max value from remaining capacity using previous items.
                value_included=max_value[w-weight[i]][i-1]+value[i];
            }
            
            // Option 2: Exclude the current item 'i'
            // Value is simply the max value from previous items with the same capacity.
            value_excluded=max_value[w][i-1];
            
            // Take the maximum of the two options. Handle cases where one option might be invalid (-1).
            max_value[w][i]=max(value_included,value_excluded);
        }
    }
    
    // The result is the max value for total capacity W using all N items.
    cout<<max_value[W][N]<<"\n";
    
    return 0;
}
```