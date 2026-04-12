# Subset Sum Problem (Dynamic Programming)

## Problem Description

Given a set of non-negative integers and a target `sum`, determine if there is a subset of the given set whose elements sum up to the target `sum`.

This is a classic dynamic programming problem.

## C++ Solution

This C++ solution uses a 2D dynamic programming table to solve the subset sum problem. The `dp[i][s]` entry in the table indicates whether it's possible to achieve a `sum` of `s` using the first `i` elements of the input array `a`.

**DP Table Definition:**

*   `dp[i][s]` = `true` if a sum `s` can be formed using the first `i` elements of the array `a`, `false` otherwise.

**Dimensions:**

*   The DP table will have `(n+1)` rows and `(sum+1)` columns, where `n` is the number of elements in the array `a` and `sum` is the target sum.

**Initialization (Base Cases):**

*   `dp[0][0] = true`: It is always possible to achieve a sum of 0 by not including any elements (from an empty set).
*   `dp[0][s] = false` for `s > 0`: It is not possible to achieve any positive sum with 0 elements.

**Recurrence Relation:**

For `dp[i][s]`, there are two possibilities:

1.  **Exclude the `i`-th element:** If we don't include the `i`-th element (`a[i]`) in our subset, then `dp[i][s]` is `true` if `dp[i-1][s]` is `true`. (`v2 = dp[i-1][s]`).
2.  **Include the `i`-th element:** If we include the `i`-th element (`a[i]`) in our subset, then `dp[i][s]` is `true` if `s >= a[i]` and `dp[i-1][s - a[i]]` is `true`. (`v1 = dp[i-1][s - a[i]]`).

Therefore, `dp[i][s] = v1 || v2`.

**Final Answer:**

The final answer is stored in `dp[n][sum]`, which tells whether the target `sum` can be achieved using all `n` elements.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <numeric>   // For std::accumulate (not directly used but useful for sums)
#include <algorithm> // For std::sort, std::reverse (some macros conflict)
#include <limits>    // For std::numeric_limits

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define ll long long 
#define ld long double 
#define vll std::vector<long long>
#define vi std::vector<int>
// #define f first // Avoiding conflicts with member access
// #define s second // Avoiding conflicts with member access
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){std::cout<<arr[i]<<" ";} std::cout<<"\n";
// #define sort(a) std::sort(a.begin(),a.end()); // Avoid conflict with std::sort
// #define rsort(a) std::sort(a.rbegin(),a.rend()); // Avoid conflict with std::sort
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid conflict with std::reverse
#define input(arr) for(long long i=0;i<arr.size();i++){std::cin>>arr[i];}\
// Typedefs, etc.

ll inf=std::numeric_limits<long long>::max();

int main()
{
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);
    
    ll n_elements, target_sum;
    std::cin >> n_elements >> target_sum;
    
    vll a(n_elements + 1, 0); // 1-indexed array for elements
    for(ll i = 1; i <= n_elements; i++){
        std::cin >> a[i];
    }
    
    // dp[i][s] = true if sum 's' is possible using the first 'i' elements
    bool dp[n_elements + 1][target_sum + 1];
    
    // Initialize base cases
    for(ll i = 0; i <= n_elements; i++)
    {
        for(ll s = 0; s <= target_sum; s++)
        {
            if(i == 0) // No elements considered
            {
                if(s == 0){dp[i][s] = true;} // Sum 0 is possible with no elements
                else{dp[i][s] = false;}   // Any other sum is not possible
            }
            else // Consider elements from 1 to i
            {
                bool include_ith_element = false;
                // If current sum s is at least a[i], check if s - a[i] was possible with (i-1) elements
                if(s >= a[i]){
                    include_ith_element = dp[i-1][s - a[i]];
                }
                
                bool exclude_ith_element = dp[i-1][s]; // Check if s was possible with (i-1) elements
                
                dp[i][s] = include_ith_element || exclude_ith_element;
            }
        }
    }
    
    if(dp[n_elements][target_sum]){
        std::cout << "Yes\n";
    }
    else{
        std::cout << "No\n";
    }
    
    return 0;
}
```