# Construct BST from Preorder Traversal

## Problem Description

Given the preorder traversal of a Binary Search Tree (BST), the task is to reconstruct the original BST. A key property of a BST is that an inorder traversal of its nodes yields elements in sorted order. This property is crucial for solving this problem.

Since we are given the preorder traversal, we can obtain the inorder traversal by simply sorting the given preorder array. Once we have both preorder and inorder traversals, the problem reduces to a classic tree reconstruction problem: constructing a binary tree from its preorder and inorder traversals.

## C++ Solution

This C++ solution reconstructs a BST from its preorder traversal.

**`TreeNode` Structure:**

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
```

**`findRootInd(vector<int>& arr, int x)` function:**

*   This is a helper function that performs a binary search on a sorted array (`arr`) to find the index of a given value `x`. In this context, `arr` will be the `inorder` traversal, and `x` will be the root value of the current subtree being built. It returns the 0-based index of `x` if found, otherwise -1 (though in this specific problem, `x` will always be found).

**`build(vector<int>& inorder, vector<int>& preorder, int inLB, int inUB, int preLB, int preUB)` function:**

*   This is a recursive function that builds the BST.
*   **Parameters:**
    *   `inorder`: The inorder traversal array.
    *   `preorder`: The preorder traversal array.
    *   `inLB`, `inUB`: Lower and upper bounds for the current segment of the `inorder` array.
    *   `preLB`, `preUB`: Lower and upper bounds for the current segment of the `preorder` array.
*   **Base Case:** If `inLB > inUB` or `preLB > preUB`, it means the current segment is invalid or empty, so return `NULL`.
*   **Recursive Step:**
    1.  The root value (`rootVal`) of the current subtree is always the first element in its `preorder` segment (`preorder[preLB]`).
    2.  Create a new `TreeNode` with `rootVal`.
    3.  Find `rootVal` in the `inorder` segment using `findRootInd`. This `rootInd` splits the `inorder` array into left and right subtrees.
    4.  Calculate `leftSize` (number of nodes in the left subtree).
    5.  Recursively call `build` for the left subtree:
        *   `inorder` range: `[inLB, rootInd - 1]`
        *   `preorder` range: `[preLB + 1, preLB + leftSize]`
    6.  Recursively call `build` for the right subtree:
        *   `inorder` range: `[rootInd + 1, inUB]`
        *   `preorder` range: `[preLB + leftSize + 1, preUB]`
    7.  Return the `root` of the current subtree.

**`Solution::constructBST(vector<int> &preorder)` function:**

*   This is the entry point for the solution.
*   It creates a copy of the `preorder` array into `inorder`.
*   It sorts the `inorder` array to obtain the sorted sequence of elements (which is the inorder traversal of a BST).
*   It determines the size `n` of the traversals.
*   Finally, it calls the `build` function with the full ranges of `inorder` and `preorder` arrays to start the tree construction process.

```cpp
#include <vector>
#include <algorithm> // Required for std::sort, std::lower_bound

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // Helper function to find the index of a value 'x' in a sorted array 'arr'
    // (Essentially a binary search)
    int findRootInd(std::vector<int>& arr, int x)
    {
        // Using std::lower_bound is more idiomatic and efficient than a manual binary search loop
        auto it = std::lower_bound(arr.begin(), arr.end(), x);
        if (it != arr.end() && *it == x) {
            return std::distance(arr.begin(), it);
        }
        return -1; // Should ideally always find in this problem context
    }

    // Recursive function to build the BST from inorder and preorder traversals
    TreeNode* build(
        std::vector<int>& inorder,
        std::vector<int>& preorder,
        int inLB, int inUB,   // Bounds for inorder traversal segment
        int preLB, int preUB  // Bounds for preorder traversal segment
    )
    {
        // Base case: If the segment is invalid or empty, return NULL
        if(inLB > inUB || preLB > preUB){return NULL;}
        
        // The first element in the preorder traversal segment is always the root of the current subtree
        int rootVal = preorder[preLB];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find the root value in the inorder traversal to determine left and right subtree sizes
        int rootInd = findRootInd(inorder, rootVal);
        
        // Calculate the size of the left subtree
        int leftSize = (rootInd - inLB);
        // The right subtree size is implicitly (inUB - rootInd)
        
        // Recursively build the left subtree
        // Inorder for left: [inLB, rootInd - 1]
        // Preorder for left: [preLB + 1, preLB + leftSize]
        root->left = build(inorder, preorder, inLB, rootInd - 1, preLB + 1, preLB + leftSize);
        
        // Recursively build the right subtree
        // Inorder for right: [rootInd + 1, inUB]
        // Preorder for right: [preLB + leftSize + 1, preUB]
        root->right = build(inorder, preorder, rootInd + 1, inUB, preLB + leftSize + 1, preUB);
        
        return root;
    }

    // Main function to construct the BST from its preorder traversal
    TreeNode* constructBST(std::vector<int> &preorder) 
    {
        // A BST's inorder traversal is its elements sorted
        std::vector<int> inorder = preorder;
        std::sort(inorder.begin(), inorder.end());

        int n = preorder.size();

        // Call the recursive build function with initial bounds for both traversals
        return build(inorder, preorder, 0, n - 1, 0, n - 1);
    }
};
```