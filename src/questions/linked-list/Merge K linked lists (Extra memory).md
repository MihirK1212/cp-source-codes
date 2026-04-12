# Merge K Linked Lists (with Extra Memory)

## Problem Description

Given `k` sorted linked lists, merge them into one sorted linked list. This problem can be solved using a min-priority queue (min-heap) to keep track of the smallest element from all lists. This approach uses extra memory for the new merged list.

## C++ Solution

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Compare{
    public:
    bool operator()(pair<int,ListNode*> &x,pair<int,ListNode*> &y)
    {
        return x.first>y.first;  
    }
};
  
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) 
    {
        priority_queue <pair<int,ListNode*>,vector<pair<int,ListNode*>>,Compare> min_h;  
        
        
        ListNode* head = NULL;
        ListNode* curr = NULL;
        
        for(auto h : lists)
        {
            if(!h){continue;}
            min_h.push({h->val,h});
        }
        
        while(!min_h.empty())
        {
            auto p = min_h.top(); min_h.pop();
            
            int val = p.first;
            ListNode* address = p.second;
            
            
            if(!head)
            {
                head = new ListNode(val);
                curr = head;
            }
            else
            {
                curr->next = new ListNode(val);
                curr = curr->next;
                curr->next = NULL;
            }
            
            
            if(address->next)
            {
                min_h.push({address->next->val,address->next});
            }
        }
        
        return head;
        
    }
};
```