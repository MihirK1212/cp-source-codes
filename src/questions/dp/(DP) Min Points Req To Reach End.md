# Minimum Points Required To Reach End (Dungeon Princess - Dynamic Programming)

## Problem Description

This problem is from InterviewBit: [Dungeon Princess](https://www.interviewbit.com/problems/dungeon-princess/).

A knight is in a dungeon, which is represented by an `m x n` grid. Each cell in the dungeon contains an integer that represents either a health boost or health penalty. The knight starts at the top-left cell `(0, 0)` and wants to reach the bottom-right cell `(m-1, n-1)`. The knight can only move right or down. During the journey, the knight's health must *always* be greater than 0. The objective is to find the minimum initial health points the knight must have to successfully reach the destination.

## C++ Solution

This C++ solution uses dynamic programming to solve the Dungeon Princess problem. The key insight is to work backward from the destination to the starting point.

**DP Table Definition:**

*   `dp[i][j]` = The minimum initial health points required at cell `(i, j)` to reach the destination `(m-1, n-1)` such that health never drops to 0 or below along any path from `(i, j)` to `(m-1, n-1)`.

**Approach (Backward DP):**

We fill the `dp` table from bottom-right to top-left.

**Base Case (Destination `(m-1, n-1)`):**

*   If `A[m-1][n-1] >= 0` (health boost or zero at destination):
    *   The knight needs at least `1` health point upon entering this cell to survive. So, `dp[m-1][n-1] = 1`.
*   If `A[m-1][n-1] < 0` (health penalty at destination):
    *   The knight needs `abs(A[m-1][n-1]) + 1` health points upon entering this cell to survive and have at least 1 HP after the penalty. So, `dp[m-1][n-1] = abs(A[m-1][n-1]) + 1`.

**Filling Last Row and Last Column:**

*   **Last Column (moving up from `m-2` to `0` for `j = n-1`):**
    *   `dp[i][n-1]` depends only on `dp[i+1][n-1]`.
    *   If `A[i][n-1] >= 0`:
        *   `dp[i][n-1] = max(1, dp[i+1][n-1] - A[i][n-1])`. We need `dp[i+1][n-1]` health to survive from `(i+1, n-1)`, but `A[i][n-1]` gives a boost. We must ensure health is at least 1 after boost.
    *   If `A[i][n-1] < 0`:
        *   `dp[i][n-1] = dp[i+1][n-1] + abs(A[i][n-1])`. We need `dp[i+1][n-1]` health, and we also need to compensate for the penalty at `A[i][n-1]`.

*   **Last Row (moving left from `n-2` to `0` for `i = m-1`):**
    *   Similar logic to the last column, but depending on `dp[m-1][j+1]`.

**Filling Inner Cells (moving up and left from `m-2, n-2` to `0, 0`):**

*   For `dp[i][j]`, the knight can move to `(i+1, j)` or `(i, j+1)`. We want the *minimum* initial health, so we choose the path that requires less health.
*   `dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - A[i][j])`.
    *   `min(dp[i+1][j], dp[i][j+1])` gives the minimum health needed from the next step.
    *   Subtract `A[i][j]` (current cell's value).
    *   `max(1, ...)` ensures that the required health is at least 1.

**Final Answer:**

The minimum initial health points required from the start `(0, 0)` is `dp[0][0]`.

```cpp
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::max, std::min
#include <cmath>     // Required for std::abs

class Solution {
public:
    // Function to calculate the minimum initial health points required to reach the destination.
    int calculateMinimumHP(std::vector<std::vector<int>>>& A) 
    {   
        // Handle empty dungeon case
        if (A.empty() || A[0].empty()) {
            return 1; // Need at least 1 HP to start
        }

        int m = A.size();    // Number of rows
        int n = A[0].size(); // Number of columns

        // dp[i][j] = minimum initial health points required at cell (i,j) to reach (m-1,n-1)
        // and survive with at least 1 HP at all times.
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, 0));

        // Base Case: Destination cell (m-1, n-1)
        if(A[m-1][n-1] >= 0){
            dp[m-1][n-1] = 1; // If health is positive/zero, need 1 HP to enter
        }
        else{
            // If health is negative, need enough HP to cover penalty and still have 1 HP.
            dp[m-1][n-1] = std::abs(A[m-1][n-1]) + 1;
        }

        // Fill the last column (moving upwards)
        for(int i = m - 2; i >= 0; i--)
        {
            // Minimum HP needed from (i+1, n-1) is dp[i+1][n-1].
            // If A[i][n-1] is a boost, subtract it from needed HP, but ensure result is at least 1.
            // If A[i][n-1] is a penalty, add its absolute value to needed HP.
            dp[i][n-1] = std::max(1, dp[i+1][n-1] - A[i][n-1]);
        }

        // Fill the last row (moving leftwards)
        for(int j = n - 2; j >= 0; j--)
        {
            // Similar logic as filling the last column, but considering dp[m-1][j+1].
            dp[m-1][j] = std::max(1, dp[m-1][j+1] - A[m-1][j]);
        }

        // Fill the rest of the DP table (moving upwards and leftwards)
        for(int i = m - 2; i >= 0; i--)
        {
            for(int j = n - 2; j >= 0; j--)
            {
                // Knight can move right or down. Choose the path that requires minimum health.
                // min_health_from_next_step = min(dp[i+1][j], dp[i][j+1]).
                // Required HP at (i,j) = min_health_from_next_step - A[i][j].
                // Ensure required HP is at least 1.
                dp[i][j] = std::max(1, std::min(dp[i+1][j], dp[i][j+1]) - A[i][j]);
            }
        }

        return dp[0][0]; // The answer is the minimum HP required at the starting cell (0,0).
    }
};
```