# Spiral Traversal of Tree

## Problem Description

Given a binary tree, the task is to print its nodes in **spiral order**. This means that nodes at level 1 should be printed from right to left, nodes at level 2 from left to right, level 3 from right to left, and so on, alternating the traversal direction for each level.

## C++ Solution

This solution uses a `std::deque` (double-ended queue) to manage nodes at each level and a boolean flag (`rev`) to toggle the traversal direction. This approach effectively simulates a level-order traversal while allowing for alternating read/write patterns.

**`Node` Structure (Binary Tree Node):**

```cpp
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
```

**`findSpiral(Node *root)` Function:**

*   **Initialization:**
    *   `ans`: A `std::vector<int>` to store the spiral traversal result.
    *   If `root` is `NULL`, return an empty `ans`.
    *   `q`: A `std::deque<Node*>` to hold nodes for the current and next levels.
    *   `rev`: A `bool` flag, initialized to `false`. When `false`, traverse left-to-right; when `true`, traverse right-to-left.
    *   Push the `root` to the front of the `deque`.

*   **Level-by-Level Traversal (using `deque`):**
    1.  While `q` is not empty:
        *   Get the `s = q.size()` (number of nodes at the current level).
        *   Iterate `s` times (processing all nodes at the current level):
            *   **If `!rev` (Left-to-Right Traversal):**
                *   Dequeue `u` from the `front` of `q` (`q.pop_front()`).
                *   Add `u->data` to `ans`.
                *   Enqueue `u->left` then `u->right` to the `back` of `q`. (For the next level, these children will be processed from the front for a left-to-right traversal).
            *   **If `rev` (Right-to-Left Traversal):**
                *   Dequeue `u` from the `back` of `q` (`q.pop_back()`).
                *   Add `u->data` to `ans`.
                *   Enqueue `u->right` then `u->left` to the `front` of `q`. (For the next level, these children will be processed from the back for a right-to-left traversal, ensuring the correct reversed order).
        *   After processing all nodes at the current level, toggle `rev = !rev` for the next level.

*   Return `ans`.

```cpp
#include <vector>  // For std::vector
#include <deque>   // For std::deque
#include <iostream> // For standard input/output (driver code)
#include <string>   // For std::string (driver code)
#include <sstream>  // For std::istringstream (driver code)

// Definition for a binary tree node (provided by platforms like GeeksforGeeks).
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = nullptr; // Use nullptr instead of NULL in modern C++
        right = nullptr;
    }
};

// Function to return a list containing the level order traversal in spiral form.
std::vector<int> findSpiral(Node *root)
{
    std::vector<int> ans; // Stores the final spiral traversal result
    
    if(!root){ // If the tree is empty, return an empty vector
        return ans;
    }
    
    std::deque<Node*> q; // Double-ended queue for level-order traversal
    bool rev = false;    // Flag to control traversal direction: false for L->R, true for R->L
    
    q.push_front(root); // Start by pushing the root to the front
    
    while(!q.empty()) // While there are nodes to process
    {
        int s = q.size(); // Number of nodes at the current level
        
        while(s--) // Process all nodes at the current level
        {
            if(!rev) // Current level: Left to Right traversal
            {
               Node* u = q.front(); 
               q.pop_front(); // Get node from front
               ans.push_back(u->data);
               
               // Add children for the NEXT level's processing.
               // For next level's L->R (if rev becomes true), these will be popped from back.
               // For next level's R->L (if rev remains false), these will be popped from front.
               // Here, children are added to the back to maintain order for next level's processing.
               if(u->left){ q.push_back(u->left); }
               if(u->right){ q.push_back(u->right); }
            }
            else // Current level: Right to Left traversal
            {
               Node* u = q.back(); 
               q.pop_back(); // Get node from back
               ans.push_back(u->data);
               
               // Add children for the NEXT level's processing.
               // To achieve a right-to-left traversal for the *current* level (when rev is true),
               // we retrieve from back and add children to the *front* in reversed order (right then left)
               // so they will be popped correctly for the *next* level's left-to-right pass.
               if(u->right){ q.push_front(u->right); }
               if(u->left){ q.push_front(u->left); }
            }
        }
        
        rev = !rev; // Toggle direction for the next level
    }
    
    return ans; // Return the collected spiral traversal
}

// Driver Code (often provided by competitive programming platforms)
// This part handles input parsing and tree construction.

// Utility function to create a new Tree Node
Node* newNode(int val)
{
    Node* temp = new Node(val);
    // Node constructor already initializes left/right to nullptr
    return temp;
}

// Function to Build Tree from level order string input
Node* buildTree(std::string str)
{
    // Corner Case: Empty string or starts with 'N' (representing null root)
    if(str.length() == 0 || str[0] == 'N')
        return nullptr;

    // Creating vector of strings from input string after splitting by space
    std::vector<std::string> ip;
    std::istringstream iss(str);
    for(std::string str_node; iss >> str_node; )
        ip.push_back(str_node);

    // Create the root of the tree
    Node* root = newNode(std::stoi(ip[0]));

    // Use a queue for level-order tree construction
    std::queue<Node*> queue;
    queue.push(root);

    // Starting from the second element (ip[1]), as ip[0] is root
    int i = 1;
    while(!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue (parent node)
        Node* currNode = queue.front();
        queue.pop();

        // Get the current node's left child value from the string
        std::string currVal = ip[i];

        // If the left child is not null ('N')
        if(currVal != "N") {
            // Create the left child for the current node
            currNode->left = newNode(std::stoi(currVal));
            // Push it to the queue for its children to be processed later
            queue.push(currNode->left);
        }

        // Move to the next element for the right child
        i++;
        if(i >= ip.size()) // Check if we've run out of input
            break;
        currVal = ip[i];

        // If the right child is not null ('N')
        if(currVal != "N") {
            // Create the right child for the current node
            currNode->right = newNode(std::stoi(currVal));
            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}

int main() {
    // Fast I/O setup
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t; // Number of test cases
    std::string tc_line; // To read the line for number of test cases
    std::getline(std::cin, tc_line);
    t = std::stoi(tc_line);

    while(t--) {
        std::string s; // Input string for tree structure
        std::getline(std::cin, s);
        Node* root = buildTree(s);

        std::vector<int> vec = findSpiral(root);
        for(int x : vec)
            std::cout << x << " ";
        std::cout << std::endl;
    }
    return 0;
}
```