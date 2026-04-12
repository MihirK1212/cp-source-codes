# Kth Manhattan Distance Neighbourhood (DP)

## Problem Description

Given a 2D integer matrix `A` of size `M x N`, and an integer `K`, find for each cell `(i, j)` the maximum value among all cells `(x, y)` such that the Manhattan distance `|i-x| + |j-y| <= K`. The result should be a new matrix of the same dimensions where each `(i, j)` cell contains this maximum value.

The Manhattan distance between two points `(x1, y1)` and `(x2, y2)` is `|x1 - x2| + |y1 - y2|`.

## C++ Solution

This solution uses dynamic programming. `dp[k][i][j]` represents the maximum value in the `k`-th Manhattan distance neighbourhood of cell `(i, j)`. The solution iteratively builds up the maximums for `k=1` to `K`.

```cpp
bool satisfies(int i,int j,int m,int n)
{
    return i>=0 && j>=0 && i<m && j<n;
}

// Helper function to find the maximum value among A[i][j] and its direct neighbors
// This is used for computing the next level of Manhattan distance
int findMax(vector<vector<int>>&A,int i,int j,int m,int n)
{
    int mval = A[i][j]; // Start with the current cell's value

    // Check and update max with adjacent cells (Manhattan distance 1)
    if(satisfies(i-1,j,m,n)){mval=max(mval,A[i-1][j]);}
    if(satisfies(i,j+1,m,n)){mval=max(mval,A[i][j+1]);}
    if(satisfies(i+1,j,m,n)){mval=max(mval,A[i+1][j]);}
    if(satisfies(i,j-1,m,n)){mval=max(mval,A[i][j-1]);}

    return mval;
}

vector<vector<int> > Solution::solve(int K, vector<vector<int> > &A) 
{
    int m = A.size(); // Number of rows
    int n = A[0].size(); // Number of columns

    // curr and next matrices are used to store DP states iteratively
    // curr stores dp[k-1] and next stores dp[k]
    vector<vector<int>> curr = A; // Initialize with the original matrix (K=0 neighbourhood)
    vector<vector<int>> next = A; // Will store the results for the current K iteration

    // Iterate for K steps (Manhattan distance)
    for(int k=1;k<=K;k++)
    {
        // For each cell, calculate the maximum value in its k-th Manhattan distance neighbourhood
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                // The maximum for dp[k][i][j] is the maximum of dp[k-1][i][j]
                // and dp[k-1] of its direct neighbors (up, down, left, right).
                // This is effectively finding the maximum in the (k-1) neighbourhood
                // of (i,j) and its direct neighbors, which expands the search to k.
                next[i][j] = findMax(curr,i,j,m,n);
            }
        }
        // Update curr to next for the next iteration
        curr = next;
    }

    return curr; // The final matrix with Kth Manhattan distance neighbourhood maximums
}
```