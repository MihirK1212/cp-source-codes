# Cycle Detection in Directed Graph (BFS - Kahn's Algorithm)

## Problem Description

Given a directed graph with `V` vertices and an adjacency list `adj`, determine if there is a cycle in the graph. This can be efficiently checked using [Kahn's algorithm](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm), which is a BFS-based approach for topological sorting.

**Kahn's Algorithm Principle:**

A directed graph has a cycle if and only if its topological sort does not include all vertices. Kahn's algorithm works by repeatedly:

1.  Finding vertices with an in-degree of 0.
2.  Adding them to the topological sort sequence.
3.  Removing their outgoing edges (which means decrementing the in-degrees of their neighbors).

If, at any point, all remaining vertices have a non-zero in-degree, then a cycle must exist among them, as there are no nodes to start from that do not have incoming edges within that subgraph. The number of vertices processed in the topological sort will be less than the total number of vertices `V`.

## C++ Solution

The `isCyclic` function implements Kahn's algorithm:

1.  **Compute In-degrees:** Initialize an `indegree` array for all vertices. Iterate through the adjacency list to calculate the in-degree for each vertex.
2.  **Initialize Queue:** Add all vertices with an in-degree of 0 to a queue.
3.  **Perform BFS:**
    *   While the queue is not empty, dequeue a vertex `u`.
    *   Increment a `count` (representing the number of vertices added to the topological sort).
    *   For each neighbor `v` of `u`:
        *   Decrement `indegree[v]`.
        *   If `indegree[v]` becomes 0, enqueue `v`.
4.  **Check for Cycle:** After the BFS completes, if `count` is not equal to `V`, it means not all vertices could be included in the topological sort, indicating the presence of a cycle. Return `true` if a cycle is found (`count != V`), otherwise `false`.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // For std::vector
#include <queue>     // For std::queue
#include <numeric>   // For std::iota (not directly used in provided code but useful for initialization)

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution {
public:
    // Function to detect cycle in a directed graph using Kahn's algorithm (BFS).
    // V: number of vertices
    // adj: adjacency list representing the directed graph
    bool isCyclic(int V, std::vector<int> adj[]) {
        
        // Step 1: Compute in-degrees for all vertices.
        // indegree[i] stores the number of incoming edges to vertex i.
        std::vector<int> indegree(V, 0);
	    
	    for(int u = 0; u < V; u++) {
	        for(int v : adj[u]) {
	            indegree[v]++; // Increment in-degree of neighbor v for each incoming edge
	        }
	    }
	    
	    // Step 2: Initialize a queue with all vertices having an in-degree of 0.
	    // These are the starting points for topological sort.
	    std::queue<int> q;
	    
	    for(int u = 0; u < V; u++) {
	        if(indegree[u] == 0) {
                q.push(u);
            }
	    }
	    
	    int count = 0; // To count the number of vertices included in the topological sort.
	    
	    // Step 3: Perform BFS (Kahn's algorithm for topological sort).
	    while(!q.empty()) {
	        int u = q.front();
            q.pop();
	        count++; // Add vertex u to the topological order (conceptually)
	        
	        // For each neighbor v of u, remove the edge u -> v by decrementing its in-degree.
	        for(int v : adj[u]) {
	            indegree[v]--;
	            // If in-degree of v becomes 0, it means all its prerequisites are met.
	            // Add v to the queue so it can be processed next.
	            if(indegree[v] == 0) {
                    q.push(v);
                }
	        }
	    }
	    
        // Step 4: Check for cycle.
        // If 'count' is not equal to 'V', it means there are vertices that could not be processed
        // because they are part of a cycle (their in-degrees never reached 0).
        return count != V; // Returns true if a cycle exists, false otherwise.
    }
};

// Driver Code (provided by the problem platform)
int main() {
    // Fast I/O setup
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t; // Number of test cases
    std::cin >> t;
    while (t--) {
        int V, E; // V: number of vertices, E: number of edges
        std::cin >> V >> E;

        // Adjacency list representation of the graph
        std::vector<int> adj[V];

        // Read edges and build the adjacency list
        for (int i = 0; i < E; i++) {
            int u, v;
            std::cin >> u >> v;
            adj[u].push_back(v); // Directed edge from u to v
        }

        Solution obj;
        // Output 1 if a cycle is detected, 0 otherwise
        std::cout << obj.isCyclic(V, adj) << "\n";
    }

    return 0;
}
```