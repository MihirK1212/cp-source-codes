# Fenwick Tree (Binary Indexed Tree) for Prefix Sum Queries and Updates

## Problem Description

This code implements a Fenwick Tree (also known as a Binary Indexed Tree, or BIT) to efficiently handle two types of operations on an array:

1.  **Prefix Sum Queries**: Calculate the sum of elements from the beginning of the array up to a given index `i` (inclusive).
2.  **Point Updates**: Update the value of an element at a given index `i`.

Both operations have a time complexity of O(log N), where `N` is the size of the array, making it much faster than a naive array for scenarios with many updates and queries.

## C++ Solution

This solution provides a standard implementation of a Fenwick Tree (BIT) in C++.

**Key Concepts:**
*   **Fenwick Tree (BIT):** A data structure that can efficiently update elements and calculate prefix sums in logarithmic time. It works by representing the array as a tree-like structure where each node stores the sum of a range of elements. The indices in a BIT are typically 1-based.
*   **Low-bit Trick (`index & (-index)`):** This operation finds the least significant set bit (rightmost '1' bit) of `index`. It's crucial for navigating the tree structure of the BIT.

**Functions:**
*   `getSum(vll& bit, ll index)`:
    *   Takes a 0-based `index`, converts it to 1-based by `index++`.
    *   Iteratively adds `bit[index]` to `sum` and moves `index` to its parent (`index -= index & (-index)`).
    *   Returns the prefix sum `a[0] + ... + a[index-1]`.
*   `update(vll& bit, ll n, ll index, ll val)`:
    *   Takes a 0-based `index`, converts it to 1-based by `index++`.
    *   Iteratively adds `val` to `bit[index]` and moves `index` to its next node to update (`index += index & (-index)`). This propagates the update upwards in the tree structure.
*   `constructBIT(vll& a, vll& bit, ll n)`:
    *   Initializes the `bit` array from a given array `a`. It iterates through `a` and calls `update` for each element.

**Main Function Example Usage:**
1.  Reads `n` (size of array) and `vll a` (the initial array).
2.  Initializes `vll bit(n+1, 0)`.
3.  Calls `constructBIT(a, bit, n)` to build the BIT.
4.  Prints the sum of `a[0...3]` using `getSum(bit, 3)`.
5.  Performs example `update` operations.
6.  Prints the sum of `a[0...4]` after updates using `getSum(bit, 4)`.

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
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
// #define sort(a) sort(a.begin(),a.end()); // Already exists in <algorithm>
#define reverse(a) reverse(a.begin(),a.end()); // Already exists in <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max(); // Using std::numeric_limits for infinity

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Function to get the prefix sum up to 'index' (0-based)
ll getSum(vll&bit,ll index)
{
    ll sum = 0;
    
    index++; // Convert to 1-based indexing for BIT operations
    while(index>0)
    {
        sum+=bit[index];
        index-=index&(-index); // Move to the parent node in the Fenwick Tree structure
    }
    
    return sum;
}

// Function to update the value at 'index' (0-based) by 'val'
void update(vll&bit,ll n,ll index,ll val)
{
    index++; // Convert to 1-based indexing for BIT operations
    while(index<=n) // Iterate up to the size of the array
    {
        bit[index]+=val;
        index+=index&(-index); // Move to the next relevant node to update (ancestor)
    }
}

// Function to construct the Fenwick Tree from an initial array 'a'
void constructBIT(vll&a,vll&bit,ll n)
{
    for(ll i=0;i<n;i++){
        update(bit,n,i,a[i]); // Update the BIT for each element in 'a'
    }
}

int main()
{
    setIO(""); // Use standard I/O for example/testing
    
    ll n_size; // Size of the array
    cin>>n_size;
    
    vll initial_array(n_size);
    input(initial_array); // Read initial array elements
    
    vll fenwick_tree(n_size+1,0); // Fenwick Tree (1-indexed, so size n+1)
    
    constructBIT(initial_array,fenwick_tree,n_size); // Build the BIT
    
    cout<<"Sum a[0...3]: "<<getSum(fenwick_tree,3)<<"\n"; // Example: get sum a[0]...a[3]
    
    update(fenwick_tree,n_size,0,-2); // Example update: decrement a[0] by 2
    update(fenwick_tree,n_size,2,3);  // Example update: increment a[2] by 3
    
    cout<<"Sum a[0...4] after updates: "<<getSum(fenwick_tree,4)<<"\n"; // Example: get sum a[0]...a[4]
  
    return 0;
}
```