# Reverse Nodes at Even Positions (Linked List)

## Problem Description

Given a singly linked list, reverse the nodes at even positions and then merge the modified even-positioned sublist back into the original list such that all nodes are in their correct relative positions (i.e., the original odd-positioned nodes remain at odd positions and original even-positioned nodes remain at even positions, but the values of even-positioned nodes are reversed).

The problem typically implies a 1-indexed list, where the head is at position 1 (odd).

## C++ Solution

This solution first separates the original linked list into two sub-lists: one containing nodes at odd positions and another containing nodes at even positions. It then reverses the sub-list of even-positioned nodes and finally merges the two sub-lists back together in the correct alternating order.

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// Function to reverse a linked list
ListNode* revList(ListNode* head)
{
    ListNode *curr = head, *prev = NULL;
    while(curr)
    {
        ListNode* next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    return prev;
}

// Function to merge two linked lists in an alternating fashion
ListNode* merge(ListNode* oddHead, ListNode* evenHead)
{
    ListNode *p1 = oddHead, *p2 = evenHead;
    ListNode *dummyHead = new ListNode(0); // Dummy node for easier merging
    ListNode *current = dummyHead;

    while(p1 && p2)
    {
        current->next = p1;
        current = p1;
        p1 = p1->next;

        current->next = p2;
        current = p2;
        p2 = p2->next;
    }

    if(p1) { // If odd list still has elements
        current->next = p1;
    }
    
    ListNode* result = dummyHead->next;
    delete dummyHead; // Free dummy node
    return result;
}

ListNode* Solution::solve(ListNode* A) 
{
    if(A == NULL || A->next == NULL) {
        return A;
    }

    ListNode* oddHead = NULL;
    ListNode* evenHead = NULL;
    ListNode* oddTail = NULL;
    ListNode* evenTail = NULL;

    ListNode* curr = A;
    int index = 1; // 1-indexed position

    while(curr) {
        if(index % 2 != 0) { // Odd position
            if(oddHead == NULL) {
                oddHead = curr;
                oddTail = curr;
            } else {
                oddTail->next = curr;
                oddTail = curr;
            }
        } else { // Even position
            if(evenHead == NULL) {
                evenHead = curr;
                evenTail = curr;
            } else {
                evenTail->next = curr;
                evenTail = curr;
            }
        }
        ListNode* next_node = curr->next;
        curr->next = NULL; // Detach current node
        curr = next_node;

        index++;
    }

    // Reverse the even-positioned list
    evenHead = revList(evenHead);

    // Merge the odd and reversed even lists
    return merge(oddHead, evenHead);
}
```