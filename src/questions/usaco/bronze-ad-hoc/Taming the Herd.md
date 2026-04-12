# Taming the Herd (USACO Bronze - Ad-Hoc / Greedy)

## Problem Description

This problem is from USACO Bronze contest: [Taming the Herd](http://www.usaco.org/index.php?page=viewproblem2&cpid=809).

Farmer John's cows are prone to escaping! He has `N` cows, and each day he records `b_i`, the number of days that have passed since the last time `i`-th cow broke out. If a cow has not broken out since he started recording, `b_i` is -1. Farmer John only knows the `b_i` values, and his task is to determine the minimum and maximum possible number of total breakouts that could have occurred.

**Key Rules:**

*   If `b_i = 0`, cow `i` broke out on day `i`.
*   If `b_i = k > 0`, cow `i` last broke out on day `i - k`.
*   If `b_i = -1`, the breakout day for cow `i` is unknown.

## C++ Solution

This C++ solution uses two passes (one backward, one forward) to determine the maximum and minimum possible number of breakouts, respectively. It handles the reconstruction of breakout days based on known values and makes greedy choices for unknown values (`-1`).

### Part 1: Finding Maximum Breakouts (Backward Pass)

This pass determines the maximum possible number of breakouts. The strategy is to fill `-1` values in a way that maximizes breakouts, while still satisfying the known `b_i` values. It processes the array from right to left.

1.  **Initialize `a[n-1]`:** The last element `a[n-1]` must be 0 if it's not -1. If it's -1, we assume it was 0 to maximize breakouts (a breakout happened on the last day). `max_ans` is incremented.
2.  **Iterate `i` from `n-2` down to `0`:**
    *   `should_be`: Represents what `a[i]` *should* be to be consistent with `a[i+1]` (i.e., `a[i+1] - 1`).
    *   If `a[i]` is fixed (`!= -1`):
        *   If `a[i] == should_be` (consistent), continue.
        *   If `a[i] == 0`, it's a new breakout, increment `max_ans`. Update `should_be` to `1`.
        *   If `a[i] != should_be` and `a[i] != 0`, it's a contradiction. No solution, return -1.
    *   If `a[i] == -1` (unknown):
        *   If a `should_be` value is active (i.e., `a[i+1]` was not 0), set `a[i] = should_be`. Update `should_be` to `should_be - 1`. If `should_be` becomes 0, it means a breakout happened, increment `max_ans`. Reset `should_be` logic for next element.
        *   If no `should_be` is active (i.e., `a[i+1]` was 0), `a[i]` is effectively a new breakout. Set `a[i]=0`, increment `max_ans`. Update `should_be` to `1`.

### Part 2: Finding Minimum Breakouts (Forward Pass)

This pass determines the minimum possible number of breakouts. The strategy is to fill `-1` values in a way that minimizes breakouts.

1.  **Initialize `a[0] = 0`:** The very first day must have a breakout (or implies a breakout occurred 0 days ago). Increment `min_ans`.
2.  **Iterate `i` from `1` to `n-1`:**
    *   `should_be`: Represents what `a[i]` *should* be to be consistent with `a[i-1]` (i.e., `a[i-1] + 1`).
    *   If `a[i]` is fixed (`!= -1`):
        *   If `a[i] == 0`, it's a new breakout. Increment `min_ans`. Update `should_be` to `1`.
        *   If `a[i] != should_be` and `a[i] != 0`, it's a contradiction. No solution, return -1.
    *   If `a[i] == -1` (unknown):
        *   If `should_be` is less than `n` (within bounds), we fill `a[i] = should_be` to avoid a new breakout (minimizing `0`s). Update `should_be` to `should_be + 1`.
        *   If `should_be` is too large (meaning a previous `a[i-1]` was too large to maintain a sequence), then `a[i]` must be `0`, implying a new breakout. Increment `min_ans`. Update `should_be` to `1`.

**Final Result:** Print `min_ans` and `max_ans`.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::max, std::min (macros conflict, use std:: explicitly)
#include <limits>    // For std::numeric_limits<long long>::max

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long x_val : arr){std::cout<<x_val<<" ";} std::cout<<"\n";
#define all(x) (x).begin(), (x).end()
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid macro conflict
#define input(arr) for(long long i_idx=0;i_idx<arr.size();i_idx++){std::cin>>arr[i_idx];}\

