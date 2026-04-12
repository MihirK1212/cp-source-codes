# Find All Possible Full Binary Trees

## Problem Description

This problem is from LeetCode: [All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/).

Given an integer `n`, return a list of all possible full binary trees with `n` nodes. Each node has `val == 0`. Each node in a full binary tree has exactly `0` or `2` children.

Return the answer in any order.

## C++ Solution

This C++ solution uses dynamic programming with memoization to find all possible full binary trees with `n` nodes. A full binary tree is defined as a tree where every node has either zero or two children. This means that a full binary tree with `n` nodes must have an odd number of nodes. If `n` is even, no full binary tree can be formed.

**Algorithm (`findCompleteTrees` recursive helper function with memoization):**

1.  **Memoization Table:** A `map<int, vector<TreeNode*>> dp` is used to store already computed results for `n` nodes. `dp[n]` will store a vector of `TreeNode*` representing all possible full binary trees with `n` nodes.

2.  **Base Cases:**
    *   If `n == 0`: Return an empty vector. No nodes, no tree.
    *   If `n == 1`: Return a vector containing a single `TreeNode` with value `0`. This is the smallest full binary tree.
    *   If `dp[n]` already contains results, return `dp[n]`.

3.  **Recursive Step:** If `n > 1` (and `n` must be odd):
    *   Initialize an empty `vector<TreeNode*> curr_ans` to store the results for the current `n`.
    *   Iterate `L` from `0` to `n-1` (representing the number of nodes in the left subtree).
        *   `R = n - 1 - L`: This calculates the number of nodes in the right subtree. `n-1` is for the root node, and `L` for the left subtree, so `R` is the remainder.
        *   **Crucially, `L` and `R` must both be odd for full binary trees.** The loop implicitly handles this because `findCompleteTrees` for even numbers will return empty lists, preventing the creation of invalid trees. Alternatively, the loop can be `for (int L = 1; L < n; L += 2)`. This optimization explicitly checks for odd `L` and `R`.
        *   Recursively call `leftTrees = findCompleteTrees(L)` and `rightTrees = findCompleteTrees(R)`.
        *   **Combine Subtrees:** For every possible `leftTree` from `leftTrees` and every possible `rightTree` from `rightTrees`:
            *   Create a new `TreeNode* newRoot = new TreeNode(0);`.
            *   Set `newRoot->left = r_l;`.
            *   Set `newRoot->right = r_r;`.
            *   Add `newRoot` to `curr_ans`.

4.  **Store and Return:** Store `curr_ans` in `dp[n]` and return `curr_ans`.

**`allPossibleFBT(int n)` function:**

*   This is the main entry point, which simply calls `findCompleteTrees(n)`.

**Note:** A full binary tree must have an odd number of nodes. If `n` is even, `findCompleteTrees(n)` will correctly return an empty vector because no combination of odd `L` and odd `R` will sum to an even `n-1` (which must be even if `n` is odd).

```cpp
#include <vector>
#include <map>

// Definition for a binary tree node (assuming it's provided by LeetCode or defined elsewhere)
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
    // Memoization table: dp[n] stores all possible full binary trees with n nodes.
    std::map<int, std::vector<TreeNode*>> dp;
    
    // Recursive function to find all possible full binary trees with 'n' nodes.
    std::vector<TreeNode*> findCompleteTrees(int n)
    {
        // If n is even, a full binary tree cannot be formed.
        // If n is 0, no nodes, so no tree.
        if(n == 0 || n % 2 == 0){ // Added n % 2 == 0 check for efficiency, although the loop handles it.
            return {}; // Return an empty vector
        }
       
        // Base case: If n is 1, return a single node tree.
        if(n == 1)
        {
            return {new TreeNode(0)};
        }

        // Check memoization table before recomputing.
        if(dp.count(n)) // Using .count() for map lookup
        {
            return dp[n];
        }
       
        std::vector<TreeNode*> current_ans; 
        
        // Iterate through possible sizes for the left subtree (L)
        // L must be odd for a full binary tree. R will also be odd since n-1 is even.
        for(int L = 1; L < n; L += 2) // L must be odd and at least 1, and less than n
        {
            int R = n - 1 - L; // Calculate nodes for the right subtree
            
            // Recursively get all possible left and right subtrees
            std::vector<TreeNode*> leftTrees = findCompleteTrees(L);
            std::vector<TreeNode*> rightTrees = findCompleteTrees(R);
            
            // Combine left and right subtrees with a new root
            for(TreeNode* r_l : leftTrees)
            {
                for(TreeNode* r_r : rightTrees)
                {
                    TreeNode* newRoot = new TreeNode(0);
                    newRoot->left = r_l;
                    newRoot->right = r_r;
                    current_ans.push_back(newRoot);
                }
            }
        }
        
        // Store the computed results in the memoization table and return.
        dp[n] = current_ans;
        
        return current_ans;
    }
    
    // Main function to initiate the process.
    std::vector<TreeNode*> allPossibleFBT(int n) 
    {
        return findCompleteTrees(n);    
    }
};
```