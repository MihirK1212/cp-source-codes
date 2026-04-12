# Fruit Feast - Method 2 (USACO Gold - Knapsack DP with Extended Euclidean Algorithm)

## Problem Description

This problem is from USACO: [Fruit Feast](http://www.usaco.org/index.php?page=viewproblem2&cpid=574).

Farmer John is trying to reach a certain level of "fullness" `T`. He has two types of fruit, `A` and `B`, which provide `A` and `B` fullness respectively. He can eat any number of fruits of type `A` and type `B`. Additionally, at most once during his feast, he can choose to drink water, which halves his current fullness. The goal is to find the maximum fullness Farmer John can achieve that is less than or equal to `T`.

This solution presents an alternative approach, focusing on dynamic programming coupled with the Extended Euclidean Algorithm to check reachability.

## C++ Solution

This C++ solution uses a combination of dynamic programming and number theory (Extended Euclidean Algorithm for Diophantine equations) to solve the Fruit Feast problem.

**`gcd_extend(ll a, ll b, ll& x, ll& y)` function:**

*   This function implements the Extended Euclidean Algorithm. It calculates `gcd(a, b)` and also finds integers `x` and `y` such that `ax + by = gcd(a, b)`.
*   This is a standard recursive implementation.

**`solution_exists(ll a, ll b, ll c)` function:**

*   This function determines if there exists a non-negative integer solution `(x, y)` for the linear Diophantine equation `ax + by = c`.
*   **Edge Cases:**
    *   Handles trivial cases where `c` is 0, `a`, `b`, or `a+b`.
    *   Handles `a=0` and `b=0` cases. If `c` is also 0, a solution exists; otherwise, no solution.
*   **General Case:**
    1.  Calculates `gcd = gcd_extend(a, b, x, y)`. `x` and `y` are updated by reference to a particular solution of `ax + by = gcd`.
    2.  If `c` is not divisible by `gcd`, then no integer solution exists for `ax + by = c`, so return `false`.
    3.  Otherwise, scale `x` and `y` to find a particular solution for `ax + by = c`: `x = x * (c / gcd)` and `y = y * (c / gcd)`.
    4.  **Adjusting for Non-Negative Solutions:**
        *   If both `x >= 0` and `y >= 0`, a non-negative solution exists, return `true`.
        *   If one of `x` or `y` is negative, we need to adjust them using the general solution form:
            *   `x' = x + k * (b / gcd)`
            *   `y' = y - k * (a / gcd)`
            where `k` is an integer.
        *   The code calculates `k` using `floor` to shift `x` and `y` such that both become non-negative (if possible). It checks if after adjustment, both `x >= 0` and `y >= 0`.

**`solve(ll T, ll A, ll B)` function:**

*   This is the core DP logic for the Fruit Feast problem.
*   `max_reach_from` array: `max_reach_from[i]` stores the maximum fullness reachable starting from fullness `i` *without* drinking water. Initialized such that `max_reach_from[i] = i`.
*   **Backward DP:** It iterates `i` from `T` down to `0`.
    *   If `(i + A)` is within `T`, it updates `max_reach_from[i]` by considering `max_reach_from[i + A]` (eating fruit A).
    *   Similarly, if `(i + B)` is within `T`, it updates `max_reach_from[i]` by considering `max_reach_from[i + B]` (eating fruit B).
    *   This DP computes, for each starting fullness `i`, the maximum fullness reachable `j >= i` by eating more fruits (A or B) without drinking water.
*   **Finding the Answer:**
    *   Initialize `ans = 0`.
    *   Iterates `i` from `0` to `T`.
    *   If `solution_exists(A, B, i)` is true (meaning fullness `i` is reachable by eating fruits without drinking water):
        *   Update `ans` with `max(ans, max_reach_from[i])` (taking `i` without drinking water).
        *   Also update `ans` with `max(ans, max_reach_from[i / 2])`. This considers achieving fullness `i` (without water), then drinking water to become `i/2`, and then eating more fruits to reach `max_reach_from[i/2]` without further water consumption.

**`main()` function:**

*   Sets up fast I/O and file redirection for USACO problems.
*   Reads `T`, `A`, `B`.
*   Calls `solve` and prints the result.

```cpp
#include<iostream>
#include <vector>
#include<string>
#include <map>
#include<cmath>
#include <set>
#include<queue>
#include<algorithm>
#include<cstdlib>
#include<numeric> // For std::gcd in modern C++ (not used in solution, but good to note)
#include<limits> // For std::numeric_limits
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
// #define reverse(a) reverse(a.begin(),a.end()); // Use std::reverse from <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef long long ll;
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
        freopen((name+".out").c_str(), "w", stdout);
    }
}

// Extended Euclidean Algorithm: finds gcd(a, b) and x, y such that ax + by = gcd(a, b)
ll gcd_extend(ll a, ll b, ll& x, ll& y)
{
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    ll g = gcd_extend(b, a % b, x, y);
    ll x1 = x, y1 = y;
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

// Checks if a non-negative integer solution exists for the Diophantine equation ax + by = c
bool solution_exists(ll a, ll b, ll c)
{
    // Handle trivial cases where c can be directly formed
    if (c == 0 || c == a || c == b || c == (a + b)) { return true; }

    // Handle cases where coefficients a or b are zero
    if (a == 0 && b == 0) {
        return (c == 0); // Solution exists only if c is also 0
    }
    if (a == 0) {
        return (c % b == 0 && c / b >= 0); // Check if c is a non-negative multiple of b
    }
    if (b == 0) {
        return (c % a == 0 && c / a >= 0); // Check if c is a non-negative multiple of a
    }

    ll x, y;
    ll common_divisor = gcd_extend(a, b, x, y); // Calculate gcd and initial particular solution

    // If c is not divisible by gcd, no integer solution exists
    if (c % common_divisor != 0) {
        return false;
    }

    // Scale the particular solution (x, y) to satisfy ax + by = c
    x *= (c / common_divisor);
    y *= (c / common_divisor);

    // Adjust x and y to find a non-negative solution if possible
    // General solution: x_k = x + k * (b / gcd), y_k = y - k * (a / gcd)

    // Calculate k to make x non-negative. If b/gcd is positive, we need to increase x.
    // If x is negative, k needs to be at least (-x * gcd / b). 
    // If b/gcd is negative, we need to decrease x. k needs to be at most (-x * gcd / b).
    // A safe way to find a k that makes x non-negative:
    ll k_for_x_pos = 0;
    if (common_divisor != 0) { // Avoid division by zero if gcd is 0 (should not happen for a,b > 0)
        ll kb = b / common_divisor;
        if (kb != 0) {
            k_for_x_pos = (x < 0) ? ((-x + kb - 1) / kb) : 0;
        }
    }
    
    ll test_x = x + k_for_x_pos * (b / common_divisor);
    ll test_y = y - k_for_x_pos * (a / common_divisor);

    if (test_x >= 0 && test_y >= 0) {
        return true;
    }

    // Re-evaluate the bounds for k to guarantee non-negative x and y
    // For this specific problem where A, B are positive fruit values, A and B are > 0.
    // x = x_0 + k*(B/gcd)
    // y = y_0 - k*(A/gcd)
    // We need x >= 0 and y >= 0.
    // x_0 + k*(B/gcd) >= 0  => k*(B/gcd) >= -x_0 => k >= -x_0*gcd/B
    // y_0 - k*(A/gcd) >= 0  => y_0 >= k*(A/gcd)  => k <= y_0*gcd/A
    // So we need to find if there is an integer k in [ceil(-x_0*gcd/B), floor(y_0*gcd/A)]
    
    // Recalculate x,y for the original equation ax+by=c (as they might have been modified in the previous block)
    ll orig_x, orig_y;
    gcd_extend(a, b, orig_x, orig_y);
    orig_x *= (c / common_divisor);
    orig_y *= (c / common_divisor);

    ll k_low = (ll)ceil((ld)(-orig_x) / (b / common_divisor));
    ll k_high = (ll)floor((ld)orig_y / (a / common_divisor));
    
    return k_low <= k_high;
}

// Main function to solve the Fruit Feast problem
ll solve(ll T, ll A, ll B)
{
    ll i;

    // max_reach_from[i] stores the maximum fullness reachable starting from fullness 'i'
    // without drinking water after this point. Initialized such that max_reach_from[i] = i.
    vll max_reach_from(T + 1);
    for(i=0; i<=T; i++){max_reach_from[i] = i;}

    // Backward DP: Compute max_reach_from[i]
    // For each fullness 'i', consider eating fruit A or B to reach a higher fullness.
    // This ensures that max_reach_from[i] reflects the maximum fullness achievable 
    // from 'i' by adding fruits, without considering the water-drinking operation.
    for(i=T; i>=0; i--)
    {
        if((i + A) <= T)
        {
            max_reach_from[i] = max(max_reach_from[i], max_reach_from[i + A]);
        }
        if((i + B) <= T)
        {
            max_reach_from[i] = max(max_reach_from[i], max_reach_from[i + B]);
        }
    }

    ll ans = 0; // Stores the overall maximum reachable fullness

    // Iterate through all possible fullness values 'i' up to T
    for(i=0; i<=T; i++)
    {
        // If fullness 'i' is reachable by eating fruits (without water, initially)
        if(solution_exists(A, B, i))
        {
            // Case 1: Don't drink water at all, just eat fruits to reach 'i'.
            // We can then eat more fruits to reach max_reach_from[i].
            ans = max(ans, max_reach_from[i]); 

            // Case 2: Reach fullness 'i', drink water to become 'i/2', then eat more fruits.
            // The maximum fullness after drinking water and eating more fruits is max_reach_from[i/2].
            ans = max(ans, max_reach_from[i / 2]);
        }
    }

    return ans;
}

// Problem link for reference
// http://www.usaco.org/index.php?page=viewproblem2&cpid=574

int main()
{
    setIO("feast"); // Set up file I/O for USACO problem
    // srand((unsigned) time(NULL)); // Seeding random number generator (not directly used for problem logic)

    ll T,A,B;
    cin>>T>>A>>B;

    cout<<solve(T,A,B)<<"\n";
    return 0;
}
```