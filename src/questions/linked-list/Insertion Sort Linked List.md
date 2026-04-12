# Insertion Sort Linked List

## Problem Description

Given the `head` of a singly linked list, sort the list using insertion sort, and return the head of the sorted linked list.

## C++ Solution

This C++ solution implements insertion sort for a singly linked list. Insertion sort works by iteratively building a sorted list (or sublist) by taking elements from the unsorted portion and inserting them into their correct position in the sorted portion.

**`ListNode` Structure:**

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
```

**`insert(ListNode* head, ListNode* ptr)` function:**

*   This helper function inserts a single node `ptr` into an already sorted linked list starting at `head`.
*   It traverses the sorted list to find the correct position where `ptr->val` should be inserted, maintaining the sorted order.
*   **Cases:**
    *   If `ptr->val` is smaller than or equal to the current `head->val`, `ptr` becomes the new head.
    *   Otherwise, it finds the node `prev` such that `prev->val <= ptr->val` and `curr->val > ptr->val` (where `curr` is `prev->next`). `ptr` is then inserted between `prev` and `curr`.
*   Returns the (potentially new) head of the sorted list.

**`Solution::insertionSortList(ListNode* A)` function:**

*   This is the main function that performs insertion sort on the input linked list `A`.
*   It initializes `sortedHead` with the first node of the input list `A`. This `sortedHead` will gradually grow to become the fully sorted list.
*   The `next` pointer of the initial `sortedHead` is set to `NULL` to effectively make it a single-node sorted list to start with.
*   It then iterates through the remaining nodes of the original list (`curr` pointer):
    1.  Stores `curr->next` in `nextAdd` to keep track of the next node to process.
    2.  Sets `curr->next = NULL` to detach `curr` from the unsorted part of the list.
    3.  Calls the `insert` function to insert `curr` into the `sortedHead` list, updating `sortedHead` if `curr` becomes the new head.
    4.  Moves `curr` to `nextAdd` to process the next node from the original list.
*   Finally, returns `sortedHead`, which is the head of the completely sorted linked list.

```cpp
#include <cstddef> // Required for NULL

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Helper function to insert a new node 'ptr' into an already sorted linked list.
// Returns the new head of the sorted list.
ListNode* insert(ListNode* head, ListNode* ptr)
{
    ListNode* curr = head; // Current node in the sorted list
    ListNode* prev = NULL; // Previous node in the sorted list

    // Traverse the sorted list to find the correct insertion point
    // Stop when curr is NULL or curr->val is greater than ptr->val
    while(curr != NULL && (curr->val) <= (ptr->val))
    {
        prev = curr;
        curr = curr->next;
    }

    // Case 1: ptr needs to be inserted at the beginning (smallest value)
    if(prev == NULL){
        ptr->next = head; // ptr's next points to the original head
        head = ptr;       // ptr becomes the new head
        return head;
    }

    // Case 2: ptr needs to be inserted in the middle or at the end
    prev->next = ptr; // prev's next points to ptr
    ptr->next = curr; // ptr's next points to curr (or NULL if inserted at end)
    return head;
}

class Solution {
public:
    // Main function to sort a singly linked list using insertion sort.
    ListNode* insertionSortList(ListNode* A) 
    {
        // Handle empty or single-node list cases
        if (A == NULL || A->next == NULL) {
            return A;
        }

        // 'sortedHead' will be the head of the sorted list, initially the first node of A.
        ListNode* sortedHead = A;
        
        // 'curr' will iterate through the unsorted part of the list, starting from the second node.
        ListNode* curr = A->next;
        
        // Detach the first node from the rest of the list to form the initial sorted list.
        sortedHead->next = NULL;

        // Iterate through the unsorted part of the list
        while(curr != NULL)
        {
            // Store the next node to process before detaching 'curr'
            ListNode* nextAdd = curr->next;
            
            // Detach 'curr' from the unsorted list
            curr->next = NULL;
            
            // Insert 'curr' into the sorted list, updating sortedHead if necessary
            sortedHead = insert(sortedHead, curr);
            
            // Move to the next node in the original unsorted list
            curr = nextAdd;
        }

        return sortedHead; // Return the head of the fully sorted linked list
    }
};
```