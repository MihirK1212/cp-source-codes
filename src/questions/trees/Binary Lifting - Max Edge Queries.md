# Binary Lifting - Maximum Edge Queries

## Problem Description

This problem involves a tree data structure where each edge has a weight. The goal is to efficiently answer queries about the maximum edge weight on the path between any two given nodes `u` and `v`. This can be solved using the Binary Lifting technique, which allows for fast LCA (Lowest Common Ancestor) and path queries.

## C++ Solution

```cpp
#define f first
#define s second

int LOG = 15; // Max log(N) where N is the maximum number of nodes. Adjust as needed.

// Function to find the maximum edge weight on the path between u and v
int findAns(int u,int v,vector<vector<int>>&parent,vector<vector<int>>&maxEdge,vector<int>&depth,int n,int LOG)
{
    if(depth[u]<depth[v]){swap(u,v);}
    
    int res = -1; // Stores the maximum edge weight found
    
    // Lift u to the same depth as v
    int k = depth[u]-depth[v];
    for(int j=0;j<LOG;j++)
    {
        if(k&(1<<j)){res=max(res,maxEdge[u][j]); u=parent[u][j];}    
    }
    
    // If u and v are the same, we've found the LCA and path is traversed
    if(u==v){return res;}
    
    // Lift u and v simultaneously until their parents are the same (just below LCA)
    for(int j=LOG-1;j>=0;j--)
    {
        if(parent[u][j]!=parent[v][j]) //we take the maximum possible jump upwards such that paths dont cross
        {
            res = max(res , maxEdge[u][j]);
            res = max(res , maxEdge[v][j]);
            u = parent[u][j];
            v = parent[v][j];
        }
    }
    
    // The LCA is parent[u][0]. The maximum edge in the path also includes edges to the LCA.
    res = max(res , maxEdge[u][0]);
    res = max(res , maxEdge[v][0]);
    
    return res;
}

// Preprocessing step to fill parent and maxEdge tables
void preprocess(vector<vector<int>>&parent,vector<vector<int>>&maxEdge,int n)
{
    for(int j=1;j<LOG;j++)
    {
        for(int u=1;u<=n;u++)
        {
            if(parent[u][j-1]==-1){continue;}
            
            parent[u][j] = parent[parent[u][j-1]][j-1];
        }
    }
    
    for(int j=1;j<LOG;j++)
    {
        for(int u=1;u<=n;u++)
        {
            if(parent[u][j-1]==-1 || parent[u][j]==-1){continue;}
            
            maxEdge[u][j] = max( maxEdge[u][j-1] , maxEdge[parent[u][j-1]][j-1] );
        }
    }
}

// DFS to fill initial parent, maxEdge (for 2^0 ancestor), and depth values
void dfs(map<int,vector<pair<int,int>>>&graph,int u,vector<vector<int>>&parent,int par,vector<vector<int>>&maxEdge,int pardEdge,vector<int>&depth,int d)
{
    parent[u][0] = par;
    maxEdge[u][0] = pardEdge;
    depth[u] = d;
    
    for(auto neighbours : graph[u])
    {
        if(neighbours.f == par){continue;}
        
        dfs(graph,neighbours.f,parent,u,maxEdge,neighbours.s,depth,d+1);
    }
}

// Debugging function (commented out in original)
// void printMatrix(vector<vector<int>>&matrix,int il,int ih,int jl,int jh)
// {
//     cout<<"\n";
//     for(int i=il;i<=ih;i++)
//     {
//         for(int j=jl;j<=jh;j++){cout<<matrix[i][j]<<" ";}
//         cout<<"\n";
//     }
//     cout<<"\n";
// }

vector<int> Solution::solve(vector<vector<int>> &edges, vector<vector<int> > &B) {
    
    int n = edges.size() + 1; // Assuming 1-indexed nodes from 1 to n
    map<int,vector<pair<int,int>>> graph;
    
    for(auto e : edges)
    {
        graph[e[0]].push_back({e[1],e[2]});
        graph[e[1]].push_back({e[0],e[2]});
    }
    
    vector<vector<int>> parent(n+1,vector<int>(LOG,-1));
    vector<vector<int>> maxEdge(n+1,vector<int>(LOG,-1));
    vector<int> depth(n+1);
    
    dfs(graph,1,parent,-1,maxEdge,-1,depth,0); // Start DFS from root (assuming node 1 is root)
    preprocess(parent,maxEdge,n);
    
    vector<int> ans;
    
    for(auto query : B)
    {
        int u = query[0] , v = query[1];
        ans.push_back(findAns(u,v,parent,maxEdge,depth,n,LOG));;   
    }
    
    return ans;
}
```