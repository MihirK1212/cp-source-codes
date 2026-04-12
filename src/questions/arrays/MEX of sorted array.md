# MEX of Sorted Array (Smallest Missing Non-Negative Integer)

## Problem Description

This problem focuses on finding the **Minimum Excluded (MEX)** element in a sorted array of non-negative integers. The MEX of a set of non-negative integers is the smallest non-negative integer that is not present in the set. For a sorted array `nums` starting potentially from 0, this translates to finding the first index `i` where `nums[i] != i`.

This is a classic problem often solved using binary search due to the sorted nature of the array.

## Reference

This solution is adapted from: [Find smallest missing element in a sorted array](https://www.techiedelight.com/find-smallest-missing-element-sorted-array/)

## C++ Solution (Recursive Binary Search)

The solution employs a recursive binary search function `findSmallestMissing` to efficiently locate the MEX.

**`findSmallestMissing(int nums[], int low, int high)` function:**

*   **Parameters:**
    *   `nums[]`: The input sorted array of non-negative integers.
    *   `low`: The lower bound of the current search range.
    *   `high`: The upper bound of the current search range.

*   **Base Case:**
    *   If `low > high`, it means that all elements from the implicit start (0) up to `high` are present and match their indices. Therefore, `low` (which is `high + 1`) is the smallest missing non-negative integer.

*   **Recursive Step:**
    1.  Calculate `mid = low + (high - low) / 2`.
    2.  **Condition 1: `nums[mid] == mid`**
        *   This implies that all integers from `0` up to `mid` are present in their correct positions. Thus, the smallest missing element must be in the right half of the array (i.e., greater than `mid`).
        *   Recursively call `findSmallestMissing(nums, mid + 1, high)`.
    3.  **Condition 2: `nums[mid] != mid`**
        *   This implies that either `mid` itself is missing, or an integer smaller than `mid` is missing. The mismatch occurs at or before `mid`.
        *   Recursively call `findSmallestMissing(nums, low, mid - 1)`.

```cpp
#include <vector> // Not explicitly used but good for general C++ practices
#include <cstdio>   // For printf

// Function to find the smallest missing non-negative element in a sorted array
// using a recursive binary search approach.
int findSmallestMissing(int nums[], int low, int high)
{
    // Base case: If the lower bound exceeds the upper bound,
    // it means all elements up to 'high' are present and match their indices.
    // So, 'low' is the first missing positive integer.
    if (low > high) {
        return low;
    }
 
    int mid = low + (high - low) / 2;
 
    // If the element at 'mid' index matches its value (nums[mid] == mid),
    // it implies all elements from 'low' to 'mid' are present.
    // The smallest missing element must therefore be in the right half.
    if (nums[mid] == mid) {
        return findSmallestMissing(nums, mid + 1, high);
    }
    else {
        // If nums[mid] != mid, it means either 'mid' itself is missing
        // or an element smaller than 'mid' is missing. So, the smallest
        // missing element is in the left half (or is 'mid' itself).
        return findSmallestMissing(nums, low, mid - 1);
    }
}

// Main function (driver code) for testing the findSmallestMissing function
int main(void)
{
    // Example sorted array of non-negative integers
    int nums[] = { 0, 1, 2, 3, 4, 5, 6 };
    int n = sizeof(nums) / sizeof(nums[0]);
 
    int low = 0, high = n - 1;
 
    // Call the function and print the result
    printf("The smallest missing element is %d\n", findSmallestMissing(nums, low, high));
 
    // Another example: {0, 1, 3, 4, 5}
    int nums2[] = {0, 1, 3, 4, 5};
    int n2 = sizeof(nums2) / sizeof(nums2[0]);
    printf("The smallest missing element in {0,1,3,4,5} is %d\n", findSmallestMissing(nums2, 0, n2-1));

    // Example: {1, 2, 3} (MEX is 0)
    int nums3[] = {1, 2, 3};
    int n3 = sizeof(nums3) / sizeof(nums3[0]);
    printf("The smallest missing element in {1,2,3} is %d\n", findSmallestMissing(nums3, 0, n3-1));

    // Example: {} (empty array, MEX is 0)
    int nums4[] = {};
    int n4 = sizeof(nums4) / sizeof(nums4[0]);
    if (n4 == 0) {
        printf("The smallest missing element in {} is %d\n", 0);
    } else {
        printf("The smallest missing element in {} is %d\n", findSmallestMissing(nums4, 0, n4-1));
    }

    return 0;
}
```