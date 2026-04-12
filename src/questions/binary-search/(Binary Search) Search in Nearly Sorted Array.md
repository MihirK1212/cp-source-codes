# Binary Search: Search in Nearly Sorted Array

## Problem Description

Given a sorted array in which an element at index `i` in the original sorted array can be present at index `i-1`, `i`, or `i+1` in the given array. This type of array is often referred to as a "nearly sorted" or "k-sorted" array where `k=1`. The task is to find the index of a given `search_num` in this array. If the element is not found, return -1.

## C++ Solution

This C++ solution implements a modified binary search algorithm to find an element in a nearly sorted array.

**Algorithm:**

1.  **Standard Binary Search Setup:** Initialize `lb = 0` (lower bound), `ub = n-1` (upper bound), and `ind = -1` (to store the result index).
2.  **Modified Search Loop:** While `lb <= ub`:
    *   Calculate `mid = lb + (ub - lb) / 2`.
    *   **Check `mid` and its neighbors:** Due to the "nearly sorted" property, the `search_num` could be at `mid`, `mid-1`, or `mid+1`.
        *   First, check `arr[mid] == search_num`. If found, set `ind = mid` and `break`.
        *   Next, check `arr[max(0, mid-1)] == search_num`. If found, set `ind = max(0, mid-1)` and `break`. The `max(0, mid-1)` handles array boundary conditions.
        *   Next, check `arr[min(n-1, mid+1)] == search_num`. If found, set `ind = min(n-1, mid+1)` and `break`. The `min(n-1, mid+1)` handles array boundary conditions.
    *   **Adjust Search Range:**
        *   If `search_num < arr[mid]`: The target is smaller than the element at `mid`. Since `arr[mid]` could have shifted from `mid-1` or `mid`, and we have already checked `mid-1`, the search space can be reduced by moving the `ub` to `mid-2`.
        *   If `search_num > arr[mid]`: The target is larger than the element at `mid`. Since `arr[mid]` could have shifted from `mid+1` or `mid`, and we have already checked `mid+1`, the search space can be reduced by moving the `lb` to `mid+2`.
3.  **Output Result:** Print `ind`.

```cpp
#include <iostream>  // Required for std::cin, std::cout
#include <vector>    // Required for std::vector
#include <algorithm> // Required for std::max, std::min

// Using namespace std; // Commonly used in competitive programming, but explicit std:: is more robust

int main()
{
    // Fast I/O setup (common in competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int n, search_num, i;
    std::cin >> n; // Read array size
    
    std::vector<int> arr(n); // Declare a vector for the array
    
    // Read array elements
    for(i = 0; i < n; i++)
    {
        std::cin >> arr[i];
    }
    
    std::cin >> search_num; // Read the number to search for
    
    int lb = 0;   // Lower bound of search space
    int ub = n - 1; // Upper bound of search space
    int mid;      // Middle index
    int ind = -1; // Stores the index of search_num, -1 if not found

    while(lb <= ub)
    {
        mid = lb + (ub - lb) / 2; // Calculate mid to prevent overflow
        
        // Check current mid index
        if(arr[mid] == search_num)
        {
            ind = mid;
            break; // Found the element
        }
        
        // Check element to the left of mid (if valid index)
        if((mid - 1) >= lb && arr[mid - 1] == search_num) // Ensure mid-1 is within current search bounds
        {
            ind = mid - 1;
            break; // Found the element
        }
        
        // Check element to the right of mid (if valid index)
        if((mid + 1) <= ub && arr[mid + 1] == search_num) // Ensure mid+1 is within current search bounds
        {
            ind = mid + 1;
            break; // Found the element
        }
        
        // Adjust search range based on comparison with arr[mid]
        if(search_num < arr[mid])
        {
            ub = mid - 2; // Move upper bound two steps left (since mid and mid-1 are checked or too large)
        }
        else // search_num > arr[mid]
        {
            lb = mid + 2; // Move lower bound two steps right (since mid and mid+1 are checked or too small)
        }
    }
    
    std::cout << ind << "\n"; // Output the result index

    return 0;
}
```