# Construct Binary Tree from Inorder and Preorder Traversal

## Problem Description

Given two integer arrays, `preorder` and `inorder`, where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

**Constraints:**

*   All values in `preorder` and `inorder` are unique.
*   `inorder` is guaranteed to be an inorder traversal of the tree.
*   `preorder` is guaranteed to be a preorder traversal of the tree.

## C++ Solution

This C++ solution constructs a binary tree from its preorder and inorder traversals using a recursive approach. The key property used is that the first element in the preorder traversal is always the root of the current subtree. In the inorder traversal, all elements to the left of the root are in its left subtree, and all elements to the right are in its right subtree.

**Algorithm (`build` recursive helper function):**

1.  **Base Case:** If `inLB > inUB` or `preLB > preUB` (indicating an empty range for either traversal), return `NULL`.
2.  **Create Root:** The value `pre[preLB]` is the root of the current subtree. Create a new `Node` with this value.
3.  **Find Root in Inorder:** Search for `rootVal` in the `inorder` array within the bounds `[inLB, inUB]`. Let its index be `rootInd`.
4.  **Calculate Subtree Sizes:**
    *   `leftSize = rootInd - inLB;` (Number of nodes in the left subtree)
    *   `rightSize = inUB - rootInd;` (Number of nodes in the right subtree)
5.  **Recursive Calls:**
    *   **Left Subtree:** Recursively call `build` for the left subtree:
        *   `inorder` range: `[inLB, rootInd - 1]`
        *   `preorder` range: `[preLB + 1, preLB + leftSize]`
    *   **Right Subtree:** Recursively call `build` for the right subtree:
        *   `inorder` range: `[rootInd + 1, inUB]`
        *   `preorder` range: `[preLB + leftSize + 1, preUB]`
6.  **Return Root:** Return the constructed `root` node.

**`buildTree(int in[], int pre[], int n)` function:**

*   This is the main entry point, which simply calls the `build` helper function with initial bounds for the entire tree.

```cpp
#include <vector>
#include <algorithm> // Not strictly needed for the logic but often useful

// Definition for a binary tree node (assuming it's provided by the platform or defined elsewhere)
struct Node
{
  int data;
  Node* left;
  Node* right;
  Node(int x) : data(x), left(nullptr), right(nullptr) {}
};

class Solution{
public:
    // Recursive helper function to build the tree
    // in: inorder traversal array
    // pre: preorder traversal array
    // inLB, inUB: lower and upper bounds for the current inorder subarray
    // preLB, preUB: lower and upper bounds for the current preorder subarray
    Node* build(int *in,int *pre,int inLB,int inUB,int preLB,int preUB)
    {
        // Base case: If the bounds are invalid, return NULL
        if(inLB > inUB || preLB > preUB){return NULL;}
        
        // The first element in preorder traversal is always the root of the current subtree
        int rootVal = pre[preLB];
        Node* root = new Node(rootVal);
        
        // Find the root's index in the inorder traversal
        int rootInd = -1;
        for(int i = inLB; i <= inUB; i++){
            if(in[i] == rootVal){
                rootInd = i; 
                break;
            }
        }
        
        // Calculate the sizes of the left and right subtrees
        int leftSize = (rootInd - inLB);
        // int rightSize = (inUB - rootInd); // Not explicitly used for bounds calculation after correction
        
        // Recursively build the left subtree
        // Inorder for left: [inLB, rootInd-1]
        // Preorder for left: [preLB+1, preLB + leftSize] (root is pre[preLB], so left subtree starts at preLB+1
        // and spans 'leftSize' elements)
        root->left = build(in,pre,inLB,rootInd-1,preLB+1,preLB+leftSize);
        
        // Recursively build the right subtree
        // Inorder for right: [rootInd+1, inUB]
        // Preorder for right: [preLB + leftSize + 1, preUB] (after left subtree, the right subtree elements follow)
        root->right = build(in,pre,rootInd+1,inUB,preLB+leftSize+1,preUB);
        
        return root;
    }

    // Main function to initiate the tree construction
    Node* buildTree(int in[],int pre[], int n)
    {
        // Call the recursive helper function with the full array bounds
        return build(in,pre,0,n-1,0,n-1);
    }
};
```

## Driver Code (C++)

```cpp
#include<bits/stdc++.h>
using namespace std;

// Definition for a binary tree node
struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
	
	Node(int x){
	    data = x;
	    left = NULL;
	    right = NULL;
	}
};

// Function to print postorder traversal (for verification)
void printPostOrder(Node *root)
{
	if(root==NULL)
		return;
	printPostOrder(root->left);
	printPostOrder(root->right);
	cout<<root->data<<" ";
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		
		int inorder[n], preorder[n];
		for(int i=0; i<n; i++)
			cin>> inorder[i];
		for(int i=0; i<n; i++)
			cin>> preorder[i];
		Solution obj;
		Node *root = obj.buildTree(inorder, preorder, n);
		printPostOrder(root);
		cout<< endl;
	}
	return 0;
}
```