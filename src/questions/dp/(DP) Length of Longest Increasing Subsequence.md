# Longest Increasing Subsequence (LIS) - DP (O(n^2))

## Problem Description

Given an unsorted array of integers, find the length of the longest increasing subsequence (LIS). An increasing subsequence is a sequence of numbers selected from the array that are strictly increasing. This solution uses dynamic programming with O(n^2) time complexity.

## C++ Solution

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
   int n,i,j;
   cout<<"Enter the length of array\n";
   cin>>n;
   int a[n],lis[n];
   cout<<"Enter the array\n";
   for(i=0;i<n;i++)
   {
       cin>>a[i];
   }
   
   //lis[i]=length of increasing subsequence ENDING at ith index
   
   int maxlis=-10;
   
   for(i=0;i<n;i++)
   {
       lis[i]=1;
       for(j=i-1;j>=0;j--)
       {
         if(a[j]<=a[i]) // Should be strictly less than for increasing subsequence
         {
            lis[i]=max(lis[i],(1+lis[j]));
         }
       }
       maxlis=max(maxlis,lis[i]);
    }
    
    cout<<maxlis<<"\n";
    return 0;
}
```