# LCM of an Array

## Problem Description

Given an array `a` of `n` positive integers, find the Least Common Multiple (LCM) of all the elements in the array.

The LCM of two numbers `x` and `y` can be calculated using the formula: `LCM(x, y) = (x * y) / GCD(x, y)`, where `GCD` is the Greatest Common Divisor. To find the LCM of an array, we can iteratively apply this formula: `LCM(a1, a2, ..., an) = LCM(LCM(a1, a2, ..., an-1), an)`.

## C++ Solution

This solution first implements the Euclidean algorithm for finding the Greatest Common Divisor (GCD) of two numbers. Then, it uses this `gcd` function to iteratively calculate the LCM of all elements in the input array.

1.  **`gcd(ll x, ll y)` function:**
    *   Implements the Euclidean algorithm recursively to find the GCD of `x` and `y`.
    *   **Base Case:** If `y` is 0, then `GCD(x, 0) = x`.
    *   **Recursive Step:** Otherwise, `GCD(x, y) = GCD(y, x % y)`.

2.  **`main()` function:**
    *   Reads the number of elements `n` and the array `a`.
    *   Initializes `lcm_arr` with the first element `a[0]`.
    *   Iterates from the second element (`i=1`) to the end of the array:
        *   Updates `lcm_arr = (lcm_arr * a[i]) / gcd(lcm_arr, a[i])`. This correctly calculates the LCM of the current `lcm_arr` and the next element `a[i]`.
    *   Prints the final `lcm_arr`.

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
#define rsort(a) sort(a.rbegin(),a.rend());
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}

// Function to find the Greatest Common Divisor (GCD) of two numbers
ll gcd(ll x,ll y)
{
    if(y==0) 
    {
        return x;
    }
    else 
    {
        return (gcd(y,x%y));
    }
}

int main()
{
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    ll n,i;
    cin>>n;
    vll a(n);
    
    input(a); // Read array elements
    
    ll lcm_arr;
    
    // Initialize LCM with the first element
    lcm_arr=a[0];
    
    // Iterate through the rest of the array to calculate LCM
    for(i=1;i<n;i++)
    {
        // LCM(A, B) = (A * B) / GCD(A, B)
        // Ensure multiplication `lcm_arr * a[i]` is done before division to avoid precision issues
        // and handle potential overflow if intermediate product exceeds ll limits.
        // For standard competitive programming, it's often assumed intermediate fits if final fits.
        lcm_arr=(lcm_arr*a[i])/(gcd(lcm_arr,a[i]));
    }
    
    cout<<lcm_arr<<"\n";
    return 0;
}
```