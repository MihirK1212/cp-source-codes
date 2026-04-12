# Path Sum within Tree

## Problem Description

This problem is from LeetCode: [Path Sum III](https://leetcode.com/problems/path-sum-iii/)

Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the nodes along the path equals `targetSum`. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

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
    
    int ans=0;
    
    void countPaths(TreeNode* root , map<long long,int>&freqPSums,int currPSum,int targetSum)
    {
        if(root==NULL){return;}
        
        int x = root->val;
        
        currPSum+=x;
        
        ans+=freqPSums[currPSum - targetSum];
        
        freqPSums[currPSum]++;
        
        countPaths(root->left,freqPSums,currPSum,targetSum);
        countPaths(root->right,freqPSums,currPSums,targetSum);
        
        freqPSums[currPSum]--;
    }
    
    int pathSum(TreeNode* root, int targetSum) 
    {
        if(root==NULL){return 0;}
        
        map<long long,int> freqPSums;
        
        freqPSums[0] = 1;
        
        countPaths(root,freqPSums,0,targetSum);
        return ans;
    }
};
```