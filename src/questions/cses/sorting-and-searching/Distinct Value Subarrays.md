# Distinct Value Subarrays (CSES Sorting and Searching)

## Problem Description

This problem is from CSES Problem Set: [Distinct Values in Subarrays](https://cses.fi/problemset/task/2216/).

Given an array of `n` integers, your task is to calculate the number of subarrays that contain only distinct values.

For example, if the array is `[1, 2, 3, 1]`, the subarrays with distinct values are:
`[1]`, `[2]`, `[3]`, `[1]`
`[1, 2]`, `[2, 3]`, `[3, 1]`
`[1, 2, 3]`

Total: 8 subarrays.

## C++ Solution

This C++ solution uses the **sliding window technique** to count the number of subarrays with distinct values. The core idea is to maintain a window `[start, end]` such that all elements within this window are distinct. When a new element is added at `end`:

*   If the element makes the window no longer distinct, we shrink the window from `start` until it becomes distinct again.
*   If the window `[start, end]` is distinct, then all subarrays ending at `end` and starting from any point within `[start, end]` are also distinct. The number of such subarrays is `(end - start + 1)`.

**Algorithm:**

1.  **Initialize:**
    *   `start = 0`, `end = 0` (pointers for the sliding window).
    *   `ans = 0` (total count of distinct subarrays).
    *   `freq`: A `map` to store the frequency of elements within the current window `[start, end]`.
2.  **Sliding Window Loop (`while(end < n)`):**
    *   **Expand Window:** Add `a[end]` to the window.
        *   Increment `freq[a[end]]`.
    *   **Shrink Window (if necessary):** While `freq[a[end]] > 1` (meaning `a[end]` is a duplicate, making the window non-distinct):
        *   Decrement `freq[a[start]]`.
        *   Increment `start`.
    *   **Count Subarrays:** After ensuring the window `[start, end]` has distinct elements, all subarrays ending at `end` and starting from `start` to `end` are distinct. The number of such subarrays is `(end - start + 1)`. Add this to `ans`.
    *   **Move `end`:** Increment `end` to expand the window.

3.  **Return `ans`.

```cpp
#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cmath>
#include<set>
#include<queue>
#include<algorithm>

using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef long long ll;
typedef long double ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();

ll ceilVal(ll a,ll b) {
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") { 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    if(name!="") {
        freopen((name+".in").c_str(), "r", stdin);
        freopen((name+".out").c_str(), "w", stdout);
    }
}

void solve() {
    ll n,i;
    cin>>n;
    vll a(n);
    input(a);

    ll start = 0, end = 0;
    ll ans = 0; // Total count of distinct subarrays

    map<ll, ll> freq; // Frequency map for elements in the current window
    
    while(end < n) {
        // Expand the window by adding a[end]
        freq[a[end]]++;

        // If adding a[end] creates a duplicate, shrink the window from the left
        // until the window [start, end] contains only distinct elements.
        while(freq[a[end]] > 1) {
            freq[a[start]]--;
            start++;
        }

        // After shrinking (if needed), the window [start, end] now has distinct elements.
        // All subarrays ending at 'end' and starting from any point between 'start' and 'end' (inclusive)
        // will have distinct elements. The number of such subarrays is (end - start + 1).
        ans += (end - start + 1);
        
        end++; // Move the end of the window to consider the next element
    }

    cout<<ans<<"\n";
}

int main() {
    setIO("");
    ll T = 1;
    while(T--) {
        solve();
    }
    return 0;
}
```