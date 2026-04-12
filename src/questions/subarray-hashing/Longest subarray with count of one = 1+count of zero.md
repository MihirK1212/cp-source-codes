# Longest Subarray with Count of Ones = 1 + Count of Zeros

## Problem Description

Given a binary array `A` (containing only 0s and 1s), find the length of the longest subarray where the count of ones is exactly one more than the count of zeros.

## C++ Solution

This problem can be solved efficiently using a hash map (or `std::map` in C++) to store the first occurrence of each `(count_zeros - count_ones)` difference encountered. We iterate through the array, maintaining `oneCount` and `zeroCount`. The target condition is `oneCount - zeroCount = 1`, which is equivalent to `oneCount - zeroCount - 1 = 0` or `(count_zeros - count_ones) = -1`.

We track the `diff = zeroCount - oneCount`. If `diff` becomes `-1` at any point, it means a subarray ending at the current index satisfies the condition, and its length is `i+1`. We also use a map `diffMinPos` to store the minimum `(i+1)` for each `diff` value. This helps in finding the longest such subarray. If we encounter a `diff` value such that `diff - 1` (i.e., `zeroCount - oneCount - 1`) has been seen before, it implies a subarray between the current index and the previously seen index satisfies the condition.

```cpp
#include <vector>
#include <map>
#include <algorithm> // For std::max

class Solution {
public:
    int solve(std::vector<int> &A) 
    {
        int ans = 0; // Stores the maximum length found
        int oneCount = 0; 
        int zeroCount = 0;

        // Map to store the first (minimum) index + 1 for each (zeroCount - oneCount) difference
        std::map<int, int> diffMinPos;

        // Initialize diffMinPos for a difference of 0 (empty prefix before index 0)
        // If diffMinPos[0] is set to 0, it means an empty prefix has difference 0. 
        // However, a difference of 0 initially represents `oneCount == zeroCount` from the start.
        // We are interested in `oneCount - zeroCount == 1`.
        // If the problem needs to consider empty prefix, map[0] = 0 is common, but here we track diff (zeroCount - oneCount).
        // So, if (zeroCount - oneCount) is X at index i, and we want (zeroCount - oneCount) = X - 1,
        // we look for X - 1 in the map. 

        // Consider an imaginary prefix before index 0 with zeroCount = 0 and oneCount = 0.
        // Thus, zeroCount - oneCount = 0. Its position is -1 (or 0 if using 1-based indexing for length). 
        // If diffMinPos maps (zeroCount - oneCount) to (index + 1),
        // then diffMinPos[0] = 0 means at index -1, the difference was 0.
        diffMinPos[0] = 0; // Initialize for an empty prefix having difference 0 at virtual index -1 (length 0)

        for(int i = 0; i < A.size(); i++)
        {
            oneCount += (A[i] == 1); 
            zeroCount += (A[i] == 0);

            int current_diff = zeroCount - oneCount; // Current difference

            // We are looking for a subarray where (oneCount - zeroCount) = 1
            // This means (zeroCount - oneCount) = -1

            // Check if (current_diff + 1) exists in the map.
            // If we have current_diff at index i, and we previously saw (current_diff + 1) at index j,
            // then from index j to i, the difference changed by -1.
            // This implies (zeroCount_i - oneCount_i) - (zeroCount_j - oneCount_j) = -1
            // which means (oneCount_j - zeroCount_j) - (oneCount_i - zeroCount_i) = -1
            // which is equivalent to (oneCount_i - zeroCount_i) = (oneCount_j - zeroCount_j) + 1
            // This isn't exactly what we want. We need (oneCount - zeroCount) = 1 for the subarray.

            // Let prefix_diff[k] = oneCount_k - zeroCount_k
            // We want prefix_diff[i] - prefix_diff[j] = 1
            // So, prefix_diff[j] = prefix_diff[i] - 1

            int prefix_diff = oneCount - zeroCount; // Let's work with this difference
            
            // If prefix_diff is 1, it means the subarray from start (or after a 0-diff prefix) to current index satisfies
            if (prefix_diff == 1) {
                ans = std::max(ans, i + 1); // Length is i+1 (0-indexed)
            }

            // If (prefix_diff - 1) has been seen before
            // i.e., at some earlier index j, we had (oneCount_j - zeroCount_j) = prefix_diff - 1
            // Then the subarray from j+1 to i has (oneCount - zeroCount) = 1
            if (diffMinPos.count(prefix_diff - 1))
            {
                int prev_pos = diffMinPos[prefix_diff - 1];
                ans = std::max(ans, i + 1 - prev_pos); // Update answer with current subarray length
            }
            
            // Store the first occurrence of the current prefix_diff (if not already present)
            if (diffMinPos.find(prefix_diff) == diffMinPos.end()) {
                diffMinPos[prefix_diff] = i + 1;
            }
        }

        return ans;
    }
};
```
