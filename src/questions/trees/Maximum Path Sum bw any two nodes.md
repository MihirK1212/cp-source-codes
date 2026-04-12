# Maximum Path Sum Between Any Two Nodes in a Binary Tree

## Problem Description

Given a binary tree, find the maximum path sum. A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to pass through the root. The path must contain at least one node and does not need to go downwards.

For example, if the tree is:
```
    1
   / \
  2   3
```
The maximum path sum would be `6` (2 -> 1 -> 3).

## C++ Solution

This problem can be solved using a recursive approach (often implemented with a helper function) that keeps track of two important values at each node:
1.  The maximum path sum that starts at the current node and goes downwards (either to its left child, right child, or just itself).
2.  The overall maximum path sum found so far, which could be a path that passes through the current node and potentially involves both its left and right subtrees.

The `solve` function returns the maximum path sum that starts at the `root` and goes downwards. The global `ans` variable (or a member variable in the `Solution` class) keeps track of the overall maximum path sum found anywhere in the tree.

```cpp
// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Tree Node
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

// Function to Build Tree from string input (level order traversal)
Node *buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after splitting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str_val; iss >> str_val;)
        ip.push_back(str_val);

    // Create the root of the tree
    Node *root = new Node(stoi(ip[0]));

    // Push the root to the queue
    queue<Node *> queue_nodes;
    queue_nodes.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue_nodes.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node *currNode = queue_nodes.front();
        queue_nodes.pop();

        // Get the current Node's left child value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current Node
            currNode->left = new Node(stoi(currVal));

            // Push it to the queue
            queue_nodes.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current Node
            currNode->right = new Node(stoi(currVal));

            // Push it to the queue
            queue_nodes.push(currNode->right);
        }
        i++;
    }

    return root;
}


 // } Driver Code Ends
// User Function template for C++

class Solution {
  public:
    // 'ans' will store the maximum path sum found anywhere in the tree
    int ans = INT_MIN; 
    
    // Helper function to find the maximum path sum starting at 'root' and going downwards.
    // It also updates the global 'ans' with the maximum path sum between any two nodes.
    int solve(Node* root)
    {
        // Base case: if node is NULL, return 0 (no contribution to sum)
        if(root == NULL){return 0;}
        
        // Recursively calculate max path sum from left and right children, ensuring non-negative contributions
        int l_sum = std::max(0, solve(root->left));
        int r_sum = std::max(0, solve(root->right));
        
        // Update the overall maximum path sum found so far.
        // A path can pass through the current root, using left_sum + root->data + right_sum.
        ans = std::max(ans, root->data + l_sum + r_sum);
        
        // Return the maximum path sum that starts at 'root' and goes downwards.
        // This path must be either root->data + l_sum or root->data + r_sum.
        return root->data + std::max(l_sum, r_sum);
    }
    
    // Main function to find the maximum path sum between any two nodes.
    int findMaxSum(Node* root)
    {
        // Handle case of empty tree
        if (root == NULL) return 0; // Or throw an exception, depending on problem spec

        solve(root); // Call the helper function to compute max sums and update 'ans'
        return ans;
    }
};

// { Driver Code Starts.


int main() {
    int tc;
    scanf("%d ", &tc);
    while (tc--) {
        string treeString;
        getline(cin, treeString);
        Solution ob;
        Node *root = buildTree(treeString);
        cout << ob.findMaxSum(root) << "\n";

    }


    return 0;
}  // } Driver Code Ends
```
