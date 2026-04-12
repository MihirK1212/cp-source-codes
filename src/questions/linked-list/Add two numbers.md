# Add Two Numbers (Linked List)

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

Input: `l1 = [2,4,3]`, `l2 = [5,6,4]`
Output: `[7,0,8]`
Explanation: `342 + 465 = 807`

## C++ Solution

This C++ solution adds two numbers represented by linked lists. The digits are stored in reverse order, which simplifies the addition process as we can iterate from the heads of the lists, just like elementary school addition. A new linked list is constructed to store the sum.

**Algorithm:**

1.  **Initialize:**
    *   Create a dummy head node for the result list (e.g., `ListNode* dummyHead = new ListNode(0);`). This simplifies handling the head of the result list.
    *   Initialize `curr` pointer to `dummyHead` to build the result list.
    *   Initialize `carry = 0`.
2.  **Iterate and Add:** Loop while either `l1` or `l2` is not `NULL`, or `carry` is not `0`:
    *   Get `x = l1 ? l1->val : 0;` (value from `l1`, or `0` if `l1` is exhausted).
    *   Get `y = l2 ? l2->val : 0;` (value from `l2`, or `0` if `l2` is exhausted).
    *   Calculate `sum = x + y + carry;`.
    *   Update `carry = sum / 10;`.
    *   Create a new node with `sum % 10` and append it to `curr->next`.
    *   Move `curr = curr->next;`.
    *   Move `l1 = l1 ? l1->next : NULL;`.
    *   Move `l2 = l2 ? l2->next : NULL;`.
3.  **Return:** Return `dummyHead->next` (skipping the dummy node).

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        ListNode* dummyHead = new ListNode(0); // Dummy node to simplify head creation
        ListNode* curr = dummyHead;
        int carry = 0;

        // Iterate until both lists are exhausted and there's no carry left
        while (l1 != NULL || l2 != NULL || carry != 0) {
            int x = (l1 != NULL) ? l1->val : 0;
            int y = (l2 != NULL) ? l2->val : 0;

            int sum = x + y + carry;
            carry = sum / 10; // Calculate new carry
            
            curr->next = new ListNode(sum % 10); // Create new node with current digit
            curr = curr->next; // Move to the next node in the result list

            if (l1 != NULL) {
                l1 = l1->next;
            }
            if (l2 != NULL) {
                l2 = l2->next;
            }
        }

        return dummyHead->next; // Return the actual head of the result list
    }
};
```