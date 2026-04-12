# Bellman-Ford Algorithm (Shortest Distance and Negative Cycle Detection)

## Problem Description

Given a weighted, directed graph with `N` vertices and `M` edges, determine if the graph contains any negative weight cycle. If it does, return `true`; otherwise, return `false`. The Bellman-Ford algorithm can also find the shortest path from a single source to all other vertices, even with negative edge weights, and detect negative cycles.

## C++ Solution

This C++ solution implements the Bellman-Ford algorithm to detect negative weight cycles in a graph.

**Algorithm:**

1.  **Initialization:**
    *   Create a `dist` array of size `N`, initialized with `INT_MAX` for all vertices, except `dist[0]` which is set to `0` (assuming starting from vertex 0, or any arbitrary source for negative cycle detection).
2.  **Relax Edges (N-1 times):**
    *   Perform `N-1` iterations. In each iteration, relax all `M` edges of the graph.
    *   For each `edge = {u, v, w_u_v}` (from `u` to `v` with weight `w_u_v`):
        *   If `dist[u]` is not `INT_MAX` (meaning `u` is reachable) and `dist[u] + w_u_v < dist[v]`:
            *   Update `dist[v] = dist[u] + w_u_v`.
3.  **Detect Negative Cycle (Nth iteration):**
    *   After `N-1` iterations, if there are no negative cycles reachable from the source, all shortest paths would have been found.
    *   Perform one more (the `N`-th) iteration of relaxing all edges.
    *   If in this `N`-th iteration, any `dist[v]` can still be relaxed (i.e., `dist[u] + w_u_v < dist[v]`), it indicates the presence of a negative weight cycle reachable from the source. Return `true`.
4.  **Return `false`:** If no relaxation occurs in the `N`-th iteration, no negative cycle is present. Return `false`.

**Time Complexity:** O(N * M)

```cpp
// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
public:
	int isNegativeWeightCycle(int n, vector<vector<int>>edges)
	{
	    // Initialize distances: dist[i] will store the shortest distance from source to i
	    vector<int> dist(n,INT_MAX);
	   
	    // Assume source is vertex 0. Distance to source itself is 0.
	    dist[0] = 0;
	    
	    // Relax all edges N-1 times
	    for(int iter=1;iter<=n;iter++)
	    {
	        for(auto edge : edges)
	        {
	            int u=edge[0] , v=edge[1] , w_u_v=edge[2];
	            
	            // If vertex u is reachable and a shorter path to v is found
	            if(dist[u]!=INT_MAX && (dist[u]+w_u_v)<dist[v])
	            {
	                // If relaxation occurs in the Nth iteration, a negative cycle exists
	                if(iter==n){return true;}
	                dist[v] = dist[u] + w_u_v;
	            }
	        }
	    }
	    
	    
	    // If no relaxation occurred in the Nth iteration, no negative cycle
	    return false;
	}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>edges;
		for(int i = 0; i < m; i++){
			int x, y, z;
			cin >> x >> y >> z;
			edges.push_back({x,y,z});
		}
		Solution obj;
		int ans = obj.isNegativeWeightCycle(n, edges);
		cout << ans <<"\n";
	}
	return 0;
}  // } Driver Code Ends
```