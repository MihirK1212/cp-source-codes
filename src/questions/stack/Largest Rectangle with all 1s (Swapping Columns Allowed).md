# Largest Rectangle with all 1s (Swapping Columns Allowed)

## Problem Description

Given a binary matrix (a matrix containing only 0s and 1s), find the largest rectangle containing only 1s. A crucial aspect of this problem is that **you are allowed to swap columns** to achieve the largest rectangle. This allowance simplifies the problem significantly.

**Interpretation with Column Swapping:**

When column swapping is allowed, for any chosen set of rows, we can arrange the columns such that all columns with a continuous block of 1s are adjacent. This effectively means that for each row, we can calculate the height of contiguous 1s for each column. These heights can then be sorted, and the problem reduces to finding the largest rectangle in a histogram where the histogram bars (column heights) are sorted.

## C++ Solution

This C++ solution uses dynamic programming and a simplified approach for largest rectangle in a histogram due to the column swapping allowance.

**Algorithm:**

1.  **Iterate Through Rows:** The main `solve` function iterates through each row of the input binary matrix `A`.
2.  **Calculate Column Heights (`colSum`):**
    *   A 1D array `colSum` is maintained. `colSum[j]` stores the current height of consecutive 1s ending at the current row `i` for column `j`.
    *   If `A[i][j]` is 1, `colSum[j]` is incremented.
    *   If `A[i][j]` is 0, `colSum[j]` is reset to 0 (the continuous block of 1s is broken).
3.  **Find Max Rectangle in Histogram (`findMaxRectangle`):**
    *   For each row, after `colSum` is updated, the `findMaxRectangle` function is called with the current `colSum` array.
    *   **Inside `findMaxRectangle`:**
        1.  The `colSum` array (representing histogram heights) is sorted in non-decreasing order. This step is valid because columns can be swapped.
        2.  For a sorted array of heights `A = [h_0, h_1, ..., h_{n-1}]` where `h_0 <= h_1 <= ... <= h_{n-1}`, the largest rectangle that can be formed using `h_i` as its height will have a width of `(n - i)`. This is because `h_i` can extend to all bars to its right (including itself), as they are all greater than or equal to `h_i`.
        3.  The maximum area is then calculated as `max(A[i] * (n - i))` for all `i` from `0` to `n-1`.
    *   The maximum area found for the current row is then compared with the overall maximum answer (`ans`).
4.  **Return Result:** The function returns the maximum area found across all rows.

```cpp
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::sort, std::max

// using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Function to find the largest rectangle in a histogram, where bars can be reordered.
// This means the input vector 'A' can be sorted before calculating the area.
int findMaxRectangle(std::vector<int>& A)
{
    // Sort the heights. This is allowed because columns can be swapped.
    // After sorting, for any bar A[i], all bars to its right are >= A[i].
    std::sort(A.begin(), A.end());
    
    int n = A.size();
    int max_area = 0;

    // Iterate through the sorted heights
    for(int i = 0; i < n; i++)
    {
        // For each bar A[i] (current height), it can extend to the right for (n - i) columns.
        // The width of the rectangle formed by A[i] as height is (n - i).
        // Calculate the area and update max_area.
        max_area = std::max(max_area, A[i] * (n - i));
    }

    return max_area;
}

class Solution {
public:
    // Main function to solve the problem: Largest Rectangle with all 1s (Swapping Columns Allowed)
    int solve(std::vector<std::vector<int>>& A) 
    {
        // Handle empty matrix cases
        if (A.empty() || A[0].empty()) {
            return 0;
        }

        int m = A.size();    // Number of rows
        int n = A[0].size(); // Number of columns

        int ans = 0; // Stores the overall maximum rectangle area

        // colSum[j] will store the current height of consecutive 1s in column j
        // Initialize colSum based on the first row
        std::vector<int> colSum(n, 0);
        for(int j = 0; j < n; j++){
            colSum[j] = (A[0][j] == 1); // 1 if A[0][j] is 1, else 0
        }
        
        // Calculate initial max rectangle area for the first row
        ans = std::max(ans, findMaxRectangle(colSum));

        // Iterate through the remaining rows, from the second row onwards
        for(int i = 1; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(A[i][j] == 1){
                    colSum[j]++; // Extend the height of 1s if current cell is 1
                }
                else{
                    colSum[j] = 0; // Reset height to 0 if current cell is 0
                }
            }
            // After updating colSum for the current row, find max rectangle area
            ans = std::max(ans, findMaxRectangle(colSum));
        }

        return ans;
    }
};
```