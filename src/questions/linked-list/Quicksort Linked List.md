# Quicksort Linked List

## Problem Description

Given the `head` of a singly linked list, sort the list using Quicksort.

## C++ Solution

This C++ solution implements the Quicksort algorithm for a singly linked list. Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

**`ListNode` Structure:**

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
```

**`swapVal(ListNode* n1, ListNode* n2)` function:**

*   A helper function to swap the `val` of two `ListNode` objects.

**`partition(ListNode* lb, ListNode* ub)` function:**

*   This function partitions the linked list segment from `lb` (inclusive) to `ub` (exclusive) around a pivot. The `lb->val` is chosen as the pivot.
*   It rearranges the elements such that all nodes with values less than or equal to the pivot come before the pivot, and all nodes with values greater than the pivot come after it.
*   Returns the `ListNode` which is the new position of the pivot after partitioning.

**`quickSort(ListNode* lb, ListNode* ub)` function:**

*   This is the recursive function that applies quicksort to the linked list segment from `lb` (inclusive) to `ub` (exclusive).
*   **Base Case:** If `lb` is `NULL` or `lb == ub`, the sublist is empty or has one element, so it is already sorted.
*   **Recursive Step:**
    1.  Calls `partition` to rearrange the sublist and get the pivot's final position `m`.
    2.  Recursively calls `quickSort` on the sublist to the left of `m` (`lb` to `m`).
    3.  Recursively calls `quickSort` on the sublist to the right of `m` (`m->next` to `ub`).

**`Solution::sortList(ListNode* A)` function:**

*   This is the main entry point. It calls `quickSort` with the head of the list `A` and `NULL` as the upper bound (indicating the end of the list).
*   Returns the head of the sorted list.

```cpp
void swapVal(ListNode* n1,ListNode* n2)
{
    int temp = n1->val; n1->val = n2->val; n2->val = temp;
}

ListNode* partition(ListNode* lb,ListNode* ub)
{
    int pivot = lb->val;
    
    ListNode* j = lb;
    ListNode* i = lb->next;
    
    while(i!=ub)
    {
        if((i->val)<=pivot)
        {
            swapVal(j->next,i);
            j = j->next;
        }
        
        i = i->next;
    }
    
    swapVal(lb,j);
    
    return j;
} 

void quickSort(ListNode* lb,ListNode* ub)
{
    if(lb==ub || lb==NULL){return;}
    
    ListNode* m = partition(lb,ub);
    quickSort(lb,m);
    quickSort(m->next,ub);    
}
ListNode* Solution::sortList(ListNode* A) 
{
    quickSort(A,NULL);
    return A;
}
```