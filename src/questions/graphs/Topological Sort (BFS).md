# Topological Sort (BFS - Kahn's Algorithm)

## Problem Description

Given a Directed Acyclic Graph (DAG) with `V` vertices and `E` edges, find any valid topological sorting of its vertices. A topological sort (also known as a topological ordering) of a DAG is a linear ordering of its vertices such that for every directed edge `u -> v`, vertex `u` comes before vertex `v` in the ordering. Kahn's algorithm uses Breadth-First Search (BFS) to achieve this.

## C++ Solution

```cpp
#include <vector>
#include <queue>
#include <numeric> // For std::iota

class Solution
{
public:
	//Function to return list containing vertices in Topological order. 
	std::vector<int> topoSort(int V, std::vector<int> adj[]) 
	{
	    // Step 1: Compute in-degrees for all vertices.
	    // indegree[v] stores the number of incoming edges to vertex v.
	    std::vector<int> indegree(V,0);
	    
	    for(int u=0; u<V; u++)
	    {
	        for(int v : adj[u]) // For each neighbor v of u
	        {
	            indegree[v]++; // Increment in-degree of v
	        }
	    }
	    
	    // Step 2: Initialize a queue with all vertices having an in-degree of 0.
	    std::queue<int> q;
	    
	    for(int u=0; u<V; u++)
	    {
	        if(indegree[u]==0){q.push(u);}
	    }
	    
	    // Step 3: Perform BFS.
	    std::vector<int> ans; // To store the topological order
	    
	    while(!q.empty())
	    {
	        int u = q.front(); // Get vertex with 0 in-degree
	        q.pop();
	        
	        ans.push_back(u); // Add it to the topological order
	        
	        // For each neighbor 'v' of 'u':
	        // Decrement its in-degree and if it becomes 0, add it to the queue.
	        for(int v : adj[u])
	        {
	            indegree[v]--;
	            if(indegree[v]==0){q.push(v);}
	        }
	    }
	    
	    // If 'ans.size() != V', it means there was a cycle in the graph,
	    // and a topological sort is not possible. For this problem, we assume DAG.
	    return ans;
	}
};
```

## Driver Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

/*  Function to check if elements returned by user
*   contains the elements in topological sorted form
*   V: number of vertices
*   *res: array containing elements in topological sorted form
*   adj[]: graph input
*/
int check(int V, vector <int> &res, vector<int> adj[]) {
    
    if(V!=res.size())
    return 0;
    
    vector<int> map(V, -1);
    for (int i = 0; i < V; i++) {
        map[res[i]] = i;
    }
    for (int i = 0; i < V; i++) {
        for (int v : adj[i]) {
            if (map[i] > map[v]) return 0;
        }
    }
    return 1;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, E; // N: number of vertices, E: number of edges
        cin >> E >> N;
        int u, v;

        vector<int> adj[N]; // Adjacency list representation of the graph

        for (int i = 0; i < E; i++) {
            cin >> u >> v;
            adj[u].push_back(v);
        }
        
        Solution obj;
        vector <int> res = obj.topoSort(N, adj);

        // The check function verifies if the returned order is a valid topological sort.
        cout << check(N, res, adj) << endl;
    }
    
    return 0;
} 
```