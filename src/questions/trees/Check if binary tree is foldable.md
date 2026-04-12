# Check if Binary Tree is Foldable

## Problem Description

Given a binary tree, determine if it is "foldable." A binary tree is foldable if its mirror image is structurally identical to the original tree. This means that if you fold the tree along the vertical axis passing through the root, the left and right subtrees must perfectly match each other in structure (though not necessarily in data values).

For example, a tree is foldable if the left child of the root has a left child, and the right child of the root has a right child, and so on, symmetrically.

This problem is available on GeeksforGeeks: [Foldable Binary Tree](https://practice.geeksforgeeks.org/problems/foldable-binary-tree/1/?track=DSASP-Tree&batchId=154).

## C++ Solution

This solution uses a recursive approach to check for foldability. The core idea is that a tree is foldable if its left subtree is structurally a mirror of its right subtree.

1.  **`IsFoldable(Node* root)` function:**
    *   **Base Case:** If the `root` is `NULL`, an empty tree is considered foldable, so return `true`.
    *   **Recursive Step:** Call the `equal` helper function with `root->left` and `root->right`. The tree is foldable if these two subtrees are "mirror-equal" in structure.
2.  **`equal(Node* r1, Node* r2)` function:**
    *   This function checks if two trees (`r1` and `r2`) are structurally mirror images of each other.
    *   **Base Cases:**
        *   If both `r1` and `r2` are `NULL`, they are mirror-equal (both empty), return `true`.
        *   If one is `NULL` and the other is not, they are not mirror-equal, return `false`.
    *   **Recursive Step:** Recursively check two conditions:
        *   The left child of `r1` must be mirror-equal to the right child of `r2` (`equal(r1->left, r2->right)`).
        *   The right child of `r1` must be mirror-equal to the left child of `r2` (`equal(r1->right, r2->left)`).
        *   If both recursive calls return `true`, then `r1` and `r2` are mirror-equal, so return `true`. Otherwise, return `false`.

```cpp
//Function to check whether a binary tree is foldable or not.
//https://practice.geeksforgeeks.org/problems/foldable-binary-tree/1/?track=DSASP-Tree&batchId=154


bool equal(Node* r1,Node* r2)
{
    // If both nodes are null, they are mirror-equal
    if(!r1 && !r2){return true;}
    // If one is null and other is not, they are not mirror-equal
    if((r1 && !r2) || (!r1 && r2)){return false;}
    
    // Recursively check:
    // Left child of r1 should be mirror-equal to Right child of r2
    // Right child of r1 should be mirror-equal to Left child of r2
    return equal(r1->left,r2->right) && equal(r1->right,r2->left);
}

bool IsFoldable(Node* root)
{
    // An empty tree is considered foldable
    if(root==NULL){return true;}
    
    // A tree is foldable if its left and right subtrees are mirror-equal
    return equal(root->left,root->right);
    
}
```