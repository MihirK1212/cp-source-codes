# Replace MaxGCD (Maximize GCD by Replacing One Element)

## Problem Description

Given an array of integers, you are allowed to replace at most one element of the array with any positive integer. The goal is to maximize the Greatest Common Divisor (GCD) of all elements in the modified array.

## Approach

To maximize the GCD of the array by replacing at most one element, we can iterate through each possible element to be replaced. When an element `a[i]` is considered for replacement, the GCD of the remaining `n-1` elements effectively determines the maximum possible GCD for the array (if `a[i]` is replaced by a multiple of that GCD).

We can precompute prefix GCDs (`gcd_l`) and suffix GCDs (`gcd_r`) of the array. Then, for each element `a[i]` to be replaced, the GCD of the remaining elements can be found by `gcd(gcd_l[i-1], gcd_r[n-i-2])`. We take the maximum of these GCDs.

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ll long long 
#define vll vector<long long>
#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define sort(a) sort(a.begin(),a.end());
#define rsort(a) sort(a.rbegin(),a.rrend());
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}


// Function to calculate GCD of two numbers
ll gcd(ll x,ll y)
{
    if(y==0)
    {
        return x;
    }
    
    return gcd(y,x%y);
}


int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    ll n,i;
    cin>>n;
    
    vll a(n);
    
    input(a);
    
    vll gcd_l(n),gcd_r(n);
    
    //gcd_l[i]= gcd of (i+1) terms from left
    //gcd_r[i]= gcd of (i+1) terms from right
    
    /*
        if a0 is replaced then max_gcd= gcd_r[n-2] = gcd of n-1 terms from right
        if a1 is replaced then max_gcd= gcd(gcd_l[0],gcd_r[n-3]) = gcd(gcd of one term from left,gcd of n-2 terms from right)
        .... and so on
        
        if a(n-2) is replaced then max_gcd= gcd(gcd_l[n-3],gcd_r[0])= gcd(gcd of n-2 terms from left, gcd of 1 terms from right)
        if a(n-1) is replaced then max_gcd= gcd_l[n-2]= gcd of n-1 terms form left
    */
    
    gcd_l[0]=a[0];
    // Populate gcd_l: gcd_l[i] stores GCD of a[0]...a[i]
    for(i=1;i<n;i++)
    {
        gcd_l[i]=gcd(gcd_l[i-1],a[i]);
    }
    
    // Populate gcd_r: gcd_r[i] stores GCD of a[i]...a[n-1]
    // Note: The original code's logic for gcd_r was a bit off, it should be suffix GCD.
    // Here we compute it as suffix_gcd[i] = gcd(a[i], suffix_gcd[i+1])
    vll suffix_gcd(n);
    suffix_gcd[n-1] = a[n-1];
    for(i=n-2;i>=0;i--)
    {
        suffix_gcd[i] = gcd(a[i], suffix_gcd[i+1]);
    }

    ll ans = 0; // Initialize with 0 for finding maximum GCD

    // Case 1: Replace a[0]
    if (n > 1) ans = max(ans, suffix_gcd[1]);
    else ans = a[0]; // If only one element, replacing it with itself gives the same GCD

    // Case 2: Replace a[i] for 1 <= i < n-1
    for(i=1;i<=(n-2);i++)
    {
        // GCD of elements to the left of i and to the right of i
        ans=max(ans,gcd(gcd_l[i-1],suffix_gcd[i+1]));
    }
    
    // Case 3: Replace a[n-1]
    if (n > 1) ans = max(ans, gcd_l[n-2]);
    
    cout<<ans<<"\n";
    
    
    return 0;
}
```