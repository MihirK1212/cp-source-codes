# Counting Paths (CSES - Trees: LCA and Difference Array on Trees)

## Problem Description

This problem, typically found on platforms like CSES (e.g., [Counting Paths](https://cses.fi/problemset/task/1136)), asks us to count, for each node in a given tree, how many of `m` specified paths pass through it. Each path is defined by two nodes `(a, b)`.

**Key Concepts and Algorithms Used:**

1.  **Depth First Search (DFS):** To precompute the depth of each node and its immediate parent in the tree.
2.  **Binary Lifting:** An efficient technique to find the Lowest Common Ancestor (LCA) of any two nodes in `O(log N)` time. This involves precomputing `up[u][j]`, which stores the `2^j`-th ancestor of node `u`.
3.  **Difference Array on Trees (Prefix Sums on Trees):** To efficiently count paths. When a path from `a` to `b` is considered, we increment counts for nodes on the path. This can be done by:
    *   Incrementing `diff[a]` by 1.
    *   Incrementing `diff[b]` by 1.
    *   Decrementing `diff[LCA(a, b)]` by 1.
    *   Decrementing `diff[parent[LCA(a, b)]]` by 1 (if `LCA(a,b)` is not the root).
    After all paths are processed, a second DFS can aggregate these `diff` values from leaves to root to get the final count for each node.

## C++ Solution

This C++ solution implements the described approach.

**Global Constants & Helpers:**

*   `LOG_MAX`: Maximum power of 2 for binary lifting (e.g., 30 for `N` up to `10^9`).
*   `ceilVal`: Utility for ceiling division.
*   `setIO`: For fast I/O.

**`dfs(ll u, vector<vll>& graph, ll par, ll d, vll& parent, vll& depth)` function:**

*   Performs a standard DFS traversal starting from `u`.
*   It populates the `parent` array (immediate parent of each node) and `depth` array (depth of each node from the root, where root is at depth 0).

**`getLCA(ll u, ll v, ll n, vll& parent, vll& depth, vector<vll>& up)` function:**

*   Finds the Lowest Common Ancestor (LCA) of nodes `u` and `v` using binary lifting.
*   **Steps:**
    1.  Ensure `u` is deeper than `v` (swap if not).
    2.  Lift `u` up by `depth[u] - depth[v]` levels using `up` array, so `u` and `v` are at the same depth.
    3.  If `u == v` at this point, `u` (or `v`) is the LCA.
    4.  Otherwise, lift both `u` and `v` simultaneously, from `LOG_MAX-1` down to `0`. If `up[u][j] != up[v][j]`, it means their `2^j`-th ancestors are different, so jump both `u` and `v` to these ancestors.
    5.  After the loop, `u` and `v` will be children of their LCA. So, `up[u][0]` (parent of `u`) is the LCA.

**`applyDiff(ll u, vector<vll>& graph, ll par, vll& diff, vll& ans)` function:**

*   This DFS function aggregates the difference array values.
*   It traverses the tree from root downwards (or post-order traversal up from leaves).
*   For each child `v` of `u`, it recursively calls `applyDiff(v, ...)`. The result `ans[v]` (which is `diff[v]` plus aggregated counts from its subtree) is added to `ans[u]`.
*   Finally, `ans[u]` is updated with `diff[u]` itself.
*   This ensures `ans[u]` correctly represents the total number of paths passing through node `u`.

**`solve()` function (Main Logic):**

1.  **Read Input:** Reads `n` (number of nodes) and `m` (number of queries).
2.  **Build Graph:** Reads `n-1` edges and constructs the adjacency list `graph`.
3.  **Precompute Parent and Depth:** Calls `dfs(0, graph, -1, 0, parent, depth)` to populate `parent` and `depth` arrays starting from node 0 as root.
4.  **Precompute Binary Lifting Table (`up`):**
    *   `up[i][0]` is initialized with `parent[i]`.
    *   `up[i][j]` is computed using `up[up[i][j-1]][j-1]` for `j` from `1` to `LOG_MAX-1`. This means the `2^j`-th ancestor of `i` is the `2^{j-1}`-th ancestor of its `2^{j-1}`-th ancestor.
5.  **Process Queries (Difference Array):**
    *   Initialize `diff` array to zeros.
    *   For each query `(a, b)`:
        *   Find `lca = getLCA(a, b, n, parent, depth, up)`.
        *   Apply difference array updates:
            *   `diff[a] += 1`
            *   `diff[b] += 1`
            *   `diff[lca] -= 1` (LCA is counted twice, so subtract one)
            *   If `parent[lca]` is not -1 (LCA is not the root), `diff[parent[lca]] -= 1`. This is because any path passing through `parent[LCA]` implies it passes through `LCA` (which is already counted).
6.  **Aggregate Differences:** Calls `applyDiff(0, graph, -1, diff, ans)` to calculate the final path counts for each node.
7.  **Output Result:** Prints the `ans` array.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // For std::vector
#include <string>    // For std::string (though not directly used in logic)
#include <map>       // For std::map (not used in logic)
#include <cmath>     // For std::ceil
#include <set>       // For std::set (not used in logic)
#include <queue>     // For std::queue (not used in logic)
#include <algorithm> // For std::swap
#include <limits>    // For std::numeric_limits (not directly used but good for ll inf)

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define f first
#define s second
#define pb push_back
#define printoneline(arr) for(long long x_val : arr){std::cout<<x_val<<" ";} std::cout<<"\n";
#define all(x) (x).begin(), (x).end()
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid macro conflict
#define input(arr) for(long long i_idx=0;i_idx<arr.size();i_idx++){std::cin>>arr[i_idx];}\
// Typedefs, etc.

typedef long long ll;
typedef long double ld;
typedef std::vector<long long> vll;
typedef std::vector<int> vi;
typedef std::vector<std::pair<ll,ll>> vpll;
typedef std::vector<std::pair<int,int>> vpii;
typedef std::pair<int,int> pii;
typedef std::pair<ll,ll> pll;
typedef std::pair<int,std::pair<int,int>> ppi;

ll LOG_MAX = 20; // Max power of 2 for binary lifting. Adjust based on N (e.g., ceil(log2(N)))

ll ceilVal(ll a,ll b) {
   return std::ceil(((ld)a)/((ld)b)); 
}

void setIO(std::string name = "") { 
    std::ios_base::sync_with_stdio(0); std::cin.tie(0); 
    if(name!="") {
        freopen((name+".in").c_str(), "r", stdin);
        freopen((name+".out").c_str(), "w", stdout);
    }
}

// DFS to precompute parent and depth for each node
void dfs(ll u, std::vector<vll>&graph, ll par, ll d, vll&parent, vll&depth)
{
    parent[u] = par;
    depth[u] = d;
    for(auto v : graph[u]) {
        if(v != par) {
            dfs(v, graph, u, d+1, parent, depth);
        }
    }
}

// Function to find the Lowest Common Ancestor (LCA) of two nodes using binary lifting
int getLCA(ll u, ll v, ll n, vll&parent, vll&depth, std::vector<vll>&up)
{
    // 1. Ensure u is the deeper node
    if(depth[u] < depth[v]){std::swap(u,v);}
    
    // 2. Lift u to the same depth as v
    ll k = depth[u] - depth[v];
    for(ll j = LOG_MAX - 1; j >= 0; j--)
    {
        if( (k >> j) & 1 ) { // If the j-th bit of k is set
            u = up[u][j];
        }    
    }
    
    // Now u and v are at the same depth
    if(u == v){return u;}
    
    // 3. Lift u and v simultaneously until their parents are the same (which will be the LCA)
    for(ll j = LOG_MAX - 1; j >= 0; j--)
    {
        if(up[u][j] != up[v][j]) // If their 2^j-th ancestors are different
        {
            u = up[u][j]; // Jump both u and v up
            v = up[v][j];
        }
    }
    
    // After the loop, u and v are children of their LCA. So, parent of u (or v) is the LCA.
    return up[u][0]; 
}

// DFS to aggregate differences from leaves to root to get final path counts
ll applyDiff(ll u, std::vector<vll>&graph, ll par, vll&diff, vll&ans)
{
    ll current_sum = 0;
    for(auto v : graph[u]) {
        if(v != par) {
            current_sum += applyDiff(v, graph, u, diff, ans); // Recursively sum up from children
        }
    }
    ans[u] = current_sum + diff[u]; // Add current node's diff and children's sums
    return ans[u]; // Return the total count for this subtree
}

void solve() {
    ll n,m;
    std::cin>>n>>m;

    std::vector<vll> graph(n);
    for(int i = 0; i < (n - 1); i++) { // Read n-1 edges for a tree
        int u, v; std::cin>>u>>v; u--; v--; // Convert to 0-indexed
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vll parent(n); // Stores immediate parent of each node
    vll depth(n);  // Stores depth of each node from root (root at depth 0)
    dfs(0, graph, -1, 0, parent, depth); // Start DFS from node 0 as root

    // Binary lifting table: up[i][j] stores the 2^j-th ancestor of node i
    std::vector<vll> up(n, vll(LOG_MAX, -1));
    for(int i = 0;  i < n; i++){up[i][0] = parent[i];} // 2^0 ancestor is the immediate parent
    for(int j = 1; j < LOG_MAX; j++) {
        for(int i = 0; i < n; i++) {
            if(up[i][j-1] != -1) {
                up[i][j] = up[up[i][j-1]][j-1]; // 2^j-th ancestor is 2^{j-1}-th ancestor of (2^{j-1})-th ancestor
            }
        }
    }

    vll diff(n, 0); // Difference array for path counting

    while(m--) { // Process each query
        ll u, v; std::cin>>u>>v; u--; v--; // Convert to 0-indexed
        ll lca = getLCA(u, v, n, parent, depth, up);

        // Apply difference array updates for path (u, v):
        // Increment counts at u and v, decrement at LCA(u,v) (counted twice) 
        // and at parent[LCA(u,v)] (to exclude path above LCA)
        diff[u]++; 
        diff[v]++;
        diff[lca]--; // Subtract once for double counting at LCA
        if(parent[lca] != -1) { // If LCA is not the root
            diff[parent[lca]]--; // Subtract once more for the node just above LCA
        }
    }
    
    vll ans(n, 0); // Final answer array
    applyDiff(0, graph, -1, diff, ans); // Aggregate differences via DFS

    printoneline(ans); // Output the result for each node
}

int main() {
    setIO(""); // Set up fast I/O
    ll T = 1; // Number of test cases (set to 1 as per CSES format)
    // std::cin >> T; // Uncomment if multiple test cases are expected
    while(T--) {
        solve();
    }
    return 0;
}
```