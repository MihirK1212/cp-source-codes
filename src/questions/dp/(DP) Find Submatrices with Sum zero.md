# Find Submatrices with Sum Zero (Dynamic Programming / Prefix Sums)

## Problem Description

This problem asks us to find the total number of submatrices within a given 2D integer matrix `A` whose elements sum up to zero.

**Approach:**

The standard approach to solve this problem is to fix the top and bottom rows of a potential submatrix. Once these rows are fixed, the problem reduces to finding subarrays with a sum of zero in a 1D array. This 1D array is formed by summing the elements column-wise between the fixed top and bottom rows.

We iterate through all possible pairs of `(top_row, bottom_row)`. For each pair, we create a temporary 1D array `row_sum`. For each column `j`, `row_sum[j]` will store the sum of `A[i][j]` for `top_row <= i <= bottom_row`.

Then, we use a helper function (similar to finding subarrays with sum zero in a 1D array) to count how many subsegments of `row_sum` sum to zero. This count is added to our total answer.

## C++ Solution

This C++ solution implements the described approach.

**`find(vector<int>& arr)` function:**

This helper function takes a 1D array `arr` and returns the count of subarrays within `arr` that sum to zero. It uses a hash map (`unordered_map`) to store the frequency of prefix sums encountered so far.

*   Initialize `p_sum_freq` (map to store frequency of prefix sums), `sum = 0`, `count = 0`.
*   Iterate through the `arr`:
    *   Add `arr[i]` to `sum`.
    *   If `sum == 0`, it means the subarray from index 0 to `i` sums to zero, so increment `count`.
    *   Add `p_sum_freq[sum]` to `count`. This accounts for subarrays ending at `i` whose sum is `sum` (meaning the subarray from a previous index `j+1` to `i` sums to zero).
    *   Increment `p_sum_freq[sum]`.

**`Solution::solve(vector<vector<int> > &A)` function:**

This is the main function that finds the total number of zero-sum submatrices.

*   Handle edge cases for empty matrix.
*   Initialize `ans = 0`.
*   Outer loop iterates `l` from `0` to `n-1` (representing the starting column of a submatrix).
*   Inner loop iterates `r` from `l` to `n-1` (representing the ending column of a submatrix).
    *   Inside these loops, `row_sum` is a temporary 1D array of size `m` (number of rows), initialized to zeros.
    *   Innermost loop iterates `i` from `0` to `m-1` (iterating through rows).
        *   `row_sum[i] += A[i][r]` accumulates the sum for the current column range `[l, r]` into each row of `row_sum`.
    *   After updating `row_sum` for the current column `r`, call `find(row_sum)` to get the count of zero-sum subarrays in this `row_sum` array. Add this to `ans`.
*   Return `ans`.

```cpp
#include <vector>
#include <unordered_map>
#include <numeric> // Required for std::accumulate (though not used in given snippet)

using namespace std;

// Helper function to find the number of subarrays with sum zero in a 1D array
int find(vector<int>& arr)
{
    unordered_map<int,int> p_sum_freq; // Map to store frequency of prefix sums

    int sum = 0;   // Current prefix sum
    int count = 0; // Count of subarrays with sum zero

    for(int i=0; i<arr.size(); i++)
    {
        sum += arr[i];

        // If current prefix sum is 0, a subarray from index 0 to i sums to zero
        if(sum == 0) {
            count++;
        }

        // Add the frequency of the current sum to count.
        // This means a subarray between a previous occurrence of 'sum' and current index i
        // has a sum of zero.
        count += p_sum_freq[sum];
        
        // Increment frequency of current prefix sum
        p_sum_freq[sum]++;
    }

    return count; 
}

class Solution {
public:
    int solve(vector<vector<int> > &A) 
    {
        if(A.size()==0 || A[0].size()==0){return 0;}
        
        int m = A.size();    // Number of rows
        int n = A[0].size(); // Number of columns

        int ans = 0; // Total count of zero-sum submatrices

        // Iterate over all possible starting columns (l)
        for(int l=0; l<n; l++)
        {
            // Initialize a 1D array to store the sum of elements for the current column range
            // across all rows. This effectively compresses the rows for a fixed column range.
            vector<int> row_sum(m, 0);

            // Iterate over all possible ending columns (r) for the current starting column (l)
            for(int r=l; r<n; r++)
            {
                // Update the row_sum array by adding elements from the current column 'r'
                // for each row.
                for(int i=0; i<m; i++){
                    row_sum[i] += A[i][r];
                }

                // After updating row_sum for the current column range [l, r],
                // find the number of zero-sum subarrays within this 1D row_sum array.
                // Each such subarray corresponds to a zero-sum submatrix.
                ans += find(row_sum);
            }
        }

        return ans;
    }
};
```