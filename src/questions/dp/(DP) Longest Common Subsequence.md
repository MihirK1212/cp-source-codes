# Longest Common Subsequence (LCS) - DP

## Problem Description

Given two sequences (arrays or strings), find the length of their longest common subsequence (LCS). A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, if `A = [1, 2, 3, 4]` and `B = [2, 4, 1, 3]`, the LCS could be `[2, 3]` (length 2) or `[2, 4]` (length 2) if order is strict. If `A = "ABCDGH"` and `B = "AEDFHR"`, the LCS is `"ADH"` of length 3.

## C++ Solution

This problem is a classic dynamic programming problem. We define `dp[i][j]` as the length of the Longest Common Subsequence (LCS) of `A[0...i-1]` and `B[0...j-1]`.

**Base Cases:**
- `dp[0][j] = 0`: LCS with an empty prefix of `A` is `0`.
- `dp[i][0] = 0`: LCS with an empty prefix of `B` is `0`.

**Recurrence Relation:**
- If `A[i-1] == B[j-1]` (characters match):
    - `dp[i][j] = dp[i-1][j-1] + 1` (We take this matching character).
- If `A[i-1] != B[j-1]` (characters don't match):
    - `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (We take the maximum of excluding `A[i-1]` or `B[j-1]`).

After filling the `dp` table, the length of the LCS is `dp[n][m]`. The solution also includes logic to reconstruct one of the actual LCS sequences.

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
#define ld long double 
#define vll vector<long long>
#define vi vector<int>
#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long val : arr){cout<<val<<" ";} cout<<"\n"; // Changed to use range-based for loop
#define sort(a) sort(a.begin(),a.end());
#define rsort(a) sort(a.rbegin(),a.rend());
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();


int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    ll T;T=1;
    while(T--)
    {
        ll n,m,i,j;
        
        cin>>n>>m;
        
        vll a(n);
        vll b(m);
        
        input(a);
        input(b);
        
        // dp[i][j] stores the length of LCS of a[0...i-1] and b[0...j-1]
        ll dp[n+1][m+1];
        
        // Initialize dp table with 0s
        memset(dp,0,sizeof(dp));
        
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                // If characters match, increment length from diagonal
                if(a[i-1]==b[j-1])
                {
                    dp[i][j]=dp[i-1][j-1] + 1;
                }
                else // If characters don't match, take max from above or left
                {
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        
        // Reconstruct LCS (one possible LCS if multiple exist)
        i=n; // Start from bottom-right of DP table
        j=m;
        
        vll ans_lcs; // Stores the elements of the LCS
        
        while(i>0 && j>0)
        {
            if(a[i-1]==b[j-1])
            {
                ans_lcs.pb(a[i-1]); // Characters match, add to LCS and move diagonally up-left
                i--;
                j--;
            }
            else
            {
                // If characters don't match, move to the direction from which max length came
                if(dp[i-1][j]>dp[i][j-1]){i--;}
                else{j--;}
            }
        }
        
        std::reverse(ans_lcs.begin(), ans_lcs.end()); // Reverse to get correct order
        cout << "Length of LCS: " << dp[n][m] << "\n";
        cout << "LCS: ";
        printoneline(ans_lcs);
        
    }
    
    return 0;
}
```