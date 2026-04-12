# Queen Attack (Number of Attacking Queens)

## Problem Description

This problem is from InterviewBit: [Queen Attack](https://www.interviewbit.com/problems/queen-attack/)

Given a chessboard represented by a `vector<string> A`, where '1' denotes the presence of a queen and '0' denotes an empty cell, determine for each empty cell `(i, j)` the number of queens that can attack it. A queen can attack horizontally, vertically, and diagonally.

## C++ Solution

{% raw %}
```cpp
vector<vector<int> > Solution::queenAttack(vector<string> &A) 
{
    int m = A.size(); // Number of rows
    int n = A[0].size(); // Number of columns

    vector<vector<int>> dp(m,vector<int>(n,0)); // dp[i][j] will store the number of queens attacking cell (i,j)

    // Define all 8 possible directions a queen can move
    vector<pair<int,int>> moves = {{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1}};

    // Iterate through each cell of the chessboard
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            // For each cell, check all 8 directions for attacking queens
            for(auto p : moves)
            {   
                int x = i + p.first , y = j + p.second; 
                
                // Traverse in the current direction until a queen is found or board boundary is reached
                while(x>=0 && x<m && y>=0 && y<n)
                {
                    if(A[x][y]=='1') // If a queen is found, increment count and break from this direction
                    {
                        dp[i][j]++; 
                        break;
                    }
                    x = x + p.first ; // Move to the next cell in the same direction
                    y = y + p.second; 
                }
            }
        }
    }

    return dp;
}
```
{% endraw %}