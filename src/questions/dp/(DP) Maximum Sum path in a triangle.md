# Maximum Path Sum in a Triangle (DP)

## Problem Description

This problem is from InterviewBit: [Maximum Path in Triangle](https://www.interviewbit.com/problems/maximum-path-in-triangle/)

Given a 2D integer array `A` of size `N x N` representing a triangle of numbers, find the maximum path sum from top to bottom. At each step, you may move to adjacent numbers on the row below.

**Note:** Adjacent cells to cell `(i, j)` are only `(i+1, j)` and `(i+1, j+1)`. Row `i` contains `i` integers and `n-i` zeroes for all `i` in `[1, n]` where zeroes represent empty cells.

## C++ Solution

```cpp
int Solution::solve(vector<vector<int> > &A) 
{
    int n = A.size();

    // dp[i][j] will store the maximum path sum starting from A[i][j] to the bottom
    int dp[n+1][n+1]; 

    // Iterate from the second last row up to the top row
    for(int i=n-1;i>=0;i--)
    {
        // Iterate through elements in the current row
        for(int j=i;j>=0;j--)
        {
            // For the last row, the maximum path sum is just the element itself
            if (i == n - 1) {
                dp[i][j] = A[i][j];
            } else {
                // For other rows, the maximum path sum is the current element
                // plus the maximum of its two adjacent elements in the row below.
                dp[i][j] = A[i][j] + max(dp[i+1][j], dp[i+1][j+1]);
            }
        }
    }

    return dp[0][0]; // The result is at the top of the triangle
}
```