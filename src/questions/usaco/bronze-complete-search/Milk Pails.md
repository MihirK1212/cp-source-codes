# Milk Pails (USACO Bronze)

## Problem Description

This problem is from USACO: [Milk Pails](http://www.usaco.org/index.php?page=viewproblem2&cpid=615).

Farmer John has two milk pails, one with capacity `X` and another with capacity `Y`. He wants to measure exactly `M` units of milk. He can perform any number of filling and emptying operations. The goal is to find the maximum amount of milk less than or equal to `M` that he can measure using these two pails.

## C++ Solution

This solution uses a brute-force approach to find the maximum amount of milk that can be measured, up to `M`. It iterates through all possible combinations of fills from pail `X` and pail `Y` such that the total milk measured does not exceed `M`. The `solve` function iterates backward from `M` down to 1 to find the largest measurable amount.

**Algorithm:**
1.  Initialize `max_milk` to a very small number (e.g., -10).
2.  Outer loop `m` from `M` down to `0`: This `m` represents a potential target amount of milk.
3.  Nested loops `i` and `j`:
    *   `i` represents the number of times pail `X` is used.
    *   `j` represents the number of times pail `Y` is used.
    *   The loops iterate such that `i * X` does not exceed `m`, and `j * Y` does not exceed `m`.
4.  Inside the innermost loop, check if `(i * X) + (j * Y)` is exactly equal to `m`.
    *   If it is, then `m` is a measurable amount. Since we are iterating `m` downwards, the first `m` that satisfies this condition is the maximum possible amount. Store `m` in `max_milk` and break all loops.
5.  Return `max_milk`.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define sort(a) sort(a.begin(),a.end());
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

ll inf=std::numeric_limits<long long>::max();

ll floorVal (ll a,ll b) {return a/b;}
ll ceilVal  (ll a,ll b) {return ceil(((ld)a)/((ld)b)); }

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Function to find the maximum measurable amount of milk up to M
ll solve(ll M,ll X,ll Y)
{
    ll m,i,j;
    ll max_milk = -10; // Initialize with a very small value
    
    // Iterate backwards from M to 1 to find the largest measurable amount
    for(m=M;m>=0;m--) // Iterate through all possible amounts from M down to 0
    {
        // Iterate through possible number of times pail X is filled
        for(i=0;i*X<=m;i++)
        {
            // Iterate through possible number of times pail Y is filled
            for(j=0;j*Y<=m;j++)
            {
                // Check if the current combination (i*X + j*Y) equals 'm'
                if((i*X)+(j*Y)==m)
                {
                    max_milk=m; // Found a measurable amount, which is the largest since we iterate downwards
                    goto end_loops; // Exit all loops
                }
            }
        }
    }
    
end_loops:
    return max_milk;
}

int main()
{
    setIO("pails"); // Set up file I/O for USACO problem
    
    ll X,Y,M; // X: capacity of first pail, Y: capacity of second pail, M: target max milk
    cin>>X>>Y>>M;
    
    cout<<solve(M,X,Y)<<"\n";
    
    return 0;
}
```