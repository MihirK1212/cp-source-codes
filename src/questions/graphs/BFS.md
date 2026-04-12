# Breadth-First Search (BFS)

## Overview

Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key') and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

### Key Characteristics:

*   **Level-by-Level Traversal:** BFS explores all nodes at a given depth (distance from the source) before moving to nodes at the next depth. This guarantees that the shortest path in an unweighted graph is found first.
*   **Queue Data Structure:** BFS uses a queue to manage which node to visit next, ensuring a FIFO (First-In, First-Out) order of processing.
*   **Applications:** Widely used for finding the shortest path in unweighted graphs, finding connected components, network broadcasting, and more.

### BFS Algorithm Steps:

1.  **Start Node:** Begin by selecting a 'start' node. This node is at distance 0 from itself.
2.  **Initialization:** Add the `start` node to a queue and mark it as visited.
3.  **Traversal Loop:** While the queue is not empty:
    a.  Dequeue a node `u` from the front of the queue.
    b.  Process node `u` (e.g., print it, add it to a path, etc.).
    c.  For each unvisited neighbor `v` of `u`:
        i.  Mark `v` as visited.
        ii. Enqueue `v`.

### Visiting Order:

1.  Visit the starting node.
2.  Visit all nodes directly adjacent to the starting node.
3.  Visit all unvisited nodes adjacent to the nodes visited in step 2.
4.  Continue this process, layer by layer, until all reachable nodes are visited.

## C++ Solution

This C++ solution implements the BFS algorithm for graph traversal.

**Graph Representation:**

*   The graph is represented using an adjacency list: `std::map<ll, vll> graph`, where keys are nodes and values are vectors of their neighbors.

**`bfs(map<ll, vll> &graph, ll start)` function:**

*   **Parameters:**
    *   `graph`: The adjacency list representing the graph.
    *   `start`: The starting node for the BFS traversal.
*   **Logic:**
    1.  Create a `std::vector<bool> visited` to keep track of visited nodes, initialized to `false`.
    2.  Create a `std::queue<ll> q` and push the `start` node onto it.
    3.  While `q` is not empty:
        *   Dequeue `u = q.front()` and pop it.
        *   If `u` has not been visited (`!visited[u]`):
            *   Mark `u` as visited (`visited[u] = true`).
            *   Process `u` (e.g., print `Visited u`).
            *   For each neighbor `x` of `u`:
                *   If `x` has not been visited (`!visited[x]`), enqueue `x`.

**`main()` function:**

*   Demonstrates how to create a sample graph (undirected in this example).
*   Prompts the user for a starting node.
*   Calls the `bfs` function to perform the traversal and prints the visited nodes.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <queue>     // Required for std::queue
#include <map>       // Required for std::map (for graph representation)
#include <algorithm> // Not explicitly used but generally useful
#include <limits>    // For std::numeric_limits (if ll inf needed)

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

#define ll long long 
#define vll std::vector<long long>
// #define f first // Avoiding conflicts with member access
// #define s second // Avoiding conflicts with member access
#define pb push_back
#define printoneline(arr,a,b) for(long long i_idx=a;i_idx<=b;i_idx++){std::cout<<arr[i_idx]<<" ";} std::cout<<"\n";
// #define sort(a) std::sort(a.begin(),a.end()); // Avoid macro conflict
// #define rsort(a) std::sort(a.rbegin(),a.rend()); // Avoid macro conflict
// #define reverse(a) std::reverse(a.begin(),a.end()); // Avoid macro conflict

// Function to perform Breadth-First Search (BFS) traversal of a graph
// graph: adjacency list representation
// start: starting node for traversal
void bfs(std::map<ll, vll>& graph, ll start)
{
    // visited array to keep track of visited nodes
    // Size should be based on maximum node index, or use a map for sparse graphs.
    // Assuming node IDs are 0-indexed and contiguous for vector<bool>.
    // For map, graph.rbegin()->first + 1 could give a max, but map itself stores visited state implicitly.
    // A safer way if nodes are arbitrary ints is to use std::map<ll, bool> visited;
    std::vector<bool> visited(graph.size(), false);
    
    std::queue<ll> q; // Queue for BFS traversal
    
    q.push(start); // Add the starting node to the queue
    visited[start] = true; // Mark the starting node as visited
    
    while(!q.empty()) // While there are nodes to visit
    {
        ll u = q.front(); // Get the front node
        q.pop();          // Remove it from the queue
        
        std::cout << "Visited " << u << "\n"; // Process the node (e.g., print it)
            
        // Enqueue all unvisited neighbors of u
        for(auto v : graph[u])
        {
            if(!visited[v])
            {
                visited[v] = true; // Mark neighbor as visited
                q.push(v);         // Add neighbor to the queue
            }
        }
    }
    return;
}

int main()
{
    // Fast I/O setup
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);
    
    // Sample graph representation using std::map for adjacency list
    std::map<ll, vll> graph;
    
    // Define graph edges
    graph[0]={1,4,5};
    graph[1]={0,2,3,4};
    graph[2]={1};
    graph[3]={1,4};
    graph[4]={0,1,3};
    graph[5]={0,6,9};
    graph[6]={5,9};
    graph[7]={8};
    graph[8]={7};
    graph[9]={5,6};
    
    ll start_node;
    
    std::cout << "BFS...\n";
    std::cout << "Enter starting node\n";
    std::cin >> start_node;
    
    bfs(graph, start_node); // Perform BFS traversal
    
    return 0;
}
```