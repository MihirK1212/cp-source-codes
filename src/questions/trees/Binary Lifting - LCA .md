# Binary Lifting - Lowest Common Ancestor (LCA)

## Problem Description

Given a tree, the task is to find the Lowest Common Ancestor (LCA) of two given nodes `u` and `v`. The LCA of two nodes `u` and `v` is the lowest (deepest) node in the tree that has both `u` and `v` as descendants (where a node can be a descendant of itself).

This problem is efficiently solved using the Binary Lifting technique, which allows querying ancestors at powers of 2 (2^0, 2^1, 2^2, ..., 2^LOG).

## C++ Solution

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

// Precomputes the ancestors for binary lifting. up[u][j] stores the (2^j)-th ancestor of node u.
void preprocess(vector<vll>&up,vll&parent,ll N,ll LOG)
{
    // Initialize 2^0 ancestor (direct parent)
    for(ll u=0;u<N;u++){up[u][0]=parent[u];}
    
    // Compute 2^j ancestors using previously computed 2^(j-1) ancestors
    for(ll j=1;j<LOG;j++)
    {
        for(ll u=0;u<N;u++)
        {
            if(up[u][j-1]==-1) // If 2^(j-1)-th ancestor doesn't exist
            {
                up[u][j]=-1; 
                continue;
            }
            
            // The 2^j-th ancestor of u is the 2^(j-1)-th ancestor of u's 2^(j-1)-th ancestor
            up[u][j] = up[up[u][j-1]][j-1];
        }
    }
}

// Computes the depth of each node from the root using BFS.
void findDepths(map<ll,vll>&graph,vll&depth)
{
    queue<ll> q;
    q.push(0); // Assuming node 0 is the root
    
    ll d = 0; // Current depth
    
    while(!q.empty())
    {
        ll s = q.size();
        while(s--)
        {
            ll u = q.front(); q.pop();
            depth[u] = d; // Set depth of current node
            for(auto v : graph[u]){q.push(v);} // Add children to queue
        }
        d++; // Increment depth for the next level
    }
}

// Finds the LCA of nodes u and v using binary lifting.
ll findLCA(ll u,ll v,vector<vll>&up,vll&depth,ll N,ll LOG)
{
    // 1. Ensure u is deeper than or at the same depth as v
    if(depth[u]<depth[v]){swap(u,v);}
    
    // 2. Lift u to the same depth as v
    ll k = depth[u]-depth[v]; // Difference in depths
    for(ll j=0;j<LOG;j++)
    {
        if(k&(1<<j)) // If the j-th bit is set in k, jump up by 2^j
        {
            u=up[u][j];    
        }
    }
    
    // If u and v are now the same node, it is the LCA
    if(u==v){return u;}
    
    // 3. Lift u and v simultaneously until their parents are the same
    // This loop starts from the largest jump and goes down
    for(ll j=LOG-1;j>=0;j--)
    {
        // If their 2^j-th ancestors are different, both can jump up
        if(up[u][j]!=-1 && up[u][j]!=up[v][j]) 
        {
            u = up[u][j];
            v = up[v][j];
        }
    }
    
    // After the loop, u and v are children of the LCA
    return up[u][0]; // Return the direct parent of u (which is also the parent of v)
}

int main()
{
    setIO("");
    
    ll N; // Number of nodes
    cin>>N;
    
    vll parent(N); // Stores the direct parent of each node
    parent[0]=-1; // Assuming node 0 is the root, it has no parent
    
    map<ll,vll> graph; // Adjacency list to represent the tree (for BFS to find depths)
    
    ll u_node, num_children;
    
    // Read tree structure (parent array and adjacency list)
    for(u_node=0;u_node<N;u_node++)
    {
        cin>>num_children;
        while(num_children--)
        {
            ll v_node;
            cin>>v_node;
            parent[v_node] = u_node; // Set parent of child node v_node to u_node
            graph[u_node].pb(v_node); // Add v_node as a child of u_node
        }
    }
    
    vll depth(N); // Stores the depth of each node
    findDepths(graph,depth);
    
    // Calculate LOG: ceil(log2(N))
    ll LOG=0;
    while((1<<(LOG+1))<=N){LOG++;}
    LOG++;
    
    vector<vll> up(N,vll(LOG)); // up[u][j] stores the 2^j-th ancestor of u
    preprocess(up,parent,N,LOG);
    
    ll Q; // Number of queries
    cin>>Q;
    
    while(Q--)
    {
        ll u_query, v_query;
        cin>>u_query>>v_query;
        cout<<findLCA(u_query,v_query,up,depth,N,LOG)<<"\n";
    }
	
  
    return 0;
}
```