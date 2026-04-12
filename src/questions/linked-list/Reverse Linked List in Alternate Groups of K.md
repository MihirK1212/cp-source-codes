# Reverse Linked List in Alternate Groups of K

## Problem Description

Given a singly linked list and an integer `K`, reverse the nodes of the list `K` at a time. This problem specifically asks to reverse *alternate* groups of `K` nodes. The first group of `K` nodes should be reversed, the second group should remain as is, the third group should be reversed, and so on. If the number of nodes remaining at the end is less than `K`, they should remain as they are.

## C++ Solution

This recursive solution traverses the linked list, processing `K` nodes at a time. A boolean flag `reverse_current_group` dictates whether the current block of `K` nodes should be reversed.

The core idea is:
1.  **Identify the current group:** Find the Kth node from the current `head`.
2.  **Handle remaining nodes:** If there are fewer than `K` nodes remaining, they are not reversed and are simply returned.
3.  **Reverse or Skip:**
    *   If `reverse_current_group` is true, reverse the current `K` nodes. The original `head` becomes the tail, and its `next` pointer is set to the result of the recursive call for the *next* block (which will *not* be reversed).
    *   If `reverse_current_group` is false, skip `K` nodes. The `head` of this block remains, and its `next` pointer is set to the result of the recursive call for the *next* block (which *will* be reversed).
4.  **Toggle flag:** The `reverse_current_group` flag is toggled for the next recursive call.

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
ListNode* helper(ListNode* head, int k, bool reverse_current_group) {
    // Base case: if no nodes left, return NULL
    if (!head) {
        return NULL;
    }

    ListNode* current = head;
    ListNode* prev = NULL;
    ListNode* next_node = NULL;
    int count = 0;

    // Find the Kth node (or end of list if less than K nodes)
    // This loop effectively finds the 'kth_node_of_group'
    ListNode* kth_node_of_group_start = head; // Keep track of the start of this block
    ListNode* kth_node_of_group_end = head; // Find the end of this block
    for(int i = 0; i < k && kth_node_of_group_end != NULL; ++i) {
        kth_node_of_group_end = kth_node_of_group_end->next;
        count++;
    }

    // If there are less than K nodes in the current segment
    // (i.e., we reached the end of the list before finding K nodes),
    // then these remaining nodes should not be reversed (as per problem statement).
    // Just return the head of this segment as is.
    if (count < k) {
        return head;
    }

    // Now, `head` points to the head of the current block,
    // and `kth_node_of_group_end` points to the node *after* the current block.

    if (reverse_current_group) {
        // Reverse the current block of K nodes
        current = head;
        prev = NULL;
        int reverse_count = 0;
        while (reverse_count < k && current) {
            next_node = current->next;
            current->next = prev;
            prev = current;
            current = next_node;
            reverse_count++;
        }
        // `head` (original head) is now the tail of the reversed group.
        // It should point to the result of the recursive call for the next block (not reversed).
        if (head) {
            head->next = helper(current, k, false); // `current` is the start of the next block
        }
        return prev; // `prev` is the new head of the reversed group
    } else {
        // Do not reverse the current block of K nodes
        // `head` already points to the head of this block.
        // We need to find the `k`-th node of this group to link it to the next recursive call.
        current = head;
        int skip_count = 0;
        while (skip_count < k - 1 && current) { // Advance `k-1` times to get to the Kth node
            current = current->next;
            skip_count++;
        }
        
        // `current` is now the Kth node of this non-reversed group (or the last node if less than K).
        // Its `next` pointer should point to the result of the recursive call for the next block (reversed).
        if (current) {
            current->next = helper(current->next, k, true); // `current->next` is the start of the next block
        }
        return head; // `head` remains the head of this non-reversed group
    }
}

ListNode* Solution::solve(ListNode* A, int B) 
{
    // Start with reversing the first group (reverse_current_group = true)
    return helper(A, B, true);
}
```