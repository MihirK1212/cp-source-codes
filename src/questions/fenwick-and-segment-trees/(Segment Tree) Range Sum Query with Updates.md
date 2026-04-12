# Segment Tree: Range Sum Query with Updates

## Problem Description

This problem involves implementing a data structure that supports two operations on an array:
1.  **`update(index, val)`:** Updates the element at a specific `index` to `val`.
2.  **`sumRange(left, right)`:** Returns the sum of elements within the range `[left, right]` (inclusive).

The solution should efficiently handle both point updates and range sum queries. A Segment Tree is an ideal data structure for this, providing logarithmic time complexity for both operations.

## C++ Solution

The `NumArray` class uses a Segment Tree to efficiently manage the array and perform operations.

**Members:**

*   `tree`: A `std::vector<int>` representing the segment tree. It stores the sum of ranges. The size is typically `4*n` for an array of size `n`.
*   `n`: The size of the original array.
*   `a`: The original input array. This array is kept updated to reflect the latest values.

**Methods:**

*   **`NumArray(vector<int>& nums)` constructor:**
    *   Initializes `a` with `nums` and `n` with `nums.size()`.
    *   Resizes `tree` to `4*n` and calls `constructST` to build the segment tree.
*   **`constructST(vector<int>&tree, int node, vector<int>&a, int l, int r)`:**
    *   Recursively builds the segment tree.
    *   **Base Case:** If `l == r` (leaf node), `tree[node] = a[l]`.
    *   **Recursive Step:** Divides the range `[l, r]` into two halves `[l, mid]` and `[mid+1, r]`. Recursively calls `constructST` for children and sets `tree[node]` to the sum of its children's values.
*   **`updateST(vector<int>&tree, int node, vector<int>&a, int l, int r, int ind, int val)`:**
    *   Performs a point update on the segment tree.
    *   The current implementation updates the `tree[node]` by subtracting the *old value of `a[ind]`* (which is passed implicitly through the `a` vector) and adding the new `val`. This effectively propagates the *change* (`val - a[ind]`) up the tree. The actual `a[ind]` in the original array is updated after this recursive call returns.
    *   **Base Case:** If `l == r` (leaf node, which is the target index `ind`), the update to `tree[node]` is complete.
    *   **Recursive Step:** If `ind` is within `[l, r]`, it continues to update relevant children.
*   **`queryST(vector<int>&tree, int node, vector<int>&a, int l, int r, int ql, int qr)`:**
    *   Performs a range sum query on the segment tree.
    *   **Base Case 1 (No Overlap):** If the current segment `[l, r]` does not overlap with `[ql, qr]`, return 0.
    *   **Base Case 2 (Full Overlap):** If the current segment `[l, r]` is fully contained within the query range `[ql, qr]`, return `tree[node]`.
    *   **Recursive Step:** Otherwise, recursively query children and return the sum of their results.
*   **`update(int index, int val)`:**
    *   Calls `updateST` to update the segment tree with the new value at `index`.
    *   Updates the original array `a[index] = val`.
*   **`sumRange(int ql, int qr)`:**
    *   Calls `queryST` to get the sum of elements in the range `[ql, qr]`.

```cpp
#include <vector>
#include <algorithm> // Not explicitly used but generally useful

class NumArray {
public:
    std::vector<int> tree; // Segment tree array to store sums of ranges
    int n;                 // Size of the original array
    std::vector<int> a;    // Original input array (kept updated to reflect latest values)
    
    // Constructor: Initializes the NumArray object and builds the segment tree.
    NumArray(std::vector<int>& nums) 
    {
        a = nums; // Copy initial array values
        n = a.size();
        tree = std::vector<int>(4*n, 0); // Allocate space for the segment tree (typically 4*n)
        
        // Build the segment tree from the initial array
        constructST(tree, 0, a, 0, n-1);
    }
    
    // Recursive function to build the segment tree.
    // 'node' is the current node in the tree, 'l' and 'r' define its range.
    int constructST(std::vector<int>&tree, int node, std::vector<int>&a, int l, int r)
    {
        if(l == r) // Base case: If it's a leaf node, store the array element directly
        {
            tree[node] = a[l];
            return tree[node];
        }
        
        int mid = l + (r-l)/2; // Calculate the mid-point to divide the range
        
        // Internal node: sum of its children's values
        tree[node] = constructST(tree, 2*node+1, a, l, mid) + constructST(tree, 2*node+2, a, mid+1, r);
        return tree[node];
    }
    
    // Recursive function to update a value at a given index 'ind' to 'val' in the segment tree.
    // This implementation propagates the *difference* in value up the tree.
    void updateST(std::vector<int>&tree, int node, std::vector<int>&a, int l, int r, int ind, int val)
    {
        // If the update index 'ind' is outside the current segment range [l, r], do nothing.
        if(ind < l || ind > r){return;}
        
        // Update the current node's sum by subtracting the old value (from 'a[ind]') and adding the new 'val'.
        // Note: 'a[ind]' here represents the value *before* the overall update call to NumArray::update.
        tree[node] = tree[node] - a[ind] + val;
        
        // If it's a leaf node, the update for this path is complete.
        if(l == r){return;}
        
        int mid = l + (r-l)/2;
        
        // Recursively update the children nodes. The actual update to a[ind] happens later.
        updateST(tree, 2*node+1, a, l, mid, ind, val);
        updateST(tree, 2*node+2, a, mid+1, r, ind, val);
    }
    
    // Recursive function to query the sum of elements in a given range [ql, qr].
    int queryST(std::vector<int>&tree, int node, std::vector<int>&a, int l, int r, int ql, int qr)
    {
        // Case 1: No overlap. The query range is completely outside the current node's range.
        if(qr < l || ql > r){return 0;}
        
        // Case 2: Full overlap. The current node's range is fully contained within the query range.
        if(ql <= l && qr >= r){return tree[node];}
        
        int mid = l + (r-l)/2;
        
        // Case 3: Partial overlap. Recurse on children and sum their results.
        return queryST(tree, 2*node+1, a, l, mid, ql, qr) + queryST(tree, 2*node+2, a, mid+1, r, ql, qr);
    }
    
    // Public method to update an array element and reflect it in the segment tree.
    void update(int index, int val) 
    {
        // Call the recursive update function to modify the segment tree.
        updateST(tree, 0, a, 0, n-1, index, val); 
        // Update the original array 'a' with the new value.
        a[index] = val; 
    }
    
    // Public method to get the sum of elements within a specified range.
    int sumRange(int ql, int qr)
    {
        return queryST(tree, 0, a, 0, n-1, ql, qr); 
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
```