typedef long long ll;
typedef long double  ld;
typedef std::vector<long long> vll;
typedef std::vector<int> vi;
typedef std::vector<std::pair<ll,ll>> vpll;
typedef std::vector<std::pair<int,int>> vpii;
typedef std::pair<int,int> pii;
typedef std::pair<ll,ll> pll;
typedef std::pair<int,std::pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b)
{
   return std::ceil(((ld)a)/((ld)b)); 
}

void setIO(std::string name = "") 
{ 
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
        freopen((name+".out").c_str(), "w", stdout);
    }
}

void solve()
{
    ll n; // Number of cows/days
    std::cin >> n;
    
    vll a_orig(n); // Original input array
    input(a_orig);
    
    // --- Calculate Maximum Breakouts (Backward Pass) ---
    // Goal: Maximize 0s by filling -1s consistently when possible, forcing 0s when necessary.
    
    vll a_max_temp = a_orig; // A copy to modify for max_ans calculation
    bool possible_max = true;
    ll max_breakouts = 0;
    
    // Process from right to left
    // should_be_val represents a[i+1]-1, what a[i] should be to be consistent.
    ll should_be_val = -1; // -1 indicates no active dependency from right
    
    for(ll i = n - 1; i >= 0; i--)
    {
        if(a_max_temp[i] != -1) // If a[i] is a known value
        {
            if(should_be_val != -1 && a_max_temp[i] != should_be_val) 
            { // Contradiction: known a[i] is not consistent with a[i+1]-1
                possible_max = false; 
                break;
            }
            should_be_val = a_max_temp[i] - 1; // Update dependency for next left element
        }
        else // If a[i] is -1 (unknown)
        {
            if(should_be_val != -1 && should_be_val >= 0) // Consistent with a[i+1]-1
            {
                a_max_temp[i] = should_be_val; // Fill it consistently
                should_be_val--; // Propagate dependency
            }
            else // No active dependency or dependency would be negative/invalid
            {   // Force a breakout at a[i] (set to 0) to maximize, and reset dependency.
                a_max_temp[i] = 0; 
                should_be_val = a_max_temp[i] - 1; // For next iteration
            }
        }
    }
    
    // After filling, count 0s for max_breakouts if possible
    if (possible_max) {
        for(ll val : a_max_temp) {
            if (val == 0) {
                max_breakouts++;
            }
        }
    }
    
    // --- Calculate Minimum Breakouts (Forward Pass) ---
    // Goal: Minimize 0s by filling -1s consistently as much as possible.

    vll a_min_temp = a_orig; // A copy to modify for min_ans calculation
    bool possible_min = true;
    ll min_breakouts = 0;

    // The very first day (index 0) must have a breakout (value 0) to be consistent.
    // If a_min_temp[0] is known and not 0, it's impossible.
    if (a_min_temp[0] != -1 && a_min_temp[0] != 0) {
        possible_min = false;
    }
    if (possible_min) {
        if (a_min_temp[0] == -1) {
            a_min_temp[0] = 0; // Assume 0 to ensure consistency (minimal choice)
        }
        min_breakouts = 1; // First day always counts as a breakout

        // Process from left to right
        // should_be_val represents a[i-1]+1, what a[i] should be to be consistent.
        ll expected_val_next = 1; // What a[i] should be, relative to a[i-1]
        
        for(ll i = 1; i < n; i++) {
            if (a_min_temp[i] != -1) { // If a[i] is a known value
                if (a_min_temp[i] == 0) { // If it's a known breakout
                    min_breakouts++;
                    expected_val_next = 1; // Reset dependency
                }
                else if (a_min_temp[i] != expected_val_next) { // Contradiction: known a[i] is not consistent
                    possible_min = false; 
                    break;
                }
                else { // Consistent, just update expected for next element
                    expected_val_next++;
                }
            }
            else { // If a[i] is -1 (unknown)
                a_min_temp[i] = expected_val_next; // Fill consistently to minimize 0s
                expected_val_next++; // Propagate dependency
            }
        }
    }

    // Output results
    if (!possible_max || !possible_min) { // If any pass found a contradiction
        std::cout << -1 << "\n";
    }
    else {
        std::cout << min_breakouts << " " << max_breakouts << "\n";
    }
}

int main()
{
    setIO("taming"); // Set up file I/O for USACO problem
    
    ll T = 1; // Number of test cases (usually 1 for USACO problems)
    // std::cin >> T; // Uncomment if multiple test cases are expected
    
    while(T--)
    {
        solve();
    }
    
    return 0;
}
```