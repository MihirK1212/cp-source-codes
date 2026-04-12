# Find Distinct Subset Sums (DP)

## Problem Description

Given an array of integers, the problem asks to find and print all possible distinct sums that can be formed by choosing a subset of the elements from the array. This is a variation of the Subset Sum Problem and can be solved using dynamic programming.

**Example:**

For `arr = {2, 3, 4, 5, 6}`:

*   Possible sums: `0` (empty set), `2`, `3`, `4`, `5`, `6`, `2+3=5`, `2+4=6`, `2+5=7`, `2+6=8`, `3+4=7`, `3+5=8`, `3+6=9`, `4+5=9`, `4+6=10`, `5+6=11`, `2+3+4=9`, ..., `2+3+4+5+6 = 20`.

The goal is to list all unique sums.

## C++ Solution

The `printDistSum(int arr[], int n)` function uses dynamic programming to find all distinct subset sums.

**Algorithm:**

1.  **Calculate Total Sum:** First, calculate the `sum` of all elements in the input `arr`. This `sum` will be the maximum possible subset sum, and thus determines the size of the DP table.
2.  **DP Table Definition:** A 2D boolean array `dp[n+1][sum+1]` is used.
    *   `dp[i][j]` is `true` if a sum `j` can be formed using a subset of the first `i` elements (`arr[0...i-1]`). Otherwise, it's `false`.
3.  **Initialization:**
    *   `dp[i][0] = true` for all `i` from `0` to `n`: An empty set can always achieve a sum of `0`.
    *   Initialize the rest of the `dp` table to `false` (using `memset`).
4.  **Fill DP Table (Bottom-Up):** Iterate `i` from `1` to `n` (representing the current element `arr[i-1]`):
    *   `dp[i][arr[i-1]] = true;`: The current element `arr[i-1]` alone can form its own sum.
    *   Iterate `j` from `1` to `sum`:
        *   If `dp[i-1][j]` is `true` (meaning sum `j` was achievable using previous `i-1` elements):
            *   `dp[i][j] = true;`: Sum `j` is still achievable without `arr[i-1]` (by taking the subset that formed it previously).
            *   `dp[i][j + arr[i-1]] = true;`: Sum `j + arr[i-1]` is now also achievable by adding `arr[i-1]` to the subset that formed sum `j`.
5.  **Print Distinct Sums:** After filling the `dp` table, iterate through the last row (`dp[n]`) from `j = 0` to `sum`. If `dp[n][j]` is `true`, print `j`.

```cpp
#include <iostream>  // For std::cout
#include <vector>    // For std::vector (could be used instead of C-style array)
#include <numeric>   // For std::accumulate (for calculating total sum easily)
#include <cstring>   // For std::memset

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

// Function to find and print all distinct subset sums of a given array.
// arr: The input array of integers.
// n: The number of elements in the array.
void printDistSum(int arr[], int n)
{
    int total_sum = 0;
    // Calculate the total sum of all elements in the array.
    // This will be the maximum possible subset sum.
    for (int i = 0; i < n; i++){
        total_sum += arr[i];
    }

    // dp[i][j] would be true if arr[0...i-1] has a subset with sum equal to j.
    // The dimensions are (n+1) rows and (total_sum+1) columns.
    bool dp[n + 1][total_sum + 1];
    // Initialize all entries of the DP table to false.
    std::memset(dp, false, sizeof(dp));

    // Base case: A sum of 0 is always achievable with an empty set (0 elements).
    // So, for any number of elements considered (i), sum 0 is possible.
    for (int i = 0; i <= n; i++){
        dp[i][0] = true;
    }

    // Fill the dp[][] table in a bottom-up manner.
    // i iterates from 1 to n (considering arr[0] to arr[n-1]).
    for (int i = 1; i <= n; i++) 
    {
        // The current element itself forms a sum.
        // Note: This line might be redundant as it will be covered by the inner loop below.
        // It is harmless but can be removed if the inner loop is correctly structured.
        // dp[i][arr[i-1]] = true; 

        // j iterates from 1 to total_sum (possible subset sums).
        for (int j = 1; j <= total_sum; j++)
        {
            // Case 1: Exclude the current element arr[i-1].
            // If sum 'j' was achievable using elements arr[0...i-2], it is still achievable.
            dp[i][j] = dp[i-1][j];

            // Case 2: Include the current element arr[i-1].
            // This is possible if: 
            // a) The current sum 'j' is greater than or equal to arr[i-1].
            // b) The remaining sum (j - arr[i-1]) was achievable using elements arr[0...i-2].
            // If both conditions hold, then sum 'j' is achievable.
            if (j >= arr[i-1] && dp[i-1][j - arr[i-1]]) {
                dp[i][j] = true; // Set to true if either excluding or including makes it true
            }
        }
    }

    // Print all distinct sums that are achievable using all 'n' elements.
    std::cout << "Distinct subset sums:\n";
    for (int j = 0; j <= total_sum; j++){
        if (dp[n][j] == true){
            std::cout << j << " ";
        }
    }
    std::cout << "\n";
}

// Driver code
int main()
{
    // Optimize C++ standard streams for faster input/output
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL);

    int arr[] = {2, 3, 4, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    printDistSum(arr, n);

    // Example 2
    // int arr2[] = {1, 2, 3};
    // int n2 = sizeof(arr2) / sizeof(arr2[0]);
    // std::cout << "\n";
    // printDistSum(arr2, n2);

    return 0;
}
```