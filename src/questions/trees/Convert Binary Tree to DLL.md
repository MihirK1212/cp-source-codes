# Convert Binary Tree to DLL

// This function should return head to the DLL

```cpp
class Solution
{
    public:
    
    Node* tail = NULL;
    
    //Function to convert binary tree to doubly linked list and return it.
    Node * bToDLL(Node *root)
    {
        if(!root){return root;}
        
        
        //process nodes in inorder fashion : left , root , right
        
        Node *head = (root->left) ? bToDLL(root->left) : root ;
        
        root->left = tail;
        
        if(tail){
            tail->right = root;
        }
        
        tail = root;
        
        root->right = bToDLL(root->right);
        
        return head;
    }
};
```
