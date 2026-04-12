# Serialize and Deserialize a Binary Tree

## Problem Description

Given the root of a binary tree, design an algorithm to **serialize** it into a sequence of numbers (e.g., a list or array) and then **deserialize** that sequence back into the original binary tree. The serialization should be lossless, meaning the deserialized tree must be identical to the original tree.

This solution uses a preorder traversal approach for both serialization and deserialization, marking `NULL` nodes with a special value (e.g., -1).

## C++ Solution

This C++ solution implements serialization and deserialization of a binary tree.

**`Node` Structure (provided by driver code):**

```cpp
struct Node {
    int data;
    Node *left;
    Node *right;
    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
```

**`Solution` Class Methods:**

### `serialize(Node *root)`

*   **Purpose:** Converts a binary tree into a linear sequence of integers (vector).
*   **Approach:** Uses a recursive preorder traversal (`solveSer`) to visit nodes.
    *   If `root` is `NULL`, it pushes `-1` to the vector `A` to mark a null child.
    *   Otherwise, it pushes `root->data` to `A`, then recursively calls `solveSer` for the left child, and then for the right child.
*   Returns the resulting `vector<int> A`.

### `deserialize(vector<int> &A)`

*   **Purpose:** Reconstructs a binary tree from a linear sequence of integers.
*   **Approach:** Uses a recursive helper function `solveDeSer` and an `index` to keep track of the current position in the serialized vector `A`.
    *   **Base Cases:**
        *   If `index` goes out of bounds, return `NULL`.
        *   Read `val = A[index]`, then increment `index`.
        *   If `val` is `-1`, it signifies a `NULL` node, so return `NULL`.
    *   **Recursive Step:**
        *   Create a new `Node` with `val`.
        *   Recursively set `root->left = solveDeSer(A, index)`.
        *   Recursively set `root->right = solveDeSer(A, index)`.
        *   Return the constructed `root`.

## Driver Code (C++)

The provided driver code handles reading tree input as a level-order string (e.g., "1 2 3 N N 4 5 N N N N"), building the tree, serializing it, deleting the original tree, deserializing it back, and then printing the inorder traversal of the deserialized tree for verification.

```cpp
#include <iostream>   // For std::cin, std::cout, std::getline
#include <vector>     // For std::vector
#include <string>     // For std::string, std::stoi
#include <sstream>    // For std::istringstream
#include <queue>      // For std::queue
#include <cstdio>     // For scanf

// Tree Node structure (provided by the problem statement/driver code)
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

// Function to build a binary tree from a level-order string input
Node *buildTree(std::string str) {
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    std::vector<std::string> ip; // Stores string tokens

    std::istringstream iss(str);
    for (std::string token; iss >> token;)
        ip.push_back(token);

    Node *root = new Node(std::stoi(ip[0])); // Create the root node

    std::queue<Node *> q; // Queue for level-order traversal
    q.push(root);

    int i = 1;
    while (!q.empty() && i < ip.size()) {
        Node *currNode = q.front();
        q.pop();

        std::string currVal = ip[i];

        // Process left child
        if (currVal != "N") {
            currNode->left = new Node(std::stoi(currVal));
            q.push(currNode->left);
        }

        // Process right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        if (currVal != "N") {
            currNode->right = new Node(std::stoi(currVal));
            q.push(currNode->right);
        }
        i++;
    }

    return root;
}

class Solution
{
public:
    // Helper function for serialization (preorder traversal)
    void solveSer(Node* root, std::vector<int>& A)
    {
        if(root == NULL){
            A.push_back(-1); // Mark NULL nodes with -1
            return;
        }
        
        A.push_back(root->data); // Add current node's data
        solveSer(root->left, A);   // Recurse for left child
        solveSer(root->right, A);  // Recurse for right child
    }
    
    // Function to serialize a tree and return a list containing nodes of tree.
    std::vector<int> serialize(Node *root) 
    {
        std::vector<int> A;
        solveSer(root, A);
        return A;
    }
    
    // Helper function for deserialization (reconstructs tree from serialized vector)
    Node* solveDeSer(std::vector<int>& A, int& index)
    {
        // If index goes out of bounds, or we encounter a -1 (NULL marker)
        if(index >= A.size() || A[index] == -1){
            index++; // Consume the -1 or out-of-bounds index
            return NULL;
        }
       
        int val = A[index]; // Get current node's value
        index++; // Move to the next element in the serialized vector
        
        Node* root = new Node(val); // Create the current root node
        root->left = solveDeSer(A, index);   // Recursively build left subtree
        root->right = solveDeSer(A, index);  // Recursively build right subtree
        
        return root;
    }
    
    // Function to deserialize a list and construct the tree.
    Node * deSerialize(std::vector<int> &A)
    {
        int index = 0; // Index to traverse the serialized vector
        return solveDeSer(A, index);
    }
};

// Function to print inorder traversal of the tree (for verification)
void inorder(Node *root) {
    if (root == NULL)
        return;
    inorder(root->left);
    std::cout << root->data << " ";
    inorder(root->right);
}

// Helper to delete tree nodes to prevent memory leaks
void _deleteTree(Node* node)  
{  
    if (node == NULL) return;  
    _deleteTree(node->left);  
    _deleteTree(node->right);  
    delete node;  
}  
  
// Wrapper to delete tree and set root to NULL
void deleteTree(Node** node_ref)  
{  
    _deleteTree(*node_ref);  
    *node_ref = NULL;  
}  

int main() {
    int tc;
    scanf("%d ", &tc); // Read number of test cases
    while (tc--) {
        std::string treeString;
        std::getline(std::cin >> std::ws, treeString); // Read tree as a string
        Node *root = buildTree(treeString);
        
        Solution serial, deserial;
        std::vector<int> A = serial.serialize(root); // Serialize the tree
        deleteTree(&root); // Delete original tree to test deserialization
        Node *getRoot = deserial.deSerialize(A); // Deserialize to get a new tree
        inorder(getRoot); // Print inorder traversal of deserialized tree
        std::cout << "\n";
        deleteTree(&getRoot); // Clean up deserialized tree
    }
    return 0;
}
```