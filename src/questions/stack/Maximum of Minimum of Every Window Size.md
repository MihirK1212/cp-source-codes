# Maximum of Minimums for Every Window Size

## Problem Description

Given an integer array `arr[]`, find the maximum of minimums for every window size from 1 to `n`. For each window size `k`, consider all contiguous subarrays of length `k` and determine the minimum element in each subarray. Among these minimum values, take the maximum one.

**Example 1:**
```
Input: arr[] = [10, 20, 30]
Output: [30, 20, 10]
Explanation: The max of min for every possible window size.
Size 1: min of [10], [20], [30], max of min is 30.
Size 2: min of [10, 20],[20,30] max of min is 20.
Size 3: min of [10,20,30], max of min is 10.
```

**Example 2:**
```
Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
Output: [70, 30, 20, 10, 10, 10, 10]
Explanation:
Size 1: min are [10, 20, 30, 50, 10, 70, 30], max of min is 70.
Size 2: min are [10, 20, 30, 10, 10, 30], max of min is 30.
Size 3: min are [10, 20, 10, 10, 10], max of min is 20.
Size 4–7: min are [10, 10, 10, 10], max of min is 10.
```

## Expected Approach: Using Stack - O(n) Time and O(n) Space

This approach leverages a monotonic stack to efficiently find the previous smaller and next smaller elements for each element in the array. These boundaries help determine the largest window in which a particular element `arr[i]` is the minimum. The steps are as follows:

1.  For each element, find the [previous smaller](https://www.geeksforgeeks.org/dsa/find-the-nearest-smaller-numbers-on-left-side-in-an-array/) and [next smaller](https://www.geeksforgeeks.org/dsa/next-smaller-element/) using a stack.
2.  These boundaries give the largest window size where the current element is the minimum.
3.  Initialize an array `len` (or `windowMax`) where `len[k]` will store the maximum of minimums for windows of size `k`. When an element `arr[top]` is the minimum in a window of size `windowSize`, update `len[windowSize] = max(len[windowSize], arr[top])`.
4.  After processing all elements, `len[k]` will contain the maximum minimum for exactly size `k` windows. However, a maximum minimum for a larger window size `k'` might also be valid for a smaller window size `k`. To account for this, propagate results backward: for `i` from `n-2` down to `0`, `res[i] = max(res[i], res[i+1])`.

## C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm> // Required for std::max

std::vector<int> maxOfMin(std::vector<int>& arr) {
    int n = arr.size();
    std::vector<int> res(n); // Stores the final result for each window size
    std::vector<int> windowMax(n + 1, 0); // windowMax[k] stores max of mins for window size k
    std::stack<int> st; // Monotonic stack to find previous/next smaller elements

    // Phase 1: Find previous and next smaller elements for each element
    // This determines the range [left + 1, right - 1] where arr[top] is the minimum
    for (int i = 0; i < n; i++) {
        // While stack is not empty and current element is smaller than or equal to stack top element
        while (!st.empty() && arr[st.top()] >= arr[i]) {
            int top_idx = st.top();
            st.pop();
            
            // 'left' is the index of the previous smaller element, or -1 if no such element
            int left_bound = st.empty() ? -1 : st.top();
            // 'right' is the index of the next smaller element (current i)
            int right_bound = i;
            
            // Calculate the window size where arr[top_idx] is the minimum
            int windowSize = right_bound - left_bound - 1;
            // Update windowMax for this windowSize with arr[top_idx]
            windowMax[windowSize] = std::max(windowMax[windowSize], arr[top_idx]);
        }
        st.push(i);
    }

    // Phase 2: Process remaining elements in the stack
    // These elements have no next smaller element (they are increasing towards the end)
    while (!st.empty()) {
        int top_idx = st.top();
        st.pop();
        
        int left_bound = st.empty() ? -1 : st.top();
        int right_bound = n; // No next smaller element, so right bound is end of array
        
        int windowSize = right_bound - left_bound - 1;
        windowMax[windowSize] = std::max(windowMax[windowSize], arr[top_idx]);
    }

    // Phase 3: Fill the result array (res)
    // windowMax[k] contains the maximum minimum for a window of *exactly* size k.
    // However, a valid result for window size `k` might also be valid for `k-1`.
    // So, we propagate results backwards: res[i] = max(res[i], res[i+1])
    for (int i = 0; i < n; i++) {
        res[i] = windowMax[i + 1]; // Shift by 1 as windowMax is 1-indexed for sizes
    }

    // Ensure that for any window size k, the maximum of minimums is at least
    // the maximum of minimums for a window size k+1.
    for (int i = n - 2; i >= 0; i--) {
        res[i] = std::max(res[i], res[i + 1]);
    }

    return res;
}

int main() {
    std::vector<int> arr = {10, 20, 30, 50, 10, 70, 30};
    std::vector<int> result = maxOfMin(arr);
    for (int val : result) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}
```