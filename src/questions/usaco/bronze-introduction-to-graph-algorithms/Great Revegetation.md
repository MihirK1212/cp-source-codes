# Great Revegetation (USACO Bronze - Graph Algorithms)

## Problem Description

This problem is from USACO: [Great Revegetation](http://www.usaco.org/index.php?page=viewproblem2&cpid=916).

Farmer John has `N` pastures, connected by `M` bidirectional paths. Each pasture needs to be planted with one of four types of grass (labeled 1, 2, 3, or 4). If two pastures are connected by a path, they must have different types of grass. The goal is to assign a grass type to each pasture such that the above condition is met. The problem asks for *any* valid assignment.

This is a graph coloring problem. Since only 4 colors are available, and the problem asks for *any* valid assignment, a greedy approach or a simple backtracking search often works.

## C++ Solution

This solution uses a backtracking Depth First Search (DFS) approach to color the graph. It attempts to assign the smallest possible color (from 1 to `k`, where `k=4`) to each pasture, ensuring that no adjacent pastures have the same color.

**Functions:**
*   `allowed(graph, u, color, c)`: Checks if it's "allowed" to color pasture `u` with color `c`. It iterates through all neighbors of `u` and returns `false` if any neighbor already has color `c`. Otherwise, it returns `true`.
*   `dfs(graph, u, color, k)`: This is the recursive backtracking function.
    1.  **Base Case:** If `u` (current pasture index) is greater than or equal to `graph.size()`, it means all pastures have been successfully colored, so return `true`.
    2.  **Recursive Step:** Iterate through colors `c` from 1 to `k`.
        *   If `allowed(graph, u, color, c)` is true:
            *   Assign `color[u] = c`.
            *   Recursively call `dfs` for the next pasture `u+1`.
            *   If the recursive call returns `true`, it means a valid coloring was found for the rest of the graph, so return `true`.
            *   **Backtrack:** If the recursive call returns `false`, unassign the color `color[u] = -1` and try the next color.
    3.  If no color works for pasture `u`, return `false`.

**Main Logic in `solve` and `main`:**
*   Reads `N` pastures and `M` paths.
*   Builds an adjacency list `graph` to represent the connections between pastures.
*   Initializes a `color` vector with -1 (uncolored) for all pastures.
*   Sets `k = 4` (since there are 4 types of grass).
*   Calls `dfs(graph, 1, color, k)` to start the coloring process from pasture 1.
*   After `dfs` completes, it prints the assigned colors for all pastures.

**Note on `printoneline` macro:** The macro `printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";}c cout<<"\n";` has a typo: `c cout` instead of `cout`. This would cause a compilation error if used. It's commented out in the solution (or rather, not used in this specific file).

```cpp
#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define pb push_back
// #define printoneline(arr) for(long long i=0;i<arr.size();i++){cout<<arr[i]<<" ";}c cout<<"\n"; // 'c' typo
#define all(x) (x).begin(), (x).end()
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

ll inf=std::numeric_limits<long long>::max(); // Using std::numeric_limits for infinity

ll ceilVal(ll a,ll b)
{
   return ceil(((ld)a)/((ld)b)); 
}

void setIO(string name = "") 
{ 
    ios_base::sync_with_stdio(0); cin.tie(0); // Faster I/O
    
    if(name!="")
    {
        freopen((name+".in").c_str(), "r", stdin); // Redirect input
	    freopen((name+".out").c_str(), "w", stdout);
    }
}

// Checks if pasture 'u' can be colored with 'c' without conflict with neighbors
bool allowed(vector<vll>&graph,ll u,vll&color,ll c)
{
    for(auto v : graph[u]) // Iterate through neighbors of 'u'
    {
        if(color[v]==c){return false;} // Conflict if neighbor 'v' has same color 'c'
    }
    
    return true; // No conflict, color 'c' is allowed
}

// Recursive Depth First Search for graph coloring
// graph: adjacency list of pastures
// u: current pasture to color
// color: vector to store assigned colors (initially -1)
// k: number of available colors (here, 4)
bool dfs(vector<vll>&graph,ll u,vll&color,ll k)
{
    if(u >= graph.size()){ // Base case: If all pastures (up to N) have been considered
        return true; // A valid coloring has been found
    }
    
    // Try coloring pasture 'u' with each available color from 1 to k
    for(ll c=1;c<=k;c++)
    {
        if(allowed(graph,u,color,c)) // If color 'c' is valid for pasture 'u'
        {
            color[u] = c; // Assign color 'c' to pasture 'u'
            if(dfs(graph,u+1,color,k)) // Recurse for the next pasture (u+1)
            {
                return true; // If recursive call finds a solution, propagate true
            }
            color[u] = -1; // Backtrack: If solution not found with 'c', unassign color
        }
    }
    
    return false; // No color worked for pasture 'u'
}


void solve()
{
    ll n,m,i; // n: number of pastures, m: number of paths
    cin>>n>>m;
    
    vector<vll> graph(n+1); // Adjacency list for the graph (1-indexed)
    
    while(m--)
    {
        ll u,v;
        cin>>u>>v;
        
        graph[u].pb(v); // Add bidirectional edge
        graph[v].pb(u);
    }
    
    vll color(n+1,-1); // Color array, initialized to -1 (uncolored)
    ll k = 4; // Number of available colors (grass types)
    
    dfs(graph,1,color,k); // Start DFS from pasture 1
    
    for(ll u=1;u<=n;u++){cout<<color[u];} cout<<"\n"; // Print assigned colors
}

int main()
{
    setIO("revegetate"); // Set up file I/O for USACO problem
    // setIO(""); // Use standard I/O if no specific file required
    
    ll T = 1; // Number of test cases (usually 1 for USACO)
    
    while(T--)
    {
        solve(); // Call the solve function for each test case
    }
    
    return 0;
}
```