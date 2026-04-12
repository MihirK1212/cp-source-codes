# Median of Two Sorted Arrays (Binary Search)

## Problem Description

Given two sorted arrays `nums1` and `nums2` of sizes `n1` and `n2` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(n1 + n2)).

The median of a sorted array of length `L` is:
*   The middle element if `L` is odd.
*   The average of the two middle elements if `L` is even.

For two sorted arrays, the median would be the element that divides the combined sorted array into two equal halves (or nearly equal halves). This problem requires finding the correct partition point.

## C++ Solution

This solution uses a binary search approach on the smaller of the two arrays to find the optimal partition. The goal is to find a cut point `i1` in `nums1` and `i2` in `nums2` such that:

1.  `i1 + i2 = (n1 + n2 + 1) / 2` (This ensures the total number of elements in the left partitions is correct for the median).
2.  `max(left_partition_of_nums1, left_partition_of_nums2) <= min(right_partition_of_nums1, right_partition_of_nums2)`.

**Algorithm:**

*   Ensure `nums1` is the smaller array to optimize binary search range. If `n1 > n2`, swap arrays.
*   Initialize `low = 0` and `high = n1`. This search space is for the partition point `i1` in `nums1`.
*   In each iteration of the binary search:
    *   Calculate `i1 = low + (high - low) / 2`.
    *   Calculate `i2 = (n1 + n2 + 1) / 2 - i1`.
    *   Define `maxLeft1`, `minRight1`, `maxLeft2`, `minRight2` as the boundary elements of the partitions. Handle `INT_MIN` and `INT_MAX` for empty partitions.
    *   **If `max(maxLeft1, maxLeft2) <= min(minRight1, minRight2)`:** This is the correct partition.
        *   If `(n1 + n2)` is odd, the median is `max(maxLeft1, maxLeft2)`.
        *   If `(n1 + n2)` is even, the median is `(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0`.
    *   **Else if `maxLeft1 > minRight2`:** The `maxLeft1` is too large, meaning `i1` is too far to the right. Adjust `high = i1 - 1`.
    *   **Else (`maxLeft2 > minRight1`):** The `maxLeft2` is too large, meaning `i1` is too far to the left. Adjust `low = i1 + 1`.

```cpp
#include <vector>
#include <algorithm> // For std::max, std::min
#include <limits>    // For INT_MIN, INT_MAX

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        int n1 = nums1.size() , n2 = nums2.size();
        
        // Ensure nums1 is the smaller array for binary search optimization
        if(n1 > n2){
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int low = 0 , high = n1; // Binary search range for partition point i1 in nums1
        // The partition point i1 means i1 elements are in the left partition of nums1.
        // The actual index for nums1 (if 0-indexed) would be i1-1.

        while(low <= high) // Using low <= high to include all possibilities
        {
            int i1 = low + (high - low) / 2; // Partition point in nums1
            // i1 elements in left part of nums1, n1-i1 elements in right part of nums1

            // Calculate partition point in nums2
            // Total elements in left half of combined array should be (n1+n2+1)/2 for both odd/even total length
            int i2 = (n1 + n2 + 1) / 2 - i1;
            // i2 elements in left part of nums2, n2-i2 elements in right part of nums2
            
            // Define boundary elements for clarity
            int maxLeft1 = (i1 == 0) ? std::numeric_limits<int>::min() : nums1[i1-1];
            int minRight1 = (i1 == n1) ? std::numeric_limits<int>::max() : nums1[i1];
            
            int maxLeft2 = (i2 == 0) ? std::numeric_limits<int>::min() : nums2[i2-1];
            int minRight2 = (i2 == n2) ? std::numeric_limits<int>::max() : nums2[i2];
            
            // Check if the partition is correct
            if(maxLeft1 <= minRight2 && maxLeft2 <= minRight1)
            {
                // Correct partition found
                if((n1 + n2) % 2 == 1){ // Total elements are odd
                    return static_cast<double>(std::max(maxLeft1, maxLeft2));
                }
                else { // Total elements are even
                    // Median is average of the two middle elements
                    return static_cast<double>(std::max(maxLeft1, maxLeft2) + std::min(minRight1, minRight2)) / 2.0;
                }
            }
            else if(maxLeft1 > minRight2){ // maxLeft1 is too large, need to move i1 left
                high = i1 - 1;
            }
            else { // maxLeft2 > minRight1, maxLeft1 is too small, need to move i1 right
                low = i1 + 1;
            }
        }
        
        return 0.0; // Should not be reached in a valid sorted array problem, indicates an error
    }
};
```