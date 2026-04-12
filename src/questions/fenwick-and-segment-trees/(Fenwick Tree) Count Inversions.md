# Fenwick Tree (Binary Indexed Tree) for Counting Inversions

## Problem Description

This code uses a Fenwick Tree (Binary Indexed Tree, or BIT) to efficiently count the number of inversions in an array. An inversion in an array `A` is a pair of indices `(i, j)` such that `i < j` and `A[i] > A[j]`.

The key idea for using a BIT to count inversions is to process the array elements from right to left. For each element `A[i]`, we query the BIT for the number of elements already processed (to its right) that are smaller than `A[i]`. These elements form inversions with `A[i]`.

## C++ Solution

This solution implements a method to count inversions using a Fenwick Tree after coordinate compression of the input array.

**Key Concepts:**
*   **Inversion Count:** The number of pairs `(i, j)` such that `i < j` and `A[i] > A[j]`.
*   **Coordinate Compression:** Since Fenwick Trees work on indices (which must be positive and within a reasonable range), if the input array `A` contains large numbers or negative numbers, we map these values to their ranks in the sorted version of the array. This transforms the values into a 0-indexed (or 1-indexed) range from 1 to `N`, suitable for BIT operations.
*   **Fenwick Tree (BIT):** Used to store frequencies of compressed values.

**Functions:**
*   `getInv(vll& bit, ll index)`: This function is named `getInv` but it essentially performs a `getSum` operation on the BIT. It returns the sum of elements up to `index` (1-based). In the context of inversion counting, it counts how many elements *smaller than or equal to `index`* have already been inserted into the BIT.
*   `update(vll& bit, ll n, ll index)`: This function updates the BIT. It's designed to increment the frequency of the element at `index` (1-based) by 1.

**Algorithm (`main` function):**
1.  **Read Input:**
    *   Read `n` (size of array).
    *   Read `n` elements into `vll a`.
2.  **Coordinate Compression:**
    *   Create a temporary `vll temp = a`.
    *   Sort `temp`.
    *   For each element `a[i]` in the original array, replace it with its 1-based rank in the sorted `temp` array. `a[i] = lower_bound(temp.begin(),temp.end(),a[i])-temp.begin() + 1;`
3.  **Initialize BIT:**
    *   Create `vll bit(n+1, 0)`.
4.  **Count Inversions:**
    *   Initialize `inv = 0`.
    *   Iterate `i` from `n-1` down to `0` (process array from right to left):
        *   `inv += getInv(bit, a[i] - 1)`: Query the BIT to find how many elements *smaller* than `a[i]` have already been processed (are to the right of `a[i]`). These form inversions with `a[i]`. We query `a[i]-1` because `getInv` includes the `index` itself.
        *   `update(bit, n, a[i])`: Insert `a[i]` into the BIT (increment its count).
5.  **Output Result:** Print `inv`.

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
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}\
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
    
    if(name!=\"\")
    {
        freopen((name+\".in\").c_str(), \"r\", stdin);\n\t    freopen((name+\".out\").c_str(), \"w\", stdout);\n    }\n}\n\n// Fenwick Tree (BIT) function to get prefix sum up to 'index' (1-based)
// In the context of inversion counting, this counts elements <= index that have been added.
ll getSum(vll&bit,ll index)\n{\n    ll sum = 0;\n    \n    while(index>0)\n    {\n        sum+=bit[index];\n        index-=index&(-index); // Move to parent node in BIT
    }\n    \n    return sum;\n}\n\n// Fenwick Tree (BIT) function to update element at 'index' (1-based) by +1
// This effectively marks the presence of an element with value 'index'.
void update(vll&bit,ll n_max_val,ll index)\n{\n    while(index<=n_max_val)\n    {\n        bit[index]++; // Increment count for this value
        index+=index&(-index); // Move to next node to update (ancestor)
    }\n}\n\nint main()\n{\n    setIO(\"\"); // Use standard I/O for example/testing
    \n    ll n_array_size,i;
    cin>>n_array_size;
    \n    vll original_array(n_array_size);
    input(original_array); // Read array elements
    \n    // Perform Coordinate Compression:\n    // Map array values to their ranks to handle large numbers or negative numbers,
    // making them suitable for 1-based Fenwick Tree indexing.
    vll temp_array = original_array;
    sort(temp_array.begin(),temp_array.end()); // Sort a copy to find ranks
    
    // Replace each element in 'original_array' with its 1-based rank
    for(i=0;i<n_array_size;i++){
        original_array[i] = lower_bound(temp_array.begin(),temp_array.end(),original_array[i])-temp_array.begin() + 1; 
    } 
    // After this, original_array contains ranks (1 to N)
    
    // Fenwick Tree (BIT) to store frequencies of ranks
    // Size N+1 for 1-based indexing, values from 1 to N_array_size (max rank)
    vll fenwick_tree(n_array_size+1,0); 
    
    ll inversion_count = 0; // Stores the total number of inversions
    
    // Iterate from right to left (n_array_size-1 down to 0)
    for(i=n_array_size-1;i>=0;i--)
    {\
        // For current element original_array[i] (which is its rank):
        // Query BIT to find how many elements *smaller* than original_array[i]
        // have already been processed (i.e., are to its right).
        // These form inversions with original_array[i].
        // We query up to `original_array[i] - 1` because `getSum` is inclusive.
        inversion_count+=getSum(fenwick_tree,original_array[i]-1);
        
        // Add the current element (its rank) to the BIT.
        // This marks its presence for future queries.
        update(fenwick_tree,n_array_size,original_array[i]);
    }\
    \n    cout<<inversion_count<<\"\\n\"; // Output the total inversion count
    \n    return 0;\
}\
```