# Number of Good Paths

## Problem Description

This problem is from LeetCode: [Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/description/)

Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and `n - 1` edges. You are also given a 0-indexed integer array `vals` of length `n` where `vals[i]` denotes the value of the `i`-th node.

You are also given a 0-indexed 2D integer array `edges` of length `n - 1`, where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi`.

A path is a sequence of distinct nodes `a, b, ..., z` such that there is an edge between `a` and `b`, an edge between `b` and the next node, and so on. A good path is a path where:

*   The starting node and the ending node have the same value.
*   All intermediate nodes in the path have values less than or equal to the starting node (and ending node) value.

Return the number of good paths.

Note that a path of a single node is considered a good path.

## Approach (Disjoint Set Union - DSU)

The problem can be efficiently solved using a Disjoint Set Union (DSU) data structure coupled with a specific processing order. The main idea is to process nodes in increasing order of their values. This ensures that when we consider a path, all intermediate nodes will naturally have values less than or equal to the current node's value (which will be the maximum value on the path).

**Algorithm:**

1.  **Sort Nodes by Value:** Create a list of pairs `(node_index, node_value)` and sort them in increasing order of `node_value`. This ensures that we process nodes with smaller values before nodes with larger values.
2.  **Initialize DSU:** Initialize a DSU structure where each node is initially in its own set. Also, initialize `rank` (or size) for union operations.
3.  **Iterate Through Sorted Nodes:** Iterate through the sorted nodes. When processing nodes with the same `value` (let's say `val`):
    *   For each node `u` with value `val`:
        *   Connect `u` to its neighbors `v` if `value[v] <= value[u]`. This step is crucial: we only unite nodes if the neighbor's value is less than or equal to the current node's value. This ensures that any path formed by these unions will satisfy the "intermediate nodes have smaller or equal value" condition relative to the current `val`.
    *   After processing all nodes with the same `value = val` and performing unions:
        *   For each connected component (identified by its representative using `find()`),
        *   Count the number of nodes within that component that also have the value `val`. Let this frequency be `freq`.
        *   These `freq` nodes can form `freq * (freq - 1) / 2` good paths where `val` is the maximum value. Add this to the total count of good paths. (This is `nC2` where `n` is `freq`).
4.  **Count Single Node Paths:** Each single node itself forms a good path. So, initialize the total count of good paths with `n`.

## C++ Solution

```cpp
#include <vector>
#include <numeric> // For std::iota
#include <algorithm> // For std::sort
#include <map>     // For std::map

class Solution {
public:

    // DSU find operation with path compression
    int find(std::vector<int>&parent,int x)
    {
        if(x==parent[x]){return x;}
        
        parent[x] = find(parent,parent[x]); // Path compression
        return parent[x];
    }

    // DSU union operation by rank/size
    void unionDSU(std::vector<int>&parent,std::vector<int>&rank,int x,int y)
    {
        int x_rep = find(parent,x);
        int y_rep = find(parent,y);
        
        if(x_rep==y_rep){return;} // Already in the same set
        
        // Union by rank heuristic
        if(rank[x_rep]>rank[y_rep]){parent[y_rep] = x_rep;}
        else if(rank[x_rep]<rank[y_rep]){parent[x_rep] = y_rep;}
        else{parent[y_rep] = x_rep; rank[x_rep]++;}
    }

    // Custom comparator for sorting nodes based on their values
    // (node_index, node_value) pair
    static bool cmp(const std::vector<int>&x,const std::vector<int>&y)
    {
        return x[1]<y[1]; // Sort by node_value (second element)
    }

    int numberOfGoodPaths(std::vector<int>& value, std::vector<std::vector<int>>& edges) 
    {
        int n = value.size();

        // Build adjacency list for the graph
        std::vector<std::vector<int>> graph(n);
        for(const auto& e : edges)
        {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }

        // Create a list of (node_index, node_value) pairs for sorting
        std::vector<std::vector<int>> ranking;
        for(int i=0;i<n;i++){ranking.push_back({i,value[i]});}
        
        // Sort nodes by their values in ascending order
        std::sort(ranking.begin(),ranking.end(),cmp);

        // Initialize DSU parent and rank arrays
        std::vector<int> parent(n);
        std::iota(parent.begin(), parent.end(), 0); // Each node is initially its own parent
        std::vector<int> rank(n,0);

        int ans = 0; // Total count of good paths
        int i = 0;

        // Iterate through sorted nodes. Process nodes with the same value together.
        while(i < ranking.size())
        {
            int current_block_start_idx = i;
            int current_node_value = ranking[i][1];

            // Process all nodes that have the same value as current_node_value
            while(i < ranking.size() && ranking[i][1] == current_node_value)
            {
                int u = ranking[i][0]; // Current node index

                // For each neighbor 'v' of 'u'
                for(int v : graph[u])
                {
                    // Only union if neighbor's value is less than or equal to current node's value.
                    // This respects the good path definition.
                    if(value[v] <= value[u])
                    {
                        unionDSU(parent, rank, u, v);
                    }
                }
                i++;
            }
            
            // After processing all nodes with current_node_value and performing unions,
            // count good paths for this value.
            std::map<int,int> freq_of_value_in_component;
            
            // Iterate through nodes that were part of the current value block
            for(int j = current_block_start_idx; j < i; j++)
            {   
                int node_idx = ranking[j][0];
                int rep = find(parent, node_idx); // Find the representative of its set
                freq_of_value_in_component[rep]++; // Count frequency of current_node_value in each component
            }

            // Add (f * (f-1)) / 2 paths for each component, where f is the frequency.
            // This counts paths where current_node_value is the maximum value.
            for(auto const& [rep_node, freq] : freq_of_value_in_component)
            {
                ans += (freq * (freq - 1)) / 2;
            }
        }

        // Add 'n' to account for good paths of single nodes (each node itself is a good path).
        return ans + n;
    }
};
```