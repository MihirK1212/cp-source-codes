# Find All Possible Paths from Start to End

## Problem Description

This problem is available on LeetCode: [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/submissions/)

This solution works for a directed acyclic graph.

## C++ Solution

```cpp
class Solution {
public:
    
    vector<vector<int>> ans;
    vector<int> path;
    
    int start,end;
    
    void dfs(vector<vector<int>>& graph,int node)
    {
        int n = graph.size();
        
       path.push_back(node);

        if(node==end)
        {
            ans.push_back(path);
            path.pop_back();
            return;
        }
        
       for(auto v: graph[node])
        {
           dfs(graph,v);
        }
        
        path.pop_back();
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph)
    {
        int n = graph.size();
        
        dfs(graph,start);
        return ans;
    }
};
```