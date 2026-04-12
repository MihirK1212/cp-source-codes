# Optimal DSU (Disjoint Set Union) with Path Compression and Union by Rank

## Problem Description

This implementation provides an optimized Disjoint Set Union (DSU) data structure, also known as Union-Find. It includes two key optimizations:

1.  **Path Compression**: Flattens the structure of the tree by making every node in the path from a node to the root directly point to the root. This significantly reduces the time complexity of future `find` operations.
2.  **Union by Rank (or Size)**: Attaches the smaller tree under the root of the larger tree. This ensures that the tree height remains small, further optimizing the `union` operation.

These optimizations make DSU operations (find and union) nearly constant time on average (amortized O(α(N)), where α is the inverse Ackermann function, which grows extremely slowly).

## C++ Implementation

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
#define sort(a) sort(a.begin(),a.end());
#define reverse(a) reverse(a.begin(),a.end());
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}
#define cy cout<<"YES\n";
#define cn cout<<"NO\n";
#define cig cin.ignore();
typedef vector<pair<ll,ll>> vpll;
typedef vector<pair<int,int>> vpii;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<int,pair<int,int>> ppi;

ll inf=std::numeric_limits<long long>::max();

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Find operation with path compression
ll find(vll&parent,ll x)
{
    if(x==parent[x]){return x;}
    
    parent[x] = find(parent,parent[x]); // Path compression: Make root of x as parent of x
    return parent[x];
}

// Union operation by rank
void unionDSU(vll&parent,vll&rank,ll x,ll y)
{
    ll x_rep = find(parent,x);
    ll y_rep = find(parent,y);
    
    if(x_rep==y_rep){return;} // Both elements already have the same root (are in the same set)
    
    // Union by rank: Attach the smaller height tree as a child of the larger height tree
    // This keeps the overall tree height minimal.
    if(rank[x_rep]>rank[y_rep]){parent[y_rep] = x_rep;}
    else if(rank[x_rep]<rank[y_rep]){parent[x_rep] = y_rep;}
    else{parent[y_rep] = x_rep; rank[x_rep]++;} // If ranks are equal, increment rank of new root
}

// Checks if two elements are in the same set
bool sameSet(vll&parent,ll x,ll y)
{
    return find(parent,x) == find(parent,y);
}

int main()
{
    setIO("");
    
    ll n = 4; // Elements belong to the set 0,1,....(n-1)
    
    vll parent(n);
    for(ll i=0;i<n;i++){parent[i] = i;} // Initialize: Each node is its own parent
    
    vll rank(n,0); // Initialize rank to 0 for all nodes
    
    unionDSU(parent,rank,0,2);
    // Note: The original code had unionDSU(parent,rank,2,4); which would be out of bounds for n=4.
    // Assuming for a valid execution, either n should be larger or this line should be adjusted.
    // For demonstration purposes with n=4, an element like 3 would be valid.
    unionDSU(parent,rank,1,3);
    
    // Example usage and output (adjusting for n=4 bounds, assuming element 4 is illustrative):
    // The following line would cause an out of bounds access if n is indeed 4 and element 4 is used.
    // cout<<sameSet(parent,0,4)<<" "<<sameSet(parent,0,1)<<" "<<sameSet(parent,0,2)<<" "<<sameSet(parent,2,3)<<"\n";
    // A corrected example output for n=4, using valid indices:
    cout << sameSet(parent,0,2) << " " << sameSet(parent,0,1) << " " << sameSet(parent,1,3) << "\n";

    return 0;
}
```