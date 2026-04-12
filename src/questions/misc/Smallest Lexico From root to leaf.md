# Smallest Lexicographical String From Root to Leaf

## Problem Description

This problem is from LeetCode: [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/submissions/)

You are given the `root` of a binary tree where each node has a value from 0 to 25 representing the letters 'a' to 'z'. Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

## C++ Solution

```cpp
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
    
   string lexSmallest(TreeNode* root,string y)
    {
        if(root==NULL){return "{";}
        
        y=(char)(root->val+'a') + y ;
        
        if((root->left)==NULL && (root->right)==NULL){return y;}
        
        string L = lexSmallest(root->left,y);
        string R = lexSmallest(root->right,y);
        
        if(L<=R)
        {
            return L;
        }
        else
        {
            return R;
        }
        
        return "";
    }

    string smallestFromLeaf(TreeNode* root)
    {
        string ans = lexSmallest(root,"");
        return ans;
    }
};
```