# Check if Tree is Height Balanced

## Problem Description

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every* node never differs by more than one.

## C++ Solution

This C++ solution uses a recursive approach to efficiently check if a binary tree is height-balanced. The key idea is to perform a post-order traversal (or a modified DFS) that not only calculates the height of each subtree but also checks for the balance condition simultaneously. If any subtree is found to be unbalanced, a special value (e.g., -1) is propagated up to indicate the imbalance.

**`Node` Structure (provided by driver code):**

```cpp
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
```

**`Solution` Class Methods:**

### `solve(Node* root)` function:

*   **Purpose:** This is a recursive helper function that returns the height of the subtree rooted at `root` if it is balanced, or `-1` if it is unbalanced.
*   **Base Case:** If `root` is `NULL`, its height is `0`. Return `0`.
*   **Recursive Step:**
    1.  Recursively call `solve` for the left child (`lh = solve(root->left)`) and the right child (`rh = solve(root->right)`).
    2.  **Check for Imbalance from Children:** If `lh` or `rh` is `-1`, it means a subtree is already unbalanced. Propagate this `-1` up by returning `-1`.
    3.  **Check Current Node's Balance:** Calculate the absolute difference between `lh` and `rh`. If `abs(lh - rh) > 1`, the current node's subtree is unbalanced. Return `-1`.
    4.  **Return Height:** If all checks pass, the current subtree is balanced. Return `max(lh, rh) + 1` (the height of the current subtree).

### `isBalanced(Node *root)` function:

*   **Purpose:** The main function that checks if the entire tree is balanced.
*   **Logic:** It simply calls `solve(root)`. If `solve` returns a value greater than or equal to 0, it means the tree is balanced (as -1 indicates imbalance). The original code uses `>0` to return `true`, implying that an empty tree (height 0) is considered balanced, which is typically correct.

## Driver Code (C++)

The provided driver code handles reading tree input as a level-order string, building the tree, and then calling the `isBalanced` function to print the boolean result.

```cpp
#include <iostream>   // For std::cin, std::cout, std::getline
#include <vector>     // For std::vector
#include <string>     // For std::string, std::stoi
#include <sstream>    // For std::istringstream
#include <queue>      // For std::queue
#include <algorithm>  // For std::max, std::abs

// Tree Node structure (provided by the problem statement/driver code)
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
}; 

// Utility function to create a new Tree Node (driver code might have different newNode)
// This is usually for convenience in driver code, not part of the Solution class itself.
Node* newNode(int val) {
    Node* temp = new Node(val);
    return temp;
}

// Function to Build Tree from a level-order string input
Node* buildTree(std::string str) {
    if (str.length() == 0 || str[0] == 'N') return NULL;

    std::vector<std::string> ip;
    std::istringstream iss(str);
    for (std::string token; iss >> token;) ip.push_back(token);

    Node* root = newNode(std::stoi(ip[0]));
    std::queue<Node*> q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < ip.size()) {
        Node* currNode = q.front();
        q.pop();

        std::string currVal = ip[i];
        if (currVal != "N") {
            currNode->left = newNode(std::stoi(currVal));
            q.push(currNode->left);
        }

        i++;
        if (i >= ip.size()) break;
        currVal = ip[i];

        if (currVal != "N") {
            currNode->right = newNode(std::stoi(currVal));
            q.push(currNode->right);
        }
        i++;
    }
    return root;
}

class Solution{
public:
    // Helper function that returns the height of the subtree rooted at 'root' if balanced,
    // or -1 if the subtree is unbalanced.
    int solve(Node* root)
    {
        // Base case: An empty tree has height 0 and is balanced.
        if(root == NULL){return 0;}
        
        // Recursively get heights of left and right subtrees
        int lh = solve(root->left);
        int rh = solve(root->right);
        
        // If any subtree is unbalanced (returned -1), propagate -1 up.
        if(lh == -1 || rh == -1){return -1;}
        
        // Check balance condition for the current node: difference in heights <= 1.
        if(std::abs(lh - rh) > 1){return -1;}
        
        // If balanced, return the height of the current subtree.
        return std::max(lh, rh) + 1;
    }   

    // Main function to check if the entire binary tree is height-balanced.
    bool isBalanced(Node *root)
    {
        // If solve(root) returns >= 0, it means the tree is balanced. Otherwise, it's -1.
        return solve(root) >= 0; 
    }
};

int main() {
    // Fast I/O setup
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t; // Read number of test cases
    std::string s_dummy; // Consume the newline character after reading t
    std::getline(std::cin, s_dummy);

    while (t--) {
        std::string s;
        std::getline(std::cin, s); // Read tree as a string
        
        Node* root = buildTree(s);
        Solution ob;
        std::cout << ob.isBalanced(root) << std::endl; // Output 1 for balanced, 0 for unbalanced
    }
    return 0;
}
```