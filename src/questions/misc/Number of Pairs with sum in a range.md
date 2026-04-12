# Number of Pairs with Sum in a Range

## Problem Description

Given an array `a` of `n` integers and a range `[l, r]`, find the number of pairs `(a[i], a[j])` such that `i < j` and `l <= (a[i] + a[j]) <= r`.

## C++ Solution

The problem can be solved efficiently using a two-pointer approach after sorting the array. The core idea is to fix one element `a[pos]` and then use two pointers (`lb` and `ub`) to find the valid range of elements `a[k]` (where `k > pos`) such that `l <= a[pos] + a[k] <= r`.

**Algorithm:**

1.  **Sort the Array:** Sort the input array `a` in non-decreasing order. This allows us to use the two-pointer technique.
2.  **Initialize Pointers:**
    *   `pos`: The main pointer, iterating from the beginning of the array (`0` to `n-1`). This `a[pos]` is one element of the pair.
    *   `lb`: A pointer for the lower bound. It will find the smallest `k > pos` such that `a[pos] + a[k] >= l`.
    *   `ub`: A pointer for the upper bound. It will find the largest `k > pos` such that `a[pos] + a[k] <= r`.
    *   `count`: Variable to store the total number of valid pairs.
3.  **Iterate with `pos`:**
    *   For each `pos` from `0` to `n-2`:
        *   Initialize `lb` and `ub` to `n-1` for each `pos` (or `max(pos, lb)` to prevent `lb` from going below `pos`).
        *   **Find `lb` (Lower Bound):** Move `lb` inwards (to the left) while `(a[pos] + a[lb]) >= l` and `lb > pos`. This finds the first index `lb` such that `a[pos] + a[lb]` is just less than `l` (or `lb` becomes `pos`). The next element `lb+1` would be the smallest element that satisfies the sum condition. So effectively we are looking for the smallest index `k` such that `a[k] >= l - a[pos]`. The given code adjusts `lb` such that `a[pos] + a[lb]` becomes less than `l`, and then `lb+1` is a potential start.
        *   **Find `ub` (Upper Bound):** Move `ub` inwards (to the left) while `(a[pos] + a[ub]) > r` and `ub > lb`. This finds the largest index `ub` such that `a[pos] + a[ub] <= r`.
        *   **Count Valid Pairs:** The number of elements `a[k]` that satisfy `l <= a[pos] + a[k] <= r` for the current `a[pos]` is `(ub - lb)`. Add this to `count`. (Specifically, `a[lb+1]` to `a[ub]` are valid elements to pair with `a[pos]`).
4.  **Output:** Print `count`.

```cpp
#include <iostream>    // For std::cin, std::cout
#include <vector>      // For std::vector
#include <algorithm>   // For std::sort, std::max, std::min

// Commonly used in competitive programming for brevity, but explicit std:: is more robust
// using namespace std;

int main()
{
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);

    long long n, i, l, r; // n: array size, l: lower bound of sum, r: upper bound of sum
    
    std::cin >> n >> l >> r;
    std::vector<long long> a(n);
    
    // Read array elements
    for(i = 0; i < n; i++)
    {
        std::cin >> a[i];
    }

    // Sort the array to enable the two-pointer approach
    std::sort(a.begin(), a.end());
    
    long long lb_ptr = n - 1; // Lower bound pointer
    long long ub_ptr = n - 1; // Upper bound pointer
    long long count = 0;      // Stores the total number of valid pairs
    
    // Iterate with the first element of the pair (a[pos])
    for(long long pos = 0; pos < n; ++pos)
    {
        // Adjust lb_ptr: find the largest index k (k > pos) such that a[pos] + a[k] < l.
        // All elements from (lb_ptr + 1) to ub_ptr will satisfy a[pos] + a[k] >= l.
        lb_ptr = std::max(pos, lb_ptr); // Ensure lb_ptr is at least 'pos'
        while(lb_ptr > pos && (a[pos] + a[lb_ptr]) >= l)
        {
            lb_ptr--;
        }

        // Adjust ub_ptr: find the largest index k (k > pos) such that a[pos] + a[k] <= r.
        // All elements up to ub_ptr will satisfy a[pos] + a[k] <= r.
        ub_ptr = std::max(pos, ub_ptr); // Ensure ub_ptr is at least 'pos'
        while(ub_ptr > pos && (a[pos] + a[ub_ptr]) > r) 
        {
            ub_ptr--;
        }    
        
        // The number of valid elements for a[pos] is from index (lb_ptr + 1) to ub_ptr.
        // Make sure ub_ptr is not less than lb_ptr.
        if (ub_ptr > lb_ptr) {
            count += (ub_ptr - lb_ptr); 
        }
    }
    
    std::cout << count << "\n";            
    return 0;
}
```