# BFS 01 Matrix (Multi-source BFS)

## Problem Description

Given a binary matrix `mat` of `m x n`, return the distance of the nearest `0` for each cell. The distance between two adjacent cells is 1. This problem can be efficiently solved using a multi-source Breadth-First Search (BFS).

## C++ Solution

```cpp
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) 
    {
        int r = mat.size();
        int c = mat[0].size();
        vector<vector<int>> min_dist(r,vector<int>(c));
        
        queue<pair<int,int>> q; // Queue for BFS, storing {row, col}
        
        // Initialize min_dist and populate the queue with all '0' cells
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(mat[i][j]==0){min_dist[i][j]=0; q.push({i,j});}
                else{min_dist[i][j]=1e8;}
            }
        }
        
        
        while(!q.empty())
        {
            int curr_x = (q.front()).first;
            int curr_y = (q.front()).second;
            q.pop();
            
            // Define neighbors (up, down, left, right)
            vector<pair<int,int>> neigbours;
            neigbours.push_back({curr_x+1,curr_y}); 
            neigbours.push_back({curr_x-1,curr_y});
            neigbours.push_back({curr_x,curr_y+1}); 
            neigbours.push_back({curr_x,curr_y-1});
            
            for(auto p:neigbours)
            {
                // Check for boundary conditions
                if(p.first<0 || p.first>=r || p.second<0 || p.second>=c){continue;}
                
                int old_dist = min_dist[p.first][p.second];
                int new_dist = min_dist[curr_x][curr_y] + 1;
                
                // If a shorter path is found, update distance and push to queue
                if(new_dist<old_dist)
                {
                    min_dist[p.first][p.second] = new_dist;
                    q.push(p);    
                }
            }
        }
        
        return min_dist;
    
    }
};
```