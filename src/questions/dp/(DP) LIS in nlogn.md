# Longest Increasing Subsequence (LIS) in O(n log n) - DP

## Problem Description

Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS). This problem can be solved with dynamic programming in O(n log n) time complexity.

## C++ Solution

```cpp
int findCeil(vector<int>&arr,int x)
{
    int lb=0,ub=arr.size()-1,mid;
    int ans = -1; // Initialize with a default value
    
    while(lb<=ub)
    {
        mid = lb + (ub-lb)/2;
        
        if(arr[mid]>=x){ans=mid; ub=mid-1;}
        else{lb=mid+1;}
    }
    
    return ans;
}
//Function to find length of longest increasing subsequence.
int longestSubsequence(int n, int a[])
{
   vector<int> tail;
   
   for(int i=0;i<n;i++)
   {
       if(tail.size()==0 || a[i]>tail.back())
       {
           tail.push_back(a[i]);
       }
       else
       {
           // Replace the smallest element in tail that is >= a[i]
           tail[findCeil(tail,a[i])]=a[i];
       }
   }
   
   return tail.size();
}
```