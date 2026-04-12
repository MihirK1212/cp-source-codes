# Mother Vertex in a Directed Graph

## Problem Description

Given a directed graph, the task is to find a **mother vertex**. A mother vertex is a vertex from which all other vertices in the graph are reachable. If multiple mother vertices exist, any one of them is a valid answer. If no such vertex exists, indicate that.

## C++ Solution

This C++ solution uses a two-pass Depth First Search (DFS) approach to find a mother vertex in a directed graph. The algorithm relies on the property that if a graph has a mother vertex, then the finishing time of a DFS traversal from that vertex will be the last among all vertices.

**Algorithm:**

1.  **First DFS Pass (Find Potential Mother Vertex):**
    *   Perform a DFS traversal on the graph. Keep track of the last visited vertex (the one with the largest finishing time).
    *   The `dfs` helper function is modified to update a `last_visited` reference with the node that finishes last in the current DFS path. This `last_visited` will eventually hold a candidate for the mother vertex if one exists.
    *   After iterating through all vertices and performing DFS from unvisited ones, `last_visited` will contain a vertex that is a potential mother vertex.

2.  **Second DFS Pass (Verify Candidate):**
    *   Reset the `visited` array.
    *   Perform another DFS traversal, this time starting *only* from the `last_visited` vertex found in the first pass.
    *   After this DFS, check if all vertices in the graph have been visited. If yes, then `last_visited` is indeed a mother vertex. Otherwise, no mother vertex exists.

**`dfs(vector<vector<int>>& graph, int u, vector<bool>& visited, int& last_visited)` function:**

*   **Parameters:**
    *   `graph`: Adjacency list representation of the directed graph.
    *   `u`: Current vertex being visited.
    *   `visited`: Boolean array to keep track of visited vertices during a DFS traversal.
    *   `last_visited`: Reference to an integer that will store the vertex with the latest finishing time in the current DFS component.
*   **Logic:**
    1.  Mark `u` as visited.
    2.  For each neighbor `v` of `u`:
        *   If `v` is not visited, recursively call `dfs(graph, v, visited, last_visited)`.
    3.  After visiting all reachable descendants, set `last_visited = u`. This ensures that `last_visited` always stores the node that *finishes last* in the DFS traversal that includes `u`.

**`Solution::motherVertex(int A, vector<vector<int> > &B)` function:**

*   **Parameters:**
    *   `A`: Number of vertices in the graph (vertices are 1-indexed, from 1 to A).
    *   `B`: A vector of vectors representing the edges, where `B[i] = {u, v}` means a directed edge from `u` to `v`.
*   **Logic:**
    1.  **Build Graph:** Construct the adjacency list `graph` from the input `B`.
    2.  **First DFS Pass:**
        *   Initialize `visited` array to `false` for all vertices (1 to `A`).
        *   Initialize `last_visited = -1`.
        *   Iterate through vertices from 1 to `A`.
        *   If a vertex `u` is not visited, perform `dfs` from `u`. The `last_visited` variable will be updated.
    3.  **Handle No Candidate:** If `last_visited` is still -1 after the first pass (e.g., empty graph or no reachable nodes from any start), return `0` (implying no mother vertex).
    4.  **Second DFS Pass:**
        *   Reset the `visited` array to `false` for all vertices.
        *   Perform a DFS starting *only* from the `last_visited` candidate vertex.
    5.  **Verify Reachability:**
        *   After the second DFS, iterate through all vertices from 1 to `A`.
        *   If any vertex `u` is still `!visited[u]`, it means `last_visited` cannot reach all other vertices, so no mother vertex exists. Return `0`.
    6.  **Return Result:** If all checks pass, `last_visited` is a mother vertex. Return `1`.

```cpp
#include <vector> // Required for std::vector
#include <algorithm> // Not explicitly used but generally useful

// Helper DFS function to traverse the graph and find the last finished vertex.
// 'last_visited' will store the vertex that finishes last in the current DFS traversal.
void dfs(std::vector<std::vector<int>>& graph, int u, std::vector<bool>& visited, int& last_visited)
{
    visited[u] = true; // Mark current vertex as visited
    
    // Recurse for all unvisited neighbors
    for(int v : graph[u])
    {
        if(!visited[v])
        {
            dfs(graph, v, visited, last_visited);
        }
    }

    // After visiting all reachable descendants from u, u is the last to finish in its current path.
    last_visited = u;
}

class Solution {
public:
    // Main function to find a mother vertex in a directed graph.
    // Returns 1 if a mother vertex exists, 0 otherwise.
    int motherVertex(int A, std::vector<std::vector<int>>& B) 
    {
        // Build the adjacency list representation of the graph.
        // Vertices are 1-indexed, so graph size A+1.
        std::vector<std::vector<int>> graph(A + 1);
        for(const auto& edge : B)
        {
            graph[edge[0]].push_back(edge[1]);
        }

        // Visited array for the first DFS pass.
        std::vector<bool> visited(A + 1, false);

        int last_visited = -1; // Candidate for mother vertex (vertex with latest finishing time)

        // First DFS pass: Traverse all components to find a potential mother vertex.
        for(int u = 1; u <= A; u++)
        {
            if(!visited[u])
            {
                dfs(graph, u, visited, last_visited);
            }
        }

        // If no nodes were visited (e.g., empty graph with A=0, or no reachable nodes from any start),
        // then no mother vertex.
        if(last_visited == -1) { return 0; }

        // Second DFS pass: Verify if the 'last_visited' candidate can reach all other vertices.
        
        // Reset visited array for the second DFS.
        std::fill(visited.begin(), visited.end(), false); // Efficiently reset all elements to false

        // Start DFS from the candidate mother vertex
        // The 'last_visited' parameter in this call is effectively a throwaway here,
        // as we are only interested in marking reachable nodes as visited.
        dfs(graph, last_visited, visited, last_visited); 

        // Check if all vertices are reachable from the candidate.
        for(int u = 1; u <= A; u++)
        {
            if(!visited[u]){
                return 0; // Not all vertices reachable, so no mother vertex exists
            }
        }

        return 1; // All vertices are reachable from 'last_visited', so it is a mother vertex.
    }
};
```