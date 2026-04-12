# Sleeping in Class (USACO Bronze - Prefix Sums and Binary Search)

## Problem Description

This problem is from USACO Bronze contest (e.g., [Sleeping in Class](http://www.usaco.org/index.php?page=viewproblem&cpid=1107) from 2021 US Open Contest). The task is to take an array of `N` numbers and merge adjacent elements until all remaining elements are equal. The goal is to find the minimum number of merge operations required.

Merging adjacent elements means replacing `A[i]` and `A[i+1]` with `A[i] + A[i+1]`. This operation reduces the number of elements by one. The problem asks for the minimum number of merges, which is equivalent to finding the maximum number of groups `(N - K)` that can be formed such that each group has the same sum, and then `K` would be the minimum merges.

## C++ Solution

This C++ solution uses prefix sums and a binary search helper function (`findMaxIndex`) within a linear scan to find the minimum number of merge operations.

**Key Idea:**

The fundamental idea is that if we merge adjacent elements to achieve `P` equal-sum groups, then each group must have a sum equal to `TotalSum / P`. We can iterate through all possible numbers of merges `k` (from `0` to `n-1`), which implies `(n-k)` resulting groups. For each `k`, we calculate the `target_group_sum = TotalSum / (n-k)` and check if the original array can indeed be partitioned into `(n-k)` contiguous segments, each summing to `target_group_sum`.

**Functions:**

1.  **`findMaxIndex(vll& a, ll lb, ll ub, ll x)`:**
    *   Performs a binary search on the prefix sum array `a` within the range `[lb, ub]`.
    *   It finds the *largest* index `ans` such that `a[ans]` is equal to `x`. This is crucial because we want the rightmost endpoint of a partition.
    *   Returns the found index, or `-1` if `x` is not found.

2.  **`allowed(vll& a, ll n, vll& p_sum, ll k)`:**
    *   **Parameters:**
        *   `a`: Original array (not directly used after prefix sum calculation).
        *   `n`: Size of the array.
        *   `p_sum`: Prefix sum array of `a`.
        *   `k`: The hypothesized number of merges. This implies `(n-k)` resulting equal-sum partitions.
    *   **Logic:**
        *   If `n - k == 0` and `total_sum == 0`, it means all elements are removed/merged, and the total sum is 0, which is valid. Return `true`.
        *   Calculate `total_sum = p_sum[n-1]`.
        *   If `total_sum` is not divisible by `(n-k)` (the number of groups), it's impossible to form equal-sum groups. Return `false`.
        *   `target_group_sum = total_sum / (n-k)`. This is the required sum for each resulting partition.
        *   The `while` loop checks if `(n-k)` partitions can be formed. It iteratively tries to find points in the `p_sum` array that correspond to the end of each partition (`target_group_sum`, `2*target_group_sum`, ..., `(n-k)*target_group_sum`).
            *   `expected_prefix_sum = current_partitions_to_match * target_group_sum`.
            *   `current_upper_bound_idx = findMaxIndex(p_sum, 0, current_upper_bound_idx, expected_prefix_sum)`: Finds the rightmost index where this `expected_prefix_sum` occurs.
            *   If `current_upper_bound_idx < 0`, it means the required prefix sum was not found, so return `false`.
            *   Decrement `current_partitions_to_match` and `current_upper_bound_idx` (to look for the next partition to its left).
        *   Return `true` if all partitions are successfully matched (`current_partitions_to_match == 0`).

**`main()` function:**

*   Handles multiple test cases.
*   For each test case:
    *   Reads `n` and array `a`.
    *   Computes the prefix sum array `p_sum`.
    *   Iterates `k` from `0` to `n-1`. For the first `k` for which `allowed(a, n, p_sum, k)` returns `true`, that `k` is the minimum number of merges. Print `k` and `break`.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <numeric>   // Required for std::accumulate (not used here but useful for sum)
#include <algorithm> // Required for std::sort, std::reverse, std::max, std::min
#include <cmath>     // Required for std::ceil (if ceilVal is used)
#include <limits>    // Required for std::numeric_limits

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
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid macro conflict
#define input(arr) for(long long i_idx=0;i_idx<arr.size();i_idx++){std::cin>>arr[i_idx];}\

ll inf=std::numeric_limits<long long>::max();

// ll ceilVal(ll a,ll b) // Not used in this version after logic adjustments
// {
//    return std::ceil(((ld)a)/((ld)b)); 
// }

void setIO(std::string name = "") 
{ 
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
        freopen((name+".out").c_str(), "w", stdout);
    }
}

// Binary search to find the largest index 'ans' such that a[ans] == x
// within the range [lb, ub]. Returns -1 if not found.
ll findMaxIndex(vll& a, ll lb, ll ub, ll x)
{
    ll mid;
    ll ans = -1;
    
    while(lb <= ub)
    {
        mid = lb + (ub - lb) / 2;
        if(a[mid] == x){
            ans = mid;     // Found x, try to find a larger index (rightmost occurrence)
            lb = mid + 1;
        }
        else if(a[mid] < x){
            lb = mid + 1;  // x is to the right
        }
        else{
            ub = mid - 1;  // x is to the left
        }
    }
    
    return ans;
}

// Checks if the array can be partitioned into (n-k) contiguous subarrays,
// each summing to a calculated target_group_sum.
// 'k' represents the number of merges (so n-k is the number of groups).
// 'p_sum' is the prefix sum array of 'a'.
bool allowed(vll& a, ll n, vll& p_sum, ll k)
{
    ll num_groups = (n - k); // Number of partitions we are trying to form

    if (n == 0) return k == 0; // If empty array, 0 merges if k=0
    if (num_groups <= 0) { // If all elements are merged/removed, total sum must be 0 for validity
        return p_sum[n-1] == 0; 
    }

    ll total_sum = p_sum[n-1];
    
    // If the total sum is not divisible by the number of partitions, it's impossible to form equal-sum groups
    if(total_sum % num_groups != 0){return false;}
    
    ll target_group_sum = total_sum / num_groups; // The required sum for each partition
    
    ll current_groups_to_match = num_groups;   // Number of partitions we still need to find
    ll current_prefix_sum_target = total_sum; // The prefix sum we are looking for (starts with total sum)
    ll search_ub_idx = n - 1;                // Upper bound for searching in p_sum array
    
    // This loop effectively tries to find the end points of partitions from right to left.
    while(current_groups_to_match >= 1) // While there are still groups to match
    {
        // Find the rightmost index where the prefix sum equals current_prefix_sum_target
        ll found_idx = findMaxIndex(p_sum, 0, search_ub_idx, current_prefix_sum_target);
        
        if(found_idx < 0) { // If the expected prefix sum is not found
            return false;
        }
        
        // One partition successfully matched. Adjust target prefix sum for the next partition.
        current_groups_to_match--;
        current_prefix_sum_target -= target_group_sum;
        search_ub_idx = found_idx - 1; // Search for the next partition in the remaining left part
    }
    
    // If we successfully matched all groups, current_groups_to_match will be 0.
    return current_groups_to_match == 0;
}

int main()
{
    setIO(""); // No specific file I/O for this problem, use standard I/O
    
    ll T; // Number of test cases
    std::cin >> T;
    
    while(T--)
    {
        ll n; // Size of the array
        std::cin >> n;
        
        vll a(n); // Array elements
        input(a); 
        
        vll p_sum(n); // Prefix sum array
        if (n > 0) {
            p_sum[0] = a[0];
            for(ll i = 1; i < n; i++){p_sum[i] = p_sum[i-1] + a[i];}
        }

        ll min_merges_k = n - 1; // Initialize with max possible merges
        
        // Iterate through all possible number of merges (k) from 0 to n-1
        // k merges means (n-k) resulting groups.
        for(ll k = 0; k < n; k++)
        {
            if(allowed(a, n, p_sum, k)){
                min_merges_k = k;
                break; // Found the minimum k, move to next test case
            }
        }
        std::cout << min_merges_k << "\n"; // Print the minimum k
    }
    
    return 0;
}
```