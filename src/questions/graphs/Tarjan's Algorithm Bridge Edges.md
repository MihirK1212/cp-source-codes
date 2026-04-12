# Tarjan's Algorithm: Bridge Edges

## Problem Description

This problem involves finding bridge edges in an undirected graph using a Depth First Search (DFS) based algorithm, often referred to as Tarjan's algorithm or a variation of it. A **bridge** (or **cut edge**) is an edge whose removal increases the number of connected components in the graph. The algorithm uses discovery times and low-link values (minimum reachable time) to identify such edges.

## C++ Solution

This C++ solution implements a variant of Tarjan's algorithm to find bridge edges in an undirected graph.

**Key Concepts:**

*   **Discovery Time (`discTime`):** `discTime[u]` stores the discovery time of node `u`, i.e., the time when `u` was first visited during DFS.
*   **Low-Link Value (`minChildTime`):** `minChildTime[u]` stores the lowest discovery time reachable from node `u` (including `u` itself) through the DFS tree and at most one back-edge.
*   **Bridge Condition:** An edge `(u, v)` is a bridge if `minChildTime[v] > discTime[u]`. This means that `v` and all its descendants in the DFS tree cannot reach `u` or any ancestor of `u` (other than `u` itself) via a back-edge. Therefore, removing `(u, v)` would disconnect `v`'s subtree from the rest of the graph.

**`dfs(vector<vll>& graph, ll u, vector<bool>& visited, ll parent, vll& discTime, vll& minChildTime, ll& t)` function:**

*   This is the recursive DFS function that performs the bridge detection.
*   **Parameters:**
    *   `graph`: Adjacency list representation of the graph.
    *   `u`: Current node being visited.
    *   `visited`: Boolean array to keep track of visited nodes.
    *   `parent`: The parent of `u` in the DFS tree (used to avoid treating the edge to parent as a back-edge).
    *   `discTime`: Discovery times for nodes.
    *   `minChildTime`: Low-link values for nodes.
    *   `t`: A global timer to assign discovery times.
