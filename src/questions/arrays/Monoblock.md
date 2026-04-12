# Monoblock (Codeforces)

## Problem Description

This problem is from Codeforces: [Monoblock](https://codeforces.com/contest/1715/problem/C).

Given an array `a` of `n` integers, a "joint" is defined at index `i` (where `1 <= i < n`) if `a[i] != a[i-1]`. For any subarray `a[l...r]`, if the number of joints within the range `(l+1)...r` (i.e., indices `k` such that `l < k <= r` and `a[k] != a[k-1]`) is `x`, then the "awesomeness" of this subarray is `x+1`.

The initial task is to calculate the sum of awesomeness over all possible subarrays. Additionally, there are `m` queries. Each query involves updating an element at a given index `ind` to a new value `x`. After each update, the sum of awesomeness over all subarrays must be recalculated and printed.

## C++ Solution

The key insight to solving this problem efficiently, especially with updates, is to understand how the total awesomeness sum can be decomposed. The awesomeness of a subarray is `(number of joints in its internal range) + 1`. Summing this over all subarrays:

`Total Awesomeness = Sum(x+1 for all subarrays) = Sum(x for all subarrays) + Sum(1 for all subarrays)`

`Sum(1 for all subarrays)` is simply the total number of subarrays, which is `n * (n+1) / 2`.

`Sum(x for all subarrays)`: This is the sum of the number of joints across all subarrays. This can be rephrased as: for each potential joint at index `i`, how many subarrays contain this joint? A joint at index `i` (where `a[i] != a[i-1]`) is part of any subarray `a[l...r]` where `l <= i-1` and `r >= i`. The number of choices for `l` is `i` (from `0` to `i-1`) and for `r` is `(n-i)` (from `i` to `n-1`). So, a joint at index `i` contributes `i * (n-i)` to `Sum(x for all subarrays)`.

Therefore, the overall formula for the sum of awesomeness is:

`Total Awesomeness = (n * (n+1) / 2) + Sum(i * (n-i) for all i where a[i] != a[i-1])`

**Handling Updates:**

When an element `a[ind]` is updated, only the joints directly affected by `a[ind]` need to be re-evaluated. These are the potential joints at `ind` and `ind+1` (and `ind-1` if `a[ind-1]` is involved in a joint with `a[ind]`, which is covered by index `ind`). Specifically, only the joint status at `ind` (comparing `a[ind]` and `a[ind-1]`) and `ind+1` (comparing `a[ind+1]` and `a[ind]`) can change.

To update efficiently:

1.  **Subtract Old Contributions:** Before updating `a[ind]`, check the joint status at `ind` and `ind+1`. If they were joints, subtract their old contributions (`k * (n-k)`) from the running `count` (which stores `Sum(i * (n-i))`).
2.  **Update `a[ind]`:** Change `a[ind]` to its new value `x`.
3.  **Add New Contributions:** After updating `a[ind]`, re-check the joint status at `ind` and `ind+1` with the new value. If they are now joints, add their new contributions to `count`.

**`subtract(std::vector<bool>& isJoint, ll ind, ll& count, ll n)` function:**

*   Removes the contribution of a joint at `ind` from `count` if `isJoint[ind]` is `true`.
*   Resets `isJoint[ind]` to `false`.

**`add(std::vector<ll>& a, std::vector<bool>& isJoint, ll ind, ll& count, ll n)` function:**

*   Checks if `ind` is a valid joint (`ind > 0 && a[ind] != a[ind-1]`).
*   If it is, marks `isJoint[ind]` as `true` and adds its contribution `ind * (n-ind)` to `count`.

**Main Loop:**

*   Calculates the initial `tot = n * (n+1) / 2` (total number of subarrays).
*   Initializes `count` by iterating through the array and finding initial joints.
*   For each query:
    *   Reads `ind` and `x`.
    *   Adjusts `ind` to be 0-indexed.
    *   Calls `subtract` for `ind` and `ind+1` (and `ind-1`, though `ind` handles the `a[ind-1]` vs `a[ind]` change).
    *   Updates `a[ind] = x`.
    *   Calls `add` for `ind` and `ind+1` (and `ind-1`).
    *   Prints `count + tot`.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // For std::vector
#include <algorithm> // For std::min, std::max
#include <limits>    // For std::numeric_limits<long long>::max

// Commonly used in competitive programming for brevity, but explicit std:: is more robust
// using namespace std;

// Using long long for large numbers in competitive programming
typedef long long ll;
typedef std::vector<ll> vll;

// Function to remove the contribution of a potential joint at 'ind' from the total 'count'
// isJoint: boolean vector tracking if an index is a joint
// ind: the index to check (1-indexed for joint definition)
// count: reference to the total sum of joint contributions
// n: size of the array
void subtract(std::vector<bool>& isJoint, ll ind, ll& count, ll n)
{
    // Joints are defined for 1 <= i < n, so index `ind` must be in [1, n-1]
    if(ind <= 0 || ind >= n){ return; }
    
    if(isJoint[ind]) // If it was a joint, subtract its contribution
    {
        count -= (ind * (n - ind));
    }
    
    isJoint[ind] = false; // Mark it as no longer a joint (or reset before re-evaluation)
}

// Function to add the contribution of a potential joint at 'ind' to the total 'count'
// a: the array of numbers
// isJoint: boolean vector tracking if an index is a joint
// ind: the index to check (1-indexed for joint definition)
// count: reference to the total sum of joint contributions
// n: size of the array
void add(vll& a, std::vector<bool>& isJoint, ll ind, ll& count, ll n)
{
    // Joints are defined for 1 <= i < n, so index `ind` must be in [1, n-1]
    if(ind <= 0 || ind >= n){ return; }
    
    // If a[ind] is different from a[ind-1], then it's a joint
    if(a[ind] != a[ind-1])
    {
        isJoint[ind] = true; // Mark it as a joint
        count += (ind * (n - ind)); // Add its contribution
    }
}

int main()
{
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);
    
    ll n, m; // n: array size, m: number of queries
    std::cin >> n >> m;
    
    vll a(n); // The input array
    // Read array elements
    for(ll i = 0; i < n; i++){ std::cin >> a[i]; }
    
    // isJoint[i] is true if index i is a joint (a[i] != a[i-1])
    std::vector<bool> isJoint(n, false);
    
    // Calculate total number of subarrays, which is Sum(1 for all subarrays)
    ll total_subarrays_count = (n * (n + 1)) / 2;
    
    ll current_joints_contribution_sum = 0; // Stores Sum(i * (n-i) for all joints)
    
    // Calculate initial joints and their contributions
    for(ll i = 1; i < n; i++) // Iterate from index 1 to n-1 for joints
    {
        if(a[i] != a[i-1])
        {
            isJoint[i] = true;
            current_joints_contribution_sum += (i * (n - i));
        }
    }
    
    // Process queries
    while(m--)
    {
        ll ind, x; // ind: 1-indexed position, x: new value
        std::cin >> ind >> x;
        ind--; // Convert to 0-indexed
        
        // Before updating a[ind], subtract contributions of affected joints:
        // 1. Joint at `ind` (comparison a[ind] vs a[ind-1])
        // 2. Joint at `ind+1` (comparison a[ind+1] vs a[ind])
        // The subtract function handles boundary checks internally (ind<=0 or ind>=n).
        subtract(isJoint, ind, current_joints_contribution_sum, n);
        subtract(isJoint, ind + 1, current_joints_contribution_sum, n);

        // Update the array element
        a[ind] = x;
        
        // After updating a[ind], add new contributions of affected joints:
        // 1. Joint at `ind` (new comparison a[ind] vs a[ind-1])
        // 2. Joint at `ind+1` (new comparison a[ind+1] vs a[ind])
        // The add function handles boundary checks internally.
        add(a, isJoint, ind, current_joints_contribution_sum, n);
        add(a, isJoint, ind + 1, current_joints_contribution_sum, n);
        
        // The final answer is the sum of total subarrays and the sum of contributions from all joints.
        std::cout << current_joints_contribution_sum + total_subarrays_count << "\n";
    }
    
    return 0;
}
```