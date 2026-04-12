# Shortest Distance between two Graph Nodes (BFS)

## Problem Description

Given an unweighted graph, find the shortest distance (number of edges) between a `start` node and an `end` node. This is a classic application of Breadth-First Search (BFS).

**BFS Principle for Shortest Path:**

BFS explores all neighbors at the current depth level before moving on to nodes at the next depth level. For unweighted graphs, this property guarantees that the first time a node is visited, it is reached via the shortest possible path from the source node. By keeping track of the distance from the source for each visited node, we can find the shortest distance to any reachable node.

## C++ Solution

The `bfs` function implements the Breadth-First Search algorithm:

1.  **Initialization:**
    *   `visited`: A `std::vector<bool>` to keep track of visited nodes to prevent reprocessing and infinite loops in cycles.
    *   `q`: A `std::queue<long long>` to store nodes to be visited.
    *   `dist`: A `std::vector<long long>` to store the shortest distance from the `start` node to each node. Initialize all distances to `-1` (unreachable) and `dist[start]` to `0`.
    *   Push `start` node into the queue.
2.  **BFS Traversal:**
    *   While the queue is not empty:
        *   Dequeue a node `u`.
        *   If `u` has not been `visited`:
            *   Mark `u` as `visited`.
            *   For each neighbor `x` of `u`:
                *   If `x` has not been `visited`:
                    *   Enqueue `x`.
                    *   If `dist[x]` is still `-1` (meaning `x` has not been reached via a shorter path yet), update `dist[x] = dist[u] + 1`.
3.  **Result:** After the BFS completes, `dist[end]` will contain the shortest distance from `start` to `end`. If `dist[end]` is still `-1`, it means `end` is unreachable from `start`.

```cpp
#include <iostream>  // For std::cin, std::cout
#include <vector>    // For std::vector
#include <queue>     // For std::queue
#include <map>       // For std::map (adjacency list representation)
#include <algorithm> // For std::sort, std::max, std::min (not directly used but generally useful)

// Commonly used in competitive programming for brevity, but explicit std:: is more robust
// using namespace std;

// Function to perform BFS and find the shortest distance from start to end.
// graph: adjacency list representation of the graph.
// start: starting node.
// end: target node.
void bfs(std::map<long long, std::vector<long long>>& graph, long long start, long long end)
{
    // A map might have keys with values that are not 0 to graph.size()-1
    // To handle general node IDs, we can use a map for visited and distance as well.
    // Or, find the maximum node ID to size vectors if node IDs are sequential from 0.
    // For simplicity, assuming node IDs are reasonably small and sequential for vector indexing.
    long long max_node_id = 0;
    for(auto const& [node_id, neighbors] : graph) {
        max_node_id = std::max(max_node_id, node_id);
        for(long long neighbor : neighbors) {
            max_node_id = std::max(max_node_id, neighbor);
        }
    }
    long long num_nodes = max_node_id + 1; // Assuming nodes are 0-indexed up to max_node_id

    std::vector<bool> visited(num_nodes, false);
    std::queue<long long> q;
    
    std::vector<long long> dist(num_nodes, -1); // Initialize distances to -1 (unreachable)
    dist[start] = 0; // Distance from start to itself is 0
    
    q.push(start);
    visited[start] = true; // Mark start node as visited when pushed to queue
    
    while(!q.empty())
    {
        long long u = q.front();
        q.pop();
        
        // No need for `if(!visited[u])` here because we mark visited when pushing to queue.
        // This ensures each node is processed once from the queue.

        // Iterate through all neighbors of u
        for(long long x : graph[u])
        {
            if(!visited[x]) // If neighbor x has not been visited yet
            {
                visited[x] = true; // Mark as visited
                q.push(x);         // Enqueue for further exploration
                dist[x] = dist[u] + 1; // Update distance
            }
        }
    }
    
    std::cout << "Shortest distance between " << start << " and " << end << " is " << dist[end] << "\n";
    
    return;
}

// Driver Code
int main()
{
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);

    // Example graph definition using an adjacency list (map for flexible node IDs)
    std::map<long long, std::vector<long long>> graph;
    
    graph[0] = {1, 4, 5};
    graph[1] = {0, 2, 3, 4};
    graph[2] = {1};
    graph[3] = {1, 4};
    graph[4] = {0, 1, 3};
    graph[5] = {0, 6, 9};
    graph[6] = {5, 9};
    graph[7] = {8};
    graph[8] = {7};
    graph[9] = {5, 6};
    
    long long start_node, end_node;
    
    std::cout << "BFS for Shortest Distance...\n";
    std::cout << "Enter starting node:\n";
    std::cin >> start_node;
    std::cout << "Enter ending node:\n";
    std::cin >> end_node;
    
    bfs(graph, start_node, end_node);
    
    return 0;
}
```