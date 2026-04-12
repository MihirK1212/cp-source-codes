# Find First Missing Positive Integer

## Problem Description

Given an unsorted integer array, find the smallest positive integer (greater than 0) that does not exist in the array. Your algorithm should run in O(n) time and use constant extra space.

## C++ Solution

This C++ solution finds the first missing positive integer in an unsorted array using an in-place modification approach, achieving O(n) time complexity and O(1) extra space.

**Algorithm:**

1.  **Segregate Non-Positive Numbers (`segregate` function):**
    *   Move all non-positive numbers (zero or negative) to the beginning of the array.
    *   The function returns the index `j`, which is the starting index of the sub-array containing only positive numbers. This effectively partitions the array into `[non-positive numbers, positive numbers]` where we only care about the positive numbers for the subsequent steps.

2.  **Mark Visited Positives (`findMissing` function):**
    *   This function operates on the sub-array of positive numbers obtained from `segregate`.
    *   For each element `a[i]` in this positive sub-array:
        *   Consider `abs(a[i])`. If `abs(a[i]) - 1` is a valid index within the positive sub-array (i.e., `0 <= abs(a[i]) - 1 < n`, where `n` is the size of the positive sub-array).
        *   And if the element at that index `a[abs(a[i])-1]` is positive, change its sign to negative. This marking indicates that the number `abs(a[i])` is present in the array.
        *   We use absolute values `abs(a[i])` because numbers might have already been marked negative by a previous iteration.

3.  **Find First Missing (`findMissing` function continued):**
    *   After marking, iterate through the positive sub-array again.
    *   The first index `i` for which `a[i]` is still positive (or zero, if 0 was originally present in the positive segment) indicates that the number `i+1` was never encountered in the original positive numbers.
    *   Return `i+1`.

4.  **Handle All Positives Present:**
    *   If all numbers from `1` to `n` (where `n` is the count of positive numbers) are present, then the loop in step 3 will complete without finding a positive element. In this case, the first missing positive is `n+1`.

**`missingNumber(int a[], int n)` function:**

*   This is the main driver function that orchestrates the segregation and finding of the missing number.
*   It calls `segregate` to partition the array.
*   Then it calls `findMissing` on the sub-array of positive numbers.

```cpp
#include <vector> // Not explicitly used but good for standard practices
#include <algorithm> // Required for std::swap, std::abs

class Solution
{
public:
    // Function to segregate non-positive numbers to the left.
    // Returns the index of the first positive number.
    int segregate(int *a, int n)
    {
        int j = 0; // Pointer for the position to swap non-positive numbers to
        for(int i = 0; i < n; i++)
        {
            if(a[i] <= 0)
            {
                std::swap(a[i], a[j]); // Move non-positive to the left
                j++; // Increment the pointer for the next non-positive number
            }
        }
        return j; // Return the count of non-positive numbers, which is the start of positives
    }

    // Function to find the smallest missing positive number in a sub-array
    // which is assumed to contain only positive numbers.
    int findMissing(int *a, int n)
    {
        // Mark elements present by changing the sign of the element at the corresponding index.
        // If we see number X, we mark a[X-1] negative.
        for(int i = 0; i < n; i++)
        {
            // Get the absolute value of the current element.
            // We use abs() because elements might have already been marked negative.
            int val = std::abs(a[i]);
            
            // If 'val' is a valid index (1-based) within the current sub-array of positives
            // and the element at that index is still positive (not yet marked)
            if((val - 1) < n && (val - 1) >= 0 && a[val - 1] > 0)
            {
                // Mark the element at (val-1) index as negative to indicate 'val' is present.
                a[val - 1] = -a[val - 1];
            }
        }
        
        // Iterate through the array to find the first positive element.
        // The index of this element (i + 1) is the first missing positive number.
        for(int i = 0; i < n; i++)
        {
            if(a[i] > 0) { // If a[i] is positive, it means (i+1) was not found in the input
                return (i + 1);
            }
        }
        
        // If all numbers from 1 to n are present (all elements are negative),
        // then the first missing positive is n+1.
        return n + 1;
    }

    // Main function to find the smallest missing positive number.
    int missingNumber(int arr[], int n) 
    { 
        // First, segregate non-positive numbers from positive numbers.
        // 'firstInd' will be the starting index of the positive numbers sub-array.
        int firstInd = segregate(arr, n);
        
        // Call findMissing on the sub-array of positive numbers.
        // (arr + firstInd) points to the start of the positive numbers.
        // (n - firstInd) is the size of this positive numbers sub-array.
        return findMissing(arr + firstInd, n - firstInd);
    } 
};
```

## Driver Code (C++)

```cpp
#include <iostream>
#include <vector> // Implicitly used by Solution class (best to include explicitly)
#include <algorithm> // Implicitly used by Solution class (best to include explicitly)
#include <cmath> // Implicitly used by Solution class (for std::abs)

// Forward declaration of the Solution class (or include the header where it's defined)
// Assuming Solution class is defined in the same file or a preceding header.

int main() { 
    // taking testcases
    int t;
    std::cin >> t;
    while(t--){
        
        // input number n
        int n;
        std::cin >> n;
        int arr[n]; // C-style array (VLA), consider std::vector in modern C++
        
        // adding elements to the array
        for(int i=0; i<n; i++){
            std::cin >> arr[i];
        }
        
        Solution ob;
        // calling missingNumber()
        std::cout << ob.missingNumber(arr, n) << std::endl;
    }
    return 0; 
}
```