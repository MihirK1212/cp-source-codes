# Nested Ranges Count (CSES - PBDS)

## Problem Description

This problem is from CSES Problem Set: [Nested Ranges Count](https://cses.fi/problemset/task/2169).

You are given `n` ranges, each defined by a start point `x` and an end point `y`. For each range, you need to answer two questions:

1.  **Count Contains:** How many other ranges *contain* this range? (A range `[a,b]` contains `[c,d]` if `a <= c` and `d <= b`).
2.  **Count Contained In:** How many other ranges are *contained within* this range? (A range `[c,d]` is contained in `[a,b]` if `a <= c` and `d <= b`).

This problem can be solved efficiently using a sweep-line algorithm combined with a Policy-Based Data Structure (PBDS) in C++, specifically an `ordered_multiset` which allows querying the number of elements less than or equal to a given value.

## C++ Solution

The solution uses `__gnu_pbds::tree` to implement an ordered multiset. The `tree` provides `order_of_key` (which returns the number of elements strictly less than the given key) and `find_by_order` (which returns an iterator to the k-th element).

**`ordered_multiset` Definition:**

```cpp
template <typename T>
using ordered_multiset = tree<pair<T, int>, null_type, less<pair<T, int>>, rb_tree_tag, tree_order_statistics_node_update>;
```

This defines an `ordered_multiset` that stores `std::pair<T, int>`. The `int` part of the pair is a unique identifier (original index) to handle duplicate values correctly within the multiset. This is necessary because `std::set` (and by extension, `tree` with `null_type` for `Mapped` type) only stores unique keys. By pairing the value with a unique ID, we effectively get a multiset behavior.

**Data Structure for Ranges:**

Each range is stored as `std::vector<ll> {start, end, original_index}`. The `original_index` is crucial to store results in the correct order.

### 1. Count Contains (Ranges that contain a given range)

To count ranges `[a,b]` that contain `[c,d]` (`a <= c` and `d <= b`):

*   **Sorting:** Sort the input ranges `r` using `cmpDecStartIncEnd`:
    *   Primary sort key: `r[0]` (start point) in **decreasing** order.
    *   Secondary sort key: `r[1]` (end point) in **increasing** order (for tie-breaking).
    *   This sorting order ensures that when we process a range `[c,d]`, all ranges `[a,b]` with `a <= c` have already been processed (or are being processed at the same `a`). The increasing end point for ties helps to count correctly.
*   **Sweep-Line with PBDS:** Iterate through the sorted ranges.
    *   For each range `[c,d]` (original index `idx`):
        *   Query the `ordered_multiset` (`rangeEnds`) for the number of elements `x` such that `x <= d`. These `x` are the end points of previously processed ranges `[a,b]` where `a <= c`. If `x <= d`, then `[a,b]` also satisfies `d <= b` (since `x` is `b` here), thus `[a,b]` contains `[c,d]`.
        *   The `order_of_key({r[1] + 1, -1})` effectively counts elements `x` in `rangeEnds` such that `x <= r[1]`. (Since `order_of_key` is strictly less, `r[1] + 1` counts up to `r[1]`).
        *   Insert the current range's end point `r[1]` and its original index `r[2]` into `rangeEnds`.

### 2. Count Contained In (Ranges contained within a given range)

To count ranges `[c,d]` that are contained in `[a,b]` (`a <= c` and `d <= b`):

*   **Sorting:** Sort the input ranges `r` using `cmpIncStartDecEnd`:
    *   Primary sort key: `r[0]` (start point) in **increasing** order.
    *   Secondary sort key: `r[1]` (end point) in **decreasing** order (for tie-breaking).
    *   This ensures that when we process a range `[a,b]`, all ranges `[c,d]` with `a <= c` have already been processed (or are being processed). The decreasing end point for ties helps to process larger containing ranges first.
*   **Sweep-Line with PBDS:** Iterate through the sorted ranges.
    *   For each range `[a,b]` (original index `idx`):
        *   Query the `ordered_multiset` (`rangeEnds`) for the number of elements `x` such that `x >= b`. These `x` are the end points of previously processed ranges `[c,d]` where `c >= a`. If `x >= b`, then `[c,d]` is contained in `[a,b]`.
        *   The total size of `rangeEnds` minus `order_of_key({r[1], -1})` gives the count of elements `x` in `rangeEnds` such that `x >= r[1]` (including `r[1]`).
        *   Insert the current range's end point `r[1]` and its original index `r[2]` into `rangeEnds`.

**`solve()` function:**

*   Reads `n` ranges.
*   Calls `helperCountContains` and `helperCountContainedIn` to print the results.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // For std::vector
#include <algorithm> // For std::sort
#include <map>       // For std::map (not directly used in final code, but common)
// The following headers are for Policy-Based Data Structures (PBDS) from GNU extension
#include <ext/pb_ds/assoc_container.hpp> // For tree (ordered_set/map)
#include <ext/pb_ds/tree_policy.hpp>     // For tree_order_statistics_node_update

// Using namespaces for PBDS and standard library elements for brevity in competitive programming
using namespace __gnu_pbds;
// using namespace std; // Using std:: explicitly for clarity and robustness

// Define long long as ll for convenience
typedef long long ll;
typedef std::vector<ll> vll;

// Ordered multiset using indexed pairs.
// Stores pairs of {value, unique_id} to handle duplicate values.
// `tree_order_statistics_node_update` allows order_of_key operations.
template <typename T>
using ordered_multiset = tree<std::pair<T, int>, null_type, std::less<std::pair<T, int>>, rb_tree_tag, tree_order_statistics_node_update>;

// Custom comparator for sorting ranges to count 'contains' relationships.
// Sorts by decreasing start point, then increasing end point for ties.
bool cmpDecStartIncEnd(const vll& r1, const vll& r2) {
    if(r1[0] == r2[0]){
        return r1[1] < r2[1]; // If starts are same, shorter range first
    }
    return r1[0] > r2[0]; // Sort by decreasing start point
}

// Helper function to count how many ranges contain the current range.
void helperCountContains(std::vector<vll> ranges)
{
    int n = ranges.size();
    // Sort ranges by decreasing start point, then increasing end point.
    std::sort(ranges.begin(), ranges.end(), cmpDecStartIncEnd);
    
    vll ans(n); // To store the results for each original index
    
    ordered_multiset<ll> rangeEnds;

    for(const auto& r : ranges) {
        // r[0]: start, r[1]: end, r[2]: original_index

        // The number of ranges [a,b] processed so far (a >= r[0]) that have b <= r[1]
        // is `order_of_key({r[1] + 1, -1})`.
        // order_of_key({value, unique_id}) counts elements *strictly less* than {value, unique_id}.
        // By using {r[1] + 1, -1}, we count all elements whose value is <= r[1].
        ans[r[2]] = rangeEnds.order_of_key({r[1] + 1, -1});
        
        // Insert the current range's end point into the ordered_multiset.
        // We use r[2] as the unique_id because it's the original index.
        rangeEnds.insert({r[1], (int)r[2]});
    }
    
    // Print the results for contains counts
    for(ll val : ans) { std::cout << val << " "; } 
    std::cout << "\n";
}

// Custom comparator for sorting ranges to count 'contained in' relationships.
// Sorts by increasing start point, then decreasing end point for ties.
bool cmpIncStartDecEnd(const vll& r1, const vll& r2) {
    if(r1[0] == r2[0]){
        return r1[1] > r2[1]; // If starts are same, longer range first (for tie-breaking)
    }
    return r1[0] < r2[0]; // Sort by increasing start point
}

// Helper function to count how many ranges are contained within the current range.
void helperCountContainedIn(std::vector<vll> ranges) 
{
    int n = ranges.size();
    // Sort ranges by increasing start point, then decreasing end point.
    std::sort(ranges.begin(), ranges.end(), cmpIncStartDecEnd);
    
    vll ans(n); // To store the results for each original index
    
    ordered_multiset<ll> rangeEnds;

    for(const auto& r : ranges) {
        // r[0]: start, r[1]: end, r[2]: original_index

        // The total number of ranges processed so far (a <= r[0]) is rangeEnds.size().
        // The number of ranges [c,d] (processed earlier) where d < r[1] is order_of_key({r[1], -1}).
        // So, the number of ranges [c,d] where d >= r[1] is totalSize - countWithEndStrictlyLess.
        ll setSize = rangeEnds.size();
        ll countWithEndStrictlyLess = rangeEnds.order_of_key({r[1], -1});
        ans[r[2]] = setSize - countWithEndStrictlyLess;
        
        // Insert the current range's end point into the ordered_multiset.
        rangeEnds.insert({r[1], (int)r[2]});
    }	
    
    // Print the results for contained-in counts
    for(ll val : ans) { std::cout << val << " "; } 
    std::cout << "\n";
}

// Main function to solve the problem
void solve() {
	ll n, i;
	std::cin >> n;

	std::vector<vll> ranges; // Stores {start, end, original_index}
	for(i = 0; i < n; i++){
        ll a, b;
        std::cin >> a >> b;
        ranges.push_back({a, b, i}); // Store original index
    }

    // Call helper functions to compute and print results
	helperCountContains(ranges);
	helperCountContainedIn(ranges);
}

int main() {
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);

    solve(); // Call the main solver function
    return 0;
}
```