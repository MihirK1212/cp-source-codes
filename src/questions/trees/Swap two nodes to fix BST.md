# Swap Two Nodes to Fix BST

## Problem Description

Two nodes of a Binary Search Tree (BST) are swapped, which means the BST is no longer valid. The task is to correct the BST by swapping them back, without changing its structure. The goal is to restore the BST property, where the in-order traversal of the tree yields a sorted sequence.

## C++ Solution

```cpp
class Solution {
  public:
    
    void solve(Node* root,Node* &first,Node* &second,Node* &prev)
    {
        if(root==NULL){return;}
        
        solve(root->left,first,second,prev);
        
        if(prev!=NULL && (prev->data)>(root->data))
        {
            if(!first){first = prev;}
            second = root;
        }
        
        prev = root;
        
        solve(root->right,first,second,prev);
    }
    
    
    void correctBST( struct Node* root )
    {
        Node *first=NULL , *second=NULL , *prev=NULL;
        
        solve(root,first,second,prev);
        
        if(!first || !second){return;}
        
        int temp = first->data;
        first->data = second->data;
        second->data = temp;
        
    }
};
```