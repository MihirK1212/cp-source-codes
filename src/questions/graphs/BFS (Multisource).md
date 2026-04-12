# Multi-Source BFS - Nearest Hotel

## Problem Description

This problem is from InterviewBit: [Hotel Service](https://www.interviewbit.com/problems/hotel-service/).

You are given a 2D grid representing a city. Some cells contain hotels (marked as 1), and other cells are empty (marked as 0). You are also given a list of queries, where each query `(r, c)` represents a customer's location. For each customer, you need to find the shortest Manhattan distance to the nearest hotel.

Manhattan distance between two points `(x1, y1)` and `(x2, y2)` is `|x1 - x2| + |y1 - y2|`.

This problem is typically solved using a Multi-Source Breadth-First Search (BFS). Instead of starting BFS from a single source, we start from all hotel locations simultaneously.

## C++ Solution

This solution employs a Multi-Source BFS to calculate the shortest distance from every cell to its nearest hotel.

1.  **Initialization:**
    *   `q`: A queue to store `(row, col)` pairs for BFS traversal.
    *   `N`, `M`: Dimensions of the grid `A`.
    *   `dist`: A 2D array initialized with `INT_MAX` to store the shortest distance from each cell to a hotel.
    *   All cells containing a hotel (`A[i][j] == 1`) are added to the `q`, and their `dist[i][j]` is set to `0`. This is the "multi-source" part.
2.  **BFS Traversal:**
    *   `moves`: A vector of `(dr, dc)` pairs representing possible movements (up, down, left, right).
    *   While `q` is not empty:
        *   Process all nodes at the current level (`s = q.size()`).
        *   For each cell `(x, y)` dequeued from `q`:
            *   Explore its 4 neighbors `(px, py)`.
            *   If a neighbor is within grid bounds and its current `dist[px][py]` is greater than `dist[x][y] + 1`:
                *   Update `dist[px][py] = dist[x][y] + 1`.
                *   Enqueue `(px, py)`.
3.  **Query Processing:**
    *   `ans`: A vector to store the results for each query.
    *   For each query `p` in `B`:
        *   Convert 1-indexed query coordinates to 0-indexed `px, py`.
        *   Add `dist[px][py]` to `ans`.
    *   Return `ans`.

```cpp
#include <vector>
#include <queue>
#include <utility> // For std::pair
#include <limits>  // For INT_MAX

// Function to find the shortest distance from each query point to the nearest hotel.
// A: 2D grid where 1 represents a hotel, 0 represents an empty cell.
// B: List of query points (1-indexed coordinates).
vector<int> Solution::nearestHotel(vector<vector<int> > &A, vector<vector<int> > &B) 
{
    queue<pair<int,int>> q; // Queue for BFS (stores {row, col})
    
    int N = A.size();
    int M = A[0].size();

    // Initialize distance matrix with a large value (infinity)
    vector<vector<int>> dist(N,vector<int>(M,std::numeric_limits<int>::max()));

    // Add all hotel locations as initial sources to the BFS queue
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            if(A[i][j]==1){ // If it's a hotel
                q.push({i,j});
                dist[i][j] = 0; // Distance from a hotel to itself is 0
            }
        }
    }

    // Possible moves (up, down, left, right)
    vector<pair<int,int>> moves = {{0,1},{1,0},{0,-1},{-1,0}};

    // Perform Multi-Source BFS
    while(!q.empty())
    {
        // No need for 's = q.size()' loop if not processing layer by layer strictly,
        // but it's good practice for level-order traversal. For shortest path, it works either way.
        // int s = q.size(); // Current level size
        // while(s--)
        // {
            int x = (q.front()).first;
            int y = (q.front()).second;
            q.pop();
            
            for(auto it : moves) // Explore neighbors
            {
                int px = x + it.first;
                int py = y + it.second;

                // Check bounds
                if(!(px>=0 && px<N && py>=0 && py<M)){continue;}
                
                // If we found a shorter path to (px, py)
                if(dist[px][py] > (dist[x][y] + 1))
                {
                    dist[px][py] = dist[x][y] + 1; // Update distance
                    q.push({px,py}); // Enqueue neighbor
                }
            }
        // } // End of current level processing
    }

    // Process queries from B
    vector<int> ans;
    for(auto p : B)
    {
        // Convert 1-indexed query coordinates to 0-indexed
        int px = p[0]-1;
        int py = p[1]-1;
        ans.push_back(dist[px][py]); // Add the shortest distance to answer
    }

    return ans;
}
```