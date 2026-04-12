# Minimum Sum Path from Start to End with Atmost K+1 Edges

## Problem Description

Given a graph with `n` nodes and `edges`, find the cheapest price (minimum sum path) from a `src` node to a `dst` node with at most `K+1` edges. If no such path exists, return -1.

This problem is similar to finding the shortest path in a graph with a limited number of stops, often solved using a modified Bellman-Ford algorithm.

## C++ Solution

This C++ solution implements a modified version of the Bellman-Ford algorithm. The standard Bellman-Ford algorithm finds shortest paths in a graph with `V-1` edges, where `V` is the number of vertices. Here, we are limited to `K+1` edges.

**Algorithm:**

1.  **Initialization:**
    *   Create a `dist` array of size `n`, initialized with a large value (e.g., `1e8` representing infinity) to store the minimum cost to reach each node.
    *   Set `dist[src] = 0` as the cost to reach the source node from itself is zero.

2.  **Relaxation (K+1 iterations):**
    *   The outer loop runs `K+1` times (from `iter = 0` to `K`). Each iteration represents considering paths with one more edge than the previous iteration.
    *   Inside the loop, a temporary `temp` array is created and initialized with the current `dist` values. This is crucial because we want to use `dist` values from the *previous* iteration (i.e., paths with `iter` edges) to calculate `temp` values for paths with `iter+1` edges. This prevents using an updated `dist[v]` value from the current iteration (which might correspond to a path with `iter+1` edges) to further update other nodes within the *same* iteration, thus ensuring we only consider paths with at most `iter+1` edges.
    *   For each edge `(u, v, w)`:
        *   If `dist[u]` is not infinity (meaning `u` is reachable within `iter` edges) and `dist[u] + w` is less than `temp[v]` (meaning we found a cheaper path to `v` with `iter+1` edges):
            *   Update `temp[v] = dist[u] + w`.
    *   After iterating through all edges, `dist` is updated with `temp` for the next iteration.

3.  **Result:**
    *   After `K+1` iterations, `dist[dst]` will contain the minimum cost to reach `dst` from `src` using at most `K+1` edges.
    *   If `dist[dst]` is still `1e8`, it means `dst` is unreachable within `K+1` edges, so return -1.
    *   Otherwise, return `dist[dst]`.

```cpp
#include <vector>
#include <algorithm> // Not explicitly used but good for general practices

class Solution {
public:
    int findCheapestPrice(int n, std::vector<std::vector<int>>& edges, int src, int dst, int K)
    {
        // dist[i] will store the minimum cost to reach node i from src
        // Initialize with a large value (infinity) to represent unreachable nodes
        std::vector<int> dist(n, 1e8); // Using 1e8 as a proxy for infinity
        
        // The cost to reach the source node from itself is 0
        dist[src] = 0;
        
        // Iterate K+1 times. Each iteration finds the shortest path with at most 'iter' edges.
        // The loop runs from iter = 0 to K, effectively covering 0 to K+1 edges.
        for(int iter=0; iter <= K; iter++)
        {
            // Create a temporary distance array to store updates for the current iteration.
            // This is crucial to ensure that updates for paths of length 'iter+1' are based 
            // on paths of length 'iter', preventing a path from being updated multiple times
            // within the same iteration (which would effectively allow more than 'iter+1' edges).
            std::vector<int> temp = dist;
            
            // Iterate through all edges to relax them
            for(auto& e : edges)
            {
                int u = e[0]; // Source of the edge
                int v = e[1]; // Destination of the edge
                int w = e[2]; // Weight of the edge
                
                // If node 'u' is reachable (dist[u] is not infinity from previous iteration)
                // and a shorter path to 'v' is found through 'u' with (iter+1) edges
                if(dist[u] != 1e8 && (dist[u] + w) < temp[v])
                {
                    temp[v] = dist[u] + w;
                }
            }
            
            // Update the main distance array with the results from the current iteration.
            // These become the 'dist' values for the next iteration.
            dist = temp;
        }
        
        // After K+1 iterations, if dist[dst] is still infinity, the destination is unreachable.
        if(dist[dst] == 1e8){
            return -1;
        }
        
        // Otherwise, return the minimum cost to reach the destination with at most K+1 edges.
        return dist[dst];
    }
};
```