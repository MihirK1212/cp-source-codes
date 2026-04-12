# Binary Search: Find Ceil of a Number

## Problem Description

Given a sorted array `arr` and a `search_num`, find the smallest element in `arr` that is greater than or equal to `search_num`. This is also commonly known as finding the "ceil" of the number in the array. If no such element exists (i.e., all elements in the array are smaller than `search_num`), then a specific value (e.g., infinity or -1) should be returned.

## C++ Solution

This C++ solution uses a modified binary search algorithm to find the ceil of a number in a sorted array.

**Algorithm:**

1.  **Initialization:**
    *   Initialize `ceil_ans` to `inf` (a very large value, representing infinity, to store the smallest candidate for ceil found so far). `std::numeric_limits<int>::max()` is used for this.
    *   Initialize `lb = 0` (lower bound), `ub = n-1` (upper bound) for binary search.

2.  **Binary Search Loop:** While `lb <= ub`:
    *   Calculate `mid = lb + (ub - lb) / 2`.
    *   **Case 1: `arr[mid] >= search_num`**
        *   This `arr[mid]` is a potential ceil. Store it in `ceil_ans = arr[mid]`.
        *   Since we are looking for the *smallest* element greater than or equal to `search_num`, we try to find an even smaller element in the left half of the array. So, `ub = mid - 1`.
    *   **Case 2: `arr[mid] < search_num`**
        *   The current `arr[mid]` is too small. We need a larger element, so discard the left half.
        *   `lb = mid + 1`.

3.  **Result:**
    *   After the loop, `ceil_ans` will hold the smallest element in `arr` that is greater than or equal to `search_num`. If no such element was found, `ceil_ans` remains `inf`.
    *   Print `ceil_ans`.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::sort, std::min
#include <limits>    // Required for std::numeric_limits<int>::max

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

int inf = std::numeric_limits<int>::max(); // Define infinity for integer type

int main()
{
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int n, search_num, i;
    std::cin >> n >> search_num; // Read array size and search number
    
    std::vector<int> arr(n); // Declare a vector for the array
    
    // Read array elements
    for(i = 0; i < n; i++)
    {
        std::cin >> arr[i];
    }
    
    // The problem statement implies the array is sorted. If not, it should be sorted.
    // std::sort(arr.begin(), arr.end()); // Uncomment if input array is not guaranteed sorted
    
    int ceil_ans = inf; // Initialize ceil_ans to infinity
    int lb = 0, ub = n - 1, mid; // Binary search bounds and mid index
    
    while(lb <= ub)
    {
        mid = lb + (ub - lb) / 2; // Calculate mid to prevent overflow

        if(arr[mid] >= search_num) // Current element is a potential ceil
        {
            ceil_ans = arr[mid];  // Store this as a candidate
            ub = mid - 1;         // Try to find a smaller ceil in the left half
        }
        else // arr[mid] < search_num, current element is too small
        {
            lb = mid + 1;         // Search in the right half for a larger element
        }
    }
    
    // Output the result. If ceil_ans is still inf, it means no element >= search_num was found.
    std::cout << ceil_ans << "\n";
    
    return 0;
}
```