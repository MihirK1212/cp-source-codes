# Maximum Sum of Non-Adjacent Nodes in a Binary Tree

## Problem Description

Given a binary tree, find the maximum sum of nodes such that no two selected nodes are adjacent. This means if a node is selected, its direct parent and direct children cannot be selected.

## C++ Solution

This problem can be solved using dynamic programming on trees (also known as tree DP). For each node, there are two possibilities to consider when calculating the maximum sum for the subtree rooted at that node:

1.  **Include the current node:** If the current node (`root`) is included, its direct children (`root->left`, `root->right`) *cannot* be included. Therefore, we must consider the maximum sums from its grandchildren. The sum for this case would be `root->data` + (maximum sum from `root->left->left`) + (maximum sum from `root->left->right`) + (maximum sum from `root->right->left`) + (maximum sum from `root->right->right`).
2.  **Exclude the current node:** If the current node (`root`) is excluded, its direct children *can* be included. The sum for this case would be (maximum sum from `root->left`) + (maximum sum from `root->right`).

The maximum of these two possibilities for each node (recursively computed) gives the optimal solution for the subtree rooted at that node. Memoization (`std::map<Node*, int> sum` and `std::map<Node*, bool> visited`) is used to store and retrieve previously computed results for subtrees to avoid redundant calculations, improving efficiency to O(N).

**Algorithm (`getMaxSum` recursive helper function with memoization):**

1.  **Base Case:** If `root` is `NULL`, return `0`.
2.  **Memoization:** If `visited[root]` is `true`, return `sum[root]` (the already computed maximum sum for this subtree).
3.  **Calculate `v1` (Exclude `root`):** Recursively calculate the maximum sum by excluding the current `root`. This involves summing the `getMaxSum` of its left child and right child.
    *   `v1 = getMaxSum(root->left) + getMaxSum(root->right);`
4.  **Calculate `v2` (Include `root`):** Calculate the maximum sum by including the current `root`. This involves `root->data` plus the `getMaxSum` of all its grandchildren.
    *   `v2 = root->data;`
    *   If `root->left` exists, add `getMaxSum(root->left->left)` and `getMaxSum(root->left->right)` to `v2`.
    *   If `root->right` exists, add `getMaxSum(root->right->left)` and `getMaxSum(root->right->right)` to `v2`.
5.  **Store and Return:** Mark `visited[root] = true` and store the maximum of `v1` and `v2` in `sum[root]`. Return `sum[root]`.

```cpp
// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h> 
using namespace std; 

// Tree Node structure (assumed to be provided or defined globally)
struct Node
{
    int data;
    Node* left;
    Node* right;
};

// Utility function to create a new Tree Node
Node* newNode(int val)
{
    Node* temp = new Node;
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;
    
    return temp;
}

// Function to Build Tree from string input (level order traversal)
Node* buildTree(string str)
{
    // Corner Case
    if(str.length() == 0 || str[0] == 'N')
            return NULL;
    
    // Creating vector of strings from input 
    // string after splitting by space
    vector<string> ip;
    
    istringstream iss(str);
    for(string str_val; iss >> str_val; )
        ip.push_back(str_val);
        
    // Create the root of the tree
    Node* root = newNode(stoi(ip[0]));
        
    // Push the root to the queue
    queue<Node*> queue_nodes;
    queue_nodes.push(root);
        
    // Starting from the second element
    int i = 1;
    while(!queue_nodes.empty() && i < ip.size()) {
            
        // Get and remove the front of the queue
        Node* currNode = queue_nodes.front();
        queue_nodes.pop();
            
        // Get the current node's left child value from the string
        string currVal = ip[i];
            
        // If the left child is not null
        if(currVal != "N") {
                
            // Create the left child for the current node
            currNode->left = newNode(stoi(currVal));
                
            // Push it to the queue
            queue_nodes.push(currNode->left);
        }
            
        // For the right child
        i++;
        if(i >= ip.size())
            break;
        currVal = ip[i];
            
        // If the right child is not null
        if(currVal != "N") {
                
            // Create the right child for the current node
            currNode->right = newNode(stoi(currVal));
                
            // Push it to the queue
            queue_nodes.push(currNode->right);
        }
        i++;
    }
    
    return root;
}

 // } Driver Code Ends
//User function Template for C++

//Node Structure (provided in problem)
/*
struct Node
{
    int data;
    Node* left;
    Node* right;
};
*/

class Solution{
public:
    // Maps for memoization:
    // 'sum' stores the maximum sum for the subtree rooted at a given Node*.
    std::map<Node*, int> sum; 
    // 'visited' tracks if the maximum sum for a Node* has already been computed.
    std::map<Node*, bool> visited; 
    
    // Function to return the maximum sum of non-adjacent nodes in a binary tree.
    int getMaxSum(Node *root) 
    {
        // Base case: If the current node is NULL, it contributes 0 to the sum.
        if(root == NULL){return 0;}
        
        // Memoization check: If the result for this node is already computed,
        // return the stored value to avoid redundant calculations.
        if(visited[root]){return sum[root];}
        
        // Case 1: Exclude the current node (root).
        // If the current node is excluded, its children (left and right) can be included.
        // So, the sum is the maximum sum from the left subtree + maximum sum from the right subtree.
        int v1 = getMaxSum(root->left) + getMaxSum(root->right);
        
        // Case 2: Include the current node (root).
        // If the current node is included, its direct children CANNOT be included.
        // We must then consider the maximum sums from its grandchildren.
        int v2 = root->data; // Start with the data of the current node.
        
        // Add max sum from left-left and left-right grandchildren
        if(root->left != NULL) {
            v2 += getMaxSum(root->left->left);
            v2 += getMaxSum(root->left->right);
        }
        
        // Add max sum from right-left and right-right grandchildren
        if(root->right != NULL) {
            v2 += getMaxSum(root->right->left);
            v2 += getMaxSum(root->right->right);
        }
        
        // Mark the current node as visited and store the maximum of the two cases.
        visited[root] = true;
        sum[root] = std::max(v1, v2);
        
        return sum[root]; // Return the computed maximum sum for this subtree.
    }
};

// { Driver Code Starts.

// Driver code 
int main()
{
  int t;
  scanf("%d ",&t);
  while (t--)
  {
        string s;
		getline(cin,s);
		Node* root = buildTree(s);
		Solution ob;
        cout<<ob.getMaxSum(root)<<endl;
  }
  return 0;
}
// } Driver Code Ends
```