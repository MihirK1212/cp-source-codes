# Check if Undirected Graph is Bipartite

## Problem Description

Given an undirected graph, determine if it is bipartite. A bipartite graph is a graph whose vertices can be divided into two disjoint and independent sets, U and V, such that every edge connects a vertex in U to one in V. In other words, there are no edges within U or within V.

This implies that a bipartite graph contains no odd-length cycles. A common approach to check for bipartiteness is to use graph coloring (specifically, 2-coloring) with either Breadth-First Search (BFS) or Depth-First Search (DFS).

## C++ Solution

This C++ solution uses a Depth-First Search (DFS) based 2-coloring algorithm to determine if an undirected graph is bipartite. The idea is to assign alternating colors (e.g., 0 and 1) to adjacent vertices. If at any point an adjacent vertex is found to have the same color as the current vertex, the graph is not bipartite.

**Algorithm:**

1.  **Graph Representation:** Build an adjacency list `graph` from the given `edges`. Since it's an undirected graph, add edges in both directions (`u -> v` and `v -> u`).
2.  **Color Array:** Initialize a `color` vector of size `n+1` (for 1-indexed vertices) with `-1`, indicating that no vertex has been colored yet.
3.  **Iterate Through Vertices:** Loop through each vertex `u` from `1` to `n`.
    *   If `color[u]` is still `-1` (meaning `u` has not been visited yet), start a DFS/coloring process from `u`:
        *   Call `isBipartite(graph, u, 1, color)`. (Start coloring `u` with color 1).
        *   If this call returns `false`, it means an odd cycle was detected, and the graph is not bipartite. Immediately return `false`.
4.  **Return `true`:** If the loop completes without finding any conflicts, the graph is bipartite. Return `true`.

**`isBipartite(map<int, vector<int>>& graph, int u, int curr_color, vector<int>& color)` function (Recursive DFS Helper):**

*   **Parameters:**
    *   `graph`: Adjacency list.
    *   `u`: Current vertex.
    *   `curr_color`: The color to assign to `u` (either 0 or 1).
    *   `color`: The global color array.
*   **Logic:**
    1.  Assign `color[u] = curr_color;`.
    2.  For each neighbor `v` of `u`:
        *   **If `v` is uncolored (`color[v] == -1`):** Recursively call `isBipartite(graph, v, !curr_color, color)` to color `v` with the opposite color. If this recursive call returns `false`, propagate `false` upwards.
        *   **If `v` is already colored:** Check if `color[v]` is the same as `color[u]`. If it is, a conflict is found (an odd cycle), so return `false`.
    3.  If all neighbors are processed without conflict, return `true`.

```cpp
#include <vector>
#include <map>
#include <numeric> // For std::iota (not used in this snippet, but common)

// Recursive DFS helper function to check for bipartiteness
// graph: adjacency list representation of the graph
// u: current vertex being processed
// curr_color: the color to assign to the current vertex u (0 or 1)
// color: vector storing the color assigned to each vertex (-1 if uncolored, 0 or 1 if colored)
bool isBipartite(std::map<int,std::vector<int>>&graph,int u,int curr_color,std::vector<int>&color)
{
    color[u] = curr_color; // Assign the current color to vertex u
    
    // Traverse all neighbors of vertex u
    for(auto v : graph[u])
    {
        // If neighbor v is uncolored, recursively color it with the opposite color
        // If the recursive call returns false, it means a conflict was found in that subtree
        if(color[v]==-1) {
            if(!isBipartite(graph,v,!curr_color,color)){ // !curr_color flips between 0 and 1
                return false; // Propagate conflict upwards
            }
        }
        // If neighbor v is already colored and has the same color as u, then it's not bipartite
        else if(color[v]==color[u])
        {
            return false; // Conflict found
        }
    }
    
    return true; // No conflict found in this component
}

class Solution {
public:
    // Main function to check if the given undirected graph is bipartite
    // n: number of vertices (1-indexed)
    // edges: list of undirected edges
    int solve(int n, std::vector<std::vector<int>>& edges)
    {
        // Build adjacency list from the given edges
        std::map<int,std::vector<int>> graph;
        
        for(const auto& e : edges)
        {
            graph[e[0]].push_back(e[1]); // Add edge u -> v
            graph[e[1]].push_back(e[0]); // Add edge v -> u (since undirected)
        }
        
        // Initialize color array: -1 for uncolored, 0 or 1 for assigned colors
        std::vector<int> color(n+1,-1);
        
        // Iterate through all vertices to handle disconnected components
        for(int u=1;u<=n;u++)
        {
            // If a vertex is uncolored, start DFS from it
            if(color[u]==-1)
            {
                // If the DFS reveals that the component is not bipartite, return 0
                if(!isBipartite(graph,u,1,color)){ // Start coloring with color 1
                    return 0; // Graph is not bipartite
                }
            }
        }
        
        return 1; // All components are bipartite, so the entire graph is bipartite
    }
};
```