# Swap Adjacent Nodes of Linked List

## Problem Description

Given a singly linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

**Example:**

Input: `head = [1,2,3,4]`
Output: `[2,1,4,3]`

## C++ Solution

This C++ solution swaps every two adjacent nodes in a singly linked list. It iterates through the list, taking two nodes at a time and reversing their order. A dummy node is often used to simplify the handling of the new head of the list.

**Algorithm:**

1.  **Handle Edge Cases:** If the list is empty or has only one node, no swapping is needed. Return the head as is.
2.  **Initialize Pointers:**
    *   `dummyHead`: A dummy node whose `next` points to the original head of the list. This simplifies updating the head of the potentially swapped list.
    *   `prev`: Points to the node *before* the current pair being swapped (initially `dummyHead`).
    *   `curr`: Points to the first node of the current pair (initially `head`).
3.  **Iterate and Swap:** Loop while `curr` and `curr->next` are not `NULL` (meaning there is at least a pair to swap):
    *   `firstNode = curr`
    *   `secondNode = curr->next`
    *   `thirdNode = curr->next->next` (or `secondNode->next`)
    *   **Perform Swap:**
        *   `prev->next = secondNode;` (Link previous segment to the `secondNode`)
        *   `secondNode->next = firstNode;` (Link `secondNode` to `firstNode`)
        *   `firstNode->next = thirdNode;` (Link `firstNode` to the rest of the list)
    *   **Advance Pointers:**
        *   `prev = firstNode;` (The `firstNode` is now the last node of the swapped pair, so it becomes the `prev` for the next pair).
        *   `curr = thirdNode;` (Move `curr` to the beginning of the next pair).
4.  **Return:** Return `dummyHead->next`.

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Basic ListNode structure (if not provided by the platform)
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) 
    {
        // Handle edge cases: empty list or single node list
        if (head == NULL || head->next == NULL) {
            return head;
        }

        // Create a dummy node to simplify handling the new head
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        
        ListNode* prev = dummyHead;
        ListNode* curr = head;

        // Iterate while there are at least two nodes to swap
        while (curr != NULL && curr->next != NULL)
        {
            ListNode* firstNode = curr;
            ListNode* secondNode = curr->next;
            ListNode* thirdNode = curr->next->next; // Store the node after the pair

            // Perform the swap
            prev->next = secondNode;   // Link previous segment to the second node
            secondNode->next = firstNode; // Link second node to the first node
            firstNode->next = thirdNode; // Link first node to the rest of the list

            // Advance pointers for the next iteration
            prev = firstNode; // The firstNode is now the last of the swapped pair
            curr = thirdNode; // Move curr to the start of the next pair
        }

        return dummyHead->next; // Return the new head of the list
    }
};
```