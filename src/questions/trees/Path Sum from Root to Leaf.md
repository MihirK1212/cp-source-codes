# Path Sum from Root to Leaf (Path Sum II)

## Problem Description

This problem is commonly known as [Path Sum II on LeetCode](https://leetcode.com/problems/path-sum-ii/).

Given the `root` of a binary tree and an integer `targetSum`, return all root-to-leaf paths where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of node values.

A **leaf** is a node with no children.

## C++ Solution

This problem can be solved using a recursive Depth-First Search (DFS) approach. We traverse the tree from the root to the leaves, maintaining the current path and the remaining sum needed.

**`TreeNode` Structure:**

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
```

**`findPaths(TreeNode* root, int sum, std::vector<int>& path)` function (Recursive Helper):**

*   **Parameters:**
    *   `root`: The current node being visited.
    *   `sum`: The remaining sum needed to reach `targetSum` from the current node to a leaf.
    *   `path`: A `std::vector<int>` that stores the node values of the current path from the root to the current node.

*   **Base Case:**
    *   If `root` is `NULL`, return (end of a branch).

*   **Recursive Step:**
    1.  Add `root->val` to the `path`.
    2.  Subtract `root->val` from `sum`.
    3.  **Check for Leaf Node:** If the current node `root` is a leaf (both `root->left` and `root->right` are `NULL`) AND `sum` is `0`, it means we have found a valid path. Add a copy of the current `path` to the `ans` (result vector).
    4.  Recursively call `findPaths` for the left child: `findPaths(root->left, sum, path)`.
    5.  Recursively call `findPaths` for the right child: `findPaths(root->right, sum, path)`.
    6.  **Backtrack:** After visiting both children, remove `root->val` from `path` using `path.pop_back()`. This step is crucial to backtrack and explore other paths correctly.

**`pathSum(TreeNode* root, int targetSum)` function (Main Entry Point):**

*   **Parameters:**
    *   `root`: The root of the binary tree.
    *   `targetSum`: The target sum to achieve.

*   **Logic:**
    1.  If the `root` is `NULL`, return an empty result (`ans`).
    2.  Initialize an empty `std::vector<int> path`.
    3.  Call the `findPaths` helper function with the `root`, `targetSum`, and `path`.
    4.  Return the `ans` vector containing all found paths.

```cpp
#include <vector>   // For std::vector
#include <iostream> // For standard input/output (optional, for testing)

// Definition for a binary tree node (provided by LeetCode/similar platforms).
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
    std::vector<std::vector<int>> ans; // Stores all valid paths
    
    // Recursive helper function to find paths that sum to the target.
    // root: current node
    // sum: remaining sum needed from current node to a leaf
    // path: current path from root to current node
    void findPaths(TreeNode* root, int sum, std::vector<int>& path)
    {
        // Base Case 1: If current node is null, return.
        if(root == nullptr) {
            return;
        }
        
        // Add current node's value to the path and subtract from the sum.
        path.push_back(root->val);
        sum -= (root->val);
        
        // Base Case 2: If it's a leaf node AND the sum becomes 0, 
        // it means we found a valid path.
        if(root->left == nullptr && root->right == nullptr && sum == 0) {
            ans.push_back(path); // Add a copy of the current path to the results.
        }
        
        // Recursively explore left and right subtrees.
        findPaths(root->left, sum, path);
        findPaths(root->right, sum, path);
        
        // Backtrack: Remove the current node's value from the path 
        // before returning to the parent, to explore other branches.
        path.pop_back();
    }
    
    // Main function to initiate the path sum search.
    std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) 
    {
        // If the tree is empty, return an empty list of paths.
        if(root == nullptr) {
            return ans;
        }
        
        std::vector<int> current_path; // Initialize an empty path vector.
        findPaths(root, targetSum, current_path); // Start the recursive search.
        
        return ans; // Return the collected paths.
    }
};
```