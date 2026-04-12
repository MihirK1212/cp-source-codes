# Merge Two Sorted Linked Lists

## Problem Description

Given the heads of two singly linked lists, `A` and `B`, both sorted in non-decreasing order, merge them into a single sorted linked list. The new list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## C++ Solution

This C++ solution merges two sorted singly linked lists (`A` and `B`) into a single sorted list. The algorithm iteratively compares the values of the current nodes in both lists and appends the smaller node to the merged list.

**`ListNode` Structure:**

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
```

**`findHead(ListNode* A, ListNode* B)` function:**

*   This helper function determines the head of the merged list. It compares the values of the first nodes of `A` and `B` (handling `NULL` lists by treating their value as `INT_MAX`). The node with the smaller value becomes the head.

**`Solution::mergeTwoLists(ListNode* A, ListNode* B)` function:**

*   **Parameters:**
    *   `A`: Head of the first sorted linked list.
    *   `B`: Head of the second sorted linked list.
*   **Logic:**
    1.  **Handle Empty Lists:** If either `A` or `B` is `NULL`, return the other list (or `NULL` if both are `NULL`). (Implicitly handled by `findHead` and main loop condition).
    2.  **Determine Initial Head:** `head = findHead(A, B)` sets the starting point of the merged list.
    3.  **Pointers:**
        *   `currA`: Current node in list `A`.
        *   `currB`: Current node in list `B`.
        *   `prevA`: Tracks the last node added to the merged list (which originated from `A`), allowing insertion of nodes from `B`.
    4.  **Main Loop (`while(currA && currB)`):** Iterates as long as both lists have nodes remaining.
        *   If `currA->val <= currB->val`:
            *   The node from `A` is smaller or equal. It's already in its correct relative position if `A` is the base list. Advance `prevA` to `currA` and `currA` to `currA->next`.
        *   Else (`currB->val < currA->val`):
            *   The node from `B` (`currB`) needs to be inserted before `currA`.
            *   Store `currB->next` in `nextB`.
            *   If `prevA` exists (not the very first node of the merged list), link `prevA->next = currB`.
            *   Link `currB->next = currA`.
            *   Update `prevA = currB` (as `currB` is now part of the merged list, and it was the last node added).
            *   Advance `currB = nextB`.
    5.  **Append Remaining List:** After the loop, one of the lists might have remaining nodes. These nodes are already sorted and larger than all nodes currently in the merged list. Append the remaining part of `currB` (if any) to the end of the merged list (via `prevA->next = currB`). If `currA` has remaining nodes, they are already linked if `A` was the starting head and no nodes from `B` were ever inserted before `currA`'s head.
    6.  **Return `head`:** The head of the fully merged and sorted linked list.

```cpp
#include <cstddef>   // Required for NULL
#include <limits>    // Required for std::numeric_limits<int>::max
#include <algorithm> // Not explicitly used but generally useful

// Definition for singly-linked list node.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Helper function to find the initial head of the merged list.
// Handles cases where one or both lists might be NULL.
ListNode* findHead(ListNode* A, ListNode* B) 
{
    // Use INT_MAX for NULL list values to ensure comparison logic works correctly.
    int val_A = A ? (A->val) : std::numeric_limits<int>::max();
    int val_B = B ? (B->val) : std::numeric_limits<int>::max();
    
    if(val_A <= val_B){
        return A;
    }
    return B;
}

class Solution {
public:
    // Function to merge two sorted singly linked lists.
    ListNode* mergeTwoLists(ListNode* A, ListNode* B) 
    {
        // Handle cases where one or both lists are empty.
        if (!A) return B;
        if (!B) return A;

        // Determine the head of the new merged list.
        ListNode* head = NULL;
        // A dummy node approach is often cleaner, but the current code avoids it.

        ListNode *currA = A; // Pointer to traverse list A
        ListNode *currB = B; // Pointer to traverse list B
        ListNode *tail = NULL; // Pointer to the last node of the merged list

        // Initialize head and first tail element
        if (currA->val <= currB->val) {
            head = currA;
            currA = currA->next;
        } else {
            head = currB;
            currB = currB->next;
        }
        tail = head;

        // Traverse both lists, adding the smaller element to the merged list
        while(currA && currB)
        {
            if(currA->val <= currB->val)
            {
                tail->next = currA;
                currA = currA->next;
            }
            else
            {
                tail->next = currB;
                currB = currB->next;
            }
            tail = tail->next; // Advance the tail of the merged list
        }

        // If there are remaining nodes in list A or list B, append them.
        if(currA) {
            tail->next = currA;
        }
        else if(currB) {
            tail->next = currB;
        }

        return head;    
    }
};
```