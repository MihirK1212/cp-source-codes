# Binary Search: Search in Sorted Matrix

## Problem Description

Given an `m x n` integer matrix `matrix` with the following properties:

*   Each row is sorted in non-decreasing order.
*   Each column is sorted in non-decreasing order.

Given a `target` integer, return `true` if `target` is in the matrix, and `false` otherwise.

This problem can be efficiently solved using a tailored search approach that resembles a binary search on the matrix, taking advantage of its sorted properties.

## C++ Solution

This C++ solution implements an efficient search algorithm for a target value in a row-wise and column-wise sorted 2D matrix. The strategy involves starting the search from the top-right corner (or bottom-left corner) of the matrix.

**Algorithm (Starting from Top-Right Corner):**

1.  **Initialization:**
    *   Initialize `i = 0` (row index, starting from the first row).
    *   Initialize `j = n - 1` (column index, starting from the last column).
    *   `m` is the number of rows, `n` is the number of columns.

2.  **Search Loop:** Continue searching while `i` is within valid row bounds (`0 <= i < m`) and `j` is within valid column bounds (`0 <= j < n`).
    *   **Case 1: `matrix[i][j] == target`**
        *   If the current element is equal to the `target`, we found it. Return `true`.
    *   **Case 2: `matrix[i][j] < target`**
        *   If the current element is smaller than the `target`, it means that `target` cannot be in the current column (because all elements below `matrix[i][j]` in this column would be greater than or equal to `matrix[i][j]`, but `target` is greater than `matrix[i][j]`, so it could be below). More accurately, since the row is sorted, all elements to the left of `matrix[i][j]` in the current row are even smaller. Therefore, the `target` must be in a row below the current one. Move down to the next row: `i++`.
    *   **Case 3: `matrix[i][j] > target`**
        *   If the current element is larger than the `target`, it means that `target` cannot be in the current row (because all elements to the right of `matrix[i][j]` in this row would be greater than or equal to `matrix[i][j]`). Therefore, the `target` must be in a column to the left of the current one. Move left to the previous column: `j--`.

3.  **Result:**
    *   If the loop finishes without finding the `target`, it means the `target` is not present in the matrix. Return `false`.

This approach effectively eliminates one row or one column in each step, leading to an `O(m + n)` time complexity.

```cpp
#include <vector> // Required for std::vector
#include <algorithm> // Not explicitly used but generally useful

class Solution {
public:
    // Function to search for a target value in a row-wise and column-wise sorted matrix.
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        // Handle empty matrix case
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }

        int m = matrix.size();    // Number of rows
        int n = matrix[0].size(); // Number of columns
        
        // Start search from the top-right corner of the matrix.
        // i: current row index (starts at 0)
        // j: current column index (starts at n-1)
        int i = 0;
        int j = n - 1;

        // Continue search as long as indices are within matrix bounds
        while(i >= 0 && i < m && j >= 0 && j < n)
        {
            // If the current element matches the target, return true.
            if((matrix[i][j]) == target)
            {
                return true;
            }
            
            // If the current element is less than the target, 
            // it means the target must be in a row below (since current row elements to left are smaller).
            // Move down to the next row.
            if(matrix[i][j] < target)
            {
                i++;
            }
            else // If the current element is greater than the target,
            {
                // it means the target must be in a column to the left (since current column elements below are larger).
                // Move left to the previous column.
                j--;
            }
        }
        
        // If the loop completes, the target was not found.
        return false;
    }
};
```