# Tarjan's Algorithm: Articulation Points

## Problem Description

This problem focuses on identifying **articulation points** (also known as cut vertices) in an undirected graph. An articulation point is a vertex whose removal (along with all incident edges) increases the number of connected components in the graph.

Finding articulation points is crucial in network reliability analysis, as they represent single points of failure.

## C++ Solution

The solution uses **Tarjan's Algorithm**, which is a Depth-First Search (DFS)-based approach. It relies on keeping track of two values for each node during DFS:

1.  **`discTime[u]` (Discovery Time):** The time (or order) at which node `u` is first visited during the DFS traversal.
2.  **`minChildTime[u]` (Low-Link Value):** The lowest discovery time reachable from node `u` (including `u` itself) through any path, including back-edges in the DFS tree. This means the minimum of `discTime[u]`, and `discTime[v]` for any back-edge `(u, v)`, and `minChildTime[v]` for any tree-edge `(u, v)`.

**Algorithm (`dfs` helper function):**

*   **Parameters:**
    *   `adj[]`: Adjacency list of the graph.
    *   `u`: Current node being visited.
    *   `parent`: Parent of `u` in the DFS tree.
    *   `visited[]`: Boolean array to track visited nodes.
    *   `isAP[]`: Boolean array to mark articulation points.
    *   `discTime[]`: Discovery time of nodes.
    *   `minChildTime[]`: Low-link value of nodes.
    *   `t`: Current time counter for discovery times.

*   **Steps:**
    1.  Mark `u` as `visited`, set `discTime[u] = minChildTime[u] = t`, and increment `t`.
    2.  Initialize `children = 0` (counts children in DFS tree for root check).
    3.  For each neighbor `v` of `u`:
        *   **If `v` is `parent`:** Continue (ignore edge to parent to prevent `minChildTime` from being incorrectly updated).
        *   **If `v` is not `visited` (Tree Edge):**
            *   Increment `children`.
            *   Recursively call `dfs(adj, v, u, ...)`.
            *   Update `minChildTime[u] = min(minChildTime[u], minChildTime[v])`. This propagates the lowest reachable time from `v` up to `u`.
            *   **Articulation Point Condition 1 (for non-root):** If `parent != -1` (u is not root) AND `minChildTime[v] >= discTime[u]`, then `u` is an articulation point. This means that `v` and its subtree cannot reach any ancestor of `u` (or `u` itself) without passing through `u`.
        *   **If `v` is `visited` and `v != parent` (Back-Edge):**
            *   Update `minChildTime[u] = min(minChildTime[u], discTime[v])`. This indicates `u` can reach `v` (an ancestor) through a back-edge, potentially finding an earlier discovery time.
    4.  **Articulation Point Condition 2 (for root):** If `parent == -1` (u is the root of DFS tree) AND `children > 1`, then `u` is an articulation point. A root is an AP if it has at least two disconnected children subtrees.

**`articulationPoints(int V, std::vector<int> adj[])` function (Main Entry Point):**

*   Initializes `visited`, `discTime`, `minChildTime`, and `isAP` arrays.
*   Iterates through all vertices. If a vertex is not visited, it calls `dfs` to start a new DFS traversal. This handles disconnected components.
*   Collects all vertices marked as articulation points into a `std::vector<int> ans`.
*   If no articulation points are found, it returns `{-1}` as per some problem conventions.

