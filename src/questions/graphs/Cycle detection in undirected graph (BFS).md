# Cycle Detection in Undirected Graph (BFS)

## Problem Description

Given an undirected graph, determine if it contains a cycle using Breadth-First Search (BFS). A cycle in an undirected graph is a path that starts and ends at the same vertex, and has at least three vertices involved.

## C++ Solution

This C++ solution uses a BFS-based approach to detect cycles in an undirected graph. The core idea is that in an undirected graph, if we encounter a visited node that is not the direct parent of the current node (in the BFS tree), then a cycle exists.

**`Solution` Class Methods:**

### `find(int V, vector<int> adj[], int source, vector<bool>& visited)` function:

*   **Purpose:** Performs a BFS traversal starting from a `source` node to detect a cycle within its connected component.
*   **Parameters:**
    *   `V`: Total number of vertices in the graph.
    *   `adj[]`: Adjacency list representation of the graph.
    *   `source`: The starting node for the current BFS traversal.
    *   `visited`: A boolean array (passed by reference) to keep track of globally visited nodes across all components.
*   **Logic:**
    1.  Initialize a `queue<int> q` and a `vector<int> parent` (size `V`, initialized to -1) to store the parent of each node in the BFS tree.
    2.  Push `source` onto `q`.
    3.  While `q` is not empty:
        *   Dequeue `u = q.front()` and pop it.
        *   If `u` has not been visited (`!visited[u]`):
            *   Mark `u` as visited (`visited[u] = true`).
            *   For each neighbor `v` of `u`:
                *   If `v` is not visited (`!visited[v]`):
                    *   Enqueue `v`.
                    *   Set `parent[v] = u` (recording `u` as the parent of `v`).
                *   Else if `v` is visited AND `v` is not the `parent[u]`:
                    *   This means `v` is an already visited node that is not the immediate parent in the BFS tree. This indicates a back-edge to an ancestor (or a cross-edge in terms of DFS), forming a cycle. Return `true`.
*   If the BFS completes without finding such a `v`, return `false`.

### `isCycle(int V, vector<int> adj[])` function:

*   **Purpose:** The main function to check for cycles in the entire graph, handling disconnected components.
*   **Logic:**
    1.  Initialize a `vector<bool> visited` (size `V`, initialized to `false`) for global tracking of visited nodes.
    2.  Iterate through each vertex `i` from `0` to `V-1`.
    3.  If `i` has not been visited (`!visited[i]`):
        *   Call `find(V, adj, i, visited)` to start a BFS from `i` and check for a cycle in its component.
        *   If `find` returns `true`, it means a cycle was detected. Return `true` immediately.
    4.  If the loop completes without finding any cycle, return `false`.

## Driver Code (C++)

The provided driver code handles multiple test cases, reading graph input (number of vertices `V`, number of edges `E`, and then `E` pairs of `u v` for edges), and then calling the `isCycle` function to print `1` if a cycle is found, or `0` otherwise.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // For std::vector
#include <queue>     // For std::queue
#include <algorithm> // Not explicitly used but generally useful

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution {
public:
    // Helper function to perform BFS and detect a cycle in a connected component.
    // Returns true if a cycle is found, false otherwise.
    bool find(int V, std::vector<int> adj[], int source, std::vector<bool>& visited)
    {
        std::queue<int> q; // Queue for BFS traversal
        // parent[i] stores the parent of node i in the BFS tree. Used to distinguish back-edges from tree-edges.
        std::vector<int> parent(V, -1);
        
        q.push(source); // Start BFS from the source node
        visited[source] = true; // Mark source as visited (important for global tracking)
        
        while(!q.empty()) // While there are nodes to visit
        {
           int u = q.front(); 
           q.pop();
           
           // No need to check !visited[u] here if source is marked visited initially
           // and subsequent nodes are marked visited when enqueued.
           // The provided code structure handles this by doing !visited[u] check before processing
           // and then marking it. If it's already visited, it skips processing its neighbors 
           // unless it was part of a cycle detected earlier via an unexpected path.

           // For each neighbor 'v' of 'u'
           for(int v : adj[u])
           {
               if(!visited[v]) // If 'v' is not visited
               {
                   visited[v] = true; // Mark 'v' as visited
                   q.push(v);         // Enqueue 'v'
                   parent[v] = u;     // Set 'u' as the parent of 'v'
               }
               else if(v != parent[u]) // If 'v' is visited AND 'v' is not the parent of 'u'
               {   // This indicates a back-edge to an already visited node that is not the direct parent.
                   // This means a cycle exists.
                   return true;
               }
           }
        }
       
        return false; // No cycle found in this connected component
    }
    
    // Main function to detect cycle in an undirected graph.
    bool isCycle(int V, std::vector<int> adj[]) {
       
       // Globally visited array to handle disconnected components
       std::vector<bool> visited(V, false);
       
       // Iterate through all vertices. If an unvisited vertex is found, start BFS from it.
       for(int i = 0; i < V; i++)
       {
           if(!visited[i]) // If vertex 'i' has not been visited yet
           {
               // Call find to detect cycle in the connected component of 'i'
               if(find(V, adj, i, visited))
               {
                   return true; // A cycle was detected
               }
           }
       }
       
       return false; // No cycle found in the entire graph
    }
};
    
// Driver Code (provided by the problem platform)
int main() {
    // Fast I/O setup
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int tc;
    std::cin >> tc; // Number of test cases
    while (tc--) {
        int V, E; // Number of vertices and edges
        std::cin >> V >> E;
        std::vector<int> adj[V]; // Adjacency list
        for (int i = 0; i < E; i++) {
            int u, v;
            std::cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u); // Undirected graph: add edge in both directions
        }
        Solution obj;
        bool ans = obj.isCycle(V, adj);
        if (ans)
            std::cout << "1\n";
        else
            std::cout << "0\n";
    }
    return 0;
}
```