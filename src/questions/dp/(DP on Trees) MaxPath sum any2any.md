# (DP on Trees) Maximum Path Sum (Any Node to Any Node)

## Problem Description

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. The path does not need to pass through the root.

Given the `root` of a binary tree, return the maximum path sum of any path. A path sum is the sum of the node values in a path.

## C++ Solution

This C++ solution uses a recursive Depth-First Search (DFS) approach with dynamic programming principles to find the maximum path sum in a binary tree. The key idea is to calculate two types of maximum sums at each node:

1.  The maximum path sum that `starts at the current node and goes downwards` (either to the left child, right child, or just ends at the current node).
2.  The maximum path sum that `passes through the current node` (connecting its left and right subtrees, or ending at the node).

The global maximum path sum (`ans`) is updated whenever a path passing through the current node is considered.

**Algorithm:**

1.  **Global Variable `ans`:** Initialize `int ans = -INT_MAX;` (or a very small number) to store the overall maximum path sum found across all nodes.

2.  **`solve(TreeNode* root)` function (Recursive Helper):**
    *   **Base Case:** If `root` is `NULL`, return `0` (an empty path contributes 0 to the sum).
    *   **Recursive Calls:**
        *   `l_sum = max(0, solve(root->left));` : Recursively find the maximum path sum that starts at the left child and goes downwards. We take `max(0, ...)` because if a path sum from a child is negative, we can choose to not include that path (effectively starting a new path from the current `root`).
        *   `r_sum = max(0, solve(root->right));` : Same for the right child.
    *   **Update Global `ans`:** `ans = max(ans, l_sum + r_sum + root->val);`.
        *   This step calculates the maximum path sum *passing through the current `root` node*. This path would be `left_path -> root -> right_path`. This path might not be extendable further upwards, so we update the global maximum here.
    *   **Return Value:** `return max(l_sum, r_sum) + root->val;`.
        *   This function returns the maximum path sum that *starts at the current `root` and goes downwards* (either through its left subtree or right subtree). This value is what the parent node will use to potentially extend its own path. We only choose the maximum of `l_sum` or `r_sum` because a path cannot branch to both left and right from the current `root` and still go upwards.

3.  **`maxPathSum(TreeNode* root)` function (Main Entry Point):**
    *   Calls `solve(root)` to start the DFS traversal and populate the global `ans`.
    *   Returns the final `ans`.

```cpp
#include <algorithm> // For std::max
#include <limits>    // For std::numeric_limits<int>::min

// Definition for a binary tree node (assuming it's provided or defined elsewhere)
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    // Global variable to store the overall maximum path sum found anywhere in the tree.
    // Initialized to the smallest possible integer value.
    int overall_max_path_sum = std::numeric_limits<int>::min();

    // Recursive helper function to calculate the maximum path sum starting at 'root' and going downwards.
    // Also updates the 'overall_max_path_sum' for paths that pass through 'root'.
    int solve(TreeNode* root)
    {
        // Base case: If the node is NULL, it contributes 0 to any path sum.
        if(root == NULL){return 0;}
        
        // Recursively calculate the maximum path sum from the left child, ensuring it's non-negative.
        // If a child path sum is negative, we ignore it (effectively starting a new path from the current node).
        int l_sum = std::max(0, solve(root->left));
        // Same for the right child.
        int r_sum = std::max(0, solve(root->right));
        
        // Update the overall maximum path sum.
        // This considers a path that goes from the left subtree, through the current root,
        // and to the right subtree. This path cannot be extended further upwards.
        overall_max_path_sum = std::max(overall_max_path_sum, l_sum + r_sum + root->val);
        
        // Return the maximum path sum that can be extended upwards from the current root.
        // A path extending upwards can only go through one child (either left or right) or just the root itself.
        return std::max(l_sum, r_sum) + root->val;
    }

    // Main function to find the maximum path sum in the binary tree.
    int maxPathSum(TreeNode* root) 
    {
        // Call the recursive helper function to populate overall_max_path_sum.
        solve(root);
        // Return the final overall maximum path sum.
        return overall_max_path_sum;
    }
};
```