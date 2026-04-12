# Sliding Window Maximum (Efficient)

## Problem Description

Given an array `A` of integers and an integer `K`, find the maximum element in every contiguous subarray (window) of size `K`. The solution should be efficient, typically achieved using a sliding window approach with a deque (double-ended queue).

**Example:**

`A = [1, 3, -1, -3, 5, 3, 6, 7]`, `K = 3`

*   Window 1: `[1, 3, -1]`, Max: `3`
*   Window 2: `[3, -1, -3]`, Max: `3`
*   Window 3: `[-1, -3, 5]`, Max: `5`
*   Window 4: `[-3, 5, 3]`, Max: `5`
*   Window 5: `[5, 3, 6]`, Max: `6`
*   Window 6: `[3, 6, 7]`, Max: `7`

Result: `[3, 3, 5, 5, 6, 7]`

## C++ Solution

The solution uses a deque to maintain a window of useful elements (potential maximums) in decreasing order. The front of the deque will always store the maximum element of the current window.

**Algorithm (`slidingMaximum` function):**

1.  **Initialization:**
    *   `n`: Size of the input array `A`.
    *   `K`: Window size. Adjust `K = min(n, K)` to handle cases where `K` might be larger than `n`.
    *   `q`: A `std::deque<int>` to store elements. This deque will maintain elements in decreasing order, and only store elements that are potentially maximums in future windows.
    *   `ans`: A `std::vector<int>` to store the maximums for each window.

2.  **Process First Window (initial `K` elements):**
    *   Iterate from `i = 0` to `K-1`:
        *   **Remove Smaller Elements from Back:** While `q` is not empty and `A[i]` is greater than `q.back()`, pop elements from the back of `q`. This ensures `q` remains in decreasing order and removes elements that can no longer be maximums.
        *   **Add Current Element:** Push `A[i]` to the back of `q`.

3.  **Slide the Window (remaining elements):**
    *   Initialize `lb = 0` (left bound of window) and `ub = K-1` (right bound of window).
    *   While `lb <= ub` and `ub < n` (ensuring window is within bounds):
        *   **Store Current Window Maximum:** The maximum for the current window is `q.front()`. Add it to `ans`.
        *   **Remove `A[lb]` if it's the Maximum:** If `q.front()` is equal to `A[lb]` (the element leaving the window), pop it from the front of `q`. 
        *   **Advance Window:** Increment `lb` and `ub`.
        *   **Process New Element `A[ub]` (if `ub < n`):**
            *   If `ub` is a valid index for the next element:
                *   **Remove Smaller Elements from Back:** While `q` is not empty and `A[ub]` is greater than `q.back()`, pop elements from the back of `q`.
                *   **Add New Element:** Push `A[ub]` to the back of `q`.

4.  Return `ans`.

```cpp
#include <vector>  // For std::vector
#include <deque>   // For std::deque
#include <algorithm> // For std::min (used for K = min(n,K))

// Solution class (often used in competitive programming platforms)
class Solution {
public:
    // Function to find the maximum in every contiguous subarray of size K.
    // A: The input array.
    // K: The size of the sliding window.
    std::vector<int> slidingMaximum(const std::vector<int>& A, int K) 
    {
        int n = A.size();
        // Adjust K if it's larger than the array size.
        K = std::min(n, K);
        
        std::deque<int> q;       // Deque to store potential maximums
        std::vector<int> ans;   // Vector to store results (maximums of each window)
        
        // Process the first window (initial K elements).
        for(int i = 0; i < K; i++)
        {
            // Remove elements from the back of the deque that are smaller than the current element A[i].
            // This ensures the deque stores elements in decreasing order.
            while(!q.empty() && A[i] >= q.back()){ // Use >= to keep only the rightmost occurrence of a max
                q.pop_back();
            }
            q.push_back(A[i]); // Add the current element to the back of the deque.
        }
        
        // The deque now holds candidates for the maximum of the first window.
        // The front of the deque is the maximum of the first window.
        // The variables lb and ub represent the left and right bounds of the current window.
        int lb = 0; // Left boundary of the window
        int ub = K - 1; // Right boundary of the window
        
        // Slide the window across the rest of the array.
        // The loop continues as long as the window is valid and within array bounds.
        while(lb <= ub && ub < n)
        {
            // The maximum element of the current window is always at the front of the deque.
            ans.push_back(q.front());
            
            // If the element leaving the window (A[lb]) is the current maximum in the deque,
            // remove it from the front.
            if(q.front() == A[lb]){
                q.pop_front();
            }
            
            // Advance the window boundaries.
            lb++; 
            ub++;
            
            // If the new right boundary (ub) is within the array bounds,
            // process the new element entering the window (A[ub]).
            if(ub < n)
            {
                // Remove elements from the back of the deque that are smaller than the new element A[ub].
                while(!q.empty() && A[ub] >= q.back()){ // Use >= to keep only the rightmost occurrence of a max
                    q.pop_back();
                }
                q.push_back(A[ub]); // Add the new element to the back of the deque.
            }        
        }
        
        return ans;
    }
};
```