```cpp
#include <vector>    // For std::vector
#include <algorithm> // For std::min
#include <iostream>  // For driver code (std::cin, std::cout)

// Solution class (common for competitive programming platforms)
class Solution {
public:
    // Recursive DFS function to find articulation points
    // adj[]: Adjacency list of the graph
    // u: Current node being visited
    // parent: Parent of u in the DFS tree
    // visited[]: Boolean array to keep track of visited nodes
    // isAP[]: Boolean array to mark articulation points
    // discTime[]: Discovery time of nodes
    // minChildTime[]: Low-link value of nodes
    // t: Current global time counter for discovery times
    void dfs(std::vector<int> adj[], int u, int parent, 
             std::vector<bool>& visited, std::vector<bool>& isAP,
             std::vector<int>& discTime, std::vector<int>& minChildTime, int& t)
    {
        visited[u] = true; // Mark current node as visited
        discTime[u] = t;   // Set discovery time
        minChildTime[u] = t; // Initialize low-link value with discovery time
        t++; // Increment global time counter
        
        int children_in_dfs_tree = 0; // Counter for children in DFS tree (for root check)
        
        // Iterate over all neighbors of u
        for(int v : adj[u])
        {
            if(v == parent) { // If v is the immediate parent, skip this edge (not a forward/back edge)
                continue;
            }

            if(!visited[v]) // Case 1: v is not visited, so (u, v) is a tree edge
            {
                children_in_dfs_tree++; // Increment child count
                dfs(adj, v, u, visited, isAP, discTime, minChildTime, t); // Recurse for child v
                
                // After recursive call, update u's low-link value with child v's low-link value
                minChildTime[u] = std::min(minChildTime[u], minChildTime[v]);
                
                // Articulation Point Condition for non-root nodes:
                // If v and its subtree cannot reach any ancestor of u (or u itself) 
                // without passing through u, then u is an articulation point.
                if(parent != -1 && minChildTime[v] >= discTime[u])
                {
                    isAP[u] = true;
                }
            }
            else { // Case 2: v is visited and not parent, so (u, v) is a back-edge to an ancestor
                // Update u's low-link value with v's discovery time (because u can reach v)
                minChildTime[u] = std::min(minChildTime[u], discTime[v]);
            }
        }
        
        // Articulation Point Condition for the root of the DFS tree:
        // The root is an AP if it has more than one child in the DFS tree.
        // (A single child or no children would not disconnect the graph).
        if(parent == -1 && children_in_dfs_tree > 1){
            isAP[u] = true;
        }
    }
    
    // Main function to find all articulation points in the graph
    // V: Number of vertices
    // adj[]: Adjacency list representation of the graph
    std::vector<int> articulationPoints(int V, std::vector<int> adj[]) 
    {
        // Initialize data structures
        std::vector<bool> visited(V, false); // V elements for 0 to V-1 nodes
        std::vector<int> discTime(V, -1);   // Discovery times
        std::vector<int> minChildTime(V, -1); // Low-link values
        std::vector<bool> isAP(V, false);   // To mark articulation points
        
        int time_counter = 0; // Global time counter, passed by reference to DFS
        
        // Iterate through all vertices to handle disconnected components
        for(int u = 0; u < V; u++)
        {
            if(!visited[u]){
                // Start DFS from u, with -1 as parent (indicating root of DFS tree)
                dfs(adj, u, -1, visited, isAP, discTime, minChildTime, time_counter);
            }
        }
        
        std::vector<int> result_aps; // Collect articulation points
        
        for(int i = 0; i < V; i++)
        {
            if(isAP[i]){ // If node i is an articulation point
                result_aps.push_back(i);
            }
        }
        
        // According to problem requirements, if no APs, return {-1}
        if(result_aps.empty()){
            result_aps.push_back(-1);
        }
        
        return result_aps;
    }
};

// Driver Code (often provided by competitive programming platforms)
// Handles input reading and output formatting.
int main(){
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int tc; // Number of test cases
    std::cin >> tc;
    while(tc--){
        int V, E; // V: number of vertices, E: number of edges
        std::cin >> V >> E;
        std::vector<int> adj[V]; // Adjacency list for the graph

        // Read edges and build the adjacency list (undirected graph)
        for(int i = 0; i < E; i++){
            int u, v;
            std::cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        Solution obj;
        std::vector<int> ans = obj.articulationPoints(V, adj);
        for(int i : ans) std::cout << i << " ";
        std::cout << "\n";
    }
    return 0;
} 
```