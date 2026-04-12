# Sort According to Frequency (Heaps)

## Problem Description

This problem is from LeetCode: [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/)

Given an array of integers `nums`, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, they should be sorted in decreasing order. This can be efficiently solved using a min-priority queue with a custom comparator.

## C++ Solution

```cpp
typedef pair<int,int> pii;

class Compare{
    public:
    bool operator()(pii &x,pii &y)
    {
        // Custom comparator for the min-priority queue.
        // If frequencies are the same, sort by value in decreasing order (larger value first).
        // Otherwise, sort by frequency in increasing order (smaller frequency first).
        if(x.first==y.first){return x.second<y.second;} 
        else
        {
           return x.first>y.first; // For min-heap, x.first > y.first means x has lower priority (comes later).
                                  // So, higher frequency goes to the bottom.
        }   
    }
};
    
class Solution {
public:
    
    vector<int> frequencySort(vector<int>& nums) {
        map<int,int> freq; // Store frequency of each number
        for(int i=0;i<(nums.size());i++)
        {
            freq[nums[i]]++;
        }
        
        vector<pair<int,int>> arr; // Convert map to vector of pairs {frequency, number}
        for(auto x:freq)
        {
            arr.push_back({x.second,x.first});
        }
        
        vector<int> ans;
        
        // Min-priority queue with custom comparator
        priority_queue <pii,vector<pii>,Compare> min_h;
        
        for(int i=0;i<(arr.size());i++)
        {
            min_h.push(arr[i]);
        }
        
        while((min_h.size())>0)
        {
            // Extract elements from min-heap and add to answer based on frequency
            for(int i=0;i<((min_h.top()).first);i++){ans.push_back((min_h.top()).second);}
            min_h.pop();
        }
        
        return ans;
    }
};
```