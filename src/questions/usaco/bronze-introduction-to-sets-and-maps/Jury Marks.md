# Jury Marks (USACO Bronze)

## Problem Description

This problem is from USACO, typically involving two sets of scores or marks, say `A` and `B`.
*   `A`: `m` marks given by the `m` jury members.
*   `B`: `n` marks received by `n` contestants.

The problem asks to find how many possible values for the "first mark" (let's say, `b[0]` from the contestants' perspective) exist such that the relative differences between contestant marks `b[i] - b[0]` can be explained by the relative differences between prefix sums of jury marks `p_sum[j] - p_sum[first_jury_mark_idx]`.

More formally, we need to find the number of distinct `f0` (index of the jury mark that aligns with the first contestant mark `b[0]`) such that for all `i` from `1` to `n-1`, there exists a unique prefix sum `p_sum[j]` (where `p_sum[j]` is a sum of some subset of `a` starting from `a[0]`) such that `b[i] - b[0] = p_sum[j] - p_sum[f0]`. This simplifies to `b[i] + p_sum[f0] - b[0] = p_sum[j]`. We are looking for values of `b[0]` that satisfy this.

## C++ Solution

This solution uses prefix sums and hash maps (`std::map<ll, bool>`) to efficiently check if a set of relative contestant scores can be matched by a set of relative jury prefix sums.

**Algorithm:**
1.  **Read Input:**
    *   Read `m` (number of jury marks) and `n` (number of contestant marks).
    *   Read the `m` jury marks into `vll a`.
    *   Read the `n` contestant marks into `vll b`.
2.  **Precompute Jury Prefix Sums:**
    *   Create `vll p_sum(m)` to store prefix sums of `a`.
    *   Create `map<ll, bool> exists_psum` to quickly check if a specific prefix sum exists among the jury marks.
    *   Calculate `p_sum[i] = a[0] + ... + a[i]` and populate `exists_psum`.
3.  **Iterate through Possible Alignments (`f0`):**
    *   Initialize `ans = 0`.
    *   Create `map<ll, bool> taken_psum0` to ensure that each *distinct* prefix sum `p_sum[f0]` is considered as the "first jury mark alignment" only once.
    *   Loop `f0` from `0` to `m-1`: `f0` represents the index of the jury mark (or the prefix sum `p_sum[f0]`) that corresponds to `b[0]`.
        *   If `p_sum[f0]` has already been considered as the starting alignment, `continue`.
        *   Mark `p_sum[f0]` as taken for the initial alignment.
        *   Create `map<ll, bool> taken_psum` for the *current* `f0` iteration to ensure that each required jury prefix sum (`req_psum`) is used only once to match a `b[i]`.
        *   Mark `p_sum[f0]` as taken in `taken_psum`.
        *   Set `bool check = true`.
        *   **Check Remaining Contestant Marks:** Loop `i` from `1` to `n-1`:
            *   Calculate the `required_prefix_sum` from the jury marks: `req_psum = b[i] - b[0] + p_sum[f0]`. This `req_psum` is the target prefix sum of jury marks that should match the current contestant mark `b[i]`.
            *   **Validation:**
                *   If `req_psum` does not exist in `exists_psum` OR `req_psum` has already been used in this `f0` iteration (`taken_psum[req_psum]`), then this `f0` is invalid. Set `check = false` and `break`.
                *   Otherwise, mark `taken_psum[req_psum] = true`.
        *   If `check` is still `true` after iterating all `b[i]`, then this `f0` (or `p_sum[f0]`) is a valid alignment, so increment `ans`.
4.  **Output Result:** Print `ans`.

```cpp
#include <bits/stdc++.h>
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
typedef long double  ld;
typedef vector<long long> vll;
typedef vector<int> vi;
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max(); // Using std::numeric_limits for infinity

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

// Custom comparison function (present but not used in main)
bool comp(vll&x,vll&y){return x[0]<y[0];}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); // Faster I/O
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin); // Redirect input
	    freopen((name+".out").c_str(), "w", stdout);
    }
}


int main()
{
    setIO(""); // Use standard I/O if no specific file required
    
    ll m,n,i,f0; // m: num jury marks, n: num contestant marks, i: loop var, f0: index for first jury mark
    
    cin>>m>>n;
    
    vll a(m); // Jury marks
    input(a);
    
    vll b(n); // Contestant marks
    input(b);
    
    // map to quickly check if a prefix sum exists
    map<ll,bool> exists_psum;
    vll p_sum(m); // Prefix sums of jury marks
    ll curr_sum = 0;
    for(i=0;i<m;i++){
        curr_sum+=a[i]; 
        exists_psum[curr_sum]=true; // Mark this prefix sum as existing
        p_sum[i]=curr_sum; // Store prefix sum
    }
    
    ll ans = 0; // Final count of possible values for the first mark
    
    // map to keep track of which p_sum[f0] values have been considered as the starting point
    map<ll,bool> taken_psum0; 
    
    // Iterate through all possible starting jury prefix sums (p_sum[f0])
    for(f0=0;f0<m;f0++)
    {
        // If this p_sum[f0] has already been used as a reference point, skip to avoid duplicate counts
        if(taken_psum0[p_sum[f0]]){continue;}
        taken_psum0[p_sum[f0]] = true; // Mark as taken for initial alignment
        
        // map to ensure each required prefix sum for current f0 is unique
        map<ll,bool> taken_psum; 
        taken_psum[p_sum[f0]] = true; // The starting prefix sum is "taken" for this check
        
        bool check = true; // Flag to indicate if current f0 is a valid alignment
        
        // Check if remaining contestant marks can be explained by unique jury prefix sums
        for(i=1;i<n;i++)
        {
            // Calculate the required jury prefix sum (req_psum) for b[i]
            // based on the relative difference from b[0] and p_sum[f0]
            ll req_psum = b[i] - b[0] + p_sum[f0]; 
            
            // If the required prefix sum does not exist among jury prefix sums
            // OR if it has already been used for a previous b[j] in this iteration,
            // then this f0 alignment is invalid.
            if(!exists_psum[req_psum] || taken_psum[req_psum] ){P
                check = false; 
                break; // Exit inner loop
            }
            
            taken_psum[req_psum] = true; // Mark this required prefix sum as used
        }
        
        if(check){ans++;} // If all checks passed, increment the answer
    }
    
    cout<<ans<<"\n"; // Output the final count
    
    return 0;
}
```