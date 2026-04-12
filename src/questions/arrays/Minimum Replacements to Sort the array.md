# Minimum Replacements to Sort the Array (Greedy)

## Problem Description

This problem is from LeetCode: [Minimum Replacements to Sort the Array](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/).

You are given a 0-indexed integer array `nums`. In one operation, you can replace any element `nums[i]` with two or more elements that sum to `nums[i]`. For example, if `nums[i] = 7`, you can replace it with `[2, 2, 3]` or `[3, 4]`. The objective is to find the minimum number of operations to make `nums` sorted in non-decreasing order.

## C++ Solution (Greedy Approach)

This problem can be solved using a greedy approach by iterating the array from right to left. The key idea is to maintain a `currMax` variable, which represents the maximum allowed value for the element at the current position to maintain a non-decreasing order with the elements to its right.

When processing `nums[i]`:

*   If `nums[i] <= currMax`: The element is already in place (or smaller than `currMax`), so we simply update `currMax = nums[i]` and move left.
*   If `nums[i] > currMax`: This element needs to be broken down. We want to break it into as few parts as possible to minimize operations, but also ensure that the largest part is less than or equal to `currMax`. To do this, we calculate `num_parts = ceil((double)nums[i] / currMax)`. The number of operations for this step will be `num_parts - 1`. The new `currMax` for the next iteration (element `nums[i-1]`) will be `nums[i] / num_parts` (integer division, which gives the smallest possible value for the largest part after division to fit the `currMax` constraint from right).

```cpp
#include <vector>
#include <algorithm> // Required for std::max, std::min
#include <cmath>     // Required for ceil (if using double for calculation)

class Solution {
public:
    long long minimumReplacement(std::vector<int>& nums) 
    {
        long long ans = 0; // Stores the total minimum replacements
        int n = nums.size();
        
        // Start from the rightmost element. This is our initial upper bound for elements to its left.
        int currMax = nums[n-1]; 
        
        // Iterate from the second last element to the beginning
        for (int i = n - 2; i >= 0; i--) {
            // If the current element is already smaller than or equal to currMax,
            // it's in place, so update currMax and move on.
            if (nums[i] <= currMax) {
                currMax = nums[i];
            }
            else {
                // If nums[i] is greater than currMax, it needs to be broken down.
                // Calculate how many parts nums[i] needs to be broken into.
                // This is ceil(nums[i] / currMax).
                long long num_parts = (nums[i] + currMax - 1) / currMax; // Equivalent to ceil division
                
                // Each split creates one more element, so num_parts - 1 operations are needed.
                ans += (num_parts - 1);

                // After splitting nums[i] into num_parts, the largest possible value of a part
                // (to minimize the number of parts) would be nums[i] / num_parts.
                // This new largest part becomes the new currMax for the elements to its left.
                currMax = nums[i] / num_parts; 
            }
        }
        
        return ans;
    }
};
```