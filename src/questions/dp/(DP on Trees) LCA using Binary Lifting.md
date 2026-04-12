# LCA using Binary Lifting (DP on Trees)

## Problem Description

This problem involves finding the Lowest Common Ancestor (LCA) of two nodes in a tree using the binary lifting technique. Binary lifting is an efficient method to answer LCA queries and `k`-th ancestor queries in O(log N) time after an O(N log N) preprocessing step.

**Key Concepts:**
*   **LCA:** The lowest common ancestor of two nodes `u` and `v` is the lowest node in the tree that has both `u` and `v` as descendants.
*   **Binary Lifting:** A technique that precomputes ancestors at powers of two (2^0, 2^1, 2^2, ...) for each node. This allows jumping up the tree by arbitrary powers of two to find ancestors or the LCA efficiently.

## C++ Solution

The solution consists of three main parts:

1.  **`preprocess(up, parent, N, LOG)`:**
    *   `up[u][j]` stores the `2^j`-th ancestor of node `u`.
    *   `up[u][0]` is simply the direct parent of `u`.
    *   For `j > 0`, `up[u][j]` is the `2^j`-th ancestor, which is the `2^(j-1)`-th ancestor of the `2^(j-1)`-th ancestor (`up[up[u][j-1]][j-1]`).
    *   This function fills the `up` table in O(N log N) time.
2.  **`findDepths(graph, depth)`:**
    *   Performs a BFS starting from the root (assumed to be node 0) to calculate the depth of each node. `depth[u]` stores the depth of node `u`.
    *   This is an O(N) operation.
3.  **`findLCA(u, v, up, depth, N, LOG)`:**
    *   First, it brings both `u` and `v` to the same depth. If `depth[u] < depth[v]`, `u` and `v` are swapped. Then, `u` is "lifted" up by `depth[u] - depth[v]` steps using binary lifting.
    *   If `u` and `v` become the same node after this (meaning one was an ancestor of the other), that node is the LCA.
    *   Otherwise, both `u` and `v` are lifted simultaneously. Starting from the largest possible jump (`LOG-1` down to `0`), if `up[u][j]` is different from `up[v][j]`, it means their `2^j`-th ancestors are different, so they are lifted to `up[u][j]` and `up[v][j]` respectively. This process continues until `u` and `v` are siblings of the LCA.
    *   Finally, the parent of `u` (or `v`) is the LCA.
    *   This function answers LCA queries in O(log N) time.

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

// Function to preprocess ancestors for binary lifting
// up[u][j] stores the 2^j-th ancestor of node u
void preprocess(vector<vll>&up,vll&parent,ll N,ll LOG)
{
    // Initialize 2^0-th ancestors (direct parents)
    for(ll u=0;u<N;u++){up[u][0]=parent[u];}
    
    // Fill up the 'up' table for higher powers of two
    for(ll j=1;j<LOG;j++)
    {
        for(ll u=0;u<N;u++)
        {
            // If the 2^(j-1)-th ancestor does not exist, then 2^j-th ancestor also does not exist
            if(up[u][j-1]==-1){up[u][j]=-1; continue;}
            
            // The 2^j-th ancestor of u is the 2^(j-1)-th ancestor of the 2^(j-1)-th ancestor of u
            up[u][j] = up[up[u][j-1]][j-1];
        }
    }
}

// Function to find depths of all nodes using BFS
void findDepths(map<ll,vll>&graph,vll&depth)
{
    queue<ll> q;
    q.push(0); // Assuming node 0 is the root
    
    ll d = 0; // Current depth
    vector<bool> visited(graph.size(), false); // To avoid cycles in case of generic graph (though usually a tree)
    
    while(!q.empty())
    {
        ll s = q.size();
        while(s--)
        {
            ll u = q.front(); q.pop();
            depth[u] = d;
            visited[u] = true;
            for(auto v : graph[u]){
                if (!visited[v]) { // Avoid revisiting in case of undirected interpretation or general graph
                    q.push(v);
                }
            }
        }
        d++;
    }
}

// Function to find the Lowest Common Ancestor (LCA) of two nodes u and v
ll findLCA(ll u,ll v,vector<vll>&up,vll&depth,ll N,ll LOG)
{
    // 1. Bring the deeper node up to the same depth as the shallower node
    if(depth[u]<depth[v]){swap(u,v);}
    
    ll k = depth[u]-depth[v]; // Difference in depths
    for(ll j=0;j<LOG;j++)
    {
        if(k&(1<<j)){ // If j-th bit of k is set, jump by 2^j
            u=up[u][j];    
        }
    }
    
    // Now u and v are at the same depth
    
    // If u and v are the same node, then this is the LCA
    if(u==v){return u;}
    
    // 2. Lift both nodes simultaneously until their parents are different
    // Iterate from largest jump size downwards
    for(ll j=LOG-1;j>=0;j--)
    {
        // If their 2^j-th ancestors are different, it means the LCA is further up
        // So, jump both u and v to their 2^j-th ancestors
        if(up[u][j]!=-1 && up[u][j]!=up[v][j]) // We take the maximum possible jump upwards such that paths don't cross
        {
            u = up[u][j];
            v = up[v][j];
        }
    }
    
    // After the loop, u and v are siblings of the LCA.
    // Their direct parent (up[u][0]) is the LCA.
    return up[u][0]; 
}

int main()
{
    setIO(""); // No specific file I/O for this generic template.
    
    ll N,M_edges; // N = number of nodes, M_edges = number of children for a node (not total edges)
    cin>>N;
    
    vll parent(N);
    parent[0]=-1; // Assuming node 0 is the root and has no parent
    
    map<ll,vll> graph; // Adjacency list representation of the tree
    
    ll u,v;
    
    // Read tree structure
    // This input format is unusual: for each node u, it reads M_edges and then M_edges children of u.
    // This implies an adjacency list from parent to child.
    for(u=0;u<N;u++)
    {
        cin>>M_edges; // Number of children for node u
        while(M_edges--)
        {
            cin>>v; // Child node v
            parent[v] = u;
            graph[u].pb(v);
        }
    }
    
    vll depth(N);
    findDepths(graph,depth); // Calculate depths of all nodes
    
    ll LOG=0;
    while((1<<(LOG+1))<=N){LOG++;}
    LOG++; // LOG will be ceil(log2(N))
    
    vector<vll> up(N,vll(LOG)); // `up` table for binary lifting
    preprocess(up,parent,N,LOG); // Precompute ancestors
    
    ll Q; // Number of queries
    cin>>Q;
    
    while(Q--)
    {
        cin>>u>>v; // Query for LCA of u and v
        cout<<findLCA(u,v,up,depth,N,LOG)<<"\n";
    }
	
  
    return 0;
}
```