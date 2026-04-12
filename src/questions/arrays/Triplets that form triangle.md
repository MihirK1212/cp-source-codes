# Triplets That Form a Triangle (Counting Triangles)

## Problem Description

Given an unsorted array of positive integers, the task is to find the number of triplets `(a, b, c)` from the array that can form the sides of a valid triangle. A triplet `(a, b, c)` can form a triangle if and only if the sum of any two sides is greater than the third side:

1.  `a + b > c`
2.  `a + c > b`
3.  `b + c > a`

## C++ Solution

This C++ solution efficiently counts the number of valid triangle triplets from a given array. The key steps involve sorting the array and then using a two-pointer technique.

**Algorithm:**

1.  **Sort the Array:** First, sort the input array `arr` in non-decreasing order. This simplifies the triangle conditions. If `a <= b <= c`, then conditions `a + c > b` and `b + c > a` are automatically satisfied (since `c` is the largest side, `a+c` and `b+c` will always be greater than `b` and `a` respectively). We only need to check the condition `a + b > c`.

2.  **Iterate for the Largest Side `c`:** Iterate from the rightmost element of the sorted array, using it as the potential largest side `c` of a triangle. Let this element be `arr[i]`.

3.  **Two-Pointer Approach for `a` and `b`:** For each chosen `arr[i]` (as `c`):
    *   Initialize two pointers: `p1` at the beginning of the array (index 0) and `p2` at `i-1`.
    *   The goal is to find pairs `(arr[p1], arr[p2])` such that `arr[p1] + arr[p2] > arr[i]`.
    *   **Loop `while (p1 < p2)`:**
        *   If `arr[p1] + arr[p2] > arr[i]`:
            *   This means `arr[p1]` and `arr[p2]` can form a triangle with `arr[i]`. Moreover, since the array is sorted, any element between `p1` and `p2-1` (i.e., `arr[p1+1]`, `arr[p1+2]`, ..., `arr[p2-1]`) when paired with `arr[p2]` will also satisfy the condition `arr[val] + arr[p2] > arr[i]`. So, there are `(p2 - p1)` such pairs. Add this count to the total `ans`.
            *   Decrement `p2` (move left) to try to find smaller sums, as we've accounted for all valid pairs with current `arr[p2]` and elements from `p1` to `p2-1`.
        *   Else (`arr[p1] + arr[p2] <= arr[i]`):
            *   The sum is too small. Increment `p1` (move right) to try to find a larger sum.

**`findNumberOfTriangles(int arr[], int n)` function:**

*   **Parameters:**
    *   `arr[]`: The input array.
    *   `n`: The size of the array.
*   **Logic:**
    1.  Sort the array `arr`.
    2.  Initialize `ans = 0`.
    3.  Iterate `i` from `n-1` down to `2` (the largest element is `arr[i]`, and we need at least two other elements, so `i` must be at least 2 for a triplet).
    4.  For each `arr[i]`, use the two-pointer approach within the range `arr[0...i-1]` to find pairs `(arr[p1], arr[p2])` satisfying `arr[p1] + arr[p2] > arr[i]`.
    5.  The `count` function (which is essentially the two-pointer logic) performs this for a fixed largest side `x` (which is `arr[i]`) and a subarray `arr[0...n-1]`.
    6.  Accumulate results in `ans`.
*   Return `ans`.

```cpp
#include <iostream>  // For std::cin, std::cout, std::endl
#include <vector>    // Not explicitly used, but generally useful
#include <algorithm> // Required for std::sort

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

class Solution
{
public:
    // Helper function using two-pointers to count pairs (arr[p1], arr[p2])
    // such that arr[p1] + arr[p2] > x, where elements are from arr[0...n-1].
    // This is called for a fixed largest side x (which is arr[i] from main loop).
    int count(int *arr, int n_limit, int x)
    {
        int pair_count = 0;
        int p1 = 0;          // Left pointer
        int p2 = n_limit - 1; // Right pointer (upper limit for current fixed x)

        while(p1 < p2)
        {
            if((arr[p1] + arr[p2]) > x) // If the sum is greater than x
            {
                // All elements from arr[p1] to arr[p2-1] when paired with arr[p2]
                // will also form a valid triangle with x. So, (p2 - p1) pairs are valid.
                pair_count += (p2 - p1); 
                p2--; // Decrement p2 to try smaller sums with larger x values
            }
            else // If the sum is less than or equal to x
            {
                p1++; // Increment p1 to try larger sums
            }
        }
        
        return pair_count;
    }

    // Function to count the number of possible triangles in an array.
    int findNumberOfTriangles(int arr[], int n)
    {
        // Step 1: Sort the array. This is crucial for the two-pointer approach.
        std::sort(arr, arr + n);
        int total_triplets = 0;

        // Step 2: Iterate from the rightmost element, fixing it as the largest side 'c'.
        // We need at least 3 elements to form a triangle, so i goes from n-1 down to 2.
        for(int i = n - 1; i >= 2; i--)
        {
            // The current element arr[i] is fixed as the largest side.
            // We need to find pairs (arr[p1], arr[p2]) from arr[0...i-1]
            // such that arr[p1] + arr[p2] > arr[i].
            // The 'count' function does exactly this.
            total_triplets += count(arr, i, arr[i]);
        }
        return total_triplets;
    }
};

// Driver Code (provided by the problem platform)
int main()
{
    // Fast I/O setup
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int T;
    std::cin >> T; // Number of test cases
    while(T--)
    {
        int n;
        std::cin >> n;
        int arr[n]; // C-style array (VLA), consider std::vector in modern C++
        for(int i=0; i<n; i++)
            std::cin >> arr[i];
        Solution ob;
        std::cout << ob.findNumberOfTriangles(arr, n) << std::endl;
    }
    return 0;
}
```