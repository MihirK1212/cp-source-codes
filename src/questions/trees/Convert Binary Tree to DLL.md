# Convert Binary Tree to Doubly Linked List

## Problem Description

Given a binary tree, convert it into a doubly linked list (DLL). The conversion should be done in-place. The structure of the doubly linked list should follow the in-order traversal of the binary tree. That is, the left pointers of the DLL nodes should point to the previous node, and the right pointers should point to the next node in the in-order traversal.

## C++ Solution

This C++ solution provides an in-place conversion of a binary tree to a doubly linked list using a modified in-order traversal. The `bToDLL` function recursively processes the tree, maintaining a `tail` pointer to track the last node added to the DLL.

**Algorithm:**

1.  **`bToDLL(Node *root)` function:**
    *   **Parameters:**
        *   `root`: The current node of the binary tree being processed.
    *   **Global Variable:** `Node* tail = NULL;` This `tail` pointer keeps track of the last node added to the doubly linked list. It is crucial for linking the current node to the previous one.
    *   **Base Case:** If `root` is `NULL`, return `root` (or `NULL`).
    *   **Recursive Step (In-order Traversal Logic):**
        1.  **Process Left Subtree:** Recursively call `bToDLL(root->left)`. The result of this call (the head of the DLL from the left subtree) is stored in `head`.
        2.  **Link Current Node to Previous (`tail`):**
            *   Set `root->left = tail;` (The left pointer of the current node points to the previously processed node in the DLL).
            *   If `tail` is not `NULL`, set `tail->right = root;` (The right pointer of the previous node points to the current node). This completes the double link.
        3.  **Update `tail`:** Set `tail = root;` (The current node becomes the new tail of the DLL).
        4.  **Process Right Subtree:** Recursively call `bToDLL(root->right)`. This will link the current `tail` (which is `root`) to the head of the DLL formed by the right subtree.
        5.  **Return Head:** Return `head`. This ensures that the head of the *entire* DLL is correctly returned from the initial call.

**Note:** The global `tail` pointer is essential here. In a typical in-order traversal, when you visit a node, you process it. In this conversion, processing a node means linking it to the previous node (tracked by `tail`) and updating `tail`.

```cpp
// Structure for a Node in Binary Tree (and Doubly Linked List)
// In a DLL, left pointer acts as 'prev' and right pointer acts as 'next'.
struct Node {
    int data;
    Node *left; // In DLL, acts as previous pointer
    Node *right; // In DLL, acts as next pointer
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

class Solution
{
public:
    // Global pointer to keep track of the tail of the Doubly Linked List
    // This is crucial for linking nodes during in-order traversal.
    Node* tail = NULL;
    
    // Function to convert binary tree to doubly linked list and return its head.
    Node * bToDLL(Node *root)
    {
        // Base case: If the current node is NULL, there's nothing to convert.
        if(!root){return root;}
        
        // Process nodes in inorder fashion: left, root, right
        
        // Recursively convert the left subtree.
        // The 'head' of the DLL formed from the left subtree will be returned here.
        // If root->left is NULL, then the current root is the first node encountered
        // in inorder traversal for its subtree, so its head is itself.
        Node *head = (root->left) ? bToDLL(root->left) : root;
        
        // Link the current root node to the previously processed node (which is 'tail').
        root->left = tail;
        
        // If there was a previous node ('tail' is not NULL), link its right pointer to the current root.
        if(tail){
            tail->right = root;
        }
        
        // Update 'tail' to the current root node, as it is now the last node in the DLL formed so far.
        tail = root;
        
        // Recursively convert the right subtree.
        // The right pointer of the current root will be linked to the head of the DLL from the right subtree.
        // Note: The global 'tail' will be updated within the recursive call for the right subtree,
        // so when it returns, 'tail' will point to the last node of the entire processed subtree (including right).
        root->right = bToDLL(root->right);
        
        // Return the head of the DLL.
        return head;
    }
};
```