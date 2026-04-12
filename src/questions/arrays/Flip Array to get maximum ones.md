# Flip Array to Get Maximum Ones (Kadane's Algorithm Variant)

## Problem Description

This problem is from InterviewBit: [Flip](https://www.interviewbit.com/problems/flip/).

You are given a binary string `A` (contains only '0's and '1's). You can choose at most one subsegment of the array and flip every character in that subsegment. Flipping a '0' changes it to a '1', and flipping a '1' changes it to a '0'. Your goal is to return the indices `[L, R]` (1-indexed) of the subsegment such that by flipping this subsegment, the resultant binary string has the maximum possible number of '1's.

If there are multiple solutions, return the one where `L` is minimal. If `L` is the same, return the one where `R` is minimal. If no flip improves the number of ones (i.e., the original array already has the maximum possible ones), return an empty array.

## Approach - Kadane's Algorithm

This problem can be elegantly solved by transforming it into a **Maximum Subarray Sum** problem, which is typically solved using Kadane's algorithm. The key is to rephrase the problem: we want to flip a subsegment such that the *increase* in the number of ones is maximized.

Consider a transformed array where:

*   Each `'0'` in the original string is treated as `+1` (because flipping a `0` adds one `1`).
*   Each `'1'` in the original string is treated as `-1` (because flipping a `1` removes one `1`).

By finding the subarray with the maximum sum in this transformed array, we are effectively finding the subsegment that, when flipped, yields the greatest net increase in the total number of ones. If this maximum sum is zero or negative, it implies that no flip operation would actually increase the total count of ones, in which case we should return an empty array as per the problem statement.

Kadane's algorithm is adapted to not only track the maximum sum but also the start and end indices of the subarray that produces this sum, respecting the tie-breaking rules (minimal `L`, then minimal `R`).

## C++ Solution

```cpp
#include <string>
#include <vector>
#include <algorithm> // Required for std::max
#include <limits>    // For std::numeric_limits<int>::min()

class Solution {
public:
    std::vector<int> flip(std::string A)
    {
        int n = A.length();

        int max_so_far = 0;      // Stores the maximum possible gain (sum) found globally
        int current_max_gain = 0;  // Stores the maximum gain ending at the current position
        
        int current_start_idx = 0; // Starting index of the current_max_gain subarray
        int best_start_idx = -1;   // Starting index of the max_so_far subarray (0-indexed)
        int best_end_idx = -1;     // Ending index of the max_so_far subarray (0-indexed)

        // Iterate through the binary string
        for (int i = 0; i < n; ++i)
        {
            // Convert '0' to +1 and '1' to -1
            int val = (A[i] == '0') ? 1 : -1;

            current_max_gain += val;

            // If current_max_gain becomes greater than max_so_far, update global max and indices.
            if (current_max_gain > max_so_far)
            {
                max_so_far = current_max_gain;
                best_start_idx = current_start_idx;
                best_end_idx = i; 
            }
            // If current_max_gain becomes negative, it means this subarray is no longer contributing 
            // to a positive gain. Reset current_max_gain and move the start_idx to the next element.
            if (current_max_gain < 0)
            {
                current_max_gain = 0;
                current_start_idx = i + 1;
            }
        }

        // If max_so_far is still 0 (meaning no positive gain was ever made),
        // or if no valid flip subsegment was found,
        // return an empty vector as per problem statement.
        if (best_start_idx == -1) {
             return {};
        }

        // Return 1-indexed results for the best subsegment
        return {best_start_idx + 1, best_end_idx + 1};
    }
};
```