# Sum Query in 2D Array (Dynamic Programming / 2D Prefix Sums)

## Problem Description

Given a 2D integer matrix `A` and an integer `B`, the task is to find the maximum sum of all possible square submatrices of size `B x B` within the matrix `A`.

This problem is efficiently solved using a technique called **2D Prefix Sums** (or **Summed-Area Table**). This method allows for calculating the sum of any rectangular submatrix in O(1) time after an initial O(rows * columns) preprocessing step.

## C++ Solution

This C++ solution uses a 2D prefix sum array to calculate the sum of `B x B` submatrices in constant time, thereby finding the maximum sum efficiently.

**`Solution::solve(vector<vector<int> > &A, int B)` function:**

*   **Parameters:**
    *   `A`: The input 2D integer matrix.
    *   `B`: The size of the square submatrix (i.e., `B x B`).
*   **Logic:**

    1.  **Initialize 2D Prefix Sum Array (`p_sum`):**
        *   Create a `vector<vector<int>> p_sum` of size `(m+1) x (n+1)`, where `m` is the number of rows and `n` is the number of columns in `A`.
        *   This `p_sum` array will store `p_sum[i][j] = sum` of elements in the rectangle from `(0,0)` to `(i-1, j-1)` in the original matrix `A`.
        *   Initialize the first row and first column of `p_sum` to zeros. `p_sum[i][0]=0` and `p_sum[0][j]=0`.

    2.  **Build 2D Prefix Sum Array:**
        *   Iterate `i` from `1` to `m` and `j` from `1` to `n`.
        *   The recurrence relation for `p_sum[i][j]` is:
            ```
            p_sum[i][j] = p_sum[i-1][j] + p_sum[i][j-1] - p_sum[i-1][j-1] + A[i-1][j-1];
            ```
            This formula calculates the sum of the rectangle ending at `(i-1, j-1)` in `A`.

    3.  **Calculate Maximum `B x B` Submatrix Sum:**
        *   Initialize `max_sum = -1e8` (a very small number to correctly capture the maximum sum, even if all sums are negative).
        *   Iterate `i` from `1` to `m` and `j` from `1` to `n`. These `i` and `j` represent the *bottom-right corner* (exclusive for `p_sum` indexing, inclusive for `A` indexing) of potential `B x B` submatrices.
        *   **Check for valid `B x B` submatrix:** A `B x B` submatrix ending at `(i-1, j-1)` (in `A`) implies its top-left corner is `(i-B, j-B)`. Thus, `i-B` and `j-B` must be `>= 0` (or `i >= B` and `j >= B` for `A` indexing). For `p_sum` 1-based indexing, this check becomes `i-B >= 0` and `j-B >= 0` for the top-left corner index (exclusive).
        *   **Query Submatrix Sum:** If `i-B >= 0` and `j-B >= 0` (meaning a `B x B` square can be formed with its bottom-right at `A[i-1][j-1]`):
            *   The sum of the `B x B` submatrix with bottom-right corner at `A[i-1][j-1]` can be calculated as:
                ```
                sum = p_sum[i][j] - p_sum[i-B][j] - p_sum[i][j-B] + p_sum[i-B][j-B];
                ```
            *   Update `max_sum = max(max_sum, sum)`.

    4.  **Return Result:** Return `max_sum`.

```cpp
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::max
#include <limits>    // Required for std::numeric_limits

class Solution {
public:
    // Function to find the maximum sum of a B x B square submatrix in a 2D integer matrix A.
    int solve(std::vector<std::vector<int>>& A, int B) 
    {
        // Handle empty matrix cases
        if (A.empty() || A[0].empty() || B <= 0) {
            return 0; // Or throw an error depending on problem constraints
        }

        int m = A.size();    // Number of rows in A
        int n = A[0].size(); // Number of columns in A

        // If B is larger than matrix dimensions, no valid BxX submatrix exists.
        if (B > m || B > n) {
            return 0; // Or return -1, problem-specific
        }

        // Create a 2D prefix sum (summed-area table) array.
        // p_sum[i][j] stores the sum of elements in the rectangle from (0,0) to (i-1, j-1) in A.
        // Size (m+1) x (n+1) for 1-based indexing convenience.
        std::vector<std::vector<int>> p_sum(m + 1, std::vector<int>(n + 1, 0));

        // Build the 2D prefix sum array
        for(int i = 1; i <= m; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                p_sum[i][j] = p_sum[i-1][j] + p_sum[i][j-1] - p_sum[i-1][j-1] + A[i-1][j-1];
            }
        }

        // Initialize max_sum to the smallest possible integer value
        int max_sum = std::numeric_limits<int>::min();

        // Iterate through all possible bottom-right corners (i, j) of B x B submatrices.
        // For 1-based p_sum, i and j refer to the bottom-right coordinate of the prefix sum rectangle.
        for(int i = 1; i <= m; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                // Check if a B x B submatrix can be formed with (i-1, j-1) as its bottom-right corner.
                // This means its top-left corner would be (i-B, j-B) (using 0-based A indexing).
                // So, i-B must be >= 0 and j-B must be >= 0 (for p_sum, these refer to the row/column just before the submatrix starts).
                if(i - B >= 0 && j - B >= 0)
                {
                    // Calculate the sum of the B x B submatrix using the 2D prefix sum formula:
                    // Sum(R1,C1,R2,C2) = p_sum[R2+1][C2+1] - p_sum[R1][C2+1] - p_sum[R2+1][C1] + p_sum[R1][C1]
                    // Here, top-left is (i-B, j-B) in p_sum coordinate terms.
                    // bottom-right is (i, j) in p_sum coordinate terms.
                    int current_submatrix_sum = p_sum[i][j] 
                                              - p_sum[i-B][j] 
                                              - p_sum[i][j-B] 
                                              + p_sum[i-B][j-B];
                    
                    max_sum = std::max(max_sum, current_submatrix_sum);
                }
            }
        }

        return max_sum;
    }
};
```