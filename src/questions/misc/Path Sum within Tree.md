# Path Sum within Tree

## Problem Description

This problem is from LeetCode: [Path Sum III](https://leetcode.com/problems/path-sum-iii/).

Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the nodes' values equals `targetSum`. A path can start or end at any node in the tree but must go downwards (traveling only from parent nodes to child nodes).

## C++ Solution

This C++ solution uses a recursive approach (DFS) combined with a hash map to efficiently count paths that sum to `targetSum`. The key idea is to track prefix sums encountered from the root down to the current node.

**Algorithm:**

1.  **`countPaths(TreeNode* root, map<long long, int>& freqPSums, int currPSum, int targetSum)` function (Recursive Helper):**
    *   **Parameters:**
        *   `root`: The current node being visited.
        *   `freqPSums`: A `map` to store the frequency of prefix sums encountered so far along the current path from the root.
        *   `currPSum`: The sum of node values from the root to the current `root` (inclusive).
        *   `targetSum`: The target sum we are looking for.
    *   **Base Case:** If `root` is `NULL`, return.
    *   **Recursive Step:**
        1.  Add `root->val` to `currPSum`.
        2.  Check if `currPSum - targetSum` exists in `freqPSums`. If it does, it means there's a subpath ending at `root` that sums to `targetSum`. Add `freqPSums[currPSum - targetSum]` to the global `ans`.
        3.  Increment `freqPSums[currPSum]` (mark this prefix sum as seen).
        4.  Recursively call `countPaths` for the left and right children.
        5.  **Backtrack:** Decrement `freqPSums[currPSum]` after processing a node's children. This is crucial because `freqPSums` should only reflect prefix sums on the *current* path from the root, not paths from other branches.

2.  **`pathSum(TreeNode* root, int targetSum)` function (Main Entry Point):**
    *   **Base Case:** If `root` is `NULL`, return `0`.
    *   Initializes `ans = 0`.
    *   Creates an empty `map<long long, int> freqPSums`.
    *   `freqPSums[0] = 1`: This is important. It handles cases where the path *itself* (starting from the root) sums to `targetSum`, or a subpath starting from any node (after the root) sums to `targetSum` where the difference `currPSum - targetSum` results in `0` (meaning the `currPSum` itself is `targetSum`).
    *   Calls `countPaths` to start the recursive traversal.
    *   Returns the final `ans`.

```cpp
// https://leetcode.com/problems/path-sum-iii/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    int ans=0;
    
    void countPaths(TreeNode* root , map<long long,int>&freqPSums,int currPSum,int targetSum)
    {
        if(root==NULL){return;}
        
        int x = root->val;
        
        currPSum+=x;
        
        ans+=freqPSums[currPSum - targetSum];
        
        freqPSums[currPSum]++;
        
        countPaths(root->left,freqPSums,currPSum,targetSum);
        countPaths(root->right,freqPSums,currPSum,targetSum);
        
        freqPSums[currPSum]--; // Backtrack: remove current prefix sum from map
    }
    
    int pathSum(TreeNode* root, int targetSum) 
    {
        if(root==NULL){return 0;}
        
        map<long long,int> freqPSums;
        
        freqPSums[0] = 1; // Represents the case where a path starts from the root and sums to targetSum
        
        countPaths(root,freqPSums,0,targetSum);
        return ans;
    }
};
```