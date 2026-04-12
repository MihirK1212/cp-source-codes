# Subarray with Sum Equal to K

## Problem Description

Given an array of integers `nums` and an integer `k`, find the length of the longest subarray whose elements sum up to `k`. If no such subarray exists, return -1. This problem can be solved efficiently using a hash map to store prefix sums.

## C++ Solution

This C++ solution uses the prefix sum technique combined with a hash map (`std::map` or `std::unordered_map`) to find the longest subarray with a sum equal to `k`. The core idea is that if the cumulative sum up to index `i` is `current_sum`, and we have seen a previous cumulative sum `(current_sum - k)` at index `j`, then the subarray `nums[j+1...i]` has a sum of `k`. We want to find the maximum length of such a subarray.

**Algorithm:**

1.  **Initialize:**
    *   `max_len = -1`: To store the maximum length found.
    *   `current_sum = 0`: To keep track of the prefix sum.
    *   `prefix_sums_map`: A hash map to store `(prefix_sum, index)` pairs. This map will store the *first* occurrence of each prefix sum to ensure we calculate the *longest* subarray.
2.  **Iterate Through Array:** For each element `a[i]` at index `i` (0-indexed):
    *   Update `current_sum += a[i];`.
    *   **Check for `current_sum == k`:** If `current_sum` itself equals `k`, it means the subarray from index `0` to `i` has a sum of `k`. Update `max_len = max(max_len, i + 1);`.
    *   **Check for `current_sum - k`:** Look for `current_sum - k` in the `prefix_sums_map`:
        *   If `prefix_sums_map.find(current_sum - k)` exists, it means a subarray `nums[j+1...i]` sums to `k`, where `j = prefix_sums_map[current_sum - k]`. The length of this subarray is `i - j`. Update `max_len = max(max_len, i - prefix_sums_map[current_sum - k]);`.
    *   **Store `current_sum`:** If `current_sum` is not already in `prefix_sums_map`, add `(current_sum, i)` to the map. We only store the *first* occurrence to correctly find the longest subarray.
3.  **Return `max_len`.

**Note:** If `max_len` remains `-1`, it means no subarray with sum `k` was found.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
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
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    ll n,k,i;
    cin>>n>>k;
    vll a(n);
    input(a);
    
    // Map to store (prefix_sum, first_occurrence_index)
    map<ll,ll> prefix_sums_map;
    
    ll max_len=-1; // Initialize max_len to -1 (no subarray found yet)
    
    ll current_sum=0;
    
    for(i=0;i<n;i++)
    {
        current_sum+=a[i];

        // Case 1: If current_sum itself is equal to k, the subarray from index 0 to i has sum k.
        // Its length is i+1.
        if(current_sum==k)
        {
            if((i+1)>max_len)
            {
                max_len=i+1;
            }
        }
        
        // Case 2: Check if (current_sum - k) has been seen before.
        // If it has, then the subarray between its stored index and current index i sums to k.
        if(prefix_sums_map.find(current_sum-k)!=prefix_sums_map.end())
        {
            // Length of this subarray is current_index - stored_index.
            if((i-prefix_sums_map[current_sum-k])>max_len)
            {
                max_len=i-prefix_sums_map[current_sum-k];
            }
        }
        
        // Store the current_sum and its index if it's the first time we've seen this prefix sum.
        // This ensures we get the longest subarray.
        if(prefix_sums_map.find(current_sum)==prefix_sums_map.end()){prefix_sums_map[current_sum]=i;}
    }
    
    cout<<max_len<<"\n";
    
    return 0;
}
```