*   **Logic:**
    1.  Mark `u` as visited.
    2.  Set `discTime[u]` and `minChildTime[u]` to the current time `t`, then increment `t`.
    3.  For each neighbor `v` of `u`:
        *   If `v` is the `parent` of `u`, continue (ignore the edge back to parent).
        *   If `v` is not visited:
            *   Recursively call `dfs(graph, v, ...)`. If this recursive call returns `true` (meaning a bridge was found in `v`'s subtree), propagate `true` up.
            *   Update `minChildTime[u]` with `min(minChildTime[u], minChildTime[v])`. This incorporates the lowest reachable time from `v`'s subtree.
            *   **Bridge Check:** If `minChildTime[v] > discTime[u]`, then `(u, v)` is a bridge. Return `true`.
        *   If `v` is visited (and not the parent, so it's a back-edge):
            *   Update `minChildTime[u]` with `min(minChildTime[u], discTime[v])`. This means `u` can reach `v` (an ancestor) through a back-edge, so its low-link value can be updated.
*   Returns `true` if a bridge is found in the current component, `false` otherwise.

**`solve()` function:**

*   Reads the number of nodes `n` and edges `m`.
*   Handles edge case `n=0` and `m=0`.
*   Builds the adjacency list `graph` for the undirected graph.
*   Initializes `visited`, `discTime`, `minChildTime` arrays.
*   Initializes `t = 1` (time counter).
*   Iterates through all nodes `u`:
    *   If `u` is not visited, call `dfs` to start a DFS from `u`.
    *   If `dfs` returns `true`, it means a bridge was found, so `solve` returns `1`.
*   If no bridge is found after visiting all components, `solve` returns `0`.

**`main()` function:**

*   Sets up fast I/O.
*   Continuously calls `solve()` until `solve()` returns -1 (indicating end of input based on `n=0, m=0`).
*   Prints "Yes" if `solve()` returns 1 (bridge found), "No" if `solve()` returns 0 (no bridge found).

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";} cout<<"\n";
#define all(x) (x).begin(), (x).end()
// #define reverse(a) reverse(a.begin(),a.end()); // Use std::reverse from <algorithm>
#define input(arr) for(long long i=0;i<arr.size();i++){cin>>arr[i];}\
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
   return ceil(((ld)a)/((ld)b)); // Requires <cmath>
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); 
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin);
\t    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Recursive DFS function to find bridge edges
// Returns true if a bridge is found in the current DFS subtree/component
bool dfs(vector<vll>&graph, ll u, vector<bool>&visited , ll parent , vll&discTime , vll&minChildTime , ll&t)
{
    visited[u] = true; // Mark current node as visited
    discTime[u] = minChildTime[u] = t; // Initialize discovery time and low-link value
    t++; // Increment global time counter
    
    for(auto v : graph[u]) // Iterate over all neighbors of u
    {
        if(v == parent){continue;} // If v is the parent in DFS tree, skip (don't consider it a back-edge)

        if(!visited[v]) // If neighbor v is not visited
        {
            // Recurse on v. If a bridge is found in the subtree rooted at v, propagate true.
            if(dfs(graph, v, visited, u, discTime, minChildTime, t)){return true;}
            
            // After recursive call returns, update minChildTime[u] with minChildTime[v]
            // This means u can reach whatever v can reach.
            minChildTime[u] = min(minChildTime[u], minChildTime[v]);

            // Bridge condition: If minChildTime[v] > discTime[u],
            // it means v and its subtree cannot reach u or any ancestor of u via a back-edge.
            // Thus, (u, v) is a bridge.
            if(minChildTime[v] > discTime[u]){return true; } // u - v is a bridge edge
        }
        else // If neighbor v is visited and not parent (it's a back-edge to an ancestor)
        {
            // Update minChildTime[u] with discTime[v].
            // This means u can reach v (an ancestor) through this back-edge, 
            // so the lowest reachable time from u could be discTime[v].
            minChildTime[u] = min(minChildTime[u], discTime[v]);
        }
    }
    
    return false; // No bridge found in this subtree/component
}

// Function to solve a single test case (find if any bridge exists in the graph)
ll solve()
{
    ll n,m,i;
    cin>>n>>m;
    
    // Base case for input termination: if n and m are both 0, stop processing.
    if(n==0 && m==0){return -1;}
    
    vector<vll> graph(n);
    
    // Read edges and build adjacency list for an undirected graph
    while(m--)
    {
        ll u,v;
        cin>>u>>v;
        
        graph[u].pb(v);
        graph[v].pb(u);
    }
    
    vector<bool> visited(n,false); // Tracks visited nodes
    vll discTime(n,inf);           // Stores discovery times
    vll minChildTime(n,inf);       // Stores low-link values
    
    ll parent = -1; // Initial parent for DFS start is -1 (no parent)
    ll t = 1;       // Global time counter, starting from 1
    
    // Iterate through all nodes to handle disconnected components
    for(ll u=0; u<n; u++)
    {
        if(!visited[u]) // If node u has not been visited, start a new DFS from it
        {
            if(dfs(graph , u , visited , parent , discTime , minChildTime , t))
            {
                return 1; // A bridge was found in this component
            }
        }
    }
    
    return 0; // No bridge found in any component of the graph
}

int main()
{
    setIO(""); // Set up fast I/O (no file redirection for this example, standard I/O)
    
    // Loop to handle multiple test cases until n=0, m=0 is encountered
    while(true)
    {
        ll res = solve();
        
        if(res == -1){break;} // Termination condition
        
        if(res == 1) // If a bridge was found
        {
            cout<<"Yes\n";
        }
        else // If no bridge was found
        {
            cout<<"No\n";
        }
    }
    
    return 0;
}
```